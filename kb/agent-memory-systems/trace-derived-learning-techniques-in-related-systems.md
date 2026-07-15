---
description: Trace-derived learning systems compared on ingestion pattern, representational form, behavioral authority, artifact structure, and evidence tier across repo reviews and lightweight coverage
type: kb/types/note.md
traits: [has-comparison, has-implementation]
tags: [learning-theory, observability]
---

# Trace-derived learning techniques in related systems

Trace-derived systems learn from CLI sessions, event streams, assistant turns, run trajectories, or next-state feedback. This note reviews what each system actually does, then draws out the axes that separate them: how they ingest traces (ingestion pattern), what representational form they promote into (distributed-parametric, prose, symbolic, or mixed), and what behavioral authority the result has (knowledge artifact consumed as evidence/advice vs system-definition artifact consumed with instruction, enforcement, routing, validation, evaluation, or learning force).

The review-backed code-inspected systems are Napkin, Pi Self-Learning, OpenViking, Operational Ontology Framework, Claude Workstream Kit, nao, MemoryOS, ClawVault, CrewAI Memory, cass-memory, deja-vu, Compound Engineering, WUPHF, REM, Autocontext, Meta-Harness, Agentic Harness Engineering, HALO, ARIS, Reflexion, Dynamic Cheatsheet, Agent Workflow Memory, ACE, ExpeL, ReasoningBank, G-Memory, AgentFly, Gnosis, Voyager, OS-Copilot, Tendril, SkillX, SkillRL, SkillWeaver, AriGraph, Amazon Science SAGE, Agent-R, Agent-S, and Self-Training-LLM (source paths noted in per-system reviews). OpenClaw-RL is a TODO for repo-backed review now that a repository exists; its current placement is based on source coverage. The lightweight systems — AgeMem and Trajectory-Informed Memory Generation — are included with lower confidence, based on local ingest notes rather than implementation inspection.

**What the survey finds.** Across readable artifacts, structure ranges from minimal verbal hints (Reflexion) through scored flat rules (ACE, ExpeL) to executable code (Voyager, OS-Copilot) — the prose-to-symbolic span. Candidate generation from traces is concrete enough to adapt; the open problem is evaluation — deciding what deserves trust, persistence, and retirement in open-ended domains. The per-system catalog below provides the evidence; the comparative analysis follows it.

## The recurring stages

We organize each system around five recurring stages:

1. **Trigger** — when mining runs
2. **Source format** — what raw session representation is consumed
3. **Extraction schema** — what target shape the model or code writes
4. **Promotion/storage** — how extracted items persist or get ranked
5. **Reinjection** — how mined artifacts affect future sessions

