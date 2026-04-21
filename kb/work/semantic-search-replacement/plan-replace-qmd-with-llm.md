# Plan: replace qmd with llm-backed semantic search

## Readiness

This plan is ready to implement **Phase 1 only**: a workshop-local prototype and benchmark. Do not start package integration, `commonplace-init` migration, install-doc changes, or skill rewrites until Phase 1 records acceptable recall and operational behavior.

The key gates before migration are:

- pick and test at least one embedding backend available in this environment
- prove `llm` collection scoping works without metadata-dependent filtering
- verify deletion behavior or specify a manifest/rebuild strategy
- compare whole-file recall against qmd on a fixed benchmark
- check concurrent read behavior against one `.search/llm.db`

## Decision

Use Simon Willison's `llm` package as the first replacement substrate for qmd, subject to the Phase 1 benchmark. Commonplace should not expose raw `llm` commands directly to skills. Instead, add a small Commonplace-owned `commonplace-search` interface that uses `llm` for embeddings and vector search behind the scenes.

This keeps the durable contract local and substrate-neutral:

- authored markdown remains the source of truth
- search configuration remains project-local
- derived search state remains rebuildable
- skills call Commonplace commands, not third-party tool details
- qmd can stay as a temporary fallback until recall and install behavior are validated

## Target interface

Add CLI commands under the package scripts:

```bash
commonplace-search-update [--config semantic-search.yml] [--database .search/search.db]
commonplace-search-query "concept" --collection notes -n 15
commonplace-search-status
```

Optional follow-ups after the first working path:

```bash
commonplace-search-keyword "term" --collection notes
commonplace-search-get notes/path.md
```

`keyword` can remain `rg` for now. `get` can remain normal file reads. The first version only needs update, query, and status.

## Configuration

Replace `qmd-collections.yml` with a substrate-neutral config, tentatively `semantic-search.yml`:

```yaml
collections:
  notes:
    path: /absolute/project/kb/notes
    pattern: "**/*.md"
  reference:
    path: /absolute/project/kb/reference
    pattern: "**/*.md"
  sources:
    path: /absolute/project/kb/sources
    pattern: "**/*.md"
  instructions:
    path: /absolute/project/kb/instructions
    pattern: "**/*.md"
  tasks-active:
    path: /absolute/project/kb/tasks/active
    pattern: "**/*.md"
  tasks-backlog:
    path: /absolute/project/kb/tasks/backlog
    pattern: "**/*.md"
  tasks-recurring:
    path: /absolute/project/kb/tasks/recurring
    pattern: "**/*.md"
```

Keep the existing collection shape so migration is mostly rename-and-rewire, not redesign.

Default derived state:

```text
.search/
  llm.db
  manifest.json   # optional, only if llm metadata is insufficient
```

`.search/` should be gitignored in initialized projects.

## Embedding backend

Start with one recommended backend and make it overridable:

- default for hosted/API-capable setups: OpenAI embeddings through `llm`
- acceptable local fallback: `llm-sentence-transformers` with a small CPU model

Do not bake the embedding model into note content or report output. Record it in `commonplace-search-status` and, if needed, in the derived DB metadata only.

Open questions before package implementation:

- whether Commonplace should install an `llm` embedding plugin as an optional extra, or document installation and fail with a clear message when no embedding model is configured
- whether the default should be API-backed (`text-embedding-3-small`) or local CPU (`llm-sentence-transformers`)

Current local observation: `llm` is installed, but only OpenAI embedding models are listed. Phase 1 must either use an available OpenAI key/model or install and test a local embedding plugin before any migration work starts.

## File identity and chunking

Use stable record IDs so repeated updates are idempotent and deletions are detectable.

Initial v1:

```text
<repo-relative-path>#file
```

Examples:

```text
kb/notes/context-engineering.md#file
kb/reference/qmd.md#file
kb/sources/some-paper.md#file
```

Store each Commonplace collection as a separate `llm` collection. `llm similar` searches one collection at a time and supports `--prefix`; it does not provide arbitrary metadata filtering through the normal CLI. Therefore `commonplace-search-query --collection notes` should map to:

```bash
llm similar notes -c "concept" -n 15 -d .search/llm.db
```

