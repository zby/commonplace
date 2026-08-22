# Recovery state

**Updated:** 2026-08-22

**Overall:** `ACTIVE`

**Resume pointer:** P3 is complete and its 942 ledger rows are terminal. The
root operator should review and commit only the ledger-defined P3 write set,
including the 325 pending tracked-source deletions and 13 new tracked-candidate
files. P4 remains pending; do not write its ADR or close the workshop as part
of the P3 commit.

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
| P3 — migrate repository data | `COMPLETE` | All 942 ledger rows are terminal; 275 ingests, 338 local assets, and 329 link occurrences have exact final parity and pass the P3 audit. |
| P4 — verify, record ADR, and close | `PENDING` | — |

## Exact next action

Review the 1,011-path P3 write set against `migration.tsv`, preserve every
dirty path outside it, and stage and commit only the P3 migration. After that
commit is accepted, start P4 by recording its own exact write set before
writing the ADR or closing the workshop.

## Active write set

P3 owns the exact 1,011-path set derived from the immutable row identities in
`migration.tsv`. The pre-execution ledger file SHA-256 is
`20b4900cab3c9f830ee8f1c36e8690312daf1f83948e49e07499912531f9517b`;
because statuses and evidence notes advance during execution, the stable
projection of `row_id`, `kind`, `source_path`, `identity`, `destination`, and
`replacement` has SHA-256
`03d4062650c769644b42f6ebaaa05f74c459d4f74c613f09fd89d8806ddf2bca`:

- the three workshop files `state.md`, `migration.tsv`, and `migrate.py`;
- every `unit` row's `source_path` and `destination`;
- every `asset` row's `destination`, plus its `source_path` only when that path
  is under `kb/sources/`;
- every `link` row's `source_path`.

The sorted unique path list produced by that definition has SHA-256
`0b2259451f736cbc036371345c761d4702a0655a628b1636ef97040a0b6083a6`
and consists of 960 `kb/sources/` paths, 42 `kb/notes/` paths, four
`kb/agent-memory-systems/` paths, one `kb/agentic-systems/` path, one
`kb/reference/` path, and the three workshop paths. The position-bias checkout
README is a read-only input, not part of the write set. Concurrent edits to
`kb/sources/COLLECTION.md`, `kb/sources/types/snapshot.md`, and every other
dirty path outside this definition remain out of scope and must be preserved.
The terminal `migration.tsv` file has SHA-256
`a91b2e9e3a9df48a14c3d2c2e2f6c304f561dba3f974a97f95cf735552d6bea3`;
its sorted immutable six-column projection still has the pre-execution hash
`03d4062650c769644b42f6ebaaa05f74c459d4f74c613f09fd89d8806ddf2bca`.
At final verification the scoped worktree has 652 visible P3 paths: 325
tracked deletions, 314 tracked modifications, and 13 untracked files. None is
staged; the 338 ignored local assets intentionally do not appear in status.

