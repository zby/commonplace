---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "RSIAgent epistemic routes: candidate verification, experience retention, downstream reliance and the limits of improvement claims."
run-id: AAS-2026-10-14-rsiagent-b11225763c0b-01
reviewed-boundary: "4d7ef43770dda341fccd9a5743db92407687c615"
---

# RSIAgent epistemic report

## Source-and-claim boundary

The question is how execution evidence becomes a local task verdict, a reusable lesson, a later decision input, or a published outcome claim. The functional boundary and exclusions are those of [boundary](boundary.md#boundary-and-evidence); sources resolve through its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design; README scores supply reported operation only. No inspected trace establishes that a generated lesson was checked, accepted, or used. No causal comparison is supplied. These are evidence limits, not proof that the routes never operate.

This overlay separates checks, disposition and retention inside the supplied runtime's valid containers. No supplied record needs supersession. The runtime's independence and freshness descriptions do not mean that code proves every full-Agent PASS has evidential support: the inspected full-Agent report parser is explicitly transport-only. The legacy freshness machinery and the full-Agent prompt have different force; see [EPI-RTE-verdict-admission](#epi-rte-verdict-admission).

Claims assessed are [RT-CLM-training-free](runtime.md#rt-clm-training-free), [EPI-CLM-knowledge-feedback](#epi-clm-knowledge-feedback), and [EPI-CLM-reported-scores](#epi-clm-reported-scores). We assess the implemented request for evidence-responsive lessons, not a hypothetical required claim schema. Procedures and scripts may encode empirically testable advice, but an uninspected generated script cannot be assigned a proposition merely from its filename.

### Coverage

“Direct” means source text read in this job at SRC-1's pin; “supplied” means a runtime finding, not an independent read here. Available uninspected variants prevent a system-complete negative about all acceptance/recovery routes.

| Entry point or operation | Source path | Coverage and records, or limit |
| --- | --- | --- |
| OSWorld baseline and RSI dispatch | `run_osworld.py`, `benchmarks/osworld/task.py`, `benchmarks/osworld/pipeline.py` | Supplied: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission). Sealed grading and frozen-host-bank conclusions are bounded to that account. |
| ALE plan/run/prepare/smoke/report dispatch | `run_ale.py` | Direct complete CLI; report is a separate material operation beyond the runtime's detailed routes: [EPI-RTE-score-report](#epi-rte-score-report). Preparation/smoke implementation not independently read; no readiness-test completeness conclusion. |
| ALE worker and official evaluation handoff | `benchmarks/ale/worker.py`, `benchmarks/ale/host.py` | Worker supplied via [RT-RTE-task-execution](runtime.md#rt-rte-task-execution); direct host grading region: [EPI-RTE-official-score](#epi-rte-official-score). External evaluator internals excluded; prevents evaluator-correctness conclusions. |
| Program/Look/Ask observations, native-call handling | `core/loop.py`, `core/actor.py`, `llm/client.py` | Supplied task route; direct client native-call branch: [EPI-RTE-observation-import](#epi-rte-observation-import). No separate provider-native tool execution inferred. |
| Done probes and legacy checks | `core/checks.py`, `core/verifier.py` | Direct validation/run-check code; supplied independent legacy route: [EPI-RTE-probe-check](#epi-rte-probe-check). Legacy budget acceptance alternatives remain as supplied, not a universal full-Agent guarantee. |
| Full-Agent report publication, parsing, cleanup | `core/verifier.py`, `explore/charter.py`, `core/verifier_runtime.py` | Direct parser, terminal return/recovery/cleanup region, and verifier decision charter; executor protections supplied: [EPI-RTE-candidate-check](#epi-rte-candidate-check), [EPI-RTE-verdict-admission](#epi-rte-verdict-admission). No executed isolation or restoration evidence. |
| WORK LOG folding and fallback | `core/loop.py` | Direct folding helpers; supplied subsequent call assembly: [EPI-RTE-worklog-fold](#epi-rte-worklog-fold). Fidelity of generated summary unresolved. |
| Distillation, reconciliation, diagnosis | `explore/charter.py`, `explore/target_learning.py` | Direct prompts and complete promotion function: [EPI-RTE-memory-proposal](#epi-rte-memory-proposal). Requested semantic criticism is not observed criticism. |
| Leakage audit, rejection and publication | `explore/commit.py`, `explore/target_learning.py`, `tools/exam_fence.py` | Direct shingle/corpus/audit and promotion functions; imported near-shingle helper located but body not inspected here. [EPI-RTE-memory-admission](#epi-rte-memory-admission), [EPI-RTE-bank-retention](#epi-rte-bank-retention). No complete leakage-prevention claim. |
| Phase-1 serial reconciliation; later frozen memory | `explore/phase1_wave.py`, `explore/practice_loop.py`, `explore/charter.py` | Supplied [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission), [RT-BAP-actor-method](runtime.md#rt-bap-actor-method); direct maintenance prompts. Guest copy may change; delivered memory is not proven used. |
| Curriculum outcomes and stop/retry | `core/self_evolving_loop.py`, `explore/unified_evolution.py` | Supplied [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search). Independent bottleneck hypotheses, routing and authority remain distinct from task correctness. |
| Recovery admissions | `explore/phase1_boundary_recovery.py`, `explore/phase2_recovery.py` | Supplied [RT-RTE-lineage-recovery](runtime.md#rt-rte-lineage-recovery); named variant bodies remain uninspected. Prevents a complete recovery/admission negative, not the supported positive routes. |
| Claims and aggregate results | `README.md`, `benchmarks/ale/report.py` | Direct README method/results regions and complete report module: [EPI-CLM-knowledge-feedback](#epi-clm-knowledge-feedback), [EPI-CLM-reported-scores](#epi-clm-reported-scores). No archived cohort results supplied. |

Opaque provider numerical state is assessed only through the supplied component records [RT-CMP-actor](runtime.md#rt-cmp-actor), [RT-CMP-verifier](runtime.md#rt-cmp-verifier), [RT-CMP-curriculum](runtime.md#rt-cmp-curriculum), and [RT-CMP-vision-model](runtime.md#rt-cmp-vision-model). Endpoint labels do not pin weights; inspected calls do not train parameters; provider-side changes and internal learning remain uninspected. No claim about absence of learning follows from fixed-parameter doctrine.

## Epistemic-object inventory

Each record owns the content, representation, substrate and limits; the overlay does not duplicate those fields.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-observation](#epi-obj-observation) | see record | see record | SRC-1, `core/loop.py` | see record |
| [EPI-OBJ-verifier-report](#epi-obj-verifier-report) | see record | see record | SRC-1, `core/verifier.py` | see record |
| [EPI-OBJ-memory](#epi-obj-memory) | see record | see record | SRC-1, `explore/charter.py` | see record |
| [EPI-OBJ-worklog](#epi-obj-worklog) | see record | see record | SRC-1, `core/loop.py` | see record |
| [EPI-OBJ-evaluation-score](#epi-obj-evaluation-score) | see record | see record | SRC-1, `benchmarks/ale/report.py` | see record |

## Authority-route ledger

The cited record owns every field marked “see”; its labelled assessment paragraph supplies the ledger-specific fields. Architectural status here is independent of operation conclusion status. Rows for supplied containers identify consequential functions not redeclared as whole routes.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-observation-import](#epi-rte-observation-import) | content transformation | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `core/loop.py` | see | see | see |
| [EPI-RTE-probe-check](#epi-rte-probe-check) | check/evidence production | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `core/checks.py` | see | see | see |
| [EPI-RTE-candidate-check](#epi-rte-candidate-check) | check/evidence production | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `core/verifier.py` | see | see | see |
| [EPI-RTE-verdict-admission](#epi-rte-verdict-admission) | disposition/acceptance | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `core/verifier.py` | see | see | see |
| [EPI-RTE-worklog-fold](#epi-rte-worklog-fold) | content transformation | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `core/loop.py` | see | see | see |
| [EPI-RTE-memory-proposal](#epi-rte-memory-proposal) | content transformation | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `explore/charter.py` | see | see | see |
| [EPI-RTE-memory-admission](#epi-rte-memory-admission) | disposition/acceptance | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `explore/target_learning.py` | see | see | see |
| [EPI-RTE-bank-retention](#epi-rte-bank-retention) | retention | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `explore/target_learning.py` | see | see | see |
| [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission) | lifecycle integration | not determinable | see | see | see | see | see | see | see | see | see | see | SRC-1, `explore/charter.py` | see | see | see |
| [RT-BAP-actor-method](runtime.md#rt-bap-actor-method) | operational admission/selection/consumption | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `explore/charter.py` | see | see | see |
| [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search) | behavior/policy adaptation | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `core/self_evolving_loop.py` | see | see | see |
| [RT-RTE-lineage-recovery](runtime.md#rt-rte-lineage-recovery) | lineage/freshness/recovery | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `explore/phase2_recovery.py` | see | see | see |
| [EPI-RTE-official-score](#epi-rte-official-score) | check/evidence production | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `benchmarks/ale/host.py` | see | see | see |
| [EPI-RTE-score-report](#epi-rte-score-report) | content transformation | implemented | see | see | see | see | see | see | see | see | see | see | SRC-1, `benchmarks/ale/report.py` | see | see | see |

For the supplied lifecycle-integration container, the additional assessment is **not determinable**: implementation requests corpus organization/revision, but whether any specific claim was accepted on evidence before integration cannot be individuated without a memory/decision artifact. Retention before that acceptance remains retention, not established lifecycle integration. For supplied downstream consumption, there is no content change at inventory delivery; content license is fallible guidance, advisory through the Actor over later tasks. For supplied Curriculum adaptation, project choice and READY/STALLED are policy updates; particular truth-apt hypothesis transformations are indeterminate without an instance. For supplied recovery, there is no content change under hash-checked replay; the license is lineage continuity, enforcing admission for resumed calls, not renewed semantic endorsement. These are narrower assessments of the supplied records, not new claims that their requested operations occurred.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-training-free](runtime.md#rt-clm-training-free) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission), [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) | none supplied | see record; mutable endpoints are not fixed weight identities | Improvement-directed bank change is wired; fixed-weight operation is declared and no training call is evidenced | Exercised or successful self-improvement not established |
| [EPI-CLM-knowledge-feedback](#epi-clm-knowledge-feedback) | see record | SRC-1, `README.md`; doctrine/design | see record | [EPI-RTE-candidate-check](#epi-rte-candidate-check), [EPI-RTE-memory-proposal](#epi-rte-memory-proposal), [EPI-RTE-bank-retention](#epi-rte-bank-retention) | none supplied | see record | Evidence and local judgments feed requested learning; a verdict does not certify a causal lesson | Semantic acceptance and later reliance remain unknown |
| [EPI-CLM-reported-scores](#epi-clm-reported-scores) | see record | SRC-1, `README.md`; reported operation | see record | [EPI-RTE-official-score](#epi-rte-official-score), [EPI-RTE-score-report](#epi-rte-score-report) | no inspectable run artifacts supplied | see record; reported aggregates include selected retries and heterogeneous budgets | Attributed outcomes, not reproduced scores or component effects | Current report code does not prove it produced the manuscript table |

## Bounded conclusion

RSIAgent has an inspected route from machine interaction to independent task judgment and consequential continuation. Program output, image observations and simulator responses enter with instrument/source warrant **unknown**, not magically preserved by textual delivery. Generated observations and interpretations remain distinct. The probe token evaluator licenses only its explicitly encoded check; the full-Agent Verifier is asked to assess all material task requirements. Its valid published verdict changes control immediately, but the transport parser does not prove that investigation occurred or that the report is correct. Cleanup and candidate rollback protect a narrower effect boundary, not semantic warrant or remote effects ([EPI-RTE-observation-import](#epi-rte-observation-import), [EPI-RTE-probe-check](#epi-rte-probe-check), [EPI-RTE-candidate-check](#epi-rte-candidate-check), [EPI-RTE-verdict-admission](#epi-rte-verdict-admission)).

Local candidate acceptance has a named intended use—handoff of this task state—and an instructed criterion—affirmative support for every material requirement. No supplied instance establishes an evidence-consuming decision satisfying that criterion. The host nevertheless enforces routing from the report token. This separates operational authority from epistemic acceptance without denying the implemented model evaluation route.

Experience-fed memory is a separate product. The same Actor is asked to distill, criticize, qualify, delete and reorganize it; Verifier PASS licenses neither the causal explanation nor transfer. Host publication checks leakage/transport rather than certifying a lesson's truth. Files may later guide any fresh Actor that selects them; delivery is advisory natural language before broad generated-code effects. Deletion/replacement changes future guidance, while journal retention preserves recovery evidence. No generated lesson is supplied, so production of an accepted ampliative claim and post-acceptance lifecycle integration are **not determinable**. This is compatible with a substantive implemented lesson-generation request and with possible correct knowledge, not a system-wide absence verdict ([EPI-RTE-memory-proposal](#epi-rte-memory-proposal), [EPI-RTE-memory-admission](#epi-rte-memory-admission), [EPI-RTE-bank-retention](#epi-rte-bank-retention), [RT-BAP-actor-method](runtime.md#rt-bap-actor-method)).

WORK LOG compaction can remove semantic evidence before later calls, even when deterministic. Its lossy text projection cannot inherit complete source warrant. Curriculum outcome-driven project choice and READY/STALLED directly adapt policy without necessarily producing a new truth-apt claim. Official scores are separate measurements, consumed for reporting after execution; score validation and cohort arithmetic establish only their numerical domain and derivations conditional on the imported scores, not evaluator truth or causal improvement ([EPI-RTE-worklog-fold](#epi-rte-worklog-fold), [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search), [EPI-RTE-official-score](#epi-rte-official-score), [EPI-RTE-score-report](#epi-rte-score-report)).

The runtime's separate theory-builder assessments remain bounded: localized hypotheses are afforded, requested content-sensitive criticism is not observed, and retained outputs have a wired next-round channel. Reflection is requested about Actor bottlenecks with a return path through practice/memory, but both causal directions are not demonstrated. Improved future capacity, reflective method revision and autonomous satisfaction of every theory operation are not established by those channels alone. For the agent-plus-bank across exploration and later task use, objective-directed self-change has the runtime's dispositional pathway; evidence does not close causal links from evidence to a particular update and from that update to later behavior. Successful self-improvement and a memory/criticism component effect require additional comparisons. These conclusions neither follow from nor refute fixed-weight operation ([RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission), [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search)).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-observation
Label: Machine observation

Task evidence returned through the execution interface: text stdout/stderr and reports are natural language or mixed textual data on host history/transcripts; images are perceptual data delivered as attachments. Truth-apt contents include claims about current files, application state and observed failures, but a raw pixel array or exit token is not itself an articulated causal theory. Distinct from [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result), which is the control/terminal result rather than turn evidence. SRC-1, `core/loop.py`; see the retained execution passage in [RT-RTE-task-execution](runtime.md#rt-rte-task-execution). External source/instrument fidelity and representativeness remain unknown. Particular truth-apt content is not determinable without an instance.

#### EPI-OBJ-verifier-report
Label: Verifier report

Part of: [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result)

The natural-language findings and requirement judgments are separable from symbolic PASS/FAIL/UNVERIFIED or route tokens, even when in one text artifact. Host transcripts/report artifacts store the text; fixed parser rules consume tokens while models interpret the explanation. Truth-apt candidate is task compliance over the current candidate; the token's operational force is not independent proof. SRC-1, `core/verifier.py`; [EPI-RTE-verdict-admission](#epi-rte-verdict-admission) supplies the passage. No actual report is supplied.

#### EPI-OBJ-memory
Label: Durable memory

Natural-language procedures, claims and possible executable scripts in guest `~/.memory`, canonical host files and journals. This is not the control-result object [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result); it is the durable product consumed by later Actors. See [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission) for the enclosing route. A file may be advice, an environment proposition or a reusable procedure; actual truth-apt claims, encoding details of generated scripts and evidential lineage are not determinable without generated files. The intended role is future capability, with explicit fallibility at consumption. SRC-1, `explore/charter.py`; passages in [EPI-RTE-memory-proposal](#epi-rte-memory-proposal) and [RT-BAP-actor-method](runtime.md#rt-bap-actor-method).

#### EPI-OBJ-worklog
Label: WORK LOG

A model-written natural-language summary string, saved in host summary artifacts and substituted into later model-visible history. It may contain factual state, key values and next-step policy, whose checks and force differ from terminal verdicts. Distinct from [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result)'s control interface; its summary mechanism is contained in [RT-RTE-task-execution](runtime.md#rt-rte-task-execution). SRC-1, `core/loop.py`; passage in [EPI-RTE-worklog-fold](#epi-rte-worklog-fold). No fidelity-tested instance supplied.

#### EPI-OBJ-evaluation-score
Label: Evaluation score

Symbolic finite numeric outcome and cohort statistics in host `eval-result.json`, `result.json`, `summary.json` and CSV. Meaning is defined by an external benchmark evaluator, not merely by numeric type validation. Distinct from the ungraded local status object [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result); terminal task artifacts can include both but verdict and official grade are not interchangeable. SRC-1, `benchmarks/ale/host.py`, `benchmarks/ale/report.py`; evidence below. No actual scores were inspected.

### Routes

#### EPI-RTE-observation-import
Label: Observation import

Part of: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

Actor/VM/callback → turn observation → Actor or independent Verifier. Code owns delivery; models own interpretation. Object: [EPI-OBJ-observation](#epi-obj-observation). Content/update relation: truth-apt transformation: acquisition/import; source warrant unknown. Check target: environment-state propositions, when articulated; evaluator is the selected tool/environment or delegated vision model, not an independent universal truth oracle. Result: returned evidence, not an acceptance decision. Force and operational authority: advisory evidence influences the model's next action within this attempt; channel is text or image observation. Claim: [EPI-CLM-knowledge-feedback](#epi-clm-knowledge-feedback). Mismatch: none; observation availability is not correctness.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Program output, pixels/vision report or Ask callback response.
- Later read-back: Summary/resume and retained lessons can carry selected observations onward; complete fidelity is not established.
- Delegated visibility: Vision sees its selected image/question; Verifier sees independently selected evidence, not full Actor reasoning.
- Selection predicate: Actor action JSON and role configuration select channel and payload.
- Invalidation or expiry: Later machine changes can obsolete observations; fresh attempts and folding remove context.
- Activation or effect: Turn evidence is wired into later calls; no actual changed decision is observed.
- Evidence limits: Source delivery does not authenticate instrument outputs or causal explanations.

SRC-1, `core/loop.py`; execution passage is supplied in [RT-RTE-task-execution](runtime.md#rt-rte-task-execution). Direct client inspection provides a counterexample to assuming every provider-returned tool request executes:

> if native_calls:
> --- `llm/client.py:392-408`

> "they were recorded as transport drift and not executed",
> --- `llm/client.py`

#### EPI-RTE-probe-check
Label: Done probe check

Part of: [RT-RTE-candidate-verification](runtime.md#rt-rte-candidate-verification)

Actor proposes checks → code validates/ranks → VM runs accepted probes → code produces booleans → Done routing. This is a checking function, not the whole disposition. Object: [EPI-OBJ-observation](#epi-obj-observation). Content/update relation: no content change to candidate; derived check output. Target: satisfaction of each proposed shell predicate on the current machine. Evaluator/domain: textual mutation/vacuity filters and PASS-without-FAIL output rule. License: only the encoded predicate, conditional on probe correctness and channel fidelity; not task completeness. Operational force: check results/rejections constrain Done handling within the current attempt, with downstream independent verification as configured. Actor proposes, code can veto, overflow drops alone do not veto; no human or gold answer is supplied. Claim: none. Mismatch: calling this a semantic soundness proof would exceed the lexical implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Accepted checks, rejection/drop reasons and per-probe CheckResult with clipped output.
- Later read-back: inapplicable — this check itself produces current-candidate results, not a retained update; the enclosing runtime may later summarize them.
- Delegated visibility: Accepted probe text reaches the VM; model receives results as loop evidence.
- Selection predicate: Malformed, mutating, constant and suspicious self-report probes are screened; capacity favors content over metadata/existence.
- Invalidation or expiry: Candidate changes invalidate the current check's factual application; no persistent certificate is created.
- Activation or effect: Results are wired into Done decisions; actual check quality and routing exercise are unobserved.
- Evidence limits: Probe author and output can be wrong; a PASS token need not mean the proposed substantive assertion is true.

SRC-1, `core/checks.py`:

> if not any(ch in probe for ch in "/~$|`"):
>     rejections.append(f"probe does not inspect the machine (no path/var/pipe): {probe[:120]}")
>     continue
> --- `core/checks.py`

> passed = bool(re.search(r"\bPASS\b", out)) and not re.search(r"\bFAIL\b", out)
> --- `core/checks.py`

Implementation deduction, not execution: proposed `printf PASS | tr A-Z A-Z` has a pipe, no constant-echo prefix and no file mutation or self-report path. Its output would satisfy the token rule although it measures no candidate property. This defeats a universal semantic-warrant reading of the screen; the independent Verifier route remains a separate check.

#### EPI-RTE-candidate-check
Label: Candidate evidence judgment

Part of: [RT-RTE-candidate-verification](runtime.md#rt-rte-candidate-verification)

Candidate/task → independent Verifier investigation → proposed report. Object: [EPI-OBJ-verifier-report](#epi-obj-verifier-report). Content/update relation: truth-apt transformation: indeterminate; the requested verdict could derive from observations, or generalize beyond them, and no instance decides entailment. Target/domain: material requirements of the given task in the current environment. Model Verifier owns probe selection and sufficiency; no expected-answer oracle or per-candidate human approval is supplied. This is task-directed inspection, with optional persistent context and effect-isolated/mirror modes, not a proof system. Epistemic license sought: current-candidate compliance only, not why the Actor succeeded or transfer to another environment. Operational force of the report is delegated to the separate admission route. Claim: [EPI-CLM-knowledge-feedback](#epi-clm-knowledge-feedback). Mismatch: prompt obligation is not guaranteed evidential adequacy.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Full report with requirement judgments and one route/verdict, or unresolved/infrastructure outcome.
- Later read-back: Persistent Verifier history and scratch carry earlier inspection context; current-candidate claims require new evidence under the instructions.
- Delegated visibility: Independent role receives task/environment, optional untrusted evidence leads, and role-specific transport; not Actor private reasoning or memory on the protected route.
- Selection predicate: Configuration chooses legacy/full-Agent and execution mode; Verifier chooses investigation and when evidence is sufficient.
- Invalidation or expiry: Candidate revisions require reinspection; executor close restores mirrored state when selected, outside-service effects excluded.
- Activation or effect: Evidence-gathering Programs and Looks are implemented; results propose but do not mechanically prove a semantic verdict.
- Evidence limits: Instrument quality, sufficient coverage, actual judgment and noninterference are not observed; executor scope is bounded as in the supplied runtime.

SRC-1, `explore/charter.py`, `core/verifier.py`; protection and cleanup scope also see [RT-RTE-candidate-verification](runtime.md#rt-rte-candidate-verification).

> - PASS only when every material requirement is affirmatively supported.
> - FAIL when concrete evidence establishes a material violation.
> - UNVERIFIED when a material claim remains unresolved after investigation, including
>   when credible instruments or observation channels disagree and you cannot yet
>   reconcile why.
> --- `explore/charter.py`

> These are untrusted leads, not Actor conclusions and not correctness evidence by
> themselves. Reproduce or falsify them from the machine using your own instruments.
> They do not override your prior observations or authorize PASS.
> --- `explore/charter.py`

#### EPI-RTE-verdict-admission
Label: Verifier verdict admission

Part of: [RT-RTE-candidate-verification](runtime.md#rt-rte-candidate-verification)

Published report → lexical token parser → Findings/status → loop/phase handoff, repair, evolution or evidence request. Object: [EPI-OBJ-verifier-report](#epi-obj-verifier-report). Content/update relation: no content change to report; symbolic route extraction. Target: valid committed decision transport, not substantive report truth. Code evaluator accepts one unique recognized decision outside fences/indented code; Verifier supplies that decision. Immediate timing: publication commits inspection termination. Epistemic authority: intended local acceptance scope and criterion are task compliance under the preceding model check; parser alone licenses only token well-formedness. Operational authority is enforcing through [RT-BAP-verdict-routing](runtime.md#rt-bap-verdict-routing), now and into stored outcomes. Model may reject/revise an earlier judgment on new evidence; code can veto ambiguous transport, infrastructure/no-progress and unsafe rollback. No human or expected answer is inserted. Claim: [EPI-CLM-knowledge-feedback](#epi-clm-knowledge-feedback). Mismatch: operationally admitted PASS is not automatically established evidence-consuming acceptance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Internal pass/wrong/evolve/unverified and complete Findings, or recovery/refusal.
- Later read-back: Committed findings enter persistent Verifier context and terminal learning inputs.
- Delegated visibility: Actor receives repair/evidence findings; Curriculum receives routed outcomes, not authority to overrule local correctness.
- Selection predicate: Standalone unambiguous allowed decision token; allow_evolve and allow_unverified alter accepted vocabulary.
- Invalidation or expiry: Ambiguous/missing tokens prompt continuation; model reinspection can change a judgment; mirror cleanup can block a safe terminal result.
- Activation or effect: Host branches on the committed route; malformed or infrastructure outcomes do not become proof of success.
- Evidence limits: Code checks transport, not whether report prose supplies adequate evidence. Legacy freshness/budget paths differ; no universal semantic-acceptance invariant is established.

SRC-1, `core/verifier.py`:

> if not matches or len(set(matches)) != 1:
>     return None
> --- `core/verifier.py`

> return "pass" if matches[0] == "PASS" else "wrong"
> --- `core/verifier.py`

> if owns_executor:
>     program_executor.close()
> --- `core/verifier.py`

Concrete implementation deduction: `VERDICT: PASS` alone yields one match and internal `pass`; adding a separate `VERDICT: FAIL` yields conflicting matches and `None`. Fenced examples are ignored. Neither case evaluates report evidence. This narrows the full-Agent warrant without denying independent model inspection or asserting that a real Verifier published such a report.

#### EPI-RTE-worklog-fold
Label: WORK LOG folding

Part of: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

Older turns/current summary → selected head/tail rendering → model summary or deterministic digest → later Actor context. Object: [EPI-OBJ-worklog](#epi-obj-worklog). Content/update relation: truth-apt transformation: indeterminate for model output; non-ampliative reshaping for the deterministic textual projection only, without established proposition preservation. Target: compact working context; evaluator is the summarizing model plus size/line rules, not factual acceptance. Code thresholds trigger it before later calls; requested summarizer priorities shape retention. Epistemic authority: no added warrant. Operational authority: advisory summary can replace original evidence in later Actor decisions within the attempt/resume horizon. Claim: none. Mismatch: textual shortening is not a fidelity check.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Summary string and updated covered-turn count; optional saved summary artifact.
- Later read-back: Task plus WORK LOG and verbatim tail are delivered to subsequent Actor calls and potential resume handoff.
- Delegated visibility: Summarizer gets current log and selected older turns after head/tail elision, not necessarily complete source traces.
- Selection predicate: Code chooses oldest eligible pairs and keep-tail thresholds; model selects semantic content; empty completion selects deterministic fallback.
- Invalidation or expiry: New summary replaces prior log; caps and folding remove visible detail, with machine reprobe rather than automatic full-transcript reload promised.
- Activation or effect: Later context replacement is wired; semantic effect and fidelity are unobserved.
- Evidence limits: Omitted caveats can change meaning even under deterministic shortening; no source-wide warrant preservation follows.

SRC-1, `core/loop.py`:

> return s[:head] + "\n…[trace middle elided]…\n" + s[-tail:]
> --- `core/loop.py`

> + " ".join(str(m["content"]).split())[:digest_chars] for m in msgs)
> --- `core/loop.py`

Concrete implementation deduction: `_fold_input("AANNBB", head=2, tail=2)` returns `AA`, the fixed middle-elision marker, and `BB`, omitting `NN`. `_digest_lines` with a user content `claim is false` and digest_chars=5 returns `[env] claim`. These pure text projections are not executed here; the inspected slices establish their lossiness. They license neither a claim that `claim` is true nor faithful preservation of a negation. No accepted entailed factual inference is established by these transformations.

#### EPI-RTE-memory-proposal
Label: Terminal memory proposal

Part of: [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission)

Terminal PASS/FAIL plus Actor trajectory → same Actor distillation → whole-corpus reconciliation → diagnosis. Object: [EPI-OBJ-memory](#epi-obj-memory); diagnosis is a separate model-interpreted handoff to Curriculum. Content/update relation: truth-apt transformation: indeterminate. Requests allow acquisition, reshaping, warranted deductions and conjectures, but no particular output establishes non-entailment; unknown is not automatically ampliative conjecture. Target: future-useful advice with scope/causal support appropriate to trajectory evidence. Actor proposes, investigates and decides readiness; neither Verifier nor Curriculum grades memory, and there is no per-content human approval or expected memory answer. Operational force: Actor may change/delete its draft bank before host publication; requested criticism can change future guidance, but no automatic claim-level withdrawal registry is implemented here. Claim: [EPI-CLM-knowledge-feedback](#epi-clm-knowledge-feedback). Mismatch: checking a task outcome does not establish an explanatory rule.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated draft guest tree, continued Actor history and separate learning diagnosis.
- Later read-back: Host can install the tree for later Actors; Curriculum receives diagnosis and outcomes separately.
- Delegated visibility: Same Actor keeps trajectory and final report; fresh readers do not automatically inherit their supporting evidence.
- Selection predicate: Grounded terminal outcomes and phase policy trigger learning; Actor chooses content, representation and stopping point.
- Invalidation or expiry: Reconciliation explicitly requests narrowing/removal of contradicted or unsupported old claims; actual changes require model action.
- Activation or effect: Source requests content-directed criticism and tree editing before publication; observed semantic revision is unavailable.
- Evidence limits: No candidate lesson, evidence-linked acceptance decision or subsequent uptake is supplied.

SRC-1, `explore/charter.py`, `explore/target_learning.py`:

> The Verifier Agent
> establishes what was or was not verified; it does not establish why your approach
> succeeded or failed. Make causal claims only when your trajectory and evidence
> support them, and preserve uncertainty where they do not.
> --- `explore/charter.py`

> Your first-pass memory update is a draft and has not been promoted.
> --- `explore/charter.py`

> Look for conflicting assertions,
> unsupported causal explanations, stale environment assumptions, and conclusions
> broader than the observed evidence.
> --- `explore/charter.py`

Theory account: [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission) owns the enclosing theory/self-improvement assessment. For this proposal part, theory-builder conditions 1–4 separately remain: condition 1 conclusion status: afforded (files can carry whole statements); condition 2 conclusion status: claimed (future semantic use instructed, not observed); condition 3 conclusion status: claimed (above criticism instructions, no completed instance); condition 4 conclusion status: wired (published tree has next-round delivery). Whole files are addressable/revisable; claim segmentation is not enforced. Horizon can span problems through the host bank. Learning as improved capacity and reflection's two causal directions are not established; reflective method criticism and autonomous exercise of all conditions are not demonstrated. Retention and computational role assignment alone do not change these findings.

#### EPI-RTE-memory-admission
Label: Memory boundary admission

Part of: [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission)

Draft tree → host shingle audit → accepted subset → exact-tree equality gate. Object: [EPI-OBJ-memory](#epi-obj-memory). Content/update relation: no content change on successful exact-tree admission; rejection can filter files internally, but this promotion caller refuses the changed tree. Target/domain: overlap with host-only instruction corpus subject to authorized-target exceptions and corpus presence/provenance controls. Code decides/vetoes, Actor proposes the tree; operator launch is not human semantic approval. Result is admission or boundary exception. Epistemic authority: no truth, causal or transfer certificate. Operational authority: enforcing gate to host journal/install for future Actor guidance; unaccepted partial tree is not silently installed by this caller. Claim: [EPI-CLM-knowledge-feedback](#epi-clm-knowledge-feedback). Mismatch: “accepted_memory” is a transport/leakage term, not evidence-consuming acceptance of each claim.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Accepted tree or PracticeBoundaryError; audit rejection logged host-side.
- Later read-back: Only successful publication reaches later bank consumers; rejection logs are not agent feedback in silent_audit.
- Delegated visibility: Host corpus and rejection detail remain host-side; authorized instruction influences allowed overlap.
- Selection predicate: Eight-word shingle overlap minus authorized exact/near exceptions; target-aware call requires corpus and equality with candidate tree.
- Invalidation or expiry: New candidate must pass again; missing required corpus and changed subset block this publication.
- Activation or effect: Gate permits or blocks journal/install, not semantic reliance certification.
- Evidence limits: Near-shingle helper body not directly inspected here; lexical leakage audit cannot prove factual truth or absence of all leakage.

SRC-1, `explore/commit.py`:

> hits = {
>     gram for gram in (_shingles(text) & corpus) - authorized
>     if not _authorized_near_shingle(gram, authorized_words)
> }
> --- `explore/commit.py`

SRC-1, `explore/target_learning.py`:

> if accepted_memory != candidate_memory:
>     raise PracticeBoundaryError("terminal memory failed the target boundary")
> --- `explore/target_learning.py`

Counterexample to semantic certification: arbitrary false advice with no forbidden corpus overlap is not rejected for falsity by this implementation. This is an implementation-domain limit, not a claim that such a lesson was generated or installed. Generic silent_audit can pass through when corpus is absent and not required; the inspected target-learning caller explicitly requires it, so that alternative does not defeat this caller's presence gate.

#### EPI-RTE-bank-retention
Label: Bank journal installation

Part of: [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission)

Admitted complete tree → host journal → canonical bank install → inventory/upload on later attempts. Object: [EPI-OBJ-memory](#epi-obj-memory). Content/update relation: no content change in byte-tree installation. Target: retain the selected complete bank, not decide whether its claims are true. Host code owns file operations; semantic readiness was Actor-owned. Trigger is successful terminal proposal and boundary admission. Force: enforcing byte installation and advisory downstream model guidance through [RT-BAP-actor-method](runtime.md#rt-bap-actor-method), across tasks until replacement/freeze. Epistemic authority: retained fallible advice, with source warrant unknown after model distillation unless specific lineage is supplied. Claim: [EPI-CLM-knowledge-feedback](#epi-clm-knowledge-feedback). Mismatch: retention and reorganization alone are not post-acceptance lifecycle integration.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Installed tree, diagnosis and continued Actor history.
- Later read-back: Later practice/target/frozen evaluation attaches the bank, supplies inventory and permits Actor-chosen reads.
- Delegated visibility: Later fresh Actors see selected memory text, not automatically the trajectory; diagnosis goes to Curriculum through its own channel.
- Selection predicate: Complete tree must survive the admission gate before journal/install; later file selection is Actor-owned.
- Invalidation or expiry: Whole-tree replacement can remove stale files; journal and backups support recovery; phase-3 host bank is frozen with no writeback.
- Activation or effect: Durable installation and later delivery are wired; actual semantic use and improved outcomes remain unobserved.
- Evidence limits: Filesystem rename recovery does not imply always-visible crash-proof swaps; guest-copy immutability and delivery differ by task path as supplied in runtime.

SRC-1, `explore/target_learning.py`:

> hooks.install_memory(str(memory_dir), accepted_memory)
> return accepted_memory, diagnosis, actor_history
> --- `explore/target_learning.py`

Installer, journal and recovery evidence is retained by [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission). This part retains that container's rollback/recovery limits without inventing semantic rollback of downstream actions.

#### EPI-RTE-official-score
Label: Official score import

Part of: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

Completed worker → safe-to-grade and output-collection gate → reference staging → external evaluate → numerical validation → result.json. Object: [EPI-OBJ-evaluation-score](#epi-obj-evaluation-score). Content/update relation: truth-apt transformation: acquisition/import, external evaluator warrant unknown. Target/domain: benchmark output score for baseline/phase3, not the Verifier's reasoning or general task competence. Host code controls admission and external benchmark evaluator judges. Criterion: confirmed rollback, collected output, no evaluator error, finite numeric score in [0,1]. Intended use: archived benchmark outcome/reporting, not a live Actor answer oracle. Operational force: enforcing error/score publication gates and later cohort reporting; learning phases instead require zero official evaluator calls. Claim: [EPI-CLM-reported-scores](#epi-clm-reported-scores). Mismatch: score shape validation does not validate benchmark semantics.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Official evaluation artifact and score in result, or error.
- Later read-back: Archived scores feed report collection; official outcomes are not routed into the inspected learning loop.
- Delegated visibility: External driver gets staged candidate/reference; worker's local completion is insufficient to establish score.
- Selection predicate: Baseline/phase3 and safe_to_grade plus successful collection admit evaluator call; errors or missing/invalid score block completion.
- Invalidation or expiry: Rollback not confirmed blocks grading; retry/regrade does not make an old local judgment a new verified lesson.
- Activation or effect: Host can publish completed scored result; actual evaluator calls and outcome quality are unobserved.
- Evidence limits: External evaluator internals and runtime environment unavailable within frozen source; no causal component inference.

SRC-1, `benchmarks/ale/host.py`:

> if not result.get("safe_to_grade"):
>     raise RuntimeError(
>         "Candidate rollback not confirmed; grading blocked"
>     )
> --- `benchmarks/ale/host.py`

> evaluation = await asyncio.wait_for(driver.evaluate(), timeout=7200)
> --- `benchmarks/ale/host.py`

> elif (
>     not result.get("transition_ready")
>     or result.get("official_evaluator_calls") != 0
> ):
>     raise RuntimeError("Learning phase is not transition-ready")
> --- `benchmarks/ale/host.py`

#### EPI-RTE-score-report
Label: Cohort score reporting

No counterpart after comparison with [RT-RTE-task-execution](runtime.md#rt-rte-task-execution): this independently exposed CLI operation consumes archived scores rather than executing/grading the task. CLI `report` → collect archived baseline/phase3 result.json → duplicate and numeric checks → cohort arithmetic → stdout/summary/CSV. Object: [EPI-OBJ-evaluation-score](#epi-obj-evaluation-score). Content/update relation: truth-apt transformation: entailed derivation for computed counts/means conditional on correct loaded cohort, scores and interpretation; selected per-task rows are non-ampliative reshaping. Target/domain: finite numeric scores and complete-cohort accounting. Evaluator: deterministic Python checks/arithmetic, not a semantic or causal evaluator. No per-result human approval or expected-answer oracle; user chooses archive roots and must explicitly resolve duplicate attempts. Criterion is score range and unique source per task/arm. Force is enforcing refusal on duplicate source or invalid score, then informational publication. Epistemic license: these numerical summaries of these inputs only; not causation or source truth. Claim: [EPI-CLM-reported-scores](#epi-clm-reported-scores). Mismatch: installed report operation is not proof of manuscript-table provenance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Summary stdout and optional summary.json/tasks.csv.
- Later read-back: inapplicable — no later model invocation or adaptive consumer of the published aggregate is wired in this inspected report module.
- Delegated visibility: User supplies archive directories; output preserves per-task score-source paths, not underlying task evidence.
- Selection predicate: Locked task cohort and baseline/phase3 paths; missing scores omitted from available mean and separately counted.
- Invalidation or expiry: Distinct duplicate source paths raise instead of selecting the best score; complete mean is withheld unless all 67 are present.
- Activation or effect: Publication/refusal changes available reporting artifacts, not agent policy or bank content.
- Evidence limits: Arithmetic is conditional on imported file truth and locked cohort; no execution or causal contrast supplied.

SRC-1, `benchmarks/ale/report.py`:

> if source and source != str(path):
>     raise RuntimeError(
>         f"Duplicate {arm} evaluations for {task}; explicitly resolve attempts before merging"
>     )
> --- `benchmarks/ale/report.py`

> "complete_cohort_mean_score": sum(scores) / 67
> if len(scores) == 67
> else None,
> --- `benchmarks/ale/report.py`

Implementation deduction: if exactly one archived score equals 1, full_credit is 1, observed_full_credit_over_67 is 1/67, mean_available_score is 1, and complete_cohort_mean_score is None. These are distinct propositions and horizons. The derivation does not license “the whole cohort averaged 1.” No inputs were fabricated or target functions executed.

### Claims

#### EPI-CLM-knowledge-feedback
Label: Verification-grounded reusable knowledge

Part of: [RT-CLM-training-free](runtime.md#rt-clm-training-free)

This narrower claim concerns the claimed content/warrant transfer, rather than parameter constancy or the entire improvement thesis. SRC-1, `README.md`, doctrine/design:

> Verifier Agent to discover how an environment works, check what they learn against actual execution,
> and retain reusable knowledge in persistent memory.
> --- `README.md`

The implemented verification-to-distillation connection supports a request for grounded lessons; task verdict, semantic memory acceptance and transfer are different objects. Counterevidence to an infallible reading is the authors' own limitation:

> Its failure analysis identifies three limits to improvement: practice can miss
> the relevant weakness, verification can accept incomplete work, and memory can
> preserve an incorrect rule.
> --- `README.md`

No memory instance proves accepted knowledge production. This qualifies the warrant, not the presence of the learning machinery.

#### EPI-CLM-reported-scores
Label: Reported RSI outcome gains

Distinct from [RT-CLM-training-free](runtime.md#rt-clm-training-free): this is a numerical reported-outcome claim, not the architectural fixed-parameter thesis. SRC-1, `README.md`, reported operation:

> | OSWorld 2.0 · 0808 offline · 82 tasks | 71.97 | **78.98** |
> | Agents' Last Exam · Near-term · 67 tasks | 83.75 | **84.82** |
> --- `README.md`

The comparison is not a matched repeated-run component experiment:

> The RSI column includes selected retries and
> checkpoints with differing budgets; it is not an average over matched repeated
> runs.
> --- `README.md`

No supplied execution artifacts authenticate these aggregates or connect them to the frozen report implementation. They support attributed outcome reports, not a causal memory effect, semantic lesson quality or critic effectiveness.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
