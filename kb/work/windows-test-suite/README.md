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

Baseline on 2026-10-27, Windows 11 Home, Python 3.14.7, checkout with `core.autocrlf=true`: 795 passed, 47 failed, 11 skipped, 6 collection errors. After the first five fixes the same day (`24b06867a` to `ef15112e6`): 819 passed, 26 failed, 11 skipped, 6 collection errors; no new failures. After the path and line-ending fixes (`030cfddcb`, `6d95f8f58` to `a5002969c`): 833 passed, 12 failed, 11 skipped, 6 collection errors; no new failures. The 12 left are items 1, 4 and 6. After the symlink fixes (`0cfb897f3`, `9d703300d`): 836 passed, 8 failed, 13 skipped, 6 collection errors; the 8 left are items 1 and 6. After skipping the analysis tests (`1cf410262`): 836 passed, 3 failed, 18 skipped, 3 collection errors; the 3 and 3 left are `commonplace-task` and the X-likes sync (item 1) and item 6. After the X-likes lock and encoding fixes (`e56440579`, `08b1b0034`, `291cec5f4`): 848 passed, 1 failed, 18 skipped, 2 collection errors; all three are `commonplace-task` and `headless/`, waiting on Workjig. On 2026-10-30 at `c54939d60`, Python 3.14.7, from Git Bash with the invocation above: 855 passed, 1 failed, 18 skipped, 2 collection errors, the same three. After the run-lock migration, the lazy publication-lock import and the task-path fix (2026-10-30, uncommitted at the time of the run): **890 passed, 13 skipped, 0 failed, 0 collection errors**. The 13 skips are four symlink-privilege skips, seven Linux-only Codex launcher or bubblewrap tests and one optional `mkdocs_redirects` import. Linux was not run locally; CI covers it. `08b1b0034` also fixed the sync script writing `.env`, state and inbox notes in the locale encoding: a liked post with an emoji crashed the sync on Windows.

## Backlog

### 1. Unix-only `fcntl` locking

**Decision (operator, 2026-10-27): agentic analysis runs on Linux only.** The `agentic-system-analyses` collection is this repository's own; `commonplace-init` never scaffolds it. On Windows the tests that build or read it are ignored (modules that import the analysis code at load time, in `tests/commonplace/conftest.py`) or skipped with `analysis_linux_only` from `tests/commonplace/platforms.py` (`1cf410262`). Linux CI runs all of them. Consequences:

- The publication-lock helper planned below is no longer needed; the publication lock stays `fcntl`.
- `commonplace-validate` on `kb/agentic-system-analyses`, and this repository's site build, crash on Windows with `No module named 'fcntl'`. The chain: the analysis artifact rule calls `publication_slug`, which imports `sources.github_checkout_path` (a pure string function); `sources` imports `effects`, which imports `fcntl` at the top for `publication_lock` alone. Moving that import into `publication_lock` was tried and reverted: validation of the collection then succeeds on Windows (222 files, 0 failures, 0 warnings). Not done; the operator decides.
- **Decision (operator, 2026-10-30): `commonplace-task` and `headless/` must work on Windows,** and read-only consumers of analysis artifacts may import the analysis code on Windows. The run lock moved to Workjig 0.2.0's `hold`/`busy` on `<run>/calls/.lock`; `effects.py` imports `fcntl` inside `publication_lock`, so publishing stays Linux-only. On Windows only `tests/commonplace/agentic_analysis/` stays ignored: with the exclusion lifted it gave 31 failures and 12 errors (sandbox, worktree, publication and audit paths). The comparison and site tests that only read analyses run on Windows again.

`fcntl` does not exist on Windows. Importing it fails, so whole modules fail to load, including `commonplace-task` and `commonplace-analysis` themselves.

