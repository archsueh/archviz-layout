# Changelog

## 1.4.1 (2026-10-09)

### Changed

- **`design-judgment` 集成块移出 SKILL.md 正文。** 2026-10-09 20:32:55 有并行会话
  在五个 archviz 仓库的 SKILL.md 末尾各追加了一段 956 字节的
  `<!-- design-judgment-integration -->` 块（交付前跑五段判断链自检）。
  **内容逐字保留，未删改一字**，但 956 字节会把本仓顶到 36,190 / 36,000 —— 超限。
  现移入 `references/design-judgment.md`，正文只留一行指针，SKILL.md 回到
  35,600 字节。`## 延伸参考` 的计数从 5 改成 6。
  **注意**：`reference_files` 这条计数断言在改之前先报了 `声明 5，实为 6` ——
  新加一个参考文件而没更新索引声明，正是这条门禁设计来抓的东西，它当场抓到了。

## 1.4.0 (2026-10-09)

本仓此前**没有 `references/` 目录**，SKILL.md 是家族里唯一「正文自含」的一个。

### Changed

- **正文拆进 `references/`，SKILL.md 51,848 → 35,233 字节（−32.1%）。** 迁出 5 节
  按需查阅的延伸规范，逐字保留、零删改（已用脚本比对：5 个文件正文与源段落
  完全相同，仅把内部 `###` 降一级为 `##`）：
  `social-editorial-cards.md` / `web-to-print-paged-media.md` /
  `ai-asset-rendering-pipeline.md` / `warm-paper-document-design.md` /
  `educational-boards-schematic-grammar.md`。
  SKILL.md 里留一张索引表 + 一句边界声明。
  **闸门、设计纪律、五步工作流、Pre-Flight、使用边界全部留在 SKILL.md** ——
  这是拆分时划的线，也是为什么这版是「保守边界」。
- 字节上限棘轮 **52,000 → 36,000**（拆之前是 99.7% 顶格，现在 97.9%）。

### Added

- **`references/` 目录** —— 本仓第一个。拆分后 35 KB 正文配 5 个参考文件，
  不再是家族里渐进披露比例最差的一个。
- **`requirements.txt`** —— `Pillow` 与 `playwright`。此前 `scripts/` 有第三方
  import 却**没有任何依赖清单**，干净检出直接 `ImportError`。
- **`deps` 检查** —— 套件新增第 6 项：把仓库里每个第三方 import 与清单对账。
  实测本仓 2/2 个 import 未声明。
- **`coverage` 检查** —— 套件新增第 7 项：`references/*.md` 必须从 SKILL.md
  **可达**（传递可达，不是直接点名）。索引表里删一行、计数断言仍然正确 ——
  这个失效模式 `counts` 结构上看不见，已用反向验证确认。

### Fixed

- **`scripts/` 有未声明的第三方依赖，且没有任何依赖清单。** `render_board_with_charts.py`
  顶层 `import PIL`，`capture_rects.py` 函数内 `import playwright` —— 干净检出跑不起来。
  现由 `requirements.txt` 声明，并由套件的 `deps` 检查守住不再复发。
  同一缺陷在**家族五个仓库里全部存在**（见套件 `deps` 检查的 docstring）。

### Notes

- **移出的那节变更日志自身有两个缺陷，照原样保留而不改写**：同一个版本有**两个
  `## v1.2.0` 标题**，且版本顺序非单调（v1.2.0 / v1.1.0 / v1.2.0 / v1.1.1）。
  两者都记在这里以便可见；都不影响版本门禁（只读第一个标题）。
- **`requirements.txt` 是给脚本用的，不是给 skill 用的。** 套件本身
  `check_archviz.py` 只用标准库 —— 它必须能在裸 Python 上守住这个仓库，
  这是当初拒绝「引入项目包」那条设计的同一条理由。
- **CI 里装依赖是为了验证清单可安装，不是为了发现缺 import。** `pip install`
  加 `compileall` 这个组合**检测不出任何缺失依赖** —— 字节编译从不 import。
  真正管这件事的是 `deps` 检查（离线、确定性、直接点名模块与文件）。
  安装步骤管的是另一件事：清单里的名字是否解析得到、版本约束是否可满足。
  经 PyPI 核对，7 个名字在 2026-10-09 全部存在。
