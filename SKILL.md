---
name: archviz-layout
description: Use when designing architectural visualization presentation boards, portfolio layouts, competition drawings, and organizing visual assets (renderings, drawings, diagrams) into clean grid systems. Also use for pre-delivery board polish — typography/tracking, real project imagery, AI render artifacts, narrative specificity, and Board readiness audit (Meng-style, adapted for archviz — not marketing landing pages).
license: MIT
metadata:
  version: 1.1.1
  source: https://github.com/archsueh/archviz-layout
  risk: safe
  author: archsueh
  triggers: presentation board, portfolio layout, competition drawing, board polish, readiness audit, grid system, 渲染评图, 视觉平衡, 对比度闸门, 展板, 作品集, 排版, 建筑可视化, architectural layout
---

# Architectural Visualization Presentation Layout (Archviz-Layout)

## 概述
Archviz-Layout（建筑表现与图面设计）是融汇**画面叙事（Narrative）**、**技术精度（Precision）**与**视觉美学（Aesthetics）**的系统性规范。本 Skill 整合了瑞士国际主义字体排印风格（Müller-Brockmann 模块化网格）、维涅里设计法则（Vignelli Canon 视觉层级）以及 Archviz 图像色彩配对系统，旨在让 AI 智能体在排版建筑设计展板（A0/A1 Panels）、个人作品集（Portfolios）和场地分析图纸时，遵循严谨的理性秩序，杜绝无序拼凑与低质 AI 审美。

---

## 触发场景 / When to Use
* **竞赛图版排版 (Competition Boards)**：设计 A0/A1 级别的超大横竖向展板，对渲染大图、总图、平立剖图纸和分析图进行网格对齐。
* **作品集版式 (Portfolio Layout)**：起草或重构 A4/A3 横向/纵向个人建筑作品集模板。
* **图纸分析图整合 (Diagram & Drawing Integration)**：在单张图纸内对概念演变、流线分析、日照分析等图表与正文进行协调。
* *配合使用*：当任务涉及具体的 3D 渲染图生成时，路由到 `archviz-3d` 或 `archviz-sketch`，本 Skill 仅负责图面排版设计。

---

## 核心设计纪律 (The Intangibles)

1. **画面叙事 (Narrative Space)**：图面即空间。展板的阅读路线应当模仿空间游历的叙事逻辑（如“鸟瞰概念 -> 场地分析 -> 主题渲染 -> 空间平立剖 -> 细部构造”），图面排列应有强烈的动线引导（Flowline）。
2. **视觉冲击力 (Visual Power)**：力量来源于**尺度的对比**，而非颜色的繁多。展板上必须存在一个绝对的视觉核心（Hero Shot），与其他辅助图纸形成鲜明的面积比差。
3. **适当性原则 (Appropriateness)**：版式调性必须与建筑项目性格匹配。
   * *粗野主义/工业项目*：刚性灰色表面，大网格，强对比，使用大字重无衬线体。
   * *文化/艺术/住宅项目*：白色或暖纸色表面，宽留白，细网格，配以优雅的衬线体标题。
4. **评审基线 (The Name-on-It Bar)**：成图前自问「我愿不愿意把名字署在这张板上？」—— 判据不是「能不能用」，而是「是否 unambiguously intentional & crafted」。落版后**强制跑第六节「渲染评图循环」**，而非只看代码或清单自查（模型看不到自己画的像素）。
5. **留白即结构 (Negative Space as Structure)**：建筑语境下空白是秩序的一部分，不是剩余废料。动线（Flowline）、材料与光的暗示、入口/转场（Threshold）都应当被**显式设计**为「穿越 moment」，而非顺手留白。这与「空气泡原则」同源但更主动：留白要有理由，要么承托 Tier 1 的呼吸，要么是页眉/页脚的 whitespace 控制。
6. **冲击留给标点 (Reserve Impact for Punctuation)**：全版只允许 1–2 处「放大」—— Hero 透视、一处饱和强调色、或一个签名式动势。其余一切保持安静收敛，大 moment 才读得出力道；满版强度 = 平。这与「视觉冲击力（尺度对比，非颜色繁多）」互为表里。

---

## 建筑版式三套视觉语言 (Architectural Visual Languages)

版式调性不只是表面的皮肤，而是项目内涵的表达介质。根据建筑方案的不同属性，应精准认领以下三套视觉语言之一来承载图面：

* **1. 静纸 (Still Paper) - 纸本手作风**
  - **适用项目**：文化中心、地标博物馆、住宅设计、城市微更新、景观与乡村规划。
  - **视觉配方**：暖白色粗糙纸面底色（`#F5F4ED`）、优雅宋体/衬线体标题（`YuMincho` / `Georgia`，500中等字重，拒绝粗体）、朱砂/红土色强调标示（`#c96442`）、极细线条边框（线宽 ≤ 0.8px）。渲染图色调处理上，采用**暖墨双色调 (duotint/duotone)**，配置为 `grade: "duo"` 暖墨，凸显手稿感和岁月沉淀的木石质感。
* **2. 实证 (Signal Proof) - 理性技术图风**
  - **适用项目**：城市TOD交通枢纽、高新产业园、科学实验室、绿色低碳/可持续性能分析图、剖面大样与构造图纸。
  - **视觉配方**：冷灰色或奶白档案底色（`#F5F5F4` 或 `#E4E8F0`）、高对比粗黑体标题（`Inter` / `Helvetica`）、科技感电蓝色强调（`#0039A6`）、工程蓝图分割线、数据分析图外框使用“VERIFIED/TECHNICAL”印记式标签进行框定。渲染图色调采用**冷色调签名 (sl-duo)**，凸显理性精度。
* **3. 图桥 (Bridge Canvas) - 电影表现力风**
  - **适用项目**：大型竞赛图纸首图、叙事性强的空间节点表现、大跨度公共空间、夜景/黄昏渲染氛围图。
  - **视觉配方**：纯黑或极深灰色背景（`#141413`）、全铺/跨栏无边框大图渲染（Hero Shot）、电影级宽银幕黑边（Cinematic Black Bars）视觉锚定，标题直接浮于大图暗部或大面积黑底中。渲染图色调采用**金绿双色调分离 (teal-gold split-tone)**，建立统一而富有戏剧性的影视画质。

---

## 五步排图工作流 (Five-Step Layout Workflow)

排版是“内容理解”与“确定性骨架”的协同过程，智能体应当遵循以下五个核心步骤进行排图，不允许直接套用千篇一律的固定模板：

1. **第一步：读懂内容 (Understand)**
   - 彻底梳理建筑方案的核心立意、场地属性及图纸清单（如：共有 3 张效果图、1 个总平面图、2 个流线分析图、4 段说明）。
   - 识别排版限制（如：A0竖展板还是A3作品集横页；需要弱化分析图颜色以突出效果图；是否保留场地原有Logo等）。
2. **第二步：风格定调 (Tune)**
   - 根据项目类型，认领上述三套视觉语言之一（静纸/实证/图桥）。
   - 确定本页/本展板的主色调，锁死调色板（Palette）与字体层级（Typography Rules），在后续生成中保持高度一致。
3. **第三步：图面分页/分块 (Split)**
   - 对内容进行“叙事分页”或“图板区域划分”。
   - 绝不将同质化的内容塞在相邻网格；每一页/每一个版面块都必须有一个“唯一任务”（如：第1块专攻场地概念；第2块专攻核心透视；第3块收尾技术大样）。
