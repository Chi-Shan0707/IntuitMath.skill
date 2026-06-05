# Cross-Domain Pattern Library

This is a SEED library. It covers common patterns but is NOT comprehensive.
When encountering topics not listed here, the agent MUST search the web.

---

## Table of Contents

### Intra-mathematical connections
- [Analysis ↔ Probability](#analysis--probability)
- [Algebra ↔ Geometry](#algebra--geometry)
- [Number Theory ↔ Analysis](#number-theory--analysis)
- [Combinatorics ↔ Analysis](#combinatorics--analysis)

### External disciplines → Mathematics
- [Economics & Finance → Mathematics](#economics--finance--mathematics)
- [Physics → Mathematics](#physics--mathematics)
- [Chemistry → Mathematics](#chemistry--mathematics)
- [Biology & Medicine → Mathematics](#biology--medicine--mathematics)
- [Demography & Social Sciences → Mathematics](#demography--social-sciences--mathematics)
- [Statistics & Data Science → Mathematics](#statistics--data-science--mathematics)
- [Computer Science & Engineering → Mathematics](#computer-science--engineering--mathematics)
- [Linguistics & Music → Mathematics](#linguistics--music--mathematics)

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

## Economics & Finance → Mathematics

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

### Pattern 6: General Equilibrium → Fixed Point Theory

- **Economics**: Can all markets clear simultaneously? (Walras, Arrow-Debreu)
- **Mathematics**: Brouwer fixed point theorem, Kakutani fixed point theorem,
  convex analysis
- **Impact**: Existence proofs in economics drove developments in
  infinite-dimensional convex analysis and optimization

### Pattern 7: Risk & Insurance → Probability

- **Economics**: How to price risk? What is a "fair" premium?
- **Mathematics**: Expected utility theory (Bernoulli 1738), actuarial mathematics,
  extreme value theory, copulas
- **Classic**: Bernoulli's St. Petersburg paradox → birth of expected utility

---

## Chemistry → Mathematics

### Pattern 1: Molecular Structure → Group Theory

- **Chemistry**: Why do molecules have specific shapes and symmetries?
- **Mathematics**: Point groups, representation theory, character tables
- **Core insight**: The symmetries of a molecule form a group. Spectroscopic
  selection rules are group-theoretic statements about representation dimensions.

### Pattern 2: Quantum Chemistry → Linear Algebra

- **Chemistry**: How do electrons behave in molecules?
- **Mathematics**: Eigenvalue problems, variational methods, perturbation theory
- **Classic**: The Hartree-Fock method is an iterative eigenvalue problem
  on a high-dimensional symmetric matrix

### Pattern 3: Reaction Kinetics → ODEs

- **Chemistry**: How fast do chemical reactions proceed?
- **Mathematics**: Systems of ODEs, mass-action kinetics, stiff equations
- **Classic**: The Lotka-Volterra equations were ORIGINALLY chemical
  reaction models before being applied to ecology

### Pattern 4: Crystallography → Lattice Theory

- **Chemistry**: How are atoms arranged in crystals?
- **Mathematics**: Bravais lattices (230 space groups), Fourier analysis
  (X-ray crystallography), reciprocal lattices
- **Core insight**: X-ray diffraction patterns are Fourier transforms of
  the electron density. Crystallography IS applied Fourier analysis.

### Pattern 5: Chemical Graph Theory

- **Chemistry**: How to represent molecular structure computationally?
- **Mathematics**: Graph theory (atoms = vertices, bonds = edges),
  topological indices, spectral graph theory
- **Impact**: Wiener index, Hosoya index — graph invariants that predict
  chemical properties (boiling point, toxicity)

---

## Biology & Medicine → Mathematics

### Pattern 1: Population Dynamics → ODEs

- **Biology**: How do populations grow, compete, and coexist?
- **Mathematics**: Lotka-Volterra equations, predator-prey models, logistic growth
- **Classic**: Fibonacci sequence from rabbit breeding (1202)

### Pattern 2: Epidemiology → Compartmental Models & Graphs

- **Biology**: How do diseases spread through populations?
- **Mathematics**: SIR/SEIR models (Kermack-McKendrick 1927), random graphs,
  percolation theory, basic reproduction number R₀
- **Modern**: COVID-19 modeling used meta-population models, network
  epidemiology, spectral graph theory

### Pattern 3: Genetics → Probability & Statistics

- **Biology**: How are traits inherited?
- **Mathematics**: Mendelian genetics → probability; population genetics →
  diffusion processes (Wright-Fisher model); genome sequencing →
  combinatorial optimization (shotgun assembly)
- **Impact**: Fisher, Haldane, Wright created modern statistical methodology
  FROM biological questions (ANOVA, maximum likelihood estimation)

### Pattern 4: Neural Signaling → PDEs

- **Biology**: How do neurons transmit signals?
- **Mathematics**: Hodgkin-Huxley equations → reaction-diffusion systems
- **Turing (1952)**: Chemical morphogenesis → pattern formation theory

### Pattern 5: Phylogenetics → Geometry & Combinatorics

- **Biology**: How are species related?
- **Mathematics**: Tree spaces, geometric central limit theorems on
  non-smooth spaces (Billera-Holmes-Vogtmann space)
- **Impact**: New mathematics created BY biological need

### Pattern 6: Medical Imaging → Harmonic Analysis

- **Medicine**: How to reconstruct internal organs from scanner data?
- **Mathematics**: Radon transform, Fourier inversion, compressed sensing,
  wavelets, inverse problems
- **Impact**: CT scans ARE Radon transform inversions. MRI IS Fourier
  reconstruction in k-space. The 1979 Nobel Prize in Medicine went to
  Cormack and Hounsfield for the mathematics of CT.

### Pattern 7: Drug Discovery → Optimization

- **Medicine**: How to design effective drugs?
- **Mathematics**: Molecular docking (optimization on manifolds),
  quantitative structure-activity relationships (QSAR, statistical learning),
  pharmacokinetics (compartmental ODE models)

---

## Demography & Social Sciences → Mathematics

### Pattern 1: Population Projection → Matrix Algebra

- **Demography**: How will a population age-structure evolve?
- **Mathematics**: Leslie matrices (1945) — age-structured population models
  as matrix iterations; dominant eigenvalue = long-term growth rate;
  stable age distribution = dominant eigenvector
- **Core insight**: Population projection IS a matrix eigenvalue problem.

### Pattern 2: Census & Sampling → Statistics

- **Demography**: How to count a population you can't enumerate?
- **Mathematics**: Sampling theory, estimation, confidence intervals,
  capture-recapture methods (combinatorial probability)
- **Classic**: Laplace's estimate of the population of France (1786) —
  one of the first uses of statistical sampling

### Pattern 3: Survival Analysis → Probability

- **Demography / Medicine**: How long do people live? What factors affect mortality?
- **Mathematics**: Survival functions, hazard rates, Kaplan-Meier estimator,
  Cox proportional hazards (partial likelihood)
- **Impact**: Actuarial science and demography drove the development of
  survival/reliability theory

### Pattern 4: Social Networks → Graph Theory

- **Sociology**: How do information, disease, and behavior spread through society?
- **Mathematics**: Random graphs (Erdős-Rényi), preferential attachment
  (Barabási-Albert), community detection (spectral clustering),
  centrality measures (eigenvectors)
- **Core insight**: Milgram's "six degrees of separation" → small-world
  network models → spectral graph theory

### Pattern 5: Voting & Fair Division → Combinatorics & Topology

- **Political Science**: How to fairly apportion seats? How to divide resources?
- **Mathematics**: Arrow's theorem, Gibbard-Satterthwaite theorem,
  cake-cutting algorithms, fair division (measure theory)
- **Classic**: The apportionment problem (Hamilton, Jefferson, Webster methods)
  — a purely mathematical question arising from representative democracy

### Pattern 6: Migration & Urban Planning → Spatial Statistics

- **Demography / Geography**: Where do people move and why?
- **Mathematics**: Spatial point processes, gravity models,
  Markov random fields, optimal transport theory
- **Modern**: Optimal transport (Monge-Kantorovich) now appears everywhere
  from ML to fluid dynamics, but originated in resource allocation problems

---

## Statistics & Data Science → Mathematics

### Pattern 1: Estimation Theory → Optimization

- **Statistics**: How to best estimate parameters from data?
- **Mathematics**: Maximum likelihood → optimization on manifolds;
  EM algorithm → alternating optimization; M-estimators → convex analysis
- **Core insight**: Fisher's maximum likelihood principle turned statistics
  into an optimization discipline

### Pattern 2: Bayesian Inference → Functional Analysis

- **Statistics**: How to update beliefs with evidence?
- **Mathematics**: Posterior distributions as measures on function spaces;
  conjugate priors as algebraic structures; MCMC as Markov chain theory
- **Impact**: Modern Bayesian computation (HMC, variational inference)
  is applied differential geometry (Riemann manifolds, information geometry)

### Pattern 3: Regression → Linear Algebra & Optimization

- **Statistics**: How to model relationships between variables?
- **Mathematics**: Least squares → projection onto subspaces (linear algebra);
  LASSO → convex optimization; kernel methods → reproducing kernel
  Hilbert spaces (functional analysis)
- **Core insight**: Linear regression IS orthogonal projection onto a
  column space. Gauss invented least squares for astronomical observations.

### Pattern 4: Hypothesis Testing → Measure Theory

- **Statistics**: Is this effect real or noise?
- **Mathematics**: Neyman-Pearson lemma → decision theory;
  p-values → tail probabilities under null measures;
  multiple testing → false discovery rate (Benjamini-Hochberg)
- **Impact**: The entire framework of statistical inference is measure-theoretic

### Pattern 5: High-Dimensional Statistics → Random Matrix Theory

- **Statistics**: What happens when dimensions exceed sample size?
- **Mathematics**: Marchenko-Pastur law, Wigner semicircle law,
  concentration of measure, compressed sensing
- **Core insight**: Random matrix eigenvalue distributions provide
  universal limits for high-dimensional estimation

---

## Computer Science & Engineering → Mathematics

### Pattern 1: Cryptography → Number Theory

- **CS**: Secure communication
- **Math**: RSA → factoring; Elliptic curves → algebraic geometry;
  Lattice-based → geometric number theory

### Pattern 2: Machine Learning → Optimization & Functional Analysis

- **CS**: Learning from data
- **Math**: Gradient descent → convex optimization;
  Neural networks → universal approximation (analysis);
  Generalization → statistical learning theory (VC dimension, Rademacher complexity)

### Pattern 3: Type Theory → Logic

- **CS**: Programming language type systems
- **Math**: Curry-Howard correspondence: proofs = programs, propositions = types
- **Impact**: Homotopy type theory unifying topology and logic

### Pattern 4: Signal Processing → Harmonic Analysis

- **Engineering**: How to filter, compress, transmit signals?
- **Math**: Fourier analysis, wavelets, sampling theorem (Shannon-Nyquist),
  compressed sensing (Candès, Tao, Donoho)
- **Core insight**: The Shannon sampling theorem connects continuous signals
  to discrete samples — analysis meets information theory

### Pattern 5: Control Theory → ODEs & Optimization

- **Engineering**: How to make systems behave as desired?
- **Math**: PID control → ODE stability; optimal control → calculus of
  variations / Pontryagin's maximum principle; robust control → H∞ theory
  (Hardy spaces)
- **Classic**: Wiener's cybernetics → modern control and filtering (Kalman filter)

### Pattern 6: Information Theory → Probability & Measure Theory

- **Engineering**: What are the fundamental limits of communication?
- **Math**: Shannon entropy → measure theory; channel capacity →
  large deviations theory; rate-distortion → variational optimization
- **Impact**: Shannon (1948) created information theory from probability;
  now feeds back into ML, statistics, and physics

---

## Linguistics & Music → Mathematics

### Pattern 1: Formal Languages → Automata Theory

- **Linguistics**: What is the structure of natural language?
- **Mathematics**: Chomsky hierarchy (regular, context-free, context-sensitive),
  formal grammars, automata theory
- **Impact**: Parser design, programming languages, natural language processing

### Pattern 2: Musical Harmony → Group Theory & Fourier Analysis

- **Music**: Why do certain note combinations sound pleasant?
- **Mathematics**: Transposition and inversion as group actions (dihedral groups);
  pitch-class sets as Z₁₂; Fourier analysis of sound waves → timbre
- **Classic**: Pythagorean tuning → rational approximations; equal temperament →
  12th root of 2

### Pattern 3: Computational Linguistics → Probability

- **Linguistics**: How to model language statistically?
- **Mathematics**: Hidden Markov models, n-grams → Markov chains;
  word embeddings → vector space models; transformers → attention matrices
- **Core insight**: Modern NLP is applied linear algebra and probability

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
