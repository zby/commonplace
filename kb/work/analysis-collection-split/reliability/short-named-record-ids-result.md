# Short named record IDs implementation result

Implemented on 2026-10-04 under the [commission](./short-named-record-ids-plan.md).
[ADR 104](../../../reference/adr/104-name-analysis-records-with-stable-short-handles.md)
carries the decision and literal TODO revisit condition. No analysis or
regeneration was run. The first analysis under this contract remains separately
commissioned work.

## Naming check before implementation

The [preflight naming check](./short-named-record-ids-naming-check.json) records
all fifty declarations, their labels, member locations, source-identity text,
proposed handles and frozen member hashes. It was written before parser mutation.
The source sets were read without rewriting them.

| Retained Dynamic Cheatsheet set | Records | Qualified | Source words dropped | No single source-native name | Unnameable | Token collisions |
|---|---:|---:|---:|---:|---:|---:|
| 2026-10-02, run 01 | 30 | 2 | 1 | 6 | 0 | 0 |
| 2026-10-03, run 02 | 20 | 1 | 0 | 2 | 0 | 0 |

Counts are deliberate classifications, not a mechanical extraction. Qualifiers
identify a generic source name or a separately analysed part. Dropped words count
abbreviation of a longer source identifier, not shortening of an analyst label.
No single source-native name includes composite or unidentified referents; it
does not mean that their source passages lack identity evidence. Such records
received suggestions from their roles, inputs or labels, without a fallback rule.

The preflight shortened `generator_outputs_so_far` to `generator-outputs`.
The [recorded refinement](./short-named-record-ids-naming-refinement.json) keeps
three distinguishing source words instead: `EPI-OBJ-generator-outputs-far`.
The original preflight remains intact as the chronology witness. Counts and
feasibility are unchanged; the refined list still has no duplicate or prefix
collision. Neither list is a migration map applied to retained sets.

## Implemented behavior

The shared parser recognizes whole candidate tokens, then checks one to three
lowercase hyphenated words whose first characters are letters. Digits may follow
letters. Numeric suffixes, digit-only words, uppercase names, excessive words,
underscores and dangling or repeated hyphens are refused. Analyst and kind
prefixes retain their controlled values.

Declarations, annotations, amendments, supersessions, part relations, route
fields, route statuses and evidenced absences use the named grammar. Set
resolution and profile citations share canonical declarations. Duplicate IDs
and same-namespace token-prefix collisions fail acceptance. An attached word
such as `MEM-OBJ-sheet-based` is checked whole and cannot resolve as `MEM-OBJ-sheet`.
The collision refusal explains its rule; worker instructions do not repeat it.

Named `through`, en dash, em dash, ASCII dash and ordinary `to` grouping resolve
the written endpoints. Code neither expands membership nor judges the grouped
claim. For an adjacent ASCII dash, a following full uppercase analyst/kind prefix
marks the second endpoint; an attached lowercase word stays in the first token.
Single-ID fields reject grouped values. Structured profile arrays still require
individual declared IDs. Numbered source IDs retain their range refusals, with a
source-specific diagnostic. Source quotations and fenced excerpts stay excluded.

An unresolved reference remains a refusal. Exact matches under other analyst
prefixes retain their existing hint. Otherwise the optional nearest-name hint
compares suffixes only within the same analyst and kind, with a similarity cutoff
of 0.6. Hints never rewrite or accept references.

Analysts choose names. The shared contract gives source-name conversion and label
rules once, keeps IDs stable across corrections, and forbids reuse of a dropped
handle for a different referent. No allocator, rename tool, migration or dual-format
reader was added.

## Consumer packet and inventory disposition

The [pre-mutation inventory](./short-named-record-ids-inventory.json) retains
search patterns and hits. The [final rescan](./short-named-record-ids-rescan.json)
records scoped searches with hidden and ignored files included. It leaves five
numeric-ID lines: three historical ADR 096 examples, now explicitly marked
amended, and two source-exclusion test strings. Current worker instructions,
types, positive fixtures and production code contain no numeric record IDs.
The full suite also exposed a fixture-only numeric substitution pattern for
noncomplete sets; it now removes named references before deleting member files.

