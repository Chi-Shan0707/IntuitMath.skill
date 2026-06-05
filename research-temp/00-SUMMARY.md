# Research Summary: IntuitMath Skill

## What We Found

### 1. The Intellectual Foundations (4 canonical texts)

**Pólya (1945)** - "How to Solve It"
- 4-phase problem-solving: Understand -> Plan -> Execute -> Reflect
- Rich dictionary of heuristics (analogy, specialization, working backward, etc.)
- Maps to our workflow: Motivation -> Derivation -> Verification -> Reflection

**Lakatos (1976)** - "Proofs and Refutations"
- Mathematics grows through dialectical process: conjecture -> proof -> refutation -> refinement
- Definitions are not fixed - they evolve through counterexamples
- "Monster-barring", "lemma-incorporation" as named techniques
- THIS IS THE FOUNDATIONAL TEXT for our project

**Lockhart (2002)** - "A Mathematician's Lament"
- Math is art, not facts
- "By concentrating on what, and leaving out why, mathematics is reduced to an empty shell"
- Problems > exercises; struggle is productive
- History and philosophy should be integral

**Tao (2007-2026)** - Blog posts and talks
- Three phases: pre-rigorous -> rigorous -> post-rigorous
- "Rigour should serve intuition, not destroy it"
- Freedom to fail; ask dumb questions
- Write everything down; partial progress matters

### 2. AI Systems Already Doing This (2023-2026)

**AlphaGeometry** - Neuro-symbolic: LM (intuition) + symbolic engine (rigor)
**FunSearch** - LLM + evaluator; searches for PROGRAMS not solutions; first new discoveries in open problems
**Prover Agent** - Generates auxiliary lemmas when stuck
**SciAgent** - Hierarchical Coordinator -> Worker -> Subagent structure
**Ax-Prover** - Orchestrator + Prover + Verifier pattern
**ETP** - Crowdsourced collaborative math with formal verification

### 3. Cross-Disciplinary Motivation

**Biology -> Math**: Evolution -> statistics, genome sequencing -> combinatorics, neural signaling -> PDEs
**Economics -> Math**: Portfolio theory -> convex optimization, game theory -> fixed point theorems
**Physics -> Math**: Quantum mechanics -> functional analysis, relativity -> differential geometry

Key pattern: REAL PROBLEMS in other fields drive PURE MATHEMATICS

### 4. HTML Visualization

- **KaTeX** is the right choice (fast, lightweight, sufficient)
- Our template already follows best practices
- Future: interactive elements, animated derivations

---

## Key Design Implications for IntuitMath

### Architecture
1. **Neuro-symbolic split**: Separate "intuitive reasoning" from "formal verification"
2. **Multi-agent**: Coordinator -> Specialists -> Verifiers (proven effective)
3. **Auxiliary lemma generation**: When stuck, generate related lemmas

### Content
1. **Always start with motivation** - why was this problem posed?
2. **Always show the pre-rigorous version first** - intuition before formalism
3. **Always search for cross-domain connections** - Bernstein principle
4. **Always include "Look back"** - what did we learn? What can we reuse?

### Workflow
1. **Lakatosian dialectic**: Conjecture -> Attempt -> Refine -> New Conjecture
2. **Pólya's heuristics**: Search for analogous problems, decompose, work backward
3. **Tao's post-rigorous**: Heuristics and rigor should inform each other

### Output
1. **Default**: Dialog mode with structured sections
2. **Optional**: HTML with KaTeX, warm typography, comparison panels
3. **Future**: Interactive notebooks, animated derivations

---

## Files in This Research Folder

| File | Content |
|------|---------|
| `01-polya-how-to-solve-it.md` | Pólya's 4-phase framework and heuristics |
| `02-lakatos-proofs-and-refutations.md` | Lakatos's dialectical method |
| `03-lockhart-mathematicians-lament.md` | Lockhart's art-of-explanation philosophy |
| `04-terence-tao-philosophy.md` | Tao's three-phase model and problem-solving advice |
| `05-ai-math-systems.md` | AlphaGeometry, FunSearch, Prover Agent, SciAgent, Ax-Prover, ETP |
| `06-cross-disciplinary-motivation.md` | Biology/economics/physics/CS -> math motivation |
| `07-math-html-visualization.md` | KaTeX, MathJax, interactive notebooks, HTML design |

All files are in `/mnt/d/CS/SKILLS/IntuitMath/research-temp/`
