---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Agent S's shipped computer-use runtimes, drivers, memory paths and rollout selection at commit 15776a8dc659658b1963816ea006f7af1978e595."
run-id: AAS-2026-10-16-agent-s-db6fee212353-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "15776a8dc659658b1963816ea006f7af1978e595"
analysis-cutoff: "2026-10-16"
evidence-tier: code-grounded
source:
  identity: https://github.com/simular-ai/Agent-S
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-agent-s/related-systems/simular-ai--Agent-S
  revision: "15776a8dc659658b1963816ea006f7af1978e595"
  sha256: null
---

# Agent S boundary

## Boundary and evidence

This run examines the open-source Agent S computer-use framework, not Simular's hosted products. Its intended use is to turn natural-language tasks and desktop observations into actions in desktop applications. The target is an **enclosing runtime** when its shipped drivers are included: those drivers acquire observations, call the agent, execute its returned actions and obtain the next observation. The library's `predict` interface alone is not the selected target. The boundary is **whole-system** for the shipped repository artifact, including current S3 and the retained S1, S2 and S2.5 paths. Version-specific responsibilities must not be projected onto all generations. SRC-1: `README.md`, `setup.py`, `gui_agents/s3/cli_app.py`, `gui_agents/s3/agents/agent_s.py`, `gui_agents/s1/core/AgentS.py`, `gui_agents/s2/agents/agent_s.py`, `gui_agents/s2_5/agents/agent_s.py`.

The installed command selects S3, and its driver supplies the action/observation loop. These implementation passages establish the runtime classification rather than a classification based only on the project's name. SRC-1: `setup.py`, `gui_agents/s3/cli_app.py`.

> "agent_s=gui_agents.s3.cli_app:main",
> --- `setup.py`

> # Get next action code from the agent
> info, code = agent.predict(instruction=instruction, observation=obs)
> --- `gui_agents/s3/cli_app.py`

> # Ask for permission before executing
> exec(code[0])
> time.sleep(1.0)
> --- `gui_agents/s3/cli_app.py`

The comment in the last passage is not evidence that permission is actually requested. The boundary includes the driver implementation, not merely its comments or the SDK contract.

Included functions are task admission through CLI/SDK and the OpenClaw wrapper; model-backed action generation and reflection; action grounding and OCR; procedural prompts, message history and text buffers; the optional S3 coding agent and local controller; historical hierarchical planning and persistent experience paths; and benchmark drivers, trajectory recording, fact generation and comparative rollout selection. The S1/S2 CLI callers that update memory and the managers/workers that retrieve it are inside this boundary. They are not excluded host applications. Likewise, the shipped OSWorld scripts remain included even though their deployment instructions copy them into another repository. SRC-1: `gui_agents/s3/agents/worker.py`, `gui_agents/s3/agents/grounding.py`, `gui_agents/s3/agents/code_agent.py`, `gui_agents/s3/memory/procedural_memory.py`, `gui_agents/s1/cli_app.py`, `gui_agents/s2/cli_app.py`, `gui_agents/s1/core/Knowledge.py`, `gui_agents/s1/core/Manager.py`, `gui_agents/s1/core/Worker.py`, `gui_agents/s2/core/knowledge.py`, `gui_agents/s2/agents/manager.py`, `gui_agents/s2/agents/worker.py`, `integrations/openclaw/agent_s_wrapper.py`, `osworld_setup/s3/OSWorld.md`.

Two retained-content consumers are especially important to the scope. Historical CLI trajectories feed persistent memory, while S3's benchmark artifacts feed a separate selection pipeline. Including only the installed S3 agent API would omit both kinds of shipped responsibility. SRC-1: `gui_agents/s2/cli_app.py`, `osworld_setup/s3/bbon/generate_facts.py`, `osworld_setup/s3/bbon/run_judge.py`, `gui_agents/s3/bbon/comparative_judge.py`.

> subtask_traj = agent.update_episodic_memory(info, subtask_traj)
> --- `gui_agents/s2/cli_app.py`

> trajectory_file = os.path.join(task_dir, "traj.jsonl")
> if os.path.exists(trajectory_file):
>     try:
>         with open(trajectory_file, "r") as f:
>             trajectory_lines = f.readlines()
>     except:
>         pass
> --- `osworld_setup/s3/bbon/generate_facts.py`

> response = call_llm_formatted(self.judge_agent, [], messages=messages)
> answer, thoughts = split_thinking_response(response)
> --- `gui_agents/s3/bbon/comparative_judge.py`

### Tracked top-level coverage

The tracked tree was enumerated at the frozen commit. Included rows designate the functional evidence available to later jobs, not a claim that every file has already received a full mechanism review. Initial inspection traced entry points, callers and retained-state consumers through the paths below. Searches of historical paths establish their presence and call relationships; detailed behavioral claims still require source inspection. Available but not yet fully inspected material is not an access gap.

