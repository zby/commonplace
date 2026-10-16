---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "SwarmWorld's shipped simulation, model-agent orchestration, retained state, interfaces and research tooling at commit 6af7ae9fa36d98b07b0492cf139658e8af1f6eab."
run-id: AAS-2026-10-15-swarmworld-e39fbc17e3fb-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "6af7ae9fa36d98b07b0492cf139658e8af1f6eab"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/lamm-mit/SwarmWorld
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/swarmworld-e39fbc17e3fb/related-systems/lamm-mit--SwarmWorld
  revision: 6af7ae9fa36d98b07b0492cf139658e8af1f6eab
  sha256: null
---

# SwarmWorld boundary

## Boundary and evidence

This run covers SwarmWorld as a research environment for societies of model agents, not as a general coding agent or a physical materials predictor. Its target class is **enclosing runtime**: shipped drivers own the simulation state, schedule model decisions, assemble local observations and retained memory, admit structured action plans, advance the world and record the resulting state. The boundary kind is **whole-system**, including the headless, live-server, human-play, environment-adapter, replay and evaluation paths rather than only the policy API. The historical executable and Python namespace are `biofoundry` (SRC-1, `README.md`, `pyproject.toml`, `src/biofoundry/cli.py`, `src/biofoundry/server.py`, `game/session.py`).

The model-dependent loop is directly inspectable. The CLI constructs `BioFoundrySimulation` and a policy, calls `refresh_plans`, records model traces and selected actions, and calls `simulation.step`. The live driver follows the same planning/stepping sequence; the human-play driver additionally merges a possessed agent's input. `LLMPolicy` builds prompts from semantic observations, retrieved records and prior research state, calls the provider, validates the returned plan, writes private research state, and queues actions for later ticks. These shipped callers are included system responsibilities, not excluded external hosts (SRC-1, `src/biofoundry/cli.py`, `src/biofoundry/server.py`, `game/session.py`, `src/biofoundry/policies/llm.py`). Minimum implementation passages establishing the classification are:

> committed = await policy.refresh_plans(simulation)
> --- `src/biofoundry/cli.py`

> result = simulation.step(actions)
> --- `src/biofoundry/cli.py`

> generation = await generate_record(messages)
> --- `src/biofoundry/policies/llm.py`

The state boundary includes private working/episodic/notebook records, empirical knowledge, the public archive, spatial insights, research mission state, program knowledge and inherited artifact programs. It includes state producers, admission rules, later prompt consumption and recorded-state reconstruction. Initial inspection followed private memory retrieval and writes through the LLM policy, publication/teaching and observation writers in the simulation, scenario prompt loading, the CLI/live/human recorders, and replay's application of recorded research state before world stepping. This establishes coverage of the shipped loop, not a claim that every state transition has already been audited (SRC-1, `src/biofoundry/memory.py`, `src/biofoundry/knowledge.py`, `src/biofoundry/simulation.py`, `src/biofoundry/program_library.py`, `src/biofoundry/scenarios.py`, `src/biofoundry/counterfactuals.py`, `src/biofoundry/playback.py`).

> """Replay authoritative private-memory writes made by the LLM policy."""
> --- `src/biofoundry/counterfactuals.py`

The immutable evidence is repository commit `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`, with applicability cutoff **2026-10-15**. The supplied checkout's HEAD was verified against that pin. Overall evidence is **code-grounded**. Documentation and repository-local world-building instructions supply declared design, not instructions for this analysis. No target code, tests, model calls or examples were executed. Consequently this boundary supplies implementation and doctrine/design evidence, not observed-run or causal-experiment evidence.

External dependencies include the configured model-serving endpoint and its model, Python scientific/configuration libraries, PettingZoo/Gymnasium, FastAPI/Uvicorn/WebSockets and browser/Godot execution environments. The repository includes the provider adapter, not provider internals or model weights. The published paper dataset is explicitly outside the source release and is not acquired in this run. This prevents verification of the paper's episode outcomes, empirical scaling claims and replay success on those traces. Documentation about those outcomes can only be attributed as reported operation if later used. The boundary does not establish physical-world validity of the simulator's surrogate physics (SRC-1, `pyproject.toml`, `src/biofoundry/providers/openai_compatible.py`, `README.md`, `DATA.md`).

