---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Reflexion's shipped task-specific experiment workflows at commit 218cf0ef1df84b05ce379dd4a8e47f17766733a0, with unavailable Git-linked search and evaluation dependencies."
run-id: AAS-2026-10-14-reflexion-19159b69b712-01
result-disposition: complete
target-class: workflow
boundary-kind: complete artifact, partial loop
reviewed-boundary: "218cf0ef1df84b05ce379dd4a8e47f17766733a0"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/noahshinn/reflexion
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/reflexion-19159b69b712/related-systems/noahshinn--reflexion
  revision: "218cf0ef1df84b05ce379dd4a8e47f17766733a0"
  sha256: null
---

# Reflexion boundary

## Boundary and evidence

This run analyses Reflexion as shipped experiment workflows for repeated model-dependent task attempts, feedback, self-reflection and subsequent attempts. The intended use is to characterize their control and retained-state mechanisms, not to certify the paper's results or the behavior of a later deployment. The target class is **workflow**: the repository supplies task-specific drivers and agents rather than a single general-purpose agent service. Its own description establishes the research-artifact context (SRC-1, `README.md`):

> This repo holds the code, demos, and log files for [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) by Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao.
> --- `README.md`

The functional boundary includes all four shipped task families: ALFWorld, HotPotQA, programming and WebShop. It includes their launch scripts or notebooks, agent/model adapters, prompt construction, reflection production, feedback/evaluation code, retained-state writes, reload/resume paths and result consumers. Shipped drivers are part of the target, not excluded host applications. For example, ALFWorld's driver owns the transition from trial execution to reflection updates and persistent environment configuration (SRC-1, `alfworld_runs/main.py`):

> # run trial
> run_trial(trial_log_path, world_log_path, trial_idx, env_configs, args.use_memory, args.model)
>
> # update memory if needed
> if args.use_memory:
>     env_configs: List[Dict[str, Any]] = update_memory(trial_log_path, env_configs)
>
> # log env configs for trial
> with open(trial_env_configs_log_path, 'w') as wf:
>     json.dump(env_configs, wf, indent=4)
> --- `alfworld_runs/main.py`

HotPotQA's three notebooks construct the agents, retry questions and save logs and serialized agents; they are included alongside `hotpotqa_runs/agents.py` and `hotpotqa_runs/util.py`. Programming's CLI dispatches simple, Reflexion, immediate-reflexion, immediate-refinement, Reflexion-UCS and test-accuracy strategies; the implemented strategy selection, not just the README's examples, defines that branch's scope (SRC-1, `programming_runs/main.py`). WebShop includes its shipped HTTP environment client, trial runner and memory/logging driver; storing reflections in its history object does not by itself establish that its action-model prompt consumes them (SRC-1, `webshop_runs/webshop_trial.py`). Later mechanism analysis must trace the actual consumption path separately for each family.

The boundary kind is **complete artifact, partial loop**. The full parent repository revision is frozen and available, but two material shipped integration paths terminate in empty Git-linked dependency directories. The tree records `programming_runs/lazzzy` at gitlink commit `404c06a5bf6201596b45d28f092aefe017306cd9` and `programming_runs/executors/leetcode_env` at `228163abdc983712bebfd8e26f7e7d360830e648`. Those are dependency pointers, not additional registered sources. No dependency checkout was acquired or inspected. The declared repositories are visible in SRC-1, `.gitmodules`:

> [submodule "programming_runs/lazzzy"]
> 	path = programming_runs/lazzzy
> 	url = https://github.com/GammaTauAI/lazzzy
> [submodule "programming_runs/executors/leetcode_env"]
> 	path = programming_runs/executors/leetcode_env
> 	url = https://github.com/GammaTauAI/leetcode-hard-gym
> --- `.gitmodules`

The UCS strategy imports its search driver from the former dependency (SRC-1, `programming_runs/reflexion_ucs.py`):

> from lazzzy.ucs import ucs
> --- `programming_runs/reflexion_ucs.py`

Its callback construction can be analysed, but the missing search implementation prevents a complete account of UCS scheduling and termination. The latter dependency supplies LeetCode environment, submission and formatting APIs referenced by the executor factory and evaluation scripts; its absence prevents a complete account of remote submission, grading and formatting semantics (SRC-1, `programming_runs/executors/factory.py`, `programming_runs/evaluate_leet_results.py`, `programming_runs/evaluate_rs_leet_results.py`). These limits do not block analysis of the parent repository's ordinary reflection loops.

### Repository coverage

The table classifies every top-level tracked entry. “Included” establishes functional scope, not a claim that every file has already been inspected. Paths not yet inspected remain available to subsequent source-grounded jobs at the same revision.

