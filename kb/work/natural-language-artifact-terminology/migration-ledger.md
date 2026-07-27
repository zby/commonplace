# Migration ledger

## Manifest

| field | value |
|---|---|
| baseline revision | `b0147dc4` |
| first implemented corpus commit | `f5a4230b` |
| failed-verification handoff and remediation start | `b2d03311` |
| first repaired corpus commit | `760bf239` |
| second-verification wording correction commit | `548f877e` |
| semantic scope | `AGENTS.md`; `kb/notes/`; `kb/reference/`; `kb/instructions/`; `kb/types/`; `kb/agent-memory-systems/`; `kb/agentic-systems/` |
| executable scope added by remediation | `src/commonplace/lib/systems_matrix.py`; `tests/commonplace/lib/test_systems_matrix.py`; `tests/commonplace/lib/fixtures/zikkaron_review.md`; generated `kb/agent-memory-systems/systems.csv` |
| excluded roots | `kb/sources/`; `kb/reports/`; `kb/articles/`; other `kb/work/` workshops |
| named exceptions | Captured versions of *Where It Lives Is Not What It Is*; named `prose` review machinery; `.replaced.*` historical review copies; quotations and historical records that must preserve source vocabulary |
| primary locator | Baseline path plus nearest Markdown heading; line numbers are convenience only |
| row-table status | Ready for a fresh independent verification: 1,903 globally unique rows, all retaining `verification: pending` |

The first verification failed because the matrix parser still encoded the old controlled vocabulary and because some editorial uses had been replaced mechanically. The first remediation retains or restores **prose** for editorial language, uses precise nouns where the category is not load-bearing, uses unhyphenated **natural language** as an ordinary noun, and reserves hyphenated **natural-language** compounds for category-bearing modifiers. The next independent verification found four wording-only leftovers; commit `548f877e` repairs those rows without changing the ledger population or dispositions.

## Coverage searches

Counts are occurrences, not matching lines. Baseline counts remain anchored to `b0147dc4`; final counts were checked again after wording-correction commit `548f877e`.

| query id | scope | query | baseline hit count | original semantic rows | repaired hit count | reconciliation |
|---|---|---|---:|---:|---:|---|
| Q1 | semantic scope | `\bprose artifacts?\b` (case-insensitive) | 13 | 13 | 0 | All seed occurrences remain migrated. |
| Q2 | semantic scope | `\bprose (form\|content\|records?\|instructions?\|memory\|knowledge\|commitments?)\b\|\bprose/symbolic\b\|\bprose-to-(code\|prose)\b` (case-insensitive) | 152 | 152 | 3 | The three survivors remain confined to two excluded `.replaced.*` historical reviews. |
| Q3 | semantic scope | `\bnatural-language (artifacts?\|form\|content\|records?\|instructions?)\b` (case-insensitive) | 4 | 4 | 295 | The increase is the intended category migration after grammar repairs; the repairs produce a net eight additional canonical-compound occurrences relative to the failed handoff. |
| Q4 | semantic scope | `\bprose\b` (case-insensitive residual audit) | 1,860 | 1,715 | 332 | The repaired result restores 12 editorial uses relative to the failed handoff; all other residual classes are unchanged. |

The three Q2 survivors are `prose knowledge` and `prose instruction` in `echowiki.replaced.2026-07-06.2.md`, and `prose instructions` in `echowiki.replaced.2026-07-06.md`. The Q4 residuals reconcile as follows:

| residual class | count | treatment |
|---|---:|---|
| ordinary or editorial survivors from the first handoff | 145 | Preserved as the obvious residual class. |
| editorial uses restored by remediation | 12 | Deliberately restored and rowed among the reopened semantic rows. |
| named machinery or locator | 73 | Preserved and rowed. |
| explicit migration rationale | 3 | Deliberately introduced, preserved, and rowed. |
| historical ADR or archived proposal | 80 | Preserved and rowed. |
| excluded historical replacement | 19 | Excluded and rowed. |
| **total** | **332** | Fully reconciled. |

## Occurrence tables

The semantic occurrence rows remain split by their original non-overlapping cohorts:

- [migration-rows-spine.md](./migration-rows-spine.md) — 57 rows for `AGENTS.md` and the vocabulary spine.
- [migration-rows-notes.md](./migration-rows-notes.md) — 273 theory-note rows.
- [migration-rows-reference-instructions-types.md](./migration-rows-reference-instructions-types.md) — 68 reference, ADR, instruction, and type rows.
- [migration-rows-external-systems.md](./migration-rows-external-systems.md) — 1,149 external-system rows.
- [migration-rows-residual-exceptions.md](./migration-rows-residual-exceptions.md) — 175 deliberate survivor rows.
- [migration-rows-executable-surface.md](./migration-rows-executable-surface.md) — 181 parser, test, fixture, and generated-output rows added by remediation.

Ellipses in excerpts delimit text from longer lines; they are not replacement text. Row IDs are globally unique across all six tables.

