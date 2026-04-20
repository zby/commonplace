---
description: How commonplace uses qmd for optional semantic search, where its collection config and index state live, and why Codex needs extra writable roots for qmd-backed queries
type: kb/types/note.md
tags: []
status: current
---

# qmd

Commonplace uses `qmd` as an optional semantic-search layer over the KB. It complements `rg` and directory indexes: `rg` finds exact terms, directory indexes expose curated descriptions, and qmd finds vocabulary-mismatched candidates inside note bodies and sources.

qmd is not a source of truth. The authoritative KB remains markdown under `kb/`. qmd's collection config and index are derived operational state.

## Shipped configuration

`commonplace-init` writes two qmd-facing files into each project:

| File | Role |
|---|---|
| `.envrc` | Exports `COMMONPLACE_QMD_INDEX=<project-name>` so skills can refer to the project index without hardcoding the name. |
| `qmd-collections.yml` | Lists the Commonplace collections qmd should index, with absolute project paths resolved at init time. |

The generated collection config covers:

- `kb/notes/` as `notes`
- `kb/reference/` as `reference`
- `kb/sources/` as `sources`
- `kb/instructions/` as `instructions`
- `kb/tasks/active/`, `kb/tasks/backlog/`, and `kb/tasks/recurring/` as separate task scopes

Operators copy the generated config to qmd's config directory:

```bash
cp qmd-collections.yml ~/.config/qmd/$COMMONPLACE_QMD_INDEX.yml
```

The resulting qmd commands stay explicit about the index:

```bash
qmd --index "$COMMONPLACE_QMD_INDEX" update
qmd --index "$COMMONPLACE_QMD_INDEX" embed
qmd --index "$COMMONPLACE_QMD_INDEX" query "context engineering" --collection notes -n 15
```

When qmd is exposed through MCP, use the MCP tools for search and retrieval inside Codex instead of invoking shell qmd for every lookup:

| Need | Shell qmd | MCP qmd |
|---|---|---|
| Keyword search | `qmd --index "$COMMONPLACE_QMD_INDEX" search "term" --collection notes` | `mcp__qmd__.search(query="term", collection="notes")` |
| Semantic search | `qmd --index "$COMMONPLACE_QMD_INDEX" query "concept" --collection notes -n 15` | `mcp__qmd__.deep_search(query="concept", collection="notes", limit=15)` or `mcp__qmd__.vector_search(...)` |
| Retrieve one file | `qmd --index "$COMMONPLACE_QMD_INDEX" get qmd://notes/file.md` | `mcp__qmd__.get(file="qmd://notes/file.md")` |
| Retrieve many files | `qmd --index "$COMMONPLACE_QMD_INDEX" multi-get "qmd://notes/*.md"` | `mcp__qmd__.multi_get(pattern="qmd://notes/*.md")` |
| Index health | `qmd --index "$COMMONPLACE_QMD_INDEX" status` | `mcp__qmd__.status()` |

MCP qmd is search/retrieval only. Continue using shell qmd for `update` and `embed`.

## Skill usage

`cp-skill-connect` treats qmd as a best-effort enhancement:

1. If shell `qmd` exists, the skill runs `qmd --index "$COMMONPLACE_QMD_INDEX" update && qmd --index "$COMMONPLACE_QMD_INDEX" embed`.
2. During discovery, it prefers MCP qmd tools when available (`deep_search`, `vector_search`, `search`, `get`, `multi_get`) and records the tool, query strings, and top results.
3. If MCP qmd is unavailable, it falls back to shell qmd queries.
4. If qmd is unavailable or unusable through both paths, the skill falls back to index scanning and keyword search.

The primary discovery path does not depend on qmd. qmd improves recall, especially for sources and body text, but failure should degrade search quality rather than block KB operation.

## Storage and rebuildability

qmd state is external to Commonplace:

| State | Location |
|---|---|
| Collection config | `~/.config/qmd/$COMMONPLACE_QMD_INDEX.yml` after copying from `qmd-collections.yml` |
| qmd SQLite index | qmd-managed cache location |
| qmd model cache | qmd-managed cache location, commonly under `~/.cache/qmd` |
| node-llama-cpp local builds | under the installed qmd npm package |

The collection config is generated from the project. The index and embeddings are rebuildable with `qmd update` and `qmd embed`.

## Codex permissions

qmd cannot currently be fully localized to the project tree. Moving only the SQLite index into the repo is insufficient: `qmd embed`, `qmd query`, and even model/device checks may write to qmd's model cache and to `node-llama-cpp` local-build lock directories under the qmd npm installation. MCP qmd avoids most shell-sandbox device/cache issues for search because the qmd model process runs outside Codex, but the daemon still has to be started and indexed by the host.

In Codex `workspace-write` sessions, the project directory is writable but those home-directory and npm-global paths are not automatically writable. Codex therefore needs additional writable roots for qmd-backed commands.

Add them to `~/.codex/config.toml`:

```toml
[sandbox_workspace_write]
network_access = true
writable_roots = [
  "/home/alice/.codex/memories",
  "/home/alice/.cache/qmd",
  "/home/alice/.npm-global/lib/node_modules/@tobilu/qmd/node_modules/node-llama-cpp/llama/localBuilds",
]
```

Use absolute paths and adjust the npm-global prefix for the local machine:

```bash
npm root -g
```

Restart Codex after editing the config. Sandbox permissions are fixed when a Codex session starts.

## Known failure mode

A typical Codex failure from missing qmd permissions is not a Commonplace config error. It looks like `node-llama-cpp` trying to create a CUDA/local-build lock under the global qmd npm install and receiving a read-only-filesystem error. qmd may then fall back to CPU or hang/timeout while reranking.

When this happens:

1. Keep the `qmd-collections.yml` / `COMMONPLACE_QMD_INDEX` setup.
2. Add the Codex writable roots above.
3. Restart Codex.
4. Re-run `qmd --index "$COMMONPLACE_QMD_INDEX" status`, then `qmd update`, `qmd embed`, or `qmd query`. If MCP qmd is configured, restart the daemon and Codex, then test `mcp__qmd__.status()`.

---

Relevant Notes:

- [Storage](./storage-architecture.md) — places qmd among Commonplace's derived indexes and external state
- [Instruction generation](./instruction-generation.md) — describes how `commonplace-init` resolves `qmd-collections.yml` and `.envrc`
- [003-connect-skill-discovery-strategy](./adr/003-connect-skill-discovery-strategy.md) — decision: qmd remains secondary to index scanning but necessary for source/body recall
