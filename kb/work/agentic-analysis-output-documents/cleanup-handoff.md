# Cleanup of the analysis code and tests

Worker packet, written 2026-09-28 from three independent reviews at
`86b4f98f` to `c2d89640`: a code review, a contract review, and a test
redundancy and backcompat review. Purpose: make the analysis workflow's
code and tests smaller without losing any guarantee a reader of a retained
set relies on, which are the pin chain, run-id and boundary agreement,
each member's validation, source and quote anchors, the committed-inputs,
running-package and worktree checks, rollback, and incumbent replacement.
No behaviour visible to an analysis coordinator changes, except error
messages that name retired concepts. The decisions in the
[transition plan](./transition-plan.md) stand.

## Work, as separate commits with a green suite after each

1. **Dead and leftover code.**
   - Delete `scripts/split_agentic_result_fixture.py` (reads the archived
     single-file format).
   - Delete `agentic_records.set_record_errors` with its tests and
     `agentic_set.declared_union`; the directory-artifacts workshop will
     reintroduce what it needs.
   - Delete `agentic_records.RECORD_ID` and `PROPOSAL_TOKEN`, and the
     non-member resolution branch of `record_reference_errors` if no
     production caller reaches it after the deletions.
   - Make `known_ids` required in `systems_matrix.validate_comparison` if
     every production caller passes it, and drop the body-scanning fallback
     (`shared_record_ids`) if nothing else uses it.
   - `PreparedPublication`'s constant field and inspect-destination's
     constant `"replaceable": True` key: remove, updating callers and the
     skill or reference only if they mention them.
   - Inline single-use wrappers `_git_blob_lines` and `_parsed_frontmatter`.
2. **Duplicated checks.**
   - Run-state parsing (`agentic_analysis.py`, the consistency rules that
     restate the run-state schema's `if/then` blocks and source rules): keep
     field extraction, delete the consistency checks, and make every caller
     that parses a run state validate it with `validate_note` first, as the
     handoff command already does (at least `cli/quote.py` and publication).
   - Publication validates the prospective state through content overrides
     before writing and again from disk after writing: keep the pre-write
     check and delete the post-write re-validation, unless a test shows the
     disk view can differ from the override view.
   - Hash and read a capture source once per verification instead of once
     per document.
   - Replace the retained-path self-comparison with one `resolve()` check
     that the retained directory stays inside the retained root.
   - Delete overview type checks that repeat `load_member_set`'s check
     (publication and the matrix loader), and `MatrixInputs.recheck` with its
     call sites.
3. **One implementation per concept.**
   - One GitHub blob URL parser and one local-anchor regex, in
     `quote_matching`, used by `agentic_analysis`.
   - One record-declaration regex, in `agentic_records`; `systems_matrix`
     uses it.
   - One run-ID pattern, one SHA-256 pattern, one normalized repository-path
     check, one reviews-path rule, each defined once and imported.
   - Make the helpers imported across modules public: `_git_blob_text`,
     `_verify_quote_anchors`, `_atomic_write`.
   - Warn handling: the handoff command treats warnings as failures, as
     publication does.
   - Split source text on `\n` rather than `str.splitlines()` in quote
     generation and matching, so ranges match editors and GitHub; add a test
     with a form-feed character.
4. **Tests.**
   - Delete the redundant tests: `test_source_anchor_past_blob_end_is_rejected`,
     `test_quote_anchor_rejects_a_local_revision_mismatch` (first tighten the
     kept `[revision]` case's match to "attribution uses revision"),
     `test_prepare_checks_handoff_without_publishing`,
     `test_prepare_validates_each_member_once…`,
     `test_publication_cli_rejects_retired_legacy_arguments`,
     `test_memory_report_quote_is_checked_at_the_frozen_source`,
     `test_prepare_rejects_an_unresolved_quote_in_a_candidate`,
     `test_publish_rejects_a_source_mismatch_before_replacing_an_incumbent`
     (add a "destination unchanged" assertion to the kept `[source]` case),
     `test_publish_requires_inspected_digest_even_for_valid_incumbent`,
     `test_publication_trial_stops_wrong_specialist_range_then_publishes_unranged`,
     and the `README.md:999` tail of the ranged-attribution test.
   - Drop repeated parametrized cases where one case already exercises the
     code path: the per-member identity cases already covered by
     `test_agentic_set.py::test_identity_errors_are_reported_per_member`,
     the per-member manifest loop cases (keep one member), the `overview`
     output-role cases of the anchor tests, the comparison-message cases
     covered in `test_systems_matrix.py`, one of each afforded/claimed and
     missing/extra pair, and the `analyze_matrix` block that repeats the
     statistics test.
   - Delete legacy-shape assertions: `[legacy-run-field]`, the `[legacy]`
     evidence-basis case, the "keep the more legible" absence check, and the
     retired-term absence lists in
     `tests/commonplace/docs/test_agentic_system_instruction_composition.py`;
     keep that file's phrase checks and `test_method_paths_exist_in_the_repository`.
   - Give bare `pytest.raises(ValueError)` calls a message match.
   - Move tests that exercise one pure function off the full git-backed
     fixture onto a lighter one, as far as a small shared helper allows;
     loop the reserved-names cases over one fixture.

Keep, each tested once: publication rollback and retry, the worktree rules
including the Unicode path, the running-package, method and ancestry checks,
quote anchors on local and GitHub attributions, manifest integrity, and
incumbent replacement. The reviews list their tests; do not remove one.

## Scope and checks

Owned: the analysis modules (`src/commonplace/lib/agentic_*.py`,
`systems_matrix.py`, `quote_generation.py`, `quote_matching.py`, the
analysis type rules in `validation.py`), `src/commonplace/cli/agentic_*.py`,
`src/commonplace/cli/quote.py`, `scripts/build_systems_matrix.py`,
`scripts/render_systems_table.py`, `scripts/analyze_matrix.py`,
`scripts/verify_report_quotes.py`, `scripts/split_agentic_result_fixture.py`,
the analysis tests, and `kb/reference/commands.md` or the analysis skill
only where a removed name is mentioned.

Not owned, never edit or stage: another session is changing
`src/commonplace/cli/init_project.py`, `src/commonplace/lib/snapshot.py`,
`src/commonplace/scaffold_manifest.py`, `tests/commonplace/cli/test_init_project.py`,
`scripts/migrate-snapshot-types.py`, `scripts/review_link_consumption.py`,
their tests, and several KB files; leave every file you did not change.
If their uncommitted edits make the suite fail, report the failing tests
and continue only if your own changes are verifiably green in isolation.

`uv run pytest` and `uv run ruff check src tests scripts` after each commit.
Report per commit: hash, what went, net lines removed from `src/`, `scripts/`
and `tests/`, test count, and suite runtime at the end.
