---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "EAL-Bench's shipped authorization-memory evaluation workflow at commit 51648690bc52d7a9c7ac080a2c67a784fe9d56cb."
run-id: AAS-2026-10-15-eal-bench-f9a76e2fa858-01
result-disposition: complete
target-class: workflow
boundary-kind: whole-system
reviewed-boundary: "51648690bc52d7a9c7ac080a2c67a784fe9d56cb"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/tommasocerruti/eal-bench
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-eal-bench/related-systems/tommasocerruti--eal-bench
  revision: "51648690bc52d7a9c7ac080a2c67a784fe9d56cb"
  sha256: null
---

# EAL-Bench boundary

## Boundary and evidence

EAL-Bench is an in-scope **workflow** for evaluating whether model-written persistent memory changes authorization and whether an executor acts on those changes. Its intended use is research evaluation, not deployment as an organization's authorization service. The boundary is the **whole shipped system**, including experiment drivers, memory admission and persistence, subsequent consumption, domain semantics, mitigation paths, reusable evaluation interfaces and result analysis. It is not restricted to the public scoring API. SRC-1, `README.md`, `domains/README.md`, `pyproject.toml` and `docs/reusable_api.md` establish this use and packaging.

> A memory writer compresses an organizational history into persistent memory; an executor later receives that memory and a new request, then chooses whether to act through a native tool.
> --- `README.md`

The classification depends on model calls issued by the shipped workflow, not merely on an external consumer using a library. The main driver dispatches domain study plans; the shared engine calls the writer, freezes a pre-execution checkpoint and calls executors over prepared evidence. It then persists memories, attempts, states, evidence, trials and model contexts. The executor batch path submits model-visible tools and scores returned calls. These responsibilities are internal to EAL-Bench (SRC-1, `experiments/run.py`, `experiments/authorization_memory/study_engine.py`, `experiments/authorization_memory/pipeline.py`).

> """Run and persist a domain-built study through shared infrastructure."""
> --- `experiments/authorization_memory/study_engine.py`

Memory production and admission are included. The LangMem wrapper assembles instructions from domain policy, maintains a single profile, parses candidates, checks visible provenance identifiers and capacity, and distinguishes accepted, unchanged and invalid candidates. It freezes the accepted artifact into executor evidence. This is a bounded benchmark memory protocol, not evidence of a general-purpose retrieval service (SRC-1, `experiments/authorization_memory/langmem_writer.py`).

> "Maintain exactly one persistent profile containing current authorization state.",
> "Update the existing profile from the supplied information; do not create another profile.",
> --- `experiments/authorization_memory/langmem_writer.py`

The included consumption paths extend beyond one immediate replay. Checkpoint resume reconstructs saved execution state and schedules missing executor calls. Pressure and mitigation studies reuse saved writer runs. The shipped closed-loop driver starts from frozen base memories, executes requests, constructs action or neutral write-back blocks, seeds subsequent writer updates with the current artifact, and uses the resulting memory for later requests. Thus write-back is not assigned to an excluded host (SRC-1, `experiments/authorization_memory/resume.py`, `experiments/mitigations/README.md`, `experiments/closed_loop.py`).

> # 1. The paper's incremental chains, then the open loop on their frozen memories.
> --- `experiments/closed_loop.py`

The reusable interface supplies trial construction, preservation assessment, propagation comparisons, end-to-end attribution, export and scoring. Its scorer delegates to the internal runner's scorer. The Inspect adapter is a shipped integration, while Inspect itself and arbitrary downstream applications remain external. An external caller's model routing or storage is not attributed to EAL-Bench. The repository's own experiment runner remains included even where the public API lets a caller supply responses (SRC-1, `src/eal_bench/eval/__main__.py`, `src/eal_bench/eval/scoring.py`, `pyproject.toml`, `docs/reusable_api.md`).

> The adapter supplies the dataset, the tools and the scorer. The model and its configuration stay
> yours.
> --- `docs/reusable_api.md`

### Frozen evidence and applicability

