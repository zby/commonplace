# Migration ledger

## Manifest

| field | value |
|---|---|
| baseline revision | `b0147dc4` |
| implemented corpus commit | `f5a4230b` |
| included roots | `AGENTS.md`; `kb/notes/`; `kb/reference/`; `kb/instructions/`; `kb/types/`; `kb/agent-memory-systems/`; `kb/agentic-systems/` |
| excluded roots | `kb/sources/`; `kb/reports/`; `kb/articles/`; `kb/work/` other than this migration ledger and lessons record |
| named exceptions | Captured versions of *Where It Lives Is Not What It Is*: `kb/sources/where-it-lives-architectural-vocabulary-retained-adaptation.md` and `kb/sources/where-it-lives-retained-adaptation-2026-06-23.md`; named `prose` review machinery; `.replaced.*` historical review copies; quotations and historical records that must preserve source vocabulary |
| primary locator | Baseline path plus nearest Markdown heading; line numbers are convenience only |
| row-table status | Complete implementation handoff; 1,722 rows, all retaining `verification: pending` for the independent session |

The decision order is: use a precise artifact name when available; use **prompt** only for material supplied or explicitly assembled as model input; otherwise use the appropriate **natural-language** category term when representational form matters; preserve **prose** for editorial, quoted, historical, or named-machinery uses.

## Baseline coverage

Counts are occurrences, not matching lines. The targeted queries are intentionally non-overlapping; the broad query contains both targeted sets.

| query id | scope | query | baseline hit count | ledger-row count | final hit count | reconciliation |
|---|---|---|---:|---:|---:|---|
| Q1 | included roots | `\bprose artifacts?\b` (case-insensitive) | 13 | 13 | 0 | Reconciled: all 13 seed occurrences have implementation rows and none survive. |
| Q2 | included roots | `\bprose (form\|content\|records?\|instructions?\|memory\|knowledge\|commitments?)\b\|\bprose/symbolic\b\|\bprose-to-(code\|prose)\b` (case-insensitive) | 152 | 152 | 3 | Reconciled: 149 changed; 3 survive only in excluded `.replaced.*` historical reviews and have exception rows. |
| Q3 | included roots | `\bnatural-language (artifacts?\|form\|content\|records?\|instructions?)\b` (case-insensitive) | 4 | 4 | 287 | Reconciled: the 4 pre-existing canonical-compatible uses have preserved comparison rows; the increase is the intended migration result. |
| Q4 | included roots | `\bprose\b` (case-insensitive residual audit) | 1860 | 1715 | 320 | Reconciled: 1,543 baseline occurrences changed, 172 non-obvious baseline survivors have rows, and 145 ordinary/editorial survivors form the counted obvious class. Three additional rowed occurrences were introduced inside the explicit revision rationale, so total handoff rows do not equal this baseline count. |

The broader baseline contains 1,860 occurrences across 364 files. Q3 has 4 hits under the narrower workshop query (the broader token `natural-language` occurs 59 times); these pre-existing canonical-compatible uses are comparison evidence rather than replacement candidates unless an edit changes them.

## Occurrence tables

The occurrence rows are split by cohort:

- [migration-rows-spine.md](./migration-rows-spine.md) — 57 rows for `AGENTS.md` and the six vocabulary-spine artifacts.
- [migration-rows-notes.md](./migration-rows-notes.md) — 273 rows for remaining theory notes, including all four Q3 comparison rows.
- [migration-rows-reference-instructions-types.md](./migration-rows-reference-instructions-types.md) — 68 rows for current reference documentation, ADRs, instructions, and type guidance.
- [migration-rows-external-systems.md](./migration-rows-external-systems.md) — 1,149 rows for agent-memory-system and agentic-system reviews/analyses.
- [migration-rows-residual-exceptions.md](./migration-rows-residual-exceptions.md) — 175 non-obvious deliberate survivors: 172 baseline survivors plus three occurrences introduced by the durable revision rationale.

Row IDs are globally unique. Each source file belongs to one cohort table only; the residual-exceptions table records survivor rows but does not own or edit those source files.

Ellipses in `original text` and `expected final text` delimit exact excerpts from longer lines; they are not replacement text. Each excerpt retains enough neighboring text to reconstruct the occurrence from its stable locator.

## Disposition totals

| disposition | count |
|---|---:|
| natural-language | 1,482 |
| prompt | 1 |
| precise noun | 64 |
| preserve prose | 156 |
| excluded | 19 |
| **total** | **1,722** |

## Implementation totals

| implementation | count |
|---|---:|
| changed | 1,543 |
| preserved | 179 |
| pending | 0 |
| **total** | **1,722** |

## Changed-file validation

The complete 260-file corpus mapping and eight handoff-control rows are in [changed-file-validation.md](./changed-file-validation.md). The final library batch invoked `commonplace-validate` on 259 changed KB artifacts and produced 309 clean validation results after dependency checks; `AGENTS.md` is covered by diff inspection and `git diff --check`.

## Final search and validation evidence

Final targeted counts are Q1 `0`, Q2 `3`, Q3 `287`, and Q4 `320`. The three Q2 survivors are:

- `kb/agent-memory-systems/reviews/echowiki.replaced.2026-07-06.2.md` — `prose knowledge` and `prose instruction`;
- `kb/agent-memory-systems/reviews/echowiki.replaced.2026-07-06.md` — `prose instructions`.

All are excluded historical replacement reviews. The 320 broad residual occurrences were classified as follows:

| residual class | count | treatment |
|---|---:|---|
| ordinary or editorial | 145 | Preserved as the expected obvious residual class; no per-occurrence row required. |
| named machinery or locator | 73 | Preserved and rowed. |
| explicit migration rationale | 3 | Introduced deliberately, preserved, and rowed. |
| historical ADR or archived proposal | 80 | Preserved and rowed. |
| excluded historical replacement | 19 | Excluded and rowed. |
| **total** | **320** | Fully reconciled. |

`git diff --check` is clean. No implementation, schema, validator, or other executable surface changed, so the full Python test suite was not required by the plan.

## Verification handoff

Independent verification is intentionally not part of this execution session. Every occurrence row says `pending` in its verification column. The verifier should read the ledger and row tables from the handoff commit, compare implemented wording against corpus commit `f5a4230b`, rerun the four searches, and verify the whole-ledger totals before changing any verification field. There are no unresolved implementation cases.
