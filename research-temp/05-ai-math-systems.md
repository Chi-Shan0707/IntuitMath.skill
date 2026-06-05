# AI Systems for Mathematical Reasoning (2023-2026)

## AlphaGeometry (DeepMind, 2024)

**What**: Neuro-symbolic system for Euclidean geometry theorem proving
**Key Innovation**: Generates millions of synthetic theorems/proofs from scratch, no human demonstrations needed
**Architecture**: Neural language model (intuition/guidance) + symbolic deduction engine (formal reasoning)
**Performance**: Solves 25/30 IMO geometry problems (approaching IMO gold medalist level)

### Key Insight for IntuitMath
AlphaGeometry's architecture mirrors how human mathematicians think:
- **Language model** = intuition, guessing which auxiliary constructions to add
- **Symbolic engine** = rigorous deduction
- The LM "suggests" while the symbolic engine "verifies" - this is exactly the "intuitive -> rigorous" pipeline we want

### Open Source
- Code: https://github.com/google-deepmind/alphageometry
- AlphaGeometry2 (2025) uses Gemini as backbone, solves 83% of historical IMO geometry problems

## FunSearch (DeepMind, 2023)

**What**: Evolutionary LLM system that discovers NEW mathematical constructions
**Key Innovation**: Searches for PROGRAMS (functions), not solutions - produces interpretable code
**Breakthrough**: First LLM to make verifiable new discoveries in open mathematical problems

### Cap Set Problem Results
- Found largest cap sets ever constructed in dimension 8 (512 elements)
- Largest improvement in 20 years for asymptotic lower bound
- The discovered programs were human-interpretable - experts could understand what they found

### Architecture
1. LLM (Codey/StarCoder) proposes program improvements
2. Evaluator scores and rejects hallucinations
3. Best programs fed back into prompts (best-shot prompting)
4. Island-based evolutionary method maintains diversity

### Key Insight for IntuitMath
FunSearch shows that LLMs CAN make genuine mathematical discoveries when paired with systematic evaluation. The "search for functions, not solutions" paradigm is deeply aligned with our project.

## Prover Agent (2025)

**What**: Multi-agent framework for formal theorem proving in Lean
**Architecture**: Informal reasoning LLM + formal prover model + Lean verification
**Key Innovation**: Generates auxiliary lemmas (not just subgoals) - special cases, useful facts, hypothesis-driven conjectures
**Performance**: 88.1% on MiniF2F benchmark

### Key Insight
The "auxiliary lemma generation" strategy is exactly what mathematicians do: when stuck, generate related lemmas that might help build a proof strategy in a bottom-up manner.

## SciAgent (2025)

**What**: Unified multi-agent system for general scientific reasoning
**Architecture**: Coordinator Agent -> Worker Systems -> Sub-agents
**Workers**: Math, Physics, Chemistry, General Exam
**Key Design**: Each Worker has Generator, Reviewer, Image Analyser sub-agents

### Key Insight
The hierarchical Coordinator-Worker-Subagent structure mirrors how mathematical research teams organize: a senior mathematician delegates to specialists, who delegate to students.

## Ax-Prover (2025)

**What**: Multi-agent theorem prover using MCP (Model Context Protocol)
**Architecture**: Orchestrator + Prover + Verifier agents
**Key Innovation**: Uses MCP tools to equip LLMs with Lean tools
**Cross-domain**: Works in both math AND quantum physics

### Key Insight
The Orchestrator-Prover-Verifier pattern maps to our IntuitMath workflow:
- Orchestrator = our "motivation analysis" step
- Prover = our "derivation" step
- Verifier = our "rigorous version" step

## Equational Theories Project (ETP, 2024-2025)

**What**: Crowdsourced collaborative math research with formal verification
**Goal**: Determine all implications between 4694 equational laws on magmas
**Scale**: 22,028,942 implications, all verified in Lean
**Method**: GitHub-based collaboration + automated tools + Lean verification

### Key Insight for IntuitMath
This is a model for how humans + AI + formal systems can collaborate at scale. The "problem library" feature of our skill could follow similar patterns.

## Implications for IntuitMath

1. **Neuro-symbolic architecture**: Our skill should separate "intuitive reasoning" (LLM) from "formal verification" (structured checks)
2. **Auxiliary lemma generation**: When stuck, the agent should generate related lemmas/facts
3. **Multi-agent coordination**: The Coordinator-Worker pattern is proven effective
4. **Formal verification as optional layer**: Like Ax-Prover, we could optionally verify with Lean
5. **Search for functions, not solutions**: Follow FunSearch's paradigm - produce interpretable structures
6. **Crowdsourced knowledge**: ETP shows how collaborative math projects can work at scale

## Sources
- AlphaGeometry: https://www.nature.com/articles/s41586-023-06747-5
- FunSearch: https://www.nature.com/articles/s41586-023-06924-6
- Prover Agent: https://arxiv.org/html/2506.19923v3
- SciAgent: https://arxiv.org/html/2511.08151v1
- Ax-Prover: https://arxiv.org/html/2510.12787v4
- ETP: https://arxiv.org/html/2512.07087v2
