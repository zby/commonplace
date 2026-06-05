---
description: "SkillWeaver review: WebArena web-agent loop that distills successful browser trajectories into reusable Playwright APIs with LLM-selected pre-action skill injection"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-02"
---

# SkillWeaver

> Replaced 2026-06-05. See [SkillWeaver](./SkillWeaver.md) for the current review.

SkillWeaver, from OSU-NLP-Group's `SkillWeaver` repository, is a research framework for self-improving web agents. It explores a website, proposes practice tasks, executes Playwright actions, judges success, and distills successful trajectories into reusable Python APIs. The retained memory is not a note store or vector database. It is a generated skill library: executable browser procedures with docstrings, metadata, optional verification counts, and retrieval-time selection before the acting agent generates its next code step.

**Repository:** https://github.com/OSU-NLP-Group/SkillWeaver

**Reviewed commit:** [f2a63d65d0f6ff46ac30e817cede8797f8f25b97](https://github.com/OSU-NLP-Group/SkillWeaver/commit/f2a63d65d0f6ff46ac30e817cede8797f8f25b97)

**Last checked:** 2026-06-02

## Core Ideas

**Skills are executable Playwright APIs, not prose memories.** The central `KnowledgeBase` stores Python function source plus metadata about versions, references, test counts, and update events. Functions are parsed with `ast`, merged by name, formatted with Black, and later exposed as ordinary callable globals in generated `act(page)` code or as Browser-Use controller actions (https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/knowledge_base.py).

**The learning loop is trajectory-to-API distillation.** Exploration chooses either a new exploration task or a test task, attempts it in a browser, writes action/state traces, checks success with an LLM over the trajectory and final screenshot, and calls `KnowledgeBase.update()` only after a successful non-test attempt. The update prompt asks for generalized Playwright functions with docstrings and usage logs, then static checks reject malformed or unsafe skill code before the function is merged (https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/explore.py, https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/check_success.py, https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/kb_procedural_update_base.md).

**Practice separates unverified generated skills from reusable ones.** Test iterations select untested functions by a simple practice-utility score, generate arguments from the current page state, and increment a function's `test_count` only when it executes without exceptions or recovery. In evaluation, `hide_unverified` defaults to hiding untested functions unless the caller passes `--allow-unverified-apis` (https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/explore.py, https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/evaluation/evaluate_single_task.py).

**Context efficiency is function selection before action generation.** Before an attempt, `create_skill_library_prompt()` calls `KnowledgeBase.retrieve()` for production tasks and, by default, for exploration/test tasks. Retrieval asks an LLM to choose relevant function names from formatted signatures and docstrings; only those selected functions are injected into the codegen prompt. This bounds volume and complexity better than loading an entire skill library, but the selector itself is LLM-mediated and not evaluated for precision in the code (https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/create_skill_library_prompt.py, https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/predict_relevant_functions.md).

**The acting prompt gives selected skills strong authority.** The codegen template tells the agent it has a library of Python functions and that it is required to use the knowledge-base function corresponding to an action if one exists. Generated action code is then type-checked against the available functions and executed with the knowledge-base code imported into the module (https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/codegen.md, https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/agent.py).

**Recovery records failed locators as repair evidence.** When Playwright locator operations fail, optional recovery wraps locator calls, captures the accessibility tree, asks an LLM for a replacement locator, tests that it points to the selected element, and records recovery details. Those recovery annotations can be included in trajectory strings so later update prompts can improve a broken skill's documentation or implementation (https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/environment/patches.py, https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/agent.py).

## Artifact analysis

- **Storage substrate:** `files` — Per-iteration output directories under the caller's `out_dir`, including `choose_task_meta.json`, state/action JSON files, `trajectory_pretty.txt`, `success_check.json`, `kb_update_diagnostics.json`, `trace.zip`, videos, and performance logs
- **Representational form:** `prose` `symbolic` — Prose trajectory strings, docstrings, prompt text, and semantic knowledge text plus symbolic JSON, executable Python, metadata, static checks, and prompt assembly
- **Lineage:** `authored` `trace-extracted` — Authored repository code/templates and system checks combine with browser trajectories, success judgments, recovery evidence, and generated skill libraries distilled from traces
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Traces and diagnostics are evidence; prompt templates and generated skills instruct/execute; static checks enforce/validate; retrieval and hide-unverified route; practice utility ranks; update/practice loops learn

**Exploration traces.** Storage substrate: per-iteration output directories under the caller's `out_dir`, including `choose_task_meta.json`, state/action JSON files, `trajectory_pretty.txt`, `success_check.json`, `kb_update_diagnostics.json`, `trace.zip`, videos, and performance logs. Representational form: mixed symbolic JSON, prose trajectory strings, screenshots/videos, and Playwright trace archives. Lineage: generated from a specific website state, proposed task, browser trajectory, success check, and model calls. Behavioral authority: knowledge artifact authority during the run; traces are evidence for whether a skill should be distilled, not themselves the normal read-back surface for future tasks.

**Generated skill code.** Storage substrate: saved `*_code.py` files from `KnowledgeBase.save()` and checked-in `skillnet/*/*_kb_post_code.py` libraries. Representational form: symbolic executable Python plus prose docstrings. Lineage: LLM-distilled from successful trajectories or later recovery/test feedback, merged by function name through `KnowledgeBase._apply()`, and formatted as Python source. Behavioral authority: system-definition artifact. Once selected, a skill expands the agent's action space and can directly execute browser operations.

**Skill metadata.** Storage substrate: saved `*_metadata.json` produced by `KnowledgeBase.save()`; the checked-in `skillnet/` snapshot at this commit includes code files but not full metadata files. Representational form: symbolic JSON with function version, `test_count`, references, and events. Lineage: generated by updates, function replacement, `increment_test_count()`, and `mark_all_as_tested()`. Behavioral authority: routing and validation-like authority because `hide_unverified` and `is_tested()` determine which functions are visible to later retrieval and evaluation.

**Semantic knowledge text.** Storage substrate: saved `*_semantic_knowledge.txt` in the runtime knowledge-base format. Representational form: prose. Lineage: the templates carry semantic knowledge into update prompts, but in this commit `KnowledgeBase.update()` sets `semantic_update_diagnostics = None` and applies only generated procedural code, so active semantic-memory maintenance is not implemented in the inspected path. Behavioral authority: advisory context if loaded into prompts; weaker than the procedural API layer in this checkout.

**Retrieval selector and prompt assembly.** Storage substrate: repository code and markdown prompt templates. Representational form: mixed symbolic Python plus prose instructions. Lineage: authored system code. Behavioral authority: system-definition authority: it chooses which retained functions are exposed, how they are described, and how strongly the agent is told to use them. This is the main read-back path.

**Verification and recovery gates.** Storage substrate: repository code plus per-run diagnostics. Representational form: symbolic static checks, schema generation, type-checking, exception wrappers, and prose recovery prompts. Lineage: authored code plus runtime failure evidence. Behavioral authority: validation and repair authority. Static checks can reject proposed skill updates; runtime test success increments `test_count`; recovery can disable a failed function during an attempt and supply evidence for later repair.

**Promotion path.** SkillWeaver's promotion path is raw browser/task trace -> LLM success judgment -> LLM-generated Playwright function -> static verification -> saved skill library -> optional no-exception practice -> visible function for later task retrieval. That path crosses from trace evidence to executable system-definition artifact, which is why this review carries `trace-derived`.

## Comparison with Our System

| Dimension | SkillWeaver | Commonplace |
|---|---|---|
| Primary purpose | Self-improving web agents through generated browser APIs | Agent-operated methodology KB with typed, reviewable artifacts |
| Main retained artifact | Playwright function library with docstrings and metadata | Markdown notes, reviews, indexes, instructions, sources, and schemas |
| Learning source | Browser trajectories, screenshots, success checks, recovery traces, practice outcomes | Human/agent-authored artifacts, source snapshots, validation, review reports |
| Promotion target | Executable APIs that expand the agent's action space | Knowledge and system-definition artifacts under collection/type contracts |
| Read-back | LLM-selected functions injected before action generation | Search/index/link/skill pull, always-loaded instructions, validation/review gates |
| Governance | Static code checks, no-exception tests, optional hidden-unverified filter | Schema validation, source citation, review bundles, git diffs, collection routing |

SkillWeaver and Commonplace both treat retained artifacts as behavior-shaping surfaces rather than passive storage. The difference is form and authority. SkillWeaver learns executable browser procedures from trajectories and then gives them high operational authority at the next action. Commonplace usually learns by writing and reviewing explicit prose or schema artifacts, then asks agents to pull them through navigation and validation workflows.

SkillWeaver is stronger where the task domain has a tight simulator and an external-ish success oracle. WebArena/VWA tasks have bounded sites, repeatable containers, action traces, screenshots, and evaluators. That makes trace-derived procedural learning practical. Commonplace's methodology notes are less amenable to direct trajectory-to-code promotion because semantic correctness is harder to test with a no-exception browser run.

SkillWeaver is weaker on lineage inside the promoted artifact. Metadata records iteration references and update/test events, but the generated function body and docstring do not carry fine-grained citations to the exact trajectory steps, screenshots, or success evidence that justified each behavior. Commonplace's source-grounded reviews are slower, but they preserve citation and review context more directly.

### Borrowable Ideas

**Promote traces into executable helpers only in bounded domains.** Commonplace could borrow this for narrow operational routines such as validation repair, source snapshot cleanup, or repeated review-bundle triage, where success can be tested. Ready for tool-facing workflows with objective checks; not ready for broad methodology-note writing.

**Keep a test-count or confidence field separate from existence.** SkillWeaver's `hide_unverified` split is useful: an artifact can exist without being eligible for high-authority read-back. Commonplace could apply the same pattern to generated commands, candidate skills, or trace-derived instructions. Ready now as vocabulary and metadata discipline.

**Use retrieval-time tool narrowing before action generation.** Injecting every helper into a prompt scales poorly. Commonplace could add a reviewed, bounded "candidate commands/artifacts for this task" step for large workflows. Needs a faithfulness test so the selector does not hide the one artifact that matters.

**Require generated procedural memory to be executable and statically checked.** SkillWeaver rejects generated skills with syntax, argument, selector, type, and structure violations. Commonplace should copy this whenever a learned artifact becomes code, CLI behavior, schema, or validator. Ready now for symbolic artifacts.

**Do not borrow high-authority executable memory without provenance.** A generated function can silently encode an accidental UI assumption. Commonplace should require source references, test cases, and invalidation conditions before learned procedures enter durable shared use.

## Write-side placement

**Write agency:** `automatic` — the exploration, success-check, update, static-check, practice, and recovery paths mutate the generated skill library without a manual authoring channel in the reviewed loop.

**Curation operations:** `evolve` `synthesize` `promote` — successful trajectories synthesize new Playwright functions, function-name merging and recovery/test feedback can update existing skills, and `test_count` plus `hide_unverified` promote practiced functions into higher-visibility read-back.

### Trace-derived learning

**Trace source:** `tool-traces` `event-streams` `trajectories` — Browser action/state records, Playwright traces and videos, recovery events, screenshots, and task-attempt trajectories feed the skill update loop.

**Learning scope:** `per-task` `per-project` `cross-task` — Learning is bounded by attempted tasks and website/task-family libraries, then saved or copied for later evaluation and reuse.

**Learning timing:** `online` `staged` — Exploration grows the library iteratively, while evaluation loads selected libraries and can stage visibility through `hide_unverified`.

**Distilled form:** `prose` `symbolic` — Successful trajectories become executable Python functions with docstrings, metadata, prompt-visible signatures, and optional semantic knowledge text.

**Trace source.** SkillWeaver qualifies as trace-derived learning. Raw signals include proposed tasks, browser accessibility trees, screenshots, generated action code, stdout/results/exceptions, recovery attempts, success-check outputs, Playwright traces, videos, and WebArena/VWA evaluator results. The central trigger boundary is one attempted task iteration; a separate practice/test boundary exists for generated functions.

**Extraction.** Extraction is LLM-mediated. `check_success_simple()` judges whether a trajectory completed its intended task; on success, `KnowledgeBase.update()` prompts the API-synthesis model to generalize the trajectory into Playwright functions. Static checks reject functions with invalid syntax, non-async top-level definitions, missing `page` first parameter, missing docstrings, disallowed selectors, unsupported annotations, try/while patterns, missing `page.goto()`, and type errors. The no-exception practice loop is a narrower oracle for whether a function can execute, not whether it solves all future semantic variants.

**Scope and timing.** Scope is website/task-family local. A skill library can be saved, loaded, copied into evaluation output, or converted into a Browser-Use controller, but the functions are still tied to the UI and semantics of the explored site. Timing is online during exploration and staged during benchmark evaluation: exploration iteratively grows the library; evaluation loads a selected library and can hide unverified APIs.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), SkillWeaver belongs in the trajectory-to-executable-artifact family. It strengthens the survey claim that trace-derived learning becomes more trustworthy when the promoted artifact has an executable form and a task environment supplies success signals. It also exposes a governance split: execution tests and static checks can validate syntax and some UI assumptions, but they do not replace source-level lineage for why a skill's docstring or procedure is semantically correct.

