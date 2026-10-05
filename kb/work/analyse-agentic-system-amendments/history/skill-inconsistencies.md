# Inconsistencies in the live analyse-agentic-system skill

**Status:** audit, 2026-10-02, read-only. Job texts, member types, schemas,
contracts and the operator docs were compared with the code that schedules,
judges and validates them. Line numbers are at commit `23a3d8e12`. Each
item names what the text says, what the code does, and which side looks
wrong. The record-ID items already in this workshop are not repeated.

The operator layer is consistent: `step` outcomes, the three `report`
events, the `start` parameters, the handoff command and the run-status
vocabulary all match `drive-a-code-scheduled-run.md` and `SKILL.md`.

## A. Can dead-end or silently pass a run

1. **`run-id` and `reviewed-boundary` are judged only after reconciliation,
   where only the memory member can change.** No job parameter or input
   states the run ID (`BOUNDARY_FIELDS` has none; `agentic_workflow.py:113`),
   so analysts infer it from the `run-state` path. `pass_refusals`
   (`agentic_workflow.py:388-418`) does not compare the fields;
   `record_check` (`:933-944`) does, after reconciliation, and every
   set-check failure is a blocker (`verify.md:61-62`). A mismatch in the
   runtime or epistemic member is then unrepairable by any permitted action
   and the run stops. Fix: pass the run ID as a job parameter and check both
   fields in `pass_refusals`.

2. **Reconciliation's reference scan is skipped on a returning round.**
   `reconcile.md:52-54` promises refusal with the unresolved IDs;
   `reconcile_refusals` returns before `reference_refusals` whenever
   `## Returned to the memory analyst` is present (`agentic_workflow.py:444`).
   Unresolved IDs in a returning reconciliation are accepted and surface only
   later. Fix the code, or state the exception in the text.

3. **The overview's amendment index lands in whichever section the boundary
   job wrote last.** `boundary.md:103` says the two sections go into the
   overview unchanged; `agentic_workflow.py:1199-1204` appends the index to
   the end of the boundary body, and `boundary_refusals` (`:304-313`) does
   not fix section order. The overview type (`:70-71`) says the line sits
   under `## Source register`. Fix: insert the line explicitly after the
   Source register section.

## B. Refusals that mislead or arrive at the wrong stage

4. **Heading order in reconciliation is enforced but unstated.** `wanted =
   ["Reconciliation", RETURNED]` (`agentic_workflow.py:435-438`); a return
   section written first is refused as "write only Reconciliation and any
   permitted memory return", which names the wrong cause. Fix the message
   and say the order in `reconcile.md:60-61`.

5. **Reconciliation is not checked for ranged prose anchors until the set
   check.** `source_anchor_refusals` runs for verification and synthesis
   (`agentic_workflow.py:504, 513`) but not in `reconcile_refusals`; the
   type rule catches it in `record_check`, costing a reconcile round. Fix:
   add it to `reconcile_refusals`.

6. **The job's own instruction is not in its reading batches.** The prompt
   says `Follow <method_paths[0]> with:` but batches only `method_paths[1:]`
   (`agentic_workflow.py:753-765`), while `worker-rules.md:71-72` says to
   follow the batches in order. Fix: batch it first, or say it is read first.

7. **Range syntax passes when its endpoints resolve.** `RT-RTE-1 through
   RT-RTE-4` is accepted with only the endpoints declared; recorded as A1 in
   [fix options](./fix-options.md) and step 1 of the README.

## C. Schema and type text disagree

8. **Memory type requires six kind headings; its schema does not.**
   `agent-memory-analysis-report.md:210-212` vs
   `agent-memory-analysis-report.schema.yaml:155-215`; the runtime schema
   enforces them (`agentic-system-runtime-report.schema.yaml:36-47`).

9. **Frontmatter openness differs silently.** Memory and reconciliation
   schemas set `additionalProperties: false` (`:153`, `:20`), rejecting
   `tags`/`traits`; runtime, epistemic and overview allow them. No type text
   mentions it. Decide one way and say it.

10. **Git revision length.** Run-state type and `frozen_source_refusals`
    (`agentic_workflow.py:329-331`) require 40 hex; the run-state schema
    (`:165`) also accepts 64. Align the schema unless SHA-256 repositories
    are intended.

## D. Contract promises with no check

Decide per item: add the check, or soften the contract to "the analyst
ensures".

11. "Never annotates a record the member declares"
    (`agentic-analysis-records.md:40`): no code intersects `annotated_ids`
    with `declared_ids`.
12. "Only the reconciliation member amends records" (`:44`): an
    `Amendment:` paragraph in an analyst member is neither rejected nor
    indexed; `amendment_index` runs only on `reconciliation.md`
    (`validation.py:1981`). The required amendment content (superseded
    value, replacement, anchor, affected findings) is not checked beyond the
    leading ID.
13. Evidenced absences require an `absent` status (`:93`):
    `conclusion_status_errors` requires a labelled status only for `RTE-`
    declarations (`agentic_records.py:164-183`).
14. Annotation location "comes from the annotating member's type" (`:41`):
    `annotated_ids` scans the whole body, so the memory type's confinement
    to `## Annotations` (`agent-memory-analysis-report.md:223-224, 334`) is
    not enforced, and the epistemic type, which defines no annotation
    location, still has its `#### On` headings accepted.
15. Code-span path anchors "must exist at that commit"
    (`agentic-analysis-sources.md:43-45`): `_verify_source_anchors`
    (`agentic_analysis.py:392-441`) resolves GitHub URLs only.
16. Prose paths carry no ranges (`:46-47`): `LOCAL_ANCHOR_RE`
    (`quote_matching.py:24-26`) requires a dot extension, so
    `` `Makefile:12-14` `` in prose is not flagged.

## Suggested order before the next test run

A1, A2, A3 and B4 to B6 first: they change what a run does. C8 to C10 are
one-line schema edits. D11 to D16 can wait for the run's evidence; D12 and
D13 are the ones most likely to matter for the `Part of:` proposal, since
splits and absences are where amendments and statuses get exercised.