The evidence is SRC-1 at full commit `51648690bc52d7a9c7ac080a2c67a784fe9d56cb`, with applicability cutoff **2026-10-15**. The checkout HEAD matches the acquired revision and its working tree was clean at inspection. The overall tier is **code-grounded**: entry-point dispatch, writer admission, persistence, executor consumption, resume, closed-loop write-back, mitigation cores and public scoring delegation were inspected as source text. No target code, tests, examples, provider calls or experiments were executed. Code inspection supports implemented paths, not successful live operation or benchmark validity.

External dependencies include LangMem and its LangChain integrations for the writer, OpenAI-compatible provider clients, configured model services, Pydantic, JSON patching and token counting; Inspect is optional. Their implementations, provider state, credentials and actual model behavior are not frozen here. The supplied repository includes dependency declarations and route-client code, not those external systems' internals. This prevents conclusions about external transport guarantees, model reliability or deployed authorization enforcement (SRC-1, `pyproject.toml`, `src/eal_bench/llm/client.py`, `docs/reusable_api.md`). The linked arXiv paper and linked external websites are not additional sources.

Historical results require a separate limit. The primary result guide says original trial, memory and provider-context JSONL files are not distributed in the normal clone, and the paper exporter can use saved counts while reporting absent originals. Some diagnostic JSONL files are tracked under `results/diagnosis/`; their presence does not supply the primary run archives. No raw archive was acquired. This prevents independent reconstruction and rescoring of the primary published runs or their bootstrap inputs from this boundary alone. Repository reports remain attributed reported operation unless later inspection establishes an actual trace or intervention with adequate conditions (SRC-1, `results/README.md`, `analysis/paper_results.py`).

> Missing raw files prevent independent scoring and reconstruction of bootstrap inputs. New model
> runs are stochastic replications and cannot replace original records.
> --- `results/README.md`

### Top-level coverage

Every tracked top-level entry is classified below. “Included” declares functional scope, not that every file has already been read. Initial inspection is stated explicitly; an available but unread file is not an access gap. Later jobs may inspect additional paths at this same registered commit. No shipped state-producing or state-consuming path is deliberately excluded.

