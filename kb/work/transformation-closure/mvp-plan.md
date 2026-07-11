# MVP build plan: closing review on the full pass over a unified diff-and-ack surface

The MVP is a minimal vertical slice: exercise the new `result_kind` schema end-to-end on one open-ended assay (critique), and test closure on the actual five-method full-pass workflow at 100% counterfactual sampling, with a simple pass-local observation record and manually run controls. Production instrumentation — event commands, ack integration, automated validation — is deliberately deferred to an observation-gated decision (part 4).

**Status, 2026-07-11:** parts 1–3 are complete. The MVP shipped, the full suite passes (377 passed, 1 skipped), and five real passes produced 53 observation events. Part 4's gate is **no for now**: all 28 counterfactual decisions were `would_rerun`, no carry opportunity was exercised, and rerun cost was not measured. See [mvp-results.md](./mvp-results.md) for the evidence and constraint classification. Part 5 remains independent and unrun.

Scope discipline note: an earlier draft of this plan accreted production event machinery through successive implementation-readiness reviews; a codex review restored the boundary with one observation — **at 100% counterfactual sampling no real ack ever occurs** (acceptance always advances through the rerun), so ack-integrated event recording solves a problem the MVP does not encounter. The machinery's design survives, recorded under part 4 so it isn't re-derived, but nothing in it blocks the first real runs.

Two structural distinctions, located at design time against shipped code, shape the build:

- **Current state vs. history.** Acceptance is deliberately current-state storage with inline pruning ([ADR 036](../../reference/adr/036-review-acceptance-is-current-state-not-append-only-history.md)): a superseding rerun deletes the prior pair, its job, and its artifacts in the same transaction. A carry judgment is *history* — so it lives in the observation record (and, if instrumentation is built, in append-only events), never only on acceptance.
- **Verdict vs. completion.** A decision (pass/warn/fail/error) and a protocol completion marker are different facts. Open-ended assays complete without deciding, so the pair needs a persisted `result_kind`, not merely a relaxed decision constraint.

Ordering note: an evidence-first alternative (closing review on the already-anchored semantic pairs before any machinery, zero code) was considered and set aside — a semantic-only closing cycle would put partial-coverage observations in the log that read as full-pass closure. The `result_kind` slice is the minimum machinery that makes the log's coverage honest.

## Report layout, retention, and the observation record (cross-part)

The key lifetime risk: judgments are auditable only if enough of the *compared reports* survives — and DB job artifacts are prunable under ADR 036. Rules:

- Each full-pass invocation mints a **`pass_id`** at step 1. Reports live under pass-scoped paths:

  ```text
  kb/reports/full-pass/<note-name>/<pass_id>/
    initial/    # step 1–6 runs
    closing/    # step 10 reruns
    controls/   # manually duplicated control runs
  ```

  A closing rerun can never overwrite an initial report, and successive passes never overwrite each other.
- Any report a judgment or comparison uses is copied out of the job artifact directory into the pass directory by the orchestrator immediately after finalization, *before* a later superseding finalization can prune it.
- Reports are referenced by `{path, sha256}`. **A hash verifies content; it does not preserve it** — compared reports are retained on disk through workshop closure (no cleanup of `kb/reports/full-pass/` while the workshop is open).
- **The observation record is committed workshop evidence, not a gitignored report**: one JSONL file per pass at `kb/work/transformation-closure/observations/<pass_id>.jsonl`, written by the orchestrator by hand — no owning command in the MVP. Judgments and outcomes are not regenerable, so they live where the workshop lives.

## Part 1: core MVP build — result kinds, migration, critique lens

Critique-note becomes the first report-kind assay executed through the batch pipeline: `commonplace-review-target-selector --model-partition {mp} critique --note {path} --json | commonplace-create-review-jobs --input - --grouping note` → sub-agent → finalize, producing acceptance rows and staleness classification exactly like semantic gates. Deliverable: that flow works end-to-end and the selector reports critique freshness for real notes.

