# Test Case: HTML / KaTeX Note

**Question**: "Make a beautiful HTML note explaining why eigenvalues matter."

## Expected Pattern

1. **LOAD**: Use `references/html-output.md` and `templates/math-note.html`.
2. **STRUCTURE**: Fill motivation, intuitive derivation, rigor, perspectives,
   cross-domain connections, and reflection.
3. **MATH**: Prefer KaTeX-safe delimiters such as `\(Ax=\lambda x\)`.
4. **ARTIFACT**: Write an `.html` file when file tools are available.
5. **REPORT**: Tell the user the generated path, or return copyable HTML if no
   file/artifact support exists.

## Key Elements to Check

- [ ] Does not dump a raw unstructured essay into HTML.
- [ ] Includes a pre-rigorous geometric explanation before `det(A-\lambda I)=0`.
- [ ] Includes at least three cross-domain uses that clarify the concept.
- [ ] Uses the template placeholders or `scripts/render-html.py`.
- [ ] Notes CDN KaTeX vs offline/bundled mode if relevant.
