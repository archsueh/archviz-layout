# DESIGN.md — 图桥 (Bridge Canvas)

> Archviz 建筑展板视觉语言之一。电影表现力风；纯黑底 + 全铺 Hero + 金绿双色调。图是主角，结构是配角。

## 1. Visual Theme & Atmosphere
大型竞赛首图、叙事性空间节点、大跨度公共空间、夜景/黄昏氛围渲染的电影表现力风。纯黑或极深灰底、跨栏无边框大图 Hero、宽银幕黑边锚定、标题浮于暗部。情绪：戏剧性、沉浸、画质统一。

## 2. Color Palette & Roles
| Token | Hex | Role |
|---|---|---|
| `canvas` | `#141413` | 纯黑/极深灰底（全页背景） |
| `surface` | `#1C1B18` | 信息盒 / 浮层底（比 canvas 深一阶） |
| `hairline` | `#44403C` | 网格线 / 信息盒边框（暗金灰） |
| `ink` | `#E8E4E0` | 标题与正文（暗底亮字） |
| `ink-muted` | `#9A958C` | 次级文字 / 图注（暖灰） |
| `accent` | `#FFD500` | 金绿双色调中的金（唯一亮色事件） |
| `on-accent` | `#141413` | 强调色上的暗字 |

## 3. Typography Rules
- **Family**：`Inter` / `Helvetica Neue` / `Liberation Sans` + `Noto Sans CJK SC`。无头渲染指定 `Liberation Sans`。
- **Hierarchy**（px / weight / leading）：
  | Token | Size | Weight | Leading | Use |
  |---|---|---|---|---|
  | `display` | 96px | 600–700 | 1.05 | 项目名 / 浮于大图暗部 |
  | `title` | 28px | 600 | 1.2 | 区块/信息盒标题 |
  | `body` | 13px | 400 | 1.6 | 浮层正文 / 图注 |
  | `label` | 11px | 500 | 1.3 | Mono 角标（片名/坐标） |
  | `data` | 14px | 600 | 1.2 | 指标 `tabular-nums` |

## 4. Component Stylings
- **Hero Shot**：整幅渲染图铺底跨栏，无边框融入；宽银幕黑边 (Cinematic Black Bars) 作视觉锚。
- **Overlay 信息盒**：`surface` 半透或实底 + 1px `hairline`；标题与指标锚定某一网格栏。
- **Buttons**：极少用；若用，实填 `ink` 或描边 `accent`，0–2px 圆角。
- **Dividers**：1px `hairline` 暗金灰。

## 5. Layout Principles
- **Spacing scale**（8px 模数）：`4 / 8 / 12 / 16 / 24 / 32 / 48`。
- **Grid**：隐于大图之上——竖向容器线 / 中轴导引 / 分栏 scaffold，可见但克制；Hero 占绝大多数画幅。
- **Whitespace**：黑底是留白本身；信息盒靠 `surface` 抬升分区。

## 6. Depth & Elevation
**无投影。** 层级靠暗底亮字的反差 + `surface` 浮层 + 1px hairline。渲染图色调采用金绿双色调分离 (teal-gold split-tone) 统一画质。

## 7. Do's and Don'ts
- ✅ 大图铺底当舞台；标题浮暗部；金绿双色调统一；网格 scaffold 克制可见。
- ❌ 不把 Hero 降级成角落缩略；不加光效/渐变叠加；不用第二种亮色；不强制两端对齐正文。

## 8. Responsive Behavior
- 桌面 A0 全铺 Hero + 浮层；窄屏 Hero 置顶、信息盒堆叠于下；移动端保持黑底沉浸。
- tap 目标 ≥ 44×44。

## 9. Agent Prompt Guide
生成图桥展板时：认领本语言 → 锁 `canvas #141413` + `accent #FFD500` → 大图铺底跨栏 → 标题浮暗部 → 金绿双色调统一 → 跑 `capture_rects.py --run-audit`（注意深底亮字用 APCA 复算对比）。快速色参：`near-black #141413, warm off-white #E8E4E0, gold #FFD500`。
