---
description: "Local multi-agent office with fresh-session runners, git-backed team wiki, per-agent notebooks, trace-to-fact extraction, playbook synthesis, and structured team skills"
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-25"
---

# WUPHF

WUPHF is a local Go application from Nex that presents a Slack-like office for AI teammates: a broker routes messages to Claude Code, Codex, or OpenClaw-backed agents, each turn starts as a fresh headless session, and durable memory lives in either the new git-backed markdown wiki backend or legacy Nex/GBrain backends. The inspected repository is not just a memory layer; it is a full multi-agent runtime with web/TUI surfaces, per-agent worktrees, scoped MCP tools, channel logs, notebooks, a shared wiki, entity extraction, playbook compilation, execution-log synthesis, lint, and team skills.

**Repository:** https://github.com/nex-crm/wuphf

**Reviewed commit:** https://github.com/nex-crm/wuphf/commit/37e96fb5d847179aa6ecbba87083908b3cc5784b

## Core Ideas

**Fresh sessions make memory an explicit substrate rather than hidden chat carryover.** The architecture doc says each agent turn shells out as a one-shot runner with no conversation-persistent session, and the code centers the broker, launcher, scoped MCP server, and isolated worktree as the runtime boundary ([ARCHITECTURE.md](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/ARCHITECTURE.md), [internal/team/headless_claude.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/headless_claude.go), [internal/team/headless_codex.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/headless_codex.go), [internal/team/worktree.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/worktree.go)). This is the important architectural pressure: if every turn is stateless, the broker has to decide what state is durable, what is routed, and what is reintroduced through tools.

**Shared memory is backend-switched, but the markdown wiki is the interesting path.** `registerSharedMemoryTools` exposes exactly one shared-memory tool family: `team_wiki_*`, notebooks, entities, playbooks, lint, and lookup when `WUPHF_MEMORY_BACKEND=markdown`; legacy `team_memory_query/write/promote` when the backend is Nex or GBrain; nothing for `none` ([internal/teammcp/server.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/teammcp/server.go), [internal/team/memory_backend.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/memory_backend.go)). The README still markets "notebook + wiki" across backends, but the code makes the richer notebook/wiki/entity/playbook machinery markdown-backend-specific ([README.md](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/README.md)).

**The team wiki is a real git repo with a single writer and rebuildable indexes.** `Repo.Init` creates `~/.wuphf/wiki/`, commits the initial layout, preserves orphan directories, runs fsck, and maintains a backup mirror; `WikiWorker` serializes all writes through one queue, commits article bytes and `index/all.md` atomically, emits SSE events, and reconciles a derived `WikiIndex` asynchronously ([internal/team/wiki_git.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/wiki_git.go), [internal/team/wiki_worker.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/wiki_worker.go), [internal/team/wiki_index.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/wiki_index.go)). This is not a database with a markdown export: markdown and git are the source of truth, while SQLite/Bleve-style index backends are rebuildable caches.

**Notebooks are the workshop layer inside the same repo.** The notebook tools enforce author-only writes under `agents/{slug}/notebook/`, allow cross-agent reads/searches by design, and submit `notebook_promote` requests for reviewer approval into `team/` wiki paths ([internal/teammcp/notebook_tools.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/teammcp/notebook_tools.go), [internal/team/notebook_worker.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/notebook_worker.go), [internal/team/broker_notebook.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/broker_notebook.go)). That gives WUPHF a concrete draft-to-canonical promotion path rather than only a vague "agents write notes" convention.

**Raw artifacts feed typed facts, entity briefs, and cited lookup.** `CommitArtifact` stores immutable raw artifacts under `wiki/artifacts/{source}/{sha}.md`; `Extractor` reads them, prompts for entities and facts, resolves entities, computes deterministic fact IDs, writes facts into the index, persists new facts to append-only JSONL under `wiki/facts/{kind}/{slug}.jsonl`, and routes failures through a DLQ ([internal/team/artifact_commit.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/artifact_commit.go), [internal/team/wiki_extractor.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/wiki_extractor.go), [docs/specs/WIKI-SCHEMA.md](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/docs/specs/WIKI-SCHEMA.md)). `QueryHandler` then classifies questions, short-circuits out-of-scope queries, retrieves facts, and asks an LLM for JSON with citations ([internal/team/wiki_query.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/wiki_query.go), [internal/team/wiki_lookup.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/wiki_lookup.go)).

