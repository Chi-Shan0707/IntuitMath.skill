# IntuitMath Subskills

Modular domain entry points. The main SKILL.md routes to these based on
the topic classification of the user's question.

## Available Subskills

| Subskill | File | Covers |
|----------|------|--------|
| `calculus` | `calculus.md` | Limits, continuity, differentiation, integration, series, real analysis |
| `linear-algebra` | `linear-algebra.md` | Vectors, matrices, eigenvalues, inner products, linear maps |
| `probability` | `probability.md` | Probability theory, distributions, LLN, CLT, stochastic processes |
| `optimization` | `optimization.md` | Extremum problems, convex optimization, variational methods, duality |
| `pde` | `pde.md` | Heat/wave/Laplace equations, Fourier analysis, weak solutions |
| `discrete-math` | `discrete-math.md` | Combinatorics, graph theory, number theory, generating functions |
| `abstract-algebra` | `abstract-algebra.md` | Groups, rings, fields, Galois theory, representation theory |

## Routing Logic

```
Question topic → Load subskill
─────────────────────────────────
Limits, continuity, ε-δ, integrals, series      → calculus
Matrices, eigenvalues, linear systems, SVD       → linear-algebra
Distributions, expectation, CLT, random walks    → probability
Max/min, convex, duality, gradient descent       → optimization
Heat/wave/Laplace, Fourier, PDE boundary values  → pde
Counting, primes, graphs, modular arithmetic     → discrete-math
Groups, rings, fields, symmetry, Galois          → abstract-algebra
Multiple or unclear                              → load main SKILL.md only
```

Each subskill contains:
- **Motivation ladders**: Historical path from original problem to modern theory
- **Toolkit reconstruction cases**: Specific era-toolkit-gap-invention analyses
- **Cross-domain connections**: Links to other fields with concrete examples
- **Bernstein principle opportunities**: Where cross-domain simplification works
- **Reflection anchors**: Open questions for deeper thinking
