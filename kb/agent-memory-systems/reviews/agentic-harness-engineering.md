---
description: "Agentic Harness Engineering review: trace-derived harness evolution loop that turns benchmark rollouts into pushed analysis, manifests, and git-tracked agent harness edits"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# Agentic Harness Engineering

Agentic Harness Engineering, from the `china-qijizhifeng/agentic-harness-engineering` repository, is an observability-driven system for improving coding agents by evolving the harness around a fixed base model. It evaluates a NexAU coding agent on benchmark tasks, distills rollouts into analysis artifacts, gives those artifacts to an evolution agent, and commits changes to prompts, tools, middleware, skills, sub-agents, and memory files. The central memory mechanism is not user preference recall. It is a trace-derived feedback loop that turns prior agent behavior into durable, git-tracked harness components.

**Repository:** https://github.com/china-qijizhifeng/agentic-harness-engineering

**Reviewed commit:** [cb6ea4e0055d60946424e8c608b4265ffaf99a09](https://github.com/china-qijizhifeng/agentic-harness-engineering/commit/cb6ea4e0055d60946424e8c608b4265ffaf99a09)

**Last checked:** 2026-06-01

## Core Ideas

**The retained unit is the harness, not a model weight update.** The README frames AHE as holding the base model fixed while evolving system prompts, tool descriptions, tool implementations, middleware, skills, sub-agents, and long-term memory. `evolve.py` initializes a workspace by copying the source agent config, creating a git repo, committing the baseline, and then committing each later iteration's workspace changes ([README.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/README.md), [evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/evolve.py)).

**Evaluation emits traces before it emits lessons.** The main loop runs `harbor run` over Terminal-Bench-style tasks with a NexAU agent config, then reads verifier rewards, exception files, and NexAU in-memory traces to compute pass/fail statistics, behavior counts, timeout signals, and cross-iteration task history. Raw traces remain in the benchmark run directories as evidence for later drill-down ([evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/evolve.py), [trace_converter.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/trace_converter.py)).

**Agent Debugger is a trace-to-report distillation layer.** When enabled, `run_parallel_adb_ask` groups task rollouts, labels traces as pass/fail/timeout, includes verifier output for failures, calls `adb ask`, and writes `input/analysis/overview.md` plus per-task detail reports. The evolution prompt explicitly tells the agent to read the generated analysis first and use raw traces only when the reports are insufficient ([evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/evolve.py), [agents/evolve_agent/evolve_prompt.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/agents/evolve_agent/evolve_prompt.md)).

**Read-back is staged: pushed summaries, pullable traces.** `build_evolution_query` pushes current evaluation results, task classifications, cross-iteration diffs, debugger overview text, historical trends, best-ever snapshots, stability analysis, and change attribution into the evolution agent's next prompt. It also points to detail files and raw traces for deliberate lookup. The acting evolution agent therefore receives a scoped memory packet before choosing changes, while retaining a pull path into deeper evidence ([evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/evolve.py)).

**Changes are supposed to be falsifiable.** The evolution prompt requires every change to name failure evidence, root cause, targeted fix, predicted impact, and risk tasks. A later iteration loads the previous `change_manifest.json`, compares predictions with actual flips and regressions, and writes `change_evaluation.json` so ineffective or harmful changes are visible to the next evolution agent ([agents/evolve_agent/evolve_prompt.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/agents/evolve_agent/evolve_prompt.md), [evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/evolve.py)).

**The repo also ships a portable harness skill.** `skills/agentic-harness-engineering` packages the HARNESS.md vocabulary, audit flow, manifest generation, verification scripts, profiles, and rollback guidance as a reusable skill for other agents. That skill is itself a retained system-definition artifact: it teaches agents to treat harness changes as component-level, evidence-backed, and reviewable ([skills/agentic-harness-engineering/SKILL.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/skills/agentic-harness-engineering/SKILL.md), [skills/agentic-harness-engineering/references/HARNESS.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/skills/agentic-harness-engineering/references/HARNESS.md)).

## Artifact analysis

- **Storage substrate:** `repo` — A filesystem workspace under the experiment directory, backed by a local git repository initialized and committed by `evolve.py`
- **Representational form:** `mixed` — Mixed prose, symbolic config, and executable code: `systemprompt.md`, `code_agent.yaml`, tool descriptions, tools, middleware, skills, sub-agents, and `LongTermMEMORY.md`

**Harness workspace.** Storage substrate: a filesystem workspace under the experiment directory, backed by a local git repository initialized and committed by `evolve.py`. Representational form: mixed prose, symbolic config, and executable code: `systemprompt.md`, `code_agent.yaml`, tool descriptions, tools, middleware, skills, sub-agents, and `LongTermMEMORY.md`. Lineage: copied from `agents/code_agent_simple`, patched from experiment config, then edited by the evolution agent from trace-derived evidence and committed/tagged per iteration. Behavioral authority: system-definition artifacts for the evaluated code agent because these files define instructions, tools, middleware hooks, loaded skills, delegation surfaces, and always-available or registered memory surfaces.

**Raw rollout traces and verifier outputs.** Storage substrate: benchmark run directories under `runs/iteration_NNN/input/benchmark/{timestamp}/{task}/`, with NexAU trace JSON, runtime logs, verifier rewards, and exception files. Representational form: mixed symbolic/prose event traces, logs, rewards, and stack/test output. Lineage: generated by Harbor rollouts of the current workspace in E2B/local sandbox contexts, normalized by the trace converter and read by statistics/debugger code. Behavioral authority: knowledge artifacts as evidence; they gain system-definition authority only when distilled into analysis, manifests, or harness edits.

**Debugger analysis reports.** Storage substrate: markdown files under `runs/iteration_NNN/input/analysis/overview.md` and `detail/{task}.md`. Representational form: prose reports with symbolic trace labels, pass/fail counts, verifier excerpts, and paths back to raw traces. Lineage: trace-derived from selected rollout traces plus verifier outputs through `adb ask`; bounded by `max_tasks`, per-task mode, retry policy, and the debug/summary prompt templates. Behavioral authority: knowledge artifacts when read as diagnosis; system-definition artifacts when `build_evolution_query` injects the overview into the evolution agent prompt as the default basis for changes.

**Evolution query, history, and attribution records.** Storage substrate: generated markdown/json/yaml files such as `evolution_history.md`, `task_history.json`, `iteration_scores.yaml`, `change_manifest.json`, and `change_evaluation.json`. Representational form: symbolic metrics plus prose summaries and predictions. Lineage: derived from current stats, cross-iteration diffs, prior manifests, debugger overviews, variant results, and best-ever snapshots. Behavioral authority: system-definition artifacts for the evolution agent because the query and prompt tell it what failures to prioritize, what changes to keep or roll back, and which workspace path to edit.

**Evolve agent traces and summaries.** Storage substrate: files under each iteration's `evolve/` directory, including `evolve_trace.json`, cleaned tracer snapshots, and `evolve_summary.md`. Representational form: message traces and prose summaries. Lineage: generated by the evolution agent while consuming the pushed query and pullable run artifacts. Behavioral authority: mostly knowledge artifacts for audit and future attribution; summaries become system-definition inputs when appended to `evolution_history.md`.

**HARNESS.md skill package.** Storage substrate: a repo directory under `skills/agentic-harness-engineering/`. Representational form: prose skill instructions, JSON schema, profile YAML, and validation/manifest scripts. Lineage: authored from the AHE paper and local harness conventions, not automatically mined from benchmark traces in the inspected code. Behavioral authority: system-definition artifact for agents that load the skill, because it prescribes component categories, manifest fields, audit checks, and rollback/verification behavior.

The promotion path is trace -> analysis report -> evolution query -> workspace edit -> git commit -> next evaluation. A second path runs manifest prediction -> later change attribution -> keep/rollback guidance. The strongest design feature is that the behavior-shaping artifact remains inspectable as files and commits. The weaker point is provenance continuity: a final harness edit may cite failure evidence in a manifest, but the code does not enforce durable links from each edited line back to specific trace spans, debugger report sections, or verifier outputs.

## Comparison with Our System

| Dimension | Agentic Harness Engineering | Commonplace |
|---|---|---|
| Primary purpose | Improve benchmark pass@1 by evolving a coding-agent harness | Maintain a typed methodology KB for future agents and maintainers |
| Raw evidence | Rollout traces, verifier output, logs, pass/fail histories | Sources, notes, reviews, work artifacts, validation and review outputs |
| Canonical retained unit | Git-tracked harness workspace plus manifests, analysis, and scores | Git-tracked markdown artifacts with type specs, links, schemas, and status |
| Learning loop | Trace-derived analysis drives edits; next evaluation falsifies them | Source-grounded writing, review, validation, and workshop-to-library promotion |
| Read-back | Pushed iteration packet plus pullable reports/traces | Mostly pull through search/indexes/links, plus instructions and generated context where configured |
| Governance | Git commits, manifests, prediction checks, pass/fail metrics, validation scripts | Collection contracts, schemas, deterministic validation, semantic review, git history |

AHE is unusually close to Commonplace because it treats externalized files as the primary behavior surface. It does not try to hide lessons inside model weights. A failing rollout can become a prose diagnosis, a manifest prediction, a middleware file, a tool description, or a long-term memory entry, all of which remain inspectable and revertible.

The main divergence is objective and artifact granularity. AHE optimizes benchmark performance and therefore accepts operational artifacts whose authority comes from future pass/fail attribution. Commonplace optimizes durable methodology and therefore asks each artifact to explain its claim, type, links, and review state. AHE can move faster because a hypothesis only needs to survive the next evaluation; Commonplace moves slower because a promoted note must stay meaningful outside the run that produced it.

**Read-back:** `both` — With instance-targeted engineered push. The evolution agent receives a generated, scoped iteration packet keyed to the current benchmark iteration before acting, and it can pull detail reports or raw traces when needed. The evaluated code agent mostly receives whatever harness components are registered or always loaded in its workspace

### Borrowable Ideas

**Treat harness edits as falsifiable hypotheses.** A Commonplace analogue would require generated instructions, validators, or routing changes to carry predicted effects and risk surfaces, then compare them against later review/validation outcomes. Ready for review-system and instruction changes.

**Keep raw evidence, distilled diagnosis, and promoted behavior separate.** AHE's run directories, analysis markdown, manifests, and workspace commits make the promotion ladder visible. Commonplace already has sources, work artifacts, notes, and validation; AHE suggests making the intermediate diagnostic layer more explicit for agent-run reviews. Ready as a workshop convention.

**Push a bounded iteration packet instead of asking the agent to rediscover everything.** `build_evolution_query` is a frontloaded context packet assembled from known state. Commonplace could generate task-specific packets from validation failures, unresolved review comments, and relevant notes before an agent starts a maintenance task. Ready where inputs are deterministic.

**Use change attribution as a memory invalidation signal.** AHE does not just record that a change happened; it later records whether predicted fixes and risks materialized. Commonplace could use similar attribution records to retire or demote advice that repeatedly fails review. Needs a clearer mapping from note/instruction changes to observable outcomes.

**Expose the harness component taxonomy as an authoring constraint.** HARNESS.md's seven component types help the evolution agent choose the right authority level: prompt, tool description, tool implementation, middleware, skill, sub-agent, or memory. Commonplace could borrow the "which behavior surface is this really?" question for system-definition artifacts. Ready as review guidance.

## Trace-derived learning placement

**Trace source.** AHE qualifies as trace-derived learning. The raw signal is benchmark execution: NexAU step traces, tool calls, model messages, runtime logs, verifier reward files, exception files, and optional test output. The trace converter normalizes in-memory tracer dumps into debugger-friendly JSON, and the main loop groups rollouts by task and outcome.

**Extraction.** Extraction is staged. First, `compute_stats`, behavior-stat extractors, and cross-iteration diff code turn run directories into pass/fail metrics, task histories, and stability views. Second, Agent Debugger prompts transform selected traces and verifier outputs into markdown overview/detail reports. Third, the evolution query pushes those reports and attribution records into the evolution agent, which turns them into workspace edits and manifests. The oracle is a combination of verifier reward, task diff, LLM debugger diagnosis, and later benchmark re-evaluation.

**Scope and timing.** Scope is per experiment and per benchmark iteration. The loop is staged: evaluate current workspace, analyze traces, evolve the next workspace, evaluate again. It is not a general background memory over arbitrary user sessions. Best-of-N mode adds parallel variant workspaces and cross-variant debugger analysis before choosing a winner.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), AHE belongs in the trace-to-system-definition family. It strengthens the survey's raw/distilled split: raw traces are retained as evidence, debugger reports are distilled knowledge artifacts, and harness edits are promoted system-definition artifacts with stronger behavioral authority.

