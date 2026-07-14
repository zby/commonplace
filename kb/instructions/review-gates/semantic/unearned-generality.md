---
gate_id: semantic/unearned-generality
name: Unearned generality
description: 'A claim is stated in vocabulary more abstract than its argument uses — the wording widens what the claim covers without changing what it forbids.'
type: kb/types/review-gate.md
lens: semantic
watches: [title, description, body]
staleness: changed
requires_trait: title-as-claim
---

## Failure mode

The central claim is stated in vocabulary more abstract than the argument uses — "note" written as "retained artifact", "agent" as "bounded consumer", "fails" as "exhibits degraded conformance". The abstraction is adopted defensively, to cover a case the concrete wording would have excluded, rather than because the reasoning operates at that level.

A claim's content is what it rules out. Widening the vocabulary extends the class of cases the claim covers while weakening what it says about each one, so the claim covers more and forbids no more than before. Coverage is not content.

This is the mirror of `semantic/load-bearing-qualifiers`, which catches a qualifier that **narrows** a claim without doing work in the argument. A note can fail both, in different terms.

## Test

Identify the central claim from the title, description, and opening argument. For each abstract term in it:

1. Name the concrete term it stands in for — the narrower word the note would use if it described only the case it argues from. If the examples, mechanism, and evidence all speak about notes, ask why the claim says "retained artifacts".
2. **Downgrade test.** Substitute the concrete term back and re-read the central argument. If the mechanism, evidence, and conclusion are unchanged, the abstraction is not load-bearing.
3. **Forbids-test.** Name a case the abstract wording rules out that the concrete wording allowed. An earned abstraction can answer — the general concept excludes what the narrow one permitted.
4. Treat an answer that names cases the claim now *covers*, rather than cases it now *forbids*, as a positive signal of failure, not merely a missing answer.
5. **Check whether the reach is argued.** Generality earned by argument passes even when step 2 leaves the primary argument intact — the note says why the mechanism does not depend on the narrower term, and ideally exhibits a second instance under the general term. A single instance class with no such argument is what makes an abstraction unearned.
6. **Check distribution.** Abstraction concentrated where the argument needs it is the healthy shape. Abstraction spread across most nouns in most sentences, with no single load-bearing site, is grounds for WARN even when no individual term is clearly indefensible.

WARN when a non-load-bearing abstraction widens the central claim or the filename-level title, or when abstraction is distributed with no load-bearing site. INFO when the abstraction is probably unearned but the note gestures at a second instance class without developing it.

Do not flag here: notation or formal decomposition that adds no precision (`prose/pseudo-formalism`); qualifications and escape hatches added to protect a claim from counterexamples (`semantic/explanatory-reach`, ad-hoc accommodation); a KB term defined once and then reused opaquely (`accessibility/jargon-persistence`). This gate is about vocabulary altitude in the claim itself.

Judge the abstraction present in the artifact. Do not repair the claim while reviewing.

## Example (fail)

Title: "Retained artifacts must record the applicability envelope of derived content."

The body argues about KB notes: the mechanism is note frontmatter, the evidence is two note reviews. Downgrading to "Notes must record where a distilled claim stops applying" leaves the argument unchanged, and the abstract title excludes nothing the concrete one allowed — asked what it adds, the note's scope section says it "also covers skills, schemas, and memory records". Coverage, not content.

## Example (pass)

Title: "Distillation strips lineage, so the dependency record must live outside the artifact."

"Artifact" is general and the argument earns it: the mechanism turns on distillation discarding its inputs — a property of the operation, not of the output format — and the note works both notes-from-sources and instructions-from-notes under the general term, so downgrading to "note" would demote the second instance to a special case. The general claim forbids storing lineage inside any distilled output, including the instruction case a note-scoped claim leaves open.

---

Relevant Notes:

- [generality bought to avoid counterexamples is paid for in precision](../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — rationale: the universality/precision trade this gate tests for
