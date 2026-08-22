# Recovery state

**Updated:** 2026-08-22

**Overall:** `ACTIVE`

**Resume pointer:** P2 is complete. The next operator must begin P3 by marking
only P3 `IN_PROGRESS`, recording its exact write set, and creating
`migration.tsv` from a fresh parsed corpus and link universe before changing
any source or ingest artifact.

**Safety hold:** do not remove or untrack source material until P3 has recorded
its durable fields, verified its local copy, and assigned its dependent links a
replacement.

## Fixed v1 decisions

- One URL-backed primary source per ingest.
- Zero or more secondaries; `implementation` is the only accepted v1 role.
- Implementation sources use immutable public commit identifiers.
- Source bodies are local materializations rather than tracked authorities.
- Source identity, capture metadata, genre, and the exact primary-snapshot
  checksum are durable ingest fields.
- The current ingest sections and analytical obligations remain.
- Body edits remove only information duplicated by new fields.
- A directory is not a supported primary source in v1.

Do not add postponed extensions to this state or the plan. The final ADR owns
one `Postponed` section.

## Progress marks

- `PENDING` — not started;
- `IN_PROGRESS` — active, with an exact next action and write set;
- `COMPLETE` — exit evidence recorded;
- `BLOCKED` — a named condition prevents progress.

At most one phase may be `IN_PROGRESS`.

## Phase ledger

| Phase | State | Verified result |
|---|---|---|
| P0 — baseline and recovery | `COMPLETE` | Corpus counts, affected surfaces, recovery rules, and navigation recorded. |
| P1 — write the exact v1 shape | `COMPLETE` | User accepted the validated `v1-shape.md` contract on 2026-08-22. |
| P2 — implement v1 | `COMPLETE` | The accepted schema, local cache, checksum-first resolver, capture defaults, instructions, distribution surfaces, and focused tests are implemented. |
| P3 — migrate repository data | `PENDING` | — |
| P4 — verify, record ADR, and close | `PENDING` | — |

## Exact next action

For P3, record its phase mark and write set, then generate `migration.tsv` with
one row for every freshly parsed tracked ingest, source snapshot or capture
asset, and dependent library link. Do not begin bulk edits until the ledger has
exact set parity with those regenerated universes.

## Active write set

No production phase is currently `IN_PROGRESS`. P2's completed write set was:

- `kb/work/ingest-and-snapshot-redesign/state.md`;
- `kb/sources/.gitignore`;
- `kb/sources/COLLECTION.md`;
- `kb/sources/README.md`;
- `kb/sources/types/ingest-report.md`;
- `kb/sources/types/ingest-report.schema.yaml`;
- `kb/sources/types/snapshot.md`;
- `kb/sources/types/snapshot.schema.yaml`;
- `kb/instructions/cp-skill-ingest/SKILL.md`;
- `kb/instructions/cp-skill-snapshot-web/SKILL.md`;
- `kb/instructions/ingest-paper-with-code.md`;
- `kb/instructions/ingest-directory.md`;
- `kb/instructions/re-ingest.md`;
- `src/commonplace/lib/snapshot.py`;
- `src/commonplace/lib/extraction/source_url.py`;
- `src/commonplace/lib/extraction/__init__.py`;
- `src/commonplace/cli/github_snapshot.py`;
- `src/commonplace/cli/x_snapshot.py`;
- `src/commonplace/scaffold_manifest.py`;
- `properdocs.yml`;
- `pyproject.toml`;
- `AGENTS.md`;
- `AGENTS.md.template`;
- `README.md`;
- `INSTALL.md`;
- `kb/reference/README.md`;
- `kb/reference/commands.md`;
- `kb/reference/architecture.md`;
- `kb/reference/storage-architecture.md`;
- `kb/reference/documentation-site.md`;
- `kb/reference/instruction-generation.md`;
- `kb/reference/collections-and-types.md`;
- `kb/reference/lib-modules.md`;
- `tests/commonplace/lib/test_snapshot.py`;
- `tests/commonplace/lib/extraction/test_source_url.py`;
- `tests/commonplace/cli/test_github_snapshot.py`;
- `tests/commonplace/cli/test_x_snapshot.py`;
- `tests/commonplace/cli/test_validate_notes.py`;
- `tests/commonplace/cli/test_init_project.py`;
- `tests/commonplace/docs/test_type_contract_integrity.py`;
- `tests/commonplace/docs/test_properdocs_hooks.py`;
- `tests/scenarios/ingest-a-source.md`.

`AGENTS.md` already contains an unrelated workshop-layout edit; preserve it
when reviewing or staging the P2 source-routing hunk. Every other dirty
worktree file is outside the completed write set. P3 must record its own exact
write set before touching the corpus. The source-unit proposal, ADR, and
workshop closure remain reserved for P4.

