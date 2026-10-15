---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Meta-Harness's shipped harness-search workflows, reference runtimes and experimental Harbor pilot at commit 8123ccabe2b19fa1123090b2e5f1bacc20963ce8."
run-id: AAS-2026-10-14-meta-harness-5e480e270fee-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: "8123ccabe2b19fa1123090b2e5f1bacc20963ce8"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/stanford-iris-lab/meta-harness
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/meta-harness-5e480e270fee/related-systems/stanford-iris-lab--meta-harness
  revision: "8123ccabe2b19fa1123090b2e5f1bacc20963ce8"
  sha256: null
---

# Meta-Harness boundary

## Boundary and evidence

This run analyses Meta-Harness as a builder or improvement plane: model-driven search over executable harness code, with retained candidate code, evaluation feedback and execution history used in later proposals. The intended use is to explain the shipped improvement mechanisms and their dependencies, not to reproduce the paper's performance results. The boundary includes both reference experiments and the experimental Harbor pilot. It does not reduce the target to the classification memory API or to the proposer wrapper alone. SRC-1, `README.md`, `reference_examples/text_classification/meta_harness.py`, `reference_examples/terminal_bench_2/meta_harness.py`, `experimental/harbor_meta_harness/agents/meta_harness.py`.

The target qualifies because its shipped drivers invoke a model-based proposer, admit candidate code, evaluate it through model-dependent task solvers, retain feedback and expose that feedback to subsequent proposals. The target's own description is:

> Meta-Harness is a framework for automated search over task-specific model harnesses: the code around a fixed base model that decides what to store, retrieve, and show while the model works. This repo contains the framework and two reference experiments from the paper.
> --- `README.md`

The boundary is **whole-system at the repository revision**, not the whole external execution stack. It covers the shipped onboarding procedure, proposer instructions and wrappers, both search drivers, candidate interfaces and baselines, task-level model invocation, persistence and reload paths, selection/finalization, evaluation adapters, and the pilot's suite preparation and scoring loop. Harbor, Claude Code, provider backends and remote sandboxes remain external dependencies; their internal behavior is not attributed to Meta-Harness. The frozen revision is `8123ccabe2b19fa1123090b2e5f1bacc20963ce8`; the analysis cutoff is 2026-10-14. The evidence tier is code-grounded, with source-native documentation treated separately as declared intent. No target program, test, example or model call was executed.

### Traced shipped loops

**Text classification.** `meta_harness.py` calls its Claude wrapper with the shipped proposer skill and run-specific history paths. It consumes `pending_eval.json`, import-checks candidates and dispatches `benchmark.py`. The benchmark constructs `inner_loop.py` invocations, saves training memory for validation runs and reloads it for test runs. The inner loop instantiates the candidate, learns from labelled training batches, saves state, evaluates requested splits and emits results. The outer driver updates the validation frontier and evolution summary, which subsequent proposer instructions consume. The baseline's `predict`, `learn_from_batch`, `get_state` and `set_state` show that retained memory affects later model inputs; the enclosing benchmark and driver are therefore included, not treated as external clients. SRC-1, `reference_examples/text_classification/meta_harness.py`, `reference_examples/text_classification/benchmark.py`, `reference_examples/text_classification/inner_loop.py`, `reference_examples/text_classification/agents/fewshot_memory.py`.

> # Need saved memory from val run
> --- `reference_examples/text_classification/benchmark.py`

> Path(args.save_memory).write_text(memory.get_state())
> --- `reference_examples/text_classification/inner_loop.py`

> memory.set_state(state)
> --- `reference_examples/text_classification/inner_loop.py`

The proposer-side history consumption is explicitly shipped procedure rather than inferred autonomous behavior:

> Treat `evolution_summary.jsonl`, `frontier_val.json`, and recent training traces as the only shipped history sources in this trimmed repo.
> --- `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`

**Terminal-Bench 2.** The second search driver supplies its proposer skill, consumes candidate import paths, validates the class, optionally smoke-checks it, invokes `scripts/run_eval.sh`, parses Harbor results and trial metrics, and updates the frontier and evolution summary. The optional final pass selects a frontier agent for additional trials on the same full dataset; it is not evidence of a separately held-out test set. The shell adapter validates the agent and dispatches Harbor with the selected environment, model, dataset and attempts. The shipped KIRA baseline subclasses Harbor's Terminus2 and directly calls LiteLLM with tools; its episode loop and prompt template are included. Harbor's inherited machinery and the remote task distribution are external. SRC-1, `reference_examples/terminal_bench_2/meta_harness.py`, `reference_examples/terminal_bench_2/scripts/run_eval.sh`, `reference_examples/terminal_bench_2/agents/baseline_kira.py`, `reference_examples/terminal_bench_2/prompt-templates/terminus-kira.txt`.