- Commonplace imports: `src/commonplace/lib/agentic_analysis/effects.py`, `src/commonplace/lib/agentic_analysis/worktree.py`, `src/commonplace/headless/jobs.py`, `scripts/sync_x_likes.py`, `tests/commonplace/agentic_analysis/test_publication_locking.py`.
- ~~Workjig import: `workjig/run.py`; waits for the Workjig fix.~~ Workjig 0.2.0 locks through its own cross-platform `platform.file_lock`.
- Collection errors: `tests/commonplace/agentic_analysis`, `comparison/test_build_systems_matrix.py`, `comparison/test_comparison_consumers.py`, `headless/test_jobs.py`, `headless/test_tasks.py`, `sources/test_sync_x_likes_script.py`.
- Failures: `docs/test_command_catalogue_integrity.py` (`commonplace-analysis`, `commonplace-task` help), `comparison/test_historical_coverage.py::test_working_or_draft_artifact_cannot_borrow_retained_byte_permission[True]`, `comparison/test_systems_matrix.py::test_mixed_strength_and_partial_coverage_preserve_only_supported_positives`, and `docs/test_properdocs_hooks.py`: `test_site_current_list_matches_comparison_population`, `test_lens_listing_links_each_current_member`.

The four locks and the plan (2026-10-27):

| Lock | Where | Protects | Plan |
|---|---|---|---|
| Run lock, `<run>/lock` | `headless/jobs.py` `_acquire`, `run_lock` | one process per analysis run (ADR 118) | ~~move to Workjig~~ done 2026-10-30 |
| Run-lock probe | `agentic_analysis/worktree.py` `_locked` | `state: running` in the status view | ~~move to Workjig~~ done 2026-10-30 |
| Publication lock | `agentic_analysis/effects.py` `publication_lock` | installs and rollbacks into one worktree's `kb/`, shared by every run in it (up to 99); waits | Commonplace helper |
| X-likes sync lock | `scripts/sync_x_likes.py` | one sync at a time, because syncs rotate the token in `.env` | ~~Commonplace helper~~ Done in `e56440579`: `sync_lock` in the script (`fcntl` / `msvcrt`) |

- ~~**Run lock to Workjig.**~~ Done 2026-10-30 against Workjig 0.2.0, which shipped all three requests. `acknowledge_stopped` now opens Workjig's records alone, since they hold the same lock. `jobs.Run` already holds Workjig's records lock (`<run>/calls/.lock`) beside its own for the whole run. A request asks Workjig for a lock-only `hold(record_dir)`, a `busy(record_dir)` probe, and a fix to `Run.__enter__` refusing a `.lock` without `run.json`. It is in the Workjig checkout as `tmp/request-from-commonplace-run-lock-api.md`. Then `run_lock` calls `workjig.hold`, `jobs.Run` drops `<run>/lock`, and `_locked` calls `workjig.busy`.
- ~~**Publication lock stays in Commonplace.**~~ Superseded: agentic analysis is Linux-only, so the publication lock keeps `fcntl`. The X-likes lock got its own small helper in the script instead. Workjig's lock is per run and refuses at once; the publication lock spans runs and waits. Write one stdlib helper in `src/commonplace/lib/`: `fcntl.flock` on Unix, `msvcrt.locking` on the first byte on Windows. It needs a waiting mode that retries, since `msvcrt`'s own blocking mode gives up after about 10 seconds. It raises `BlockingIOError` when not waiting, unlocks explicitly before closing, and never deletes the lock file. Use it in `effects.py`, the sync script and `test_publication_locking.py`.

### 2. Backslashes written into Markdown links (real bug)

Diagnosed 2026-10-27. Markdown links must use `/` on every platform.

- ~~**Relocation:**~~ Done in `24b06867a`. `format_relative_link` in `src/commonplace/lib/relocation.py:77` returns `os.path.relpath(...)` unconverted. Fix: `Path(os.path.relpath(...)).as_posix()`. Confirmed by patch to fix 5 tests:
  - `relocation/test_relocate_directory.py`: `test_relocate_directory_apply_moves_and_rewrites`, `test_relocate_directory_moves_hidden_payload_without_inspecting_it`.
  - `relocation/test_relocate_note.py`: `test_rewrite_links_to_moved_files_updates_real_links_only`, `test_relocate_note_apply_moves_file_with_to_directory`, `test_relocate_note_apply_moves_note_across_kb_collections`.
- ~~**Site hooks, same pattern:**~~ Done in `ef15112e6`, through a `_relative_link` helper. `src/commonplace/docs/properdocs_hooks.py` builds links with `os.path.relpath` at about lines 112 and 115 (lens listing; its tests are hidden behind item 1) and in `_tag_link` at about 269. The `_tag_link` one also causes item 6's `bad escape \l`.
- Already correct: `index_generated.py` and `promotion.py` use `.as_posix()`.