## Evidence ledger

| Date | Phase | Evidence |
|---|---|---|
| 2026-08-22 | P0 | The four workshop Markdown files passed `commonplace-validate` individually. |
| 2026-08-22 | P0 | The source-unit proposal passed `commonplace-validate` cleanly. |
| 2026-08-22 | P1 | User fixed the v1 source model, implementation-only secondary role, local source-material direction, and minimal ingest-body change. |
| 2026-08-22 | P1 | User excluded full-directory ingestion and directed that unimplemented extensions appear only as postponed items in the ADR. |
| 2026-08-22 | P1 | `v1-shape.md` fixes the field names, examples, local path, lookup rule, bounded body diff, and two irregular migrations; `commonplace-validate` passed cleanly. |
| 2026-08-22 | P1 | User moved capture metadata to the ingest and required a SHA of the primary snapshot; the shape now uses flat capture fields and an exact-file `snapshot_sha256`. |
| 2026-08-22 | P1 | After the metadata and checksum revision, all five workshop documents passed individual `commonplace-validate` checks cleanly. |
| 2026-08-22 | P1 | User accepted the v1 shape and instructed that it be committed before delegating P2. |
| 2026-08-22 | P2 | `uv run pytest tests/commonplace/lib/test_snapshot.py tests/commonplace/lib/extraction/test_source_url.py tests/commonplace/cli/test_github_snapshot.py tests/commonplace/cli/test_x_snapshot.py tests/commonplace/cli/test_validate_notes.py tests/commonplace/cli/test_init_project.py tests/commonplace/docs/test_type_contract_integrity.py tests/commonplace/docs/test_properdocs_hooks.py` passed: 134 tests. |
| 2026-08-22 | P2 | Changed production modules passed `uv run ruff check --select E4,E7,E9,F,I`; focused test modules passed `--select E4,E7,E9,F`. Adding `I` to the test-module scan exposes seven pre-existing import-order findings in unchanged import blocks, so P2 does not claim those as clean. |
| 2026-08-22 | P2 | All 18 edited KB contract, instruction, reference, and recovery-state Markdown files passed individual `commonplace-validate` runs. Full source-collection validation remains a P3/P4 check because the corpus has not been migrated to the new required fields. |
| 2026-08-22 | P2 | `uv build` produced the sdist and wheel; wheel inspection found `commonplace/_data/kb/sources/.gitignore`; the required editable `uv tool install --reinstall --python ">=3.11" --editable .` completed. |
| 2026-08-22 | P2 | `git check-ignore -v kb/sources/.snapshots/probe.md` resolved to the nested `.snapshots/` rule, and `git diff --check` reported no whitespace errors. |
| 2026-08-22 | P2 | Root review independently reran all 134 focused tests and all 18 edited KB-document validations cleanly, inspected the contract/runtime diff, and confirmed that no corpus artifact or P3/P4 file entered the P2 change set. |

## Event log

- **2026-08-22 — workshop opened.** Baseline and recovery state recorded; no
  implementation started.
- **2026-08-22 — plan reduced to minimal v1.** Removed the semantic-decision
  survey, separate feature phases, generalized pilots, and future-work backlog.
  P1 now writes exact examples for decisions already made.
- **2026-08-22 — v1 shape written.** Reused top-level `source`, moved `genre`
  to the ingest, represented implementations through `secondary_sources`, and
  selected ignored `.snapshots/` storage with URL lookup. P1 remains open only
  for user acceptance or corrections.
- **2026-08-22 — durable capture record expanded.** Moved capture time,
  mechanism, and adapter-provided metadata to the ingest; added an exact-file
  SHA-256 and checksum-first local lookup. No production implementation began.
- **2026-08-22 — P1 accepted.** User accepted the exact v1 shape. P2 remains
  pending until its delegated operator records the production write set.
- **2026-08-22 — P2 started.** The delegated operator recorded the exact
  contract, runtime, instruction, distribution, documentation, and test write
  set before production edits. Corpus migration and decision recording remain
  reserved for P3 and P4.
- **2026-08-22 — P2 complete.** Ingests now own the durable primary URL,
  capture fields, ingest-read genre, exact primary Markdown checksum, and the
  optional implementation-only secondary list. Local captures default to the
  ignored `.snapshots/` directory; checksum-first resolution exposes exact,
  duplicate, changed, and unavailable states without mutating the ingest.
  Focused schema, runtime, adapter, scaffold, publication, and documentation
  checks passed. No corpus artifact, migration ledger, proposal, or ADR was
  changed.
- **2026-08-22 — P2 root-reviewed.** The primary agent independently reran the
  focused suite, corrected an overbroad lint-evidence statement, and accepted
  the implementation diff. P3 remains pending.