| Top-level entry | Classification and role | Initial inspection and limits |
|---|---|---|
| `README.md` | Included: purpose, protocol, entry points and evidence limits | Read; doctrine/design, not proof of outcomes. |
| `USAGE.md` | Included: operator use of evaluation tracks | Located, not yet inspected; no independent behavioral claim rests on it. |
| `MODELS.md` | Included: model/provider configuration guidance | Located, not yet inspected; external provider behavior is not established. |
| `pyproject.toml` | Included: dependencies, packaged domains/experiments/analysis and Inspect registration | Read; confirms these are shipped responsibilities rather than excluded callers. |
| `config.yaml` | Included: repository route and task configuration | Located, not yet inspected; no specific target-route capability is asserted. |
| `src/` | Included: `eal_bench/llm/` transport/configuration/logging and `eal_bench/eval/` trial builders, memory scoring, replay attribution, resource identity, exports, reference fixtures and Inspect adapter | Read client construction/preflight, evaluation CLI and scoring delegation; traced evaluation and Inspect definitions and read reusable-interface contract. Reference artifacts and remaining implementations are available for later inspection, not observed runs established by this boundary. |
| `experiments/` | Included: `run.py`, `extension_cli.py`, `authorization_memory/` study plans/engine, writer, admission, surfaces, persistence, provenance, resume and validation; `closed_loop.py`, writer variants and diagnosis; `mitigations/` source-authority gating and event extraction/reduction | Inspected main dispatch, study execution/checkpoint/persistence, writer instructions/admission/freezing, executor batch consumption, persistence helpers, checkpoint resume and closed-loop updates. Read mitigation guide and gate/reducer cores. Other study builders and validation fixtures remain available, not exhaustively inspected. |
| `domains/` | Included: `base.py`, shared toolkit/source-authority/event-sourcing contracts; Procurement, Cybersecurity and Finance adapters, corpora/data, presentations, prompts, semantics/oracles, release/review/calibration and maintenance/compilation procedures | Read domain contract and Procurement executor prompt/oracle delegation; searched all three adapters and Procurement study prompts for responsibilities. Concrete corpus and semantic details require later source inspection; they are not excluded. Shipped maintenance instructions belong to the workflow, not a separate host. |
| `analysis/` | Included: `paper_results.py`, shared loaders, memory fidelity/failure analysis, propagation and intervention summaries, mitigation/closed-loop analysis, replication and plots | Inspected paper export's manifest/hash/count/raw-availability handling; other modules located but not yet inspected. No independent validation of the published statistical claims is asserted. |
| `results/` | Included: per-domain manifests/counts/reports, mitigation and extension snapshots, closed-loop analyses, diagnosis artifacts and figures | Read shared result guide and inventoried tracked paths; historical reports and individual artifacts not yet substantively inspected. Missing primary raw archives are an evidence gap, not exclusion of the evaluator. |
| `docs/` | Included: reusable API, extensions and reproduction contracts | Read `reusable_api.md`; other guides located, not yet inspected. |
| `examples/` | Included: `llm_calls.py`, an illustrative provider-client consumer | Located, not yet inspected; no example execution or correctness claim. |
| `judge.py` | Included: auxiliary model-based choice extraction helper | Read; not substituted for the deterministic authorization scorer. |
| `assets/` | Included: `figures/eal-bench-system-overview.png`, explanatory artwork | Located, not inspected; no mechanism claim depends on the image. |
| `.env.example` | Included: credential-configuration template | Located, not inspected; no credentials or provider access acquired. |
| `.gitattributes` | Excluded: Git presentation/attribute metadata | Deliberate exclusion; prevents conclusions about attribute-driven checkout transformations, not the memory loop. |
| `.gitignore` | Included: artifact-retention configuration | Located, not read; raw-availability limits above rely on the result guide and tracked-tree inventory, not inferred ignore behavior. |
| `.python-version` | Included: environment version hint | Located, not read; dependency compatibility is not verified. |
| `uv.lock` | Included: dependency-resolution artifact | Located, not read; no installed-version or supply-chain audit is claimed. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/tommasocerruti/eal-bench` | 51648690bc52d7a9c7ac080a2c67a784fe9d56cb | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-eal-bench/related-systems/tommasocerruti--eal-bench`. Implementation: bounded sections of `experiments/run.py`, `experiments/authorization_memory/study_engine.py`, `experiments/authorization_memory/runner.py`, `experiments/authorization_memory/langmem_writer.py`, `experiments/authorization_memory/pipeline.py`, `experiments/authorization_memory/persistence.py`, `experiments/authorization_memory/resume.py`, `experiments/closed_loop.py`, `experiments/mitigations/source_authority/gate.py`, `experiments/mitigations/event_sourcing/core.py`, `src/eal_bench/eval/__main__.py`, `src/eal_bench/eval/scoring.py`, `src/eal_bench/llm/client.py`, `domains/procurement/adapter.py`, `analysis/paper_results.py` and `judge.py`; repository tree and scoped definition searches. Doctrine/design: `README.md`, `pyproject.toml`, `domains/README.md`, `docs/reusable_api.md`, `experiments/mitigations/README.md`, `results/README.md`. | Implementation: [study engine](https://github.com/tommasocerruti/eal-bench/blob/51648690bc52d7a9c7ac080a2c67a784fe9d56cb/experiments/authorization_memory/study_engine.py), [writer](https://github.com/tommasocerruti/eal-bench/blob/51648690bc52d7a9c7ac080a2c67a784fe9d56cb/experiments/authorization_memory/langmem_writer.py), [closed loop](https://github.com/tommasocerruti/eal-bench/blob/51648690bc52d7a9c7ac080a2c67a784fe9d56cb/experiments/closed_loop.py), [scoring](https://github.com/tommasocerruti/eal-bench/blob/51648690bc52d7a9c7ac080a2c67a784fe9d56cb/src/eal_bench/eval/scoring.py). Doctrine/design: [README](https://github.com/tommasocerruti/eal-bench/blob/51648690bc52d7a9c7ac080a2c67a784fe9d56cb/README.md), [result limits](https://github.com/tommasocerruti/eal-bench/blob/51648690bc52d7a9c7ac080a2c67a784fe9d56cb/results/README.md). | Primary historical raw run archives not supplied: cannot independently rescore those runs or reconstruct missing bootstrap inputs. External dependencies/services and arXiv paper not captured: cannot establish their internals or live behavior. No observed execution or causal experiment is established by this initial inspection; historical result claims require artifact-specific examination. Available but unread source paths remain inspectable under SRC-1. |