> response = await litellm.acompletion(**completion_kwargs)
> --- `reference_examples/terminal_bench_2/agents/baseline_kira.py`

> update_frontier(results)
> --- `reference_examples/terminal_bench_2/meta_harness.py`

**Experimental Harbor pilot.** The outer `AgentHarness` calls a model with terminal and `evaluate_harness` tools. Evaluation downloads the current candidate, invokes `controller.py` in a subprocess, records the result against a finite evaluation budget and feeds the response back into the model conversation. The controller reads the selected suite, checks source syntax/interface and forbidden references, stages candidate code for child Harbor jobs and aggregates their rewards. The outer agent writes and uploads evaluation history; the shipped outer-task verifier reads that history and returns the maximum accepted reward if its budget arithmetic is valid. The default suite's three local tasks, the seed harness, task verifiers, suite files and collection preparation scripts belong to this loop. SRC-1, `experimental/harbor_meta_harness/agents/meta_harness.py`, `experimental/harbor_meta_harness/controller.py`, `experimental/harbor_meta_harness/suite.toml`, `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`, `experimental/harbor_meta_harness/scripts/prepare_collections.py`.

> next_state = state.record(result)
> --- `experimental/harbor_meta_harness/agents/meta_harness.py`

> reward = max(rewards, default=0.0) if valid else 0.0
> --- `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`

### Top-level tracked coverage

Every top-level tracked entry is classified below. Included means part of the functional evidence boundary, not that every byte has already been inspected. The material production, admission, persistence and consumption paths above were inspected as source text. Remaining included fixtures and supporting implementations are available at the same revision for later jobs; they are not access gaps.

| Top-level entry | Included or excluded; role and material paths | Inspection status and conclusion limits |
|---|---|---|
| `.env.example` | Included: provider and sandbox credential/configuration surface. | Inspected; names do not establish credential validity or service availability. SRC-1, `.env.example`. |
| `.gitignore` | Included: repository retention boundary, including ignored jobs, experience and downloaded datasets. | Inspected; ignored content is not supplied run evidence. SRC-1, `.gitignore`. |
| `CITATION.cff` | Excluded from mechanism analysis: citation metadata. | Inspected; no independent assessment of bibliographic claims. SRC-1, `CITATION.cff`. |
| `LICENSE` | Excluded from mechanism analysis: MIT licensing text. | Inspected; this run does not assess legal compliance. SRC-1, `LICENSE`. |
| `ONBOARDING.md` | Included: operator/coding-assistant adaptation procedure, domain specification, data separation, evidence retention and budget instructions. | Inspected in full as doctrine/design; no evidence that a particular adaptation followed it. SRC-1, `ONBOARDING.md`. |
| `README.md` | Included: declared target, entry points, adaptation flow and release limitations. | Inspected in full. External project links are not additional evidence sources. SRC-1, `README.md`. |
| `assets/` | Excluded: `repo.png`, presentation image. | Tree inventoried, image not inspected; prevents assessment of image-only design claims, not executable loop coverage. |
| `reference_examples/` | Included: classification `meta_harness.py`, `benchmark.py`, `inner_loop.py`, `memory_system.py`, `llm.py`, `claude_wrapper.py`, `.claude/skills/meta-harness/SKILL.md`, `agents/`, `config.yaml`, `data/` and `tests/`; terminal `meta_harness.py`, `scripts/run_eval.sh`, `claude_wrapper.py`, `.claude/skills/meta-harness-terminal-bench-2/SKILL.md`, `agents/`, `anthropic_caching.py`, `prompt-templates/`, setup/package files and tests. | Both READMEs and both proposer skills inspected in full; driver, wrapper, classification memory save/reload, baseline prediction/state and terminal baseline model/episode paths inspected in bounded ranges. Remaining provider/cache internals, loaders/evaluators, test bodies, dataset records and setup details are available but not yet fully inspected; no comprehensive correctness or data-quality claim. SRC-1, `reference_examples/text_classification/README.md`, `reference_examples/terminal_bench_2/README.md`. |
| `experimental/` | Included: `harbor_meta_harness/agents/`, `controller.py`, `suite.toml`, `suites/`, `scripts/`, `tasks/` with environments, seeds, instructions, solutions and tests, plus package metadata and `tests/test_controller.py`. | README, outer agent and terminal scaffold inspected in full; suite loading, source admission, staging, child dispatch, result aggregation, collection preparation and outer reward consumer inspected. Default suite and outer Dockerfile inspected. Remaining local task fixtures/verifier bodies and unit-test bodies available but not yet fully inspected. Downloaded collection contents are unavailable in the frozen Git source. SRC-1, `experimental/harbor_meta_harness/README.md`, `experimental/harbor_meta_harness/controller.py`, `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`. |

