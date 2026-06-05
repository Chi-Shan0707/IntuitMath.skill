<div align="center">

# IntuitMath

**Teach your AI agent to think like a mathematician.**

*A portable skill for Hermes, OpenClaw, and any SKILL.md-compatible agent.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## The Problem

Every student has felt it. You open a textbook, and there it is:

> **Definition.** A function $f$ is *integrable* if for every $\varepsilon > 0$, there exists a partition $P$ such that...

Why? Why this definition? Who needed it? What broke without it?

Most AI agents answer the same way textbooks do — they state the definition, prove the theorem, and move on. Correct, complete, and utterly lifeless.

**IntuitMath is built on a different belief**: the definition is the *last* thing you should see, not the first. Before it, you deserve the story — the problem that demanded the invention, the bold attempts that failed, the moment someone realized the old tools weren't enough.

---

## What IntuitMath Does

When your agent loads IntuitMath, it stops behaving like a textbook and starts behaving like a mathematician:

**It starts with motivation.** Every concept is introduced through the original problem that motivated it. The ε-δ definition appears because Euler's formal algebra produced paradoxes. Lebesgue integration appears because the Dirichlet function broke Riemann. Galois theory appears because 200 years of failing to solve the quintic demanded a structural explanation.

**It reconstructs the toolkit.** For any concept X, the agent goes back to the inventor's era: what tools did they *already have*? What were they *missing*? The gap between the two is the motivation. This is the signature move — we call it **toolkit reconstruction**.

**It shows intuition before rigor.** Following Terence Tao's three-phase model, the agent always presents the *pre-rigorous* version first — wild calculations, physical reasoning, bold assumptions annotated as such — and only then the formal proof. Intuition is not a poor cousin of rigor. It is the thing rigor serves.

**It searches across domains.** Named after Sergei Bernstein's probabilistic proof of the Weierstrass theorem, the **Bernstein principle** says: when a hard problem in one field has an easy solution from another field, that solution reveals the essence of the problem. The agent proactively looks for these connections — probability illuminating analysis, economics driving optimization, physics motivating PDEs, chemistry demanding group theory.

**It dispatches research subagents.** For deep questions, the skill sends parallel subagents to search the web for historical context and cross-domain connections, then synthesizes their findings into a single coherent narrative.

---

## A Taste

Suppose you ask: *"Why do we need the Lebesgue integral? What's wrong with Riemann?"*

A textbook says:

> The Riemann integral of $f$ on $[a,b]$ is defined as... The Lebesgue integral generalizes this by...

IntuitMath says something closer to this:

---

**The crisis.** The Riemann integral works beautifully for continuous functions on $[a,b]$. But by the 1890s, mathematicians kept bumping into functions it couldn't handle. The most notorious: the Dirichlet function, which is 1 on the rationals and 0 on the irrationals.

**A bold attempt.** Let's try to Riemann-integrate the Dirichlet function on $[0,1]$. Every upper sum equals 1 (rationals are dense). Every lower sum equals 0 (irrationals are dense). The upper and lower integrals don't agree. Dead end.

*[Bold assumption: maybe the "area" should just be 0 — the rationals are countable, they take up no space.]*

**Lebesgue's move (1901).** Riemann partitions the *domain* — chop $[0,1]$ into intervals. Lebesgue partitions the *range* — collect all the $x$ where $f(x)$ takes a given value, and measure how much of the domain that set occupies. For the Dirichlet function: the set $\{x : f(x) = 1\}$ is the rationals, which have measure 0. The set $\{x : f(x) = 0\}$ is the irrationals, which have measure 1. So the integral is $1 \cdot 0 + 0 \cdot 1 = 0$. Done.

**Why it matters beyond analysis.** The Lebesgue integral isn't just a technical fix. It turns out:
- In probability, $E[X]$ *is* a Lebesgue integral with respect to $P$
- In quantum mechanics, observables live in $L^2$ — a Lebesgue space
- In signal processing, Fourier analysis requires $L^p$ — Lebesgue spaces
- The dominated convergence theorem — a Lebesgue result — is the workhorse that justifies "limit under the integral sign" in every application

**Something to sit with.** There *is* an integral that handles even more than Lebesgue — the Henstock-Kurzweil integral. But it never caught on. Why? What does it take for a mathematical tool to become standard — correctness, or something more?

