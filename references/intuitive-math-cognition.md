# Intuitive Mathematical Cognition

Use this reference when shaping an answer so it feels like mathematical
rediscovery rather than textbook delivery. It explains the cognitive backbone
behind IntuitMath and the multi-agent workflow.

## The Central Claim

Mathematical intuition is not a vague feeling that replaces proof. It is a
network of examples, representations, analogies, failed attempts, and compressed
proof experience. Good rigor does not kill intuition; it filters and upgrades
it.

## Six Lenses of Mathematical Understanding

### 1. Problem Before Definition

A definition is a repair tool. It should appear after the learner has seen the
problem it repairs.

Use:

```text
crisis -> naive attempt -> failure -> need for a new distinction -> definition
```

Avoid:

```text
definition -> theorem -> proof -> application
```

unless the user explicitly asks for a definition.

### 2. Toolkit Reconstruction

To understand a concept, temporarily remove the later tools that make it look
obvious. Ask what was available at the time and what was missing.

This prevents "historian's fallacy": explaining Newton, Euler, Cauchy, or
Noether using concepts they did not have.

### 3. Guided Reinvention

Do not simply tell the answer. Build a path where the learner almost reinvents
it:

1. Choose a phenomenon that creates pressure.
2. Let a natural model emerge from that phenomenon.
3. Show why the model is insufficient.
4. Refine the model into the formal concept.
5. Reuse the refined model on a new problem.

This works for pure topics too: the "phenomenon" can be an internal
mathematical pattern, not a real-world story.

### 4. Examples as Laboratories

Examples are not decorations. They are experiments in the mathematical world.

Use at least one of:

- Minimal example: the smallest case where the idea exists.
- Generic example: a case that displays the main mechanism.
- Pathological example: a case that breaks naive intuition.
- Boundary example: a limiting or degenerate case.
- Transfer example: the same structure in another domain.

### 5. Counterexamples as Sculptors

Counterexamples do not merely destroy claims. They sculpt better definitions.

When a naive claim fails:

1. Identify whether the counterexample attacks the conjecture, a lemma, or an
   unstated definition.
2. Decide whether to restrict hypotheses, refine definitions, or seek a new
   invariant.
3. Explain what the counterexample teaches.

This is the Lakatosian move: proof and refutation co-create the concept.

### 6. Post-Rigorous Compression

After the formal proof, return to intuition:

- Which heuristic survived?
- Which heuristic was repaired?
- What is now safe to say informally?
- What mental picture should the user keep?

The best ending is not "QED"; it is a refined intuition that can guide the next
problem.

## Multi-Agent Mapping

| Cognitive lens | Agent role |
|---|---|
| Historical pressure | Historian |
| Guided reinvention | Intuition Builder |
| Example laboratory | Intuition Builder + Skeptic |
| Definition repair | Skeptic + Formalizer |
| Proof discipline | Formalizer |
| Transfer and compression | Connector + Synthesizer |

Use separate agents only when separation protects the work. For a simple
question, these can be internal checklist items.

## Response Pattern

```markdown
## The Pressure
What problem makes the concept necessary?

## The First Natural Attempt
What would a smart person try before knowing the modern theory?

## Where It Breaks
What example, ambiguity, or contradiction forces refinement?

## The Repair
What definition/theorem/proof fixes exactly that failure?

## The Bigger Shape
Where does the same structure reappear?

## What To Keep
What refined intuition should the learner carry forward?
```

## Common Failure Modes

- **Pretty but false**: vivid analogy with no Skeptic pass.
- **Rigorous but dead**: correct proof with no pressure or examples.
- **Fake history**: confident origin story without source support.
- **Application dumping**: long list of applications without explaining what
  they reveal.
- **Forced multi-agent**: many roles that all restate the same idea.
- **Premature formalization**: definitions arrive before the learner feels why
  they are needed.

## Source Anchors

These are intellectual anchors, not exhaustive authorities:

- Pólya, *How to Solve It*: understand, plan, execute, look back.
- Hadamard, *The Psychology of Invention in the Mathematical Field*:
  preparation, incubation, illumination, verification.
- Poincaré, "Intuition and Logic in Mathematics": intuition as an instrument of
  invention and logic as an instrument of demonstration.
- Lakatos, *Proofs and Refutations*: mathematical concepts evolve through
  proofs, counterexamples, and refinements.
- Tao, "There's more to mathematics than rigour and proofs": rigor should
  refine intuition rather than replace it.
- Freudenthal / Realistic Mathematics Education: guided reinvention and
  emergent models.
- Thurston, "On proof and progress in mathematics": mathematical progress is
  tied to shared understanding, not only formal verification.

Useful stable URLs for future verification:

- Tao: `https://terrytao.wordpress.com/career-advice/theres-more-to-mathematics-than-rigour-and-proofs/`
- Poincaré/MacTutor: `https://mathshistory.st-andrews.ac.uk/Extras/Poincare_Intuition/`
- Thurston/arXiv: `https://arxiv.org/abs/math/9404236`
