---
description: "Proposal: collapse the two divergent review execution paths (multi-gate single-note bundle, single-gate multi-note sweep) onto one (note, gate)-pair grammar with one executor, demoting batching to a packing strategy over pairs rather than a distinct protocol"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# Unify review bundling around (note, gate) pairs

The review subsystem runs the same logical unit of work — review one note against one gate, emit a decision keyed by `(note_path, gate_id)` — through two divergent execution paths with two prompt grammars, two parsers, and two packing strategies. This proposal collapses both onto one pair grammar driven by a single executor, leaving *how many pairs ride in one LLM call* as a packing decision rather than a protocol fork. The data model already speaks in pairs: `gate_reviews` is keyed by `(review_run_id, note_path, gate_id)` and `review_target_selector` emits `(note, gate)` staleness pairs. The duplication is confined to the prompt/parse/orchestrate layers above that model.

## Current state (as of 2026-06-12)

Two execution paths exist, each a full prompt → parse → finalize pipeline:

- **`run_review_bundle` (multi-gate, single-note).** One note, many gates, one LLM call. Prompt rendered by `render_bundle_prompt`; output delimited by `=== GATE REVIEW START/END: {gate-id} ===`; parsed by `extract_bundle_reviews` (`BUNDLE_START_RE`/`BUNDLE_END_RE`). This path also owns the live-agent entry points (`create-review-run --with-prompt` → agent writes `bundle-output.md` → `ingest-bundle-output`).
- **`run_gate_sweep` (single-gate, multi-note).** One gate, many notes, batched at `--batch-size` (default 5) per LLM call. Prompt rendered by `render_sweep_prompt` over `GateSweepNoteTarget`s; output delimited by `=== NOTE START/END: {note_path} ===`; parsed by `extract_gate_sweep_reviews` (`NOTE_START_RE`/`NOTE_END_RE`).
- **`review_sweep` (orchestrator).** Selects stale `(note, gate)` pairs via `select_stale_gates`, groups them into per-note `SweepJob`s, and fans them out across `run_bundle` in parallel worker threads (`DEFAULT_PARALLELISM = 4`). It is a batching layer on top of the first path, not a third grammar.

Shared below the fork: `record_and_finalize_run` (writes `gate_reviews`, validates coverage, completes the run, appends acceptance events), the `review_db` data layer, `resolve_gates`, `review_target_selector`, and `review_metadata` provenance. `run_gate_sweep` already imports nine helpers out of `run_review_bundle`, which is evidence the split is incidental rather than essential.

The two parsers also carry near-identical twins: `rewrite_bundle_result_footers` and `rewrite_gate_sweep_result_footers` differ only in which sentinel they scan for. The clearest symptom of the missing pair key is `build_note_local_bundle` in `run_gate_sweep`: after extracting a per-note review from sweep output, it re-renders that review as a synthetic single-note bundle and re-parses it with `parse_bundle_gate_reviews` — a parse → render → parse round trip whose only purpose is to reach the bundle path's finalize tail.

The failure policies have also diverged. Usage-exhaustion detection (`UsageExhausted`) exists only in the bundle path; `KeyboardInterrupt` handling exists only in the sweep path. Parsing is all-or-nothing per call: one missing or malformed block raises, and the sweep path then fails every remaining run in the batch — including pairs whose reviews were already successfully extracted into `parsed_reviews`.

The sweep commands (`review_sweep`, `run_gate_sweep`, `gate_sweep_format`, `ack_trivial_note_changes`) are flagged experimental in [review architecture](../review-architecture.md) — interfaces explicitly subject to change — so this consolidation lands inside the part of the system already marked unstable.

## The problem

The unit of review is the `(note, gate)` pair. Both paths exist only because they chose different *axes to hold constant* when packing pairs into one LLM call: the bundle path fixes the note and varies the gate; the sweep path fixes the gate and varies the note. That choice is a packing strategy — which pairs share a call to amortize the note text or the gate definition — not a difference in the work being done. Encoding it as two grammars means every change to the pair protocol (a new decision field, a provenance column, a sentinel escape rule, a coverage-validation tweak) must be made and tested twice, and the live-agent path only exists for one of the two.

This is the [separate-selection-from-joint-reasoning](../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) shape: *which* pairs to review and *how to pack* them into bounded calls are scheduler concerns that should sit above a single executor, not be welded into the executor's grammar.

The cost of the fork grows with autonomy. An autonomous maintenance loop runs many small checks because small checks are the reliable ones, and learns which gates earn their keep from per-pair decision statistics. That regime multiplies both the number of batched calls (so per-call overhead and partial-failure handling dominate cost) and the number of protocol variants any policy change must touch. The per-pair statistics themselves are already safe — `gate_reviews` and `acceptance_events` key on `(note, gate, model)` regardless of how calls were packed — but the execution layer above them currently pays the duplication tax on every change.

## Proposed design

One grammar, one executor, batching as a strategy parameter.

### One pair grammar

A single sentinel pair delimits one reviewed pair regardless of how the surrounding call was packed:

```
=== PAIR REVIEW START: {note_path} :: {gate_id} ===
### Summary
...
### Findings
- <severity>: <finding>
### Suggested Revision
<optional>
## Result: PASS|WARN|FAIL|ERROR
=== PAIR REVIEW END: {note_path} :: {gate_id} ===
```

