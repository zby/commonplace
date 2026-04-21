---
description: "Source-available coding-agent CLI with file-backed `.brv/context-tree`, tiered search/query, live scoring+archive/manifest layers, git-like context-tree VC, and multi-agent connector packaging"
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-10"
---

# ByteRover CLI

ByteRover CLI is a source-available TypeScript coding-agent runtime from ByteRover, currently packaged as version 3.1.0 with an oclif CLI, React/Ink REPL, local daemon, MCP server, connector installers, hub client, and built-in version control for its knowledge tree. Its core bet is still that agent memory should live in real markdown files under `.brv/context-tree/`, but the current repo is broader than "a local memory CLI": it treats that tree as a managed substrate with tiered retrieval, agent-mediated curation, reviewable mutations, derived loading artifacts, cloud-backed collaboration, and packaging for many other coding-agent environments. The repo also ships the paper source in `paper/main.tex`, which makes the implementation especially important to inspect rather than taking the paper's broader framing on faith.

**Repository:** https://github.com/campfirein/byterover-cli

## Core Ideas

**The context tree is a real file substrate, not a database projection.** The canonical knowledge store is `.brv/context-tree/`, created by `FileContextTreeService`, with directories and markdown files managed by `DirectoryManager` and written atomically. Search indexes, manifests, summaries, archives, and VC state are layered around those markdown files rather than replacing them. ByteRover is still one of the clearest production examples of "files first, runtime second."

**Query is a staged control path that tries hard not to pay for full agentic synthesis.** `QueryExecutor` explicitly documents five tiers: exact cache, fuzzy cache, direct search response, prompt-time injection of pre-fetched context plus manifest context, and only then a fuller agent loop. `SearchKnowledgeService` backs that with MiniSearch BM25, symbolic path queries, subtree scoping, overview mode, parent-score propagation through a symbol tree, and out-of-domain short-circuits. The interesting mechanism is not "search markdown"; it is a budgeted escalation policy.

**Curation is LLM-mediated, but the write path is scaffolded and reviewable.** `CurateExecutor` pre-processes attached files, runs pre-compaction, injects task-scoped context variables, and tells the model to use `tools.curation.recon()`, `mapExtract()`, `groupBySubject()`, and `dedup()` rather than freehanding file mutations. Afterward it computes snapshot diffs, propagates summary staleness, and rebuilds the manifest opportunistically. Separately, the review transport and `brv review pending|approve|reject` flow make high-impact curate operations inspectable and reversible instead of silently trusting every model write.

**Derived artifacts are first-class loading aids, not marketing language.** `FileContextTreeSummaryService` regenerates `_index.md` summaries bottom-up from child hashes; `FileContextTreeManifestService` allocates summaries, contexts, and archive stubs into token-budgeted lanes for query injection; archive stubs point to full archived files and remain searchable. The canonical store is still the markdown tree, but ByteRover now very clearly treats compiled loading artifacts as a normal runtime layer.

**The adaptive lifecycle is materially live now, though not equally strong in every part.** `memory-scoring.ts` uses a real compound score with relevance, importance, and recency weights; `SearchKnowledgeService` decays scores by file age and batches `recordAccessHits` back into frontmatter during index maintenance; archive candidate selection uses decayed importance and maturity. This is no longer just paper rhetoric. But the strongest live effect is ranking and promotion, not automatic forgetting: I found active archive services and archive-candidate logic, but not a comparably central background policy that regularly calls `archiveEntry` in the main executors.

**Distribution and collaboration are core product features, not side adapters.** The repo supports four connector modes (`rules`, `hook`, `mcp`, `skill`), has agent-specific config writers for a wide set of coding tools, exposes `brv-query` and `brv-curate` over MCP, and ships a `byterover` skill template that tells other agents how to use the memory layer. It also now treats the context tree as a git-like artifact with `brv vc` commands for branch/commit/merge/push/pull. In practice, ByteRover is as much a packaging and coordination system as it is a memory substrate.

## Comparison with Our System

