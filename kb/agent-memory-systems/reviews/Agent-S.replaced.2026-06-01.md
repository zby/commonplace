---
description: "Agent-S review: Simular GUI-agent stack with S1/S2 JSON experience memory, S2.5/S3 prompt-time reflection, code-agent delegation, and BBoN trace judging"
type: ../types/agent-memory-system-review.md
status: outdated
tags: []
last-checked: "2026-05-16"
---

# Agent-S

> Replaced 2026-06-01. See [Agent-S](./Agent-S.md) for the current review.

Agent-S is Simular AI's open-source computer-use agent stack for desktop GUI automation. The inspected repository contains four generations: S1 and S2 use hierarchical planning plus retrieved experience memory, S2.5 simplifies into a single worker with prompt-time reflection, and S3 keeps the simpler worker while adding a local code-agent action and Behavior Best-of-N evaluation over multiple rollouts. For this review, the memory system is not one stable substrate across versions; it is a set of retained surfaces that shifted from JSON experience stores toward in-context reflection, scratch text buffers, execution-history handoff, and offline trajectory judging.

**Repository:** https://github.com/simular-ai/Agent-S

**Reviewed commit:** 73ea17225bae73ab45d077cc442978d3ff8e286a

**Commit URL:** https://github.com/simular-ai/Agent-S/commit/73ea17225bae73ab45d077cc442978d3ff8e286a

## Core Ideas

**S1 and S2 have real experience memory, but it is JSON summaries, not a curated KB.** Both generations maintain `narrative_memory.json`, `episodic_memory.json`, and `embeddings.pkl` under a platform-specific local KB directory. Narrative memory maps a task search query to a whole-task summary; episodic memory maps a subtask key to a summarized subtask trajectory. Retrieval embeds the current instruction or subtask query, computes cosine similarity against memory keys, and injects the nearest prior summary into the planner or worker prompt ([gui_agents/s2/core/knowledge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/core/knowledge.py), [gui_agents/s2/agents/agent_s.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/agent_s.py), [gui_agents/s2/agents/manager.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/manager.py), [gui_agents/s2/agents/worker.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/worker.py)).

**The retained artifact is a prose summary with embedding sidecar.** The behavior-shaping operative part is prose: LLM-written summaries of successful task or subtask trajectories. The storage substrate is local JSON plus a pickle embedding cache. The embedding cache is a derived retrieval surface, not the canonical memory. Lineage is partly present in the key string and the trajectory-derived prompt, but the stored summary is not linked to screenshots, actions, rewards, or result files after promotion ([gui_agents/s2/agents/agent_s.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/agent_s.py), [gui_agents/s2/utils/common_utils.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/utils/common_utils.py)).

**S2 can bootstrap from release-hosted default KB assets.** `AgentS2` can download a platform-specific ZIP such as `s2_linux.zip` from a GitHub release into the local KB directory when `use_default_kb=True`. The README describes these release assets as a knowledge base that updates during inference, and the code warns that deleting the folder wipes experience gained since download. That makes the release ZIP a seed knowledge artifact, while runtime JSON writes are local derived state ([gui_agents/s2/agents/agent_s.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/agent_s.py), [gui_agents/utils.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/utils.py), [README.md](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/README.md)).

**S2.5 removes durable experience retrieval and relies on live reflection plus a scratch text buffer.** `AgentS2_5` has no `KnowledgeBase` object in its worker path. It keeps bounded generator and reflection histories, asks a reflection agent to judge the current task trajectory, and exposes `save_to_knowledge(...)` as an action that appends strings to `grounding_agent.notes`. That note buffer is only an in-run substrate: it is prompt-visible for later turns, but not persisted across sessions ([gui_agents/s2_5/agents/agent_s.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2_5/agents/agent_s.py), [gui_agents/s2_5/agents/worker.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2_5/agents/worker.py), [gui_agents/s2_5/agents/grounding.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2_5/agents/grounding.py)).

**S3 adds a code-agent channel rather than a long-term KB.** The installed console entry point runs S3 by default. S3's worker builds a prompt from the current screenshot, bounded trajectory, optional reflection, the in-run text buffer, and any result left by `call_code_agent`. The code agent executes Python or Bash through the environment controller for up to a budget, stores an execution history and LLM-generated summary in `last_code_agent_result`, and hands that result back to the GUI worker on the next step. This is a behavior-changing handoff surface inside a task, but it is not persistent memory ([setup.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/setup.py), [gui_agents/s3/agents/worker.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/worker.py), [gui_agents/s3/agents/grounding.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/grounding.py), [gui_agents/s3/agents/code_agent.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/code_agent.py)).

