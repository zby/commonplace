# MVP build plan: closing review on the full pass over a unified diff-and-ack surface

Phased build plan for the workshop's MVP, given the design in [unified-diff-and-ack.md](./unified-diff-and-ack.md). The MVP is a calibrated one-cycle closing review with full method coverage, carry judgments recorded as append-only events with required rationale, and an observation log with a variance control arm. Each phase is self-contained: it delivers testable value on its own and later phases build on it without reaching back. Everything below is the lightest reversible representation available; nothing here closes a design decision beyond what building forces.

Two structural distinctions, located at design time against shipped code (a codex review of an earlier draft of this plan), shape the whole build:

- **Current state vs. history.** Acceptance is deliberately current-state storage with inline pruning ([ADR 036](../../reference/adr/036-review-acceptance-is-current-state-not-append-only-history.md)): a superseding rerun deletes the prior pair, its job, and its artifacts in the same transaction. A carry judgment is *history* — so it cannot live (only) on acceptance, or the audit rerun destroys the attribution substrate exactly when the audit result arrives.
- **Verdict vs. completion.** A decision (pass/warn/fail/error) and a protocol completion marker are different facts. Unbounded assays complete without deciding, so the pair needs a persisted `result_kind`, not merely a relaxed decision constraint.

Ordering note: an evidence-first alternative (closing review on the already-anchored semantic pairs before any machinery, zero code) was considered and set aside — a semantic-only closing cycle would put partial-coverage observations in the log that read as full-pass closure. Machinery first, then one log whose coverage is honest.

## Phase 1: persisted result kinds + critique execution

Critique-note becomes the first unbounded assay executed through the batch pipeline: `commonplace-review-target-selector --model-partition {mp} critique --note {path} --json | commonplace-create-review-jobs --input - --grouping note` → sub-agent → finalize, producing acceptance rows and staleness classification exactly like semantic gates. Phase deliverable: that flow works end-to-end and the selector reports critique freshness (`missing-review` / `note-changed` / `gate-changed`) for real notes.

- Registration surface: **through the batch mechanism**, not after-the-fact recording. The pipeline pins snapshots itself as part of executing the assay, so the anchor is enforced by construction; a standalone recording command would accept the orchestrator's claim that report matches bytes — a self-reported anchor with a time-of-check gap. Naming stays layered: "gate" remains the operational term; the batch mechanism gains an assay class, not a rename.
- **Class-homogeneous jobs via a separate bundle — already given by shipped packing.** Critique is its own one-assay bundle; `--grouping note` already keys jobs by `(note, bundle)` (`_note_groups`, `src/commonplace/cli/review/create_review_jobs.py`) and `--grouping gate` packs per-gate, so no job ever mixes result-kind classes.
- **Persist the result kind on the pair.** `review_pairs.result_kind = verdict | report`, written at pair creation from the bundle's declared class; `decision` stays `pass|warn|fail|error|NULL`. `## Result: REPORT` is a completion marker, not a decision. Finalization parses against the *persisted* contract — `review_jobs` stores only `packing`, and reading gate frontmatter at finalize time would reintroduce a time-of-check gap, so the expectation must be snapshotted when the pair is created.
- Code touchpoints beyond the schema: `upsert_acceptance` rejects null-decision pairs (`src/commonplace/review/review_db.py:763`) and must instead require *completion* (a decision for verdict-kind pairs, completed report for report-kind); the `current_gate_acceptances` view's `rp.decision IS NOT NULL` predicate becomes result-kind-aware. Report-kind rows stay out of the warn queue (warn-selector filters on `decision = 'warn'`, unchanged).
- **Class declaration: virtual lens, decided.** `critique` is a virtual lens (the ADR 038/041 pattern): gate identity is `kb/instructions/critique-note.md`, one derived pair per note, the lens declares `result_kind = report`. The catalog-file alternative (a gate-shaped file with class frontmatter) is rejected — it duplicates the instruction and materially changes resolver work. Editing `critique-note.md` stales its records as `gate-changed`, no new mechanism.
- Report routing: either the pair result file becomes the report (full-pass step 7 reads from job artifacts) or finalize copies it to `kb/reports/critique/<note>.critique.md`. Decide by whichever keeps the full-pass instruction's read path simpler.
- Consequence for the instruction: step 3 of the full pass becomes a selector/create-jobs/finalize flow structurally identical to step 5.
- Scope: **critique-note only.** Friction, compression, and connect are not anchored in the MVP — full-pass closure coverage comes from phase 3 re-running them directly instead.

## Phase 2: durable carry-event recording

The carry judgment is history, so it gets an append-only record independent of acceptance. Lightest representation: a command-owned JSONL log in this workshop; a `carry_events` table only if the JSONL proves load-bearing beyond the MVP.

- **Event written at judgment time**, capturing the prior evidence *before* finalization's pruning can remove it (ADR 036 deletes superseded pairs and artifacts inline).
- **JSONL event schema, fixed now** (one object per line):
  `ts`, `note_path`, `assay_id`, `event` (`would_ack | ack | rerun | control_rerun`), `baseline_note_hash`, `current_note_hash`, `rationale` (required for `would_ack`/`ack`), `edit_kinds` (free-text list), `prior` ({`result_kind`, `decision` or `report_ref`, `note_hash`}), `outcome` (for reruns: {`flip`: bool} for verdict-kind, {`material_divergence`: bool, `note`} for report-kind).