- **pre-commit 垫片装到了 `.git/hooks/pre-commit`。** `.git/hooks/` 不进版本库，
  所以脚本躺在 `scripts/` 里不等于它会执行 —— 五个仓库里有四个只有脚本没有垫片。
  已把 archviz-diagram 早就有的那个三行垫片补装到 archviz-3d / archviz-sketch /
  archviz-animated / 本仓库。撤销方式：删掉该文件。
- **依赖安装只在 CI 做，不在 pre-commit 做。** 否则每次提交都依赖网络。

## 1.3.0 (2026-10-09)

This repo had **no CI and no `CHANGELOG.md`** before this release — the release
history lived inside SKILL.md, where nothing could check it against the code.

### Changed

- **The release history moved out of SKILL.md into this file.** It was a
  `## 版本变更（Changelog）` section at the end of SKILL.md, 8.5 KB and 14% of
  the file. Moving it does three things at once: SKILL.md gets smaller, the
  version gate gets an anchor to check `metadata.version` against, and a
  separate `CHANGELOG.md` does not duplicate a section that already existed.
  The section is reproduced below **verbatim**, with its heading levels
  normalised from `###` to `##` to match the family convention.
- Version 1.2.0 → 1.3.0.

### Added

- **`scripts/check_archviz.py`** — the family's portable consistency kit
  (archviz-diagram ADR-003). One file, per-repo `archviz-checks.json`, stdlib
  only, no venv and no package import required. Five checks: `version` /
  `budget` / `routing` / `counts` / `cjk`. `--self-test` carries 23 adversarial
  fixtures, four of which must **not** fire.
- **`.github/workflows/ci.yml`** — first CI for this repo.
- **`scripts/git-pre-commit.sh`** — the same gates locally.
- **`.gitattributes`** — pins SKILL.md to LF; the byte cap counts LF-normalised
  bytes.
- **`archviz-checks.json`** — registry: the four visual languages read from
  SKILL.md's `## 建筑版式 4 套视觉语言` section.

### Fixed

- **`description` named none of the four visual languages.** It described board
  design, grid systems and the readiness audit but never said Still Paper,
  Signal Proof, Bridge Canvas or Technical Blueprint — the four things a board
  actually gets designed *in*. All four are now named, each with its Chinese
  name. The description is the one text an agent reads *before* deciding to
  load the skill.
- **The "four visual languages" count had no machine-checkable anchor.** Every
  mention of the number used the Chinese numeral (`四套`) or the English word
  `four` — no Arabic numeral existed anywhere in the file, so the `counts` gate
  found no assertion point and **failed closed**, which is how it was designed:
  an assertion whose target has disappeared is itself a failure, not a pass.
  The `description` now leads with `4 套视觉语言（visual languages）` and the
  section heading with `建筑版式 4 套视觉语言`, giving two independent assertion
  points; the five remaining prose mentions of `四套` were normalised to `4 套`
  for the same reason.
- **`SKILL.md` was 59,972 bytes with zero `references/` files** — the worst
  progressive-disclosure ratio in the family (archviz-diagram: 43 KB over 49
  reference files). Moving the changelog brings it to ~51.5 KB. That is a
  reduction, not a fix: the byte cap below is a **ratchet**, and the real work —
  splitting the body into `references/` — is deliberately left open rather than
  done hastily. See the note under `### Notes`.

### Notes

- **The byte cap is set to 52,000 as a ratchet, not as a target.** The family's
  reference project (`diagram-design`) caps SKILL.md at 40,000 bytes and
  actively slimmed to 28,869. This repo is ~11 KB above that even after the
  changelog move, and it has no `references/` directory to move anything into.
  A proper split is a real piece of work and should not be improvised.
- **The moved section has two defects of its own, preserved rather than
  rewritten**: it contains **two `## v1.2.0` headings for the same release**,
  and its version order is non-monotonic (`v1.2.0`, `v1.1.0`, `v1.2.0`,
  `v1.1.1`). Both are recorded here so they are visible; neither affects the
  version gate, which reads only the first heading.
- **`scripts/` has undeclared third-party dependencies.** `render_board_with_charts.py`
  imports `PIL` at module level and `capture_rects.py` imports `playwright`
  inside a function, but this repo ships neither a `requirements.txt` nor a
  `pyproject.toml` — so a clean checkout cannot run either script, and CI has
  nothing to install. Not fixed here: recorded because the new CI step only
  byte-compiles `scripts/`, and byte-compilation cannot see a missing import.
  Left as a finding rather than a silent scope expansion.
