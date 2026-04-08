---
description: Agent-native coding CLI with local `.brv/context-tree` markdown memory, tiered query execution, derived summary/manifest artifacts, and connector-based distribution into other coding agents
type: related-system
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: 2026-04-03
---

# ByteRover CLI

ByteRover CLI is a source-available TypeScript coding-agent runtime from the ByteRover team, packaged as an oclif CLI plus React/Ink REPL, local daemon, MCP server, and connector installer. Its core bet is that agent memory should stay in real markdown files under `.brv/context-tree/`, while query, curation, summarization, archiving, sync, and agent integration are runtime services layered around that file substrate rather than external databases. The repo also ships a research paper (`paper/main.tex`) that argues the production code in this tree is the evaluated system, which makes the implementation especially important to inspect rather than taking the paper's framing on faith.

**Repository:** https://github.com/campfirein/byterover-cli

## Core Ideas

**The context tree is a real file substrate wrapped in a larger runtime.** The canonical knowledge store is `.brv/context-tree/`, created by `FileContextTreeService`, with directories and markdown files managed by `DirectoryManager` and written atomically. This is genuinely filesystem-first storage, not a database hidden behind a filesystem metaphor. The runtime around it is substantial, though: a daemon, TUI, CLI commands, transport client, provider integrations, and sync handlers all exist to make those files usable inside live coding-agent sessions.

**Query is a tiered execution pipeline, not one retrieval primitive.** `QueryExecutor` implements a five-tier path: cache hit, fuzzy cache hit, direct search response without an LLM, prompt-time injection of pre-fetched context plus manifest context, and finally a fuller agent loop. Underneath that, `SearchKnowledgeService` builds a MiniSearch index over title/content/path, supports symbolic path queries and overview mode via a symbol tree, applies out-of-domain checks, and can answer exact high-confidence matches without model involvement. The interesting design choice is not "search markdown" but splitting query into cheap, increasingly expensive stages.

**Curation is delegated to the LLM, but inside constrained helper scaffolding.** `CurateExecutor` pre-processes file references, optionally pre-compacts large inputs, creates an isolated task session, injects the source context into sandbox variables, and tells the model to use `tools.curation.recon()`, `mapExtract()`, `groupBySubject()`, and `dedup()` rather than freehanding file edits. This is a real agent-mediated write path, not a deterministic parser. The constraint comes from the helper API and file operations, not from a schema that eliminates model judgment.

**Derived artifacts are first-class loading aids.** After curation, `FileContextTreeSummaryService` can regenerate `_index.md` summaries bottom-up based on child hashes, and `FileContextTreeManifestService` builds `_manifest.json` by allocating summaries, contexts, and archive stubs into token-budgeted lanes. Unlike many systems where "compilation" is just a slogan, these artifacts really do transform the canonical files into cheaper query-time representations. They are derived, fail-open, and explicitly non-canonical, which is the right separation.

**The adaptive lifecycle exists, but less strongly than the paper suggests.** The repo contains importance/recency scoring, maturity tiers, archive stubs, archive restore, and decayed archive-candidate selection. But the current scoring weights in `memory-scoring.ts` set `W_IMPORTANCE = 0` and `W_RECENCY = 0`, so ranking is effectively normalized BM25 only. Search-hit feedback is also commented out in `SearchKnowledgeService` "for benchmark", and the archive service is present as infrastructure rather than an obviously central runtime path. So there is a lifecycle mechanism here, but it is not yet the dominant force in retrieval.

**Distribution into other agent environments is a core product feature.** The repo supports four connector modes (`rules`, `hook`, `mcp`, `skill`) and ships templates that tell external agents to use `brv query` before work and `brv curate` after work. This is one of the clearest reviewed examples of treating memory not just as a local store, but as something that must be packaged across many agent surfaces. In practice, ByteRover is as much a memory distribution system as a memory substrate.

## Comparison with Our System

