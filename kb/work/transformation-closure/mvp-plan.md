# MVP build plan: closing review on the full pass over a unified diff-and-ack surface

Implementation-ready phased plan for the workshop's MVP, given the design in [unified-diff-and-ack.md](./unified-diff-and-ack.md). The MVP is a calibrated one-cycle closing review with full method coverage, carry judgments recorded as append-only events with required rationale, and an observation log with a variance control arm. Each phase is self-contained: it delivers testable value on its own and later phases build on it without reaching back.

Two structural distinctions, located at design time against shipped code (a codex review of an earlier draft of this plan), shape the whole build:

- **Current state vs. history.** Acceptance is deliberately current-state storage with inline pruning ([ADR 036](../../reference/adr/036-review-acceptance-is-current-state-not-append-only-history.md)): a superseding rerun deletes the prior pair, its job, and its artifacts in the same transaction. A carry judgment is *history* — so it cannot live (only) on acceptance, or the audit rerun destroys the attribution substrate exactly when the audit result arrives.
- **Verdict vs. completion.** A decision (pass/warn/fail/error) and a protocol completion marker are different facts. Unbounded assays complete without deciding, so the pair needs a persisted `result_kind`, not merely a relaxed decision constraint.

Ordering note: an evidence-first alternative (closing review on the already-anchored semantic pairs before any machinery, zero code) was considered and set aside — a semantic-only closing cycle would put partial-coverage observations in the log that read as full-pass closure. Machinery first, then one log whose coverage is honest.

## Report layout and retention (cross-phase)

The key lifetime risk: decision history is auditable only if enough of the *compared reports* survives — event rows alone are insufficient, and DB job artifacts are prunable under ADR 036. Rules:

- Each full-pass invocation mints a **`pass_id`** at step 1; it doubles as the `closing_cycle_id` in events (one closing cycle per pass). Reports live under genuinely pass-scoped paths:

  ```text
  kb/reports/full-pass/<note-name>/<pass_id>/
    initial/    # step 1–6 runs
    closing/    # step 10 reruns
    controls/   # duplicate control runs
  ```

  A closing rerun can never overwrite an initial report, and successive passes never overwrite each other.
- Any report a judgment, audit, or comparison uses is copied out of the job artifact directory into the pass directory by the orchestrator immediately after finalization, *before* a later superseding finalization can prune it.
- Events reference reports as `{path, sha256}`. **A hash verifies content; it does not preserve it** — so compared reports are retained on disk through workshop closure (no cleanup of `kb/reports/full-pass/` while the workshop is open), and the hash exists to detect tampering or accidental rewrite, not to substitute for retention.

## Phase 1: persisted result kinds + critique execution

Critique-note becomes the first unbounded assay executed through the batch pipeline: `commonplace-review-target-selector --model-partition {mp} critique --note {path} --json | commonplace-create-review-jobs --input - --grouping note` → sub-agent → finalize, producing acceptance rows and staleness classification exactly like semantic gates. Phase deliverable: that flow works end-to-end and the selector reports critique freshness for real notes.

