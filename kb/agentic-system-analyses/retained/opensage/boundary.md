---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "OpenSage's shipped runtime, memory, drivers and evaluation integrations at commit 54d64702e18d195c8f0fed711c6db5dc1d62ab29."
run-id: AAS-2026-10-14-opensage-291d1ed79d37-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "54d64702e18d195c8f0fed711c6db5dc1d62ab29"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/opensage-agent/OpenSage
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/opensage-291d1ed79d37/related-systems/opensage-agent--OpenSage
  revision: "54d64702e18d195c8f0fed711c6db5dc1d62ab29"
  sha256: null
---

# OpenSage boundary

## Boundary and evidence

This run analyses OpenSage as an **enclosing runtime**, not only its agent class or memory API. Its intended use is to characterize the shipped model-driven execution, coordination and retained-state mechanisms, including the drivers that create and later consume that state. The boundary is **whole-system** for the repository's own implementation, prompts, configurations, agent library, evaluation drivers and training integration surfaces. It does not include implementation bodies of external dependencies.

The evidence is frozen at `54d64702e18d195c8f0fed711c6db5dc1d62ab29`, with an applicability cutoff of **2026-10-14**. The acquired checkout's HEAD equals that pin. The canonical identity remains `https://github.com/opensage-agent/OpenSage`; references to the older `opensage-adk` name in source documentation do not establish another source. The evidence tier is **code-grounded**: source inspection establishes implemented paths and declared policy, not successful execution, model compliance or measured benefit.

### Entry points and state loop

The installed `opensage` command resolves to `opensage.cli.opensage_cli:main` (SRC-1, `pyproject.toml`). The CLI loads an agent factory, registers its tree, spawns a root instance, starts the manager and sends user input. It restores saved session state on resume and saves a session snapshot on shutdown when cleanup is disabled (SRC-1, `src/opensage/cli/opensage_cli.py`). These shipped caller responsibilities belong to OpenSage rather than an excluded application.

OpenSage depends on Google ADK for the underlying model-agent execution machinery, but supplies session services, resource managers, orchestration and patches around it. The session constructs an agent manager; the manager constructs per-instance ADK runners with OpenSage services and plugins (SRC-1, `src/opensage/session/opensage_session.py`, `src/opensage/orchestration/manager.py`). This makes the target an enclosing runtime assembled around a dependency, not merely a returning computation or runtime client.

> return Runner(
>     app_name=self._app_name,
>     agent=agent,
>     session_service=self._opensage_session.session_service,
>     artifact_service=self._opensage_session.artifact_service,
>     memory_service=self._opensage_session.memory_service,
>     credential_service=self._opensage_session.credential_service,
>     plugins=plugins,
> )
> --- `src/opensage/orchestration/manager.py`

The memory boundary includes creation of sandbox memory directories, runtime path injection, trajectory persistence, agent-written knowledge files and their index, compaction and pinned content, host-side instance state and resume. The import path applies patches; the run wrapper injects runtime memory information and configurable policy, initializes layouts and persists trajectories (SRC-1, `src/opensage/__init__.py`, `src/opensage/patches/agent_run_async.py`). Knowledge-store initialization and runtime path disclosure are separate from the prompt's agent-maintenance policy (SRC-1, `src/opensage/memory/file_based/long_term/knowledge_store.py`, `src/opensage/memory/file_based/short_term/prompt.py`, `src/opensage/templates/auto_insert_prompts/default.md`). Policy is evidence of intended maintenance, not proof that agents performed it.

> 1. Skim `index.md`. Did you learn anything that future-you (or another agent)
>    would want and can't find here?
> 2. If yes, write a new `.md` and append a line to `index.md`. Be concise —
>    one short markdown file beats a long one.
> 3. If you found an existing entry to be wrong or stale, update or remove it
>    (and its index line) instead of leaving the contradiction.
> --- `src/opensage/templates/auto_insert_prompts/default.md`

State consumers include the CLI's resume/review paths, web routes that read sessions and disk instance trees, and evaluation drivers that retain event traces. The ordinary web `/run` route submits input through the manager. Evaluation registers and spawns agents through that manager and subsequently collects their session events (SRC-1, `src/opensage/cli/opensage_web_app.py`, `src/opensage/evaluation/base.py`). These are included producers and consumers, not external hosts.

> await opensage_session.agent_manager.spawn(
>     agent_name=agent.name,
>     session_id=task.session_id,
>     parent_session_id=None,
> )
> --- `src/opensage/evaluation/base.py`

