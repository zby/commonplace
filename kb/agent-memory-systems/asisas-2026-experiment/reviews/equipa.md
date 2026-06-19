---
description: "EQUIPA review: SQLite-backed agent orchestrator with trace-derived lessons, episodes, prompt variants, and prompt-time read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# EQUIPA

EQUIPA, from `sbknana/equipa`, is a Python multi-agent software-development orchestrator. It stores project context, tasks, agent telemetry, lessons, episodes, prompt-evolution records, graph edges, and session state in a local SQLite database, then assembles role-specific prompts for developer, tester, reviewer, security, planner, evaluator, and related agents.

**Repository:** https://github.com/sbknana/equipa

**Reviewed commit:** [6aa4af8d4505b12ae6877c1068162a8bec8e3d70](https://github.com/sbknana/equipa/commit/6aa4af8d4505b12ae6877c1068162a8bec8e3d70)

**Source directory:** `related-systems/equipa`

## Core Ideas

**The central object is an orchestrated agent team with durable operational state.** The README frames EQUIPA as a system that creates tasks, dispatches specialized agents, monitors them, retries failures, and reports results ([README.md](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/README.md)). The schema backs that with tables for projects, tasks, decisions, session notes, agent runs, lessons, episodes, ForgeSmith runs/changes, graph edges, flow state, actions, and agent sessions ([schema.sql](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/schema.sql)).

**Memory is split into generic lessons and episodic experience.** `lessons_learned` stores active prose lessons with role/error metadata, counters, effectiveness score, and optional embeddings; `agent_episodes` stores task-linked approach summaries, outcomes, error patterns, reflections, Q-values, injection counts, and optional embeddings ([schema.sql](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/schema.sql), [equipa/lessons.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/lessons.py)). ForgeSmith extracts repeated failure lessons from `agent_runs`, while the episode path records reflexion-style task traces and adjusts Q-values after later task outcomes.

**Read-back is prompt assembly, not a separate memory query by the worker.** `build_system_prompt` loads the static common and role prompt, then builds a dynamic suffix containing selected ForgeSmith lessons, selected episodes, task metadata, project context, task-type guidance, initiative context, language guidance, budgets, and retry/compaction context ([equipa/prompts.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/prompts.py)). From the spawned agent's perspective, selected retained memory arrives before action.

**Relevance selection combines identifiers, lexical scoring, optional embeddings, and optional graph ranking.** Lesson selection filters active lessons by role and error type, orders by recurrence and recency, deduplicates, caps, and increments injection counters ([forgesmith.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith.py), [equipa/parsing.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/parsing.py)). Episode retrieval filters by role, project, task type, Q-value, and reflection presence, then scores by recency, keyword overlap, optional Ollama embedding similarity, and optional PageRank over graph edges ([equipa/lessons.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/lessons.py), [equipa/embeddings.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/embeddings.py), [equipa/graph.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/graph.py)).

**Self-improvement has multiple artifact targets.** ForgeSmith mines telemetry into lessons and proposed config/prompt changes; SIMBA synthesizes rules from high-variance episodes and stores them as lessons; GEPA converts episodes into optimization examples, writes versioned role prompt files, records them in `forgesmith_changes`, and can A/B select them at dispatch when the feature flag is enabled ([forgesmith.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith.py), [scripts/forgesmith_simba.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/scripts/forgesmith_simba.py), [forgesmith_gepa.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith_gepa.py)). Defaults matter: ForgeSmith lessons and episodes default on; vector memory, knowledge graph, GEPA A/B testing, and session persistence default off in `DEFAULT_FEATURE_FLAGS` ([equipa/config.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/config.py)).

**Context efficiency is local and pragmatic.** EQUIPA splits static and dynamic prompt sections for provider caching, estimates token load, trims older episode and lesson sections, reduces episode count when prompts are already large, wraps database-derived content as untrusted task input, persists large tool results to disk with previews, and can save bounded session state for later resume ([equipa/prompts.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/prompts.py), [equipa/tool_result_storage.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/tool_result_storage.py), [equipa/sessions.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/sessions.py)). There is no single global activation budget across every dynamic prompt component.

## Artifact analysis

- **Storage substrate:** `sqlite` — The primary retained behavior-shaping state persists in the local TheForge SQLite database: lessons, episodes, agent runs, tasks, project context, graph edges, session rows, ForgeSmith records, flow state, and telemetry. Repo files and artifact files also matter, especially prompt files and persisted tool outputs, but SQLite is the main memory substrate.
- **Representational form:** `prose` `symbolic` `parametric` — Lessons, reflections, prompts, task descriptions, session notes, and tool-output previews are prose; tables, feature flags, role names, task IDs, Q-values, prompt versions, graph edges, JSON state, and MCP schemas are symbolic; optional embeddings and GEPA/DSPy optimization outputs add parametric behavior-shaping state.
- **Lineage:** `authored` `trace-extracted` — Baseline prompts, standing orders, task records, configuration, and orchestrator code are authored; agent runs, reviewer findings, episode reflections, session state, action logs, Q-values, lessons, SIMBA rules, and GEPA prompt variants derive from execution traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Stored context and telemetry advise; injected lessons, episodes, standing orders, and prompts instruct; dispatch and prompt-version selection route; gates, safety rails, tests, sanitizers, and rollback checks validate; embeddings, graph edges, Q-values, and recency rank; ForgeSmith/SIMBA/GEPA learn from traces.

**Lessons.** `lessons_learned` rows carry prose lesson text plus role, error type, source, active flag, recurrence counters, injection counters, effectiveness score, and optional embedding. Lineage is trace-derived when ForgeSmith groups repeated failed `agent_runs`, when reviewer findings are upserted as lessons, and when SIMBA stores synthesized rules. Behavioral authority rises from knowledge to instruction when `format_lessons_for_injection` places active lessons in the next prompt ([forgesmith.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith.py), [equipa/lessons.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/lessons.py)).

**Episodes.** `agent_episodes` rows retain task id, role, task type, project id, approach summary, turns used, outcome, error patterns, reflection, Q-value, optional embedding, and injection count. `record_agent_episode` parses agent output into approach/reflection/error patterns and assigns an initial Q-value; `update_injected_episode_q_values_for_task` rewards or penalizes previously injected episodes after task completion ([equipa/lessons.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/lessons.py)). Selected episodes become advisory prompt instructions under "Past Experience."

**Prompt and standing-order files.** Repo files under `prompts/` and `standing_orders/` are authored prose system-definition artifacts. GEPA can add versioned prompt files and record the evolution in `forgesmith_changes`; `build_system_prompt` can select an evolved prompt for A/B testing and later rollback if observed success is worse than baseline ([equipa/prompts.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/prompts.py), [forgesmith_gepa.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith_gepa.py)).

**Ranking and retrieval state.** Optional embeddings persist as JSON in lesson and episode rows; `lesson_graph_edges` stores co-accessed and similarity edges; PageRank reranking can blend graph influence with similarity scores ([schema.sql](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/schema.sql), [equipa/embeddings.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/embeddings.py), [equipa/graph.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/graph.py)). These artifacts do not instruct directly; they select which prose memories receive prompt authority.

**Session and large-result continuity.** `agent_sessions` rows store bounded JSON state with TTL for cross-cycle restore, and `tool-results` files preserve large outputs while injecting only a preview and file path ([schema.sql](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/schema.sql), [equipa/sessions.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/sessions.py), [equipa/tool_result_storage.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/tool_result_storage.py)). Their authority is continuity support: they shape later prompts without making a permanent general lesson.

Promotion path: agent run -> error pattern -> active lesson -> prompt instruction; agent run -> episode -> Q-value/embedding/graph state -> selected past experience; episode corpus -> SIMBA rule or GEPA prompt variant -> stronger prompt behavior. The path is inspectable through rows and files, but most promotions are system-mediated rather than human-reviewed.

## Comparison with Our System

| Dimension | EQUIPA | Commonplace |
|---|---|---|
| Primary purpose | Orchestrate software agents and improve them from operational traces | Build a typed, agent-operated methodology KB |
| Main substrate | SQLite database, prompt files, runtime artifacts, worktrees | Git-tracked Markdown collections, source snapshots, type specs, generated indexes |
| Memory unit | Lessons, episodes, prompt versions, session state, graph edges | Notes, reviews, instructions, sources, ADRs, indexes, reports |
| Learning path | Trace-derived extraction, Q-value updates, SIMBA rules, GEPA prompt evolution | Authored artifacts under collection/type contracts, validation, semantic review, git history |
| Read-back | Prompt-time push plus MCP/CLI query tools | Mostly explicit pull through `rg`, indexes, links, skills, and review workflows |
| Governance | Feature flags, sanitizers, prompt safety rails, rollback checks, tests | Frontmatter schemas, collection contracts, citations, validation, review gates |

EQUIPA is stronger than Commonplace on automatic read-back. Its worker agents do not need to remember a search procedure before receiving selected lessons, episodes, language guidance, project context, and resume state. That directly attacks the failure mode where knowledge is stored but never enters the action context.

Commonplace is stronger on artifact governance. EQUIPA can trace a lesson or episode through tables and counters, but it does not give each promoted lesson a source-cited Markdown review lifecycle, collection contract, or semantic gate before prompt authority. That makes EQUIPA faster to adapt but easier to overfit or repeat a low-quality reflection.

The main design difference is authority assignment. Commonplace tends to keep retained knowledge advisory until a maintainer or workflow promotes it into an instruction, validator, or indexed artifact. EQUIPA gives active extracted lessons and selected episodes prompt authority as soon as the feature path accepts them.

### Borrowable Ideas

**Prompt-time lesson injection with provenance labels.** Commonplace could test this in review workshops by injecting a few prior review lessons into the next review task. Ready as an experiment only if each injected item carries source path, status, and expiry.

**Separate episodes from generalized lessons.** EQUIPA's split between task episodes and reusable lessons maps well to Commonplace workshop traces versus promoted library notes/instructions. Ready as vocabulary and storage design; runtime push needs a concrete workflow.

**Record which memory was injected before rewarding it.** `_injected_episodes_by_task`, `times_injected`, and post-task Q-value updates create an attribution surface. Commonplace review runs could record which guidance was loaded before a run so later quality signals attach to the right artifact. Needs a run-log schema.

**Keep graph/vector machinery below prose authority.** EQUIPA's embeddings and PageRank influence selection, while the injected object remains readable prose. That is the right direction if Commonplace adds derived search layers.

**Persist large outputs as references.** Replacing large tool outputs with preview-plus-path messages is directly borrowable for high-volume snapshot, review, and test-output workflows. Ready where output artifacts are retained on disk and referenced in context.

**Do not borrow automatic promotion into durable instructions without gates.** EQUIPA's trace-to-prompt path is productive for operational agents, but Commonplace should require human or semantic review before lessons become always-on instructions, validators, or collection rules.

## Write side

**Write agency:** `manual` `automatic` — Operators and agents can author tasks, context, prompts, config, and lessons; automatic paths record agent runs and episodes, extract repeated-failure lessons, update Q-values/injection counters, create graph edges/embeddings, capture sessions, synthesize SIMBA rules, and write GEPA prompt variants.

**Curation operations:** `dedup` `synthesize` `invalidate` `decay` `promote` — Lesson retrieval deduplicates overlapping lessons; ForgeSmith/SIMBA/GEPA synthesize new lessons, rules, and prompt variants from stored traces; GEPA rollback and SIMBA pruning mark ineffective artifacts inactive or reverted; session TTL purges expired session state; Q-values, injection counts, effectiveness scores, and prompt A/B selection promote or demote memory salience. I did not find an automatic in-place `evolve` path for an existing lesson's semantic content beyond counters/status.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `trajectories` — Raw signals include agent run telemetry, outputs, reviewer findings, episode reflections, action/tool logs, session state, injected-episode outcomes, and ForgeSmith/SIMBA/GEPA training inputs.

**Learning scope:** `per-task` `per-project` `cross-task` — Episodes are task-linked; retrieval and sessions are role/project/task scoped; lessons and prompt variants can influence future tasks for a role or project.

**Learning timing:** `online` `staged` — Prompt read-back and telemetry capture happen during orchestration; Q-value/session updates happen between cycles; ForgeSmith, SIMBA, and GEPA are staged improvement passes.

**Distilled form:** `prose` `symbolic` `parametric` — Distillation yields prose lessons, episode reflections, SIMBA rules, evolved prompt text, symbolic metadata/counters/graph edges/prompt versions, and optional embeddings or optimizer outputs.

ForgeSmith extracts lessons by grouping repeated failed `agent_runs` and generating sanitized lesson text. Episode recording parses task output into approach/reflection/error-pattern fields and later adjusts Q-values for episodes that were actually injected. SIMBA uses Claude to contrast successful and failed episodes into behavioral rules stored as lessons, then evaluates/prunes rules by observed before/after success rates. GEPA uses episode examples to evolve role prompts, stores versioned prompt files, and records A/B evidence in `forgesmith_changes` ([forgesmith.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith.py), [equipa/lessons.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/lessons.py), [scripts/forgesmith_simba.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/scripts/forgesmith_simba.py), [forgesmith_gepa.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/forgesmith_gepa.py)).

Survey fit: EQUIPA is a deploy-time trace-to-artifact system. It strengthens the pattern where raw execution traces become readable lessons, episodic examples, ranking state, and prompt-version artifacts. Its unresolved pressure is governance: several trace-derived artifacts can gain prompt authority faster than their provenance and review controls mature.

## Read-back

**Read-back:** `both` — Worker agents receive selected lessons, episodes, context, and optional resume state during prompt construction, while MCP tools expose lessons, run logs, project context, and session notes for explicit host or human queries.

**Read-back signal:** `identifier` `inferred / lexical` `inferred / embedding` — Prompt-time push targets role, error type, project id, and task type identifiers; episode ranking adds keyword overlap; optional vector memory adds embedding similarity. Optional graph PageRank is ranking over retained relation state, not a separate targeting signal.

**Faithfulness tested:** `no` — EQUIPA tracks success, Q-values, injection counts, prompt versions, and rollback/pruning signals, but I did not find item-level WITH/WITHOUT ablation proving that a specific injected memory changed a specific action.

For the acting worker, read-back is pre-invocation: `build_system_prompt` decides what memory enters the dynamic suffix before the agent runs. Lesson selection is active-only, role/error filtered, deduplicated, capped, and counted. Episode selection is role/project/task scoped, Q-value filtered, reflection-required, and reranked by recency, lexical overlap, optional embeddings, and optional graph influence. Session persistence can prepend resume state when enabled, but that feature defaults off ([equipa/prompts.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/prompts.py), [equipa/config.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/config.py), [equipa/sessions.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/sessions.py)).

The pull path is the MCP server and CLI-adjacent query surface. `equipa_lessons`, `equipa_agent_logs`, `equipa_project_context`, and `equipa_session_notes` let a host or user fetch retained memory explicitly; `equipa_dispatch` and task-creation tools can also route work into the orchestrator ([equipa/mcp_server.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/mcp_server.py)). These tools provide knowledge context rather than automatic prompt injection for the querying agent.

Authority at consumption is mostly advisory instruction. Injected lessons and episodes are not hard gates, but they appear in the system prompt before the agent decides what to do. GEPA prompt variants carry stronger system-definition authority because they can replace role instructions during A/B dispatch. Effective behavioral attribution remains approximate without per-memory ablation or post-action audit.

## Curiosity Pass

**The everyday memory is ordinary prose despite advanced options.** Embeddings, graph ranking, SIMBA, and GEPA exist, but the common active path is short lesson and episode prose inserted into the next prompt.

**Default feature flags matter.** ForgeSmith lessons and episodes default on, while vector memory, knowledge graph, GEPA A/B testing, and session persistence default off. The implemented design is broader than the default runtime behavior.

**SIMBA has a source-label wrinkle.** `store_rules` writes rules with `source = 'simba_generated'`, while `get_active_simba_rules` loads `source = 'simba' OR source = 'forgesmith'` ([scripts/forgesmith_simba.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/scripts/forgesmith_simba.py), [equipa/lessons.py](https://github.com/sbknana/equipa/blob/6aa4af8d4505b12ae6877c1068162a8bec8e3d70/equipa/lessons.py)). That does not remove the SIMBA storage path, but it means one rule-scoring retrieval path may miss rules from the inspected script unless another path normalizes source labels.

**Many memory failures are deliberately non-fatal.** Embedding, graph, telemetry, and episode write failures usually log and continue. That protects orchestration, but memory quality can silently degrade unless logs and counters are reviewed.

**SQLite makes the system inspectable but not editorially reviewed.** The rows are durable and queryable; they do not carry the richer artifact lifecycle that Commonplace uses for review status, citations, replacement history, and semantic QA.

## What to Watch

- Whether SIMBA source labels are unified so generated rules consistently participate in later scoring and injection.
- Whether lesson and episode provenance becomes item-level enough to audit a prompt-injected lesson back to exact runs, outputs, or findings.
- Whether GEPA prompt variants gain human approval, diff review, or semantic QA before A/B activation.
- Whether vector memory and graph ranking move from optional features to default behavior, changing read-back from mostly symbolic/lexical selection to hybrid retrieval.
- Whether evaluation grows from success-rate, Q-value, and prompt-version telemetry into per-memory faithfulness tests.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../../trace-derived-learning-techniques-in-related-systems.md) - places: EQUIPA turns agent run traces into lessons, episodes, prompt variants, and ranking state.
- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: EQUIPA's distinctive move is prompt-time read-back rather than storage alone.
- [Activate Behavior-Changing Memory Before The Mistake](../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: lessons and episodes are selected before the next worker action.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: EQUIPA's rows, prompt files, embeddings, graph edges, and sessions differ by substrate, form, lineage, and authority.
- [Deploy-time learning is the missing middle](../../../notes/deploy-time-learning-is-the-missing-middle.md) - exemplifies: EQUIPA adapts deployed agent behavior through retained prose and symbolic artifacts.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - distinguishes: logs, traces, session notes, project context, and queried lessons can serve as evidence or context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - distinguishes: injected lessons, selected episodes, prompt files, dispatch metadata, and GEPA variants can instruct, select, or configure behavior.
