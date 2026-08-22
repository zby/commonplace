# Initial inventory

**Measured:** 2026-08-22

This is a planning baseline, not a completion ledger. The checkout was already
dirty and contains untracked source work, so worktree and Git-tracked counts are
reported separately. P3 must regenerate the exact migration universes before
bulk edits.

## Current allocation of responsibility

| Concern | Current authority or behavior | Migration consequence |
|---|---|---|
| Canonical external URL | snapshot `source` frontmatter | must become recoverable without a tracked snapshot |
| Capture time and mechanism | snapshot `captured` and `capture` | move to the tracked ingest as durable provenance |
| Adapter capture metadata | optional snapshot fields such as `status_id`, `conversation_id`, `post_count`, and `api_url` | copy capture-generated values to the ingest under their current flat names |
| Genre | snapshot `genre`, per ADR 045 | move to the tracked ingest as the durable authority |
| Source body | tracked snapshot Markdown and related assets | preserve locally before any current-tree removal and anchor the primary Markdown file with `snapshot_sha256` |
| KB-relative analysis | adjacent `.ingest.md` | preserve its current analytical shape; remove only direct restatements of new durable fields |
| Ingest identity | singular `source_snapshot` path | replace with durable primary identity under the selected model |
| Code grounding | optional `code_revisions` plus required section | migrate into the first operative secondary role without losing commit pins |
| Canonical URL extraction | direct `source`, then recursive `source_snapshot` lookup | teach consumers the new durable ingest representation |
| Publication | exclude snapshots, re-include ingests and source contracts | simplify or restate after local-only materialization |
| Re-ingestion | requires the snapshot file to exist | add checksum-first local lookup, refetch, and explicit mismatch semantics |

## Corpus baseline

The counts below parse only the first frontmatter block. Simple `rg '^type:'`
counts are higher because type specs and templates contain example `type:`
lines in their bodies.

| Class | Worktree files | Worktree bytes | Worktree median words | Tracked files | Tracked bytes | Tracked median words |
|---|---:|---:|---:|---:|---:|---:|
| typed ingest reports | 275 | 2,582,480 | 1,272 | 264 | 2,517,348 | 1,280 |
| typed source snapshots | 269 | 13,401,243 | 3,729 | 257 | 12,615,156 | 3,432 |

Additional tracked material under `kb/sources/`:

- 21 Markdown files not classified as either shipped source type, totaling
  305,943 bytes;
- 59 non-Markdown files, totaling 3,253,932 bytes;
- 264 filenames ending in `.ingest.md` and 279 other tracked Markdown
  filenames. Filename and parsed-type counts differ, so migration must use
  parsed artifacts rather than suffixes alone.

All 275 parsed worktree ingests have a `source_snapshot` value. Of those, 273
resolve to an existing file. Two are known exceptions:

- `position-bias.ingest.md` points to `kb/sources/position-bias/`;
- `gentle-coding.ingest.md` stores a prose description of a grouped source
  rather than one path.

Three tracked ingests currently carry `code_revisions`:

- `intern-s2-mobius-arxiv-v1.ingest.md`;
- `scienceflow-long-horizon-agent-for-ml-research-and-discovery.ingest.md`;
- `spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md`.

These counts establish scale. This version does not mechanically shorten long
ingests. P1 fixes a representative minimal body diff; P3 then records a
field-dedup disposition for every ingest.

## Link baseline

A read-only Markdown-link scan, excluding `kb/sources/`, `kb/work/`, and
`kb/reports/` as link authors, found:

| Target class | Link occurrences | Author files | Distinct targets |
|---|---:|---:|---:|
| source snapshots | 125 | 57 | 59 |
| ingest reports | 259 | 85 | 104 |

Within ingest reports, a separate scan found 231 Markdown links from 163 files
to 181 non-ingest source targets. These are in addition to frontmatter
`source_snapshot` pointers. Some are source citations; others may be template
or navigation links. They require classification before source bodies retire.

The link baseline is intentionally semantic. Replacing every snapshot target
with an ingest would change a citation from “the source says this” to
“Commonplace's analysis says this.” P3 therefore records each link in the
single migration ledger.

## Primary affected surfaces

### Decisions and contracts

- `kb/reference/proposals/ingest-source-units-and-supporting-material.md`
- `kb/reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md`
- `kb/sources/COLLECTION.md`
- `kb/sources/types/ingest-report.md`
- `kb/sources/types/ingest-report.schema.yaml`
- `kb/sources/types/snapshot.md`
- `kb/sources/types/snapshot.schema.yaml`