Record collection and path metadata only for reporting, status, deletion checks, or later direct SQL use. Do not depend on metadata filtering for v1 query behavior.

Suggested stored record shape:

```text
llm collection: notes
id: kb/notes/context-engineering.md#file
metadata.collection: notes
metadata.path: kb/notes/context-engineering.md
metadata.unit: file
metadata.content_hash: sha256(...)
```

This embeds whole files. It is simple and enough to validate the substrate against qmd.

If whole-file recall is too coarse, move to chunk IDs in v2:

```text
kb/notes/context-engineering.md#chunk-0001
kb/notes/context-engineering.md#chunk-0002
```

Do not start with chunking unless the benchmark shows it is necessary. Chunking adds link/report complexity and stable-boundary questions.

## Implementation phases

### Phase 1 — Prototype outside the package

Goal: prove `llm` can index and query the current Commonplace KB with acceptable recall.

Tasks:

1. Create a throwaway script under `kb/work/semantic-search-replacement/` that reads `qmd-collections.yml` or `semantic-search.yml`.
2. Create `.search/llm.db` and one `llm` collection per Commonplace collection (`notes`, `reference`, `sources`, `instructions`, `tasks-active`, `tasks-backlog`, `tasks-recurring`).
3. Feed collection files into `llm embed-multi` using stable IDs and enough metadata to diagnose results. Do not rely on metadata filtering for query behavior.
4. Run `llm similar <collection> -c "query"` for 10-20 known queries from connect reports or recent search sessions.
5. Compare top-5/top-10 results against qmd and `rg`.
6. Test repeated update idempotence.
7. Test deletion behavior by indexing a tiny temporary collection, deleting one file, rerunning update, and checking whether stale IDs remain. Record whether v1 needs a manifest or full collection rebuild.
8. Test two concurrent read commands against the same DB.
9. Record results in the workshop, including setup friction and failures.

Exit criteria:

- at least comparable top-10 recall to qmd on the benchmark
- a tested embedding backend is available here, either API-backed or local CPU
- no GPU requirement
- no home-directory writable-root requirement beyond normal `llm`/plugin caches, or a documented repo-local configuration for those caches
- two shell sessions can run query commands concurrently against the same DB
- deletion behavior is known and either acceptable or handled by a specified manifest/rebuild strategy

### Phase 2 — Add Commonplace search module

Goal: put the prototype behind a stable Commonplace interface.

Files likely affected:

- `src/commonplace/lib/search_config.py` — parse collection config and resolve paths
- `src/commonplace/lib/search_index.py` — list files, compute IDs, call `llm`, normalize output
- `src/commonplace/cli/search_update.py`
- `src/commonplace/cli/search_query.py`
- `src/commonplace/cli/search_status.py`
- `pyproject.toml` — add `commonplace-search-*` scripts and optional dependency group
- `test/commonplace/cli/test_search_*.py`
- `test/commonplace/lib/test_search_*.py`

Implementation rules:

- The Python code may shell out to `llm` for v1. Do not import private `llm` internals unless the CLI proves too awkward.
- Treat `llm` collections as the collection filter boundary. Do not implement v1 by placing all records in one `llm` collection and filtering metadata unless Phase 1 proves the CLI cannot support the one-collection-per-Commonplace-collection shape.
- Add a manifest only if Phase 1 shows `llm embed-multi` cannot handle deletions cleanly.

Exit criteria:

```bash
uv run commonplace-search-update --config semantic-search.yml
uv run commonplace-search-query --collection notes "context compression" -n 10
uv run commonplace-search-status
uv run pytest test/commonplace/cli/test_search_*.py test/commonplace/lib/test_search_*.py
```

### Phase 3 — Scaffold and install migration

Goal: new projects get the substrate-neutral search setup.

Files likely affected:

- `src/commonplace/assets/qmd-collections.yml` -> replace with `semantic-search.yml` asset
- `src/commonplace/cli/init_project.py` -> generate `semantic-search.yml`
- `src/commonplace/_data/.envrc.template` -> remove qmd-specific variables, add search DB/config variables only if needed
- `test/commonplace/cli/test_init_project.py` -> expect `semantic-search.yml`
- `INSTALL.md` -> replace qmd setup with llm setup
- `.gitignore` scaffold guidance -> add `.search/`

