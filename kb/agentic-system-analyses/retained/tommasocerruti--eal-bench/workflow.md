---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "EAL-Bench workflow account tracing Procurement writer formation, ordinary probe execution, rejection recovery and persisted delivery."
run-id: AAS-2026-10-15-eal-bench-f9a76e2fa858-01
reviewed-boundary: "51648690bc52d7a9c7ac080a2c67a784fe9d56cb"
---

# EAL-Bench workflow report

## Workflow account

### Selected workflow and evidence

This account follows the **ordinary generated-final probe branch of the Procurement writer study**: an operator selects a study; a writer forms persistent authorization memory; code freezes that memory into evidence; executor models receive requests behind it; deterministic scoring and persistence deliver an experiment run directory. This branch exposes the system's central handoff: model-written state becomes another model's evidence without becoming the scorer's authorization oracle. It also exposes bounded repair and interruption recovery. The unit of work is an experiment, not a real organizational purchase.

The baseline records are [RT-RTE-study-execution](runtime.md#rt-rte-study-execution), [RT-RTE-writer-admission](runtime.md#rt-rte-writer-admission) and [RT-RTE-executor-score](runtime.md#rt-rte-executor-score). This member adds SRC-1 implementation inspection of `domains/procurement/studies/routes.py` (writer-plan construction and the beginning of its post-writer builder), `experiments/authorization_memory/study_engine.py` (run, preparation, final persistence and exception handling), and `experiments/authorization_memory/langmem_writer.py` (update-wave progression, repair, fallback and payload processing). All are within the registered revision. No target code, test, provider call or example was executed. No run trace or causal experiment is established here; the account describes wired progression, not successful historical execution.

The writer study also installs a post-writer builder for additional diagnostic jobs. Its existence is not conflated with the ordinary probe branch, and this account does not establish the diagnostic selector's complete semantics. Candidate review, mitigations and closed-loop feedback remain distinct alternatives in the runtime member, not stages joined into this workflow.

### 1. Operator request becomes a host-owned plan

The launch request selects domain, study, cases, writer/executor targets, repetitions and related options. CLI cost acknowledgement is launch control, not human approval of individual memories or executor decisions; see [RT-RTE-study-execution](runtime.md#rt-rte-study-execution). The Procurement plan builder filters writer specifications by selected conditions. Its ordinary job builder pairs each generated evidence item with each probe for that item's case (SRC-1, `domains/procurement/studies/routes.py`).

> for item in evidence
> for probe in selected_domain.corpus.probes(by_case[item.case_id])
> --- `domains/procurement/studies/routes.py`

> study_id="writer",
> writer_chains=specs,
> --- `domains/procurement/studies/routes.py`

The shared engine validates the plan definition, resolves presentation and tasks, calibrates capacity, checks target compatibility, creates a run directory and writes its manifest before model work. Symbolic code owns the next-step policy; the writer does not choose to launch an executor or select arbitrary downstream agents. The plan supplies the chain, update ordering and targets. The separate writer and executor model identities are described in [RT-CMP-writer-model](runtime.md#rt-cmp-writer-model) and [RT-CMP-executor-model](runtime.md#rt-cmp-executor-model); frozen source identity does not pin provider weights.

### 2. Writer delegation returns a candidate, not a verified grant

The engine delegates writer chains to the LangMem wrapper. Each writer invocation receives domain guidance, one existing profile and the selected update messages. Its returned profile is a proposal. Software checks profile protocol, payload shape, cited-source visibility and enabled capacity limits; it does not thereby prove authorization entailment. The writer's inference and software admission are separate decisions, with no per-update human approval in this inspected path. [RT-RTE-writer-admission](runtime.md#rt-rte-writer-admission) supplies the admission evidence and structural-versus-semantic limit; [RT-BAP-profile-update](runtime.md#rt-bap-profile-update) identifies the prior-profile consumption path.

Within a chain, accepted changed content replaces current memory; no-change is recorded separately. The host advances ordered update positions and ultimately freezes current memory. Returned writer artifacts include memories, attempts, state rows, final evidence and model contexts, rather than the writer's unrestricted conversation becoming executor context (SRC-1, `experiments/authorization_memory/langmem_writer.py`).

> final_evidence.append(_freeze(chain.current, chain.spec.run_id))
> --- `experiments/authorization_memory/langmem_writer.py`

### 3. Rejection has a bounded owner and a non-success fallback

A writer/provider error or invalid payload is recorded as an unsuccessful attempt. When configured for two attempts, the wrapper schedules one repair invocation with feedback from the first attempt. Accepted or unchanged output does not enter this retry branch (SRC-1, `experiments/authorization_memory/langmem_writer.py`).

> if attempt.status not in {"accepted", "no_change"} and max_attempts == 2:
>     retry.append((chain, update, attempt))
> --- `experiments/authorization_memory/langmem_writer.py`

> repair_feedback=[
>     _repair_feedback(first) for _, _, first in retry
> ],
> --- `experiments/authorization_memory/langmem_writer.py`

Recovery belongs to wrapper code, not an autonomous writer deciding to broaden its task. An unsuccessful proposal does not overwrite an existing accepted artifact. If the terminal attempt leaves no current artifact, code creates an empty payload artifact and records its retained identity. This permits downstream evidence formation even when no substantive writer update succeeded. Consequently, an evidence artifact or completed experiment is not proof that the writer accepted a meaningful authorization update. The earlier rejection diagnostics remain in attempts and state rows (SRC-1, `experiments/authorization_memory/langmem_writer.py`).

> if chain.current is None:
>     chain.current = _artifact(
>         domain,
>         chain,
>         update.block_index,
>         _empty_payload(domain, architecture),
> --- `experiments/authorization_memory/langmem_writer.py:610-639`

This is structural repair, not gold correction of an authorization mistake. A plausible but semantically false grant can survive the baseline checks. The deterministic scorer later measures consequences; it does not retroactively prevent admission.

### 4. Preparation fixes the writer-to-executor handoff

The engine passes a `WriterRunBundle` to the configured post-writer callback, combines returned artifacts with the existing bundle and validates jobs. It rejects inconsistent memory or evidence identity collisions. The ordinary job builder consumes generated writer evidence, while the post-writer expansion can add separate jobs. The engine validates executor surfaces and freezes the pre-execution checkpoint before issuing executors (SRC-1, `experiments/authorization_memory/study_engine.py`). The retained plan is [RT-OBJ-executor-plan](runtime.md#rt-obj-executor-plan).

The handoff supplies selected frozen evidence plus a case/probe request and execution identity, not the writer's private reasoning. Under default executor construction, code serializes the selected memory into a delimited user-message frame beside the request, under a separate domain system prompt. Each job gets a fresh frame. Explicit messages and prepared challenge contexts are alternatives; the default frame is not a universal rule for every study. See [RT-RTE-executor-score](runtime.md#rt-rte-executor-score) and [RT-BAP-memory-evidence](runtime.md#rt-bap-memory-evidence).

This isolation resembles passing selected values between task frames: the retained artifact escapes the writer frame, but a memory identifier alone cannot be followed by the model to recover omitted history. The host must supply the payload. Neither serialization nor delivery establishes that an executor will follow it correctly.

An operator can stop after the writer checkpoint. The returned directory is then an intermediate delivery, not a completed executor experiment: the manifest explicitly records zero executor calls and a need for resume (SRC-1, `experiments/authorization_memory/study_engine.py`).

> "reason": "precommitted_writer_formation_review",
> "executor_calls_made": 0,
> "resume_required": True,
> --- `experiments/authorization_memory/study_engine.py`

### 5. Executor choice becomes a scored trial

The executor receives domain-native tool definitions and chooses its response. The inspected benchmark runner scores that response rather than dispatching a real order. The domain ledger and authorized issuers supply the answer oracle independently of remembered grants. No call, multiple calls, malformed arguments and provider errors have distinct handling; a generated terminal response is not automatically an accepted valid action. [RT-RTE-executor-score](runtime.md#rt-rte-executor-score) supplies the scorer's passages and scope.

The important rejection boundary is measurement: the scorer can mark a response invalid or identify unauthorized action, but it is not a pre-transaction veto in an external procurement service. The generic handler loop is a separate effectful path, not part of this experiment's tool dispatch; see [RT-RTE-alternate-consumers](runtime.md#rt-rte-alternate-consumers). Ordinary probe scoring does not automatically revise writer memory. The explicit feedback mechanism in [RT-RTE-closed-feedback](runtime.md#rt-rte-closed-feedback) is another workflow.

### 6. Persistence delivers the result; continuation recovers missing work

After executor work, the engine validates correspondence between model contexts and the call log. It writes applicable memory, attempt, state, evidence, trial and context rows, plus study-specific artifacts. The manifest records file hashes and counts; completion also verifies retained checkpoint files have not changed. The normal return value is the run-directory path, not a prose answer or a real purchase receipt (SRC-1, `experiments/authorization_memory/study_engine.py`).

> "status": "completed",
> "finished_at": datetime.now().astimezone().isoformat(),
> "files": files,
> "counts": counts,
> --- `experiments/authorization_memory/study_engine.py`

The engine records an exception in the manifest as failure and rethrows rather than reporting successful completion. This catch covers errors inside the run's guarded execution/persistence block, not every possible failure before manifest creation (SRC-1, `experiments/authorization_memory/study_engine.py`).

> "status": "failed",
> "finished_at": datetime.now().astimezone().isoformat(),
> "error": f"{type(exc).__name__}: {exc}",
> --- `experiments/authorization_memory/study_engine.py`

For supported checkpoint continuation, the resume driver validates saved artifacts and reconstructed identities, reuses completed calls and schedules missing executor work without regenerating the writer. Changed artifacts reject continuation; reviewer-backed writer checkpoints are explicitly unsupported. This recovery is grounded by [RT-RTE-checkpoint-resume](runtime.md#rt-rte-checkpoint-resume), not a newly observed interruption trial. It requires trustworthy local artifacts and does not establish exactly-once provider execution.

Delivery therefore means persisted, indexed experimental outputs after the selected work has been processed, or an explicitly labelled checkpoint pause. It does not mean every trial was valid, authorization was preserved, or the workflow improved model performance. Primary historical raw archives and provider behavior remain outside the available execution evidence described in [the boundary](boundary.md#boundary-and-evidence).

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

#### On [RT-RTE-study-execution](runtime.md#rt-rte-study-execution)

Workflow selection: Procurement writer study's ordinary generated-final probes. The host pairs each generated evidence item with its case's probes. The post-writer callback is an additional preparation branch, not model-chosen delegation. Delivery distinguishes completed artifact persistence from an explicit pre-execution pause; neither entails valid or successful trials.

#### On [RT-RTE-writer-admission](runtime.md#rt-rte-writer-admission)

Workflow recovery: the host gives an unsuccessful first attempt one repair opportunity when configured for two attempts. Terminal failure preserves prior accepted state; without prior state it creates an empty payload artifact. Thus downstream availability of frozen evidence is compatible with failed substantive writing. Attempts retain the failure rather than making fallback an accepted proposal.

#### On [RT-RTE-executor-score](runtime.md#rt-rte-executor-score)

Workflow verification role: measurement after response generation, not a live procurement approval gate. It verifies trial form and evaluates action authorization against the independent domain oracle. Ordinary probe results reach persisted trials, not an automatically scheduled writer correction.

#### On [RT-RTE-checkpoint-resume](runtime.md#rt-rte-checkpoint-resume)

Workflow recovery boundary: resume continues supported frozen executor work; it is not a writer repair mechanism or a guarantee that every failure can be resumed. Local artifact/identity validation and missing-call selection do not establish provider-side exactly-once behavior.