Both current grammars are special cases: a single-note bundle is N pairs sharing one `note_path`; a single-gate sweep batch is N pairs sharing one `gate_id`. The parser keys every block on the full `(note_path, gate_id)` it carries, so it no longer needs to infer the missing axis from prompt context. One parser, one footer-rewriter, one coverage check.

### One executor

A single `run_pairs(pairs, *, runner, model, ...)` library function: render the prompt for an arbitrary set of pairs, invoke the runner, parse pair blocks, and hand the keyed results to the existing `record_and_finalize_run`. The current three entry points become thin callers that differ only in *which* pairs they hand in and *how they group them*, not in protocol. The live-agent path (`--with-prompt` / `ingest-bundle-output`) generalizes for free, because it consumes the same pair grammar instead of being wired to the bundle-only sentinels.

The executor owns one failure policy, replacing the per-path divergence. Parsing salvages rather than aborts: every pair block that parsed is finalized, and only the missing or malformed pairs are failed — and, optionally, re-asked in a follow-up call carrying just those pairs. At many-small-checks scale this is the larger efficiency win: today a ten-pair call with one bad block discards nine good reviews. Usage-exhaustion detection and interrupt handling likewise live once, in the executor, instead of one apiece in the two paths.

### Batching as a packing strategy

The grouping decision — pairs-per-call and which axis to share — becomes an explicit policy over the flat pair list the selector already produces, not a property baked into the path:

- **share-note** (today's bundle): group pairs by `note_path` to amortize note text across its gates.
- **share-gate** (today's gate sweep): group pairs by `gate_id` to amortize a gate definition across notes; cap each group at a batch size.
- **parallelism**: the `review_sweep` thread-pool fan-out becomes orthogonal — a knob over groups, available to any packing strategy, rather than tied to the share-note path alone.

The packing strategy is chosen by the caller for cost reasons (which text is expensive to repeat, how large a call the model handles well), exactly the packing/scheduling trade-off in [decomposition heuristics for bounded-context scheduling](../../notes/decomposition-heuristics-for-bounded-context-scheduling.md). It does not change the recorded result for any pair.

## Free choices

- **Sentinel syntax for the composite key.** `{note_path} :: {gate_id}` versus two nested sentinels (an outer note frame containing gate blocks, or vice versa). A flat composite key is simplest to parse but must escape a separator that could appear in a gate id; nested sentinels avoid the separator but reintroduce two block levels. Note ids and gate ids are both path-like, so the separator must be chosen to not collide.
- **Whether one call may mix shared axes.** A fully general packer could place arbitrary pairs in one call (some sharing a note, some a gate). Permitting this maximizes packing freedom but complicates the prompt (no single repeated header to amortize) and weakens the cost rationale. The conservative version keeps each call single-axis and treats the strategy as a choice of axis, not free mixing.
- **Where the packing policy lives.** A parameter on the executor, a separate planner that returns groups, or strategy objects. A separate planner keeps the executor ignorant of grouping (cleaner selection/packing/execution split) at the cost of one more seam.
- **Migration shape.** Build the unified executor and reimplement the three callers on top, then delete the old grammar; or keep both grammars behind the new key until the parser is proven, then remove. No external consumers and the experimental flag favour the direct cut.

## Risks

- **Prompt economy regression.** A flat per-pair header repeats the shared axis (note path or gate id) on every block. If a packer naively emits the full note text per pair instead of once per group, the share-note case loses its whole reason to exist. The executor must still hoist the shared, expensive material (resolved note markdown, gate definitions) to the group header even though the result sentinels are per-pair.
- **Coverage validation across mixed shapes.** `record_and_finalize_run` validates that every expected pair came back. The expected-set construction must be derived from the pairs handed to the executor, not re-inferred per grammar, or a packing bug could silently drop a pair.
- **Live-agent prompt churn.** Generalizing the sentinels changes the canonical prompt that the live-agent path writes to `prompt.md`. Any in-flight `bundle-output.md` artifacts under the old grammar would not parse under the new one — acceptable given no durable consumers, but the cutover must not strand a half-finished run.
- **Loss of a debugging affordance.** Two named paths make logs self-describing ("this was a gate sweep"). A single executor with a strategy parameter must surface the strategy in run telemetry so a reader can still tell how a run was packed.

## Open questions

- Does `run_gate_sweep`'s nine-helper import from `run_review_bundle` already mark the natural seam, such that the unified executor is mostly a rename plus a parser merge rather than a rewrite?
- Should packing be recorded as run provenance (strategy, a batch id, and batch size on `review_runs`)? Runner telemetry is per LLM call, so per-pair cost can only be amortized if a run knows what shared its call; recording it would also let a later analysis compare share-note vs share-gate cost and quality.
- Does the live-agent path want a packing strategy at all, or does an interactive agent always review one note's pairs at a time (share-note, batch size = all its gates)?
- Should the [gate-learning loop](./gate-learning-from-accepted-edits.md)'s per-gate precision/recall accounting prefer one packing axis (share-gate makes per-gate batches the natural accounting unit)?

---

Relevant Notes:

- [decomposition heuristics for bounded-context scheduling](../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) — rationale: batching is a packing/scheduling choice over a unit of work, separable from the executor that does the work
- [review architecture](../review-architecture.md) — part-of: the shipped review subsystem whose two execution paths this proposal would unify
- [gate learning from accepted edits](./gate-learning-from-accepted-edits.md) — see-also: an adjacent undecided extension to the same review subsystem; its per-gate accounting interacts with the packing axis
