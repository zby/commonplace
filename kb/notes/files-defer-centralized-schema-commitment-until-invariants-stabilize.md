---
description: "Canonical files can defer a centralized schema while meanings remain unsettled; a database becomes canonical only when an explicit authority decision and operative write path commit resolutions the files no longer determine."
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources, synthesis]
tags: [architecture]
---

# Canonical files may defer a shared schema while database authority remains a separate commitment

Canonical authored files can defer a centralized schema while the meaning and write rules for a state class remain unsettled. A state class here means a bounded set of state governed by the same accepted meaning and authority path. A database becomes canonical for that class only after the system makes an explicit authority decision and uses an operative write path to install accepted commitments that the files do not determine. Until then, deferral is safe only while the files retain accepted irrecoverable commitments and serving or index views remain accountable to them.

A centralized schema commitment makes one shared symbolic model and its write rules binding across the state class. It is not the first appearance of structure: filenames, directories, structured sections, frontmatter, schemas, validators, and conventions already [constrain file-backed state](./definitions/constraining.md). Because storage substrate, representational form, lineage, and behavioural authority are [separate axes](./axes-of-artifact-analysis.md), delaying a centralized schema is a timing choice, not a contrast between files and schema.

## When deferral remains safe

While materially different meanings or write rules remain live, central codification can freeze one unsettled interpretation. This note transfers the timing pattern from [progressive constraining](./progressive-constraining-commits-only-after-patterns-stabilize.md): just as repeated LLM runs can reveal stable interpretations before code commits them, repeated use of file-backed state can reveal stable meanings and write rules before a central schema commits them. File-backed state can acquire local schemas, validators, and other constraints as those patterns stabilize without committing all authored state to one shared model. Deferral remains viable only while the current workload's correctness needs can be met without a central canonical schema. Local validation, object- or edge-keyed files, traversal, and regeneration are possible mechanisms, not universal substitutes for indexed or transactional storage.

Schema deferral does not permit accepted commitments to go unrecorded. An accepted resolution that its inputs do not determine must be retained when it is accepted; deleting its only copy loses information that the inputs cannot recover. This follows from the distinction between [derivation and commitment](./commitment-not-derivation-creates-new-ground-truth.md). Persistence alone does not make a candidate write canonical. A candidate becomes governing only after it is selected, validated, authorized, and installed on a path that can durably affect later reads or behaviour, as [governing behaviour-changing writes require](./continual-learning-requires-governing-behaviour-changing-writes.md).

The retention duty applies only to information already known to encode an accepted, irrecoverable decision. A system may retain additional raw fields, but safe deferral cannot require identifying information whose relevance is not yet knowable.

A serving or index view remains derived only to the extent that its declared inputs and rule determine its output. Its [lineage](./definitions/lineage.md) must also state the applicable refresh, checking, review, or invalidation obligation. A mechanically recomputable copy that is retained and trusted must be checked against its current source; otherwise it should exist only as live or build-time output and be absent when not generated. [Judgment-derived prose instead needs managed staleness](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md), and a retained commitment cannot be checked back into a source that never contained it. An unchecked convenience view can otherwise drift into an accidental second authority. Accountability, rather than co-location or cheap replay, is what lets authored files remain canonical while another substrate provides derived capabilities.

## Pressure does not transfer authority

Three observations often motivate codification or a different substrate, but none alone decides lineage:

| Observation | What follows | What does not follow |
|---|---|---|
| An invariant stabilizes | The interpretation is mature enough to consider codifying with appropriate force. | Canonical state must move to a database. |
| Mutable many-to-many edge state has no endpoint owner | Use an edge-keyed representation and treat lookup, invalidation, and transaction needs as workload pressure. | Files cannot represent the relation, file count decides authority, or a database is thereby canonical. A composite-keyed file per edge remains possible, as the [many-to-many analysis](./many-to-many-edge-state-is-where-files-yield-to-a-database.md) itself notes. |
| Availability, recovery time, or current queries depend on a database | Treat the store as an operational dependency and design recovery accordingly. | The database is ground truth, or rebuildability alone settles lineage. |

The last distinction has an existence witness, not a universal recipe. In one self-reported production system, S3 is the source of truth: writes and single-item reads go to S3, while PostgreSQL serves list queries through a Lambda-maintained sync ([source analysis](../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md)). Serving dependence can therefore coexist with canonical state elsewhere.

## Canonicality moves with governing commitments

The positive boundary is a deliberate authority transfer plus an exercised write path. The system accepts a database-backed representation and transition rules as the meaning of one state class, then uses the authorized path to install commitments that the files do not determine. File renderings must then have an explicit derived, archival, or provenance role. The added-resolution test identifies what needs new ground truth; the governing write path identifies where that ground truth is installed.

Commonplace's review subsystem is one scoped witness. Its architecture keeps authored knowledge canonical in Markdown and regenerates indexes from it, while an accepted decision made SQLite canonical for review operational state. That decision made acknowledgement a database transition and Markdown reviews derived inspection views ([ADR](../reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md); [storage architecture](../reference/storage-architecture.md)). The case demonstrates a deliberate transfer for one state class, not a general threshold at which files must yield.

Authority should therefore be classified separately for each state class, while operational guarantees are evaluated in their local context. Transactions, bidirectional invalidation, lookup cost, latency, availability, migration cost, and existing tooling can favor one substrate in a given system; distributed file constraints can themselves require migration. Files are not schema-free, databases are not inherently rigid, and neither substrate is universally simpler or cheaper. The available evidence supplies no universal cost metric and no workload threshold at which edge files become impractical. A mixed system can keep authored knowledge canonical in files, maintain database indexes with explicit derived lineage, and make a database canonical for different operational state.