## Read-back placement

**Read-back:** `both` — The agent can pull from the skill library through explicit retrieval machinery, and task attempts also run relevance-gated pre-action selection that pushes chosen generated skills into the acting prompt before code generation.

**Read-back signal:** `inferred / judgment` — The active push path asks an LLM to select relevant function names from the current task string plus formatted skill signatures and docstrings.

**Faithfulness tested:** `no` — The implementation evaluates task success and function execution, but the review found no WITH/WITHOUT read-back ablation proving a pushed skill changed a decision.

**Direction.** SkillWeaver has both pull and engineered push. The retrieval module is explicitly called by the attempt loop, but from the acting agent's perspective selected functions arrive in the prompt before it writes the next `act(page)` function.

**Targeting and signal.** The push path is `instance`-targeted: each attempt turns the current task into a task string and asks retrieval to select functions for that task instance. The signal is `inferred / judgment`, because `KnowledgeBase.retrieve()` asks an LLM to judge relevance over the task string and formatted skill signatures/docstrings. There is also an embedding-similarity helper in `KnowledgeBase`, but the active prompt path uses LLM function-name selection.

**Selection, scope, and complexity.** Selection scope is the currently loaded knowledge base, filtered by `hide_unverified` when configured. Prompt complexity is bounded by selected functions, not by a hard token budget. If the library has fewer than five functions, the embedding helper would return all functions, but the active LLM retrieval path can still select by name. Actual selector precision and context dilution are not verified from code.

