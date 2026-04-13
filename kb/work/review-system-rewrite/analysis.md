# Structural analysis of the current review system

## Size

~5,800 lines across ~30 files. Library: ~4,300 lines (14 modules). CLI wrappers: ~1,500 lines (18 modules).

## Module-by-module

### review_db.py (910 lines) — the monolith

What it does: SQLite connection management, all CRUD for the four-table execution/review model (`review_runs`, `review_run_gates`, `gate_reviews`, `acceptance_events`), plus high-level finalization orchestration.

Tangles:
- **Finalization logic baked into DB layer.** `record_and_finalize_run` validates gate coverage, rekeys the model ID if actual differs from requested, and auto-appends acceptance events. These are business rules that should be orchestration, not persistence.
- **`load_effective_gate_review_map` is a query god** (~60 lines of CTE logic). Serves both "which acceptance to prioritize" and "latest review regardless of acceptance". Called by warn_selector but duplicates freshness filtering the selector does independently.
- **Two finalization paths** (`complete_review_run` vs `fail_review_run`) both update the same row via raw SQL with no application-level guard against concurrent calls.

### run_review_bundle.py (536 lines) — bundle orchestrator

What it does: coordinates single-note multi-gate review — target resolution, prompt construction, runner invocation, output parsing, artifact writing, DB finalization.

Tangles:
- **Output parsing spans three modules.** Sentinel extraction here, decision regex in review_decisions.py, footer rewriting in review_decisions.py. The LLM output contract has no single owner.
- **Error handling across 3 catch blocks** with separate DB reconnections. Failures at different stages are handled differently.
- **Prompt construction reads from disk** (gates, note content, resolved links) without transactional guarantee against concurrent gate changes.

### run_gate_sweep.py (405 lines) — gate-sweep orchestrator

What it does: selects stale notes for one gate, batches them, invokes runner once per batch, parses and finalizes per-note.

Tangles:
- **Two runner paths fork early.** `persist_runs=False` uses fake ordinal IDs without DB records; `True` creates real records. Downstream code can't tell which mode is active.
- **Per-note finalization inside loop.** If finalization fails on note N, earlier notes are committed, later ones marked failed. No batch transaction.
- **Near-duplicate of run_review_bundle pipeline** with different input shape.

### review_runners.py (774 lines) — subprocess invocation

What it does: spawns claude-code or codex CLI, captures stdout, extracts telemetry from session logs and stream events.

Tangles:
- **Telemetry extraction is 400+ lines of runner-specific conditional logic.** Claude has 6 event sources; codex has a different session log format. No abstraction for "query telemetry from runner output."
- **Session log matching is a fragile heuristic** — searches by matching prompt text line-by-line, filtered by mtime window.
- **`run_prompt` does too much:** spawns process, threads for piping, accumulates chunks, searches session logs, loads telemetry, returns result. No intermediate validation.

### review_decisions.py (335 lines) — decision parsing

What it does: parses review decisions from freeform text using 19 regex patterns tried in order.

Tangles:
- **Order-dependent regex chain.** First match wins. Patterns overlap. Reordering silently changes behavior.
- **Two parsing codepaths.** `_extract_declared_review_decision` (runtime) vs `infer_manual_import_review_decision` (legacy import with special fallback). Duplicated logic, different semantics.
- The order-dependency is acceptable given that this is a best-effort parser for fuzzy LLM output (see constraint 5 in README). Over-engineering this is counter-productive.

### review_target_selector.py (278 lines) — freshness

What it does: loads current acceptances, compares note/gate SHAs, classifies staleness.

Tangles:
- **Gate applicability check is buried mid-loop** rather than pre-filtered.
- **Freshness filtering duplicated** with warn_selector (same SHA comparison, different output contract).
- **`note_diff_since` is expensive and all-or-nothing.** Must decide upfront whether diffs are needed.

### review_metadata.py (292 lines) — git provenance

What it does: git-backed provenance (blob_sha, commit, file_text_at_commit) plus ReviewMetadata block parsing for legacy review export files.

Tangles:
- **Dual-path provenance.** `review_note_provenance` allows uncommitted state; `committed_file_provenance` forbids it. Callers must know which to use. Silent misuse causes SHA mismatches downstream.
- **ReviewMetadata parse/render is now relocation-export support, not dead code.** The base code-structure rewrite moved review export metadata rewriting into `commonplace.review.relocation_hook`, which calls `parse_review_metadata` and `inject_review_metadata` when note paths change. This is scar tissue from review exports, but it is active scar tissue until exports are retired or migrated.

### relocation_hook.py (202 lines) — downstream relocation integration