- Registration surface: **through the batch mechanism**, not after-the-fact recording. The pipeline pins snapshots itself as part of executing the assay, so the anchor is enforced by construction; a standalone recording command would accept the orchestrator's claim that report matches bytes — a self-reported anchor with a time-of-check gap. Naming stays layered: "gate" remains the operational term; the batch mechanism gains an assay class, not a rename.
- **Class-homogeneous jobs via a separate bundle — already given by shipped packing.** Critique is its own one-assay bundle; `--grouping note` keys jobs by `(note, bundle)` (`_note_groups`, `src/commonplace/cli/review/create_review_jobs.py`) and `--grouping gate` packs per-gate, so no job ever mixes result-kind classes.
- **Persist the result kind on the pair, and carry it through the stack.** `review_pairs.result_kind = verdict | report`, written at pair creation from the bundle's declared class, and threaded through pair models, SQL reads/writes, manifests, and CLI payloads. `## Result: REPORT` is a completion marker, not a decision. Finalization parses against the *persisted* contract — `review_jobs` stores only `packing`, and reading gate frontmatter at finalize time would reintroduce a time-of-check gap.
- **Executable `result_kind` invariants:**
  - queued pair (either kind): `decision NULL`, `reviewed_at NULL`
  - completed verdict pair: `decision NOT NULL`, `reviewed_at NOT NULL`
  - completed report pair: `decision NULL`, `reviewed_at NOT NULL`
  - column and table constraints, exactly: `result_kind TEXT NOT NULL CHECK (result_kind IN ('verdict','report'))` and `CHECK (result_kind = 'verdict' OR decision IS NULL)`
  - **pair completion is per-kind** — `reviewed_at` alone is insufficient for a verdict pair
  - **validation split, matching shipped finalization order** (pairs complete → acceptance upserts → pruning → job marked completed): `upsert_acceptance` validates *pair* completion per-kind, replacing its null-decision rejection (`src/commonplace/review/review_db.py:763`); the `current_gate_acceptances` view separately requires the completed parent job (it already joins on `j.status = 'completed'`) plus per-kind pair completion, and exposes `result_kind` and `decision`
  - warn queue untouched: warn-selector filters `decision = 'warn'`, which never matches a report pair
- Schema scope: the `result_kind` column with its CHECK, the view predicate change, `REVIEW_SCHEMA_VERSION` 4 → 5. `acceptance` gains no column (class derives through the accepted-pair join).
- **Migration script, recorded in the repo.** Populated review stores exist on more than one machine, and every acceptance row is paid-for review evidence — recreate-and-re-earn is not acceptable. Part 1 ships `scripts/migrate-review-db-v4-to-v5.py` (stdlib-only) **in the same commit as the schema bump** (a store migrated ahead of the code bump would be rejected by `init_db`, and vice versa). The table rebuild is FK-sensitive — `acceptance.accepted_review_pair_id` references `review_pairs` — so the sequence is exact:
  1. `PRAGMA foreign_keys = OFF` — issued on the fresh connection, **before** any transaction (the pragma is a no-op inside one);
  2. `BEGIN IMMEDIATE`;
  3. create `review_pairs_new` with the full v5 shape (both CHECKs), `INSERT ... SELECT` from `review_pairs` with `'verdict'` backfilled and **`review_pair_id` values preserved verbatim** — this is why `acceptance` needs no rebuild;
  4. `DROP TABLE review_pairs`; `ALTER TABLE review_pairs_new RENAME TO review_pairs`; recreate the two `review_pairs` indexes; drop and recreate `current_gate_acceptances` with the new completion predicate;
  5. `PRAGMA foreign_key_check` — any returned row aborts with `ROLLBACK`;
  6. `PRAGMA user_version = 5`; `COMMIT`; `PRAGMA foreign_keys = ON`.

  `init_db`'s version gate stays; its mismatch error message should point at the script.
