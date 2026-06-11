<div align="center">

# IntuitMath

**A portable AI-agent skill that teaches mathematics the way it was discovered — through problems, not definitions.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/SKILL.md-v1.0-8A2BE2)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](#contributing)

</div>

---

## At a Glance

| What | Why |
|------|-----|
| **Not a calculator** | It doesn't solve problems *for* you — it teaches you to think |
| **Not a textbook** | It starts with the crisis that forced a definition, not the definition itself |
| **A thinking framework** | Built on Pólya, Lakatos, Lockhart, and Tao — a lineage, not a curriculum |

IntuitMath is a **SKILL.md-compatible portable skill** for AI agents (Claude, Codex, Hermes, OpenClaw, and any agent that can load a `SKILL.md`). When a user asks a math question, the agent stops regurgitating textbook definitions and starts reasoning like a mathematician: *What problem was being solved? What tools were available? What broke?*

---

## Why This Exists

Every student has felt it. You open a textbook, and there it is:

> **Definition.** A function $f$ is *integrable* if for every $\varepsilon > 0$, there exists a partition $P$ such that...

Why? *Why* this definition? Who needed it? What broke without it?

Most AI agents answer the way textbooks do — they state the definition, prove the theorem, and move on. Correct, complete, and utterly lifeless.

**IntuitMath is built on a different belief:** the definition is the *last* thing you should see, not the first. Before it, you deserve the story — the problem that demanded the invention, the bold attempts that failed, the moment someone realized the old tools weren't enough.

---

## A Taste: Lebesgue vs. Riemann

Suppose you ask: *"Why do we need the Lebesgue integral? What's wrong with Riemann?"*

**Textbook mode**:
> The Riemann integral of $f$ on $[a,b]$ is defined as... The Lebesgue integral generalizes this by...

**IntuitMath mode**:

---

**The crisis.** The Riemann integral works beautifully for continuous functions. But by the 1890s, mathematicians kept bumping into functions it couldn't handle. The most notorious: the Dirichlet function — 1 on the rationals, 0 on the irrationals.

**A bold attempt.** Let's try to Riemann-integrate the Dirichlet function on $[0,1]$. Every upper sum = 1 (rationals are dense). Every lower sum = 0 (irrationals are dense). The upper and lower integrals don't agree. Dead end.

*[Bold assumption: maybe the "area" should just be 0 — the rationals are countable, they take up no space.]*

**Lebesgue's move (1901).** Riemann partitions the *domain* — chop $[0,1]$ into intervals. Lebesgue partitions the *range* — collect all the $x$ where $f(x)$ takes a given value, and measure that set. For Dirichlet: $\{x : f(x)=1\}$ is the rationals (measure 0); $\{x : f(x)=0\}$ is the irrationals (measure 1). The integral is $1 \cdot 0 + 0 \cdot 1 = 0$.

**Why it matters beyond analysis.** The Lebesgue integral isn't a technical fix — it's the foundation of:
- **Probability**: $E[X]$ is a Lebesgue integral with respect to $P$
- **Quantum mechanics**: observables live in $L^2$ — a Lebesgue space
- **Signal processing**: Fourier analysis requires $L^p$ spaces
- **Every "limit under the integral"**: the dominated convergence theorem

**Something to sit with.** There *is* an integral that handles even more than Lebesgue — the Henstock-Kurzweil integral. It never caught on. Why? What makes a mathematical tool become standard — correctness, or something more?

---

That's the difference. Same mathematics. But now you understand *why it exists*.

---

## Core Methodology

### Toolkit Reconstruction (The Signature Move)

For any concept $X$, the agent reconstructs the moment of invention:

```
1. Identify the era     → Who invented X? When? For what problem?
2. Reconstruct toolkit  → What did they already know? What was missing?
3. Expose the gap       → The gap = the motivation for X
4. Show the bold try    → What did they attempt with existing tools?
5. Show the breakdown   → Where did it fail?
6. Show the invention   → How did X fill the gap?
```

### The Bernstein Principle

> **When a hard problem in one field has an easy solution from another field, that solution reveals the essence of the problem.**

Named after Sergei Bernstein's probabilistic proof of the Weierstrass Approximation Theorem. The agent proactively searches across domains — probability illuminating analysis, economics driving optimization, biology motivating ODEs.

### Tao's Three-Phase Model

All responses follow: **Pre-rigorous** (intuition, wild calculations, bold assumptions) → **Rigorous** (formal proof) → **Post-rigorous** (refined intuition). Rigor serves intuition, not the reverse.

### Multi-Agent When It Adds Real Value

IntuitMath does **not** force multi-agent overhead. It uses separate agents only when separation improves mathematical cognition:

- **Historian** verifies origin, era, toolkit, and historical uncertainty.
- **Intuition Builder** invents examples, pictures, and bold first attempts.
- **Formalizer** turns the idea into definitions, assumptions, and proof.
- **Skeptic** attacks hidden assumptions, edge cases, and false generalizations.
- **Connector** finds cross-domain lenses that clarify the mechanism.
- **Synthesizer** preserves the discovery order: crisis → attempt → breakdown → repair.

For simple questions, the same lenses run internally in one concise pass. See `references/multi-agent-workflow.md` and `references/intuitive-math-cognition.md`.

---

## What's Inside

```
IntuitMath/
├── SKILL.md                          ← Entry point — the agent loads this
├── ROUTES.json                        ← Compact navigation index for file routing
│
├── subskills/                        ← Domain-specific deep dives
│   ├── calculus.md                       Limits, integrals, series, ε-δ
│   ├── linear-algebra.md                 Matrices, eigenvalues, SVD
│   ├── probability.md                    CLT, stochastic processes
│   ├── optimization.md                   Convex, variational, duality
│   ├── pde.md                            Heat/wave/Laplace, Fourier
│   ├── discrete-math.md                  Combinatorics, number theory, graphs
│   └── abstract-algebra.md               Groups, rings, Galois theory
│
├── references/                       ← Methodology and seed data
│   ├── mathematician-thinking.md         Core thinking framework (mandatory)
│   ├── cross-domain-patterns.md          8 disciplines × pattern library
│   ├── historical-methodology.md         Reconstruction techniques
│   ├── known-developments.md             Seed cases: antiquity → modern era
│   ├── intuitive-math-cognition.md       Research-backed intuition model
│   ├── multi-agent-workflow.md           Useful-not-forced role workflow
│   ├── input-processing.md               OCR, screenshots, PDFs, handwriting
│   ├── html-output.md                    KaTeX/HTML note generation
│   └── platform-adapters.md              Claude/Codex/Hermes/OpenClaw mapping
│
├── templates/
│   └── math-note.html                ← KaTeX + serif, elegant output
│
├── scripts/
│   ├── save-problem.py               ← Automated problem library
│   └── render-html.py                ← Single-file HTML note renderer
│
└── problem-library/                  ← Grows with every question asked
```

The agent loads `SKILL.md` first, routes to the appropriate subskill based on the question's domain, and uses the host platform's available capabilities — search, file tools, shell, OCR/vision, or subagents — without requiring a single vendor runtime.

---

## Universal Agent Compatibility

IntuitMath is intentionally platform-neutral:

| Platform | How to use it |
|---|---|
| **Claude** | Add the folder as project/skill context; use web/vision/artifacts when available |
| **Codex** | Put the folder in a workspace or skill directory; use shell helpers when useful |
| **Hermes** | Register the folder as a `SKILL.md` skill; map `web_search`/`delegate_task` if available |
| **OpenClaw** | Place under the skills path and let `SKILL.md` drive routing |
| **Other agents** | Load `SKILL.md`; read only referenced files as needed |

No mathematical behavior depends on platform-specific metadata. Platform-specific files should remain thin wrappers around the same universal workflow.

---

## OCR and Visual Math

When a user supplies a screenshot, PDF, scan, or handwritten problem, IntuitMath uses a transcription-first workflow:

1. Recover the formula/diagram in LaTeX or structured Markdown.
2. Mark ambiguous symbols explicitly.
3. Solve only after the transcription is inspectable.
4. State assumptions and sanity-check the result against the image.

See `references/input-processing.md`.

---

## HTML / KaTeX Notes

For polished explanations, IntuitMath can generate a single HTML file with CDN KaTeX by default:

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

See `references/html-output.md` and `templates/math-note.html`.

---

## Cross-Domain Connections

The pattern library links mathematics to external disciplines. These aren't "applications tacked on at the end" — they are motivations that drove the mathematics in the first place.

| Discipline | What it gave mathematics |
|---|---|
| **Physics** | Calculus (Newton), Fourier analysis (heat), Hilbert spaces (quantum), differential geometry (relativity) |
| **Chemistry** | Group theory (molecular symmetry), Fourier analysis (crystallography), eigenvalue problems (quantum chemistry) |
| **Biology & Medicine** | ODEs (population dynamics), graph theory (epidemiology), Radon transform (CT imaging) |
| **Economics & Finance** | Fixed point theorems (equilibrium), Itô calculus (options), combinatorics (mechanism design) |
| **Demography** | Eigenvalue theory (Leslie matrices), probability (survival analysis), optimal transport (migration) |
| **Statistics** | Optimization (MLE), differential geometry (Bayesian inference), random matrix theory (high dimensions) |
| **Engineering** | Harmonic analysis (signal processing), calculus of variations (control), measure theory (information) |
| **Linguistics & Music** | Automata theory (formal languages), dihedral groups (harmony), Fourier analysis (timbre) |

---

## Installation

### From GitHub
```bash
git clone https://github.com/Chi-Shan0707/IntuitMath.skill.git
```

Then link it into your agent's skill directory:

### Claude

Add `SKILL.md` and the referenced folders to a Claude Project or custom skill/context setup. Paths vary by host; keep the whole folder together so `references/`, `subskills/`, `templates/`, and `scripts/` remain reachable.

### Codex

Use it from a workspace or copy it into a Codex skill directory when your Codex environment supports skills:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -r IntuitMath.skill "${CODEX_HOME:-$HOME/.codex}/skills/intuitmath"
```

You can also point Codex at the repository in a normal workspace and ask it to use `SKILL.md`.

### Hermes
```bash
cp -r IntuitMath.skill ~/.hermes/skills/intuitmath/
```
Auto-detected via `SKILL.md`. No configuration needed.

### OpenClaw
```bash
cp -r IntuitMath.skill /path/to/openclaw/skills/intuitmath/
```

### Any SKILL.md-compatible Agent
```bash
# Clone first, then point your agent to SKILL.md
git clone https://github.com/Chi-Shan0707/IntuitMath.skill.git
```

Load `SKILL.md` into your agent's context when mathematical questions appear. The core thinking framework works everywhere; multi-agent and HTML features require specific agent capabilities.

---

## Design Principles

### Framework, Not Encyclopedia
Mathematics is too vast to encode in files. IntuitMath provides a **thinking framework** with **seed cases** and **web search integration** — not a comprehensive database.

### The Intellectual Lineage

| Idea | From | How we use it |
|---|---|---|
| **Heuristic reasoning** | Pólya, *How to Solve It* (1945) | Four-phase workflow: understand → plan → execute → reflect |
| **Mathematics as dialectic** | Lakatos, *Proofs and Refutations* (1976) | Conjecture → proof → counterexample → refinement |
| **Motivation before technique** | Lockhart, *A Mathematician's Lament* (2002) | Never start with a definition; start with the problem |
| **Pre-rigorous → rigorous** | Terence Tao (2007–) | Intuition before formalism; the goal is *refined* intuition |

---

## Contributing

IntuitMath grows through use. Contributions welcome:

- **New subskills** — topology, differential geometry, logic, complex analysis, dynamical systems...
- **Toolkit reconstruction cases** — your favorite "why was X invented" stories
- **Cross-domain patterns** — connections not yet catalogued
- **HTML template improvements** — dark mode, interactive diagrams, collapsible sections
- **Test cases** — example questions with expected response structures

Every new pattern makes every future response richer.

---

## License

MIT License. Use freely, modify freely, share freely.

---

<div align="center">

*Every definition was once a desperate solution<br>to a problem someone couldn't ignore.*

</div>