4. **第四步：落版布局 (Layout)**
   - 按照网格系统（Grid System）将 drawings 填充进分栏中。
   - 严格执行**影像优先（Image-First）**原则：能用图纸/分析图说话，就不堆砌文字。将图片置于视觉重心。若无图（纯文字叙事），则通过大号文字比例或排版装饰器创造呼吸感。
5. **第五步：成图核校 (Verify)**
   - 检查视线流动线（Flowline）是否对齐，段落是否有寡妇词悬挂（Runts），色彩对比度是否满足易读性，网格间距是否一致，确认图面无过度装饰后成图。
   - 随后强制跑一遍 **Meng-style Board Polish**（见下节）：字距、假图、AI 伪影、项目专属 human detail、Board readiness 输出。落版不等于可提交；核校通过才可交付。

---

## 理性网格系统 (The Modular Grid)

版式设计的基石是网格。网格不是装饰，而是信息的承载骨架。

### 1. 网格设定与页面比例
* **外留白 (Margins)**：四周边距必须保持一致且神圣不可侵犯。
  - A0 展板：外边距建议留出至少 `50mm - 80mm`。
  - A3/A4 作品集：外边距建议为页面短边的 `6% - 8%`，为手指握持和装订预留空间。
* **模块分栏 (Modular Columns)**：
  - **A0 竖向展板**：采用 `3栏` 或 `6栏` 竖向网格。
  - **A0 横向展板**：采用 `4栏`、`8栏` 或 `12栏` 横向网格。
  - **A4/A3 作品集（横版）**：采用 `6栏` 或 `12栏` 细分网格。
* **网格间距 (Gutters)**：图纸/文本框之间的间距必须保持统一，推荐使用 baseline 的倍数（如 A0 展板间距设为 `20mm`，作品集设为 `8mm - 12mm`）。

### 2. 基准线锁定 (Baseline Lock) & Subgrid
* 正文及小标注的行高、段前/段后间距必须严格锁定为基准线高度（如 `8px` 或 `12px`）的整数倍。
* **图片与图纸的高度**：所有渲染图和工程图在网格中放置时，其顶部和底部边框必须精准对齐网格模块的格线（Baseline/Flowline），确保横向视线贯通。

### 3. 光学对齐 (Optical Alignment)
* 超大字号的标题（如 `60pt` 以上的项目名称）在左侧对齐网格线时，必须引入光学左移（Optical Left Shift），即向左微调 `2px - 8px`，使首字母的字形物理墨迹（而非字体外框边界）与垂直网格线重合，消除视觉凹陷。

---

## 网格导轨与构图范式 (Grid Rails & Composition Patterns)

网格是骨架，但骨架可以「可见」也可以「隐于内容」。本节能从通用网页网格体系（editorial / image-first）移植的，是**把秩序画出来**与**让图当舞台**两件事——它们与瑞士网格同源，但更强调结构的可感知性。

### 1. 结构导轨 (Structural Guide Lines)
* 在版面上**显式画出**外框轨（Outer Rails）、中轴导引线（Center Guides）、四角标记（Corner Markers），给无形状的白色区域一个可依附的秩序骨架。
* **克制优先**：导轨线宽 ≤ `0.8px`、色号取网格线同族（`#D6D3D1` / `#44403C`），不抢内容；它们的作用是「让结构 quietly organize」，不是装饰。
* 与「光学对齐」呼应：导轨是几何基准，眼睛是最终裁判——测量齐了但若看着偏，仍要手动 ±1–2px 光学微调。

### 2. 图为主舞台 (Image-as-Stage)
* Tier 1 Hero / 图桥语言的大图应被当作**舞台（Stage）**：整幅渲染图铺底占据绝大多数画幅，网格与文字块只是浮在其上的 overlay 结构。
* 在图上叠一层**安静的网格系统**（竖向容器线 / 中轴导引 / 分栏 scaffold），可见但克制；主标题与 CTA/图名锚定在某一网格栏，次级信息盒（引用 / 指标 / 叙事）落在相邻栏。
* **绝不**把大图降级成角落缩略图或卡片缩略——图是主角，结构是配角。

### 3. 底部锚定 Hero + 邻栏次信息 (Bottom-Anchored Hero)
* Hero 文案与项目名**锚定在版面下部或某条明确边线**，而非永远居中；次级 box（引用 / 证言 / 指标 / 支撑叙事）浮在相邻网格车道，保留强负空间。
* 这避免「居中单栏 mush」——中轴对齐是瑞士网格的利器，但**持续居中**会读成平均化、无主张。

### 4. 服务行列表 (Service-Row Listings)
* Tier 3 工程图 / 技术大样 / 指标行，应以**干净的多栏清列**呈现：极小 metadata（标高 / 比例 / 图号）+ 强标题 + 克制的交互态，而非卡片堆叠。
* 与「空气泡原则」结合：成组排列时外边线严格对齐网格边缘，图纸间距一致，组间留白即结构。

---

## 视觉层级与资产排布 (Hierarchy & Asset Mapping)

### 1. 资产等级划分 (Asset Priority)
排版前，将所有图面元素分级，严格按下表分配图面面积和视线权重：

| 等级 | 元素类型 | 版面占比 | 对齐/设计要求 |
|---|---|---|---|
| **Tier 1 (焦点)** | 氛围效果图 (Hero Render)、鸟瞰图 (Isometric) | 35% - 50% | 跨多栏布局，通常居中或置顶，不贴文字 |
| **Tier 2 (核心)** | 总平面图 (Master Plan)、核心透视剖面 (Perspective Section) | 20% - 30% | 严格置于流动线 (Flowline) 基准上，确保比例尺清晰 |
| **Tier 3 (支撑)** | 平立剖工程图 (Technical Drawings)、大样图 | 15% - 20% | 成组排列，外边线严格对齐网格边缘，图纸间距一致 |
| **Tier 4 (叙事)** | 场地概念演变分析图 (Analysis Diagrams) | 10% - 15% | 采用系列化（Sequence）横向连环画式排布 |
| **Tier 5 (辅助)** | 说明文字、经济技术指标、图名标注 | 5% - 10% | 紧凑排布在边缘栏，使用弱对比色，严禁跨格乱飞 |

### 2. 空气泡原则 (Air Bubble Principle)
* 在超大效果图或总图周围，必须保留至少一个完整的网格单元（Module）作为留白。
* 严禁将大段正文或硬线条分析图标注紧贴渲染图的边缘，防止破坏渲染图所营造的图面氛围。

---

## 字体系统与字型排印 (Typography)

限制字体数量，通过尺度与粗细字重的巨大反差来体现视觉张力。

### 1. 字体搭配系统
* **方案 A：现代技术流 (Modernist / Grotesque)**
  - 适用：概念建筑、城市设计、工业遗址改造。
  - 字体：`Inter` / `Helvetica Neue` / `Liberation Sans` + `Noto Sans CJK SC` (思源黑体)。
* **方案 B：人文艺术流 (Serif / Editorial)**
  - 适用：文化地标、博物馆、住宅设计、历史更新项目。
  - 字体：`YuMincho` (游明朝) / `Georgia` + `Noto Serif CJK SC` (思源宋体)。

