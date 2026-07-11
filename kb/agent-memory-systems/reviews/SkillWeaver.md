---
description: "SkillWeaver review: web-agent trajectories distilled into Playwright API skills with LLM relevance push and verification metadata"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
tags: [trace-derived]
---

# SkillWeaver

SkillWeaver, from the OSU NLP Group's `OSU-NLP-Group/SkillWeaver` repository, is a web-agent self-improvement framework that explores WebArena-style websites, proposes useful shortcut tasks, attempts them with Playwright code, and distills successful trajectories into reusable Python APIs. At the reviewed commit, the retained memory is a file-backed procedural knowledge base: `_code.py` functions, `_metadata.json` test/version/reference records, optional `_semantic_knowledge.txt`, exploration logs, and task-time relevance predictions. The system is an agent-memory system because past browser trajectories can become executable skills that later agents are instructed to call.

**Repository:** https://github.com/OSU-NLP-Group/SkillWeaver

**Reviewed commit:** [f2a63d65d0f6ff46ac30e817cede8797f8f25b97](https://github.com/OSU-NLP-Group/SkillWeaver/commit/f2a63d65d0f6ff46ac30e817cede8797f8f25b97)

**Source directory:** `related-systems/OSU-NLP-Group--SkillWeaver`

## Core Ideas

**Successful browser trajectories become Playwright APIs.** The exploration loop chooses either an exploration task or a test task, attempts it in the browser, writes states/actions/trajectory artifacts, asks an LLM success checker whether the trajectory achieved the task, and calls `KnowledgeBase.update(...)` only when the attempt succeeds ([skillweaver/explore.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/explore.py), [skillweaver/knowledge_base/check_success.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/check_success.py)). The resulting APIs are intended to compress multi-step website interactions into callable functions.

**The procedural store is executable code plus governance metadata.** `KnowledgeBase.save(prefix)` writes `prefix_code.py`, `prefix_metadata.json`, and `prefix_semantic_knowledge.txt`; `load_knowledge_base(prefix)` reads the same triplet back ([skillweaver/knowledge_base/knowledge_base.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/knowledge_base.py)). Metadata tracks per-function version, test count, references, and update/test events, so the same function name can be overwritten while preserving a lightweight event trail.

**Skill synthesis is constrained by static checks before it enters the store.** `KnowledgeBase.update(...)` asks an LLM for updated Python, retries up to ten times on violations, then merges function definitions into the current AST. `check_code(...)` rejects syntax errors, non-async functions, missing docstrings, missing initial `page.goto`, broad `try` blocks, `while` loops, CSS-style selectors, unsupported annotations, `*_id` parameter names, and type errors ([skillweaver/knowledge_base/knowledge_base.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/knowledge_base.py), [skillweaver/knowledge_base/code_verification.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/code_verification.py)). The checks are shape and style gates, not proof that the function completes a future task.

**Runtime read-back is relevance-filtered prompt injection.** Before an attempted task, `create_skill_library_prompt(...)` either returns all functions for exploration/test modes or calls `knowledge_base.retrieve(task_string, lm)` for production and retrieval-enabled exploration. `retrieve(...)` asks an LLM to identify relevant functions from the function list and returns formatted signatures/docstrings for the selected functions ([skillweaver/create_skill_library_prompt.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/create_skill_library_prompt.py), [skillweaver/knowledge_base/knowledge_base.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/knowledge_base.py)). There is also an unused embedding-similarity helper, but the wired retrieval path is LLM judgment, not vector search.

**Context efficiency is topological compression plus one-shot selection.** The learned API compresses a multi-action browser procedure into one function call, and retrieval limits the agent-facing prompt to LLM-selected functions instead of dumping the full library. There is no persistent vector index, progressive disclosure ladder, token budget, or per-step retrieval refresh in the main `attempt_task(...)` path; selected functions are computed once before the action loop and then reused for every generated action in that task ([skillweaver/attempt_task.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/attempt_task.py)).

**Adoption affordance is plain Python interop.** The stored skills are inspectable Python functions and can also be converted into Browser-Use controller actions by executing the stored code and registering selected functions as controller actions ([skillweaver/attempt_task_browser_use.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/attempt_task_browser_use.py), [skillweaver/knowledge_base/knowledge_base.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/knowledge_base.py)). That makes the memory easy to inspect and reuse, but also means activated memory can execute browser automation code.

## Artifact analysis

- **Storage substrate:** `files` `repo` `in-memory` — The durable procedural KB is saved as local files (`*_code.py`, `*_metadata.json`, `*_semantic_knowledge.txt`) and the repository includes shipped `skillnet/*/*_kb_post_code.py` examples; active runs also hold the KB in a Python object protected by an async lock.
- **Representational form:** `prose` `symbolic` — Function docstrings, usage logs, prompts, task descriptions, success-check explanations, and semantic knowledge are prose; Python functions, AST merges, JSON metadata, schemas, test counts, event records, and Playwright calls are symbolic. The reviewed wired path does not persist embeddings or model weights as the operative memory.
- **Lineage:** `authored` `trace-extracted` — Templates, validators, harness code, and shipped skillnet examples are authored; learned functions and metadata are distilled from browser trajectories, success checks, recovery notes, and test executions.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Logs and diagnostics are evidence; selected functions and docstrings instruct later action; static checks, codegen sanity checks, type checks, and hide-unverified filtering constrain use; retrieval routes and ranks functions through LLM judgment; success checks and test counts validate promotion; update prompts turn traces into learned APIs.

**Raw trajectory artifacts.** Storage substrate: per-iteration files under the exploration or attempt output directory, including `task.json`, `choose_task_meta.json`, state snapshots, `*_action.json`, `trajectory_pretty.txt`, `success_check.json`, `kb_update_diagnostics.json`, `perfmon.json`, and `trace.zip`. Representational form: prose/symbolic browser states, actions, screenshots, generated code, exceptions, recoveries, and LLM judgments. Lineage: trace-extracted from a task attempt. Behavioral authority: knowledge artifact for audit and update prompts; raw traces do not directly act unless converted into an API.

**Procedural API library.** Storage substrate: `*_code.py` files and the in-memory `KnowledgeBase.code` string. Representational form: symbolic executable Python plus prose docstrings. Lineage: authored for shipped examples or trace-extracted through `KnowledgeBase.update(...)` from successful attempts. Behavioral authority: system-definition artifact; once selected, the code is embedded into the generated action module or registered as a Browser-Use controller action and can directly change browser behavior.

**Metadata and verification state.** Storage substrate: `*_metadata.json` and in-memory `metadata`. Representational form: symbolic JSON fields for `global_version`, per-function `version`, `test_count`, `references`, and `events`. Lineage: automatically updated when functions are created, overwritten, marked tested, or successfully executed in a test task. Behavioral authority: validation and routing authority, because `hide_unverified` and `only_verified` paths decide which APIs are visible for evaluation or test prompts.

**Semantic knowledge sidecar.** Storage substrate: `*_semantic_knowledge.txt` and `KnowledgeBase.semantic_knowledge`. Representational form: prose. Lineage: loaded and passed through update/task-proposal prompts, but the inspected single-update path leaves `semantic_update_diagnostics = None` and does not implement a semantic sidecar update. Behavioral authority: weak knowledge and prompt context; it can influence proposal and synthesis prompts when present, but the central implemented memory is procedural code.

**Retrieval and tool schemas.** Storage substrate: no durable index in the wired path; retrieval decisions are transient LLM responses saved as `relevant_function_prediction.json` during attempts. Representational form: prose reasoning plus symbolic function names and JSON schemas. Lineage: generated from the current task and parsed KB functions. Behavioral authority: routing/ranking authority over which APIs become visible to the action agent or Browser-Use controller.

**Promotion path.** SkillWeaver promotes website experience through staged artifacts: browser trace -> LLM success judgment -> LLM-generated Playwright function -> static/schema/type validation -> AST merge and versioned metadata -> optional test-count increment -> task-time relevance selection -> prompt/controller execution. That path crosses from trace evidence into executable system-definition authority, but it does not attach stable source-node ids, replay handles, or explicit retirement records to each generated function.

## Comparison with Our System

SkillWeaver and Commonplace both treat prior agent work as material that should change later agent behavior, but they codify different endpoints. SkillWeaver turns successful task trajectories into executable Playwright APIs. Commonplace turns sources, notes, reviews, instructions, schemas, and generated indexes into inspectable repo artifacts. SkillWeaver is stronger at reducing repeated UI interaction into callable code; Commonplace is stronger at source-grounded prose, archival replacement, link contracts, and deterministic validation of retained artifacts.

The strongest alignment is promotion discipline. SkillWeaver does not let arbitrary traces directly become future behavior; it requires a success judgment, an LLM synthesis step, and code-shape checks. That resembles Commonplace's preference for moving raw logs into typed artifacts before they gain authority. The difference is oracle strength: SkillWeaver's promotion oracle is an LLM success checker plus static code checks, while Commonplace often wants citations, human/agent review, and validation over artifact structure.

The strongest divergence is read-back. Commonplace mostly asks the agent to pull relevant files through `rg`, indexes, links, and skills. SkillWeaver's host loop chooses relevant APIs before the action model call and pushes them into the action context. That avoids expecting the action model to search the library, but it moves a lot of trust into the retrieval LLM and the generated API docs.

Another divergence is governance of executable memory. SkillWeaver overwrites functions by name, increments version, resets test count, and appends references/events. Commonplace would need a stronger lifecycle before granting generated code comparable authority: explicit supersession, provenance links, review status, rollback, and retirement.

### Borrowable Ideas

**Use executable skills as a promoted endpoint only where the action boundary is narrow.** In Commonplace, a repeated repair or validation workflow could graduate from a note into a `commonplace-*` command or skill when inputs, oracle, and rollback are clear. Ready for narrow developer workflows, not for general KB writing.

**Keep verification metadata next to generated procedures.** SkillWeaver's `test_count`, `version`, `references`, and event history are lightweight but useful. Commonplace could attach similar generated-procedure metadata to workshop scripts or skills. Ready now as a convention.

**Separate relevance selection from execution authority.** SkillWeaver uses docstrings/signatures as the retrieval surface while code remains the action surface. Commonplace can borrow this for tools: index concise descriptions for selection, then execute or inspect the canonical script. Ready now for command/skill catalogs.

**Retry synthesis against deterministic shape checks.** The update loop feeds violations back to the synthesizer before accepting code. Commonplace already validates artifacts after writing; borrowing the retry loop for generated procedures is useful when the validator gives actionable errors. Ready now for code-generation workflows.

**Do not borrow LLM-only success as enough for durable library authority.** A success checker over trajectory plus screenshot is useful evidence, but Commonplace should require replay, source grounding, or human review before generated code gets instruction-level authority. Needs a concrete use case and stronger oracle.

## Write side

**Write agency:** `manual` `automatic` — Operators choose websites, schedules, initial KBs, and whether to run exploration/evaluation, but the distinctive writes are automatic: exploration writes traces, LLM success checks, generated functions, metadata updates, test-count increments, diagnostics, and post-iteration KB snapshots.

**Curation operations:** `evolve` `promote` — Existing functions can be replaced in place by exact name, incrementing version and resetting `test_count`; successful test tasks increment test counts and thereby promote functions into verified visibility. The system does not implement durable deduplication, consolidation, contradiction invalidation, decay, or cross-memory synthesis beyond generating/updating individual APIs from one attempt.

### Trace-derived learning

**Trace source:** `trajectories` `tool-traces` `session-logs` — The raw signal is browser-agent task execution: accessibility-tree states, screenshots, generated Playwright code, executed actions, stdout, exceptions, recovery annotations, final states, and success-check judgments.

**Learning scope:** `per-project` `cross-task` — A KB prefix is website/project scoped, while functions learned during exploration are intended to transfer across later tasks on that website and shipped `skillnet` libraries cover multiple WebArena sites.

**Learning timing:** `online` `staged` — During exploration, a successful iteration can update the KB before later iterations; evaluation and demo runs can also load a previously staged KB prefix.

**Distilled form:** `prose` `symbolic` — Distilled artifacts are Python function code, docstrings, schemas, metadata, and optional semantic prose, not model weights.

**Extraction.** `_choose_explore_task(...)` asks an LLM to propose useful website shortcut tasks. `attempt_task(...)` records the trajectory. `check_success_simple(...)` judges whether the task succeeded from the action log and final screenshot. `KnowledgeBase.update(...)` then prompts an API-synthesis model with existing verified procedures, semantic knowledge, action history, intended task, and feedback, and accepts code only after static checks pass ([skillweaver/explore.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/explore.py), [skillweaver/templates/kb_procedural_update_base.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/kb_procedural_update_base.md)).

**Distillation trigger and policy.** The trigger is operator-run exploration. Each iteration decides between exploring for a new skill and testing an unverified one according to `explore_schedule`. A successful exploration task can create or update a function; a successful test task increments that function's `test_count`; an unsuccessful or exception-bearing test does not count as verified. The policy is success-gated and shape-validated, with optional recovery annotations fed into the trajectory string.

**Survey placement.** SkillWeaver belongs in the trace-to-executable-procedure family. It strengthens the survey distinction between raw trace retention and distilled behavior-shaping artifacts: the trajectory logs are evidence, while the accepted Python APIs plus metadata are the durable operative memory.

## Read-back

**Read-back:** `push` — Retained APIs reach the action agent because the host loop selects visible functions before the model call and injects formatted function text into the action prompt; the Browser-Use path similarly retrieves functions and registers them as controller actions before `agent.run()`.

**Read-back signal:** `inferred / judgment` — The wired retrieval path asks an LLM to judge which functions may be useful for the current task. Exploration/test modes can also expose all or verified functions, but production-style task attempts use the LLM relevance judgment path.

**Faithfulness tested:** `no` — The code includes evaluation scripts and supports running with or without `knowledge_base_path_prefix`, but the inspected repository does not implement a built-in with/without-memory ablation or perturbation test proving that a selected API caused a specific behavior change.

**Direction edge case.** `KnowledgeBase.retrieve(...)` is a pull API from the orchestrator's perspective, but it is push for the action model: `attempt_task(...)` computes `visible_functions_string` before the loop, and `codegen_generate(...)` receives that same string as prompt context at each step. The model is instructed to use a KB function when the corresponding action exists, so selected skills have stronger authority than passive notes.

**Selection, scope, and complexity.** Selection is LLM judgment over the parsed function list and current task string, not a durable embedding index. Scope is the loaded KB prefix and the current `hide_unverified` policy; evaluation hides unverified functions unless `--allow-unverified-apis` is passed, while demo task attempts set `hide_unverified = False`. Complexity is bounded by selected functions, but a selected function is full executable browser code plus documentation, so the complexity risk is procedural opacity rather than just token volume.

**Authority at consumption.** In the native SkillWeaver path, selected API text instructs the code-generation model and the full KB code is included in the generated action module, making selected names callable. In the Browser-Use path, selected functions become controller actions. That is system-definition authority: selected memory can execute, not merely advise.

**Other consumers.** Humans can inspect generated code, metadata, diagnostics, logs, and shipped `skillnet` libraries. Evaluation scripts consume task outputs and evaluator scores; the explored agent does not automatically rewrite the KB during a production task attempt.

## Curiosity Pass

**The semantic sidecar is less implemented than the procedural story.** The KB constructor carries `semantic_knowledge`, templates mention semantic knowledge, and save/load persists it, but the inspected `KnowledgeBase.update(...)` sets `semantic_update_diagnostics = None`. The working memory mechanism is procedural APIs, not a rich semantic KB.

**There is an embedding helper but no persistent vector memory.** `get_most_relevant_functions_via_embedding_similarity(...)` can score functions with `text-embedding-3-small`, but `create_skill_library_prompt(...)` uses the LLM `retrieve(...)` path. Reviews should not classify SkillWeaver as a vector-store memory system at this commit.

**Verification is real but narrow.** Static checks constrain generated APIs and test-count metadata records exception-free calls, yet successful future behavior is still mostly empirical. A function can be syntactically valid, documented, and tested once while remaining brittle under changed UI state.

**Overwrite-by-name is a lightweight evolution mechanism.** Replacing a function resets `test_count` and appends references/events, which is better than silent overwrite. It is still not full invalidation: there is no explicit obsolete state, replay evidence, or history of the prior implementation unless prior output snapshots remain available.

**The read-back push is frontloaded per task.** SkillWeaver does not refresh skill retrieval after each action in the native path, even if the page state changes. That keeps the loop simple but can miss skills whose relevance becomes apparent only after navigation.

## What to Watch

- Whether the semantic knowledge update path becomes implemented. That would add a prose memory layer distinct from executable skills.
- Whether the embedding helper becomes the deployed retrieval path or a persistent index. That would change the read-back signal from LLM judgment toward embedding-based inferred push.
- Whether generated APIs gain explicit provenance links back to trajectory files, success-check outputs, recovery annotations, and website/environment versions. That would make executable memory easier to audit and invalidate.
- Whether evaluation scripts grow first-class ablation reports comparing no-KB, all-KB, verified-only, and retrieved-KB modes. That would strengthen faithfulness claims.
- Whether function replacement gains supersession, rollback, or retirement metadata. That would make the `evolve` operation safer to borrow for Commonplace-controlled procedures.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: SkillWeaver explicitly wires retained APIs into pre-action prompt/controller context.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - applies: successful browser trajectories become reusable procedures for later tasks.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: SkillWeaver requires separating raw traces, generated code, metadata, semantic sidecars, and retrieval decisions.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - frames: generated APIs shift from evidence to instruction/execution authority when selected.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: Playwright APIs, validators, retrieval decisions, and controller actions configure future behavior.
- [Codification](../../notes/definitions/codification.md) - exemplifies: SkillWeaver crosses from natural-language/task traces into executable Python procedures.
- [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) - applies: LLM success checks and exception-free tests are useful but weaker than deterministic replay proofs.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - exemplifies: the system mutates deployable, readable APIs rather than fine-tuning model weights.
