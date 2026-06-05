# Math Visualization in HTML

## KaTeX (Recommended)

**Website**: https://katex.org/
**GitHub**: https://github.com/KaTeX/KaTeX

### Key Features
- Fastest math typesetting library for the web
- Renders synchronously (no reflow)
- Print quality (based on Donald Knuth's TeX)
- Self-contained, no dependencies
- Server-side rendering possible

### Usage
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.17.0/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.17.0/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.17.0/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body);"></script>
```

### Delimiters
- `$$...$$` or `\[...\]` for display math
- `$...$` or `\(...\)` for inline math

## MathJax

**Website**: https://www.mathjax.org/

### Key Features
- Supports MathML, TeX, ASCIImath as input
- HTML+CSS, SVG, or MathML output
- Accessibility: screen readers, zoom, exploration
- Works in all browsers
- Can copy equations into Office, LaTeX, wikis

### When to Use
- Need broader format support (MathML, AsciiMath)
- Need accessibility features
- Need interactive exploration of equations
- For simpler projects, KaTeX is preferred (faster, lighter)

## Interactive Math Notebooks in HTML

### CAScad (Pure HTML/JS/CSS)
- Reactive notebook for symbolic computation
- Multi-kernel: Giac/Xcas, CortexJS Compute Engine
- MathLive for visual math input
- JSXGraph for interactive 2D/3D plots
- KaTeX for rendering
- **No build step** - pure browser ES2020+

### Jupyter-Kit
- Renders .ipynb notebooks in the browser
- Framework-agnostic (React, Vue, Svelte, Web Component)
- Optional: Pyodide for in-browser Python execution
- KaTeX/MathJax support
- 13 chrome themes, 8 syntax themes

## Design Principles for IntuitMath HTML Output

### 1. Typography
- Serif font for body text (Georgia, Literata, Lora)
- Sans-serif for UI elements
- Monospace for code
- KaTeX for math

### 2. Color Scheme
- Warm background (#faf9f6)
- Accent color for motivation blocks (#2c5f8a)
- Danger color for "bold attempts" (#8b3a3a)
- Success color for "rigorous versions" (#3a6b4a)
- Warning color for "bold assumptions" (#d4a030)

### 3. Layout
- Max-width: 780px (optimal reading width)
- Generous line-height (1.75)
- Clear section breaks
- Responsive (mobile-friendly)

### 4. Components
- **Motivation block**: Bordered box with accent color
- **Comparison panels**: Side-by-side (wild vs rigorous)
- **Bold assumption**: Yellow left border
- **Motivation note**: Blue italic annotation
- **Reflection box**: Gradient background
- **History note**: Dashed border
- **Math block**: Code-like background

### 5. Interactive Elements (Future)
- Collapsible sections for detail
- Tab switching between perspectives
- Animated derivation steps
- Clickable cross-reference links

## Implications for IntuitMath

1. **KaTeX is the right choice** for our template - faster, lighter, sufficient for our needs
2. **Our template already follows best practices** - warm serif typography, clear sections, comparison panels
3. **Future enhancement**: Add interactive elements (collapsible sections, tabs)
4. **Self-contained HTML**: All CSS/JS inline or CDN-linked, single file output
5. **Print-friendly**: CSS @media print rules for paper output

## Sources
- KaTeX: https://katex.org/
- MathJax: https://www.mathjax.org/
- CAScad: https://github.com/s-celles/CAScad
- Jupyter-Kit: https://github.com/walkframe/jupyter-kit
