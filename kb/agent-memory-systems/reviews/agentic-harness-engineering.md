---
description: "Agentic Harness Engineering review: trace-driven outer loop that distills coding-agent rollouts into debugger reports and durable harness edits"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
tags: [trace-learning]
---

# Agentic Harness Engineering

Agentic Harness Engineering, by china-qijizhifeng, is an experiment framework for improving a coding agent by evolving the harness around a fixed base model. At the reviewed commit, the system evaluates a workspace agent with Harbor, converts rollout traces into debugger reports, prompts a NexAU evolution agent to edit harness components, records predicted changes, and evaluates the next iteration to attribute task flips and regressions.

**Repository:** https://github.com/china-qijizhifeng/agentic-harness-engineering

**Reviewed commit:** [cb6ea4e0055d60946424e8c608b4265ffaf99a09](https://github.com/china-qijizhifeng/agentic-harness-engineering/commit/cb6ea4e0055d60946424e8c608b4265ffaf99a09)

**Last checked:** 2026-06-05

## Core Ideas

**The memory target is the harness, not model weights.** The README frames AHE as holding the base model fixed while evolving system prompts, tool descriptions, tool implementations, middleware, skills, sub-agents, and long-term memory; the implementation copies `agents/code_agent_simple/` into an experiment `workspace/`, initializes it as a git repo, and later commits evolved workspace changes ([README.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/README.md), [evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/evolve.py), [agents/code_agent_simple](https://github.com/china-qijizhifeng/agentic-harness-engineering/tree/cb6ea4e0055d60946424e8c608b4265ffaf99a09/agents/code_agent_simple)). The retained artifact is therefore a runnable agent configuration, not a note database.

**Trace-derived analysis is staged before harness editing.** Harbor writes per-task rollout outputs, including `agent/nexau_in_memory_tracer.cleaned.json`, runtime logs, verifier output, and rewards. `run_parallel_adb_ask()` groups those traces by task, calls Agent Debugger with pass/fail labels and verifier context, then writes `input/analysis/overview.md` and `input/analysis/detail/{task}.md` for the evolution agent to read first ([README.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/README.md), [evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/evolve.py), [trace_converter.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/trace_converter.py)).

**Edits are supposed to be falsifiable.** The evolve prompt requires failure evidence, root cause, targeted fix, and predicted impact before each change, and it requires a `change_manifest.json` with predicted fixes and risk tasks. On the next iteration, `evaluate_changes()` compares the manifest to fail-to-pass and pass-to-fail task transitions and writes a `change_evaluation.json` with verdicts such as effective, mixed, ineffective, or harmful ([agents/evolve_agent/evolve_prompt.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/agents/evolve_agent/evolve_prompt.md), [evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/evolve.py)).

**Context efficiency is a mix of pre-digestion and middleware compaction.** The evolution query carries aggregate pass rates, task classifications, cross-iteration diffs, debugger overview, trend history, best-ever snapshot, and change attribution so the evolve agent does not have to inspect every trace by default. The prompt still tells it where to drill into detailed analysis and raw traces, and the evolve agent also has context compaction middleware with a token threshold and recent-message retention ([evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/evolve.py), [agents/evolve_agent/evolve_prompt.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/agents/evolve_agent/evolve_prompt.md), [agents/evolve_agent/middleware/context_compaction/middleware.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/agents/evolve_agent/middleware/context_compaction/middleware.py)). The system reduces both volume and complexity by turning trace forests into summaries, tables, and pointers before the model call.

**Adoption is native to coding-agent harness work.** The editable unit is ordinary files under `workspace/`, loaded by NexAU YAML, Python tools/middleware, prompt Markdown, skills, and optional sub-agents. Git commits and tags preserve rollback points, while workspace snapshots under `runs/iteration_NNN/input/workspace/` preserve the exact candidate evaluated in each loop ([evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/evolve.py), [agents/evolve_agent/evolve_agent.yaml](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/agents/evolve_agent/evolve_agent.yaml)).

## Artifact analysis

- **Storage substrate:** `files` `repo` — The standing harness lives as workspace files plus a git history; experiment evidence and derived state live as files under `experiments/.../runs/`, including benchmarks, analyses, scores, histories, manifests, snapshots, and traces. There is no code-grounded vector store, graph store, or model-weight update path in the reviewed source.
- **Representational form:** `prose` `symbolic` — Prompts, long-term memory, skills, debugger reports, summaries, and feedback are prose; YAML agent configs, tool schemas, Python tools/middleware, JSON traces, manifests, score files, git commits, and task-result tables are symbolic.
- **Lineage:** `authored` `imported` `trace-extracted` — Baseline agent components and evolution prompts are authored; external source and web material can be imported by the explore agent into skills; rollout traces, verifier results, debugger reports, score histories, change evaluations, and evolved harness edits are derived from agent/evaluation events.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Trace reports and histories advise the evolution agent; prompts, skills, long-term memory, tool descriptions, middleware, and sub-agents instruct future code-agent behavior; workspace-only rules and validation commands constrain edits; YAML config, component registration, and sub-agent/tool names route behavior; Harbor/verifier results, change attribution, and validation scripts check outcomes; pass rates, best-ever snapshots, variant selection, and change verdicts rank candidates; trace-derived analyses and edits are the learning loop.

**Workspace harness.** The main retained behavior-shaping artifact is the git-backed workspace copied from `agents/code_agent_simple/`. Its prose operative parts are `systemprompt.md`, `LongTermMEMORY.md`, and any skills; its symbolic operative parts are `code_agent.yaml`, tool descriptions, Python tools, middleware, and sub-agent configs. It is consumed by Harbor/NexAU as a system-definition artifact for the next evaluation.

**Trace and debugger analysis artifacts.** Raw rollout traces, runtime logs, verifier rewards, and cleaned trace JSON are source material. Agent Debugger reports are derived knowledge artifacts that compress those traces into root-cause summaries and per-task detail files. Their authority is advisory until the evolution agent turns them into workspace edits.

**Change manifests and attribution.** `change_manifest.json` records the evolution agent's declared evidence, predicted fixes, risks, and component level. `change_evaluation.json` is a derived symbolic report that compares those predictions with later task flips. This is the system's clearest promotion path: trace evidence becomes a manifest-backed edit, then later evaluation can keep, revise, or roll back that edit.

**Scores, histories, and snapshots.** `iteration_scores.yaml`, `iteration_scores.md`, `task_history.json`, `evolution_history.md`, `best_ever.json`, and workspace snapshots are symbolic/prose lineage surfaces. They let the evolution prompt point to previous performance and best versions without reloading every trace.

**Evolve-agent traces and memory.** The evolve agent itself saves conversation traces and has a `save_memory` tool modeled on Gemini's memory tool, but the configured evolve agent does not list that tool in `evolve_agent.yaml` at this commit ([agents/evolve_agent/tools/session_tools/save_memory.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/agents/evolve_agent/tools/session_tools/save_memory.py), [agents/evolve_agent/evolve_agent.yaml](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/agents/evolve_agent/evolve_agent.yaml)). The operative memory path is therefore the experiment/workspace loop, not a personal-memory tool.

## Comparison with Our System

AHE and Commonplace both treat readable artifacts as the tractable unit of agent learning. AHE learns by changing a runnable harness from benchmark traces; Commonplace learns by writing typed KB artifacts, review outputs, indexes, and instructions. Both preserve enough source lineage for a later agent to audit the decision, but AHE's lineage is performance-trace centered while Commonplace's is citation, type-contract, and review centered.

The strongest alignment is staged distillation. AHE does not push raw multi-million-token traces straight into the evolve agent. It first computes task statistics, debugger summaries, cross-iteration diffs, and change-attribution tables, then leaves raw traces as drill-down evidence. Commonplace uses the same broad principle through snapshots, reviews, indexes, and validation reports, though not usually against a pass/fail benchmark oracle.

The strongest divergence is authority. AHE can automatically rewrite prompts, tools, middleware, skills, and sub-agents because Harbor supplies a hard external score. Commonplace deliberately keeps most semantic promotion human/agent-reviewed because note truth is not as cheaply falsified. Borrowing the automation level without an oracle would be unsafe; borrowing the trace-to-candidate-to-falsification structure is more realistic.

### Borrowable Ideas

**Change manifests with predicted effects.** Commonplace review or writing runs could require each substantial edit to name expected effects and risk artifacts, then compare later validation/review outcomes against that manifest. Ready for review-gate and note-revision workflows.

**Pre-digested trace reports with raw-trace drill-down.** Commonplace could retain concise per-run analyses plus paths to raw command/session traces instead of asking future agents to infer from logs. Ready where commands already emit structured output.

**Best-ever snapshot as a rollback target.** AHE tracks the best-scoring workspace and can restore snapshots on resume. Commonplace could track best validated/reviewed artifact versions for risky generated rewrites, but it needs a clear quality oracle first.

**Variant exploration with explicit strategy constraints.** AHE's best-of-N mode assigns different component-level strategies and evaluates all variants. Commonplace could use that for high-impact note rewrites or instruction changes, but only when semantic judging is strong enough to choose a winner.

**Do not borrow score worship.** AHE optimizes pass@1 on a benchmark. Commonplace should treat validation/review signals as evidence, not as semantic truth; otherwise it would overfit artifacts to local gates.

## Write side

**Write agency:** `manual` `automatic` — Operators configure experiments and baseline harnesses, while the system automatically initializes workspaces, writes benchmark results, debugger analyses, histories, scores, traces, manifests, snapshots, and LLM-authored workspace changes through the evolution agent.

**Curation operations:** `evolve` `promote` — The evolution agent modifies existing harness artifacts in light of newly derived trace/debugger evidence, and best-of-N can promote a winning variant into the main workspace. Rollback is available through snapshots and prompts, but the ordinary loop records harmful/ineffective verdicts rather than automatically invalidating every bad edit.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` — The loop consumes cleaned NexAU traces, runtime logs, verifier rewards/output, task-result transitions, score histories, change manifests, and evolve-agent traces.

**Extraction.** The raw stage is Harbor/NexAU execution evidence. The first distillation stage is deterministic and LLM-mediated analysis: trace normalization, task stats, verifier-error extraction, Agent Debugger reports, history updates, and change-attribution verdicts. The second distillation stage is the evolution agent's harness edit: it must cite failure evidence, root cause, targeted fix, predicted impact, affected files, and risk tasks. The oracle is benchmark pass/fail plus verifier output, with an LLM debugger and LLM evolve agent in the middle; the code does not prove semantic faithfulness of those LLM-written analyses beyond later task outcomes.

**Learning scope:** `per-project` `cross-task` — Each experiment workspace learns across tasks in one dataset/run, and the resulting harness can be post-evaluated or transferred, but the implementation's durable store is experiment/project scoped.

**Learning timing:** `staged` — Evaluation writes traces, analysis writes reports, evolution edits the workspace, and the next iteration evaluates whether the prior edit helped or hurt.

**Distilled form:** `prose` `symbolic` — Debugger reports, prompts, skills, and long-term memory are prose; configs, tool schemas, Python tools/middleware, manifests, scores, histories, and git snapshots are symbolic. I did not find a parametric distilled artifact in the reviewed code.

This is a strong trace-learning system by Commonplace's survey standard: raw traces are not merely stored, but are transformed into behavior-shaping harness artifacts and later checked by an external benchmark. The main caveat is that the learned artifact is optimized for benchmark performance, not for general truth or maintainability.

## Read-back

**Read-back:** `both` — The evolution agent pulls detailed reports and raw traces when instructed, while each evolution query pushes retained run memory into the agent's next context: current results, task classifications, debugger overview, cross-iteration diffs, historical trends, best-ever snapshot, change attribution, variant results, workspace path, and strategy hints.

**Read-back signal:** `coarse` `identifier` — The query always includes coarse experiment memory for the current iteration, and it uses identifiers such as iteration number, task name, variant id, workspace path, and change id to point the agent at specific retained artifacts. I did not find embedding, lexical retrieval, or LLM relevance selection driving automatic push read-back.

**Faithfulness tested:** `no` — AHE evaluates whether evolved harness changes improve benchmark outcomes, but it does not run a with/without ablation proving the evolve agent used a particular pushed memory item, debugger report, or change-attribution table faithfully.

The receiving evolution agent gets a pre-invocation prompt assembled by `build_evolution_query()`. That prompt includes enough retained state to steer the next edit without opening every artifact, and it points to detail files and raw traces for pull-based drill-down. The system's context risk is not vector-retrieval noise; it is summary over-trust, prompt length, and benchmark overfitting. The compaction middleware can manage message volume for the evolve agent, but it is not a retrieval system and may discard conversation history rather than improve evidence selection.

For the code agent being evaluated, read-back is simpler. The baseline `code_agent_simple` prompt and `LongTermMEMORY.md` are always-loaded harness files, but the baseline memory file is essentially empty at the reviewed commit ([agents/code_agent_simple/systemprompt.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/agents/code_agent_simple/systemprompt.md), [agents/code_agent_simple/LongTermMEMORY.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/cb6ea4e0055d60946424e8c608b4265ffaf99a09/agents/code_agent_simple/LongTermMEMORY.md)). Later iterations may add richer always-loaded or component-specific memory, but that is an evolved outcome, not present in the baseline source.

## Curiosity Pass

**The most interesting memory is not named memory.** `LongTermMEMORY.md` exists, but AHE's important retained learning is a modified harness plus experiment reports, manifests, histories, and snapshots.

**The README's "long-term memory" component is real as an editable slot, not as a populated mechanism.** The baseline file is a placeholder, and the evolve agent can choose to edit it, but the inspected code does not include specialized retrieval or lifecycle management for it.

**The falsification loop is stronger than the semantic extraction loop.** Benchmark flips can reject a bad harness change, but they cannot fully explain why a prose debugger report or LLM-authored root cause was right. AHE's safety comes from repeated external evaluation, not from guaranteed interpretation quality.

**Trace-learning is bounded by diagnostic richness.** The system invests heavily in verifier context, pass/fail labels, per-task reports, and partial-pass comparison. That gives the evolution agent better evidence than raw scores alone, and it is the main reason the loop is more than blind prompt search.

**Best-of-N turns harness evolution into population search.** The implementation can run strategy-constrained variants and adopt a winner. That is useful, but it changes the memory story from one cumulative lineage to competing lineages, making attribution and rollback more important.

## What to Watch

- Whether the partially open-sourced Agent Debugger becomes fully inspectable; current review can inspect the orchestration around `adb ask`, but not all debugger internals.
- Whether `save_memory` becomes registered in `evolve_agent.yaml` or the code agent gains a real memory tool; that would add a separate write/read-back path beside workspace evolution.
- Whether change-attribution verdicts start automatically rolling back or invalidating changes instead of merely informing the next evolution prompt; that would strengthen the write-side lifecycle classification.
- Whether variant selection adds stronger causal attribution than pass-rate comparison; current best-of-N can choose a winner, but semantic lessons from losing variants remain prompt-mediated.
- Whether post-evolve transfer tests become part of the ordinary loop rather than optional validation; that would reduce benchmark-specific overfitting risk.

Relevant Notes:

- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - applies: AHE turns rollout traces into debugger reports, manifests, and harness changes.
- [Evaluate memory by effects](../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) - applies: the learned harness is judged by later benchmark behavior rather than storage alone.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes AHE's stored experiment artifacts from the evolution query that actually pushes selected memory into context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - supports separating traces, reports, manifests, harness files, scores, and snapshots by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies AHE's prompts, tool descriptions, tools, middleware, skills, sub-agents, configs, and validation/evaluation harness.
- [Diagnostic richness constrains outer-loop learning quality](../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) - explains why AHE's verifier-grounded debugger reports are more valuable than raw pass/fail traces alone.
