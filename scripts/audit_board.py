#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_board.py — Archviz 展板成图审计脚本（零依赖，纯标准库）

把 archviz-layout v1.1.0「渲染评图循环」里的可测量检查落成可跑工具：
  - 像素模式（--image 必填）：从渲染截图算「视觉平衡（墨密度重心）」与「粗粒度局部对比」。
  - 矩形模式（--rects 可选）：从浏览器导出的元素框算 碰撞 / 对齐节律 / 间距节奏 / WCAG 对比。
  - 输出 JSON 报告 + 带标注的 SVG 叠加图（给独立 judge 看「哪里」）。

设计原则（见 SKILL.md §成图渲染评图循环）：
  - GATES = 正确性（碰撞、对比、溢出），可硬挡；
  - SIGNALS = 约定（平衡、对齐、间距节奏），是指针不是裁决，不可为追分过度纠正。

依赖：仅 Python 3 标准库（zlib / struct / math / json / argparse / sys）。

用法：
  python3 audit_board.py --image board.png
  python3 audit_board.py --image board.png --rects rects.json --out report.json --overlay overlay.svg
  python3 audit_board.py --image board.png --bg #F5F4ED --opt-x 0.50 --opt-y 0.46

rects.json 格式（从 Playwright / 浏览器 devtools 导出元素 bounding box + 颜色）：
  [
    {"x":120,"y":80,"w":600,"h":40,"kind":"text","color":"#141413","bg":"#F5F4ED","large":false},
    {"x":120,"y":140,"w":600,"h":300,"kind":"box","color":"#44403C","bg":"#F5F4ED"}
  ]
  kind ∈ {text, box}；color/bg 为 #rrggbb；large=true 表示 ≥18pt 或 14pt bold（对比阈值 3:1）。