| Top-level tracked path | Treatment and material paths | Role, initial inspection and limits |
|---|---|---|
| `.github/` | Included: `.github/workflows/lint.yml` | Read workflow; packaging installation and formatting check, not observed test results. |
| `.gitignore` | Excluded | Repository hygiene, not runtime behavior; no conclusions about ignored deployment files or actual local state. |
| `LICENSE` | Excluded | Licensing text; no legal assessment. |
| `README.md` | Included | Read project description, installed CLI, SDK caller, coding-environment warnings and reported results. Hosted-product descriptions are attributed declarations, not hosted implementation evidence. |
| `WAA_setup.md` | Included | Searched deployment instructions and external WindowsAgentArena handoff; not a captured Windows execution. |
| `evaluation_sets/` | Included: `evaluation_sets/test_all.json`, `evaluation_sets/test_small_new.json` | Tracked benchmark selection manifests; inspected a sample of the smaller manifest. Full task semantics and task environments are not contained in these lists. |
| `gui_agents/` | Included: `gui_agents/utils.py`; `gui_agents/s1/cli_app.py`, `gui_agents/s1/core/`, `gui_agents/s1/aci/`, `gui_agents/s1/mllm/`, `gui_agents/s1/utils/`; `gui_agents/s2/cli_app.py`, `gui_agents/s2/agents/`, `gui_agents/s2/core/`, `gui_agents/s2/memory/`, `gui_agents/s2/utils/`; corresponding `gui_agents/s2_5/` and `gui_agents/s3/` agent/core/memory/utils paths; `gui_agents/s3/bbon/` | Runtime implementations, prompts, provider adapters, historical memory production/retrieval, grounding and code execution. Read S3 agent and worker, selected grounding/code/prompt sections, S2.5 agent, historical memory-writing sections and shared KB downloader. Searched historical CLI, managers, workers and knowledge paths to trace persistent-state callers and consumers. Enumerated provider adapters and auxiliary modules; their detailed semantics remain for downstream inspection. |
| `images/` | Excluded: logos, result graphics, architecture/result PDFs, `images/waa_setup/`, `.DS_Store` | Presentation and reported diagrams/results; not used as implementation evidence. This prevents independently extracting or verifying numerical results or architectural details found only in those graphics. Textual declarations remain available in included documentation. |
| `integrations/` | Included: `integrations/openclaw/agent_s_task`, `integrations/openclaw/agent_s_wrapper.py`, `integrations/openclaw/SKILL.md`, `integrations/openclaw/README.md` | Shipped task bridge and operating instructions; read Python wrapper and skill text, searched README and shell entry point. OpenClaw itself is external, but this bridge's argument construction, subprocess invocation and result handling are not. |
| `models.md` | Included | Searched provider-use documentation and version-specific SDK examples; provider behavior must be checked against code rather than assumed from examples. |
| `osworld_setup/` | Included: `osworld_setup/s1/`, `osworld_setup/s2/`, `osworld_setup/s2_5/`, `osworld_setup/s3/` run scripts, single-example helpers and deployment docs; `osworld_setup/s3/run.sh`, `osworld_setup/s3/bbon/` | Shipped observation/action drivers, task distribution, logging, evaluation calls, retained screenshots/trajectories, fact-caption production and later judging. Read S3 single-example loop, deployment instructions, shell workflow and selected fact-generation code; searched generation-specific launchers and read comparative judge. External environment implementation is not supplied here. |
| `requirements.txt` | Included | Dependency declaration, enumerated but not yet read; no assertion that it exactly matches `setup.py` or that either installs successfully. |
| `setup.py` | Included | Read package metadata, dependencies, Python constraints and the S3 console entry point. |
| `tests/` | Included: `tests/test_providers.py` | Read provider initialization/configuration tests as source. Not executed; no claim that tests pass or cover desktop task success. |

All path/role statements in this table refer to SRC-1 at the reviewed commit. Supporting anchors include `setup.py`, `.github/workflows/lint.yml`, `tests/test_providers.py`, `gui_agents/utils.py`, `gui_agents/s2/cli_app.py`, `gui_agents/s3/agents/worker.py`, `osworld_setup/s3/lib_run_single.py`, `osworld_setup/s3/run.sh`, `osworld_setup/s3/bbon/generate_facts.py`, `integrations/openclaw/agent_s_wrapper.py` and `integrations/openclaw/SKILL.md`.

### Frozen evidence and external limits

The sole frozen source is SRC-1, repository `https://github.com/simular-ai/Agent-S` at full commit `15776a8dc659658b1963816ea006f7af1978e595`. The acquired checkout's HEAD was verified against that revision and its working tree was clean. The applicability cutoff is **2026-10-16**, the supplied run date; this is not a claim about later releases or deployments. Overall evidence is **code-grounded**. Repository documentation supplies declared intent and attributed performance reports. No target, tests, examples, provider calls or desktop sessions were executed for this boundary.