## Read-back placement

**Direction.** AHE uses both push and pull from the evolution agent's perspective. The iteration query pushes a scoped memory packet into the next evolution run; detail reports and raw traces remain available through deliberate file reads. This is memory read-back, not shipped documentation injection: the pushed packet is assembled from retained run traces, debugger reports, history, manifests, scores, and attribution records accumulated by the experiment loop.

**Targeting and signal.** Targeting is `instance`: `build_evolution_query` assembles the packet for the already-known evolution instance, using the current `iteration`, `job_dir`, task results, rollout counts, cross-iteration diff, stability state, best-ever snapshot, change attribution, and optional variant comparison. The signal is `identifier`: benchmark iteration, task names, outcome labels, file paths, and declared experiment/configuration fields identify which retained records belong to this run. Agent Debugger may use an LLM to distill trace content into reports, but the push selector itself is not embedding or LLM relevance retrieval; precision/recall of the packet's practical relevance is not verified from code.

**Timing relative to action.** Read-back happens before the evolution agent edits the workspace. It can change which files are modified, which failure patterns are prioritized, and whether previous changes are kept, improved, or rolled back.

**Selection, scope, and complexity.** The pushed packet is broad enough to orient the agent but avoids loading all traces. The prompt points to per-task detail files and raw traces for deeper inspection. This is progressive disclosure: summary first, sourced reports second, full traces last. Actual context dilution is not verified from code.

