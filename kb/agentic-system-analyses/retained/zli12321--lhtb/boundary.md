---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "LHTB's model-dependent terminal evaluation workflow and bundled modified Harbor at commit 7ca0cacea9bf6a0694eaad7306bed794eaaaabce."
run-id: AAS-2026-10-15-lhtb-a0548ba4edbf-01
result-disposition: complete
target-class: workflow
boundary-kind: whole-system
reviewed-boundary: "7ca0cacea9bf6a0694eaad7306bed794eaaaabce"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/zli12321/lhtb
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/lhtb-a0548ba4edbf/related-systems/zli12321--lhtb
  revision: "7ca0cacea9bf6a0694eaad7306bed794eaaaabce"
  sha256: null
---

# LHTB boundary

## Boundary and evidence

LHTB is in scope as a **workflow** for evaluating model-driven terminal work, including its bundled execution and continuation machinery. The intended use of this analysis is to explain how task instructions, persistent sandbox artifacts, model context, hidden verification and run results interact. It is not a review of the scientific correctness of every benchmark problem or a replication of the leaderboard. The boundary is **whole-system** for that evaluation workflow, not for every independent use of the vendored Harbor framework.

The target includes both task generations, shipped launch configurations and drivers, the modified Harbor job/trial orchestrator, Terminus-2 and its context management, supported agent and environment integration paths, verifier isolation and artifact transfer, result persistence and later consumption, and the shipped patch-maintenance instructions. The bundled runtime is not an external dependency merely because the benchmark invokes its CLI. Task-local RAG, memory and simulation programs are benchmark workloads, not automatically general capabilities of the evaluation harness. These distinctions follow the shipped driver and consumers: SRC-1, `configs/examples/full_benchmark_2.0.yaml`, `scripts/daytona_cleanup/run_daytona_eval.sh`, `harbor/src/harbor/cli/jobs.py`, `harbor/src/harbor/trial/trial.py`, and `tasks/langchain-version-migration/task.toml`.

The bundled Harbor README identifies its connection to LHTB (SRC-1):

> This copy of Harbor is **not** stock upstream Harbor. It is the exact harness used to
> run [LHTB](../README.md), based on Harbor **0.7.0** with the
> **continue-until-timeout** extension plus verifier-isolation and binary-feedback
> hardening.
> --- `harbor/README.md`

The default full-suite configuration selects a model-calling agent and both task roots:

> agents:
>   - name: terminus-2
>     model_name: openai/gpt-4.1
> --- `configs/examples/full_benchmark_2.0.yaml`

> datasets:
>   - path: ./tasks
>   - path: ./tasks-2.0
> --- `configs/examples/full_benchmark_2.0.yaml`

### Entry-point and state-loop coverage

Initial tracing followed the console entry point declared in `harbor/pyproject.toml` through `harbor/src/harbor/cli/main.py` and the job-start consumer in `harbor/src/harbor/cli/jobs.py`. That consumer creates and runs a `Job`. `harbor/src/harbor/job.py` expands task/agent configurations, reloads existing trial results, and reconciles remaining trials. The trial layer invokes the selected agent, runs verification, transfers configured artifacts to separate verifier environments when selected, and writes the final trial result. Terminus-2 constructs prompts from task instructions and terminal state, calls the model through `Chat`, and exposes a same-conversation continuation path. Thus this is not just a passive task dataset or a returning numeric grader. All paths in this paragraph are SRC-1 implementation evidence: `harbor/src/harbor/agents/terminus_2/terminus_2.py`, `harbor/src/harbor/llms/chat.py`, `harbor/src/harbor/verifier/verifier.py`, and the entry-point paths above.

The model-call boundary is explicit:

> llm_response: LLMResponse = await self._model.call(
>             prompt=prompt,
>             message_history=self._messages,
>             logging_path=logging_path,
>             previous_response_id=self._last_response_id,
>             **kwargs,
>         )
> --- `harbor/src/harbor/llms/chat.py`

The continuation consumer can reuse the existing conversation and terminal session:

