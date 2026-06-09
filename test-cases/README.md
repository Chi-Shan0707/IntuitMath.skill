# IntuitMath Test Cases

This directory contains example Q&A pairs and multi-agent workflow demonstrations
for validating that IntuitMath produces high-quality responses.

## Structure

Each test case shows:
- **Question**: The user input
- **Expected pattern**: The structure IntuitMath should follow
- **Key elements checked**: What the response must include
- **Example output**: A representative response
- **Capability surface**: Dialog, OCR, HTML, web/source verification, or saving

## Validation

Run through these cases after any significant change to verify
that the skill still produces coherent, motivation-first responses.

Suggested coverage:

- `01-lebesgue-integral.md`: concept motivation and cross-domain explanation
- `02-epsilon-delta.md`: historical crisis and rigorous repair
- `03-eigenvalues-history.md`: history plus applications
- `04-ocr-math-image.md`: transcription-first image/PDF workflow
- `05-html-note.md`: standalone KaTeX note generation
- `06-false-conjecture.md`: counterexample and refined theorem
- `07-proof-gap.md`: proof audit and hidden assumptions
- `08-multi-agent-trace.md`: useful-not-forced role workflow