## Reopened and added rows

The remediation reopened 58 semantic rows:

`EX-0019`, `EX-0053`, `EX-0157`, `EX-0278`, `EX-0308`, `EX-0371`, `EX-0377`, `EX-0443`, `EX-0501`, `EX-0522`, `EX-0564`, `EX-0605`, `EX-0617`, `EX-0618`, `EX-0621`, `EX-0622`, `EX-0638`, `EX-0639`, `EX-0710`, `EX-0777`, `EX-0850`, `EX-0918`, `EX-0941`, `EX-0992`, `EX-0993`, `EX-1006`, `EX-1010`, `EX-1011`, `EX-1032`, `EX-1085`, `EX-1115`, `EX-1117`, `NT-0029`, `NT-0030`, `NT-0036`, `NT-0056`, `NT-0091`, `NT-0108`, `NT-0111`, `NT-0130`, `NT-0131`, `NT-0132`, `NT-0189`, `NT-0198`, `NT-0199`, `NT-0218`, `NT-0220`, `NT-0226`, `NT-0227`, `NT-0243`, `NT-0244`, `NT-0268`, `RT-0020`, `RT-0021`, `RT-0028`, `RT-0038`, `RT-0057`, and `SP-0012`.

It added executable rows `ES-0001`–`ES-0181`. No existing row ID was reused.

The second verification reopened four additional existing semantic rows: `EX-0001`, `NT-0109`, `NT-0123`, and `NT-0163`. Their wording and row evidence were corrected in `548f877e`; all four remain verification-pending. Across both correction passes, 62 semantic rows have therefore been reopened.

## Reconciled totals

### Semantic rows

| disposition | count |
|---|---:|
| natural-language | 1,451 |
| prompt | 1 |
| precise noun | 83 |
| preserve prose | 168 |
| excluded | 19 |
| **total** | **1,722** |

| implementation | count |
|---|---:|
| changed | 1,531 |
| preserved | 191 |
| **total** | **1,722** |

### Executable rows

| surface class | count |
|---|---:|
| source code | 4 |
| test | 14 |
| fixture | 9 |
| generated output | 154 |
| **total** | **181** |

### Whole ledger

| implementation | count |
|---|---:|
| changed | 1,712 |
| preserved | 191 |
| **total** | **1,903** |

All 1,903 rows have `verification: pending`.

## Systems-matrix evidence

`python3 scripts/build_systems_matrix.py` reported:

```text
rows written: 152  (code-grounded=152)
identity (repo/clone) joined: 149/152
flags: 1
  - atlas.md: Curation operations: `none` cannot be mixed with controlled values
```

The Atlas flag predates and is unrelated to this vocabulary migration. A read-only corpus parse then established:

- 152 current review files and 152 CSV rows;
- 152 authored `natural-language` representational-form leads and 152 populated `form_natural_language` cells;
- 94 authored `natural-language` distilled-form leads and 94 populated `df_natural_language` cells;
- 151 mixed `natural-language`/`symbolic` leads and 151 rows retaining both components;
- no representational-form or distilled-form parser flags;
- no hand-maintained CSV columns, and three newly generated current-review rows (`exo.md`, `hermes-agent.md`, and `kgai.md`) recorded as `ES-0179`–`ES-0181`.

The active parser, focused test, fixture, schema/type, and generated CSV surfaces contain no `form_prose`, `df_prose`, or controlled backticked `prose` value. No backwards-compatibility alias was added.

## Validation evidence

The remediation validation is mapped file-by-file in [changed-file-validation.md](./changed-file-validation.md).

- `commonplace-validate` passed on every repaired library Markdown artifact. Two unchanged descriptions emit pre-existing length warnings (`axes-of-artifact-analysis.md` and `system-definition-artifacts-are-crystallized-reasoning-under-context.md`); there are no validation failures.
- `commonplace-validate` passed cleanly on every changed workshop Markdown artifact.
- `pytest tests/commonplace/lib/test_systems_matrix.py -q`: 11 passed.
- `pytest -q`: 483 passed.
- `git diff --check`: clean.
- Historical *Where It Lives Is Not What It Is* captures are byte-unchanged from remediation start `b2d03311`; no named prose-review machinery changed.

The final semantic-leftover searches found zero body/editorial-frame forms, zero readability tautologies, and zero awkward verb-plus-`in natural-language` forms. The bare-preposition search has one reviewed survivor: “land in natural-language, symbolic, or distributed-parametric forms,” where all three adjectives share the trailing noun `forms`. `ordinary natural-language` has one reviewed survivor, “ordinary natural-language instructions,” where `ordinary` modifies `instructions` rather than the category name.

## Verification handoff

This execution repaired implementation and evidence; it did not perform the next independent verification. The verifier must start from the committed handoff, compare semantic wording against current corpus commit `548f877e`, rerun the migration plan’s entire protocol over the 1,722 semantic rows and 181 executable rows, and only then change verification fields. The workshop remains open and there are no unresolved implementation cases.