### 2. 尺度层级配置 (Two-Size Scale - Vignelli 启发)
为了绝对的克制，整张展板/页面上**最多只出现两种字号**。例如：
* **模式 A（展板超大对比）**：
  - 大字号（项目名称 / 关键数字）：`72pt` (超轻/超细字重，避免臃肿)
  - 小字号（副标题 / 正文 / 标注）：`10pt` (中/粗字重，确保可读性)
* **模式 B（作品集雅致比例）**：
  - 标题字号：`24pt`
  - 正文与标注：`9pt`
* *排印规则*：**标题字重尽量轻（Light/Medium），正文及标注字重相对适中**。正文排版一律采用**左对齐、右侧自然流出 (Flush-left, ragged-right)**，绝对禁止强制两端对齐以避免出现不自然的单词空隙。

### 3. 层级清晰铁律（眯眼测试）
* 整张板在**眯眼或退远**状态下，标题与正文必须一眼可分——若分不出，层级过弱（不是字号不够，是字重/对比/面积反差没拉开）。
* 技术图纸的标高、面积、坐标等**数据**一律 `tabular-nums` 等宽数字对齐成列；**仅当数值真成列对齐时用 Mono**，禁止把 Mono 当装饰微标签（伪技术 caption 如 `35MM · DEVELOP · SCAN`）——那是无语义 trend-slop，与瑞士克制相悖。

---

## 色彩与灰度控制 (Color Palette)

色彩是用于表达逻辑的标识系统（Chromotype），而非单纯的装饰。

### 1. 配色提取纪律
* **主色提取 (Color Extraction)**：从项目的 Tier 1 焦点效果图（如清晨、落日或夜景渲染）中，提取 **1 种核心主色** 和 **1 种微弱辅色**。
* **色彩分配原则**：
  - 版面底色与网格线：保持在单色黑白灰（底色：纯白 `#FFFFFF` / 暖纸色 `#F5F4ED` / 深黑 `#141413`）。
  - 分析图标注、流线箭头、重点数据：统一使用提取的核心主色，其余元素全部弱化为灰色。
  - **最大一处强调色 (Max 1 Accent)**：全图只允许一处（通常是项目标题或流线终点）使用最高饱和度的强调色。

### 2. 灰度适配 (Value Tuning)
* **日景主题展板**：底色 `#FFFFFF` 或 `#F5F5F4`，文字 `#111111`，边框线 `#D6D3D1`（低对比，高雅）。
* **夜景/特定叙事展板**：底色 `#141413`（深色），文字 `#E8E4E0`，边框 `#44403C`，渲染图边框使用微发光或无边界融入。

### 3. 对比度闸门（WCAG 地板 + APCA 感知）
色彩对比不是「看着清楚就行」，必须有可测量的判据：
* **WCAG 2 作为合规地板**：正文文本对比 ≥ `4.5:1`，大字号（≥ `18pt` 或 `14pt` bold）≥ `3:1`。这是可访问性硬门槛，也是展板退远 2m 与手机缩略预览的双重底线。
* **APCA 用于感知设计**：WCAG 比率对深底亮字、中间调灰阶误判严重。做图桥语言（深底亮字）或灰阶层次时，用 **APCA**（apcacontrast.com）按感知亮度决策，而非 WCAG 比值。
* **实测，不口述**：落版核验（第五步 Verify 与 Meng-style Polish）必须取版面主文与底色算对比、标注数值（如 `APCA Lc 78` / `WCAG 7.2:1`），禁止只写「够清楚」。

---

## 经典版式模板 (Layout Schemes)

### 1. 经典 A0 竖向展板“三段网格”
```
+------------------------------------------------+
| [A] 项目名称 / 大数字指标 (72pt, 占 1/6 高度)      |
+------------------------------------------------+
|                                                |
| [B] HERO SHOT - 焦点透视图 (占 3/6 高度)         |
|     (跨所有 3 栏网格，左右到边)                  |
|                                                |
+----------------+---------------+---------------+
| [C1] 场地/概念  | [C2] 总平面图 | [C3] 剖面大样  |
|      分析图     |      与正文   |      与指标    |
|   (栏 1 放置)   |  (栏 2 放置)   |  (栏 3 放置)   |
+----------------+---------------+---------------+
```

### 2. A3作品集双页跨版 (Double Page Spread)
```
[ 左页 - 概念与叙事 ]                [ 右页 - 表现与实景 ]
+--------------------------------++--------------------------------+
|  Chapter 01                    ||                                |
|  PROJECT TITLE  [Text Col 1]   ||            HERO SHOT           |
|                                ||         (Full Bleed)           |
|  [Diagram A]   [Text Col 2]    ||                                |
|  [Diagram B]   [Text Col 3]    ||                                |
+--------------------------------++--------------------------------+
```

---

## 社交与编辑性卡片排版 (Social & Editorial Card Layouts)

当需要将建筑项目、图纸及分析结论生成可在社交平台（小红书、微信、B站、抖音）分享的轻量卡片或精致电子画册时，必须严格遵守以下卡片排版系统规范，杜绝“AI 生成味”的廉价排版（如 Tailwind 大色块堆砌、emoji 滥用）。

### 1. 社交卡片黄金尺寸与安全区 (Dimensions & Safety Zones)
* **横版封面 (16:9 / 2.35:1)**：B站/YouTube 封面（1280×720）或微信公众号首图（900×383）。采用**非对称构图**：左侧 2/3 放置特大项目名与副标题，右侧 1/3 放置裁剪精准的透视渲染图。
* **竖版内容卡 (3:4 / 4:5)**：小红书/微信视频号（1080×1440）。
  - *Editorial Artifact 模式*：卡面使用 Parchment 浅底，周围有一圈细淡的虚线或实线分割网格，像一页精致的实体建筑杂志。
  - *Dark Magazine Cover 模式*：深色背景（`#141413`），中心放大项目名或单张夜景渲染，配以单个亮红色（Terracotta）强调词。
  - *Flomo Note Card (便签手记) 模式*：深色背景（`#1e1e1e` 或 `#141413`），非常适合分享简短想法、书签链接、设计随笔或工具清单。视觉构成包括：
    * **左上角**：Display Quote Mark 装饰性双引号（色号 `#ebd5b3` 或 `--tc`）。
    * **右上角**：署名与日期（Mono 字体，`font-size: 12px`, 色号 `#87867f` / `--sg`）。
    * **正文部**：大标题（色号 `#ebd5b3`）与内容列表/超链接（蓝色 `#58a6ff` 或单色 `#faf9f5`）。
    * **左下角**：MEMOS/DAYS 计数统计元信息（Mono 字体全大写，`font-size: 11px`，字间距 `0.05em`，色号 `#87867f`）。
    * **右下角**：微型像素贡献网格（Contribution Grid SVG，暗灰色背景配合淡绿色活跃格子），增加“知识沉淀”的视觉质感。
    * **中底端**：极浅浮水印品牌签名（`opacity: 0.15`）。
* **抖音/故事竖屏安全区 (9:16 - 1080×1920)**：
  - 顶部 `14%`：只放置品牌 Logo / 章节 Kicker，不得放关键正文。
  - 中部 `44% - 52%`：主视线区域，放置核心大字标题。
  - 底部 `20%` & 右侧 `15%`：避让平台交互按钮和点赞区，保持空白或纯色过渡。

