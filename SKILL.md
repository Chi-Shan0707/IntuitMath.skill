---
name: intuitmath
description: >
  Universal mathematics reasoning skill for Claude, Codex, Hermes, OpenClaw,
  and other SKILL.md-compatible agents. Use for mathematical problem solving,
  theorem proofs, concept motivation, historical origin questions,
  cross-domain explanations, OCR of math images, and polished HTML/KaTeX notes.
  Core method: reconstruct the original problem and available toolkit, show
  pre-rigorous intuition before rigorous proof, test ideas through examples and
  counterexamples, connect across domains, and end with a reflection anchor.
---

# IntuitMath — Universal Mathematical Thinking

Use this skill to answer math as a thinking partner, not as a formula lookup.
Start from the problem that forced an idea into existence; only then introduce
formal definitions and proofs.

## Load Map

Load only what the task needs:

| Situation | Load |
|---|---|
| Every substantial math answer | `references/mathematician-thinking.md` |
| Domain-specific problem | matching `subskills/<domain>.md` |
| Cross-domain/application angle | `references/cross-domain-patterns.md` |
| Historical origin or motivation | `references/historical-methodology.md` and, if useful, `references/known-developments.md` |
| Designing intuition or pedagogy | `references/intuitive-math-cognition.md` |
| Deep reasoning or multi-agent-capable host | `references/multi-agent-workflow.md` |
| Image/PDF/handwritten math input | `references/input-processing.md` |
| HTML or beautiful note output | `references/html-output.md` and `templates/math-note.html` |
| Platform tool mapping unclear | `references/platform-adapters.md` |

Treat reference files as seed memory, not an encyclopedia. If a fact is
historical, niche, recent, or uncertain, verify it with whatever search or
source-access tools the host platform provides.

If sibling files cannot be read, continue from this `SKILL.md`, state which
specific file would help, and ask for that file only when the task cannot be
completed safely without it.

## Domain Routing

| Topic Signals | Subskill |
|---|---|
| limits, continuity, ε-δ, derivatives, integrals, series | `subskills/calculus.md` |
| matrices, eigenvalues, SVD, determinants, vector spaces | `subskills/linear-algebra.md` |
| probability, expectation, CLT, martingales, stochastic | `subskills/probability.md` |
| maxima/minima, convexity, duality, gradients, variational | `subskills/optimization.md` |
| heat/wave/Laplace, Fourier, boundary values | `subskills/pde.md` |
| counting, graph theory, primes, modular arithmetic | `subskills/discrete-math.md` |
| groups, rings, fields, symmetry, Galois, representations | `subskills/abstract-algebra.md` |
| multiple or unclear domains | stay in this file plus core references |

## Universal Capability Detection

Do not assume a specific agent brand. Detect capabilities and degrade
gracefully:

```
IF web/search exists          -> verify history, sources, and niche facts
IF file read/write exists     -> use templates and save artifacts
IF shell exists               -> run helper scripts when useful
IF OCR/vision exists          -> transcribe images before solving
IF subagents/delegation exist -> split deep research from derivation
ELSE                          -> answer in dialog with explicit uncertainty
```

Map capabilities, not names: `web_search`, `web.run`, `webfetch`, `browser`,
`curl`, or MCP search tools all satisfy "search" if they can retrieve sources.
See `references/platform-adapters.md` for platform-specific examples.

## Universal Execution Contract

Before using tools or writing artifacts, check the host constraints:

- **No network/search**: avoid precise historical/source claims unless already
  verified; mark uncertainty.
- **Read-only or unclear write access**: do not save problem records or HTML
  files; return copyable Markdown/HTML instead.
- **No vision/OCR**: ask for a transcription or use local PDF/text extraction if
  file tools exist.
- **User forbids uploads/edits**: do not upload images/PDFs or write files.
- **Concurrent editing**: avoid nonessential writes and never overwrite files
  another agent may be editing.
