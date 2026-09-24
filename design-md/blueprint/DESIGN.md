# DESIGN.md — 技术蓝图 (Technical Blueprint)

> Archviz 建筑展板视觉语言（**新增，v1.2.0**）。深色工程控制台 / CAD 图幅气质：深蓝底 + 青色 hairline 网格 + Mono 标签 + 0 圆角。
> 来源：archviz 自身 Swiss 极简纪律 + 同基因子集（IBM Carbon / Supabase / HashiCorp / Linear / Vercel）的「精密技术网格」共性——4/8px 间距模数、字重 600 封顶 + 负字距、surface 层级替投影、1px hairline、单色灰阶 + 单一青色强调、0 圆角、Mono 微标签。
> 与现有语言区分：**signal-proof** 是轻量冷灰 + 电蓝文档风；**bridge-canvas** 是黑底 + 金绿电影风；**blueprint** 是深蓝图幅 + 青色网格线，专供技术图纸 / 构造详图 / 规范表类板。

## 1. Visual Theme & Atmosphere
技术图纸、构造大样、BIM/明细表、设备与管综、规范对照板的工程控制台气质。深蓝图幅底、青色 hairline 网格隐约可见、等宽字体标注坐标与标高、单一青色强调。情绪：精确、冷静、像一张会发光的 CAD 图幅。

## 2. Color Palette & Roles
| Token | Hex | Role |
|---|---|---|
| `canvas` | `#0D1B2A` | 深蓝图幅底（全页背景） |
| `surface-1` | `#14253A` | 信息盒 / 浮层底（抬升一阶） |
| `surface-2` | `#1B3047` | 次级浮层 / hover |
| `hairline` | `#2A4A6B` | 青蓝网格线 / 1px 边框（蓝图线） |
| `ink` | `#DBE7F0` | 标题与正文（冷亮字） |
| `ink-muted` | `#8AA4BF` | 次级文字 / 图注 |
| `ink-subtle` | `#5C748F` | 三级文字 / 坐标占位 |
| `accent` | `#5FD0E8` | 青色（蓝图线高亮 / 唯一亮色事件） |
| `on-accent` | `#0D1B2A` | 强调色上的暗字 |

## 3. Typography Rules
- **Family**：`Inter` / `Helvetica Neue` / `Liberation Sans` + `Noto Sans CJK SC`；数据/标注用 `ui-monospace`/`SFMono`/`Menlo`。
- **Hierarchy**（px / weight / leading / tracking）：
  | Token | Size | Weight | Leading | Tracking | Use |
  |---|---|---|---|---|---|
  | `display` | 88px | 600 | 1.05 | -2.0px | 项目名 / 关键数字（负字距收紧） |
  | `title` | 26px | 600 | 1.2 | -0.6px | 区块标题 |
  | `body` | 13px | 400 | 1.55 | 0 | 正文 / 图注 |
  | `label` | 11px | 600 | 1.3 | 0.6px | 大写章节眉标（Mono，正字距） |
  | `data` | 14px | 600 | 1.2 | 0 | 标高/面积/坐标 `tabular-nums` |
- **Principle**：展示字重 600 封顶（禁 700+）；display 负字距是品牌声量；Mono 仅用于坐标/标高/章节眉标，绝不装饰性 trend-slop。

## 4. Component Stylings
- **Buttons**：实填 `accent` + `on-accent` 暗字，0px 圆角（方正工程感）；次级 1px `hairline` 描边。
- **Cards / 图框**：`surface-1` 底 + 1px `hairline` 青蓝线，无阴影；图幅边框即蓝图网格。
- **Stamps / 网格标号**：Mono 全大写，字距 0.06em，`accent` 或 `ink-muted`；作技术身份印记。
- **Dividers**：1px `hairline` 青蓝蓝图分割线。

## 5. Layout Principles
- **Spacing scale**（8px 模数，4px 半步）：`4 / 8 / 12 / 16 / 24 / 32 / 48 / 96`。
- **Grid**：显式青蓝 hairline 网格（可隐约可见，线宽 ≤ 0.8px）；A0 竖向 3/6 栏、横向 4/8/12 栏；外留白神圣。
- **Whitespace**：深蓝底是留白本身；区块靠 `canvas↔surface-1` 抬升 + hairline 分区。

## 6. Depth & Elevation
**无投影、无渐变氛围。** 层级靠 `canvas→surface-1→surface-2` 三级表面抬升 + 1px hairline。深底亮字对比用 APCA 复算（非 WCAG 比值）。

## 7. Do's and Don'ts
- ✅ 深蓝图幅 + 青色 hairline 网格；单色冷灰阶 + 唯一青色；0 圆角方正；Mono 仅技术标注；字重 600 封顶 + 负字距。
- ❌ 不引入第二种饱和色；不加阴影/渐变光效；不方化之外的圆角；不在青色上用非暗字；不写无语义伪技术 caption。

## 8. Responsive Behavior
- 桌面 A0 按 3/6 栏，蓝图网格隐约可见；窄屏塌单栏，主间距 16px；移动端 display 收紧行高。
- tap 目标 ≥ 44×44。

## 9. Agent Prompt Guide
生成 blueprint 展板时：认领本语言 → 锁 `canvas #0D1B2A` + `accent #5FD0E8` + `hairline #2A4A6B` → 青蓝 hairline 网格 → 0 圆角方正组件 → 字重 600 封顶 + display 负字距 → 跑 `capture_rects.py --run-audit`（深底亮字用 APCA 复算）。快速色参：`deep navy #0D1B2A, cool off-white #DBE7F0, blueprint cyan #5FD0E8`。
