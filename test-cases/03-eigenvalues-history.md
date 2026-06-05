# Test Case: Eigenvalues — Historical Origin

**Question**: "Where do eigenvalues come from? Why do they matter?"

## Expected Pattern

1. **TOOLKIT RECONSTRUCTION**: Before eigenvalues (pre-1800), mathematicians could solve linear systems (Cramer, Gauss) and work with quadratic forms
2. **THE CRISIS**: Analyzing the shape of a quadric surface (ellipsoid, hyperboloid) required finding its "principal axes" — directions where the quadratic form becomes diagonal
3. **THE BOLD ATTEMPT**: Lagrange and others tried coordinate transformations by hand — worked for 2×2 but impractical beyond
4. **THE INVENTION**: Cauchy (1829) formulated Ax = λx and det(A - λI) = 0 — the eigenvalue problem. This simultaneously solved principal axes AND diagonalization
5. **WHY IT MATTERS**: Quantum mechanics (energy levels = eigenvalues), Google PageRank (largest eigenvector), PCA (eigenvectors of covariance matrix), vibration analysis (natural frequencies)

## Key Elements to Check

- [ ] Connects eigenvalues to the geometric problem of principal axes
- [ ] Shows eigenvalues emerged from quadratic forms, not abstract algebra
- [ ] Explains why "eigen" (German for "own/characteristic") fits
- [ ] Cross-domain: at least 3 applications from different fields
- [ ] Shows that the concept naturally extends (spectral theorem, SVD)
- [ ] Ends with reflection anchor

## Example Output (Abbreviated)

> **The crisis.** By the early 1800s, mathematicians could solve linear systems and work with quadratic forms. But analyzing the shape of a quadric surface — is it an ellipsoid or a hyperboloid? — required finding its "principal axes": the directions where the quadratic form becomes diagonal. For 2×2 this was manageable. For 3×3, a mess. For n×n, hopeless by hand.
>
> **[Bold assumption: maybe the directions that diagonalize a quadratic form are the fixed directions of some transformation — the ones that don't rotate.]**
>
> **Cauchy's move (1829).** He formulated Ax = λx: find vectors that don't change direction under A, only scale. The eigenvalues λ are the scaling factors. The equation det(A - λI) = 0 gave a single polynomial whose roots are all eigenvalues. This simultaneously solved principal axes AND diagonalization — the eigenvectors ARE the principal axes.
>
> **Why it matters everywhere.** Eigenvalues didn't stay in geometry. Quantum mechanics: every observable's possible values are eigenvalues of an operator. Google PageRank: the ranking vector is the largest eigenvector of the link matrix. PCA: the principal components are eigenvectors of the covariance matrix. Vibration analysis: natural frequencies are eigenvalues of the stiffness matrix.
>
> **Something to sit with.** The spectral theorem says every real symmetric matrix is orthogonally diagonalizable. What about non-symmetric matrices — what replaces eigenvalues? (Hint: singular values — and they also have a beautiful geometric interpretation.)

## Note

This case tests the cross-domain connection engine heavily — eigenvalues may be the most cross-disciplinary concept in all of mathematics.