Not every shipped driver uses the same enclosing loop. The local-support CLI creates an ADK runner directly, saves a trace and may issue repeated continuation calls; the vulnerability-memory benchmark also contains direct ADK runner paths. They remain included, rather than being attributed automatically to the manager loop (SRC-1, `agent_library/local_support/local_cli.py`, `benchmarks/secodeplt/vul_detection_memory.py`). The RL client resolves shipped agents and benchmark interfaces; training launchers may delegate to an external trainer (SRC-1, `src/opensage/evaluation/rl_adapters/client.py`, `rl/areal/train.sh`). Later mechanism findings must distinguish these paths.

### Tracked top-level coverage

“Included” defines functional coverage, not a claim that every blob has already been read. The tree was inventoried at the frozen commit. Initial inspection traced the principal executable and retained-state loop above, plus alternate callers. Detail not yet inspected is explicitly identified below and remains available under SRC-1; it is not an access gap.

| Top-level tracked path | Classification and role | Initial inspection or limit; conclusion prevented by exclusion |
|---|---|---|
| `.github/` | Excluded repository governance and CI machinery, including workflows for unit/integration tests, docs and code review. | Tree inventoried; workflow bodies not inspected. No conclusions about actual CI results, contributor governance or automated review efficacy. |
| `.gitignore` | Excluded repository housekeeping. | Inventoried only; no conclusions about working-tree retention guarantees. |
| `.gitmodules` | Included dependency-boundary declaration. | Read; names the SWE-bench Pro gitlink. Does not supply that repository's implementation. |
| `.pre-commit-config.yaml` | Excluded development lint-hook configuration. | Inventoried only; no claim about enforced development quality. |
| `.python-version` | Included interpreter configuration. | Inventoried; compatibility details not yet inspected. |
| `LICENSE` | Excluded licensing terms. | No licensing assessment. |
| `README.md` | Included declared usage, setup and examples. | Headings and entry-point references inspected; reported benefits not verified. |
| `README_zh.md` | Included alternate-language documentation. | Inventoried, not yet inspected; no translation-equivalence claim. |
| `SKILL.md` | Included shipped framework-use instructions. | Architecture, CLI, memory, agent and evaluation sections located by bounded search; detailed recipes not yet inspected. Its instructions are target evidence, not worker authority. |
| `agent_library/` | Included agent factories, task prompts/configs, feature demonstrations and local-support drivers. Material paths include `agents/`, `agents_101/`, `agents_with_features/`, `local_support/local_cli.py`, `local_support/server/` and `local_support/tbench-agent/`. | Summarization agent factory read; local CLI's direct runner and trace loop read; support-server entry file searched. Remaining agent prompts/configs and adapters await detailed inspection, not excluded host status. |
| `benchmarks/` | Included task drivers, prompt construction, output/reward collection and baseline comparison adapters: security, CTF, DevOps, Harbor, SWE-bench Pro, Termigen, AgentBeats and code-comprehension paths. | Direct runner, retained session and reward locations searched in `secodeplt/vul_detection_memory.py`; AgentBeats entry file searched. Other benchmark bodies not yet inspected. No benchmark score or effectiveness is established by their presence. |
| `docs/` | Included declared design and operational guidance under `wiki/`, with CLI-generation tooling under `scripts/`. | Tree inventoried: history/sessions/multi-agent component docs, configuration, example, evaluation, RL and sandbox guidance. Detailed prose/tooling not yet inspected. Assets support presentation, not mechanism evidence. |
| `pyproject.toml` | Included package entry point, distribution contents and dependency declarations. | Read completely; establishes CLI mapping and wheel inclusion of agent library, UI bundle and hook files. |
| `rl/` | Included OpenSage-side training launchers, configs, mock agent and integration documentation: `areal/`, `slime/`, `nemo_rl/`. | AReaL launcher argument/dependency resolution read; documentation integration references and mock agent searched. External trainer bodies are excluded; training-loop correctness and learned improvement cannot be established. |
| `src/` | Included shipped implementation. Material paths: `opensage/cli/`, `agents/`, `config/`, `session/`, `orchestration/`, `llm/`, `memory/file_based/`, `features/`, `patches/`, `plugins/`, `sandbox/`, `sandbox_scripts/`, `toolbox/`, `bash_tools/`, `templates/`, `utils/`, `workflow/`, and `evaluation/` including RL adapters. | Agent constructor, session ownership, runner construction, CLI/web entry and persistence paths, memory setup/policy injection, compaction persistence, evaluation dispatch/collection and RL client inspected. Sandbox backend/tool/plugin internals, skill scripts and remaining live-web paths are available but not yet characterized. The bundled `cli/vendor/adk_browser/` is included as a shipped UI consumer; its minified internals were not inspected. |
| `tests/` | Included authored checks and fixtures for runtime, orchestration, compaction/pinned memory, sandbox/tools, benchmark and RL interfaces. | Tree inventoried and CLI-resume test opening read. Tests are specification/implementation evidence only; not executed and do not establish a passing suite. |
| `third_party/` | Included checked-in Cybergym integration code as source available at this pin; excluded external SWE-bench Pro gitlink contents. | Cybergym tree inventoried, bodies not yet inspected. SWE-bench Pro is recorded as gitlink `1f255c2ff7109cf92bb56b9cbf2416fd8b0de103`, not a registered second repository. Exclusion prevents claims about its dataset/evaluator implementation. |
| `uv.lock` | Included dependency-resolution artifact. | Inventoried, not yet inspected; installed dependency bytes and their behavior are not frozen by this analysis. |
| `zensical.toml` | Excluded documentation-site build configuration. | No conclusions about published-site build or deployment behavior. |