What it does: implements the core relocation hook protocol for review-owned state. It plans review export directory moves, rewrites ReviewMetadata note paths in exported review files, and rekeys review DB rows after core file/link/MkDocs relocation succeeds.

Tangles:
- **Cross-subsystem adapter.** This is intentionally not part of `commonplace.lib`: core relocation exposes `RelocationHook`, and the CLI composes `ReviewRelocationHook`. The rewrite must preserve this dependency direction.
- **Post-core partial failure boundary.** Hook execution happens after core relocation writes. If review export moves or DB rekeys fail, the core note move has already happened. That failure mode is acceptable but must remain explicit in the integration design.
- **Persistence bypasses future repos.** The hook currently calls `review_db` functions directly. In the target structure, this should use the persistence/repo layer's note-path rekey operation rather than raw review_db helpers.

### gate_sweep_format.py (287 lines) — sweep output parsing

What it does: parses gate-sweep batch output (NOTE sentinels wrapping GATE sentinels).

Tangles:
- **Code duplication with bundle parsing.** Outer loop is duplicated; inner gate block reuses `extract_bundle_reviews`. If bundle format changes, sweep may break independently.

### ack_trivial_note_changes.py (229 lines) — auto-ack

What it does: compares note text at acceptance time vs current, checks if changes are in unwatched fields.

Tangles:
- **Previous-text retrieval is fallback-heavy** — tries git blob at commit, then falls back to time-based heuristic search.
- **Whitespace/frontmatter normalization is ad-hoc.** No spec for what "normalized" means.

### warn_selector.py (207 lines) — warn queue

What it does: finds warn-decision reviews, extracts actionable findings via regex.

Tangles:
- **Finds structure in unstructured markdown** using hardcoded regexes for "### Findings" and "- warn: ...". If reviewers deviate, warnings are missed.
- **Freshness filtering duplicated** from review_target_selector (has a TODO noting this).

## Cross-cutting concerns

### Review/core integration (new boundary)

The base code-structure rewrite removed the old direct dependency from `commonplace.lib.relocation` to `commonplace.review`. Review-specific relocation behavior now lives in `commonplace.review.relocation_hook`.

This changes the review rewrite baseline:
- Review path rekeying is no longer hidden inside core relocation.
- Review export metadata parsing has an active caller.
- The review system owns its own integration adapters for core workflows.
- Any future rewrite must keep `commonplace.lib` review-free and wire review hooks only at CLI/composition boundaries.

### Prompt construction (scattered)

- `run_review_bundle.py`: `build_review_run_prompt` — reads note, resolves links, builds gate prompt.
- `gate_sweep_format.py`: `build_gate_sweep_prompt` — near-identical link resolution, different batching wrapper.
- Both construct "resolved links" sections independently. If the output contract changes, touch two files.

### Output parsing (three-module pipeline)

1. Runner returns raw stdout (review_runners.py)
2. Sentinel extraction: bundle sentinels (run_review_bundle.py) or NOTE+GATE sentinels (gate_sweep_format.py)
3. Decision parsing: regex chain (review_decisions.py)

No single module owns the LLM I/O contract end to end.

### Git provenance (scattered)

Five modules call provenance functions independently. No batch-loading, no caching. Each call site passes `(sha, commit)` as separate arguments or tuples.

### Runner output boundary (ad hoc)

Subprocess is implemented in review_runners.py. Live-agent is a separate command sequence (create-review-run + agent follows prompt + ingest-bundle-output). The problem is not primarily that each runner lacks its own module; the problem is that orchestration lacks a narrow shared result shape and resume boundary.

### Bundle vs gate-sweep duplication

| Concern | Bundle | Gate-sweep |
|---------|--------|------------|
| Prompt build | run_review_bundle | gate_sweep_format |
| Output parse | run_review_bundle | gate_sweep_format (wraps bundle parser) |
| Finalization | one call to record_and_finalize_run | per-note loop calling record_and_finalize_run |
| Artifact write | write_bundle_artifacts (once) | write_bundle_artifacts (per note) |

Same artifacts written via different code paths. Same finalization called with different arguments from different orchestrators.

## CLI layer

Most wrappers are thin (~50 lines). Exception: **cli/review_sweep.py (231 lines)** contains selection logic, job grouping, ThreadPoolExecutor driver, and env-var parallelism parsing. This is orchestration in CLI clothing.

## Dead code / scar tissue

- `ReviewMetadata` parse/render in review_metadata.py — active only for review export relocation. Keep it quarantined with export-management code; do not treat it as general provenance.
- `review_run_gates.ordinal` column — used only for deterministic run-gate ordering during ingest/finalization; not part of freshness semantics.
- Legacy decision regex patterns in review_decisions.py — support import formats that may no longer be produced.
