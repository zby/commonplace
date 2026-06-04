---
description: "Agent-S review: GUI-agent framework with S2 trace-summarized episodic/narrative memory, embedding read-back, and S3 transient reflection/code-agent context"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# Agent-S

Agent-S, from Simular AI's `simular-ai/Agent-S` repository, is a GUI-agent framework for computer-use tasks across Linux, macOS, and Windows. The current package entry point runs Agent S3, a simplified worker loop with reflection, visual/text grounding, an optional local code agent, and Behavior Best-of-N tooling. The strongest durable memory system, however, is in the S2 path: it stores task and subtask trajectory summaries as JSON, caches embeddings and web/RAG results, and injects retrieved experience into later planner and worker prompts.

**Repository:** https://github.com/simular-ai/Agent-S

**Reviewed commit:** [73ea17225bae73ab45d077cc442978d3ff8e286a](https://github.com/simular-ai/Agent-S/commit/73ea17225bae73ab45d077cc442978d3ff8e286a)

**Last checked:** 2026-06-01

## Core Ideas

**The repo contains multiple agent generations with different memory contracts.** `setup.py` exposes `agent_s=gui_agents.s3.cli_app:main`, and the top-level README documents S3 as the recommended path ([setup.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/setup.py), [README.md](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/README.md)). S1 and S2 carry a persistent knowledge-base design; S2.5 and S3 move toward a flatter worker loop with bounded trajectory context, reflection, grounding, and optional code execution.

**S2's memory is a local file-backed experience store.** `AgentS2` builds `local_kb_path` from `memory_root_path` and `memory_folder_name`, can download a default release knowledge base, and initializes a `KnowledgeBase` with platform-specific `episodic_memory.json`, `narrative_memory.json`, `embeddings.pkl`, query-cache JSON, and RAG-cache JSON paths ([gui_agents/s2/agents/agent_s.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/agent_s.py), [gui_agents/s2/core/knowledge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/core/knowledge.py), [gui_agents/utils.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/utils.py)). The stored unit is not a raw transcript; it is an LLM summary of either a full task trajectory or a subtask trajectory.

**Read-back is relevance-gated and pushed into planner/worker prompts.** At the first S2 planning turn, the manager formulates a search query, retrieves the most similar narrative experience by embedding similarity, optionally retrieves web/RAG knowledge, fuses it, and appends the result to the task instruction before the planner prompt is installed ([gui_agents/s2/agents/manager.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/manager.py), [gui_agents/s2/core/knowledge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/core/knowledge.py)). At each new subtask, the worker builds a subtask query from the search query, subtask name, and subtask info, retrieves the most similar episodic experience, rewrites element ids to generic descriptions, and inserts the result into the worker's task instruction ([gui_agents/s2/agents/worker.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/worker.py)).

**Trace summarization is the learning step.** S2 accumulates whole-task and per-subtask trajectories from planner/executor metadata, then summarizes them through dedicated prompts before saving them in JSON memory files ([gui_agents/s2/core/knowledge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/core/knowledge.py), [gui_agents/s2/memory/procedural_memory.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/memory/procedural_memory.py)). This is a trace-to-prose memory loop: past action traces become concise advice that future agents may use.

**S3 trades persistent memory for bounded transient context.** `AgentS3` has one worker; it keeps `worker_history`, `reflections`, and screenshots in memory, flushes older images or turns by `max_trajectory_length`, and prepends the latest reflection plus `Current Text Buffer` from `grounding_agent.notes` to each next worker message ([gui_agents/s3/agents/agent_s.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/agent_s.py), [gui_agents/s3/agents/worker.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/worker.py), [gui_agents/s3/agents/grounding.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/grounding.py)). The `save_to_knowledge` action name is misleading for durable-memory comparison: it appends to an in-process notes list and returns `WAIT`.

**S3 adds a code-agent subloop and an offline best-of-N evaluator.** The optional `call_code_agent` action runs a separate code agent against an environment controller, stores a structured result, and pushes that result into the next worker prompt for GUI verification ([gui_agents/s3/agents/grounding.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/grounding.py), [gui_agents/s3/agents/code_agent.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/code_agent.py)). The OSWorld S3 harness saves screenshots, trajectory JSONL, and scores; Behavior Best-of-N can turn those trajectories into fact captions and use a comparative judge to select among rollout directories ([osworld_setup/s3/lib_run_single.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/lib_run_single.py), [osworld_setup/s3/bbon/generate_facts.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/bbon/generate_facts.py), [osworld_setup/s3/bbon/run_judge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/bbon/run_judge.py)).

## Artifact analysis

- **Storage substrate:** `files` — Platform-scoped JSON files under the user-selected local KB directory, notably `narrative_memory.json` and `episodic_memory.json`
- **Representational form:** `prose` `symbolic` `parametric` — Prose trajectory summaries and prompts, symbolic JSON caches/DAG contracts/action records, and embedding vectors for retrieval
- **Lineage:** `authored` `imported` `trace-extracted` — Authored procedural prompts and framework code, optional imported default KB assets, and trajectory-derived summaries/caches
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` `validation` `learning` — Stored experience is knowledge when inspected, prompts instruct, embeddings route and rank read-back, verification/evaluation artifacts validate outcomes, and trajectory summarization learns reusable advice

**S2 narrative and episodic memory JSON.** Storage substrate: platform-scoped JSON files under the user-selected local KB directory, notably `narrative_memory.json` and `episodic_memory.json`. Representational form: prose summaries keyed by task/search-query text or subtask trajectory preambles. Lineage: derived from planner/executor trajectories, reflections, subtask status transitions, and LMM summarization prompts; default seed KBs can also be downloaded from GitHub release assets. Behavioral authority: system-definition artifacts when embedding-retrieved and inserted into planner or worker prompts as advice for future actions; knowledge artifacts when inspected as remembered experience. The promotion path is raw trajectory to summarized prose to retrieved prompt advice, without a deterministic validator between summary and reuse.

**S2 embeddings and retrieval caches.** Storage substrate: `embeddings.pkl`, `formulate_query.json`, and `{search_engine}_rag_knowledge.json` under the same platform KB path. Representational form: distributed-parametric embeddings plus symbolic JSON caches. Lineage: embeddings are derived from task instructions and stored memory keys; query and RAG caches are derived from LLM query formulation, LLM internal search, or Perplexica calls. Behavioral authority: ranking and routing system-definition artifacts because they decide which memory is pushed into planner/worker context. Precision, recall, and whether the injected memory improves action quality are not verified by the code.

**S2 procedural prompts and DAG translator.** Storage substrate: Python constants and dynamic prompt constructors in `gui_agents/s2/memory/procedural_memory.py`. Representational form: prose instructions with a symbolic JSON DAG contract. Lineage: authored framework code. Behavioral authority: system-definition artifacts that define planning, subtask execution, reflection, summarization, and graph translation. They constrain the agent more strongly than retrieved memories because every S2 run consumes them.

**S3 transient worker context and text buffer.** Storage substrate: Python object fields such as `generator_agent.messages`, `reflection_agent.messages`, `worker_history`, `reflections`, `screenshot_inputs`, and `grounding_agent.notes`. Representational form: mixed prose, image messages, action code strings, and list entries. Lineage: derived online from the current task, screenshots, generated plans, reflections, and `save_to_knowledge` calls. Behavioral authority: short-lived system-definition context for the next action within the same episode; not durable memory because it resets with the agent object and is bounded by flushing.

**S3 code-agent execution records.** Storage substrate: transient dictionaries in `last_code_agent_result`, plus logs when logging is configured. Representational form: symbolic fields (`completion_reason`, `steps_executed`, `budget`) plus prose summaries and executable code snippets. Lineage: derived from a worker-triggered `call_code_agent` action, code-agent LMM responses, environment-controller execution results, and a summary prompt. Behavioral authority: advisory system-definition context for the next GUI action, especially verification; it does not persist as a future-task memory store in this code.

**OSWorld trajectories and Behavior Best-of-N facts/results.** Storage substrate: per-task result directories with `step_*.png`, `traj.jsonl`, `instruction.txt`, `result.txt`, `fact_captions.jsonl`, and judge output JSON. Representational form: mixed screenshots, symbolic metrics, action traces, fact-caption prose, and selected-trajectory paths. Lineage: generated from OSWorld rollouts and environment scores; fact captions are LMM-derived from before/after screenshots and pyautogui actions; judge outputs are derived from final screenshots and fact captions. Behavioral authority: evaluation and selection artifacts for benchmark runs, not persistent agent memory for later tasks unless an external workflow feeds them back.

## Comparison with Our System

| Dimension | Agent-S | Commonplace |
|---|---|---|
| Primary purpose | Operate desktop GUIs and benchmark computer-use agents | Maintain a typed methodology KB for future agents and maintainers |
| Main durable memory | S2 JSON summaries, embeddings, query/RAG caches, release KB assets | Git-tracked markdown artifacts, type specs, generated indexes, review outputs |
| Learning loop | Trace summarization into task/subtask experience | Source-grounded writing, review, validation, and workshop-to-library promotion |
| Read-back | Embedding-selected experience pushed into planner/worker prompts in S2; transient always-load context in S3 | Pull through search/indexes/links, plus explicit instructions and generated context where configured |
| Governance | Prompt instructions, embedding similarity, cached JSON, benchmark evaluation | Collection contracts, schemas, deterministic validation, semantic review, git history |

Agent-S is closer to Commonplace than most GUI-agent repos because S2 explicitly separates raw trajectory, summarized experience, retrieval, and prompt injection. Both systems treat retained prose as behavior-shaping context, but Commonplace makes the artifact lifecycle inspectable and reviewable in Git, while Agent-S keeps memory as local JSON and pickle files whose quality depends mostly on LMM summaries and embedding similarity.

The largest divergence is authority. In Commonplace, a note, instruction, index, or validation rule has an explicit type and review surface before it shapes later work. In Agent-S S2, once a trajectory summary is written, embedding retrieval can insert it into future planner or worker prompts with no schema-level quality gate. That is pragmatic for task automation, but it makes stale or overfit experiences harder to audit.

S3 is useful as a contrast because it intentionally cuts durable memory out of the main path. It pushes recent reflection, text-buffer notes, and code-agent results into the next action, then bounds context by image/turn flushing. That keeps runtime context manageable and reduces the operational burden of maintaining a KB, but loses S2's cross-task learning surface.

**Read-back:** `push` — S2 uses retrieval machinery internally, but from the planner/worker perspective embedding-selected narrative and episodic experience are pushed into prompts before action; S3 mainly uses always-loaded transient episode context, not durable memory read-back

### Borrowable Ideas

**Make task/subtask summaries a first-class trace-derived candidate.** Agent-S's split between full-task narrative memory and subtask episodic memory maps well to Commonplace review or validation runs. A Commonplace analogue would save a failed or successful run summary at two granularities before deciding whether any lesson should become a durable instruction. Ready as a workshop artifact; not ready for automatic promotion.

**Separate retrieval targets by consumer.** Agent-S retrieves narrative experience for the manager and episodic experience for the worker. Commonplace could apply the same distinction by assembling different context packets for planner, writer, reviewer, and validator roles. Ready where those roles are already explicit; otherwise needs a concrete multi-agent workflow.

**Cache query formulation as an inspectable artifact.** `formulate_query.json` records the search query chosen for an instruction. Commonplace could retain generated search plans or review-bundle selectors to make later retrieval decisions auditable. Ready for generated reports if paired with source and prompt metadata.

**Use code-agent result summaries as handoff context, not final authority.** S3's GUI worker must verify code-agent changes after receiving the code result. Commonplace can borrow that authority split for automation: programmatic edits can propose a state change, but a separate read/review path should confirm it before completion. Ready as an instruction pattern.

**Keep best-of-N facts separate from winner selection.** Behavior Best-of-N first derives fact captions from trajectories, then uses a comparative judge over those facts and screenshots. Commonplace could use a similar two-stage review for multiple generated drafts: fact extraction first, preference judgment second. Needs a high-value generation workflow before implementation.

## Trace-derived learning placement

- **Trace source:** `trajectories` — S2 learns from task and subtask trajectories, and S3/OSWorld writes rollout trajectories for evaluation facts
- **Learning scope:** `per-task` `cross-task` — S3 reflection and OSWorld artifacts are per-episode/per-task, while S2 summaries are reused across later tasks in the local KB
- **Learning timing:** `online` `offline` `staged` — S2 summarizes when subtasks/tasks close during a run, S3 reflection is online, and OSWorld/Behavior Best-of-N distillation is offline evaluation work
- **Distilled form:** `prose` — The reusable S2 memory is prose task/subtask experience; Behavior Best-of-N distills trajectories into fact-caption prose

**Trace source.** Agent-S qualifies as trace-derived learning through S2. The raw traces are task and subtask trajectories assembled from task/search-query text, subtask names and instructions, executor plans, reflections, subtask status transitions, screenshots in the live prompt path, and OSWorld result artifacts. S3's OSWorld harness also writes `traj.jsonl` with plans, actions, rewards, done flags, info, and screenshot filenames.

**Extraction.** S2 extraction is summarization. The narrative summarizer turns a whole-task trajectory into a reusable task-level plan or failure explanation; the episode summarizer turns a subtask trajectory into a smaller plan/action memory with generic element-description placeholders. Behavior Best-of-N extraction is evaluative rather than a future-memory loop: it captions before/after screenshot changes from saved trajectories and asks a comparative judge to select the better rollout.

**Scope and timing.** S2 memory is local-KB and platform scoped. Retrieval runs at the first planning turn for narrative memory and at worker initialization for each subtask's episodic memory. Writes happen when subtask trajectories close and when a task finalizes. S3 reflection and code-agent summaries are online and per-episode; OSWorld trajectory artifacts are offline benchmark outputs.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Agent-S belongs in the trace-to-prose-experience family for S2 and in the trace-to-evaluation-facts family for S3 Behavior Best-of-N. It strengthens the survey split between raw trajectory retention and behavior-changing distilled artifacts: S2 summaries are the reusable behavior-shaping memory, while S3 trajectories and fact captions mostly support evaluation unless another workflow feeds them back.

## Read-back placement

**Direction.** Agent-S memory read-back is push. S2 uses pull-style retrieval internally, but the selected memory is pushed into the planner or worker prompt before the receiving agent chooses its next action. S3 pushes current-episode reflection, text-buffer notes, and code-agent results into the next worker turn when present, but those objects are transient episode context rather than retained memory read-back.

**Read-back signal:** `inferred / embedding` — S2 selects narrative and episodic memory by embedding similarity against the task instruction or subtask query before injecting it into prompts.

**Read-back timing:** `pre-action` — S2 read-back reaches the planner or worker prompt before the receiving agent plans or acts.

**Faithfulness tested:** `no` — The reviewed code has OSWorld evaluation and Behavior Best-of-N selection, but no isolated memory read-back ablation or perturbation test.

**Targeting and signal.** S2's memory push is instance-targeted with an inferred / embedding signal. The trigger is first-turn planning or first-turn subtask execution, and narrative and episodic memories are selected by embedding similarity against the task instruction or subtask query key. Optional web/RAG knowledge is selected through a formulated query and optional search engine, but it is not the trace-derived experience path. S3's reflection and code-agent result injection is event-keyed rather than semantic retrieval: if a previous action/reflection/code result exists, it is included.

**Timing relative to action.** S2 read-back happens before planning or subtask execution, so it can change the next plan or action. S3 reflection happens after the previous action and before the next action, so it can steer recovery. Behavior Best-of-N selection happens after complete rollouts, so it changes which trajectory is selected, not the steps inside that already-finished rollout.

**Selection, scope, and complexity.** S2 selects one nearest narrative or episodic memory, excluding the exact same key when it is the top match. It does not implement a token budget, source freshness check, or multi-candidate diversity policy for retrieved memory. S3 bounds complexity by flushing older images for long-context providers and older turns for other providers, but its transient text buffer has no durable curation policy.

**Authority at consumption.** Retrieved S2 memories are advisory prose appended into task instructions, but because the same prompt drives planner/worker behavior, they function as soft system-definition artifacts. S3 reflection and code-agent summaries are also advisory, with stronger verification guidance around code-agent outputs. The code does not test whether injected memory actually changes behavior in the intended direction.

**Faithfulness.** I did not find a WITH/WITHOUT memory ablation or perturbation test in the inspected code. OSWorld evaluation and Behavior Best-of-N measure task outcomes and select rollouts, but they do not isolate memory read-back faithfulness.

**Other consumers.** Humans can inspect local JSON memory, OSWorld trajectory files, fact captions, logs, and result scores. The OpenClaw integration wraps the S3 CLI as a callable external skill, which makes Agent-S itself a tool-like consumer surface rather than adding a new memory store ([integrations/openclaw/agent_s_wrapper.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/integrations/openclaw/agent_s_wrapper.py)).

## Curiosity Pass

**The README's learning claim is true for S2, less so for S3's default entry point.** The repo introduction says Agent-S can learn from past experiences, and S2 implements that through durable narrative and episodic memory. The installed `agent_s` command runs S3, where memory is mostly per-episode reflection and notes.

**`save_to_knowledge` sounds more durable than it is in S3.** The docstring calls it a long-term knowledge bank, but the implementation appends to `self.notes` on the ACI instance. It is useful scratchpad context, not persistent cross-task memory.

**The query key is doing a lot of work.** S2 stores narrative memory under `current_search_query`, not directly under the original instruction, and the subtask key includes the search query plus subtask text. That may improve generalization when queries normalize tasks, but it also makes memory identity depend on an LMM-generated intermediary.

**The repository keeps benchmark artifacts and memory artifacts adjacent but distinct.** OSWorld trajectories are rich traces, and Behavior Best-of-N distills them into facts, but the inspected code does not route those facts back into S2/S3 as reusable memory.

**S3's code agent is an authority experiment.** It gives a sub-agent permission to execute code, but the main GUI worker is instructed to verify through the GUI before declaring done. That explicit split between programmatic modification and perceptual verification is more interesting than the code execution itself.

## What to Watch

- Whether S3 reintroduces durable cross-task memory; that would determine whether the default `agent_s` path remains a transient agent or becomes the main memory-bearing system again.
- Whether S2 memories gain schema fields for source trajectory ids, prompt/model versions, timestamps, success scores, and review state; that would make stale or harmful experience easier to invalidate.
- Whether retrieval expands beyond single nearest-neighbor experience with budgets, diversity, or confidence thresholds; that would change the read-back path from simple top-match injection to governed context assembly.
- Whether Behavior Best-of-N fact captions are fed back into training or memory, rather than only selecting among rollouts; that would turn the evaluation pipeline into a learning loop.
- Whether the code-agent verification contract is tested with failure cases; that would make the handoff pattern more borrowable for Commonplace automation.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - compares: Agent-S S2 distills task and subtask trajectories into reusable prose experience, while S3 Behavior Best-of-N distills trajectories into evaluation facts.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Agent-S requires separating JSON experience, embeddings, prompt templates, transient notes, code-agent results, trajectories, and judge outputs by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: raw trajectories, screenshots, logs, fact captions, and result files are evidence unless a read-back or selection path consumes them.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: S2 retrieved summaries, embeddings as ranking inputs, procedural prompts, and code-agent handoff prompts shape later behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: S2 extracts reusable task/subtask experience from execution traces instead of replaying full transcripts.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Agent-S shows both sides, with S2 relevance-gated activation and S3 benchmark traces that remain inert unless consumed by an evaluator.
