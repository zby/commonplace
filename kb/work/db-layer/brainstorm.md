# Database layer brainstorm

## Problem statement

The review system (and upcoming revision system) are accumulating scripts that abstract over the filesystem. The current data layer is split across:

- **Filesystem mtime** — the new staleness model for gate reviews (`review_target_selector.py`)
- **Git blob SHAs + HTML comment metadata** — the legacy review system (`selector_engine.py`, `review_state.py`, `review_metadata.py`)
- **CSV index** — `kb/reports/review-csv/gate_reviews.csv`, rebuilt after each gate review
- **Gate YAML frontmatter** — watched regions, staleness policies parsed at query time (`gate_core.py`)
- **Markdown link parsing** — promotion candidates, connection discovery

Each new feature adds more filesystem queries, more path-encoding conventions, more scripts that scan directories. At some point direct filesystem access becomes too low-level an interface for the queries the system needs to perform.

## Constraint: notes stay as files

Notes, gates, and instructions must remain editable markdown files in the repo. The database is for **derived metadata** — review state, staleness, link graphs, frontmatter indexes — not for primary content.

## Constraint: repo-portable state

Ideally the database state lives in the repo so that `git clone` gives you a working system. This rules out external services and server-based databases.

## What the database would store

1. **Review state** — which (note, gate, model) triples have reviews, when they were written, whether they're stale
2. **Staleness signals** — note mtime, gate mtime, review mtime (or hashes, or both)
3. **Frontmatter index** — type, status, tags, description for every note, queryable without parsing
4. **Link graph** — source, target, relationship-type for every link
5. **Promotion/lifecycle data** — text vs note vs seedling classification, inbound link counts

## Option A: SQLite in the repo

SQLite is a single file. It could live at e.g. `db/commonplace.sqlite`.

**Advantages:**
- Real SQL queries — joins, aggregates, GROUP BY
- Single file, easy to `.gitignore` or track
- Python stdlib (`sqlite3`), zero dependencies
- Fast — all the filesystem scanning happens once at rebuild time

**Problems:**
- Binary file in git — merges are impossible, diffs are opaque
- Two people working on different branches would get merge conflicts on the binary
- Even solo, rebasing across commits that both touch the DB is painful

**Mitigation: treat as cache, not source of truth.**
- `.gitignore` the sqlite file
- Rebuild from filesystem on demand (`scripts/rebuild_db.py`)
- Scripts check if DB exists and is fresh; if not, rebuild
- Cost: rebuild time. For ~200 notes, likely <1s. Acceptable.

This is the simplest option. The DB is a **materialized view** of the filesystem.

## Option B: SQLite + CSV export for version tracking

The user's initial idea: keep CSV files in git, rebuild the DB from them on pull.

**Flow:**
1. Scripts read/write SQLite during work
2. Pre-commit hook exports tables to CSV
3. CSVs are committed (human-readable diffs)
4. Post-merge hook imports CSVs back into SQLite

**Advantages:**
- CSVs give you readable git history of metadata changes
- Merge conflicts on CSVs are resolvable (they're text)

**Problems:**
- Two-way sync is fragile — which is canonical, CSV or DB?
- Hook discipline required (what if someone forgets?)
- CSV → DB rebuild on every pull adds friction
- The current system already has a CSV (`gate_reviews.csv`) and the direction is to remove it
- If the DB is a cache (Option A), the filesystem is already the readable version-tracked source

**Verdict:** This adds complexity for a benefit (version-tracked metadata) that the filesystem already provides. The review files themselves are the readable history.

## Option C: SQLite as ephemeral cache + filesystem remains canonical

A refinement of Option A. The DB is:
- Not tracked in git (`.gitignore`)
- Rebuilt automatically when stale or missing
- Provides fast indexed queries for scripts
- Never written to as a source of truth — all writes go to filesystem, DB is rebuilt

**Freshness detection:**
- Store a rebuild timestamp in the DB
- Compare against `git log -1 --format=%ct` (last commit time) and max mtime of `kb/`
- If either is newer, rebuild

**What changes for scripts:**
- `review_target_selector.py` queries the DB instead of walking `kb/reports/reviews/`
- `resolve_gates.py` queries the DB for gate metadata instead of parsing YAML each time
- `promotion_candidates.py` queries link counts from the DB instead of regex-parsing all files
- New queries (e.g. "all seedling notes with <2 inbound links") become trivial

**Migration path:**
1. Build `scripts/rebuild_db.py` that scans filesystem → SQLite
2. Add a thin query layer (`scripts/db.py`) that auto-rebuilds if stale
3. Migrate scripts one at a time to use DB queries
4. Remove CSV index and hash-based staleness code

## Option D: Don't add a database yet

The mtime-based system in REVIEW-SYSTEM.md is deliberately simple. Adding a DB is a layer of indirection. The question is whether the current pain justifies it.

**Signs it's too early:**
- The mtime system hasn't been fully deployed yet (legacy code still exists)
- Only ~200 notes — filesystem scans are fast
- The main complexity is two parallel systems, not filesystem speed

**Signs it's time:**
- Scripts are duplicating filesystem traversal logic
- Path encoding conventions are spreading (encoded note paths, encoded gate ids, encoded model names)
- New features (revision system) will need the same queries the review system already performs
- The link graph has no queryable representation

## Open questions

1. **Rebuild cost at scale** — at what note count does full filesystem scan become painful? Is incremental rebuild worth the complexity?
2. **mtime vs hash for the DB world** — if the DB tracks hashes, mtime-based staleness becomes redundant. Should the DB unify both models?
3. **Schema design** — what tables? Sketch a schema before building.
4. **Write path** — if a script writes a review file, should it also update the DB, or always rebuild? Per-write updates are faster but create consistency risks.
5. **Link graph extraction** — the hardest part. Markdown link parsing is lossy (can't always determine relationship type without NLP). Is a partial graph useful?

## Tentative direction

**Option C** (SQLite as ephemeral cache) seems right. It:
- Preserves the filesystem-as-source-of-truth principle
- Avoids git-binary-file problems entirely
- Gives real query power for the growing script layer
- Has a clean migration path from current code
- Doesn't require anyone to change how they edit notes

The key insight: **the database is not storage, it's an index.** Like a search engine index over documents — the documents are canonical, the index accelerates queries and is rebuilt from scratch when needed.