"""

import argparse
import json
import math
import struct
import sys
import zlib

# ----------------------------------------------------------------------------
# 1. 纯标准库 PNG 解码（支持 8-bit RGB / RGBA；灰度按需扩展）
# ----------------------------------------------------------------------------

def _read_png(path):
    with open(path, "rb") as f:
        data = f.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("不是 PNG 文件: %s" % path)
    pos = 8
    width = height = bitdepth = colortype = None
    idat = b""
    while pos < len(data):
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        ctype = data[pos + 4:pos + 8]
        chunk = data[pos + 8:pos + 8 + length]
        if ctype == b"IHDR":
            width, height, bitdepth, colortype = struct.unpack(">IIBB", chunk[:10])
        elif ctype == b"IDAT":
            idat += chunk
        elif ctype == b"IEND":
            break
        pos += 12 + length
    if width is None:
        raise ValueError("PNG 缺少 IHDR")
    if bitdepth != 8 or colortype not in (2, 6):
        raise ValueError("仅支持 8-bit RGB(2)/RGBA(6)，当前 colortype=%s bitdepth=%s"
                         % (colortype, bitdepth))
    channels = 3 if colortype == 2 else 4
    raw = zlib.decompress(idat)
    stride = width * channels
    # 逐扫描线解滤镜
    pixels = bytearray(height * stride)
    prev = bytearray(stride)
    rp = 0  # 读指针（raw）
    for y in range(height):
        ftype = raw[rp]; rp += 1
        line = bytearray(raw[rp:rp + stride]); rp += stride
        if ftype == 0:      # None
            pass
        elif ftype == 1:    # Sub
            for i in range(channels, stride):
                line[i] = (line[i] + line[i - channels]) & 0xFF
        elif ftype == 2:    # Up
            for i in range(stride):
                line[i] = (line[i] + prev[i]) & 0xFF
        elif ftype == 3:    # Average
            for i in range(stride):
                a = line[i - channels] if i >= channels else 0
                line[i] = (line[i] + ((a + prev[i]) >> 1)) & 0xFF
        elif ftype == 4:    # Paeth
            for i in range(stride):
                a = line[i - channels] if i >= channels else 0
                b = prev[i]
                c = prev[i - channels] if i >= channels else 0
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[i] = (line[i] + pr) & 0xFF
        pixels[y * stride:y * stride + stride] = line
        prev = line
    return width, height, channels, pixels


# ----------------------------------------------------------------------------
# 2. 颜色工具
# ----------------------------------------------------------------------------

def _hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _rgb2hex(rgb):
    return "#%02x%02x%02x" % rgb


def _luminance(rgb):
    r, g, b = [c / 255.0 for c in rgb]
    def lin(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def wcag_ratio(rgb1, rgb2):
    l1, l2 = _luminance(rgb1), _luminance(rgb2)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def _contains(outer, inner, tol=1):
    """outer 是否完整包住 inner（父子嵌套，非真实碰撞）。"""
    return (inner["x"] >= outer["x"] - tol and inner["y"] >= outer["y"] - tol and
            inner["x"] + inner["w"] <= outer["x"] + outer["w"] + tol and
            inner["y"] + inner["h"] <= outer["y"] + outer["h"] + tol)


def _detect_bg(width, height, channels, pixels):
    # 采样外圈 4px 环，量化到 /16 取众数，再返回该众数组的真实均值色（避免取整误差）
    from collections import Counter
    cnt = Counter()
    acc = {}
    ring = 4
    for y in range(height):
        for x in range(width):
            if ring <= x < width - ring and ring <= y < height - ring:
                continue
            i = (y * width + x) * channels
            r, g, b = pixels[i], pixels[i + 1], pixels[i + 2]
            key = (r >> 4, g >> 4, b >> 4)
            cnt[key] += 1
            if key not in acc:
                acc[key] = [0, 0, 0, 0]
            acc[key][0] += r
            acc[key][1] += g
            acc[key][2] += b
            acc[key][3] += 1
    if not cnt:
        return (255, 255, 255)
    top = cnt.most_common(1)[0][0]
    s = acc[top]
    return (s[0] // s[3], s[1] // s[3], s[2] // s[3])


# ----------------------------------------------------------------------------
# 3. 像素模式度量
# ----------------------------------------------------------------------------

def audit_pixels(width, height, channels, pixels, bg, opt_x=0.50, opt_y=0.46,
                 grid=20):
    lb = _luminance(bg)
    # —— 平衡重心：全分辨率（细线元素不能漏）——
    sum_w = 0.0
    sum_wx = 0.0
    sum_wy = 0.0
    stride = width * channels
    for y in range(height):
        base = y * stride
        for x in range(width):
            i = base + x * channels
            if channels == 4 and pixels[i + 3] < 128:
                continue  # 透明 → 当底色
            d = abs(_luminance((pixels[i], pixels[i + 1], pixels[i + 2])) - lb) / 255.0
            if d <= 0:
                continue
            sum_w += d
            sum_wx += d * x
            sum_wy += d * y
    if sum_w == 0:
        cx = cy = 0.5
    else:
        cx = (sum_wx / sum_w) / width
        cy = (sum_wy / sum_w) / height
    dx = cx - opt_x
    dy = cy - opt_y
    balance_pass = abs(dx) < 0.03 and abs(dy) < 0.04

    # —— 粗粒度局部对比：网格采样 + 小窗口 min/max ——
    worst_contrast = float("inf")
    half = 8
    for y in range(0, height, grid):
        for x in range(0, width, grid):
            lmin, lmax = 1.0, 0.0
            for yy in range(max(0, y - half), min(height, y + half)):
                base2 = yy * stride
                for xx in range(max(0, x - half), min(width, x + half)):
                    i = base2 + xx * channels
                    if channels == 4 and pixels[i + 3] < 128:
                        continue
                    ln = _luminance((pixels[i], pixels[i + 1], pixels[i + 2]))
                    if ln < lmin:
                        lmin = ln
                    if ln > lmax:
                        lmax = ln
            if lmax > lmin:
                c = (lmax + 0.05) / (lmin + 0.05)
                if c < worst_contrast:
                    worst_contrast = c
    return {
        "balance": {
            "tier": "SIGNAL",
            "name": "visual-balance (ink centroid)",
            "centroid_x": round(cx, 4),
            "centroid_y": round(cy, 4),
            "optical_x": opt_x,
            "optical_y": opt_y,
            "delta_x": round(dx, 4),
            "delta_y": round(dy, 4),
            "accept": "<0.03 / <0.04",
            "pass": balance_pass,
            "note": "墨密度重心 vs 光学中心；刻意非对称时 SIGNAL 冲突属正常，创意选择通常赢。",
        },
        "local_contrast": {
            "tier": "SIGNAL",
            "name": "coarse local contrast (pixel)",
            "worst_ratio": round(worst_contrast, 2) if worst_contrast != float("inf") else None,
            "pass": worst_contrast >= 3.0 if worst_contrast != float("inf") else None,
            "note": "像素粗粒度采样的最差局部对比；真实文本对比请用 --rects 做 WCAG。",
        },
        "sampled_pixels": width * height,
    }


# ----------------------------------------------------------------------------
# 4. 矩形模式度量（元素框）
# ----------------------------------------------------------------------------

def audit_rects(rects):
    checks = []
    elems = []
    for e in rects:
        x, y, w, h = e["x"], e["y"], e["w"], e["h"]
        color = _hex2rgb(e.get("color", "#000000"))
        bg = _hex2rgb(e.get("bg", "#FFFFFF"))
        elems.append({"x": x, "y": y, "w": w, "h": h,
                      "kind": e.get("kind", "box"), "color": color, "bg": bg,
                      "large": bool(e.get("large", False))})

    # 碰撞（GATE）：交叠面积 / min(面积) ≥ 12%
    collisions = []
    for i in range(len(elems)):
        for j in range(i + 1, len(elems)):
            a, b = elems[i], elems[j]
            ix = max(a["x"], b["x"]); iy = max(a["y"], b["y"])
            ix2 = min(a["x"] + a["w"], b["x"] + b["w"])
            iy2 = min(a["y"] + a["h"], b["y"] + b["h"])
            if ix2 <= ix or iy2 <= iy:
                continue
            # 父子嵌套（一个完整包住另一个）不算碰撞，只留同级部分交叠
            if _contains(a, b) or _contains(b, a):
                continue
            overlap = (ix2 - ix) * (iy2 - iy)
            mn = min(a["w"] * a["h"], b["w"] * b["h"])
            ratio = overlap / mn if mn else 0
            if ratio >= 0.12:
                collisions.append({"a": (a["x"], a["y"], a["w"], a["h"]),
                                   "b": (b["x"], b["y"], b["w"], b["h"]),
                                   "ratio": round(ratio, 3)})
    checks.append({
        "name": "collision", "tier": "GATE",
        "count": len(collisions), "pass": len(collisions) == 0,
        "detail": collisions[:10],
        "note": "交叠 ≥12% 视为真实碰撞（GATE）。刻意重叠属创意选择，人眼确认而非自动 fail。",
    })

    # 对比（GATE）：文本元素 WCAG
    bad_contrast = []
    for e in elems:
        if e["kind"] != "text":
            continue
        ratio = wcag_ratio(e["color"], e["bg"])
        thr = 3.0 if e["large"] else 4.5
        if ratio < thr:
            bad_contrast.append({"rect": (e["x"], e["y"], e["w"], e["h"]),
                                 "ratio": round(ratio, 2), "threshold": thr})
    checks.append({
        "name": "contrast-wcag", "tier": "GATE",
        "count": len(bad_contrast), "pass": len(bad_contrast) == 0,
        "detail": bad_contrast[:10],
        "note": "WCAG 2 地板：正文 4.5:1 / 大字 3:1。深底亮字用 APCA 复算。",
    })

    # 对齐（SIGNAL）：同排文本/box 左缘近距 miss（1–7px）
    near_miss = []
    for i in range(len(elems)):
        for j in range(i + 1, len(elems)):
            a, b = elems[i], elems[j]
            # 跳过父子嵌套（包装盒与其子元素左缘本就重合，非真实错位）
            if _contains(a, b) or _contains(b, a):
                continue
            # 同排：y 区间重叠
            if not (b["y"] < a["y"] + a["h"] and a["y"] < b["y"] + b["h"]):
                continue
            d = abs(a["x"] - b["x"])
            if 1 <= d <= 7:
                near_miss.append({"a": a["x"], "b": b["x"], "delta": d})
    checks.append({
        "name": "alignment", "tier": "SIGNAL",
        "count": len(near_miss), "pass": len(near_miss) == 0,
        "detail": near_miss[:10],
        "note": "左缘 1–7px 偏差；可能是意外失齐（catch），也可能是刻意。看标注图再判。",
    })

    # 间距节奏（SIGNAL）：同排元素间 gap 的变异系数
    rows = {}
    for e in elems:
        rows.setdefault(round(e["y"]), []).append(e)
    spacings = []
    for y, group in rows.items():
        group.sort(key=lambda e: e["x"])
        for k in range(1, len(group)):
            gap = group[k]["x"] - (group[k - 1]["x"] + group[k - 1]["w"])
            if gap > 0:
                spacings.append(gap)
    if len(spacings) >= 2:
        mean = sum(spacings) / len(spacings)
        var = sum((s - mean) ** 2 for s in spacings) / len(spacings)
        cov = (var ** 0.5) / mean if mean else 0
    else:
        cov = 0.0
    checks.append({
        "name": "spacing-rhythm", "tier": "SIGNAL",
        "cov": round(cov, 3), "pass": cov < 0.35,
        "note": "同排 gap 变异系数；>0.35 提示节奏不齐（SIGNAL，非缺陷）。",
    })
    return checks, elems


# ----------------------------------------------------------------------------
# 5. SVG 叠加图（标注 findings，给独立 judge 看「哪里」）
# ----------------------------------------------------------------------------

def build_overlay(path, width, height, bg, checks, elems, balance, opt_x, opt_y):
    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
                 'viewBox="0 0 %d %d">' % (width, height, width, height))
    parts.append('<image href="%s" x="0" y="0" width="%d" height="%d"/>'
                 % (_escape(path), width, height))
    # 碰撞框：红
    for c in checks:
        if c["name"] == "collision" and c["count"]:
            for d in c["detail"]:
                for r in (d["a"], d["b"]):
                    parts.append(_rect(r, "#ff3b30", 3))
    # 低对比文本：橙
    for c in checks:
        if c["name"] == "contrast-wcag" and c["count"]:
            for d in c["detail"]:
                parts.append(_rect(d["rect"], "#ff9500", 3))
    # 对齐近距 miss：黄
    # （对齐为点，画竖线示意）
    for c in checks:
        if c["name"] == "alignment" and c["count"]:
            for d in c["detail"]:
                for xx in (d["a"], d["b"]):
                    parts.append('<line x1="%d" y1="0" x2="%d" y2="%d" '
                                 'stroke="#ffcc00" stroke-width="1" stroke-dasharray="4 4"/>'
                                 % (xx, xx, height))
    # 光学中心十字 + 墨密度重心
    cx = balance["centroid_x"] * width
    cy = balance["centroid_y"] * height
    ox = opt_x * width
    oy = opt_y * height
    parts.append('<circle cx="%.1f" cy="%.1f" r="10" fill="none" stroke="#34c759" '
                 'stroke-width="3"/>' % (cx, cy))
    parts.append('<line x1="%.1f" y1="0" x2="%.1f" y2="%d" stroke="#34c759" '
                 'stroke-width="1"/>' % (ox, ox, height))
    parts.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="#34c759" '
                 'stroke-width="1"/>' % (oy, width, oy))
    parts.append('</svg>')
    return "\n".join(parts)


def _rect(r, color, lw):
    x, y, w, h = r
    return ('<rect x="%d" y="%d" width="%d" height="%d" fill="none" '
            'stroke="%s" stroke-width="%d"/>' % (x, y, w, h, color, lw))


def _escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ----------------------------------------------------------------------------
# 6. 主流程
# ----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Archviz 展板成图审计（零依赖）")
    ap.add_argument("--image", required=True, help="渲染截图 PNG 路径")
    ap.add_argument("--rects", help="元素框 JSON（浏览器导出）；提供则启用碰撞/对齐/对比检查")
    ap.add_argument("--bg", default="auto", help="底色 auto 或 #rrggbb")
    ap.add_argument("--opt-x", type=float, default=0.50)
    ap.add_argument("--opt-y", type=float, default=0.46)
    ap.add_argument("--out", help="JSON 报告输出路径")
    ap.add_argument("--overlay", help="SVG 标注图输出路径")
    args = ap.parse_args()

    width, height, channels, pixels = _read_png(args.image)
    bg = _detect_bg(width, height, channels, pixels) if args.bg == "auto" else _hex2rgb(args.bg)

    report = {"image": args.image, "width": width, "height": height,
              "bg": _rgb2hex(bg), "optical_center": [args.opt_x, args.opt_y]}
    px = audit_pixels(width, height, channels, pixels, bg, args.opt_x, args.opt_y)
    report["pixel_mode"] = px

    if args.rects:
        with open(args.rects, "r", encoding="utf-8") as f:
            rects = json.load(f)
        rect_checks, elems = audit_rects(rects)
        report["rect_mode"] = rect_checks
        if args.overlay:
            svg = build_overlay(args.image, width, height, bg, rect_checks,
                                elems, px["balance"], args.opt_x, args.opt_y)
            with open(args.overlay, "w", encoding="utf-8") as f:
                f.write(svg)
            report["overlay"] = args.overlay

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)

    # 人类可读摘要
    print("=== Archviz Board Audit ===")
    print("image: %s  (%dx%d)  bg=%s" % (args.image, width, height, report["bg"]))
    b = px["balance"]
    print("· balance (SIGNAL): centroid=(%.3f, %.3f)  Δ=(%+.3f, %+.3f)  %s"
          % (b["centroid_x"], b["centroid_y"], b["delta_x"], b["delta_y"],
             "PASS" if b["pass"] else "REVIEW"))
    lc = px["local_contrast"]
    print("· coarse contrast (SIGNAL): worst=%s  %s"
          % (lc["worst_ratio"], "PASS" if lc["pass"] else "REVIEW"))
    if args.rects:
        for c in report["rect_mode"]:
            if "count" in c:
                val = "count=%d" % c["count"]
            else:
                val = "cov=%s" % c.get("cov")
            print("· %s (%s): %s  %s"
                  % (c["name"], c["tier"], val, "PASS" if c["pass"] else "REVIEW"))
    if args.out:
        print("· report -> %s" % args.out)
    if args.overlay:
        print("· overlay -> %s" % args.overlay)
    print("GATES 全过 = 过确定性地板（非好看）；SIGNALS 是指针不是裁决。")


if __name__ == "__main__":
    main()
