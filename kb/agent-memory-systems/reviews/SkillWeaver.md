---
description: "SkillWeaver review: web-agent exploration loop that distills successful Playwright trajectories into reusable Python API skills and shipped SkillNet files"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-27"
---

# SkillWeaver

SkillWeaver is an OSU NLP Group web-agent system for learning website-specific Playwright skills. The inspected code implements an exploration loop that proposes website tasks, runs a browser agent, judges success from the resulting trajectory, and distills successful attempts into async Python functions. Its memory system is therefore a generated API library for web automation, not a general note store or vector memory.

**Repository:** https://github.com/OSU-NLP-Group/SkillWeaver

**Reviewed commit:** f2a63d65d0f6ff46ac30e817cede8797f8f25b97

**Commit URL:** https://github.com/OSU-NLP-Group/SkillWeaver/commit/f2a63d65d0f6ff46ac30e817cede8797f8f25b97

## Core Ideas

**The memory atom is an async Playwright API.** `KnowledgeBase` stores a single Python source string plus metadata and optional semantic text. It parses top-level async functions with `ast`, exposes signatures/docstrings as skill descriptions, and persists a library as `{prefix}_code.py`, `{prefix}_metadata.json`, and `{prefix}_semantic_knowledge.txt`. Metadata tracks function `version`, `test_count`, `references`, and event history, but the behavior-changing artifact is still executable code ([knowledge_base.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/knowledge_base.py)).

**Exploration alternates between discovering skills and practicing unverified ones.** Each iteration chooses either an exploratory task proposed from the current accessibility tree or a test task for an untested function. The test scheduler can be probability-based or alternating; untested functions are weighted by a simple practice-utility score of interaction count minus version count. Iterations write task metadata, state/action logs, a pretty trajectory, success checks, update diagnostics, performance data, and a browser trace before saving `kb_post` artifacts ([explore.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/explore.py), [generate_practice_args.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/generate_practice_args.md), [propose_skill.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/propose_skill.md)).

**Skill synthesis is gated by success, then statically checked.** For non-test tasks, an LLM sees the action trajectory, intended task, current verified procedural knowledge, and semantic knowledge; it returns new or updated function definitions. `check_code(...)` rejects syntax errors, synchronous functions, missing `page` first parameters, missing docstrings, reserved `act`, missing `page.goto`, broad `try`, `while` loops, locator-style selectors, and type errors from `pyright`. Accepted functions are merged by name into the AST-backed library, resetting `test_count` on modified skills ([kb_procedural_update_base.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/kb_procedural_update_base.md), [kb_procedural_update_single.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/kb_procedural_update_single.md), [code_verification.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/code_verification.py), [type_checking.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/type_checking.py)).

**Retrieval is LLM selection over function descriptions, not a persistent index.** The production path asks an LLM to inspect all parsed functions and return relevant function names for a task. There is an embedding-similarity helper in `KnowledgeBase`, but the active `retrieve(...)` method uses `predict_relevant_functions_templ(...)` and returns pretty-formatted functions for prompt injection. Exploration can disable retrieval for explore/test tasks, while production always calls retrieval ([knowledge_base.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/knowledge_base.py), [create_skill_library_prompt.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/create_skill_library_prompt.py), [predict_relevant_functions.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/predict_relevant_functions.md)).

**The agent consumes skills as executable globals or as Browser-Use actions.** The native agent injects retrieved function source into the generated action module and prompts the LLM to call existing functions whenever useful. The Browser-Use adapter loads the same knowledge base, retrieves relevant functions, wraps selected functions as `Controller` actions, and rewrites the first `page` parameter to Browser-Use's `browser` surface ([agent.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/agent.py), [attempt_task.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/attempt_task.py), [attempt_task_browser_use.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/attempt_task_browser_use.py), [codegen.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/codegen.md)).

