---
name: intuitmath:calculus
description: >
  Calculus and real analysis intuition. Covers limits, continuity,
  differentiation, integration, series, sequences, and the historical
  path from Newton/Leibniz to Cauchy/Weierstrass to modern analysis.
  Loads the main IntuitMath framework plus calculus-specific guidance.
parent: intuitmath
---

# IntuitMath — Calculus & Real Analysis

## Quick Load

Read these files before proceeding:
1. `references/mathematician-thinking.md` (mandatory)
2. `references/known-developments.md` (for seed cases on series, calculus)
3. `references/cross-domain-patterns.md` (for probability/physics connections)

## Key Motivation Ladders

### Limits → Why They Were Needed

```
Euler's formal algebra (1730s)
  → Produced beautiful results AND contradictions
  → Grandi's series: 1-1+1-1+... = ?
  → Conditionally convergent series: rearrangement changes sum (Riemann)
  → Cauchy (1821): Need a FINITARY condition to decide convergence
  → ε-N definition: "for any error tolerance ε, there exists a stage N"
  → This was the GAP between algebraic formalism and rigorous analysis
```

### Derivatives → From Motion to Tangent to Rate

```
Zeno's paradox (c. 450 BC) → instantaneous velocity is contradictory
  → Newton/Leibniz (1660s): "fluxions" and "infinitesimals"
  → Berkeley's critique (1734): "ghosts of departed quantities"
  → Cauchy (1823): derivative = limit of difference quotients
  → Modern: linear approximation, best local linear map
```

### Integrals → From Areas to Measures

```
Archimedes (c. 250 BC): Method of exhaustion for parabolic area
  → Cavalieri (1635): Indivisibles — "stacking slices"
  → Newton/Leibniz: FTC connects integral to antiderivative
  → Riemann (1854): Rigorous definition via upper/lower sums
  → Lebesgue (1901): Measure-theoretic integral — handles more functions
  → Motivation for Lebesgue: Dirichlet function is not Riemann integrable
```

## Toolkit Reconstruction Cases

### Case 1: Why ε-δ?

**Era**: 1820s. Euler had algebra and calculus but no convergence theory.
**Toolkit-Had**: Formal manipulation, infinite series, Taylor expansions.
**Toolkit-Needed**: A way to decide which infinite operations are legitimate.
**Bold Attempt**: Euler's "formal algebraic consistency" — works beautifully for well-behaved functions but produces paradoxes.
**Invention**: Cauchy's ε-N (1821) and later ε-δ (1823) give a finitary check.

### Case 2: Why the Riemann Integral Wasn't Enough

**Era**: Late 1890s. Riemann integration was standard.
**Toolkit-Had**: Riemann sums, continuity, bounded variation.
**Toolkit-Needed**: Integration of functions with dense discontinuities; convergence theorems (limit under integral sign).
**Gap**: Dirichlet function (1 on rationals, 0 on irrationals) is not Riemann integrable, but "should" have integral 0.
**Invention**: Lebesgue (1901) uses measure theory — partition the range, not the domain.

## Cross-Domain Connections

- **Probability**: Riemann integral → distribution functions; Lebesgue integral → expectation; measure theory = probability theory
- **Physics**: Differentiation = velocity; integration = work/area; FTC = conservation of energy
- **Economics**: Marginal cost = derivative; consumer surplus = integral; optimization = critical points
- **Engineering**: Signal processing (Fourier = integration); control (stability = convergence)

## Bernstein Principle Opportunities

- **Weierstrass Approximation → Bernstein polynomials** (probability proof via LLN)
- **Central Limit Theorem → Fourier analysis** (characteristic functions are Fourier transforms)
- **Heat equation → Brownian motion** (PDE = stochastic process)
- **Dominated Convergence → Martingale convergence** (measure theory = probability)

## Reflection Anchors

- Why did it take 150 years from Newton to Cauchy to rigorize calculus?
- Is the ε-δ definition the "right" definition, or just one that works?
- Could we have developed analysis without infinitesimals? (Nonstandard analysis says no and yes simultaneously.)
