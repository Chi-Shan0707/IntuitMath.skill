# Multi-Agent Mathematical Cognition

Use this reference when a host can run subagents, parallel tasks, separate tool
passes, or explicit role-based reasoning **and** the task benefits from separate
cognitive modes. The goal is not just speed. The goal is to approximate how
mathematicians think together: one person invents a picture, another tries to
break it, another formalizes it, and another notices that the same structure
already exists in physics, probability, or geometry.

Multi-agent work is not mandatory. It is a tool for increasing mathematical
truth, intuition, and communicability. If it adds overhead without adding a
distinct check, discovery path, or representation, do not use it.

## Core Principle

Separate incompatible cognitive modes:

- **Inventive mode** wants analogies, guesses, pictures, and bold leaps.
- **Critical mode** wants counterexamples, hidden assumptions, and edge cases.
- **Formal mode** wants definitions, quantifiers, proof, and computation.
- **Historical mode** wants source-grounded motivation and path dependence.
- **Connective mode** wants other domains where the same structure is simpler.

Do not ask one agent to do all modes at once for deep tasks. That produces
textbook answers with a thin "intuition" wrapper.

## Utility Gate

Before spawning or delegating, answer these questions:

| Question | Use multi-agent if the answer is yes |
|---|---|
| Would independent historical/source verification change the answer? | Historian |
| Are there multiple plausible intuitions or representations? | Intuition Builder + Connector |
| Could a beautiful explanation hide a false claim? | Skeptic |
| Does the proof depend on assumptions the user may not notice? | Formalizer + Skeptic |
| Could another branch give a simpler proof or model? | Connector |
| Is there image/OCR ambiguity? | Transcriber + Solver + Skeptic |
| Is the output also a designed artifact? | Math Synthesizer + Visual Designer |

If none apply, stay single-agent. If only one applies, use only that role or run
that lens internally. A two-agent exchange that checks a proof can be better
than a six-agent ritual.

## Research-Informed Model of Mathematical Intuition

Use multi-agent roles to preserve these complementary forces:

- **Pólya**: problem solving needs understanding, planning, execution, and
  looking back; the "look back" step should become a Skeptic/Reflector role.
- **Hadamard**: invention often cycles through preparation, incubation,
  illumination, and verification; Intuition Builder should not be forced to
  formalize too early, while Formalizer handles verification.
- **Poincaré**: logic gives demonstration, intuition guides invention; the
  workflow should keep both rather than letting one erase the other.
- **Lakatos**: proofs, counterexamples, and concept refinement co-evolve; the
  Skeptic should improve definitions, not merely reject ideas.
- **Tao**: rigor should destroy bad intuition and elevate good intuition; the
  Synthesizer should end in post-rigorous understanding where heuristics and
  formal proof point to each other.
- **Freudenthal/RME**: learners should be guided to reinvent concepts through
  meaningful phenomena and emergent models; Intuition Builder should create a
  route of rediscovery, not just an analogy.

This is why the roles are separated: each role protects one part of real
mathematical cognition.

## Role Set

### 1. Orchestrator

Owned by the main agent.

- Classify the problem.
- Choose roles and assign narrow tasks.
- Prevent duplicated work.
- Keep the final answer coherent and mathematically correct.
- Decide whether the output should be dialog, Markdown, HTML, or a saved record.

### 2. Historian

Question: *Why did this idea have to be invented?*

Deliver:

- Era, people, source names, and dates when available.
- The concrete problem or crisis.
- Toolkit available at the time.
- What was missing.
- Caution labels for uncertain or disputed claims.
- Labels separating verified history, plausible reconstruction, and pedagogical
  analogy.

Do not derive the proof unless asked. Provide evidence and motivation.

### 3. Intuition Builder

Question: *What would make the idea feel inevitable before rigor?*

Deliver:

- Toy examples.
- Geometric, physical, probabilistic, or computational pictures.
- Bold attempts and why they feel natural.
- A "first wrong idea" that almost works.
- A bridge from the toy example to the general claim.

Do not hide non-rigorous assumptions. Mark them.

### 4. Formalizer

Question: *What exact theorem, definition, proof, or computation repairs the
intuition?*

Deliver:

- Precise assumptions and definitions.
- Formal derivation/proof.
- Boundary conditions and domains.
- A short explanation of why this proof strategy matches the intuition.

Do not start from definitions without explaining their job.

### 5. Skeptic / Refuter

Question: *Where can this story fail?*

Deliver:

- Smallest counterexample to overbroad claims.
- Hidden assumptions.
- Edge cases and degenerate cases.
- Common student misconception.
- Whether the proposed proof handles all cases.

The Skeptic is not negative for its own sake. The Skeptic protects the answer
from becoming a beautiful false story.

### 6. Connector

Question: *Where does another field reveal the same structure more clearly?*

Deliver:

- Cross-domain analogies or applications.
- Alternative proofs from another branch.
- "Bernstein principle" candidates: hard in one lens, easy in another.
- Why the connection is illuminating, not just decorative.

