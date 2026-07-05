# Review system code audit — 2026-07-05

Audit of `commonplace.review` + `commonplace.cli.review` (~5,000 lines) for bugs, simplifications, and architectural improvements. Baseline: all 317 tests pass. Two findings are confirmed with reproductions; the rest are code-reading findings. Closes when the confirmed bugs are fixed and the simplification list is triaged into fixes or explicit won't-fixes.

## Confirmed bugs

### B1. `_RESULTISH_LINE_RE` + `re.IGNORECASE` fails whole jobs on any bare word line

`src/commonplace/review/protocol/decisions.py:11-16`. The guard regex's last branch `(?:\*\*)?(?:PASS|WARN|FAIL|ERROR|[A-Z]{2,})(?:\*\*)?\s*$` is compiled with `re.IGNORECASE`, so `[A-Z]{2,}` matches **any** all-letter word of ≥2 characters alone on a line — `none`, `ok`, `Approved`, `Summary`. `parse_review_decision` then raises `invalid result signal`, and finalization fails the entire job (all pair decisions nulled, worker output discarded).

Reproduction: a review body with a valid `## Result: PASS` footer plus the line `none` under `### Suggested Revision` raises `invalid result signal: none`. The prompt template invites exactly this — `### Suggested Revision` / `<optional; omit if not needed>` makes a worker writing `none` realistic.

Fix: keep case-insensitivity only for the alias branches (`Verdict:`, `Outcome:`, …) and make the caps-word branch case-sensitive — e.g. wrap alias branches in `(?i:...)` inline groups and compile without the global flag, or use two regexes. Consider also narrowing the guard's scope to the tail of the block (after the last section heading) so prose can never fail a job.

### B2. Derived result paths are unstable under superseded-pair pruning

Result filenames are derived from the job's **current** pair set: for gate packing, `_note_filename` (`src/commonplace/review/artifacts.py:79`) uses the plain basename when it is unique across the job's notes and the `__`-encoded full path otherwise. Inline pruning (`prune_superseded_acceptances`) deletes superseded pair rows out of completed jobs. When a gate-packed job contained two notes with the same basename and one pair is later superseded, the surviving pair's derived `result_path` silently changes from the encoded name (what was written to disk) to the bare basename (which does not exist).

Reproduced end-to-end: gate-packed job over `kb/notes/x/sample.md` + `kb/notes/y/sample.md`; after re-reviewing only the first note, the surviving pair's derived path became `.../review-job-1/sample.md` while the disk still holds `kb__notes__y__sample.md`. Downstream, `warn_selector._load_review_text` returns `None` and the pair's warn findings silently vanish; the stale job-1 `MANIFEST.json` is never refreshed either.

Fix options, in order of preference:

1. Make result filenames a pure function of the single pair (always encode the full note path in gate packing; encode the gate path in note packing) — stable under pruning, keeps the ADR-035 derived-paths decision intact.
2. Refuse to prune pairs from jobs that still carry accepted sibling pairs.
3. Re-store result paths (reverses the phase-2 decision in `kb/work/review-system-simplification/`; not recommended).

Note the note-packing analog: `result_filename` uses the bare gate basename with no collision handling at all. The CLI's grouping-by-bundle makes collisions impossible today, but `prepare_grouped_review_job` is a library API and nothing in `artifacts.py` enforces the assumption. Option 1 fixes both sides.

## Likely bugs / robustness gaps (not reproduced, from code reading)

- **Two clocks, string-ordered timestamps.** `clock.iso_now()` stamps local time with offset; `review_db._now_utc_iso()` stamps UTC (snapshots). `load_latest_completed_review_pair` orders by `reviewed_at DESC` and `warn_selector` picks the newest review by string comparison — ISO strings with different UTC offsets do not sort chronologically (DST transitions, machines in different timezones sharing a store). Standardize on one UTC clock helper.
- **Queued job with no prompt on write failure.** In `prepare_grouped_review_job` (`batch.py`), only `ValueError` from `render_pairs_prompt` fails the job. An `OSError` from `mkdir`/`write_text` propagates after the job row is committed, leaving a permanently queued job with no prompt artifact and no failure record. The create-jobs CLI loops over groups, so a mid-loop failure also leaves earlier jobs created but unreported (`parser.error` output says nothing about them).
- **`_targets_for_pairs` trusts `packing="note"` blindly.** With packing `note` it takes `pairs[0][0]` as the single note; a library caller passing mixed notes gets DB pairs for all notes but a prompt for only the first — guaranteed `missing pairs` failure at finalize. Cheap to validate at entry.
- **`attach_execution_data` edge behavior.** Effort-without-model raises `ValueError` outside the finalization `try` (CLI guards it; library callers crash with a traceback instead of a failed outcome). Missing job silently returns in one branch and silently no-ops in the other.
- **Partial result files on finalize failure.** `write_pair_result_files_to_derived_paths` failing mid-write leaves already-written result files on disk for a job marked failed. The refreshed failed manifest makes this discoverable, so low priority.

