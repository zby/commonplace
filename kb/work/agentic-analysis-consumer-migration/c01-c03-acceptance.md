# C01–C03 acceptance — direct main-result comparisons

Accepted on 2026-09-05 for the reader migration. Production corpus regeneration
and public landscape refresh remain outstanding. No commit has been made.

## Inputs and retention decision

The main analysis now authors `memory-comparison` in the exact result, pointing
to its canonical records and naming the compared memory boundary. The 14 axes
cover the existing analyzer's storage, representation, lineage, authority,
write/curation, read-back, trace-learning, and faithfulness questions. They
replace body-token parsing, not the source-grounded findings themselves.

Pond exposed why trace-derived lineage cannot be equated with trace learning
or automatic push. Maka exposed why one primary storage token cannot represent
several stores and consumers. The contract therefore preserves value sets,
comparison scope, evidence basis, and distinct absence, inapplicability,
uninspected, and not-determinable assessments. Known means complete within the
stated scope, with aggregation justified by the canonical records. The parser
checks shape and references; semantic support remains the main review's job.

Public comparisons require exact findings available from a clean checkout.
Publication now retains byte-identical `result.md` under
`kb/reports/retained/agentic-system-analysis/<run-id>/`, with its path and SHA-256
in the compact public review. This is an additional copy of one analysis, not a
rewritten memory review. Run state continues to identify the working result;
completion verification checks that the retained copy has the same hash.
Existing retained bytes cannot be overwritten through publication. The site
publishes only these result files from the otherwise excluded reports area.

## C01 — Matrix builder

`test_comparison_tools_use_retained_results_without_local_or_legacy_inputs`
creates one current-contract fixture, then removes ignored run state, source
checkouts, and the entire legacy collection. It builds a CSV from the retained
main result alone. The output has one row, both `files` and `sqlite`, explicit
uninspected lineage, and the exact review/result hashes. An ordinary navigation
file in the discovery directory is ignored.

Parameterized reader tests reject missing result bytes, byte drift, missing
comparison fields, a different source identity, and revision mismatch. A
repeated source requires explicit selection; the input recheck rejects later
changes. Missing metadata preserves the prior output. No old CSV, identity
join, hand-classified column, tag-derived classification, or prose fallback is
consulted. Old hand-classified columns are dropped; provenance comes from the
main review and result.

## C02 — Table renderer

The same clean fixture builds the table directly from the retained result. It
does not read the newly built CSV. The table retains the two stores and wired
basis, separates code-grounded and doc-grounded cohorts, records both hashes,
and links the compact review and retained exact result. Deterministic
validation confirms the fixture's links resolve without local state or legacy
files. Missing metadata leaves an incumbent table unchanged.

## C03 — Analyzer

The clean fixture reports a fully assessed two-store value set and separately
reports uninspected axes. Additional tests show wired code-grounded values enter
statistics, claimed and afforded values remain separately reported, and
doc-grounded rows are excluded from numerical comparisons. Value-set categories
have their own fill, entropy, and redundancy statistics; member values are not
silently expanded into independent systems.

## Publication and verification

The publication integration test accepts current semantic passes, writes the
retained result byte-for-byte, publishes its projections, and verifies complete
state. Negative tests reject a missing comparison profile and an existing
retained destination. Injecting a later legacy-output write failure rolls back
the retained copy, projections, and state together, preserving private
candidates. Ordinary rollback is tested; crash-level partial writes remain the
publication workflow's existing limitation.

- `uv run pytest -q --tb=short`: **711 passed**.
- `uv run ruff check .`: passed.
- Changed collection, instruction, type, command, and workshop Markdown:
  `commonplace-validate`, zero failures and warnings.
- Site-boundary tests confirm retained main results are publishable while local
  run results, run state, and unrelated retained reports stay excluded.
- The generic skill-creator quick validator rejects Commonplace's existing
  `argument-hint`, `context`, `model`, `type`, and `user-invocable` frontmatter.
  Those fields were not introduced here. The repository's skill validation and
  instruction-composition tests pass.

## Live population and remaining work

A default build against this checkout exits 1 at Apache Maka's generated review:
`missing or mismatched retained result; regenerate the main review`. It creates
no trial CSV. Existing generated findings were not hand-patched to make this
pass. The old production matrix and table were not changed, and no replacement
production matrix or table was generated.

The landscape skill's old procedure is limited to historical reconstruction
with its matching old parser and contracts. C04 is the next input migration;
its current refresh cannot use the old bundle with the new scripts. C15's
navigation changed only where needed to describe these new commands. C12/C14
still require duplicate legacy drafting and publication until the remaining
active consumers are resolved.
