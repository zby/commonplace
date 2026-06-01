---
description: "EQUIPA review: SQLite-backed multi-agent orchestrator with trace-derived lessons, episodic memory, graph reranking, and prompt-level read-back"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# EQUIPA

EQUIPA, from sbknana's `equipa` repository, is a Python multi-agent software-development orchestrator. It stores tasks, project context, agent run telemetry, lessons, episodes, graph edges, prompt-evolution records, and session state in a local SQLite database, then builds role-specific prompts for developer, tester, reviewer, security, planner, evaluator, and other agents.

**Repository:** https://github.com/sbknana/equipa

**Reviewed commit:** [6aa4af8d4505b12ae6877c1068162a8bec8e3d70](https://github.com/sbknana/equipa/commit/6aa4af8d4505b12ae6877c1068162a8bec8e3d70)

**Last checked:** 2026-06-01

## Core Ideas

**The orchestrator is a database-backed agent team, not just a prompt wrapper.** The root README presents EQUIPA as a system that breaks work into tasks, dispatches specialized agents, monitors them, retries failures, and records outcomes (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/README.md). The schema confirms that the durable control surface is a SQLite database with projects, tasks, decisions, session notes, agent runs, lessons, episodes, flow revisions, config versions, and agent sessions (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/schema.sql).

**Memory is split between generic lessons and episodic traces.** `lessons_learned` stores reusable prose lessons with role, error type, source, counters, active state, and optional embeddings; `agent_episodes` stores task-specific approach summaries, outcomes, error patterns, reflections, Q-values, injection counts, and optional embeddings (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/schema.sql, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/lessons.py). The generic lesson path is mostly pattern extraction from agent runs and review findings; the episodic path is closer to MemRL, where remembered episodes receive reward-like Q-value updates after later tasks succeed or fail.

**Read-back happens during prompt assembly.** `build_system_prompt` builds a static cacheable prefix from common, role, and standing-order prompts, then appends dynamic material: ForgeSmith lessons, relevant episodes, task metadata, project context, task-type guidance, initiative context, language guidance, budgets, and retry/compaction context (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/prompts.py). From the acting agent's perspective, this is push activation: the orchestrator decides which retained material enters the prompt before the agent starts.

**Relevance selection combines symbolic filters, recency, Q-values, keyword overlap, optional embeddings, and optional graph reranking.** Episode retrieval starts from role/project/task-type filters and Q-value thresholds, then scores candidates by recency and keyword overlap. If vector memory is enabled, it blends in Ollama embedding similarity; if the knowledge graph is enabled, it reranks with PageRank over co-accessed and similarity edges (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/lessons.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/embeddings.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/graph.py). Lesson retrieval for ForgeSmith lessons is simpler: role/error filters, deduplication, and a capped list injected into the prompt.

**Self-improvement has several artifact targets.** ForgeSmith mines `agent_runs` into `lessons_learned`, stores proposed changes in `forgesmith_changes`, and can run SIMBA and GEPA phases (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith.py). SIMBA contrasts successful and failed episodes, asks Claude for short tactical rules, validates them, and stores them as lessons (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/scripts/forgesmith_simba.py). GEPA converts episodes into DSPy examples, evolves role prompt instructions, writes versioned prompt files, records the evolution in `forgesmith_changes`, and optionally A/B selects the evolved prompt at dispatch (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith_gepa.py).

**Context efficiency is engineered at several levels, but not uniformly governed.** EQUIPA uses static/dynamic prompt splitting for provider prompt caching, trims old episodes and lessons when token estimates exceed targets, caps injected episodes, truncates formatted episode summaries, persists large tool results to disk with preview messages, and can save/restore bounded session state (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/prompts.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/tool_result_storage.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/sessions.py). The controls are pragmatic and code-level, but there is no single global context budget across all read paths and host interactions.

## Artifact analysis

**TheForge SQLite database.** The storage substrate is the local SQLite database identified by `THEFORGE_DB` and managed from `schema.sql` through `equipa/db.py` (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/schema.sql, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/db.py). The representational form is mixed: symbolic tables and fields, prose task/session/lesson/reflection text, JSON blobs, and optional embedding vectors serialized as JSON. Lineage is runtime operational state: user-created tasks, agent outputs, orchestrator telemetry, reviewer findings, generated lessons, and derived self-improvement records. Behavioral authority ranges from knowledge artifact authority for project context and logs to system-definition authority for active lessons, prompt-version selection, graph/ranking state, session resume context, and dispatch decisions.

**Lessons learned.** The storage substrate is `lessons_learned` rows with role, error type, source, active flag, counters, effectiveness score, and optional embedding (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/schema.sql). The representational form is prose plus symbolic metadata and optional distributed-vector state. Lineage is trace-derived or review-derived: ForgeSmith generates lessons from repeated `agent_runs` error summaries, code/security review findings can be upserted as developer lessons, and SIMBA can synthesize rules from contrasted episodes (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/loops.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/scripts/forgesmith_simba.py). Behavioral authority becomes system-definition artifact authority when `format_lessons_for_injection` puts active lessons into an agent's prompt; the lesson text is also a knowledge artifact when queried through MCP or read by a human.

**Agent episodes.** The storage substrate is `agent_episodes` rows. The representational form is structured symbolic fields plus prose approach summaries, reflections, and error patterns; optional embeddings add a distributed-vector retrieval lane (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/lessons.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/embeddings.py). Lineage is per-agent-run trace extraction: result text is parsed into approach, reflection, failure class, outcome, turns, and Q-value; later task outcomes update Q-values for episodes that were injected. Behavioral authority is advisory system-definition authority at read-back because selected episodes become "Past Experience" in the prompt, while their stored rows also serve as audit and learning-input knowledge artifacts.

**Prompt files, standing orders, and GEPA prompt versions.** The storage substrate is repo files under `prompts/` and `standing_orders/`, plus versioned prompt files created by GEPA and metadata in `forgesmith_changes` (https://github.com/sbknana/equipa/tree/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/prompts, https://github.com/sbknana/equipa/tree/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/standing_orders, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith_gepa.py). The representational form is prose instruction with symbolic file naming, protected-section checks, diff-ratio validation, and A/B version labels. Lineage is split between authored baseline role prompts and trace-derived GEPA candidate prompts trained from episode examples. Behavioral authority is high: these files are system-definition artifacts that define role behavior before task-specific context is added.

**Knowledge graph and embeddings.** The storage substrate is `lesson_graph_edges`, lesson/episode `embedding` columns, and live Ollama embedding calls (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/schema.sql, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/graph.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/embeddings.py). The representational form is mixed symbolic graph edges and distributed-vector embeddings. Lineage derives from stored lesson/episode text and co-access events during prompt assembly. Behavioral authority is ranking influence: graph and vector state do not directly instruct agents, but they decide which prose memories get prompt authority.

**Agent sessions and large tool-result references.** The storage substrate is `agent_sessions` rows, `.forge-state.json`, soft checkpoint files, and session-local `tool-results` files (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/sessions.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/tool_result_storage.py). The representational form is JSON state, prose resume prompts, and file references. Lineage is in-flight trace capture from soft checkpoints, forge state, and recent tool calls, with a 14-day TTL and 32 KB cap for session state. Behavioral authority is continuity support: restored session state is pushed into the next dispatch as context, while persisted tool outputs reduce context volume by turning large blobs into pointers.

**MCP and CLI surfaces.** The storage substrate is Python handler code and JSON schemas in `equipa/mcp_server.py` plus CLI/orchestrator scripts (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/mcp_server.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forge_orchestrator.py). The representational form is symbolic tool schema and executable Python. Lineage is authored system code. Behavioral authority is system-definition authority over task creation, dispatch, lesson/log/context queries, and session-note access; it is the integration path through which a host assistant can create work and inspect retained memory.

**Promotion path.** EQUIPA has several promotions: agent run -> extracted lesson -> prompt-injected instruction; agent run -> episode -> embedding/Q-value -> prompt-injected past experience; reviewer finding -> developer lesson -> prompt-injected prevention rule; episode corpus -> SIMBA rule or GEPA prompt version -> future prompt behavior. These paths cross from trace evidence to prose or mixed system-definition artifacts. They are reviewable because the intermediate records are stored, but most promotions are automated or script-mediated rather than human-approved.

## Comparison with Our System

| Dimension | EQUIPA | Commonplace |
|---|---|---|
| Primary purpose | Orchestrate software agents and improve them from operational traces | Build a typed, agent-operated methodology KB |
| Main substrate | SQLite database, prompt files, runtime artifacts, worktrees | Git-tracked Markdown collections, type specs, generated indexes, source snapshots |
| Memory unit | Lessons, episodes, prompt versions, session state, graph edges | Notes, reviews, instructions, sources, ADRs, indexes, reports |
| Learning path | Trace-derived extraction, Q-value updates, SIMBA rules, GEPA prompt evolution | Agent-authored artifacts under collection/type contracts, validation, reviews, and git lifecycle |
| Activation | Prompt-time push with relevance scoring and feature flags | Mostly explicit pull through `rg`, indexes, links, skills, and review workflows |
| Governance | Sanitizers, feature flags, prompt safety rails, A/B rollback checks, tests | Frontmatter schemas, collection contracts, validation, semantic review gates, citations |

EQUIPA is stronger than Commonplace on automatic activation. Its orchestrator does not wait for the acting agent to remember a search command; it injects lessons, episodes, project context, language guidance, budgets, and resume state before action. That directly addresses the storage-to-context failure mode that Commonplace still handles mostly through agent discipline.

Commonplace is stronger on library governance and provenance. EQUIPA can trace a lesson back to tables, sources, counters, and sometimes error signatures, but it does not maintain Markdown-quality source citations, collection contracts, review status, or semantic validation before a lesson becomes prompt authority. The result is fast deploy-time learning with weaker artifact curation.

The deepest design difference is authority assignment. Commonplace tends to keep knowledge artifacts advisory until an agent or maintainer promotes them through an explicit type, instruction, validator, or workflow. EQUIPA gives extracted lessons and selected episodes prompt authority immediately when their feature flag is on. That makes it more adaptive, but also raises the risk that a misleading reflection, bad reviewer finding, or overfit SIMBA rule becomes a repeated behavioral constraint.

Read-back: push, with engineered relevance-gated activation for lessons and episodes during prompt construction; MCP lesson/log/context queries also provide a pull path for hosts and humans.

### Borrowable Ideas

**Prompt-time lesson injection with explicit provenance labels.** Commonplace could add a narrow, review-workshop-only memory injector that loads a few prior review lessons into the next review task. Ready as an experiment if each injected item carries source path, review status, and expiry.

**Separate episodic examples from generalized lessons.** EQUIPA's split between `agent_episodes` and `lessons_learned` is useful. Commonplace could mirror it as workshop traces versus promoted notes/instructions, with different activation rules for each. Ready now as vocabulary and storage design; runtime push needs a concrete workflow.

**Track whether a memory was injected before rewarding it.** `_injected_episodes_by_task` and post-task Q-value updates are a small but important control surface. Commonplace review bundles could record which guidance was loaded before a run so later quality signals can attach to the right artifact. Needs a run-log schema.

**Use graph and vector signals only as ranking influence.** EQUIPA keeps embeddings and PageRank below the prose authority layer. That is a sensible Commonplace-compatible pattern: retrieval machinery can select candidates without becoming the canonical knowledge.

**Do not borrow automatic promotion into durable instructions without gates.** EQUIPA's trace-to-prompt loop is productive for operational agents, but Commonplace should require human or semantic-gate review before lessons become always-on instructions, validators, or collection rules.

**Persist large tool outputs as pointers.** The tool-result storage path is a direct context-efficiency idea: preserve the full artifact on disk, inject only a preview and path. Ready for high-volume review or snapshot workflows.

## Trace-derived learning placement

**Trace source.** EQUIPA qualifies as trace-derived learning. Raw traces include `agent_runs` telemetry, agent output text, reviewer findings, error summaries, `agent_episodes` reflections, Q-values, in-flight session state, recent tool calls, and ForgeSmith/SIMBA/GEPA analysis inputs (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/db.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/lessons.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/sessions.py).

**Extraction.** Extraction has several oracles. ForgeSmith uses repeated failures and error summaries to generate generic lessons; reviewer findings become developer lessons; episode recording parses approach/reflection/error patterns from agent output and assigns Q-values from outcome; SIMBA uses Claude to contrast successful and failed episodes into rules; GEPA uses DSPy optimization over episode examples and success labels to produce evolved prompt instructions (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/scripts/forgesmith_simba.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith_gepa.py).

**Four fields.** Raw traces persist in SQLite rows, JSON state, and artifact files; distilled artifacts persist as lessons, episodes with adjusted Q-values, graph edges, embeddings, versioned prompt files, and `forgesmith_changes`. The representational form moves from prose traces and symbolic telemetry into prose rules/lessons, symbolic routing and scoring metadata, distributed-vector embeddings, and optionally evolved prompt files. Lineage is visible at table/file granularity, but not always at item-level provenance inside a lesson. Behavioral authority rises from knowledge artifact evidence in traces to system-definition authority when lessons, episodes, or prompt versions are injected or selected.

**Scope and timing.** Scope is mostly project, role, task type, and recent-window scoped. Timing is mixed: prompt read-back is online at dispatch, episode Q-value updates happen after tasks, ForgeSmith/SIMBA/GEPA are staged improvement passes, and session capture/restore supports continuity across cycles.

**Survey placement.** EQUIPA belongs in the deploy-time trace-to-artifact family. It strengthens the survey claim that agent memory systems often combine several promotion targets: readable lessons, episodic examples, ranking state, and prompt-version artifacts. It also shows the main governance pressure: trace-derived artifacts can gain high prompt authority faster than their provenance and review controls mature.

## Read-back placement

**Direction.** Read-back is both push and pull. Acting agents receive memory by push during `build_system_prompt`; hosts and humans can pull lessons, logs, context, and session notes through MCP tools (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/prompts.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/mcp_server.py).

**Trigger and relevance signal.** Lesson injection is feature-flagged and role/error filtered, then deduplicated and capped. Episode injection is feature-flagged and relevance-gated by project, role, task type, Q-value threshold, recency, keyword overlap, optional embedding similarity, and optional graph reranking (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/config.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/lessons.py). This is stronger than unconditional always-load and justifies `push-activation`.

**Timing relative to action.** Memory is loaded before agent work begins. Resume state can also be inserted on loop entry before redispatch after prior capture (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/loops.py). Post-task Q-value updates and ForgeSmith passes affect future dispatches, not the just-finished action.

**Selection, scope, and complexity.** Selection is bounded by lesson limits, episode limits, token-estimate trimming, summary truncation, and optional graph/vector ranking. Complexity can still accumulate because the dynamic suffix also includes task metadata, project context, language guidance, initiative context, budgets, retry history, and arbitrary extra context. EQUIPA has local context controls, not a single audited activation budget.

**Authority at consumption.** Injected lessons and episodes are presented in the system prompt as derived task input. They are not hard gates, but they have advisory instruction force because the acting agent receives them before deciding what to do. GEPA prompt versions have stronger system-definition authority because they can replace role instructions in A/B dispatch.

**Faithfulness.** EQUIPA tracks success, Q-values, injection counts, prompt versions, and rollback checks, but I did not find an item-level WITH/WITHOUT ablation proving that a specific injected lesson caused a specific behavior change. Structural activation is implemented; effective behavioral attribution remains approximate.

**Other consumers.** The MCP server exposes lessons, agent logs, project context, and session notes to host assistants or humans. ForgeSmith, SIMBA, GEPA, graph reranking, and A/B rollback are additional consumers of the same retained traces.

## Curiosity Pass

**The most consequential memory is ordinary prose in a database.** Despite embeddings, PageRank, and GEPA, the common path is still short natural-language lessons and episode reflections pushed into the next prompt.

**There is a source-name wrinkle around SIMBA rules.** `store_rules` writes SIMBA-generated rules with `source = 'simba_generated'`, while `get_active_simba_rules` looks for `source = 'simba' OR source = 'forgesmith'` (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/scripts/forgesmith_simba.py, https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/lessons.py). That does not negate the broader lesson-injection path, but it means the specific SIMBA-rule scoring bonus may not see rules stored by the inspected SIMBA script unless another path normalizes the source.

**The system is aggressive about not letting telemetry failures crash orchestration.** Many memory writes and retrieval enhancements catch errors and continue. That is operationally sane, but it can hide memory quality degradation unless logs are monitored.

**GEPA is present but not default.** `gepa_ab_testing` defaults to false, while ForgeSmith lessons and episodes default true (https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/config.py). The everyday memory story is lesson and episode injection; prompt evolution is a heavier optional path.

**SQLite gives inspectability but not curation.** Rows are visible and queryable, yet they do not carry the same editorial lifecycle as Commonplace artifacts. The storage substrate is local and durable, but review state is much thinner.

## What to Watch

- Whether SIMBA source labels are unified so generated rules consistently participate in later scoring and injection. That determines whether the rule-learning loop is just storage or active behavior.
- Whether lesson and episode provenance becomes item-level rather than table/file-level. That is the main missing bridge from fast trace learning to auditable memory.
- Whether GEPA prompt versions gain stronger human approval, diff review, or semantic QA before A/B activation. That matters because prompt files carry high system-definition authority.
- Whether vector memory and knowledge graph features remain optional or become default. That changes activation from mostly symbolic filtering to hybrid retrieval/ranking.
- Whether session persistence becomes default. If it does, cross-cycle state shifts from recovery aid to routine read-back path and needs more authority labeling.
- Whether evaluation grows from run-level success/Q-value updates to per-memory faithfulness tests. That would make the activation claims much stronger.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: EQUIPA turns agent run traces into lessons, episodes, prompt versions, and ranking state.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: EQUIPA actively pushes selected memory into future prompts rather than leaving agents to search.
- [Activate Behavior-Changing Memory Before The Mistake](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: lessons and episodes are selected before the next action.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: EQUIPA's database rows, prompt files, graph edges, embeddings, and sessions differ by substrate, form, lineage, and authority.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - exemplifies: EQUIPA adapts deployed agent behavior through readable and symbolic artifacts, not only weights.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: logs, traces, session notes, and queried lessons can serve as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: injected lessons, selected episodes, prompt files, routing metadata, and GEPA variants can instruct, select, or configure behavior.