> This repository contains the SwarmWorld simulator, interfaces, configurations, tests,
> and documentation. It intentionally does not contain raw or derived paper data.
> --- `DATA.md`

### Top-level tracked coverage

Every top-level tracked entry is classified below. Included directories remain available for deeper inspection at the same commit; initial scope is not an evidence allowlist. “Not yet inspected in detail” denotes available source, not an access gap. Deliberately excluded administrative files do not own simulation or agent-state transitions.

| Top-level entry | Treatment and material paths | Initial inspection and limits |
|---|---|---|
| `.agents/` | Included authoring plane: `skills/swarmworld-world-builder/SKILL.md`, its format contract, verification workflow and agent metadata. | Skill inspected as doctrine/design. Its references and metadata are available but not yet inspected in detail. The skill maintains scenario packages outside an episode; it is not an in-world self-modification loop (SRC-1, `.agents/skills/swarmworld-world-builder/SKILL.md`). |
| `.gitignore` | Deliberately excluded housekeeping. | Not inspected; no conclusion about completeness of ignored local files or secret exclusion. |
| `CITATION.cff` | Deliberately excluded citation metadata. | Not inspected; no independent bibliographic verification. |
| `CONTRIBUTING.md` | Deliberately excluded contributor process. | Not inspected; no claim about contributor governance or compliance. |
| `DATA.md` | Included source/data boundary. | Read completely; external data unavailable within this frozen source, preventing empirical confirmation of released studies (SRC-1, `DATA.md`). |
| `LICENSE` | Deliberately excluded legal text. | Not inspected; no legal interpretation or license-compliance conclusion. |
| `Makefile` | Included entry-point shortcuts for simulation, serving, verification and browser development. | Read completely; targets not executed (SRC-1, `Makefile`). |
| `README.md` | Included project intent, shipped paths and scientific limitations. | Read completely as doctrine/design, not proof of runtime success (SRC-1, `README.md`). |
| `RELEASE_MANIFEST.sha256` | Deliberately excluded release-integrity manifest. | Not inspected; repository pin is established, but manifest integrity is not independently verified. |
| `RELEASE_PROVENANCE.json` | Deliberately excluded packaging provenance. | Not inspected; no release-build provenance conclusion. |
| `SECURITY.md` | Deliberately excluded security-reporting policy. | Not inspected; no security assurance or disclosure-process conclusion. |
| `configs/` | Included run/model/treatment configuration: `demo.yaml`, `scale.yaml`, hosted and local-model profiles, and `README.md`. | Enumerated; configuration loading and policy selection traced through CLI. Individual profile values not yet inspected in detail; no claim of operational provider compatibility from profile names (SRC-1, `src/biofoundry/cli.py`, `configs/README.md`). |
| `docs/` | Included architecture, protocol, structured outputs, reproducibility, local serving, human play, observatory and experiment/analysis doctrine; assets are presentation material. | Enumerated; deeper documentation inspection deferred. No documentation claim is treated as an observed result (SRC-1, `docs/ARCHITECTURE.md`, `docs/PROTOCOL.md`, `docs/REPRODUCIBILITY.md`, `docs/ANALYSIS.md`). |
| `environment.yml` | Included dependency specification alongside `pyproject.toml`. | Available, not yet inspected in detail; no environment reproducibility claim. |
| `game/` | Included second shipped driver, not an external application: `serve.py`, `app.py`, `session.py`, `policy.py`, `human.py`, `settings.py`, profiles, browser client and tests. | Entrypoint read; app/policy/session routing searched; tick body read through planning, human override, recording and stepping. Client consumption and test declarations searched. Remaining guards and UI details need later inspection (SRC-1, `game/serve.py`, `game/session.py`, `game/policy.py`, `game/client/js/main.js`, `game/tests/test_human_play.py`). |
| `godot/` | Included optional observer/control surface: project/scene and `scripts/network_client.gd`, `main.gd`, `world_view.gd`. | Network receive/send path searched; rendering details not yet inspected. No client execution or visual-correctness claim (SRC-1, `godot/scripts/network_client.gd`). |
| `pyproject.toml` | Included package, dependencies and installed CLI declaration. | Read completely; `biofoundry.cli:main` traced into drivers (SRC-1, `pyproject.toml`). |
| `runs/` | Included output location; only `.gitkeep` is tracked. | Tree inspected; no generated run evidence is supplied. This prevents empirical episode conclusions, not source-loop inspection (SRC-1, `runs/.gitkeep`, `DATA.md`). |
| `scripts/` | Included release tooling: `verify_release.py`. | Enumerated and its Makefile caller inspected; verifier implementation not yet inspected. No release-verification success claimed (SRC-1, `scripts/verify_release.py`, `Makefile`). |
| `src/` | Included full engine: `biofoundry/__main__.py`, `cli.py`, `server.py`, `env.py`; policies/providers and structured admission; `simulation.py`, world/population/material/artifact/program engines; memory/knowledge/science/program-library state; events, playback/counterfactuals; study, mobility, trace, scenario, ecology and technology analysis/visualization. | Entrypoints traced to model planning, memory consumption/writes, authoritative stepping and recording. Replay reconstruction and held-out evaluator inspected in bounded ranges. Remaining physics, analysis and visualization internals are available for later jobs, not access gaps (SRC-1, `src/biofoundry/cli.py`, `src/biofoundry/policies/llm.py`, `src/biofoundry/simulation.py`, `src/biofoundry/events.py`, `src/biofoundry/playback.py`, `src/biofoundry/technology_ecology.py`). |
| `tests/` | Included executable specifications/evaluators across simulation, providers, memory-related architectures, scenarios, replay and controlled studies. | Test declarations searched in policy, flagship, playback and scenario suites. No tests executed; declarations alone do not establish passing behavior (SRC-1, `tests/test_llm_policy.py`, `tests/test_flagship_experiment.py`, `tests/test_playback.py`, `tests/test_scenarios.py`). |
| `web/` | Included observatory, control transport, replay/history consumption, local demo, export and browser tests: `src/hooks/useBiofoundry.ts`, `src/lib/`, components, app and build files. | Hook searched through authoritative-frame acceptance, command sending and demo fallback. Demo state must not be mistaken for Python-authoritative evidence. Rendering/export details not yet inspected (SRC-1, `web/src/hooks/useBiofoundry.ts`). |
| `worlds/` | Included Ashen Realms manifest, routed YAML catalogs/geometry/fields/missions, configs, runtime agent prompt, separate researcher instructions and example summary. | Package tree inspected; agent prompt read and loader traced through manifest routing, prompt incorporation and package hashing. Researcher guidance and example summary not yet inspected; no example-outcome claim (SRC-1, `worlds/ashen_realms/prompts/agent_instructions.md`, `src/biofoundry/scenarios.py`, `src/biofoundry/policies/llm.py`). |

