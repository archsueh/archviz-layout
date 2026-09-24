# DESIGN.md — 静纸 (Still Paper)

> Archviz 建筑展板视觉语言之一。投影、渐变、玻璃拟态一律禁止；克制与手稿感是高级感的来源。
> 本文件供 AI 生成/校验静纸语言展板时直接读取，是 SKILL.md 的紧凑 token 伴侣。

## 1. Visual Theme & Atmosphere
文化地标、博物馆、住宅、城市微更新、景观与乡村规划的纸本手作风。暖白粗糙纸面、衬线标题、岁月沉淀的木石质感；理性网格藏在内容之下，不喧宾夺主。情绪：安静、人文、有重量。

## 2. Color Palette & Roles
| Token | Hex | Role |
|---|---|---|
| `canvas` | `#F5F4ED` | 暖白纸面底色（全页背景） |
| `surface` | `#EFECE3` | 卡片/图框底（比 canvas 深一阶） |
| `hairline` | `#C9C7BC` | 结构导轨 / 边框线（线宽 ≤ 0.8px） |
| `ink` | `#141413` | 标题与正文（近黑，绝不用纯黑） |
| `ink-muted` | `#6B6256` | 次级文字 / 图注（暖灰） |
| `accent` | `#C96442` | 朱砂/红土强调，**仅用于无字强调**（填充块 / 发丝线 / 标记点；全图唯一饱和色事件）。作按钮填充时**必须压深字 `ink`**（4.73:1） |
| `accent-ink`（浅面） | `#8A3A22` | 浅底上的强调色**文字**（朱砂在浅底仅 3.54:1，压深后 7.05:1） |
| `accent-ink`（暗面） | `#E07A54` | 暗面色块上的强调色**文字**——同一朱砂在 `#1C1B18` 上只有 **4.41:1**（差一点不达标），暗面必须**提亮**而非压深 |
| `on-accent` | `#F5F4ED` | 强调填充上的反白文字（须配 `accent-ink` 底 7.05:1；**配 `accent` 底仅 3.54:1，不达标**） |

## 3. Typography Rules
- **Family**：`YuMincho`/`Georgia` + `Noto Serif CJK SC`（游明朝/ Georgia 衬线）。无头渲染必须指定 `Georgia` 或嵌入真字体，禁用裸 `serif` 降级。
- **Two-Size 原则**（Vignelli 启发）：整板最多两种字号尺度，靠字重/面积反差拉张力。
- **Hierarchy**（px / weight / leading）：
  | Token | Size | Weight | Leading | Use |
  |---|---|---|---|---|
  | `display` | 96px (72pt) | 300–500 | 1.05 | 项目名 / 关键数字（轻字重，拒绝粗体） |
  | `title` | 28px | 500 | 1.2 | 区块标题 |
  | `body` | 13px (10pt) | 400–500 | 1.6 | 正文 / 图注 |
  | `label` | 11px | 500 | 1.3 | 角标 / 章节标号（可 Mono） |
  | `data` | 14px | 500 | 1.2 | 标高/面积/坐标等 `tabular-nums` 等宽数字 |
- **Principle**：标题字重尽量轻（Light/Medium）；正文一律 Flush-left ragged-right，**禁止强制两端对齐**。

## 4. Component Stylings
- **Buttons**：极少用；若用，无填充、1px `hairline` 描边、`ink` 文字，0–2px 圆角。
- **Cards / 图框**：`surface` 底 + 1px `hairline` 边框，无阴影；图框内渲染图用暖墨双色调 (duotone, `grade:"duo"`)。
- **Stamps / 角标**：Mono 或小型衬线，全大写，字距 0.05em，色 `ink-muted` 或 `accent`。
- **Dividers**：1px `hairline` 横分割线，线宽 ≤ 0.8px。

## 5. Layout Principles
- **Spacing scale**（基线倍数）：`4 / 8 / 12 / 20 / 32 / 48 / 96`（A0 展板主间距 20mm，作品集 8–12mm）。
- **Grid**：A0 竖向 3 或 6 栏；横向 4/8/12 栏；作品集 6/12 栏。外留白神圣不可侵犯（A0 ≥ 50–80mm，作品集短边 6–8%）。
- **Whitespace**：留白即结构；大图自带呼吸，文字块靠网格对齐，不用空 div 夹白。

## 6. Depth & Elevation
**无投影、无渐变背景、无氛围叠加。** 层级只靠 `canvas→surface` 一阶抬升 + 1px `hairline` 表达。深度来自纸面纹路与墨色层次，而非光效。

## 7. Do's and Don'ts
- ✅ 衬线标题轻字重；网格导轨 ≤0.8px 克制可见；暖墨双色调统一渲染图调性。
- ❌ 不用粗体标题（≥700）、不用阴影/渐变/玻璃拟态、不用第二种饱和色、不用 emoji 装饰。

## 8. Responsive Behavior
- 桌面 A0（841×1189mm 比例）按 3/6 栏；窄屏（≤1024px）塌为单栏堆叠，主间距缩到 12–16px；移动端大号 display 保持但区隔行高放松。
- tap 目标 ≥ 44×44（若展板含可点元素）。

## 9. Agent Prompt Guide
生成静纸展板时：认领本语言 → 锁 `canvas #F5F4ED` + `accent #C96442` → 衬线轻字重标题 → 网格导轨 ≤0.8px → 渲染图暖墨 duotone → 跑 `capture_rects.py --run-audit` 核验碰撞/对比/平衡。快速色参：`warm off-white #F5F4ED, near-black ink #141413, terracotta accent #C96442`。