- **Critique virtual lens, fully specified:** request form `critique` derives one pair per explicitly targeted note (`--note` paths/directories); persisted gate identity is `kb/instructions/critique-note.md` in a source checkout, resolving through the same installed-framework path mechanism as catalog gates in generated projects; resolver work is a `critique` branch beside the type/collection lens derivations in the selector and `resolve_gates.py`, declaring `result_kind = report`. **Excluded from `--all-gates` during the MVP**, for three reasons: sweeps would pay for a heavyweight per-note adversarial run whose output nothing in the sweep path consumes (report-kind rows never reach the warn queue or the fix system); a sweep would put "critique: fresh" on the whole KB — the "critiqued and handled" certification illusion case 3 exists to test — before the experiment has run; and sweep-created acceptance state would sit outside the MVP protocol, contaminating the observations. Exclusion is the reversible default. At promotion time the real question is whether `--all-gates` should distinguish question shapes at all (closed-ended by default, open-ended opt-in). Editing `critique-note.md` stales its records as `gate-changed`, no new mechanism.
- **Prompt conflict and instruction TOCTOU resolved together, pre-release.** Two changes, both free now because no critique acceptance state exists yet:
  - Revise `critique-note.md` so the judgment method and report shape are separate from its hand-run output destination (routing becomes caller-supplied) — the instruction stops mandating a path that conflicts with the worker contract (write only `bundle-output.md`).
  - The rendered job prompt **embeds the instruction text captured in the job's gate snapshot** — the worker never reads the live file, so it cannot judge by different criteria than the snapshot acceptance pins. This deliberately diverges from the ADR 038 read-from-disk pattern, which carries the same theoretical gap for type/collection pairs; embedding costs prompt tokens but buys input integrity, which is the point of a version-anchoring experiment. Reconciling the two patterns is a promotion-time question. Report-specific language (emit the critique as this pair's block, end with `## Result: REPORT`) lives in the renderer.
- Report routing: after finalize, the orchestrator copies the pair's report block to `kb/reports/full-pass/<note-name>/<pass_id>/{initial|closing}/critique.md` per the retention rules above.
- Consequence for the instruction: step 3 of the full pass becomes a selector/create-jobs/finalize flow structurally identical to step 5.
- Scope: **critique-note only.** Friction, compression, and connect are not anchored in the MVP — full-pass closure coverage comes from part 2 re-running them directly.

## Part 2: MVP workflow — step 10, observation record, manual controls

Add a step 10 to `kb/instructions/run-full-improvement-pass-on-note.md`: after the step-9 flow pass, the orchestrator runs one closing cycle over **all five methods** —

- Anchored assays (semantic bundle, critique): read the selector's cumulative diff (accepted snapshot → final bytes), record a **counterfactual judgment** — `would_ack` or `would_rerun`, with rationale and rough edit kinds — then **re-run regardless** (100% counterfactual sampling) and record the outcome against the judgment.
- **Step-10 semantic reruns are single-pair jobs** — `--grouping gate --batch-size 1` against the one target note — unlike step 5's whole-bundle note-grouped job. This is what makes controls possible: a single-gate persisted prompt can be duplicated verbatim apart from its output destination, whereas replaying the bundle prompt would rerun every gate including the linked-input ones excluded from the control rotation (the alternative — duplicate the bundle prompt and snapshot every linked input — was rejected as heavier).
- Unanchored methods (compression bundle, friction, connect): re-run directly against the final text and compare initial → closing reports. Compression compares at bundle level with per-gate detail nested in the outcome.
- Audit unit differs by result kind: verdict-kind reruns record `flip`; report-kind reruns record `material_divergence` — would the fresh report have changed steps 8–9? Don't pre-formalize "materially"; record the judgment and let the record show whether it stabilizes.
- License distinction in the prompt: only closed-ended assay acceptances ever carry skip semantics; a carried open-ended record is reused evidence, endorsing nothing; the friction gate's "For the human" line is never satisfied by a carry.
- Stopping rule: at most this one cycle. Step 10 appends a "Closing cycle" section to `full-pass-report.md` — `pass_id` plus a per-assay table of judgment and outcome — and residual findings route to the packet's Open items; they do not trigger another transformation round.

**Observation record** — one schema-v2 JSONL line per closing event in `observations/<pass_id>.jsonl`, hand-written against an unambiguous template: one line per anchored pair, one per unanchored method family, and one per control. Common fields identify the pass, note, assay, initial/final note hashes, and the adjudicator. Each report reference carries its own execution provenance (`runner`, nullable `model`, nullable `effort`), because a comparison spans independent runs; unavailable values are JSON null, never the string `"unknown"`. The rest is discriminated by `record_kind`:

- `carry_audit` (anchored semantic/critique — the rerun tests a counterfactual carry): `would_ack` vs `would_rerun` with rationale and rough edit kinds, initial and closing report refs, verdict `flip` or `material_divergence`;
- `closing_comparison` (unanchored compression/friction/connect — no carry judgment exists): initial and closing report refs, divergence outcome only;
- `control_comparison` (a duplicate of a closing run, *not* an initial-vs-closing comparison): source and control report refs, gate/instruction snapshot hash, source and control prompt hashes, `flip` or divergence.

