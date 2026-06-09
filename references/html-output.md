# HTML Output Guide

Use this reference when the user asks for a webpage, polished note, visual
explanation, or shareable artifact.

## Design Goals

- Motivation-first mathematical narrative.
- KaTeX-compatible formulas.
- Single HTML file with CDN KaTeX by default and graceful mobile layout.
- Clear separation between intuition, rigor, cross-domain connections, and
  reflection.

## Template

Use `templates/math-note.html`. Fill these placeholders:

| Placeholder | Content |
|---|---|
| `{{TITLE}}` | concise topic title |
| `{{SUBTITLE}}` | one-sentence motivation |
| `{{TAGS}}` | comma-separated concepts |
| `{{DATE}}` | ISO date |
| `{{MOTIVATION}}` | historical/conceptual crisis |
| `{{INTUITIVE_DERIVATION}}` | pre-rigorous idea and toy example |
| `{{RIGOROUS_VERSION}}` | formal theorem/proof/calculation |
| `{{MULTI_PERSPECTIVE}}` | visual/probabilistic/geometric/computational lens |
| `{{CROSS_DOMAIN}}` | applications and external motivations |
| `{{REFLECTION}}` | open question or deeper prompt |

## Rendering Procedure

If shell access exists, use:

```bash
python scripts/render-html.py \
  --title "Why Eigenvalues Matter" \
  --subtitle "Eigenvalues find directions a transformation cannot rotate." \
  --tags "linear algebra,eigenvalues,geometry" \
  --section MOTIVATION=motivation.md \
  --section INTUITIVE_DERIVATION=intuition.md \
  --section RIGOROUS_VERSION=rigor.md \
  --section MULTI_PERSPECTIVE=perspective.md \
  --section CROSS_DOMAIN=connections.md \
  --section REFLECTION=reflection.md \
  --out eigenvalues.html
```

If no shell exists, copy `templates/math-note.html` and replace placeholders
manually. If no file/artifact support exists, return one complete HTML code
block labeled "copyable HTML".

## Output Mode Matrix

| Host capability | Output |
|---|---|
| Filesystem writable | write `.html` file and report path |
| Artifact/canvas support | create artifact/canvas HTML |
| No write access but long output allowed | return complete copyable HTML block |
| No artifact and concise answer requested | return Markdown note instead |
| Offline requirement | bundle/download KaTeX assets or warn that CDN formulas need internet |

## Math Markup

- Prefer inline math: `\(Ax=\lambda x\)`
- Prefer display math: `\[\det(A-\lambda I)=0\]`
- `$...$` and `$$...$$` also work in the template, but escape literal currency
  dollar signs to avoid accidental rendering.
- Avoid unsupported LaTeX packages; KaTeX supports common AMS-style notation.
- Escape raw `<`, `>`, and `&` in prose unless intentionally writing HTML.
- `scripts/render-html.py` accepts a simple Markdown subset: headings, unordered
  and ordered lists, blockquotes, fenced code, simple tables, paragraphs, and
  raw math blocks. Use `--raw-html` only for trusted agent-authored sections.

## Visual Structure

Use template classes when helpful:

```html
<div class="motivation">
  <div class="motivation-title">The crisis</div>
  <p>...</p>
</div>

<div class="bold-assumption">Maybe the operation still behaves like the finite case.</div>

<div class="comparison">
  <div class="comparison-panel wild"><div class="comparison-label">Wild idea</div>...</div>
  <div class="comparison-panel rigorous"><div class="comparison-label">Rigorous repair</div>...</div>
</div>
```

## Offline Note

The default template loads KaTeX from a CDN. If the user needs offline HTML,
download KaTeX assets locally or tell them that formulas require internet
access unless assets are bundled.
