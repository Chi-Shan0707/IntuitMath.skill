# Test Case: Lebesgue Integral Motivation

**Question**: "Why do we need the Lebesgue integral? What's wrong with Riemann?"

## Expected Pattern

1. **MOTIVATION**: Show a concrete function Riemann fails on (Dirichlet function)
2. **TOOLKIT RECONSTRUCTION**: What tools did mathematicians have in 1900? What was missing?
3. **PRE-RIGOROUS**: Intuitive "range partition" idea before measure theory
4. **RIGOROUS**: Formal measure definition, dominated convergence
5. **CROSS-DOMAIN**: Probability expectation, quantum L² spaces, signal processing
6. **REFLECTION ANCHOR**: Why didn't Henstock-Kurzweil replace Lebesgue?

## Key Elements to Check

- [ ] Starts with the *failure* of Riemann, not the definition of Lebesgue
- [ ] Shows the Dirichlet function as concrete counterexample
- [ ] "Upper sum = 1, lower sum = 0" computation present
- [ ] Lebesgue's move presented as: partition range, not domain
- [ ] At least one bold assumption annotated
- [ ] Cross-domain connections shown (probability, physics, signal processing)
- [ ] Ends with an open question
- [ ] No textbook-style "Definition → Theorem" ordering

## Example Output (Abbreviated)

> **The crisis.** The Riemann integral works beautifully for continuous functions on [a,b]. But by the 1890s, mathematicians kept bumping into functions it couldn't handle. The most notorious: the Dirichlet function — 1 on the rationals, 0 on the irrationals.
>
> **A bold attempt.** Let's try to Riemann-integrate the Dirichlet function on [0,1]. Every upper sum = 1 (rationals are dense). Every lower sum = 0 (irrationals are dense). The upper and lower integrals don't agree. Dead end.
>
> [Bold assumption: maybe the "area" should just be 0 — the rationals are countable, they take up no space.]
>
> **Lebesgue's move (1901).** Riemann partitions the *domain* — chop [0,1] into intervals. Lebesgue partitions the *range* — collect all the x where f(x) takes a given value, and measure that set. For the Dirichlet function: {x : f(x)=1} is the rationals (measure 0); {x : f(x)=0} is the irrationals (measure 1). The integral is 1·0 + 0·1 = 0. Done.
>
> **Why it matters beyond analysis.** The Lebesgue integral isn't just a technical fix — it's the foundation of probability theory, quantum mechanics (L² spaces), and modern analysis.
>
> **Something to sit with.** There is an integral that handles even more than Lebesgue — the Henstock-Kurzweil integral. It never caught on. Why?