Some systems add a step between extraction and promotion — deduplication or conflict resolution against existing artifacts (cass-memory's Jaccard similarity, ExpeL's EDIT/REMOVE/MERGE, ClawVault's observation deduplication). This is common enough to note but varies too much in placement to warrant a sixth stage.

What varies is not whether the loop exists, but how structured the input is, whether the system assumes one active session or many repeated runs, and whether the promotion target is a readable artifact, service-managed memory, or model weights. [Axes of artifact analysis](../notes/axes-of-artifact-analysis.md) sharpens the distinction: "service memory" is usually a storage-substrate choice, not a representational form alongside readable artifacts and weights.

## Napkin

Napkin keeps mining outside the core CLI, in a `pi` extension rather than the `napkin` binary.

**Trigger.** Distillation starts on `session_start` via a timer. Every `intervalMinutes`, the extension checks whether the current session file grew. There is also a manual `/distill` command.

**Source format.** The extension does not parse messages. It gets the current session file via `ctx.sessionManager.getSessionFile()`, checks byte size, forks with `SessionManager.forkFrom(...)`, and passes the fork to a subprocess. The consumed format is whatever pi stores as a session file — Napkin treats it as opaque.

**Extraction.** The subprocess is another `pi` invocation with a fixed `DISTILL_PROMPT` that tells the model to inspect the vault (`napkin overview`, `napkin template list/read`), search before creating, and write notes using vault templates. Extraction is not "transcript → JSON" but "forked session → agent subprocess → tool-mediated note writes."

**Promotion.** Delegated to the vault. The extension writes directly into durable notes without maintaining a separate scored store.

**Scope.** Single-session, single-agent. One `activeProcess`, one `lastSessionSize`, one timer loop.

## Pi Self-Learning

The cleanest example of direct transcript mining into a narrow schema.

**Trigger.** Reflection runs on `agent_end`; reinjection runs on `before_agent_start`.

**Source format.** The extension reads the current branch via `ctx.sessionManager.getBranch()`, filters `type === "message"` entries, and serializes them through `convertToLlm(...)` and `serializeConversation(...)`. It also scans recent branch entries for interruption signals — `toolResult` errors, permission denials, blocked commands, aborted turns. The consumed format is pi's branch event structure, not a plain text transcript.

**Extraction.** The reflection prompt is deliberately narrow: focus only on what went wrong and how it was fixed, return strict JSON with schema `{"mistakes":["..."],"fixes":["..."]}`. Project mode keeps repo-specific detail; global mode rewrites toward cross-project rules.

**Promotion.** Raw reflections append to daily markdown. Durable promotion runs through a scored index with frequency bonus and recency decay, then renders into `CORE.md` and related memory files.

**Scope.** Single-session, single-agent. Supports project-vs-global memory scope but not shared multi-agent coordination.

## OpenViking

Structurally different from Napkin and Pi Self-Learning because it owns the session and message schema.

**Trigger.** Mining runs on `session.commit()` or `POST /api/v1/sessions/{session_id}/commit`. Background commit with task tracking is supported.

**Source format.** Messages are structured as `role + parts`, serialized to JSONL. Parts include `text`, `context`, and `tool`. The extractor formats archived messages as `[user]: ...` / `[assistant]: ...` lines and serializes tool calls as embedded JSON. Unlike the pi-based systems, OpenViking consumes a first-class typed session log it defines itself.

**Extraction.** `Session.commit()` archives messages, then calls `extract_long_term_memories(...)`. The extractor sends formatted messages to an LLM and expects parsed candidates in explicit categories: user memory (`profile`, `preferences`, `entities`, `events`), agent memory (`cases`, `patterns`), and tool/skill memory (`tools`, `skills`). Tool-call statistics and skill names are part of the mined trace, not just conversation text.

**Promotion.** Writes into typed memory directories with deduplication/merge logic. Mined items persist in a service-managed memory substrate, not human-authored notes.

**Scope.** Multi-session, multi-tenant. The server has tenant auth, session isolation, user/agent-space initialization, and background task tracking by `session_id`. The only inspected system here built as a shared service.

## Operational Ontology Framework

A local filesystem runner that learns from a deliberately thin task-result trace rather than from raw transcripts or tool logs.

**Trigger.** After each completed task in `run_cycle()`, the runner marks the task done, records a `Learned:` line in `_spec.md`, appends the learning to within-session context, and later consolidates non-trivial learnings into `_facts.md`. At run end, it writes a new handoff file.

**Source format.** The source trace is the model's task response parsed into `result`, `decision`, and `learned`, plus the task line. The raw model output is retained in memory for the run, but the durable artifacts use the structured fields. OOF does not parse a conversation transcript, tool log, or external session file.

**Extraction.** The task prompt itself asks the model to produce the three fields. Code validation caps lengths and supplies defaults, but there is no separate judge, recurrence check, or comparison against task outcome.

**Promotion.** Symbolic filesystem artifacts. `learned` strings become `_facts.md` bullets with source/date/confidence metadata, `_spec.md` gets task-local `Learned:` annotations, and handoff markdown records decisions and continuation state. No database, embeddings, or weight update.

**Scope.** Per-project, single-agent. It owns the project artifact schema but not a multi-agent trace bus or shared cross-project memory.

## Claude Workstream Kit

A repo-local active-work ledger for Claude Code, where trace-derived learning is operational state rather than reusable lesson memory.

**Trigger.** Workstream updates happen through explicit lifecycle skills: create, work, handoff, and close. Session-start read-back happens through a hook that prints `ACTIVE.md`, active-workstream status, staleness signals, and handoff inbox counts.

**Source format.** The kit does not parse raw chat transcripts. The source signal is the current work session's concrete outcomes: user gates, task checkboxes, command output, verifier findings, git commits/tags, handoff files, and closure evidence.

**Extraction.** The acting Claude Code agent writes the extraction under procedural skill rules. Completed work becomes evidence notes in `workstream.md`; current state becomes a compact `.state/ACTIVE.md` pointer; closure dispositions route learnings to durable files, handoffs, or explicit drops before the active workstream directory is removed.

**Promotion.** The promoted artifact is not a general memory database. Session activity becomes project-local active work state, then closure extracts anything that should survive outside `.state/`, appends an archive line, creates a `ws/<name>` tag, and resets `ACTIVE.md`.

**Scope.** Per-project and per-workstream. This strengthens the survey by adding an active-work-ledger subtype: the learned artifact is the lifecycle-governed state of unfinished work, with closure as the mechanism that prevents active memory from becoming stale ambient context.

## nao

A product analytics assistant that separates file-shaped project context from database-backed user-personalization memory.

**Trigger.** Memory extraction is scheduled during the live chat stream immediately after the request is sent to the agent. It is asynchronous and failure-tolerant rather than a blocking write path.

**Source format.** Recent user/assistant UI messages from the current chat, limited to the last 17 messages and truncated per message. The application stores richer typed message parts, including tool input/output and feedback elsewhere, but the extractor consumes joined text parts rather than the full tool trace.

**Extraction.** An LLM receives existing memories plus recent conversation text and returns structured `user_instructions` and `user_profile` arrays. The prompt defaults to no extraction, requires strong permanence signals for instructions, permits profile facts for identity/background information, and supports `supersedes_id` for replacements.

**Promotion.** Database rows in `memories`, categorized as `global_rule` or `personal_fact`, with optional chat provenance and supersession. Active memories are reinjected into future system prompts under a 1000-token cap.

**Scope.** Per-user and project-gated. This is personalization memory, not shared project knowledge, cross-agent playbooks, or analytics-doc synthesis.

## MemoryOS

A conversational memory library and MCP server that turns live user/assistant dialogue into hierarchical profile state and retrievable knowledge artifacts.

**Trigger.** `add_memory(...)` writes each user input / agent response pair into short-term memory. Short-term overflow triggers mid-term analysis; hot mid-term sessions trigger long-term extraction. `get_response(...)` also writes the generated answer back into memory, so normal deployment conversations feed the loop.

**Source format.** Timestamped user/assistant dialogue pairs plus optional current-turn metadata. The PyPI path stores JSON files with short-term turns, mid-term sessions, long-term user memory, and assistant memory; the ChromaDB variant stores retrieval surfaces in persistent collections with sidecar metadata.

**Extraction.** LLM prompts detect continuity, write page meta-info, summarize topics, extract keywords, rewrite the user profile, and extract user-private and assistant-knowledge facts. Threshold logic around short-term capacity and mid-term heat decides when each extraction stage runs.

**Promotion.** Prose plus vectors: session summaries, page summaries, profile text or profile JSON, user knowledge entries, assistant knowledge entries, timestamps, and embeddings. The system has capacity and heat mechanics, but no source-linked review state or curation workflow.

**Scope.** Per configured user and assistant. This is single-assistant personalization memory rather than shared project knowledge or cross-agent skill learning.

## ClawVault

Two mining paths: direct assistant-turn capture into typed markdown memories, and incremental session observation over OpenClaw session files with weekly reflection.

**Trigger.** `captureTurn(...)` stores memories from assistant responses immediately. The OpenClaw plugin also triggers on `agent_end` heartbeats, `before_compaction`, and `before_reset`, with optional auto-checkpointing and weekly reflection on session start. A standalone `observe` command supports one-shot compression, cron runs, or file watching.

**Source format.** Consumes both assistant turns and session logs. The active observer reads `sessions/*.jsonl`, tracks per-session byte offsets in `.clawvault/observe-cursors.json`, and processes new content past a size threshold. The parser strips tool/system/developer noise, structured metadata, and base64 payloads, keeping user/assistant conversational content.

**Extraction.** Two layers. `src/capture/extractor.ts` extracts typed memories from assistant responses via `<memory_note>` tags plus heuristic sentence classification (`decision`, `preference`, `lesson`, `relationship`, `episode`, etc.). `src/observer/compressor.ts` turns session updates into scored observation lines `[type|c=...|i=...] content`. The observation type system: `decision`, `preference`, `fact`, `commitment`, `task`, `todo`, `commitment-unresolved`, `milestone`, `lesson`, `relationship`, `project`.

**Promotion.** Capture writes into category folders (`facts`, `preferences`, `decisions`, `lessons`, `people`). The observer writes dated observation ledgers. `runReflection(...)` promotes recurring observations into weekly reflections: importance ≥ 0.8 promotes immediately; importance ≥ 0.4 promotes when seen on at least two dates — implemented in `promoteWeekRecords(...)`.

**Scope.** Single-agent vault with session lifecycle support. Owns its vault substrate and watches session files, but does not present as a multi-tenant backend. Best understood as a workshop-memory system around one workspace.

## CrewAI Memory

Framework-integrated runtime memory: it lives inside CrewAI's agent, crew, and flow execution paths rather than as an external service or offline reflector.

**Trigger.** Task-result mining runs after agent execution; standalone agent and LiteAgent runs save input/result pairs after execution; `@human_feedback(..., learn=True)` distills lessons after non-empty human feedback. Recall runs before task execution, standalone kickoff, LiteAgent execution, and HITL pre-review.

**Source format.** Thin runtime traces assembled by code: task description, agent role, expected output, and result; standalone input plus output; or method output plus raw human feedback. It does not mine full tool logs or long session transcripts in the inspected path.

**Extraction.** `extract_memories_from_content(...)` asks an LLM for discrete reusable memory statements and falls back to storing the whole content if extraction fails. Save-time analysis infers scope, categories, importance, and metadata, then consolidation compares against similar records and can keep, update, delete, or insert. HITL learning uses a separate lesson-distillation prompt for reusable rules or preferences.

**Promotion.** Symbolic service memory: `MemoryRecord` rows in LanceDB by default, optional Qdrant Edge, with content, scope, categories, metadata, importance, source, private flag, and vector embedding. The artifact is inspectable through APIs/TUI/events but not a human-authored note.

**Reinjection.** Recalled records are injected into task prompts and standalone agent inputs; memory tools also let the agent explicitly search or save. HITL lessons are recalled before human review and used by an LLM to pre-review the method output.

**Scope.** Per-crew, per-flow, per-agent, or caller-provided scope. Crew memory roots under `/crew/{name}`; flows under `/flow/{name}`; agent-scoped views and multi-scope slices are available.

## cass-memory

The only inspected system that makes cross-agent session mining a first-class feature. Structurally a two-phase extraction pipeline (diary then reflection) feeding a scored playbook.

**Trigger.** Explicit CLI commands: `cm reflect` orchestrates the full pipeline (discover → diary → reflect → curate); `cm diary <session>` extracts a single session. No event-driven hooks — triggers are manual or agent-initiated. `orchestrateReflection()` in `orchestrator.ts` coordinates the multi-session flow.

**Source format.** `findUnprocessedSessions()` in `cass.ts` discovers sessions via the external `cass` search engine, using `cassTimeline()` (primary) or broad keyword searches (fallback). `cassExport()` exports sessions as markdown via `cass export --format markdown`, with fallback to direct file parsing of `.jsonl`, `.json`, or `.md` files. `formatRawSession()` in `diary.ts` normalizes multiple agent formats — Claude Code JSON, Cursor, Codex CLI, Aider, Pi — into markdown. Agent identity is pattern-matched from file paths (`.claude`, `.cursor`, `.codex`, `.aider`, `.pi/agent/sessions`). Session content is truncated to 50k chars and secrets are stripped before LLM processing.

**Extraction.** Two phases. Phase 1: `extractDiary()` in `llm.ts` produces a Zod-validated `DiaryEntry` with accomplishments, decisions, challenges, preferences, key learnings, tags, and search anchors — each field asks for specific file names, function names, and error messages rather than vague summaries. Diary IDs are deterministic content hashes for idempotency. Phase 2: `runReflector()` in `llm.ts` takes the diary plus existing playbook bullets plus cross-agent history and proposes `PlaybookDelta` operations: `add`, `helpful`, `harmful`, `replace`, `deprecate`, `merge`. Runs up to 3 iterations with early exit on diminishing returns; `deduplicateDeltas()` prevents duplicates within and across iterations.

**Promotion.** `curatePlaybook()` in `curate.ts` applies deltas to YAML playbook files (global at `~/.cass-memory/playbook.yaml`, optional per-repo overlays). New bullets enter as `candidate` maturity. Curation checks Jaccard similarity for duplicates, detects conflicts via negation/directive markers, and reinforces existing bullets on near-matches. `getEffectiveScore()` in `scoring.ts` computes `decayedHelpful - (4 × decayedHarmful)` with exponential decay (90-day half-life). When harmful feedback exceeds a threshold, `invertToAntiPattern()` creates a new bullet prefixed "AVOID:" with `kind: "anti_pattern"`. Maturity progresses `candidate → established → proven → deprecated` based on effective score.

**Reinjection.** `cm context "<task>"` retrieves relevant bullets by keyword matching, effective score, and optional embedding similarity, returning ranked rules, anti-patterns, related session history, and warnings about deprecated patterns. Cross-agent enrichment happens during diary generation: `enrichWithRelatedSessions()` queries the `cass` search engine for sessions from *other* agents that match the current diary's challenges and learnings, with access logged to `privacy-audit.jsonl`.

**Scope.** Cross-agent, multi-session. Reflects over sessions from Claude Code, Cursor, Codex, Aider, and Pi within a configurable lookback window (default 7 days, up to N sessions). A single shared playbook accumulates rules from all agents, with optional per-repo overlays. `ProcessedLog` in `tracking.ts` tracks which sessions have been reflected on to enable incremental processing.

## deja-vu

The pure trace-to-recall case: existing agent session histories become a redacted lexical index and optional startup context, without promotion into rules, summaries, or policies.

**Trigger.** Indexing is staged behind user or agent commands such as search, warmup, stats, sync export, MCP recall, and context lookup. The Claude `SessionStart` hook reads only an already-warm index; it does not cold-build the index during startup.

**Source format.** Existing Claude Code and Codex JSONL histories plus opencode's local SQLite database. The parsers extract user/assistant text, roles, session ids, project/path metadata, and timestamps; they do not own the upstream session schema or mine rich tool traces.

**Extraction.** Mechanical, not model-judged: parse trace text, redact secrets, write records, tokenize into bucket postings, maintain manifest/session metadata, and rank search results by match count and recency. There is no diary, reflection, summarization, or lesson oracle.

**Promotion.** Redacted records, token buckets, GOB manifests/session metadata, sync JSONL batches, MCP recall results, `ctx` digests, and optional Claude startup context. These are knowledge/routing/ranking artifacts, not curated system-definition rules.

**Scope.** Cross-harness and cross-task local recall with project-scoped push for Claude. It strengthens the weak-promotion branch of the survey: trace-derived memory can remain an access structure over prior sessions and still change later work through pull recall or coarse project startup context.

## Compound Engineering

A multi-host engineering workflow plugin where trace-derived learning is optional and project-local rather than a daemonized memory service.

**Trigger.** `ce-sessions` is invoked directly by the user or synchronously from `ce-compound` when an interactive Full run opts into session history. Lightweight and headless `ce-compound` runs skip session history.

**Source format.** Host-managed Claude Code, Codex, and Cursor session files. Discovery and metadata extraction filter by repo, branch/cwd, timestamps, and keywords; skeleton extraction avoids whole-transcript loading by writing filtered user/assistant text and collapsed tool summaries to scratch files.

**Extraction.** A synthesis-only historian agent reads the scratch skeletons and returns sections such as prior attempts, failed approaches, decisions, and related context. `ce-compound` can then label session-sourced content and fold it into a structured `docs/solutions/` learning.

**Promotion.** Two-stage prose promotion. Raw session JSONL and scratch skeletons remain knowledge artifacts; durable behavior-shaping material appears only when a workflow distills findings into project-local Markdown such as `docs/solutions/`. There is no scored playbook, embedding store, or automatic promotion loop.

**Scope.** Per-repo and time-windowed. The design is closest to cass-memory on cross-harness session recall, but weaker as autonomous learning and stronger as explicit workflow curation: session traces become maintainable only when a human-invoked skill promotes them into the repository's learning docs.

## WUPHF

A local multi-agent office where trace-derived learning sits inside the broker/wiki runtime rather than a standalone memory daemon.

**Trigger.** Raw artifacts commit through the wiki artifact path, then extraction runs asynchronously through the wiki worker hook. Entity brief synthesis and playbook synthesis run at thresholds or on demand; playbook learning is triggered after enough recorded executions.

**Source format.** Immutable markdown artifacts under `wiki/artifacts/{source}/{sha}.md`, append-only fact logs, channel and broker state, notebook drafts, and `team/playbooks/{slug}.executions.jsonl`.

**Extraction.** Artifact extraction prompts for entities and facts, resolves entities, computes deterministic fact IDs, and persists facts to both index state and JSONL logs. Playbook synthesis reads recent execution entries and updates only `## What we've learned`, preserving the authored procedure body.

**Promotion.** Facts, entity briefs, wiki articles, playbooks, and compiled `SKILL.md` files in the git wiki, plus team skills in broker state. The learned forms are readable prose and symbolic artifact state, not model weights.

**Scope.** Workspace/team-scoped multi-agent office. The strongest new subtype is the execution-log-to-playbook-skill loop: repeated procedure runs revise a bounded learned section, which then recompiles into the next invokable skill wrapper.

## REM

A service-owned episodic memory backend with the simplest consolidation pipeline in the survey and the widest gap between aspirational lifecycle management and actual implementation.

**Trigger.** Consolidation queued on every episode write via Redis (fire-and-forget), plus a periodic Celery task. Requires 3+ unconsolidated episodes to proceed.

**Source format.** Agent-submitted content strings via HTTP API (`POST /api/v1/episodes`), enriched at write time by GPT-4o-mini into intent, entities, domain (7 fixed categories), emotion signal, and importance score. Not a session log or conversation transcript — an opaque content field that the service parses. The Go API stores the episode in PostgreSQL, upserts the embedding in Qdrant, and creates a temporal node in Neo4j.

**Extraction.** Two-step: keyword clustering (group by domain, then greedy intent-token overlap requiring 2+ shared tokens), then GPT-4o compression asking for 1-5 "durable, reusable facts" per cluster as JSON with confidence, fact_type, and domain. Episode content is truncated to 500 chars per episode in the prompt. The clustering is the coarsest in the survey — well below the semantic similarity the system's own embeddings could support.

**Promotion.** Append-only semantic memories in PostgreSQL and Qdrant. Each fact is a short string (max 200-300 chars) with confidence score, fact type (preference/rule/pattern/skill/fact), domain, and source episode IDs. No deduplication, no revision, no lifecycle management. The `SemanticMemory` domain struct has `Active`, `ContradictedBy`, and `Superseded` fields, but no code populates them.

**Scope.** Per-agent, multi-session. Each agent's episodes consolidate independently. No cross-agent mining, no shared knowledge store across agents.

## Autocontext

The clearest inspected system spanning both artifact learning and weight promotion. Mines repeated run trajectories rather than one interactive transcript.

**Trigger.** Two clocks. During multi-generation runs, `accumulate_lessons(...)` turns judge feedback into generation-level lessons carried forward in the playbook. At run end, `generate_session_report(...)` summarizes the trajectory and `ArtifactStore.write_session_report(...)` persists it. Weight distillation is a separate offline step: export JSONL from prior runs, train, publish.

**Source format.** Not a transcript or message bus. The source trace splits across SQLite generation rows (`best_score`, `gate_decision`, Elo), stored competitor outputs, per-scenario artifact files (`playbook.md`, `hints.md`), and generated markdown session reports. The export path packages per-generation records with `strategy`, `score`, `gate_decision`, and a `context` object containing `playbook`, `hints`, and `trajectory`.

**Extraction.** Intentionally simple. `accumulate_lessons(...)` turns judge reasoning and dimension scores into structured lesson text. `generate_session_report(...)` produces markdown with gate counts, top improvements, and dead ends. `export_training_data(...)` re-expresses kept generations as JSONL training records.

**Promotion.** Two-step. First into files: versioned playbooks, hints, lesson history, session reports. Then optionally into weights: `TrainingRunner` uses exported JSONL, `publish_training_output(...)` registers a distilled model by scenario/backend/runtime. Autocontext is the only inspected system that bridges both promotion targets.

**Scope.** A trajectory-learning control plane over many runs and generations. Knowledge is scenario-scoped, accumulated across runs, and optionally compiled into a model that no longer needs the full playbook at inference.

## Meta-Harness

A code-inspected outer loop for optimizing the harness around a fixed base model: memory-system classes for text classification and agent-scaffold subclasses for Terminal-Bench 2.

**Trigger.** Iteration cycle: run baselines or current candidates, collect logs/results/frontiers, invoke a Claude proposer with a local skill, validate generated candidates, benchmark, update the frontier, repeat. Smoke tests gate the expensive Terminal-Bench run.

**Source format.** Repeated run trajectories: prediction JSONL, saved memory state, prompt hashes, validation/test result JSON, frontier summaries, evolution summaries, Claude proposer sessions, Harbor job directories, verifier rewards, cost/token/turn metrics, and failed/successful task trajectories. It is not a conversation-memory system; it is a benchmark-trace consumer.

**Extraction.** Claude Code reads those traces under task-specific skills and writes executable candidates plus `pending_eval.json` metadata. The text-classification path writes `MemorySystem` subclasses; the Terminal-Bench path writes Harbor-compatible `AgentHarness` subclasses.

**Promotion.** Executable Python harness artifacts and run metadata. The frontier records winners, but the learned form is code. No weight promotion in the inspected repo; no durable prose playbook beyond run-local reports and summaries.

**Scope.** Per-domain, per-benchmark optimization. The onboarding prompt generalizes the setup, but transfer between domains is manual through a new domain spec and new harness interface.

## Agentic Harness Engineering

Code-inspected outer loop for evolving a NexAU coding-agent harness against Harbor benchmarks, with Agent Debugger as an intermediate trace-distillation layer.

**Trigger.** Iteration cycle: copy the baseline code-agent workspace, evaluate with Harbor, compute pass@k and task flips/regressions, run Agent Debugger analyses, invoke an evolve agent, commit workspace changes, and repeat until target pass rate or iteration cap.

**Source format.** Harbor job directories, NexAU in-memory traces, verifier rewards, exception files, timeout labels, task-history diffs, variant results, debugger reports, and prior change manifests. Unlike Meta-Harness, AHE puts a dedicated debugger-analysis layer between raw traces and the proposer by default.

**Extraction.** Deterministic code computes statistics and change attribution; Agent Debugger turns cleaned traces into per-task root-cause reports; the evolve agent reads those reports plus raw-trace pointers and writes prompt, tool, middleware, skill, sub-agent, or memory changes with prediction-bearing manifests.

**Promotion.** Mixed system-definition artifacts in the experiment workspace: markdown prompts and memories, YAML tool and agent config, Python tool/middleware code, skill packages, and sub-agent definitions. Git commits and `change_manifest.json` make the promotion auditable, but there is no separate curated prose library.

**Scope.** Per-experiment benchmark optimization, with Terminal-Bench defaults in the public config. It is closest to Meta-Harness on "harness as learning target," but its distinctive contribution is the component-level mutation menu plus debugger-mediated trace compression before the evolve step.

## HALO

Code-inspected trace-analysis runtime for optimizing an agent harness from OpenTelemetry-shaped execution traces. HALO is closest to Agentic Harness Engineering on debugger-mediated trace compression, but narrower: the inspected package owns trace indexing, bounded trace inspection, subagent-assisted diagnosis, and sandboxed aggregate analysis, while durable harness edits remain outside the engine.

**Trigger.** Staged loop: instrument an agent harness, run it to collect JSONL spans, invoke `halo TRACE_PATH --prompt ...`, inspect the diagnostic report, patch the harness through a coding agent or maintainer, then redeploy and collect another trace batch.

**Source format.** OTel-shaped JSONL spans with `trace_id`, `span_id`, parent links, timing, status, resource attributes, and normalized `inference.*` keys for project, model, agent, token, and observation metadata. The sidecar index records byte offsets, span counts, error flags, service/model/agent names, token totals, and project id, but the trace file remains authoritative.

**Extraction.** A trace-analysis agent uses `get_dataset_overview`, filtered trace summaries, literal `search_trace`, surgical `view_spans`, LLM synthesis, optional subagents, and optional sandboxed Python over the trace store. Tool descriptions and prompts enforce progressive disclosure over long traces.

**Promotion.** First into prose diagnostic reports; then, if a downstream actor accepts the diagnosis, into symbolic harness artifacts such as prompts, tool descriptions, retry logic, configuration, or code. The repository does not implement automatic patch generation, patch validation, or redeployment.

**Scope.** Per-harness and per-benchmark/deployment. It strengthens the survey's trace-richness claim by making bounded drill-down paths part of the diagnostic runtime, but it also reinforces that reports are only knowledge until an external promotion step changes the harness.

## ARIS

Markdown workflow harness whose trace-derived loop targets the skill system itself rather than task-domain memory.

**Trigger.** Claude Code hooks call `tools/meta_opt/log_event.sh` on tool use, tool failure, user prompt submit, session start, and session end. `tools/meta_opt/check_ready.sh` prints a reminder after five skill invocations since the last optimization. `/meta-optimize` is still manually invoked; patch application is user-approved.

**Source format.** Structured JSONL under `.aris/meta/events.jsonl`, written both project-locally and globally. Records include `skill_invoke`, `tool_failure`, Bash/Edit/Read summaries, Codex calls, slash commands, user prompts, and session start/end metadata. It is lighter than raw transcripts but richer than success/failure counters.

**Extraction.** The `meta-optimize` skill asks the agent to compute frequency, failure, convergence, and human-intervention patterns, rank optimization opportunities, and generate concrete diffs against `SKILL.md` prompts, defaults, convergence rules, workflow ordering, or cautious artifact schemas. Proposed patches then go through cross-model review before recommendation.

**Promotion.** Proposed markdown skill diffs plus a meta-optimization report. Application backs up the original skill and logs the optimization, but the inspected contract explicitly forbids auto-apply without user approval. The learned artifact is prose-form system-definition text, not a separate memory store.

**Scope.** Per-project harness optimization with optional global trend accumulation. It is closest to Meta-Harness on "harness as learning target," but its promotion target is promptware/skillware rather than executable Python harness classes, and its oracle is weaker: log-derived evidence plus reviewer judgment rather than benchmark score frontiers.

## OpenClaw-RL

TODO: write a repo-backed review now that a reachable repository exists. The current placement is retained from source coverage rather than a current `agent-memory-system-review` note.

**Trigger.** Live API traffic. `OpenClawAPIServer` proxies `POST /v1/chat/completions` with `X-Session-Id`, `X-Turn-Type`, and `X-Session-Done` headers. PRM judging runs asynchronously once next-state evidence arrives; rollout workers drain scored samples into training queues.

**Source format.** A session-aware chat-completion stream. The proxy normalizes message arrays, separates `main` turns from side turns, and pairs assistant outputs with later next-state feedback. `TrainingSample` carries `session_id`, `turn_num`, prompt/response tokens, sampled log-probs, `loss_mask`, scalar `reward`, optional `teacher_logprobs`, and `sample_type`.

**Extraction.** Two signal families from the same trace: evaluative signal via PRM scoring over assistant output plus next-state evidence, and directive signal via teacher log-probs and OPD-style token-level supervision. `combine_loss.py` mixes PPO-style reward advantages with teacher-minus-student token-level advantages; `data_formatter.py` converts samples into Tinker datums.

**Promotion.** Directly into model weights during deployment. Separate rollout and training paths for binary RL, OPD, and combined training, all feeding background optimization rather than text artifacts.

**Scope.** Session-aware policy-learning backend. Many live sessions feed one continuously trained policy; the result is opaque weights, not inspectable memory.

## Reflexion

The earliest trajectory-to-artifact system in this survey and the simplest.

**Trigger.** After each failed task attempt, via explicit failure feedback (test results, reward signals, environment observations).

**Source format.** Failed trial histories from benchmark tasks (ALFWorld, HumanEval). The source is a bounded attempt log, not a long-lived session.

**Extraction.** A short natural-language self-reflection or plan. The schema is deliberately minimal — one or a few sentences of self-critique.

**Promotion.** Reflections append to a rolling buffer and inject into the next attempt's prompt. Only the most recent reflections carry forward. No durable store, scoring, or lifecycle management.

**Scope.** Single-task, bounded retries. Reflections are local to one task family and do not accumulate across domains.

## Dynamic Cheatsheet

Artifact learning through prompt-mediated state carryover rather than structured memory operations.

**Trigger.** After each benchmark query, the model rewrites the cheatsheet for the next query.

**Source format.** Ordered benchmark queries, model answers, and optionally retrieved prior input-output pairs. Not session logs or trajectory files.

**Extraction.** A second LLM call receives the current cheatsheet and the latest query-answer pair, then rewrites the cheatsheet wholesale. Prompts ask the model to preserve, compress, and refine, but the code extracts a `<cheatsheet>` block and replaces the old one entirely — full-document rewrite, not operation-based editing.

**Promotion.** One carried-forward cheatsheet string. Optional retrieval variants use embeddings over prior examples. No separate scored store or lifecycle management.

**Scope.** Single benchmark run. The cheatsheet is not transferable across domains.

## Agent Workflow Memory

Web-agent trajectory distillation into website-scoped workflow prompt files.

**Trigger.** Offline induction runs over annotated Mind2Web training examples. Online Mind2Web induction runs between batches of test examples. WebArena's pipeline runs inference, evaluates the trajectory, then updates a workflow file after each task.

**Source format.** Annotated web-task examples, Mind2Web result JSON with environment/action steps, and WebArena experiment logs plus ground-truth or auto-eval success signals.

**Extraction.** LLM-mediated workflow induction after script-level filtering and deduplication. Mind2Web formats examples into prompts and filters the generated workflow text. WebArena parses thought/action blocks, removes invalid actions, deduplicates by task template and abstract action sequence, and can ask an LLM to summarize selected successful examples.

**Promotion.** Plain text workflow files such as `workflow/{website}.txt`, optionally assisted by a FAISS workflow retriever over names and docstrings. The behavior-changing artifact is prompt text injected into later acting contexts, while evidence stays in result directories and logs.

**Scope.** Website- and benchmark-scoped. AWM is stronger than Dynamic Cheatsheet on task-boundary and oracle discipline, but weaker than ExpeL or ACE on artifact lifecycle because workflows are overwritten rather than maintained as addressable units.

## ACE

Three-role playbook-learning loop with counter-based maintenance.

**Trigger.** After each question attempt. Offline mode trains on labeled samples with validation; online mode updates during evaluation. Both use the same reflector-curator pipeline.

**Source format.** Question attempts, reasoning traces, feedback signals (ground truth or environment), and bullet IDs from the current playbook. The generator answers with the playbook in context; the reflector receives the full attempt plus feedback.

**Extraction.** Two-phase. The reflector tags used bullets as `helpful`, `harmful`, or `neutral` and writes freeform reflection text. The curator reads the reflection plus playbook stats and proposes operations (`ADD`, `UPDATE`, `MERGE`, `DELETE`), though in practice only `ADD` is fully implemented; counters are updated separately.

**Promotion.** Sectioned playbook text with stable bullet IDs and helpful/harmful counters. Deduplication handled by an optional bulletpoint analyzer. Structurally richer than Dynamic Cheatsheet's rewrite, but still append-heavy.

**Scope.** Per-benchmark task family. Supports offline training and online evaluation modes.

## ExpeL

The clearest trajectory-to-rule consolidation system in this survey.

**Trigger.** Explicitly staged: first `train.py` gathers trajectories over training tasks, then `insight_extraction.py` runs a separate consolidation pass. Short reflections also run inline between failed attempts.

**Source format.** Succeeded and failed task trajectories gathered across benchmark tasks and folds. Not session logs or live event streams.

**Extraction.** `create_rules(...)` compares successful and failed trajectories, prompts for critique operations, and parses explicit `ADD`, `EDIT`, `REMOVE`, and `AGREE` verbs. Rules carry strength counters updated through `update_rules(...)` — rules can be edited in place and decay to removal when strength reaches zero.

**Promotion.** Numbered natural-language rule list plus a vectorstore of prior successful trajectories for fewshot retrieval. At evaluation, `insert_before_task_prompt()` injects rules; `update_dynamic_prompt_components()` retrieves similar past traces by task, thought, step, or action.

**Scope.** Cross-task within one benchmark family. Consolidation runs over training folds, not live sessions.

## ReasoningBank

Three-step pipeline with bidirectional extraction and optional test-time parallel comparison.

**Trigger.** Sequential: run inference with memory retrieval, auto-evaluate correctness, extract memory items. Also supports a parallel-trajectory scaling mode that runs multiple attempts and compares them.

**Source format.** Benchmark task trajectories (WebArena, SWE-Bench). Both successful and failed runs feed extraction through separate prompts.

**Extraction.** Separate prompts for successes and failures. Each produces up to 3 structured memory items with `Title`, `Description`, and `Content` fields. The parallel-scaling variant uses cross-trajectory "self-contrast reasoning" for richer extraction.

**Promotion.** Append-only JSONL with embeddings. Retrieval is query-to-query cosine similarity (matching current task query against prior task queries, not memory content). No editing, merging, or removal of existing items.

**Scope.** Benchmark-scoped. Memory accumulates across tasks within a benchmark but has no cross-domain transfer mechanism.

## G-Memory

Multi-agent memory harness with three distinct reuse substrates.

**Trigger.** After each multi-agent task run. Key-step extraction runs on every completed task; full insight maintenance starts after configured thresholds.

**Source format.** Multi-agent benchmark trajectories (ALFWorld, FEVER, PDDL). Within-task coordination captured as `StateChain` — a networkx `DiGraph` of agent messages with upstream edges recording dependency structure.

**Extraction.** Two layers. Completed tasks are stored in Chroma with success/failure labels. Separately, `InsightsManager` compares successful and failed trajectories and proposes `ADD`/`EDIT`/`REMOVE`/`AGREE` operations over a scored rule list. Periodic FINCH clustering merges related rules.

**Promotion.** Three substrates: (1) Chroma-backed episode store for trajectory retrieval, (2) task-similarity graph for neighborhood-expanded search, (3) scored JSON rule list for durable text guidance. Prompt-time injection formats all three into per-role agent context.

**Scope.** Multi-agent benchmark runs across three MAS orchestration styles. The only multi-agent trace-mining system in this survey.

## AgentFly

Planner-case memory with optional learned case selection.

**Trigger.** After each benchmark question in the CBR clients. The scripts run a planner-executor agent, judge the final answer against ground truth, append result records, and update memory before continuing.

**Source format.** DeepResearcher-style benchmark questions, planner JSON, executor task outputs, tool-call records, final answers, judge rationales, and retrieved case lists. The source trace is a repeated task run rather than an open-ended session transcript.

**Extraction.** Non-parametric mode compresses each completed run to `{question, plan, reward}`. Parametric mode writes `{case, plan, case_label}` and, when cases were retrieved, query-case training pairs whose `truth_label` is the current run's correctness. The oracle is an LLM answer judge over benchmark ground truth.

**Promotion.** Two substrates: append-only JSONL case memory consumed as positive/negative planner demonstrations, and optional binary selector weights trained to score query-case pairs. The learned weights choose cases; they do not replace the external case bank.

**Scope.** Benchmark-scoped planner improvement. Strong evidence for the "artifact first, selector weights second" pattern, but no lifecycle beyond append, reload, and manual retraining.

## Gnosis

Doctrine-mediated live capture into repo-local prose memory.

**Trigger.** Agent workflow instructions: read `gn help plan` before implementation, write entries during work when a decision or external constraint appears, and read `gn help review` after finishing.

**Source format.** Live coding-session context as interpreted by the agent — human statements, rejected alternatives, empirical observations, and work decisions. Gnosis does not preserve or parse raw transcripts.

**Extraction.** Agent judgment under a fixed doctrine: prefer perishable human or empirical knowledge, avoid analysis another agent could rederive from code, and prefer a code comment when the knowledge has a precise code anchor.

**Promotion.** Repo-local `.gnosis/entries.jsonl` records with ID, topics, text, related IDs, and timestamps. SQLite FTS5 is a disposable search projection in a per-repo cache.

**Scope.** Per-repository, online during normal work. It is the lightest inspected trace-derived system: no hook, observer, transcript miner, or judge, but a real recurring capture loop through AGENTS instructions plus a CLI.

## Voyager

Trajectory-to-executable-code promotion gated by a critic.

**Trigger.** After each task attempt. A `CurriculumAgent` proposes tasks; an `ActionAgent` generates and iterates code; a `CriticAgent` checks environment state for success. Only success triggers skill promotion.

**Source format.** Embodied task trajectories in Minecraft: execution errors, chat logs, inventory state, nearby entities, chest memory, and critic feedback. The curriculum also maintains a QA cache of world-knowledge questions in a separate Chroma store.

**Extraction.** `ActionAgent` generates JavaScript code from environment context and retrieved prior skills, iteratively repaired through execution feedback. Once the critic confirms success, the final `program_code` and `program_name` are the extracted artifact.

**Promotion.** `SkillManager` stores code under `skill/code/`, auto-generated descriptions under `skill/description/`, a manifest in `skills.json`, and a Chroma vector store over descriptions. Retrieval is semantic over descriptions; reinjection is actual code into the action-agent system prompt. The only system in this survey that promotes into executable artifacts.

**Scope.** Single embodied domain with compositional skill accumulation. No cross-domain transfer.

## OS-Copilot

OS-task trajectory promotion into reusable Python tools.

**Trigger.** During FRIDAY task execution, after a Python subtask completes and the judge assigns a sufficiently high generality score; in self-learning mode, a generated curriculum repeatedly creates lessons that drive more task attempts.

**Source format.** Generated Python code, invocation logic, environment output, error text, working directory state, directory listing, downstream task requirements, LLM critique, repair attempts, and final judge score. The trace is task-local execution state rather than a full transcript.

**Extraction.** The LLM judge classifies each attempt as `Complete`, `Amend`, or `Replan` and scores generality. Completed high-scoring Python subtasks are distilled into a tool name, code, and description; failed or insufficiently general attempts are repaired or replanned rather than promoted. The review notes a repair-path caveat: after a repaired attempt succeeds, the storage call still appears to receive the original code variable.

**Promotion.** Symbolic executable artifacts: Python files, description text files, a JSON registry, and a Chroma vector index over descriptions. Retrieval later changes action capacity because FRIDAY can call the stored code rather than merely read advice.

**Scope.** Local generated-tool repository for OS/software automation. It is the closest non-game analogue to Voyager's executable skill library, but without Voyager's explicit embodied curriculum state, skill composition discipline, or clean repair-to-promotion handoff.

## Tendril

Online capability creation from live requests into a workspace-local executable registry.

**Trigger.** Every action is prompt-directed to start with `listCapabilities()`. If no matching capability exists, the model registers a new capability before executing it. Failed executions can lead the model to fix and retry the registered code during the same deployment interaction.

**Source format.** Live user request, compact capability summaries from `tools/index.json`, model judgment about trigger/suppression fit, generated TypeScript code, JSON arguments, Deno execution output or errors, and workspace file state. Tendril does not mine stored transcripts or benchmark trajectories.

**Extraction.** Model-mediated direct codification. The model writes a capability definition with name, description, triggers, and suppression rules, plus Deno TypeScript source. The runtime validates names and stores files, but there is no separate judge, approval gate, or recurrence test before promotion.

**Promotion.** Symbolic executable artifact: `tools/index.json` plus `tools/{name}.ts` in the selected workspace. Later sessions activate the artifact by listing the registry and executing by name; execution is name-gated and workspace-scoped through Deno.

**Scope.** Per workspace and online during normal deployment. Tendril is not a trajectory-run learner; it is trace-to-tool learning where the promoted artifact changes future action capacity immediately.

## SkillX

A staged construction pipeline for building hierarchical skill libraries from successful benchmark trajectories.

**Trigger.** Offline or staged extraction over loaded trajectory files. Loaders filter successful runs by reward threshold; expansion can synthesize additional tasks from failed-only or missing API coverage.

**Source format.** Benchmark task trajectories with user task, interaction steps, reward, assistant tool calls, tool responses, metadata, and optional failed trajectories for contrast.

**Extraction.** LLM plan extraction turns successful histories into reusable plans; functional-skill extraction processes plan steps against current skills; atomic-skill extraction focuses on tool-centered guidance. Extractors use `add`, `modify`, and `keep`, so the library can be revised rather than only appended. DBSCAN clustering, LLM merging, and LLM/tool-schema filtering refine the library.

**Promotion.** JSON skill libraries: planning skills plus functional and atomic skills with `name`, `document`, `content`, `tools`, and metadata. The shipped AppWorld skill database demonstrates the artifact shape, but inference/retrieval is incomplete in the inspected code.

**Scope.** Benchmark and tool-environment scoped. The reviewed repository is strongest as a construction pipeline for prompt-injectable skill artifacts, not as a complete deploy-time memory system.

## SkillRL

Trajectory-derived SkillBank learning for RL agents, with both explicit prompt memory and optional policy learning.

**Trigger.** Offline pipelines build generated memories, aggregate skill banks, and create SFT data from rollout traces. During RL, dynamic updates can fire when training or validation success rates fall below configured thresholds, producing new failed-trajectory skills for later rollouts.

**Source format.** ALFWorld, WebShop, and Search rollouts: task metadata, success/failure labels, refined trajectory summaries, planning patterns, mistake records, decoded prompt/response histories, and SFT distillation records.

**Extraction.** Generated memory JSON is aggregated into `claude_style_skills*.json` SkillBanks with general skills, task/category skills, and common mistakes. The dynamic path parses failed trajectories, asks an LLM skill updater for new `dyn_NNN` general skills, appends them to the training memory object, and saves updated SkillBank snapshots.

**Promotion.** Hybrid two-stage substrate. The inspectable artifact is a JSON SkillBank whose selected prose rules are pushed into future prompts; the same skill-conditioned prompts and distilled examples can then train behavior into SFT/RL checkpoints. Dynamic updates append new prompt-facing skills rather than revising or retiring accepted ones.

**Scope.** Environment-scoped across ALFWorld, WebShop, and Search tasks. SkillRL sits between SkillX-style prose skill libraries and Amazon Science SAGE-style skill scaffolds for weight learning: it keeps a visible SkillBank at runtime while also compiling skill-conditioned behavior into policy weights.

## SkillWeaver

A web-agent exploration loop that promotes successful browser trajectories into executable Playwright APIs.

**Trigger.** Exploration iterations alternate between proposed website tasks and practice tasks for unverified skills. Successful non-test tasks trigger knowledge-base updates; successful direct tests increment function test counts.

**Source format.** Browser task traces: accessibility-tree states, screenshots, generated `act(page)` code, stdout/errors, locator recovery records, final screenshot, Playwright trace zips, task metadata, and success checks.

**Extraction.** For non-test tasks, an LLM receives the action trajectory, task, existing procedural knowledge, and semantic knowledge, then returns new or updated async Python functions. Code is statically checked for syntax, async shape, `page` parameter, docstrings, `page.goto`, type errors, and other Playwright-specific constraints before merge.

**Promotion.** Executable Python source plus metadata and optional semantic text. Functions are merged by name into the knowledge base, version/test counters are updated, and selected functions are later injected into codegen prompts or wrapped as Browser-Use controller actions.

**Scope.** Website/domain scoped. The shipped SkillNet covers WebArena-like domains, but exported code currently carries thinner lifecycle evidence than the exploration directories that produced it.

## AriGraph

Online text-game observations distilled into a semantic world model plus episodic memory.

**Trigger.** During each TextWorld step, the agent updates memory from the latest observation before the next planning or action-selection prompt. The QA path uses a staged variant: each question starts with a cleared graph, ingests paragraph observations, then answers from the retrieved graph and episodic context.

**Source format.** TextWorld observations, actions, inventory strings, admissible actions, current location, environment facts, and QA paragraphs treated as observations. This is a live environment trace, not a stored transcript or benchmark result table.

**Extraction.** LLM prompts convert observations into triplets or hypergraph theses, select important entities for retrieval, and decide which prior graph facts are stale. Contriever embeddings index triplet strings, entity names, and raw observation episodes.

**Promotion.** Temporary symbolic-plus-vector state: triplet graph or hypergraph facts, entity embeddings, and episodic observation records. The graph can be corrected during a run, but the reviewed code does not promote it into a durable cross-run memory artifact.

**Scope.** Per-run world-model memory for games, and per-question memory for QA. AriGraph is strongest as trace-to-operational-state learning: memory changes retrieval, planning, exploration, and navigation affordances without becoming reusable policy, code, or long-lived project knowledge.

## Amazon Science SAGE

An AppWorld RL system where temporary executable skills become training scaffold rather than a durable skill repository.

**Trigger.** During paired AppWorld rollouts. The first sampled subtask can generate reusable functions; the second subtask receives those functions and is rewarded when it uses them successfully.

**Source format.** AppWorld task trajectories: generated code blocks, observations, execution outcomes, task rewards, scenario/subtask identifiers, and extracted function definitions. The SFT path also consumes successful Claude rollout logs.

**Extraction.** Python `FunctionDef` nodes are parsed from generated code, imports are preserved, retrieved skills are smoke-executed before injection, and second-round code is checked for calls to existing skill names without redefinition. SFT extraction normalizes successful final code blocks from rollout logs.

**Promotion.** Two-stage substrate. The intermediate memory is symbolic executable code injected into a paired rollout. The durable promotion target is opaque model weights through SFT and GRPO checkpoints; the skill library itself is mostly transient dictionaries or experiment JSONL.

**Scope.** AppWorld-specific and scenario-local during training. This is not a maintained external skill KB; it is evidence for using external symbolic artifacts as scaffolds for policy learning.

## Agent-R

Search-tree mining into corrected conversation traces for weight training.

**Trigger.** MCTS over environment interaction. Each node executes a candidate action, records observation and reward, and backpropagates scores. Failed branches terminate early as `disaster` states.

**Source format.** MCTS search trees over benchmark tasks (WebShop, SciWorld, TextCraft). High-value and low-value leaf paths are paired for comparison.

**Extraction.** `path_collection.py` pairs good and bad paths, finds the first wrong step via `revise_worst_path(...)`, inserts a synthetic revision thought, and splices the corrected continuation from a better branch. The artifact is a repaired conversation trace, not a reflection or rule. `conversation_generation(...)` converts searched paths into training conversations with loss markers.

**Promotion.** JSONL training datasets handed to Xtuner for fine-tuning. The search trees and spliced conversations are intermediate; the final learning target is model weights.

**Scope.** Benchmark task families with executable environments. The repo implements collection and dataset construction more concretely than the training harness itself.

## Agent-S

Versioned computer-use agents where durable experience memory is strongest in older S1/S2 paths and the newer S3 path uses rich trace capture for immediate control and post-run selection.

**Trigger.** S1/S2 CLI paths can update experience memory after a task or subtask trajectory. S3 records benchmark trajectories during OSWorld runs; BBoN runs after multiple result directories exist, first captioning screenshot/action transitions and then judging among rollouts.

**Source format.** Mixed GUI execution traces: task/subtask text, screenshots, accessibility or screen state, grounded Python/pyautogui actions, reflections, executor plans, `traj.jsonl`, result files, rewards, and BBoN fact-caption JSONL.

**Extraction.** S1/S2 summarize trajectories through LLM prompts into narrative and episodic JSON records with embeddings. S3 reflection is online prompt-time feedback, not durable extraction. BBoN uses a behavior narrator to turn before/after screenshots plus executed actions into fact captions, then a comparative VLM judge selects among trajectories.

**Promotion.** S1/S2 promote into local JSON experience memory plus pickled embeddings. S3 deployment mostly keeps working state in prompt context and logs. BBoN promotes into benchmark artifacts — screenshots, trajectory JSONL, fact-caption JSONL, judge JSON, and result summaries — whose authority is selection/evaluation rather than next-task memory.

**Scope.** Computer-use tasks across OSWorld, WindowsAgentArena, AndroidWorld, and local CLI use. Agent-S is a split case: earlier versions are trajectory-to-prose-memory systems; the latest S3 runtime is closer to in-task control plus post-run trajectory evaluation.

## Self-Training-LLM

Corpus-grounded generation-trace self-training for factual QA.

**Trigger.** Offline script stages: `wiki_generation.py` creates or loads Wikipedia topics, generated questions, answers, and scores; `train.py` consumes answer pickles for SFT/DPO; `generate_response.py` and `pairwise_eval.py` test checkpoints.

**Source format.** JSONL questions/test sets and pickle answer datasets containing instructions, topics, documents, gold answers, raw answer samples, hallucination or consistency scores, and generation metadata.

**Extraction.** NLI/SelfCheckGPT/BSDetector/semantic-entropy scoring, threshold filters for question quality and unknownness, and `get_dpo_sample` selection of chosen/rejected answer pairs.

**Promotion.** SFT/DPO training data to model checkpoints via TRL SFTTrainer/DPOTrainer. No durable readable artifact; data files are staging.

**Scope.** Wikipedia factual QA over predefined topic categories and model-specific configs. The source traces are corpus-grounded generation traces, not autonomous agent task trajectories.

## Lightweight systems

These systems are included on weaker evidence — no implementation code inspected locally. They prevent code availability from biasing the taxonomy.

### AgeMem

From the [AgeMem lightweight note](./lightweight/agemem.md), [AgeMem ingest](https://arxiv.org/html/2601.01885v1), and [memory management policy is learnable but oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md): AgeMem learns a memory-management policy from interaction trajectories through RL. Trajectories with multiple stages, fixed memory operations (`Add`, `Update`, `Delete`, `Retrieve`, `Summary`, `Filter`), task-completion and context-management rewards. Promotion target is model weights. A clear trajectory-to-weights system, though the concrete storage/runtime implementation is unknown locally.

### Trajectory-Informed Memory Generation

From the [Trajectory-Informed Memory Generation lightweight note](./lightweight/trajectory-informed-memory-generation.md) and [trajectory-informed ingest](https://arxiv.org/html/2603.10600v1): completed execution trajectories are analyzed into strategy, recovery, and optimization tips, then consolidated and retrieved at runtime. Same broad input class as AgeMem and OpenClaw-RL, but the promotion target is inspectable text artifacts with prompt-time retrieval — the direct non-weight counterpart. Implementation details, consolidation prompts, and thresholds are unknown locally.

## What the comparison makes concrete

With the per-system evidence in place, the two axes previewed in the introduction become concrete.

### Axis 1: trace ingestion pattern

**Single-session extension.** Run inside an existing agent runtime, mine the current conversation, reuse the runtime's session representation, write back into markdown artifacts. Napkin and Pi Self-Learning fit here, though Napkin is even looser — it treats the session as an opaque file and delegates extraction to a subprocess agent.

**Doctrine-mediated live capture.** Do not mine a stored log; instead, instruct the acting agent to identify durable session knowledge while working and write it through a small CLI. Gnosis is the clean case. It is trace-derived in the weak/manual sense: the raw signal is session context, but extraction happens through agent compliance with doctrine rather than a hook or offline miner.

**Local filesystem runner.** Own a small execution cycle and artifact schema, but keep all learned state in project files rather than a service backend. Operational Ontology Framework fits here: it promotes task-output learnings into `_facts.md`, `_spec.md`, and handoff markdown, but the trace is much thinner than a transcript or typed tool log.

**Cross-agent session aggregator.** Discover and mine session logs from multiple agent runtimes via an external search engine, normalize heterogeneous formats into a common representation, accumulate results in a shared playbook. cass-memory is the only inspected system in this category — it reads session files from Claude Code, Cursor, Codex, Aider, and Pi, normalizes them through `formatRawSession()`, and mines them through a two-phase diary-then-reflection pipeline. Unlike single-session extensions, it operates *after* sessions complete rather than during them, and unlike service backends, it does not own the session format.

**Local trace recall index.** Discover existing session stores from several harnesses, preserve the original logs as authority, and build a redacted access structure for later lookup rather than mining lessons. deja-vu fits here: it indexes Claude, Codex, and opencode histories into a local lexical cache, then serves pull recall and optional project-scoped startup context. This category separates "trace-derived memory as search substrate" from systems that distill traces into playbooks or policies.

**Framework-integrated runtime memory.** Live inside the agent framework, consume task/run outputs and optional human feedback at the framework hook boundary, and promote into the same memory store that later prompt assembly uses. CrewAI Memory is the clear case here. It is not an external service, and it is not an offline trajectory learner; its distinctive feature is tight integration with agent execution.

**Online capability creation.** Keep the runtime's bootstrap tool surface stable, but let the agent turn live task needs into durable callable artifacts during deployment. Tendril is the clean case: it lists workspace capabilities, registers a new Deno TypeScript tool when none fits, then executes future requests by capability name. This differs from trajectory-run systems because there is no offline consolidation phase; the write immediately creates a system-definition artifact.

**Service-owned trace backend.** Own the message or event schema, accept structured traffic over an API or proxy, separate archive from extraction from downstream processing, support many sessions feeding one backend. OpenViking fits as a memory service; nao and MemoryOS as product/conversation assistants with user-memory extraction; REM as a simpler episodic memory service with keyword-clustered consolidation; OpenClaw-RL as a policy-learning backend. ClawVault partially fits as a local vault-plus-observer rather than a shared multi-tenant service.

**Trajectory-run pattern.** Learn from repeated runs rather than one live conversation, consume scored generations or completed-task traces, consolidate across many episodes before promotion. Autocontext, Meta-Harness, Agentic Harness Engineering, Reflexion, Dynamic Cheatsheet, Agent Workflow Memory, ACE, ExpeL, ReasoningBank, AgentFly, Voyager, OS-Copilot, SkillX, SkillRL, SkillWeaver, Amazon Science SAGE, Agent-R, and Agent-S fit here, along with lightweight AgeMem and Trajectory-Informed Memory Generation. Self-Training-LLM is an edge case: it learns from corpus-grounded generation traces rather than autonomous task trajectories, but it has the same staged trace-to-training-data shape. G-Memory extends the pattern to multi-agent trajectories with within-run coordination structure. AriGraph sits next to this pattern rather than fully inside it: it learns online from an environment trajectory, but promotes into per-run operational graph state instead of consolidating across repeated episodes. Autocontext straddles this boundary — it owns its trace format (SQLite, competitor outputs, playbooks) like a service backend, but learns from repeated runs like a trajectory system; it is placed here because episode-level iteration is its primary learning mechanism.

### Axis 2: promotion target / representational form

**Trace-to-recall access structures.** Mine traces into searchable records, indexes, metadata, and context digests whose job is to make prior episodes findable, not to assert a new lesson. deja-vu is the clean case: its durable learned surface is a redacted lexical cache plus routing/ranking metadata. The original session logs remain the evidence authority; the promoted artifact changes future work only by retrieval and optional startup injection.

**Readable artifact learning.** Mine traces into inspectable artifacts — observations, tips, playbooks, reports, executable code, structured memory records, case rows, or skill patches. Keep learned results in forms humans can inspect, diff, or curate. Use heuristics, recurrence, judges, or retrieval-time relevance to decide what persists. ClawVault, CrewAI Memory, cass-memory, REM, nao, MemoryOS, Tendril, and Trajectory-Informed Memory Generation fit cleanly; Autocontext for its playbooks and reports; Napkin, Pi Self-Learning, Operational Ontology Framework, and Gnosis in narrower senses; Reflexion, Dynamic Cheatsheet, Agent Workflow Memory, ACE, ExpeL, ReasoningBank, AgentFly, SkillX, SkillRL, Agent-S, and G-Memory as trajectory-run artifact-learners. AriGraph adds a temporary symbolic-state variant: traces become triplets, graph edges, embeddings, and episodic records that are inspectable in code/log terms but not promoted into a maintained library. Voyager, OS-Copilot, and SkillWeaver extend the category to executable code artifacts — JavaScript skills in Voyager, Python OS tools in OS-Copilot, Playwright browser APIs in SkillWeaver — all promoted after environment-grounded success; Meta-Harness extends it to executable harness code promoted by benchmark frontiers; Agentic Harness Engineering extends that harness-code branch with a broader component menu spanning promptware, tool descriptions, middleware, skills, sub-agents, and memory files; ARIS extends it to markdown skill diffs promoted by hook-log evidence and reviewer judgment. The category spans from prose form (verbal hints, profile/fact strings, scored rules, structured records, repo-local entries) to symbolic form (workflow instructions and executable code); their storage substrates differ further still, but they share the readable side of the representational-form split with weight learning.

**Distributed-parametric learning.** Mine trajectories, next-state signals, or generation traces under a sufficiently strong oracle, re-express them as training signals, and promote into model weights, adapters, learned rankers, or controllers. AgeMem, OpenClaw-RL, Amazon Science SAGE, SkillRL, Agent-R, Self-Training-LLM, and Autocontext fit here. Autocontext bridges both — symbolic artifacts first, then optionally weights. Amazon Science SAGE adds a symbolic-to-distributed-parametric variant: generated functions are rollout-time skill scaffolds, but the durable promotion target is the policy checkpoint. SkillRL adds a readable-skill-bank-to-policy variant: JSON skills remain prompt-facing artifacts while SFT/RL can absorb their behavior into model weights. AgentFly is a weaker adjacent case: the trained parameters select external cases, while the case bank remains the primary memory. Agent-R adds dataset surgery between trace collection and training: MCTS paths are paired, corrected, and spliced into revision conversations before becoming fine-tuning data. Self-Training-LLM adds corpus-grounded answer-sample surgery: generated questions and sampled answers are scored, filtered, and paired before SFT/DPO.

### What the expanded survey reveals: artifact structure varies widely

Within the readable-artifact branch, the artifact-learning systems span a wide range of structure and maintenance:

- **Minimal verbal hints:** Reflexion stores one or a few reflection sentences in a rolling buffer.
- **Full-document rewrite:** Dynamic Cheatsheet carries forward one cheatsheet blob, rewritten wholesale each step.
- **Workflow prompt files:** Agent Workflow Memory writes website-scoped workflow text from examples and successful trajectories, then injects the whole file into later acting contexts.
- **Scored flat rules:** ACE (bullet counters), ExpeL (strength counters with mutation verbs), G-Memory (scored insights with clustering).
- **Planner case rows:** AgentFly (question/plan/outcome JSONL rows, optionally paired with learned query-case selector weights).
- **Hierarchical skill objects:** SkillX (plan memories, functional skills, atomic tool skills with documents, content, tools, and metadata).
- **Prompt skill banks:** SkillRL (general skills, task/category skills, and common mistakes in JSON, pushed into SFT/RL prompts and optionally updated from failed trajectories).
- **GUI experience summaries and judged traces:** Agent-S (S1/S2 JSON trajectory summaries; S3/BBoN screenshot/action fact captions and judge records).
- **Temporary world models:** AriGraph (in-run triplet/hypergraph facts, entity embeddings, and episodic observation records).
- **Profile and fact memory:** MemoryOS (session summaries, user profile, user knowledge, assistant knowledge, embeddings).
- **Structured records:** ReasoningBank (title/description/content JSONL), CrewAI Memory (vector records with scope/categories/importance/source/private metadata), cass-memory (YAML playbook with maturity stages).
- **Repo-local prose entries:** Gnosis (JSONL why-memory with topics, related IDs, and timestamps, extracted by live agent judgment).
- **Typed durable observations:** ClawVault (observation ledgers with weekly reflection), OpenViking (categorized user/agent memory spaces), nao (user instruction/profile rows with supersession).
- **Workflow instruction patches:** ARIS (hook-log-derived diffs to markdown skills and workflow defaults).
- **Executable code:** Voyager (JavaScript skills with generated descriptions and vector retrieval), OS-Copilot (Python OS tools with generated descriptions and vector retrieval), Tendril (Deno TypeScript capabilities with trigger/suppression metadata), SkillWeaver (async Playwright APIs with docstrings, metadata, and static checks).

The maintenance path also varies: append-only (Reflexion, ReasoningBank), rewrite-and-carry-forward (Dynamic Cheatsheet), workflow-file replacement (Agent Workflow Memory), counter-based (ACE), explicit CRUD verbs (ExpeL, G-Memory), and critic- or judge-gated promotion (Voyager, OS-Copilot). These differences matter more for real system design than the broader representational-form distinction.

## Log formats matter more than the prompts

The biggest difference across systems is not extraction prompt wording but the shape of the source trace:

| System | Source trace |
|---|---|
| Napkin | Opaque pi session file, delegated to subprocess |
| Pi Self-Learning | Pi branch events: messages + tool-result interruptions |
| OpenViking | Own typed message schema with text/context/tool parts, JSONL |
| Operational Ontology Framework | Per-task model JSON fields (`result`, `decision`, `learned`) plus markdown project artifacts |
| nao | Recent user/assistant UI message text from a product chat, with richer typed message parts stored but not mined by the memory extractor |
| ClawVault | Assistant turns + incremental OpenClaw session JSONL, noise-stripped |
| CrewAI Memory | Framework-assembled task outputs, standalone input/result pairs, and optional human-feedback output/feedback pairs |
| cass-memory | Multi-agent session files (Claude Code JSON, Cursor, Codex, Aider, Pi), discovered via `cass` search engine, normalized to markdown |
| deja-vu | Existing Claude Code and Codex JSONL histories plus opencode SQLite text parts, parsed into redacted lexical records |
| REM | Agent-submitted content strings via HTTP API, parsed by GPT-4o-mini into intent/entities/domain/emotion/importance |
| Autocontext | Run trajectories from SQLite metrics, competitor outputs, playbooks, hints |
| Meta-Harness | Benchmark run logs, saved memory/harness state, frontiers, proposer sessions, and task trajectories |
| Agentic Harness Engineering | Harbor job directories, NexAU traces, verifier outputs, task flips/regressions, debugger reports, and change manifests |
| HALO | OTel-shaped JSONL agent spans with sidecar byte-offset index, trace summaries, span search, and sandbox-readable trace store |
| ARIS | Claude Code hook events: skill invocations, tool failures, Codex calls, slash commands, prompts, session boundaries |
| OpenClaw-RL | Live chat-completion traces + next-state feedback → training samples |
| Reflexion | Failed task attempts + feedback (test results, rewards, success/failure) |
| Dynamic Cheatsheet | Ordered benchmark queries and answers, optionally retrieved prior examples |
| Agent Workflow Memory | Annotated web-task examples, result JSON, WebArena logs, and benchmark success signals |
| ACE | Question attempts, reasoning traces, feedback, bullet usage tags |
| ExpeL | Succeeded and failed task trajectories gathered across benchmark folds |
| ReasoningBank | Benchmark task trajectories (WebArena, SWE-Bench), successes and failures |
| G-Memory | Multi-agent benchmark trajectories with state-graph coordination structure |
| AgentFly | Benchmark question runs: planner JSON, executor steps, tool history, final answer, judge rationale, reward/correctness labels |
| Gnosis | Live coding-session context selected by the acting agent; no raw transcript mining |
| Voyager | Embodied task trajectories: execution errors, inventory state, critic feedback |
| OS-Copilot | OS subtask execution traces: generated code, invocation, environment output/errors, downstream needs, judge critique, repair attempts, generality score |
| Tendril | Live user requests, capability-registry reads, generated TypeScript tools, JSON arguments, Deno outputs/errors, and workspace state |
| SkillX | Benchmark task trajectories: user task, interaction steps, reward, tool calls/responses, and optional failed traces |
| SkillRL | ALFWorld/WebShop/Search rollouts: generated memories, success/failure labels, prompt/response histories, failed-trajectory update traces, and SFT distillation records |
| SkillWeaver | Browser task trajectories: accessibility trees, screenshots, generated action code, outputs/errors, recovery records, Playwright traces, and success checks |
| AriGraph | TextWorld observations, inventory/location strings, admissible actions, environment facts, and QA paragraphs treated as observations |
| Amazon Science SAGE | AppWorld paired-subtask rollouts: generated functions, environment outcomes, skill use, rewards, and SFT rollout logs |
| Agent-R | MCTS search trees: action-observation-reward nodes with backpropagated scores |
| Agent-S | GUI task trajectories: screenshots, accessibility/screen state, grounded Python actions, reflections, result files, rewards, fact captions, and judge records |
| Self-Training-LLM | Generated Wikipedia QA traces: question records, gold/context answers, raw sampled answers, NLI/SelfCheck scores |
| AgeMem | RL trajectories over memory operations + task/context rewards |
| Trajectory-Informed | Completed execution trajectories → strategy/recovery/optimization tips |

Trace richness constrains what can be learned. Tool calls, statuses, gates, scores, and context snapshots enable operational pattern mining that plain transcripts cannot support. Opaque traces force the miner to trust the upstream runtime. Oracle-aligned traces enable promotion all the way to weights. [Meta-Harness](./reviews/meta-harness.md) confirms the implementation side of the existing paper evidence: on text classification, the paper reports that a proposer agent with access to raw execution traces (10 MTok/iteration) achieves median 50.0% accuracy, while the same proposer with scores-only (34.6%) or scores+summary (34.9%) trails by 15+ points. The repo's local skills and loops are built around that lesson: the proposer is expected to read raw logs, memory states, trajectories, and frontier files, not just scores. [Agentic Harness Engineering](./reviews/agentic-harness-engineering.md) adds the adjacent pattern: raw traces are preserved, but an explicit debugger layer first compresses them into root-cause reports before the evolve agent edits the harness. [HALO](./reviews/halo.md) narrows that debugger layer into a reusable runtime: byte-offset trace indexing, bounded trace tools, oversized summaries, subagent fan-out, and sandboxed aggregate analysis keep diagnostic reports tied to drill-down paths back into raw spans. Summaries do not recover all compressed signal, but staged diagnostic summaries can still be useful when they preserve drill-down paths to raw evidence. This quantifies what the survey table above implies: diagnostic richness is a binding constraint on outer-loop learning quality, not just a convenience.

## What looks borrowable

- **Explicit boundary triggers.** `agent_end`, `session.commit()`, periodic distill checks — concrete extraction clocks.
- **Narrow extraction schemas.** Pi Self-Learning's `mistakes/fixes` pair; OpenViking's fixed memory categories.
- **Tool-result mining.** Both Pi Self-Learning and OpenViking mine beyond user/assistant prose — blocked commands, permission denials, tool statuses.
- **Separate trigger from promotion.** Systems that keep extraction and ranking/promotion distinct are easier to reason about.
- **Artifact-to-weight handoff.** Autocontext makes explicit what others leave implicit: mined artifacts can be intermediate, not terminal.
- **Representational-form choice as design decision.** The same input class can end as notes/observations/tips or as distributed-parametric updates.
- **Explicit mutation verbs on learned artifacts.** ExpeL's `ADD`/`EDIT`/`REMOVE`/`AGREE` and G-Memory's matching operations give the maintenance loop a visible contract.
- **Critic-gated promotion.** Voyager only promotes successful programs — a strong filter that prevents accumulation of failed attempts.
- **Bidirectional extraction from successes and failures.** ReasoningBank uses separate prompts for successful and failed trajectories, yielding different kinds of insights.
- **Executable code as promotion target.** Voyager and OS-Copilot show that some trace-derived learnings should become callable programs, not just textual guidance.
- **Name-gated generated tools.** Tendril adds a runtime pattern where generated code must first become a named registry artifact before it can execute.
- **Executable APIs as memory.** SkillWeaver narrows the executable-code pattern further: a learned memory can be a domain-specific API over a repeated web surface, not only a one-off script.
- **Scaffold-to-weight promotion.** Amazon Science SAGE uses generated functions as temporary symbolic memory, then rewards reuse so the behavior can compile into policy weights.
- **Readable skill bank before policy learning.** SkillRL keeps the generated SkillBank inspectable and prompt-facing before SFT/RL can absorb the behavior, which is a useful hybrid only if provenance and lifecycle governance are added.
- **Harness code as promotion target.** Meta-Harness pushes the executable-artifact point one level outward: the learned artifact can be the retrieval, memory, context, or tool-use harness around a model.
- **Bounded trace drill-down before promotion.** HALO shows that the diagnostic layer itself can enforce progressive disclosure: overview first, filtered summaries second, surgical span reads and sandboxed aggregates only when justified.
- **Skill text as promotion target.** ARIS shows the softer promptware version of the same move: traces can propose changes to invocation procedures and workflow defaults, but weak oracles require reviewer and user gates.
- **Case-selection weights around readable memory.** AgentFly shows a narrow hybrid where JSONL case rows stay inspectable while learned parameters decide which cases deserve prompt budget.
- **Multi-granularity skill memory.** SkillX separates trajectory-derived memory into plans, functional skills, and atomic tool skills, making granularity an explicit artifact-design choice.
- **Dataset surgery between traces and training.** Agent-R's path-pairing and splice-correction is more informative than binary success/failure labels.
- **Oracle/filtering surgery before weight updates.** Self-Training-LLM separates question-quality filtering from unknownness filtering before constructing SFT/DPO records.
- **Counter-based artifact scoring.** ACE's bullet-level helpful/harmful counters and ExpeL's strength counters create real lifecycle behavior without full curation.
- **Human-context capture filter.** Gnosis shows the lowest-friction way to control noise in agent-written memory: tell agents to preserve perishable human or empirical context, not reasoning that future agents can rederive from code.

## What remains open

None of the reviewed systems closes the harder learning-loop mutations — the ones that require judgment beyond local task success. They extract and persist candidates well, and some close the loop for scenario-bounded updates, but that is still different from:

- deciding whether two notes should be linked
- synthesizing a better abstraction from several sessions
- retiring a stale learning for principled reasons
- judging whether a mined pattern has explanatory reach or is just a recurring local patch

The additional trajectory-run systems reinforce this from the artifact side. ExpeL's explicit rule operations and Voyager's critic-gated code promotion show increasingly structured maintenance, but both depend on strong local oracles (benchmark outcomes, environment success). Self-Training-LLM shows the same oracle dependence from the weight-learning side: its "unknown" examples are only as good as the NLI/SelfCheck and judge signals that select them. cass-memory's score-based deprecation and `invertToAntiPattern()` mechanism are the closest to principled retirement, but they are mechanical (threshold-driven) rather than explanatory — they retire artifacts that stop working without reasoning about why. None of these systems demonstrates retirement grounded in explanatory reach, cross-domain abstraction, or open-ended judgment.

The concrete update to [automating KB learning is an open problem](../notes/automating-kb-learning-is-an-open-problem.md): **session- or trajectory-derived candidate generation is concrete enough in source code to adapt; oracle-backed evaluation is not.** Once you have a strong enough oracle, the same mined traces can feed readable artifacts or weight updates. The open problem is not extraction — it is deciding what deserves trust and persistence in open-ended domains.

---

Relevant Notes:

- [continual learning's open problem is behaviour, not knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md) — sharpens: the survey's artifact-promotion systems count as behaviour-change learning via readable system-definition artifacts; the distributed-parametric cases take the expensive mechanism
- [Axes of artifact analysis](../notes/axes-of-artifact-analysis.md) — sharpens: separates storage substrate, representational form, lineage, and behavioral authority, clarifying that service memory is usually a substrate choice rather than a form or authority family
- [automating KB learning is an open problem](../notes/automating-kb-learning-is-an-open-problem.md) — sharpens: source-inspected systems now give concrete extraction and promotion loops for workshop artifacts and policy learning; the remaining bottleneck is still evaluation of higher-order mutations
- [a functioning knowledge base needs a workshop layer, not just a library](../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — grounds the artifact-promotion side of this survey: several systems operationalize workshop-to-library bridges from session traces or run trajectories, even though the weight-learning cases extend beyond that note's domain
- [Designing a Memory System for LLM-Based Agents](../notes/designing-agent-memory-systems.md) — rationale: turns the survey's repeated techniques into a needs map for direct-authored and trace-derived memory, including capture, activation, promotion, lifecycle, and evaluation
- [Napkin](./reviews/napkin.md) — source-inspected instance: forked-session distill via a subprocess agent and vault templates
- [Pi Self-Learning](./reviews/pi-self-learning.md) — source-inspected instance: branch-event mining into strict `mistakes`/`fixes` JSON plus scored promotion
- [OpenViking](./reviews/openviking.md) — source-inspected instance: typed session messages, commit-triggered extraction, and multi-tenant user/agent memory spaces
- [Operational Ontology Framework](./reviews/operational-ontology-framework.md) — source-inspected instance: local filesystem runner that promotes per-task model learnings into project facts, spec annotations, and handoff artifacts
- [nao](./reviews/nao.md) — source-inspected instance: product analytics assistant that extracts conservative user instruction/profile memories from recent chat text into database rows
- [MemoryOS](./reviews/MemoryOS.md) — source-inspected instance: conversational memory library that promotes dialogue into session summaries, user profiles, and retrievable knowledge entries
- [ClawVault](./reviews/clawvault.md) — source-inspected instance: assistant-turn capture, incremental OpenClaw session observation, scored observation ledgers, and recurrence-based weekly reflection
- [CrewAI Memory](./reviews/crewai-memory.md) — source-inspected instance: framework-integrated task/output and HITL feedback mining into scoped vector memory records with automatic prompt reinjection
- [cass-memory](./reviews/cass_memory_system.md) — source-inspected instance: cross-agent session mining via `cass` search engine, two-phase diary-then-reflection extraction, and confidence-decayed YAML playbook with anti-pattern inversion
- [deja-vu](./reviews/deja-vu.md) — source-inspected instance: Claude, Codex, and opencode session traces indexed into redacted lexical recall plus optional project-scoped Claude startup context
- [REM](./reviews/REM.md) — source-inspected instance: service-owned episodic memory backend with keyword-clustered consolidation into append-only scored facts; widest gap between aspirational lifecycle fields and actual single-pass implementation
- [Autocontext](./reviews/autocontext.md) — source-inspected instance: run-trajectory mining into playbooks, session reports, JSONL training exports, and optional weight distillation
- [Meta-Harness](./reviews/meta-harness.md) — source-inspected instance: benchmark-trace-driven outer loop that promotes generated memory systems and agent scaffolds into executable harness code
- [Agentic Harness Engineering](./reviews/agentic-harness-engineering.md) — source-inspected instance: benchmark-trace-driven outer loop with debugger-mediated trace distillation and component-level promotion into prompts, tools, middleware, skills, sub-agents, and memory files
- [HALO](./reviews/halo.md) — source-inspected instance: OTel-trace diagnostic runtime with bounded drill-down tools, sandboxed aggregate analysis, and coding-agent-mediated harness promotion
- [ARIS](./reviews/Auto-claude-code-research-in-sleep.md) — source-inspected instance: Claude Code hook logs become reviewer-gated proposals to patch markdown skills and workflow defaults
- [OpenClaw-RL: Train Any Agent Simply by Talking](https://arxiv.org/html/2603.10165v1) — TODO for repo-backed review; current placement records source-grounded next-state feedback, PRM scoring, OPD-style supervision, and live background weight updates
- [Reflexion](./reviews/reflexion.md) — source-inspected instance: early verbal reinforcement loop with rolling reflection buffer and bounded retry scope
- [Dynamic Cheatsheet](./reviews/dynamic-cheatsheet.md) — source-inspected instance: prompt-state artifact learning through full-document cheatsheet rewrites across benchmark queries
- [Agent Workflow Memory](./reviews/agent-workflow-memory.md) — source-inspected instance: web-task trajectories and annotated examples distilled into website-scoped workflow prompt files
- [ACE](./reviews/ace.md) — source-inspected instance: three-role playbook loop with bullet IDs, helpful/harmful counters, and append-heavy curation
- [ExpeL](./reviews/expel.md) — source-inspected instance: staged trajectory gathering and rule consolidation with explicit ADD/EDIT/REMOVE/AGREE operations and strength counters
- [ReasoningBank](./reviews/reasoning-bank.md) — source-inspected instance: bidirectional extraction from successes and failures into append-only structured memory items with embedding retrieval
- [G-Memory](./reviews/g-memory.md) — source-inspected instance: multi-agent trajectory capture with state-graph coordination, task-neighborhood retrieval, and scored insight maintenance
- [AgentFly](./reviews/AgentFly.md) — source-inspected instance: judged benchmark runs distilled into JSONL planner-case memory, with optional learned query-case selector weights
- [Voyager](./reviews/voyager.md) — source-inspected instance: critic-gated promotion of successful embodied trajectories into executable JavaScript skills with vector retrieval
- [OS-Copilot](./reviews/OS-Copilot.md) — source-inspected instance: judge-gated promotion of successful OS task executions into executable Python tools with vector retrieval
- [Tendril](./reviews/tendril.md) — source-inspected instance: live deployment requests promoted directly into named Deno TypeScript capabilities in a workspace-local registry
- [SkillX](./reviews/SkillX.md) — source-inspected instance: successful benchmark trajectories distilled into plan, functional-skill, and atomic-tool-skill JSON artifacts
- [SkillRL](./reviews/SkillRL.md) — source-inspected instance: ALFWorld/WebShop/Search rollouts distilled into prompt-facing SkillBank JSON, dynamic failed-trajectory skills, and skill-conditioned SFT/RL
- [SkillWeaver](./reviews/SkillWeaver.md) — source-inspected instance: browser task traces distilled into executable Playwright API skills with static checks and WebArena-style evaluation
- [AriGraph](./reviews/AriGraph.md) — source-inspected instance: online TextWorld observations distilled into a temporary semantic graph plus episodic memories that alter planning, retrieval, exploration, and navigation
- [Amazon Science SAGE](./reviews/amazon-science--SAGE.md) — source-inspected instance: AppWorld rollouts where generated functions act as transient skills whose reuse is rewarded into SFT/GRPO checkpoints
- [Agent-R](./reviews/agent-r.md) — source-inspected instance: MCTS search-tree mining into corrected conversation traces and fine-tuning datasets for weight updates
- [Agent-S](./reviews/Agent-S.md) — source-inspected instance: computer-use trajectories summarized into S1/S2 JSON experience memory and S3/BBoN benchmark fact/judge artifacts
- [Self-Training-LLM](./reviews/Self-Training-LLM.md) — source-inspected instance: generated Wikipedia QA traces, NLI/SelfCheck filtering, and SFT/DPO promotion into model checkpoints
- [the fundamental split in agent memory is not storage format but who decides what to remember](./agentic-memory-systems-comparative-review.md) — extends: the wider survey places AgeMem and other lightweight systems in the broader agency and substrate design space
- [memory management policy is learnable but oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: these systems learn or curate policy only as far as their available promotion oracle allows
