---
description: Broad review of Napkin, Pi Self-Learning, OpenViking, ClawVault, cass-memory, Autocontext, OpenClaw-RL, and trajectory learners — compares trace formats, promotion targets, and learning loops
type: note
traits: [has-comparison, has-implementation]
tags: [learning-theory, observability]
status: seedling
---

# Trace-derived learning techniques in related systems

Eight code-inspected systems and two source-only systems all learn from traces — CLI sessions, event streams, assistant turns, run trajectories, or next-state feedback. This note reviews what each system actually does, then draws out the two axes that separate them: how they ingest traces and where they promote the result. In the KB's newer vocabulary, the second axis is mainly a **substrate-class** choice: do traces promote into durable symbolic artifacts or into model weights?

The code-inspected systems are Napkin, Pi Self-Learning, OpenViking, ClawVault, cass-memory, Autocontext, and OpenClaw-RL (source paths noted in per-system reviews). The source-only systems — AgeMem and Trajectory-Informed Memory Generation — are included with lower confidence, based on local ingest notes rather than implementation inspection.

## The recurring stages

Across these systems, the same five stages appear:

1. **Trigger** — when mining runs
2. **Source format** — what raw session representation is consumed
3. **Extraction schema** — what target shape the model or code writes
4. **Promotion/storage** — how extracted items persist or get ranked
5. **Reinjection** — how mined artifacts affect future sessions

What varies is not whether the loop exists, but how structured the input is, whether the system assumes one active session or many repeated runs, and whether the promotion target is symbolic artifacts, service-managed memory, or model weights. [Learning substrates, backends, and artifact forms](./learning-substrates-backends-and-artifact-forms.md) sharpens the distinction: "service memory" is usually a backend choice within the symbolic artifact substrate, not a third top-level substrate alongside artifacts and weights.

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

## ClawVault

Two mining paths: direct assistant-turn capture into typed markdown memories, and incremental session observation over OpenClaw session files with weekly reflection.

**Trigger.** `captureTurn(...)` stores memories from assistant responses immediately. The OpenClaw plugin also triggers on `agent_end` heartbeats, `before_compaction`, and `before_reset`, with optional auto-checkpointing and weekly reflection on session start. A standalone `observe` command supports one-shot compression, cron runs, or file watching.

**Source format.** Consumes both assistant turns and session logs. The active observer reads `sessions/*.jsonl`, tracks per-session byte offsets in `.clawvault/observe-cursors.json`, and processes new content past a size threshold. The parser strips tool/system/developer noise, structured metadata, and base64 payloads, keeping user/assistant conversational content.

**Extraction.** Two layers. `src/capture/extractor.ts` extracts typed memories from assistant responses via `<memory_note>` tags plus heuristic sentence classification (`decision`, `preference`, `lesson`, `relationship`, `episode`, etc.). `src/observer/compressor.ts` turns session updates into scored observation lines `[type|c=...|i=...] content`. The observation type system: `decision`, `preference`, `fact`, `commitment`, `task`, `todo`, `commitment-unresolved`, `milestone`, `lesson`, `relationship`, `project`.

**Promotion.** Capture writes into category folders (`facts`, `preferences`, `decisions`, `lessons`, `people`). The observer writes dated observation ledgers. `runReflection(...)` promotes recurring observations into weekly reflections: importance ≥ 0.8 promotes immediately; importance ≥ 0.4 promotes when seen on at least two dates — implemented in `promoteWeekRecords(...)`.

**Scope.** Single-agent vault with session lifecycle support. Owns its vault substrate and watches session files, but does not present as a multi-tenant backend. Best understood as a workshop-memory system around one workspace.

## cass-memory

The only inspected system that makes cross-agent session mining a first-class feature. Structurally a two-phase extraction pipeline (diary then reflection) feeding a scored playbook.

**Trigger.** Explicit CLI commands: `cm reflect` orchestrates the full pipeline (discover → diary → reflect → curate); `cm diary <session>` extracts a single session. No event-driven hooks — triggers are manual or agent-initiated. `orchestrateReflection()` in `orchestrator.ts` coordinates the multi-session flow.

**Source format.** `findUnprocessedSessions()` in `cass.ts` discovers sessions via the external `cass` search engine, using `cassTimeline()` (primary) or broad keyword searches (fallback). `cassExport()` exports sessions as markdown via `cass export --format markdown`, with fallback to direct file parsing of `.jsonl`, `.json`, or `.md` files. `formatRawSession()` in `diary.ts` normalizes multiple agent formats — Claude Code JSON, Cursor, Codex CLI, Aider, Pi — into markdown. Agent identity is pattern-matched from file paths (`.claude`, `.cursor`, `.codex`, `.aider`, `.pi/agent/sessions`). Session content is truncated to 50k chars and secrets are stripped before LLM processing.

