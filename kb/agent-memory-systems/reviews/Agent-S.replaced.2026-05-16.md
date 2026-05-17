---
description: "Agent-S review: versioned computer-use agents with S1/S2 JSON experience memory, S2.5/S3 prompt-time reflection, code-agent delegation, and BBoN trajectory judging"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-04-27"
---

# Agent-S

> Replaced 2026-05-16. See [Agent-S](./Agent-S.md) for the current review.

Agent-S is Simular AI's `gui-agents` framework for computer-use agents. The repository is a moving stack rather than one memory design: S1 and S2 implement hierarchical manager-worker GUI agents with a downloaded, locally updated experience knowledge base; S2.5 removes the hierarchy for a single worker loop; S3 keeps that simpler runtime, adds optional code-agent delegation, and supplies a Behavior Best-of-N evaluation layer that captions and judges benchmark trajectories.

**Repository:** https://github.com/simular-ai/Agent-S

**Reviewed commit:** 5caa76cb19c6a6b947a524f74995c45848c2efbc

**Commit URL:** https://github.com/simular-ai/Agent-S/commit/5caa76cb19c6a6b947a524f74995c45848c2efbc

## Core Ideas

**The architecture evolves from persistent hierarchical memory to lighter prompt-time control.** S1's `GraphSearchAgent` downloads a release KB if the local path is absent, then wires a `Manager` and `Worker`. The manager formulates a search query, retrieves narrative experience, optionally fuses web knowledge, produces a high-level plan, translates it to a DAG, and topologically sorts subtasks for the worker. S2 keeps the manager-worker split but replans after failures and completed subtasks. S2.5 and S3 drop the manager entirely: `AgentS2_5` and `AgentS3` wrap one worker that receives the full task, screenshot history, reflection, and a short text buffer ([s1 AgentS.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s1/core/AgentS.py), [s1 Manager.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s1/core/Manager.py), [s2 manager.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s2/agents/manager.py), [s2_5 agent_s.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s2_5/agents/agent_s.py), [s3 agent_s.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s3/agents/agent_s.py)).

**Procedural memory is generated from the action API, not learned skills.** Each version constructs a system prompt by inspecting grounding-agent methods marked with `is_agent_action`, inserting method signatures and docstrings into the prompt, and then asking the model for a single grounded Python call. S3 adds stronger guidelines for when to use GUI actions versus a code agent, and format checkers reprompt unless the answer contains exactly one valid agent action ([s2_5 procedural_memory.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s2_5/memory/procedural_memory.py), [s3 procedural_memory.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s3/memory/procedural_memory.py), [s3 formatters.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s3/utils/formatters.py)).

**S1/S2 have the actual durable experience memory.** Their `KnowledgeBase` stores `episodic_memory.json`, `narrative_memory.json`, `formulate_query.json`, `{search_engine}_rag_knowledge.json`, and `embeddings.pkl` under a platform-specific local KB directory. Retrieval is cosine similarity over embedded task or subtask keys; saving summarizes trajectories through LLM prompts and writes JSON. The CLI paths call `update_narrative_memory(...)` and `update_episodic_memory(...)`, but the OSWorld harness primarily records `traj.jsonl` and screenshots rather than invoking these memory-update methods ([s1 Knowledge.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s1/core/Knowledge.py), [s2 knowledge.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s2/core/knowledge.py), [s2 cli_app.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s2/cli_app.py), [s3 lib_run_single.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/osworld_setup/s3/lib_run_single.py)).

**S3's "knowledge" during deployment is mostly in-context state.** The grounding agent has `save_to_knowledge(...)`, but that only appends strings to `self.notes` for reuse during the same task. Reflection is also prompt-time: the reflection agent sees the latest trajectory and screenshot, then the worker injects the result into the next action prompt. Long-context models keep text while dropping older images; shorter-context models drop whole turns. None of this becomes a cross-task memory file in the S3 runtime ([s3 grounding.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s3/agents/grounding.py), [s3 worker.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s3/agents/worker.py), [s3 cli_app.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s3/cli_app.py)).

**The code agent is a delegated execution loop, not a persistent skill learner.** S3 can expose `agent.call_code_agent(...)` when the grounding agent has an environment controller. The code agent receives a task, screenshot, and step budget; it iteratively emits Python or Bash, executes it through the controller, appends execution results back into its own prompt, and returns a summary plus execution history. The worker injects that result on the next turn and then clears it. This is powerful execution-time decomposition, but the learned artifact is only the transient history/result unless benchmark logs preserve it ([code_agent.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s3/agents/code_agent.py), [s3 grounding.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s3/agents/grounding.py), [s3 worker.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s3/agents/worker.py)).