### 3. Backslashes in repository paths in messages, JSON and navigation

Diagnosed 2026-10-27. Repository-relative paths are identifiers that also appear in links and on Linux, so output uses `/` on every platform; fix the code, not the tests. There is no shared helper today; modules use local `str(x.relative_to(root))` or f-strings.

- ~~**`_display_path` in `src/commonplace/cli/validate_notes.py:172`:**~~ Done in `49e2ef1b9`. `str(path.relative_to(repo_root))`. `.as_posix()` is confirmed by patch to fix:
  - `validation/test_directory_artifact.py::test_cli_json_counts_artifact_once_and_locates_member_failure`
  - `validation/test_validation_scope.py::test_recent_drilldown_keeps_collection_scope`
  - `validation/test_validate_notes.py`: `test_source_collection_validation_prints_local_snapshot_warning`, `test_validation_json_is_compact_and_structured`
- ~~**`_display_snapshot_path` in `src/commonplace/lib/validation.py:900`:**~~ Done in `49e2ef1b9`. same; fixes 2 of the 3 `sources/test_quote_verification.py` failures (`test_checksum_locates_differently_named_snapshot_with_empty_quotes`, `test_missing_expected_snapshot_reports_same_url_as_different_bytes`).
- ~~**Inline sites in `src/commonplace/lib/validation.py`**~~ Done in `030cfddcb`, by adding `.as_posix()` at each site rather than a shared helper (line numbers approximate):
  - 1915 and 1933: `docs/test_collection_landing_integrity.py` (2 tests).
  - 1781-1782: `test_validate_notes.py::test_validate_collection_structure_flags_nested_collection`.
  - 1222: `test_validate_notes.py::test_note_target_also_validates_marked_tag_readmes` and `validation/test_validation_tag_readme.py::test_complete_mark_ranges_over_every_participating_collection`.
  - 1455: `validation/test_validation_tag_readme.py::test_tagged_note_fails_without_a_head`.
  - 1839 (`names()`): `test_validate_notes.py`: `test_source_snapshot_cache_warns_about_redundant_alternate_copy`, `test_source_snapshot_cache_reports_same_url_as_related_observation`.
  - Same pattern, no failing test: 583, 1152, 1187, 1742, 1768.
- ~~**Relocation messages**~~ Done in `030cfddcb`. in `src/commonplace/lib/relocation.py` (about 455-676, including `Relocate:` and `Move write brief:`): `relocation/test_relocate_note.py::test_relocate_note_dry_run_reports_brief_without_moving`.
- ~~**Site navigation:**~~ Done in `ef15112e6`. `src/commonplace/docs/properdocs_hooks.py:77`, `str(readme.relative_to(docs_dir))`: `docs/test_properdocs_hooks.py::test_on_config_omits_unpublished_report_collection`.
- ~~**Test-only:**~~ Done in `030cfddcb`. `sources/test_quote_generation.py` (2 tests). The product already prints `.as_posix()` (`src/commonplace/lib/quote_grounding.py`); the tests build the expected text from a Windows path. Use `source.file.as_posix()` in the tests and in their `block()` helper.
- **Other `str()` paths, no test:** `lib/quote_verification.py` `display_path`, `lib/project_paths.py`, `lib/tasks.py` (`run_dir=` is serialised), and `lib/agentic_analysis/audit.py`, whose `accepted_sha256` keys would differ between operating systems.
- **Proposed shape (not taken):** fix `_display_path` and `_display_snapshot_path`; add one `repo_relative(path, root) -> str` helper in `lib/` (for example beside `artifact_identity` in `library.py`); replace the inline sites with it. Grepping for `str(.*relative_to`, `os.path.relpath` and f-strings over `relative_to` finds them.

### ~~4. Symlinks need a privilege~~