**SkillNet is a shipped code library, but with thin lifecycle data.** The `skillnet/` directory contains large generated `*_kb_post_code.py` files for CMS, GitLab, map, Reddit, and shopping domains. These files demonstrate the learned artifact format: many async Playwright functions with docstrings and usage logs. At this commit, the shipped SkillNet files are code-only; accompanying metadata and semantic-knowledge files are not present in the directory, so trust state such as references and test counts is not shipped with the code artifacts ([skillnet](https://github.com/OSU-NLP-Group/SkillWeaver/tree/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillnet), [reddit_kb_post_code.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillnet/reddit/reddit_kb_post_code.py)).

**Evaluation is WebArena-centered and artifact-aware.** `evaluate_benchmark(...)` loads WebArena or VisualWebArena test cases, copies a selected knowledge base into the run directory, fans out subprocess evaluations, and reports success/failure/error counts, cost, and step length. `evaluate_single_task(...)` hides unverified functions unless `--enable_unverified` is set, runs either the SkillWeaver agent or a computer-use-preview path, then calls WebArena/VWA evaluators and writes `eval.json`, traces, actions, and performance logs ([evaluate_benchmark.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/evaluation/evaluate_benchmark.py), [evaluate_single_task.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/evaluation/evaluate_single_task.py)).

## Comparison with Our System

| Dimension | SkillWeaver | Commonplace |
|---|---|---|
| Primary substrate | Async Python functions for website actions | Markdown notes, sources, reviews, ADRs, instructions, generated indexes |
| Source signal | Browser states, generated code actions, execution outputs, screenshots, success checks, traces | Authored artifacts, source snapshots, code-grounded reviews, validation and review findings |
| Memory atom | Website-specific Playwright API with docstring and optional test metadata | Typed knowledge artifact with frontmatter, links, validation, and status |
| Retrieval | LLM selection over parsed function descriptions | `rg`, indexes, titles/descriptions, authored links, reports |
| Verification | LLM success check, direct function test count, static code/type checks, benchmark evaluator | Structural validation, semantic review, source grounding, human/agent judgment |
| Behavior-changing artifact | More callable actions in future web tasks | Better context plus stronger KB artifacts such as notes, instructions, reviews, and scripts |
| Lifecycle | Function replacement by name, version/test counters, saved per-iteration artifacts | Status, archival, replacement, generated indexes, review gates, explicit link contracts |

SkillWeaver is stronger when the desired memory is a new action primitive. A learned function can immediately change the agent's action space: future prompts receive the function, can call it directly, and can use the Browser-Use controller variant as an external tool surface.

Commonplace is stronger on provenance, navigability, and authority. SkillWeaver saves rich raw iteration artifacts in exploration logs, but the durable SkillNet artifact is mostly Python source. Once detached from the iteration directory, a function's exact source trajectory, success oracle, repair history, and evaluator evidence are not first-class review surfaces.

The systems also differ on retrieval philosophy. SkillWeaver makes activation model-mediated: the LLM reads a candidate function list and selects names. Commonplace makes activation more inspectable but less automatic through lexical search, indexes, and links. SkillWeaver is a useful counterexample: automatic activation is possible without vectors, but the selection policy then becomes another prompt-governed component to evaluate.

## Borrowable Ideas

**Treat executable skills as a first-class memory substrate.** Ready to borrow for narrow operational domains. Commonplace should keep most methodology in prose, but generated helper scripts could use a SkillWeaver-like pairing of function source, docstring, schema, references, and test state.

**Separate exploration from practice.** Ready as a workflow shape. SkillWeaver distinguishes "discover something useful to learn" from "test an unverified skill"; Commonplace could use the same distinction for candidate instructions or scripts that need deliberate rehearsal before promotion.

**Require a homepage-resetting precondition in procedural artifacts.** Worth borrowing for browser or CLI task helpers. SkillWeaver's insistence that learned functions start with `page.goto(...)` is crude, but it makes the skill callable from a known state instead of depending on the previous episode's hidden context.

**Use static checks before accepting generated procedures.** Ready to borrow in spirit. The exact Playwright rules are domain-specific, but the pipeline shape is right: generated procedures should pass syntax, schema, style, and type checks before they become reusable memory.

**Keep direct execution evidence separate from LLM success judgment.** Needs a stronger authority model. SkillWeaver has both: direct exception-free test execution increments a function counter, while broader task success is judged from trajectory plus screenshot. Commonplace could preserve the distinction between "artifact ran" and "artifact accomplished the intended work."

**Do not borrow code-only SkillNet as sufficient lifecycle.** The shipped SkillNet files are useful examples of learned actions, but code without source trajectory IDs, review state, deprecation policy, and evaluator links is too thin for long-lived KB trust.

## Trace-derived learning placement

**Trace source.** SkillWeaver qualifies as trace-derived learning. The raw signal is a browser-task trajectory: initial and intermediate accessibility-tree states, screenshots, generated `act(page)` code, stdout/output/exception records, optional locator recovery records, final screenshot, Playwright trace zip, and task metadata. Exploration tasks are proposed from the current page state; test tasks are generated for existing unverified functions.

**Extraction.** The extraction oracle is staged. For successful test tasks that call the target function without exception or recovery attempts, SkillWeaver increments the function's test count. Otherwise, `check_success_simple(...)` asks an LLM to judge the trajectory and final screenshot. If successful, `KnowledgeBase.update(...)` prompts an LLM to synthesize or revise Python functions from the trajectory, then accepts only code that passes static and type checks.

**Storage substrate, form, and lineage.** The distilled retained state is symbolic: async Python functions with docstrings, inferred JSON schemas, saved source files, optional metadata JSON, and optional semantic text. Its lineage is browser trajectory -> LLM synthesis or revision -> static/type checks -> saved knowledge-base prefix. The system does not update model weights and does not primarily store prose lessons.

**Behavioral authority.** The retained function is a system-definition artifact. It changes future agent behavior because it becomes available as a callable shortcut in native codegen prompts or as a Browser-Use controller action.

**Scope.** Scope is website-specific and task-family-specific. The repo's shipped SkillNet covers WebArena-like domains such as CMS, GitLab, map, Reddit, and shopping, while each exploration run writes its own prefix-based KB artifacts.

**Timing.** Learning is online during exploration iterations and staged across saved iteration directories. Evaluation is a later consumption phase: a selected knowledge-base prefix is loaded, optionally filtered to verified functions, and used during benchmark tasks.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), SkillWeaver belongs in the trajectory-to-executable-skill-library branch. It strengthens the survey claim that external symbolic artifacts can be more behavior-changing than retrieved prose, and it splits executable-skill systems by domain: OS-Copilot promotes general OS/software tools, while SkillWeaver promotes website-specific browser APIs.

## Curiosity Pass

The strongest implementation is not "self-improvement" in the broad sense; it is a narrow loop that turns browser success traces into Playwright helper functions. The model, prompts, evaluator, and retrieval policy do not themselves get rewritten.

The semantic-memory surface is present but underused. `KnowledgeBase` can save and load semantic knowledge, and exploration/proposal prompts include it, but `KnowledgeBase.update(...)` leaves `semantic_update_diagnostics` as `None`. The implemented learning target at this commit is procedural code, not a maintained semantic website model.

The repository has two levels of evidence with different durability. Exploration logs can contain trajectories, screenshots, traces, success checks, and update diagnostics; the shipped `skillnet/` directory contains only generated code files. That makes SkillWeaver more auditable immediately after an exploration run than after skills are exported as a standalone library.

The README command for benchmark evaluation names `python -m skillweaver.evaluate_benchmark`, while the inspected runnable module is under `skillweaver/evaluation/evaluate_benchmark.py`. That is a small packaging/documentation mismatch, but it matters for reproducibility because there is no package manifest beyond `requirements.txt`.

## What to Watch

- Whether SkillNet starts shipping metadata and semantic-knowledge files alongside code, so references, test counts, and event histories survive export.
- Whether the semantic update path becomes implemented instead of a saved empty side channel.
- Whether retrieval gains an inspectable ranking/evaluation layer beyond LLM name selection over all functions.
- Whether locator recovery results become promotion evidence for patching existing skills, not only execution-time recovery records.
- Whether generated functions get replay tests or benchmark-linked provenance before being treated as verified APIs.
- Whether Browser-Use integration becomes the main consumption surface, since it turns learned functions into ordinary controller actions.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: SkillWeaver is a browser-trajectory-to-executable-API case.
- [OS-Copilot](./OS-Copilot.md) - compares-with: both promote successful traces into callable code, but SkillWeaver specializes in website APIs and WebArena-style evaluation.
- [SkillX](./SkillX.md) - compares-with: both build skill libraries from trajectories, but SkillX stores prompt-facing plans/skills while SkillWeaver stores executable Playwright functions.
- [Voyager](./voyager.md) - compares-with: both grow an executable skill library, but SkillWeaver's skills are web automation APIs rather than Minecraft programs.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - qualifies: SkillWeaver is deploy-time symbolic learning when exploration is run against a live website.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: SkillWeaver separates raw traces, generated code artifacts, metadata, and retrieval prompts into distinct artifact roles.
