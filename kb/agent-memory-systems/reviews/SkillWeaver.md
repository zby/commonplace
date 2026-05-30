---
description: "SkillWeaver review: website-specific browser trajectories distilled into Playwright API skills, metadata counters, retrieval prompts, and executable tool authority"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# SkillWeaver

SkillWeaver is an OSU NLP Group framework for web agents that learn website-specific skills by exploring with Playwright, checking whether attempts succeeded, and distilling successful browser trajectories into reusable async Python APIs. The memory system is a generated skill library, not a general note store: raw browser traces remain as logs, while the behavior-changing retained artifacts are function definitions, docstrings, metadata counters, retrieval prompts, and optional Browser-Use controller actions.

**Repository:** https://github.com/OSU-NLP-Group/SkillWeaver

**Reviewed commit:** f2a63d65d0f6ff46ac30e817cede8797f8f25b97

**Commit URL:** https://github.com/OSU-NLP-Group/SkillWeaver/commit/f2a63d65d0f6ff46ac30e817cede8797f8f25b97

## Core Ideas

**The retained skill is executable Playwright code.** `KnowledgeBase` stores a single Python source string plus metadata and semantic text. Its operative part is symbolic: parsed async functions whose first argument is `page`, whose docstrings become tool descriptions, and whose parameters are converted to JSON schemas. The library is saved as three files with a shared prefix: `_code.py`, `_metadata.json`, and `_semantic_knowledge.txt` ([skillweaver/knowledge_base/knowledge_base.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/knowledge_base.py), [skillweaver/knowledge_base/generate_schema.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/generate_schema.py)).

**Exploration produces trace evidence before it produces memory.** Each exploration iteration chooses either a new explore task or a test task for an unverified function, runs `attempt_task`, writes task/state/action files, `trajectory_pretty.txt`, success checks, performance data, and Playwright `trace.zip`, then saves the post-iteration knowledge base. Those raw files are trace-derived knowledge artifacts: they preserve evidence, but they are not the surface future agents normally call ([skillweaver/explore.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/explore.py), [skillweaver/attempt_task.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/attempt_task.py)).

**Successful trajectories are distilled into API updates.** The exploration loop only calls `KnowledgeBase.update(...)` after an LLM success check says an explore attempt succeeded; test attempts instead increment the target function's test count when the function executes without an exception or recovery. The update prompt asks the model to generalize from the action history into new or revised Playwright functions, including usage logs and observed behavior ([skillweaver/explore.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/explore.py), [skillweaver/knowledge_base/check_success.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/check_success.py), [skillweaver/templates/kb_procedural_update_base.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/kb_procedural_update_base.md), [skillweaver/templates/kb_procedural_update_single.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/kb_procedural_update_single.md)).

**Metadata is a lightweight lineage and verification surface.** When a function is added or updated, SkillWeaver records version, `test_count`, references such as `iter_42`, and event records. Updates reset the function's `test_count`; exception-free tests increment it. This lineage is useful, but shallow: it points to iteration labels rather than embedding full source trace paths, success-check reasoning, or replay results inside each function record ([skillweaver/knowledge_base/knowledge_base.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/knowledge_base.py)).

**Activation happens through prompt-time retrieval and execution.** For production tasks, `create_skill_library_prompt(...)` asks the knowledge base to retrieve relevant functions. Retrieval is LLM-based over formatted function signatures and docstrings; the selected function text is injected into the agent prompt, and the code executor makes the functions available as globals. The codegen prompt says the agent must call an existing knowledge-base function when it corresponds to an action, so selected functions have system-definition-artifact authority over future action generation ([skillweaver/create_skill_library_prompt.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/create_skill_library_prompt.py), [skillweaver/knowledge_base/knowledge_base.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/knowledge_base.py), [skillweaver/templates/predict_relevant_functions.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/predict_relevant_functions.md), [skillweaver/templates/codegen.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/codegen.md), [skillweaver/agent.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/agent.py)).

