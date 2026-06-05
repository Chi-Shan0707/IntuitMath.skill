---
name: intuitmath:pde
description: >
  Partial differential equations intuition. Covers the three classical
  PDEs (heat, wave, Laplace), Fourier analysis, and the deep connections
  to physics, probability, and geometry.
parent: intuitmath
---

# IntuitMath — Partial Differential Equations

## Quick Load

1. `references/mathematician-thinking.md` (mandatory)
2. `references/cross-domain-patterns.md` (physics, probability, engineering connections)

## Key Motivation Ladders

### The Three Classical PDEs

```
Heat equation (∂u/∂t = Δu):
  → Fourier (1807): "Any function is a sum of sines"
  → Physical origin: heat flows from hot to cold
  → Probability origin: density of Brownian motion

Wave equation (∂²u/∂t² = Δu):
  → d'Alembert (1747): 1D wave solution
  → Physical origin: vibrating strings, sound, light
  → Geometry origin: curvature of spacetime

Laplace equation (Δu = 0):
  → Laplace (1782): Gravitational potential in free space
  → Physical origin: steady-state temperature, electrostatics
  → Complex analysis: real/imaginary parts of holomorphic functions
```

### Fourier Analysis → The Universal Decomposition

```
Heat problem (Fourier, 1807): Need to expand ANY function in sines
  → Fourier series: periodic functions = sum of harmonics
  → Fourier transform: non-periodic = integral of frequencies
  → The controversy: "Any function?? This is absurd!" (Lagrange objected)
  → Resolution: Yes, under mild conditions (Dirichlet, 1829)
  → Modern: Fourier analysis IS harmonic analysis on groups (Pontryagin duality)
```

## Toolkit Reconstruction Cases

### Case 1: Why the Heat Equation Mattered So Much

**Era**: Early 1800s. Understanding heat conduction was an engineering imperative.
**Toolkit-Had**: Calculus, Newton's law of cooling, some ODE theory.
**Toolkit-Needed**: Model spatial+temporal temperature evolution.
**Bold Attempt**: Fourier tried polynomial expansions — wrong basis, messy algebra.
**Invention**: Trigonometric series. The key insight: heat equation separates in space and time when expanded in eigenfunctions of Δ. This INVENTED Fourier analysis.

### Case 2: Why Weak Solutions?

**Era**: 1930s-1950s. Classical solutions required smoothness.
**Toolkit-Had**: Explicit formulas for special geometries, separation of variables.
**Toolkit-Needed**: Solutions for non-smooth data (discontinuous initial conditions, irregular domains).
**Gap**: Physical problems have shocks (gas dynamics), discontinuities, corners.
**Invention**: Sobolev spaces (Sobolev, 1935) + weak derivatives + Lax-Milgram theorem. Move the derivative onto a test function via integration by parts.

## Cross-Domain Connections

- **Probability**: Heat kernel = Brownian motion transition density; Feynman-Kac = PDE pricing via expectation
- **Physics**: ALL of physics is PDEs (Maxwell, Schrödinger, Einstein, Navier-Stokes)
- **Geometry**: Ricci flow (PDE) proved Poincaré conjecture (Perelman, 2003)
- **Engineering**: Signal processing (Fourier), image processing (diffusion), acoustics (wave equation)
- **Finance**: Black-Scholes PDE = heat equation after change of variables

## Bernstein Principle Opportunities

- **Heat equation → Random walk** (microscopic randomness → macroscopic diffusion)
- **Fourier transform → Central Limit Theorem** (characteristic function proof)
- **Laplace equation → Complex analysis** (harmonic functions = real parts of holomorphic functions)
- **Wave equation → Geometry** (Huygens' principle = light travels along geodesics)

## Reflection Anchors

- Fourier said "any function" and was ridiculed. He was essentially right. What does this teach us about bold claims?
- Navier-Stokes existence/smoothness is a Millennium Prize problem. Why is fluid flow still mysterious?
- Are PDEs "applied" or "pure"? The history says the distinction is meaningless.
