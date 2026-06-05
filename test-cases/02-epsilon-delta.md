# Test Case: The Epsilon-Delta Definition

**Question**: "Why is the epsilon-delta definition of a limit so complicated? Why can't we just say 'approaches'?"

## Expected Pattern

1. **TOOLKIT RECONSTRUCTION**: Before Cauchy (1820s), mathematicians (Euler, Newton) used "infinitesimals" and "fluxions" — intuitive but logically shaky
2. **THE CRISIS**: Euler's formal manipulation of series produced paradoxes — Grandi's series 1-1+1-1+... "equals" both 0 and 1/2 depending on how you group it
3. **THE BOLD ATTEMPT**: Euler's "principle of algebraic consistency" — manipulate series as if they were finite — gave beautiful results but contradictions
4. **THE INVENTION**: Cauchy's ε-N and ε-δ reduced limit to a finitary condition checkable without knowing the limit value
5. **MODERN PERSPECTIVE**: Nonstandard analysis (Robinson, 1960s) rehabilitated infinitesimals in a rigorous way — showing Cauchy's definition wasn't the only possible one

## Key Elements to Check

- [ ] Shows pre-Cauchy intuition (Newton's fluxions, Euler's formal algebra)
- [ ] Concrete paradox demonstrated (Grandi's series or similar)
- [ ] Explains why "gets arbitrarily close" needs a precise definition
- [ ] Shows Cauchy's move as a *reduction to finitary conditions*
- [ ] Mentions nonstandard analysis as alternate rigorous approach
- [ ] Ends with reflection anchor

## Example Output (Abbreviated)

> **Before Cauchy (1700s).** Euler manipulated infinite series the way you manipulate finite expressions. If 1/(1-x) = 1 + x + x² + ..., then plugging x = -1 gives 1 - 1 + 1 - 1 + ... = 1/2. Beautiful. But grouping as (1-1) + (1-1) + ... gives 0. Which is it? The "algebraic" principle gave no way to decide.
>
> **[Bold assumption: maybe all these groupings should give the same answer — after all, finite sums don't care about parentheses.]**
>
> **Cauchy's move (1821).** Instead of defining "the sum" directly, he defined "the limit of the partial sums." This shifted the question from an infinite process to a finite condition: for any ε > 0, there exists N such that... The definition tells you *how to check* convergence without needing to know the limit.
>
> **Something to sit with.** In the 1960s, Abraham Robinson showed you CAN make infinitesimals rigorous (nonstandard analysis). So why does everyone still teach Cauchy's ε-δ? What makes one rigorous formalism succeed over another?