P2's completed write set was:

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
worktree file is outside the completed write set. P3's exact write set and
terminal evidence are recorded above. The source-unit proposal, ADR, and
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
| 2026-08-22 | P3 | Fresh parsing found 275 ingest units (264 tracked, 11 untracked), 267 tracked typed snapshots, 12 untracked typed snapshots, two additional tracked raw Markdown source bodies, and 56 tracked non-Markdown capture companions. The exact tracked retirement universe is therefore 269 Markdown bodies plus 56 companions. |
| 2026-08-22 | P3 | The pre-execution `migration.tsv` contains 942 unique pending rows: 275 units, 338 assets (325 tracked retirements, 12 reconciled untracked snapshots, and one position-bias materialization), and 329 durable-link occurrences from 210 authors to 198 retiring targets. Its immutable six-column row projection has SHA-256 `03d4062650c769644b42f6ebaaa05f74c459d4f74c613f09fd89d8806ddf2bca`. |
| 2026-08-22 | P3 | A fresh `python3 kb/work/ingest-and-snapshot-redesign/migrate.py verify-ledger` regeneration reported `ledger_parity PASS` with the same counts and no duplicate row ids. No corpus or link-author path was edited before this parity check. |
| 2026-08-22 | P3 | `migrate.py dry-run` passed across all 275 units, 338 assets, and 329 links: it reconstructed and locally validated each proposed ingest, hashed every current primary/retiring asset, found no destination collision, parsed eight genres, converted three code-grounded units in memory, and checked all semantic link dispositions. `.venv/bin/ruff check kb/work/ingest-and-snapshot-redesign/migrate.py` passed; `uv run` was unavailable because the host's snap-confined `uv` lacks its required capability. |
| 2026-08-22 | P3 | `migrate.py apply-all` completed in unit→link→asset order. Every row reached `complete`: 275 units, 329 link occurrences, and 338 assets. The executor copied each destination before retiring its source, refused byte-different collisions, and checkpointed each row independently. |
| 2026-08-22 | P3 | All 275 migrated ingests contain one HTTP(S) `source`, `captured`, `capture`, `genre`, and lowercase 64-character `snapshot_sha256`; zero retain `source_snapshot` or `code_revisions`. Three code-grounded ingests each contain one immutable GitHub commit secondary with role `implementation`, and the 173 capture-adapter field occurrences copied from local primaries compare equal to their source values. |
| 2026-08-22 | P3 | The final genre census is 147 `scientific-paper`, 58 `conceptual-essay`, 47 `practitioner-report`, eight `tool-announcement`, five `conversation-thread`, five `design-proposal`, three `code-repository`, and two `technical-documentation`. No directory primary or non-`implementation` secondary was admitted. |
| 2026-08-22 | P3 | Position Bias was materialized from pinned commit `483150e8e1938c17331f9e82f86e41a653286651` with checksum `a211f5c86410fd2c4fdffe50a2e29ea0b9eb4b8ac064e0919238124cdca05471`. Gentle Coding retained all three exact local documents, hashes only the designated primary (`5c99601b818bcc5461e7c7c2fe4d8776773cca417aee8775d197d0739b65bb56`), and uses the accepted “three repository documents read together” wording. |
| 2026-08-22 | P3 | The other boundary dispositions are terminal: nine ignored nested Sutskever ingests moved to the source root and use official chapter-preview URLs; the two untracked root pairs and one untracked orphan snapshot were preserved; the two raw primaries use explicit `manual`/`manual-paste` capture records; and the two former `file://` primaries use the public ASISAS track URL. |
| 2026-08-22 | P3 | A context audit reviewed all 192 external replacements across 94 authors. Every occurrence cites source/evidence rather than Commonplace analysis; existing ingest links remain separate where analysis is intended. The remaining 137 link rows remove only retired metadata-display links. Thirteen stale snapshot-facing citation labels in eight non-ingest library artifacts were corrected to name the external paper, report, article, or documentation. |
| 2026-08-22 | P3 | `migrate.py audit-final` passed: 942 terminal rows, exact 275-unit and 338-asset parity, all 329 link rows terminal, zero retiring-source or `.snapshots/` links, 275 distinct primary checksums verified, all 338 local files ignored, and all 264 formerly tracked ingests' five analytical sections byte-identical after normalizing only migrated link targets. The 11 reconciled untracked ingests retain their ledgered pre-migration hashes. |
| 2026-08-22 | P3 | Final validation of the 275 migrated ingests reported 255 clean passes, 20 passes with warnings, and zero failures. Eighteen warnings are existing links to the already-absent `kb/notes/definitions/distillation.md`; two are the schema's accepted open-genre warnings for `technical-documentation`. `commonplace-validate kb/sources` analysed 290 files with 20 warning notes and zero failures, and all 48 changed non-source link authors passed individually. |
| 2026-08-22 | P3 | Final mechanical checks passed: `.venv/bin/ruff check kb/work/ingest-and-snapshot-redesign/migrate.py`, `python3 -m py_compile`, the ledger-defined `git diff --check`, and the unchanged write-set/projection hashes. All 337 retiring source paths are absent from the worktree; the 325 formerly tracked ones are represented exactly as pending deletions for the root commit. No `.snapshots/` file is tracked or staged. |
| 2026-08-22 | P3 | Root review independently reran `migrate.py audit-final`, `commonplace-validate kb/sources`, all 48 changed non-source author validations, retired-field and tracked-cache-link searches, and the ledger-scoped `git diff --check`. It reproduced the 1,011-path write-set hash, found no staged paths, and sampled ordinary, code-grounded, Position Bias, Gentle Coding, Sutskever-chapter, and dependent-link migrations without finding scope drift. |

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
- **2026-08-22 — P3 started.** The delegated operator reread the complete
  workshop and committed P2 contracts at `05232c0b`, recorded the preliminary
  ledger-only write set, and retained the safety hold on all corpus and link
  authors until a fresh ledger proves exact universe parity.
- **2026-08-22 — P3 ledger parity proved.** The ledger reconciles tracked and
  untracked ingest/source material and names every retiring tracked source
  body or companion plus every durable link occurrence. The safety hold was
  lifted only after all 942 regenerated row identities matched; the exact
  1,011-path P3 write set is now fixed by ledger columns and hashes.
- **2026-08-22 — P3 executor audited.** A complete no-write pass reconstructed
  all migrated ingests, verified every primary and retiring asset hash,
  classified every link disposition, and found no collision. Row execution is
  ready in the strict unit-then-link-then-asset order.
- **2026-08-22 — P3 complete.** All repository source units, local assets, and
  dependent links were migrated through the recovery ledger. Final parity,
  schema/link validation, checksum and ignore checks, semantic link review,
  bounded-body comparison, lint, compile, and whitespace checks passed. The
  root operator owns review and the atomic P3 commit; P4 remains pending.
- **2026-08-22 — P3 root-reviewed.** The primary agent reproduced the final
  parity and write-set checks, independently validated the source collection
  and all changed non-source link authors, and accepted representative normal
  and boundary-case diffs. The migration remains deliberately unstaged for an
  atomic P3-only commit; P4 remains pending.
