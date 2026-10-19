---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "ModularRSI workflow: support-task diagnosis, isolated implementation, rejection recovery and generation delivery."
run-id: AAS-2026-10-18-modularrsi-4218ceff5530-01
reviewed-boundary: b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9
---

# ModularRSI workflow report

## Workflow account

### Selection and evidence limits

This account selects one ordinary two-lane evolution window, from an operator's configured support-task curriculum to a promoted module library used by later solver launches. It is representative because it connects the shipped improvement entry point to the executable product, rather than joining independent editor and solver capabilities. It is a source-supported control-flow trace, not a reconstructed successful training episode. Evaluation-only invocation consumes the product but does not perform this window. The baseline establishes these distinctions in [RT-RTE-generation-change](runtime.md#rt-rte-generation-change) and [RT-RTE-solver-task](runtime.md#rt-rte-solver-task).

Evidence is SRC-1 implementation and shipped prompt/design text at the frozen revision. Additional inspection covered `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py` brief construction and lane execution, `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py` recovery/selection/retry/disposition, and `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` two-lane editor/gate wiring and promotion accounting. No target execution or bundled individual trajectory was inspected. Consequently, model compliance, successful delivery in an actual evolution run and improvements attributable to a change remain uninspected. The detailed workflow below specializes existing runtime referents; it does not allocate duplicate records.

### 1. Request becomes solver evidence