**Authority at consumption.** The pushed packet is advisory context with structurally high authority because the evolution prompt says to read analysis first, use change attribution to decide rollback, and optimize pass@1. Effective authority is not verified from code. Workspace files that result from the packet are stronger system-definition artifacts for the evaluated code agent.

**Faithfulness.** AHE has a stronger faithfulness story than systems that only assume context presence equals use: the next benchmark iteration can falsify predicted fixes and regressions. It still does not prove that a specific injected report sentence caused a specific harness edit; the evidence is iteration-level attribution, not sentence-level causal tracing.

**Other consumers.** Humans can inspect the run directories, analysis reports, manifests, scores, git history, and evolved workspace. The same retained artifacts serve as experiment audit trail, agent context, and rollback substrate.

## Curiosity Pass

**The memory component exists, but it is not central in the baseline.** `agents/code_agent_simple/LongTermMEMORY.md` is present, and the evolution prompt lists long-term memory as a modifiable component, but the baseline agent config inspected here registers only one shell tool and a system prompt. The interesting memory mechanism is therefore the outer evolution loop, not the baseline agent's own memory file.

**The README's seven-component story is broader than the initial agent.** The shipped simple code agent starts minimal: one system prompt, one shell tool, one config, and an empty long-term memory file. That matches the AHE claim that components should be earned by evidence, but it also means many component categories are capabilities of the evolution system rather than active baseline behavior.

