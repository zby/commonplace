---
description: "Embodied Minecraft agent that promotes critic-approved rollouts into retrievable JavaScript skills, with checkpointed traces, curriculum memory, QA cache, and Chroma indexes"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# Voyager

Voyager is MineDojo's embodied lifelong-learning agent for Minecraft. The inspected source implements a Python orchestration loop around a Mineflayer/Fabric-controlled game environment: a curriculum agent proposes tasks, an action agent writes Mineflayer JavaScript, a critic judges task success from world observations, and the skill manager promotes successful programs into a reusable skill library. The memory system is therefore not a general note store. It is a checkpoint directory whose behavior-shaping artifacts include executable JavaScript skills, generated skill descriptions, Chroma retrieval indexes, curriculum task lists, QA cache entries, and chest/world-event traces.

**Repository:** https://github.com/MineDojo/Voyager

**Reviewed commit:** [55e45a880755d0c8c66ca7fb5fe7962ac8974f89](https://github.com/MineDojo/Voyager/commit/55e45a880755d0c8c66ca7fb5fe7962ac8974f89)

## Core Ideas

**The agent loop is curriculum, action, critic, skill promotion.** `Voyager.learn()` repeatedly asks `CurriculumAgent.propose_next_task(...)` for a task, runs `rollout(...)`, calls `CriticAgent.check_task_success(...)` after each generated program execution, promotes only successful rollout code through `SkillManager.add_new_skill(...)`, and then records the task in completed or failed task lists ([voyager/voyager.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py)). This makes the critic's success decision the promotion oracle for executable memory.

**The environment is an embodied Mineflayer/Fabric substrate.** Python `VoyagerEnv` starts a Node Mineflayer server, optionally launches a Minecraft instance through Azure login, posts generated code to `/step`, and receives serialized observations back ([voyager/env/bridge.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/env/bridge.py)). The Node server uses Mineflayer, pathfinder, tool, collectblock, pvp, and observation plugins, then evaluates the submitted JavaScript together with loaded programs ([voyager/env/mineflayer/index.js](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/env/mineflayer/index.js), [voyager/env/mineflayer/package.json](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/env/mineflayer/package.json)). The docs pin the experimental Minecraft stack to Fabric loader `0.14.18` on Minecraft `1.19` with pause and respawn mods ([installation/fabric_mods_install.md](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/installation/fabric_mods_install.md), [installation/minecraft_instance_install.md](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/installation/minecraft_instance_install.md)).

**Rollout traces are saved as evidence, but the successful program is the learned artifact.** Each action step records event lists under `ckpt/events/`, including observations, chat, execution errors, saves, status, inventory, nearby blocks, entities, chests, and other Mineflayer-derived signals ([voyager/utils/record_utils.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/utils/record_utils.py), [voyager/env/mineflayer/lib/observation](https://github.com/MineDojo/Voyager/tree/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/env/mineflayer/lib/observation)). Those raw event files are knowledge artifacts: they preserve what happened. Only a rollout whose `info["success"]` is true contributes `program_code` and `program_name` to the skill manager, where the code can change future action.

**Skills are executable JavaScript files plus JSON and description sidecars.** `SkillManager.add_new_skill(...)` writes `skill/code/<name>.js`, `skill/description/<name>.txt`, and `skill/skills.json`; it also stores the code and description in memory for future execution and prompting ([voyager/agents/skill.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/skill.py)). The shipped `skill_library/trial*/skill/skills.json` files show the expected retained form: each skill has JavaScript code and a prose description, and `skill_library/README.md` documents the checkpoint layout for sharing only the learned `skill/` directory ([skill_library/README.md](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/skill_library/README.md), [skill_library/trial1/skill/skills.json](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/skill_library/trial1/skill/skills.json)).

**Retrieval is description embedding, activation is code injection.** Generated skill descriptions are embedded into a persistent Chroma collection under `ckpt/skill/vectordb`; `retrieve_skills(query)` runs similarity search and returns the matching JavaScript code from `skills.json` ([voyager/agents/skill.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/skill.py)). At the next reset or retry, the action agent renders retrieved skills and control primitives into the system prompt, and `VoyagerEnv.step(...)` passes all programs to Mineflayer for evaluation ([voyager/agents/action.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/action.py), [voyager/voyager.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py)). The embedding index is a distributed-parametric derived view with ranking authority; the JavaScript code remains the symbolic source of action authority.

**Curriculum memory is separate from skill memory.** The curriculum agent persists `completed_tasks.json`, `failed_tasks.json`, `qa_cache.json`, and a Chroma index for QA-cache questions under `ckpt/curriculum/`; those lists and cached answers shape future task proposals and context, and completed-task count even changes the environment difficulty after 15 tasks ([voyager/agents/curriculum.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/curriculum.py)). This is memory, but not executable skill memory: completed/failed tasks and QA answers are knowledge artifacts when read as context, and system-definition artifacts when inserted into prompts that constrain the next task or context.

**Overwrite behavior preserves old files weakly but replaces active authority.** If a promoted `program_name` already exists, the skill manager deletes the old Chroma entry, writes the new description under the same vector ID and `skills.json` key, and dumps the new code under a versioned filename such as `nameV2.js` while the active in-memory and JSON entry remains keyed by `program_name` ([voyager/agents/skill.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/skill.py)). That gives a file-level trace of overwritten code, but no explicit supersession metadata, reviewer status, invalidation reason, or replay evidence.

## Comparison with Our System

| Dimension | Voyager | Commonplace |
|---|---|---|
| Primary substrate | Checkpoint directory with JSON, JavaScript, text descriptions, event logs, Chroma stores | Git-tracked Markdown notes, instructions, sources, reviews, ADRs, generated indexes |
| Main retained artifact | Critic-approved executable Mineflayer skill | Typed knowledge artifacts and system-definition artifacts |
| Raw evidence | Rollout events, world observations, chat, errors, inventory/status traces | Source snapshots, notes, review reports, validation output |
| Representational form | Symbolic JavaScript, prose descriptions/prompts, JSON task/cache state, embedding indexes | Mostly prose plus structured frontmatter, scripts, schemas, commands |
| Activation | Description embedding retrieves code; prompt and Mineflayer executor make it callable | `rg`, indexes, links, instructions, validation, and review workflows |
| Promotion oracle | LLM or manual critic over final observation and task context | Human/agent review, validation, semantic QA, source-grounding discipline |
| Lifecycle | Append logs; rewrite active skill by name; persist derived Chroma index | Archive, status, backlinks, validation, generated indexes, explicit review dates |

Voyager is much stronger than commonplace on embodied trace-to-action learning. A successful Minecraft trajectory can become a function that future tasks call directly. Commonplace has stronger artifact governance: notes and instructions have frontmatter, status, source links, validation, and archive conventions, while Voyager's skills carry only code, generated description, active name, and a weak file-level version suffix.

The authority split is the central design lesson. Raw events, chat logs, world observations, QA answers, and completed/failed task lists are knowledge artifacts when used as evidence or context. Generated JavaScript skills are system-definition artifacts: once retrieved, they are inserted into the action prompt and execution environment. Chroma indexes have ranking authority because they choose which skills and QA entries are activated, but they are derived from descriptions/questions rather than canonical sources.

Voyager also shows a risk commonplace mostly avoids: executable memory can compound capability quickly, but a weak critic can promote brittle or lucky code into future behavior. The critic reads final observations and returns JSON success/critique; it is not a deterministic verifier, replay suite, or human review gate ([voyager/agents/critic.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/critic.py), [voyager/prompts/critic.txt](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/critic.txt)). That oracle is usable because Minecraft tasks often leave observable inventory or world-state evidence, but it remains soft.

## Borrowable Ideas

**Executable promotion target.** Ready as a design pattern, not as a default KB feature. Repeated successful behavior can graduate from prose notes into scripts, validators, commands, or agent skills when the action boundary and oracle are clear.

**Separate raw trace, distilled code, description, and index.** Ready now. Voyager is easiest to reason about when `events/`, `skill/code/`, `skill/description/`, `skills.json`, and `skill/vectordb/` are treated as separate artifact classes with separate authority.

**Use generated descriptions as retrieval handles for code.** Useful for small skill libraries. The description is cheap to embed and inspect, while the code remains the source of action. Commonplace could use this pattern for script/tool discovery without making embeddings canonical.

**Keep curriculum memory apart from skill memory.** Ready as a workshop pattern. Task-history memory, QA cache, and executable skill memory serve different consumers and should not share one "memory" lifecycle.

**Make overwrite semantics explicit before adopting executable memory.** Needed before borrowing. Voyager's versioned dumped filenames are useful, but commonplace would require explicit supersession, evidence, review status, and retirement rules before promoted code received instruction-level authority.

## Trace-derived learning placement

**Trace source.** Voyager qualifies as trace-derived learning. The raw trace source is an embodied rollout: generated JavaScript, Mineflayer execution, chat logs, errors, observations, inventory/status changes, nearby blocks/entities/chests, event records, and the task/context pair. The trigger boundary is a rollout attempt inside `Voyager.rollout(...)`, with repeated action retries until critic success or retry exhaustion.

**Extraction.** Extraction is success-gated. The action agent parses the final async JavaScript function from an LLM response, the environment executes it, and the critic judges task success from final observations. Only successful rollouts pass `program_code` and `program_name` into `SkillManager.add_new_skill(...)`; failed attempts remain as event records and failed task entries. The description generator then distills the accepted code into a one-line functional summary for retrieval.

**Storage substrate.** Raw traces live as JSON event files under `ckpt/events/`. Action-side chest memory lives in `ckpt/action/chest_memory.json`. Curriculum memory lives under `ckpt/curriculum/` as completed and failed task JSON, QA-cache JSON, and a Chroma directory for question similarity. Distilled skill memory lives under `ckpt/skill/` as JavaScript files, text descriptions, `skills.json`, and a Chroma directory. Shared learned libraries use only the `skill/` subtree.

**Representational form.** Raw events are mixed symbolic JSON and textual chat/error observations. Successful skills are symbolic JavaScript programs. Skill descriptions and QA answers are prose. Completed/failed task lists and `skills.json` are symbolic JSON. Chroma stores are distributed-parametric derived indexes over descriptions/questions, not canonical memory.

**Lineage.** The implemented lineage is rollout events to critic success to promoted program code to generated description to embedding index. It is present operationally but not strongly encoded in the artifacts: skills do not store pointers to the event file, critic reasoning, task attempt number, source prompt, Minecraft version, or replay result. Reusing a function name overwrites active authority in `skills.json` and Chroma while leaving older dumped code files under versioned names.

**Behavioral authority.** Event records, world observations, QA answers, and task lists are knowledge artifacts when consumed as evidence or context. Curriculum prompts give task lists and QA answers system-definition-artifact authority because they constrain the next task. Skill descriptions have routing/ranking authority through Chroma. Generated JavaScript skills have direct system-definition-artifact authority because retrieved functions are inserted into prompts and executed by Mineflayer as future behavior.

**Scope.** Scope is embodied, environment-local, and mostly project/checkpoint-local. A skill library can transfer to a new Minecraft world through `skill_library_dir`, but the code assumes Mineflayer APIs, control primitives, Minecraft 1.19/Fabric setup, and task definitions that the critic can judge from observations.

**Timing.** Learning is online during `learn()`: after each successful task, the skill library and curriculum memory are mutated before future tasks. Inference over a supplied `skill_library_dir` loads existing skills and runs subgoals without resuming learning from that directory.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), Voyager is a trajectory-to-executable-artifact system. It strengthens the survey distinction between raw trace storage and distilled behavior-changing artifacts: the durable learning is not the event log, but the critic-approved JavaScript program plus retrieval metadata that future rollouts can execute.

## Curiosity Pass

The strongest mechanism is also the main governance weakness: a single LLM critic can turn a one-off successful trajectory into executable future behavior. The code has parser constraints on generated JavaScript shape and prompt rules against unsafe patterns such as infinite loops or direct API misuse, but it does not have a replay suite, static security review, semantic diff review, or deterministic Minecraft verifier ([voyager/agents/action.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/action.py), [voyager/prompts/action_template.txt](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/action_template.txt)).

The Chroma stores are derived views with strict sync assumptions. Both curriculum and skill managers assert vector-count equality with JSON state and suggest manual deletion if a run starts from scratch with stale indexes. That is reasonable research-code ergonomics, but it is not a lifecycle model for durable memory.

The checkpoint directory is the real storage substrate. The README foregrounds "skill library", but a running Voyager also depends on chest memory, curriculum task lists, QA cache, event logs, and derived vector stores. Treating only `skill/` as shareable is useful because skills are the portable behavior-changing artifacts; it also means transferred libraries lose most rollout evidence and curriculum lineage.

Tests and documentation are thin for a behavior-changing system. The repo has installation, FAQ, prompts, and example skill libraries, but no Python test suite was present, and the Mineflayer package's `test` script exits with "Error: no test specified" ([voyager/env/mineflayer/package.json](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/env/mineflayer/package.json)). That matters because generated skills can become action authority without automated regression checks.

## What to Watch

- Whether future versions add replay or benchmark gates before adding or replacing active skills.
- Whether promoted skills gain explicit lineage back to event files, critic decisions, prompts, Minecraft/Fabric versions, and generated descriptions.
- Whether overwrite/versioning becomes a first-class lifecycle with supersession, deprecation, and rollback rather than filename suffixes plus active JSON replacement.
- Whether Chroma indexes remain derived convenience stores or become harder-to-audit sources of activation truth.
- Whether curriculum QA cache and completed/failed task lists receive clearer status, invalidation, or transfer rules when skill libraries move between worlds.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Voyager is a trajectory-to-executable-JavaScript case where critic-approved rollouts become future action authority.
- [OS-Copilot](./OS-Copilot.md) - compares-with: both promote interaction experience into executable tools, but Voyager's substrate is Minecraft/Mineflayer skills rather than desktop OS Python tools.
- [SkillWeaver](./SkillWeaver.md) - compares-with: both convert successful embodied/browser trajectories into executable APIs with generated descriptions and retrieval scaffolding.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: Voyager requires separating raw events, code, descriptions, embeddings, QA cache, task lists, and prompts by substrate, form, lineage, and authority.
- [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) - grounds: Voyager's critic is a soft task-success oracle over world observations rather than a deterministic verifier.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - exemplifies: Voyager changes deployed behavior by mutating readable/executable artifacts without fine-tuning the base LLM.