Compatibility stance: no backwards compatibility is required for unpublished consumers. If a migration shim is useful during the transition, mark it with `# BACKCOMPAT:` and remove it after the qmd references are gone.

Exit criteria:

- `commonplace-init` creates `semantic-search.yml`
- install docs can build and query the search index without qmd
- no qmd MCP daemon setup remains in the happy path

### Phase 4 — Update skills and reports

Goal: agents stop invoking qmd.

Files likely affected:

- `kb/instructions/cp-skill-connect/SKILL.md`
- `kb/instructions/example-onboard-second-brain.md`
- `kb/reports/types/connect-report.md`
- `kb/reference/qmd.md` -> replace with `semantic-search.md` or archive as superseded
- `kb/reference/storage-architecture.md`
- `kb/reference/instruction-generation.md`
- `kb/reference/README.md`
- `kb/reference/adr/003-connect-skill-discovery-strategy.md` -> update wording from "qmd" to substrate-neutral semantic search where appropriate

Report vocabulary should change from:

```text
Semantic search: via qmd
```

to:

```text
Semantic search: via commonplace-search
```

or simply:

```text
Semantic search: available | unavailable
```

Exit criteria:

- `rg "qmd|mcp__qmd__|COMMONPLACE_QMD_INDEX|qmd-collections" kb/instructions kb/reference kb/reports INSTALL.md AGENTS.md src test` only finds historical ADR/workshop references or explicitly superseded docs
- connect skill uses `commonplace-search-query` for semantic search and falls back to `rg`

### Phase 5 — Retire qmd state and docs

Goal: remove qmd operational burden from the repo.

Tasks:

1. Remove qmd writable-root guidance from Codex setup.
2. Remove qmd MCP instructions from install docs.
3. Remove qmd config asset and qmd env exports.
4. Add a short migration note: delete `qmd-collections.yml`, remove qmd MCP config, remove `.cache/qmd` writable root if no other project needs it.
5. Close or supersede `kb/work/qmd-repo-local-setup/` and this workshop.

Exit criteria:

- fresh init + install + search works without qmd installed
- `uv run pytest` passes
- durable decision captured in an ADR or reference note

## Benchmark plan

Use a small fixed benchmark before removing qmd.

Query set:

- 10 queries from previous connect reports
- 5 queries known to need vocabulary mismatch
- 5 source/body queries where frontmatter descriptions are insufficient

For each query, record:

```text
query:
expected useful targets:
rg top results:
qmd top 10:
llm top 10:
judgment: llm better | comparable | worse
notes:
```

Minimum acceptance: `llm` is comparable to qmd on top-10 recall and does not introduce worse operational friction. Results should include setup notes for the embedding backend, deletion behavior, and concurrent-read behavior.

## Risks

- `llm embed-multi` may not give enough control over deletion handling. Mitigation: own a manifest and explicitly rebuild changed collections if needed.
- Whole-file embeddings may be too coarse for long sources. Mitigation: add chunking only after benchmark evidence.
- Plugin install friction may replace qmd friction. Mitigation: test both API and CPU-local embedding paths before switching install docs.
- `llm` schema assumptions may limit metadata or filtering. Mitigation: use one `llm` collection per Commonplace collection for v1 and keep `sqlite-vec` fallback viable behind the same `commonplace-search` interface.
- qmd may become easier to operate after upgrading. Upstream qmd v2.1.0 reports `XDG_CACHE_HOME` support for model cache, and newer code has GPU mode controls. This does not remove the replacement rationale, but it means the qmd critique should distinguish installed qmd 1.0.7 from current qmd before making a durable ADR.

## Non-goals for v1

- MCP server for semantic search
- chat over the KB
- automatic tagging
- reranking
- graph traversal
- replacing `rg` keyword search

## First next step

Build the Phase 1 prototype and benchmark in the workshop directory. Do not change `commonplace-init`, install docs, package CLI, or skills until the benchmark shows `llm` recall is acceptable and the deletion/concurrency checks are recorded.
