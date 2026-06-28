#!/usr/bin/env python3
"""
Layout + Diagram fusion renderer.
Embeds archviz-diagram charts into archviz-layout board templates.
Supports: A0 vertical board, A3 portfolio, social card (3:4).
"""
import argparse
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Layout templates
TEMPLATES = {
    "a0-vertical": {
        "width": 841,  # A0 width in mm (portrait)
        "height": 1189,
        "margin": 60,  # mm
        "columns": 3,
        "gutter": 20,
    },
    "a3-landscape": {
        "width": 420,
        "height": 297,
        "margin": 30,
        "columns": 6,
        "gutter": 10,
    },
    "social-3-4": {
        "width": 1080,
        "height": 1440,
        "margin": 60,
        "columns": 1,
        "gutter": 0,
    },
}

# Visual languages
VISUAL_LANGUAGES = {
    "still-paper": {
        "name": "静纸 (Still Paper)",
        "bg": "#F5F4ED",
        "text": "#141413",
        "accent": "#c96442",
        "border": "#C9C7BC",
        "font": "serif",
    },
    "signal-proof": {
        "name": "实证 (Signal Proof)",
        "bg": "#F5F5F4",
        "text": "#0a0a0a",
        "accent": "#0039A6",
        "border": "#94a3b8",
        "font": "sans",
    },
    "bridge-canvas": {
        "name": "图桥 (Bridge Canvas)",
        "bg": "#141413",
        "text": "#E8E4E0",
        "accent": "#FFD500",
        "border": "#44403C",
        "font": "sans",
    },
}

# Chart colors (from archviz-diagram)
CHART_COLORS = [
    "#002fa7",  # IKB
    "#94a3b8",  # Slate
    "#a8a29e",  # Stone
    "#d6d3d1",  # Pebble
    "#c96442",  # Terracotta
    "#5e5d59",  # Warm Gray
]

SCALE = 2


def hex_rgba(value, alpha=255):
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4)) + (alpha,)


def c(v):
    return int(round(v * SCALE))


def load_font(size, font_type="sans", bold=False):
    candidates = []
    if font_type == "serif":
        candidates = [
            "/System/Library/Fonts/Supplemental/Georgia.ttf",
            "/System/Library/Fonts/Times.ttc",
        ]
    candidates.extend([
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    ])
    for path in candidates:
        try:
            return ImageFont.truetype(path, c(size))
        except OSError:
            continue
    return ImageFont.load_default()


def render_chart_in_layout(data, x, y, width, height, language="still-paper"):
    """Render a chart within a layout region."""
    theme = VISUAL_LANGUAGES[language]
    
    img = Image.new("RGBA", (c(width), c(height)), hex_rgba(theme["bg"]))
    draw = ImageDraw.Draw(img)
    
    # Chart data
    categories = data.get("categories", [])
    values = data.get("values", [])
    labels = data.get("labels", [])
    title = data.get("title", "")
    
    if not categories or not values:
        return img
    
    # Layout
    margin = 20
    chart_width = width - margin * 2
    chart_height = height - margin * 2 - 40  # Reserve space for title
    
    # Title
    font_title = load_font(14, theme["font"], bold=True)
    draw.text(
        (c(margin), c(margin)),
        title,
        font=font_title,
        fill=hex_rgba(theme["text"]),
    )
    
    # Calculate bar width
    n_bars = len(categories)
    bar_width = min(40, chart_width / n_bars * 0.7)
    gap = (chart_width - bar_width * n_bars) / (n_bars + 1)
    
    # Max value for scaling
    max_val = max(values) if values else 1
    
    # Draw bars
    font_label = load_font(10, theme["font"])
    font_value = load_font(9, theme["font"])
    
    for i, (cat, val) in enumerate(zip(categories, values)):
        bar_height = (val / max_val) * chart_height
        x_pos = margin + gap + i * (bar_width + gap)
        y_pos = margin + 40 + chart_height - bar_height
        
        # Bar color
        color = CHART_COLORS[i % len(CHART_COLORS)]
        
        # Draw bar
        draw.rectangle(
            [c(x_pos), c(y_pos), c(x_pos + bar_width), c(margin + 40 + chart_height)],
            fill=hex_rgba(color),
            outline=hex_rgba(theme["border"]),
        )
        
        # Category label
        label = labels[i] if i < len(labels) else cat
        bbox = draw.textbbox((0, 0), label, font=font_label)
        label_width = bbox[2] - bbox[0]
        draw.text(
            (c(x_pos + bar_width / 2 - label_width / 2 / SCALE), c(margin + 40 + chart_height + 5)),
            label,
            font=font_label,
            fill=hex_rgba(theme["text"]),
        )
        
        # Value label
        value_text = f"{val:.1f}"
        bbox = draw.textbbox((0, 0), value_text, font=font_value)
        value_width = bbox[2] - bbox[0]
        draw.text(
            (c(x_pos + bar_width / 2 - value_width / 2 / SCALE), c(y_pos - 15)),
            value_text,
            font=font_value,
            fill=hex_rgba(theme["accent"]),
        )
    
    return img


