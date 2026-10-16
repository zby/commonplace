---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "AI Agents in Depth's Experiment 9-6 campaign: failure diagnosis, coding-model handoff, candidate rejection and delivery of evidence rather than an installed successor."
run-id: AAS-2026-10-12-ai-agent-book-d56e8121d636-01
reviewed-boundary: "dbc046eb896ac4e39aa19c7774c8bf49583b89a6"
---

# AI Agents in Depth workflow report

## Workflow account

### Selection and evidence

The representative workflow is the retry-policy campaign launched by `chapter9/self-modifying-agent/run_experiment_9_6.py`. It is selected because one shipped driver connects diagnosis, a rejected control, a coding-model proposal, software verification and artifact delivery. It does not join unrelated chapter capabilities. The suite has separate experiments, not an established common scheduler; this workflow is one bounded experiment within the [boundary](boundary.md#boundary-and-evidence). Its existing identity is [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate), with evaluation in [RT-RTE-candidate-validation](runtime.md#rt-rte-candidate-validation).

All findings use SRC-1 at the reviewed commit. Added inspection covers the complete campaign driver, `chapter9/self-modifying-agent/evolution.py`, `chapter9/self-modifying-agent/llm_generator.py`, `chapter9/self-modifying-agent/candidate_sandbox.py` and `chapter9/self-modifying-agent/sandbox_runner.py`. These supply implementation evidence only. No target code or provider was executed, and no retained campaign results were inspected. Thus this account establishes coordination wiring, not that a model proposal passed, that a campaign completed, or that later operation improved. Stable-source and supplied-trajectory contents rely on the runtime's bounded account rather than fresh inspection here.

### 1. Human launch and host-owned diagnosis

The human requests the campaign by launching the driver and can choose provider, model, seed and output directory. That is launch/configuration authority, not approval of each source proposal. Local Python owns sequencing and the filesystem effects. It reads stable source and failure trajectories from fixed project paths and hashes stable source, trajectories and four trusted evaluation files before generation. The desired change is fewer redundant permanent-error calls while preserving temporary recovery and the public API. SRC-1: `chapter9/self-modifying-agent/run_experiment_9_6.py`, `chapter9/self-modifying-agent/evolution.py`; [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate).

Host diagnosis groups failed, non-retryable trajectories with more than one attempt by tool/error code. At least two matching cases produce a diagnosis targeting retry/circuit-breaker code. This is a deterministic selector over supplied records, not an online agent noticing its own live failure. It supplies case IDs, trajectory hashes, the alleged cause, expected fix and regression concerns to later generation. SRC-1: `chapter9/self-modifying-agent/evolution.py`; the cause and threshold are supported by [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate).

### 2. Rejection precedes the coding-model handoff

The host first generates an intentionally over-broad control that disables every retry. It evaluates that control and packages its source hash, failed checks, rejection reason and a fixed failure description as `rejected_history`. This is a software-authored negative control, not evidence of a naturally occurring failed model predecessor. The same campaign then constructs a deterministic comparison and sends one coding request. SRC-1: `chapter9/self-modifying-agent/run_experiment_9_6.py`, `chapter9/self-modifying-agent/evolution.py`; [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate).

> rejected_history = [{
>         "candidate_sha256": rejected["source_sha256"],
>         "failed_checks": rejected_manifest["failed_checks"],
>         "rejection_reason": rejected_manifest["rejection_reason"],
>         "failure": "disabled temporary-timeout retries",
>     }]
> --- `chapter9/self-modifying-agent/run_experiment_9_6.py`

The coding provider receives one user message containing the complete stable module, diagnosis, rejected-history summary and a request for predicted impact followed by complete replacement source in JSON. It does not receive the rejected source or raw failure-trajectory file through that history handoff. The request asks it to preserve public signatures and temporary retries, stop permanent retries, open the circuit immediately for permanent failures, update the version, and leave validation/release logic alone. The model authors a proposal, not a release decision; provider/model mutability is already scoped in [RT-CMP-coding-model](runtime.md#rt-cmp-coding-model). SRC-1: `chapter9/self-modifying-agent/llm_generator.py`.

> Previously rejected candidates (do not repeat their failure):
> {json.dumps(rejected_history or [], ensure_ascii=False, indent=2)}
> --- `chapter9/self-modifying-agent/llm_generator.py`

Host code extracts JSON, converts the source field to text, ensures a trailing newline, and packages a diff, source hash, patch size, prediction and API receipt. It does not execute proposed source during packaging. Prompt delivery establishes the requested response, not compliance or content-dependent learning from the rejected control. There is one coding call in this driver, not an automatic re-prompt loop following rejection of its own proposal. SRC-1: `chapter9/self-modifying-agent/llm_generator.py`, `chapter9/self-modifying-agent/run_experiment_9_6.py`; [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate).

### 3. Software verification and authority separation

After generation, the host rehashes the protected inputs and evaluator files. It validates deterministic, model-generated and rejected-control candidates through the same validation function, adds `protected_surfaces_unchanged` to each check dictionary, obtains manifests, and separately computes bounded behavior metrics against a stable baseline. The hash comparison happens after generation, not after every evaluation or file write; it is a checked snapshot, not continuous filesystem protection. SRC-1: `chapter9/self-modifying-agent/run_experiment_9_6.py`.

> checks = validate_candidate(candidate["source"], trajectories, stable_source)
>         checks["protected_surfaces_unchanged"] = protected_unchanged
> --- `chapter9/self-modifying-agent/run_experiment_9_6.py`

Verification has two owners. The host rejects oversized/uncompilable source and forbidden AST constructs before candidate execution. It then supplies source, trajectories and stable source to a disposable Docker evaluator via bounded stdin JSON. The evaluator loads candidate functions, checks exact signatures, tests retry/circuit outputs for supplied failures, and checks temporary-recovery and threshold behavior. These fixed expectations are the answer oracle; the coding model's prediction is not. The host receives bounded JSON checks, not a separate reviewing agent's prose. SRC-1: `chapter9/self-modifying-agent/evolution.py`, `chapter9/self-modifying-agent/candidate_sandbox.py`, `chapter9/self-modifying-agent/sandbox_runner.py`; [RT-RTE-candidate-validation](runtime.md#rt-rte-candidate-validation).

The requested envelope includes no network, a read-only filesystem, an unprivileged user and resource limits. Its effective isolation depends on Docker/kernel/image contracts, and candidate and evaluator share a container process. Hence host containment is distinct from adversarial verdict integrity. The runtime's [RT-RTE-candidate-validation](runtime.md#rt-rte-candidate-validation) retains those limits and supporting passages; no stronger isolation or deployment guarantee is inferred here.

### 4. Rejection, failure and recovery

The manifest accepts only a changed candidate with a nonempty check set whose values all pass. False checks produce `reject_candidate`, with the failed names retained. The campaign adds the protected-file check, whereas arbitrary direct manifest callers can supply another check set. It is not universal release authorization. SRC-1: `chapter9/self-modifying-agent/evolution.py`, `chapter9/self-modifying-agent/run_experiment_9_6.py`; [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate).

Infrastructure rejection also has a bounded continuation path. The sandbox wrapper removes a timed-out container and raises `SandboxError`; validation converts that into a partially populated check dictionary with remaining checks false. Metrics converts sandbox failure into null measures and `evaluation_failed`. The campaign can then retain failed artifacts and report failed gates. Source-size, compile and AST rejection likewise return false checks without running candidate source. These are wired recovery paths, not observed failures. SRC-1: `chapter9/self-modifying-agent/candidate_sandbox.py`, `chapter9/self-modifying-agent/evolution.py`; [RT-RTE-candidate-validation](runtime.md#rt-rte-candidate-validation).

That recovery is not comprehensive. The inspected coding function and campaign do not catch credential, provider-call or JSON-extraction exceptions to retry generation or write a final report. File errors can also interrupt delivery. Rejection of the model-generated candidate does not cause another model round. The host keeps stable source unchanged by writing proposals to candidate paths; rollback readiness evaluates selected stable behavior and records its hash, not an exercised restoration of a deployed successor. SRC-1: `chapter9/self-modifying-agent/llm_generator.py`, `chapter9/self-modifying-agent/run_experiment_9_6.py`, `chapter9/self-modifying-agent/evolution.py`; [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate).

### 5. What is delivered

Delivery is an audit package and terminal summary, not a running successor. The driver creates a fresh output directory and writes every candidate's source and manifest regardless of admission. It constructs a report containing diagnosis, rejected history, comparisons, metrics, receipts, input hashes, manifests and campaign-level gates. The aggregate `accepted` flag is the conjunction of campaign gates, distinct from each candidate's manifest decision. It then writes `evidence.json`, its checksum and Python artifact hashes; copies canonical latest evidence; writes canonical model and rejected manifests; and prints a JSON summary. If these steps finish, exit zero means all campaign gates passed; otherwise the ordinary completed path returns one. SRC-1: `chapter9/self-modifying-agent/run_experiment_9_6.py`.

> "accepted": all(gates.values()),
> --- `chapter9/self-modifying-agent/run_experiment_9_6.py`

> return 0 if report["accepted"] else 1
> --- `chapter9/self-modifying-agent/run_experiment_9_6.py`

The final writes are not an atomic transaction or externally acknowledged delivery. Earlier artifacts may exist when a later write fails. The printed summary assumes the output directory can be made relative to the project root; a caller-selected directory outside that root can raise at the final `relative_to(ROOT)` after artifacts have been written. This implementation limit prevents equating artifact presence with successful terminal return. SRC-1: `chapter9/self-modifying-agent/run_experiment_9_6.py`.

> "evidence": str(evidence_path.relative_to(ROOT)),
> --- `chapter9/self-modifying-agent/run_experiment_9_6.py`

Finally, `release_to_canary` is a manifest eligibility label with shadow-only scope. This driver does not route live traffic through the proposal or install it over stable source. Delivery therefore establishes neither activated self-modification nor successful improvement. The independent theory, learning and self-improvement limits remain those of [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate), rather than being inferred from a completed package. SRC-1: `chapter9/self-modifying-agent/run_experiment_9_6.py`, `chapter9/self-modifying-agent/evolution.py`; [RT-CLM-canary-decision](runtime.md#rt-clm-canary-decision).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate)

Workflow selection: the campaign is representative because its one driver connects a negative-control rejection to the coding handoff and then to verification and evidence delivery. The human configures launch; Python schedules generation, verification and artifact writes; the model proposes source only. No independent worker scheduler or human per-candidate approval is established in this selected route.

Workflow handoff: rejected-control hash, failed checks, reason and a fixed failure description reach the next coding request alongside diagnosis and stable source. That is summary delivery within one campaign, not the rejected source itself or proof that the model revised its reliance. A failed model proposal has no further coding round in the inspected driver.

Delivery criterion: evidence and candidate files are written, canonical summaries are refreshed, a terminal JSON summary is printed, and the campaign returns according to its aggregate gate flag. These steps do not install a successor and are not transactional. An out-of-root output directory can leave written evidence while failing terminal summary construction. The workflow account retains the relevant campaign anchors and passages. SRC-1: `chapter9/self-modifying-agent/run_experiment_9_6.py`, `chapter9/self-modifying-agent/llm_generator.py`.

#### On [RT-RTE-candidate-validation](runtime.md#rt-rte-candidate-validation)

Workflow recovery owner: the sandbox wrapper removes the timed-out container and reports infrastructure failure; the host validator leaves unsuccessful checks false and the metric wrapper returns failed-evaluation placeholders. The campaign's manifest/report machinery can then preserve rejection. This does not cover coding-provider or filesystem exceptions, and it does not implement deployed rollback. SRC-1: `chapter9/self-modifying-agent/candidate_sandbox.py`, `chapter9/self-modifying-agent/evolution.py`, `chapter9/self-modifying-agent/run_experiment_9_6.py`.
