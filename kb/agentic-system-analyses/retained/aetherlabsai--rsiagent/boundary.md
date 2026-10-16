---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "RSIAgent's shipped exploration, memory-learning and benchmark-execution runtime at commit 4d7ef43770dda341fccd9a5743db92407687c615."
run-id: AAS-2026-10-14-rsiagent-b11225763c0b-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "4d7ef43770dda341fccd9a5743db92407687c615"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/AetherLabsAI/RSIAgent
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/rsiagent-b11225763c0b/related-systems/AetherLabsAI--RSIAgent
  revision: 4d7ef43770dda341fccd9a5743db92407687c615
  sha256: null
---

# RSIAgent boundary

## Boundary and evidence

This run examines how the shipped RSIAgent framework coordinates model-driven task execution, verification, curriculum selection, persistent learning and later frozen-memory use. The target is in scope as an **enclosing runtime**, not merely a memory API or an improvement component embedded in an unexamined application. Its root drivers launch the benchmark phases; those phases supply environments and connect the shared agent loop to memory publication and subsequent task execution. These shipped drivers and adapters belong to the target, even where they delegate environment provisioning or official grading to external benchmark packages (SRC-1, `run_osworld.py`, `run_ale.py`, `benchmarks/osworld/pipeline.py`, `benchmarks/ale/host.py`, `benchmarks/ale/worker.py`).

The authors describe the intended scope as follows:

> RSIAgent is a **training-free framework for recursive self-improvement** in new
> digital environments. It coordinates the Curriculum Agent, Actor Agent, and
> Verifier Agent to discover how an environment works, check what they learn against actual execution,
> and retain reusable knowledge in persistent memory. Model parameters stay fixed
> throughout exploration and downstream task execution.
> --- `README.md`

Implementation inspection supports the runtime classification rather than relying on that description alone. The generic target loop constructs a fresh environment, Verifier and Actor, calls work and verification hooks, and passes learned memory forward. Both benchmark integrations connect to that machinery. The model client issues completion requests; this is not a collection of static prompts awaiting an unspecified external agent (SRC-1, `core/self_evolving_loop.py`, `benchmarks/osworld/phase2.py`, `benchmarks/ale/learning.py`, `llm/client.py`).

>             actor = hooks.fresh_target_actor(memory, target_cycles)
> --- `core/self_evolving_loop.py`

>             resp = _c().chat.completions.create(model=model, messages=messages,
>                                                 max_tokens=max_tokens, temperature=temperature, **kwargs)
> --- `llm/client.py`

The **whole-system** boundary includes the two public benchmark drivers, their orchestration and host/worker separation, the shared Actor/Verifier runtime, guest transport and rollback support, curriculum and practice loops, prompt-based memory maintenance, host-side memory admission and journaling, recovery admission, and frozen-memory consumers. It also includes shipped configuration, preparation, evaluation adapters and portable tests as source evidence. This is a functional whole-system boundary, not a claim that every function or test was read or that all branches were exercised.

The memory loop is materially present within this repository. Phase 1 branches resume the same Actor to distill and reconcile experience, audit the candidate tree, journal it and install it in canonical memory. Phase 2 learning similarly connects terminal outcomes to distillation, reconciliation and publication. The shared installer stages a complete tree before replacing the durable directory. Phase 3 copies frozen memory, records no writeback or curriculum, and checks the frozen host tree after execution. The task consumers upload that memory and expose an inventory through the shipped retrieval prompt (SRC-1, `explore/phase1_wave.py`, `explore/target_learning.py`, `explore/practice_loop.py`, `explore/charter.py`, `benchmarks/osworld/pipeline.py`, `benchmarks/osworld/task.py`, `benchmarks/ale/worker.py`).

>     hooks.journal_memory(
>         str(journal_dir), branch.project_index, accepted,
>         {"kind": "phase1-parallel-terminal-memory",
>          "terminal_outcome": branch.terminal_outcome})
>     hooks.install_memory(str(canonical_memory_dir), accepted)
> --- `explore/phase1_wave.py`

Maintenance instructions and retrieval instructions are included, not treated as incidental documentation:

> Inventory the complete current durable-memory tree at {memory_root} and inspect
> every claim-bearing file. Reconcile the corpus as a whole against the trajectory
> and final Verifier evidence already in context.
> --- `explore/charter.py`

> First understand the task, then inspect memory as you judge useful: you may list,
> search across, preview, re-read, or fully read files in any order.
> --- `explore/charter.py`

