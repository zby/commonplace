# Alternative architectures for `src/commonplace/`

Survey from a full read of `src/` (~11.4k LOC). Three exploration passes mapped the review subsystem, the core lib, and the CLI layer. Below are five structural axes where a genuinely different architecture is on the table, ordered by leverage. Axes 1–3 are one insight at three altitudes and form the main thread; 4–5 are independent and lower-stakes.

## Orientation

Two subsystems dominate. The **core lib** (`lib/`) has strong frozen-dataclass value objects (`ParsedDocument`, `TypeProfile`, `ParsedNote`), one central path authority (`project_paths.py`), and one god-module (`relocation.py`, 703 lines). The **review** subsystem (`review/` + `cli/review/`, ~3.5k LOC) is the most complex part: a hand-rolled SQLite store (`review_db.py`, 924 lines), a clean `(note,gate)`-pair protocol and runner-adapter layer, and a 490-line `executor.py` coordinator with three near-duplicate execution paths.

The library/CLI split (`lib` = pure, `cli` = thin argparse) is real and well enforced. Most of the agent-flagged smells (parse-duplication, grab-bag modules, scattered path resolution) are helper-extraction fixes. The items below are the ones that are actually *architectural*.

## Axis 1 — review storage substrate (the live one)

Decision baseline: review state — store, log, and blobs — lives **outside Git** (gitignored, continuous with ADR-010/ADR-007). So "binary churns Git" and "log is Git-survivable" are *not* deciding factors; nothing is committed either way. The axis that remains is the source-of-truth *form*.

Three coherent shapes:

| | source of truth | index | form / recovery | selector complexity |
|---|---|---|---|---|
| **A. SQLite-as-store, Git-decoupled** (current) | one `.sqlite` blob | same file | binary; blob *is* truth, corruption unrecoverable, schema changes are migrations | low (SQL) |
| **B. Pure-file store** | content-addressed dir tree | the tree itself | plain-text; but **high** selector cost | **high** — re-implement joins over directories |
| **C. Append-only event log + derived SQLite** | JSONL log + `blobs/` | rebuildable `.sqlite` cache | plain-text truth, index disposable/rebuildable | low (SQL over the cache) |

Recommendation: lean **C**, but it must win on its own merits, not on Git. The Git-decoupling goal is already satisfied inside **A** by [ADR 032](../../reference/adr/032-review-freshness-uses-db-snapshots-not-git.md): snapshot bytes live in `review_file_snapshots.content_text`, and freshness uses SHA-256 over file content instead of Git blob SHAs. So C is an *optional refinement* over A, justified only by: a plain-text source of truth an agent can `rg` without SQLite (the llm-wiki dual-interface property A gives up), a disposable index that rebuilds from the log instead of migrating, and natural alignment with the content-addressed ledger (Axis 3). B's plain-text appeal is real but `pure-file-review-store-design.md` flags its fatal cost — re-implementing relational joins over directories — so C keeps SQL for queries while making the log the truth. See [append-only-log-with-snapshots.md](./append-only-log-with-snapshots.md) for the A-vs-C decision kept separate from the Git mandate.

## Axis 2 — collapse the executor's three paths into one pipeline

`executor.py` + `batch.py` + the live-agent path (`create_review_runs`/`ingest_bundle_output`) are three orchestrations of the same sequence: `resolve → capture → render → run → parse → finalize`. They differ only in the **run** step (in-process subprocess / external agent writes a file / external orchestrator fans out). The `batch.py`↔`executor.py` finalization duplication is the symptom.

Alternative: model the sequence as one pipeline with a pluggable *execution stage*. `RunnerAdapter` (the cleanest abstraction in the subsystem) already proves the seam for subprocess harnesses; extend the same seam to "external agent" and "external orchestrator" as adapters that *suspend* between render and parse. `prepare`/`ingest` stop being a separate path and become the render stage + parse-finalize stage of the one pipeline. Same move ADR-029 made at the pair level, lifted to execution. Net: `executor.py` becomes a stage sequencer, `batch.py` disappears, finalization lives in one place.

## Axis 3 — reframe: review state *is* a content-addressed memo cache

Strip away runs/bundles/packing/sweeps (execution strategy) and the essential domain is tiny:

> `accept(sha256(note_bytes), sha256(gate_bytes), model_partition) → decision + rationale`

An append-only ledger keyed by **content hashes** (not paths) is the whole truth. Key acceptance by content hash rather than `(note_path, gate_path)` and:

- **relocation rekeying vanishes** — `count_note_path_records` / `rekey_note_path` in `review_db.py`, called from the 703-line `relocation.py`. Moving a file doesn't change its bytes, so its acceptances still resolve.
- staleness becomes a pure hash inequality — no diff-from-Git path needed.
- the ledger is small enough to be trivially file-backed, feeding Axis 1's log directly.

This is the highest-leverage reframe: it separates a *minimal durable ledger* from *disposable execution orchestration*, and most of the subsystem's complexity turns out to sit on the orchestration side. Caveat to resolve: path is still needed as a *display/CLI* handle and to locate the current file — content-key for identity, path for retrieval. [ADR 032](../../reference/adr/032-review-freshness-uses-db-snapshots-not-git.md) already moved gate identity from shorthand to `gate_path`; this thread asks whether content keys should eventually go further and become ledger identity.

## Axis 4 — core lib: "load once, project many" KB graph

`index_directory`, `index_generated`, `validation`, and `review_target_selector` each independently re-walk `kb/` and re-`frontmatter.parse` every file (same `parse(path.read_text()).data` idiom in ~7 places). Not a missing helper — a missing *model*.

Alternative: one indexing pass builds an in-memory `KbGraph` (notes with resolved frontmatter, links, tags, types, in/out edges); every consumer queries it. Orphan detection, tag indexes, dir indexes, validation, review targeting all become projections over one loaded graph. Natural home for the missing `Note` aggregate (`ParsedNote` is currently defined locally inside `validation.py`) and a typed `Frontmatter` accessor instead of `dict[str, Any]`. Independent of the review thread; lower stakes.

## Axis 5 — CLI sprawl (a trade-off, not a clear win)

21 console-scripts, each a hand-rolled argparse `main` repeating `repo_root = cwd or Path.cwd()` / `prepare_review_db` boilerplate. The conventional refactor is one `commonplace <noun> <verb>` dispatcher with a shared context object.

But the flat surface is deliberate: skills invoke `commonplace-prepare-review-batch` by bare name; the design is agent-addressable. A multiplexed CLI helps humans and hurts agents. So: extract a shared `CliContext` to kill the boilerplate, but **keep the flat entry-point surface**. Flagged mainly so the boilerplate isn't "fixed" in a way that fights the agent-facing design.

## Where the thread starts

Axes 1 → 3 are the same insight at two altitudes (content-addressed ledger → file-backed event log); 2 falls out of 1 nearly for free. 4 and 5 are independent and can wait. The active work begins at Axis 1, with the snapshot-embedding rule from Axis 3 as its first concrete constraint.

## Incidental finding (not architectural)

`type_resolver.py:306-309` — the `if type_doc_rel == TYPE_SPEC_PATH: expected_type = TYPE_SPEC_PATH else: expected_type = TYPE_SPEC_PATH` branch is dead (both arms assign the same value). Behaviorally correct, vestigial. Trivial cleanup, noted so it isn't re-discovered.
</content>
