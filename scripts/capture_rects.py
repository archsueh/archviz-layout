#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
capture_rects.py — Archviz 展板 HTML → 元素框一键抓取（Playwright）

把「人工从浏览器 devtools 导出 rects.json」这一步自动化：
  1. 用 Playwright headless 渲染 HTML 展板（file:// 或 http(s)://）；
  2. 遍历可见元素，导出每个元素的 bounding box（文档坐标）、计算色、底色、
     kind（text/box）、large（≥18pt 或 14pt bold）；
  3. 写 rects.json（直接喂给 audit_board.py 跑 GATES：碰撞 / 对齐 / WCAG 对比）；
  4. 同时截一张 full-page PNG（与 rects 1:1 对齐，给像素模式 + SVG 标注用）；
  5. 可选 --run-audit：链式调用同目录的 audit_board.py，一键出全量报告 + SVG。

坐标对齐约定（关键）：
  - deviceScaleFactor = 1；
  - 先把视口自动适配到内容尺寸（或按 --width/--height 固定），此时无滚动，
    元素的 getBoundingClientRect + scroll 偏移 == 文档坐标；
  - 截图用 full_page=True，deviceScaleFactor=1，得到与 rects 像素级对齐的 PNG。

rects.json 输出格式（与 audit_board.py 完全兼容）：
  [
    {"x":120,"y":80,"w":600,"h":40,"kind":"text","color":"#141413",
     "bg":"#F5F4ED","large":false},
    {"x":120,"y":140,"w":600,"h":300,"kind":"box","color":"#44403C",
     "bg":"#F5F4ED"}
  ]

依赖：playwright（仅本脚本需要；audit_board.py 仍零依赖）。
  pip install playwright && playwright install chromium

用法：
  # 仅抓框 + 截图
  python3 capture_rects.py --html board.html --out rects.json --screenshot board.png

  # 一键：抓框 + 截图 + 跑 audit 出全量报告（含 SVG 标注）
  python3 capture_rects.py --html board.html --out rects.json \
      --screenshot board.png --run-audit --audit-out report.json --overlay overlay.svg

  # 固定展板尺寸（海报/作品集，不自动适配高度）
  python3 capture_rects.py --html board.html --width 1080 --height 1440
