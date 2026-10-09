# 网页到印刷排版 (Web-to-Print & CSS Paged Media)

> 从 `SKILL.md` 原样迁出（2026-10-09 渐进式披露拆分，v1.4.0），**内容逐字未删改**，
> 仅把内部 `###` 标题降一级为 `##`（因为小节标题升为本文 H1）。
> 何时加载：做作品集 / 画册 PDF，走 HTML+CSS Paged Media 渲染时。
> **本文件不需要随 skill 一起加载** —— SKILL.md 里只有一行索引指向它。

## 网页到印刷排版 (Web-to-Print & CSS Paged Media)

在制作作品集或画册 PDF 时，直接使用 HTML+CSS 并配合 Paged Media 渲染引擎（如 WeasyPrint 或 paged.js）是一个高度敏捷的系统方案。相比传统 InDesign，它支持数据 reflow 与自动化模板排版。

## 1. 页面几何尺寸与装订边距 (Page Geometry & Margins)
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

## 2. 章节首页页眉遮挡 Hack (Suppressing Header on Chapter Start)
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

## 3. 段落微排版控制 (Micro-Typography)
* **避头尾与防单行 (Widows & Orphans)**：
  - `orphans: 2;`：每页底部至少保留段落的 2 行，防止孤立的段落首行留在上一页。
  - `widows: 2;`：每页顶部至少保留段落的 2 行，防止段落的最后一句话单独掉入下一页页首。
* **自动折行与连字符 (Auto-Hyphenation)**：
  - 必须在 HTML 根节点设置正确的语言属性（如 `<html lang="en-us">`），连字符字典才会生效。
  - 样式声明：`body { hyphens: auto; hyphenate-limit-chars: 6 3 2; }`（控制单词折行的字数阈值），使两端对齐的文本边缘更自然平滑。
* **防单词悬挂 (Preventing Runts)**：
  - 在 HTML 中，使用非换行空格（`&nbsp;`）替换段落中最后两个单词之间的普通空格，确保最后一行至少有 2 个单词，避免段底出现孤立单词。