### Procedures

- `kb/instructions/cp-skill-ingest/SKILL.md`
- `kb/instructions/cp-skill-snapshot-web/SKILL.md`
- `kb/instructions/ingest-paper-with-code.md`
- `kb/instructions/ingest-directory.md`
- `kb/instructions/re-ingest.md`

The current ingest skill requires connection discovery, a fixed-decomposition
lens for every experiment-bearing source, six report sections, three to seven
extractable-value items, effort tags, and exactly one next action. Those
obligations remain in this version. The only body deletions are lines whose
information has moved into durable fields; broader readability work is
deferred.

### Runtime code

- `src/commonplace/cli/github_snapshot.py`
- `src/commonplace/cli/x_snapshot.py`
- `src/commonplace/lib/snapshot.py`
- `src/commonplace/lib/extraction/source_url.py`
- `src/commonplace/lib/extraction/__init__.py`
- generic validation code only if the adopted schema needs an invariant JSON
  Schema cannot express clearly

Both capture CLIs currently default to `kb/sources`, stamp the snapshot type,
deduplicate by scanning Markdown in that directory, and report `Snapshot
saved:` paths. The ordinary web and PDF branches encode the same destination in
the snapshot skill rather than a shared runtime adapter.

Do not include `src/commonplace/freshness/`, `src/commonplace/review/`, or the
Commonplace store merely because they use the word `snapshot`. Those are
review-input artifact snapshots and are outside this workshop.

### Tests

- `tests/commonplace/cli/test_github_snapshot.py`
- `tests/commonplace/cli/test_x_snapshot.py`
- `tests/commonplace/lib/test_snapshot.py`
- `tests/commonplace/lib/extraction/test_source_url.py`
- source cases in `tests/commonplace/cli/test_validate_notes.py`
- `tests/commonplace/docs/test_type_contract_integrity.py`
- `tests/commonplace/docs/test_properdocs_hooks.py`
- scaffold/install tests if shipped paths or source type files change

### Distribution and documentation

- `.gitignore`
- `properdocs.yml`
- `src/commonplace/docs/properdocs_hooks.py`
- `src/commonplace/scaffold_manifest.py`
- `pyproject.toml` package and command surfaces
- `AGENTS.md` source routing and command descriptions
- `kb/reference/available-types.md`
- source/capture sections in `kb/reference/commands.md`, architecture, storage,
  and installation documentation found by a fresh P2 search

The current docs site excludes `sources/**` and then re-includes ingests,
collection docs, and type specs. The current ignore file has only isolated
source exceptions; it has no general local source-cache rule.

### Corpus

- every parsed `ingest-report` and `snapshot` under `kb/sources/`;
- raw JSON, images, PDFs, and untyped/grouped captures;
- all `source_snapshot` and `code_revisions` metadata;
- inbound links from notes, reference, instructions, articles, and external
  system collections;
- source-to-source links whose target will no longer be tracked.

## Migration hazards

- **Authority loss:** deleting a snapshot before moving its URL, genre, and
  version facts can leave an ingest unable to identify its source.
- **Local-copy loss:** a tracked-file removal can also remove the only working
  copy unless cache preservation happens first.
- **Mutable refetch:** re-running capture later does not guarantee the same
  article bytes. A checksum mismatch must expose the new observation rather
  than silently replacing the one that grounded the ingest.
- **False copyright confidence:** local-only storage reduces redistribution by
  this repository; it does not determine upstream license, quotation, or fair
  use questions.
- **Citation drift:** ingest and source links are not interchangeable.
- **Schema overreach:** a flexible secondary list can imply support for roles
  no consumer understands.
- **Validation overclaim:** structural acceptance cannot prove that a repository
  implements a paper.
- **Name collision:** global searches for `snapshot` pull in the unrelated
  review freshness subsystem.
- **Dirty baseline:** current untracked source artifacts mean deletion and
  migration universes must be regenerated from parsed files, then reconciled
  with `git ls-files`.

## Refresh recipes

Cheap searches for the next phase:

```bash
rg -n "source_snapshot|code_revisions" kb/instructions kb/reference src tests
rg -n "kb/sources/types/snapshot.md|Snapshot saved:|Already snapshotted:" \
  kb/instructions kb/reference src tests
rg -n "genre.*snapshot|snapshot.*genre" kb/reference kb/instructions kb/sources/types
git status --short
git ls-files kb/sources
```

P3 must turn the frontmatter and Markdown-link measurement used for this
baseline into `migration.tsv` before bulk edits. Do not copy aggregate numbers
forward as if they were a durable item list.