### 2. 视觉双轨系统 (Visual Dual-Track System)
每套社交卡片必须严格继承且不混用以下两种调性之一：
* **电子杂志风 (Editorial × E-ink)**：宋体/衬线体 display 标题 + 稳重无衬线/等宽 body 体，搭配暖白/墨色/纸本底色（Kraft / Dune / Ink Classic）。底色上方必须叠有**纸张纹理（Paper Grain）或 WebGL 墨水渲染动效层**，丰富图面细节，适合叙事、设计随笔、手绘及人文调性。
* **瑞士国际主义风 (Swiss International)**：Grotesque 无衬线体（大字号特轻/特细以防笨重，小标注使用 Mono 字体），极其严苛的网格线左对齐与 0.8px 网格线。大色块间使用高饱和度单一锚点色（如 IKB 蓝、柠檬黄、安全橙），强调数据指标和功能框架。

### 3. 公众号双封面系统 (WeChat Paired Cover System)
* **联合设计预览**：微信公众号封面必须产出 `21:9` 主封面 + `1:1` 辅助封面配对（在同一个 HTML 中渲染预览）。
* **独立排版原则**：**禁止**直接将 21:9 封面强行裁剪为 1:1。21:9 封面应以主副标题及视觉透视图为核心；1:1 封面则采用大号文字排版，去除小字副标题，默认不加插图，确保缩略图状态下的极端易读性。

### 4. 3:4 竖卡填充密度 (3:4 Portrait Density Rules)
* **必须吃满画布**：社交卡片（3:4 竖版）的内容（文字 + 配图 + 数据指标）在垂直方向必须覆盖 **$\ge 75\%$** 的画布高度。
* **留白纪律**：禁止使用 `<div style="flex: 1"></div>` 上下夹击强行将内容压缩在中段。任何超过 15% 画布高度的纯空白条带必须提供留白理由（如：大图自带的呼吸留白、单行金句/宣言的极简排版、或设计好的页眉页脚 whitespace 控制）。

### 5. 配图筛选与真实版权溯源 (Web-Sourced Images & Provenance)
* **真实媒介优先**：优先向用户索取真实照片、截图。当必须采用网络配图时，优先从免版权或署名图库检索：Pexels（适合国风/中文特定场景） $\rightarrow$ Unsplash（适合生活方式/质感插图） $\rightarrow$ Flickr CC（通过 `license=2,3,4,5,6,9` 参数检索具象纪实摄影）。
* **落盘溯源纪律**：网络拉取的图片必须在任务目录的 `assets/SOURCES.md` 中以 `文件名 ← 原 URL` 形式落盘存档。生成卡片时，如用户确认需要，须在卡片角落标注微型 Mono 字体的来源（如 "Photo · Pexels · @author"）。

### 6. SVG 矢量排版工艺系统 (SVG Typography & Ornaments)
SVG 不是插图工具，而是**数字版的印刷版刻工艺**。SVG 元素需满足 CSS 无法实现的需求，且整体视觉面积占比不得超过内容区的 `15%`。

* **类型 A：对称排版装饰器 (Typographic Ornament)**
  - 用途：替代平庸的 CSS 细实线，用于分节、段落过渡。
  - 规范：左右轴对称构图，中心使用小菱形或双圆节点（色号 `#c96442`），两侧发丝细线（线宽 ≤ 0.8px，色号 `#b0aea5`）。
* **类型 B：大号引言符 (Display Quote Mark)**
  - 用途：在金句、设计宣言或项目概况的背景底层置入半透明巨型引号。
  - 规范：使用 SVG `<text>` 渲染 Georgia 字体，字号 `70px - 100px`，透明度 `0.07 - 0.12`，绝对定位在文字块左上角，`z-index: 0`。
* **类型 C：图案底纹纹理 (Pattern Texture)**
  - 用途：为技术指标区块、摘要列制造纸质和活字印刷网点纹理。
  - 规范：利用 `<pattern>` 绘制 `6px - 10px` 的网点（`circle`）或网格细线，颜色为 `#c96442`，透明度控制在 `0.05 - 0.08` 之间，隐约可见即可。
* **类型 D：嵌入式数据可视化 (Embedded Data Viz)**
  - 用途：展示建筑技术指标（如碳排放、绿化率、出让面积比例）。
  - 规范：折线图（`<polyline>`）或进度条（`<line>`）通过 `stroke-dasharray` 增加淡入动画。柱状图（`<rect>`）边缘必须带 `rx="1"` 轻微圆角，正向数据用 Terracotta，辅助数据用 Stone-Gray。**禁止使用 3D 柱体或彩色饼图**。

---

## 网页到印刷排版 (Web-to-Print & CSS Paged Media)

在制作作品集或画册 PDF 时，直接使用 HTML+CSS 并配合 Paged Media 渲染引擎（如 WeasyPrint 或 paged.js）是一个高度敏捷的系统方案。相比传统 InDesign，它支持数据 reflow 与自动化模板排版。

### 1. 页面几何尺寸与装订边距 (Page Geometry & Margins)
利用 `@page` 控制物理纸张大小，并用 `:left` 和 `:right` 选择器控制不对称的内外侧边距（Inside/Outside Margins），为装订预留安全空间：
```css
:root {
    --inside-margin: 0.75in;  /* 靠近书脊/装订线的一侧，边距加宽防止图文被卷入 */
    --outside-margin: 0.5in;  /* 靠外一侧边距 */
}

@page {
    size: A4 landscape;       /* 建筑作品集常用横版 A4 */
    margin-top: 0.7in;
    margin-bottom: 0.7in;
}

@page :left {
    margin-left: var(--outside-margin);
    margin-right: var(--inside-margin);
    @top-left {
        content: "PROJECT PORTFOLIO";
        font-family: "Inter", sans-serif;
        font-size: 8.5pt;
        color: #666;
    }
}

@page :right {
    margin-left: var(--inside-margin);
    margin-right: var(--outside-margin);
    @top-right {
        content: counter(page);  /* 自动页码计数 */
        font-family: "Jost", sans-serif;
        font-size: 9pt;
    }
}
```

### 2. 章节首页页眉遮挡 Hack (Suppressing Header on Chapter Start)
当章节首页使用大标题时，通常需要隐藏页眉以保持画面干净。由于纯 CSS 缺乏跨页状态条件判断，可以通过为章节标题设置伪元素，生成白色背景色块向上“物理遮挡”页眉：
```css
h2.chapter-title {
    position: relative;
    break-before: page;       /* 强制该章节在新页开始 */
}

/* 用白色区域物理遮盖上方的页眉区域 */
h2.chapter-title::before {
    content: '';
    position: absolute;
    top: -1in;                /* 负偏置覆盖到页空页眉区域 */
    left: 0;
    width: 100%;
    height: 1.8in;
    background-color: white;  
    z-index: 10;              /* 确保在页眉层级之上 */
}

/* 降低页眉的 z-index 确保其能被遮盖 */
@page :left { @top-left { z-index: -1; } }
@page :right { @top-right { z-index: -1; } }
```

### 3. 段落微排版控制 (Micro-Typography)
* **避头尾与防单行 (Widows & Orphans)**：
  - `orphans: 2;`：每页底部至少保留段落的 2 行，防止孤立的段落首行留在上一页。
  - `widows: 2;`：每页顶部至少保留段落的 2 行，防止段落的最后一句话单独掉入下一页页首。
