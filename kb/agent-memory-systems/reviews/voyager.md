---
description: "Voyager review: embodied Minecraft agent that turns critic-approved rollouts into retrievable executable JavaScript skills"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# Voyager

Voyager, from MineDojo, is an embodied lifelong-learning agent for Minecraft. The inspected source implements a Python orchestration loop around a Mineflayer/Fabric-controlled game environment: a curriculum agent proposes tasks, an action agent writes Mineflayer JavaScript, a critic judges task success from world observations, and the skill manager promotes successful programs into a reusable skill library. The memory system is therefore not a general note store. It is a checkpointed trace-to-action system whose behavior-shaping artifacts include executable JavaScript skills, generated skill descriptions, Chroma retrieval indexes, curriculum task lists, QA cache entries, chest memory, and event logs.

**Repository:** https://github.com/MineDojo/Voyager

**Reviewed commit:** [55e45a880755d0c8c66ca7fb5fe7962ac8974f89](https://github.com/MineDojo/Voyager/commit/55e45a880755d0c8c66ca7fb5fe7962ac8974f89)

**Last checked:** 2026-06-02

## Core Ideas

**The core loop is curriculum, action, critic, and skill promotion.** `Voyager.learn()` repeatedly asks the curriculum agent for a task, rolls out action attempts, lets the critic judge success, promotes only successful `program_code`/`program_name` through `SkillManager.add_new_skill(...)`, and updates completed or failed task lists ([voyager/voyager.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py)). That makes the critic's success decision the promotion oracle for executable memory.

**The environment is a live Mineflayer execution substrate.** Python `VoyagerEnv` starts a Node Mineflayer server, optionally launches Minecraft, posts generated code to `/step`, and receives serialized observations back ([voyager/env/bridge.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/env/bridge.py)). The Node server loads Mineflayer plugins, injects observation and skill helpers, and evaluates submitted JavaScript together with the retrieved programs ([voyager/env/mineflayer/index.js](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/env/mineflayer/index.js), [voyager/env/mineflayer/lib/skillLoader.js](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/env/mineflayer/lib/skillLoader.js)).

**Rollout traces are evidence, but successful programs are the durable learning.** Each action step records event lists under `ckpt/events/`, including observations, chat, errors, status, inventory, nearby blocks, entities, chests, and save signals ([voyager/utils/record_utils.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/utils/record_utils.py), [voyager/env/mineflayer/lib/observation](https://github.com/MineDojo/Voyager/tree/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/env/mineflayer/lib/observation)). Failed attempts remain evidence and failed-task state. Only successful rollouts become active skill entries.

**The skill library is code plus retrieval handles.** `SkillManager.add_new_skill(...)` writes JavaScript code, a generated text description, `skills.json`, and a persistent Chroma vector database under `ckpt/skill/`; `retrieve_skills(query)` embeds over descriptions and returns the matching code snippets ([voyager/agents/skill.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/skill.py)). The shipped `skill_library/trial*/skill/` directories show the shareable retained form: `code/`, `description/`, `skills.json`, and `vectordb/` ([skill_library/README.md](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/skill_library/README.md), [skill_library/trial1/skill/skills.json](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/skill_library/trial1/skill/skills.json)).

**Context efficiency is top-k skill injection, not progressive disclosure.** The action-agent prompt receives control primitives plus at most `skill_manager_retrieval_top_k` retrieved skills, defaulting to five. Retrieval is run from task context at reset and from task context plus summarized chat needs after each step ([voyager/voyager.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py), [voyager/agents/action.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/action.py)). This bounds volume but not complexity: selected skills are full executable functions, and all selected programs are also passed into the Mineflayer execution environment.

**Curriculum memory is distinct from skill memory.** `CurriculumAgent` persists completed tasks, failed tasks, a QA cache, and a Chroma index for QA-cache questions; those artifacts shape future task proposals and task context, and completed-task count even changes environment difficulty after 15 tasks ([voyager/agents/curriculum.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/curriculum.py)). This is memory, but it is not the executable skill library.

**Overwrite behavior replaces active authority.** If a promoted `program_name` already exists, the skill manager deletes the old Chroma entry, writes the new description under the same vector ID and active `skills.json` key, and dumps the new code under a suffixed filename such as `nameV2.js` ([voyager/agents/skill.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/skill.py)). That preserves some file-level history but not explicit supersession metadata, replay evidence, retirement state, or reviewer status.

## Artifact analysis

- **Storage substrate:** `files` — JSON files under `ckpt/events/`, plus Mineflayer observation modules that define the emitted event surface
- **Representational form:** `prose` `symbolic` `parametric` — prose descriptions, QA answers, chat/error text, and prompts; symbolic JSON, executable JavaScript, parsers, task lists, and harness code; Chroma embeddings over skill descriptions and QA questions
- **Lineage:** `authored` `imported` `trace-extracted` — prompts, parsers, and the harness are authored; supplied skill libraries can be loaded through `skill_library_dir`; active skills, curriculum state, events, and QA/cache records derive from rollouts, critic outcomes, and model-generated summaries
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — raw traces and QA records are evidence/context; prompts and selected skills instruct action; parsers, retry limits, and critic gates constrain promotion; Chroma routes and ranks skills; the rollout-to-skill path mutates future behavior

**Raw event records.** Storage substrate: JSON files under `ckpt/events/`, plus Mineflayer observation modules that define the emitted event surface. Representational form: mixed symbolic JSON and prose chat/error text. Lineage: captured from each action attempt and task label by `EventRecorder.record(...)`; source changes in observation code or environment setup change what later traces contain. Behavioral authority: knowledge artifact for audit, debugging, and possible resume analysis; raw events do not by themselves become future action authority.

**Executable skill records.** Storage substrate: `ckpt/skill/code/*.js`, active `ckpt/skill/skills.json`, in-memory `self.skills`, and shipped `skill_library/trial*/skill/` examples. Representational form: symbolic executable JavaScript plus JSON envelopes. Lineage: generated by the action agent during a rollout, parsed for an async function, executed in Minecraft, accepted by the critic, and then persisted by the skill manager. Behavioral authority: system-definition artifact. Once retrieved, the code enters both the action prompt and the Mineflayer execution context, so it can directly change future behavior.

**Skill descriptions and Chroma index.** Storage substrate: `ckpt/skill/description/*.txt`, active descriptions in `skills.json`, and Chroma files under `ckpt/skill/vectordb`. Representational form: prose descriptions plus distributed-parametric embeddings. Lineage: LLM-generated from accepted program code by the skill prompt, then embedded and persisted; stale or missing Chroma files break the manager's count-sync assertion. Behavioral authority: routing and ranking authority over which executable skills activate for a task, while the code remains the action source.

**Curriculum and QA memory.** Storage substrate: `ckpt/curriculum/completed_tasks.json`, `failed_tasks.json`, `qa_cache.json`, and `curriculum/vectordb`. Representational form: symbolic lists and maps, prose QA answers, and embeddings over questions. Lineage: completed/failed tasks derive from critic outcomes; QA entries derive from model answers to generated or task-specific Minecraft questions. Behavioral authority: mixed. They are knowledge artifacts when read as context, and system-definition artifacts when prompt assembly uses them to choose or constrain the next task.

**Chest memory and checkpoint state.** Storage substrate: `ckpt/action/chest_memory.json`, action-agent process state, event logs, and the checkpoint directory chosen by `ckpt_dir` or `skill_library_dir`. Representational form: symbolic JSON over positions/items plus runtime Python state. Lineage: derived from observed chest states and resume loading. Behavioral authority: advisory context for action and critic prompts; it can change where the agent deposits or retrieves items, but it is not promoted into a reusable skill.

**Prompts, parsers, and execution harness.** Storage substrate: Python and JavaScript source files plus prompt text under `voyager/prompts/`. Representational form: prose prompts, symbolic parsers, retry limits, top-k configuration, and executable harness code. Lineage: authored system-definition artifacts. Behavioral authority: instruction, validation, routing, execution, and promotion authority, because they define generated-code constraints, critic success checks, task selection, retrieval, and environment execution.

Promotion path: Voyager promotes raw rollout trace -> parsed generated JavaScript -> environment execution -> critic success -> persisted skill code -> generated description -> embedding index -> pre-action retrieval. The path crosses from trace evidence to executable system-definition artifact, but the code does not encode strong lineage from each skill back to the accepted event file, critic reasoning, prompt, Minecraft version, or replay result.

## Comparison with Our System

| Dimension | Voyager | Commonplace |
|---|---|---|
| Primary purpose | Embodied Minecraft lifelong-learning agent | Agent-operated methodology KB |
| Main retained artifact | Critic-approved executable Mineflayer skill | Typed Markdown knowledge and system-definition artifacts |
| Raw evidence | Rollout events, observations, chat, errors, inventory/status traces | Source snapshots, citations, notes, review reports, validation output |
| Storage substrate | Checkpoint directory with JSON, JavaScript, descriptions, Chroma stores | Git-tracked Markdown, schemas, scripts, generated indexes |
| Activation | Embedding retrieval injects selected skills before action generation and execution | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Promotion oracle | LLM/manual critic over final world observation and task context | Human/agent review, deterministic validation, semantic QA, source-grounding discipline |

Voyager is stronger than Commonplace on embodied trace-to-action learning. A successful Minecraft trajectory can become a function that future tasks call directly. Commonplace is stronger on artifact governance: its durable artifacts carry frontmatter, collection contracts, source links, validation, review state, and archive conventions, while Voyager skills carry only active name, code, generated description, and weak file-level version traces.

The main design contrast is authority. Voyager's raw traces, QA answers, chest memory, and completed/failed task lists are mostly knowledge artifacts until prompt assembly consumes them. Generated JavaScript skills are system-definition artifacts: selected functions are inserted into the action prompt and passed to the execution environment. Chroma indexes are also system-definition artifacts because they decide which skills gain that authority.

**Read-back:** `push` — Voyager's orchestrator runs instance-targeted skill retrieval before the action agent writes its next program, then injects selected skills into the action prompt while making the full active skill set available to execution

### Borrowable Ideas

**Executable promotion target.** Ready as a pattern, not as a default KB feature. Repeated successful behavior can graduate from prose notes into scripts, validators, commands, or agent skills when the action boundary and promotion oracle are clear.

**Separate raw trace, code, description, and index.** Ready now. Voyager is easiest to reason about when `events/`, `skill/code/`, `skill/description/`, `skills.json`, and `skill/vectordb/` are treated as different artifact classes with different authority.

**Use prose descriptions as retrieval handles for code.** Useful for small tool and skill libraries. The description is cheap to inspect and embed, while the executable code remains the canonical action artifact.

**Keep curriculum memory apart from skill memory.** Ready as a workshop pattern. Task-history memory, QA cache, and executable skills serve different consumers and should not share one lifecycle merely because they live in one checkpoint directory.

**Require explicit supersession before executable memory gets authority.** Needed before borrowing. Voyager's suffixed code dumps are useful, but Commonplace would need explicit lineage, review status, supersession, rollback, and retirement rules before promoted code received instruction-level authority.

**Treat retrieval indexes as rebuildable views.** Ready now. Voyager's Chroma count assertions show the cost of index/source drift. Commonplace should keep embeddings or search sidecars rebuildable from canonical files rather than letting them become source-of-truth memory.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
- **Trace source:** `event-streams` `trajectories` — embodied rollout event records and task-attempt trajectories carry observations, chat, errors, inventory/status changes, nearby world state, generated code, execution, and critic judgment
- **Learning scope:** `per-task` `cross-task` — each successful task can promote a skill, and the resulting skill library is reused across later tasks or transferred through `skill_library_dir`
- **Learning timing:** `online` — during `learn()`, successful rollouts update skill and curriculum memory before future tasks
- **Distilled form:** `prose` `symbolic` `parametric` — accepted rollouts become executable JavaScript, generated prose descriptions, JSON state, and Chroma embedding indexes

**Trace source.** Voyager qualifies as trace-derived learning. The raw trace source is an embodied rollout: task and context, generated JavaScript, Mineflayer execution, chat logs, execution errors, observations, inventory/status changes, nearby blocks/entities/chests, save events, and final critic judgment. The trigger boundary is one rollout attempt series inside `Voyager.rollout(...)`, with retries until critic success or retry exhaustion.

**Extraction.** Extraction is success-gated. The action agent parses the final async JavaScript function from an LLM response, the environment executes it, and the critic judges task success from observations. Only successful rollouts pass code into `SkillManager.add_new_skill(...)`; failed attempts remain event records and failed-task entries. The skill manager then asks an LLM to summarize the accepted code into a retrieval description.

**Four fields.** The raw stage is JSON/prose event evidence in checkpoint files, with knowledge-artifact authority. The distilled stage is executable JavaScript plus generated description and embedding index under `ckpt/skill/`, with direct system-definition authority at read-back. The system-definition layer is the prompt/parser/critic/retrieval/execution code that decides what gets promoted and what later activates.

**Scope and timing.** Scope is Minecraft/Mineflayer-specific and mostly checkpoint-local. A skill library can transfer to a new Minecraft world through `skill_library_dir`, but the skills assume the same control primitives, Mineflayer APIs, and task-observation style. Timing is online during `learn()`: after each successful task, skill and curriculum memory mutate before future tasks. Inference over a supplied skill library loads existing skills and runs subgoals without treating that library as a learning checkpoint.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Voyager is a trajectory-to-executable-artifact system. It strengthens the survey distinction between raw trace retention and distilled behavior-changing artifacts: the durable learned object is not the event log, but the critic-approved JavaScript program plus retrieval metadata that future rollouts can execute.

## Read-back placement

**Direction.** Push. The acting `ActionAgent` does not choose to search memory; Voyager's orchestration layer retrieves skills before rendering the action-agent system message. The retrieval call is pull from the orchestrator's implementation perspective, but it is push for the receiving agent.

**Read-back signal:** `coarse` `inferred / embedding` — Chroma selects skills by embedding similarity over current task/chat context, while the full active skill set is also made coarsely available to Mineflayer execution.

**Faithfulness tested:** `no` — the review found injection and execution wiring, but no with/without-skill ablation or replay test in the inspected codebase.

**Targeting and signal.** The action-prompt push is `instance`-targeted. Skill retrieval fires at task reset using the current task context and again after each step using context plus summarized chat-log needs; `SkillManager.retrieve_skills(...)` runs Chroma similarity over generated skill descriptions and returns the matching skill code, bounded by `retrieval_top_k`. The signal is `inferred / embedding`, because relevance is derived from the current task/chat content rather than from an assigned task or skill identifier. Separately, each Mineflayer `/step` receives `self.skill_manager.programs`, which makes the full active skill set available to execution; that execution-side availability is `coarse` rather than instance-selected.

**Injection point.** Retrieval happens before the next action-agent LLM call and before Mineflayer execution, so selected skills can change both the generated plan and the callable program set.

**Selection, scope, and complexity.** Selection is top-k over skill descriptions, defaulting to five. Scope is the loaded checkpoint or `skill_library_dir`. Complexity is higher than ordinary text snippets because each selected item is a full executable function that can call other primitives and can be reused by generated code. The code grounds the selection mechanism; precision, recall, and prompt dilution are not verified by this review.

**Authority at consumption.** Retrieved skills have strong system-definition authority. They appear as "useful programs" in the system prompt and are also supplied as executable `programs` to the Mineflayer server. Skill descriptions have routing authority, not direct action authority.

**Faithfulness.** The source demonstrates injection and execution wiring, but it does not include a with/without-skill ablation or replay test in the codebase. The Node package's `test` script exits with "Error: no test specified", so automated behavioral regression coverage is not present in the inspected source ([voyager/env/mineflayer/package.json](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/env/mineflayer/package.json)).

**Other consumers.** Human users can share and load learned skill libraries. The curriculum agent consumes completed/failed tasks and QA cache for task proposals. The critic consumes observations, context, and chest memory for success judgment.

## Curiosity Pass

The strongest mechanism is also the main governance weakness: a single LLM or manual critic can turn one successful trajectory into future executable behavior. The action parser checks for an async function shape, and the action prompt bans several direct or unsafe patterns, but the code does not provide static security review, semantic diff review, deterministic Minecraft verification, or replay before promotion ([voyager/agents/action.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/action.py), [voyager/prompts/action_template.txt](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/action_template.txt), [voyager/agents/critic.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/critic.py)).

The Chroma stores are derived views with strict sync assumptions. Both skill and curriculum managers assert vector-count equality with JSON state and tell the operator to manually delete stale vector directories when starting from scratch. That is acceptable research-code ergonomics, but it is not a durable memory lifecycle.

The checkpoint directory is broader than the public "skill library" story. The README correctly treats `skill/` as the portable learned library, but a running agent also depends on event logs, chest memory, completed and failed task lists, QA cache, and vector indexes. Transferring only `skill/` preserves behavior but loses most rollout evidence and curriculum lineage.

The generated skill descriptions are intentionally summaries of code, not proof of success. They are useful retrieval handles, but they do not carry preconditions, postconditions, task id, critic result, environment version, or evidence pointers.

## What to Watch

- Whether future versions add replay or benchmark gates before adding or replacing active skills; that would make executable promotion safer to borrow.
- Whether promoted skills gain explicit lineage back to event files, critic decisions, prompts, Minecraft/Fabric versions, and generated descriptions.
- Whether overwrite/versioning becomes a first-class lifecycle with supersession, deprecation, rollback, and retirement rather than filename suffixes plus active JSON replacement.
- Whether Chroma indexes remain derived convenience stores or become harder-to-audit sources of activation truth.
- Whether curriculum QA cache and completed/failed task lists receive clearer status, invalidation, or transfer rules when skill libraries move between worlds.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Voyager is a trajectory-to-executable-JavaScript system where critic-approved rollouts become future action authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Voyager explicitly wires retrieval into pre-action prompt and execution context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Voyager requires separating raw events, code, descriptions, embeddings, QA cache, task lists, prompts, and harness code by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw rollout events, observations, QA answers, task lists, and chest memory advise or evidence future work.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: generated JavaScript skills, Chroma retrieval, prompts, parsers, critic routing, and execution harness code constrain future behavior.
- [Codification](../../notes/definitions/codification.md) - exemplifies: Voyager crosses from natural-language task attempts into executable Mineflayer procedures.
- [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) - applies: Voyager's critic is a soft task-success oracle over world observations rather than a deterministic verifier.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - exemplifies: Voyager changes deployed behavior by mutating readable/executable artifacts without fine-tuning the base LLM.
