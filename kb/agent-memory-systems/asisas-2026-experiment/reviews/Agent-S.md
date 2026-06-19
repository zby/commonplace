---
description: "Agent-S review: GUI agent framework with S1/S2 JSON experience memory, embedding retrieval, S3 reflection, and BBON trace evaluation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
tags: [trace-derived]
---

# Agent-S

Agent-S, from Simular AI's `simular-ai/Agent-S` repository, is a Python framework for multimodal GUI agents. At the reviewed commit, its durable memory surface is mainly in the legacy/current S1 and S2 agents: task-level narrative summaries, subtask-level episodic summaries, cached embeddings, query caches, and optional imported release KB data. The current installed console entry point runs Agent S3, which removes the S1/S2 JSON experience store from the main package path and instead uses task-local reflection, bounded message history, optional local code execution, and OSWorld/BBON trace-evaluation utilities.

**Repository:** https://github.com/simular-ai/Agent-S

**Reviewed commit:** [73ea17225bae73ab45d077cc442978d3ff8e286a](https://github.com/simular-ai/Agent-S/commit/73ea17225bae73ab45d077cc442978d3ff8e286a)

**Source directory:** `related-systems/simular-ai--Agent-S`

## Core Ideas

**Agent generation matters: S1/S2 and S3 have different memory contracts.** The checkout contains `gui_agents/s1`, `gui_agents/s2`, `gui_agents/s2_5`, and `gui_agents/s3`, while `setup.py` installs `agent_s=gui_agents.s3.cli_app:main` ([setup.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/setup.py)). S1's `GraphSearchAgent` and S2's `AgentS2` maintain a local knowledge base under `memory_root_path/memory_folder_name`; S3's `AgentS3` has no equivalent durable KB object and relies on per-run worker/reflection state ([gui_agents/s1/core/AgentS.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s1/core/AgentS.py), [gui_agents/s2/agents/agent_s.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/agent_s.py), [gui_agents/s3/agents/agent_s.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/agent_s.py)).

**S1/S2 store two levels of experience as JSON summaries.** The `KnowledgeBase` classes set `episodic_memory.json`, `narrative_memory.json`, and `embeddings.pkl` paths under the local KB directory and platform subdirectory ([gui_agents/s1/core/Knowledge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s1/core/Knowledge.py), [gui_agents/s2/core/knowledge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/core/knowledge.py)). Narrative memory summarizes whole task trajectories; episodic memory summarizes subtask trajectories. The stored values are LLM-produced prose reflections over trace text, keyed by task/search-query or subtask description.

**Retrieval uses embeddings and first-turn prompt injection.** S1/S2 compute or reuse embeddings for the current instruction and stored keys, rank candidates with cosine similarity, and return the most similar non-identical entry ([gui_agents/s2/core/knowledge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/core/knowledge.py)). The manager retrieves task-level narrative experience at planning turn zero; the worker retrieves subtask-level episodic experience at executor turn zero and appends it to the task instruction before the generator prompt is finalized ([gui_agents/s2/agents/manager.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/manager.py), [gui_agents/s2/agents/worker.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/worker.py)).

**Context efficiency is small-k recall plus trajectory truncation, not governed packing.** The S1/S2 retrieval path selects one narrative or one episodic neighbor, and optional web/LLM search results are cached by instruction in `*_rag_knowledge.json` ([gui_agents/s2/core/knowledge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/core/knowledge.py)). S3 bounds context by `max_trajectory_length`: long-context model paths keep recent images while retaining text, while other paths drop old turns from generator and reflection histories ([gui_agents/s3/agents/worker.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/worker.py)). There is no token-budgeted memory packer, multi-hop memory expansion, or faithfulness audit for retrieved experience.

**S3 moves the live agent toward task-local reflection and tool result reuse.** S3's worker creates a reflection agent, adds per-step reflections to the next generator message, optionally includes a `CODE AGENT RESULT` section from the grounding agent, and clears that result after injection ([gui_agents/s3/agents/worker.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/worker.py)). This is memory-like within a task, but it is not durable cross-task retention in the package's live entry point.

**BBON is trace-derived evaluation, not the normal read-back path.** OSWorld runners save screenshots, `traj.jsonl`, and `result.txt`; BBON scripts generate `fact_captions.jsonl` from screenshot/action transitions and use a comparative judge to select among result directories ([osworld_setup/s3/lib_run_single.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/lib_run_single.py), [osworld_setup/s3/bbon/generate_facts.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/bbon/generate_facts.py), [osworld_setup/s3/bbon/run_judge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/bbon/run_judge.py)). These traces shape evaluation and trajectory selection experiments, but the S3 runtime does not reload BBON results as future action memory.

## Artifact analysis

- **Storage substrate:** `files` — S1/S2 memories persist as local JSON and pickle files; initial KB assets can be imported from GitHub release ZIPs; LLM/search/grounding services supply summaries, embeddings, web-like search results, reflections, and action grounding.
- **Representational form:** `prose` `symbolic` `parametric` — Narrative and episodic summaries are prose; file names, JSON keys, subtask/status fields, cached query maps, result records, and code prompts are symbolic; embedding vectors and LLM/grounding model state are parametric.
- **Lineage:** `authored` `imported` `trace-extracted` — Procedural prompts and agent code are authored; default KB ZIPs are imported release assets; narrative/episodic summaries, reflections, OSWorld trajectories, fact captions, and BBON judge outputs are derived from agent execution traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Retrieved memories advise planners/workers as contextual knowledge; procedural prompts instruct the agents; managers/workers route task/subtask control; OSWorld and BBON outputs validate trajectories; embedding similarity ranks memories; summary agents transform traces into reusable experience.

**S1/S2 local knowledge base.** Storage substrate: files under `{memory_root_path}/{memory_folder_name}/{platform}/`, notably `narrative_memory.json`, `episodic_memory.json`, `embeddings.pkl`, `formulate_query.json`, and optional `{search_engine}_rag_knowledge.json`. Representational form: prose summaries and cached search results plus symbolic JSON keys/status fields and parametric embeddings. Lineage: imported baseline KB data when `download_kb_data()` is used, then trace-extracted summaries from live task/subtask trajectories. Behavioral authority: knowledge and ranking, because retrieved summaries are selected by embedding similarity and inserted into planning/execution prompts.

**S1/S2 trajectory summarizers.** Storage substrate: repository prompt/code plus retained JSON summary outputs. Representational form: authored prose prompts and symbolic write logic that produce prose summary entries. Lineage: generated from trajectory strings assembled from reflection and executor plan fields in the CLI/agent loop ([gui_agents/s1/cli_app.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s1/cli_app.py), [gui_agents/s2/agents/agent_s.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/agent_s.py)). Behavioral authority: learning, because successful or completed trajectories become future retrieved experience.

**S3 reflection and worker history.** Storage substrate: in-process `Worker` fields and LLM message histories, not a durable store. Representational form: prose reflection text, symbolic message records, screenshots, plan code, and optional code-agent result summaries. Lineage: trace-extracted inside the current task. Behavioral authority: instruction/knowledge during the next action, but only for the active run; reset discards this state.

**S3 OSWorld/BBON trace artifacts.** Storage substrate: result directories containing screenshots, `traj.jsonl`, `result.txt`, `fact_captions.jsonl`, and `BoN{i}.json` outputs. Representational form: symbolic JSON/JSONL records plus prose fact captions and judge thoughts. Lineage: trace-extracted from OSWorld rollouts and screenshot/action deltas. Behavioral authority: validation and ranking for experiment selection; not a deployed memory read-back channel in `AgentS3`.

**Procedural prompts and action surfaces.** Storage substrate: repository Python modules under `gui_agents/*/memory/procedural_memory.py` and agent/grounding code. Representational form: prose instructions plus symbolic action schemas and parser/formatter checks. Lineage: authored. Behavioral authority: instruction, routing, and validation, because these prompts define how agents plan, reflect, ground actions, and check formatted outputs.

**Promotion path.** S1/S2 promote raw task execution into durable advice through a small pipeline: trajectory text -> LLM summary -> JSON memory entry -> embedding cache -> prompt-injected retrieved experience. S3's BBON pipeline promotes evaluation traces into fact captions and comparative selections, but stops at evaluation artifacts rather than updating the live agent's durable memory.

## Comparison with Our System

Agent-S and Commonplace both treat previous agent work as material that should change future behavior, but Agent-S is runtime-first while Commonplace is artifact-first. Agent-S stores compact experiential summaries and injects the nearest one into the GUI agent's next task/subtask prompt. Commonplace stores typed Markdown artifacts with explicit source links, validation, collection contracts, replacement history, and review workflows.

Agent-S has a more direct trace-to-action loop. A completed GUI trajectory can become a future planning hint without an intermediate human-readable review stage. That is useful for repeated UI tasks, but it makes provenance and invalidation weak: the JSON summary does not retain stable source citations, score context, review status, or contradiction handling.

Commonplace has stronger governance and weaker automatic recurrence. Its notes and indexes remain inspectable in git, and validation can reject malformed artifacts, but Commonplace does not automatically summarize every agent run into future advice. Borrowing from Agent-S would require a workshop or report layer that keeps the trace-derived candidate inspectable before promotion.

S3 is also a useful caution. The current installed path emphasizes task-local reflection, code-agent result reuse, and bounded message histories rather than cross-task memory. For Commonplace, that distinction matters: in-session reflection is valuable context engineering, but it is not a retained library artifact until something durable is written and made discoverable.

### Borrowable Ideas

**Two-level experience memory.** A Commonplace analogue would separate whole-task lessons from subtask/tool-operation lessons, with different retrieval keys and adoption thresholds. Ready as a workshop/report convention; durable library mutation needs review.

**First-turn experience injection.** Agent-S limits retrieved experience to the beginning of planning or subtask execution. Commonplace could use the same trigger for workflow-specific reminders instead of repeatedly injecting the same note on every turn. Ready when the workflow has a clear task/subtask boundary.

**Keep default knowledge distinct from learned experience.** Agent-S imports release KB assets and then continually appends learned summaries. Commonplace already has source notes versus generated reports; a trace-derived workflow should preserve that split explicitly. Ready as a design rule.

**Do not borrow unreviewed JSON memories as authoritative notes.** Agent-S summaries are useful hints, but they lack citations, validation, and replacement semantics. In Commonplace they should enter as candidate observations or review artifacts before becoming notes or instructions.

**BBON fact captions as evaluation evidence.** Turning screenshot/action traces into concise fact captions could help Commonplace review UI-agent runs or workflow demonstrations. Needs a concrete evaluation loop before becoming a standing system feature.

## Write side

**Write agency:** `manual` `automatic` — Operators choose agent versions, memory folders, imported KB assets, and run scripts manually; S1/S2 automatically formulate query caches, cache search results, summarize completed task/subtask trajectories, write JSON memories, and update embedding caches during execution. S3 and OSWorld/BBON scripts automatically write per-run trace/evaluation files when those workflows are invoked.

**Curation operations:** `synthesize` `promote` — S1/S2 synthesize new prose memory entries from trajectory text and promote them into prompt-affecting JSON memory through embedding retrieval. BBON synthesizes fact captions and promotes result directories into comparative selections. The code does not implement durable deduplication, contradiction invalidation, age decay, or in-place evolution of existing memory entries.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `trajectories` — S1/S2 consume task/subtask trajectory strings composed from reflections, executor plans, statuses, and action results; OSWorld/S3 evaluation saves screenshots, action records, rewards, and results in `traj.jsonl` and companion files.

**Learning scope:** `per-project` `cross-task` — The local KB is scoped by a user-selected memory folder and OS platform, then reused across future tasks within that environment. Imported release KBs are version/platform scoped.

**Learning timing:** `online` `offline` `staged` — S1/S2 write summaries during or at the end of normal inference runs; default KB imports and BBON evaluation/fact-caption generation are offline/staged script workflows.

**Distilled form:** `prose` `symbolic` `parametric` — The main distilled memory is prose summary text stored in symbolic JSON maps; embeddings provide parametric retrieval state; BBON outputs symbolic/prose comparative records.

**Extraction.** The S1/S2 oracle is the agent loop itself: completed task/subtask boundaries trigger summarization, and duplicate keys suppress repeat writes. The summarizers do not inspect environment reward or run a verifier before accepting a memory entry; they compress the trajectory text into reusable advice.

**Distillation trigger and policy.** Narrative memory is written when the CLI sees a done/fail action or `AgentS2.update_narrative_memory()` is called; episodic memory is written when a subtask boundary finalizes the prior subtask trajectory. The policy is append-if-key-missing, not merge, revise, or invalidate ([gui_agents/s2/agents/agent_s.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/agent_s.py), [gui_agents/s2/core/knowledge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/core/knowledge.py)).

**Survey placement.** Agent-S strengthens the survey distinction between trace-derived knowledge artifacts and stronger system-definition artifacts. Its raw trajectories and summaries are retained knowledge artifacts with advisory prompt authority; they do not become validators, route tables, or fine-tuned model weights. S3/BBON adds a separate trace-derived evaluation path, but the evaluated traces do not feed back into the live S3 agent as memory.

## Read-back

**Read-back:** `both` — S1/S2 expose explicit retrieval/search methods over retained memories, and the deployed manager/worker paths automatically insert selected narrative or episodic experience into first-turn planning/execution prompts. S3's normal entry point is mostly task-local reflection and does not read back the S1/S2 JSON KB.

**Read-back signal:** `inferred / embedding` `coarse` — S1/S2 use embedding similarity over the current instruction or constructed subtask key to select an instance-relevant prior experience; injection itself is a coarse first-turn rule in the manager/worker loop.

**Faithfulness tested:** `no` — The repository evaluates task performance and BBON trajectory selection, but the reviewed code does not implement a with/without-memory ablation, perturbation test, or audit proving that a retrieved memory changed a specific future action.

**Direction edge case.** The same S1/S2 method call is pull from the manager/worker implementation and push for the generator agent that receives the modified prompt. From the acting LLM's perspective, memory arrives unsolicited in the system/task instruction at the first planning or subtask turn.

**Selection, scope, and complexity.** Retrieval is top-one by cosine similarity over keys, with a skip when the nearest key equals the current instruction. Scope is platform-local and memory-folder-local. Complexity is low volume but high risk of stale advice: one summary can carry compressed assumptions without source citation, score, or freshness metadata.

**Injection point.** Read-back occurs before the planning or worker model call. S1/S2 managers retrieve narrative experience at first planning turn; workers retrieve episodic subtask experience at first executor turn. Later trajectory capture, summarization, and embedding writes are write-side maintenance, not another read-back moment.

**Authority at consumption.** Retrieved memories are advisory context: the prompt says the agent may refer to retrieved or similar experience if useful. They are not hard gates, validators, or route selectors, although their wording can influence the plan and grounded action.

**Other consumers.** Humans can inspect and delete the local JSON/pickle KB files, OSWorld traces, and BBON outputs. The release KB mechanism gives users an adoption affordance but also makes learned experience easy to wipe by deleting the local KB directory.

## Curiosity Pass

**The installed agent is less memory-centric than the legacy code.** The package entry point runs S3, while the durable experience KB lives in S1/S2. A review that only follows old `KnowledgeBase` paths would overstate current packaged memory behavior.

**Embedding retrieval keys are summaries' handles, not full semantic documents.** The code embeds task/subtask keys and retrieves one stored summary. That is efficient, but the ranking surface can miss a useful memory when the key wording differs from the operative lesson.

**Trace acceptance is weakly governed.** A completed or boundary-crossing trajectory can become memory without reward filtering, human review, or contradiction checks. The system trusts summarization and future embedding selection more than provenance.

**`embeddings.pkl` is an access structure, not the source of truth.** JSON memories hold the readable entries; embeddings are regenerated/cached for retrieval. Treating the pickle as the memory would obscure the prose-summary lineage.

**BBON is closer to evaluation memory than agent memory.** Fact captions and selected trajectories preserve useful behavioral evidence, but they currently serve comparative scoring rather than future prompt assembly.

## What to Watch

- Whether S3 adds a durable cross-task KB or reloads BBON/fact-caption outputs into the live agent. That would materially change the read-back verdict and storage analysis.
- Whether S1/S2 memory writes gain reward filtering, human review, contradiction handling, or invalidation. That would move the write side beyond simple synthesis/promotion.
- Whether release KB assets become inspectable in-repo or carry provenance metadata. That would clarify imported-memory authority.
- Whether the embedding retriever gains top-k packing, token budgets, or source-aware summaries. That would make context efficiency and trust easier to evaluate.
- Whether explicit ablations compare runs with and without retrieved narrative/episodic memory. That would strengthen the faithfulness claim.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: S1/S2 move stored memories into prompt context, while S3 task-local traces alone do not constitute durable read-back.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: Agent-S requires separating local JSON memory, embedding access structures, prompts, runtime reflections, and BBON traces.
- [Use trace-derived extraction as meta-learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - applies: S1/S2 summarize trajectories into future advisory context.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: narrative and episodic summaries are advisory evidence/context, not enforced rules.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: procedural prompts, action formatters, and BBON evaluation scripts configure behavior or evaluation.
- [Context engineering](../../../notes/definitions/context-engineering.md) - frames: Agent-S combines small retrieved experience injection with bounded task-local trajectory context.
- [Lineage](../../../notes/definitions/lineage.md) - frames: the key risk is weak trace provenance from raw trajectory to durable summary.