* **自动折行与连字符 (Auto-Hyphenation)**：
  - 必须在 HTML 根节点设置正确的语言属性（如 `<html lang="en-us">`），连字符字典才会生效。
  - 样式声明：`body { hyphens: auto; hyphenate-limit-chars: 6 3 2; }`（控制单词折行的字数阈值），使两端对齐的文本边缘更自然平滑。
* **防单词悬挂 (Preventing Runts)**：
  - 在 HTML 中，使用非换行空格（`&nbsp;`）替换段落中最后两个单词之间的普通空格，确保最后一行至少有 2 个单词，避免段底出现孤立单词。

---

## AI 资产渲染与品牌一致性管线 (AI Asset Rendering & Brand Consistency Pipeline)

在混合使用 AI 渲染图像、视频与动态字形图层时，必须遵循严苛的管线控制，以确保文字可读性与品牌视觉的一致性，防止生成图像中的文本或标识发生漂移。

### 1. 文字避让区构图 (Text Zone Composition)
* **不要**在生成图像后才试图通过描边、阴影或半透明蒙版来强行提高文字可读性。在生成图画前，必须**将 1/3 的画面空间设计为避让区（Text Zone）**。
* **构图避让区划分**：每一幅画面需声明其避让的 1/3 区域（左侧、右侧或底部），并指定明确的**自然对比源**以控制色彩亮度。
  - **暗色避让区（配白色文字）**：提示词中指定具体的自然光影结构，例如：“the left third of frame is in deep shadow from the architectural overhang, near-black”（左侧 1/3 为建筑阴角深色投影）或“dark polished concrete ground fills the bottom third”（底部 1/3 为深色抛光混凝土路面）。
  - **亮色避让区（配深色文字）**：例如：“bright overcast sky fills the upper-left third”（左上 1/3 为明亮的阴天天空）。
* **防干扰保护性条款 (Preservation Clause)**：在向 Veo 或 Image 2 发送提示词时，必须显式限制生成模型在避让区中添加细节或运动。
  - *模板*：“The [left/right/bottom] third of frame is [contrast source]. This area stays dark and empty throughout the shot — no light creep, no objects entering, and no motion in this zone.”

### 2. 锁定品牌一致性 (Locked Brand Identity)
为了在不同透视效果图、展板及 mockups 中维持标志/字形完全一致，禁止让 AI 自由绘制 logo。应采用**两步锁定管线**：
* **步骤 A：建立 canonical 标志底片**
  - **SVG 转 PNG（首选）**：使用代码绘制精准的 SVG 标志（标题 + icon），并在渲染端导出为高分辨率 PNG（在 headless 环境下，避免 `Helvetica` 降级为圆角 `Noto Sans`/`Calibri` 的 Slop 效应，必须指定 **`Liberation Sans`** 或嵌入的品牌真字体）。
  - **GPT Image 2 单色标志板**：在平面纯色背景上生成标志板，挑出字形与间距最完美的一张，将其 PNG 固化为 master 底片。
* **步骤 B：在后续场景生成中强制引用 (inputImages)**
  - 将 canonical 标志 PNG 作为 `inputImages` / 参考图传入所有的场景渲染任务。
  - 提示词中附加**重现约束命令**：*“Reproduce the provided brand logo artwork EXACTLY as shown — same letterforms, spacing and symbol; do not redraw, restyle, translate or re-letter it. Place it as a printed/applied graphic in the scene.”*
* **文字锁定品牌包 (Brand Kit)**：图像模型对十六进制 Hex 色值不敏感，必须在每个提示词末尾添加一行描述性 Brand Kit：描述 5 个代表品牌的色彩字面名（如 "fresh spring-leaf green, deep evergreen ink, warm off-white, with marigold-yellow accents"），并附带指令 `Spell every word exactly; no invented or garbled text, no extra logos.`。

### 3. 字体渲染降级与光学对齐 (Font Fallback & Optical Alignment)
* **无头渲染降级防护**：在 Puppeteer/WeasyPrint 等无头 Chrome 浏览器中，默认 `sans-serif` 会降级为 `Noto Sans CJK` 等圆角字形。如果需要经典的 Helvetica 视觉效果，必须加载 **`Liberation Sans`** 或配置 `@font-face` 嵌入本地真字体文件。
* **运行时光学对齐 JS 纠偏**：大字号标题的墨迹边界（Ink Boundary）由于字形前轴测间距（Side-bearing）而不会与网格绝对重合。在 `document.fonts.ready` 后，通过 canvas 测量 `actualBoundingBoxLeft`，自动计算并向左微调 `margin-left`（如 `el.style.marginLeft = -abl + 'px'`），确保视线上文字的墨迹外轮廓完美咬合在网格线上。

---

## 极简纸本排版与数据文档规范 (Warm Paper & Minimalist Document Design)

当排版长篇技术报告、学术性白皮书、项目策划案或印刷级作品集文本时，必须遵循严谨的“纸本感”版式规范，确保阅读的宁静与客观。

### 1. 纸本视觉基调 (The Kami Stance)
* **画布色底**：基色采用温润的羊皮纸/温和白（`#F4F1EA` 或 `#F3F0E8`），而非刺眼的纯白 `#FFFFFF`，以提供舒适的阅读底纹。
* **文字层级与衬线主导**：主标题与陈述性文字使用高雅的衬线体/宋体（英文 Charter / Georgia，中文 TsangerJinKai02 / 思源宋体），其余正文配以安静的无衬线体/黑体。
* **字号比例**：遵循“双字号法则”，Display 大标题的字号通常为正文字号的 2 倍。大标题字重需偏轻（Light/Medium），严禁为了凸显存在感而加粗大字号标题。

### 2. 对齐与微间距纪律
* **两端排布**：正文必须使用**左对齐，右侧自然流出 (Flush-left, ragged-right)**。严禁使用强制两端对齐（Justified），避免在非英文或中英混排下产生极不自然的单词间距拉断。
* **缺图/无图的备用设计**：如果项目缺乏真实的配图或截图，直接在 HTML 模板中注释掉图片容器，改走高雅的**纯文字排版**与大字号文字块呼吸留白，决不允许用低质网络免版权插画（如扁平几何、彩色渐变块）作为无意义的装饰。

### 3. 参数化沟通 (Feedback Protocol)
当针对页面进行视觉微调沟通时，禁止使用“不够专业/太挤/太松/不好看”等模糊主观词汇，必须结合参数化属性进行定量表达：
* 调整行高（当前行高与目标行高，如 `1.25` $\rightarrow$ `1.4`）、边距（Padding/Margin）、字体族、或灰度对比。

---

## 教学式图板与矢量分析图语法 (Educational Boards & Schematic Diagram Grammar)

在展板、幻灯片或分析图册中，分析图纸（Architecture Diagrams / Flowcharts）必须承担**客观叙事**的职能，拒绝成为无语义的“色块摆设”。

### 1. 画板优先于卡片 (Canvas Before Card)
每个分析图面是一个固定比例的**独立画板（Artboard）**，而非装饰性的卡片堆叠：
* 四周必须保留安全避让带（Safe Area）。
* 每个画板只承载**一个核心教学模型/系统流程**。
* 严禁无意义的卡片嵌套与层层投影叠放。背景应当比所有内容都安静。

