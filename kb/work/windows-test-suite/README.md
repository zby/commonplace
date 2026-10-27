# Windows test suite

## Commission

Posed by the operator on 2026-10-27. Make the full test suite (`uv run pytest -m ''`) pass on native Windows, then run it in CI on `windows-latest`. Several failures are real Windows bugs in Commonplace, not test artefacts. The work was split from [windows-install](../windows-install/README.md), which covers installing and starting the commands; this workshop covers whether the code and its tests behave correctly once running.

**Closes when** the full suite passes on Windows locally and in CI, with the pytest step in `.github/workflows/ci.yml` no longer Linux-only. Each failure below is fixed or skipped on Windows with a recorded reason. Then mark E1 item 7's pytest part done in [e1-windows-execution.md](../execution-channel-compatibility/e1-windows-execution.md), delete this directory and its entry in `kb/work/README.md`. The workshop produces commits, not library artifacts. The exception is a decision that changes a cross-platform contract, such as which path separator command output uses; that gets an ADR or an amendment to the ADR that owns the contract.

## Coordination

- **Workjig:** another agent is making Workjig Windows-compatible (as of 2026-10-27). Do not patch Workjig here. Commonplace's own `fcntl` imports are this workshop's work.
- **windows-install:** owns the install procedure, shims and `commonplace-init`'s installation warning. A fix there that also fixes a test here is recorded in both.
- **E1** in [execution-channel-compatibility](../execution-channel-compatibility/e1-windows-execution.md): owns skills and shell snippets on Windows. This workshop takes over E1 item 7's pytest part.

## Conventions

- Follow `AGENTS.md` and [tests/README.md](../../../tests/README.md). Do not weaken assertions or isolation to make a test pass on Windows. Fix the code when the behaviour is wrong on Windows. Fix the test when only its expectation is platform-specific. Skip on Windows only when the feature truly cannot work there, and say why in the skip reason.
- Every fix must keep Linux passing. Run the affected suites on Linux, or rely on CI, before marking an item done.
- One commit per item, or per small group in the same module. Commits carry `Workshop: kb/work/windows-test-suite`.
- Mark progress here: strike through a finished item and add its commit hash.
- Test names below are as of commit `aad4a69d7`. Causes come from one-line tracebacks; confirm each before fixing.

## Running the suite on Windows

From Git Bash, not PowerShell: Windows PowerShell 5.1 drops the empty `''` argument, and pytest then rejects `-m`.

```bash
UV_CACHE_DIR='C:\Users\<user>\.cache\uv' uv run --python 'C:\Program Files\Python314\python.exe' pytest -m '' -q -p no:cacheprovider --continue-on-collection-errors
```

- `--python`: without it uv may choose 3.15, where pyyaml has no wheel and the build needs MSVC.
- `UV_CACHE_DIR`: inside the Claude desktop app uv's default cache is in the app's virtualised `AppData`. That path exceeds the Windows path limit and uv fails with `Trivial strip failed` ([windows-install](../windows-install/README.md), problem 9).
- `--continue-on-collection-errors`: until item 1 is done, six modules fail to import.

Baseline on 2026-10-27, Windows 11 Home, Python 3.14.7, checkout with `core.autocrlf=true`: 795 passed, 47 failed, 11 skipped, 6 collection errors.

## Backlog

### 1. Unix-only `fcntl` locking

`fcntl` does not exist on Windows. Importing it fails, so whole modules fail to load, including `commonplace-task` and `commonplace-analysis` themselves.

- Commonplace imports: `src/commonplace/lib/agentic_analysis/effects.py`, `src/commonplace/lib/agentic_analysis/worktree.py`, `src/commonplace/headless/jobs.py`, `scripts/sync_x_likes.py`, `tests/commonplace/agentic_analysis/test_publication_locking.py`.
- Workjig import: `workjig/run.py`; waits for the Workjig fix.
- Needs one cross-platform lock helper (for example `msvcrt.locking` on Windows), not five local fixes.
- Collection errors: `tests/commonplace/agentic_analysis`, `comparison/test_build_systems_matrix.py`, `comparison/test_comparison_consumers.py`, `headless/test_jobs.py`, `headless/test_tasks.py`, `sources/test_sync_x_likes_script.py`.
- Failures: `docs/test_command_catalogue_integrity.py` (`commonplace-analysis`, `commonplace-task` help), `comparison/test_historical_coverage.py::test_working_or_draft_artifact_cannot_borrow_retained_byte_permission[True]`, `comparison/test_systems_matrix.py::test_mixed_strength_and_partial_coverage_preserve_only_supported_positives`, and `docs/test_properdocs_hooks.py`: `test_site_current_list_matches_comparison_population`, `test_lens_listing_links_each_current_member`.