**Playbooks compile into skills and learn from execution logs.** A `team/playbooks/{slug}.md` article compiles deterministically into `team/playbooks/.compiled/{slug}/SKILL.md`; the compiled skill tells agents to read the source playbook, execute the steps, and record an outcome through `playbook_execution_record` ([internal/team/playbook_compiler.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/playbook_compiler.go), [internal/team/playbook_executions.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/playbook_executions.go)). After enough executions, `PlaybookSynthesizer` asks an LLM to update only a trailing `## What we've learned` section while preserving the author's body, then the normal wiki write hook recompiles the skill ([internal/team/playbook_synthesizer.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/playbook_synthesizer.go), [internal/team/playbook_synthesizer_v2.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/playbook_synthesizer_v2.go)).

**Team skills are broker-state procedures, not wiki-native knowledge.** The recent commit adds `team_skill_create`; any registered agent can propose a skill, only CEO can create active skills immediately, and human approval requests activate or reject proposals. Invocations increment usage and append channel messages ([internal/teammcp/skills.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/teammcp/skills.go), [internal/team/broker.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/broker.go)). This is a real procedural-memory surface, but it currently lives in `broker-state.json`, not as files in the git wiki. That makes it more operational than the compiled-playbook path.

## Comparison with Our System

| Dimension | WUPHF | Commonplace |
|---|---|---|
| Primary product boundary | Multi-agent office runtime with broker, channels, web UI, scoped MCP, and worktrees | Knowledge-base methodology and repo-native artifact system |
| Canonical knowledge substrate | Markdown/git wiki for the markdown backend; broker JSON for channels/skills; optional Nex/GBrain backends | Markdown files in one repo with frontmatter, links, indexes, validation |
| Work-in-progress layer | Per-agent notebooks under `agents/{slug}/notebook/` plus channel/task state | Workshop directories under `kb/work/` by convention |
| Raw trace layer | `wiki/artifacts/*`, channel messages, execution logs, broker state | Source snapshots, review bundles, work notes; no general session trace substrate |
| Promotion path | Notebook promotion requests, artifact extraction to facts, fact-count-triggered entity brief synthesis, execution-count-triggered playbook learning | Agent/human writing and validation; review gates; explicit note/instruction promotion |
| Procedural memory | `team_skill_*` broker skills plus playbook articles compiled into `SKILL.md` | Skills/instructions as repo files with explicit authoring contracts |
| Retrieval | Literal search, generated `index/all.md`, typed fact index, `/lookup` cited answers, lint | `rg`, generated indexes, descriptions, typed links, explicit traversal |
| Governance | Git attribution, single-writer queue, reviewer promotions, lint, contradiction resolution, CEO-only skill activation | Git, validation, semantic review, type specs, collection-owned link vocabulary |

WUPHF is ahead of commonplace on live multi-agent operations. It has the office, message bus, scoped tool surface, worktree isolation, web UI, channel history, per-agent notebooks, and push-driven wakeups that commonplace mostly treats as external harness concerns. It also implements a concrete workshop-to-library path: raw artifacts and notebook drafts can become facts, briefs, wiki articles, playbook learnings, or skills.

Commonplace is ahead on knowledge-artifact semantics. WUPHF's wiki articles, facts, and playbooks are structured, but the relation language is still mostly wikilinks, fact triplets, generated indexes, and prompt contracts. Commonplace has a richer document-type system, collection-specific writing conventions, semantic link labels, status discipline, and review bundles. WUPHF has a stronger runtime; commonplace has a stronger library methodology.

The deepest convergence is the shared bet that agent memory should not be opaque chat history. WUPHF gets there by making fresh sessions cheap and then rebuilding continuity through wiki/notebook/tool surfaces. Commonplace gets there by making the repository itself the memory substrate. The difference is where each system spends complexity: WUPHF spends it in a broker and derived workers; commonplace spends it in artifact contracts and editorial discipline.

