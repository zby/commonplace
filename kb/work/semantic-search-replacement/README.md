# Workshop: semantic-search replacement

This workshop evaluates whether to replace `qmd` as Commonplace's semantic-search layer, and if so, with what. It is the outgrowth of `kb/work/qmd-repo-local-setup/`, where the attempt to make qmd's state repo-local kept hitting new assumptions baked into qmd.

## Motivation

The `qmd-repo-local-setup` workshop untangled qmd's config (`~/.config/qmd`) and SQLite database (`~/.cache/qmd`) and made them repo-local. Several things did not move:

- **Hardcoded model cache** at `~/.cache/qmd/models` — needed by `qmd embed` / `qmd query`.
- **node-llama-cpp localBuilds** under the installed npm package prefix — needed for GPU/CPU model builds; fails in sandboxes with a read-only-filesystem error.
- **GPU affinity**. qmd's embedder expects a visible device; `workspace-write` sandboxes hide GPUs. It falls back to CPU unreliably and sometimes hangs during rerank.
- **Single-client MCP behavior**. The HTTP MCP daemon appears to keep one initialized MCP transport for the process: one Codex session can connect, but a second parallel session may fail during initialize with "Server already initialized" / "error decoding response body". Parallel Codex sessions need separate qmd MCP processes on separate ports.

The accumulated friction — two writable-root holes in `.codex/config.toml`, an MCP daemon workaround for issue #343, mirrored `index`/`$COMMONPLACE_QMD_INDEX` DBs, one-MCP-client-per-process behavior, and a repo-local setup that still cannot run `qmd embed` in-sandbox — has outgrown what the semantic-search role is worth. qmd is optional in the connect path and catches roughly "vocabulary-mismatched body matches"; it is not load-bearing.

This workshop asks whether a more established substrate can provide the same recall gain with less infrastructure per agent.

See [qmd-issues.md](./qmd-issues.md) for the full catalogue of observed problems grouped by root cause.

## qmd Usage Surface

The evaluation must cover every place qmd is called or documented. If a replacement cannot fill a slot, we either drop that slot or bridge it.

### Call-sites (runtime)

- `kb/instructions/cp-skill-connect/SKILL.md` — the only active skill that calls qmd. Runs `qmd update && qmd embed` if shell qmd exists, then prefers MCP `deep_search` / `vector_search` / `search` / `get` / `multi_get`, falling back to the shell verbs. If qmd is unavailable, it falls back to grep-only discovery.
- `kb/reports/types/connect-report.md` — the template cites "Semantic search: via qmd" in the discovery trace; the substrate name is user-visible in reports.
- `AGENTS.md` — exports `QMD_CONFIG_DIR` and `INDEX_PATH` for every agent in the checkout; documents `flock` for writer serialization.
- `.envrc` / `.envrc.template` (repo) — same exports.

### Install / packaging

- `src/commonplace/cli/init_project.py` — copies the asset to project-root `qmd-collections.yml` with path substitution.
- `src/commonplace/assets/qmd-collections.yml` — shipped collection config template.
- `src/commonplace/_data/.envrc.template` — shipped envrc template (still exports `COMMONPLACE_QMD_INDEX`).
- `test/commonplace/cli/test_init_project.py` — asserts `qmd-collections.yml` is created with paths substituted.
- `INSTALL.md` — Section 5 describes qmd setup, MCP daemon config, Codex writable roots, and issue #343 mirroring workaround.
- `.codex/config.toml` — adds `~/.cache/qmd` and the node-llama-cpp localBuilds path to `writable_roots`.

### Documentation

- `kb/reference/qmd.md` — collection config, CLI/MCP table, storage locations, Codex permissions, known failure modes.
- `kb/reference/storage-architecture.md` — places qmd among Commonplace's derived indexes.
- `kb/reference/instruction-generation.md` — notes that `qmd-collections.yml` is a generated template.
- `kb/reference/README.md` — mentions qmd as optional recall booster.
- `kb/reference/adr/003-connect-skill-discovery-strategy.md` — records the decision that semantic search is secondary to index scanning, but still necessary for sources and body text.

### Call pattern — the verbs we actually use

| Operation | Shell qmd | MCP qmd | Consumer |
|---|---|---|---|
| Scan collection dirs for changes | `qmd update` | — | connect skill (writer) |
| Generate embeddings for pending docs | `qmd embed` | — | connect skill (writer) |
| Keyword search scoped by collection | `qmd search "term" -c notes` | `mcp__qmd__.search(query, collection)` | connect skill (reader) |
| Semantic search scoped by collection | `qmd query "concept" -c notes -n 15` | `mcp__qmd__.deep_search(...)`, `mcp__qmd__.vector_search(...)` | connect skill (reader) |
| Retrieve one file by URI | `qmd get qmd://notes/file.md` | `mcp__qmd__.get(file=...)` | connect skill, reports |
| Retrieve many files by glob URI | `qmd multi-get "qmd://notes/*.md"` | `mcp__qmd__.multi_get(pattern=...)` | connect skill, reports |
| List collections | `qmd collection list` | — | operator |
| Index health | `qmd status` | `mcp__qmd__.status()` | operator, skill sanity check |