---

That's the difference. Same mathematics. But now you understand *why it exists*.

---

## Installation

### Hermes

```bash
cp -r IntuitMath ~/.hermes/skills/intuitmath/
```

Auto-detected via `SKILL.md`. No configuration needed.

### OpenClaw

```bash
cp -r IntuitMath /path/to/openclaw/skills/intuitmath/
```

### Any Agent

Load `SKILL.md` into your agent's context when mathematical questions appear.
The skill degrades gracefully: multi-agent research requires `delegate_task`,
HTML output requires `write_file`, but the core thinking framework works
everywhere.

---

## Architecture

```
IntuitMath/
├── SKILL.md                          ← Entry point — the agent loads this
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
│   └── known-developments.md             Seed cases: antiquity → modern era
│
├── templates/
│   └── math-note.html                ← KaTeX + Literata, elegant output
│
├── scripts/
│   └── save-problem.py               ← Automated problem library
│
└── problem-library/                  ← Grows with every question asked
```

The agent loads `SKILL.md` first, then routes to the appropriate subskill
based on the question's domain. Each subskill contains motivation ladders,
toolkit reconstruction cases, cross-domain connections, and reflection
anchors — structured content the agent can weave into a narrative.

---

## Cross-Domain Connections

The pattern library links mathematics to eight external disciplines.
These aren't "applications tacked on at the end" — they are motivations
that drove the mathematics in the first place.

| Discipline | What it gave mathematics |
|-----------|-------------------------|
| **Physics** | Calculus (Newton), Fourier analysis (heat), Hilbert spaces (quantum), differential geometry (relativity) |
| **Chemistry** | Group theory (molecular symmetry), Fourier analysis (crystallography), eigenvalue problems (quantum chemistry) |
| **Biology & Medicine** | ODEs (population dynamics), graph theory (epidemiology), Radon transform (CT imaging) |
| **Economics & Finance** | Fixed point theorems (equilibrium), Itô calculus (options pricing), combinatorics (mechanism design) |
| **Demography** | Eigenvalue theory (Leslie matrices), probability (survival analysis), optimal transport (migration) |
| **Statistics** | Optimization (MLE), differential geometry (Bayesian inference), random matrix theory (high dimensions) |
| **Engineering** | Harmonic analysis (signal processing), calculus of variations (control), measure theory (information) |
| **Linguistics & Music** | Automata theory (formal languages), dihedral groups (harmony), Fourier analysis (timbre) |

When the seed library doesn't cover a connection, the agent searches the web
and can add newly discovered patterns back to the library for future use.

---

## Design Principles

### Framework, Not Encyclopedia

Mathematics is too vast to encode in files. There are dozens of major
branches, each with centuries of development. IntuitMath doesn't try.
Instead it provides:
- A **thinking framework** — how to think, not what to know
- **Seed cases** that demonstrate the methodology
- **Web search integration** for everything beyond the seeds

The subskills and reference files grow over time through use.

### The Intellectual Lineage

Four ideas converge in IntuitMath:

| Idea | From | How we use it |
|------|------|---------------|
| **Heuristic reasoning** | Pólya, *How to Solve It* (1945) | The four-phase workflow: understand → plan → execute → reflect |
| **Mathematics as dialectic** | Lakatos, *Proofs and Refutations* (1976) | Responses structured as conjecture → proof → counterexample → refinement |
| **Motivation before technique** | Lockhart, *A Mathematician's Lament* (2002) | Never start with a definition; start with the problem that demanded it |
| **Pre-rigorous → rigorous → post-rigorous** | Terence Tao (2007–) | Intuition always precedes formalism; the goal is *refined* intuition |

---

## Contributing

IntuitMath grows through use. Contributions welcome:

- **New subskills** — topology, differential geometry, logic, dynamical systems, complex analysis, measure theory...
- **Toolkit reconstruction cases** — your favorite "why was X invented" stories
- **Cross-domain patterns** — connections we haven't catalogued yet
- **HTML template improvements** — collapsible sections, dark mode, interactive diagrams
- **Test cases** — example questions with expected response structures

Every new pattern or subskill makes every future response richer.

---

## License

MIT License. Use freely, modify freely, share freely.

---

<div align="center">

*Every definition was once a desperate solution<br>to a problem someone couldn't ignore.*

</div>