- Registration surface: **through the batch mechanism**, not after-the-fact recording. The pipeline pins snapshots itself as part of executing the assay, so the anchor is enforced by construction; a standalone recording command would accept the orchestrator's claim that report matches bytes — a self-reported anchor with a time-of-check gap. Naming stays layered: "gate" remains the operational term; the batch mechanism gains an assay class, not a rename.
- **Class-homogeneous jobs via a separate bundle — already given by shipped packing.** Critique is its own one-assay bundle; `--grouping note` keys jobs by `(note, bundle)` (`_note_groups`, `src/commonplace/cli/review/create_review_jobs.py`) and `--grouping gate` packs per-gate, so no job ever mixes result-kind classes.
- **Persist the result kind on the pair.** `review_pairs.result_kind = verdict | report`, written at pair creation from the bundle's declared class. `## Result: REPORT` is a completion marker, not a decision. Finalization parses against the *persisted* contract — `review_jobs` stores only `packing`, and reading gate frontmatter at finalize time would reintroduce a time-of-check gap.
- **Executable `result_kind` invariants:**
  - queued verdict pair: `decision NULL`, `reviewed_at NULL`
  - completed verdict pair: `decision NOT NULL`, `reviewed_at NOT NULL`
  - queued report pair: `decision NULL`, `reviewed_at NULL`
  - completed report pair: `decision NULL`, `reviewed_at NOT NULL`
  - column and table constraints, exactly: `result_kind TEXT NOT NULL CHECK (result_kind IN ('verdict','report'))` and `CHECK (result_kind = 'verdict' OR decision IS NULL)` — a report pair can never acquire a decision
  - **pair completion is per-kind** — `reviewed_at` alone is insufficient for a verdict pair: a verdict pair is complete when `decision IS NOT NULL AND reviewed_at IS NOT NULL`; a report pair when `reviewed_at IS NOT NULL`
  - **validation split, matching shipped finalization order** (pairs complete → acceptance upserts → pruning → job marked completed): `upsert_acceptance` validates *pair* completion per-kind, replacing its null-decision rejection (`src/commonplace/review/review_db.py:763`); the `current_gate_acceptances` view separately requires the completed parent job (it already joins on `j.status = 'completed'`) plus per-kind pair completion, and exposes `result_kind` and `decision`
  - warn queue untouched: warn-selector filters `decision = 'warn'`, which never matches a report pair
- Schema scope: the `result_kind` column with its CHECK, the view predicate change, `REVIEW_SCHEMA_VERSION` 4 → 5. `acceptance` gains no column (class derives through the accepted-pair join).
- **Migration script, recorded in the repo.** Populated review stores exist on more than one machine, and every acceptance row is paid-for review evidence — recreate-and-re-earn is not acceptable. Phase 1 ships `scripts/migrate-review-db-v4-to-v5.py` (stdlib-only) **in the same commit as the schema bump** (a store migrated ahead of the code bump would be rejected by `init_db`, and vice versa). One transaction: SQLite table rebuild for `review_pairs` — `ALTER TABLE` cannot add the table-level `CHECK (result_kind = 'verdict' OR decision IS NULL)`, so create-new / copy with `result_kind='verdict'` backfill / drop / rename — recreate the two `review_pairs` indexes, drop and recreate `current_gate_acceptances` with the new completion predicate, `PRAGMA foreign_key_check`, bump `user_version` to 5. `init_db`'s version gate stays; its mismatch error message should point at the script.
- **Critique virtual lens, fully specified:** request form `critique` derives one pair per explicitly targeted note (`--note` paths/directories); persisted gate identity is `kb/instructions/critique-note.md` in a source checkout, resolving through the same installed-framework path mechanism as catalog gates in generated projects; resolver work is a `critique` branch beside the type/collection lens derivations in the selector and `resolve_gates.py`, declaring `result_kind = report`. **Excluded from `--all-gates` during the MVP**, for three reasons: sweeps would pay for a heavyweight per-note adversarial run whose output nothing in the sweep path consumes (report-kind rows never reach the warn queue or the fix system); a sweep would put "critique: fresh" on the whole KB — the "critiqued and handled" certification illusion case 3 exists to test — before the experiment has run; and sweep-created acceptance state would sit outside the MVP protocol (no closing cycle, no carry events), contaminating phase 4's log. Exclusion is the reversible default. At promotion time the real question is whether `--all-gates` should distinguish assay classes at all (bounded by default, unbounded opt-in) — "all applicable criteria" was defined when every criterion carried a verdict. Editing `critique-note.md` stales its records as `gate-changed`, no new mechanism.
- **Prompt conflict and instruction TOCTOU resolved together, pre-release.** Two changes, both free now because no critique acceptance state exists yet:
  - Revise `critique-note.md` so the judgment method and report shape are separate from its hand-run output destination (routing becomes caller-supplied) — the instruction stops mandating a path that conflicts with the worker contract (write only `bundle-output.md`).
  - The rendered job prompt **embeds the instruction text captured in the job's gate snapshot** — the worker never reads the live file, so it cannot judge by different criteria than the snapshot acceptance pins. This deliberately diverges from the ADR 038 read-from-disk pattern, which carries the same theoretical gap for type/collection pairs; embedding costs prompt tokens but buys input integrity, which is the point of a version-anchoring experiment. Reconciling the two patterns is a promotion-time question. Report-specific language (emit the critique as this pair's block, end with `## Result: REPORT`) lives in the renderer.
