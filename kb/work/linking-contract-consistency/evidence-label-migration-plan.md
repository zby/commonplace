---
description: "Use when replacing the ambiguous evidence link label with directional identifiers across contracts, authored edges, and current guidance"
type: kb/types/instruction.md
---

# Migrate the evidence link label

## Outcome

Replace the ambiguous `evidence` identifier with a source-as-subject inverse pair:

- `source evidenced-by target` — the source assertion points to an observation or source that bears on it;
- `source is-evidence-for target` — the source observation or review bears on the target assertion, without claiming the target already cites or incorporates it.

Both directions remain independently authored reader aids. Do not add or remove a reciprocal edge merely because its counterpart exists.

Adopt the general naming invariant—every directional identifier completes `source <label> target`—while leaving migration of other failing labels to later runs.

## Scope

Change together:

- the decision record adopting the naming invariant and evidence pair;
- the shared catalogue and every live collection authorization;
- current instructions, types, examples, and navigation that state evidence-label semantics;
- active authored edges whose registered identifier is `evidence`;
- current workshop conclusions that would otherwise recommend the retired identifier.

Do not mechanically rewrite prose uses of the ordinary word “evidence.” Preserve immutable snapshots, frozen audit reports, generated/ignored reports, archived proposals, and historical quotations unless they incorrectly present themselves as current guidance. Do not absorb neighboring-label cleanup (`supports`, `grounds`, lineage labels) into this migration.

## Execute

1. **Baseline the live uses.** Recompute the inventory rather than trusting workshop counts. Classify each registered `evidence` edge by its source-as-subject assertion and record counts, exclusions, and ambiguous cases in [the migration retrospective](./evidence-label-migration-retrospective.md). Preserve enough source/target information to reconcile the post-migration inventory.

2. **Adopt the semantics.** Record the source-as-subject invariant, the two assertion templates above, their reader needs, and their non-obligation to reciprocate. Update the shared catalogue and collection contracts in the same change. Treat the 26-edge inverse cohort reviewed in [evidence direction review](./evidence-direction-review.md) as the established `is-evidence-for` case, while rechecking against live bytes.

3. **Migrate authored edges by meaning.** Use `evidenced-by` when the linked target supplies evidence for the source assertion. Use `is-evidence-for` when the source artifact supplies evidence bearing on the linked target assertion. Reclassify or remove an edge only when neither assertion is honest; log that case rather than forcing it into the pair. Preserve link targets, context phrases, and edge presence unless the semantic review itself requires a change.

4. **Reconcile current guidance.** Search active KB and system-definition surfaces for literal label lists, examples, direction glosses, and claims about the old identifier. Do not turn the migration into a general rewrite of collection grammar or other labels.

5. **Verify and close.** Re-run the inventory and reconcile every baseline edge as `evidenced-by`, `is-evidence-for`, deliberately reclassified/removed, or intentionally excluded. Validate every changed KB artifact, run any tests whose fixtures or code actually changed, check link resolution and diff hygiene, and commit only the migration's explicit files.

## Surprise capture and plan improvement

Write surprises into [evidence-label-migration-retrospective.md](./evidence-label-migration-retrospective.md) when they are discovered, before the local resolution makes them look obvious. Record only information that could change another label migration: a failed assumption, unexpected surface, semantic ambiguity, unsafe automation boundary, validation blind spot, or sequencing problem.

Before declaring the migration complete:

1. reconcile planned and actual counts;
2. state which surprises were evidence-specific and which generalize;
3. write concrete **add / remove / reorder / automate** amendments for the next label plan;
4. link any deferred problem to its owning workshop instead of expanding this migration;
5. update this workshop's working-file index so the next implementer is routed to the retrospective.

The next directional-label migration must read the retrospective and explicitly carry forward or reject each proposed amendment. After a second run confirms a recurring workflow, extract the stable core into a reusable instruction; do not promote a one-run procedure as established method.

## Done when

- Current authoritative surfaces define only `evidenced-by` and `is-evidence-for` for these two journeys.
- Every active old `evidence` edge has a recorded disposition and post-migration counterpart or explicit removal reason.
- The new identifiers are authorized for every source→destination pair in which they occur.
- Reciprocal links are unchanged except where independently reviewed.
- Validation and relevant tests pass.
- The retrospective contains the reconciled counts, surprises, and next-plan amendments.