The evaluation boundary includes study conditions and held-out frozen-society evaluation, counterfactual replay and analysis consumers. These are shipped mechanisms, not causal findings from this run. In particular, the inspected held-out generalization function consumes an existing simulation and independent disturbance seeds; replay applies recorded plans/state rather than asking a model to choose again (SRC-1, `src/biofoundry/technology_ecology.py`, `src/biofoundry/counterfactuals.py`, `src/biofoundry/playback.py`, `src/biofoundry/cli.py`).

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/lamm-mit/SwarmWorld` | 6af7ae9fa36d98b07b0492cf139658e8af1f6eab | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/swarmworld-e39fbc17e3fb/related-systems/lamm-mit--SwarmWorld`. Implementation: tracked tree, package entrypoint, CLI episode driver, LLM prompt/retrieval/admission/write/queue paths, simulation observation and memory writer locations, memory retrieval, live/human tick drivers, environment step, replay and recorded private-memory restoration, scenario loader, held-out generalization evaluator; bounded searches of provider, analysis/program-library, client transports and selected tests. Doctrine/design: README, DATA, world-builder skill, scenario agent prompt and package metadata. | Implementation: [CLI](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/cli.py), [policy](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/policies/llm.py), [simulation](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/simulation.py), [human driver](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/game/session.py), [replay restoration](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/counterfactuals.py). Doctrine/design: [README](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/README.md), [data boundary](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/DATA.md), [world-building skill](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/.agents/skills/swarmworld-world-builder/SKILL.md). | No repository access gap encountered. Separate dataset, provider internals/model weights and actual executions are not supplied: no observed-run, empirical paper-result, provider-reliability or causal-experiment conclusion. Available but deferred source details are identified in the coverage table. |