External dependencies include generation and grounding model endpoints, OCR and GUI-control libraries, operating-system permissions and desktop applications, and OSWorld's `DesktopEnv`, VM/provider infrastructure and task/evaluation definitions. Historical default knowledge bundles are downloaded from release assets rather than present in the tracked tree. The downloader is inspectable; the contents of those bundles are not frozen here. These distinctions follow SRC-1: `setup.py`, `gui_agents/s3/agents/grounding.py`, `gui_agents/utils.py`, `osworld_setup/s3/run.py`, `osworld_setup/s3/run_local.py`, `osworld_setup/s3/lib_run_single.py`.

The following are evidence gaps or deliberate functional exclusions, not omitted shipped drivers:

- **External model/service and platform implementations are not captured.** Code supports conclusions about calls, prompt construction and returned-result handling, not model accuracy, endpoint availability, service retention policies or desktop reliability.
- **External benchmark environments, downloaded KB assets and actual rollout directories are not captured.** The source supports analysis of recording, summarization, retrieval, selection and evaluation call sites, not the correctness of unseen KB entries, actual generated captions, realized benchmark outcomes or causal performance improvements.
- **OpenClaw's enclosing orchestration is excluded; its shipped Agent S bridge is included.** The bridge cannot establish the host's scheduling, authorization or memory behavior. SRC-1: `integrations/openclaw/agent_s_wrapper.py`, `integrations/openclaw/SKILL.md`.
- **Sai, Simular Cloud and Simular API implementations are excluded.** Their links and descriptions in `README.md` do not freeze those services or establish that their mechanisms are identical to this code. Hosted-product performance and operation cannot be attributed to the inspected runtime.
- **Linked papers, blog posts, videos and other repositories are not additional sources.** Their contents were not fetched. Repository text can be cited as the authors' report, not as independent experimental verification. No observed-run or causal-experiment evidence is established by this boundary.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/simular-ai/Agent-S` | 15776a8dc659658b1963816ea006f7af1978e595 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-agent-s/related-systems/simular-ai--Agent-S`. Implementation: tracked tree and entry-point enumeration; `setup.py`; `gui_agents/s3/agents/agent_s.py`, `gui_agents/s3/agents/worker.py`, selected `gui_agents/s3/agents/grounding.py`, `gui_agents/s3/agents/code_agent.py`, `gui_agents/s3/bbon/comparative_judge.py`; historical agent/memory-writing sections and searches through S1/S2 knowledge/manager/worker consumers and CLI memory callers; `gui_agents/utils.py`; `osworld_setup/s3/lib_run_single.py`, launcher searches, selected `osworld_setup/s3/bbon/generate_facts.py` and `osworld_setup/s3/bbon/run_judge.py`; OpenClaw wrapper and entry-point searches; tests and lint workflow. Doctrine/design: `README.md`, `gui_agents/s3/memory/procedural_memory.py` worker prompt construction, `integrations/openclaw/SKILL.md`, deployment/model documentation searches, `osworld_setup/s3/OSWorld.md` and `osworld_setup/s3/run.sh`. Reported operation: benchmark and product claims in `README.md`, treated only as attributed reports. | Implementation: [entry point](https://github.com/simular-ai/Agent-S/blob/15776a8dc659658b1963816ea006f7af1978e595/setup.py), [desktop loop](https://github.com/simular-ai/Agent-S/blob/15776a8dc659658b1963816ea006f7af1978e595/gui_agents/s3/cli_app.py), [worker](https://github.com/simular-ai/Agent-S/blob/15776a8dc659658b1963816ea006f7af1978e595/gui_agents/s3/agents/worker.py), [historical memory caller](https://github.com/simular-ai/Agent-S/blob/15776a8dc659658b1963816ea006f7af1978e595/gui_agents/s2/cli_app.py), [rollout recording](https://github.com/simular-ai/Agent-S/blob/15776a8dc659658b1963816ea006f7af1978e595/osworld_setup/s3/lib_run_single.py), [selection](https://github.com/simular-ai/Agent-S/blob/15776a8dc659658b1963816ea006f7af1978e595/gui_agents/s3/bbon/comparative_judge.py). Doctrine/design: [prompts](https://github.com/simular-ai/Agent-S/blob/15776a8dc659658b1963816ea006f7af1978e595/gui_agents/s3/memory/procedural_memory.py), [deployment](https://github.com/simular-ai/Agent-S/blob/15776a8dc659658b1963816ea006f7af1978e595/osworld_setup/s3/OSWorld.md). Reported operation: [README](https://github.com/simular-ai/Agent-S/blob/15776a8dc659658b1963816ea006f7af1978e595/README.md). | No checkout access gap identified. Initial inspected paths are not an allowlist: other tracked files at this commit remain available for inspection. External environments, model weights/endpoints, release KB assets, hosted products and actual execution traces are not frozen; their internal behavior, realized task success and causal benchmark claims cannot be established. Documentation and reported results do not supply observed-run or causal-experiment evidence. |