**Extraction.** Two phases. Phase 1: `extractDiary()` in `llm.ts` produces a Zod-validated `DiaryEntry` with accomplishments, decisions, challenges, preferences, key learnings, tags, and search anchors — each field asks for specific file names, function names, and error messages rather than vague summaries. Diary IDs are deterministic content hashes for idempotency. Phase 2: `runReflector()` in `llm.ts` takes the diary plus existing playbook bullets plus cross-agent history and proposes `PlaybookDelta` operations: `add`, `helpful`, `harmful`, `replace`, `deprecate`, `merge`. Runs up to 3 iterations with early exit on diminishing returns; `deduplicateDeltas()` prevents duplicates within and across iterations.

**Promotion.** `curatePlaybook()` in `curate.ts` applies deltas to YAML playbook files (global at `~/.cass-memory/playbook.yaml`, optional per-repo overlays). New bullets enter as `candidate` maturity. Curation checks Jaccard similarity for duplicates, detects conflicts via negation/directive markers, and reinforces existing bullets on near-matches. `getEffectiveScore()` in `scoring.ts` computes `decayedHelpful - (4 × decayedHarmful)` with exponential decay (90-day half-life). When harmful feedback exceeds a threshold, `invertToAntiPattern()` creates a new bullet prefixed "AVOID:" with `kind: "anti_pattern"`. Maturity progresses `candidate → established → proven → deprecated` based on effective score.

**Reinjection.** `cm context "<task>"` retrieves relevant bullets by keyword matching, effective score, and optional embedding similarity, returning ranked rules, anti-patterns, related session history, and warnings about deprecated patterns. Cross-agent enrichment happens during diary generation: `enrichWithRelatedSessions()` queries the `cass` search engine for sessions from *other* agents that match the current diary's challenges and learnings, with access logged to `privacy-audit.jsonl`.

**Scope.** Cross-agent, multi-session. Reflects over sessions from Claude Code, Cursor, Codex, Aider, and Pi within a configurable lookback window (default 7 days, up to N sessions). A single shared playbook accumulates rules from all agents, with optional per-repo overlays. `ProcessedLog` in `tracking.ts` tracks which sessions have been reflected on to enable incremental processing.

## Autocontext

The clearest inspected system spanning both artifact learning and weight promotion. Mines repeated run trajectories rather than one interactive transcript.

**Trigger.** Two clocks. During multi-generation runs, `accumulate_lessons(...)` turns judge feedback into generation-level lessons carried forward in the playbook. At run end, `generate_session_report(...)` summarizes the trajectory and `ArtifactStore.write_session_report(...)` persists it. Weight distillation is a separate offline step: export JSONL from prior runs, train, publish.

**Source format.** Not a transcript or message bus. The source trace splits across SQLite generation rows (`best_score`, `gate_decision`, Elo), stored competitor outputs, per-scenario artifact files (`playbook.md`, `hints.md`), and generated markdown session reports. The export path packages per-generation records with `strategy`, `score`, `gate_decision`, and a `context` object containing `playbook`, `hints`, and `trajectory`.

**Extraction.** Intentionally simple. `accumulate_lessons(...)` turns judge reasoning and dimension scores into structured lesson text. `generate_session_report(...)` produces markdown with gate counts, top improvements, and dead ends. `export_training_data(...)` re-expresses kept generations as JSONL training records.

**Promotion.** Two-step. First into files: versioned playbooks, hints, lesson history, session reports. Then optionally into weights: `TrainingRunner` uses exported JSONL, `publish_training_output(...)` registers a distilled model by scenario/backend/runtime. Autocontext is the only inspected system that bridges both promotion targets.

**Scope.** A trajectory-learning control plane over many runs and generations. Knowledge is scenario-scoped, accumulated across runs, and optionally compiled into a model that no longer needs the full playbook at inference.

## OpenClaw-RL

An implemented asynchronous training stack behind the paper's architecture.

**Trigger.** Live API traffic. `OpenClawAPIServer` proxies `POST /v1/chat/completions` with `X-Session-Id`, `X-Turn-Type`, and `X-Session-Done` headers. PRM judging runs asynchronously once next-state evidence arrives; rollout workers drain scored samples into training queues.