**BBoN treats rollout traces as evidence for selection, not as agent memory.** The S3 benchmark path saves screenshots, instructions, trajectory JSONL, rewards, environment info, and result files for each task. The BBoN scripts generate per-step fact captions from before/after screenshots plus actions, then compare multiple result directories for variance tasks and write selected trajectory records plus score summaries. Those artifacts have evaluation and ranking authority over rollouts, but they are not loaded back into the S3 runtime as reusable knowledge ([osworld_setup/s3/lib_run_single.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/lib_run_single.py), [gui_agents/s3/bbon/behavior_narrator.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/bbon/behavior_narrator.py), [gui_agents/s3/bbon/comparative_judge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/bbon/comparative_judge.py), [osworld_setup/s3/bbon/generate_facts.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/bbon/generate_facts.py), [osworld_setup/s3/bbon/run_judge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/bbon/run_judge.py), [osworld_setup/s3/bbon/utils.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/bbon/utils.py)).

## Comparison with Our System

| Dimension | Agent-S | Commonplace |
|---|---|---|
| Primary substrate | Runtime prompt state, JSON experience summaries, pickle embeddings, screenshots/JSONL eval traces | Markdown notes, source snapshots, reviews, ADRs, instructions, generated indexes |
| Memory atom | Task or subtask summary, in-run note, code-agent result, rollout fact caption | Typed artifact with frontmatter, links, validation, status, and collection rules |
| Creation trigger | Finished task/subtask, `save_to_knowledge`, code-agent execution, offline BBoN fact generation | Deliberate authoring, ingest, review, validation, promotion |
| Retrieval/activation | Embedding nearest-neighbor summaries in S1/S2; prompt histories and text buffer in S2.5/S3; BBoN judge for rollout selection | `rg`, indexes, titles/descriptions, authored links, review reports |
| Lineage | Mostly implicit after summary promotion; richer in raw OSWorld result directories | Explicit source links, review metadata, archived replacements, generated indexes |
| Behavioral authority | Advice/context for planner and worker; in-run instruction surface for actions; evaluation/ranking force in BBoN | Knowledge-artifact context plus stronger system-definition artifacts such as instructions, validators, commands, and schemas |
| Lifecycle | Add-if-missing JSON entries, local folder deletion, message flushing, benchmark result directories | Status, archive, replacement, validation, review gates, curated navigation |

Agent-S is stronger where the goal is immediate GUI action under bounded context. It has carefully engineered prompt surfaces for screenshots, action APIs, reflection, text buffers, code execution, and grounding models. Commonplace is not trying to operate a desktop in real time, so its memory surfaces are slower but more inspectable.

Commonplace is stronger on provenance and lifecycle. Agent-S's S1/S2 summaries can help a later task, but the stored memory does not retain enough source trace, review state, confidence, or invalidation metadata for a future agent to audit it without rerunning or finding external logs. BBoN result directories preserve richer traces, but they live in the evaluation workflow rather than the runtime memory substrate.

The most important design drift is that Agent-S moved away from durable experience memory in the default path. S2 advertises a continually updated KB, while S3's current runtime emphasizes reflection, local code execution, and BBoN rollout selection. That makes Agent-S less like a persistent knowledge base than earlier versions suggest.

**Read-back:** push — runtime code retrieves embedding-nearest experience summaries and injects them into planner or worker prompts.

## Borrowable Ideas

**Split task-level and subtask-level experience.** Ready to borrow conceptually. Agent-S's narrative/episodic split is crude but useful: whole-task plans and subtask action recipes have different retrieval keys and consumers. Commonplace already has different artifact types; a workshop layer could still benefit from making task and subtask learning surfaces explicit.

**Use a scratch text buffer for intra-task recall.** Ready for agent runtimes, not for the library layer. `save_to_knowledge(...)` is a tiny but useful primitive: it lets the acting agent preserve copied text, discovered facts, or element descriptions without promoting them to durable memory.

**Treat code execution as a delegated modality with a structured handoff.** Worth borrowing for GUI or document workflows. S3's code agent returns completion reason, summary, step count, budget, and execution history, then the GUI worker must verify the result. The authority split is good: code can do bulk work, but the GUI worker retains task completion authority.

**Use trajectory fact captions for rollout evaluation.** Useful for benchmarks and review gates. BBoN's before/after/action captions are a compact evidence layer between raw screenshots and final judge choice. Commonplace could use an analogous derived evidence layer for long semantic-review runs, but only if the raw trace remains reachable.

**Do not borrow summary-only promotion as sufficient memory.** Agent-S shows the weakness clearly. A trajectory-derived prose summary can improve future prompts, but without source trace references, confidence, update policy, or retirement rules, it is hard to trust as long-lived KB content.

## Trace-derived learning placement

**Trace source.** Agent-S qualifies as trace-derived learning in two different ways. In S1/S2, the raw traces are task and subtask execution trajectories assembled from reflections, plans, grounded actions, subtask status, and screenshots observed during a run. In S3 BBoN, the raw traces are benchmark result directories containing step screenshots, `traj.jsonl` records, rewards, final results, and instructions.

**Extraction.** S1/S2 extraction is LLM summarization. `update_narrative_memory(...)` summarizes the whole task trajectory under the search-query key, and `update_episodic_memory(...)` summarizes completed subtask trajectories under a subtask key. BBoN extraction is a separate evaluation pipeline: a behavior narrator turns before/after screenshot pairs and executed actions into fact captions, then a comparative judge selects among multiple trajectories for tasks where rollout results vary.