### 2. 语义化元素与线条分级 (Semantic Elements & Wire Hierarchy)
分析图中的每种线和框必须在逻辑上有所指代：
* **节点 (Node)**：指代概念、执行步骤、核心组件或断点。节点标签文字必须短小精炼（中文 $\le 12$ 字，英文 $\le 4$ 词）。
* **连线 (Edge)**：指代依赖关系、因果流动、状态转化或反馈环。
* **分组 (Group)**：指代系统边界、架构分层或分类对比。
* **线条粗细分级**：结构边界线控制在 `1-2px`；常规关系连线 `2-3px`；高亮/焦点流动线 `3-4px`。箭头严禁穿越或碰撞文本标签。

### 3. 矢量图表语法的自动路由 (Schematic Diagram Auto-Selection)
分析数据的图表类型，必须基于数据结构进行精准路由，严禁凭主观喜好随意挑选：

| 数据结构与图面叙事 (Data / Logic Shape) | 图表语法路由 (Chart / Diagram Type) |
|---|---|
| 包含开盘/收盘/最高/最低的时序指标、日度股价 | **K 线图 (Candlestick)** |
| 包含一系列有增有减的输入贡献度，最终求和汇总（如收入 bridge 拆解） | **瀑布图 (Waterfall)** |
| 单一系列且各项占比相加为 100%，分类项数 $\le 6$ | **环形图 (Donut Chart)** |
| 单一系列且各项占比相加为 100%，分类项数 $\ge 7$ | **横向柱状图 (Horizontal Bar Chart)** |
| 跨越时间轴（月、季、年）的两个或多个趋势对比 | **折线图 (Line Chart)** |
| 包含时序概念但变化以绝对数为主，无高频波动率 | **纵向柱状图 (Bar Chart)** |
| 两个或三个分类集合之间的交集与重合度 | **维恩图 (Venn Diagram)** |
| 具有 2×2 战略定位、优先级象限或双轴权衡 | **2x2 象限图 (Quadrant / Matrix)** |
| 具有树状分支或多层级深入（层级 $\ge 2$）的逻辑 | **树形拓扑图 (Tree / Hierarchy)** |
| 包含复杂因果决策路径与条件分支的流程 | **流程图 (Flowchart)** |
| 跨团队协作、跨系统交互，包含 $\ge 3$ 个明确的执行主体 | **泳道图 (Swimlane)** |

---

## 常见设计缺陷与自查 (Anti-Patterns)

| 缺陷 (Anti-Pattern) | 现象 (Symptom) | 修正方案 (Fix) |
|---|---|---|
| **拼贴画效应 (Collagism)** | 效果图和剖面图交错重叠，边缘不齐 | 严格使用 Subgrid，每个图框的角点必须落在网格交叉点上。 |
| **彩虹图表 (Rainbow Diagrams)** | 分析图用红黄蓝绿等多种颜色画流线和功能分区 | 将所有背景分析图转为灰度，仅用一种提取的核心色表达关键流线/功能。 |
| **标题轰炸 (Title Bombing)** | 图名、小标题字号多达 5-6 种，粗细不一 | 贯彻“双字号规则”(Two-Size Rule)，利用空间留白 and 字重对比产生层级。 |
| **文字压图 (Text Overlap)** | 将大段文字或指标直接叠放在渲染图暗部 | 文字一律移出效果图范围，使用干净的纸色底。如必须压图，采用带 opacity 遮罩的偏侧小气泡。 |
| **强制拉伸 (Aspect Ratio Distortion)**| 为了对齐网格将平面图或透视图的长宽比破坏拉伸 | 绝对禁止扭曲图纸。保持原图比例，通过调整周围留白 (Margin/Padding) 使其边缘与网格对齐。 |
| **文字易读性妥协 (Outline Slop)**| 使用多层投影、粗描边或大面积黑 scrim 挽救文字可读性 | 贯彻“文字避让区构图”，生成图前划分 1/3 自然对比区，仅配微弱单层阴影保险。 |
| **标志标识漂移 (Logo Drift)**| 在不同的 OOH/展板场景中，品牌标志字形与符号发生微调变形 | 先建立唯一的 SVG/PNG Canonical Logo Plate，将其作为 reference inputImages 喂给模型，并加 strict copy 命令。 |
| **无头环境字体畸变 (Fallback Distortion)**| 网页转 PDF 或渲染图时，Helvetica 缩略字形变成圆角 Calibri / 微软雅黑 | 无头环境指定 `Liberation Sans` 或加载本地 TTF，禁用裸 `sans-serif` 声明。 |
| **字距塌陷 (Tracking Collapse)** | 全大写图名/指标栏 letter-spacing 为 0 或负值，小字号挤成一团 | 全大写/Mono 标注给 `0.04em–0.12em` tracking；正文勿负 tracking；缩略图/手机预览再查一次。 |
| **假氛围 Hero (Atmosphere Slop)** | Tier 1 用「现代建筑抽象氛围」或无关 stock 顶替方案真实渲染/现场 | Hero 必须是本项目方案图/实景；无图则改纯文字高雅排版，禁止假图凑数。 |
| **装饰性 Human Touch 失败** | 加随机渐变、emoji、无语义装饰线冒充「细节」 | 只保留 1–2 处**项目相关**细节（材料小图、构造节点、场地专属图注）。 |

---

## 成图渲染评图循环（Render-then-Critique Vision Loop）

> 移植自 ckw-design-skill `design-spatial` 的「模型看不到自己画的像素」命题，改写为建筑展板语境。这是第五节 Verify 的**强制前置**——落版后、跑 Meng-style 皮面前，必须先 render 成图、用独立 judge 评图。

### 1. 为什么必须 render
展板以 HTML/CSS（或 SVG）产出，模型生成的是 token 流不是像素——它看不到碰撞、边切线（edge tangent）、失衡、错位间距。它会写出压住 Hero 的标题而毫无察觉。**渲染成图，评的是图，不是代码，更不是自评。**

### 2. 流程
1. 起静态服务（`python3 -m http.server` 或 `npx serve`），用 Playwright headless 截图，**多宽度**（桌面 + 窄屏 ~390px / ~1024px）。
2. **独立 judge 评图**：用一个**没写过这版**的 subagent 当裁判，命它专门找「错」——碰撞、边切线、参差对齐、失衡、无清晰焦点、某些宽度崩。
3. 修 → 重渲 → 再评，直到 judge 找不到阻断级问题。
4. **自动度量兜底（一键）**：用 `scripts/capture_rects.py` 直接吃 HTML 展板，Playwright headless 渲染 → 导出元素框 `rects.json`（坐标/色/底色/kind/large，与 audit 完全兼容）+ 裁到展板本体的截图 PNG，再链式 `--run-audit` 一把出全量报告 JSON + 标注 SVG 叠加图。零手工导矩形。
   ```bash
   # 一键：抓框 + 截图 + 跑 audit 出全量报告（含 SVG 标注）
   python3 scripts/capture_rects.py --html board.html --out rects.json \
       --screenshot board.png --run-audit --audit-out report.json --overlay overlay.svg
   # 指定展板本体选择器（默认 .board / [data-board]；无匹配回退整页）
   # 加 --width 1080 --height 1440 可固定海报尺寸
   ```
   `audit_board.py` 算：全分辨率墨密度重心（平衡 SIGNAL，x=0.50/y≈0.46，接受 ±0.03/±0.04）+ 矩形 GATES（碰撞 ≥12% 交叠、WCAG 对比）+ 对齐/间距 SIGNAL；碰撞检查跳过父子嵌套（只留同级部分交叠），底色相同的冗余 wrapper 在抓取端去重。纯标准库零依赖，任意机器可跑；`capture_rects.py` 仅额外需要 `pip install playwright && playwright install chromium`。

