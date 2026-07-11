# MVP build plan: closing review on the full pass over a unified diff-and-ack surface

Phased build plan for the workshop's MVP, given the design in [unified-diff-and-ack.md](./unified-diff-and-ack.md). The MVP is a calibrated one-cycle closing review on `run-full-improvement-pass-on-note.md`, with carry judgments recorded as rationale-bearing acks and an observation log with a variance control arm. Each phase is self-contained: it delivers testable value on its own and later phases build on it without reaching back. Everything below is the lightest reversible representation available; nothing here closes a design decision beyond what building forces.

Ordering note: an evidence-first alternative (closing review on the already-anchored semantic pairs before any machinery, zero code) was considered and set aside — a semantic-only closing cycle would put partial-coverage observations in the log that read as full-pass closure. Machinery first, then one log whose coverage is honest.

## Phase 1: critique into the review system

Critique-note becomes the first unbounded assay executed through the batch pipeline: `commonplace-review-target-selector critique --note {path}` → create-jobs → sub-agent → finalize, producing acceptance rows and staleness classification exactly like semantic gates. Phase deliverable: that flow works end-to-end and the selector reports critique freshness (`missing-review` / `note-changed` / `gate-changed`) for real notes.

- Registration surface: **through the batch mechanism**, not after-the-fact recording. The pipeline pins snapshots itself as part of executing the assay, so the anchor is enforced by construction; a standalone `commonplace-record-assay` command would accept the orchestrator's claim that report matches bytes — a self-reported anchor with a time-of-check gap. Naming stays layered: "gate" remains the operational term; the batch mechanism gains an assay class, not a rename.
- **Class-homogeneous jobs via a separate bundle — already given by shipped packing.** Critique is its own one-assay bundle; `--grouping note` already keys jobs by `(note, bundle)` (`_note_groups`, `src/commonplace/cli/review/create_review_jobs.py`) and `--grouping gate` packs per-gate, so no job ever mixes result-kind classes and no new guard is needed. Each job carries exactly one output contract.
- **The difficult part is the parser.** Finalization currently requires `## Result: PASS|WARN|FAIL|ERROR` per pair; the expected result kind must instead be resolved from the job's bundle. Three design choices live here:
  - *Class declaration.* Something must declare "critique is unbounded" for the parser to depend on. Cleanest precedent is the virtual-lens pattern (ADR 038/041): `critique` as a virtual lens whose gate identity is `kb/instructions/critique-note.md`, one derived pair per note — avoids duplicating the instruction into a catalog file. Alternative: a `class:` frontmatter field on a gate-shaped catalog file.
  - *Verdict-free result marker.* All-or-nothing finalization still needs a parseable per-pair completion line (e.g. `## Result: REPORT`) — a truncated critique must be distinguishable from a complete one.
  - *Report routing.* The full pass reads `kb/reports/critique/<note>.critique.md`; batch writes pair result files in the job artifact dir. Either the pair result file becomes the report (step 7 reads from job artifacts) or finalize copies it out.
- Schema: relax the `decision` CHECK constraint in `review-schema.sql` to admit the verdict-free kind, record the assay's declared class — **bounded** or **unbounded** — on the acceptance surface, and adjust the `current_gate_acceptances` view's `rp.decision IS NOT NULL` filter so verdict-free rows count for freshness while staying out of the warn queue (warn-selector filters on `decision = 'warn'`, so it needs no change). The license a fresh record carries derives from the class, never from where the assay runs or whether a result line exists.
- Assay identity is the instruction file path, so editing `critique-note.md` stales its records as `gate-changed` — the ADR 038/041 pattern, no new mechanism.
- Consequence for the instruction: step 3 of the full pass becomes a selector/create-jobs/finalize flow structurally identical to step 5.
- Scope: **critique-note only.** Friction follows the same pattern later if it proves cheap (its output contract is already verdict-free by design); the compression bundle (own multi-gate runner) and connect (skill machinery) stay un-anchored — log what that leaves uncovered rather than silently treating the pass as fully anchored.

## Phase 2: rationale on ack

Add a rationale field (and a rough edit-kind tag) to `commonplace-ack-gate-review` and the `acceptance` table, recorded at ack time. The ack is the MVP's carry record; without the why-at-decision-time, audit flips have no attribution substrate. See the residual-requirement section of [unified-diff-and-ack.md](./unified-diff-and-ack.md). Phase deliverable: acks carry rationale for both bounded and unbounded acceptances; independent of phase 1 except that unbounded acks exercise the new acceptance kind.

## Phase 3: closing-review step and observation log

Add a step 10 to `kb/instructions/run-full-improvement-pass-on-note.md`: after the step-9 flow pass, the orchestrator runs one closing cycle —

- For each assay anchored during the pass, read the selector's cumulative diff (accepted snapshot → final bytes).
- Either **ack** with rationale + edit-kind tag, or **re-run** the assay against the final text.
- Keep the license distinction sharp in the prompt: only bounded-assay acceptances ever carry skip semantics; an ack on an unbounded-assay record reuses evidence and endorses nothing; the friction gate's "For the human" line is never satisfied by an ack.
- Stopping rule: at most this one cycle. Findings from closing re-runs route to the packet's Open items; they do not trigger another transformation round.

The observation log lands in the same phase — a plain file in this workshop (no DB, no schema): one line per closing-cycle event — note, assay, ack-or-rerun, rationale/edit-kind, and for re-runs whether the outcome flipped against the prior record.

- **Control arm:** occasional re-runs on *unchanged* bytes to measure the base flip rate from model variance. Without it no flip is attributable to an edit.
- **Audit unit differs by class:** for bounded assays a flip is a verdict change; for unbounded assays every re-run differs textually, so log instead whether the fresh sample materially diverges from the carried report (would it have changed steps 8–9?). Don't pre-formalize "materially" — record the judgment and let the log show whether it stabilizes.
- The log calibrates the trust dial and locates the workshop's candidate constraints; it is not training data for a system-side heuristic.

Phase deliverable: the instruction closes over its own edits, and every closing cycle leaves a log line.

## Phase 4: run and observe

Use the MVP on real full passes. Audit sampling starts at 100% — every ack is *also* re-run, so initially the ack decision costs nothing to check; the dial only decays later, against evidence. This phase is where constraints get located (see below); it produces observations, not code.

## Explicitly not built

- Footprint enforcement machinery — declared footprints stay stated intent the cumulative diff verifies.
- Any edit-kind taxonomy in the system — the tag on acks is free-text observation vocabulary.
- Trust-dial automation — sampling rate changes are manual judgments against the log.
- Human-attestation pairs (workshop case 2) — untouched until the MVP has run.

## What phase 4 should observe (constraint location)

Ties to the location criteria in [carry-heuristics.md](./carry-heuristics.md):

- Constraint 1 (direction over size): do flips in the log track edit *direction* rather than diff size?
- Constraint 2 (non-compositionality): does an accumulated series of individually-acked edits ever flip a coherence check? (Baseline anchoring should surface this as a growing cumulative diff.)
- Constraint 3's premise: is a declared flow-only step 9 ever caught changing a claim in the cumulative diff?
- Constraint 4: does the one-cycle stopping rule ever leave residual findings that genuinely needed a second round, or does routing to Open items suffice?
- Case 3 flip: does a current-critique signal ever get read downstream as "critiqued and handled"? That observation, if it occurs, relocates the do-not-anchor rule as a real constraint.