**Authority at consumption.** Selected functions have strong operational authority. The codegen prompt says matching knowledge-base functions are required when they exist, the generated `act(page)` code can call them directly, and Browser-Use integration can register selected functions as controller actions. This is more than advisory memory; it is an action-space extension.

**Faithfulness.** SkillWeaver evaluates task success and records no-exception function tests, but I did not find a WITH/WITHOUT read-back ablation in the implementation path itself. The README describes comparing with and without `--knowledge-base-path-prefix`, and evaluation commands support that comparison, but the code does not prove that any individual pushed skill improved a given decision.

**Other consumers.** Human researchers consume the saved trajectories, diagnostics, checked-in `skillnet/` libraries, and benchmark result directories. Browser-Use consumes selected functions as controller actions. Static checkers and evaluators consume the same skill artifacts as governance surfaces.

## Curiosity Pass

**The semantic knowledge field is less active than the README framing suggests.** The update prompts mention semantic knowledge, and the save/load format carries it, but the inspected update implementation does not rewrite `semantic_knowledge`. The durable learning mechanism at this commit is procedural API synthesis.

**The strongest governance is structural, not semantic.** Static checks are valuable, but they mainly enforce shape: async functions, docstrings, parameter schemas, selector style, no broad try/while, and type consistency. They cannot tell whether a generated skill overgeneralized from one successful trajectory.

