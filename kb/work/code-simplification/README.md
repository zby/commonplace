# Code simplification backlog

**Goal.** Cut lines and complexity from `src/commonplace/`, `scripts/` and `tests/` without changing behaviour, by working through the findings below. Posed by the operator on 2026-09-28, after a four-agent read-only review of the package.

**Already done.** Code with no callers, finished migrations, and code only tests reached were removed in 45d6afba, 765df352 and 4150e388 (about 1,950 lines). This backlog is what remains: duplicated code, test clean-up, and design-level changes.

**Closes when** every item below is committed or struck through with a one-line reason. The workshop produces commits, not library artifacts. The exception is a design-level item that changes module ownership: that one gets an ADR (or an amendment to the ADR that owns the boundary). Delete the directory when it closes.

## Conventions

- **Line numbers are as of 4150e388** and will drift. Find the code by the symbol names given.
- **The estimates came from reviewers reading the code.** Confirm each claim before acting on it. Strike an item that turns out wrong, and say why.
- **One commit per item, or a small group of items in the same module.** `uv run pytest` and `uv run ruff check .` must pass before each commit. Each commit carries a `Workshop: kb/work/code-simplification` trailer.
- **Behaviour stays the same**, apart from the bug in item 1, which is fixed deliberately and gets a regression test. Error-message wording may change only when an item says so.
- **Mark progress in this file.** Strike through a finished item and add its commit hash.

## Tier 4 — merge duplicated code

1. **Staleness check written three times (~110 lines).** The shared helper is `freshness/selector.py` `_changed_inputs_for_baseline`. Its UnicodeDecodeError/ValueError and OSError branches have identical bodies, and it builds `ChangedInput` four times. Make it the single implementation:
   - `review/review_target_selector.py` `select_stale_criteria` re-implements the hash comparison; have it call the helper.
   - `review/warn_selector.py` does the same, around its `missing-baseline` handling; have it call the helper too.
   - Deduplicate the diff code: `text_diff_from_text` and the diff in `freshness/status.py`.
   - Deduplicate the JSON output: `_changed_input_payload` and `_changed_input_to_json`.
   - Use `dataclasses.replace` in `_attach_diffs`.
   - **Probable bug:** `warn_selector` builds paths as `repo_root / artifact_path`, so a `commonplace:` library criterion probably always reads as changed. The shared helper resolves paths through `resolve_file_text`, which handles those. Write a failing test first.
   - Its `missing-baseline` branch cannot run: the pair map is built from the baseline view, so every key has a baseline.
2. **`review/review_db.py` boilerplate (~70 lines).**
   - Replace field-by-field row mapping (`_review_job_from_row`, and `FreshnessBaseline` in `load_current_freshness_baselines`) with `Cls(**dict(row))`.
   - Put the job column list, written out twice, into one `_JOB_SELECT` constant, like `_PAIR_SELECT`.
   - Drop `create_job`'s parameters no caller passes: `completed_at`, `failure_reason`, `telemetry_json`.
   - Fold `create_job` and `create_review_pairs` into `create_job_with_pairs`.
   - Have `ReviewJobPlan` reuse `ReviewJobRow` instead of repeating its 11 fields.
   - Remove the `resolve_db_path` and `ensure_db` wrappers; call `store` directly.
   - Replace `ReviewFileSnapshot`, a renamed `ArtifactSnapshot`, with `ArtifactSnapshot`.
   - Inline `_review_pairs_from_rows`.
   - Remove the `DEFAULT_DB_PATH` and `DB_ENV_VAR` aliases.
3. **The ack path checks the same things up to three times (~50 lines).**
   - `acknowledgement.records_from_selector_payload` and `_selected_inputs` both check unique roles and matching reasons.
   - The expected-revision (CAS) check runs in `ack_pairs`, then `transitions.ack_target_inputs`, then `baselines.refresh_review_baseline_from_observation`.
   - The evidence-pair query `SELECT evidence_review_pair_id FROM review_freshness_evidence WHERE target_id` appears in three places.
   - `ack_target_inputs` builds `SupersededFreshnessBaseline` by hand; `review_db._superseded_baseline_for_target` already does this.
   - Hex-hash validation is duplicated between `acknowledgement._content_hash` and `transitions.parse_input_observation`.