The operator requests improvement by configuring and launching evolution: model access, support tasks, resources and a module lock bound the experiment. Phase0 delegates the curriculum to the online driver. The driver launches solver task groups against a captured generation. Each solver receives a task and selected executable bundle, not the whole improvement backlog. The chosen loop controls model calls, tool actions and stopping. Harbor's task verifier supplies a separate reward; the solver's completion signal is not that correctness judgment. Returned rewards and trajectories become the evidence for reflection, not automatic proof that a particular module caused failure. These handoffs and their source passages are in [RT-RTE-solver-task](runtime.md#rt-rte-solver-task) and [RT-RTE-bundle-selection](runtime.md#rt-rte-bundle-selection).

Completed groups trigger a background reflection window while solver launches can continue. Thus the window is not a global stop-the-world barrier: some collected evidence and in-flight tasks can refer to earlier generations. Task and bundle identities matter for interpreting the resulting diagnoses. Investigators receive selected task summaries and permitted trajectories in separate sessions; their findings feed the persistent proposal path. Software selects proposals rather than allowing each implementer to choose whichever failure is most vivid. A window can leave a lane empty. The source requests counterfactual, module-local diagnosis, including the possibility that no warranted change exists; it does not establish that investigators obeyed. See [RT-RTE-generation-change](runtime.md#rt-rte-generation-change).

### 2. Proposal becomes an isolated implementation brief

Before selecting work, the window invokes lease recovery so a proposal left selected by an interrupted window is not invisible to the open-proposal selector. Selected proposals then go to independent staging trees from the same parent. The implementation handoff includes proposal identity, lane, action, target, behavioral delta, causal hypothesis and supporting findings. It does not merge investigator conversation histories into the editor session (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py`, `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`).

> for recovered in _lease.recover(archive_root, step=step):
> --- `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py`

The brief requests generality across the support, but the actual delivered support is bounded: individual finding JSON bodies are truncated at `MAX_FINDING_CHARS`, and unreadable finding IDs produce an explicit incomplete-evidence warning. The preamble's assertion of complete evidence therefore must be read with these transformations, not as a guarantee of complete raw trajectories. The source describes the intended isolation precisely:

> """Assemble one lane's instruction from ONLY its own proposal + evidence."""
> --- `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`

> if len(body) > MAX_FINDING_CHARS:
>         body = body[:MAX_FINDING_CHARS] + "\n… [truncated]"
> --- `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`

The editor implements the assigned action: modify an existing variant, add a variant, or replace one using supersession metadata. It is instructed to validate, commit a patch and signal completion. The online callback supplies staging, archive, solver-trajectory root, skills, model configuration, turn budget and module lock, then passes the editor outcome to the gate battery. The editor cannot declare the result delivered merely by ending its conversation (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`).

### 3. Verification can reject, but does not certify improvement

The gate sequence checks committed edits, smoke/static contracts, action shape and niche, model review, required variant identification, then forced activation and crash sanity. The review sees diff and intent with reward-omitting summaries, not the investigator's full context. The expected-answer oracle is the task verifier used for support-task outcomes; review instead requests model judgment. Sanity checks crash freedom and required activation, not a reward-improvement margin. A normal-routing probe does not veto. These scopes and supporting excerpts are retained in [RT-RTE-generation-change](runtime.md#rt-rte-generation-change).

An explicit structured review rejection can stop a candidate. Reviewer timeout or exception, however, passes as skipped; missing verdicts can initially pass until circuit-breaker handling applies. Sanity-crash repair can change the tree after review without returning through every earlier gate. Consequently, neither “review approved every final byte” nor “passing candidates improve task reward” is established. Supported editor file guards also do not sandbox imported Python; the executable effect boundary is [RT-BAP-module-execution](runtime.md#rt-bap-module-execution), not a general safety guarantee.

### 4. Rejection separates a bad direction from a bad build

A particularly consequential branch is a reviewer classifying the direction as sound but its implementation as wrong. The window examines failed, actually attempted, non-retry outcomes. Only the implementation rejection class, with a readable proposal below the attempt threshold, qualifies for the second implementer. A proposal-class rejection does not enter this branch. The rejected tree is discarded; the second editor starts from the parent with the repair brief, rather than continuing from the faulty candidate (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py`).

> if not outcome.attempted or not _lane_failed(outcome) or outcome.retry:
>             continue
>         kind, brief = _reject_class(outcome)
>         if kind != "implementation":
>             continue
> --- `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py`

> _staging.discard_staging(outcome.staging_dir)
>         picks.append(_RetryPick(proposal))
>         briefs[outcome.proposal_id] = brief
> --- `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py`

The second build returns through the same editor-and-gate callback before promotion planning. It is a bounded rewrite, not an unlimited repair conversation. If that retry ends as a rejected implementation, final disposition also marks the direction taboo. Other failed/unclassified attempts are disposed of without pretending that the reviewer classified them as a wrong proposal. This separates proposal reliance from implementation repair; it establishes a criticism-delivery mechanism, not that any supplied criticism was correct (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py`).

> if outcome.retry and closed_as == _proposals.REJECTED_IMPLEMENTATION:
> --- `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py`

Staging failure is handled differently from an editor attempt: the proposal is returned to open and its lease finished without charging an implementation attempt. Once the editor is about to run, the attempt-start marker is written before awaiting it. This makes recovery sensitive to whether work actually started, rather than treating every infrastructure interruption as evidence against the direction (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`).

> _lease.record_attempt_started(archive_root, pid, step=step)
>     try:
>         result = await run_lane(brief)
> --- `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`

### 5. Passing trees become delivered generations

A passing lane is eligible for promotion, not automatically an independently valid merge with another passing lane. The default promotion order is incumbent first. A second passing lane is rebased onto the newly promoted parent. Conflicts reject it; successful rebases rerun tree-dependent gates, while an unchanged change-local diff can reuse its review. Archive synchronization is best effort after filesystem promotion, so failure to synchronize does not undo the numbered generation. The window returns its newest promoted path, or a discard reason when nothing lands. These transition semantics and their minimum source passages are in [RT-RTE-generation-change](runtime.md#rt-rte-generation-change).

Delivery here means the admitted executable tree has become a generation and the driver updates the library path for later launches. It is not a natural-language editor response or an assertion that already-running tasks switched modules. Later loads discover executable factories, while ordinary composition interprets retained descriptions to choose strategies. Forced replay and static selection remain alternate consumption paths. See [RT-BAP-module-execution](runtime.md#rt-bap-module-execution) and [RT-BAP-description-selection](runtime.md#rt-bap-description-selection). Confirmation can later retire poorly performing variants from ordinary dynamic selection; this is not full transactional rollback of every persisted artifact.

The workflow therefore wires evidence-responsive change through to a live consumer across task launches. It does not show, without an inspected evolution trace, that a particular update was exercised or beneficial. The runtime's separately scoped theory and self-change assessments remain in [RT-RTE-generation-change](runtime.md#rt-rte-generation-change); this workflow adds no empirical theory-building or improvement claim.

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

#### On [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

Workflow handoff boundary: the online driver owns the window; investigators diagnose, software selects proposals, separate editors implement selected directions, and the gate callback decides candidate eligibility. Only selected proposal/evidence content crosses into each lane, subject to missing-finding warnings and truncation. A reviewer-classified implementation failure can redirect one fresh build from the parent before promotion planning. Lease and attempt accounting distinguish preparation failure from started work. The detailed source evidence for these workflow fields is retained above.

Workflow delivery boundary: promotion returns the newest usable generation to the driver. Archive sync and downstream task success are separate outcomes. Parallel in-flight tasks keep their launch generation; delivery is a later-launch transition, not a synchronized replacement of every active solver.

#### On [RT-RTE-solver-task](runtime.md#rt-rte-solver-task)

Workflow return distinction: model completion ends solver interaction according to the selected verification strategy; Harbor's subsequent verifier supplies the outcome consumed by evolution. Neither alone constitutes delivery of an improved library. That delivery belongs to the generation transition above.
