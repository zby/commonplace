---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "SkillWeaver's shipped skill-building, browser-agent consumption and evaluation paths at commit f2a63d65d0f6ff46ac30e817cede8797f8f25b97."
run-id: AAS-2026-10-14-skillweaver-c921cc7a5ed0-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: f2a63d65d0f6ff46ac30e817cede8797f8f25b97
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/OSU-NLP-Group/SkillWeaver
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/skillweaver-c921cc7a5ed0/related-systems/OSU-NLP-Group--SkillWeaver
  revision: f2a63d65d0f6ff46ac30e817cede8797f8f25b97
  sha256: null
---

# SkillWeaver boundary

## Boundary and evidence

This run analyses SkillWeaver as a **builder or improvement plane**: it uses model-mediated browser practice to construct and maintain reusable Python skills. The boundary is **whole-system**, not just its knowledge-base API. It includes the shipped exploration driver, native browser-agent loop, retained skill representation and reload paths, experimental Browser-Use integration, browser recovery support, and benchmark orchestration and evaluators. These consumers and drivers are part of the target even though they call library APIs. The intended use is to explain how website practice becomes reusable skills and how subsequent task attempts consume those skills; this boundary does not establish that the resulting skills improve performance.

The classification rests on executable orchestration, not just the project's self-description. The exploration driver invokes task attempts, checks success or records a successful test, updates the knowledge base and persists an iteration checkpoint (SRC-1, `skillweaver/explore.py`). Its successful-attempt branch contains:

> update_diagnostics = await knowledge_base.update(
>     api_synthesis_lm,
>     task,
>     trajectory_string,
>     f"iter_{iteration}",
> )
> --- `skillweaver/explore.py`

The persistence and later-use paths are also shipped. The knowledge base writes code, metadata and semantic text; the loader reads that representation. The native task driver retrieves task-relevant functions, generates actions and executes generated code with the knowledge-base code available (SRC-1, `skillweaver/knowledge_base/knowledge_base.py`, `skillweaver/attempt_task.py`, `skillweaver/agent.py`). Minimum persistence and consumption passages are:

> with open(prefix_path + "_code.py", "w") as f:
>     f.write(self.code)
> --- `skillweaver/knowledge_base/knowledge_base.py`

> module = importlib.__import__(module_name)
> output = await module.act(page)
> --- `skillweaver/agent.py`

This includes the code-admission path in `skillweaver/knowledge_base/code_verification.py`, the update/retrieval prompts loaded by `skillweaver/templates/__init__.py`, and the caller's verification-visibility controls. It includes the experimental consumer that retrieves skills, constructs a Browser-Use controller and supplies it to an external `Agent` (SRC-1, `skillweaver/attempt_task_browser_use.py`, `skillweaver/knowledge_base/knowledge_base.py`). It also includes the benchmark driver that reloads a knowledge base, starts per-task subprocesses and invokes evaluators; the evaluator code is evidence about scoring rules, not evidence of achieved scores (SRC-1, `skillweaver/evaluation/evaluate_benchmark.py`, `skillweaver/evaluation/evaluate_single_task.py`).

### Frozen evidence and time boundary

The sole frozen source is SRC-1, the canonical repository at full commit `f2a63d65d0f6ff46ac30e817cede8797f8f25b97`. Its supplied read-only checkout reports that same HEAD. The analysis cutoff is **2026-10-14**, the supplied run date; it is an applicability cutoff, not an assertion about the commit's publication date. The overall tier is **code-grounded**. Repository documentation and prompts additionally supply declared intent. No target execution, provider call, dependency installation or browser experiment was performed. No separate paper, live project page, external repository or generated execution trace is registered.

### Repository coverage

The tracked top-level tree has five entries. All functional shipped paths remain inside the boundary. Initial inspection traces the production, maintenance, admission, persistence, reload, consumption and scoring interfaces; it does not imply a line-by-line audit of every skill body or evaluator. “Not yet inspected” below means available evidence, not an access gap or an exclusion from the functional boundary.