**Source format.** A session-aware chat-completion stream. The proxy normalizes message arrays, separates `main` turns from side turns, and pairs assistant outputs with later next-state feedback. `TrainingSample` carries `session_id`, `turn_num`, prompt/response tokens, sampled log-probs, `loss_mask`, scalar `reward`, optional `teacher_logprobs`, and `sample_type`.

**Extraction.** Two signal families from the same trace: evaluative signal via PRM scoring over assistant output plus next-state evidence, and directive signal via teacher log-probs and OPD-style token-level supervision. `combine_loss.py` mixes PPO-style reward advantages with teacher-minus-student token-level advantages; `data_formatter.py` converts samples into Tinker datums.

**Promotion.** Directly into model weights during deployment. Separate rollout and training paths for binary RL, OPD, and combined training, all feeding background optimization rather than text artifacts.

**Scope.** Session-aware policy-learning backend. Many live sessions feed one continuously trained policy; the result is opaque weights, not inspectable memory.

## Source-only systems

These systems are included on weaker evidence — no implementation code inspected locally. They prevent code availability from biasing the taxonomy.

### AgeMem

From the [AgeMem ingest](../sources/agentic-memory-learning-unified-long-term-and-short-term-memory-management.ingest.md) and [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md): AgeMem learns a memory-management policy from interaction trajectories through RL. Trajectories with multiple stages, fixed memory operations (`Add`, `Update`, `Delete`, `Retrieve`, `Summary`, `Filter`), task-completion and context-management rewards. Promotion target is model weights. A clear trajectory-to-weights system, though the concrete storage/runtime implementation is unknown locally.

### Trajectory-Informed Memory Generation

From the [trajectory-informed ingest](../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md): completed execution trajectories are analyzed into strategy, recovery, and optimization tips, then consolidated and retrieved at runtime. Same broad input class as AgeMem and OpenClaw-RL, but the promotion target is inspectable text artifacts with prompt-time retrieval — the direct non-weight counterpart. Implementation details, consolidation prompts, and thresholds are unknown locally.

## What the comparison makes concrete

The systems separate on two axes.

### Axis 1: trace ingestion pattern

**Single-session extension.** Run inside an existing agent runtime, mine the current conversation, reuse the runtime's session representation, write back into markdown artifacts. Napkin and Pi Self-Learning fit here, though Napkin is even looser — it treats the session as an opaque file and delegates extraction to a subprocess agent.

**Cross-agent session aggregator.** Discover and mine session logs from multiple agent runtimes via an external search engine, normalize heterogeneous formats into a common representation, accumulate results in a shared playbook. cass-memory is the only inspected system in this category — it reads session files from Claude Code, Cursor, Codex, Aider, and Pi, normalizes them through `formatRawSession()`, and mines them through a two-phase diary-then-reflection pipeline. Unlike single-session extensions, it operates *after* sessions complete rather than during them, and unlike service backends, it does not own the session format.

**Service-owned trace backend.** Own the message or event schema, accept structured traffic over an API or proxy, separate archive from extraction from downstream processing, support many sessions feeding one backend. OpenViking fits as a memory service; OpenClaw-RL as a policy-learning backend. ClawVault partially fits as a local vault-plus-observer rather than a shared multi-tenant service.

**Trajectory-run pattern.** Learn from repeated runs rather than one live conversation, consume scored generations or completed-task traces, consolidate across many episodes before promotion. Autocontext, AgeMem, and Trajectory-Informed Memory Generation fit here.

### Axis 2: promotion target / substrate class

**Symbolic artifact learning.** Mine traces into inspectable artifacts — observations, tips, playbooks, reports. Keep learned results in a substrate humans can inspect, diff, or curate. Use heuristics, recurrence, judges, or retrieval-time relevance to decide what persists. ClawVault, cass-memory, and Trajectory-Informed Memory Generation fit cleanly; Autocontext for its playbooks and reports; Napkin and Pi Self-Learning in a narrower sense. Their backends differ, but their substrate class is the same.

**Weight learning.** Mine trajectories or next-state signals under a sufficiently strong oracle, re-express as training signals, promote into model weights. AgeMem, OpenClaw-RL, and Autocontext fit here. Autocontext bridges both — symbolic artifacts first, then optionally weights.

## Log formats matter more than the prompts

The biggest difference across systems is not extraction prompt wording but the shape of the source trace:

