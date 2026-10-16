---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "LHTB epistemic routes: task outcomes, oracle-relative grading, context handoffs and post-run model assessments."
run-id: AAS-2026-10-15-lhtb-a0548ba4edbf-01
reviewed-boundary: "7ca0cacea9bf6a0694eaad7306bed794eaaaabce"
---

# LHTB epistemic report

## Source-and-claim boundary

The question is what LHTB checks and licenses for reliance, rather than whether a terminal agent can generate plausible explanations. Scope, exclusions, external-service limits and evidence identity are see [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register). All added reads below are SRC-1 implementation or explicitly labelled doctrine/design, at the frozen commit. Nothing here is target execution. No independently inspected trajectories or intervention results establish actual repair, summary fidelity, generalization or component benefit.

The runtime baseline is provisional. Direct CLI inspection found exposed `check` and `analyze` operations omitted from that baseline. They produce assessments of task quality and reward legitimacy, so a negative about all assessment routes based only on the solver loop would be invalid. Task-local public feedback also differs materially from the hidden binary continuation channel. These are additions, not supersessions of the supplied runtime records.

| Entry point or operation | Source path | Coverage and limit |
|---|---|---|
| Job/trial invocation, resume, multi-step, verifier disable | `harbor/src/harbor/cli/main.py`; `harbor/src/harbor/trial/trial.py` | CLI wiring directly read; progression see [RT-RTE-trial-execution](runtime.md#rt-rte-trial-execution), [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery). |
| Terminal commands, installed agents, dynamic imports, MCP/skills | `harbor/src/harbor/agents/terminus_2/terminus_2.py`; `harbor/src/harbor/agents/factory.py` | Supplied [RT-RTE-terminal-actions](runtime.md#rt-rte-terminal-actions), [RT-RTE-agent-dispatch](runtime.md#rt-rte-agent-dispatch). Other installed-agent/provider internals uninspected: no system-complete absence of additional evaluators. |
| Filtering, summarization, overflow recovery | `harbor/src/harbor/agents/terminus_2/terminus_2.py` | Direct filter and handoff-install reads; rest see [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff). |
| Interim/final checks, cleanup, rejection, separate artifacts, timed checkpoints | `harbor/src/harbor/trial/trial.py`; `harbor/src/harbor/verifier/verifier.py` | Supplied [RT-RTE-verifier-execution](runtime.md#rt-rte-verifier-execution), [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation), [RT-CLM-grader-isolation](runtime.md#rt-clm-grader-isolation). No deployed isolation evidence. |
| Public feedback, hidden judge, dense scoring | `tasks-2.0/acoustic_beamforming_peak__01/environment/app/tools/feedback`; `tasks-2.0/acoustic_beamforming_peak__01/tests/private/judge.py`; `tasks-2.0/acoustic_beamforming_peak__01/tests/private/dense_reward.py`; `tasks-2.0/acoustic_beamforming_peak__01/tests/test.sh` | Direct reads: [EPI-RTE-public-feedback](#epi-rte-public-feedback), [EPI-RTE-hidden-semantics](#epi-rte-hidden-semantics), [EPI-RTE-dense-reward](#epi-rte-dense-reward). One task is not an audit of all 77 oracles. |
| Task quality check, trial analysis, job aggregation | `harbor/src/harbor/cli/analyze.py`; `harbor/src/harbor/analyze/` | Direct caller/backend/checker/analyzer and default rubric reads: [EPI-RTE-task-check](#epi-rte-task-check), [EPI-RTE-trial-analysis](#epi-rte-trial-analysis), [EPI-RTE-analysis-cache](#epi-rte-analysis-cache), [EPI-RTE-job-aggregation](#epi-rte-job-aggregation). Custom prompts and actual SDK behavior unobserved. |
| Old task check/debug and trial summarize | `harbor/src/harbor/cli/tasks.py`; `harbor/src/harbor/cli/trials.py` | Direct dispatch reads: these print removal notices and exit, rather than adding independent evaluators. |
| END hooks, metrics and saved results | `harbor/src/harbor/job.py` | Direct completion-hook read: reward updates stats and metrics and writes job result. Recovery see [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery). Configured metric implementations, custom hooks, sweeps, viewer/upload consumers uninspected: no exhaustive ranking or adaptation conclusion. |
| Patch-maintenance and alternate installed runtime | `harbor/skills/apply-lhtb-patches/PATCH.md`; `harbor/patches/single_step.py.harbor-0.20.0` | Supplied [RT-RTE-runtime-patching](runtime.md#rt-rte-runtime-patching): source-supported alternative policy, not an observed deployment. |

Consequential public claims are [EPI-CLM-benchmark-warrant](#epi-clm-benchmark-warrant) and [RT-CLM-grader-isolation](runtime.md#rt-clm-grader-isolation). Missing images, opaque provider weights/state and unavailable historical runtime identity prevent deployment assurance. Uninspected remaining graders prevent a uniform claim about every task's criterion. Missing comparison evidence prevents attributing learning or scientific validity to a score.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-task-instruction](runtime.md#rt-obj-task-instruction) | Task facts and requirements; imperatives are not themselves truth claims | see record | SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py` | Imported authored guidance, not verified world knowledge. |
| [EPI-OBJ-reconstruct](#epi-obj-reconstruct) | Candidate scenario-output mapping and numerical summaries | see record | SRC-1, `tasks-2.0/acoustic_beamforming_peak__01/tests/private/judge.py` | Implementation alone does not individuate an agent's proposed explanation or actual output. |
| [EPI-OBJ-check-report](#epi-obj-check-report) | Public match results, hidden semantic checks and reward | see record | SRC-1, `tasks-2.0/acoustic_beamforming_peak__01/tests/private/dense_reward.py` | Program-reference-relative, not a scientific validity certificate. |
| [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) | Model summary/answers about prior work | see record | SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py` | Route citation owns handoff findings; semantic preservation unknown. |
| [EPI-OBJ-analysis](#epi-obj-analysis) | Task quality, trial legitimacy, failure explanations, job narrative | see record | SRC-1, `harbor/src/harbor/analyze/analyzer.py` | Candidate model judgments; schema compliance does not establish truth. |
| [RT-OBJ-trial-result](runtime.md#rt-obj-trial-result) | Recorded rewards, errors and timings | see record | SRC-1, `harbor/src/harbor/job.py` | Retention and scheduler reliance are not acceptance of explanations. |
| [RT-CMP-terminus-model](runtime.md#rt-cmp-terminus-model) | Distributed-parametric content not locally individuated | see record | SRC-1, `harbor/src/harbor/llms/chat.py` | Exact weights, internal reasoning and provider-side updates uninspected. |
| [EPI-CMP-analysis-model](#epi-cmp-analysis-model) | Distributed-parametric content not locally individuated | see record | SRC-1, `harbor/src/harbor/analyze/backend.py` | Separate model selection and SDK; do not inherit Terminus identity. |

## Authority-route ledger

Each row separates a consequential function; repeated record citations refer to the same implementation, not new records. All implemented routes remain unobserved in supplied run evidence.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-terminal-actions](runtime.md#rt-rte-terminal-actions) | content transformation | implemented | see record | truth-apt transformation: indeterminate | Task-solving response | Model; arbitrary terminal tasks | see record | Analysis, commands, completion intent possible | see record | Candidate generation, no truth license from parser | see record | see [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance) | SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py` | none | none | No concrete generated claim proves entailment or ampliation. |
| [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) | content transformation | implemented | see record | truth-apt transformation: indeterminate | Prior conversation to summary/answers | Model; historical task state | see record | Replacement context | see record | Fidelity unverified; intended compression is not proven non-ampliative reshaping | see record | see [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance) | SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py` | none | none | Omission or invented inference cannot be ruled out. |
| [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) | operational admission/selection/consumption | implemented | see record | no content change | Install handoff as next context | Code; successful model return, not semantic test | see record | Automatic context replacement | see record | No evidence-consuming acceptance | Later solver receives selected history by value | see [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance) | SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py` | none | none | No raw-history reload established. |
| [EPI-RTE-public-feedback](#epi-rte-public-feedback) | check/evidence production | implemented | see [EPI-OBJ-reconstruct](#epi-obj-reconstruct) | truth-apt transformation: entailed derivation | Public output/signature match | see record | see record | Public checks and diffs | Advisory | Exact predicate over supplied reference; no hidden-scenario license | Feedback can guide shell-driven repair, not stop trial | Solver via terminal stdout; advisory; current trial | SRC-1, `tasks-2.0/acoustic_beamforming_peak__01/environment/app/tools/feedback` | none | none | Signature alternative can pass despite unequal payloads. |
| [EPI-RTE-hidden-semantics](#epi-rte-hidden-semantics) | check/evidence production | implemented | see [EPI-OBJ-reconstruct](#epi-obj-reconstruct) | truth-apt transformation: entailed derivation | Hidden numerical outputs and artifact gates | see record | see record | Pass/fail report | Input to score, not direct command veto | Toleranced agreement on finite hidden scenarios only | Grader report reaches score converter | Judge JSON to dense grader; enforcing scoring input; one verification | SRC-1, `tasks-2.0/acoustic_beamforming_peak__01/tests/private/judge.py` | [EPI-CLM-benchmark-warrant](#epi-clm-benchmark-warrant) | Scope narrower than real-tool reconstruction | Oracle correctness and source encoding not certified. |
| [EPI-RTE-dense-reward](#epi-rte-dense-reward) | content transformation | implemented | see [EPI-OBJ-check-report](#epi-obj-check-report) | truth-apt transformation: entailed derivation | Judge report to numeric score | see record | see record | Graded reward or binary fallback | Scoring | Ladder-defined arithmetic, not proportion of all requirements met | Reward becomes continuation/metric input | Reward file to Verifier and trial; enforcing continuation input; trial | SRC-1, `tasks-2.0/acoustic_beamforming_peak__01/tests/private/dense_reward.py` | none | none | Dense partial credit differs from acceptance. |
| [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation) | disposition/acceptance | implemented | see [RT-OBJ-trial-result](runtime.md#rt-obj-trial-result) | no content change | Whether numeric full pass ends continuation | see record | see record | Full pass or rejection/another phase | see record | Acceptance of tested task result for benchmark stopping, not a general explanatory claim | see record | Trial controller via reward; enforcing; remaining budget | SRC-1, `harbor/src/harbor/trial/trial.py` | [EPI-CLM-benchmark-warrant](#epi-clm-benchmark-warrant) | Binary default not universal | Timeout or disabled grading is not acceptance. |
| [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation) | behavior/policy adaptation | implemented | see record | non-truth-apt policy/content update: another repair phase | Continue task after rejection | see record | see record | Another model turn/run | see record | Rejection identifies no blamed claim | Current workspace can be revised; not rolled back | see [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance) | SRC-1, `harbor/src/harbor/trial/trial.py` | none | none | Adapted continuation does not demonstrate learning. |
| [EPI-RTE-task-check](#epi-rte-task-check) | check/evidence production | implemented | see [EPI-OBJ-analysis](#epi-obj-analysis) | truth-apt transformation: indeterminate | Task quality under rubric | see record | see record | Model check outcomes/explanations | Advisory | Candidate rubric assessment, not certified quality | Printed or optionally saved, not a launch veto | CLI/operator via table/JSON; advisory; later human use unobserved | SRC-1, `harbor/src/harbor/analyze/checker.py` | none | none | No outcome-fidelity check shown. |
| [EPI-RTE-trial-analysis](#epi-rte-trial-analysis) | check/evidence production | implemented | see [EPI-OBJ-analysis](#epi-obj-analysis) | truth-apt transformation: indeterminate | Reward legitimacy and task specification | see record | see record | Trial summary/checks | Advisory | Candidate explanation against available files | Can inform operator; does not withdraw trial reward | CLI and aggregation via structured assessment; advisory; post-run | SRC-1, `harbor/src/harbor/analyze/analyzer.py` | none | none | Possible unsupported inference from missing task files. |
| [EPI-RTE-analysis-cache](#epi-rte-analysis-cache) | operational admission/selection/consumption | implemented | see [EPI-OBJ-analysis](#epi-obj-analysis) | no content change | Structured output admissibility | Pydantic schema, not truth evaluator | see record | Reject invalid structure; admit valid result | Enforcing structure | No epistemic acceptance of explanation | Valid results can be printed/persisted/aggregated | Analyzer via model validation; enforcing; assessment invocation | SRC-1, `harbor/src/harbor/analyze/analyzer.py` | none | none | A valid conclusion can be false. |
| [EPI-RTE-analysis-cache](#epi-rte-analysis-cache) | retention | implemented | see [EPI-OBJ-analysis](#epi-obj-analysis) | no content change | Save and reuse analysis JSON | see record | see record | Cached assessment returned | Permissive reuse | No new evidence check on cache hit | Reanalysis skipped unless overwrite | Later Analyzer via file/cache flag; enforcing reuse; subsequent invocations | SRC-1, `harbor/src/harbor/analyze/analyzer.py` | none | none | Existence is not freshness or endorsement. |
| [EPI-RTE-job-aggregation](#epi-rte-job-aggregation) | content transformation | implemented | see [EPI-OBJ-analysis](#epi-obj-analysis) | truth-apt transformation: indeterminate | Per-trial assessments to job narrative | see record | see record | Saved job summary | Advisory | Inherits unverified inputs; no new warrant from aggregation | Narrative reaches CLI/operator and cache | Summary text/JSON; advisory; later analysis use | SRC-1, `harbor/src/harbor/analyze/analyzer.py` | none | none | No independent source recheck in aggregation call. |
| [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery) | retention | implemented | see [RT-OBJ-trial-result](runtime.md#rt-obj-trial-result) | no content change | Completed results retained/reloaded | see record | see record | Completed trial skipped, stats reused | see record | Saved outcome metadata, not accepted theory | see record | Scheduler via saved files; enforcing; job restart | SRC-1, `harbor/src/harbor/job.py` | none | none | Does not restore solver conversation. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-benchmark-warrant](#epi-clm-benchmark-warrant) | see record | SRC-1, `README.md`, doctrine/design and reported operation | see record | [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation), [EPI-RTE-hidden-semantics](#epi-rte-hidden-semantics) | No inspected run trace | No independently varied comparison; finite tests and environment contracts bound scores | Self-reported completion alone does not set full-pass reward; task tests and numeric threshold do | Binary-only default claim does not describe every bundled restarted path. Reproducing oracle outputs is narrower than establishing the mechanism or real-tool validity. |
| [RT-CLM-grader-isolation](runtime.md#rt-clm-grader-isolation) | see record | SRC-1, `harbor/skills/apply-lhtb-patches/PATCH.md`, doctrine/design | see record | [RT-RTE-verifier-execution](runtime.md#rt-rte-verifier-execution), [RT-RTE-runtime-patching](runtime.md#rt-rte-runtime-patching) | see record | see record | Binary prompt construction and separation mechanisms are inspectable | Best-effort cleanup, alternate runtimes, mounted logs and provider contracts prevent universal confidentiality. |

## Bounded conclusion

LHTB imports task instructions and terminal observations, generates candidate actions, checks task products and lets reward alter continuation. These are separate authorities: command parsing permits effects; numeric grading licenses stopping; natural-language feedback guides the next model turn. An adverse reward does not undo earlier workspace changes. See [RT-RTE-terminal-actions](runtime.md#rt-rte-terminal-actions) and [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation).

The inspected reconstruction evaluator can derive bounded propositions about agreement with a shipped reference computation. Its acoustics reference computes an exponentially decaying sinusoid and convolution; the judge checks length, energy and peak with tolerances. Those facts do not warrant that a candidate recovered a physical mechanism, independently reproduces a real tool across its domain, or generalizes beyond hidden scenarios. Public feedback is an additional, detailed advisory channel, not the hidden rejection channel; it even permits signature equality as an alternative to payload agreement. See [EPI-RTE-public-feedback](#epi-rte-public-feedback), [EPI-RTE-hidden-semantics](#epi-rte-hidden-semantics).

Checks, arithmetic and stopping are not interchangeable. A parsed score is evidence for the task's declared acceptance criterion, not an accepted ampliative explanation. No concrete model-produced proposition in the accessible run evidence establishes production, evidence-consuming acceptance and subsequent lifecycle integration of an ampliative claim. This is a bounded evidential limit, not a system-complete architectural negative: opaque agents, remaining tasks and uninspected hooks remain relevant. See [EPI-RTE-dense-reward](#epi-rte-dense-reward).

Model-produced handoffs retain selected historical content for later solver invocation without a semantic acceptance gate. The intended compression cannot be classified as faithful reshaping from source wiring alone. The deterministic filter is different: it preserves selected byte segments and explicitly omits the interior; an observation can therefore disappear without being rejected as false. See [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff).

Post-run `check` and `analyze` provide a second evaluator family. They request file-informed model judgments about task coverage and reward legitimacy, reject malformed structure, save assessments, reuse them and summarize across trials. Within the inspected callers, their verdicts are advisory: no consumer withdraws a scored reward or blocks a later benchmark launch because an analysis says `fail`. Cache reuse is operational reliance before any demonstrated epistemic acceptance. See [EPI-RTE-task-check](#epi-rte-task-check), [EPI-RTE-trial-analysis](#epi-rte-trial-analysis), [EPI-RTE-analysis-cache](#epi-rte-analysis-cache), [EPI-RTE-job-aggregation](#epi-rte-job-aggregation).

Continuation, retained summaries and post-run diagnosis independently establish implemented behavior-changing routes, not improved future capacity. Model parameter changes are not exposed in the inspected call paths, and provider internals remain uninspected. No supplied experiment establishes learning, benefits of summarization, causal effects of hardening or exercised self-improvement of the harness. Runtime patch adoption remains a separate afforded machinery-change path, see [RT-RTE-runtime-patching](runtime.md#rt-rte-runtime-patching). None of these limits collapses the independent positive findings about checking, retention or operational control.

## Shared records

### Components

#### EPI-CMP-analysis-model
Label: Analysis SDK model

Distinct from [RT-CMP-terminus-model](runtime.md#rt-cmp-terminus-model): selected through Claude Agent SDK in SRC-1, `harbor/src/harbor/analyze/backend.py`, with CLI defaults `sonnet` for check and `haiku` for analyze in `harbor/src/harbor/cli/analyze.py`. Distributed-parametric weights live outside the repository. No parameter-update operation is exposed in this backend; provider-side change is uninspected. The aliases do not pin exact weights/version; external resolution can change. Prompts and returned judgments are natural language, not the parameters themselves.

> model=normalize_model_name(model),
> --- `harbor/src/harbor/analyze/backend.py`

### Operative objects

#### EPI-OBJ-reconstruct
Label: reconstruct.py scenario behavior

Distinct from [RT-OBJ-task-instruction](runtime.md#rt-obj-task-instruction): this is the task product, not its specification. Source-native `/app/workspace/reconstruct.py` is symbolic source on sandbox disk, executed on scenario JSON to produce numerical/symbolic summaries. Those outputs are truth-apt relative to a named scenario/reference; actual candidate contents are not supplied. SRC-1, `tasks-2.0/acoustic_beamforming_peak__01/tests/private/judge.py`.

> reconstruct = args.workspace / "reconstruct.py"
> --- `tasks-2.0/acoustic_beamforming_peak__01/tests/private/judge.py`

#### EPI-OBJ-check-report
Label: Judge report and dense reward

Part of: [RT-RTE-verifier-execution](runtime.md#rt-rte-verifier-execution)

This object is material intermediate state inside the containing verification route, not a replacement for that route. Symbolic JSON check outcomes/details and numeric text reward are written to verifier files. Public feedback is stdout JSON consumed interpretively by the solver. Private results enter Verifier and trial control. SRC-1, `tasks-2.0/acoustic_beamforming_peak__01/tests/test.sh`.

> cat /tmp/dense_reward.out > /logs/verifier/reward.txt
> --- `tasks-2.0/acoustic_beamforming_peak__01/tests/test.sh`

#### EPI-OBJ-analysis
Label: Analysis judgments and summaries

No counterpart among supplied runtime objects: these are post-run task/trial assessments, not TrialResult or active solver context. Natural-language summaries and explanations coexist with symbolic check outcomes in structured model responses and disk `analysis.json`/`analysis.md`. JSON fields control cache/formatting; prose guides operator interpretation and job summarization. SRC-1, `harbor/src/harbor/analyze/analyzer.py` and `harbor/src/harbor/analyze/checker.py`.

> return QualityCheckResult(checks=parsed.model_dump())
> --- `harbor/src/harbor/analyze/checker.py`

### Routes

#### EPI-RTE-public-feedback
Label: Public scenario feedback

No counterpart in supplied runtime routes: a task-local, solver-invoked evaluator, not hidden verification. SRC-1 implementation, `tasks-2.0/acoustic_beamforming_peak__01/environment/app/tools/feedback`: code runs reconstruct.py, reads public reference products, compares signature or summaries, prints results. Candidate comes from solver; fixed code decides matches; no human veto or rollback is required. Mode is bounded public-scenario testing, triggered by invoking the tool. It admits no workspace change; it supplies advisory repair evidence.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON public checks, field diffs and pass count to stdout.
- Later read-back: inapplicable — this tool does not persist feedback for a later invocation; terminal history handling belongs to the agent.
- Delegated visibility: Candidate receives public scenario JSON; solver receives public expected values/diffs and signatures.
- Selection predicate: Public manifest scenarios and workspace reconstruct.py presence.
- Invalidation or expiry: Rerunning recomputes checks against current candidate; no stored verdict is withdrawn.
- Activation or effect: Feedback is delivered through terminal output if invoked; repair compliance unobserved.
- Evidence limits: Signature-match disjunction and public-only domain prevent a semantic or hidden-generalization guarantee.

> passed = got_signature == expected_signature or got_summary == expected_summary or got == expected_output
> --- `tasks-2.0/acoustic_beamforming_peak__01/environment/app/tools/feedback`

The disjunction is a source-supported counterexample to interpreting public pass as necessarily equal numerical output: a dict with the expected signature and wrong summary can satisfy its first term. This is a deduction from inspected code, not an executed exploit.

#### EPI-RTE-hidden-semantics
Label: Hidden oracle semantic checks

Part of: [RT-RTE-verifier-execution](runtime.md#rt-rte-verifier-execution)

The task-specific evaluator inside that containing harness route. SRC-1 implementation, `tasks-2.0/acoustic_beamforming_peak__01/tests/private/judge.py`; family selection confirmed in `tasks-2.0/acoustic_beamforming_peak__01/tests/private/variant.json`. Task author supplies scenario/reference/criteria, solver supplies candidate, fixed code judges. Target is artifact gates and finite hidden scenario summaries, not the candidate's explanation. Acoustics checks `rir_len` with absolute tolerance 6/relative .02, energy relative .25, peak relative .20 and positive energy. The reference below is executable arithmetic, not a proof of physical encoding fidelity. Tests can veto pass but do not roll back the product. Mode is bounded benchmark verification.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON report and success/failure exit code.
- Later read-back: Report reaches dense scoring in the same verification; retained host rewards reach later job consumers through supplied runtime routes.
- Delegated visibility: Candidate receives scenario; private evaluator holds expected output and checks.
- Selection predicate: Artifact/config gates precede hidden loop; private oracle selected by family; loop stops on first failure.
- Invalidation or expiry: New verification recomputes against current workspace; prior saved results are not automatically erased.
- Activation or effect: Check report drives task score conversion.
- Evidence limits: Scientific source truth, images, package behavior and all-task coverage unverified; finite tolerances bound the license.

> if not passed:
>                         checks["candidate_matches_hidden_semantics"] = False
>                         break
> --- `tasks-2.0/acoustic_beamforming_peak__01/tests/private/judge.py`

> n = 256 + stable_int(params.get("rir_length"), 256)
>     decay = stable_float(params.get("absorption_level"), 0.02, 0.005)
>     rir = np.exp(-np.arange(n) * decay) * np.sin(np.arange(n) / 4)
>     src = np.zeros(n); src[0] = 1; src[50] = 0.5
>     y = signal.fftconvolve(src, rir)[:n]
> --- `tasks-2.0/acoustic_beamforming_peak__01/tests/private/offcode20_oracle.py`

#### EPI-RTE-dense-reward
Label: Judge report to dense reward

Part of: [RT-RTE-verifier-execution](runtime.md#rt-rte-verifier-execution)

This material score conversion differs from the hidden check and later stopping disposition. SRC-1 implementation, `tasks-2.0/acoustic_beamforming_peak__01/tests/private/dense_reward.py` and `tasks-2.0/acoustic_beamforming_peak__01/tests/test.sh`. Fixed ladder requires prior gates; semantic refinement adds within-stage credit. Launcher falls back to judge exit-code reward when conversion fails. No human selects a score per candidate; criterion is arithmetic, intended use benchmark credit, not explanation acceptance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Numeric score text to launcher/reward file, or parser error causing binary fallback.
- Later read-back: Reward is retained in trial result and consumed by continuation/job stats; see supplied runtime routes.
- Delegated visibility: Converter sees private judge JSON; ordinary same-conversation solver receives binary rejection instead.
- Selection predicate: Loadable report with checks; sequential ladder and semantic detail flags.
- Invalidation or expiry: Later verification can overwrite current reward output; saved historical outcomes require separate retention policy.
- Activation or effect: Numeric output becomes the verifier result input for pass/continue.
- Evidence limits: Arithmetic cannot authenticate report provenance or establish oracle validity.

> graded = stage / MAX_STAGE
>     if stage < MAX_STAGE:
>         graded += refine / MAX_STAGE
> --- `tasks-2.0/acoustic_beamforming_peak__01/tests/private/dense_reward.py`

Concrete deduction: `{"checks":{"workspace_nonempty":true,"workspace_has_editable_artifact":true},"details":[]}` clears stage 1 only; refinement is zero, so grade is round(1/6,4) = 0.1667. With no `passed` flag, CLI chooses that grade, not 1.0. This is checked implementation arithmetic, not observed operation or a newly validated world claim.

#### EPI-RTE-task-check
Label: Task quality rubric assessment

No counterpart among supplied routes: explicit CLI `check`, not solver command parsing or hidden grading. SRC-1 implementation, `harbor/src/harbor/analyze/checker.py`, `harbor/src/harbor/cli/analyze.py`; rubric doctrine/design, `harbor/src/harbor/analyze/prompts/check-rubric.toml`. Caller selects model/prompt/rubric; model judges task coverage, schemas, dependencies and cheating risks. Program validates structure, not truth. Model is the evaluator, with no independent expected-answer oracle. Mode is operator-requested assessment; optional output is saved automatically, no per-judgment human admission gate. It does not edit/reject the task itself or provide rollback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured quality checks, printed table and optional caller-selected JSON output.
- Later read-back: uninspected — optional saved output has no later consumer established in these callers.
- Delegated visibility: SDK gets task working directory, file tree, rubric guidance and Read/Glob/Grep tools.
- Selection predicate: Existing valid task directory and chosen/default rubric/prompt.
- Invalidation or expiry: Reinvocation recomputes; no automatic semantic withdrawal found in inspected caller.
- Activation or effect: Advisory results reach CLI/operator; not a benchmark launch veto here.
- Evidence limits: Actual file reads, model compliance and rubric judgment accuracy unobserved; source assumptions about hidden tests are not deployment facts.

> tools=["Read", "Glob", "Grep"],
>         output_schema=response_model.model_json_schema(),
> --- `harbor/src/harbor/analyze/checker.py`

#### EPI-RTE-trial-analysis
Label: Trial legitimacy and specification assessment

No counterpart among supplied runtime routes: post-run diagnosis is distinct from binary in-trial rejection. SRC-1 implementation, `harbor/src/harbor/analyze/analyzer.py`; rubric doctrine/design, `harbor/src/harbor/analyze/prompts/analyze-rubric.toml`. Model receives task access when locally available and trial directory access, proposes summary and rubric judgments. The default rubric asks whether reward came from legitimate solving and whether instructions suffice. These are substantive truth-apt assessments, but request and schema do not guarantee evidence consumption or accuracy. No human per-result veto; invalid structure is rejected by code. No reward withdrawal or automatic machinery change occurs in this inspected path. Mode is requested post-run analysis.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured trial summary and check judgments.
- Later read-back: Results persist/reload through [EPI-RTE-analysis-cache](#epi-rte-analysis-cache), and feed job aggregation.
- Delegated visibility: SDK gets trial cwd, read tools and optional task directory; when absent, prompt requests inference from trajectory/test output.
- Selection predicate: Selected trial directory, cache miss/overwrite; optional passing/failing filters at CLI/job selection.
- Invalidation or expiry: Overwrite requests reanalysis; unchanged cache otherwise reuses prior judgment.
- Activation or effect: Judgment enters reports and aggregation, not scored reward mutation.
- Evidence limits: Diagnosis is not causal identification; absent task source weakens specification assessments; no observed SDK trace.

> "The task directory is not available locally. "
>                 "Use the trajectory and test output to infer what the task required."
> --- `harbor/src/harbor/analyze/analyzer.py`

#### EPI-RTE-analysis-cache
Label: Analysis validation persistence and reuse

No counterpart to [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery): different files, consumer and consequence; this reuses model assessments rather than trial outcomes. SRC-1 implementation, `harbor/src/harbor/analyze/analyzer.py`. Program rejects invalid structured response, writes valid assessment, and can return cached JSON without querying the model. This is structural admission and retention, not evidence-consuming epistemic acceptance. Caller can choose overwrite; no human review gate or automatic truth-based rollback. Existing file policy controls replacement.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Validated AnalyzeResult, from fresh output or cached JSON.
- Later read-back: Later analyze invocation can reuse trial analysis; job aggregation can consume cached trial assessments and cached job summary.
- Delegated visibility: Later consumer receives parsed assessment, not necessarily original raw evidence.
- Selection predicate: Cache exists and overwrite is false; otherwise model validation and disk writes.
- Invalidation or expiry: Explicit overwrite; no evidence-change digest check in inspected cache branch.
- Activation or effect: Cache can skip model evaluation and supply prior judgment downstream.
- Evidence limits: Schema validity does not certify factual correctness, freshness or execution provenance.

> if not overwrite and cached.exists():
>             return AnalyzeResult.model_validate_json(cached.read_text())
> --- `harbor/src/harbor/analyze/analyzer.py`

> parsed = self._config.response_model.model_validate(raw)
> --- `harbor/src/harbor/analyze/analyzer.py`

#### EPI-RTE-job-aggregation
Label: Trial assessment to job narrative

No counterpart among supplied runtime routes: natural-language aggregation of diagnoses is distinct from numeric job metrics. SRC-1 implementation, `harbor/src/harbor/analyze/analyzer.py` and `harbor/src/harbor/analyze/backend.py`. Code builds text from trial name, summary and checks; model returns job summary without file tools. No independent oracle or semantic acceptance gate; summary is automatically retained/returned. Model proposes narrative, code admits it; human authors rubric/prompt or later judges use, not per-content approval in this path. Mode is bounded post-run job analysis; failed trial analyses are reported separately, not silently converted into success.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JobAnalyzeResult with generated summary and constituent assessments.
- Later read-back: Job analysis JSON can be reused when trial analyses were all cached and overwrite is false.
- Delegated visibility: Aggregation model gets summaries and checks in prompt, not raw trajectories through its tool-less call.
- Selection predicate: Successful selected per-trial analyses; passing/failing filter and cache policy.
- Invalidation or expiry: Overwrite or uncached trial analysis triggers new aggregation.
- Activation or effect: Job narrative is written and displayed; causal benefit or later operator action unobserved.
- Evidence limits: Summarization may omit or infer; failed analyses and selected subset bound coverage; retention does not establish lifecycle integration after acceptance.

> return await query_agent(
>         prompt=prompt,
>         model=model,
>         cwd=".",
>         tools=[],
> --- `harbor/src/harbor/analyze/backend.py`

### Claims

#### EPI-CLM-benchmark-warrant
Label: Hidden verification rather than self-report

SRC-1, `README.md`, doctrine/design, claims useful-work measurement with hidden rebuild-from-artifact verification, reconstruction of scientific/engineering tools and binary rejection until timeout/pass. These are benchmark claims, not a claim to produce accepted scientific theories. Closest supplied [RT-CLM-grader-isolation](runtime.md#rt-clm-grader-isolation) concerns hardening; this claim covers what the benchmark measures and licenses. Reported leaderboard results do not supply causal evidence of generalization or installed-policy identity.

> Unlike short-horizon coding benchmarks where an agent writes one artifact and stops, LHTB drops the agent into a stateful environment and grades it with **hidden, rebuild-from-artifact verifiers** — self-reported progress does not count.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
