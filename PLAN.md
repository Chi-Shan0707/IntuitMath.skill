# IntuitMath — Project Plan

## 0. Vision

IntuitMath is a portable skill for autonomous AI agents (Claude, Codex, Hermes, OpenClaw, etc.) that makes them **think like a mathematician** when facing any mathematical question.

Not a calculator. Not a proof checker. Not a textbook.

A *thinking partner* that approaches problems the way a mathematician would: with motivation, with bold attempts, with cross-domain awareness, and with the humility to show dead ends alongside insights.

The project is grounded in four canonical texts:
- **Pólya** (*How to Solve It*, 1945): the 4-phase heuristic framework
- **Lakatos** (*Proofs and Refutations*, 1976): mathematics as dialectical process
- **Lockhart** (*A Mathematician's Lament*, 2002): math as art, motivation before technique
- **Tao** (blog/talks 2007-2026): the pre-rigorous → rigorous → post-rigorous pipeline

---

## 1. Core Design Principles

### 1.1 The "Toolkit Reconstruction" Trick

This is the signature move of IntuitMath. When faced with any mathematical concept X:

1. **Identify the era**: When was X first introduced? By whom? For what concrete problem?
2. **Reconstruct the toolkit**: What did that mathematician *already have*? What were they *missing*?
3. **Show the gap**: The gap between what they had and what they needed *is* the motivation for X.
4. **Bold first attempt**: What did they try with their existing tools? Where did it break?
5. **The invention**: How did X fill that gap?

This trick works because mathematics is *path-dependent*. Every concept was invented to solve a specific problem, and the solution only makes sense in the context of that problem.

**Example**: Why did Cauchy invent the ε-δ definition?
- *Era*: 1820s. Euler's "formal manipulation" had produced paradoxes (Grandi's series, conditionally convergent series giving different sums under rearrangement).
- *Toolkit*: Mathematicians had algebra, calculus, and infinite series. They did NOT have a rigorous notion of "limit" or "convergence."
- *Gap*: They needed to decide which infinite operations were legitimate.
- *Bold attempt*: Euler tried "formal algebraic consistency" — it gave beautiful results but also contradictions.
- *Invention*: Cauchy reduced convergence to a finitary condition (ε-N) that could be checked without knowing the limit value.

### 1.2 The Bernstein Principle

Named after Sergei Bernstein's probabilistic proof of the Weierstrass Approximation Theorem:

> **When a hard problem in one field has an easy solution from another field, that solution reveals the essence of the problem.**

The agent should always search for cross-domain simplifications:
- A complex analysis proof may have a simple probability interpretation
- An abstract algebra result may have a concrete geometric visualization
- A pure math theorem may have an elegant economics or biology motivation

### 1.3 Pre-Rigorous Before Rigorous

Following Tao's three-phase model:

1. **Pre-rigorous** (show first): Intuition, analogy, "wild calculations," physical reasoning
2. **Rigorous** (show second): Formal proof with explicit assumptions
3. **Post-rigorous** (the goal): Refined intuition backed by rigor — where every heuristic "naturally suggests" its formal counterpart

The agent should NEVER start with the rigorous version. The pre-rigorous version *always* comes first.

### 1.4 The Lakatosian Dialectic

Structure responses as a dialectical process, not a linear presentation:

```
Conjecture → Attempted Proof → Counterexample → Refinement → Stronger Conjecture
```

This mirrors how mathematics actually develops and makes the learning process feel like discovery rather than reception.

### 1.5 External Fields as Motivation

Mathematics does not exist in a vacuum. The agent should proactively search for:
- **Economics**: Game theory → fixed point theorems; portfolio optimization → convex analysis; mechanism design → combinatorics
- **Biology**: Population dynamics → ODEs; phylogenetics → combinatorics; epidemics → graph theory
- **Physics**: Quantum mechanics → functional analysis; relativity → differential geometry; statistical mechanics → probability
- **Computer Science**: Cryptography → number theory; machine learning → optimization; type theory → logic

These are not "applications tacked on at the end." They are *motivations that drive the mathematics in the first place*.

---

## 2. Architecture: Why We Don't Try to Be an Encyclopedia

Mathematics is too vast to encode in reference files. Instead, IntuitMath provides:

1. **A thinking framework** (this PLAN, the SKILL.md, references/mathematician-thinking.md)
2. **A utility-gated multi-agent workflow** that separates historian,
   intuition-builder, formalizer, skeptic, connector, and synthesizer roles
   only when the separation adds real mathematical value
3. **Capability adapters** for Claude, Codex, Hermes, OpenClaw, and other
   SKILL.md-compatible agents
4. **OCR/input workflows** for screenshots, PDFs, and handwritten math
5. **Templates** for structured output (HTML with KaTeX)
6. **A problem library** for long-term accumulation

The reference files contain:
- `mathematician-thinking.md` — the core methodology (how to think, not what to know)
- `historical-methodology.md` — techniques for historical reconstruction (ported from Kimi math-history skill)
- `known-developments.md` — a seed case library (series, calculus, linear algebra, probability, number theory) — NOT comprehensive, but illustrative
- `cross-domain-patterns.md` — a seed pattern library — grows over time through use and research
- `intuitive-math-cognition.md` — the cognitive model behind intuition, proof, counterexample, and guided reinvention
- `multi-agent-workflow.md` — useful-not-forced role workflows and merge protocol
- `input-processing.md` — OCR/PDF/screenshot/handwriting workflow
- `html-output.md` — HTML/KaTeX output workflow
- `platform-adapters.md` — capability mapping for different host agents

