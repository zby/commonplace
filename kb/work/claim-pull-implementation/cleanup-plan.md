# Claim-pull semantic cleanup plan

## Purpose

Repair source-grounding debt that predates the prospective rule. The
[structural migration](./ingest-template-migration.md) first gives every ingest
an honest `## Claims` section. Cleanup populates it only after reading the source,
then links affected notes to the ingest.

The cleanup unit is a claim in one library artifact, not an ingest. The 284
tracked ingests are not the queue.

## Debt classes

Keep these outcomes distinct:

1. a load-bearing external premise has no captured or cited source;
2. a source is cited, but its ingest does not ground the exact claim and scope;
3. the local claim is broader or more confident than the source;
4. the source contradicts the local claim;
5. the source establishes a premise but the local transfer or design delta
   remains distinct; and
6. candidate generation was wrong and there is no relevant external dependency.

## Execution plan

1. **Freeze a cohort.** Record target paths and revisions. Include more than
   missing citations; the cohort must exercise narrowing or contradiction.
2. **Inventory local claims first.** Preserve each target commitment in its own
   language before source reading.
3. **Generate candidates.** Keep deterministic provenance signals separate from
   model-suggested literature matches. A model suggestion is a reading assignment,
   not evidence.
4. **Ground the source claim.** Dispatch the grounding-worker instruction with
   the cleanup runner's bounded claim packet. The worker reads the complete
   existing `Claims` section, adds or revises only what the source warrants, and
   avoids obvious semantic duplicates. Cleanup owns candidate selection; the
   worker does not expand the cohort or search for literature. V1 routes only
   primary-source claims; give secondary-source candidates a named blocker
   rather than checking them against the primary snapshot. If the worker returns
   `BLOCKED: legacy recovery required`, the cleanup runner alone may invoke
   `cp-skill-ingest` with the ingest's exact canonical URL. Require the same
   ingest path and checksum, byte-preserved `Claims`, and exactly one recovered
   local checksum match, then dispatch a new fresh grounding worker. Never
   resume the blocked worker or expose this fallback through ordinary writes.
5. **Compare source and target.** Judge source claim, scope, authority, target
   transfer, and surviving local conclusion separately.
6. **Disposition the target.** Choose false positive, source unavailable,
   grounded as written, narrowed, contradicted and repaired, established premise
   plus retained local delta, or handoff to `literature-disposition`.
7. **Link and validate.** The target links to the ingest as a whole and states
   which source claim it uses. A verifier reads the entire `Claims` section.
8. **Re-run and account.** Record candidate precision, unavailable sources,
   effort, and repairs by kind without claiming unknown corpus recall.

## Boundaries

- Do not assign claim IDs or build a per-claim graph during cleanup.
- Do not populate `Claims` by splitting existing ingest summaries or connection
  prose.
- Do not treat a source-free claim as automatically defective.
- Do not count a link as grounding when the note fails to articulate what it
  imports or why it transfers.
- Do not begin bulk semantic cleanup before the fidelity decision states what
  can be checked under ignored snapshots.
- Do not promote the legacy-recovery fallback into `cp-skill-write`, the
  grounding-worker instruction, or a user-invocable skill. It is temporary
  cleanup orchestration.

## Completion of the first run

- The target cohort and revisions are frozen.
- Every selected claim has a terminal disposition or named blocker.
- Every grounded target links an ingest whose complete `Claims` section supports
  the articulated dependency.
- All authorized repairs and handoffs are tracked.
- Validation and before/after selector results are recorded.
- Any pressure for IDs or finer addressing is reported as an observation rather
  than implemented during the run.
- When the cleanup scope closes, every recovery attempt has a terminal result,
  no active instruction calls the fallback, its permanent safety rules have
  been extracted, and the frozen runbook is retired to an authorized
  non-operative archive.