| Dimension | ByteRover CLI | Commonplace |
|---|---|---|
| Canonical substrate | Markdown files under `.brv/context-tree/`, managed by a daemon and agent tools | Markdown files in the repo, managed directly through notes, instructions, and git |
| Main knowledge unit | Context entry with tags, keywords, `related`, and scoring frontmatter | Typed note with discriminating description, explicit status, and prose semantics |
| Query model | Tiered runtime: MiniSearch + symbol tree + OOD checks + direct response + manifest/prefetch + LLM synthesis | Progressive disclosure by descriptions, indexes, link phrases, and explicit traversal decisions |
| Curation model | LLM-mediated extraction and file mutation through helper tools | Human+agent writing and revision with explicit type routing and note templates |
| Derived artifacts | `_index.md` summaries, `_manifest.json`, archive stubs, snapshot/merge metadata | Generated indexes and validation output, but fewer runtime-generated loading artifacts |
| Link semantics | `related` paths plus parsed relations/backlinks; useful but semantically lighter | Standard markdown links with explicit relationship language (`extends`, `grounds`, `contradicts`, `enables`, `example`) |
| Integration surface | REPL, CLI, daemon, MCP server, connector installers, cloud sync spaces | Repo-native instructions and skills; strong inside the KB, thinner as a packaged product surface |
| Team sync | Built-in push/pull/space workflow with merge and conflict capture | Git-native collaboration and review |

ByteRover is stronger where commonplace is currently thin: it is a packaged, agent-facing product with an actual runtime, a connector strategy, and multiple query-time optimization layers. If a team wants "memory for coding agents" that works immediately across many agent clients, ByteRover is much closer to a deployable system than commonplace.

Commonplace is stronger where ByteRover stays operational. Our notes are designed to carry explanatory reach, explicit relationship semantics, retrieval-quality descriptions, and type-specific writing constraints. ByteRover's entries are more like managed memory records: useful for recall, weaker for articulated reasoning. The result is that ByteRover optimizes for working memory and retrieval ergonomics, while commonplace optimizes for durable conceptual structure and composability.

The deepest difference is where each system commits intelligence. ByteRover commits more intelligence into runtime services around the files: search stages, manifests, summaries, archive stubs, connectors, and daemon workflows. Commonplace commits more intelligence into the documents and authoring rules themselves. ByteRover's center of gravity is execution. Ours is curation.

## Borrowable Ideas

**Treat non-canonical loading artifacts as first-class citizens.** ByteRover cleanly separates canonical knowledge files from `_index.md` summaries, `_manifest.json`, and archive stubs. For commonplace, this suggests a stronger generated-artifact layer for loading aids that does not contaminate the note layer itself. This is ready to borrow now as an architectural principle, even if the exact artifact shapes still need a use case.

**Add direct-response and out-of-domain gates before expensive synthesis.** The query path does not always escalate to a full model loop. Sometimes it returns "not covered", sometimes it returns the matched files directly, and only then does it pay for broader synthesis. If we build more interactive KB query tooling, this is ready to borrow now.

**Package one knowledge system into multiple agent surfaces from a shared source.** The `rules`/`hook`/`mcp`/`skill` split is a strong distribution pattern. Commonplace currently relies on repo conventions plus skills, but the same knowledge-routing core could be emitted into multiple target formats instead of hand-maintained separately. This needs a concrete integration use case first.

**Use archive stubs instead of hard deletion for low-value knowledge.** ByteRover's `.stub.md` plus `.full.md` split preserves searchability and lineage while shrinking active context. That pattern could be useful for workshop outputs or stale operational notes where full deletion is too aggressive but full active presence is too expensive. Needs a concrete use case first.

**Make sync conflicts explicit artifacts, not invisible merge pain.** `FileContextTreeMerger` preserves conflicting local copies in a dedicated conflict directory and restores from backup on failure. The general pattern is worth borrowing anywhere agent-generated artifacts may sync across machines or spaces. Not immediately relevant to commonplace's git-first path, but strong if we ever add non-git sync surfaces.

## Curiosity Pass

**"Hierarchical context tree" is partly mechanism and partly naming.** The mechanism is real: files are arranged in directories, a symbol tree is built from paths, `_index.md` files annotate folders, and relation/backlink parsing enriches traversal. But this is still a file hierarchy with derived indexes, not a richer knowledge graph substrate. The paper's "knowledge graph" language is best read as "filesystem plus reference graph", not as graph-native storage.