**Manual controls.** The variance control arm runs by hand during the MVP. Retain the closing single-pair job's prompt and raw sentinel-bracketed output under `controls/`; duplicate the prompt with only its output destination changed; execute it in a newly isolated sub-agent; and compare raw source output with raw control output rather than a finalized pair artifact with a bundle. Read the gate-snapshot hash from the completed source pair's reviewed snapshot, not the live criterion file. Record both prompt/output hashes and per-run provenance in `control_comparison`. Controls are never finalized — no acceptance change, no pruning of the duplicated run. Schedule: each closing cycle duplicates one verdict-kind run and one report-kind run (critique) on the identical final bytes. The verdict-kind rotation is fixed to the four self-contained semantic gates — `internal-consistency`, `load-bearing-qualifiers`, `explanatory-reach`, `explication-quality` — because `grounding-alignment` follows up to 5 links and `completeness-boundary-cases` may read a cited source, so identical note+gate bytes do not guarantee identical inputs for them.

Deliverable: the instruction closes over its own edits with full method coverage, and every closing cycle leaves observation lines and retained reports.

## Part 3: run and observe — complete

Five real full passes ran at 100% counterfactual sampling. **No real ack occurred** — acceptance always advanced through the rerun; the carry decision was measured, not trusted. The observations support keeping the closing rerun for this substantive workflow, but they did not locate the proposed general carry heuristics; see [mvp-results.md](./mvp-results.md).

## Part 4: instrumentation decision — no for now

Build durable carry infrastructure **only if part 3 shows real carrying is worth having** — roughly: `would_ack` judgments are usually confirmed by their reruns *and* the rerun cost is material enough that skipping some would pay. If carrying isn't useful, this part is a documented no.

The gate did not open. There were zero `would_ack` judgments, so the confirmation rate is undefined rather than high, and the record contains no usable cost measurement. Do not build the machinery below from the current evidence. Reconsider only with a deliberately different probe that produces plausible carry candidates and measures rerun cost.

The machinery below was designed and reviewed during planning; it is recorded here so a yes-decision doesn't re-derive it:

- `commonplace-carry-event`: append-only JSONL writer (`O_APPEND`, one write per line), "no event, no carry" failure semantics;
- correlated immutable event kinds — `carry_judgment` (rationale required), `ack_outcome`, `audit_result` (reserved for reruns testing a carry, `audits_event_id`), `comparison_result` (unconditional initial↔closing comparisons), `control_result` (with `gate_snapshot_sha256`, `source_prompt_sha256`, `control_prompt_sha256`) — plus `event_id` / `closing_cycle_id` correlation and corrections-as-new-events;
- **event-first cross-store ordering**: JSONL and SQLite cannot commit atomically, so the `carry_judgment` is appended before the DB transaction and `ack_outcome` after; an orphaned judgment is valid history with no state effect;
- ack integration: `commonplace-ack-gate-review` gains a required `--rationale` and owns the event sequence, one judgment per pair, shared rationale fanning out;
- automated control identity validation and a mechanical control-prompt adapter;
- generalized durable report archival;
- reduced audit sampling, trust-dial operation, and real rationale-bearing carries.

## Part 5: human-attestation design probe (independent)

Outside the MVP and outside its completion criteria — it uses what the closure experiment teaches about state, history, and evidence, but must not delay the first runs. A design-selection probe whose deliverable is a chosen representation written as a proposal in `kb/reference/proposals/`. The candidates (an acceptance requires completed review-pair evidence, so this is not a cheap reuse of the part 1 mechanism): a synthetic completed review job/pair under a human partition; generalizing acceptance away from review-pair evidence; attestations as their own fact/event type — the current-state-vs-history lesson applies with force here, since attestation history is plausibly the point.

Design constraints that survive regardless of representation:

