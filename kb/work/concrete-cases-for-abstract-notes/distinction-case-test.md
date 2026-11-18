---
gate_id: semantic/distinction-case-test
name: Distinction case test
description: 'A note draws a distinction that does not sort concrete cases cleanly: a case fits both sides, fits neither, or its side depends on a word the note leaves open.'
type: types/review-gate.md
lens: semantic
watches: [body]
staleness: changed
depth: 2
---

<!-- Draft in kb/work/concrete-cases-for-abstract-notes/. Not in the catalog. -->

## Failure mode

The note's central contribution is a distinction, and the distinction reads well in general terms but fails on a particular case. One of these happens when a concrete case is put through it:

- the case satisfies the stated criteria of both sides;
- the case satisfies neither, though the note presents the sides as covering the situations it discusses;
- which side the case falls on depends on the meaning of a word the note uses and does not fix;
- the case falls cleanly on a side, but the note draws from that side a conclusion the case does not support;
- the two sides lead to the same action, expectation and check, so the distinction changes nothing.

Fluent general wording hides these. A particular case exposes them.

## Test

1. State the central distinction in one sentence, and for each side copy the criterion the note gives for membership, in the note's words. If the note's central contribution is not a distinction, return PASS; this gate does not apply. If a side has no stated criterion, record that and use the nearest statement the note makes.
2. State what the note says differs between the sides: what one should do, expect, report or check. If the note states no difference, record that.
3. Build four cases. Each is a particular situation with enough detail to judge, drawn from the note's own domain. Prefer a case the note or a note it links to mentions; otherwise construct one and say it is constructed.
   - **A plain case for each side**: the kind of situation the author had in mind.
   - **A mixed case**: a situation with features of both sides.
   - **A lapsed or changed case**: a situation that was plainly on one side and where one feature has since changed, such as a rule nobody follows any more, a step that became optional, or a role that was reassigned.
4. Sort each case using only the criteria copied in step 1. Do not use a better criterion the note does not state. For each case record the side, or `both`, `neither`, or `depends on <word>` with the two readings of that word.
5. For each case that sorts cleanly, check the note's stated difference from step 2 against it: does the action, expectation or check the note attaches to that side fit the case?
6. Check the note's own text for the result. A note that names the hard case and says how it is handled, or limits its scope to exclude it, passes on that case. Judge what is on the page.

WARN when a plain case fails to sort cleanly, or when the mixed or lapsed case sorts as `both`, `neither` or `depends on`, and the note neither handles that case nor excludes it by scope. Quote the criterion, give the case in two or three sentences, and state the result.

WARN when the note states no difference between the sides, or when the stated difference is the same for both.

PASS when all four cases sort cleanly and the stated difference fits them, or when the note handles or excludes the ones that do not. Under a PASS decision, add an INFO finding when a case sorts only under a reading the note supports but does not state, or when a constructed case is far from the situations the note discusses.

This gate does not return FAIL. The cases are the reviewer's constructions, so a failed sort is a reason to look, not a ground for escalation.

Do not repair. Do not propose a new criterion; report the case and where the stated criterion fails on it.

Do not flag here: an enumeration or taxonomy that leaves out part of the space it claims to cover (`semantic/completeness-boundary-cases`); an assertion with two readings where no case is needed to show it (`semantic/underspecified-assertions`); a scope wider than the support (`semantic/unwarranted-scope`); a note that shows no case of its own (`accessibility/abstract-claim-without-case`). This gate is about whether the distinction survives cases the reviewer builds.

## Example (fail)

A note separates a *wait* (execution cannot proceed until a person acts) from a *required task* (the specification assigns it). The stated difference: removing a wait is automation; removing a required task is a change of requirements that must be reported.

Lapsed case, constructed: the specification assigns a weekly review, and nobody has done it or treated it as binding for a year. Sorting: `depends on "required"`. If required means written in the specification, the review is a required task and automating around it conceals an omission. If required means still endorsed by the process owner, it is stale text and nothing is concealed. The note does not say which, and does not exclude the case.

## Example (pass)

The same note adds: "A requirement that has lapsed in practice is still reported: its lapse is a retirement of the requirement." The lapsed case now sorts the same way under both readings, and the stated difference fits it.