- Report routing: after finalize, the orchestrator copies the pair's report block to `kb/reports/full-pass/<note-name>/{initial|closing}/critique.md` per the retention rules above and records its hash in the event log.
- Consequence for the instruction: step 3 of the full pass becomes a selector/create-jobs/finalize flow structurally identical to step 5.
- Scope: **critique-note only.** Friction, compression, and connect are not anchored in the MVP — full-pass closure coverage comes from phase 3 re-running them directly.

## Phase 2: durable carry-event recording

The carry judgment is history, so it gets an append-only record independent of acceptance.

- **Path and owner:** `kb/work/transformation-closure/observations/carry-events.jsonl`, written only through a new `commonplace-carry-event` command that validates an event against the schema below and appends one line (`O_APPEND`, one `write()` per line, no rewrites). **Failure semantics: no event, no carry** — if the append fails, the orchestrator must rerun instead of carrying (enforced-or-omitted, fail toward rerun).
- **Events are immutable and correlated.** Common fields: `event_id` (UUID), `ts`, `closing_cycle_id` (= the pass's `pass_id`), `note_path`, `assay_id`, `runner`, `model`, `effort`, `baseline_note_hash`, `current_note_hash`. Kinds, each its own immutable event:
  - `carry_judgment` — `judgment: would_ack | ack`, `rationale` (**required**), `edit_kinds` (free-text list), `prior: {result_kind, decision | report_ref: {path, sha256}, note_hash}` — the prior evidence captured *before* pruning can remove it;
  - `ack_outcome` — `carry_event_id`, `succeeded: bool` — the DB result of a real ack (see ordering below);
  - `audit_result` — `audits_event_id` (the `carry_judgment` it audits — **reserved for reruns that test a real or counterfactual carry**), `outcome: {flip: bool}` for verdict-kind or `{material_divergence: bool, note}` for report-kind, `report_refs` for the compared reports;
  - `comparison_result` — `initial_report_ref`, `closing_report_ref`, `outcome` (same per-kind shape) — for the unanchored always-rerun methods, whose initial-to-closing comparisons audit no carry judgment;
  - `control_result` — references the first-run event/report it duplicates, same outcome shape.
  Corrections are new events referencing the corrected `event_id`, never edits.
- **Ack ordering across the two stores is event-first, stated explicitly.** JSONL and SQLite cannot commit atomically. A `carry_judgment` is a judgment record, appended *before* the DB transaction — if the append fails, the ack aborts before touching the DB ("no event, no carry"). After the DB transaction, the ack command appends `ack_outcome`. A judgment event whose DB update subsequently failed is valid history — the judgment happened — with no state effect; a judgment with no `ack_outcome` (crash window) is resolved by checking current acceptance against the judgment's hashes.
- **CLI workflow:** `would_ack` events are appended explicitly by the orchestrator via `commonplace-carry-event` (no DB state changes, hence no outcome event). Real acks go through `commonplace-ack-gate-review`, which gains a **required `--rationale`** and owns the event-first sequence above, one `carry_judgment` per acked pair — real carries are recorded without relying on orchestrator discipline. A shared rationale across several gates of one note is allowed at the CLI and fans out to per-pair events. Audit and comparison outcomes are appended by the orchestrator after comparing reruns against `prior`/report refs.
- At 100% sampling: record `would_ack` and re-run — acceptance moves once, on the rerun, never transiently.

Phase deliverable: every carry judgment (real or counterfactual) leaves a durable, correlated event that survives acceptance pruning.

## Phase 3: closing-review step in the full-pass instruction

Add a step 10 to `kb/instructions/run-full-improvement-pass-on-note.md`: after the step-9 flow pass, the orchestrator runs one closing cycle (minting a `closing_cycle_id`) over **all five methods** —

- Anchored assays (semantic bundle, critique): read the selector's cumulative diff (accepted snapshot → final bytes), then `would_ack`/ack-or-rerun per the phase 2 contract.
- Unanchored methods (compression bundle, friction, connect): **re-run directly** against the final text — no DB anchoring needed to join a 100%-rerun experiment. Their initial-to-closing comparisons audit no carry judgment, so they log `comparison_result` events (`initial_report_ref` → `closing_report_ref`), never `audit_result`.
- **Audit granularity:** semantic per gate (one judgment/audit per gate pair); critique, friction, and connect per report; compression at bundle level — one rerun, one report — with per-gate comparisons nested inside the `audit_result` outcome.
- **Control arm, deterministic schedule (initial):** every closing cycle duplicate-runs two assays on the *identical* final bytes — one verdict-kind (round-robin over the semantic gates across cycles) and one report-kind (critique) — recorded as `control_result`. A control is valid only if bytes, instruction snapshot, runner, model, and effort are identical to the run it duplicates, all recorded in the event.
- **Controls never touch acceptance.** A control re-executes the *persisted job prompt* of the run it duplicates in a fresh sub-agent; its output is parsed with the same parser, written under `controls/`, and **never finalized** — no acceptance upsert, no pruning of the run it duplicates. No new finalization mode is needed; controls simply have no DB path.
- **Control input identity is complete only for self-contained gates.** Some semantic gates follow linked artifacts, so identical note+gate bytes do not guarantee identical inputs. The MVP restricts the verdict-kind control rotation to gates whose inputs are genuinely note-plus-gate (documented per gate when the rotation is set up); linked-input snapshotting is a later extension if the restriction starves the rotation. The schedule is revisited once the base flip/divergence rate stabilizes.
- License distinction in the prompt: only bounded-assay acceptances ever carry skip semantics; a carried unbounded record is reused evidence, endorsing nothing; the friction gate's "For the human" line is never satisfied by a carry.
- Stopping rule: at most this one cycle. **Packet update:** step 10 appends a "Closing cycle" section to `full-pass-report.md` — cycle id plus a per-assay table of judgment and outcome — and residual findings route to the packet's Open items; they do not trigger another transformation round.
- Audit unit differs by result kind: verdict-kind reruns log `flip`; report-kind reruns log `material_divergence` — would the fresh report have changed steps 8–9? Don't pre-formalize "materially"; record the judgment and let the log show whether it stabilizes.

Phase deliverable: the instruction closes over its own edits with full method coverage, and every closing cycle leaves correlated event-log lines and retained reports.

## Phase 4: real runs at 100% counterfactual-ack sampling

Use the MVP on real full passes. Every carry judgment is recorded as `would_ack` and then re-run, so initially the carry decision costs nothing to trust; the sampling rate only decays later, against evidence from the log. This phase produces observations, not code — it is where constraints get located (see below).

## Phase 5: human-attestation design selection

A **design-selection phase, not a build phase**: its deliverable is a chosen representation, written as a proposal in `kb/reference/proposals/`, informed by what phases 1–4 taught about the event model. Implementation happens only after selection. The candidates (an acceptance requires completed review-pair evidence, so this is not a cheap reuse of the phase 1 mechanism):

- a synthetic completed review job/pair under a human partition;
- generalizing acceptance away from review-pair evidence;
- attestations as their own fact/event type — the current-state-vs-history lesson applies with force here, since attestation history is plausibly the point.

Design constraints that survive regardless of representation:

- **One kind, force-free.** The contract file states exactly: *the user recorded that they reviewed these bytes* — no "accepts", no approval semantics; "accepts it" is already endorsement-shaped. Force-free means no machinery consumes a fresh attestation as a license.
- The contract file is the gate-side identity, so editing what the attestation means stales every attestation as `gate-changed`.
- Single `human` partition; per-actor partitions only if observation demands them.
- **Explicit byte confirmation over after-the-fact echo:** the command requires the user to pass what they reviewed — `commonplace-attest {note} --reviewed-hash {sha}`, with the hash obtained from a separate show step — and fails on mismatch, rather than pinning current bytes and merely echoing the hash afterwards.
- This is the anchored alternative to the `reviewed: true` boolean the README's purpose asks about — friction with it in use is direct evidence on why systems default to unanchored booleans.

## Explicitly not built

- Footprint enforcement machinery — declared footprints stay stated intent the cumulative diff verifies.
- Any edit-kind taxonomy in the system — `edit_kinds` in the event log is free-text observation vocabulary.
- Trust-dial automation — sampling rate changes are manual judgments against the log.
- Attestation machinery — phase 5 selects a representation; building it is a post-selection decision. Kinds and forces wait for observed need.
- Anchoring for compression, friction, and connect — phase 3 re-runs them directly; DB anchoring for them waits until the critique pattern has proven itself.

## Test matrix (per phase)

Phase 1:

- parser accepts `## Result: REPORT` only for report-kind pairs and rejects it for verdict-kind; rejects `PASS/WARN/FAIL/ERROR` on report-kind pairs
- queued/completed invariants hold for both kinds, including the `result_kind = 'verdict' OR decision IS NULL` CHECK
- freshness classification for critique pairs: `missing-review`, `note-changed`, `gate-changed` (on editing `critique-note.md`)
- warn queue never contains a report-kind pair
- a job creation request mixing result kinds is rejected (packing prevents it; the test asserts the invariant anyway)
- the rendered critique prompt embeds the gate-snapshot instruction text: editing `critique-note.md` after job creation does not change the job's prompt
- `upsert_acceptance` accepts a completed report pair and a completed verdict pair, rejects an incomplete pair of either kind (verdict with `reviewed_at` but NULL decision included)
- existing verdict-gate flows are behavior-identical (regression: same selector output, same finalization results on a fixture store)
- the migration script upgrades a populated v4 fixture store: `user_version` becomes 5, every pre-existing pair reads `result_kind='verdict'`, acceptance rows and freshness classifications are unchanged, `PRAGMA foreign_key_check` is clean, and re-running the script on a v5 store is a refused no-op

Phase 2:

- an appended event and its copied report remain readable after a superseding finalization prunes the original pair/job/artifacts
- concurrent appends do not interleave lines
- a failed append blocks the carry (the ack command refuses to touch the DB if its `carry_judgment` write fails)
- a DB failure after a successful judgment append leaves the judgment event, an `ack_outcome` with `succeeded: false`, and unchanged acceptance
- `commonplace-ack-gate-review` without `--rationale` fails

Phase 3:

- a closing rerun writes under `closing/` and leaves `initial/` byte-identical; two passes over the same note write under distinct `pass_id` directories
- a `control_result` is rejected unless bytes, instruction snapshot, runner, model, and effort match the duplicated run
- a control run leaves the review DB byte-identical (no acceptance change, no pruning of the duplicated run)
- unanchored-method comparisons emit `comparison_result`, never `audit_result`
- the packet gains a "Closing cycle" section and residual findings land in Open items

Phase 5 (post-selection, if built):

- `commonplace-attest` fails on a stale `--reviewed-hash`

## What phases 4–5 should observe (constraint location)

Ties to the location criteria in [carry-heuristics.md](./carry-heuristics.md):

- Constraint 1 (direction over size): do flips in the log track edit *direction* rather than diff size?
- Constraint 2 (non-compositionality): does an accumulated series of individually-carried edits ever flip a coherence check? (Baseline anchoring should surface this as a growing cumulative diff.)
- Constraint 3's premise: is a declared flow-only step 9 ever caught changing a claim in the cumulative diff?
- Constraint 4: does the one-cycle stopping rule ever leave residual findings that genuinely needed a second round, or does routing to Open items suffice?
- Case 3 flip: does a current-critique signal ever get read downstream as "critiqued and handled"? That observation, if it occurs, relocates the do-not-anchor rule as a real constraint.
- Case 2 (human attestation): does the single force-free kind get stretched — the user wanting to record something weaker or stronger, or wanting a fresh attestation to actually license something? Each stretch is a located requirement for the kinds/forces design.
