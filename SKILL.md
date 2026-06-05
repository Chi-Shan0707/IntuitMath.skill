---
name: intuitmath
description: >
  A skill that makes AI agents think like mathematicians. When a user asks any
  mathematical question — concept motivation, theorem proof, problem solving,
  cross-domain connection, historical analysis — load this skill. Core features:
  (1) Motivation-first analysis with "toolkit reconstruction" — go back to the
  mathematician's era, see what tools they had and what they needed; (2)
  Pre-rigorous before rigorous — intuition and bold attempts before formal
  proofs; (3) Cross-domain awareness — probability illuminating analysis,
  economics driving optimization, biology motivating ODEs; (4) Optional elegant
  HTML output with KaTeX; (5) Multi-agent research workflow for deep
  exploration; (6) Long-term problem accumulation. Inspired by Pólya, Lakatos,
  Lockhart, and Tao.
---

# IntuitMath — Think Like a Mathematician

## Quick Start

Load these files as needed:

| Situation | Load |
|-----------|------|
| Always (mandatory) | `references/mathematician-thinking.md` |
| Question about specific domain | `subskills/<domain>.md` (see Routing below) |
| Cross-domain connections needed | `references/cross-domain-patterns.md` |
| Historical motivation analysis | `references/historical-methodology.md` |
| Known development cases | `references/known-developments.md` |
| HTML output requested | `templates/math-note.html` |

**Important**: Mathematics is too vast to encode in reference files. When you
encounter a topic NOT covered in the references or subskills, you MUST use web
search (see Web Search Integration below). The references are seeds, not
encyclopedias.

---

## Subskill Routing

When the question falls into a specific domain, load the corresponding subskill
for deeper motivation ladders, toolkit reconstruction cases, and domain-specific
cross-domain connections:

| Topic Signals | Subskill File |
|---------------|---------------|
| limits, continuity, ε-δ, integrals, series, convergence | `subskills/calculus.md` |
| matrices, eigenvalues, linear systems, SVD, determinants | `subskills/linear-algebra.md` |
| distributions, expectation, CLT, random walks, stochastic | `subskills/probability.md` |
| max/min, convex, duality, gradient descent, variational | `subskills/optimization.md` |
| heat/wave/Laplace, Fourier, PDE boundary values | `subskills/pde.md` |
| counting, primes, graphs, modular arithmetic, combinatorics | `subskills/discrete-math.md` |
| groups, rings, fields, symmetry, Galois, representations | `subskills/abstract-algebra.md` |
| multiple domains or unclear | stay on main SKILL.md |

If no subskill matches, proceed with the main workflow using only
`references/mathematician-thinking.md`.

---

## Core Workflow

### Step 1: Classify the Question

| Type | Signal | Primary Action |
|------|--------|---------------|
| **Concept Motivation** | "Why does X exist?", "What motivated X?" | Toolkit reconstruction |
| **Proof/Derivation** | "Prove X", "How to derive X?" | Pre-rigorous → Rigorous → Post-rigorous |
| **Cross-Domain** | "What connects X and Y?", "Another perspective?" | Bernstein principle search |
| **Historical** | "How was X discovered?", "Who invented X?" | Era reconstruction + dialectic |
| **Problem Solving** | "Solve X", "Calculate Y" | Pólya 4-phase + intuition first |

### Step 2: Load Appropriate Subskill

Based on classification, load the relevant subskill file. If the topic is
covered by a subskill, its motivation ladders and toolkit reconstruction cases
will provide immediate structured content. If not, proceed with web search.

### Step 3: Toolkit Reconstruction (ALWAYS do this)

For ANY mathematical question about a concept X:

```
1. ERA: When was X introduced? By whom? For what concrete problem?
2. TOOLKIT-HAD: What did that mathematician already have?
3. TOOLKIT-NEEDED: What were they missing?
4. GAP: The gap between HAD and NEEDED = the motivation for X.
5. BOLD-ATTEMPT: What did they try with existing tools? Where did it break?
6. INVENTION: How did X fill the gap?
```

If you don't know the answers, **search the web** (see below). This is not
optional. Check subskills and reference files first; if they don't cover it,
dispatch a web search.

### Step 4: Construct the Response

**Structure** (follow this order, always):

```
1. MOTIVATION — Why does this question matter? What was the original problem?
2. PRE-RIGOROUS — Intuitive, bold, possibly "wild" derivation
   - Annotate: [Motivation: ...], [Bold assumption: ...]
3. RIGOROUS — Formal proof with explicit assumptions
4. CROSS-DOMAIN — Alternative perspectives from other branches or fields
5. REFLECTION — Open question for deeper thinking
```

**Key rules**:
- NEVER start with the rigorous version. Pre-rigorous ALWAYS comes first.
- NEVER present definitions as starting points. Show why they became necessary.
- NEVER mock historical "errors" — they were reasonable in context.
- ALWAYS show dead ends and failed attempts alongside successful ones.
- ALWAYS search for the "Bernstein principle" — a simpler proof from another domain.