**Behavior Best-of-N is trajectory augmentation plus judge selection.** The OSWorld S3 harness writes `step_*.png`, `instruction.txt`, `traj.jsonl`, `result.txt`, and logs per task. The BBoN pipeline then generates fact captions from screenshot pairs and `exec_code`, saves them as `fact_captions.jsonl`, and asks a comparative VLM judge to choose among result directories using initial/final screenshots plus fact captions. This is benchmark-side selection memory, not a runtime memory store used by the next S3 task ([s3 lib_run_single.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/osworld_setup/s3/lib_run_single.py), [behavior_narrator.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s3/bbon/behavior_narrator.py), [generate_facts.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/osworld_setup/s3/bbon/generate_facts.py), [comparative_judge.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/gui_agents/s3/bbon/comparative_judge.py), [run_judge.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/osworld_setup/s3/bbon/run_judge.py)).

**OpenClaw integration packages Agent-S as an external skill.** The integration is a wrapper and skill document: OpenClaw calls `agent_s_task` or `agent_s_wrapper.py`, which shells out to the installed `agent_s` CLI with provider/model and grounding settings. It does not expose Agent-S memory internals to OpenClaw; it makes GUI automation callable as a skill from another agent runtime ([OpenClaw README](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/integrations/openclaw/README.md), [SKILL.md](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/integrations/openclaw/SKILL.md), [agent_s_wrapper.py](https://github.com/simular-ai/Agent-S/blob/5caa76cb19c6a6b947a524f74995c45848c2efbc/integrations/openclaw/agent_s_wrapper.py)).

## Comparison with Our System

| Dimension | Agent-S | Commonplace |
|---|---|---|
| Primary substrate | GUI-agent prompts, pyautogui code strings, JSON experience memory in S1/S2, benchmark result files | Markdown notes, sources, reviews, instructions, ADRs, generated indexes |
| Memory atom | Task/subtask summary, search result, text buffer item, code-agent result, fact caption, trajectory log | Typed knowledge artifact with frontmatter, links, validation, status, and source evidence |
| Activation | Automatic prompt injection inside the running agent; BBoN judge selection after multiple rollouts | Agent-directed `rg`, indexes, authored links, skills, validation and review workflows |
| Learning trigger | CLI task completion in S1/S2, code-agent turns inside S3, benchmark trajectory post-processing for BBoN | Deliberate authoring, ingest, connect, review, and promotion |
| Governance | Prompt constraints, format checkers, environment reward/evaluate, comparative VLM judge | Type specs, deterministic validation, semantic review, git history, link contracts |
| Persistence | Mixed: local JSON KB for S1/S2; logs/facts/results for benchmarks; mostly transient state in S3 deployment | Files are the source of truth; derived reports and indexes are regenerable |

Agent-S is stronger where memory is subordinate to action. Its best mechanisms are not knowledge management surfaces; they are decision loops that keep a GUI agent moving: manager-worker planning, action-API prompt synthesis, visual grounding, single-action formatting gates, reflection, code delegation, and BBoN selection.

Commonplace is stronger where memory must become inspectable, cited, maintained knowledge. Agent-S's S1/S2 memories are JSON summaries keyed by task strings with embeddings, not source-linked artifacts. S3's runtime has even less durable memory: its text buffer, reflections, and code-agent summaries improve the immediate task but do not produce reusable notes, procedures, tests, or reviewable lessons.

The interesting overlap is trace handling. Agent-S captures rich action traces, screenshots, rewards, and judge annotations in evaluation directories. Commonplace has stronger artifact contracts but weaker native capture of execution trajectories. Agent-S shows how much useful evidence is available when a harness treats screenshots, actions, and results as first-class outputs.

## Borrowable Ideas

**Generate procedural prompts from live action APIs.** Ready to borrow for tool-heavy skills. Agent-S avoids hand-maintaining a tool list by introspecting decorated methods and their docstrings. A commonplace analogue could render command or MCP affordances into a task-local instruction surface from real callable metadata.

**Keep reflection as a bounded control signal.** Ready as a warning and a pattern. S2.5/S3 reflections are not stored forever; they are immediate trajectory feedback. For many workflows, a short-lived reflection channel may be better than promoting every observation into the library layer.

**Use format checkers before execution.** Ready to borrow for generated action workflows. S3's single-action and valid-code checks are small, but they make prompt compliance part of the runtime contract before pyautogui code executes.

**Capture multimodal task evidence as a review substrate.** Worth borrowing if commonplace adds agent-execution evaluations. Agent-S's benchmark directories preserve initial/final screenshots, per-step screenshots, action JSONL, rewards, and fact captions. That is a stronger evidence bundle than a text-only transcript.

**Treat code execution as a separate specialist with a summary handoff.** Useful for GUI or document tasks that cross from visual work into file manipulation. The code agent's step budget, execution history, and summary give the GUI worker a compact handoff, though commonplace would need stronger provenance and sandboxing.

**Do not borrow S1/S2 memory as-is.** The JSON experience store is useful but too weakly governed for a KB: no citation chain from a summary to exact screenshots/actions, no confidence or status, no contradiction handling, and no promotion path from "this task worked" into a maintained procedure.

## Trace-derived learning placement

**Trace source.** Agent-S has two qualifying trace sources. S1/S2 consume live task and subtask trajectories in the CLI path, including reflections and executor plans. S3/BBoN consumes benchmark result directories containing screenshots, `traj.jsonl`, executed code/actions, rewards, and task outcomes.

**Extraction.** S1/S2 summarize trajectories into narrative and episodic JSON memory through LLM prompts, then retrieve by task-key embeddings. S3/BBoN uses `BehaviorNarrator` to caption before/after screenshot changes and a comparative judge to select the better rollout among multiple result directories. The extraction oracle is mixed: LLM summarization for S1/S2, environment reward/evaluate for benchmark scoring, and VLM judge selection for BBoN.

**Storage substrate, form, and lineage.** The durable S1/S2 retained state is prose JSON plus pickled embeddings. Its lineage is task or subtask trajectory -> LLM summary -> stored episodic memory. The BBoN retained state is benchmark artifacts: screenshot PNGs, JSONL trajectories, fact-caption JSONL, judge JSON, and result text. The S3 deployment state is mostly transient prompt state rather than durable memory.

**Behavioral authority.** S1/S2 experience summaries are knowledge artifacts: they are retrieved as relevant prior experience for a future task or subtask. BBoN fact captions have evaluation authority: they improve selection among already generated rollouts, not the behavior of the next single Agent-S run. The S3 code-agent result is in-task working memory, not cross-task system-definition use.

**Scope.** S1/S2 memory is local to the configured KB directory, platform, and agent version. BBoN is per benchmark experiment and result-directory set. There is no repo-level mechanism that promotes learned GUI procedures into reusable skills or model weights.

**Timing.** S1/S2 CLI learning is online at task completion. BBoN is offline or post-run: first generate multiple trajectories, then caption facts, then judge. S3's reflection and code-agent handoffs happen online during a task but are not persisted as learned memory.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), Agent-S splits across two regions: S1/S2 are trajectory-to-prose-memory systems, while S3/BBoN is trajectory-run evaluation and selection with fact-caption augmentation. It strengthens the survey distinction between trace capture and behavior-changing memory: Agent-S captures very rich traces, but its latest runtime mostly uses them for immediate control or benchmark selection rather than durable system-definition artifacts.

## Curiosity Pass

The README's "learn from past experiences" framing is true for S1/S2's JSON KB paths, but much less true for the current S3 CLI. At this commit, the default `agent_s` console entry point runs S3; its durable outputs are logs, while reusable experience memory lives mainly in older versioned code paths and benchmark artifacts.

The manager-worker design did not disappear because it was unimplemented. S1/S2 contain real DAG planning and subtask memory retrieval. S2.5/S3 are simpler by design: less inference overhead, less persistent knowledge machinery, and more reliance on direct visual grounding plus reflection.

The code agent looks like a skill learner at first glance, but it is better read as a local execution specialist. It can produce a detailed execution history and summary, yet the worker consumes that result once and clears it. Without a promotion path, successful code-agent strategies do not become reusable tools.

BBoN is memory-like but not agent memory in the commonplace sense. Fact captions are distilled from trajectories and persisted, but they serve the judge's comparison surface for a batch of rollouts. They do not automatically update S3's future prompt, action API, or procedural memory.

OpenClaw integration is packaging, not integration of memory systems. It lets another agent invoke Agent-S as a shell skill, but the bridge returns status/log pointers rather than structured memories or reusable experience artifacts.

## What to Watch

- Whether S3 reintroduces a durable cross-task memory path, or whether the project continues treating memory as benchmark-side traces plus prompt-time state.
- Whether BBoN facts become training data, reusable task memories, or runtime retrieval context instead of staying a post-hoc judge aid.
- Whether code-agent execution histories get promoted into reusable procedures, tests, or application-specific skills.
- Whether the OpenClaw wrapper grows a structured result contract that other agents can ingest, rather than only streaming CLI output and pointing at logs.
- Whether release KB assets gain provenance linking each experience summary back to concrete trajectories, screenshots, scores, and extraction prompts.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Agent-S splits trace-derived learning between S1/S2 trajectory summaries and S3/BBoN benchmark-side fact/judge artifacts.
- [OS-Copilot](./OS-Copilot.md) - compares-with: both are computer-use agents, but OS-Copilot promotes trajectories into executable tools while Agent-S S3 mainly uses prompt-time reflection and benchmark selection.
- [SkillWeaver](./SkillWeaver.md) - compares-with: both operate over visual/action trajectories, but SkillWeaver promotes successful traces into callable Playwright functions while Agent-S keeps S3 actions in runtime prompts and logs.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - qualifies: S1/S2 have deploy-time prose memory, while S3 shifts much of the improvement story to execution-time reflection and post-run evaluation.
- [agent-memory-needs-discoverable-composable-trusted-knowledge-under-bounded-context](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) - contrasts: Agent-S captures rich evidence but does not turn latest-runtime traces into discoverable, governed KB artifacts.
- [knowledge-storage-does-not-imply-contextual-activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - grounds: S3 has strong immediate activation but weak durable storage; S1/S2 have storage with thinner governance.