## Borrowable Ideas

**Per-agent notebooks with explicit promotion requests.** Ready to borrow. Commonplace's workshop layer is currently broad and directory-shaped; WUPHF's notebook design is narrower and operationally ergonomic: each agent has an author-owned draft space, peers can inspect it, and promotion creates a reviewable request rather than silently mutating the canonical wiki.

**Single-writer queue for all git-backed runtime writes.** Ready to borrow if commonplace ever supports live agent services. WUPHF's wiki worker serializes wiki, notebook, fact, playbook, lint, and artifact writes through one queue. That is a practical answer to the "many agents commit to one repo" race.

**Compile canonical playbooks into invokable skills.** Ready to borrow conceptually. Commonplace already has skills and instructions, but WUPHF's source-playbook-to-compiled-skill path cleanly separates authored procedure from runtime invocation wrapper and ties every run back to an append-only execution log.

**Keep automated synthesis in a clearly owned trailing section.** Ready to borrow. The playbook synthesizer preserves the author's main body and only replaces `## What we've learned`. That is a useful compromise between autonomous learning and editorial ownership.

**Treat lint findings as wiki artifacts with resolution tools.** Ready to borrow for operational health checks. WUPHF commits daily lint reports and provides a `resolve_contradiction` mutation path over fact logs; commonplace review bundles are stronger semantically, but WUPHF's "report as artifact plus resolver tool" shape is product-ready.

**Backend-switched tool surfaces.** Needs a use case first. WUPHF prevents markdown and Nex/GBrain memory tools from coexisting in one MCP server. That avoids ambiguous agent behavior, but commonplace does not yet have multiple memory backends to switch between.

## Trace-derived learning placement

**Trace source.** WUPHF consumes several trace-like sources: raw artifacts under `wiki/artifacts/{source}/{sha}.md`, channel/task broker state, per-agent notebook drafts, append-only playbook execution logs, and optionally external backend context. The strongest qualifying traces are the artifact ingestion path and playbook execution logs: both are durable records of prior work that later workers transform into future behavior-changing artifacts.

**Extraction.** The artifact path uses an LLM extractor to produce entities and typed facts, then deterministic resolver/fact-ID/gate code writes index rows and append-only JSONL fact logs. The playbook path uses execution-count thresholds, feeds recent executions plus optional reinforced cross-entity clusters into an LLM, and commits only the learned trailing section after a preservation merge.

**Storage substrate, form, and lineage.** WUPHF uses a local file/git substrate for raw artifacts, notebook drafts, wiki pages, playbooks, JSONL logs, and derived indexes. The retained forms are mixed readable and symbolic: raw artifacts, notebooks, wiki articles, and synthesized briefs are prose files; fact logs, entity rows, triplets, graph edges, lint findings, and execution logs are symbolic records; derived indexes are rebuildable operational caches. The lineage path is raw artifact or execution log -> extractor/resolver/synthesis step -> wiki fact, brief, index, or learned playbook section. No weight updates are present.

**Behavioral authority.** Entity facts and briefs are mostly knowledge artifacts: agents query them for sourced answers. Compiled playbook skills and broker team skills are system-definition artifacts: reading or invoking them changes how an agent acts. Playbook synthesis is the clearest trace-to-policy loop because execution outcomes revise the future procedure wrapper.

**Scope.** Workspace/team-scoped. The system is not a benchmark learner; it is an office runtime where multiple role agents share one local wiki and broker state. Legacy Nex/GBrain backends can move memory outside the local wiki, but the inspected trace-derived mechanics are local.

**Timing.** Online and staged. Raw writes happen during normal operation; extraction and index reconciliation run asynchronously; entity and playbook synthesis run when thresholds are crossed or when requested; lint can run manually or on a cron-like path.

**Survey placement.** On the [survey axes](../trace-derived-learning-techniques-in-related-systems.md), WUPHF sits between SignetAI and OpenViking: a runtime-owned trace backend with a local file/git canonical substrate, not a hosted service database and not a pure promptware wiki. It strengthens the survey's "raw-first capture plus derived artifact" pattern and adds a distinctive procedure-learning subtype: execution logs update a bounded learned section, which then recompiles into an invokable skill.

## Curiosity Pass

**The markdown wiki is strong, but not all memory is in it.** The wiki, notebooks, facts, artifacts, playbooks, and lint reports are git-backed. Broker channels, requests, scheduler jobs, shared-memory fallback state, and team skills live in `broker-state.json` ([internal/team/broker.go](https://github.com/nex-crm/wuphf/blob/37e96fb5d847179aa6ecbba87083908b3cc5784b/internal/team/broker.go)). That is reasonable for a live app, but it means "shared brain" is split across two persistence models. The compiled-playbook path is more inspectable than the `team_skill_create` path.

**The wiki-schema document is more ambitious than the currently wired paths.** `docs/specs/WIKI-SCHEMA.md` describes a full three-layer architecture with artifacts, facts, insights, playbooks, lint, redirects, and graph logs. The code implements large parts of that, but some paths are still uneven: normal `team_wiki_write` writes article bytes directly; rich artifact extraction requires callers to use artifact-specific paths; team skills do not round-trip through wiki files.

**The extraction loop has better substrate discipline than many memory systems.** The fact-log persistence code explicitly protects the rebuild guarantee after in-memory submission succeeds. That is the kind of failure-mode thinking missing from many LLM memory repos: if the derived index can be wiped, every accepted fact needs a file-backed row that can rebuild it.

**The playbook learning loop is refreshingly bounded.** It does not let an LLM rewrite the canonical procedure. It gives the model one owned section, detects missing headings, stamps counters, and relies on git diffs. The mechanism can still produce poor advice, but the blast radius is constrained and auditable.

**Fresh-session economics may be doing as much work as memory.** The benchmark story depends on prompt caching, scoped tools, and no accumulated history. That is adjacent to memory design but not reducible to it. WUPHF is partly a memory system and partly a cost/control architecture for multi-agent execution.

## What to Watch

- Whether team skills move from broker JSON into the git wiki or stay as operational broker state.
- Whether notebook promotion becomes a robust review workflow with clear reviewer ownership, not just a request queue.
- Whether artifact ingestion gets first-class UI/tool paths for chat, email, meeting, and manual sources, or remains mostly internal plumbing.
- Whether `/lookup` quality improves through better retrieval over articles plus facts, rather than fact index search alone.
- Whether playbook execution logs produce genuinely useful `## What we've learned` sections after repeated real runs.
- Whether the markdown wiki remains the default backend as Nex/GBrain compatibility and hosted integrations grow.

