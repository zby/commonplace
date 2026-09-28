# Consumer inventory of the single-result shape (2026-09-28)

Produced by an independent read-only code survey for step 3 of the
[workshop](./README.md). Line numbers refer to the checkout at commit
`6f3a9c10`. Everything below reports what exists; the
[transition plan](./transition-plan.md) decides what changes.

## Consumers

| Consumer (file:lines) | Reads | Verifies or fails on | Needs under the set |
|---|---|---|---|
| `agentic_analysis.py` `parse_agentic_analysis_run_state` 160-282 | run-state `result{path,sha256}`, `generated-review{path,sha256}` via `_output_identity` 141-157 | `result.path` must equal `state/.../<run-id>/result.md` (209-220); review path under `reviews/` (221-231); status and disposition matrix (232-268) | accept an overview path or a new key; no member mapping in the run state if the overview's manifest carries it |
| `verify_agentic_analysis_run_state` 709-862 | bytes of `result` and `generated-review`; result frontmatter identity fields (778-789) | SHA match (731-739); full `validate_note` of each output (744-767); identity; retained copy bytes (799-812); review frontmatter incl. `analysis-result(-sha256)` (817-835); source and quote anchors per output (842-860) | verify the manifest: each member's hash and type; identity from the overview; retain every member; review keys renamed; anchor checks on every member |
| `_verify_result_projection_paths` 633-655, `_run_identity_value` 623-630 | result body `**Run state:**`, `**Generated review:**` lines | equality with the state and review paths | move to the overview's Run identity |
| `_verify_memory_report` 658-706 (called 774-776 for `complete`) | result body `**Memory analysis report:**` and SHA line; `memory-report.md`, `memory-input.md` bytes; report frontmatter fields | path and hash projection; field equality; `validate_note(report)`; anchors on the report | becomes the check of `memory.md`: `finalized-from` equals the local report's hash; the report path and hash lines leave the result body |
| `render_agentic_analysis_handoff` 592-620 | `state.result.display_path` | requires `complete` | print the overview path and members |
| `validation.py` `validate_agentic_analysis_run_state` 1217-1239 | delegates to the two functions above | | unchanged wiring |
| `validation.py` `_agentic_evidence_and_references_rule` 923-944 (result and report types) | body via `record_reference_errors`; blockquotes | ID errors; quote shape (581-603); a complete result or report needs at least one attributed quote | resolve IDs across the set; decide which member types need a quote |
| `validation.py` `_agentic_comparison_rule` 947-961, `_memory_report_comparison_rule` 964-980 | `memory-comparison` frontmatter plus body | `validate_comparison` | profile in `memory.md`; its record references resolve against IDs declared in other members |
| result schema (headings ~55-172, body patterns 173-190) | eleven `##` sections in order; subsections; the four `**…:**` run-identity lines | schema fail | per-member schemas |
| `agentic_publication.py` `_require_candidate_in_run` 132-141 | reserved names `result.md`, `memory-input.md`, `memory-report.md`, `incumbent-review.md`, `incumbent-result.md` | candidate rejected | add member names |
| `_check_incumbent` 144-213 | incumbent review pin fields; retained result frontmatter; on a dirty tree the receipt `run-state.md` fields incl. the literal `result.md` path (199-202) | canonical path; hash; type literal (185); receipt equality | accept the overview pin; receipt compares the overview |
| `_render_final_state` 230-266 | writes `result{path: run_dir/result.md, sha256}` and `generated-review` | | write the overview pin |
| `_check_bundle` 269-332 | `run_dir/result.md` (287): `complete`, has `memory-comparison` (290-293); retained path must not exist (294-298); overrides for review and retained result (310) | validates the final state text with overrides | read `memory-comparison` from `memory.md`; one override per retained member |
| `publish_publication` 363-430 | targets retained result, review, state (369-373); backups `incumbent-review.md`, `incumbent-result.md` (375-378) | rollback | retain N members; back up the incumbent set |
| `systems_matrix.py` `retained_result_path` 103-106 | `RETAINED_ROOT/<run>/result.md` | run-ID regex | overview path function |
| `systems_matrix.load_results` 291-415 | review pin fields; result frontmatter identity and `memory-comparison`; body between `## Source register` and `## Shared records` (355-361) | path and hash (315-325); `validate_note(result)` (329-342); type and complete (343-348); identity (349-352); source identity present in register text (362-365); one review per source; `validate_comparison` (370) | verify overview pin, manifest, members; identity from the overview; profile from `memory.md`; register text from the overview; CSV `result_file`/`result_sha256` columns (83-97) change meaning |
| `systems_matrix.validate_comparison` 119-240 | `## Shared records` up to `## Runtime account` (result) or `## Write side` (report) (134-138) | references within that one section's IDs | needs the declared-ID set of the whole set |
| `scripts/build_systems_matrix.py` 26, `render_systems_table.py` 72-97, `analyze_matrix.py` 66 | `load_results` only | | follow `load_results`; the table's result link changes |
| `scripts/bundle_agentic_landscape.py` | `METHOD_INPUTS` 27-28 name the result type and schema; copies review plus one result (107-111); `verify` reruns `load_results` (190, 210) | manifest, matrix, population equality | copy every member; add member type specs to `METHOD_INPUTS`; any runtime change makes old bundles unverifiable from this checkout by design |
| `cli/init_project.py` `_RESULT_PIN` 318, `_repin_result_checksums` 347-355, 385, 424-429, 674 | any `.md` under `kb/`: regex on `analysis-result-sha256`; rehash keyed by the old hash of every file whose type line was rewritten | | would not match `analysis-overview-sha256`; would not update manifest hashes inside the overview after a member's type line is rewritten |
| `scripts/verify_report_quotes.py`, `cli/quote.py` | run-state `source` only | | unaffected |
| `scan-agentic-system-transfer/SKILL.md` 17-19, 40-47, 81, 94 | `state/.../result.md` plus `run-state.md`; the handoff command; result path and SHA against the run state; boundary, shared records, lens findings, limitations | prose | name the overview and members and which holds what |
| `synthesize-agent-memory-landscape/SKILL.md` 22-29, 47-58, 105-107, 119 | the pin fields; source register, shared records, memory lens, reconciliation, limits; the bundle script | prose | pin names; section-to-member map |
| `kb/agentic-systems/COLLECTION.md` 30-31, 46-50, 93 | promises the pin and the retained `result.md` | contract | rewrite |
| `comparisons/README.md` 5-10, 42, 61 | same promise | contract | rewrite |
| `properdocs.yml` 6 | publishes `retained/agentic-system-analysis/**/result.md` | site | publish the member names |
| `analyse-agentic-system/SKILL.md` 24, 53, 228, 237, 297, 332-336, 350, 371 | literal `result.md`, `memory-report.md`, the pin fields, `incumbent-result.md` | test-pinned | rewrite |