**The derived-artifact story is stronger than the lifecycle story.** Summary regeneration and manifest allocation are clearly wired into post-curation and query-time behavior. By contrast, the "adaptive knowledge lifecycle" is only partially live: ranking ignores importance and recency, access-hit reinforcement is disabled, and archive logic looks more like prepared infrastructure than the system's active center. The simpler description is "BM25 search over curated files plus generated summaries/manifests", and right now that simpler description is closer to the mechanism.

**ByteRover's most distinctive contribution is distribution, not just storage.** Plenty of systems store files. Fewer systems turn that store into a product surface that can be installed as rules, hooks, MCP config, or skill files across many coding agents. The real property this produces is deployment reach: the same memory layer can show up inside different agent harnesses without asking each one to reinvent memory from scratch.

**"Zero external infrastructure" is true for storage, not for the full system.** The local substrate really is just files. But ByteRover still depends on an LLM provider for `query` and `curate`, and it has optional ByteRover-hosted sync through `push`, `pull`, and spaces. So the repo genuinely rejects vector databases and graph databases, but it does not eliminate operational dependencies in the broader sense.

**The benchmark story is only partially inspectable from this repo.** The paper source is checked in and explicitly claims the production code is the evaluated system. But the public tree does not obviously include the benchmark harnesses or datasets used for LoCoMo and LongMemEval. That does not falsify the results, but it limits how far a code-grounded reviewer can verify the evaluation claims. The mechanism we can inspect confidently is the runtime and storage design, not the full empirical pipeline.

## What to Watch

- Whether importance/recency weighting and access-hit reinforcement get turned back on in production retrieval, making the lifecycle logic materially affect ranking instead of sitting mostly on the side.
- Whether archive stubs become a central runtime feature or remain supporting infrastructure that mostly exists for the paper's broader architectural claim.
- Whether the connector surface stays coherent as the number of supported agent environments grows; distribution breadth can easily become maintenance drag.
- Whether the benchmark/evaluation layer becomes reproducible from the public repo rather than primarily inspectable through the paper source and reported numbers.
- Whether the system grows richer semantic structure than `related` paths and backlinks, or decides that operational recall is enough and deeper knowledge semantics are out of scope.

---

Relevant Notes:

- [Files, not database](../files-not-database.md) — exemplifies: ByteRover is a strong production case for a real file substrate, but also shows how much runtime machinery can accumulate around that choice
- [Agents navigate by deciding what to read next](../agents-navigate-by-deciding-what-to-read-next.md) — contrasts: ByteRover increasingly pre-shapes the agent's next read through search tiers, manifests, and direct-response shortcuts
- [Pointer design tradeoffs in progressive disclosure](../pointer-design-tradeoffs-in-progressive-disclosure.md) — extends: `_index.md` summaries, manifest lanes, and archive stubs are three different pointer forms with different costs and guarantees
- [Context efficiency is the central design concern in agent systems](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: the whole query stack is an optimization around bounded windows and escalating cost
- [Distillation](../definitions/distillation.md) — extends: summary and manifest generation are genuine derived-context artifacts, while the archive and lifecycle rhetoric overstates how much transformation is currently active
- [The boundary of automation is the boundary of verification](../the-boundary-of-automation-is-the-boundary-of-verification.md) — complicates: the repo exposes how far LLM-mediated curation can be productized before stronger verification becomes necessary
- [Inspectable substrate, not supervision, defeats the blackbox problem](../inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — foundation: ByteRover's strongest design choice is keeping the memory substrate inspectable even while the runtime grows sophisticated
- [Napkin](./napkin.md) — contrasts: both are file-first agent memory CLIs, but Napkin is lighter and more Obsidian-shaped while ByteRover is a fuller daemon-plus-connector product
- [OpenViking](./openviking.md) — contrasts: both build hierarchical loading aids, but OpenViking virtualizes a database behind filesystem semantics while ByteRover uses real files
- [Supermemory](./supermemory.md) — contrasts: Supermemory is stronger on hosted/open integration surfaces, while ByteRover is stronger on local inspectable substrate and checked-in runtime code