| System | Source trace |
|---|---|
| Napkin | Opaque pi session file, delegated to subprocess |
| Pi Self-Learning | Pi branch events: messages + tool-result interruptions |
| OpenViking | Own typed message schema with text/context/tool parts, JSONL |
| ClawVault | Assistant turns + incremental OpenClaw session JSONL, noise-stripped |
| cass-memory | Multi-agent session files (Claude Code JSON, Cursor, Codex, Aider, Pi), discovered via `cass` search engine, normalized to markdown |
| Autocontext | Run trajectories from SQLite metrics, competitor outputs, playbooks, hints |
| OpenClaw-RL | Live chat-completion traces + next-state feedback → training samples |
| AgeMem | RL trajectories over memory operations + task/context rewards |
| Trajectory-Informed | Completed execution trajectories → strategy/recovery/optimization tips |

Trace richness constrains what can be learned. Tool calls, statuses, gates, scores, and context snapshots enable operational pattern mining that plain transcripts cannot support. Opaque traces force the miner to trust the upstream runtime. Oracle-aligned traces enable promotion all the way to weights.

## What looks borrowable

- **Explicit boundary triggers.** `agent_end`, `session.commit()`, periodic distill checks — concrete extraction clocks.
- **Narrow extraction schemas.** Pi Self-Learning's `mistakes/fixes` pair; OpenViking's fixed memory categories.
- **Tool-result mining.** Both Pi Self-Learning and OpenViking mine beyond user/assistant prose — blocked commands, permission denials, tool statuses.
- **Separate trigger from promotion.** Systems that keep extraction and ranking/promotion distinct are easier to reason about.
- **Artifact-to-weight handoff.** Autocontext makes explicit what others leave implicit: mined artifacts can be intermediate, not terminal.
- **Substrate choice as design decision.** The same input class can end as notes/observations/tips or as opaque weight updates.

## What remains open

None of the reviewed systems closes the harder KB-learning mutations. They extract and persist candidates well, and some close the loop for scenario-bounded updates, but that is still different from:

- deciding whether two notes should be linked
- synthesizing a better abstraction from several sessions
- retiring a stale learning for principled reasons
- judging whether a mined pattern has explanatory reach or is just a recurring local patch

The concrete update to [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md): **session- or trajectory-derived candidate generation is a solved enough pattern to copy; oracle-backed evaluation is not.** Once you have a strong enough oracle, the same mined traces can feed symbolic artifacts or weight updates. The open problem is not extraction — it is deciding what deserves trust and persistence in open-ended domains.

---

Relevant Notes:

- [continuous learning requires durability, not weight updates](./continuous-learning-requires-durability-not-weight-updates.md) — sharpens: the survey's non-weight cases count as continuous learning because their improvements persist, not because they imitate weight learning
- [Learning substrates, backends, and artifact forms](./learning-substrates-backends-and-artifact-forms.md) — sharpens: separates substrate class from backend and artifact form, clarifying that service memory is usually symbolic-artifact storage rather than a third substrate
- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — sharpens: source-inspected systems now give concrete extraction and promotion loops for workshop artifacts and policy learning; the remaining bottleneck is still evaluation of higher-order mutations
- [a functioning knowledge base needs a workshop layer, not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — grounds the artifact-promotion side of this survey: several systems operationalize workshop-to-library bridges from session traces or run trajectories, even though the weight-learning cases extend beyond that note's domain
- [Napkin](./related-systems/napkin.md) — source-inspected instance: forked-session distill via a subprocess agent and vault templates
- [Pi Self-Learning](./related-systems/pi-self-learning.md) — source-inspected instance: branch-event mining into strict `mistakes`/`fixes` JSON plus scored promotion
- [OpenViking](./related-systems/openviking.md) — source-inspected instance: typed session messages, commit-triggered extraction, and multi-tenant user/agent memory spaces
- [ClawVault](./related-systems/clawvault.md) — source-inspected instance: assistant-turn capture, incremental OpenClaw session observation, scored observation ledgers, and recurrence-based weekly reflection
- [cass-memory](./related-systems/cass_memory_system.md) — source-inspected instance: cross-agent session mining via `cass` search engine, two-phase diary-then-reflection extraction, and confidence-decayed YAML playbook with anti-pattern inversion
- [Autocontext](./related-systems/autocontext.md) — source-inspected instance: run-trajectory mining into playbooks, session reports, JSONL training exports, and optional weight distillation
- [OpenClaw-RL: Train Any Agent Simply by Talking](../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) — source-grounded and code-inspected instance: next-state feedback, PRM scoring, OPD-style supervision, and live background weight updates
- [the fundamental split in agent memory is not storage format but who decides what to remember](./related-systems/agentic-memory-systems-comparative-review.md) — extends: the wider survey places AgeMem and other source-only systems in the broader agency and substrate design space
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: these systems learn or curate policy only as far as their available promotion oracle allows
