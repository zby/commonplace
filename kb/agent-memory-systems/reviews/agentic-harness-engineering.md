---
description: Code-inspected review of AHE, an observability-driven coding-agent harness optimizer that mines benchmark rollouts into prompt, tool, middleware, skill, memory, and sub-agent changes
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-29"
---

# Agentic Harness Engineering

Agentic Harness Engineering (AHE) is a Python outer loop for evolving the harness around a fixed coding agent rather than changing model weights. The `china-qijizhifeng/agentic-harness-engineering` repository evaluates a simple NexAU code agent with Harbor, converts and analyzes rollout traces, asks a NexAU-based evolve agent to edit the workspace harness, commits the result, and repeats until the benchmark target or iteration cap is reached. Its strongest contribution for us is not "memory" as a store, but trace-grounded context engineering: benchmark experience is distilled into system prompts, tool descriptions, tool implementations, middleware, skills, sub-agents, and long-term memory files.

**Repository:** https://github.com/china-qijizhifeng/agentic-harness-engineering

**Reviewed commit:** [6c8845ef8a89e1c18aba2a12336a09b109c9e2b1](https://github.com/china-qijizhifeng/agentic-harness-engineering/commit/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1)

**Last checked:** 2026-04-29

## Core Ideas

**Harness components are the learned substrate.** The README frames AHE as holding the base model fixed while evolving the surrounding harness: prompts, tool descriptions, tools, middleware, skills, sub-agents, and long-term memory. The code makes that concrete by copying `agents/code_agent_simple/` into an experiment `workspace/`, initializing a git repository there, applying config patches, and then letting the evolve agent modify only that workspace during each iteration ([README.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/README.md), [evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/evolve.py), [agents/evolve_agent/evolve_prompt.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/agents/evolve_agent/evolve_prompt.md)). The baseline agent is deliberately narrow: a NexAU agent with one shell tool and `LongTermMEMORY.md` / `ShortTermMEMORY.md` files waiting to be evolved ([agents/code_agent_simple/code_agent.yaml](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/agents/code_agent_simple/code_agent.yaml), [agents/code_agent_simple/LongTermMEMORY.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/agents/code_agent_simple/LongTermMEMORY.md)).

**The main loop is benchmark-first, not chat-memory-first.** `run_single_experiment()` creates an experiment directory, snapshots the workspace into `runs/iteration_NNN/input/workspace`, runs Harbor into `input/benchmark`, computes pass@k-style statistics, updates task history, optionally runs Agent Debugger analysis, invokes the evolve agent, commits the workspace, records scores, and repeats ([evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/evolve.py)). This makes evaluation the control signal. The stored "memory" around an experiment is mostly run state: snapshots, benchmark job directories, `task_history.json`, `evolution_history.md`, `change_manifest.json`, `change_evaluation.json`, and score tables.

**Trace distillation is layered before the evolve agent sees the problem.** AHE does not merely hand raw traces to a meta-agent. `_build_adb_jobs()` groups rollout directories by task, prefers `nexau_in_memory_tracer.cleaned.json`, labels pass/fail/timeout traces, collects verifier output, and `_run_single_adb_ask()` asks Agent Debugger targeted questions about root cause, pass-vs-fail divergence, critical mistakes, and general mechanisms. `_write_debugger_analyse()` then writes `input/analysis/overview.md` and per-task detail files that the evolve query injects as primary evidence ([evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/evolve.py), [agents/evolve_agent/skills/agent-debugger-cli/SKILL.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/agents/evolve_agent/skills/agent-debugger-cli/SKILL.md)). The local `trace_converter.py` normalizes NexAU in-memory spans into assistant turns, tool calls, reasoning fields, sub-agent traces, tool definitions, and top-level cleaned messages ([trace_converter.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/trace_converter.py)).

**The evolve prompt is a strong authority boundary.** `evolve_prompt.md` tells the meta-agent to modify only `workspace/`, treat `runs/` as read-only, preserve original prompt rules, avoid task-specific hacks, write a structured `change_manifest.json`, commit each logical change, and validate the agent config. It also teaches the agent that each failure pattern can be addressed at several component levels: prompt, tool description, tool implementation, middleware, skill, sub-agent, or long-term memory ([agents/evolve_agent/evolve_prompt.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/agents/evolve_agent/evolve_prompt.md), [agents/evolve_agent/skills/nexau-evolution-guide/SKILL.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/agents/evolve_agent/skills/nexau-evolution-guide/SKILL.md)). The boundary is prompt-enforced more than sandbox-enforced, but it is detailed enough to function as the system's operating contract.

**Best-of-N turns harness editing into parallel architecture search.** When enabled, AHE creates one git worktree per variant, gives each evolve agent a strategy constraint, evaluates all variant workspaces in parallel, selects the highest pass rate with exception count as tie-breaker, merges the winner, tags loser branches, and writes cross-variant analysis for the next iteration ([configs/base.yaml](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/configs/base.yaml), [evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/evolve.py)). That is a real context-engineering move: the next evolve context receives not just "what happened," but a structured comparison of competing harness hypotheses.

**Explore-agent preloads the meta-agent with generated skills.** On the first iteration, AHE can run Harbor and an explore-agent in parallel. The explore-agent clones or reuses NexAU sources, reads specified web sources, writes `nexau-framework-internals` and `coding-agent-sota-research` skill packages into the experiment's evolve-agent copy, and registers them in `evolve_agent.yaml` ([configs/base.yaml](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/configs/base.yaml), [agents/explore_agent/run.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/agents/explore_agent/run.py)). This is not trace-derived learning from task rollouts, but it is relevant context engineering: before optimization begins, the meta-agent gets domain-specific operational references.

## Comparison with Our System

| Dimension | AHE | Commonplace |
|---|---|---|
| Primary target | Improve a coding-agent harness against a benchmark | Maintain a durable agent-operated knowledge base |
| Learned substrate | Prompt/tool/middleware/skill/sub-agent/memory files in an experiment workspace | Typed notes, source reviews, instructions, indexes, skills, scripts, and workshop artifacts |
| Raw evidence | Harbor job directories, NexAU traces, verifier outputs, pass/fail flips | Source snapshots, note diffs, validation output, review findings, local task context |
| Distillation path | Agent Debugger summaries plus evolve-agent edits into executable/prompt artifacts | Human/agent-authored notes and explicit promotion into instructions, skills, validation, and indexes |
| Oracle | Benchmark rewards, pass@k, task flips, regression tracking | Deterministic validation plus semantic review; usually weaker task-level oracles |
| Lifecycle | Iteration snapshots, git commits, winner merges, score tables, best-ever tracking | Library/workshop split, frontmatter state, link semantics, generated indexes, review gates |
| Scope | Per-experiment and benchmark-scoped | Cross-project methodology KB, intended to accumulate over time |

AHE is stronger than commonplace where the problem admits a hard-ish evaluator. Its loop can say whether a harness variant improved pass@1, which tasks flipped, which tasks regressed, and whether a change's declared predictions matched the next evaluation. Commonplace has richer document semantics, but its ordinary KB mutations rarely have a comparable outcome oracle.

Commonplace is stronger on durable knowledge shape. AHE's analysis files, score files, and evolution history are excellent workshop state, but they are not a curated library with typed claims, stable navigation, link contracts, or review status. Even `LongTermMEMORY.md` is only a mutable harness component; the code does not maintain provenance, contradiction handling, retirement, or semantic indexing for remembered claims.

The useful comparison is that AHE treats context engineering as an optimization target, not just as retrieval. It asks: which component should change so the next rollout behaves differently? That is close to our promotion ladder from observation to note, instruction, skill, script, or guardrail, but AHE makes the choice under benchmark feedback and commits the resulting harness file directly.

## Borrowable Ideas

**Make change manifests prediction-bearing.** AHE's evolve prompt requires each change to name a failure pattern, predicted fixes, risk tasks, and component level, and `evaluate_changes()` compares those predictions with next-iteration flips and regressions ([agents/evolve_agent/evolve_prompt.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/agents/evolve_agent/evolve_prompt.md), [evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/evolve.py)). Commonplace could borrow this now for review-system and fix-system changes: every nontrivial remediation could declare expected warning reductions and regression risks before the next gate run.

**Feed agents pre-digested traces but preserve drill-down paths.** AHE's `overview.md` / `detail/{task}.md` layer is the right compromise between context budget and provenance. For commonplace review sweeps, a comparable bundle could summarize failure classes while keeping exact note paths, validator lines, and raw findings available. Ready to borrow for high-volume review triage.

**Treat component level as part of the diagnosis.** AHE forces the evolve agent to ask whether a failure belongs in a prompt, tool description, tool implementation, middleware, skill, sub-agent, or long-term memory. Commonplace already has analogous surfaces: note, index, instruction, skill, validator, generated view, or script. Making that choice explicit in fix reports is ready to borrow now.

**Use parallel variant worktrees for high-stakes methodology experiments.** Best-of-N evolution is heavier than most KB work needs, but the pattern is valuable when we have a gate: create multiple constrained variants, evaluate them independently, select a winner, preserve loser summaries, and feed cross-variant lessons forward. Needs a concrete costly experiment before borrowing wholesale.

**Generate task-local skills before the main loop starts.** The explore-agent's generated skill registration is a useful preloading pattern. For commonplace, this suggests a workshop-specific research pass that writes temporary skills or context packs before a review/fix campaign. Needs clear lifecycle rules so generated skills do not silently become permanent doctrine.

## Trace-derived learning placement

**Trace source.** AHE consumes repeated benchmark rollouts: Harbor job directories, verifier rewards and stdout, exception files, NexAU `nexau_in_memory_tracer.cleaned.json` or raw in-memory traces, per-task pass/fail/timeout labels, task-history diffs, and variant evaluation outputs ([evolve.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/evolve.py), [trace_converter.py](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/trace_converter.py)).

**Extraction.** Extraction is staged. Deterministic code computes task statistics, pass@k, flips, regressions, exception clusters, behavior counts, and change attribution. Agent Debugger then reads cleaned traces plus verifier output and produces per-task root-cause analyses. The evolve agent receives those summaries, optional raw-trace pointers, prior history, change attribution, and strategy constraints, then edits harness files and writes a manifest.

**Substrate class.** Raw substrate is structured trace JSON plus benchmark result files. Distilled substrate is mixed prose and symbolic: analysis markdown, evolution history, change manifests, prompt/tool/skill/memory markdown, YAML agent config, and Python tool or middleware code. There is no weight update in the inspected repo.

**Role.** The distilled artifacts are system-definition artifacts, not just knowledge records. Reading or executing the changed prompt, tool description, middleware, skill, sub-agent, or memory file is part of the next agent's disposition. The analysis files are knowledge support; the workspace files are the behavior-changing layer.

**Scope.** The learning is per-experiment and per-benchmark, with Terminal-Bench defaults in the shipped config. Some mechanisms, such as tool output handling or context compaction, may generalize, but the implemented loop measures transfer only through configured Harbor datasets.

**Timing.** Offline/staged iterative learning. Each cycle evaluates, analyzes, edits, commits, then evaluates the next version. Best-of-N adds within-cycle parallel exploration and cross-variant analysis before the following iteration.

**Survey placement.** AHE belongs near Meta-Harness, auto-harness, CORAL, and HyperAgents: trace-derived harness optimization rather than end-user memory. It strengthens the survey claim that artifact-learning often matters more than retrieval in coding-agent systems, and it splits the "artifact" bucket into promptware, executable tool/middleware code, skills, and explicit memory files rather than treating all non-weight learning as one substrate.

## Curiosity Pass

**The README's "observability system" claim is directionally fair, but partly dependency-shaped.** The repo contains substantial orchestration, trace normalization, debugger job construction, and experiment bookkeeping. But core pieces are external or partially private: NexAU, Harbor, and `agent_debugger_core` are package dependencies, and the README says Agent Debugger is only partially open-sourced ([README.md](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/README.md), [pyproject.toml](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/pyproject.toml)). So the checked-in repo is best read as an integration harness around important private or external engines, not a fully self-contained implementation.

**The authority boundary is mostly instructional.** `evolve_prompt.md` is careful about writable scope and anti-cheating rules, and `EVOLVE_WORK_DIR` points the evolve agent at the experiment root. But enforcement mostly depends on tool behavior and prompt compliance; the evolve agent still has local file and shell tools configured in a local sandbox ([agents/evolve_agent/evolve_agent.yaml](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/6c8845ef8a89e1c18aba2a12336a09b109c9e2b1/agents/evolve_agent/evolve_agent.yaml)). For benchmark research this may be fine. For production harness evolution, the permission model would need tighter hard gates.

**Memory is present but not independently governed.** `LongTermMEMORY.md` is one mutable component among many, and the evolve prompt treats it as a place for recurring pitfalls and strategies. The code does not make it a separate memory system with retrieval, confidence, review status, or lifecycle. The strongest memory mechanism is therefore not the memory file; it is the entire trace-to-harness loop.

**The trace analysis path is robust enough to matter even when ADB fails.** `_run_single_adb_ask()` retries debugger calls and writes fallback summaries with verifier failure lines and timing information when the debugger times out or errors. That means the evolve agent still gets some grounded signal rather than an empty analysis phase. This small reliability detail is important in long outer loops.

**Best-of-N winner selection is simple by design.** The current selector chooses highest pass rate, then fewer exceptions, then lower index. It does not reason about confidence intervals, task instability, cost, diff size, or long-term maintainability. The simpler selector is inspectable, but it may overfit noisy benchmark samples when `k` or task count is small.

## What to Watch

- Whether the partially open Agent Debugger becomes fully inspectable; it is central to the trace distillation claim.
- Whether AHE adds stronger hard enforcement for workspace-only edits, anti-cheating constraints, and component validation beyond prompt rules.
- Whether evolved `LongTermMEMORY.md` entries gain provenance, scoring, retirement, or conversion into more durable skills/tools.
- Whether Best-of-N grows beyond pass-rate winner selection into stability-aware, cost-aware, or maintainability-aware selection.
- Whether the loop demonstrates cross-benchmark transfer, or whether most improvements remain Terminal-Bench-local harness tuning.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: AHE is a trace-to-harness artifact-learning system with mixed prose and executable substrates
- [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: AHE can automate harness evolution because Harbor and verifier rewards give it an iteration oracle
- [Evaluation automation is phase-gated by comprehension](../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) — parallels: AHE inserts Agent Debugger comprehension before the evolve agent edits the harness
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — exemplifies: AHE's experiment directory is almost entirely workshop state around one optimization process
- [Skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) — relates: AHE treats skills as one behavior-changing component type among prompt, tool, middleware, sub-agent, and memory surfaces
- [Meta-Harness](./meta-harness.md) — compares: both optimize agent harnesses from benchmark traces, but AHE targets NexAU component files and richer observability plumbing
- [auto-harness](./auto-harness.md) — compares: both are benchmark-driven outer loops, with AHE adding trace distillation, component-level edits, Best-of-N variants, and generated skills
- [CORAL](./CORAL.md) — compares: both use eval-gated coding-agent runs, but CORAL emphasizes multi-agent collaborative search while AHE emphasizes meta-agent harness mutation