### 2. Backslashes written into Markdown links (real bug)

Relocation writes links such as `[def](..\notes\definitions\d.md)`. Markdown links must use `/` on every platform. Probably a relative path built with `os.path`/`Path` and rendered with `str()` instead of `as_posix()`.

- `relocation/test_relocate_directory.py`: `test_relocate_directory_apply_moves_and_rewrites`, `test_relocate_directory_moves_hidden_payload_without_inspecting_it`.
- `relocation/test_relocate_note.py`: `test_rewrite_links_to_moved_files_updates_real_links_only`, `test_relocate_note_apply_moves_file_with_to_directory`, `test_relocate_note_apply_moves_note_across_kb_collections`, `test_relocate_note_dry_run_reports_brief_without_moving`.
- Check other link writers for the same pattern.

### 3. Backslashes in repository paths in messages, JSON and navigation

Repository-relative paths are printed as `kb\notes` instead of `kb/notes`. Decide once whether command output, JSON and site navigation always use `/` for repository paths (likely, since they are identifiers that also appear in links and on Linux), then fix the code, not the tests.

- `docs/test_collection_landing_integrity.py` (2 tests).
- `docs/test_properdocs_hooks.py::test_on_config_omits_unpublished_report_collection` (`notes\README.md` in the site navigation).
- `validation/test_directory_artifact.py::test_cli_json_counts_artifact_once_and_locates_member_failure`.
- `validation/test_validate_notes.py`: `test_validate_collection_structure_flags_nested_collection`, `test_source_snapshot_cache_warns_about_redundant_alternate_copy`, `test_source_collection_validation_prints_local_snapshot_warning`, `test_validation_json_is_compact_and_structured`, `test_source_snapshot_cache_reports_same_url_as_related_observation`, and probably `test_note_target_also_validates_marked_tag_readmes`.
- `validation/test_validation_scope.py::test_recent_drilldown_keeps_collection_scope`.
- `sources/test_quote_verification.py` (3 tests) and `sources/test_quote_generation.py` (2 tests): probably the same; confirm.

### 4. Symlinks need a privilege

Creating a symlink fails with `WinError 1314` unless Developer Mode is on or the process is elevated. All four are test setup.

- `general/test_collection_resolution.py::test_resolve_collection_rejects_missing_noncollection_and_external_targets`
- `installation/test_init_project.py::test_init_and_check_resolve_the_library_from_the_project_root`
- `installation/test_init_project.py::test_init_project_preserves_symlinked_skill_directories`
- `validation/test_directory_artifact.py::test_symlink_member_fails`

Options: skip when symlinks cannot be created, with that reason; or rewrite setups that only need a second directory. Do not require Developer Mode for the suite. Framework-delivery decided that nothing is linked on Windows.

### 5. Line endings (probable)

This checkout has `core.autocrlf=true`, so tracked files are CRLF on disk. Not confirmed as the cause of:

- `comparison/test_historical_coverage.py::test_real_allowlist_pins_exact_unchanged_publications`: content hash differs from the pinned one.
- `validation/test_full_pass_validation.py` (6 tests): "resolution projection: body section does not match canonical frontmatter rendering".
- `sources/test_quote_matching.py` (2 tests).
- `installation/test_init_project.py::test_init_project_creates_core_layout_and_is_idempotent`: an unexpected `.template` entry; may be a separate cause.

Confirm first, for example by re-running in a checkout with `core.autocrlf=false`. Then decide between a `.gitattributes` rule (`* text=auto eol=lf` or narrower), and code that normalises line endings before hashing or comparing. Users' KBs on Windows will have CRLF files too, so the code may need to handle them whatever the checkout does.

### 6. One-off failures

- `tooling/test_scan_tool_failures.py::test_unicode_separators_are_not_record_boundaries`: `UnicodeEncodeError` printing `\u2028` to a cp1250 console. Output encoding should not depend on the console code page; consider UTF-8 output with `errors=` handling.
- `docs/test_properdocs_hooks.py::test_on_page_markdown_keeps_headless_tags_as_text`: a Windows path is inserted into a regular expression or a `re.sub` replacement (`bad escape \l`). Use `re.escape`, or a function as the replacement.

### 7. Not yet diagnosed

- `validation/test_validation_tag_readme.py`: `test_complete_mark_ranges_over_every_participating_collection`, `test_tagged_note_fails_without_a_head`.
- `validation/test_validation_unquoted_sources.py::test_one_verified_quote_brings_the_note_under_the_bound`.

### 8. CI

When the suite passes locally on Windows, drop the Linux-only condition on the pytest step in `.github/workflows/ci.yml` and update its comment.
