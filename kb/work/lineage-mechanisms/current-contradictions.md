# Current lineage contradictions

This ledger separates contradictions in Commonplace's current lineage rules from the workshop's broader open design space. Each item already has conflicting live witnesses; resolving it requires choosing or scoping a rule, not merely inventing a future feature.

## 1. Source-side lineage is stated as universal, but articles store it target-side

The shared [link vocabulary](../../reference/link-vocabulary.md#lineage-semantics) says lineage is recorded at the source and that the downstream artifact carries no source backlink by default. The [writing skill](../../instructions/cp-skill-write/SKILL.md) makes the rule categorical: add an `... into:` footer to the source, and do not link back from the produced artifact.

The article profile deliberately uses the opposite carrier. [`source_notes`](../../articles/COLLECTION.md) is stored on the downstream article, validated there, and searched to find articles affected by a note change. The archived proposal makes the exception explicit: article-side only, with no source-side `Adapted into:` footer in v1.

**Operational consequence:** a generic `cp-skill-write` run can follow its universal mechanics and violate the article contract. The shared vocabulary also describes a repository-wide default that no longer covers every shipped profile.

**Decision needed:** make lineage placement contract-specific and give the write path a discoverable override mechanism, or narrow articles back to the source-side convention.

## 2. Source-side footers are impossible on immutable snapshots

The shared lineage rule says a derivation dependency is recorded in the source's footer. The [sources collection](../../sources/COLLECTION.md#outbound-links) prohibits editing or annotating captured snapshots after capture. A note abstracted or derived from such a snapshot therefore cannot record the relationship using the prescribed source-side footer.

The working workaround is downstream links from notes and descriptive reviews to snapshots. That can be a sound carrier, but it is currently an exception created by necessity rather than a declared lineage-placement rule.

**Operational consequence:** authors must choose between violating snapshot immutability and violating the universal lineage procedure.

**Decision needed:** specify the carrier for immutable and externally owned sources—target-side metadata/link, a mutable ingest companion, or an external edge record—and state how change impact is surfaced from that carrier.

## 3. Lineage relation direction and recording direction are conflated

The vocabulary names semantic relations from downstream to upstream (`derived-from`, `abstracted-from`, `adapted-from`, `operationalized-from`) while prescribing source-side `Derived into:`, `Abstracted into:`, `Adapted into:`, and `Operationalized into:` footers. These can be two renderings of one normalized relation, but the system does not currently declare that normalized direction independently of its storage surface.

The ambiguity appears in collection rules. [Notes](../../notes/COLLECTION.md#outbound-links) authorize `abstracted-from` from a generalizing note to a source, while [sources](../../sources/COLLECTION.md#outbound-links) authorize the same asymmetric label from an ingest/source review to a note and explain it as “this claim was abstracted from this source.” The label is therefore authorized on both orientations of the same relationship.

**Operational consequence:** inversion cannot reliably recover whether an edge means “source was abstracted into target” or “source artifact was abstracted from target”; authors can create semantically opposite edges under one asymmetric identifier.

**Decision needed:** define a normalized relation tuple such as `(derivative, relation, source)`, then specify which carriers render it as `*-from`, `* into:`, or metadata without changing its semantics.

## 4. Placement and invalidation policy vary by artifact contract, but the vocabulary couples them

Source-side footers are justified as edit-time interruption: changing a source should surface downstream review targets. Articles instead retain a dated publication, store `source_notes` downstream, and treat source divergence as a decision about annotation or follow-up rather than automatic staleness. Generated reports, mechanically derived copies, abstracted claims, and canonical notes updated from reports also have different invalidation behavior.

**Operational consequence:** “has lineage” currently implies a stronger and more uniform freshness response than several artifact classes actually support. Conversely, target-side lineage can be treated as deficient even where the target's lifecycle deliberately does not follow source freshness.

**Decision needed:** separate at least three decisions: semantic relation, storage carrier, and invalidation response. Each artifact contract should select all three rather than inheriting them as one package.

## 5. The generic write procedure has no lineage-override lookup

`cp-skill-write` correctly loads collection and type contracts for ordinary authoring and link labels, but its lineage paragraph appears under “Universal Mechanics” and does not ask either contract for a carrier or invalidation override. The article exception therefore exists in a surface the generic lineage procedure does not consult for that decision.

**Operational consequence:** adding another legitimate lineage profile—external Git review, immutable source, frozen publication, generated view—requires contradicting the universal paragraph or silently relying on agent judgment.

**Decision needed:** decide whether lineage policy belongs in `COLLECTION.md`, the type spec, a shared lineage profile referenced by either, or a precedence rule across those surfaces.

## Related open cases, not yet contradictions

These remain design gaps until a live contract chooses incompatible answers:

- inverse lineage for an external work produced from internal vocabulary (`externalized-as`, `published-as`, or prose-only);
- minimal lineage for retained one-off prompts and source packets before they acquire a type;
- merge-back event lineage when a canonical note is revised from reports or generated context;
- external Git-backed source identity and freshness without copying a repository into `kb/sources/`;
- promotion and retention of useful observations from ignored generated reports.

Resolution work should update this ledger as contradictions are eliminated and extract durable rules into the appropriate note, ADR, collection contract, type contract, or instruction.
