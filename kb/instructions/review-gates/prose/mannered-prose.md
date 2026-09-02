---
gate_id: prose/mannered-prose
name: Mannered prose
description: 'The note uses figurative flourish that adds reading effort or unintended connotations without improving the statement.'
type: kb/types/review-gate.md
lens: prose
watches: [body]
staleness: changed
---

## Failure mode

The failure is not metaphor itself. It is figurative wording whose main effect
is ornament: it does not usefully compress, clarify, or structure the idea, but
it makes the reader translate an image or introduces connotations that the note
does not establish.

## Test

Scan the body for conspicuous metaphors, idioms, and other figurative phrases
used to state a claim, relation, action, or transition. For each candidate:

1. State the intended literal meaning with its qualifications. The existence of
   this paraphrase is not by itself a failure.
2. Ask what the figurative form contributes. Keep it when it functions as
   precise technical shorthand, concisely names a recognized pattern, sharpens
   a real contrast, clarifies a mechanism, or supplies a mapping that the later
   explanation uses.
3. Check the source image's added connotations, such as agency, deservingness,
   direction, continuous control, causal mechanism, scale, or certainty. Ask
   whether the note means and supports them.
4. Flag the phrase only when the literal version is at least as clear and the
   figurative version both contributes no useful precision, compression,
   contrast, or explanation and adds interpretation work or unsupported
   connotations.

For each finding, quote the phrase, give a literal replacement, and state what
ambiguity, connotation, or reading effort the replacement removes. Do not infer
the writer's motive. Do not flag a metaphor merely because it is vivid or
because a literal paraphrase exists. An arguable preference between two equally
clear formulations is not a finding.

Return WARN for one or more local instances. Return FAIL only when the pattern
is pervasive enough to obstruct a direct reading of the note. Return PASS when
no phrase meets the test. Return ERROR only when the target text cannot be
inspected.

Do not duplicate a finding that is wholly owned by a more specific gate. A
model cognition claim belongs to `prose/anthropomorphic-framing`; an unmapped
source-domain residue belongs to `prose/source-residue`; and a removable filler
sentence belongs to `sentence/stock-phrases`. Apply this gate when a needed idea
remains but its wording should become literal.

## Example (fail)

> A dial worth turning.
>
> This point earns its keep.

The intended claims are only that a parameter should be varied and a point
remains relevant. `Dial` adds continuous manual control, while `earns its keep`
adds deservingness. The text uses neither connotation.

## Example (pass)

> A parameter worth varying.
>
> This point still matters.

These phrases state the intended ideas directly.

## Example (pass — conventional metaphor)

> The retained prior version is a safety net if validation fails.

`Safety net` is familiar and concise, and its protective connotation matches
the function described. It does not add an unsupported mechanism or judgment.

## Example (pass — explanatory mapping)

> Treat the filter as a sieve: each stage removes candidates that violate one
> named constraint, and the next stage examines what remains.

The passage states the mapping and uses it to explain the staged filtering
mechanism.