### Exclusions and evidence limits

- **External optimized harness artifact and paper:** the root and Terminal-Bench READMEs point to a separate optimized-harness repository and paper. Neither is frozen here. This prevents claims about that artifact's actual implementation, paper-result reproduction or the completeness of the paper's experimental history. SRC-1, `README.md`, `reference_examples/terminal_bench_2/README.md`.
- **External execution substrate:** Claude Code supplies proposer execution; Harbor, LiteLLM/model providers and Runloop/Modal supply important task execution services. This boundary supports analysis of shipped invocations and adapters, not provider behavior, inherited Harbor correctness, remote sandbox isolation or operational availability. SRC-1, `reference_examples/text_classification/claude_wrapper.py`, `reference_examples/terminal_bench_2/scripts/run_eval.sh`, `experimental/harbor_meta_harness/controller.py`.
- **Downloaded collections:** pilot fetch/preparation scripts and suite configurations are included, but the downloaded Terminal-Bench, HumanEvalFix and CodePDE payloads are not frozen by this repository pin. This prevents checking their complete tasks, leakage surfaces or reported probe scores from task/run evidence. It does not remove the shipped pilot controller or default local tasks from scope. SRC-1, `experimental/harbor_meta_harness/scripts/fetch_collections.sh`, `.gitignore`.
- **No observed run or causal experiment:** no independently inspectable execution trace or experimental intervention was supplied to this boundary. The pilot README's local probe scores are reported operation only. Unit tests are implementation evidence until executed; no runtime success, measured gain or causal attribution follows from their presence. SRC-1, `experimental/harbor_meta_harness/README.md`.
- **Declared holdout separation is not secrecy:** the classification documentation explicitly distinguishes operational finalization from access control over publicly shipped test data. This prevents interpreting the workflow alone as proof of inaccessible test labels or uncontaminated candidate generation. SRC-1, `reference_examples/text_classification/README.md`.

> The test
> data is included in this public repository, so this is operational isolation,
> not access control.
> --- `reference_examples/text_classification/README.md`

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/stanford-iris-lab/meta-harness` | 8123ccabe2b19fa1123090b2e5f1bacc20963ce8 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/meta-harness-5e480e270fee/related-systems/stanford-iris-lab--meta-harness`. Implementation: both reference search drivers, classification benchmark and memory persistence/consumption paths, proposer wrapper, terminal eval adapter and baseline call/episode paths, pilot outer agent, source admission, child evaluation, suite preparation and outer reward consumer. Doctrine/design: root README, onboarding, both reference READMEs and proposer skills, pilot README and terminal prompt. Reported operation: pilot README probe-score table, without underlying run artifacts. The tracked tree was inventoried, including hidden proposer instructions. | Implementation: [classification driver](https://github.com/stanford-iris-lab/meta-harness/blob/8123ccabe2b19fa1123090b2e5f1bacc20963ce8/reference_examples/text_classification/meta_harness.py), [classification benchmark](https://github.com/stanford-iris-lab/meta-harness/blob/8123ccabe2b19fa1123090b2e5f1bacc20963ce8/reference_examples/text_classification/benchmark.py), [terminal driver](https://github.com/stanford-iris-lab/meta-harness/blob/8123ccabe2b19fa1123090b2e5f1bacc20963ce8/reference_examples/terminal_bench_2/meta_harness.py), [pilot controller](https://github.com/stanford-iris-lab/meta-harness/blob/8123ccabe2b19fa1123090b2e5f1bacc20963ce8/experimental/harbor_meta_harness/controller.py). Doctrine/design: [onboarding](https://github.com/stanford-iris-lab/meta-harness/blob/8123ccabe2b19fa1123090b2e5f1bacc20963ce8/ONBOARDING.md). Reported operation: [pilot README](https://github.com/stanford-iris-lab/meta-harness/blob/8123ccabe2b19fa1123090b2e5f1bacc20963ce8/experimental/harbor_meta_harness/README.md). | No access gap to tracked source. External dependencies, paper, optimized artifact repository, remote datasets and actual search-run artifacts are outside this frozen source; their absence prevents implementation or performance conclusions about those materials. Available but uninspected supporting files are distinguished in the coverage table. No observed-run or causal-experiment layer is claimed. |
