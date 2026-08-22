# Recovery state

**Updated:** 2026-08-22

**Overall:** `ACTIVE`

**Resume pointer:** P2 handoff — P1 is accepted. The P2 operator must mark P2
`IN_PROGRESS`, record its exact production write set, and implement the
accepted `v1-shape.md` contract without expanding scope.

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
| P2 — implement v1 | `PENDING` | — |
| P3 — migrate repository data | `PENDING` | — |
| P4 — verify, record ADR, and close | `PENDING` | — |

## Exact next action

Begin P2. First mark it `IN_PROGRESS` and replace the inactive write-set text
below with the exact files owned by the implementation. Then implement the six
accepted choices in `v1-shape.md`. Do not write another options survey or
companion proposal.

## Active write set

No production write set is active. P1 may edit only:

- `kb/work/ingest-and-snapshot-redesign/v1-shape.md`;
- these workshop state files;
- the existing source-unit proposal only if it needs a concise selected
  direction before later archival.

Other dirty worktree files are not owned by this workshop.

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