> async def resume_after_verifier_rejection(
>         self,
>         user_prompt: str,
>         context: AgentContext,
>     ) -> None:
>         """Continue the existing Chat and tmux session after binary rejection."""
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

Host-side result persistence is also part of the target, not an excluded caller:

> self._trial_paths.result_path.write_text(self.result.model_dump_json(indent=4))
> --- `harbor/src/harbor/trial/trial.py`

The coverage table accounts for every top-level tracked entry. “Included” fixes functional scope; it does not assert that every file in that subtree has already been read. Initial inspection is named separately from source that remains available for the downstream analysis. No uninspected file is described as inaccessible.

| Top-level tracked entry | Treatment and role | Initial inspection and remaining limits |
|---|---|---|
| `.env.example` | Included: launch-time provider/environment configuration surface. | Tree inspected; contents not yet inspected. No conclusion about secret handling or all provider requirements is established here. |
| `.gitattributes` | Excluded: repository transport metadata. | Tree inspected; exclusion prevents claims about checkout/filter behavior. |
| `.gitignore` | Excluded: repository hygiene policy. | Tree inspected; exclusion prevents claims that all generated run material is tracked or retained. |
| `LICENSE` | Excluded: legal terms. | Not a mechanism source; no licensing assessment. |
| `README.md` | Included: system intent, launch instructions and attributed results. | Inspected introduction, harness declaration and result discussion; launch references searched. Results are reported operation, not independently observed runs. |
| `README.zh-CN.md` | Included: parallel documentation. | Available, not initially inspected; translation parity is not established. |
| `assets/` | Included: published result data and figure consumers, notably `make_figures_2.0.py`, `lhtb2_results.csv` and `lhtb2_reward_over_time.csv`. | Inspected figure script's data contract and result loader; CSVs, remaining plotting code and binary figures are not initially audited. No independent performance conclusion. |
| `configs/` | Included: agent/model/provider selection, budgets, task-root selection and rerun recipes under `examples/` and `leaderboard/`. | Read `examples/full_benchmark_2.0.yaml`; other configurations remain available. One example does not establish every reported run's settings. |
| `dataset.toml` | Included: dataset declaration. | Tree inspected; contents remain to be inspected if needed. No registry/publication parity claim. |
| `harbor/` | Included: shipped evaluation runtime and its operator/maintenance surfaces. Material paths include `pyproject.toml`, `src/harbor/cli/{main,jobs}.py`, `job.py`, `trial/{trial,process_reward,queue}.py`, `models/{task,job,trial}/`, `agents/`, `llms/`, `environments/`, `verifier/`, `metrics/`, `viewer/`, `upload/`, `storage/`, `docs/`, `tests/`, `patches/` and `skills/apply-lhtb-patches/PATCH.md`. | Inspected README, CLI wiring/start consumer, job reload/planning, trial agent/verification/finalization/transfer paths, Terminus-2 initial and resumed execution, summarization entry, JSON prompt template, Chat call/history handling, verifier execution, and patch-guide search. Provider implementations, queue internals, viewer/upload consumers, most tests and drop-in implementation remain available, not yet inspected. No claim of parity between the current bundled implementation, historical patch and every installed Harbor version. Unrelated dataset adapters, standalone RewardKit use, training workflows and Harbor website internals are deliberately excluded as independent Harbor uses; this prevents general conclusions about Harbor outside LHTB. |
| `scripts/` | Included: launch, provider smoke/inference, preflight, task-resource maintenance and sandbox cleanup paths. | Read `daytona_cleanup/run_daytona_eval.sh` and `lhtb_harbor_preflight.py`; searched provider and cleanup entry points. Other implementation details remain available. The wrapper explicitly targets a separately installed Harbor version; its responsibilities remain part of the target, but the installation actually used in a historical run is not established. |
| `tasks/` | Included: original task instructions, environment definitions, workload code/data, reference solutions, artifact declarations and hidden evaluators. | Tree inspected across tasks; read `langchain-version-migration/task.toml` as a separate-verifier/artifact-declaration example. Other task internals remain available. The boundary does not establish scientific validity, grading robustness or memory behavior uniformly across tasks. |
| `tasks-2.0/` | Included: additions, public observations/feedback, reconstruction artifacts and private grading/oracle paths. | Read collection README and `acoustic_beamforming_peak__01/{task.toml,tests/test.sh}` as a shared-verifier example; tree inspected across additions. Other task-specific feedback, graders and oracle implementations remain available. Declared image contents are not inspected image evidence. |