- **The pre-commit hook was installed at `.git/hooks/pre-commit`.** `.git/hooks/`
  is not versioned, so a script existing in `scripts/` does not make it run —
  four of the five repos had the script and no hook. The same three-line shim
  that archviz-diagram already carried was installed in archviz-3d,
  archviz-sketch, archviz-animated and here. To undo: delete that file.

### Verified

- `scripts/check_archviz.py` → PASS (5/5)
- `scripts/check_archviz.py --self-test` → 23/23

---

> **The section below was moved verbatim from SKILL.md §版本变更（Changelog） on
> 2026-10-09**, with heading levels normalised `###` → `##`. Nothing else was
> edited. Its duplicate `v1.2.0` heading and non-monotonic order are preserved
> as written.

## v1.2.0 — awesome-design-md 拆解补强：DESIGN.md 伴侣 + 视觉目录 + 第四套视觉语言（2026-09-24）
**来源**：`VoltAgent/awesome-design-md`（MIT，73+ 真实 `DESIGN.md`，9 段式 token 规范）。本仓库提供的是**格式范本 + 真实 token 语料库**，而非可直接搬运的内容——其主体为通用 Web-UI 装饰套路，已被 v1.1.0「使用边界 OUT 列」明确排除。本次只取「格式骨架」与「同基因子集的真实 token 证据」，其余不采纳。

**A 层 — DESIGN.md 伴侣（4 份，落 `design-md/<lang>/DESIGN.md`）**
1. 为现有三套语言（still-paper / signal-proof / bridge-canvas）各补一份 9 段式 DESIGN.md 伴侣，把 Skill 里的散落 token 归一为单文件权威规范：Visual Theme / Color Palette & Roles / Typography Rules / Component Stylings / Layout Principles / Depth & Elevation / Do's & Don'ts / Responsive Behavior / Agent Prompt Guide。
2. 新增第四套语言 **技术蓝图 Technical Blueprint** 的 DESIGN.md（navy `#0D1B2A` + cyan `#5FD0E8` hairline 网格），与 signal-proof（轻量冷灰电蓝文档）、bridge-canvas（黑底金绿电影）明确区分。

**B 层 — 视觉目录 preview.html（8 份）**
- 每套语言各 1 个 `preview.html`（token 色板/字阶/组件/网格导轨可视化目录）+ 1 个 `preview-dark.html`（跨表面可读性基线）。同时充当 `capture_rects.py` 的测试板。

**C 层 — 第四套视觉语言 + 集成**
1. SKILL.md：视觉语言表「三套」→「四套」，新增「技术蓝图」配方块；五步工作流 / Pre-Flight / 渲染支持列表同步加入 blueprint。
2. `scripts/render_board_with_charts.py`：`VISUAL_LANGUAGES` 加入 blueprint；`--language` 选项开放 blueprint；新增 `CHART_PALETTES` 按语言分发的图表配色（blueprint 用 navy 安全的青/钢灰，避免暗色柱在深蓝底上消失）。

**验证与回头修（用本 Skill 自己的审计链路自查样本）**
- 8 份 preview（4 语言 × 明暗两表面）全跑 `capture_rects.py --run-audit`，最终 **collision / contrast-wcag / alignment 三项全 0 PASS**。
- 审计回头抓出两个真缺陷并已修：
  1. **中间调强调色的双向陷阱**（still-paper 朱砂 `#C96442`）：浅底强调文字仅 3.54:1；且**正反压字都不达标**——浅字压朱砂同样 3.54:1。解法分表面：浅面用压深 `accent-ink #8A3A22`（7.05:1，文字）或朱砂填充配深字 `ink`（4.73:1，按钮）；**暗面必须反向提亮**为 `#E07A54`（朱砂在 `#1C1B18` 上只有 4.41:1，压深会更糟）。
  2. **alignment SIGNAL 误报**：包装盒与其子元素左缘本就重合，被判为「近距错位」。已与 collision GATE 对齐，同样跳过父子嵌套（`36d58dd`）。
- 结论：把 DESIGN.md 伴侣写成可跑的 preview，再用审计链路回头验，能抓出「只看 token 表看不出」的跨表面对比缺陷——这就是 B 层存在的理由，不只是好看的目录。

