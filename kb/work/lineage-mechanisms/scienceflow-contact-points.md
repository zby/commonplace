# ScienceFlow contact points: rollback, retained evidence, and consumer-relative lineage

Working note. ScienceFlow is a long-horizon research-agent harness that archives executable workspaces, structured memory, validation evidence, and resource records. ESTRA can resume from the current state or restore an archived state. Its relevance to this workshop is not the reported benchmark gain. It is the persistence split: the active research route can move backward while the evidence archive and cumulative resource account continue forward.

Evidence is the [code-grounded ingest](../../sources/scienceflow-long-horizon-agent-for-ml-research-and-discovery.ingest.md) over arXiv v1 and the official repository at commit [`f16be15660284898354e2a5d0fe195f97e4685c4`](https://github.com/huawei-noah/noah-research/commit/f16be15660284898354e2a5d0fe195f97e4685c4). The code inspection was static. The paper's benchmark and ablation outcomes were not reproduced.

## Why this is a second case, not another Eigenius example

[Eigenius](./eigenius-contact-points.md) approaches lineage from the far end of constraining: immutable typed layers, explicit epistemic categories, replayable derivations, commit gates, and proof checking. ScienceFlow operates in a mixed form. It combines natural-language agent context, executable workspace files, task-specific evaluators, summaries, resource events, and content-addressed snapshots. The systems therefore pressure different parts of the lineage model.

| Eigenius case | ScienceFlow case | Workshop pressure |
|---|---|---|
| Immutable typed graph layers | A mutable workspace restored from archived anchors | Separate reversible active state from the non-rewindable record |
| Trace and justification terms are distinct | Raw Stage cards coexist with folded agent-facing memory | Separate retained evidence from a derivative consumption view |
| Content-addressed typed derivations aim at replay | A content-addressed workspace supports recovery and state-matched branching | State what a lineage packet is sufficient to reproduce |
| Commit gates decide whether a graph mutation enters | Stage gates decide whether a research state becomes an anchor | Do not turn operational acceptance into epistemic endorsement |

Eigenius asks how much can be made checkable by codifying the derivation. ScienceFlow asks what must survive when the current route, context, and workspace are intentionally replaced. The cases are complementary rather than cumulative.

## Restoration is non-monotone; lineage is monotone

An archived ScienceFlow state contains a workspace snapshot, structured memory, validation evidence, and resource records. Restoring an archive resets those state components to an earlier anchor, but the paper says resource accounting remains cumulative and the full archive remains available. A discarded post-anchor branch is retained as negative evidence rather than erased.

This supplies a direct whole-system witness for a rule the workshop currently implies but does not name:

> A system may move its active state backward without moving its lineage backward. Restoration selects an earlier basis for future work; it does not make later attempts or spent resources cease to have happened.

The distinction matters anywhere rollback is an operational feature. If an agent can restore both the workspace and the only record of expenditure or failure, rollback becomes evidence deletion. A restoration anchor and a history cursor must therefore be separate concepts even when both are represented by timestamps or commit-like identifiers.

This is the dynamic counterpart to [history has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md). The existing note explains why a history fact must be recorded when it occurs. ScienceFlow adds the next condition: once recorded, the fact must live outside any state boundary that later operations are allowed to rewind.

## Folded context is a derivative, not a replacement

ScienceFlow's Stage-memory implementation calls the append-only ledger the source of truth. Fold creates an addressable summary for bounded model context while retaining raw current and verification cards. Unfold resolves selected evidence from the retained ledger. After an archived-state restoration, the folded abandoned branch remains available even though it is no longer part of the active route.

This is an operational example of the workshop's source-preservation rule. The compact derivative is more useful to the immediate consumer, but it cannot replace its source because later consumers need different operations:

- the agent needs a bounded view for the next decision;
- the evaluator needs concrete result cards;
- restoration needs the workspace manifest and archived state;
- audit or replay needs the uncompressed record;
- a later Unfold needs the addressable source behind the summary.

The general consequence is stronger than “keep raw logs.” Retention follows future operations. A derivative may be sufficient for reading while its source remains necessary for verification, regeneration, restoration, or alternate-context assembly. This aligns with [preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) and gives the lineage workshop a runtime case rather than only an artifact-publication case.

## Lineage sufficiency is consumer-relative

ScienceFlow's workspace store hashes file contents, writes immutable objects and a manifest, and validates referenced objects before mutating a restore target. That is strong evidence for recovering the captured workspace bytes. It is weaker evidence for reproducing a scientific outcome.

The paper's state description may include environment metadata and references to large artifacts rather than all transitive inputs. Model responses, provider behavior, external data, hardware behavior, and uncaptured dependencies may also affect the trajectory. A restored workspace can therefore be recovery-complete for the next agent action without being reproduction-complete for the original experiment.

This refines the workshop's re-derivability bridge. “Inputs preserved” needs a consumer and an operation:

- preserved enough to render a prior view;
- preserved enough to restore active work;
- preserved enough to replay one controlled branch;
- preserved enough to reproduce a result independently.

These are not interchangeable guarantees. Candidate vocabulary for extraction is **recovery closure** versus **derivation closure**, but the distinction is more important than those names. A lineage record should state the operation it closes, not merely claim that state was captured.

## A Stage verdict selects an anchor; it does not certify truth

A ScienceFlow Gate evaluates a task-specific result signal before admitting a Stage. Accepted evidence then affects trajectory selection and resource allocation. This is operationally valuable, but it does not turn the retained scientific hypothesis into a generally verified claim. The evaluator may be benchmark-specific, incomplete, or wrong.

The case corroborates the workshop's result-kind stance from a different system. An accepted Stage records that an evaluator ran and licensed a transition under its contract. Readers must still cite the proposition-bearing artifact and its evidence, not treat transition status as the proposition's warrant. This parallels Eigenius's separation between a gate result, a trace, and the claim being evaluated.

## Storage weight: a ledger is not automatically a database case

ScienceFlow has an append-only Stage ledger, archived states, content-addressed objects, manifests, and resource events. That does not supply the missing second churning lineage mesh from [storage weight across derivation cases](./storage-weight-across-cases.md). Within one run, these records have natural owners and are primarily append-once or immutable. The system needs indexed access, but the case does not show Commonplace-style mutable current state on an ownerless many-to-many relation.

The useful transfer is therefore at weights 1 and 2:

- keep owner-local manifests and source pointers with the retained state;
- keep non-regenerable attempt and merge-back history on an append-only or committed event surface when a real consumer needs it;
- derive bounded views and current anchors from that retained substrate;
- do not escalate to a generic operational store without the workshop's churn-and-selector predicate.

ScienceFlow strengthens the case for separating current state from event history. It does not weaken the workshop's YAGNI conclusion about a generic lineage database.

## What to take into extraction

1. **Name the rollback rule.** Active state may rewind; lineage events, evidence, and spent-budget records do not silently rewind with it.
2. **Make source preservation operation-relative.** Retain the source when a derivative cannot support verification, regeneration, restoration, or a different bounded view.
3. **State the closure promised by a lineage packet.** Recovery closure is not automatically derivation or reproduction closure.
4. **Keep acceptance roles narrow.** A transition verdict licenses state selection under one evaluator; it is not a portable endorsement of the underlying claim.
5. **Keep the storage predicate unchanged.** Append-only run history with a natural owner is not the second many-to-many freshness mesh.

## What not to infer

- The paper's benchmark results do not validate the workshop's lineage theory, and they remain unreproduced in the ingest.
- Content-addressed workspace files do not establish that every dependency required for scientific reproduction was captured.
- An append-only Stage ledger does not by itself provide factual correctness, faithful summaries, or independent auditability.
- ScienceFlow's fixed task adapters, evaluator contracts, Stage trigger, action vocabulary, and worker topology bound what its retained evidence can reveal.
- This case does not replace Eigenius. Eigenius remains the stronger witness for typed warrant and production-time enforcement; ScienceFlow is the stronger witness for rollback boundaries and source-preserving context compression.

---

Relevant notes and working files:

- [verification locus and provenance theory](./verification-locus-and-provenance-theory.md) — extends: adds rollback persistence and consumer-relative closure to the state/history account
- [automatic derivation rules](./automatic-derivation-rules.md) — is-evidence-for: a useful derivative does not eliminate the source needed by later operations
- [lineage profile matrix](./lineage-profile-matrix.md) — is-evidence-for: different consumers require different retained lineage surfaces
- [active work state is not retrospective memory or chat history](../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) — rests-on: restoration operates over active work state, not chat reconstruction
- [learning inside a fixed decomposition inherits its mistakes](../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — limits: lineage fidelity cannot correct a fixed evaluator or response space