"""

import argparse
import json
import os
import subprocess
import sys

# ----------------------------------------------------------------------------
# 浏览器内执行：导出元素框
# ----------------------------------------------------------------------------

_JS_EXTRACT = r"""
() => {
  const rgbToHex = (c) => {
    const m = String(c).match(/-?\d+(\.\d+)?/g);
    if (!m || m.length < 3) return '#000000';
    const clamp = (v) => Math.max(0, Math.min(255, Math.round(parseFloat(v))));
    return '#' + [clamp(m[0]), clamp(m[1]), clamp(m[2])]
      .map(v => v.toString(16).padStart(2, '0')).join('');
  };
  const getEffectiveBg = (el) => {
    let node = el;
    while (node) {
      const bg = getComputedStyle(node).backgroundColor;
      if (bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent') return bg;
      node = node.parentElement;
    }
    return 'rgb(255,255,255)';
  };
  const isVisible = (el, cs) => {
    if (cs.visibility === 'hidden' || cs.display === 'none') return false;
    if (parseFloat(cs.opacity) === 0) return false;
    const r = el.getBoundingClientRect();
    return r.width >= 1 && r.height >= 1;
  };
  const SEL = %s;
  const els = Array.from(document.querySelectorAll(SEL));
  const out = [];
  const sx = window.scrollX || 0, sy = window.scrollY || 0;
  for (const el of els) {
    const cs = getComputedStyle(el);
    if (!isVisible(el, cs)) continue;
    const r = el.getBoundingClientRect();
    // 直接文本节点（不含子元素文本）
    let direct = 0;
    for (const n of el.childNodes) {
      if (n.nodeType === 3) direct += (n.textContent || '').trim().length;
    }
    // 是否有成块子元素（装饰/容器）
    const hasBlockChild = Array.from(el.children).some(ch => {
      const ccs = getComputedStyle(ch);
      const cr = ch.getBoundingClientRect();
      return cr.width > 2 && cr.height > 2 && ccs.display !== 'inline';
    });
    const kind = (!hasBlockChild && direct > 0) ? 'text' : 'box';
    const fs = parseFloat(cs.fontSize) || 0;          // px
    const fw = parseInt(cs.fontWeight, 10) || 400;
    // 18pt≈24px；14pt≈18.66px
    const large = fs >= 24 || (fs >= 18.66 && fw >= 700);
    out.push({
      x: Math.round(r.left + sx),
      y: Math.round(r.top + sy),
      w: Math.round(r.width),
      h: Math.round(r.height),
      kind: kind,
      color: rgbToHex(cs.color),
      bg: rgbToHex(getEffectiveBg(el)),
      large: large,
    });
  }
  return out;
}
"""

# 默认选择器：structural + text 全量覆盖（靠 Python 端同 kind 去重收敛噪声）
DEFAULT_SELECTOR = (
    "h1,h2,h3,h4,h5,h6,p,li,figcaption,blockquote,label,button,a,"
    "span,img,svg,canvas,section,article,div,figure,table,tr,td,th,"
    "header,footer,nav,aside,main,ul,ol,dt,dd"
)


def _dedupe(rects, thresh=0.92):
    """收敛噪声：
    - text：全部保留（都是对比度目标；嵌套重复由 collision 的嵌套跳过处理）。
    - box：仅当被已保留的更大 box 覆盖 ≥thresh 且**底色相同**时，视为冗余 wrapper 删除；
          有独立底色的卡片 / 列 / 图版一律保留（它们是真实视觉块）。
    """
    def area(a):
        return a["w"] * a["h"]

    def covered(a, b):
        ix = max(a["x"], b["x"]); iy = max(a["y"], b["y"])
        ix2 = min(a["x"] + a["w"], b["x"] + b["w"])
        iy2 = min(a["y"] + a["h"], b["y"] + b["h"])
        if ix2 <= ix or iy2 <= iy:
            return False
        return area(a) > 0 and (ix2 - ix) * (iy2 - iy) / area(a) >= thresh

    kept = []
    for r in rects:
        if r["kind"] == "text":
            kept.append(r)
            continue
        skip = False
        for b in kept:
            if b["kind"] != "box":
                continue
            if r["bg"] == b["bg"] and covered(r, b):
                skip = True
                break
        if not skip:
            kept.append(r)
    return kept


def capture(html_path, out_json, screenshot=None, selector=DEFAULT_SELECTOR,
            width=None, height=None, board_selector=None):
    from playwright.sync_api import sync_playwright

    url = html_path if html_path.startswith(("http://", "https://", "file://")) \
        else "file://" + os.path.abspath(html_path)

    rects_raw = []
    shot_path = None
    shot_clip = None
    vw = vh = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        ctx = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1,
        )
        page = ctx.new_page()
        page.goto(url, wait_until="load")
        try:
            page.wait_for_timeout(300)
        except Exception:
            pass

        # 适配视口到内容尺寸（无滚动 → 文档坐标 == 视口坐标）
        if width and height:
            vw, vh = width, height
        else:
            dims = page.evaluate(
                "({w: Math.max(document.documentElement.scrollWidth, "
                "document.body.scrollWidth, window.innerWidth), "
                "h: Math.max(document.documentElement.scrollHeight, "
                "document.body.scrollHeight, window.innerHeight)})"
            )
            vw = max(dims["w"], width or 0) or dims["w"]
            vh = max(dims["h"], height or 0) or dims["h"]
        page.set_viewport_size({"width": vw, "height": vh})
        try:
            page.wait_for_timeout(150)
        except Exception:
            pass

        # 展板本体裁剪：截图只取 .board / [data-board]，rects 转成展板局部坐标，
        # 这样平衡 / 对比只在展板内衡量，不被画布留白带偏。
        board = None
        if board_selector:
            board = page.evaluate(
                "(sel)=>{const el=document.querySelector(sel); if(!el) return null;"
                "const r=el.getBoundingClientRect();"
                "return {x:r.left+window.scrollX, y:r.top+window.scrollY, "
                "w:r.width, h:r.height};}",
                board_selector)

        rects_raw = page.evaluate(_JS_EXTRACT % json.dumps(selector))
        if board:
            ox, oy = round(board["x"]), round(board["y"])
            for r in rects_raw:
                r["x"] -= ox
                r["y"] -= oy
            shot_clip = {"x": board["x"], "y": board["y"],
                         "width": board["w"], "height": board["h"]}

        if screenshot:
            shot_path = screenshot
            if shot_clip:
                page.screenshot(path=shot_path, clip=shot_clip)
            else:
                page.screenshot(path=shot_path, full_page=True)
        browser.close()

    rects = _dedupe(rects_raw)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(rects, f, ensure_ascii=False, indent=2)

    n_text = sum(1 for r in rects if r["kind"] == "text")
    n_box = len(rects) - n_text
    print("=== capture_rects ===")
    print("source: %s" % url)
    print("viewport: %dx%d  board-clip=%s" % (vw, vh, "yes" if board else "no (full page)"))
    print("elements: raw=%d → kept=%d (text=%d box=%d)"
          % (len(rects_raw), len(rects), n_text, n_box))
    print("rects -> %s" % out_json)
    if shot_path:
        print("screenshot -> %s" % shot_path)
    return rects, shot_path


def run_audit(image, rects, audit_out, overlay, bg="auto",
              script_dir=None):
    script_dir = script_dir or os.path.dirname(os.path.abspath(__file__))
    audit_py = os.path.join(script_dir, "audit_board.py")
    cmd = [sys.executable, audit_py, "--image", image, "--rects", rects,
           "--bg", bg]
    if audit_out:
        cmd += ["--out", audit_out]
    if overlay:
        cmd += ["--overlay", overlay]
    print("--- running audit_board.py ---")
    subprocess.run(cmd, check=True)
    return audit_py


def main():
    ap = argparse.ArgumentParser(
        description="Archviz 展板 HTML → 元素框一键抓取（Playwright）")
    ap.add_argument("--html", required=True, help="HTML 展板路径或 URL")
    ap.add_argument("--out", default="rects.json", help="输出 rects.json 路径")
    ap.add_argument("--screenshot", help="full-page 截图 PNG 路径（可选）")
    ap.add_argument("--selector", default=DEFAULT_SELECTOR,
                    help="元素选择器（默认覆盖 structural + text）")
    ap.add_argument("--width", type=int, help="固定视口宽（海报/作品集）")
    ap.add_argument("--height", type=int, help="固定视口高")
    ap.add_argument("--board", default=".board, [data-board]",
                    help="展板本体选择器；匹配则截图裁到展板、rects 转局部坐标"
                         "（默认 .board, [data-board]；无匹配则回退整页）")
    ap.add_argument("--run-audit", action="store_true",
                    help="链式跑 audit_board.py 出全量报告")
    ap.add_argument("--audit-out", help="audit 报告 JSON 路径")
    ap.add_argument("--overlay", help="audit 标注 SVG 路径")
    ap.add_argument("--bg", default="auto", help="audit 底色 auto 或 #rrggbb")
    args = ap.parse_args()

    # --run-audit 但没有显式截图 → 自动落一张（在 capture 内一并完成，避免二次起浏览器）
    screenshot = args.screenshot
    if args.run_audit and not screenshot:
        screenshot = os.path.splitext(args.out)[0] + "_screenshot.png"

    rects, shot = capture(
        args.html, args.out, screenshot, args.selector,
        args.width, args.height, args.board)

    if args.run_audit:
        run_audit(shot, args.out, args.audit_out, args.overlay, args.bg)


if __name__ == "__main__":
    main()
