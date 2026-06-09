# Test Case: False Conjecture / Counterexample

**Question**: "I think every continuous function is differentiable somewhere. Prove it."

## Expected Pattern

1. **SKEPTIC FIRST**: Do not try to prove a false statement.
2. **NAIVE INTUITION**: Explain why the claim feels plausible from smooth
   examples and graphs.
3. **COUNTEREXAMPLE**: Give a correct counterexample, such as the Weierstrass
   function for "nowhere differentiable continuous", or a simpler correction if
   the user only needs an accessible discussion.
4. **REFINEMENT**: State a true nearby theorem, such as differentiability
   almost everywhere for absolutely continuous functions, or Rademacher's
   theorem for Lipschitz functions.
5. **REFLECTION**: Ask what regularity condition turns visual smoothness into
   differentiability.

## Key Elements to Check

- [ ] Identifies the statement as false.
- [ ] Does not hallucinate a proof.
- [ ] Explains what intuition broke.
- [ ] Provides a true repaired theorem with assumptions.
- [ ] Distinguishes continuous, absolutely continuous, and Lipschitz if used.
