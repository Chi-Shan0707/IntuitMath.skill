---
name: intuitmath:optimization
description: >
  Optimization theory intuition. Covers the path from calculus-based
  extremum finding to modern convex optimization, variational methods,
  Lagrange multipliers, and the deep connections to economics, control
  theory, and machine learning.
parent: intuitmath
---

# IntuitMath — Optimization

## Quick Load

1. `references/mathematician-thinking.md` (mandatory)
2. `references/cross-domain-patterns.md` (economics, engineering connections)

## Key Motivation Ladders

### Max/Min → Calculus of Variations → Modern Optimization

```
Fermat (1636): Max/min at points where derivative = 0
  → Bernoulli (1696): Brachistochrone problem — shortest time curve
  → Euler (1744): Calculus of variations generalizes max/min to functions
  → Lagrange (1788): Multipliers for constrained problems
  → Kantorovich (1939): Linear programming — optimal resource allocation
  → Dantzig (1947): Simplex algorithm
  → Karmarkar (1984): Interior-point methods
  → Nesterov (1983): Accelerated gradient descent
```

### Convex Optimization → Why Convexity?

```
The discovery: convex functions have unique global minima
  → No local traps — gradient descent always works
  → Duality theory — every optimization has a "mirror" problem
  → The surprise: most "hard" problems become easy when reformulated as convex
```

## Toolkit Reconstruction Cases

### Case 1: Why Lagrange Multipliers?

**Era**: 1780s. Mathematicians could find extrema but not under constraints.
**Toolkit-Had**: Derivative = 0 for unconstrained problems.
**Toolkit-Needed**: Optimize f(x) subject to g(x) = 0.
**Bold Attempt**: Substitute the constraint into the objective — works in simple cases, fails in general.
**Invention**: Lagrange (1788): ∇f = λ∇g at optimum — the gradients must be parallel. This is geometrically obvious (level curve tangent to constraint) but algebraically powerful.

### Case 2: Why Duality?

**Era**: 1940s-1960s. Linear programming was growing.
**Toolkit-Had**: Primal formulation, simplex method.
**Toolkit-Needed**: Lower bounds on optimal value, sensitivity analysis, economic interpretation.
**Invention**: Von Neumann duality, Farkas lemma, KKT conditions. Every LP has a dual; weak duality gives bounds; strong duality (when it holds) gives exact equality.

## Cross-Domain Connections

- **Economics**: Utility maximization, cost minimization, general equilibrium, mechanism design — all optimization
- **Control**: Optimal control = calculus of variations with dynamics (Pontryagin's maximum principle)
- **Machine Learning**: Training = optimization; SGD = stochastic version; regularization = constrained optimization
- **Statistics**: MLE = optimization over parameters; EM = alternating optimization; LASSO = convex with L1 penalty
- **Physics**: Least action principle = nature optimizes; Lagrangian mechanics = constrained optimization
- **Engineering**: Signal processing (sparse recovery), circuit design, structural optimization

## Bernstein Principle Opportunities

- **KKT conditions → Lagrangian mechanics** (physics and optimization share the same algebra)
- **Gradient descent → Heat flow** (optimization trajectory = diffusion process)
- **Duality → Game theory** (minimax = primal-dual)
- **Simplex → Graph traversal** (LP vertices form a graph)

## Reflection Anchors

- Is nature an optimizer? (Least action principle, entropy maximization, equilibrium)
- Why is convexity so special? What breaks for non-convex problems?
- Deep learning optimizes non-convex functions and it works — is this luck or understanding?