---

Relevant Notes:

- [Files, not database](../../notes/files-not-database.md) — exemplifies: WUPHF's markdown backend makes git files canonical and treats indexes as rebuildable caches, though broker state remains JSON
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — implements: per-agent notebooks are a concrete draft workspace with promotion into a shared wiki
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: fresh sessions, scoped MCP tools, generated indexes, and cited lookup all optimize bounded context rather than growing chat history
- [Agent statelessness means the context engine should inject context automatically](../../notes/agent-statelessness-means-the-context-engine-should-inject-context.md) — exemplifies: WUPHF makes every agent turn stateless and reintroduces continuity through broker-selected tools and memory surfaces
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) — complicates: WUPHF automates extraction and bounded playbook learning, but still relies on review, lint, and owned sections to control synthesis risk
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — exemplifies: execution logs and playbook recompilation improve future behavior through readable artifacts rather than model weights
- [Skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) — extends: WUPHF has both broker-state team skills and wiki playbooks compiled into invokable `SKILL.md` files
- [OpenViking](./openviking.md) — compares: both own a runtime/session boundary and mine traces into durable memory, but OpenViking uses virtual filesystem service storage while WUPHF's markdown backend uses real git files
- [SignetAI](./signetai.md) — compares: both are runtime context layers with trace extraction and broad agent integration, but Signet is cross-harness daemon/database infrastructure while WUPHF is a multi-agent office with a local git wiki
- [LLM Wiki](./llm-wiki.md) — compares: both use markdown wiki framing, but LLM Wiki is primarily promptware/protocol while WUPHF implements a broker, git writer, extractor, index, lint, and web UI