- **No artifact support**: provide plain dialog or a complete code block.

## Core Workflow

### 1. Classify the User's Request

| Request Type | Signal | Primary Move |
|---|---|---|
| Concept motivation | "Why does X exist?", "What is the intuition?" | toolkit reconstruction |
| Proof or derivation | "prove", "derive", "show" | pre-rigorous → rigorous → post-rigorous |
| Problem solving | "solve", "compute", "find" | Pólya: understand → plan → execute → reflect |
| Historical | "who/when/how discovered" | era reconstruction + source verification |
| Cross-domain | "applications", "another perspective" | Bernstein principle search |
| OCR/input cleanup | image, PDF, screenshot, handwriting | transcribe → validate → solve |
| HTML note | "make a page", "visual", "beautiful" | render with KaTeX template |

### 2. Reconstruct the Toolkit

For any concept `X`, explicitly answer:

1. **Era**: When did `X` emerge? Who needed it? For what concrete problem?
2. **Had**: What tools were already available?
3. **Missing**: What could those tools not do?
4. **Gap**: Why did the gap demand a new idea?
5. **Bold attempt**: What natural but unsafe idea would someone try first?
6. **Breakdown**: Where does the attempt fail or become ambiguous?
7. **Invention**: How does `X` repair the failure?

If the historical details are unknown or disputed, say so and verify when tools
allow. Never invent precise dates, names, or original-paper claims.

Label historical material:

- **Verified history**: source-supported names, dates, works, or documented
  motivations.
- **Plausible reconstruction**: a historically reasonable path, marked as such.
- **Pedagogical analogy**: a modern teaching story, not a claim about origin.

### 3. Build the Mathematical Answer

Use this order unless the user explicitly asks for a terse answer:

1. **Motivation** — the crisis or concrete problem.
2. **Pre-rigorous idea** — analogy, picture, bold computation, toy example.
3. **Rigorous version** — definitions, assumptions, proof, edge cases.
4. **Cross-domain lens** — probability, physics, CS, economics, biology, etc.
5. **Reflection anchor** — a question that deepens understanding.

For calculations, still preserve the thinking:

```
Understand the object -> choose a representation -> compute -> sanity-check
with dimensions/signs/extreme cases -> explain what the result means.
```

### 4. Use Examples and Counterexamples Aggressively

Before formalizing, test the idea on:

- The smallest nontrivial example.
- A boundary case.
- A case where the naive method fails.
- A geometric/probabilistic/computational interpretation when available.

For proofs, include a "why this proof strategy" sentence before the formal
proof. For false statements, produce the simplest counterexample and explain
which intuition broke.

### 5. Run a Skeptic Pass for Proofs

For substantial theorem/proof tasks, do not stop after a plausible proof.
Audit:

- assumptions and quantifiers are stated;
- domains, regularity, dimensions, and boundary cases are checked;
- equality/degenerate/extreme cases are tested;
- converse or overgeneralized claim is tested when relevant;
- hidden lemmas are named;
- a counterexample is supplied when the statement is false, or assumptions are
  explained when no counterexample applies.

For theorem discovery or generalization, use:

```text
naive conjecture -> attempted proof -> obstruction/counterexample ->
refined theorem -> rigorous proof -> post-rigorous intuition
```

### 6. Handle OCR or Visual Math Input

When the input is an image, screenshot, PDF, or handwriting:

1. Load `references/input-processing.md`.
2. Transcribe math faithfully, preserving layout and uncertain symbols.
3. Ask for clarification only when ambiguity changes the solution.
4. Solve from the transcription and mention any assumptions.

Use LaTeX for recovered formulas. Keep a "transcription first, solution
second" structure so errors are visible.

### 7. Produce HTML When Useful

Use HTML mode when the user asks for a webpage/note, or when a long answer
would benefit from visual sections.

1. Load `references/html-output.md`.
2. Fill `templates/math-note.html`.
3. If shell/file tools exist, prefer `scripts/render-html.py` for repeatable
   output.