def render_board(template_name, charts, language="still-paper", title="Project Title"):
    """Render a complete board with embedded charts."""
    template = TEMPLATES[template_name]
    theme = VISUAL_LANGUAGES[language]
    
    width = template["width"]
    height = template["height"]
    margin = template["margin"]
    
    img = Image.new("RGBA", (c(width), c(height)), hex_rgba(theme["bg"]))
    draw = ImageDraw.Draw(img)
    
    # Draw border
    draw.rectangle(
        [c(margin / 2), c(margin / 2), c(width - margin / 2), c(height - margin / 2)],
        outline=hex_rgba(theme["border"]),
        width=c(1),
    )
    
    # Title area (Tier 1)
    font_title = load_font(36, theme["font"], bold=True)
    draw.text(
        (c(margin), c(margin)),
        title,
        font=font_title,
        fill=hex_rgba(theme["text"]),
    )
    
    # Subtitle
    font_sub = load_font(14, theme["font"])
    draw.text(
        (c(margin), c(margin + 50)),
        f"Visual Language: {theme['name']}",
        font=font_sub,
        fill=hex_rgba(theme["accent"]),
    )
    
    # Draw horizontal line
    draw.line(
        [(c(margin), c(margin + 80)), (c(width - margin), c(margin + 80))],
        fill=hex_rgba(theme["border"]),
        width=c(1),
    )
    
    # Chart areas (Tier 4 - Analysis Diagrams)
    if charts:
        n_charts = len(charts)
        chart_width = (width - margin * 2 - (n_charts - 1) * 20) / n_charts
        chart_height = 200
        
        for i, chart_data in enumerate(charts):
            x = margin + i * (chart_width + 20)
            y = margin + 100
            
            # Render chart
            chart_img = render_chart_in_layout(
                chart_data, x, y, chart_width, chart_height, language
            )
            
            # Paste chart onto board
            img.paste(chart_img, (c(x), c(y)), chart_img)
            
            # Draw chart border
            draw.rectangle(
                [c(x), c(y), c(x + chart_width), c(y + chart_height)],
                outline=hex_rgba(theme["border"]),
                width=c(1),
            )
    
    # Footer
    font_footer = load_font(10, theme["font"])
    draw.text(
        (c(margin), c(height - margin - 20)),
        "Generated by archviz-layout × archviz-diagram",
        font=font_footer,
        fill=hex_rgba(theme["text"], 128),
    )
    
    return img


def main():
    parser = argparse.ArgumentParser(description="Layout + Diagram fusion renderer")
    parser.add_argument("--template", default="a0-vertical", 
                       choices=["a0-vertical", "a3-landscape", "social-3-4"],
                       help="Board template")
    parser.add_argument("--language", default="still-paper",
                       choices=["still-paper", "signal-proof", "bridge-canvas"],
                       help="Visual language")
    parser.add_argument("--title", default="Project Title", help="Board title")
    parser.add_argument("--charts", nargs="+", help="Chart JSON files")
    parser.add_argument("--outdir", default="./output", help="Output directory")
    parser.add_argument("--basename", default="board", help="Output filename base")
    args = parser.parse_args()
    
    # Load charts
    charts = []
    if args.charts:
        for chart_file in args.charts:
            with open(chart_file, "r", encoding="utf-8") as f:
                charts.append(json.load(f))
    
    # Render board
    img = render_board(args.template, charts, args.language, args.title)
    
    # Save
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    
    png_path = outdir / f"{args.basename}.png"
    img.save(png_path)
    print(f"PNG saved: {png_path}")
    
    return png_path


if __name__ == "__main__":
    main()
