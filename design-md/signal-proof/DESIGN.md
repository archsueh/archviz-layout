# DESIGN.md — 实证 (Signal Proof)

> Archviz 建筑展板视觉语言之一。理性技术图风；冷灰档案底 + 电蓝强调 + 工程蓝图分割线。禁止装饰性光效，靠精度说话。

## 1. Visual Theme & Atmosphere
城市 TOD 枢纽、高新产业园、实验室、绿色性能分析、剖面大样与构造图纸的理性技术图风。冷灰/奶白档案底、高对比粗黑体标题、电蓝强调、VERIFIED/TECHNICAL 印记式外框。情绪：精确、可信、工程化。

## 2. Color Palette & Roles
| Token | Hex | Role |
|---|---|---|
| `canvas` | `#F5F5F4` | 冷灰档案底色（全页背景） |
| `canvas-alt` | `#E4E8F0` | 奶白/冷蓝灰交替区段带 |
| `surface` | `#FFFFFF` | 卡片 / 图表外框底 |
| `hairline` | `#CBD5E1` | 工程蓝图分割线 / 1px 边框 |
| `ink` | `#0A0A0A` | 标题与正文（近黑） |
| `ink-muted` | `#52525B` | 次级文字 / 图注 |
| `accent` | `#0039A6` | 科技电蓝（全图唯一饱和强调） |
| `accent-soft` | `#1D4ED8` | 链接 / 焦点态 |
| `on-accent` | `#FFFFFF` | 强调色上的文字 |

## 3. Typography Rules
- **Family**：`Inter` / `Helvetica Neue` / `Liberation Sans` + `Noto Sans CJK SC`。无头渲染指定 `Liberation Sans`，禁用裸 `sans-serif`。
- **Hierarchy**（px / weight / leading）：
  | Token | Size | Weight | Leading | Use |
  |---|---|---|---|---|
  | `display` | 88px | 600–700 | 1.05 | 项目名 / 关键数字（高对比粗黑体） |
  | `title` | 26px | 600 | 1.2 | 区块标题 |
  | `body` | 13px (10pt) | 400 | 1.55 | 正文 / 图注 |
  | `label` | 11px | 600 | 1.3 | 大写章节眉标 / 印记标签 |
  | `data` | 14px | 600 | 1.2 | 指标数字 `tabular-nums` |

## 4. Component Stylings
- **Buttons**：实填 `accent` + 白字，0–2px 圆角；次级为 1px `hairline` 描边。
- **Cards / 图表外框**：`surface` 白底 + 1px `hairline`；数据分析图外框加 `VERIFIED`/`TECHNICAL` 印记式标签框定。
- **Stamps**：全大写、字距 0.08em、`accent` 或 `ink`；作为技术身份印记，非装饰。
- **Dividers**：1px `hairline` 工程蓝图分割线。

## 5. Layout Principles
- **Spacing scale**（8px 模数）：`4 / 8 / 12 / 16 / 24 / 32 / 48 / 96`。
- **Grid**：A0 竖向 3/6 栏；横向 4/8/12 栏；作品集 6/12 栏。外留白神圣。
- **Whitespace**：靠 `canvas↔canvas-alt` 区段带 + 1px hairline 分区，而非大垂直间隙。

## 6. Depth & Elevation
**无投影、无渐变氛围。** 层级靠 `canvas→surface` 抬升 + 1px hairline。渲染图色调采用冷色调签名 (sl-duo) 凸显理性精度。

## 7. Do's and Don'ts
- ✅ 粗黑体高对比标题；电蓝仅用于 CTA/链接/印记；图表外框 VERIFIED 印记；tabular-nums 数据列对齐。
- ❌ 不引入第二种饱和色；不加阴影/渐变；不在电蓝上用非白字；不写无语义 trend-slop 伪技术 caption。

## 8. Responsive Behavior
- 桌面 A0 按 3/6 栏；窄屏塌单栏，主间距 16px；移动端 display 收紧行高。
- tap 目标 ≥ 44×44。

## 9. Agent Prompt Guide
生成实证展板时：认领本语言 → 锁 `canvas #F5F5F4` + `accent #0039A6` → 粗黑体高对比标题 → 工程蓝图 hairline 网格 → 图表外框 VERIFIED 印记 → 跑 `capture_rects.py --run-audit`。快速色参：`cool gray #F5F5F4, near-black #0A0A0A, electric blue #0039A6`。
