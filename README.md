# Arcviz-Layout (建筑表现与图面设计 Agent Skill)

[![Agent Skill](https://img.shields.io/badge/Agent--Skill-arcviz--layout-blue.svg?style=flat-square)](https://github.com/archsueh/archviz-layout)
[![Supported Agents](https://img.shields.io/badge/Supported--Agents-Claude%20%7C%20Gemini%20%7C%20Codex-orange.svg?style=flat-square)](https://github.com/archsueh/archviz-layout)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://github.com/archsueh/archviz-layout)

`arcviz-layout` 是一个专为 AI 智能体（如 Claude Code, Gemini CLI, Codex 等）设计的建筑学图面排版与视觉设计 Skill。

本 Skill 融汇了**画面叙事（Narrative）**、**技术精度（Precision）**与**视觉美学（Aesthetics）**的系统性规范。它整合了瑞士国际主义字体排印风格（Müller-Brockmann 模块化网格）、维涅里设计法则（Vignelli Canon 视觉层级）以及 Archviz 图像色彩配对系统，旨在让 AI 智能体在排版建筑设计展板（A0/A1 Panels）、个人作品集（Portfolios）、场地分析图纸以及社交卡片时，遵循严谨的理性秩序，杜绝无序拼凑与低质 AI 审美。

---

## 🚀 快速安装 / Installation

### 方式 A：通过 `npx skills` 自动安装 (推荐)
在你的项目根目录下执行：
```bash
npx skills add https://github.com/archsueh/archviz-layout --skill arcviz-layout
```

### 方式 B：手动克隆到全局 Agent 技能目录
```bash
git clone https://github.com/archsueh/archviz-layout.git ~/.agents/skills/arcviz-layout
```

---

## 💡 核心设计纪律 (Core Disciplines)

1. **画面叙事 (Narrative Space)**：图面即空间。展板的阅读路线应当模仿空间游历的叙事逻辑（如“鸟瞰概念 -> 场地分析 -> 主题渲染 -> 空间平立剖 -> 细部构造”），图面排列应有强烈的动线引导（Flowline）。
2. **视觉冲击力 (Visual Power)**：力量来源于**尺度的对比**，而非颜色的繁多。展板上必须存在一个绝对的视觉核心（Hero Shot），与其他辅助图纸形成鲜明的面积比差。
3. **适当性原则 (Appropriateness)**：版式调性必须与建筑项目性格匹配。
   - *粗野主义/工业项目*：刚性灰色表面，大网格，强对比，使用大字重无衬线体。
   - *文化/艺术/住宅项目*：白色或暖纸色表面，宽留白，细网格，配以优雅的衬线体标题。

---

## 🎨 建筑版式三套视觉语言 (Visual Languages)

| 视觉语言 | 适用项目 | 视觉配方 (底色 / 标题 / 强调 / 渲染色调) |
| :--- | :--- | :--- |
| 🌿 **静纸 (Still Paper)**<br>_纸本手作风_ | 文化中心、地标博物馆、住宅设计、城市微更新、景观与乡村规划。 | <ul><li>底色：`#F5F4ED` (暖白色粗糙纸面)</li><li>标题：`YuMincho` / `Georgia` (500中等字重，无粗体)</li><li>强调：`#c96442` (朱砂/红土色)</li><li>分割：极细线条边框 (线宽 ≤ 0.8px)</li><li>渲染：`grade: "duo"` 暖墨双色调</li></ul> |
| ⚡ **实证 (Signal Proof)**<br>_理性技术图风_ | 城市TOD交通枢纽、高新产业园、科学实验室、绿色低碳/可持续性能分析图、剖面大样与构造图纸。 | <ul><li>底色：`#F5F5F4` 或 `#E4E8F0` (冷灰或奶白)</li><li>标题：`Inter` / `Helvetica` (高对比粗黑体)</li><li>强调：`#0039A6` (科技感电蓝色)</li><li>分割：工程蓝图分割线、数据分析图外框使用“VERIFIED/TECHNICAL”印记式标签</li><li>渲染：`grade: "sl-duo"` 冷色调签名</li></ul> |
| 🎬 **图桥 (Bridge Canvas)**<br>_电影表现力风_ | 大型竞赛图纸首图、叙事性强的空间节点表现、大跨度公共空间、夜景/黄昏渲染氛围图。 | <ul><li>底色：`#141413` (纯黑或极深灰色)</li><li>布局：全铺/跨栏无边框大图渲染 (Hero Shot)</li><li>视觉锚定：电影级宽银幕黑边 (Cinematic Black Bars)</li><li>标题：直接浮于大图暗部或大面积黑底中</li><li>渲染：金绿双色调分离 (Teal-Gold Split-Tone)</li></ul> |

---

## 📊 矢量图表语法的自动路由 (Schematic Diagram Auto-Selection)

分析数据的图表类型，必须基于数据结构进行精密路由，严禁凭主观喜好随意挑选：

| 数据结构与图面叙事 (Data / Logic Shape) | 图表语法路由 (Chart / Diagram Type) |
| :--- | :--- |
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

## 🔄 AI 资产渲染与品牌一致性管线

1. **文字避让区构图 (Text Zone Composition)**
   * 在生成效果图/分析图前，必须**将 1/3 的画面空间设计为避让区（Text Zone）**。
   * **暗色避让区（配白色文字）**：提示词中指定具体的自然光影结构，如：`the left third of frame is in deep shadow from the architectural overhang, near-black`。
   * **亮色避让区（配深色文字）**：如：`bright overcast sky fills the upper-left third`。
2. **锁定品牌一致性 (Locked Brand Identity)**
   * **步骤 A**：建立唯一的 SVG/PNG Canonical Logo Plate。
   * **步骤 B**：在后续场景生成中强制引用（作为 `inputImages`），并在 Prompt 中附加重现约束命令：*“Reproduce the provided brand logo artwork EXACTLY as shown...”*
3. **无头环境字体还原与光学对齐**
   * 无头 Chrome (如 Puppeteer/WeasyPrint) 渲染 PDF 时，指定 **`Liberation Sans`** 或配置 `@font-face` 嵌入本地真字体文件，禁用裸 `sans-serif` 声明。

---

## 📋 执行前检查清单 (Pre-Flight Checklist)

执行排图任务前，请逐项确认，全部满足后再落版：

- [ ] **1. 确认输出媒介**：A0 展板 / A4 作品集 / 社交卡片 / PDF 画册。
- [ ] **2. 已认领三套视觉语言之一**：静纸 / 实证 / 图桥。
- [ ] **3. 锁定调色板与字体方案**，且与项目性格一致。
- [ ] **4. 资产清单已分级**：Tier 1 焦点图 $\ge 35\%$ 版面占比。
- [ ] **5. 网格已定**：分栏数 + 网格间距 + 外留白均已确定。
- [ ] **6. 对齐基准**：所有图纸顶部/底部已锁定到 Flowline。
- [ ] **7. 安全区**：渲染图/效果图周围 $\ge 1$ 个网格单元留白。
- [ ] **8. 字号控制**：全篇 $\le 2$ 种字号，已确认字重层级（Display vs Body 比例维持在 2:1 到 7:1）。
- [ ] **9. 反模式自检**：彩虹图表 / 标题轰炸 / 文字压图 / 标志漂移。
- [ ] **10. 确认导出格式**：PNG / SVG / PDF / HTML 卡片。

---

## 🛠️ 使用边界 / Scope Boundary

| 属于本 Skill (IN) | 不属于本 Skill (OUT) |
| :--- | :--- |
| 展板/作品集/卡片版式、网格、字体、配色 | 3D 渲染生成 $\rightarrow$ `archviz-3d` / `archviz-sketch` |
| 分析图排版与图表类型路由 | 纯信息图表 HTML 生成 $\rightarrow$ `archviz` |
| 社交卡片/印刷 PDF/CSS Paged Media | 网站前端工程实现 $\rightarrow$ `frontend-design` |
| AI 渲染品牌一致性管线 | 代码级 SVG 动画 $\rightarrow$ `threejs-*` |

---

## 🔗 相关资源与参考

* 完整的排版规则与技术公式请参阅 [SKILL.md](file:///Users/mac/.agents/skills/arcviz-layout/SKILL.md)。
* 想要深度探讨设计方案？可以使用 `/grill-me` 针对本 Skill 或具体设计进行审计。

## 📄 开源协议

本项目采用 [MIT License](https://opensource.org/licenses/MIT) 开源协议。