| Dimension | ByteRover CLI | Commonplace |
|---|---|---|
| Canonical substrate | Markdown files under `.brv/context-tree/`, managed by a daemon and agent tools | Markdown files in the repo, managed directly through notes, instructions, and git |
| Main knowledge unit | Context entry with tags, `related`, scoring frontmatter, and runtime-owned lifecycle metadata | Typed note with discriminating description, explicit status, and prose semantics |
| Query model | Tiered runtime: caches, MiniSearch, symbol-tree/path search, OOD checks, manifest injection, then LLM synthesis | Progressive disclosure by descriptions, indexes, link phrases, and explicit traversal decisions |
| Curation model | LLM-mediated extraction and file mutation through helper tools, review queues, and post-curation recompilation | Human+agent writing and revision with explicit type routing, note templates, and review gates |
| Derived artifacts | `_index.md` summaries, `_manifest.json`, archive stubs/fulls, abstracts, cached indexes | Generated indexes and validation output, but fewer runtime-generated loading artifacts |
| Lifecycle model | Live scoring, decay, hit-based promotion, archive candidates, git-like context-tree VC | Status fields, workshop/library split, reviews, and git-native collaboration, with less automatic ranking |
| Link semantics | `related` paths, backlinks, and symbol-tree structure; useful but semantically lighter | Standard markdown links with explicit relationship language (`extends`, `grounds`, `contradicts`, `enables`, `example`) |
| Integration surface | REPL, CLI, daemon, MCP server, connectors, hub packages, cloud remotes | Repo-native instructions and skills; strong inside the KB, thinner as a packaged product surface |

ByteRover is still stronger where commonplace is thin: it is a packaged, agent-facing product with a real runtime, explicit collaboration surface, and multiple query-time optimization layers. If a team wants "memory for coding agents" that can be installed into many agent clients immediately, ByteRover is much closer to a deployable product than commonplace.

Commonplace is still stronger where ByteRover remains operational rather than conceptual. Our notes are designed to carry explanatory reach, explicit relationship semantics, retrieval-quality descriptions, and type-specific writing constraints. ByteRover's entries are more like managed memory records: useful for recall, weaker for articulated reasoning. The result is that ByteRover optimizes for working memory and retrieval ergonomics, while commonplace optimizes for durable conceptual structure and composability.

The deepest difference is still where each system commits intelligence. ByteRover commits more intelligence into runtime services around the files: search stages, manifests, summaries, archive stubs, review flows, connectors, and daemon workflows. Commonplace commits more intelligence into the documents and authoring rules themselves. ByteRover's center of gravity is execution. Ours is curation.

## Borrowable Ideas

**Treat non-canonical loading artifacts as first-class citizens.** ByteRover cleanly separates canonical knowledge files from `_index.md` summaries, `_manifest.json`, and archive stubs. For commonplace, this suggests a stronger generated-artifact layer for loading aids that does not contaminate the note layer itself. This is ready to borrow now as an architectural principle, even if the exact artifact shapes still need a use case.

**Add direct-response and out-of-domain gates before expensive synthesis.** The query path does not always escalate to a full model loop. Sometimes it returns "not covered", sometimes it returns the matched files directly, and only then does it pay for broader synthesis. If we build more interactive KB query tooling, this is ready to borrow now.

**Persist retrieval feedback as lightweight symbolic metadata instead of hiding it in opaque services.** ByteRover's access-hit batching writes back into frontmatter scoring rather than only influencing an in-memory ranker. That keeps the adaptive signal inspectable. Commonplace should not copy the exact scoring scheme blindly, but the "write learning into readable metadata" pattern is worth borrowing when we have a clear use case.

**Package one knowledge system into multiple agent surfaces from a shared source.** The `rules`/`hook`/`mcp`/`skill` split is a strong distribution pattern. Commonplace currently relies on repo conventions plus skills, but the same knowledge-routing core could be emitted into multiple target formats instead of hand-maintained separately. This needs a concrete integration use case first.

**Put a review queue in front of high-impact model-authored knowledge edits.** ByteRover's pending review operations are a pragmatic middle position between fully manual curation and blind auto-apply. Commonplace already has a stronger general review system, but ByteRover is a good reference for what an agent-facing review UX looks like when it is attached directly to a write workflow. This is more a product-surface reference than a new methodological principle.

## Curiosity Pass