### Step 5: Output

**Dialog mode** (default): Respond directly in conversation.

**HTML mode** (when user requests, or answer is complex with 3+ major sections):
- Use `templates/math-note.html` as template
- Replace placeholders: `{{TITLE}}`, `{{SUBTITLE}}`, `{{TAGS}}`, `{{DATE}}`,
  `{{MOTIVATION}}`, `{{INTUITIVE_DERIVATION}}`, `{{RIGOROUS_VERSION}}`,
  `{{MULTI_PERSPECTIVE}}`, `{{CROSS_DOMAIN}}`, `{{REFLECTION}}`
- Write to current working directory
- Tell the user the file path

### Step 6: Save to Problem Library

After every question, save a record:

**If `scripts/save-problem.py` is executable**:
```bash
python scripts/save-problem.py \
    --question "..." \
    --summary "..." \
    --tags "tag1,tag2,tag3" \
    --cross-domain "..." \
    --reflection "..."
```

**Otherwise, manually** create `problem-library/YYYY-MM-DD-<topic>.md` with:
- Question, Summary, Tags, Cross-domain connections, Reflection

---

## Multi-Agent Workflow (if delegate_task is available)

### When to Activate

**Single-agent** (default for simple questions, quick lookups, topics covered
in subskills/reference files).

**Multi-agent** when ANY of:
- Topic not covered in subskills or reference files
- User asks for "deep analysis" or "detailed exploration"
- Question touches 2+ mathematical branches
- Historical context is central

### Executable Delegation Pattern

When multi-agent mode is triggered, use `delegate_task` with the following
concrete structure:

```
delegate_task(
    tasks=[
        {
            "goal": "Research historical context for [CONCEPT]",
            "context": "Search web for: who introduced [CONCEPT], when, why,
                        what tools they had, what they needed, their first
                        bold attempt, where it broke down, how [CONCEPT]
                        filled the gap. Provide specific dates, names,
                        paper titles. Return a structured report.",
            "toolsets": ["web"]
        },
        {
            "goal": "Find cross-domain connections for [CONCEPT]",
            "context": "Search web for: alternative proofs of [CONCEPT]
                        from other branches, applications in physics,
                        chemistry, biology, medicine, economics, finance,
                        demography, statistics, engineering, linguistics,
                        music, social sciences. Look for the Bernstein
                        principle — a simpler proof from another domain.
                        For each connection: what it is, why illuminating.",
            "toolsets": ["web"]
        }
    ]
)
```

Researcher and Connector run **in parallel**. After both return, the main
agent acts as Deriver+Synthesizer: it constructs the mathematical content
(pre-rigorous → rigorous → cross-domain) using the research results,
then delivers the response.

### Merge Strategy (Synthesizer)

When subagent results return:

1. **If Researcher and Connector agree**: Use both. Weave historical context
   into the motivation section; weave cross-domain findings into the
   multi-perspective section.

2. **If they conflict**: Present both viewpoints with attribution.
   "The historical record suggests [A], though [B] offers an alternative
   interpretation." Never silently discard a subagent's finding.

3. **If one fails (empty results)**: Proceed with whatever was found.
   If both fail, fall back to single-agent mode using your own knowledge
   and mark the response: "Note: external research was unavailable for
   this question."

4. **Always**: The main agent adds the mathematical derivation itself
   (pre-rigorous intuition, rigorous proof, reflection anchor). Subagents
   provide RESEARCH, not the mathematical content.

---

## Web Search Integration

### When to Search

Search is MANDATORY when:
- The topic is not covered in subskills/ or references/
- The user asks "who/when/how was X discovered"
- Cross-domain connections are needed but not in the pattern library

### How to Search

**Tool availability varies by platform. Use the first available:**

| Priority | Hermes | Claude | OpenClaw | Best For |
|----------|--------|--------|----------|----------|
| 1 | `web_search` | `websearch` / `exa-search` / `research-lookup` | `web_search` | General queries |
| 2 | `web_extract` | `webfetch` | `web_extract` | Extracting from specific URLs |
| 3 | `browser_navigate` | — | `browser_navigate` | Interactive pages, JS-heavy sites |
| 4 | `curl` (via terminal) | `curl` (via bash) | `curl` (via terminal) | APIs, plain-text endpoints |

### Search Query Templates

For **historical context**:
```
"[CONCEPT] history origin who invented motivation"
"[MATHEMATICIAN] [CONCEPT] original paper year"
"history of [CONCEPT] in mathematics"
```

For **cross-domain connections**:
```
"[CONCEPT] application in [FIELD]"
"[CONCEPT] alternative proof probability/physics/economics"
"[CONCEPT] connection to [OTHER_BRANCH]"
"[CONCEPT] Bernstein principle simpler proof"
```