These passages establish instructed behavior and its integration points, not proof that a model follows those instructions or that resulting memory is correct.

### Repository coverage

Every top-level tracked file or directory is classified below. Paths and roles are from SRC-1. “Included” means within the functional evidence boundary; initial inspection can be a bounded code read, an import/call-site search, or tree inventory as specified. Files not yet read are not access gaps and remain available at this same pin. No material shipped loop responsibility is deliberately excluded.

| Top-level path | Classification and material paths | Initial inspection and limits |
| --- | --- | --- |
| `.env.example` | Included: credential and path configuration surface. | Read; credentials themselves are external and unavailable. |
| `.github/` | Included: `.github/workflows/tests.yml` portable validation and CLI checks. | Read; workflow execution results not supplied. |
| `.gitignore` | Excluded: checkout hygiene. | Tree inventory only; no conclusion about ignored local artifacts or secret-handling completeness. |
| `.python-version` | Included: interpreter selection metadata. | Inventoried, not read; no interpreter-compatibility conclusion from it. |
| `LICENSE` | Excluded: legal terms. | Inventoried, not assessed; no licensing conclusion. |
| `README.md` | Included: system purpose, public entrypoints, installation, runtime phases and reported results. | Read in full; results remain author reports, not reproduced measurements. |
| `benchmarks/` | Included: OSWorld `pipeline.py`, `phase1.py`, `phase2.py`, `task.py`, `actor_boundary.py`, runtime/provider and evaluator adapters; ALE `host.py`, `worker.py`, `learning.py`, `protocol.py`, `report.py`, practice, preparation, transport and platform adapters. | Traced root drivers to phases, learning, frozen-memory consumers and grading handoff. Read selected pipeline, task, host and learning regions and the full worker; searched phase and protocol entrypoints. Remaining adapter details are not yet inspected, not externalized responsibilities. |
| `config/` | Included: `settings.py`, `runtime_paths.py`, `benchmark_runtime.py`, `roles/`, OSWorld/ALE locks, query inputs and study configuration. | Read `roles/actor.yaml` and `osworld/rsi.example.json`; searched settings/path APIs and role memory settings; inventoried locks and remaining profiles. No claim that all configurations are equivalent. |
| `core/` | Included: `loop.py`, `actor.py`, `verifier.py`, `verifier_runtime.py`, `self_evolving_loop.py`, tracing, checks, visual observation, baseline and grading helpers. | Read the central target-loop region; searched Actor/Verifier APIs and memory-related loop integration. Full action/verification edge cases remain for later inspection. |
| `docs/` | Included: `ARCHITECTURE.md`, `OPERATIONS.md` and source-native guides, provenance and reporting documents. | Architecture and operations read in full. Other guides, `RSIAgent.pdf` and visual assets inventoried but not inspected. No figure interpretation, manuscript audit or reported-score verification is claimed. |
| `env/` | Included: `vm.py`, `qemu_rollback.py`, `verifier_control.py`, `controller_oom.py`. | Searched transport/control/rollback APIs and read rollback scope declarations. No live isolation or recovery guarantee established. |
| `explore/` | Included: `charter.py`, `phase1_wave.py`, `practice_loop.py`, `unified_evolution.py`, `target_learning.py`, `commit.py`, hashing, provisioning, isolation, recovery modules and practice fixtures. | Read retrieval/maintenance prompts, publication and installer regions, complete `commit.py`, and selected recovery admission code; searched routing and recovery entrypoints. Remaining recovery variants and fixture bodies are not yet inspected. |
| `llm/` | Included: `client.py` provider requests, history/image handling and transport recovery. | Read request construction and provider-call region; searched client APIs. No provider operation observed. |
| `pytest.ini` | Included: test-run configuration. | Inventoried, not read; no collection or marker claim. |
| `requirements-dev.txt` | Included: development/test dependency metadata. | Inventoried, not read; not installed. |
| `requirements.txt` | Included: pinned host dependencies. | Read; external package implementations are not registered sources. |
| `run_ale.py` | Included: public preparation, smoke, planning, execution and reporting dispatch. | Read in full; traced to ALE host/worker and learning paths. |
| `run_osworld.py` | Included: batch planner and executor for baseline and RSI phases. | Read in full; traced to task and pipeline modules. |
| `scripts/` | Included: `run_rsi.sh` phase driver and `setup_ale.py` environment setup. | Wrapper read in full; setup script inventoried, not read. No environment installation performed. |
| `tests/` | Included: portable regression specifications covering memory, isolation, learning, recovery, transport and release paths. | Tree inventoried; read retrieval-lifecycle test region. No tests executed and no suite-pass claim. |
| `tools/` | Included: release checks, benchmark preparation, corpus/fence production, smoke tools and `recover_phase1_wave.py`. | Read `check_rsi_release.py`; searched recovery entrypoints; inventoried preparation/fence tools and inspected the memory audit's call into `exam_fence.py`. Detailed tool internals remain available for later inspection. |