**"Hierarchical context tree" is partly mechanism and partly naming.** The mechanism is real: files are arranged in directories, a symbol tree is built from paths, `_index.md` files annotate folders, and relation/backlink parsing enriches traversal. But this is still a file hierarchy with derived indexes, not a richer knowledge graph substrate. The paper's "knowledge graph" language is best read as "filesystem plus reference graph", not as graph-native storage.

**The adaptive lifecycle is now real, but its strongest live effect is ranking rather than forgetting.** The previous version of this review understated the implementation: importance/recency weights are live, access hits are persisted, and archive candidate selection is wired. What still looks weaker than the paper framing is automatic forgetting. I found archive services and archive-candidate logic, but not an equally central automatic archive loop in the main executor path. The simpler description is "scored retrieval over curated files with compiled summaries/manifests and optional archive machinery."

**ByteRover's most distinctive contribution is now the combination of inspectable substrate plus deployment surface.** Plenty of systems keep files. Fewer package those files across rules, hooks, MCP, skills, review queues, and context-tree version control from one shared runtime. The real property this produces is deployment reach: the same memory layer can show up inside different agent harnesses without asking each one to reinvent memory from scratch.

**"Zero external infrastructure" is true for storage, not for the full system.** The local substrate really is just files. But ByteRover still depends on an LLM provider for `query` and `curate`, and cloud collaboration depends on ByteRover-hosted git remotes. So the repo genuinely rejects vector databases and graph databases, but it does not eliminate operational dependencies in the broader sense.

**The benchmark story is only partially inspectable from this repo.** The paper source is checked in and explicitly claims the production code is the evaluated system. But the public tree does not obviously include the benchmark harnesses or datasets used for LoCoMo and LongMemEval. That does not falsify the results, but it limits how far a code-grounded reviewer can verify the evaluation claims. The mechanism we can inspect confidently is the runtime and storage design, not the full empirical pipeline.

## What to Watch

- Whether automatic archiving becomes a central background policy rather than a capability that mostly sits ready beside the live ranking system.
- Whether the connector surface stays coherent as the number of supported agent environments grows; distribution breadth can easily become maintenance drag.
- Whether the git-like context-tree VC layer becomes the dominant collaboration interface, fully displacing older snapshot/space mental models in practice.
- Whether the review queue materially improves curate quality, or mostly shifts operator burden to another UI.
- Whether the benchmark/evaluation layer becomes reproducible from the public repo rather than primarily inspectable through the paper source and reported numbers.
- Whether the system grows richer semantic structure than `related` paths and backlinks, or decides that operational recall is enough and deeper knowledge semantics are out of scope.

---

Relevant Notes:

- [Files, not database](../../notes/files-not-database.md) — exemplifies: ByteRover is a strong production case for a real file substrate, but also shows how much runtime machinery can accumulate around that choice
- [Agents navigate by deciding what to read next](../../notes/agents-navigate-by-deciding-what-to-read-next.md) — contrasts: ByteRover increasingly pre-shapes the agent's next read through search tiers, manifests, and direct-response shortcuts
- [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — extends: `_index.md` summaries, manifest lanes, and archive stubs are three different pointer forms with different costs and guarantees
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: the whole query stack is an optimization around bounded windows and escalating cost
- [Distillation](../../notes/definitions/distillation.md) — extends: summary, manifest, abstract, and stub generation are genuine derived-context artifacts layered over the canonical files
- [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — complicates: the repo exposes how far LLM-mediated curation can be productized before stronger verification becomes necessary
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — foundation: ByteRover's strongest design choice is keeping the memory substrate inspectable even while the runtime grows sophisticated
- [Napkin](./napkin.md) — contrasts: both are file-first agent memory CLIs, but Napkin is lighter and more Obsidian-shaped while ByteRover is a fuller daemon-plus-connector product
- [OpenViking](./openviking.md) — contrasts: both build hierarchical loading aids, but OpenViking virtualizes a database behind filesystem semantics while ByteRover uses real files
- [Supermemory](./supermemory.md) — contrasts: Supermemory is stronger on hosted/open integration surfaces, while ByteRover is stronger on local inspectable substrate and checked-in runtime code