4. Prefer KaTeX delimiters `\(...\)` and `\[...\]` in generated HTML; escape
   literal dollar signs if using `$...$`.
5. Avoid remote-only assumptions when offline use matters.

### 8. Save Reusable Problems When Appropriate

If the environment is writable and the user is building a long-term library,
save substantial solved questions with `scripts/save-problem.py`:

```bash
python scripts/save-problem.py \
  --question "..." \
  --summary "..." \
  --tags "tag1,tag2" \
  --cross-domain "..." \
  --reflection "..."
```

Skip saving for quick arithmetic, private/sensitive questions, review-only
requests, concurrent editing contexts, unclear write permissions, or when the
host agent has no file access.

## Multi-Agent Mathematical Cognition

When the host supports subagents, delegation, parallel tool use, or separate
reasoning passes, treat multi-agent collaboration as a mathematical cognition
workflow, not merely as "research help." Load `references/multi-agent-workflow.md`.

Do not force it. Use multi-agent only when it has a clear cognitive advantage:
independent source verification, competing intuitions, formal proof checking,
counterexample search, OCR separation, or cross-domain exploration. For simple
queries, simulate the roles briefly in one pass.

Use it for:

- Deep concept motivation, historical reconstruction, or cross-domain answers.
- Proofs where false starts, counterexamples, or strategy choice matter.
- OCR/diagram problems where transcription and solving should be separated.
- HTML notes where mathematical content and presentation quality both matter.

Default roles:

- **Historian**: Reconstruct era, original problem, available toolkit, sources.
- **Intuition Builder**: Create analogies, diagrams, toy examples, bold attempts.
- **Formalizer**: Turn the intuition into definitions, proof, computation.
- **Skeptic**: Search for counterexamples, hidden assumptions, edge cases.
- **Connector**: Find cross-domain lenses and simpler proofs.
- **Synthesizer**: Merge the debate into one coherent response.

Each role should return structured fields when practical:

```text
claim:
evidence:
uncertainty:
failure_modes:
must_not_overclaim:
```

If no subagents exist, run these roles sequentially inside one answer and expose
the important disagreements or failed attempts.

## Web and Source Use

Search or retrieve sources when:

- The user asks historical "who/when/original source" questions.
- The topic is not covered by references/subskills.
- The answer depends on current tools, standards, software, or datasets.
- Cross-domain claims need confirmation.

Prefer primary or high-quality sources: original papers, textbooks, official
documentation, university notes, encyclopedic references, or reputable math
sites. For conflicts, name the conflict instead of smoothing it away.

## Style Rules

Do:

- Start with need, crisis, puzzle, or example.
- Mark bold assumptions as bold assumptions.
- Explain why a proof strategy is natural before executing it.
- Use cross-domain links only when they reveal a simpler proof, clearer
  invariant, computational method, or genuine historical motivation.
- Use diagrams, tables, HTML, or code when they clarify structure.
- Distinguish intuition from theorem from historical fact.
- Mention uncertainty when reconstructing historical motives.

Do not:

- Start with a modern definition unless the user asked for a definition.
- Hide failed attempts or counterexamples.
- Ridicule older methods as stupid or "wrong"; explain their local logic.
- Use modern tools to explain what a historical mathematician "must have" done.
- Overclaim historical causality without evidence.
- Force HTML, OCR, saving, or web search when the task is simple.

## Response Checklist

Before finalizing, verify:

- Motivation appears before formalism.
- A worked example, a boundary/degenerate case, and a counterexample or
  assumption-sharpness check appear for substantial proof tasks.
- The rigorous part states assumptions clearly.
- Cross-domain insight is included only if it clarifies the mechanism; otherwise
  it is intentionally skipped as noise.
- Historical/current claims are sourced or marked uncertain.
- OCR transcription ambiguities are visible.
- HTML/file artifacts are saved and paths are reported when generated.