For **specific math content**:
```
"[CONCEPT] intuitive explanation motivation"
"[CONCEPT] why does it work"
"proof of [THEOREM] without [ADVANCED_TOOL]"
```

### Failure Handling

- **No results**: Broaden the query. Remove quotes, use synonyms.
- **CAPTCHA/blocked**: Switch to a different search tool or use `curl` on
  known academic sites (Wikipedia, MathWorld, nLab, Stacks Project).
- **Conflicting sources**: Present the conflict. "Source A says X, Source B
  says Y. The more standard account is..."
- **Rate limited**: Wait 5 seconds and retry with a simpler query.

### Caching

After a successful search, if the finding is significant and reusable:
- Consider adding it to `references/cross-domain-patterns.md` as a new pattern
- Consider adding a toolkit reconstruction case to the relevant subskill

---

## Style Guide

### DO
- Use mathematicians' names and dates for historical depth
- Show the *reasoning* behind "wild" calculations — why they felt natural
- Use physical/geometric intuition to drive abstract concepts
- Pause after key steps: "At this point you might wonder..."
- Admit uncertainty: "We don't know for certain whether X thought this way,
  but the more likely story is..."
- Give reflection anchors — open questions with no standard answer
- Proactively mention economic, biological, physical, chemical, demographic,
  statistical, engineering, linguistic, or musical motivations
- When a subskill is loaded, use its motivation ladders as the backbone

### DO NOT
- Present modern axiomatic definitions as starting points
- Skip the motivation chain and jump to conclusions
- Ridicule historical "mistakes" — they were reasonable in context
- Describe mathematical development as linear progress
- Use ε-δ language to explain pre-19th-century mathematics
- Give only the rigorous version without the pre-rigorous one
- Ignore cross-domain connections
- Load a subskill and then ignore its content

---

## Quality Checklist

Before delivering any response, verify:
- [ ] Does it show *why* the question matters (motivation)?
- [ ] Does it include at least one "bold attempt" that may not be rigorous?
- [ ] Does it identify cross-domain connections?
- [ ] Does it distinguish "pre-rigorous intuition" from "rigorous proof"?
- [ ] Does it include a reflection anchor (open question)?
- [ ] Does it avoid textbook-style "definition → theorem → proof" ordering?
- [ ] If the topic wasn't in subskills or reference files, did it search the web?
- [ ] Was the problem saved to the library?

---

## Example Interaction

### Input
> "Why do we need Lebesgue integration? What's wrong with Riemann?"

### Expected Output Structure

**1. MOTIVATION** (why this matters):
The Riemann integral works beautifully for continuous functions on
[a,b]. But by the late 1800s, mathematicians kept bumping into functions
that Riemann couldn't handle...

**2. PRE-RIGOROUS** (bold attempt):
Let's try to integrate the Dirichlet function f(x) = 1 if x is rational,
0 if x is irrational, on [0,1]...

[Bold assumption: maybe we can just "count" the rationals vs irrationals]

The problem: every Riemann upper sum = 1 (rationals are dense), every
lower sum = 0 (irrationals are dense). The Riemann integral doesn't exist.

But intuitively, the "area under the curve" should be 0 — the rationals
take up zero "space" in [0,1]. Lebesgue's idea: partition the RANGE
instead of the domain...

**3. RIGOROUS**: Lebesgue integral via measure theory, monotone convergence,
dominated convergence, etc.

**4. CROSS-DOMAIN**:
- Probability: E[X] IS a Lebesgue integral with respect to P
- Physics: Quantum observables require Lebesgue integration (L² spaces)
- Signal processing: Lp spaces and Fourier analysis need Lebesgue
- Economics: Expected utility = Lebesgue integral of utility function

**5. REFLECTION**: Is there an integral that handles even more than Lebesgue?
(Hint: Henstock-Kurzweil. But why hasn't it replaced Lebesgue?)

---

## Configuration Detection

```
IF delegate_task available    → enable multi-agent mode (parallel research)
IF write_file + templates/    → enable HTML generation
IF scripts/save-problem.py    → use automated problem saving
IF problem-library/ writable  → enable long-term accumulation
ELSE                          → degrade gracefully to single-agent dialog
```

---

## Intellectual Lineage

This project draws from:

| Thinker | Key Contribution | How We Use It |
|---------|-----------------|---------------|
| **Pólya** (1945) | 4-phase heuristic: Understand → Plan → Execute → Reflect | Workflow structure |
| **Lakatos** (1976) | Mathematics as dialectic: Conjecture → Proof → Refutation → Refinement | Response structure |
| **Lockhart** (2002) | Math is art; motivation before technique; problems over exercises | Core philosophy |
| **Tao** (2007-) | Pre-rigorous → Rigorous → Post-rigorous | Presentation order |
| **Bernstein** (1912) | Probabilistic proof of Weierstrass theorem | Cross-domain simplification principle |
| **AlphaGeometry** (2024) | Neural intuition + symbolic verification | Multi-agent neuro-symbolic workflow |
