# Migration ledger

## Manifest

| field | value |
|---|---|
| baseline revision | `b0147dc4` |
| included roots | `AGENTS.md`; `kb/notes/`; `kb/reference/`; `kb/instructions/`; `kb/types/`; `kb/agent-memory-systems/`; `kb/agentic-systems/` |
| excluded roots | `kb/sources/`; `kb/reports/`; `kb/articles/`; `kb/work/` other than this migration ledger and lessons record |
| named exceptions | Captured versions of *Where It Lives Is Not What It Is*: `kb/sources/where-it-lives-architectural-vocabulary-retained-adaptation.md` and `kb/sources/where-it-lives-retained-adaptation-2026-06-23.md`; named `prose` review machinery; quotations and historical records that must preserve source vocabulary |
| primary locator | Baseline path plus nearest Markdown heading; line numbers are convenience only |
| row-table status | Pending population after the classification pass; every implementation row will retain `verification: pending` for the independent session |

The decision order is: use a precise artifact name when available; use **prompt** only for material supplied or explicitly assembled as model input; otherwise use the appropriate **natural-language** category term when representational form matters; preserve **prose** for editorial, quoted, historical, or named-machinery uses.

## Baseline coverage

Counts are occurrences, not matching lines. The targeted queries are intentionally non-overlapping; the broad query contains both targeted sets.

| query id | scope | query | baseline hit count | ledger-row count | final hit count | reconciliation |
|---|---|---|---:|---:|---:|---|
| Q1 | included roots | `\bprose artifacts?\b` (case-insensitive) | 13 | pending | pending | pending |
| Q2 | included roots | `\bprose (form\|content\|records?\|instructions?\|memory\|knowledge\|commitments?)\b\|\bprose/symbolic\b\|\bprose-to-(code\|prose)\b` (case-insensitive) | 152 | pending | pending | pending |
| Q3 | included roots | `\bnatural-language (artifacts?\|form\|content\|records?\|instructions?)\b` (case-insensitive) | 4 | pending | pending | pending |
| Q4 | included roots | `\bprose\b` (case-insensitive residual audit) | 1860 | pending | pending | pending |

The broader baseline contains 1,860 occurrences across 364 files. Q3 has 4 hits under the narrower workshop query (the broader token `natural-language` occurs 59 times); these pre-existing canonical-compatible uses are comparison evidence rather than replacement candidates unless an edit changes them.

## Occurrence tables

The non-overlapping row tables will be populated by cohort:

- `migration-rows-spine.md` — `AGENTS.md` and the six vocabulary-spine artifacts.
- `migration-rows-notes.md` — remaining theory notes.
- `migration-rows-reference-instructions-types.md` — current reference documentation, ADRs, instructions, and type guidance.
- `migration-rows-external-systems.md` — agent-memory-system and agentic-system reviews/analyses.
- `migration-rows-residual-exceptions.md` — non-obvious deliberate survivors discovered by the broad residual audit.

Row IDs are globally unique. Each source file belongs to one cohort table only; the residual-exceptions table records survivor rows but does not own or edit those source files.

## Disposition totals

| disposition | count |
|---|---:|
| natural-language | pending |
| prompt | pending |
| precise noun | pending |
| preserve prose | pending |
| excluded | pending |

## Implementation totals

| implementation | count |
|---|---:|
| changed | pending |
| preserved | pending |
| pending | pending |

## Changed-file validation

| changed file | row IDs | deterministic validation result |
|---|---|---|
| pending | pending | pending |

## Final search and validation evidence

Pending implementation, residual audit, and deterministic validation.

## Verification handoff

Independent verification is intentionally not part of this execution session. Every occurrence row must still say `pending` in its verification column when the implementation handoff is committed.