**The code validates shape more than task success.** Generated API updates pass syntax, async-function, docstring, `page.goto`, selector, argument-type, and pyright-style checks before merging. Runtime success is tracked separately by test counters and benchmark evaluators. The shipped `skillnet/` libraries show the intended output format as large website-specific `_kb_post_code.py` files, but those checked-in examples do not carry the saved metadata or semantic sidecars ([skillweaver/knowledge_base/code_verification.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/code_verification.py), [skillnet](https://github.com/OSU-NLP-Group/SkillWeaver/tree/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillnet), [skillweaver/evaluation/evaluate_single_task.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/evaluation/evaluate_single_task.py)).

**Semantic knowledge is present but underimplemented.** The storage object has `semantic_knowledge`, the exploration prompt uses it when proposing new skills, and `save(...)` writes it to `_semantic_knowledge.txt`. However, at this commit `KnowledgeBase.update(...)` sets `semantic_update_diagnostics = None` and does not mutate `self.semantic_knowledge`; the semantic update template exists but is not wired into the inspected update path ([skillweaver/knowledge_base/knowledge_base.py](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/knowledge_base.py), [skillweaver/templates/kb_semantic_update.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/kb_semantic_update.md), [skillweaver/templates/propose_skill.md](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/propose_skill.md)).

## Comparison with Our System

| Dimension | SkillWeaver | Commonplace |
|---|---|---|
| Primary substrate | Python skill files, metadata JSON, optional semantic text, browser traces | Markdown notes, sources, reviews, ADRs, instructions, generated indexes |
| Retained artifact | Website-specific async Playwright APIs plus docstrings and test counters | Typed knowledge artifacts and stronger system-definition artifacts |
| Source signal | Browser trajectories, screenshots, accessibility trees, action code, success checks | Source snapshots, authored notes, reviews, validation, semantic gates |
| Representational form | Symbolic executable code with prose docstrings; prompt text for retrieval; JSON metadata | Mostly prose and structured frontmatter, with scripts/schemas/commands where codified |
| Lineage | Iteration references, events, trace folders, action logs | Explicit source links, archive records, validation reports, indexes |
| Activation | LLM selects relevant functions; prompt requires using matching APIs; code executor imports them | `rg`, indexes, links, review reports, and explicit instruction/validation surfaces |
| Verification | Static code checks, LLM success checks, exception-free test counters, benchmark evaluation | Structural validation, source-grounded review, semantic QA, link discipline |

SkillWeaver is closer to executable skill learning than to commonplace's library layer. Its most important artifact is not a note about how to use a site; it is an imported function that can click, fill, navigate, and return values on behalf of a future agent. The storage substrate is therefore more brittle but also more directly behavior-changing.

Commonplace is stronger on inspectability and lifecycle. SkillWeaver keeps enough metadata to know whether a function has been updated or tested, but it does not make the generated API a reviewed artifact with explicit status, retirement rules, trace links, or source-grounding comments. The raw traces are available in iteration directories, yet the executable skill does not carry a rich lineage contract.

The authority split is useful. Raw trajectories and success checks are knowledge artifacts: evidence for why a skill should exist. Generated functions are system-definition artifacts: once retrieved, they become callable actions in the agent's execution environment. Retrieval prompts sit between the two as a ranking and activation layer.

**Read-back:** push — relevant generated functions are selected and injected into the agent prompt before action generation.

## Borrowable Ideas

**Executable skills as a promotion target.** SkillWeaver gives a concrete pattern for promoting repeated trace lessons beyond prose: when a behavior is stable and valuable enough, it can become a callable API with parameters, validation, and retrieval metadata.

**Separate raw traces from distilled authority.** The system is clearest when browser trajectories, screenshots, action logs, generated code, metadata counters, and semantic text are treated as different artifacts with different review contracts.

**Use lightweight counters as a visibility gate.** `test_count` is too weak to prove correctness, but it is useful as an operational signal for hiding newly generated functions until they have at least survived execution.

**Keep retrieval inspectable for small libraries.** SkillWeaver's LLM-based selection over signatures and docstrings is a viable activation layer when the library is small enough to format and inspect. It avoids hiding tool selection entirely inside embeddings.

**Treat semantic and procedural memory as separate channels.** The code's unfinished semantic channel is still a useful warning: prose observations, executable procedures, and retrieval metadata need separate lifecycles rather than one undifferentiated "memory" label.

## Takeaways

**Executable skills are a stronger promotion target than prose reminders.** SkillWeaver shows what happens when a trace-derived lesson is promoted all the way into a callable API. For commonplace, the equivalent promotion path would move from notes to instructions, scripts, validators, or task-specific tools only when the repeated behavior justifies the extra authority.

**Keep the raw/distilled split explicit.** Browser traces, screenshots, action JSON, generated code, metadata counters, and semantic text have different review methods. SkillWeaver is easiest to understand when these are not collapsed into one word, "memory."

**Use test counters as weak confidence, not proof.** `test_count` is a practical gate for hiding unverified APIs, but it does not by itself establish that a function remains correct across site changes or task variants. It needs lineage, replay, and invalidation to become durable trust.

**Retrieval can choose tools without embeddings.** SkillWeaver has an embedding helper, but the implemented `retrieve(...)` path asks an LLM to select relevant functions from formatted signatures and docstrings. That is a legitimate activation design for small skill libraries, and it keeps the selected rationale inspectable.

**Semantic and procedural memory should not share a lifecycle by accident.** The code already has a semantic-knowledge field and template, but the procedural update path is the real implemented mechanism. Commonplace should preserve this distinction when borrowing the design: prose observations, executable procedures, and retrieval metadata deserve separate contracts.

## Trace-derived learning placement

**Trace source.** SkillWeaver qualifies as trace-derived learning. Its raw signal is a browser-use trajectory: task choice, accessibility-tree observations, screenshots, generated `act(page)` code, stdout/results/exceptions, recovery annotations, final states, Playwright traces, and LLM success checks.

**Extraction.** Exploration alternates between proposing new tasks and testing unverified functions. Successful explore attempts trigger an LLM procedural update over the action history and current library; successful test attempts increment function counters. The extraction oracle is therefore mixed: LLM task proposal, LLM success checking, static code verification, and exception-free execution for tests.

**Storage substrate.** Raw traces live in per-iteration log directories with JSON state/action files, pretty trajectories, trace ZIPs, diagnostics, and performance files. Distilled memory lives in `kb_post_code.py`, `kb_post_metadata.json`, and `kb_post_semantic_knowledge.txt` files or equivalent loaded prefixes. Shipped examples under `skillnet/` preserve code libraries only.

**Representational form.** The distilled operative part is symbolic Python code plus prose docstrings. Metadata is symbolic JSON. Retrieval prompts and success/update prompts are prose system-definition surfaces. No model weights or adapters are updated.

**Lineage.** Function metadata records update/test references and events, usually by iteration label. The fuller lineage remains external in the iteration folder, so the generated function is not self-sufficient for audit or regeneration. Updating a function resets its test count, which is a simple invalidation rule.

**Behavioral authority.** Raw trajectories are knowledge artifacts when used as evidence for synthesis or debugging. Generated functions become system-definition artifacts when retrieved into a prompt and executed as globals, or when wrapped as Browser-Use controller actions. Metadata has gating authority when `hide_unverified` excludes functions with zero tests.

**Scope.** Scope is website-local and benchmark-environment-local. The code supports WebArena-style sites and VisualWebArena test sets, and the generated functions are intended as lightweight APIs for a specific site rather than cross-domain conceptual knowledge.

**Timing.** Learning is staged: exploration produces and tests skills over many iterations, then evaluation or production task attempts load a saved prefix. The production path can execute and log tasks, but it does not update the knowledge base during `attempt_task(...)` itself.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), SkillWeaver belongs in the trajectory-to-executable-artifact branch. It strengthens the survey distinction between source traces and distilled behavior-shaping artifacts: the durable improvement is the generated API surface, not the browser log.

## Open Questions

**How durable are skills under website drift?** The code can recover from locator failures during execution and can annotate recoveries, but there is no full lifecycle for expiring, replaying, or deprecating stale APIs after site changes.

**Should semantic knowledge be promoted or removed?** The field and template imply a prose website knowledge base, but the update path leaves it unchanged. It is unclear whether this is a planned second channel or a design remnant.

**How much provenance is enough for executable authority?** Iteration references are useful but thin. A stronger version would link each function version to source trajectories, success checks, generated prompt diagnostics, static-check attempts, and benchmark outcomes.

**Can generated APIs be safely composed?** The skill format encourages shortcut functions, but composition risks hidden state assumptions: current URL, login state, language settings, and side effects. The required `page.goto` helps, but richer precondition contracts would make composition safer.

**When should unverified APIs be visible?** The CLI and evaluation paths expose switches for hiding or allowing unverified functions. That policy is central to behavioral authority, and it deserves explicit evaluation because unverified executable code can change future actions more strongly than a prose hint.

## Curiosity Pass

The semantic-knowledge path is the main thing to inspect in future commits. At this commit, `semantic_knowledge` is stored and surfaced in prompts, but the update path does not actually mutate it, which makes the prose-memory channel look more like a planned feature than an implemented memory mechanism.

The checked-in `skillnet/` outputs are also worth revisiting. They show large generated code libraries, but not the metadata and semantic sidecars that the runtime save path can produce, so they are weaker evidence for lineage than the framework design suggests.

Finally, SkillWeaver raises a useful boundary question for commonplace: when a KB insight becomes executable enough to act directly in the environment, it should probably move from ordinary note governance into instruction, script, validator, or skill governance.

## What to Watch

Watch whether future versions wire semantic updates into `KnowledgeBase.update(...)`, add richer provenance from function versions back to source trajectories, and introduce replay or drift checks for website changes.

Also watch the authority policy around unverified skills. If generated APIs can be retrieved before replay or review, the system has a much higher behavioral-risk profile than a prose memory system with the same source traces.

## Bottom Line

SkillWeaver is a strong trace-derived executable-memory case: it converts successful website trajectories into callable Playwright APIs with retrieval and verification scaffolding. Its main weakness is artifact governance. The code can create and activate powerful system-definition artifacts, but provenance, lifecycle, semantic-memory maintenance, and replay-based trust are thinner than the authority those artifacts receive.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: SkillWeaver is a trajectory-to-executable-API case with separate raw trace, generated code, metadata, and retrieval surfaces.
- [Agent-S](./Agent-S.md) - compares-with: both operate web/GUI trajectories, but Agent-S mainly stores prose summaries or benchmark evidence while SkillWeaver promotes callable browser APIs.
- [SkillX](./SkillX.md) - compares-with: both distill trajectories into skill libraries, but SkillX stores plan/functional/atomic prompt artifacts while SkillWeaver stores executable Playwright functions.
- [OS-Copilot](./OS-Copilot.md) - compares-with: both promote interaction experience into tools, but SkillWeaver's tools are website-local browser APIs with test counters.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - qualifies: SkillWeaver has staged exploration-time learning and strong deploy-time activation, but production task attempts do not update the library inline.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: SkillWeaver requires separating storage substrate, representational form, lineage, and behavioral authority across traces, code, metadata, prompts, and controller actions.