| Top-level entry | Inclusion and material paths | Initial inspection and limits |
|---|---|---|
| `.gitignore` | Excluded: repository housekeeping. | Not inspected; no conclusion about ignored-file policy. No task-loop responsibility attributed to it. |
| `.gitmodules` | Included: dependency declarations for programming search and LeetCode integration. | Inspected with Git tree pointers; dependency contents unavailable as explained above. |
| `LICENSE` | Excluded: licensing text. | Not inspected; no licensing assessment. |
| `README.md` | Included: declared purpose, task entry points, strategy vocabulary and reported log locations. | Read completely; statements are author declarations, not independent verification. External paper, blog and alternative implementations are excluded; no claims about their contents. |
| `alfworld_runs/` | Included: `run_reflexion.sh`, `run_simple.sh`, `main.py`, `alfworld_trial.py`, `generate_reflections.py`, `env_history.py`, `utils.py`, `base_config.yaml`, `prompts/`, `reflexion_few_shot_examples.txt`, requirements and `root/` results. | Driver, trial, reflection generator and history read; launch scripts searched. Prompt/configuration/helper contents and stored result JSON not yet inspected. Covers persistence, resume, reflection admission, action consumption and trial evaluation as source responsibilities, not observed success. |
| `hotpotqa_runs/` | Included: all three `notebooks/` entry points, `agents.py`, `prompts.py`, `fewshots.py`, `llm.py`, `util.py`, alternate `react.py`/`environment.py`, `tests.py`/`mocks.py`, `data/`, requirements and `root/` results. | Notebook code cells, agent implementation and logging/serialization utility read; alternate implementation and prompts searched. Examples, wrappers, dataset and stored results not yet read in detail. Notebook output cells are not used as observed-run evidence here. Serialization is included; no reload consumer is presumed merely from saved files. |
| `programming_runs/` | Included: `main.py`, all `run_*.sh` launchers and six dispatched strategies; `generators/`, `executors/` and cargo harness; `utils.py`; validation/evaluation scripts; dataset creation/sampling/sorting utilities, `benchmarks/`, vendored `human-eval/`, requirements and `root/` results. | CLI, ordinary Reflexion loop, factories and resume/logging utility read; variant strategies, generators, executors and result validators/evaluators searched. Detailed alternate algorithms, vendored evaluator, dataset utilities, benchmark data and saved results remain uninspected. Git-linked dependencies are unavailable, not deliberately excluded. This prevents the whole-system classification. |
| `figures/` | Excluded: explanatory diagrams and illustrations. | Not inspected; no mechanism or performance conclusion based on images. |
| `webshop_runs/` | Included: `run_base.sh`, `run_reflexion.sh`, `main.py`, `webshop_trial.py`, `generate_reflections.py`, `env_history.py`, `utils.py`, `base_prompt.txt`, reflection examples and all base/reflexion result directories. | Driver, full trial/client implementation and reflection generator read; launch scripts searched. History helper, prompt/example contents and saved JSON remain uninspected. Client-side control and persistence are in scope; server implementation is not supplied. |

All source-dependent coverage above refers to SRC-1 and its commit-relative paths. External execution dependencies include model-provider services and model weights, LangChain/Wikipedia retrieval, the ALFWorld environment and data, the WebShop HTTP server, Python/Rust execution facilities and the two Git-linked programming dependencies. The repository's adapters are included; dependency internals and live service state are excluded or unavailable. Consequently this analysis cannot establish provider output behavior, live retrieval contents, environment/server correctness, deployment availability or secure isolation of generated code merely from these adapters (SRC-1, `alfworld_runs/alfworld_trial.py`, `hotpotqa_runs/agents.py`, `webshop_runs/webshop_trial.py`, `programming_runs/generators/model.py`, `programming_runs/executors/py_executor.py`, `programming_runs/executors/rs_executor.py`).

The frozen revision is `218cf0ef1df84b05ce379dd4a8e47f17766733a0`, verified as the acquired checkout's HEAD. The applicability cutoff is **2026-10-14**, the supplied run date, not a claim about the commit's publication date. Overall evidence is **code-grounded**: source text establishes implemented paths; documentation supplies declared intent. No target code, examples or tests were executed. Tracked logs and serialized results are within the frozen parent source but have not been examined as run evidence in this boundary. Their presence and the README's description do not establish a reproduced performance result or causal benefit from reflection.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/noahshinn/reflexion` | 218cf0ef1df84b05ce379dd4a8e47f17766733a0 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/reflexion-19159b69b712/related-systems/noahshinn--reflexion`. Implementation: parent Git tree; ALFWorld driver/trial/reflection/history; WebShop driver/trial/reflection; HotPotQA notebook code cells, agents and serialization; programming CLI, Reflexion loop, factories and resume/logging utilities. Bounded source searches: launchers, strategy variants, programming generation/execution/evaluation modules, alternate HotPotQA environment/agent implementation and prompts. Doctrine/design: complete README and dependency declarations. | Implementation: [ALFWorld driver](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/main.py), [HotPotQA agents](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/agents.py), [programming driver](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/main.py), [WebShop trial](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/webshop_trial.py). Doctrine/design: [README](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/README.md), [dependency declarations](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/.gitmodules). | Implementation: empty `programming_runs/lazzzy` and `programming_runs/executors/leetcode_env` gitlink directories prevent complete UCS search and LeetCode evaluation accounts. External providers/environments are not frozen here; no conclusion about their internals or present operation. Available but uninspected paths are distinguished in the coverage table, not treated as access gaps. Doctrine/design: author descriptions cannot establish operational or causal results. No observed-run or causal-experiment layer claimed in this boundary. |
