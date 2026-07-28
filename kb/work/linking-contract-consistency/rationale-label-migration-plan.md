---
description: "Use when reviewing and migrating the target-role rationale link identifier under the source-as-subject rule"
type: kb/types/instruction.md
---

# Migrate the rationale link label

## Outcome

Replace `rationale` with a source-as-subject identifier only after the live corpus confirms one coherent relation. Test `rests-on` as the leading candidate:

> source artifact `rests-on` target claim

Preserve the current reader journey: a maintainer follows the edge from a design, description, procedure, or working artifact to the theoretical claim it depends on. Do not migrate if material uses instead mean evidence, derivation, implementation, or note-to-note premise grounding.

## Decision gate

Inventory every active registered `rationale` edge by resolved source→destination pair and inspect representative uses from each pair. Compare the assertion against `grounds`, `derived-from`, `abstracted-from`, and `operationalized-from`. Before any bulk edit, record whether:

- `rests-on` honestly covers the corpus and remains distinguishable from `grounds`;
- more than one relation is present and needs a split;
- some edges should be reclassified or removed.

If the first condition does not hold, stop after the review and revise this packet with the adopted identifier or pair. Do not let the working candidate decide the evidence.

## Migration boundary

Once the gate passes, change the decision/catalogue surfaces, live collection authorizations, current authoring guidance, and active registered edges together. Preserve immutable snapshots, frozen experiments and calibration artifacts, generated/ignored reports, archived proposals, historical quotations, and ordinary prose uses of “rationale” unless they falsely state current identifier guidance. Reciprocal edge presence is not part of this migration.

## Inherited amendments from the evidence run

- **Accept—add:** define positive mutable surfaces and mutually exclusive exclusion buckets; inventory resolved source→destination pairs; compare them with collection authorization; separately scan active recommendation and procedure prose for the literal identifier.
- **Accept—remove:** do not use the historical authorization matrix, earlier counts, or a repository-wide lexical replacement set as the migration baseline.
- **Accept—reorder:** classify live edges first; record authorization deltas and exclusions; adopt the identifier and contracts; reconcile guidance; migrate edges; then run tuple conservation, exclusion, authorization, link, and validation checks. Re-diff selected paths after any approval wait.
- **Accept—automate:** generate a temporary TSV containing source path, target, resolved destination, proposed disposition, and exclusion reason. Make reconciliation fail on missing or unexpected tuples, active old labels, or excluded labels outside exactly one bucket. Do not retain a reusable command yet.

Record surprises at discovery time in [the rationale retrospective](./rationale-label-migration-retrospective.md). This second run must decide whether the repeated procedure is stable enough to extract into a reusable instruction.

## Done when

- The decision gate records the adopted source-as-subject assertion and its boundary from neighboring labels.
- Every active `rationale` edge has a conserved successor, explicit reclassification/removal, or one exclusion reason.
- Current authoritative guidance and collection authorizations agree with the adopted identifier.
- Reciprocal links are unchanged unless independently reviewed.
- Changed artifacts validate, relevant tests pass, and the retrospective reconciles counts and surprises.
- The retrospective explicitly accepts or rejects promotion of the two-run migration procedure.