### Dependencies and evidence limits

External dependencies include ADK, LiteLLM/model providers, sandbox/container services, Neo4j for supported graph tooling, MCP services and evaluation/training ecosystems. The package declares ADK and LiteLLM dependencies along with optional Harbor, AgentBeats, Nitrobox and OpenSandbox integrations (SRC-1, `pyproject.toml`). This source set supports OpenSage-side wiring and contracts, not those services' implementation behavior. External model outputs, datasets, deployed sandboxes, live sites and trainer repositories are not captures in this boundary.

There is no supplied execution trace or causal experiment. The target, its tests and examples were not executed. Thus this boundary supports analysis of implemented and intended operation, not claims about model adherence to knowledge maintenance, successful cross-restart recovery in a deployed environment, benchmark performance or improvement caused by memory. Available but unread files in the coverage table are inspection work for subsequent source-grounded jobs, not unavailable evidence. No material OpenSage-owned execution or retained-state responsibility has been deliberately excluded.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/opensage-agent/OpenSage` | 54d64702e18d195c8f0fed711c6db5dc1d62ab29 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/opensage-291d1ed79d37/related-systems/opensage-agent--OpenSage`. Implementation: tracked-tree inventory; `pyproject.toml`; selected entry/constructor/retention ranges in `src/opensage/cli/opensage_cli.py`, `src/opensage/cli/opensage_web_app.py`, `src/opensage/agents/opensage_agent.py`, `src/opensage/session/opensage_session.py`, `src/opensage/orchestration/manager.py`; complete `src/opensage/__init__.py`, `src/opensage/patches/agent_run_async.py`, `src/opensage/memory/file_based/short_term/prompt.py`, `src/opensage/memory/file_based/long_term/knowledge_store.py`, `src/opensage/evaluation/dispatchers/native.py`; selected compaction and evaluation-loop ranges in `src/opensage/features/summarization.py`, `src/opensage/evaluation/base.py`; RL client opening, sample summarization agent, local-support CLI runner/trace loop and CLI-resume test opening. Searches also located persistence/session-file helpers, support-server and vulnerability-memory/AgentBeats benchmark paths. Doctrine/design: complete default memory policy and `.gitmodules`, bounded README/SKILL/RL documentation searches and AReaL launcher dependency resolution. | Implementation: [package/entry declarations](https://github.com/opensage-agent/OpenSage/blob/54d64702e18d195c8f0fed711c6db5dc1d62ab29/pyproject.toml), [runtime manager](https://github.com/opensage-agent/OpenSage/blob/54d64702e18d195c8f0fed711c6db5dc1d62ab29/src/opensage/orchestration/manager.py), [run-memory wrapper](https://github.com/opensage-agent/OpenSage/blob/54d64702e18d195c8f0fed711c6db5dc1d62ab29/src/opensage/patches/agent_run_async.py), [evaluation consumer](https://github.com/opensage-agent/OpenSage/blob/54d64702e18d195c8f0fed711c6db5dc1d62ab29/src/opensage/evaluation/base.py). Doctrine/design: [memory policy](https://github.com/opensage-agent/OpenSage/blob/54d64702e18d195c8f0fed711c6db5dc1d62ab29/src/opensage/templates/auto_insert_prompts/default.md), [framework instructions](https://github.com/opensage-agent/OpenSage/blob/54d64702e18d195c8f0fed711c6db5dc1d62ab29/SKILL.md). | Repository source is reachable. External dependency/trainer/service bodies and SWE-bench Pro gitlink contents are outside this frozen source set; their internal behavior cannot be attributed to OpenSage. Implementation layer has no observed execution or causal support. Doctrine/design establishes declared policy and usage only, not compliance or performance. Uninspected tracked paths remain available within this Git source. |
