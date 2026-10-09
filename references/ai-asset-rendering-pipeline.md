# AI 资产渲染与品牌一致性管线 (AI Asset Rendering & Brand Consistency Pipeline)

> 从 `SKILL.md` 原样迁出（2026-10-09 渐进式披露拆分，v1.4.0），**内容逐字未删改**，
> 仅把内部 `###` 标题降一级为 `##`（因为小节标题升为本文 H1）。
> 何时加载：生成 AI 渲染图，且要在图上压文字或放品牌标志时。
> **本文件不需要随 skill 一起加载** —— SKILL.md 里只有一行索引指向它。

## AI 资产渲染与品牌一致性管线 (AI Asset Rendering & Brand Consistency Pipeline)

在混合使用 AI 渲染图像、视频与动态字形图层时，必须遵循严苛的管线控制，以确保文字可读性与品牌视觉的一致性，防止生成图像中的文本或标识发生漂移。

## 1. 文字避让区构图 (Text Zone Composition)
* **不要**在生成图像后才试图通过描边、阴影或半透明蒙版来强行提高文字可读性。在生成图画前，必须**将 1/3 的画面空间设计为避让区（Text Zone）**。
* **构图避让区划分**：每一幅画面需声明其避让的 1/3 区域（左侧、右侧或底部），并指定明确的**自然对比源**以控制色彩亮度。
  - **暗色避让区（配白色文字）**：提示词中指定具体的自然光影结构，例如：“the left third of frame is in deep shadow from the architectural overhang, near-black”（左侧 1/3 为建筑阴角深色投影）或“dark polished concrete ground fills the bottom third”（底部 1/3 为深色抛光混凝土路面）。
  - **亮色避让区（配深色文字）**：例如：“bright overcast sky fills the upper-left third”（左上 1/3 为明亮的阴天天空）。
* **防干扰保护性条款 (Preservation Clause)**：在向 Veo 或 Image 2 发送提示词时，必须显式限制生成模型在避让区中添加细节或运动。
  - *模板*：“The [left/right/bottom] third of frame is [contrast source]. This area stays dark and empty throughout the shot — no light creep, no objects entering, and no motion in this zone.”

## 2. 锁定品牌一致性 (Locked Brand Identity)
为了在不同透视效果图、展板及 mockups 中维持标志/字形完全一致，禁止让 AI 自由绘制 logo。应采用**两步锁定管线**：
* **步骤 A：建立 canonical 标志底片**
  - **SVG 转 PNG（首选）**：使用代码绘制精准的 SVG 标志（标题 + icon），并在渲染端导出为高分辨率 PNG（在 headless 环境下，避免 `Helvetica` 降级为圆角 `Noto Sans`/`Calibri` 的 Slop 效应，必须指定 **`Liberation Sans`** 或嵌入的品牌真字体）。
  - **GPT Image 2 单色标志板**：在平面纯色背景上生成标志板，挑出字形与间距最完美的一张，将其 PNG 固化为 master 底片。
* **步骤 B：在后续场景生成中强制引用 (inputImages)**
  - 将 canonical 标志 PNG 作为 `inputImages` / 参考图传入所有的场景渲染任务。
  - 提示词中附加**重现约束命令**：*“Reproduce the provided brand logo artwork EXACTLY as shown — same letterforms, spacing and symbol; do not redraw, restyle, translate or re-letter it. Place it as a printed/applied graphic in the scene.”*
* **文字锁定品牌包 (Brand Kit)**：图像模型对十六进制 Hex 色值不敏感，必须在每个提示词末尾添加一行描述性 Brand Kit：描述 5 个代表品牌的色彩字面名（如 "fresh spring-leaf green, deep evergreen ink, warm off-white, with marigold-yellow accents"），并附带指令 `Spell every word exactly; no invented or garbled text, no extra logos.`。

## 3. 字体渲染降级与光学对齐 (Font Fallback & Optical Alignment)
* **无头渲染降级防护**：在 Puppeteer/WeasyPrint 等无头 Chrome 浏览器中，默认 `sans-serif` 会降级为 `Noto Sans CJK` 等圆角字形。如果需要经典的 Helvetica 视觉效果，必须加载 **`Liberation Sans`** 或配置 `@font-face` 嵌入本地真字体文件。
* **运行时光学对齐 JS 纠偏**：大字号标题的墨迹边界（Ink Boundary）由于字形前轴测间距（Side-bearing）而不会与网格绝对重合。在 `document.fonts.ready` 后，通过 canvas 测量 `actualBoundingBoxLeft`，自动计算并向左微调 `margin-left`（如 `el.style.marginLeft = -abl + 'px'`），确保视线上文字的墨迹外轮廓完美咬合在网格线上。