### Frozen evidence and dependencies

The sole evidence source is SRC-1 at full Git revision `7ca0cacea9bf6a0694eaad7306bed794eaaaabce`; the checkout HEAD was verified against the acquired pin and its status was clean. The applicability cutoff is **2026-10-15**. Later commits, mutable web pages, the linked paper, upstream Harbor revisions, hosted datasets and unbundled execution traces are outside the frozen source set. The overall tier is **code-grounded** because the entry points and model-dependent continuation/verification consumers are inspectable, not merely described in documentation.

External dependencies include model services, sandbox/container providers, installed agent CLIs, task-specific scientific packages, and container images. Their configuration and invocation code in SRC-1 are included; their independently deployed implementation and service behavior are not. In particular, a digest-pinned image in `tasks-2.0/acoustic_beamforming_peak__01/task.toml` identifies a dependency but is not a captured image. These limits prevent an end-to-end runtime assurance, a claim that hidden material was unreachable in actual runs, or a reproducibility claim about live services. No target code, tests, examples, providers or environments were executed.

The README and `assets/make_figures_2.0.py` supply attributed result summaries and their declared plotting/data-consumption contract. They do not supply an independently inspected causal experiment. The actual leaderboard trajectories linked outside this repository were not acquired, so this boundary does not establish observed model behavior or causal benefits of continuation, summarization or verifier isolation. Available but uninspected source files remain under the same SRC-1 pin; inspecting them later does not require a new repository or revision.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/zli12321/lhtb` | 7ca0cacea9bf6a0694eaad7306bed794eaaaabce | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/lhtb-a0548ba4edbf/related-systems/zli12321--lhtb`. Implementation: CLI entry declaration and routing, job start/reload/planning, trial continuation/artifact transfer/finalization, Terminus-2 model/context entry points, Chat model call, verifier execution, full-suite config, launch/preflight scripts, figure loader and representative shared/separate task contracts. Doctrine/design: `README.md`, `harbor/README.md`, `tasks-2.0/README.md`, Terminus-2 JSON template and searched `harbor/skills/apply-lhtb-patches/PATCH.md`. Reported operation: README leaderboard and run-condition discussion; figure script's declared CSV contract. The coverage table names individual initial reads and uninspected surfaces. | Implementation: [trial loop](https://github.com/zli12321/lhtb/blob/7ca0cacea9bf6a0694eaad7306bed794eaaaabce/harbor/src/harbor/trial/trial.py), [Terminus-2](https://github.com/zli12321/lhtb/blob/7ca0cacea9bf6a0694eaad7306bed794eaaaabce/harbor/src/harbor/agents/terminus_2/terminus_2.py), [job state](https://github.com/zli12321/lhtb/blob/7ca0cacea9bf6a0694eaad7306bed794eaaaabce/harbor/src/harbor/job.py), [full-suite caller](https://github.com/zli12321/lhtb/blob/7ca0cacea9bf6a0694eaad7306bed794eaaaabce/configs/examples/full_benchmark_2.0.yaml). Doctrine/design and reported operation: [README](https://github.com/zli12321/lhtb/blob/7ca0cacea9bf6a0694eaad7306bed794eaaaabce/README.md), [task additions](https://github.com/zli12321/lhtb/blob/7ca0cacea9bf6a0694eaad7306bed794eaaaabce/tasks-2.0/README.md), [figure consumer](https://github.com/zli12321/lhtb/blob/7ca0cacea9bf6a0694eaad7306bed794eaaaabce/assets/make_figures_2.0.py). | No checkout access gap identified. External images, installed runtimes/services and hosted trajectories are not captured; no deployment assurance or independently observed/causal performance conclusion. Initial source coverage is not an exhaustive audit of every task or Harbor integration. |