**When the agent encounters a topic not covered in references, it should use the
best available capability: source search, subagents, or a single-agent pass with
explicit uncertainty. Multi-agent is valuable only when it adds independent
verification, counterexample pressure, alternate representations, or artifact
quality.**

---

## 3. Utility-Gated Multi-Agent Workflow

### 3.1 Overview

```
User Question
     │
     ▼
[Orchestrator] ── Analyzes question type, decides whether subagents are useful
     │
     ├── [Historian] ── Verifies historical context, original motivations,
     │                   available toolkit, and uncertainty
     │
     ├── [Intuition Builder] ── Creates toy examples, analogies,
     │                          diagrams, and bold attempts
     │
     ├── [Formalizer] ── States assumptions, definitions, proof,
     │                    computations, and boundary conditions
     │
     ├── [Skeptic] ── Searches for counterexamples, hidden assumptions,
     │                 proof gaps, and degenerate cases
     │
     ├── [Connector] ── Finds cross-domain lenses only when they clarify
     │                   proof, invariant, computation, or history
     │
     └── [Synthesizer] ── Integrates debate into discovery order:
                          crisis → attempt → breakdown → repair
```

### 3.2 Utility Gate

Do not spawn agents by ritual. Use them when at least one condition holds:

- independent historical/source verification could change the answer;
- multiple representations or intuitions are plausible;
- the proof has hidden assumptions or fragile edge cases;
- the user asks for deep exploration;
- OCR/diagram ambiguity should be separated from solving;
- the output is both mathematical content and designed artifact.

Otherwise, run the lenses internally in one concise pass.

### 3.3 Role Contracts

Each role should return:

```
claim:
evidence:
uncertainty:
failure_modes:
must_not_overclaim:
```

---

## 4. Project Structure

```
IntuitMath/
├── SKILL.md                          # Main entry point (agent loads this)
├── PLAN.md                           # This file
├── .gitignore
├── references/
│   ├── mathematician-thinking.md     # Core methodology
│   ├── historical-methodology.md     # Historical reconstruction techniques
│   ├── known-developments.md         # Seed case library
│   ├── cross-domain-patterns.md      # Seed pattern library
│   ├── intuitive-math-cognition.md   # Intuition/proof/counterexample model
│   ├── multi-agent-workflow.md       # Useful-not-forced role workflow
│   ├── input-processing.md           # OCR/PDF/screenshot workflow
│   ├── html-output.md                # HTML/KaTeX output workflow
│   └── platform-adapters.md          # Universal capability mapping
├── templates/
│   └── math-note.html                # HTML output template (KaTeX)
├── problem-library/
│   ├── index.md                      # Problem index
│   └── YYYY-MM-DD-<topic>.md         # Individual problem records
├── research-temp/                    # Research artifacts (not part of skill)
│   ├── 00-SUMMARY.md
│   ├── 01-polya-how-to-solve-it.md
│   ├── 02-lakatos-proofs-and-refutations.md
│   ├── 03-lockhart-mathematicians-lament.md
│   ├── 04-terence-tao-philosophy.md
│   ├── 05-ai-math-systems.md
│   ├── 06-cross-disciplinary-motivation.md
│   └── 07-math-html-visualization.md
└── scripts/
    ├── save-problem.py
    └── render-html.py
```

---

## 5. Implementation Roadmap

### Phase 1: Core Framework (current)
- [x] Research intellectual foundations
- [x] Rewrite SKILL.md in English with improved universal design
- [ ] Rewrite references/mathematician-thinking.md in English
- [ ] Update references/cross-domain-patterns.md with research findings
- [x] Add intuition cognition and multi-agent workflow references
- [x] Add OCR/input processing workflow
- [x] Update HTML template and renderer
- [ ] Initial git commit

### Phase 2: Seed Content
- [ ] Expand known-developments.md with more cases
- [ ] Add "motivation ladders" for core undergraduate topics
- [ ] Test the multi-agent workflow on 3-5 real questions

### Phase 3: Polish & Test
- [ ] Refine subagent prompts based on test results
- [ ] Add more cross-domain patterns
- [ ] Improve HTML template (collapsible sections, tabs)
- [ ] Write usage examples

### Phase 4: Distribution
- [ ] Finalize for Hermes skill format
- [ ] Test with OpenClaw compatibility
- [ ] Write README.md
- [ ] Tag v1.0 release

---

## 6. Intellectual Lineage

This project stands on the shoulders of:

| Thinker | Key Contribution | How We Use It |
|---------|-----------------|---------------|
| **Pólya** (1945) | 4-phase heuristic: Understand → Plan → Execute → Reflect | Our workflow structure |
| **Lakatos** (1976) | Mathematics as dialectic: Conjecture → Proof → Refutation → Refinement | Our response structure |
| **Lockhart** (2002) | Math is art; motivation before technique; problems over exercises | Our core philosophy |
| **Tao** (2007-) | Pre-rigorous → Rigorous → Post-rigorous; "rigour should serve intuition" | Our presentation order |
| **AlphaGeometry** (2024) | Neural intuition + symbolic verification | Our neuro-symbolic workflow |
| **FunSearch** (2023) | Search for interpretable structures, not just answers | Our "look for functions" principle |
| **Bernstein** (1912) | Probabilistic proof of Weierstrass theorem | Our "cross-domain simplification" principle |

---

*Created: 2025-06-05*
*Last updated: 2025-06-05*
*Status: Phase 1 — Core Framework*