| Top-level tracked entry | Included or excluded | Material paths and role | Initial inspection and conclusion limits |
|---|---|---|---|
| `README.md` | Included | Installation/configuration doctrine and documented entry points for exploration, task attempts, Browser-Use and evaluations. | Read in full. External hyperlinks and demonstration GIF are not frozen here; their contents cannot support operation or performance conclusions. |
| `LICENSE` | Included | Distribution terms. | Read in full; supplies no operational evidence. |
| `requirements.txt` | Included | Declared Python, browser, model-client, static-checking, Docker and evaluation dependencies. | Read in full. Dependency declarations do not freeze dependency implementation or demonstrate a working installation. |
| `skillnet/` | Included | `cms/cms_kb_post_code.py`, `gitlab/gitlab_kb_post_code.py`, `map/map_kb_post_code.py`, `reddit/reddit_kb_post_code.py`, `shopping/shopping_kb_post_code.py`: shipped site-specific skill libraries. | Sampled the beginning of every library and inventoried function declarations. Remaining skill bodies are available but not yet inspected. These code artifacts and their usage-log docstrings are not independently observed runs; initial inspection cannot establish correctness or coverage of all library functions. |
| `skillweaver/` | Included | Exploration, task drivers, model adapter, knowledge-base operations, prompt templates, browser environment, containerization, evaluation and utilities; material paths are detailed below. | Traced the material loop and both native and experimental consumption routes. Supporting implementation details not yet inspected remain available at SRC-1. No functional shipped responsibility is deliberately excluded. |

The `skillweaver/` row includes these responsibilities:

| Material paths | Role and initial inspection | Limit of initial inspection |
|---|---|---|
| `skillweaver/explore.py` | Read iteration orchestration, shared knowledge-base handling and CLI setup/reload; searched task proposal and test selection entry points. | Task-selection helpers not yet read in full; no scheduling-quality or exploration-effectiveness conclusion established. |
| `skillweaver/attempt_task.py`, `skillweaver/agent.py`, `skillweaver/create_skill_library_prompt.py`, `skillweaver/lm.py` | Read the native action loop, generated-code execution, library-prompt selection and provider-client wrapper; searched generation entry points and CLI reload. | Prompt-generation and provider completion internals are available but not all read; no model-quality or provider-reliability conclusion established. |
| `skillweaver/knowledge_base/knowledge_base.py`, `skillweaver/knowledge_base/code_verification.py`, `skillweaver/knowledge_base/check_success.py`, `skillweaver/knowledge_base/generate_schema.py`, `skillweaver/knowledge_base/type_checking.py` | Read update, save, function visibility, retrieval, controller construction, reload and code checks; inventoried supporting schema, success-check and type-check modules. | Supporting checker details and earlier mutation/metadata methods are not yet fully inspected. Inclusion of an admission path is not a claim that it guarantees safe or correct code. |
| `skillweaver/templates/` | Read `__init__.py`, `kb_procedural_update_base.md` and `kb_procedural_update_single.md`. Included shipped code-generation, accessibility, proposal, practice, relevance, result-verification, debugging, semantic-update and multiple-episode update templates. | Other template bodies are not yet inspected; loading or shipping a template does not establish that every variant is active. `.DS_Store` is nonfunctional metadata, not an instruction or run artifact. |
| `skillweaver/environment/` | Read browser observation interface and locator-recovery setup/function selection; searched Python module interfaces. Included `browser.py`, `state.py`, `a11y.py`, `patches.py`, `playwright_regex_patch.py`, `__init__.py` and `ts/` accessibility helpers/compiler/compiled script. | Recovery continuation and DOM/accessibility helper details are available but not yet fully inspected. No recovery success rate, complete browser-state fidelity or sandbox guarantee established. |
| `skillweaver/attempt_task_browser_use.py` | Read retrieved-function controller handoff and external-agent invocation; traced controller implementation in the knowledge base. | External Browser-Use implementation is not registered; conclusions stop at SkillWeaver's adapter/handoff. No compatibility or successful end-to-end run established. |
| `skillweaver/containerization/containers.py`, `skillweaver/containerization/containers.json`, `skillweaver/containerization/serve.py` | Inventoried container interfaces and read the Flask obtain/release/status server used by shipped drivers. | Container specifications and orchestration internals are available but not yet fully inspected. External Docker images and hosted sites are not frozen; no reproducible environment state established. |
| `skillweaver/evaluation/` | Read benchmark subprocess/reload interfaces, single-task reload/visibility and scoring invocation/output, `load_test_cases.py` and `run_experiment.py`. Included `webarena_evaluators.py`, `webarena_evaluators_with_debug_info.py`, `vwa_evaluators.py`, their helpers, image utilities, login/configuration/access-token support and `test_cases/` raw benchmark JSON. | Evaluator bodies and raw task sets are not yet fully inspected; they remain available for later analysis. Ignored/generated split cases and actual result directories are not supplied run evidence. The experiment wrapper refers to `webrover/experiments/`, absent from the tracked tree; that prevents reconstructing its experiment configurations from this pin alone. |
| `skillweaver/sanity_check_code.py`, `skillweaver/util/` | Included source checking, JSON-schema helpers, async/value helpers, performance monitoring, demo evaluation caller and video/montage processing. Inventoried utility entry points and read `run_for_demo_video.py`. | Remaining utility details are not yet fully inspected. Demo helper references to collected libraries do not supply the referenced files or a demonstration trace. |

