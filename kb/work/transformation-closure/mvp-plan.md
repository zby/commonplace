# MVP build plan: closing review on the full pass over a unified diff-and-ack surface

Concrete build list for the workshop's MVP, given the design in [unified-diff-and-ack.md](./unified-diff-and-ack.md). The MVP is a calibrated one-cycle closing review on `run-full-improvement-pass-on-note.md`, with carry judgments recorded as rationale-bearing acks and an observation log with a variance control arm. Everything below is the lightest reversible representation available; nothing here closes a design decision beyond what building forces.

## 1. Class-bearing acceptance kind (review DB)

Let report-only assays (compression bundle, critique-note, composition-friction-gate, connect) register acceptance rows without a pass/warn/fail/error decision, and record each assay's declared class — **detection** or **attention** — on the acceptance surface. The license a fresh record carries derives from the class (see the failure-mode split in [unified-diff-and-ack.md](./unified-diff-and-ack.md)), never from where the assay runs or whether a result line exists.

- Relax the `decision` CHECK constraint in `review-schema.sql` to admit a verdict-free kind (or accept NULL-decision pairs into acceptance).
- Adjust the `current_gate_acceptances` view's `rp.decision IS NOT NULL` filter so verdict-free rows count as acceptances for freshness while staying out of the warn queue (warn-selector filters on `decision = 'warn'`, so it needs no change).
- Registration surface: either a small `commonplace-record-assay`-shaped command (note path, assay id + class, report path → snapshots + acceptance row) or a finalization mode that accepts a verdict-free result line. Whichever is less code; the command is likely simpler than teaching the bundle-output parser a new result kind.
- Gate identity for these rows is the assay's instruction file path (`kb/instructions/critique-note.md`, etc.), so editing an assay instruction stales its records as `gate-changed` — the ADR 038/041 pattern, no new mechanism.

## 2. Rationale on ack

Add a rationale field (and a rough edit-kind tag) to `commonplace-ack-gate-review` and the `acceptance` table, recorded at ack time. The ack is the MVP's carry record; without the why-at-decision-time, audit flips have no attribution substrate. See the residual-requirement section of [unified-diff-and-ack.md](./unified-diff-and-ack.md).

## 3. Closing-review step in the full-pass instruction

Add a step 10 to `kb/instructions/run-full-improvement-pass-on-note.md`: after the step-9 flow pass, the orchestrator runs one closing cycle —

- For each assay anchored during the pass, read the selector's cumulative diff (accepted snapshot → final bytes).
- Either **ack** with rationale + edit-kind tag, or **re-run** the assay against the final text.
- Keep the license distinction sharp in the prompt: only detection-assay acceptances ever carry skip semantics; an ack on an attention-assay record reuses evidence and endorses nothing; the friction gate's "For the human" line is never satisfied by an ack.
- Stopping rule: at most this one cycle. Findings from closing re-runs route to the packet's Open items; they do not trigger another transformation round.

During the MVP, audit sampling is 100%: every ack is *also* re-run, so initially the ack decision costs nothing to check. The dial only decays later, against evidence.

## 4. Observation log with control arm

A plain log file in this workshop (no DB, no schema): one line per closing-cycle event — note, assay, ack-or-rerun, rationale/edit-kind, and for re-runs whether the outcome flipped against the prior record.

- **Control arm:** occasional re-runs on *unchanged* bytes to measure the base flip rate from model variance. Without it no flip is attributable to an edit.
- The log calibrates the trust dial and locates the workshop's candidate constraints; it is not training data for a system-side heuristic.

## Explicitly not built

- Footprint enforcement machinery — declared footprints stay stated intent the cumulative diff verifies.
- Any edit-kind taxonomy in the system — the tag on acks is free-text observation vocabulary.
- Trust-dial automation — sampling rate changes are manual judgments against the log.
- Human-attestation pairs (workshop case 2) — untouched until the MVP has run.

## What MVP use should observe (constraint location)

Ties to the location criteria in [carry-heuristics.md](./carry-heuristics.md):

- Constraint 1 (direction over size): do flips in the log track edit *direction* rather than diff size?
- Constraint 2 (non-compositionality): does an accumulated series of individually-acked edits ever flip a coherence check? (Baseline anchoring should surface this as a growing cumulative diff.)
- Constraint 3's premise: is a declared flow-only step 9 ever caught changing a claim in the cumulative diff?
- Constraint 4: does the one-cycle stopping rule ever leave residual findings that genuinely needed a second round, or does routing to Open items suffice?
- Case 3 flip: does a current-critique signal ever get read downstream as "critiqued and handled"? That observation, if it occurs, relocates the do-not-anchor rule as a real constraint.
