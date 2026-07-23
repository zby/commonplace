---
gate_id: semantic/explication-quality
name: Explication quality
description: 'A definition names a term without sharpening its ordinary meaning, boundary, contrasts, or operational use for the KB.'
type: kb/types/review-gate.md
lens: semantic
watches: [body]
staleness: changed
requires_type: kb/types/definition.md
---

## Failure mode

The note names a term but does not actually sharpen it. The instructions call for *explication* in Carnap's sense — replacing a vague, overloaded, or borrowed term with a precise one that serves KB work — but a reader finishes the note with the same ambiguity they started with. Either the definition restates the ordinary meaning, the sharpening is invisible (no contrast with prior use, no boundary), or the note buries the operational meaning under philosophical survey.

## Test

Apply Carnap's four explication criteria to the definition:

1. **Similarity.** Identify the explicandum — the ordinary, overloaded, or borrowed term the note is sharpening. Check that the note names it and that the sharpened meaning still connects to that starting point, rather than drifting into a different concept under the same label.
2. **Exactness.** Check that the reader can state what falls inside and outside the term. Look for explicit scope, exclusions, or contrasts with nearby concepts. A definition that treats its boundary cases as interchangeable with the core meaning fails this test.
3. **Fruitfulness.** Check that the note shows what the sharpened term enables — workflows, review gates, arguments, or decisions that depend on this meaning. A term with no operational payoff is decorative.
4. **Simplicity.** Check that the definition is as simple as the operational purpose allows. Philosophical surveys, historical tours, or taxonomies that outweigh the sharpened meaning violate this test; the definition instructions explicitly prohibit them.

WARN when the explicandum is missing, the boundary is absent, the operational payoff is absent, or the apparatus outweighs the definition. INFO when any criterion is present but thin — plausible but not yet sharp enough to constrain future use.

Boundary: this gate tests explication quality only — the four criteria above are the whole test. Whether the note satisfies the rest of the definition type's contract (required sections, linking, template shape) belongs to the note's type-conformance pair, whose gate is the type spec itself; do not re-flag general contract violations here.