**方法论结论（与 X 帖子判定一致）**：awesome-design-md 可拆解，但只取格式与同基因真实 token；通用 Web-UI 装饰套路仍排除。新 blueprint 的纪律（4/8px 模数、字重 ≤600 + 负字距、表面层级替代投影、1px hairline、单强调色、0 圆角、Mono 微标签）提炼自 Linear / Vercel / IBM Carbon / Supabase / HashiCorp 同基因子集。

## v1.1.0 — 全量补强（2026-09-24）
**来源**：ckw-design-skill（`design-spatial` / `design-system` / `design-thinking`，MIT）、martinavila `skills/agent-skills/web-design` 网格配方（agency-grid-layout-minimal / image-first-grid-layout）。

**新增 / 增强**
1. **渲染评图循环（Render-then-Critique）**：落版后强制 render 成图、独立 judge 评图（非自评）；可测量视觉平衡（墨密度重心 x=0.50 / y≈0.46，接受 ±0.03/±0.04）；GATES vs SIGNALS 纪律，防过度纠正成平均。
2. **对比度闸门**：WCAG 2 作合规地板（正文 4.5:1 / 大字 3:1）+ APCA 作感知设计判据，落版实测数值。
3. **网格导轨与构图范式**：结构导轨（外框轨 / 中轴导引 / 角标）、图为主舞台、底部锚定 Hero、服务行列表。
4. **字体层级清晰铁律**：眯眼测试 + 数据 `tabular-nums` 等宽对齐；禁止 Mono 当装饰微标签（trend-slop）。
5. **核心设计纪律 4–6**：评审基线（Name-on-It Bar）、留白即结构、冲击留给标点。
6. **Pre-Flight B-18**：HTML 卡窄屏无横向溢出闸门 + `aspect-ratio` 防 CLS。
7. **成图审计脚本** `scripts/audit_board.py`（零依赖纯标准库）：渲染截图 → 全分辨率墨密度重心（平衡 SIGNAL）+ 粗粒度局部对比 + 矩形模式（碰撞/对齐/间距/ WCAG 对比 GATES）+ 标注 SVG 叠加。把本循环的"可测量"从口头变成可跑工具。

## v1.2.0 — DESIGN.md 伴侣 + 技术蓝图视觉语言（2026-09-24）
**来源**：VoltAgent/awesome-design-md（MIT，73 个真实 DESIGN.md 集合）的**同基因子集**（IBM Carbon / Supabase / HashiCorp / Linear / Vercel）「精密技术网格」共性——4/8px 间距模数、字重 600 封顶 + 负字距、surface 层级替投影、1px hairline、单色灰阶 + 单一强调色、0 圆角、Mono 微标签。整批品牌 token 因属通用 Web-UI 装饰（archviz 已排除）而**未采纳**；仅借格式范式 + 同基因子集。

**新增**
1. **`design-md/` 目录**：为四套视觉语言各写一份 9 节 DESIGN.md 伴侣（静纸 / 实证 / 图桥 / 技术蓝图），把色板语义名+hex+角色、排版层级表、组件、布局、Do/Don't、Agent 提示固化成代理可读 token sheet。
2. **`preview.html` + `preview-dark.html`**：每套语言的可视化目录（色板/字阶/按钮/卡片/hairline 网格），兼作 `capture_rects.py` 审计链路的可测展板——评图循环的视觉基线参照。
3. **第四套视觉语言「技术蓝图 Technical Blueprint」**：深蓝图幅（`#0D1B2A`）+ 青色 hairline 网格（`#2A4A6B`）+ 唯一青色强调（`#5FD0E8`）+ 0 圆角方正 + 字重 600 封顶 + display 负字距 + Mono 技术标注。填补 archviz 缺的「技术图纸/构造详图深色板」，与 signal-proof（轻量冷灰电蓝）、bridge-canvas（黑底金绿电影）明确区分。接入 SKILL.md 视觉语言表与 `render_board_with_charts.py` 的 `VISUAL_LANGUAGES`。

**显式未采纳（Deliberately Excluded）**
- 73 个品牌里绝大多数（Binance 黄 / Shopify 霓虹绿 / Renault aurora 渐变 / Runway 电影暗黑 / Mastercard 奶油轨道药丸等）属通用 Web-UI 品牌官网视觉，与建筑展板印刷级 Swiss 极简领域错位，未搬入。

## v1.1.1 — 一键抓取 + 审计精度修正（2026-09-24）
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
