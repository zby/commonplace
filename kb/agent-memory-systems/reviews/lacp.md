---
description: "LACP review: local control-plane agent harness with trace-learning Obsidian/SMS memory, hook-time context injection, RAG pull, and policy gates"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-learning]
---

# LACP

LACP, from 0xNyk's `0xNyk/lacp` repository, is a local-first agent harness for Claude, Codex, and related CLI agents. At the reviewed commit it combines policy-gated execution, hook-based Claude Code context injection, Obsidian-style knowledge storage, a trace-derived memory pipeline, an SMS self-memory module, hybrid sparse/dense retrieval indexes, and local verification gates. The review below treats retained memory separately from the shipped baseline instructions, context-mode files, and live safety/eval gates.

**Source:** https://github.com/0xNyk/lacp

**Reviewed commit:** [003eef16a583dbaa3fdd56e5efe393397f463f3f](https://github.com/0xNyk/lacp/commit/003eef16a583dbaa3fdd56e5efe393397f463f3f)

**Last checked:** 2026-06-04

## Core Ideas

**LACP is a harness first, memory system second.** The top-level README frames the system around policy gates, verification artifacts, execution tiers, hooks, and a "5-layer memory stack"; the dispatcher exposes many control-plane commands alongside `brain-*`, `obsidian`, `context`, `sms`, and RAG-related commands ([README.md](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/README.md), [bin/lacp](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/bin/lacp)). Its memory behavior should therefore be read as part of a governed agent operating environment, not as a standalone notes app.

**Retained memory is file-backed and multi-layered.** Durable memory lives across Obsidian vault notes, `~/control/knowledge/knowledge-memory` registries/indexes, Claude project `MEMORY.md` files, handoff JSON, `~/.lacp/sms/*.jsonl` and JSON state, and staging files under `~/.lacp/memory-staging` ([Memory/README.md](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/Memory/README.md), [hooks/self_memory_system.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/self_memory_system.py), [hooks/extract_memories.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/extract_memories.py), [automation/scripts/sync_research_knowledge.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/automation/scripts/sync_research_knowledge.py)). The substrate is inspectable files rather than a service store.

**Context efficiency is mostly budgeted injection plus pull retrieval.** `session_start.py` collects candidate context blocks, assigns priorities, estimates tokens, and stops adding lower-priority blocks when `LACP_SESSION_BUDGET_TOKENS` would be exceeded; `MEMORY.md` has a 200-line/25KB guard; RAG query returns top-k chunks from a local hybrid index ([hooks/session_start.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/session_start.py), [automation/scripts/memory_index_guard.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/automation/scripts/memory_index_guard.py), [automation/scripts/query_memory_rag.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/automation/scripts/query_memory_rag.py)). Context complexity is bounded by coarse priority ordering, line caps, chunking, and top-k, not by a deeply typed semantic contract.

**Agent traces feed durable memory.** The Stop hook can extract memory-worthy signals from the last assistant message and append JSONL staging records; `brain-expand --apply` promotes those staged records into Obsidian inbox notes; the stop quality gate also writes SMS episodes and updates a self-model from session summaries, changed files, and test-failure signals ([hooks/extract_memories.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/extract_memories.py), [bin/lacp-brain-expand](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/bin/lacp-brain-expand), [hooks/stop_quality_gate.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/stop_quality_gate.py)).

**The memory graph has automatic maintenance beyond capture.** `sync_research_knowledge.py` exact-dedups and semantic-dedups incoming signals, merges observations/provenance/categories into existing items, computes semantic/temporal/causal edges, scores promotion, writes graph notes and indexes, and marks related existing nodes as evolved; consolidation code can generate synthesis notes, detect conflicts, mark superseded losers, and archive low-strength items ([automation/scripts/sync_research_knowledge.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/automation/scripts/sync_research_knowledge.py), [automation/scripts/consolidate_research.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/automation/scripts/consolidate_research.py), [automation/scripts/memory_consolidation.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/automation/scripts/memory_consolidation.py)).

**Live gates are not retained-memory read-back by themselves.** Risk routing, context contracts, pretool guards, write validation, and stop quality gates shape behavior, but their baseline rules are shipped/configured system-definition artifacts rather than memories learned from use ([hooks/pretool_guard.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/pretool_guard.py), [hooks/write_validate.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/write_validate.py), [hooks/stop_quality_gate.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/stop_quality_gate.py)). They matter for governance, but they do not by themselves make a memory read-back path.

## Artifact analysis

- **Storage substrate:** `files` - LACP stores the behavior-shaping memory surfaces in local files: Obsidian Markdown notes, JSON registries, RAG indexes, hook contracts/state, staging JSONL, handoff JSON, SMS JSONL/JSON, and Claude project `MEMORY.md` files.
- **Representational form:** `prose` `symbolic` `parametric` - Markdown notes and injected summaries are prose; frontmatter, registries, hook contracts, policies, scores, edges, and command outputs are symbolic; sparse/dense vectors and embeddings in the RAG/research registry act as parametric retrieval state ([automation/scripts/build_memory_rag_index.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/automation/scripts/build_memory_rag_index.py), [automation/scripts/sync_research_knowledge.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/automation/scripts/sync_research_knowledge.py)).
- **Lineage:** `authored` `imported` `trace-extracted` - Context-mode files, policies, docs, focus files, and manual notes are authored; URLs/text/media and inbox notes are imported; Claude transcripts, assistant messages, daily session artifacts, handoffs, and stop-hook summaries are trace-extracted.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` - Notes and graph nodes provide knowledge; `CLAUDE.md`/`AGENTS.md`, context modes, focus, SMS summaries, and hook injections can instruct; pretool/write/stop gates enforce or validate; route/context commands select execution paths; RAG/registry scores rank recall; SMS and graph update paths learn from traces.

**Obsidian and research graph notes.** These are Markdown-plus-frontmatter knowledge artifacts, with provenance fields, categories, links, statuses, confidence, and generated indexes. `brain-ingest` can create link notes with schema-ready metadata, `brain-promote` can move inbox notes to permanent vault directories, and `sync_research_knowledge.py` materializes promoted research items as graph Markdown ([bin/lacp-brain-ingest](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/bin/lacp-brain-ingest), [bin/lacp-brain-promote](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/bin/lacp-brain-promote), [automation/scripts/sync_research_knowledge.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/automation/scripts/sync_research_knowledge.py)).

**Research registry and graph edges.** `registry.json` is the core symbolic memory index for research signals: normalized text ids, observations, provenance, categories, evidence URLs, storage/retrieval strength, embeddings, and semantic/temporal/causal edges. It has ranking and learning authority because it decides what becomes graph-visible and how later access structures are weighted.

**RAG index.** `hybrid-index.json` stores chunk text, sparse vectors, optional dense vectors, IDF values, chunk metadata, and Ollama embedding metadata; `query_memory_rag.py` combines sparse, dense, lexical, and reciprocal-rank-fusion scoring. This is a ranking artifact and a pull retrieval surface, not a push system by itself ([automation/scripts/build_memory_rag_index.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/automation/scripts/build_memory_rag_index.py), [automation/scripts/query_memory_rag.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/automation/scripts/query_memory_rag.py)).

**Session-start injected state.** Focus briefs, recent handoffs, SMS context, memory-cap warnings, git/test context, health snapshots, workflow reminders, and context-mode files are assembled into a `systemMessage` before a Claude Code session starts. Only the focus/handoff/SMS/MEMORY-derived pieces are retained-memory read-back; baseline context modes and hardcoded reminders are configured instructions ([hooks/session_start.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/session_start.py)).

**SMS artifacts.** Episodes, epochs, narratives, and self-model JSON persist under `~/.lacp/sms`; Stop hooks record episodes and update the self-model, while session-start builds a small context block from current focus, self-model, narrative, and recent significant episodes ([hooks/self_memory_system.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/self_memory_system.py), [hooks/stop_quality_gate.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/stop_quality_gate.py), [bin/lacp-sms](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/bin/lacp-sms)).

The promotion path is real but mixed: staged trace signals can become inbox notes, registry items can become graph notes, clusters can become synthesis notes, and some memories can be marked stale/superseded or archived. LACP can therefore move material from trace-derived prose into symbolic/parametric access structures and stronger instruction/ranking surfaces, but manual review is still part of the advertised quality workflow ([docs/memory-quality-workflow.md](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/docs/memory-quality-workflow.md)).

## Comparison with Our System

LACP and Commonplace both prefer local files, command-line operations, explicit provenance, and validation over opaque hosted memory. The difference is center of gravity. Commonplace is a typed knowledge-base methodology with collection contracts, validation, indexes, and review workflows; LACP is an agent execution control plane that also maintains memory.

LACP is stronger on hook-time operational integration: it can push handoff/SMS/focus state into a live Claude session, record sessions, route risky commands, and block low-quality stops. Commonplace is stronger on library semantics: artifact types, review standards, link contracts, durable source grounding, and validation make the knowledge layer easier to inspect and govern.

LACP's automatic maintenance is more ambitious than Commonplace's current generated indexes. It performs semantic dedup, edge construction, promotion scoring, consolidation, active recall probes, forgetting/pruning, and SMS self-model updates. That ambition also creates more hidden authority: a corrupted registry, stale embedding index, or overzealous pruning run can change what memory reaches future agents.

### Borrowable Ideas

**Session-start memory budget ordering.** Commonplace could borrow the priority-ordered context assembly pattern for generated session briefs. Ready now as a small command-output convention, provided each injected block is labeled by source and authority.

**Memory-cap guards for routing documents.** LACP treats `MEMORY.md` as a routing document with hard line/byte caps. Commonplace could apply similar caps to high-load entrypoint docs and warn before they become stores. Ready now.

**Active recall probes.** LACP tests whether important items can be retrieved from the RAG index. A Commonplace analogue would test whether indexes/search/link paths can recover target notes from expected prompts. Needs a concrete retrieval layer beyond `rg` and generated indexes.

**Trace-to-inbox staging.** LACP's staged JSONL extraction keeps low-latency trace capture separate from later promotion. Commonplace could use the same split for workshop logs or review observations. Useful, but only with a review gate so trace noise does not become instruction.

**Do not borrow implicit self-model authority wholesale.** SMS context can be useful, but Commonplace should keep agent identity/self-model claims clearly scoped and reviewable before they influence high-authority behavior.

## Write side

**Write agency:** `manual` `automatic` - Users and agents can author/edit/promote notes manually, while hooks and maintenance commands automatically extract trace signals, update registries, build indexes, score promotion, write graph nodes, synthesize epochs, and update the SMS self-model.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `invalidate` `decay` `promote` - `consolidate_research.py` creates canonical synthesis notes from clusters; `semantic_dedup` and normalized text ids merge duplicates; `sync_research_knowledge.py` updates existing categories, provenance, storage strength, edges, and `last_evolved`; Ollama-backed consolidation generates new insight text across clustered signals; contradiction/supersession paths mark losers stale or superseded; retrieval strength decays and consolidation can archive weak items; promotion scoring and `brain-promote` move items toward graph/permanent status.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` - LACP reads Claude transcript JSONL, last assistant messages, session ids, cwd, changed-file traces, hook contracts, daily session files, and inbox notes derived from agent activity.

**Extraction** - The low-latency Stop-hook extractor uses regex indicators for decisions, lessons, architecture choices, process rules, and user corrections, deduplicates within the extraction, and writes up to five signals to staging. The stop quality gate separately records SMS episodes from final assistant text plus changed-file and eval-checkpoint context. Later `brain-expand` and research-sync scripts promote, classify, embed, dedup, score, and connect those traces.

**Learning scope:** `per-project` `cross-task` - Handoff and Claude project memory are project-scoped; the knowledge-memory registry, research graph, RAG index, SMS root, and promotion/consolidation scripts can accumulate across tasks and sessions.

**Learning timing:** `online` `staged` `offline` - Stop hooks write trace-derived state online; `brain-expand` promotes staged signals and synthesizes epochs in a staged workflow; RAG builds, promotion suggestions, consolidation, probes, and benchmark pipelines are offline maintenance.

**Distilled form:** `prose` `symbolic` `parametric` - Distillation outputs include Markdown inbox/graph/synthesis notes, JSON registry state and graph edges, and sparse/dense vector indexes.

On the trace-learning survey axes, LACP is a hybrid trace-to-memory control plane: it has online capture, staged promotion, local embedding/ranking, graph maintenance, and explicit retrieval probes. It supports the survey claim that trace learning needs a curation boundary; without the staging/promote/resolve layers, the regex extractor would be too noisy to carry authority.

## Read-back

**Read-back:** `both` - Retained memory can be pulled through explicit commands such as RAG query, SMS inspection, brain graph/index commands, and Obsidian notes; selected retained state is also pushed into Claude Code at session start through `systemMessage` assembly.

**Read-back signal:** `coarse` `identifier` - The push path fires on coarse session-start conditions and configured files, with identifier-scoped selection for current working directory, project slug, handoff hash, session id, focus file, and recent SMS episodes. It does not perform semantic relevance search over the live user prompt before injection.

**Faithfulness tested:** `no` - LACP tests retrieval quality and gates stop quality, but I found no WITH/WITHOUT ablation or perturbation test proving that pushed focus/handoff/SMS memory changes the agent's behavior as intended.

The main push injection point is pre-invocation at Claude Code session start. `session_start.py` loads and prioritizes identity, context mode, focus, handoff, git status, test command, SMS, health, memory-cap warning, and degradation messages, then emits a combined `systemMessage` within a rough token budget. From the receiving agent's perspective, focus/handoff/SMS/MEMORY-derived material arrives unsolicited.

Pull remains substantial. `query_memory_rag.py` is explicit query-time retrieval over `hybrid-index.json`; `lacp sms context|episodes|epochs|self-model` exposes SMS state on demand; `brain-ingest`, `brain-promote`, `brain-resolve`, `brain-expand`, and Obsidian commands are operator-driven access and maintenance surfaces. A host could choose to push their outputs, but the commands themselves are pull interfaces.

Authority at consumption is mixed. Session-start memory is advisory instruction/context unless the injected block comes from a baseline context mode or gate policy. Stop quality gates and pretool guards can block actions, but those are live configured enforcement mechanisms rather than memories being read back from learned use.

## Curiosity Pass

**The memory vocabulary is biologically ambitious, but much of the implementation is deterministic plumbing.** "Mycelium," "SMS," "FSRS," and "spreading activation" name useful design inspirations, but the implemented behavior is mostly local files, thresholds, regex extraction, cosine similarity, scoring, and scheduled maintenance.

**Trace extraction is intentionally shallow at capture time.** The Stop hook avoids LLM calls and only stages heuristic matches. That is a good latency choice, but it makes the later promotion/consolidation gates essential.

**The read-back push is broad rather than prompt-relevance targeted.** Session-start injection can include relevant retained state, but it is keyed by session/project/focus availability rather than by the actual next task prompt. This lowers selection cost and raises dilution risk.

**Governance and memory are tightly coupled.** LACP's gates can protect memory writes and execution, but the same coupling can blur whether a behavior was caused by retained memory, baseline policy, or the harness's live eval machinery.

## What to Watch

- Whether LACP adds prompt-time semantic selection before session-start or tool-use injection; that would change the read-back signal from mostly coarse/identifier to inferred.
- Whether active recall probes grow into behavioral ablations for injected memory; that would change the faithfulness verdict.
- Whether consolidation merge candidates are actually merged rather than previewed or synthesized around; that would sharpen the `dedup`/`consolidate` boundary.
- Whether trace-derived SMS self-model claims gain review metadata or expiry; without that, identity-shaped memory can silently overfit.
- Whether LACP separates baseline context-mode instructions from learned memory in emitted `systemMessage` blocks; that would make authority easier to audit.

## Bottom Line

LACP is a genuine trace-derived agent memory system embedded in a broader local control plane. Its most distinctive contribution is not one retrieval algorithm; it is the combination of hook-time memory push, staged trace capture, file-backed Obsidian/RAG memory, automatic graph maintenance, and live policy gates. For Commonplace, the borrowable parts are the session-start budget discipline, trace staging, and retrieval probes; the caution is to keep learned memory authority separate from configured enforcement.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: LACP stores many memory surfaces, but only session-start injection is retained-memory push.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: LACP separates file substrates, prose/symbolic/parametric forms, trace/import/authored lineage, and multiple behavioral authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: Obsidian notes, graph nodes, synthesis notes, and RAG results mostly act as knowledge artifacts.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: context modes, gates, routing policies, validation hooks, and ranking indexes can carry stronger authority.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: LACP's central memory problem is selecting, budgeting, and injecting local context for agent sessions.
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) - compares: LACP has strong discoverability and bounded-context mechanisms, with trust depending on staging, provenance, and gates.