## Literal strings and regexes

- `result.md`: `agentic_analysis.py:217,220`; `agentic_publication.py:138,200,239,287`; `systems_matrix.py:106`; `properdocs.yml:6`; the result type's One entry artifact section.
- `memory-report.md`, `memory-input.md`: `agentic_analysis.py:664,667,670`; `agentic_publication.py:138`.
- `incumbent-result.md`, `incumbent-review.md`: `agentic_publication.py:139,376-377`.
- `analysis-result`, `analysis-result-sha256`: `agentic_analysis.py:825-826`; `agentic_publication.py:176,181`; `systems_matrix.py:315,324`; `init_project.py:318,348,674`.
- Result type literal: `agentic_analysis.py:24`; `systems_matrix.py:18`; `agentic_publication.py:185`; `validation.py:923,947`; `bundle_agentic_landscape.py:27-28`.
- Headings: `"## Source register\n"` and `"## Shared records"` at `systems_matrix.py:355-356`; the Shared records span at `systems_matrix.py:134-137`; `_section` names at `agentic_records.py:69,74`; `^## Reconciliation` at `agentic_records.py:59`; `^## Outcome` at `agentic_publication.py:256`.
- Run-identity labels at `agentic_analysis.py:624,638-639,666,677` and the result schema body patterns.
- ID regexes: `agentic_records.py:8-19`; `systems_matrix.py:141`.

