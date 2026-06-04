---
description: "Agent-S review: GUI-agent framework with authored procedural prompts, S1/S2 episodic JSON memory, S3 task-local reflection, and BBON trace judging"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-04"
---

# Agent-S

> Replaced 2026-06-04. See [Agent-S](./Agent-S.md) for the current review.

Agent-S, from Simular AI, is an open-source computer-use agent framework for controlling desktop GUIs across Linux, macOS, and Windows. At the reviewed commit, the installed `agent_s` console entry point runs the S3 stack: a single worker agent, a grounding model for UI coordinates, optional reflection, optional local code execution, bounded screenshot history, and OSWorld behavior-best-of-N evaluation tooling. The repository also retains S1/S2 implementations with a more explicit knowledge-base path: downloaded seed knowledge plus JSON episodic and narrative memories updated from task trajectories.

**Repository:** https://github.com/simular-ai/Agent-S

**Reviewed commit:** [73ea17225bae73ab45d077cc442978d3ff8e286a](https://github.com/simular-ai/Agent-S/commit/73ea17225bae73ab45d077cc442978d3ff8e286a)

**Last checked:** 2026-06-04

## Core Ideas

**The current packaged agent favors task-local context over durable memory.** `setup.py` exposes `agent_s=gui_agents.s3.cli_app:main`, and `README.md` presents S3 as the primary SDK/CLI path ([setup.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/setup.py), [README.md](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/README.md)). S3's `AgentS3.reset()` creates one `Worker`; the worker rebuilds its generator and reflection agents on reset, then carries current-turn prompt history, reflections, screenshot inputs, a grounding-agent text buffer, and optional code-agent output inside the active run ([gui_agents/s3/agents/agent_s.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/agent_s.py), [gui_agents/s3/agents/worker.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/worker.py)). This is context engineering for a live desktop task, not a durable knowledge-base service.

**Procedural memory is mostly authored promptware plus reflected trajectory snippets.** S3's `PROCEDURAL_MEMORY` module constructs the worker system prompt from the available grounding-agent action methods, embeds detailed rules for GUI/code-agent choice, verification, and action formatting, and defines separate prompts for reflection, code execution, code summarization, behavior narration, and comparative trajectory judging ([gui_agents/s3/memory/procedural_memory.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/memory/procedural_memory.py)). These artifacts have high behavioral authority because they become system prompts, but their lineage is authored code, not learned memory.

**Context efficiency is bounded history plus prompt specialization.** S3 keeps all text for long-context providers while deleting older image parts after `max_trajectory_length`; for other providers it drops whole older turns from generator and reflection agents ([gui_agents/s3/agents/worker.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/agents/worker.py)). S3 also hides unavailable actions such as `call_code_agent` when no environment controller exists, injects only the current grounding-agent notes buffer, and clears the last code-agent result after adding it to the next worker prompt. This manages context volume and action-surface complexity, but it does not provide progressive disclosure over a durable store.

**S1/S2 carry the explicit durable memory mechanism.** Older `GraphSearchAgent`/`AgentS2` code initializes a local platform-specific `kb_s1` or `kb_s2` directory, optionally downloads seed knowledge from GitHub release assets, reads `narrative_memory.json` and `episodic_memory.json`, caches embeddings in `embeddings.pkl`, and writes summarized task and subtask trajectories after inference ([gui_agents/s1/core/AgentS.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s1/core/AgentS.py), [gui_agents/s1/core/Knowledge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s1/core/Knowledge.py), [gui_agents/s2/agents/agent_s.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/agent_s.py), [gui_agents/s2/core/knowledge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/core/knowledge.py), [gui_agents/utils.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/utils.py)). The S1 README explicitly describes a knowledge base that updates during inference and is seeded from release assets ([gui_agents/s1/README.md](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s1/README.md)).

**Read-back in S2 is instance-targeted at task and subtask boundaries.** On the first planning step, S2 formulates a search query, retrieves the most similar narrative experience by embedding similarity, optionally fuses that with web or LLM search results, and appends the integrated knowledge to the planner instruction. On the first executor step for a subtask, it retrieves similar episodic experience by embedding similarity and appends it to the worker instruction ([gui_agents/s2/agents/manager.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/manager.py), [gui_agents/s2/agents/worker.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/agents/worker.py), [gui_agents/s2/core/knowledge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s2/core/knowledge.py)). From the receiving planner/worker's perspective, this is pushed memory: the retrieved experience is inserted before the model call rather than requiring that agent to call a tool.

**S3's behavior-best-of-N is trace-derived evaluation, not a live memory store.** OSWorld S3 runs save screenshots and JSONL trajectory records per task; `generate_facts.py` turns screenshot pairs plus actions into fact captions, and `run_judge.py` uses fact captions plus initial/final screenshots to select among rollout directories ([osworld_setup/s3/lib_run_single.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/lib_run_single.py), [osworld_setup/s3/bbon/generate_facts.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/bbon/generate_facts.py), [osworld_setup/s3/bbon/run_judge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/osworld_setup/s3/bbon/run_judge.py), [gui_agents/s3/bbon/behavior_narrator.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/bbon/behavior_narrator.py), [gui_agents/s3/bbon/comparative_judge.py](https://github.com/simular-ai/Agent-S/blob/73ea17225bae73ab45d077cc442978d3ff8e286a/gui_agents/s3/bbon/comparative_judge.py)). That path learns from trajectories in the evaluation/selection sense; it does not write a reusable future-task memory artifact.

## Artifact analysis

- **Storage substrate:** `repo` `files` `vector` `in-memory` — Authored prompts and agent code live in the repository; S1/S2 memories persist as local JSON files plus `embeddings.pkl`; S3 worker/reflection histories, grounding notes, screenshots, and code-agent outputs are in-memory during a run; OSWorld/BBON traces are result-directory files.
- **Representational form:** `prose` `symbolic` `parametric` — Procedural prompts, task summaries, retrieved experiences, fact captions, reflections, and code summaries are prose; DAGs, JSON memories, trajectory records, action method schemas, CLI parameters, and result records are symbolic; embeddings and grounding-model outputs are distributed-parametric selection state.
- **Lineage:** `authored` `imported` `trace-extracted` — Prompt templates, action APIs, and policies are authored; seed S1/S2 knowledge may be imported from GitHub release assets; episodic/narrative memories, fact captions, reflections, code summaries, and OSWorld result records derive from task traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` `learning` `validation` — Retrieved experiences and saved notes advise planners/workers; procedural memory and generated system prompts instruct action; DAG planning routes subtasks; embedding similarity ranks memories; summarizers and BBON captioners/judges learn from traces; comparative judging validates and ranks rollout choices. There is no durable hard-enforcement layer over learned memories.

**S3 procedural prompt modules.** Storage substrate: repository Python files under `gui_agents/s3/memory/` and runtime LMMAgent system prompts. Representational form: prose instructions assembled with symbolic action-method signatures and skipped-action filtering. Lineage: authored, with no runtime mutation except prompt assembly for platform, task, and available actions. Behavioral authority: instruction and routing; the worker prompt decides how the agent should choose GUI versus code actions, verify results, format code, and stop.

**S3 task-local trajectory state.** Storage substrate: in-memory `generator_agent.messages`, `reflection_agent.messages`, `worker_history`, `reflections`, `screenshot_inputs`, grounding-agent `notes`, and `last_code_agent_result`; CLI and OSWorld runners also write logs, screenshots, and `traj.jsonl` result files. Representational form: prose plans/reflections/summaries, symbolic action code/results, and image bytes. Lineage: trace-extracted from the current task only. Behavioral authority: knowledge and instruction inside the active run. The next S3 model call sees selected trajectory evidence and code-agent summaries, but reset clears the worker state.

**S1/S2 narrative and episodic memories.** Storage substrate: local files under `kb_s1`/`kb_s2` or caller-selected `memory_root_path`, especially platform-specific `narrative_memory.json`, `episodic_memory.json`, `formulate_query.json`, search-result JSON files, and `embeddings.pkl`. Representational form: prose summaries keyed by task/subtask descriptions, symbolic JSON dictionaries, and parametric embeddings. Lineage: seed knowledge may be imported from release ZIP assets; new entries are trace-extracted from completed trajectories and summarized by LLM prompts. Behavioral authority: knowledge and ranking when similar experiences are retrieved and inserted into S1/S2 planner or worker prompts.

**S1/S2 retrieval and planning policies.** Storage substrate: repository code and runtime constructor arguments. Representational form: symbolic parameters and prose prompts: search-engine choice, embedding engine selection, DAG translator prompts, summarization prompts, and planner/worker prompt templates. Lineage: authored system-definition artifacts. Behavioral authority: routing, ranking, and instruction; these policies decide when to formulate search queries, how to retrieve memories, how to fuse retrieved web/LLM knowledge with prior experience, and how to convert plans into DAG subtasks.

**S3 local code-agent loop.** Storage substrate: runtime `CodeAgent` messages, execution history, environment-controller script outputs, and a final summary returned to the GUI worker. Representational form: prose reasoning/summaries plus symbolic Python/Bash snippets and result dictionaries. Lineage: trace-extracted from a delegated code-execution session. Behavioral authority: instruction and knowledge inside the next worker turn; the code agent can execute local scripts through the environment controller, but the retained summary is task-local.

**BBON rollout traces, fact captions, and comparative judge results.** Storage substrate: OSWorld result directories containing screenshots, `traj.jsonl`, `fact_captions.jsonl`, and JSON evaluation outputs. Representational form: screenshots, prose fact captions and judge thoughts, symbolic result records and scores. Lineage: trace-extracted from multiple task rollouts. Behavioral authority: evaluation and ranking over rollout selection, not durable advice for the next live S3 task. The promotion path would be to distill winning/losing trajectory facts into reusable procedural memory, but the reviewed code stops at evaluation/selection output.

Promotion path: Agent-S has two partial promotion paths. S1/S2 promote raw task/subtask traces into prose summaries and embedding-indexed JSON memory, then read those summaries back into future prompts. S3/BBON promotes rollout traces into fact captions and a selected trajectory, but does not promote those facts into future procedural rules, validators, or a persistent runtime memory.

## Comparison with Our System

| Dimension | Agent-S | Commonplace |
|---|---|---|
| Primary purpose | Computer-use agents for GUI tasks and OSWorld-style evaluation | Git-native methodology KB for agent-operated knowledge bases |
| Canonical retained artifacts | Authored prompts, local JSON experience memories, embeddings, task trajectories, screenshots, fact captions, judge results | Typed Markdown notes, instructions, ADRs, source snapshots, indexes, schemas, review reports |
| Write path | S1/S2 summarize trajectories into JSON memory; S3 keeps task-local history; BBON writes evaluation traces and captions | Human/agent-authored artifacts routed through collection contracts, validation, and semantic review |
| Read-back | S1/S2 embedding retrieval injects similar experience into planner/worker prompts; S3 mostly uses active-run history and reflection | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | Prompt-format checks, step budgets, max trajectory length, benchmark scoring, comparative judge prompts | Type specs, schemas, git diffs, deterministic validators, review bundles, source-grounded lineage |

Agent-S is useful to Commonplace less as a durable KB design and more as a study in task-time context control. Its strongest current design choice is aggressively shaping the action surface and prompt context for a GUI agent: method signatures are reflected into prompts, unavailable actions are hidden, image history is bounded, reflections are task-local, and code-agent output is summarized before reentry.

The older S1/S2 memory path is closer to the agent-memory landscape: it stores summarized experiences, retrieves them by embedding similarity, and pushes them into future planning and execution prompts. Compared with Commonplace, that path is much cheaper to operate but much weaker on provenance and review. A memory item is keyed by task/subtask text and contains an LLM summary, not a typed artifact with source spans, review status, expiry, or an acceptance gate.

S3's BBON path is a different kind of trace-derived mechanism. It extracts facts from before/after screenshots and uses those facts to judge which rollout did better. Commonplace should read this as an evaluation pattern, not as evidence that S3 has persistent runtime learning. The reviewed code can select among trajectories; it does not convert those judgments into reusable system-definition artifacts.

**Read-back:** `both` — S1/S2 expose explicit retrieval machinery, but their planner and worker also receive instance-targeted retrieved experience automatically at first planning/subtask steps; S3's current package path is mostly task-local push of reflection, notes, and code-agent summaries, not durable memory read-back.

### Borrowable Ideas

**Hide unavailable actions before prompt assembly.** Ready now. Commonplace skills and review workflows could similarly generate task prompts from the currently available commands/tools instead of describing unavailable affordances and relying on the agent to remember constraints.

**Separate execution summaries from raw execution traces.** Ready for workshops. The S3 code agent returns a compact result summary plus selected execution history to the GUI worker. Commonplace could use the same split for long command-running investigations: retain raw logs, but hand the next reasoning step a small structured summary.

**Use before/after fact captions for trace review.** Needs a concrete evaluation workflow. BBON's fact-caption stage is a useful pattern for making UI trajectories judgeable without forcing the judge to infer every step from raw screenshots. In Commonplace, analogous "fact captions" could summarize diffs, validation runs, or review sweeps before a semantic gate.

**Borrow embedding retrieval only with review metadata.** Needs stronger lineage. S1/S2's memory retrieval is useful because it is automatic and instance-targeted, but Commonplace should not inject prior summaries without source links, review state, expiry, and a way to suppress stale or low-confidence memories.

**Treat task/subtask memory as lifecycle state, not a universal ontology.** Ready as vocabulary. S1/S2 distinguish whole-task narrative memory from subtask episodic memory. Commonplace can reuse that distinction inside workshop runs without making it the primary library schema.

## Write-side placement

**Write agency:** `manual` `automatic` — Authored prompts and code are manually maintained in the repository; S1/S2 automatically summarize task/subtask traces into local memory files, S3 automatically accumulates task-local worker/reflection/code-agent state, and BBON automatically writes fact captions and judge outputs from result traces.

**Curation operations:** `consolidate` `synthesize` `promote` — S1/S2 consolidate multi-step trajectories into compact narrative and episodic summaries; search-result fusion synthesizes retrieved web/LLM knowledge with prior experience; embedding retrieval and BBON comparative judging promote selected experiences or trajectories into the next prompt or chosen rollout. The reviewed code does not implement deduplication, contradiction invalidation, or aging/decay over durable memories.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `trajectories` — Agent-S consumes GUI task trajectories, planner/worker outputs, action code, screenshots, code-agent execution history, rewards/results, and before/after screenshot pairs.

**Learning scope:** `per-task` `cross-task` — S3 worker/reflection/code-agent state is per-task; S1/S2 local memories are cross-task within the platform-specific local KB directory; BBON compares runs for benchmark tasks.

**Learning timing:** `online` `offline` `staged` — S3 context updates online within each turn; S1/S2 trajectory summaries are staged at subtask/task boundaries; BBON fact captions and comparative judging run offline over completed result directories.

**Distilled form:** `prose` `symbolic` `parametric` — Distillation yields prose task/subtask summaries, reflections, code summaries, fact captions, and judge thoughts; symbolic JSON memories/results and action records; and embeddings for S1/S2 similarity retrieval.

**Trace source.** Agent-S qualifies as trace-derived through two distinct paths. The S1/S2 path records planner/worker trajectories and summarizes them into narrative and episodic memories. The S3/OSWorld path records screenshots, action traces, rewards, and result files, then derives fact captions and comparative judgments.

**Extraction.** S1/S2 extraction is LLM summarization of successful or failed task/subtask trajectories under `TASK_SUMMARIZATION_PROMPT` and `SUBTASK_SUMMARIZATION_PROMPT`; the key is the task or subtask description, and the output is written only if the key is not already present. S3's code-agent loop summarizes code execution history for the next GUI worker turn. BBON extraction uses `BehaviorNarrator` to caption visual differences between before/after screenshots, then `ComparativeJudge` to choose among trajectories from their fact captions and initial/final screenshots.

**Scope and timing.** S3 online context is per reset/task. S1/S2 memories persist in a local platform directory and can affect later tasks through embedding retrieval. BBON is offline and benchmark-scoped: it writes result artifacts and selected trajectories, but the reviewed code does not feed those selections back into S3 prompts as durable learned policy.

**Survey placement.** Agent-S splits the survey axes. S1/S2 are trace-to-experience-summary systems with instance-targeted embedding read-back. S3/BBON is trace-to-evaluation: it extracts facts from rollouts and ranks completed trajectories, strengthening the distinction between learning for selection/evaluation and learning for future contextual activation.

## Read-back placement

**Read-back:** `both` — S1/S2 have pull-like retrieval functions, but their planner and worker automatically receive instance-targeted retrieved experience in the prompt; S3's current default loop mainly pushes task-local reflection, notes, and code-agent summaries rather than durable memory.

**Read-back signal:** `inferred / embedding` `coarse` — S1/S2 select narrative and episodic memories by embedding similarity to the current task/subtask, while S3 includes active-run reflection/notes/code-agent summaries by coarse turn state.

**Faithfulness tested:** `no` — The repository contains OSWorld/BBON scoring and comparative judging machinery, but the reviewed code does not show a with/without memory ablation proving that S1/S2 retrieved experiences or S3 pushed summaries reliably change downstream behavior.

**Direction edge cases.** The durable-memory verdict comes mainly from S1/S2, not the installed S3 entry point. `retrieve_narrative_experience()` and `retrieve_episodic_experience()` are pull functions as APIs, but the planner and worker call them internally at first planning/subtask steps and inject their outputs into another agent's prompt. That makes them push from the receiving planner/worker's perspective. S3's reflection and grounding notes are push to the worker, but they are task-local state, not retained cross-task memory.

**Targeting and signal.** S1/S2 target the current instance by embedding the current instruction or subtask query key and comparing it to stored memory keys. This is `inferred / embedding`, not an identifier match: the selector keys on semantic similarity between descriptions. S3's worker receives the current text buffer and last code-agent result without semantic selection, so those inclusions are coarse.

**Injection point.** S1/S2 retrieval happens before the first planner or worker model call for a task/subtask, so retrieved experience can shape the next plan/action. S3 reflection and code-agent summaries are assembled into the next worker message before generation. BBON judging happens after completed trajectories and is therefore evaluation/write-side selection, not read-back into the same action.

**Selection, scope, and complexity.** S1/S2 retrieval returns one nearest narrative or episodic memory, with embeddings cached in `embeddings.pkl`; there is no top-k context budget, source-span filtering, review-state gate, or stale-memory invalidation. S3 controls context complexity by limiting image history and by summarizing code-agent output, but long text history can remain for long-context providers.

**Authority at consumption.** Retrieved S1/S2 experience is advisory context appended to the instruction, but because it is inserted into planner/worker prompts it can influence the generated DAG or grounded action. S3 procedural memory has stronger instruction authority; task-local reflections and code summaries are softer evidence. Effective authority is not verified from code.

**Faithfulness.** The repo evaluates agents through OSWorld result scoring and BBON comparative judging, but I did not find a memory-specific ablation that disables retrieved S1/S2 experience or S3 summary/reflection injection while holding the rest of the loop fixed. The activation mechanisms are structurally implemented; actual impact is an empirical claim.

**Other consumers.** Human developers consume the same artifacts through logs, screenshots, JSONL trajectories, benchmark result files, release KB assets, and fact-caption outputs. These are inspectable enough for debugging, but not governed as reviewed knowledge artifacts.

## Curiosity Pass

**The name "memory" means different things across versions.** S1/S2 use memory in the cross-task experience sense. S3's `memory/procedural_memory.py` is mostly authored prompts. BBON learns from trajectories, but for selection/evaluation rather than future prompt memory.

**S3 removed hierarchy and most durable memory from the default path.** The installed agent prioritizes fewer inference calls and bounded live context over S2's planner/worker/RAG structure. That is a deliberate context-efficiency tradeoff, but it means the newest path is less useful as a durable memory-system reference.

**The local code agent is a risky but interesting sub-agent memory surface.** It executes Python/Bash in a bounded loop, then summarizes its own execution for the GUI worker. The summary is a practical compression boundary, but the same feature expands operational risk because generated code runs with local permissions.

**S1/S2 memory has weak lineage.** The JSON summaries know the task/subtask key and summary text, and embeddings cache retrieval state. They do not retain source step ids, screenshots, model/prompt versions per entry, reviewer acceptance, confidence, or invalidation status.

**BBON is close to a promotion loop but stops one step early.** It identifies better trajectories using fact captions and screenshots. A next design step would distill repeated winning/losing facts into procedural rules or tests, but that promotion is not implemented in the reviewed code.

## What to Watch

- Whether S3 reintroduces a durable memory path for learned GUI procedures; that would change Agent-S from task-local context engineering back into a cross-task memory system.
- Whether BBON-selected trajectory facts become reusable prompt rules, validators, or training data with lineage; that would make the trace-derived evaluation path behavior-shaping beyond benchmark selection.
- Whether S1/S2 memories gain source pointers to screenshots, trajectory rows, prompt/model versions, and review state; without that, embedding read-back remains hard to audit.
- Whether the S3 code-agent result summary gets structured verification fields rather than free prose; that would make the GUI worker's follow-up verification more reliable.
- Whether evaluations add explicit ablations for retrieved experience, reflection, code-agent summaries, and BBON selection; this matters for distinguishing context presence from behavioral effect.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Agent-S splits trace-derived experience memory from trace-derived rollout evaluation.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: S1/S2 memories matter because the planner/worker read them back; S3 result traces alone do not activate future behavior.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Agent-S bundles authored prompts, JSON summaries, embeddings, trajectories, screenshots, and judge outputs under different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: retrieved experiences, reflections, notes, code summaries, and fact captions are mostly advisory context or evidence.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: procedural prompts, action APIs, DAG translators, retrieval policies, and judge prompts configure future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: S1/S2 summarize trajectories into reusable experience memories, while BBON extracts facts from rollout traces.