### 3. 可测量视觉平衡（不靠 VLM 猜）
视觉重量 = 面积 × 墨密度（同面积不同重：实心黑标题重，灰/ASCII/亮图轻，正文稀疏）。重心目标：光学中心 `x = 0.50`，`y ≈ 0.46`（略高，几何正中会读成下坠）。
- **接受准则**：`|centroid_x − 0.50| < 0.03` 且 `|centroid_y − 0.46| < 0.04`，左右/上下不平衡度低。
- **修复靠 see-saw**：加重对立元素 > 拉大对立面积 > 把重物内移（缩短力臂）> 缩小重物（最后手段）。

### 4. 闸门 vs 信号纪律（最关键，防过度纠正）
| 类别 | 检查 | 性质 |
|---|---|---|
| **GATES（正确性）** | 碰撞 ≥12% 交叠、对比 WCAG（见色彩 §3）、横向溢出 `scrollWidth−clientWidth = 0`、tap ≥44×44 | 事实缺陷，**可硬挡** |
| **SIGNALS（约定）** | 平衡、对齐节律、间距节奏（CoV） | 对称/规整美学，**不可为追分而过度纠正** |

- **GATES 是必要非充分**：全过只说明过了确定性地板，不代表好看；门后仍需 §2 的 fresh-eyes 评判与品牌契合。
- **SIGNALS 是指针不是裁决**：刻意的偏离对称、刻意重叠、表现性节奏，往往是版面上最好的东西。信号与有趣选择冲突时，**有趣选择通常赢**——别把展板「修」成平均。
- **绝不一票未看就改**：flag 是指向「去看」的指针；看了标注图再决定。

### 5. 与 Meng-style 的分工
本循环 = 成图前强制 render 评图（结构 / 碰撞 / 平衡 / 对比）；Meng-style = 成图后反 AI 味皮面（字距 / 伪影 / human detail）。**先过本循环，再过 Meng-style**；本循环 judge 找不到阻断级问题，才进 Meng-style。

---

## Meng-style Board Polish（成图核校增强层）

> 原则：网格与三套视觉语言是主干；本节只补 **最后 10% 反 AI 味**。灵感移植自 Meng To 落地页 critique（字距、真实图、伪影、human detail），已改写为建筑展板/作品集/社交卡语境。  
> **不引入**落地页专属项：CTA 文案、hover 微交互、SaaS marketing 套路。社交 HTML 卡允许极轻量 reveal/hover，印刷展板一律忽略。

### 1. 修复优先级（高 → 低）

落版后按此顺序改，禁止先抠边角装饰：

1. **Typography & tracking** — 字距、字重、全大写标注、缩略可读性  
2. **Real project imagery** — Hero/关键图是否为本方案真实资产  
3. **Image artifacts** — AI 渲染伪影、比例、光影、Logo 漂移  
4. **Hierarchy & air** — Tier 占比、空气泡、Flowline  
5. **Project-specific human detail** — 1–2 处方案专属细节  
6. **Medium fitness** — 印刷灰阶 / 3:4 密度 / 9:16 安全区

### 2. 核校条目（Board 版）

| 维度 | 通过标准 | 常见失败 → 修正 |
|---|---|---|
| **Typography & letter-spacing** | 全篇 ≤ 2 字号；Display 轻字重；全大写/Mono 有适度 tracking；小字在 A0 退远与手机缩略均可读 | 正文负 tracking、指标栏挤成一坨 → 加大 tracking 或字号，减字数 |
| **Real references** | Tier 1 为本项目渲染/实景/图纸；网络图已溯源 `assets/SOURCES.md` | 假氛围/无关 stock → 换真图或删图走纯文字 |
| **Image refinement** | 无畸形结构、无乱码招牌、无漂浮 Logo；光影方向与相邻图一致；不拉伸图纸 | AI 伪影/比例扭曲 → 重渲或裁切替换，禁止 `object-fit: fill` 硬拉 |
| **Narrative specificity** | 说明文字含场地/体量/策略等项目名词，禁止「现代、灵动、和谐」空话 | 空话段落 → 改写为可验证的设计陈述或删短 |
| **Human detail** | 恰好 1–2 处方案专属细节（材料、节点、场地注记），服务叙事 | 0 处像模板；3+ 处像拼贴 → 收敛到 1–2 |
| **Medium quality** | 展板：退 2m 灰阶层级清晰；社交卡：3:4 垂直覆盖 ≥75%；9:16 避让平台 UI | 中段空洞或安全区撞按钮 → 按媒介密度规则重排 |

### 3. 交付输出格式（强制）

核校或交付前，必须用以下格式汇报（可审计、可对比）：

```text
Board readiness: [Ready / Needs polish / Not ready]

Top fixes:
1. [Issue] — [specific correction]
2. [Issue] — [specific correction]
3. [Issue] — [specific correction]

Checklist:
- Typography & letter-spacing: [pass/fail + note]
- Real project imagery: [pass/fail + note]
- Image refinement / artifacts: [pass/fail + note]
- Narrative specificity: [pass/fail + note]
- Human detail (1–2 project-specific): [pass/fail + note]
- Medium fitness (print / social / PDF): [pass/fail + note]
```

*Ready*：六项全 pass，可提交/出图。  
*Needs polish*：有 fail 但结构骨架正确，列 Top fixes 后可修。  
*Not ready*：网格未定、无 Hero、视觉语言混用或假图占 Tier 1 —— 退回第四步落版，不修皮。

### 4. 与主干的分工

| 层 | 负责 | 不负责 |
|---|---|---|
| **主干**（网格 / 三套语言 / Tier / 五步流程） | 结构、叙事动线、调性认领 | 细部字距与伪影清单 |
| **Meng-style polish**（本节） | 成图后反 AI 味、readiness 判决 | 改网格分栏、换视觉语言、做 3D 渲染 |

---

## 使用边界 / Scope Boundary

| 属于本 Skill (IN) | 不属于本 Skill (OUT) |
|---|---|
| 展板/作品集/卡片版式、网格、字体、配色 | 3D 渲染生成 → `archviz-3d` / `archviz-sketch` |
| 分析图排版与图表类型路由 | 纯信息图表 HTML 生成 → `archviz-diagram` |
| 社交卡片/印刷 PDF/CSS Paged Media | 网站前端工程实现 → `frontend-design` |
| AI 渲染品牌一致性管线 | 代码级 SVG 动画 → `threejs-*` |
| — | 通用 Web-UI 装饰（重投影 / 材质阴影 / 渐变网格 / SEO / 爬虫）→ 反 Swiss 网格，已显式排除 |

## 执行前检查清单 (Pre-Flight Checklist)

### A. 落版前（结构骨架）

全部 ✓ 再进入第四步 Layout：