4. **`review_target_selector.py` parallel helpers (~30 lines).**
   - Merge `_normalize_type_requests` with `_normalize_collection_requests`, and `_applicable_type_spec_path` with `_applicable_collection_md_path`.
   - `_partition_criterion_requests` evaluates each predicate twice.
   - Merge the two `missing-baseline` appends.
   - `_is_type_definition_content` duplicates `project_paths.is_type_definition_content`.
5. **Six review commands repeat the same boilerplate (~30 lines).** They repeat "strip `--model-partition`, error if empty, normalize", and five places repeat "resolve db path + `ensure_db`". `prepare_review_db` already exists; use it everywhere.
6. **`lib/relocation.py` (~90 lines).**
   - `relocate_note` and `relocate_directory` share the link-rewrite loop and the dry-run/ProperDocs report printing.
   - `rewrite_links_to_moved_files` is `rebase_and_rewrite_in_moved_file` for a file that did not move. Merge them, and keep the `exists()` fallback only for moved files.
   - "Resolve a path and require it under `kb/`" is written three times.
   - `rewrite_source_notes` and `_declared_brief_node` repeat the same frontmatter lookup.
   - Inline the `resolve_note` and `move_path` wrappers.
7. **Python re-checks what the schemas already enforce (~75 lines).**
   - `full_pass.parse_full_pass_report` re-checks enums and closing rules. Have `load_full_pass_report` validate against the schema first, as `agentic_analysis.load_run_state` does, then drop the duplicate checks.
   - `systems_matrix.validate_comparison`: keep only what the schema cannot express (per-axis vocabularies, record resolution, cross-axis rules).
   - `full_pass.guard_input` builds `GuardResult` five times; use `dataclasses.replace`.
   - `GuardResult.to_dict` can be `asdict`.
8. **`cli/validate_notes.py` (~85 lines).**
   - `build_single_validation_report` repeats `build_validation_report`, which gives the same report for a single path.
   - The redirects and landings branches in `main` differ only in the validator called and the subject path; make them one table-driven branch.
   - The three `diagnostics.extend(...)` blocks become one loop.
   - Fold the `== kb → _TOO_BROAD_MESSAGE` check (three copies) into `_collection_target`.
9. **`lib/validation.py` local cleanups (~50 lines).**
   - In `ValidationRun.parse_note`, write the cache once instead of in three places.
   - In `validate`, assign the result once instead of in both `try` and `except`.
   - `inbound_info` maps each key to itself; use `if target in inbound`. It also repeats the target filtering in `_linked_md_targets`.
   - The split of schema errors by severity exists twice (`_validate_artifact`, `apply_schema_validation`).
   - Drop the `isinstance(schema, dict)` re-checks in `_schema_error_message`.
   - Compute the exemption wording in `validate_title_and_slug` once.
   - Use `snapshot.SNAPSHOT_DIR` instead of a hard-coded `kb/sources/.snapshots`.
10. **Shared helpers copied between modules (~120 lines).**
    - "Text under one `##` heading" has six copies: `agentic_records.section`, `lifecycle_validation._section`, `quote_verification.ingest_quotes_section`, `full_pass.resolution_section`, and others. Put one helper in `note_parser`.
    - "Show a path relative to the repo" has four copies (`_display_path` ×2, `_display_snapshot_path`, `quote_verification.display_path`). Put one in `project_paths`.
    - Git subprocess calls: `agentic_publication._git`, `project_status._run_git`, and inline calls in `agentic_analysis`.
    - Atomic write: `agentic_publication.atomic_write` and `validate_notes.emit_json_report`.
    - `_required_string` and `_repo_relative_file` are copied between `agentic_analysis` and `full_pass`.
    - `full_pass._capture_file` re-implements `agentic_set.is_normalized_relative`.
    - `agentic_records._analysis_prose` has its own fence tracker.
    - `TAG_README_TYPE` is defined in both `validation.py` and `index_generated.py`.
    - `x_snapshot` and `github_snapshot` repeat capture writing: dedup, reobserve slug, write, message.
11. **Idiom sweeps (~60 lines).**
    - `try: relative_to / except ValueError` used as a membership test becomes `Path.is_relative_to`. Sites: `validation.py` ×3, `type_resolver.py` ×2, `project_paths.py`, `lifecycle_validation.py`.
    - Absolute-path branches that repeat the repo-relative branch (`repo_root / "/abs"` is `/abs`): `validate_notes.py` target resolution and `project_paths.resolve_note`. `resolve_note` also calls `list_kb_note_paths` twice.
    - `note_parser`: blanking fenced code gives the same matches as removing it, so drop the `blank=False` path.
