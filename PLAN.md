# IntuitMath — Project Plan

## 0. Vision

IntuitMath is a portable skill for autonomous AI agents (Hermes, OpenClaw, Claude, etc.) that makes them **think like a mathematician** when facing any mathematical question.

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
2. **A multi-agent workflow** that dispatches subagents to *search the web* for historical context, cross-domain connections, and applications
3. **Templates** for structured output (HTML with KaTeX)
4. **A problem library** for long-term accumulation

The reference files contain:
- `mathematician-thinking.md` — the core methodology (how to think, not what to know)
- `historical-methodology.md` — techniques for historical reconstruction (ported from Kimi math-history skill)
- `known-developments.md` — a seed case library (series, calculus, linear algebra, probability, number theory) — NOT comprehensive, but illustrative
- `cross-domain-patterns.md` — a seed pattern library — grows over time through use and research

**When the agent encounters a topic not covered in references, it MUST dispatch search subagents.** This is by design.

---

## 3. Multi-Agent Workflow

### 3.1 Overview

```
User Question
     │
     ▼
[Orchestrator] ── Analyzes question type, dispatches subagents
     │
     ├── [Researcher] ── Searches web for historical context,
     │                    biographical info, original motivations
     │
     ├── [Connector] ── Searches web for cross-domain connections,
     │                    alternative proofs, applications in
     │                    economics/biology/physics/CS
     │
     ├── [Deriver] ── Constructs the mathematical content:
     │                  pre-rigorous derivation → rigorous version
     │
     └── [Synthesizer] ── Integrates all findings, generates
                          final response (dialog or HTML)
```

### 3.2 The Research Subagent

**Role**: Historical and contextual research.

**Prompt template**:
```
You are a mathematical historian. For the concept [X]:
1. Who introduced it? When? In what paper/work?
2. What concrete problem were they trying to solve?
3. What mathematical tools did they ALREADY have at that time?
4. What tools were they MISSING?
5. What was their first bold attempt?
6. Where did it break down?
7. How did [X] fill the gap?

Search the web thoroughly. Provide specific dates, names, paper titles,
and historical context. Quote primary sources when possible.
```

### 3.3 The Connector Subagent

**Role**: Cross-domain connection mining.

**Prompt template**:
```
You are searching for cross-domain mathematical connections for [X].

Search for:
1. Alternative proofs from other branches (probability → analysis, 
   geometry → algebra, etc.) — the "Bernstein principle"
2. Applications in economics (game theory, optimization, mechanism design)
3. Applications in biology (population dynamics, phylogenetics, epidemiology)
4. Applications in physics (quantum mechanics, statistical mechanics, relativity)
5. Applications in computer science (cryptography, ML, complexity theory)
6. Historical surprises: cases where an application in Field A drove 
   the development of pure mathematics in Field B

For each connection, provide:
- The specific connection (1-2 sentences)
- Why it's illuminating
- Source URL if available
```

### 3.4 The Deriver Subagent

**Role**: Construct mathematical content.

**Instructions**:
1. Start with the **pre-rigorous** version: intuition, analogy, bold calculations
2. Annotate each step with motivation: `[Motivation: ...]` and `[Bold assumption: ...]`
3. Then present the **rigorous** version
4. If possible, show a **cross-domain alternative** proof
5. End with a **reflection anchor** — an open question for the user

### 3.5 The Synthesizer

**Role**: Integrate all subagent outputs into a coherent response.

**Decision**: Dialog mode or HTML mode?
- Default: dialog mode
- Switch to HTML if: user requests it, or the answer spans 3+ major sections

### 3.6 When to Activate Multi-Agent Mode

**Single-agent mode** (default):
- Simple questions, quick lookups
- Topics well-covered in reference files
- User wants a brief answer

**Multi-agent mode** (triggered when ANY of):
- Question involves concepts not in reference files
- User asks for "deep analysis" or "detailed exploration"
- Question touches 2+ mathematical branches
- Historical context is central to the question

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
│   └── cross-domain-patterns.md      # Seed pattern library
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
    └── (future: problem-saving utilities)
```

---

## 5. Implementation Roadmap

### Phase 1: Core Framework (current)
- [x] Research intellectual foundations
- [ ] Rewrite SKILL.md in English with improved design
- [ ] Rewrite references/mathematician-thinking.md in English
- [ ] Update references/cross-domain-patterns.md with research findings
- [ ] Update HTML template
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