**Agent Debugger reports are only as good as their source and prompt.** The code preserves paths back to traces and verifier output, which is good. But the debugger's root-cause prose is still LLM-generated; the system relies on later evaluation to catch bad diagnoses rather than enforcing source-span-level proof before edits.

**The manifest vocabulary appears in two forms.** The evolution prompt's `change_manifest.json` schema uses fields like `id`, `predicted_fixes`, and `risk_tasks`, while the portable HARNESS skill's manifest schema uses `change_id`, `component`, and `predicted_impact`. That split may be harmless for separate contexts, but it weakens portability unless normalized.

**Rollback is partly automatic and partly advisory.** `evolve.py` can evaluate changes, archive manifests, track best-ever snapshots, and provide rollback guidance. The evolution agent still decides how to act on many ineffective or harmful changes, so governance is not fully enforced.

## What to Watch

- Whether future releases enforce trace-to-edit provenance in manifests; that would make every harness edit auditable back to specific traces or debugger sections.
- Whether the two manifest schemas converge; that would make the standalone HARNESS skill and the experiment loop share one reviewable contract.
- Whether long-term memory becomes an active read/write surface in the evaluated code agent; that would change AHE from harness evolution with a memory component into a direct agent-memory system.
- Whether debugger reports gain deterministic validators or citation checks; that would reduce the risk of promoting unsupported LLM diagnoses into system-definition artifacts.
- Whether selection of analysis snippets becomes learned or retrieval-based; that would move the current structured push packet toward a more general relevance-gated activation system.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - compares: AHE turns benchmark traces into reports, manifests, and harness edits.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: AHE separates traces, reports, manifests, workspace files, commits, and skills by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: AHE's retained traces matter because the loop actively pushes summaries and points to pullable detail.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: AHE extracts reusable harness changes from prior agent behavior.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - exemplifies: AHE pre-assembles evaluation, attribution, and debugger context before the evolution agent runs.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: evolved harness files and pushed evolution queries directly shape later agent behavior.
