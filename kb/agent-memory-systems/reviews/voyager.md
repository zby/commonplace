---
description: "Voyager review: Minecraft lifelong-learning agent with trace-derived executable skill libraries, Chroma retrieval, curriculum QA cache, and prompt pushback"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
tags: [trace-derived]
---

# Voyager

Voyager, from MineDojo, is a Minecraft research agent that uses LLM calls to choose tasks, write Mineflayer JavaScript, critique execution, and retain successful behaviors as an executable skill library. At the reviewed commit, the durable memory surfaces are checkpoint files: generated skill code and descriptions, `skills.json`, Chroma vector databases for skill and QA retrieval, curriculum task records, chest memory, and event traces. The strongest memory mechanism is not a prose note store but trace-derived promotion into reusable code.

**Repository:** https://github.com/MineDojo/Voyager

**Reviewed commit:** [55e45a880755d0c8c66ca7fb5fe7962ac8974f89](https://github.com/MineDojo/Voyager/commit/55e45a880755d0c8c66ca7fb5fe7962ac8974f89)

**Last checked:** 2026-06-05

## Core Ideas

**The central retained artifact is an executable skill library.** `SkillManager` creates `skill/code`, `skill/description`, and `skill/vectordb` under the checkpoint directory, stores successful program code and generated descriptions in `skills.json`, and persists a Chroma vector index for retrieval ([voyager/agents/skill.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/skill.py)). The bundled learned libraries show the same shape as JSON maps from skill names to JavaScript code plus description text ([skill_library/README.md](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/skill_library/README.md), [skill_library/trial1/skill/skills.json](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/skill_library/trial1/skill/skills.json)).

**Successful action programs are promoted into future affordances.** The learning loop asks the action agent for JavaScript, executes it in Mineflayer, records environment events, asks the critic whether the task succeeded, and calls `skill_manager.add_new_skill(info)` only when `info["success"]` is true ([voyager/voyager.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py), [voyager/agents/action.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/action.py), [voyager/agents/critic.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/critic.py)). That makes the skill library trace-derived: it is created from attempted tasks, generated programs, execution feedback, and success judgments.

**Read-back happens through both prompt context and executable environment scope.** `retrieve_skills()` selects top-k skill descriptions by Chroma similarity and returns the saved code; `ActionAgent.render_system_message()` includes retrieved skills with authored control primitives in the action prompt ([voyager/agents/skill.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/skill.py), [voyager/agents/action.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/action.py)). During execution, `env.step(..., programs=self.skill_manager.programs)` also makes the full program library available to the Mineflayer side ([voyager/voyager.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py)).

**The curriculum has its own smaller memory path.** `CurriculumAgent` persists completed tasks, failed tasks, a QA cache, and a Chroma index over QA questions; it reuses cached answers for later task context and includes completed/failed tasks in curriculum observations after warm-up thresholds ([voyager/agents/curriculum.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/curriculum.py), [voyager/prompts/curriculum.txt](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/curriculum.txt)). This is weaker than the skill library because it mostly guides task choice and context, not reusable action execution.

**Context efficiency is top-k code injection plus checkpoint state, not token-budgeted packing.** Skill retrieval defaults to `retrieval_top_k=5`, and the action prompt contains those retrieved skills plus base control primitives ([voyager/voyager.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py), [voyager/agents/skill.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/skill.py), [voyager/prompts/action_template.txt](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/action_template.txt)). The code controls count but not token budget, provenance density, or complexity of injected JavaScript. Curriculum observations are thresholded and partly randomized, but there is no global context assembler.

**Adoption is via inspectable checkpoints and shared skill libraries.** The README documents resuming from a checkpoint and running inference with a learned `skill_library_dir`; the skill-library README invites users to share learned checkpoints ([README.md](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/README.md), [skill_library/README.md](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/skill_library/README.md)). The artifacts are inspectable files plus a vector store, but the generated skills do not carry source traces, confidence, or test metadata beyond the success gate that admitted them.

## Artifact analysis

- **Storage substrate:** `files` `vector` `in-memory` — Checkpoint JSON/text/code files hold learned skills, descriptions, task lists, QA cache, chest memory, and event traces; Chroma vector stores persist skill and QA retrieval indexes; active prompts, conversations, rollout state, and environment events live in Python objects during a run.
- **Representational form:** `prose` `symbolic` `parametric` — Skill descriptions, prompts, QA answers, critiques, and event observations are prose; JavaScript skills, control primitives, JSON task/cache records, parsed action code, and Mineflayer calls are symbolic; OpenAI embeddings, Chroma similarity ranking, and LLM behavior are parametric surfaces.
- **Lineage:** `authored` `imported` `trace-extracted` — Prompts, base control primitives, and framework code are authored; bundled/community skill libraries are imported when supplied through `skill_library_dir`; generated skills, descriptions, event records, completed/failed task lists, QA cache entries, and chest memory are extracted from interaction traces and task execution.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Retrieved skills and QA answers advise the action/curriculum models as context; prompts and code schemas instruct generation; JavaScript functions and Mineflayer programs route execution; the critic and parser validate success/format; Chroma ranks memories; successful traces become future reusable skills.

**Executable skill entries.** A skill entry bundles JavaScript code, a generated description, a JSON key, and a vector entry. The code is the strongest operative part because it can be called or reused by later generated programs; the description mainly feeds retrieval. Duplicate program names overwrite the live `skills` entry and vector id, while versioned `.js`/`.txt` dumps preserve older file names locally ([voyager/agents/skill.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/skill.py)).

**Control primitives and prompts.** Authored primitives such as `mineBlock`, `craftItem`, `smeltItem`, and `exploreUntil` are loaded into the action prompt as reusable programs, and the prompt explicitly tells the model to reuse them instead of lower-level APIs ([voyager/control_primitives_context/mineBlock.js](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/control_primitives_context/mineBlock.js), [voyager/prompts/action_template.txt](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/action_template.txt)). These are system-definition artifacts with instruction and executable authority, not learned memory.

**Curriculum and QA state.** Completed/failed task JSON files, QA cache JSON, and the QA question vector index guide task proposal and task context. They are checkpoint memory, but their authority is mostly knowledge/ranking for curriculum decisions rather than executable skill reuse ([voyager/agents/curriculum.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/curriculum.py)).

**Action chest memory and events.** `ActionAgent` persists `chest_memory.json` from observed nearby chests and renders it into later observations; `EventRecorder` writes raw event files and reconstructs item/biome/position histories on resume ([voyager/agents/action.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/action.py), [voyager/utils/record_utils.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/utils/record_utils.py)). Chest memory is advisory world state; event files are mostly trace/provenance and progress analytics, not directly retrieved skill memory.

**Promotion path.** The main path is environment trace and generated code -> critic success verdict -> stored JavaScript skill -> generated skill description -> Chroma embedding -> retrieved prompt program and executable environment program. The code therefore crosses from prose/task context into symbolic executable memory, but without a retained source-span chain from the originating events to the final skill.

## Comparison with Our System

Voyager and Commonplace both treat previous work as material that should shape later agent behavior, but they choose different promotion targets. Commonplace promotes traces into reviewable Markdown artifacts, indexes, and instructions. Voyager promotes successful trajectories into executable JavaScript functions plus a retrieval index. Voyager is faster at turning experience into capacity; Commonplace is stronger at provenance, review, invalidation, and collection-level governance.

The strongest alignment is the raw-to-distilled split. Voyager does not rely on replaying all event logs into every prompt. It distills successful action attempts into named functions, descriptions, and embeddings, then retrieves a few relevant skills. That is a concrete form of context compression, and it keeps recurrent behavior outside the model's weights.

The strongest divergence is authority. A Commonplace note generally advises until some separate instruction or validator gives it stronger force. A Voyager skill can become executable affordance immediately after a critic success check. That makes memory more operationally powerful, but also riskier: generated code may encode accidental assumptions, lacks explicit tests, and can be retrieved on semantically similar but materially different tasks.

Voyager also shows a useful split between authored base capabilities and learned extensions. Control primitives are stable, human-authored substrate; learned skills compose them into higher-level behaviors. Commonplace has analogous layers in shipped commands, skills, instructions, and notes, but it does not yet have a normal route for promoting repeated agent work into executable tools.

### Borrowable Ideas

**Trace-to-executable promotion.** Commonplace could promote repeated workflow fragments into scripts or skills when the behavior has clear success criteria. Ready only for narrow workflows with tests or deterministic validation.

**Description as retrieval handle for executable code.** Voyager retrieves over short generated descriptions while injecting executable code. Commonplace could use concise summaries as retrieval handles for larger instructions or tools, but the handle must stay aligned with the underlying artifact. Ready as an indexing pattern.

**Separate authored primitives from learned compositions.** Commonplace should keep stable primitives under stronger review and let trace-derived candidates compose them in a weaker workshop layer first. Ready as a lifecycle rule.

**Success-gated memory admission.** Voyager admits a skill only after the critic marks the task successful. Commonplace could require a task-specific gate before promoting trace-derived lessons, but LLM-only success checks should not be enough for high-authority artifacts. Needs concrete gate design.

**Checkpoint portability.** Voyager's `skill_library_dir` makes learned capability movable between worlds. Commonplace could package task-scoped workshop outputs for reuse in another project, but should preserve lineage and expiry metadata. Needs a project-transfer use case.

## Write side

**Write agency:** `manual` `automatic` — Users manually choose checkpoint directories, resume mode, imported skill libraries, task/inference mode, and model settings; the system automatically records events, updates chest memory, writes curriculum task/QA files, generates and stores successful skills, updates vector indexes, and persists checkpoints.

**Curation operations:** `synthesize` `promote` `dedup` `evolve` — Voyager synthesizes new executable skills and descriptions from successful rollout material, promotes them into the skill library after the critic success gate, deduplicates completed curriculum tasks, removes completed tasks from the failed-task list, and evolves an existing skill entry when a generated program reuses an existing function name. It does not retain explicit invalidation history, implement age decay, or consolidate multiple skills into higher-level summaries.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` — The action loop consumes generated code, execution errors, chat logs, environment observations, inventory state, critic feedback, and task success/failure; the recorder stores event traces under `ckpt/events`.

**Extraction.** The extraction oracle is the agent loop plus critic. The action LLM proposes JavaScript, Mineflayer execution produces observations/errors/chat, the critic returns a success boolean and critique, and only successful `program_code`/`program_name` pairs are passed to `SkillManager.add_new_skill()`. A second LLM call writes the skill description used for retrieval ([voyager/voyager.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py), [voyager/agents/skill.py](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/skill.py), [voyager/prompts/skill.txt](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/skill.txt)).

**Learning scope:** `per-project` `cross-task` — A checkpoint accumulates across tasks in one learning run, and a learned `skill_library_dir` can be loaded for a new task or new Minecraft world. It is not a global service shared across unrelated projects unless users copy/import the checkpoint.

**Learning timing:** `online` `staged` — During lifelong learning, skills, task lists, QA cache, chest memory, and events are written as the agent acts. Reusing a learned skill library for inference is a staged/offline transfer step.

**Distilled form:** `prose` `symbolic` `parametric` — Raw observations and critiques become prose descriptions and QA answers; successful behaviors become symbolic JavaScript functions and JSON records; Chroma embeddings provide parametric retrieval state.

**Survey placement.** Voyager is a strong trace-derived code-promotion system: traces do not merely create reminders, they create executable affordances. It strengthens the survey distinction between raw trace artifacts and distilled behavior-shaping artifacts, and it highlights the governance problem of promoting generated code without source-linked tests or invalidation metadata.

## Read-back

**Read-back:** `both` — The skill manager exposes explicit retrieval methods, while the main agent loop automatically retrieves skills for the current context/chatlog and injects them into the receiving action prompt; checkpoint state such as chest memory and curriculum progress is also pushed into later prompts by the orchestration code.

**Read-back signal:** `coarse` `inferred / embedding` — Chest memory, completed/failed tasks, and current observations are included by rule or warm-up thresholds; skills and cached QA questions are selected by embedding similarity over the current context/question.

**Faithfulness tested:** `no` — Voyager evaluates task success through the critic and reports aggregate task performance in the README, but the inspected code does not run per-decision with/without-memory ablations, perturb retrieved skills, or audit whether a fired skill changed the next generated action.

**Direction edge case.** `retrieve_skills(query)` is a pull API from the Python orchestrator's perspective. For the action LLM, the same retrieved JavaScript arrives unsolicited in the system message before generation, so it is push read-back for the receiving agent. The full `programs` string passed to `env.step` is also executable scope, not just textual context.

**Selection, scope, and complexity.** Skill selection is bounded by `retrieval_top_k`, defaulting to five, and by Chroma similarity over generated descriptions. QA cache reuse uses nearest-question similarity with a hard score threshold. The selected material can be large because it is JavaScript source, and the system has no token-aware packer or source-aware complexity budget.

**Injection point.** Skill read-back occurs before each action model call: `reset()` retrieves from the initial task context, and `step()` retrieves again from task context plus summarized chat log after execution. Curriculum and chest memory are assembled before curriculum/action prompts. Later event recording, skill creation, and vector persistence are write-side maintenance.

**Authority at consumption.** Retrieved skill code is advisory prompt context for the action LLM, but it is also executable material available to the Mineflayer execution environment. QA answers and chest/task memory are advisory context. The critic has validation authority over success, but the retrieved memories are not themselves hard gates.

**Other consumers.** Humans can inspect JSON/code/text checkpoint artifacts and share skill libraries. The Chroma indexes are less transparent than the code and descriptions, and the repository does not provide a review UI or provenance report for deciding which generated skills should remain.

## Curiosity Pass

**Voyager is closer to executable memory than ordinary RAG.** The embedding store retrieves descriptions, but the thing that matters is code reuse. Treating Chroma as the memory would miss the main behavioral authority.

**The success gate is useful but thin.** A critic success verdict admits the generated function, yet the stored skill does not retain the task trace, test case, preconditions, or failure modes that justified it.

**Skill descriptions are both helpful and lossy.** Retrieval keys are generated summaries of code rather than the code itself. That keeps retrieval cheap, but a bad or generic description can hide the operative preconditions of the function.

**The checkpoint has several memory layers with different force.** Skill code changes what can be executed; chest memory changes world-state context; completed/failed tasks change curriculum selection; event logs support analytics/resume. Lumping them together as "memory" hides important authority differences.

**The environment can execute more than the prompt shows.** The prompt receives top-k retrieved skills, while `self.skill_manager.programs` concatenates all learned programs for execution. That split is efficient for the model context but creates a difference between visible prompt affordances and runtime affordances.

## What to Watch

- Whether future Voyager variants add tests, source traces, or precondition metadata to each learned skill. That would make executable memory more reviewable and safer to transfer.
- Whether skill retrieval becomes token-budgeted or call-graph aware. That would change the context-efficiency story from top-k injection to governed packing.
- Whether duplicate or obsolete skills gain explicit retirement/invalidation instead of overwrite/delete behavior. That would make the write side closer to a maintained knowledge base.
- Whether the critic is supplemented by deterministic task checks. That would strengthen promotion gates for high-authority executable artifacts.
- Whether shared community checkpoints include provenance and version metadata. That would clarify when imported skill libraries should be trusted.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: Voyager's skills matter because they are retrieved and injected into later action prompts, not merely stored in checkpoint files.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Voyager requires separating file storage, vector indexes, generated code, prose descriptions, and execution authority.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - applies: Voyager turns task trajectories into reusable symbolic/prose/parametric artifacts.
- [Codification](../../notes/definitions/codification.md) - applies: successful action attempts cross from natural-language task context into executable JavaScript skills.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompts, control primitives, validators, and executable skills can carry instruction or execution force.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: QA answers, chest memory, and retrieved descriptions mostly advise rather than enforce.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - frames: Voyager reduces full trace replay into top-k skill injection, but leaves complexity and token cost mostly unmanaged.