### External dependencies and excluded evidence

Model services (OpenAI/Azure client configuration in SRC-1, `skillweaver/lm.py`), Playwright/browser implementations, Browser-Use's enclosing agent, Docker images and website backends are external dependencies, not target-owned mechanisms. Their implementations and live states are outside the registered evidence. This prevents attributing provider behavior, Browser-Use planning, browser-engine guarantees or website-side persistence to SkillWeaver. SkillWeaver's adapters, configuration and orchestration for them remain included (SRC-1, `requirements.txt`, `skillweaver/containerization/serve.py`, `skillweaver/attempt_task_browser_use.py`).

No separate execution artifact or intervention/comparison result was supplied. This prevents claims of observed end-to-end operation, achieved benchmark performance or causal benefit from the library. Shipped skill docstrings report usage; they do not overcome that limit. Available but uninspected source files are not access gaps, and later workers may inspect them at this same pin under SRC-1 without adding another source.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/OSU-NLP-Group/SkillWeaver` | f2a63d65d0f6ff46ac30e817cede8797f8f25b97 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/skillweaver-c921cc7a5ed0/related-systems/OSU-NLP-Group--SkillWeaver`. Implementation: tracked-tree inventory; exploration iteration and CLI; native attempt/action execution; knowledge-base update/check/save/retrieve/reload/controller paths; experimental agent handoff; evaluation driver/load/scoring interfaces; browser observation/recovery setup; container server; sampled all five `skillnet/` libraries. Doctrine/design: full `README.md`, `requirements.txt`, `LICENSE`, template loader and procedural-update base/single templates. Reported operation: usage-log docstrings in the sampled shipped libraries, without independent traces. Detailed initial coverage and uninspected material are listed above. | Implementation: [exploration](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/explore.py), [knowledge base](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/knowledge_base/knowledge_base.py), [native execution](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/agent.py), [evaluation](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/evaluation/evaluate_single_task.py), [external-agent adapter](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/attempt_task_browser_use.py). Doctrine/design: [README](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/README.md), [update instructions](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillweaver/templates/kb_procedural_update_base.md). Reported operation: [sample skill usage logs](https://github.com/OSU-NLP-Group/SkillWeaver/blob/f2a63d65d0f6ff46ac30e817cede8797f8f25b97/skillnet/map/map_kb_post_code.py). | No access gap in the registered Git tree. No independent observed run or causal experiment registered. External services, dependency implementations, website/container states and absent experiment configurations are not frozen; they prevent end-to-end reproducibility and effectiveness conclusions. Uninspected files listed above are available evidence, not missing evidence. |
