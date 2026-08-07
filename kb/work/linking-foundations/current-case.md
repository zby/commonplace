# Current case: from direction repair to mechanism ambiguity

This file records the concrete work that opened the foundations question. Counts are dated baselines from successive reviews, not timeless corpus facts.

## What changed

### Collection ownership and reciprocal links

The work began by correcting the idea that links are simply forward-authored and asymmetric, with backlinks as the only reverse surface. The current rule is more precise: the source collection governs outbound authorization; each direction is independently authored when it serves a reader need; semantic symmetry does not require mirrored Markdown; and a useful reciprocal edge is allowed rather than discouraged. Backlinks remain a derived inbound view, not a prohibition on reciprocal authoring.

The collection contract can authorize local collection destinations, the reserved `external` destination, or literal `any`, which includes `external`. This made destination permission independent from label semantics.

### Directional grammar

[ADR 058](../../reference/adr/058-directional-identifiers-use-source-as-subject.md) adopted the invariant:

> Every directional identifier completes `source <label> target`.

The source is the artifact containing the Markdown edge. A reader should not need a collection table to discover that the identifier silently describes the target's role instead.

### Evidence migration

The old `evidence` identifier was used for both assertion→observation and observation→assertion. The review found that both reader journeys were real rather than accidental reciprocity. ADR 058 therefore adopted:

- `source evidenced-by target` for assertion→observation;
- `source is-evidence-for target` for observation→assertion.

The migration covered 207 active old-label edges, including 26 inverse-journey cases, and updated contracts, current guidance, and the mutable corpus together (`b3f7e126`). It established the reusable rule that semantic classification precedes mechanical replacement.

### Rationale and off-pattern grounds

The old `rationale` identifier also described the target: the target was the rationale on which the source depended. Corpus review found 134 active edges in three semantic groups rather than one renameable relation. [ADR 060](../../reference/adr/060-rationale-becomes-rests-on-and-off-pattern-grounds-reclassified.md) adopted `source rests-on target` for design, description, procedure, rule, and system-definition dependence.

The migration (`dac39977`) assigned the 134 old `rationale` rows as:

| successor | rows |
|---|---:|
| `rests-on` | 114 |
| `evidenced-by` | 15 |
| `is-evidence-for` | 2 |
| `implements` | 2 |
| `compares-with` | 1 |

It also reclassified 38 off-pattern `grounds` rows: 8 to `rests-on`, 20 to `evidenced-by`, and 10 to `is-evidence-for`. The remaining 276 note→note `grounds` edges were deliberately preserved for a separate premise review. The evidence and rationale runs supplied the repeated mechanical core now recorded in [Migrate a directional link label](../../instructions/migrate-directional-link-label.md).

### Grounds evaluation and adjudication

The [grounds direction review](../linking-contract-consistency/grounds-label-direction-review.md) rebaselined 283 active rows: the preserved 276 note→note cohort plus seven newly authored sources→notes evidence mappings. It recommended `premised-on` for 160 clear premise dependencies while finding 49 mechanism/explanation rows, 23 extensions or specializations, 39 mixed definition/lineage/comparison/navigation rows, and 12 evidence rows.

The [maintainer adjudication](../linking-contract-consistency/grounds-label-boundary-adjudication.md) accepted `premised-on` and assigned exact successors to the evidence, extension, and mixed cohorts. Eight rows from the coarse X/D buckets proved to be premise dependencies on closer inspection:

| disposition | rows at adjudication baseline |
|---|---:|
| `premised-on` | 168 |
| `extends` | 23 |
| `defined-in` | 13 |
| `exemplifies` | 12 |
| `is-evidence-for` | 9 |
| `evidenced-by` | 8 |
| `see-also` | 1 |
| deferred mechanism evaluation | 49 |

This reconciles the 283-row review baseline. A later mechanism scan found 285 active `grounds` rows—278 notes→notes and seven sources→notes—showing again that review counts drift while work is in flight. The two newer note→note rows still require disposition before implementation.

## The mechanism problem

At the next baseline, the active surface contained 79 edges literally labeled `mechanism`—78 notes→notes and one reference→notes—plus the 49 `grounds` rows deferred as mechanism-like. Nine source files author both old labels. Their local use does not establish a stable distinction: `mechanism` sometimes names a prerequisite or explanatory theory, while `grounds` sometimes names an operational path.

The unadjudicated [mechanism direction review](../linking-contract-consistency/mechanism-label-direction-review.md) reconciles all 128 candidate tuples and recommends a split:

| semantic class | rows | proposed treatment |
|---|---:|---|
| explanatory relation | 41 | candidate `explained-by` |
| operational mechanism | 72 | candidate `operates-through` |
| enabling condition or prerequisite | 10 | defer to `enables` / `precondition` review |
| extension or exemplification | 3 | exact existing relation still selected per row |
| premise | 1 | `premised-on` |
| evidence | 1 | `is-evidence-for` |

The report was requested for Luna, but its own provenance says Luna execution was not verified; the attempted local `--model luna` dispatch failed because this account does not support that model. Treat its semantic split as evidence awaiting maintainer review, not an adopted decision. Its 128-row ledger reconciles structurally, but structural validation does not establish that the artifact/claim/phenomenon distinction was applied correctly.

## Why this is a foundational problem

The candidate split exposes at least three different assertions:

1. a source claim is **explained by** a target claim;
2. a source phenomenon or capability **operates through** a target process or component;
3. a source assertion is **premised on** a target claim about how something works.

These are not merely alternative names. `explained-by` is an epistemic or discourse relation between claims; `operates-through` is a stronger subject-matter claim about productive organization; `premised-on` records an inferential dependency. Yet Markdown endpoints are artifacts, whose claim titles sometimes stand in for propositions and sometimes describe systems or phenomena. A grammatically correct identifier can therefore still cross levels invisibly.

The distinction also changes maintenance:

- rejecting an explanation calls for revisiting the source's explanatory account but need not falsify the phenomenon;
- changing a process or component calls for operational or interface review;
- rejecting a premise reopens the source assertion's truth or applicability;
- losing evidence changes its support record;
- removing an associative neighbor need not invalidate anything.

The current reader-need test catches part of this—“verify,” “understand how,” “inspect the process”—but does not by itself say what the source asserts or what revision should propagate.

## What the foundations workshop must settle

- Whether formal identifiers primarily encode a subject-matter assertion, an inferential role, a discourse function, or a revision consequence.
- Whether `explained-by` and `operates-through` remain reliably distinguishable when endpoints are notes rather than literal phenomena and mechanisms.
- Whether a relation signature must state source role and target role, or whether collection plus claim title supplies that context cheaply enough.
- Whether the operational-mechanism category from the 128-edge review survives independent adjudication using the stricter philosophy-of-mechanism test.
- Whether prerequisite relations should be handled as a separate family before any mechanism migration.
- Which distinctions improve agent follow/skip, reasoning, or maintenance behavior enough to justify their authoring cost.

Until these questions are answered, the consistency workshop can preserve inventories and exact non-mechanism dispositions, but it should not adopt or migrate `explained-by` or `operates-through`.