```
[ ] 1. 确认输出媒介：A0 展板 / A4 作品集 / 社交卡片 / PDF 画册
[ ] 2. 已认领三套视觉语言之一：静纸 / 实证 / 图桥（不混用）
[ ] 3. 锁定调色板与字体方案，且与项目性格一致
[ ] 4. 资产清单已分级：Tier 1 焦点图 ≥ 35% 版面占比
[ ] 5. 网格已定：分栏数 + 网格间距 + 外留白均已确定
[ ] 6. 对齐基准：所有图纸顶部/底部已锁定到 Flowline
[ ] 7. 安全区：渲染图/效果图周围 ≥ 1 个网格单元留白
[ ] 8. 字号控制：全篇 ≤ 2 种字号，已确认字重层级
[ ] 9. 反模式自检：彩虹图表 / 标题轰炸 / 文字压图 / 标志漂移 / 强制拉伸
[ ] 10. 导出格式已确认：PNG / SVG / PDF / HTML 卡片
```

### B. 成图后（Meng-style Board Polish）

全部 ✓ 且 `Board readiness` ≠ Not ready 再交付：

```
[ ] 11. 字距：全大写/Mono 标注 tracking 合适；正文无负 tracking；退远/缩略可读
[ ] 12. 真图：Tier 1 为本项目资产，非假氛围；网络图已溯源
[ ] 13. 伪影：结构/招牌/Logo/光影无 AI 破绽；图纸未拉伸
[ ] 14. 叙事：说明含场地/体量/策略名词，无空话堆砌
[ ] 15. Human detail：恰好 1–2 处项目专属细节（非随机装饰）
[ ] 16. 媒介：印刷灰阶 / 3:4≥75% / 9:16 安全区 已按输出媒介核过
[ ] 17. 已输出 Board readiness 块（Ready / Needs polish / Not ready + Top fixes）
[ ] 18. HTML 卡无溢出：窄屏（≤390px / ~1024px）实测 `scrollWidth − clientWidth = 0`；媒体盒 `aspect-ratio` 预留防 CLS（仅社交/网页卡适用，印刷 PDF 忽略）
```

---

## 交叉优化：Layout × Diagram (Board with Charts)

**功能：** 将 archviz-diagram 的图表嵌入到 archviz-layout 的版面中

**脚本：** `scripts/render_board_with_charts.py`

**支持模板：**
- `a0-vertical` — A0 竖向展板
- `a3-landscape` — A3 横向作品集
- `social-3-4` — 3:4 社交卡片

**支持视觉语言：**
- `still-paper` — 静纸风格
- `signal-proof` — 实证风格
- `bridge-canvas` — 图桥风格

**数据格式：**
```json
{
  "title": "Chart Title",
  "categories": ["A", "B", "C"],
  "values": [10, 20, 15],
  "labels": ["Label A", "Label B", "Label C"]
}
```

**渲染命令：**
```bash
python3 scripts/render_board_with_charts.py \
  --template a0-vertical \
  --language still-paper \
  --title "Project Title" \
  --charts chart1.json chart2.json \
  --outdir ./output \
  --basename board-name
```

**参数：**
- `--template`: 版面模板
- `--language`: 视觉语言
- `--title`: 展板标题
- `--charts`: 图表 JSON 文件（可多个）

**输出：**
- `board-name.png` — 完整展板

**版面结构：**
- Tier 1: 标题区（35%）
- Tier 4: 分析图区（图表嵌入）
- Footer: 生成信息

---

| 场景 | 大标题 (Display) | 正文 / 标注 (Body) | 图名标注 (Caption) |
|---|---|---|---|
| A0 展板 (超大对比) | `72pt` / Light | `10pt` / Medium | `7pt` / Regular |
| A3 作品集 (雅致) | `24pt` / Light | `9pt` / Regular | `7pt` / Regular |
| 社交卡片 (3:4) | `36pt` / Medium | `13pt` / Regular | `10pt` / Mono |
| 公众号封面 (21:9) | `48pt` / Light | — | `10pt` / Mono |

> **规则**：Display vs Body 比例维持在 **2:1 到 7:1**；Body vs Caption 比例维持在 **1.2:1 到 1.5:1**。Display 字重一律轻，严禁粗体标题。

---
## 版本变更（Changelog）

### v1.1.0 — 全量补强（2026-09-24）
**来源**：ckw-design-skill（`design-spatial` / `design-system` / `design-thinking`，MIT）、martinavila `skills/agent-skills/web-design` 网格配方（agency-grid-layout-minimal / image-first-grid-layout）。

**新增 / 增强**
1. **渲染评图循环（Render-then-Critique）**：落版后强制 render 成图、独立 judge 评图（非自评）；可测量视觉平衡（墨密度重心 x=0.50 / y≈0.46，接受 ±0.03/±0.04）；GATES vs SIGNALS 纪律，防过度纠正成平均。
2. **对比度闸门**：WCAG 2 作合规地板（正文 4.5:1 / 大字 3:1）+ APCA 作感知设计判据，落版实测数值。
3. **网格导轨与构图范式**：结构导轨（外框轨 / 中轴导引 / 角标）、图为主舞台、底部锚定 Hero、服务行列表。
4. **字体层级清晰铁律**：眯眼测试 + 数据 `tabular-nums` 等宽对齐；禁止 Mono 当装饰微标签（trend-slop）。
5. **核心设计纪律 4–6**：评审基线（Name-on-It Bar）、留白即结构、冲击留给标点。
6. **Pre-Flight B-18**：HTML 卡窄屏无横向溢出闸门 + `aspect-ratio` 防 CLS。
7. **成图审计脚本** `scripts/audit_board.py`（零依赖纯标准库）：渲染截图 → 全分辨率墨密度重心（平衡 SIGNAL）+ 粗粒度局部对比 + 矩形模式（碰撞/对齐/间距/ WCAG 对比 GATES）+ 标注 SVG 叠加。把本循环的"可测量"从口头变成可跑工具。

### v1.1.1 — 一键抓取 + 审计精度修正（2026-09-24）
**新增**
1. **`scripts/capture_rects.py`（Playwright）**：HTML 展板 → 一键导出元素框 `rects.json` + 裁到展板本体的截图 PNG，并支持 `--run-audit` 链式出全量报告 + 标注 SVG。省去人工从 devtools 导矩形（`audit_board.py` 仍零依赖）。
2. **`--board` 展板裁剪**：截图只取 `.board` / `[data-board]` 本体并做坐标偏移，平衡/对比只在展板内衡量，不被画布留白带偏。
3. **示例展板 `examples/board-sample.html`（still-paper 干净样本）与 `examples/board-stress.html`（触发器验证夹具，埋低对比/交叠/错位三类问题）**。

**审计精度修正（audit_board.py）**
- 碰撞 GATE 跳过父子嵌套（一个完整包住另一个），只留同级部分交叠 → 消除容器包子文本的大规模误报。
- 抓取端 dedup 仅删除「底色相同且被覆盖 ≥92%」的冗余 wrapper，保留有独立底色的卡片/列/图版（hero/aside/plate/列等）。

**显式未采纳（Deliberately Excluded）**
- 通用 Web-UI 装饰套路（重投影 / 材质阴影 / 渐变网格 / 玻璃拟态 / SEO / 爬虫）：与 Swiss 极简网格相悖，已在「使用边界」OUT 列排除。
- X 帖子（@kail_designs）所列 `beautiful-shadows` / `apple-design` / `frontend-design` 等通用 Web-UI skill：经判定为通用产品界面技能，与建筑展板垂直领域错位，不能用于全量优化本系列（详见会话判定）。其真正可迁移的 2–3 点（评图流程 / 极简纪律 / 品牌一致）已由 ckw 来源以更严版本覆盖。

---

*“理性的网格是空间叙事的骨架，克制的色谱是视觉高贵的来源。”*
