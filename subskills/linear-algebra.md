---
name: intuitmath:linear-algebra
description: >
  Linear algebra intuition. Covers vectors, matrices, linear
  transformations, eigenvalues, inner products, and the path from
  solving systems of equations to modern abstract linear algebra.
parent: intuitmath
---

# IntuitMath — Linear Algebra

## Quick Load

1. `references/mathematician-thinking.md` (mandatory)
2. `references/cross-domain-patterns.md` (algebra-geometry duality)

## Key Motivation Ladders

### Systems of Equations → Matrices → Linear Maps

```
Ancient China (Nine Chapters, c. 200 BC): Gaussian elimination
  → Descartes (1637): Coordinate geometry connects equations to geometry
  → Cayley (1858): Matrix algebra — "a convenient notation"
  → The insight: a matrix IS a linear transformation written in coordinates
  → Eigenvalues = "what doesn't change direction" under the map
```

### Determinants → Before Matrices

```
Seki Takakazu (1683) / Leibniz (1693): Determinants appear FIRST
  → Cramer (1750): Cramer's rule for solving systems
  → Vandermonde (1772): Determinant as volume scaling
  → The historical surprise: determinants preceded matrices by ~175 years
```

### Inner Products → Geometry Meets Algebra

```
Euclid (c. 300 BC): Length, angle, orthogonality via geometry
  → Grassmann (1844): Exterior algebra — "geometric calculus"
  → Gram (1883) / Schmidt (1907): Orthogonalization procedure
  → Hilbert (1900s): Infinite-dimensional inner product spaces
  → The bridge: inner products let you DO geometry algebraically
```

## Toolkit Reconstruction Cases

### Case 1: Why Eigenvalues?

**Era**: 1740s-1850s. Mathematicians had differential equations and rigid body dynamics.
**Toolkit-Had**: Calculus, ODEs, ad hoc methods for specific equations.
**Toolkit-Needed**: A systematic way to solve coupled linear ODEs and analyze quadratic forms.
**Bold Attempt**: Euler (1748) tried separation of variables for PDEs — found special "characteristic" values.
**Invention**: "Eigenwerte" (Hilbert, 1904) — the values for which Ax = λx has solutions. These diagonalize the system.

### Case 2: Why Abstract Vector Spaces?

**Era**: Early 1900s. Matrices and coordinates were standard.
**Toolkit-Had**: Matrix algebra, determinants, Euclidean geometry.
**Toolkit-Needed**: A unified theory covering polynomials, functions, sequences, AND Euclidean vectors.
**Gap**: Every application used the same theorems with different notation.
**Invention**: Peano (1888, overlooked) → Banach (1922) → Modern axiomatization. Abstract = reusable.

## Cross-Domain Connections

- **Probability**: Covariance matrix = Gram matrix of random variables; PCA = eigendecomposition
- **Physics**: Quantum states = vectors in Hilbert space; observables = linear operators
- **Economics**: Input-output models (Leontief) = solving linear systems; Markov chains = eigenvectors
- **Chemistry**: Molecular orbitals = eigenvectors of Hamiltonian matrix
- **Statistics**: Least squares = orthogonal projection onto column space (Gauss, 1809)
- **Engineering**: Fourier transform = eigenfunctions of translation; signal processing = linear algebra over function spaces
- **Demography**: Leslie matrices — population projection IS matrix iteration

## Bernstein Principle Opportunities

- **Spectral theorem → Probability**: Eigenvalues of a random matrix follow universal distributions (Wigner, Marchenko-Pastur)
- **SVD → Data science**: Best low-rank approximation = Eckart-Young theorem
- **QR decomposition → Numerical stability**: Gram-Schmidt made computationally robust
- **Matrix exponential → ODEs**: e^(At) solves any linear system x' = Ax

## Reflection Anchors

- Why did determinants come before matrices? What does this say about notation vs. concept?
- Is there a "right" basis for a vector space, or is the whole point that all bases are equivalent?
- Linear algebra is "finished" as pure math but still growing in applications — why?