### External boundary and evidence limits

The reviewed revision is **4d7ef43770dda341fccd9a5743db92407687c615**, with applicability cutoff **2026-10-14**. The acquired checkout's HEAD matches that revision and its working-tree status was clean when inspected. The source mapping is copied unchanged from acquisition. Only the registered Git object supplies evidence; later upstream changes and live linked pages are outside this run.

External dependencies include the separately installed OSWorld-V2 and Agents' Last Exam implementations and assets, Docker/QEMU/KVM and guest images, model providers and credentials, and task websites or remote services. The shipped wrappers, configuration checks, VM adapters and evaluator handoffs are included; the internals and actual availability of those external dependencies are not. This prevents conclusions about official evaluator correctness, complete benchmark reproduction, provider reliability or end-to-end execution success. Repository instructions and dependency pins are evidence of expected integration, not inspected upstream implementations (SRC-1, `README.md`, `docs/OPERATIONS.md`, `requirements.txt`, `benchmarks/ale/host.py`, `benchmarks/osworld/task.py`).

Remote effects are not automatically within a guest rollback boundary. The source explicitly limits that scope:

> External
> services outside the QEMU guest are not covered by this transaction. Provider
> launch adaptation belongs to the host harness, not this generic VM boundary.
> --- `env/qemu_rollback.py`

The overall tier is **code-grounded**: selected executable control and state paths were inspected. Source-native architecture and prompts additionally supply doctrine/design, and README performance numbers supply reported operation only. No target code, examples, tests or model calls were executed. No independently inspectable run trace or intervention/comparison artifact was supplied or inspected, so the boundary establishes neither observed operation nor causal improvement. Uninspected source files are available evidence for later jobs, not a reason to substitute an unavailable enclosing host or omit shipped consumers.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/AetherLabsAI/RSIAgent` | 4d7ef43770dda341fccd9a5743db92407687c615 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/rsiagent-b11225763c0b/related-systems/AetherLabsAI--RSIAgent`. Implementation: root drivers, selected OSWorld pipeline/phase/task and ALE host/worker/learning paths, target-loop hooks, memory promotion/install/transport/audit, and recovery admissions; bounded API searches and tracked-tree inventory as detailed above. Doctrine/design: complete README, architecture and operations; selected retrieval and maintenance charters and study/role configuration. Reported operation: README aggregates, not reproduced. | Implementation: [batch entrypoint](https://github.com/AetherLabsAI/RSIAgent/blob/4d7ef43770dda341fccd9a5743db92407687c615/run_osworld.py), [phase orchestration](https://github.com/AetherLabsAI/RSIAgent/blob/4d7ef43770dda341fccd9a5743db92407687c615/benchmarks/osworld/pipeline.py), [ALE worker](https://github.com/AetherLabsAI/RSIAgent/blob/4d7ef43770dda341fccd9a5743db92407687c615/benchmarks/ale/worker.py), [memory publication](https://github.com/AetherLabsAI/RSIAgent/blob/4d7ef43770dda341fccd9a5743db92407687c615/explore/target_learning.py). Doctrine/design: [architecture](https://github.com/AetherLabsAI/RSIAgent/blob/4d7ef43770dda341fccd9a5743db92407687c615/docs/ARCHITECTURE.md), [charters](https://github.com/AetherLabsAI/RSIAgent/blob/4d7ef43770dda341fccd9a5743db92407687c615/explore/charter.py). Reported operation: [README](https://github.com/AetherLabsAI/RSIAgent/blob/4d7ef43770dda341fccd9a5743db92407687c615/README.md). | No checkout access gap encountered. External benchmark/provider/service implementations and live runtime evidence are not frozen here; prevents upstream correctness, execution-success and causal performance conclusions. Initial uninspected files remain available under this registered commit; excluded legal/hygiene surfaces do not support legal or local-artifact conclusions. |
