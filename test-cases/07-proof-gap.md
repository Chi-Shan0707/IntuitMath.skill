# Test Case: Proof Gap / Hidden Assumption

**Question**:

> Find the flaw: Since \(a_n \to 0\), the series \(\sum a_n\) converges.

## Expected Pattern

1. **MOTIVATION**: Explain why the claim feels tempting.
2. **SKEPTIC PASS**: Identify the hidden assumption: terms going to zero is
   necessary, not sufficient.
3. **COUNTEREXAMPLE**: Use the harmonic series \(a_n=1/n\).
4. **RIGOR**: Show divergence by grouping or integral comparison.
5. **REPAIR**: State a true sufficient condition, e.g. comparison, ratio test,
   absolute convergence, or \(p\)-series with \(p>1\).

## Key Elements to Check

- [ ] Contains the phrase "necessary but not sufficient" or equivalent.
- [ ] Uses a concrete counterexample.
- [ ] Shows why the counterexample diverges.
- [ ] Offers a repaired theorem.
- [ ] Ends with refined intuition about tail size vs term size.
