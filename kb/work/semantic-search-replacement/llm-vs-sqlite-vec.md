# `llm` vs `sqlite-vec` — replacement evaluation

Evaluation of two candidate substrates for the role qmd plays in Commonplace today. For what qmd is used for and what the replacement must cover, see [README.md](./README.md); for the qmd problems being addressed, see [qmd-issues.md](./qmd-issues.md).

Both candidates share the key property qmd lacks: **search is pure vector math; embedding generation is a separate, pluggable concern.** They also avoid qmd MCP's single-client daemon problem — parallel agents can run independent read-only search commands against the same SQLite-backed state without negotiating session ownership. Reseek was checked and excluded from the comparison because it is a hosted second-brain product, not a local substrate.

## Option A — `llm` CLI with SQLite storage

Simon Willison's `llm` CLI (`pipx install llm`) plus an embeddings plugin.

- **CLI verbs**: `llm embed-multi <collection> --files <dir> '**/*.md' -m <model>`; `llm similar <collection> -c "query" -n 5`; `llm collections list`.
- **Process model**: pure CLI. No server, no daemon, no port. Each invocation is a short-lived Python process that opens the SQLite file, runs, and exits. Parallel agents just open the same DB; SQLite handles concurrent readers natively.
- **Storage**: single SQLite DB, path controllable via `--database` or `LLM_USER_PATH`. Easy to place under `.qmd/` (or `.search/`) in the repo.
- **Embedding backends**: plugins cover OpenAI (built-in), Voyage, Gemini, Cohere, Ollama, sentence-transformers. We can pick a CPU-friendly local model (`all-MiniLM-L6-v2` via `llm-sentence-transformers`) or an API. No GPU ever required.
- **Collections**: first-class concept, named and stored in the same DB.
- **Incremental refresh**: `embed-multi` skips unchanged IDs when the input stream repeats them; for directory-tree refresh we'd script "list files, pass to stdin" and let `llm` de-dup by ID.
- **Metadata**: arbitrary JSON per record, indexable.

**Strengths**: working CLI surface, large plugin ecosystem, single well-known maintainer, standard SQLite schema. Adopting it collapses "install + configure + command surface" in one step.

**Gaps vs qmd surface**:
- No `get` / `multi-get` by URI — trivial to replace with `Read` against the stored path.
- No built-in keyword search — we already use `rg` for that; no regression.
- No MCP endpoint — the dropped requirement.
- No directory → collection binding in config. We'd keep the `qmd-collections.yml` shape (renamed) as a Commonplace-side config and feed paths to `embed-multi` from a small `commonplace-search` driver.

## Option B — `sqlite-vec` SQLite extension with a Commonplace-owned driver

Alex Garcia's `sqlite-vec` (`vec0` virtual table, `vec_distance_*` functions) embedded into a `commonplace-search` Python module.

- **CLI verbs**: we write them. `commonplace-search update`, `commonplace-search query`, plus whatever else we need.
- **Process model**: no process at all. `sqlite-vec` is a loadable SQLite extension — a single `.so`/`.dylib` that gets loaded into whatever SQLite client already opened the DB (Python's `sqlite3`, the `sqlite3` CLI, etc.). No daemon, no port, and even less surface than `llm`. Concurrent reads are SQLite's default; writes serialize via the file lock.
- **Storage**: single SQLite DB with a `vec0` virtual table and a sibling metadata table. We own the schema entirely.
- **Embedding backends**: we pick. Easiest: OpenAI `text-embedding-3-small` via the `openai` SDK, or `sentence-transformers` for offline. Pluggable only if we invest.
- **Collections**: just a column in our table. Trivial.
- **Incremental refresh**: we own the mtime / content-hash bookkeeping.
- **Metadata**: arbitrary columns.

**Strengths**: smallest runtime surface, zero non-SQLite processes, cleanest tailored data model, no third-party CLI conventions to fight, single-file distribution. No plugin stack to vet for sandbox friendliness.

**Gaps vs qmd surface**: everything in the user-visible CLI must be built. That includes the driver for "walk a directory, diff against stored content hashes, call the embedder for changed docs, write vectors and metadata". Rough size: a few hundred lines of Python. No plugin ecosystem — switching embedder means code changes.

## Hybrid — `llm` as the embedder, `sqlite-vec` as the store

Use `llm`'s plugin ecosystem solely for embedding generation (run the CLI non-interactively or call the Python library), and persist into a `sqlite-vec` table we own. Gets the plugin breadth of Option A with the schema control of Option B, at the cost of maintaining the glue.

## Side-by-side

| Concern | `llm` | `sqlite-vec` |
|---|---|---|
| CLI already exists | Yes | No — we build it |
| Server / daemon required | No — short-lived CLI process per call | No — SQLite extension loaded in-process |
| Storage is SQLite | Yes (schema fixed by `llm`) | Yes (we own schema) |
| Embedding backends | Plugin ecosystem | Whatever we import |
| Collections | First-class | A column we add |
| Incremental refresh | Content-ID de-dup; we drive the list | We drive everything |
| Sandbox friendliness | No GPU need; DB path configurable | No GPU need; nothing except SQLite |
| Parallel Codex sessions | Multiple CLI reads against one DB; no MCP session ownership | Multiple SQLite readers by default; no daemon |
| Maintainer footprint | Large user base | Large user base |
| Dependency weight | `llm` + chosen plugin(s) | SQLite extension (single `.so`) |
| Build time | Hours | Days |
| Long-term fit for Commonplace-specific needs | Medium — we bend to its schema | High — we own the shape |

## Recommendation

Lead with **Option A (`llm`)** for v1. Reasons:

- It closes the gap fastest: the CLI verbs exist, the storage is SQLite, the sandbox story is clean, and the embedding choice is deferrable.
- The parts of qmd we actually use map onto `llm` commands directly: `embed-multi` replaces `update`+`embed`, `similar` replaces `query`, collection scoping replaces `-c <collection>`.
- If `llm`'s schema ever pinches — for example if we need custom metadata not expressible in its JSON column, or much higher throughput — Option B is a migration, not a rewrite: the embeddings are just floats, and the corpus is just markdown files on disk.

Keep **Option B (`sqlite-vec`)** as the fallback if (a) `llm`'s schema or CLI assumptions become load-bearing against us, or (b) we want to eliminate one more upstream dependency once the shape has stabilized.

Reject the hybrid unless we hit a specific need that forces it.
