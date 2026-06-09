# Input Processing: OCR, PDFs, Screenshots, and Handwritten Math

Use this reference when the user supplies an image, PDF, screenshot, scan, or
messy copied math.

## OCR Workflow

1. **Choose the safest tool path**: use native vision first when available; for
   PDFs try text extraction before OCR; for local tools try `pdftotext`,
   `tesseract`, or Python image inspection; if none exist, ask for a crop or
   transcription.
2. **Inventory the input**: identify pages/images, orientation, crop, and
   whether diagrams matter.
3. **Transcribe first**: write the problem in LaTeX/Markdown before solving.
4. **Mark uncertainty**: use `[?]` or alternatives such as `a_n` vs `a^n` when
   symbols are ambiguous.
5. **Preserve layout**: keep cases, matrices, aligned equations, labels,
   diagram annotations, and answer choices.
6. **Validate mathematically**: check dimensions, domains, signs, and whether
   the transcription creates a coherent problem.
7. **Ask only when necessary**: if ambiguity changes the answer, ask for a crop
   or clarification; otherwise state the assumption and continue.

## Concrete Extraction Order

Use the first available safe option:

1. Native image/vision understanding in the host agent.
2. Embedded PDF text extraction (`pdftotext`, browser PDF text selection, or
   equivalent).
3. Local OCR (`tesseract`, platform OCR, or trusted local tools).
4. Manual visual transcription by the agent.
5. Ask the user for a clearer crop or typed transcription.

Never upload user images/PDFs to third-party OCR, search, or storage services
unless the user explicitly permits it.

## Math OCR Conventions

| Visual Pattern | Preferred Transcription |
|---|---|
| stacked fraction | `\frac{...}{...}` |
| radical with long bar | `\sqrt{...}` |
| matrix/table | `\begin{pmatrix}...\end{pmatrix}` or Markdown table |
| piecewise brace | `\begin{cases} ... \end{cases}` |
| circled/boxed answer | note as `selected answer: ...` |
| graph/diagram | list axes, labels, key points, and visual relationships |

## Ambiguity Checklist

Common OCR confusions:

- `1`, `l`, `I`
- `0`, `O`, `\theta`
- `x`, `\times`, `X`
- `n`, `m`, `r`
- `a_n`, `a^n`, `a_n^2`
- `\in`, `\subset`, `\epsilon`
- minus sign vs fraction bar
- decimal point vs multiplication dot

## Confidence Notation

Attach confidence to regions when useful:

```text
page 1, main equation, high confidence: \int_0^1 x^2 e^{-x}\,dx
page 1, lower-left annotation, low confidence: \alpha vs a
diagram, angle label, medium confidence: 30^\circ
```

Use region labels such as `page 2 lower-left`, `matrix row 3 column 1`, or
`diagram label near point B`.

## Image-to-Solution Structure

Use this response shape:

```markdown
## Transcription
... recovered problem ...

## Assumptions
- I read the lower limit as `0`, not `O`.
- The diagram appears to mark a right angle at `B`.

## Solution
... IntuitMath workflow ...

## Check
... sanity check against the image/problem constraints ...
```

## Diagrams

For geometry, graphs, circuits, or applied math diagrams:

- Name every visible point, axis, angle, and length.
- Convert visual constraints into equations before solving.
- If the diagram is not to scale, do not infer unmarked equalities.
- If it appears to be to scale but unmarked, use it only as intuition.

## Privacy and Tooling

- Prefer local OCR/vision tools when available.
- Never send user images or PDFs to external OCR/search services without
  explicit permission.
- If OCR confidence is low, solve a symbolic version and ask for confirmation.