## Simplifications

- **Dead code:**
  - `artifacts.encode_stage_filename` — no callers.
  - `artifacts.write_pair_result_files` — no callers (only `..._to_derived_paths` is used).
  - `review_db.load_completed_review_pairs_for_job` — no callers.
  - `require_paths` parameter — threaded through `load_review_job_plan` / `list_review_job_plans` / `_job_plan_from_job` and explicitly ignored (`_ = require_paths`).
  - `ParsedPairBundle.canonical_markdown` + `rewrite_pair_result_footers` — computed on every finalize, consumed only by one test.
  - `review_db.load_review_pairs_for_note` — used only by relocate tests, not by production code.
  - `snapshot_file`'s `UPDATE ... WHERE content_text IS NULL` branch — nothing inserts NULL text, and the store is recreated rather than migrated.
- **`has_only_unwatched_changes` (`ack_trivial_note_changes.py:95`).** After the watched-key loop returns `False` on any watched change, `changed_keys` can only contain unwatched keys, so `changed_keys - watched_keys == changed_keys` and the final expression reduces to `bool(changed_keys)`. Separately, a semantic gap: a note whose hash changed but whose parsed parts are all equal (trailing whitespace, blank-line, frontmatter-formatting churn) returns `False` — the *most* trivial changes are the only ones the trivial-ack sweep cannot ack, and they stay stale until a manual `commonplace-ack-gate-review`. Decide intent; if such changes should ack, return `True` for the all-equal case.
- **`warn_selector.scan_reviews`** runs `extract_warns` twice per selected review (once to pre-filter, once to emit) and re-checks `review.decision is None` after selection already required it. One pass storing extracted warns is simpler and halves the regex work.
- **`create_review_jobs` CLI** loads **all** job plans (each an extra pairs+paths query) and filters to the just-created ids; `load_review_job_plan` per created id is direct. `_job_payload` also sorts `plan.pairs` twice.
- **`select_stale_gates`** recomputes the note's SHA-256 (full file read) once per gate instead of once per note; with `--all-gates` that is ~gate-count redundant reads per note. Same for `applicable_gate_ids_for_note`, which re-reads every gate's frontmatter for every note (N×G file reads per selector run) — a per-run gate-metadata cache removes it.
- **Five variants of repo-relative path validation** — `review_db.snapshot_file` (inline), `acknowledgement._normalize_note_path`, `artifacts.repo_relative_path`, `paths._reject_unsafe_relative`, `resolve_gates._reject_unsafe_gate_arg`. One shared helper with a `label` argument covers them all.
- **Gate frontmatter key inconsistency**: `requires_trait` (underscore) vs `requires-type` (hyphen), mirrored in `resolve_gates.applicable_gate_ids_for_note`. Works, but is an authoring landmine; converging needs a small data migration plus the code change.

## Architectural observations

- The core shape is sound and matches `kb/reference/review-architecture.md`: canonical SQLite state, derived artifacts, thin CLI wrappers, a single finalization seam, and the two-input freshness hash with a clearly commented boundary. Nothing here argues for restructuring.
- B2 is the one place where the phase-2 "derive, don't store" decision leaks: derived paths are only safe if derivation inputs are immutable, and inline pruning mutates them. Making filenames pair-local (fix 1 above) restores the invariant instead of reversing the decision.
- The strict result-line protocol pushes all leniency out of the parser, which is right for canonical state — but B1 shows the guard heuristics can exceed their mandate. Guards that can fail a whole job deserve their own tests over realistic prose bodies.
- Timestamps deserve one owner. `clock.iso_now` (local) vs `_now_utc_iso` (UTC) is invisible until two rows are compared lexically.

## Suggested order of attack

1. B1 regex fix + prose-body regression tests (small, high value).
2. B2 pair-local result filenames (drops `_note_filename`, the `all_note_paths` plumbing, and the note/gate asymmetry — a net simplification that also fixes the bug).
3. Unify clocks on UTC.
4. Dead-code sweep (mechanical).
5. Remaining robustness and efficiency items as touched.