- **One kind, force-free.** The contract file states exactly: *the user recorded that they reviewed these bytes* — no "accepts", no approval semantics; "accepts it" is already endorsement-shaped. Force-free means no machinery consumes a fresh attestation as a license.
- The contract file is the gate-side identity, so editing what the attestation means stales every attestation as `gate-changed`.
- Single `human` partition; per-actor partitions only if observation demands them.
- **Explicit byte confirmation over after-the-fact echo:** `commonplace-attest {note} --reviewed-hash {sha}`, hash obtained from a separate show step, failing on mismatch.
- This is the anchored alternative to the `reviewed: true` boolean the README's purpose asks about — friction with it in use is direct evidence on why systems default to unanchored booleans.

Adoption criterion, observable only once a kind exists (which is why it lives here and not in part 3): does the single force-free kind get stretched — the user wanting to record something weaker or stronger, or wanting a fresh attestation to actually license something? Each stretch is a located requirement for the kinds/forces design.

## Explicitly not built (in the MVP)

- Everything in part 4 until its gate says yes — event commands, ack integration, automated control validation, archival generalization, trust-dial operation.
- Footprint enforcement machinery — declared footprints stay stated intent the cumulative diff verifies.
- Any edit-kind taxonomy in the system — edit kinds in the observation record are free-text vocabulary.
- Attestation machinery — part 5 selects a representation; building is post-selection.
- Anchoring for compression, friction, and connect — part 2 re-runs them directly; DB anchoring for them waits until the critique pattern has proven itself.

## Test matrix (part 1 — the only code the MVP ships)

- parser accepts `## Result: REPORT` only for report-kind pairs and rejects it for verdict-kind; rejects `PASS/WARN/FAIL/ERROR` on report-kind pairs
- queued/completed invariants hold for both kinds, including the `result_kind = 'verdict' OR decision IS NULL` CHECK
- `upsert_acceptance` accepts a completed report pair and a completed verdict pair, rejects an incomplete pair of either kind (verdict with `reviewed_at` but NULL decision included)
- freshness classification for critique pairs: `missing-review`, `note-changed`, `gate-changed` (on editing `critique-note.md`)
- warn queue never contains a report-kind pair
- a job creation request mixing result kinds is rejected (packing prevents it; the test asserts the invariant anyway)
- the rendered critique prompt embeds the gate-snapshot instruction text: editing `critique-note.md` after job creation does not change the job's prompt
- a completed report pair writes its result artifact despite `decision = NULL`
- `load_latest_completed_review_pair` and the ack lookup recognize completed report-kind evidence (an ack can carry a report-kind acceptance forward)
- existing verdict-gate flows are behavior-identical (regression: same selector output, same finalization results on a fixture store)
- the migration script upgrades a populated v4 fixture store **including acceptance rows referencing pairs**: `user_version` becomes 5, every pre-existing pair reads `result_kind='verdict'` with its `review_pair_id` preserved, acceptance rows still join to their pairs and freshness classifications are unchanged, `PRAGMA foreign_key_check` is clean, and re-running the script on a v5 store is a refused no-op

Part 2 is instruction + procedure, checked by hand per pass: closing reports land under `closing/` with `initial/` byte-identical, the packet gains its "Closing cycle" section, the observation file covers every assay, and controls leave the review DB and the source run's output untouched.

## What part 3 was intended to observe

Ties to the location criteria in [carry-heuristics.md](./carry-heuristics.md):

- Constraint 1 (direction over size): do flips in the record track edit *direction* rather than diff size? **Unidentified:** the record lacks matched directions and diff-size measurements.
- Constraint 2 (non-compositionality): does an accumulated series of individually-judged edits ever flip a coherence check? **Untested:** no individually accepted sequence existed; all decisions were `would_rerun`.
- Constraint 3's premise: is a declared flow-only step 9 ever caught changing a claim? **Untested:** the cumulative baseline combines steps 8 and 9, so it cannot attribute leakage to step 9.
- Constraint 4: does the one-cycle stopping rule ever leave residual findings that genuinely needed a second round, or does routing to Open items suffice? **Locally answered as policy:** every pass retained residuals and still terminated by routing them; no convergence comparison was run.
- Case 3 flip: does a current-critique signal ever get read downstream as "critiqued and handled"? **Untested:** no downstream misuse protocol was instrumented.
- **Part 4's gate:** the `would_ack` confirmation rate and measured rerun cost. **Did not open:** zero `would_ack` decisions and no usable cost record.

(The case 2 attestation observation lives under part 5's adoption criterion — nothing attestation-shaped exists to observe during the closure runs.)
