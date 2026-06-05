# Cross-Domain Pattern Library

This is a SEED library. It covers common patterns but is NOT comprehensive.
When encountering topics not listed here, the agent MUST search the web.

---

## Table of Contents
- [Analysis ↔ Probability](#analysis--probability)
- [Algebra ↔ Geometry](#algebra--geometry)
- [Number Theory ↔ Analysis](#number-theory--analysis)
- [Combinatorics ↔ Analysis](#combinatorics--analysis)
- [Economics → Mathematics](#economics--mathematics)
- [Biology → Mathematics](#biology--mathematics)
- [Physics → Mathematics](#physics--mathematics)
- [Computer Science → Mathematics](#computer-science--mathematics)

---

## Analysis ↔ Probability

### Pattern 1: Bernstein Polynomials / Weierstrass Approximation

| Analysis View | Probability View |
|---------------|-----------------|
| Convolution + mollifiers | Law of large numbers |
| Technical, requires real analysis tools | Intuitive, constructive |
| Shows HOW approximation works | Shows WHY approximation works |

**Core insight**: Approximation of continuous functions IS convergence of
frequencies (LLN). The Bernstein polynomial B_n(f)(x) = E[f(X/n)] where
X ~ Binomial(n,x).

### Pattern 2: Central Limit Theorem

| Analysis View | Probability View |
|---------------|-----------------|
| Fourier transforms (characteristic functions) | Sum of independent random variables |
| Requires complex analysis | Requires only independence |
| Proof: Lévy continuity theorem | Intuition: "sum of small effects is normal" |

**Core insight**: The normal distribution is the fixed point of convolution
(maximum entropy under variance constraint).

### Pattern 3: Heat Equation / Diffusion

| Analysis View | Probability View |
|---------------|-----------------|
| Parabolic PDE: ∂u/∂t = Δu | Brownian motion / random walk |
| Green's function, fundamental solution | Stochastic process, transition density |
| Requires PDE theory | Requires only probability intuition |

**Core insight**: Heat conduction = macroscopic shadow of microscopic random motion.
The heat kernel IS the probability density of Brownian motion at time t.

### Pattern 4: Measure Theory

| Analysis View | Probability View |
|---------------|-----------------|
| Lebesgue measure, abstract σ-algebras | Probability space, events, random variables |
| General integration theory | Expected values, distributions |

**Core insight**: Probability theory IS measure theory where the total measure is 1.

### Pattern 5: Hilbert Spaces

| Analysis View | Probability View |
|---------------|-----------------|
| L² spaces, orthonormal bases | Random variables with finite variance |
| Fourier analysis | Karhunen-Loève expansion |

**Core insight**: Second-order random variables form a Hilbert space.
PCA/EOF is just Fourier analysis in this space.

---

## Algebra ↔ Geometry

### Pattern 1: Linear Transformations ↔ Matrices

| Algebra View | Geometry View |
|-------------|--------------|
| Matrix multiplication | Composition of linear maps |
| Determinant | Volume scaling factor |
| Eigenvalues | Principal stretch directions |

### Pattern 2: Group Theory ↔ Symmetry

| Algebra View | Geometry View |
|-------------|--------------|
| Group axioms | Set of symmetry transformations |
| Normal subgroups | "Symmetries of symmetries" |
| Representation theory | How symmetry acts on spaces |

**Core insight**: Groups ARE the algebraic language of symmetry.

### Pattern 3: Galois Theory ↔ Geometric Constructions

| Algebra View | Geometry View |
|-------------|--------------|
| Solvability of polynomial equations | Constructibility with compass and ruler |
| Galois group structure | Automorphisms of field extensions |

**Core insight**: Quintic unsolvability ↔ regular heptagon non-constructibility.

---

## Number Theory ↔ Analysis

### Pattern 1: Prime Number Theorem

| Number Theory View | Analysis View |
|-------------------|--------------|
| Distribution of primes among integers | Zeros of the Riemann zeta function |
| Counting: π(x) ~ x/ln(x) | ζ(s) has no zeros on Re(s)=1 |

**Core insight**: The primes are not random — their distribution is encoded in
the analytic structure of ζ(s).

### Pattern 2: Modular Forms

| Number Theory View | Analysis View | Geometry View |
|-------------------|--------------|--------------|
| Integer partitions, congruences | Holomorphic functions on upper half-plane | Hyperbolic symmetry |
| Ramanujan τ-function | Fourier coefficients | Automorphic representations |

---

## Combinatorics ↔ Analysis

### Pattern 1: Generating Functions

| Combinatorics View | Analysis View |
|-------------------|--------------|
| Encoding counting sequences | Power series coefficients |
| Discrete objects | Continuous functions |

**Core insight**: Generating functions bridge discrete and continuous.
The "algebraic" manipulation of generating functions IS analytic continuation.

### Pattern 2: Probabilistic Method

| Combinatorics View | Probability View |
|-------------------|-----------------|
| Existence proofs | Random constructions |
| Non-constructive | Expected value calculations |

**Core insight**: To prove an object exists, show that a random object
satisfies the condition with positive probability.

---

## Economics → Mathematics

### Pattern 1: Game Theory → Fixed Point Theorems

- **Economics**: Nash equilibrium — does every game have a stable outcome?
- **Mathematics**: Brouwer/Kakutani fixed point theorems in topology
- **Nash's insight**: Mixed strategy equilibrium IS a fixed point of the
  best-response mapping

### Pattern 2: Portfolio Optimization → Convex Analysis

- **Economics**: How to invest optimally? (Markowitz, 1952)
- **Mathematics**: Quadratic programming, convex optimization, Lagrange duality
- **Impact**: Launched modern financial mathematics and convex optimization theory

### Pattern 3: Options Pricing → Stochastic Calculus

- **Economics**: How to price derivatives? (Black-Scholes, 1973)
- **Mathematics**: Itô calculus, stochastic differential equations, martingale theory
- **Impact**: The Black-Scholes PDE made Itô calculus one of the most applied
  areas of pure mathematics

### Pattern 4: Mechanism Design → Combinatorics

- **Economics**: How to design auctions, voting systems, matching markets?
- **Mathematics**: Combinatorial optimization, graph matching (Gale-Shapley),
  algorithmic game theory
- **Impact**: Spectrum auctions alone generated >$60 billion using matching theory

### Pattern 5: Social Choice → Algebra

- **Economics**: Is there a perfect voting system? (Arrow, 1951)
- **Mathematics**: Arrow's impossibility theorem — an algebraic impossibility result
- **Impact**: Connected welfare economics to abstract algebra and logic

---

## Biology → Mathematics

### Pattern 1: Population Dynamics → ODEs

- **Biology**: How do populations grow, compete, and coexist?
- **Mathematics**: Lotka-Volterra equations, predator-prey models, logistic growth
- **Classic**: Fibonacci sequence from rabbit breeding (1202)

### Pattern 2: Epidemiology → Graph Theory

- **Biology**: How do diseases spread?
- **Mathematics**: SIR models, random graphs, percolation theory
- **Modern**: Network epidemiology uses spectral graph theory

### Pattern 3: Genetics → Probability & Statistics

- **Biology**: How are traits inherited?
- **Mathematics**: Mendelian genetics → probability; population genetics →
  diffusion processes; genome sequencing → combinatorial optimization
- **Impact**: Fisher, Haldane, Wright created modern statistical methodology
  FROM biological questions

### Pattern 4: Neural Signaling → PDEs

- **Biology**: How do neurons transmit signals?
- **Mathematics**: Hodgkin-Huxley equations → reaction-diffusion systems
- **Turing (1952)**: Chemical morphogenesis → pattern formation theory

### Pattern 5: Phylogenetics → Geometry

- **Biology**: How are species related?
- **Mathematics**: Tree spaces, geometric central limit theorems on
  non-smooth spaces (Billera-Holmes-Vogtmann space)
- **Impact**: New mathematics created BY biological need

---

## Physics → Mathematics

### Pattern 1: Mechanics → Calculus

- **Physics**: Motion, gravity, celestial mechanics
- **Mathematics**: Newton/Leibniz calculus, differential equations
- **Classic**: The need to compute instantaneous velocity and areas
  under curves DROVE the invention of calculus

### Pattern 2: Heat → Fourier Analysis

- **Physics**: How does heat conduct?
- **Mathematics**: Fourier series, Fourier transform, harmonic analysis
- **Impact**: Fourier's "any function is a sum of sines" launched
  modern analysis

### Pattern 3: Quantum Mechanics → Functional Analysis

- **Physics**: Subatomic behavior
- **Mathematics**: Hilbert spaces, operator theory, spectral theory,
  C*-algebras
- **Impact**: von Neumann rigorized quantum mechanics and created
  operator algebra theory

### Pattern 4: Relativity → Differential Geometry

- **Physics**: Gravity as spacetime curvature
- **Mathematics**: Riemannian geometry, tensor calculus, topology
- **Impact**: Einstein needed differential geometry that didn't exist yet;
  Ricci and Levi-Civita provided it

### Pattern 5: Statistical Mechanics → Probability & Information

- **Physics**: Macro behavior from micro statistics
- **Mathematics**: Probability theory, ergodic theory, information theory
- **Impact**: Boltzmann's entropy → Shannon's information theory

---

## Computer Science → Mathematics

### Pattern 1: Cryptography → Number Theory

- **CS**: Secure communication
- **Math**: RSA → factoring; Elliptic curves → algebraic geometry;
  Lattice-based → geometric number theory

### Pattern 2: Machine Learning → Optimization

- **CS**: Learning from data
- **Math**: Gradient descent → convex optimization;
  Neural networks → universal approximation (analysis);
  Generalization → statistical learning theory

### Pattern 3: Type Theory → Logic

- **CS**: Programming language type systems
- **Math**: Curry-Howard correspondence: proofs = programs, propositions = types
- **Impact**: Homotopy type theory unifying topology and logic

---

## Usage Guide

When the agent encounters concept X:

1. Search this file for X or related concepts
2. If found, incorporate the cross-domain connections in the response
3. If NOT found, search the web using the Connector subagent prompt
4. Always look for the "Bernstein principle" — is there a simpler proof
   from another field?
5. Add newly discovered patterns to this file for future use

This file should grow over time through use.