Diagnosed 2026-10-27. Creating a symlink fails with `WinError 1314` unless Developer Mode is on or the process is elevated. `tests/` has no shared guard; only `validation/test_full_pass.py` skips locally. Add one `symlink_or_skip(link, target, *, directory=False)` helper in `tests/commonplace/conftest.py` and use it everywhere. More symlink setups will fail the same way once item 1 lets their modules load: `agentic_analysis` (`test_audit`, `test_acquisition`, `test_effects`, `test_integration`, `test_publication_migration`, `test_rerun_stats`, `test_source_guards`, `test_worktree`) and `tooling` (`test_isolated_codex`, `test_capture_test_state`).

- ~~Done in `0cfb897f3`.~~ `general/test_collection_resolution.py::test_resolve_collection_rejects_missing_noncollection_and_external_targets`: checks that a link escaping the KB is rejected. A user can make a junction, so on Windows use a directory junction (`_winapi.CreateJunction`), same assertions. Confirmed: all six cases raise with a junction.
- ~~Done in `0cfb897f3`.~~ `installation/test_init_project.py::test_init_and_check_resolve_the_library_from_the_project_root`: the symlink is not needed and weakens the test, because `.resolve()` hides the regression it targets. Rewrite with a real `other/kb/instructions/` and compare `as_posix()` paths; the routing file renders paths with `as_posix()`. Confirmed: the rewrite passes, and a mutant that ignores `start` fails.
- ~~Done in `0cfb897f3`.~~ `installation/test_init_project.py::test_init_project_preserves_symlinked_skill_directories`: tests that init never writes through a symlinked skill folder. Use `symlink_or_skip`; a junction is not a symlink to `is_symlink()`.
- ~~Done in `0cfb897f3`.~~ `validation/test_directory_artifact.py::test_symlink_member_fails`: a symlinked member file; junctions cannot point to files. Use `symlink_or_skip`.
- ~~**Product gap (confirmed):**~~ Done in `9d703300d`, with a Windows-only junction test; the guard reads the reparse tag, which works on 3.11. `commonplace-init` checks `dest.is_symlink()` (`src/commonplace/lib/library.py`, about lines 283 and 292). A junction is not a symlink, so init wrote through a junctioned skill folder into its target. Treat junctions as foreign too. `Path.is_junction()` needs Python 3.12 and `requires-python` is `>=3.11`, so guard it. Add a junction test beside the symlink test.

- **Done 2026-10-27:** `tests/commonplace/link_helpers.py` has `symlink_or_skip`, which skips only on `WinError 1314`, and `junction`. Every test that creates a symlink uses the helper, apart from the Linux-only `tooling/test_isolated_codex.py`.
- **Left for later:** the other guards that check only `is_symlink()` miss junctions too: `full_pass.py`, `agentic_analysis/` (`preparation.py`, `analyses.py`, `sources.py:266`, `effects.py`, `worktree.py`), `directory_artifact.py:83, 97`, `validation.py:534, 2113`, and `scripts/agentic_system_rerun_stats.py` and `migrate_analysis_publications.py`. They matter once agentic analysis runs on Windows; its sandbox is Linux-only today. When that work starts, move `_is_link` from `lib/library.py` to a shared module and use it in each guard, with a junction test for each. The guards that also compare `resolve()` (`guards.py:72`, `sources.py:317`, `directory_artifact.py:111`) already catch junctions.

### 5. Line endings

Diagnosed 2026-10-27, by running the tests in a clone with `core.autocrlf=false`. The checkout's CRLF explains only one failure. Most come from writing in Python text mode, which on Windows writes CRLF, then reading raw bytes without normalising. That is a product bug users' Windows KBs will hit.

- ~~**CRLF checkout:**~~ Done in `6d95f8f58` with `* text=auto eol=lf`; the two captured CSVs with CRLF bytes in `kb/reports/retained/codex-ingest-session-tool-result-volume-20260831/` are `-text`. The index needed no renormalising. Existing Windows checkouts keep CRLF copies until those files are checked out again. `comparison/test_historical_coverage.py::test_real_allowlist_pins_exact_unchanged_publications`. The test hashes tracked `kb/reports/retained/.../memory-profile.md`, whose bytes are pinned in `src/commonplace/lib/systems_matrix.py` (about 170-173, checked about 309). In a CRLF checkout the systems matrix itself stops recognising the two historical profiles. Passes in the LF clone. Fix: add a `.gitattributes` (there is none) with `* text=auto eol=lf`, or at least `kb/** text eol=lf`.
- ~~**Validator keeps `\r` (product):**~~ Done in `aee32bd98`, with a CRLF-ingest regression test. `ValidationRun.load_document` in `src/commonplace/lib/validation.py:239` decodes raw bytes and keeps CRLF. Fix: `.replace("\r\n", "\n")` after decoding; hashing keeps using exact bytes. Confirmed in the clone to fix:
  - `validation/test_full_pass_validation.py` (6 tests): `resolution_section` (`src/commonplace/lib/full_pass.py`) returns CRLF text that never equals the LF rendering.
  - `validation/test_validation_unquoted_sources.py::test_one_verified_quote_brings_the_note_under_the_bound`: `INGEST_QUOTES_HEADING_RE` (`src/commonplace/lib/quote_verification.py:56`) cannot match `## Quotes\r`, so quotes go unverified.
