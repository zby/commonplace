---
description: "Decision that the type and collection conformance reviews stop judging the title and description properties four frontmatter gates already judge, and that three pairs of catalog gates asking one question are merged"
type: reference/types/adr.md
tags: []
status: accepted
---

# 131-Conformance reviews leave titles and descriptions to their gates

**Status:** accepted
**Date:** 2026-11-14
**Amends:** [ADR 038](./038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) and [ADR 041](./041-collection-conformance-reviews-use-collection-md-as-the-gate.md): their wrappers no longer ask for the title and description properties that catalog gates own.

## Context

The review operations are being treated as one pool of atoms for a single
improvement procedure. Reading every criterion side by side showed the
same question asked by several of them.

A title's claim shape was judged three times per note. The type wrapper
applied the whole type spec, the collection wrapper named "title and
description conventions" among what it judges, and the frontmatter bundle
has dedicated gates: `title-as-claim`, `claim-strength`,
`title-composability` and `description-discrimination`. The theory
contract itself says the `title-as-claim` trait exists so that review
gates check the promise.

Three pairs of catalog gates also had one failure mode each:
`prose/confidence-miscalibration` with `semantic/epistemic-status-blur`,
`prose/pseudo-formalism` with `complexity/framework-decoration`, and
`prose/bridge-paragraph-duplication` with `prose/redundant-restatement`.

A repeated question costs a launch each time and yields findings that
disagree or repeat, and the disposition work downstream cannot tell a
second opinion from a second problem.

## Decision

Both conformance wrappers carry one added instruction. Catalog gates judge
four properties for every note: whether a claim title is a proposition,
whether it is contestable, whether it composes as a linkable phrase, and
whether the description discriminates the note. The conformance reviewer
leaves those to their gates and judges a title or description only against
a convention its own document adds. The collection wrapper's list of what
it judges changes accordingly: placement, quality goal, outbound linking
rules, and the title and description conventions specific to the
collection.

Three gates are retired into their partners:

- `semantic/epistemic-status-blur` takes the checks of
  `prose/confidence-miscalibration`: the note's own construction asserted
  as established, and a well-supported finding hedged without reason.
- `complexity/framework-decoration` takes the checks of
  `prose/pseudo-formalism` for notation and equations.
- `prose/redundant-restatement` takes the check of
  `prose/bridge-paragraph-duplication` for a closing preview.

The catalog goes from 43 gates to 40.

## Considered alternatives

Remove title and description from the conformance reviews entirely.
Rejected: types and collections add conventions no catalog gate knows,
such as an instruction's trigger-shaped description or a collection's
naming rule. Those stay with the document that states them.

Keep the conformance reviews as the owner and retire the frontmatter
gates. Rejected: the gates have one failure mode and one test each and can
be calibrated alone; a whole-document review cannot.

Merge `sentence/concept-attribution` into `sentence/misleading-link-text`.
Not done: [ADR 082](./082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md)
gives them different units, every identity claim and every link, with a
grounding ladder for each. They are one question at two units, not one
question twice.

Merge the remaining overlaps with the compression bundle, the adversarial
reports and the higher-order check. Deferred until those operations sit in
one pool with the gates.

## Consequences

One launch per note no longer re-judges what four gates judge. A sweep
that requests only the `type` or `collection` lens no longer covers a
claim title's strength or the description's discrimination; those need the
`frontmatter` bundle, which `--all-gates` includes.

The wrappers are outside the freshness hashes, so no stored conformance
result becomes stale; results written before this change may still carry
title and description findings. The two surviving merged gates changed
text, so their stored results are stale. Stored results of the three
retired gates no longer have a criterion and are not removed by this
decision.

The operativity path: the wrapper text is supplied to every type and
collection review worker by the gate sweep, and the catalog is read from
`kb/instructions/review-gates/` at each sweep.
