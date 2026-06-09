# Test Case: OCR / Screenshot Math Input

**Question**: User uploads a screenshot of a handwritten problem:

> Evaluate `\int_0^1 x^2 e^{-x}\,dx` and explain the method.

The lower limit might visually look like `O`, and the exponent might be
misread as `-x^2`.

## Expected Pattern

1. **TRANSCRIPTION**: State the recovered formula in LaTeX before solving.
2. **ASSUMPTIONS**: Explicitly note uncertain symbols and confidence.
3. **PRE-RIGOROUS**: Explain why integration by parts or parameter methods fit.
4. **RIGOROUS**: Carry out the calculation carefully.
5. **CHECK**: Verify positivity and rough size.

## Key Elements to Check

- [ ] Does not solve before showing transcription.
- [ ] Marks ambiguity if OCR confidence is low.
- [ ] Asks for clarification only if ambiguity changes the answer.
- [ ] Uses LaTeX for recovered math.
- [ ] Includes a sanity check against the integrand and interval.

## Example Output Shape

```markdown
## Transcription
page 1, main equation, high confidence:
\[\int_0^1 x^2 e^{-x}\,dx\]

## Assumptions
- The lower limit is `0`, not the letter `O`.
- The exponent is `-x`, not `-x^2`.

## Solution
...

## Check
The integrand is positive and bounded by `x^2`, so the answer should lie
between `0` and `1/3`.
```