- ~~**Init rewrites its own template (product):**~~ Done in `20b3c0543`, including the CRLF-tolerant `_record_existing` and a regression test. `_write_template` in `src/commonplace/cli/init_project.py` builds `expected_bytes` with LF but writes with `write_text` (line 93), so the file lands CRLF and every rerun reports `AGENTS.md.template` as differing. Fix: `target.write_bytes(expected_bytes)`; confirmed by `installation/test_init_project.py::test_init_project_creates_core_layout_and_is_idempotent`. Also make `_record_existing` ignore CR-versus-LF differences, so a user's CRLF copy counts as unchanged; `test_init_project_treats_raw_template_source_as_matching` passes in the CRLF checkout only by coincidence.
- ~~**Test writers:**~~ Done in `3cb67ca6d`. `sources/test_quote_matching.py::test_three_verifiers_agree_on_same_quote_and_region[one\none-False]` writes `"one\none"` in text mode and hashes the LF text; snapshot pins are byte-exact by design, so write with `write_bytes` or `newline=""`. Same for `sources/test_quote_verification.py::test_matching_checksum_with_different_source_url_warns` (its `_ingest` helper), which then also needs item 3's `_display_snapshot_path` fix.
- ~~**Not tested, inferred:**~~ Done in `a5002969c`, without a test (it would only fail on Windows). `x_snapshot.py` (about 435) and `github_snapshot.py` (about 180) write snapshots in text mode and print the SHA-256 of the CRLF bytes. If such a snapshot is committed with `autocrlf=true`, Git stores LF and the pin breaks elsewhere. Write snapshots with `newline=""`.

### ~~6. Encoding and regular-expression one-offs~~

Diagnosed 2026-10-27.

- ~~Done in `291cec5f4`.~~ `tooling/test_scan_tool_failures.py::test_unicode_separators_are_not_record_boundaries`: not console output. The test helper `trace()` (line 17) calls `write_text()` without `encoding`, so Windows writes cp1250 and fails on ` `. Fix: `encoding="utf-8"` there and at lines 105 and 158. Confirmed: all 16 tests pass with `PYTHONUTF8=1`.
- ~~Done in `291cec5f4`.~~ `sources/test_quote_matching.py::test_notes_only_match_retained_bodies[one two]`: same kind. Line 48 writes without `encoding`, so an em dash becomes cp1250 byte `0x97`. Fix: `encoding="utf-8"`.
- ~~`docs/test_properdocs_hooks.py::test_on_page_markdown_keeps_headless_tags_as_text`~~ Done in `ef15112e6`, with a backslash-in-status regression test: two bugs in `src/commonplace/docs/properdocs_hooks.py`. The badge `re.sub` (about 312) uses page text in a replacement template, which breaks on any `\`, on Linux too; use a function replacement. And `_tag_link` writes a backslash link (item 2). Needs both fixes; inferred, not run.
- Grep the tests for `write_text(` and `open(` without `encoding=`; more may fail on non-UTF-8 Windows locales.

### 7. Not yet diagnosed

Nothing left: the three tests listed here were diagnosed into items 3 and 5.

### 8. CI

When the suite passes locally on Windows, drop the Linux-only condition on the pytest step in `.github/workflows/ci.yml` and update its comment. Done in the working tree on 2026-10-30: the step runs on both runners under `shell: bash`. No CI result yet; this workshop closes only after a green `windows-latest` run.