- **Rationale is required on carry**, not merely a field. The ack command gains a required `--rationale`; acceptance may cache the latest rationale for convenience, but the event log is the authoritative history.
- **At 100% sampling, record `would_ack` and re-run** — do not transiently advance acceptance only for the rerun to supersede it. The counterfactual judgment plus the rerun outcome is the observation; acceptance moves once, on the rerun.

Phase deliverable: every carry judgment (real or counterfactual) leaves a durable event that survives acceptance pruning.

## Phase 3: closing-review step in the full-pass instruction

Add a step 10 to `kb/instructions/run-full-improvement-pass-on-note.md`: after the step-9 flow pass, the orchestrator runs one closing cycle over **all five methods**, not just the anchored ones —

- For the anchored assays (semantic bundle, critique): read the selector's cumulative diff (accepted snapshot → final bytes), then `would_ack`/ack-or-rerun per the phase 2 contract.
- For the unanchored methods (compression bundle, friction, connect): **re-run them directly** against the final text. They need no DB anchoring to participate in a 100%-rerun experiment, and this makes the closure honestly full-pass instead of two-of-five. Their rerun outcomes go into the same event log (`prior.report_ref` pointing at the pass's report files).
- Keep the license distinction sharp in the prompt: only bounded-assay acceptances ever carry skip semantics; a carried unbounded record is reused evidence, endorsing nothing; the friction gate's "For the human" line is never satisfied by a carry.
- Stopping rule: at most this one cycle. Findings from closing re-runs route to the packet's Open items; they do not trigger another transformation round.
- Control arm: occasional re-runs on *unchanged* bytes (logged as `control_rerun`) to measure the base flip rate from model variance. Without it no flip is attributable to an edit.
- Audit unit differs by result kind: verdict-kind reruns log `flip`; report-kind reruns log `material_divergence` — would the fresh report have changed steps 8–9? Don't pre-formalize "materially"; record the judgment and let the log show whether it stabilizes.

Phase deliverable: the instruction closes over its own edits with full method coverage, and every closing cycle leaves event-log lines.

## Phase 4: real runs at 100% counterfactual-ack sampling

Use the MVP on real full passes. Every carry judgment is recorded as `would_ack` and then re-run, so initially the carry decision costs nothing to trust; the sampling rate only decays later, against evidence from the log. This phase produces observations, not code — it is where constraints get located (see below).

## Phase 5: human-attestation probe

The simplest slice of workshop case 2, deliberately last — informed by what the event model taught. This is a separate architectural probe, **not** a cheap reuse of the phase 1 mechanism: an acceptance requires a completed review pair, so `commonplace-attest` cannot just pin snapshots and write an acceptance row. Three candidate representations, chosen against phases 1–4 experience:

- a synthetic completed review job/pair under a human partition;
- generalizing acceptance away from review-pair evidence;
- attestations as their own fact/event type — the current-state-vs-history lesson applies with force here, since attestation history is plausibly the point.

Design constraints that survive regardless of representation:

- **One kind, force-free.** A single attestation whose contract file states exactly: *the user recorded that they reviewed these bytes* — no "accepts", no approval semantics; "accepts it" is already endorsement-shaped. Force-free means no machinery consumes a fresh attestation as a license.
- The contract file is the gate-side identity, so editing what the attestation means stales every attestation as `gate-changed`.
- Single `human` partition for the MVP; per-actor partitions only if observation demands them.
- The command echoes what it pinned (short hash or one-line diff summary against the previously attested state) so the user can catch attesting to bytes they didn't just read.
- This is the anchored alternative to the `reviewed: true` boolean the README's purpose asks about — friction with it in use is direct evidence on why systems default to unanchored booleans.

Phase deliverable: the user can attest a note, the selector (or a sibling query) reports attestation freshness, and nothing else changes behavior.

## Explicitly not built

- Footprint enforcement machinery — declared footprints stay stated intent the cumulative diff verifies.
- Any edit-kind taxonomy in the system — `edit_kinds` in the event log is free-text observation vocabulary.
- Trust-dial automation — sampling rate changes are manual judgments against the log.
- A review-kind taxonomy or attestation forces — the MVP ships exactly one force-free attestation kind; kinds and forces wait for observed need (see phase 5).
- Anchoring for compression, friction, and connect — phase 3 re-runs them directly; DB anchoring for them waits until the critique pattern has proven itself.

## What phases 4–5 should observe (constraint location)

Ties to the location criteria in [carry-heuristics.md](./carry-heuristics.md):

- Constraint 1 (direction over size): do flips in the log track edit *direction* rather than diff size?
- Constraint 2 (non-compositionality): does an accumulated series of individually-carried edits ever flip a coherence check? (Baseline anchoring should surface this as a growing cumulative diff.)
- Constraint 3's premise: is a declared flow-only step 9 ever caught changing a claim in the cumulative diff?
- Constraint 4: does the one-cycle stopping rule ever leave residual findings that genuinely needed a second round, or does routing to Open items suffice?
- Case 3 flip: does a current-critique signal ever get read downstream as "critiqued and handled"? That observation, if it occurs, relocates the do-not-anchor rule as a real constraint.
- Case 2 (human attestation): does the single force-free kind get stretched — the user wanting to record something weaker or stronger, or wanting a fresh attestation to actually license something? Each stretch is a located requirement for the kinds/forces design.