| Consumer class / packet field | Disposition |
|---|---|
| Authoritative declaration and enforcement | Shared record contract and parser; grammar and identity checks at member/set acceptance; semantic naming suitability remains review work. |
| Resolvers and validators | Parser updated; workflow, validation and ledger consume its declarations and reference checks. Route/status/absence recognizers updated with the same grammar. |
| Schemas and derived constraints | No record-suffix schema constants found. Run IDs, source IDs and source anchor line numbers remain numeric. Profile record arrays resolve against declarations. |
| Emitters | Analysts author records under the shared contract. Amendment indexing reads named IDs. Code allocates no record names. |
| Migration scripts | None required or authorized; current retained population is empty. |
| Skills, rules, jobs, types and templates | Canonical contract updated once; runtime examples updated; memory allocation wording replaced; reconciliation example shortened; verification source guidance retained. Existing skill projections resolve to the canonical collection. |
| Control plane | Root instructions and init templates do not specify record suffix grammar. No changes needed. |
| References and ADRs | ADR 104 states the choice; ADR 096 is marked amended while retaining historical examples. Analytical definitions and ownership rules are unchanged. |
| Tests and fixtures | Positive member, profile, ledger, workflow and matrix fixtures use names; refusal tests cover the new boundary. Fixture file inventory is [retained](./short-named-record-ids-changed-fixtures.json). |
| Published views | No suffix-specific site or redirect consumer found. Existing views render member content; no published corpus regeneration authorized. |
| Byte pins | Worker hashes/bytes measured below; no historical member or manifest rewritten or re-pinned. New runs pin their method commit as before. |
| Spellings | Preflight searched literal IDs, numeric regexes and allocation/range wording; rescan checks active code, tests, projections and references. Frozen reports and workshop history remain deliberate witnesses. |
| Generated/projected forms | Editable installation reads canonical checkout files; skill projections remain valid. Scratch init and pointer checks pass. No generated analysis requested. |
| Fresh/existing installations | Scratch init validates. Re-running with a plain historical numeric-ID witness preserves its bytes; pointer check and validation pass. Init does not migrate KB content. Checkout changes are direct. |
| Diagnostics and acceptance probe | Parser tests exercise invalid names, duplicates, collisions, unresolved endpoints and nearest hints. A complete named set including its profile validates through the public CLI in a scratch repository. |
| Drift guard | Existing contract/route-field comparison and complete-set/profile/workflow tests run under the new grammar. No code name generator or second grammar exists to synchronize. |
| Historical witnesses | Old reports remain behind their validation-exclusion marker; ADR 096 marks its examples historical; source-exclusion fixtures intentionally quote old forms. |
| Identity conventions and exclusions | Analyst/kind prefixes and Shared records level-four headings stay authoritative; quotes/fences cannot declare or supply fields. Profile arrays resolve against this same declaration set. |
| Relocation effects | No relocation. |

## Worker input measurements

The [byte baseline](./short-named-record-ids-byte-baseline.json) was saved before
mutation. [Final measurements](./short-named-record-ids-measurements.json) retain
bytes and SHA-256 before and after for every worker instruction and member type,
including unchanged files. Every file meets its bound.

| Affected file | Before bytes | After bytes | Net |
|---|---:|---:|---:|
| Shared record contract | 14,473 | 15,168 | +695 |
| Memory job | 4,549 | 4,537 | −12 |
| Reconciliation job | 4,334 | 4,250 | −84 |
| Runtime job | 2,760 | 2,720 | −40 |
| Record verification job | 5,802 | 5,730 | −72 |
| Synthesis verification job | 2,176 | 2,104 | −72 |
| Runtime member type | 3,456 | 3,425 | −31 |

The shared contract stays below 700 bytes net growth. All other measured worker
files have zero or negative net growth. Reduced text removes redundant examples
and allocation/range instructions; it preserves evidence, status and identity
comparison requirements.

## Verification and limits

- `uv run pytest -q`: **1,034 passed**, including complete named-set publication,
  profile citations, supersessions, amendments, absence evidence and refusals.
- `uv run ruff check .`: passed. `git diff --check`: passed.
- `commonplace-validate kb/agentic-system-analyses --json`: 28 artifacts,
  zero failures and warnings.
- ADR 104 and amended ADR 096 each validate with zero failures and warnings.
- Complete named fixture set, including `memory-profile.md`, validates with
  zero failures and warnings through `commonplace-validate` in a scratch repository.
- Fresh and refreshed scratch installations validate with zero failures and
  warnings; `commonplace-init --check` passes. No init was run in this checkout.
- Every preflight frozen-member hash still matches. The 218-file historical
  reports aggregate remains
  `d9b45e24be4baa2ab97c2672bdabcd208b33fa8d162c47ca1cc6216168fed676`.
  Its exact recipe is in the measurement record and the collection-split result.

Fixtures establish parser behavior, not analyst naming quality or fewer reference
errors. Future commissioned analyses must count source-range refusals, unresolved
or altered references, collisions, within-job repairs and retries separately.
Semantic grouping faults are separate observations; permitted named grouping is
not itself an error. ADR 104 retains the literal TODO and all five revisit triggers.