12. **Wrappers with one caller (~40 lines).** Inline:
    - `canonical_type_identity`, `note_parser.strip_frontmatter`, `_quote_citation_rule`;
    - `run_validation`, `prepare_publication`, `baselines.load_expected_baseline_revision`;
    - `build_generated_section`, and `collect_index_pages`'s `is_root` parameter (derive it from depth).

    Also:
    - `refresh_review_baseline_from_captures` returns `superseded_target_id`, which no caller uses.
    - `finalization.ACTIVE_REVIEW_JOB_STATUSES` is a one-element set.
    - `revisions.allocate_initial_revision` re-runs `load_generation_next_revision`'s query.
    - `freshness/snapshots.py` writes the row→`ArtifactSnapshot` mapping twice.
13. **Smaller items in the agentic modules (~60 lines).**
    - `verify_agentic_analysis_run_state` now always has `run`, so read through `run.read_bytes` and drop `_text_override`, `_read_output_bytes`, `_read_output_text`, `_parsed_output` and the `try: run.read_bytes … except: pass` warm-ups.
    - `load_results` and `agentic_publication._check_incumbent` duplicate the review→retained-set check; move one helper into `agentic_set`.
    - `_load_running_state` re-parses a state that `load_run_state` has already parsed.
    - Nothing imports the re-exports in `systems_matrix.__all__`.
    - `_check_set` rebuilds `retained_set_paths()` inline.
    - `init_project`: `_copy_scaffold_file` and `_write_template` share the same "exists → classify, else write" code.

## Tier 5 — tests (~500 lines)

14. **Shared helpers.**
    - `write(path, content)` has about 30 copies; `tests/commonplace/validation_helpers.py` already has one.
    - `make_note`, `make_gate`, `seed_freshness_baseline`, `db_path_for` and `build_fixture` are copied across `tests/commonplace/review/` and `cli/relocation_review_helpers.py`. Move them to `review/pair_helpers.py` or a `conftest.py`.
    - Byte-identical pairs: `write_type_spec`, `pair_block`, `target`.
15. **Parametrize near-identical test pairs.** Candidates: `freshness/test_integrity.py`, `test_quote_verification.py` (two pairs), `lib/test_agentic_analysis.py`, `review/test_review_outcome_parser.py`, `lib/test_type_resolver.py`, `lib/test_frontmatter.py`, `lib/test_snapshot.py`.

## Design-level — decide before starting

16. **Break the import cycle between `freshness/` and `review_db`.** `freshness/*` imports `FreshnessBaseline`, `SupersededFreshnessBaseline` and `load_current_freshness_baselines` from `review_db`, and `review_db` imports freshness, which forces deferred imports. Move baseline loading, upsert and prune into `freshness/baselines.py`, leaving `review_db` to store jobs and pairs only. This needs an ADR or ADR amendment, because it changes which module owns baselines.
17. **One result type for a stale review target.** `StaleCriterion` and `StaleTarget` describe the same thing, so each has its own renderer and the ack path has its own parser for selector output. Merging them absorbs the rest of items 1 and 3. Do this after item 1.
18. **One implementation of snapshot lookup.** `validation.SnapshotDirectory`/`SnapshotFacts` overlap `lib/snapshot.py` (`dedup_existing_snapshot`, `snapshot_sha256`, the http-source check).
19. **Separate diagnostic types for lifecycle validation.** `LifecycleDiagnostic` and `LifecycleValidationResults` repeat `ValidationDiagnostic`, and the CLI converts every item from one to the other.
20. **Rows of checks in `project_status._actions`.** Its ~120 lines could become a table of (condition, id, severity, message, command) rows.
21. **Three scripts over the systems matrix.** `build_systems_matrix.py`, `render_systems_table.py` and `analyze_matrix.py` are thin wrappers over `systems_matrix.load_results`; they could become one script with subcommands. They are live and are referenced from `kb/agentic-systems/comparisons/README.md`.
22. **`scripts/session-tools.py`.** Delete it only if nobody runs it by hand; ask the operator.