### Data model we rely on

- **Collections**: named scopes (`notes`, `reference`, `sources`, `instructions`, `tasks-active`, `tasks-backlog`, `tasks-recurring`) each bound to a directory and glob pattern in `qmd-collections.yml`.
- **URI scheme**: `qmd://<collection>/<path-from-collection-root>`, surfaced in skill output and connect reports.
- **Storage**: single SQLite file (embeddings + metadata); `flock`-serialized writers.
- **Incremental update**: `update` rescans and re-embeds only changed files.

### What we do not use

- qmd's own ranking tuning or rerankers beyond the defaults.
- qmd-specific LLM integrations (summaries, chat).
- Any qmd feature that requires its embedder at query time beyond "turn the query string into a vector".

## Requirements for a Replacement

Anything that lands here has to:

1. **Run in sandboxes without GPUs and without home-directory writes.** The substrate's state (DB, caches, locks) must fit under the repo or a pre-agreed writable root.
2. **Decouple embedding generation from search.** Vector math must not need a local LLM at query time; embedding generation must be switchable (API call, CPU-local model, or offline-prepared).
3. **Provide scoped semantic search.** Collections or equivalent filters over the corpus.
4. **Provide incremental refresh.** Re-embedding only what changed.
5. **Be scriptable from shell and Python.** Skills are shell; `commonplace-*` commands are Python.
6. **Avoid an always-on daemon for the common path.** MCP-as-workaround is acceptable, but the baseline shell path must not require one.
7. **Support parallel agent sessions without coordination.** Two Codex sessions should be able to search the same index at the same time without separate daemons, port assignments, or session ownership.
8. **Have enough maintenance headroom that we are not the only user.**

We can drop:

- The `qmd://` URI scheme (substrate-specific; connect reports can cite plain paths).
- The MCP daemon (it existed to work around GPU-in-sandbox; with a CPU-only or API-based stack it is unnecessary, and the current single-client behavior is actively harmful for parallel agents).
- `multi-get` (a glob plus `Read` covers it).

## Evaluation

Two candidate substrates: Simon Willison's `llm` CLI, and Alex Garcia's `sqlite-vec` SQLite extension. Full comparison — process model, storage, embedding backends, sandbox behavior, side-by-side table, and recommendation — lives in [llm-vs-sqlite-vec.md](./llm-vs-sqlite-vec.md).

Short version: lead with `llm` for v1 (CLI surface already exists, SQLite-backed, sandbox-clean, plugin ecosystem for embedders); keep `sqlite-vec` as the fallback if `llm`'s schema or CLI assumptions become load-bearing against us. Reseek was checked and excluded because it is hosted rather than a local substrate. Reject the hybrid unless forced.

Migration plan: [plan-replace-qmd-with-llm.md](./plan-replace-qmd-with-llm.md).
Proposed ADR: [adr-replace-qmd-with-llm.md](./adr-replace-qmd-with-llm.md).

## Open Questions

- **Embedding model default.** API (OpenAI `text-embedding-3-small`) is cheaper and better; offline (`sentence-transformers/all-MiniLM-L6-v2`) is private and free. Default? Overridable how?
- **Where does the DB live?** Reuse `.qmd/` (confusing — name carries the old tool) or rename to `.search/` / `.index/`?
- **Config shape.** Keep the `collection: {path, pattern}` YAML or reduce to a single `paths:` list with collection implied by the first path segment?
- **Connect-report vocabulary.** Keep "via qmd" as a substrate-specific token, or replace with substrate-neutral "via semantic search"?
- **Install path.** Does `commonplace-init` bundle `llm` install instructions, or assume the operator already has it (as it does with `uv`)?

## Closure Conditions

This workshop can close when:

- A decision on substrate is committed (either by picking `llm` and moving, or by rejecting both and keeping qmd with explicit acceptance of the current friction).
- If a replacement is chosen: the call-sites listed in *qmd Usage Surface* are updated or explicitly out of scope for a follow-up.
- If a replacement is chosen: `qmd-repo-local-setup` can be closed or superseded.
- Any durable lesson about choosing a semantic-search substrate for an agent-operated KB is extracted into `kb/notes/` or `kb/reference/`.
