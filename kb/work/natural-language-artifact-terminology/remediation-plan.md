# Verification-remediation plan

This plan repairs the leftovers found by the first independent verification of the `prose` → `natural-language` migration. It is a correction pass over the existing migration, not a new terminology decision.

## Execution contract

The one-line goal is:

> Execute `kb/work/natural-language-artifact-terminology/remediation-plan.md`.

An agent given that goal owns steps 1–7 below. It must begin from the committed verification handoff, preserve unrelated work, update the corpus and migration evidence together, and finish with a committed handoff for a new independent verification session. It must not mark rows `verified` or close the workshop.

## 1. Reopen the failed verification

Record the starting revision and treat the first verification as failed for two independent reasons:

1. active review/type documents use the controlled token `natural-language`, while the systems-matrix parser, tests, fixture, and generated CSV still encode `prose`;
2. some editorial uses were misclassified as representational-category uses and replaced with awkward or incorrect wording.

At minimum, reopen `NT-0029`, `EX-0053`, `EX-0501`, and `EX-1006`. These are examples, not an exhaustive repair list.

## 2. Audit the semantic leftovers

Review every changed occurrence whose baseline or result uses an editorial frame such as:

- `in prose` / `in natural-language`;
- `body prose` / `body natural-language`;
- `editorial prose` / `editorial natural-language`;
- `ordinary prose` / `ordinary natural-language`;
- bare `natural-language` after prepositions or where a concrete noun is required.

Use the original decision order rather than a reverse bulk replacement:

1. retain or restore **prose** for genuinely editorial wording;
2. use the precise noun when the sentence is about text, documentation, a body, a description, or another concrete artifact rather than the representational category;
3. use **natural language** as ordinary unhyphenated English where that is what the grammar requires;
4. use a canonical compound such as **natural-language content**, **natural-language form**, or **natural-language instruction** when the representational category is load-bearing.

Inspect each match in its full sentence and note context. Update the affected occurrence row's semantic class, disposition, expected final text, rationale, and implementation state to agree with the repaired corpus. Keep verification `pending`.

Luna subagents may apply already-classified corrections in non-overlapping files, but the primary agent owns classification, the shared ledger, and review of every resulting diff.

## 3. Migrate the executable vocabulary surface

Make the systems-matrix contract agree with the active review type:

- recognize the controlled token `natural-language` for `Representational form` and `Distilled form`;
- rename `form_prose` to `form_natural_language` and `df_prose` to `df_natural_language` in the parser, column schema, tests, fixtures, and generated CSV;
- emit `natural-language` in the derived `representational_form` value;
- do not add a backwards-compatibility alias for `prose`;
- update any active documentation or code that names the old columns or controlled value.

Search the whole repository for `form_prose`, `df_prose`, controlled backticked `` `prose` `` values, and `representational_form` expectations before declaring this surface complete. Preserve historical sources, `.replaced.*` review copies, and the named prose-review machinery unless they are active parser fixtures or contracts.

Add an executable-surface batch table to the migration ledger for these newly in-scope occurrences. Its rows must distinguish source code, tests/fixtures, and generated output, and must retain `verification: pending`.

## 4. Regenerate and inspect the systems matrix

Run `python3 scripts/build_systems_matrix.py` only after the parser and tests are updated. Inspect both its reported flags and the CSV diff.

Acceptance conditions for this step:

- all current review `natural-language` lead tokens populate their corresponding one-hot columns;
- mixed rows retain every component rather than silently dropping the natural-language component;
- no `Representational form` or `Distilled form` off-vocabulary/missing-controlled-value flag is caused by this migration;
- the CSV header and derived values use the new vocabulary;
- unrelated hand-maintained columns survive regeneration;
- unrelated pre-existing flags are reported separately rather than hidden or attributed to the migration.

Add or revise tests so a corpus-shaped `natural-language`-only row and a mixed `natural-language`/`symbolic` row would fail if the component were dropped again.

## 5. Reconcile the migration evidence

Update the manifest, occurrence totals, coverage searches, changed-file table, and validation evidence after all repairs. Recompute counts from the new result rather than carrying forward the previous handoff's Q1–Q4 totals.

The changed-file table must now cover:

- repaired library Markdown;
- updated row tables and manifest;
- parser and builder code if changed;
- tests and active fixtures;
- regenerated `systems.csv`.

Every changed or deliberately restored occurrence needs a row. Row IDs remain globally unique, batch ownership remains non-overlapping, and all verification fields remain `pending`.

## 6. Validate the repaired result

Run:

- `commonplace-validate` on every changed KB Markdown artifact;
- the focused systems-matrix tests;
- the full `pytest` suite;
- `git diff --check`;
- the original Q1–Q4 searches plus the semantic-leftover searches from step 2;
- a read-only corpus parse confirming the counts of recognized `natural-language` form and distilled-form tokens equal the counts present in current review lead lines.

Inspect the complete diff for semantic drift and confirm again that the historical **Where It Lives Is Not What It Is** captures remain unchanged.

## 7. Prepare a fresh verification handoff

Commit the corrections and reconciled evidence with explicit paths. Report:

- starting and result revisions;
- every reopened or newly added row ID;
- revised manifest and coverage totals;
- systems-matrix regeneration output and any surviving unrelated flags;
- deterministic validation and test results;
- final semantic-leftover search results.

Stop with verification still pending. A separate session must rerun the entire independent verification protocol from the original [migration plan](./plan.md), including all original and executable-surface rows. Workshop closure remains conditional on that whole-table verification succeeding.

## Completion criteria

The remediation implementation is ready for independent verification only when:

1. every semantic leftover is correctly classified and worded;
2. parser, tests, fixtures, and generated matrix use the same controlled vocabulary as the review type;
3. no natural-language component is dropped from matrix data;
4. all tables and counts reconcile with the repaired result;
5. validation and the full test suite pass;
6. the historical article captures and named prose-review machinery remain preserved.
