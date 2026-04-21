# ADR-XXX: Replace qmd with llm-backed commonplace search

## Status

Proposed

## Context

Commonplace currently uses qmd as an optional semantic-search layer. The connect skill uses semantic search as a secondary discovery path after directory and index scanning, mainly to find vocabulary-mismatched body/source matches. The markdown library remains the source of truth; qmd is derived operational state.

qmd has accumulated operational friction disproportionate to that role:

- qmd writes to `~/.config/qmd`, `~/.cache/qmd`, and `node-llama-cpp` local build directories under the global npm package install.
- Codex `workspace-write` sessions need extra writable roots for qmd caches and build locks.
- GPU-dependent embedding/reranking does not fit Codex shell sandboxes; the MCP daemon workaround moves work outside the sandbox but introduces a separate always-on process.
- qmd issue #343 means custom `--index` does not reliably carry through HTTP MCP, forcing default-index mirroring.
- The HTTP MCP server appears single-client per process, so parallel Codex sessions require separate qmd MCP processes on separate ports.

The replacement should preserve the useful part of qmd: collection-scoped semantic recall over markdown. It should not preserve qmd-specific URI schemes, daemon requirements, GPU assumptions, or MCP behavior.

The evaluated options were:

- `llm` CLI with SQLite storage and pluggable embedding backends.
- `sqlite-vec` with a Commonplace-owned Python driver.
- Reseek, checked and excluded because it is a hosted second-brain product rather than a local substrate.

## Decision

Replace qmd with an `llm`-backed Commonplace search interface.

Commonplace will expose its own stable commands instead of asking skills to invoke raw `llm` commands directly:

```bash
commonplace-search-update
commonplace-search-query
commonplace-search-status
```

The implementation may shell out to `llm` in v1. The public contract is the Commonplace command surface, not the `llm` CLI shape.

Search configuration will be substrate-neutral. Replace `qmd-collections.yml` with `semantic-search.yml`, keeping the existing collection shape:

```yaml
collections:
  notes:
    path: /absolute/project/kb/notes
    pattern: "**/*.md"
```

Derived search state will live under a project-local directory such as `.search/` and will be rebuildable.

Stable record IDs will use repo-relative paths plus a content unit:

```text
kb/notes/context-engineering.md#file
```

Collection is stored as metadata, not duplicated in the ID:

```text
id: kb/notes/context-engineering.md#file
collection: notes
path: kb/notes/context-engineering.md
unit: file
content_hash: sha256(...)
```

Whole-file embeddings are the v1 default. Chunking is deferred until a benchmark shows whole-file retrieval is too coarse.

`sqlite-vec` remains the fallback if `llm`'s schema, CLI behavior, or metadata handling become load-bearing constraints.

## Consequences

Positive:

- Removes qmd's GPU, MCP daemon, and node-llama-cpp build-lock problems from the happy path.
- Supports parallel agent sessions through normal CLI/SQLite read behavior rather than MCP session ownership.
- Keeps the source of truth as markdown and the index as rebuildable derived state.
- Gives Commonplace a substrate-neutral search interface that can later move from `llm` to `sqlite-vec` without changing skills.
- Lets embedding generation be selected by environment: API-backed, local CPU model, or another `llm` plugin.

Negative:

- Adds a Commonplace-owned search driver and tests.
- Introduces a dependency on `llm` and at least one embedding backend/plugin.
- Requires benchmarking because qmd's recall may differ from the selected `llm` embedding model.
- Whole-file embeddings may be too coarse for long sources; chunking may be needed later.
- qmd-related docs, install instructions, scaffold assets, and skill instructions need migration.

## Implementation Notes

Migration should happen in phases:

1. Prototype in `kb/work/semantic-search-replacement/` and benchmark against qmd on real queries.
2. Add `commonplace-search-*` CLI commands behind tests.
3. Update `commonplace-init` to generate `semantic-search.yml` and ignore `.search/`.
4. Update connect skill, report templates, and reference docs to use substrate-neutral semantic search language.
5. Remove qmd MCP/setup guidance from the happy path after the new search path passes the benchmark.

The qmd path can remain temporarily as a fallback during validation. It should not remain as a long-term parallel substrate unless a concrete recall regression requires it.

## Open Questions

- Which embedding backend should be the documented default: OpenAI via `llm`, local `llm-sentence-transformers`, or both?
- Should `llm` and the embedding plugin be package extras, install-doc prerequisites, or checked at runtime with actionable errors?
- Where exactly should derived search state live: `.search/llm.db`, `.index/search.db`, or another path?
- What benchmark threshold is sufficient to declare qmd replaced?
- If chunking is needed, what stable chunk-boundary rule should be used?

## References

- `kb/work/semantic-search-replacement/README.md`
- `kb/work/semantic-search-replacement/llm-vs-sqlite-vec.md`
- `kb/work/semantic-search-replacement/plan-replace-qmd-with-llm.md`
- qmd issue #343: https://github.com/tobi/qmd/issues/343