## Identifier checks (`agentic_records.record_reference_errors` 46-79)

The prose filter (22-38) removes fenced blocks and blockquote lines; inline code spans are not excluded. A declaration is an ID at line start, optionally after a table cell bar, a list marker or a level-three-to-six heading, counted only inside `## Shared records` (69-70); duplicates fail. A `SRC-n` token anywhere in `## Source register` counts as declared. A reference is any ID token in the prose; unresolved ones fail. Shorthand and ranges fail. `MEM-` and `EPI-` prefixes are allowed only inside `## Reconciliation` (58-67). A memory report runs only the shorthand check (52-56). `validate_comparison` has a near-duplicate regex (141) allowing `MEM-` for reports and excluding SRC, scoped to a section that ends at a named heading. Every check runs on one file's body; the standing type rule sees one file at a time, so a cross-member check belongs to the set verifier.

## Quote-anchor check

Standing validation checks shape only (`validate_quote_citations` 581-603); a complete result needs at least one attributed quote (936-944). Resolution against the frozen source (`_verify_quote_anchors` 494-565 with `_verify_source_anchors` 416-491) runs from `verify_agentic_analysis_run_state` 842-860 over the result and the review, and from `_verify_memory_report` 692-703 on the local report. Publication reaches it through `_check_bundle` 311-317 and again after publishing (400). `load_results` does not resolve quotes.

## Run-state mappings

Written only by `_render_final_state` 239-251; read by `parse_agentic_analysis_run_state` 202-231, the incumbent receipt comparison 199-208, the transfer-scan skill, and the handoff renderer. The schema's `$defs.output` is `{path, sha256}` with no extra properties, and nulls are enforced per status. An overview pin touches the schema, `_output_identity`, the expected-path check 209-220, the state dataclass, `_render_final_state`, the receipt literal, and the tests' `valid_run_state` fixture.

## Population and coexistence

There are 60 retained `result.md` files. Of 53 review files, 41 are generated and 40 pin `analysis-result` with matching hashes; `pond.md` has no pin. Only 3 generated reviews load under the current contract, the three 2026-09-27 pilots; 37 fail `validate_note` on the pre-ADR-093 `memory-comparison` shape (329-342) and `pond.md` fails at 315-318. Default `load_results` therefore already raises, and the committed `memory-systems.csv` cannot be regenerated from the corpus.

If old results and new sets coexisted: `load_results` 314-318 rejects a review pinning `analysis-overview`; `_check_incumbent` 176-177 rejects a new-shape incumbent and its dirty-receipt branch compares the literal result path; `verify_agentic_analysis_run_state` 822-835 fails on the renamed review keys; the init repin skips overview pins. Run states are git-ignored, so only local runs are affected by run-state changes.

## Tests that would change

`tests/commonplace/lib/test_agentic_analysis.py`: the fixtures `result_fixture`, `valid_run_state` (~137-316), `memory_report_fixture` (100-128), `sync_retained_fixture` (338-351) and `publication_fixture` (354-367) build the single result and the pin; tests at 370, 470, 480, 501, 520, 553 (run-state outputs), 603, 637, 674, 714, 736 (anchors), 755, 778, 808 (handoff), 824-1064 (publication, reserved names, memory handoff lines, retained link), 1095-1195 (`load_results` and scripts), 1254-1371 (incumbents), 1382-1619 (quote and ID checks) inherit them. Also: `test_agentic_records.py` (all seven, single-body semantics); `test_systems_matrix.py` (all seven, one body's Shared records); `test_landscape_bundle.py` (all nine, `copy_member` 30-44); `docs/test_agentic_system_analysis_result_type.py` 147-221 (eleven sections and run identity); `docs/test_agentic_system_instruction_composition.py::test_exact_result_has_one_fixed_state_location` 35-46 and its neighbours reading the type text; `docs/test_site_publication_boundaries.py` 22-34; `cli/test_init_project.py` 383-403 (repin regex). Unaffected: `test_quote_matching.py`, `test_validate_notes.py:1109`, `test_project_paths.py:118`, `test_systems_matrix_redirects.py`.