**The retrieved skill can be too authoritative.** The prompt requires using a matching knowledge-base function if one exists. That helps reuse, but if retrieval selects a stale or brittle function, the model is pushed toward using it rather than re-solving the page from first principles.

**The checked-in `skillnet/` libraries are useful evidence but not full runtime records.** They show the generated API style, including docstrings and usage logs, but the metadata/test-count side of the runtime knowledge-base format is not checked in beside those code files at this commit.

**Browser-Use integration is a strong adoption affordance.** SkillWeaver can turn learned functions into a `Controller`, so the learned APIs are not locked to its own codegen loop. That makes the skill library closer to portable action middleware than a private memory cache.

## What to Watch

- Whether future commits add fine-grained provenance from generated functions back to trajectory ids, screenshots, success checks, and recovery events; that would make trace-derived executable memory auditable.
- Whether semantic knowledge updates are implemented or removed from the active workflow; that determines whether SkillWeaver remains procedural-only memory or gains a real prose knowledge layer.
- Whether retrieval gains measured precision/recall or per-task ablations, because the `push-activation` mechanism's quality is otherwise assumed from prompt presence.
- Whether generated skills gain richer invalidation rules for UI drift, environment version, site route, and selector brittleness.
- Whether `skillnet/` includes metadata and verification records alongside code, making the published libraries comparable to runtime knowledge-base snapshots.
- Whether recovery annotations become durable function patches automatically or remain evidence passed to later update prompts.

## Bottom Line

SkillWeaver is a clear trace-derived memory system for web agents: it turns successful browser trajectories into executable Playwright APIs, then retrieves and pushes selected APIs into future action generation. Its best idea for Commonplace is the promotion discipline around learned symbolic artifacts: a trace-derived candidate should remain low-authority until it is statically checked, practiced, and scoped. Its main risk is provenance. Executable memory can be powerful under bounded tasks, but without source-linked lineage it is hard to know which part of a learned procedure came from durable website structure and which part came from one lucky trajectory.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - source-inspected instance: SkillWeaver distills successful browser trajectories into executable Playwright skills.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: task traces become reusable behavior when extraction, verification, and authority are explicit.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: SkillWeaver activates stored skills through retrieval-time prompt injection.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: traces, skill code, metadata, selectors, prompts, and validators differ by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: generated skills, retrieval prompts, static checks, and controller actions can instruct, route, validate, or execute future behavior.