**Storage substrate.** S1/S2 distilled state lives in local JSON files under `{memory_root_path}/{memory_folder_name}/{platform}/`, with embeddings cached in `embeddings.pkl`. Raw benchmark traces live as files in OSWorld result directories: screenshots, `traj.jsonl`, `instruction.txt`, and `result.txt`. BBoN distilled evidence and decisions live in `fact_captions.jsonl` and JSON judge result files.

**Representational form.** S1/S2 memory is prose summaries plus distributed-parametric embedding vectors used for retrieval. The embeddings are a derived retrieval index over text keys, not learned agent weights. S3 runtime memory is mostly prompt text and Python/Bash execution history. BBoN artifacts are mixed: prose fact captions, image files, symbolic JSON records, and numeric scores.

**Lineage.** Lineage is strongest before distillation and weaker after. S1/S2 summaries are derived from trajectories but do not store direct links back to screenshots or result files. BBoN preserves better file-level lineage because captions and judge outputs are generated inside task directories or against named result directories.

**Behavioral authority.** S1/S2 summaries are knowledge artifacts when retrieved into planner/worker prompts: they advise future action without enforcing it. The scratch text buffer is in-run working context. S3 code-agent results have stronger local authority because they are inserted as a structured handoff that the GUI worker is instructed to verify before finishing. BBoN fact captions and judge records are system-definition artifacts in the evaluation path: they rank or select rollouts and affect benchmark score calculation, but they do not instruct the deployed S3 agent.

**Scope.** S1/S2 experience memory is platform-local and folder-local. It can be seeded from release assets, then grows in the user's local KB directory. BBoN scope is per benchmark experiment and per result directory set.

**Timing.** S1/S2 learning is online during CLI use when the task reaches done/subtask boundaries. BBoN learning is offline after collecting multiple rollouts. S2.5/S3 prompt reflection is online but mostly transient, so it is adaptation during a run rather than durable learning.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), Agent-S splits across two branches: S1/S2 are trajectory-to-prose-memory systems, while S3 BBoN is trajectory-to-evaluation-evidence and rollout-selection. It weakens any single-axis claim that "Agent-S memory" is one thing across releases, and it strengthens the distinction between runtime memory and benchmark-time trace distillation.

## Curiosity Pass

The README's current headline is S3, but the durable experience-memory implementation is strongest in S1/S2. At this commit, the default console script points to S3, whose live agent path does not load the S1/S2 JSON experience KB.

The phrase "long-term knowledge bank" in `save_to_knowledge(...)` is misleading for S2.5/S3. The implementation appends to an in-memory list on the grounding agent. That is useful working memory, not durable memory.

The S2 `KnowledgeBase` contains a more encapsulated trajectory API (`initialize_task_trajectory`, `update_task_trajectory`, `finalize_task`) in addition to the `AgentS2.update_*_memory(...)` methods used by the CLI path. The duplication suggests the memory lifecycle was being refactored, but the current review should trust the called path, not the nicer unused interface.

BBoN is impressive as an evaluation wrapper, but it is not an experience replay system. It selects a trajectory after several runs; it does not produce a reusable rule, skill, prompt patch, or training datum for later Agent-S execution.

The code-agent handoff is the most practical S3 memory-adjacent mechanism. It gives the GUI worker a compact account of what was attempted programmatically, but the result is cleared after prompt injection, so it behaves as short-term working memory.

## What to Watch

- Whether S3 reintroduces a durable memory substrate or keeps treating reflection and code-agent handoff as task-local context.
- Whether release KB assets for S2 gain manifest metadata, provenance, versioning, or review state beyond ZIP distribution.
- Whether BBoN fact captions become reusable training/evaluation data for prompt patches, skills, or model fine-tuning.
- Whether code-agent execution histories are persisted and reused across tasks, which would move S3 closer to executable-artifact memory.
- Whether the duplicate S2 knowledge lifecycle paths converge into one maintained API.
- Whether default runtime settings keep S3's security-sensitive local code execution enabled only behind explicit user choice.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Agent-S spans trajectory-to-prose memory and trajectory-to-evaluation-evidence rather than one trace-derived pattern.
- [OS-Copilot](./OS-Copilot.md) - compares-with: both are desktop computer-use agents, but OS-Copilot promotes successful execution into retrievable tools while Agent-S S3 mostly keeps code execution task-local.
- [SkillWeaver](./SkillWeaver.md) - compares-with: both inspect GUI/web trajectories, but SkillWeaver promotes executable browser APIs while Agent-S S1/S2 promote prose summaries and S3 BBoN selects rollouts.
- [ReasoningBank](./reasoning-bank.md) - compares-with: both extract reasoning or experience from trajectories into reusable prompt context, but Agent-S uses a thinner JSON summary lifecycle.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - qualifies: Agent-S S1/S2 perform deploy-time prose-memory learning, while S3 shifts toward transient adaptation and offline selection.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: Agent-S requires separating storage substrate, representational form, lineage, and behavioral authority across JSON memories, prompt buffers, execution histories, and BBoN artifacts.