### 7. Synthesizer

Question: *What should the learner see, and in what order?*

Deliver:

1. Motivation/crisis.
2. Intuitive attempt.
3. Refutation or breakdown.
4. Rigorous repair.
5. Cross-domain lens.
6. Reflection anchor.

The Synthesizer must preserve disagreements when they matter.

## Role Output Contract

Ask each role to return these fields when practical:

```text
claim:
evidence:
uncertainty:
failure_modes:
must_not_overclaim:
```

For roles where a field is not relevant, write `not applicable`. This prevents
beautiful prose from hiding missing evidence or assumptions.

## Dispatch Patterns

### Concept Motivation

Use:

- Historian
- Intuition Builder
- Skeptic
- Connector
- Synthesizer

Prompt shape:

```text
Historian: For [concept], reconstruct the original problem, era, available
toolkit, missing tool, and source-grounded caveats. Do not write the final
answer.

Intuition Builder: For [concept], invent the simplest toy examples, bold
attempts, and visual/physical analogies that make the concept feel necessary.

Skeptic: Find where the naive story for [concept] breaks. Give counterexamples,
edge cases, and hidden assumptions.

Connector: Find cross-domain lenses or alternative proofs for [concept].
Prioritize illuminating connections over long application lists.
```

### Proof / Theorem

Use:

- Intuition Builder
- Formalizer
- Skeptic
- Connector if a second proof might exist

Prompt shape:

```text
Intuition Builder: Explain why the theorem [T] should be true using examples,
pictures, or heuristics. Mark non-rigorous assumptions.

Formalizer: Prove [T] under explicit assumptions. Explain why this proof
strategy is natural given the intuition.

Skeptic: Try to break [T] by weakening assumptions. Produce counterexamples or
state why the assumptions are necessary.
```

Required synthesis shape:

```text
naive conjecture -> attempted proof -> obstruction/counterexample ->
refined theorem -> rigorous proof -> post-rigorous intuition
```

The final answer should not present the refined theorem as if it was obvious
from the start.

### Problem Solving

Use:

- Solver/Formalizer
- Skeptic
- Explainer/Synthesizer

Prompt shape:

```text
Solver: Solve the problem cleanly and show the method.

Skeptic: Check the solution for algebra errors, missing cases, domain issues,
and sanity checks.

Explainer: Rewrite the solution so the method feels motivated rather than
mechanical.
```

### OCR / Diagram Problem

Use:

- Transcriber
- Solver
- Skeptic

Prompt shape:

```text
Transcriber: Recover the math from the image/PDF. Preserve layout and mark
uncertain symbols. Do not solve.

Solver: Solve from the transcription and state assumptions.

Skeptic: Check whether OCR ambiguity could change the result.
```

### HTML Note

Use:

- Mathematical Synthesizer
- Visual Designer
- Skeptic

Prompt shape:

```text
Mathematical Synthesizer: Produce the motivation, intuition, rigor,
cross-domain, and reflection sections.

Visual Designer: Convert the sections into template-friendly HTML blocks with
KaTeX-safe math and clear visual hierarchy.

Skeptic: Check mathematical accuracy, KaTeX syntax, and whether the note starts
with motivation rather than definitions.
```

## Merge Protocol

When results return:

1. **Create a claim table**: claim, source/role, confidence, conflict status.
2. **Resolve conflicts**:
   - If mathematical, decide by proof or counterexample.
   - If historical, prefer primary/high-quality sources and mark uncertainty.
   - If pedagogical, choose the explanation that best supports the user's level.
   - If cross-domain, keep only connections that reveal a proof strategy,
     invariant, model, computation, or genuine historical motivation.
3. **Preserve productive failure**: include the wrong attempt if it teaches why
   the rigorous concept is needed.
4. **Write in discovery order**: crisis → attempt → breakdown → repair.
5. **Run final skeptic pass**: assumptions, edge cases, notation, arithmetic.

## When Not to Spawn

Avoid multi-agent overhead for:

- Simple arithmetic.
- A user-requested one-line answer.
- A well-known fact where no proof or motivation is requested.
- Environments where delegation would expose private data.
- Cases where all roles would use the same context and produce the same answer.
- Time-sensitive interactions where a quick correct explanation is better.

In those cases, simulate the roles briefly in one pass.

## Minimal Sequential Version

If the platform has no subagents, do this internally:

```text
Historian lens: What problem created this?
Inventor lens: What would I try first?
Skeptic lens: Where does that fail?
Formalizer lens: What exact structure fixes it?
Connector lens: Where else does the same idea appear?
Synthesizer lens: What order helps the learner rediscover it?
```

## Quality Gates

- The Intuition Builder's output must contain at least one concrete example.
- The Skeptic's output must contain at least one edge case, counterexample, or
  explicit statement that no counterexample was found under the assumptions.
- The Formalizer must state assumptions.
- The Connector must explain why a connection illuminates the concept.
- The Synthesizer must not erase uncertainty or failed attempts.
