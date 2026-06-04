---
description: "Signet AI review: local-first cross-harness memory daemon with SQLite recall, transcript distillation, graph context, and hook-based push activation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# Signet AI

Signet AI, from the `Signet-AI/signetai` repository, is a local-first portable context layer for AI coding and assistant harnesses. It runs a daemon, CLI, SDK, dashboard, connectors, skills, and benchmark harness around a SQLite-backed memory substrate; its strongest memory-system claim is that session traces, explicit remembers, workspace documents, skills, identity, and graph state can survive across Claude Code, OpenCode, OpenClaw, Codex, Gemini CLI, Pi, Oh My Pi, Hermes Agent, and related harnesses.

**Repository:** https://github.com/Signet-AI/signetai

**Reviewed commit:** [b7f5176bc4280baceace933d2442d4b04796b336](https://github.com/Signet-AI/signetai/commit/b7f5176bc4280baceace933d2442d4b04796b336)

**Last checked:** 2026-06-02

## Core Ideas

**The daemon owns the durable memory substrate.** Signet's baseline schema stores memories, embeddings, conversations, FTS indexes, and optional `sqlite-vec` vectors in the local workspace database; later migrations add transcript, temporal, graph, skill, feedback, recall-dedupe, and ontology-control tables (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/core/src/migrations/001-baseline.ts, https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/core/src/migrations/040-session-transcripts.ts, https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/docs/ARCHITECTURE.md). The operational source of truth is SQLite plus workspace artifacts, not a hosted chat app.

**Memory is captured from both explicit and ambient paths.** Agents or users can call `remember`, while harness hooks capture prompt snapshots, session-end transcripts, compaction summaries, and checkpoint state (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/routes/hooks-routes.ts, https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/hooks.ts). The prompt-submit path appends or rewrites canonical transcript state before retrieval; session-end preserves the retained transcript and queues summary work when the pipeline is enabled (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/hooks.ts).

**The trace-derived pipeline promotes raw text cautiously.** `extractFactsAndEntities` asks an LLM for bounded facts and entities, validates the parsed JSON, strips reasoning blocks, caps input and output, and returns warnings instead of trusting arbitrary model output (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/pipeline/extraction.ts). The worker then runs shadow decisions, prefetches embeddings outside the write transaction, applies write gates and confidence checks, deduplicates by normalized content hash, and records proposals in `memory_history` before writing derived facts through `txIngestEnvelope` (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/pipeline/worker.ts).

**Recall is a multi-channel authorized retrieval pipeline.** `hybridRecall` explicitly splits candidate collection from content handling: FTS, generated hints, vector search, structured-path search, temporal candidates, and graph traversal collect IDs and scores first; only after authorization can content be read, reranked, dampened, hydrated, or access-tracked (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/memory-search.ts). Context efficiency is therefore engineered by limits, top-k, score thresholds, hint caps, traversal budgets, reranker budgets, dedupe, and an authorization boundary rather than by loading every retained record.

**Push activation is real, but narrow.** The session-start route returns ready-to-inject identity, memories, and recent context; prompt-submit builds a `## Relevant Entity Context` block only when a user prompt matches known entities or active aliases, then selected attributes clear a min-score threshold and fit the injection budget (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/routes/hooks-routes.ts, https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/hooks.ts). This is engineered read-back before the next model action, not just a search API.

**Procedural memory is treated as graph state.** Installed `SKILL.md` files become skill entities with metadata, embeddings, optional LLM-enriched descriptions/triggers/tags, and graph relations extracted from the skill body (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/docs/PROCEDURAL-MEMORY.md, https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/core/src/migrations/018-skill-meta.ts). That gives procedural artifacts a path into the same retrieval substrate as declarative memories, though the docs mark full skill retrieval and decay as still partial.

## Artifact analysis

- **Storage substrate:** `sqlite` — Local SQLite under the Signet workspace, especially `memories`, `memories_fts`, `embeddings`, optional `vec_embeddings`, access counters, source fields, scope/project/agent fields, and history tables (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/core/src/migrations/001-baseline.ts)
- **Representational form:** `prose` `symbolic` `parametric` — prose memory content plus symbolic metadata, FTS rows, hashes, graph state, scores, and distributed-vector embeddings
- **Lineage:** `authored` `imported` `trace-extracted` — explicit remembers and authored skills/config, imported documents and workspace artifacts, and session/prompt/compaction traces all feed retained state
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — recalled memories advise as knowledge; hooks, prompt blocks, write gates, authorization, graph paths, validators, scores, and trace pipelines instruct, gate, route, validate, rank, and learn

**Memory rows, embeddings, FTS, and vector state.** Storage substrate is local SQLite under the Signet workspace, especially `memories`, `memories_fts`, `embeddings`, optional `vec_embeddings`, access counters, source fields, scope/project/agent fields, and history tables (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/core/src/migrations/001-baseline.ts). Representational form is mixed: prose memory content plus symbolic metadata, FTS rows, hashes, and distributed-vector embeddings. Lineage is authored, imported, explicitly remembered, extracted from session summaries, or pipeline-derived from source memories; content hashes and source IDs provide dedupe and provenance. Behavioral authority is mostly knowledge artifact authority when recalled as context or evidence, but embeddings, FTS, access counters, and ranking metadata have system-definition authority over what later agents see.

**Raw transcripts, prompt snapshots, compaction summaries, and temporal heads.** Storage substrate is `session_transcripts`, summary jobs, `session_summaries`, generated memory/artifact files, and canonical transcript artifacts (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/core/src/migrations/040-session-transcripts.ts, https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/core/src/migrations/044-memory-md-temporal-head.ts, https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/hooks.ts). Representational form is mixed JSONL/markdown/prose plus symbolic session metadata. Lineage is trace-derived from prompt-submit snapshots, live session appends, session-end transcripts, and compaction events; summaries and temporal heads are derived views. Behavioral authority starts as evidence and fallback context, then strengthens when summaries, MEMORY.md synthesis, or session facts are injected or indexed for future recall.

**Pipeline proposals, facts, hints, graph rows, and scores.** Storage substrate is SQLite job, history, hint, graph, entity, attribute, session-score, and feedback tables plus pipeline code (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/pipeline/worker.ts, https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/pipeline/summary-worker.ts, https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/core/src/migrations/038-memory-hints.ts). Representational form is symbolic state with prose claims and optional embeddings. Lineage is LLM-derived, validator-filtered, write-gated, or feedback-derived from source memories and session traces. Behavioral authority is system-definition authority for promotion, ranking, traversal, currentness, and recall quality; the same derived fact also acts as a knowledge artifact when surfaced to an agent.

**Knowledge graph, ontology attributes, aliases, and procedural skill nodes.** Storage substrate is graph/entity/attribute/dependency tables, skill metadata, installed skill files, and reconciler code. Representational form is mixed symbolic/prose: entity names, aspects, attributes, constraints, claim/group keys, aliases, triggers, tags, and skill bodies. Lineage is mixed: authored skill files, explicit ontology repair, inline entity linking, extraction output, and reconciler-enriched metadata. Behavioral authority ranges from knowledge artifact context to routing and activation authority; graph paths decide which memories and attributes can enter prompt-submit and recall outputs.

**Hooks, connectors, MCP tools, and injected blocks.** Storage substrate is repository code, installed harness config, generated agent files, daemon runtime config, and built-in skills. Representational form is executable symbolic code plus prose prompt blocks. Lineage is authored system-definition code and user configuration. Behavioral authority is high: hooks decide when memory is captured, whether bypass applies, what gets injected before a turn, and which explicit recall/remember tools are available (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/integrations/codex/plugin/plugins/signet/hooks/hooks.json, https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/integrations/openclaw/memory-adapter/src/index.ts).

**Promotion path.** Signet's main promotion chain is raw session/prompt/document/remember text -> stored raw artifact or source memory -> LLM-extracted facts/entities and summary facts -> controlled-write memory rows, graph state, hints, summaries, and scores -> recall or hook injection. A separate procedural chain promotes `SKILL.md` files into graph nodes and embeddings. This is a cross-form and cross-authority promotion: raw evidence can become derived knowledge artifacts, ranking/control artifacts, and eventually pre-action prompt context.

## Comparison with Our System

| Dimension | Signet AI | Commonplace |
|---|---|---|
| Primary purpose | Runtime portable memory and context layer across agent harnesses | Git-tracked methodology KB and review system for agents |
| Canonical substrate | SQLite daemon database plus workspace files, artifacts, installed hooks, and dashboard | Markdown files, type specs, validation, indexes, reports, and git history |
| Capture | Ambient hooks, transcripts, compaction, explicit remember, imports, skills, documents | Agent-authored notes/reviews, source snapshots, explicit validation and review workflows |
| Retrieval | Hybrid FTS/vector/hints/graph/traversal/reranker/temporal recall plus entity prompt context | `rg`, curated/generated indexes, links, skills, type contracts, review bundles |
| Activation | Pull tools plus session-start and entity-gated prompt-submit push | Mostly pull through search/indexes/links; instructions can be always-loaded by harness |
| Governance | Scope/project/agent filters, bypass, write gates, shadow mode, history, repair, feedback | Collection contracts, schemas, citation rules, validation, semantic review, git diffs |

Signet is stronger as a live operational substrate. It already wires many harnesses, captures session state without asking the agent to remember a workflow, and can inject bounded entity context before a prompt. Its database-first architecture also lets it maintain access counts, feedback scores, dedupe ledgers, traversal caches, and structured graph views that would be awkward as plain markdown.

Commonplace is stronger as a durable argument and method library. Signet's behavior-shaping state is distributed across daemon code, config, SQLite rows, hook installers, embeddings, graph state, and generated artifacts. Commonplace keeps its strongest artifacts in reviewable prose and schemas where a later agent can inspect every claim and cite the source. The tradeoff is speed: Signet promotes operational traces quickly; Commonplace promotes slowly but with stronger textual accountability.

**Read-back:** `both` — Agents can explicitly pull through CLI/API/MCP recall and search surfaces, while session-start and entity-gated prompt-submit hooks push selected retained memory into the receiving agent's prompt path before action.

### Borrowable Ideas

**Entity-gated prompt-submit injection.** Commonplace could add an opt-in hook that only injects current structured context when a prompt names a known entity and a narrow aspect clears a score threshold. Ready as a design pattern; implementation should wait for a concrete host integration and audit format.

**Keep candidate IDs separate from authorized content.** Signet's recall boundary is a useful invariant: high-recall channels can over-fetch IDs, but no content-bearing rerank, summary, or hydration stage runs until authorization. Commonplace can borrow this immediately for any future vector/graph layer.

**Shadow-mode extraction history.** Pipeline proposals recorded without mutation are a good middle stage between "LLM said it" and "the KB changed." Commonplace could use a similar ledger for proposed note updates and review-gate findings. Ready for review tooling.

**Prospective hints as cue bridges.** Generated future-query hints solve a real retrieval problem: users ask with different words than the stored fact. Commonplace should not add this globally yet, but it is promising for high-volume source snapshots or review reports.

**Continuity scoring against injected memory.** Signet's summary worker scores whether pre-loaded memories were actually relevant to the session. Commonplace could use that as an evaluation idea for agent-loaded review bundles, but it needs a controlled task set before it should influence ranking.

**Do not borrow database opacity for durable methodology claims.** Signet's live utility depends on SQLite rows, vectors, and feedback loops. Commonplace should keep durable claims and instructions as inspectable markdown, using a database only as an operational index or staging layer.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` `event-streams` — prompt-submit events, live/canonical session transcripts, session-end transcripts, compaction summaries, and injected-memory feedback are the qualifying trace signals.

**Learning scope:** `per-task` `per-project` `cross-task` — trace state is scoped by session as well as workspace, project, agent, harness, and memory visibility group, then reused across future recall and hook paths.

**Learning timing:** `online` `staged` — prompt-submit updates transcript state before the turn, while session-end summary work and pipeline fact extraction run as queued or worker-driven stages.

**Distilled form:** `prose` `symbolic` `parametric` — summaries and facts are prose, graph entities/attributes/hints/scores are symbolic, and vectors participate in the distilled retrieval substrate.

**Trace source.** Signet qualifies as trace-derived. The qualifying trace signals are prompt-submit events, live/canonical session transcripts, session-end transcripts, compaction summaries, and injected-memory feedback. Explicit remember calls and imported documents can enter the same extraction substrate, but they are adjacent source inputs rather than the basis for the trace-derived tag. The central qualifying trace is the agent/user session transcript, not merely user-authored notes.

**Extraction.** Extraction has several stages. Prompt-submit and session-end preserve raw or cleaned transcript material. The summary worker chunk-summarizes long transcripts, inserts session facts, writes summary artifacts, writes temporal DAG nodes, and scores continuity from the transcript plus injected memories (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/pipeline/summary-worker.ts). The Pipeline V2 worker extracts facts/entities from memory content, runs decision proposals, and applies controlled writes only when enabled, above confidence, not frozen, not duplicate, and passing write gates (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/pipeline/worker.ts). The oracle is mixed: LLM extraction and summarization, deterministic validation, confidence thresholds, dedupe, write gates, optional contradiction checks, and operator config.

**Four fields.** Raw traces are stored as session transcript rows, canonical artifacts, prompt/session checkpoint state, and summary jobs; their form is prose/JSONL plus symbolic metadata; lineage is direct runtime execution; behavioral authority is evidence, replay, fallback, and learning input. Distilled artifacts are derived facts, summaries, temporal heads, graph entities/attributes, hints, session scores, and possibly MEMORY.md synthesis; their form is prose plus symbolic metadata and vectors; lineage is LLM-derived or code-derived from raw traces and source memories; authority ranges from recalled knowledge artifact to system-definition ranking, traversal, injection, and synthesis control.

**Scope and timing.** Scope is per workspace, project, agent, harness, session, and optional memory visibility group. Timing is both online and staged: prompt-submit updates transcript state before the turn, session-start/prompt-submit can inject before action, session-end queues asynchronous summary jobs, and pipeline workers process extracted facts after writes. Shadow mode and frozen mutations let operators run the trace-learning loop without applying changes.

**Survey placement.** Signet belongs in the service-local session-memory branch of the trace-derived survey: it owns a runtime memory daemon, captures live harness traces, distills them into symbolic/prose artifacts, and reactivates them through recall and hooks. It strengthens the survey claim that useful agent memory often promotes traces into external artifacts rather than model weights. It also splits trace-derived systems by authority speed: Signet has richer live activation than report-only systems, but weaker review-before-promotion than Commonplace.

## Read-back placement

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` — session-start does coarse bounded memory loading, while prompt-submit resolves entity names and aliases as identifiers and scores prompt residue through embedding or lexical fallback.

**Faithfulness tested:** `no` — continuity scoring audits relevance of injected memories, but the review does not report a with/without ablation proving that injected context changes downstream behavior.

**Direction.** Signet is both pull and push. Pull is explicit `signet recall`, `/recall`, MCP/API recall, dashboard inspection, session search, and source expansion. Push is session-start injection and entity-gated user-prompt-submit injection from the receiving agent's perspective. Shipped system prompts, plugin prompt contributions, secret listings, and command affordance text are baseline context surfaces; the read-back verdict rests on retained identity/user/working-memory files, SQLite memory rows, session recovery context, inherited session context, and entity attributes.

**Targeting and signal.** Signet has mixed push targeting. Session-start is mostly `coarse`: a lifecycle hook always attempts bounded memory loading, scoring recent/project-matching memories by effective score, pinned state, recency, and configured budgets, with additional project/session-key scoped recovery and traversal blocks. Prompt-submit is `instance`: it first resolves known entity names and aliases carried by the current prompt, so that narrowing is `identifier`, then computes the non-entity prompt residue and selects entity attributes by `inferred / embedding` when embeddings are available, falling back to `inferred / lexical` scoring. Precision/recall, prompt dilution, and actual model uptake are not verified from code (https://github.com/Signet-AI/signetai/blob/b7f5176bc4280baceace933d2442d4b04796b336/platform/daemon/src/hooks.ts).

**Injection point.** Session-start injects before the new session begins. Prompt-submit runs before each user turn is handed to the model. Pre-compaction and compaction-complete run around summarization and can only affect later actions, not the action already taken.

**Selection, scope, and complexity.** Prompt-submit has a tight default injection budget and min score; full recall has broader FTS/vector/hint/graph/traversal/reranking channels, limit normalization, authorization, dedupe, and optional aggregate synthesis. This reduces prompt dilution compared with unconditional always-load, but effective precision/recall is not verified from code.

**Authority at consumption.** Injected context has advisory prompt authority: it can change the next model step, but the system does not prove the model obeyed it. Session-start identity and Memory Check Loop text have stronger instruction-like authority because they are prepended to the system prompt path. The continuity scorer evaluates relevance of injected memories after the session, but that is an audit signal rather than a pre-action faithfulness guarantee.

**Other consumers.** Humans consume the CLI, dashboard, docs, and artifact files. The daemon consumes feedback, scores, access counts, graph state, and summary DAGs as control state. Connectors consume hook responses and translate them into harness-specific hidden or prepended memory blocks.

## Curiosity Pass

**The main contribution is activation, not storage.** SQLite, FTS, vectors, and graph traversal are substantial, but the more discriminating design choice is wiring memory into the session lifecycle so context can arrive before the agent asks for it.

**The system contains several memory models at once.** Signet has declarative facts, session summaries, transcripts, MEMORY.md temporal heads, graph attributes, skills, feedback ledgers, hints, and source documents. That breadth is powerful but makes lineage and authority easy to blur unless each consumer path names which artifact it trusts.

**The graph is both retrieval structure and ontology control surface.** Entity/aspect/attribute rows are not just browsable metadata; prompt-submit uses them to decide what enters context. That gives graph quality direct behavioral consequences.

**Trace-derived does not mean fully autonomous learning.** The pipeline has shadow mode, write gates, mutation freezes, update/delete controls, confidence thresholds, and repair surfaces. The code is closer to cautious artifact promotion than to unconstrained self-modification.

**Memorybench is valuable but not the memory system itself.** The repository includes a benchmarking framework and Signet provider, but the reviewed memory architecture stands on the daemon, pipeline, hooks, recall, and connectors. Benchmark claims should be treated as evaluation artifacts, not implementation behavior.

## What to Watch

- Whether prompt-submit moves beyond entity-name matching into stronger intent matching without increasing prompt dilution.
- Whether MEMORY.md synthesis and temporal heads preserve enough source IDs, prompt versions, and model metadata to audit distilled continuity claims.
- Whether procedural skill retrieval becomes a first-class injected context path; that would raise skill nodes from indexed procedural memory to active instruction selection.
- Whether continuity scoring starts influencing ranking or write gates. That would turn an audit artifact into a system-definition artifact.
- Whether cross-harness connectors keep equivalent capture and injection semantics, or whether some harnesses become memory-write-only while others get full push activation.
- Whether the ontology-control plane matures into reviewable proposals with explicit promotion gates comparable to Commonplace's type and validation contracts.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Signet distills session and prompt traces into memories, summaries, graph state, hints, scores, and hook-injected context.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Signet implements explicit hook paths that activate stored memory before a model step.
- [Activate Behavior-Changing Memory Before The Mistake](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: prompt-submit and session-start can deliver relevant context before action.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Signet's transcripts, memories, summaries, graph rows, hints, skills, hooks, and scores differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: memories, transcripts, summaries, source chunks, and recalled context mainly advise or evidence future work.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: hooks, pipeline gates, ranking metadata, graph traversal, config, skills, and injection code route or constrain behavior.
