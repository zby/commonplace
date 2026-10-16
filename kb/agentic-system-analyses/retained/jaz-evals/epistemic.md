---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "jaz-evals epistemic routes: benchmark verdicts, trace-conditioned advice, structural admission and later reliance."
run-id: AAS-2026-10-15-jaz-evals-17ab95f93794-01
reviewed-boundary: "2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72"
---

# jaz-evals epistemic report

## Source-and-claim boundary

The question is which routes turn benchmark interaction into checked outcomes or advice that can affect later solvers, and what reliance those checks license. The target is the shipped evaluation workflow, not the external JAZ runtime. Scope, revision, exclusions and evidence identity are as in the [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register). All new inspection below is SRC-1 implementation or doctrine/design at the frozen commit. No target execution, observed run or causal experiment is supplied.

The strongest explicit improvement-method claim is [RT-CLM-ttsi-experiment](runtime.md#rt-clm-ttsi-experiment). ACE's own claim and deliberately advisory authority are [EPI-CLM-playbook-advice](#epi-clm-playbook-advice). Benchmark scores, usable advice, and warranted general explanations are different targets. Checking the first does not accept the other two.

| Entry point or operation | Source path | Coverage and record | Limit and conclusion prevented |
| --- | --- | --- | --- |
| Installed CLI, configuration and central grading | SRC-1 `pyproject.toml`, `src/jaz_evals/cli.py`, `src/jaz_evals/eval_harness.py` | Supplied [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt); entry-point metadata directly searched | No execution or result archive; no actual scores verified |
| All five registered harnesses | SRC-1 `src/jaz_evals/harnesses/__init__.py` | Direct registration search agrees with supplied [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue), [RT-RTE-fresh-session](runtime.md#rt-rte-fresh-session), [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation), [RT-RTE-letta-bridge](runtime.md#rt-rte-letta-bridge), [RT-RTE-smolagents-chain](runtime.md#rt-rte-smolagents-chain) | External model/runtime decisions opaque; delivery is not semantic uptake |
| Host tools, hooks and return checks | SRC-1 `src/jaz_evals/env.py`, `src/jaz_evals/hooks.py`, `src/jaz_evals/harnesses/jaz_harness.py` | Supplied [RT-OBJ-agent-env](runtime.md#rt-obj-agent-env), [RT-RTE-codeact-filter](runtime.md#rt-rte-codeact-filter), [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue) | Not independently re-audited here; queue completion is not correctness, AppWorld early-return caveat retained |
| AppWorld submission, grading, cleanup and score | SRC-1 `src/jaz_evals/envs/appworld.py` | Direct reads of completion, evaluation, tracker conversion, failure truncation, cleanup and score; [EPI-RTE-appworld-check](#epi-rte-appworld-check), [EPI-RTE-appworld-disposition](#epi-rte-appworld-disposition) | Native grader, tasks and world internals unavailable; criterion validity unverified |
| StuLife feedback and task disposition | SRC-1 `src/jaz_evals/envs/stulife.py` | Direct completion scoring/return branch; [EPI-RTE-stulife-feedback](#epi-rte-stulife-feedback) | Other scoring branches supplied only by runtime or uninspected; no complete grader-validity claim |
| ACE feedback, reflection, proposal and advice use | SRC-1 `src/jaz_evals/harnesses/ace.py` | Direct `_adapt`, `_feedback`, solver prompt; supplied lifecycle [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation) | No generated reflection or bullet linked to an execution; truth-apt content of particular model output not determinable |
| ACE validation, rendering, additions and deduplication | SRC-1 `src/jaz_evals/harnesses/ace_playbook.py`, `src/jaz_evals/harnesses/ace_dedup.py` | Direct parser/validation/add/strip branches and similarity/group/merge/encoder construction; [EPI-RTE-curator-check](#epi-rte-curator-check), [EPI-RTE-curator-admission](#epi-rte-curator-admission), [EPI-RTE-count-reshape](#epi-rte-count-reshape), [EPI-RTE-dedup-check](#epi-rte-dedup-check), [EPI-RTE-dedup-replacement](#epi-rte-dedup-replacement) | Similarity is not semantic equivalence; model merge fidelity unverified |
| Post-run analysis and log viewers | SRC-1 `src/jaz_evals/analyze_cli.py`, `pyproject.toml` | Direct analysis main/metadata; [EPI-RTE-analysis-report](#epi-rte-analysis-report); viewer implementation uninspected | Printed diagnostics do not themselves retrain or admit advice; detailed diagnostic validity and viewer transformations unassessed |
| Official AppWorld driver | SRC-1 `scripts/run_appworld_official_react.sh` | Supplied [RT-RTE-official-baseline](runtime.md#rt-rte-official-baseline) | Native evaluator and resume semantics unavailable |
| Plot/table/release consumers, patches and other prompts | SRC-1 `scripts/`, `tables/`, `src/jaz_evals/`, `prompts/` | Included but remaining implementations uninspected here, as bounded in supplied reports | Prevents system-complete negatives, historical-result reconstruction, exhaustive withdrawal/publication or cross-method knowledge claims |

No new source is registered. Missing external runtime implementations prevent assessments of their internal memory acceptance, compaction fidelity and parametric updates; missing benchmark implementations/data prevent grading-validity conclusions. Missing linked run evidence prevents attribution of any particular advice, actual rejection, acceptance, activation or benefit. Readable uninspected material above is not an access gap or an evidenced absence.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-task-verdict](#epi-obj-task-verdict) | Task passed/failed, assertions, score/reason | see record | SRC-1 `src/jaz_evals/envs/appworld.py`, `src/jaz_evals/envs/stulife.py` | Runtime grader truth not verified |
| [EPI-OBJ-ace-playbook](#epi-obj-ace-playbook) | Potential strategies and causal diagnoses; imperatives can instead be non-truth-apt policy | see record | SRC-1 `src/jaz_evals/harnesses/ace.py` | No generated instance; classification of particular advice not determinable |
| [EPI-OBJ-curator-payload](#epi-obj-curator-payload) | Proposed advice plus reasoning; syntax fields themselves are control data | see record | SRC-1 `src/jaz_evals/harnesses/ace_playbook.py` | Structural validity does not imply justified advice |
| [RT-OBJ-agent-env](runtime.md#rt-obj-agent-env) | None in the tool view itself; tool outputs can carry propositions | see record | see record | No inference of grader secrecy |
| [RT-CMP-lite-llm](runtime.md#rt-cmp-lite-llm), [RT-CMP-lite-llm-model](runtime.md#rt-cmp-lite-llm-model), [RT-CMP-letta-model](runtime.md#rt-cmp-letta-model) | Particular distributed-parametric content not individuable here | see records | see records | Provider state and generated content uninspected |
| [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer) | Dense similarity representations, not independently stated claims | see record | see record | Not a truth evaluator |

## Authority-route ledger

Fields owned by declaring records are referenced rather than recopied. No ledger row asserts observed operation. In the following table, “see” refers to the linked route record in that row. Content relations describe the edge, not a system-wide capability.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs | Mismatch marker | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-appworld-check](#epi-rte-appworld-check) | check/evidence production | implemented | [EPI-OBJ-task-verdict](#epi-obj-task-verdict) | truth-apt transformation: acquisition/import | see | see | see | see | see | External grader result, warrant unknown | see | see | see | none | none | Grader internals unavailable |
| [EPI-RTE-appworld-disposition](#epi-rte-appworld-disposition) | operational admission/selection/consumption | implemented | [EPI-OBJ-task-verdict](#epi-obj-task-verdict) | no content change | see | see | see | see | see | No general explanation accepted | see | see | see | none | none | Failure and grader error both advance |
| [EPI-RTE-stulife-feedback](#epi-rte-stulife-feedback) | operational admission/selection/consumption | implemented | [EPI-OBJ-task-verdict](#epi-obj-task-verdict) | no content change | see | see | see | see | see | Correctness withheld from agent | see | see | see | none | none | Detailed grader validity unassessed |
| [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue) | content transformation | implemented | revised guidance/helpers; see | truth-apt transformation: indeterminate | see | see | see | see | see | Candidate generation, not warranted generalization | see | see | see | [RT-CLM-ttsi-experiment](runtime.md#rt-clm-ttsi-experiment) | Requested veto not independently enforced | Prompt-following and particular content unobserved |
| [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation) | content transformation | implemented | [EPI-OBJ-ace-playbook](#epi-obj-ace-playbook) | truth-apt transformation: indeterminate | see | see | see | see | see | Model interpretation, not an oracle | see | see | see | [EPI-CLM-playbook-advice](#epi-clm-playbook-advice) | none | Novelty request alone does not prove non-entailment |
| [EPI-RTE-curator-check](#epi-rte-curator-check) | check/evidence production | implemented | [EPI-OBJ-curator-payload](#epi-obj-curator-payload) | no content change | see | see | see | see | see | Payload shape/section domain only | see | see | see | none | none | Not a content test |
| [EPI-RTE-curator-admission](#epi-rte-curator-admission) | disposition/acceptance | implemented | [EPI-OBJ-curator-payload](#epi-obj-curator-payload) | no content change | see | see | see | see | see | Structural admission, not epistemic acceptance | see | see | see | none | none | No evidence-consuming generality gate |
| [EPI-RTE-count-reshape](#epi-rte-count-reshape) | content transformation | implemented | [EPI-OBJ-ace-playbook](#epi-obj-ace-playbook) | truth-apt transformation: non-ampliative reshaping | see | see | see | see | see | Advice body unchanged on checked domain | see | see | see | none | none | Metadata is removed |
| [EPI-RTE-dedup-check](#epi-rte-dedup-check) | check/evidence production | implemented | [EPI-OBJ-ace-playbook](#epi-obj-ace-playbook) | no content change | see | see | see | see | see | Similarity, not equivalence or truth | see | see | see | none | none | Greedy groups can overlap |
| [EPI-RTE-dedup-replacement](#epi-rte-dedup-replacement) | content transformation | implemented | [EPI-OBJ-ace-playbook](#epi-obj-ace-playbook) | truth-apt transformation: indeterminate | see | see | see | see | see | No checked meaning-preservation | see | see | see | none | none | Merge-free branch is deletion; model branch may alter claims |
| [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation) | retention | implemented | [EPI-OBJ-ace-playbook](#epi-obj-ace-playbook) | no content change | see | see | see | see | see | Retention alone adds no warrant | see | see | see | none | none | Not lifecycle integration after epistemic acceptance |
| [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation) | operational admission/selection/consumption | implemented | [EPI-OBJ-ace-playbook](#epi-obj-ace-playbook) | no content change | see | see | see | see | see | Advisory, not authoritative | see | see [RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance) | see | [EPI-CLM-playbook-advice](#epi-clm-playbook-advice) | none | Delivery does not prove dependence |
| [EPI-RTE-analysis-report](#epi-rte-analysis-report) | check/evidence production | implemented | retained attempt evidence | truth-apt transformation: indeterminate | see | see | see | see | see | Diagnostics bounded by uninspected helpers | see | see | see | none | none | No automatic update consumer in inspected main |
| [RT-RTE-codeact-filter](runtime.md#rt-rte-codeact-filter) | operational admission/selection/consumption | implemented | current history/input bindings | non-truth-apt policy/content update: visibility restriction | see | see | see | see | see | No truth check | see | see | see | none | none | Other message content survives |

The JAZ batch-test/discard discipline remains doctrine-only as an independent **acceptance gate**: [RT-CLM-ttsi-experiment](runtime.md#rt-clm-ttsi-experiment) states it; [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue) affords model execution without independently enforcing experimental comparisons. This does not negate the implemented invocation route. No source-supported entailed derivation from independently warranted task premises, accepted ampliative claim, or subsequent epistemic lifecycle integration is established in the inspected routes. Uninspected material prevents upgrading that bounded finding to system-wide absence.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-ttsi-experiment](runtime.md#rt-clm-ttsi-experiment) | see record | see record | see record | [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue) | None supplied | No controlled comparison supplied; task order, other changes and shared state complicate attribution | Improvement-directed delegation and requested hypothesis/test/discard discipline | Actual tests, rejected changes and benefit unknown; no independent gate |
| [EPI-CLM-playbook-advice](#epi-clm-playbook-advice) | see record | see record | see record | [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation), [EPI-RTE-curator-admission](#epi-rte-curator-admission), [EPI-RTE-dedup-replacement](#epi-rte-dedup-replacement) | None supplied | A frozen tail can be configured, but is not itself a causal experiment or validated advice | Trace-conditioned advice is admitted and delivered with explicitly advisory force | Successful improvement and semantic correctness unestablished; source does not promise authoritative knowledge |

## Bounded conclusion

**Benchmark outcome measurement is implemented, but its license is local.** AppWorld imports a native grader verdict, preserves selected structured fields, trims long failure traces, records errors as failures, and consumes results for scores and agent feedback. It advances and tears down the task regardless of success. StuLife retains score and reason but deliberately withholds them from the agent; ACE cannot recover those omitted fields. A claim that every adaptation receives grading feedback is false for this inspected branch. The external grader's source warrant is unknown, and a task pass does not warrant a causal diagnosis or transferable strategy. See [EPI-RTE-appworld-check](#epi-rte-appworld-check), [EPI-RTE-appworld-disposition](#epi-rte-appworld-disposition) and [EPI-RTE-stulife-feedback](#epi-rte-stulife-feedback).

**Advice gains operational availability without epistemic acceptance.** ACE requests diagnoses and additions from task/trajectory/feedback, structurally validates the reply, admits ADD content, optionally removes or replaces similarity-group members, retains snapshots and renders the result to later solvers. Structural admission enforces a payload contract, not a named evidential criterion for truth or transfer. The later solver is explicitly told to ignore inapplicable advice. Thus the update consumer has enforcing syntax rules, while the later decision consumer receives advisory text. Particular output could contain truth-apt conjectures or only imperative policies; no generated instance settles that question, entailment or non-entailment. See [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation), [EPI-RTE-curator-check](#epi-rte-curator-check), [EPI-RTE-curator-admission](#epi-rte-curator-admission), [EPI-RTE-dedup-replacement](#epi-rte-dedup-replacement) and [RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance).

**Cleanup is neither truth checking nor universal withdrawal.** Parser failures keep prior advice; unknown sections drop only affected additions. Merge parsing failure keeps the entire group, whereas merge-free dedup deliberately discards nonleaders. A similarity pass does not withdraw false claims on evidence. Count stripping demonstrably preserves advice bodies but removes unused counters; model merging has no corresponding semantic-preservation check. No accepted-claim lifecycle integration is established by these operations. See [EPI-RTE-count-reshape](#epi-rte-count-reshape), [EPI-RTE-dedup-check](#epi-rte-dedup-check) and [EPI-RTE-dedup-replacement](#epi-rte-dedup-replacement).

**Improvement properties remain independent.** JAZ guidance requests content-directed criticism and tests; ACE supplies a trace-fed organizational update path and repeated advice delivery. Their supplied theory, reflection and dispositional self-change assessments remain those in [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue) and [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation). Missing authored candidates prevents establishing particular formulated criticism; missing subsequent dependence prevents exercised self-improvement attribution (especially causal link 4); missing comparisons prevents improved future capacity or successful improvement. None of these gaps cancels the implemented adaptation path. Remote parameters and encoder weights have the separate fixity limits in the component records; no inspected caller updates weights, but this does not deny context-mediated change. Analysis reports and official-driver diagnostics add reporting channels, not demonstrated acceptance or automated semantic repair. The uninspected published-result and external-runtime routes preclude a single system-wide epistemic verdict.

## Shared records

### Operative objects

#### EPI-OBJ-task-verdict
Label: Task verdict

Source-native identity: AppWorld `result` and StuLife `record`, specifically their outcome fields, separated from queue cursors. Representational form: symbolic Boolean/numeric fields plus natural-language reasons/assertion descriptions. Storage substrate: in-process dict/list and task-results JSONL. Distinct from [RT-OBJ-agent-env](runtime.md#rt-obj-agent-env), the tool view; it is output of environment tools rather than that view. Closest container route is [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt), not a duplicate object. SRC-1, `src/jaz_evals/envs/appworld.py`, `src/jaz_evals/envs/stulife.py`; passages and field selection below.

#### EPI-OBJ-ace-playbook
Label: ACE playbook

Source-native identity: `playbook` text, with counted stored bullets and count-stripped model-facing copies. Representational form: natural-language advice; symbolic headers, IDs and counters control local parsing. Storage substrate: in-process string, per-task/final files and optional seed file. This is distinct from the supplied tool-view object; it is state carried by [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation), whose retained passages establish writing and later delivery. Particular advice, its truth-aptness, and provenance beyond that pipeline remain unobserved. SRC-1, `src/jaz_evals/harnesses/ace.py`, `src/jaz_evals/harnesses/ace_playbook.py`. The checked rendering passage is in [EPI-RTE-count-reshape](#epi-rte-count-reshape).

#### EPI-OBJ-curator-payload
Label: Curator payload

Source-native identity: parsed curator `payload` and its `operations`; distinct candidate rather than the already admitted [EPI-OBJ-ace-playbook](#epi-obj-ace-playbook). Representational form: symbolic JSON operation envelope around model-interpreted reasoning and content. Storage substrate: model response/string, parsed dict/list, raw-call diagnostics supplied in [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation). No counterpart object is declared in the supplied runtime; it is an intermediate on that route. SRC-1, `src/jaz_evals/harnesses/ace.py`, `src/jaz_evals/harnesses/ace_playbook.py`; parser passages below.

### Routes

#### EPI-RTE-appworld-check
Label: AppWorld check

Part of: [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt)

Endpoints/progression: current world → `_world.evaluate()` → `_tracker_result` or error record. Owner: host environment invoking an external native grader. Target/domain: submitted answer and world state against that task's assertions. The native grader supplies expected outcomes; its validity is uninspected. `_tracker_result` converts structured fields, and `_failure` truncates long trace detail. Acquired content has unknown upstream warrant and degraded detail for long traces, not an independent derivation of correctness. No human per-verdict decision is wired. Mode: configured finite benchmark queue.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: success, counts, assertion descriptions and bounded failure details, or a success=False error record.
- Later read-back: result rows reach post-run scores/analysis; feedback can reach later model invocations through the supplied adaptation routes.
- Delegated visibility: completion exposes the result without task ID/index; expected-versus-actual detail may remain.
- Selection predicate: current open task on completion; normal grader response versus caught Exception.
- Invalidation or expiry: no re-evaluation of earlier verdicts in this inspected function; task teardown follows downstream.
- Activation or effect: verdict feeds the disposition route, scores and completion feedback; no actual invocation observed.
- Evidence limits: grader internals/task data unavailable; an error result is not evidence the solver's answer was false.

SRC-1, `src/jaz_evals/envs/appworld.py`:

> return _tracker_result(self._world.evaluate())
> --- `src/jaz_evals/envs/appworld.py`

> "success": bool(tracker.success),
> "num_passed": int(tracker.pass_count),
> "num_failed": int(tracker.fail_count),
> "passes": [str(entry.get("requirement", "")) for entry in tracker.passes],
> "failures": [_failure(entry) for entry in tracker.failures],
> --- `src/jaz_evals/envs/appworld.py`

> detail[:_MAX_FAILURE_DETAIL_CHARS] + "..." if len(detail) > _MAX_FAILURE_DETAIL_CHARS else detail
> --- `src/jaz_evals/envs/appworld.py`

#### EPI-RTE-appworld-disposition
Label: AppWorld disposition

Part of: [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt)

Endpoints/progression: evaluated result → internal/streamed row → close world, advance cursor → completion report and later score. Owner: environment Python code. Function: operational finality, not acceptance of a general explanation. Software decides continuation; neither model nor human approves each verdict. Mode and oracle: same benchmark as the check, with no additional evaluator. Criterion for task-credit reporting is recorded success over the whole selected queue; unsubmitted tasks count as failures. This criterion licenses a benchmark score, not replay safety, mechanism attribution or transfer. Force: enforcing queue advancement, informative feedback, later numeric reporting.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: result minus task identity, plus remaining count/next-step instruction.
- Later read-back: streamed/internal outcomes reach score and reporting; supplied adaptation can consume the returned feedback.
- Delegated visibility: agents receive outcome but not task identity fields; graders retain the full internal row.
- Selection predicate: any completed task, independent of verdict success.
- Invalidation or expiry: current world closes; `_close_world` suppresses teardown exceptions and clears references; no rollback on failed score.
- Activation or effect: advances after failure as after success, ending current task opportunity; no acceptance gate for later advice.
- Evidence limits: streamed write errors are suppressed; no historical rows supplied; native-world cleanup internals uninspected.

SRC-1, `src/jaz_evals/envs/appworld.py`:

> self._results.append(result)
> self._write_result(result)
>
> self._close_world()
> self._index += 1
> --- `src/jaz_evals/envs/appworld.py`

> return sum(1 for result in results if result.get("success")) / n_tasks
> --- `src/jaz_evals/envs/appworld.py`

#### EPI-RTE-stulife-feedback
Label: StuLife feedback boundary

Part of: [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt)

Endpoints/progression: selected scoring branch → correctness/score/reason retained → cursor advances → agent gets progress only. Owner: StuLife adapter; task-specific scoring is partly delegated to benchmark helpers. Target/domain: task credit, with distinct trigger, quiz and action branches. Software marks triggers successful and unacted driver-mode action tasks zero; these are not independent evidence for successful problem solving. Computational decision; no per-task human veto. Distinct part from AppWorld: feedback visibility differs materially. Mode: sequential benchmark episode; expected ground truth is used internally, not returned in completion.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: remaining count and next-step text, not outcome fields.
- Later read-back: retained correctness can feed grading/reporting, while ACE's feedback renderer drops the returned progress fields and yields no evaluation feedback.
- Delegated visibility: score, success and reason intentionally withheld from the agent-facing completion result.
- Selection predicate: scoring branch selected by task type, trigger status and whether driver-mode action occurred.
- Invalidation or expiry: submission final and cursor advances; no correctness-based retry in this return path.
- Activation or effect: enforces task finality without feedback-driven correction through this channel.
- Evidence limits: not all scoring helpers inspected; no inference that agents lack all other task evidence.

SRC-1, `src/jaz_evals/envs/stulife.py`:

> success = score == 1.0
> --- `src/jaz_evals/envs/stulife.py`

> # `success` is recorded on `record` above (for grading) but deliberately NOT returned to the
> # agent: echoing per-task correctness back is a ground-truth feedback leak -- it would let the
> # agent learn it got a quiz wrong and retry/steer, which the sequential episode must not allow.
> response: dict[str, Any] = {"tasks_remaining": tasks_remaining}
> --- `src/jaz_evals/envs/stulife.py`

SRC-1, `src/jaz_evals/harnesses/ace.py`:

> if key in ("success", "next_step", "tasks_remaining", "api_executions"):
>     continue
> lines.append(f"{key}: {value}")
> return "\n".join(lines) if lines else "(no evaluation feedback available)"
> --- `src/jaz_evals/harnesses/ace.py`

#### EPI-RTE-curator-check
Label: Curator structural check

Part of: [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation)

Endpoints/progression: model curation → extract JSON → validate reply/operations/allowed sections. Owner/evaluator: deterministic parser and `validate_operations`. Target/domain: operation envelope shape, required fields, ADD-only opcode and section whitelist. Content need only be present; the inspected validator does not assess its truth or task-general usefulness. No human gate or answer oracle for advice. Mode: online bounded curriculum while adaptation enabled. Model proposes; software checks; disposition is separate below.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: kept operations or ValueError; JSON extraction can return None.
- Later read-back: inapplicable — this check has no separate accumulated memory; its admitted output proceeds to the application route.
- Delegated visibility: reflector/curator receive rendered context described in the supplied parent; later solvers do not receive a proof of advice validity.
- Selection predicate: presence/types of reasoning and operations; each operation must be an ADD with section/content and a whitelisted normalized section.
- Invalidation or expiry: unknown section is omitted with callback; malformed envelope/operation raises.
- Activation or effect: parse/check result controls whether software can append advice, not its epistemic truth.
- Evidence limits: syntactically acceptable wrong advice can pass; no generated payload supplied.

SRC-1, `src/jaz_evals/harnesses/ace_playbook.py`:

> if typed["type"] != "ADD":
>     raise ValueError(f"curator operation {index} has type {typed['type']!r}; only 'ADD' is supported")
> missing = {"type", "section", "content"} - set(typed)
> --- `src/jaz_evals/harnesses/ace_playbook.py`

> if normalize_section(section) not in ALLOWED_SECTIONS:
>     if on_unknown_section is not None:
>         on_unknown_section(section)
>     continue
> kept.append(typed)
> --- `src/jaz_evals/harnesses/ace_playbook.py`

#### EPI-RTE-curator-admission
Label: Curator admission

Part of: [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation)

Endpoints/progression: parser result → preserve old playbook or apply admitted ADDs → optional dedup → next playbook. Owner: Python `_adapt`. This is a disposition with structural criteria, not evidence-consuming acceptance of truth-apt advice. Reflector/curator model supplies diagnoses/proposals; software can veto malformed output, human only chooses configuration/seed. Trigger: each eligible completed task. Proposed change: additional advice bullets. Guidance and conditional theory/property assessments remain in the supplied parent; no independent generated theory is established here. Recovery is prior playbook on parse/validation failures, with diagnostics; the parent separately records outer adaptation-exception recovery. Appending is not semantic correction or withdrawal. Intended use: later task-solving assistance within the configured curriculum, not validated general knowledge.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: unchanged or newly appended playbook and next ID.
- Later read-back: changed advice reaches subsequent solver/adaptation prompts via the parent route.
- Delegated visibility: later solvers receive text, not structural-failure logs as a correctness certificate.
- Selection predicate: successful parse/validation and eligible adaptation index; no task-success threshold gates each advice item.
- Invalidation or expiry: invalid reply keeps prior state; unknown section drops only that item; later dedup can replace/delete members.
- Activation or effect: enforcing local write admission, advisory downstream prompt authority; behavioral effect unobserved.
- Evidence limits: no independent evidence test of advice generality or correctness; retention is not lifecycle integration after acceptance.

SRC-1, `src/jaz_evals/harnesses/ace.py`:

> except ValueError as exc:
>     _append_jsonl(ace_dir / "curator_failures.jsonl", {"task": index, "reason": str(exc)})
>     return playbook, next_id
>
> playbook, next_id = apply_add_operations(playbook, operations, next_id)
> --- `src/jaz_evals/harnesses/ace.py`

#### EPI-RTE-count-reshape
Label: Count-stripped rendering

Part of: [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation)

Endpoints/progression: counted playbook → `strip_counts` → model-facing playbook. Owner/evaluator: deterministic line matcher; target/domain is recognized bullet prefixes. This is non-ampliative reshaping for the advice body, not semantic summarization. Concrete source deduction, without execution: a matching line `[abc-00001] helpful=0 harmful=0 :: Keep receipts.` becomes `[abc-00001] Keep receipts.`; section headings and unmatched lines pass through. Dropping counts removes metadata, not the advice proposition. Counters carry no success license: the implementation comments state nothing increments them. Distinct from model merging below.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: joined model-facing string.
- Later read-back: rendered changed playbook reaches solver/reflector/curator in the supplied parent route.
- Delegated visibility: body and IDs remain; recognized helpful/harmful counters do not.
- Selection predicate: `_BULLET_COUNTS` match on each line.
- Invalidation or expiry: inapplicable — pure rendering creates no separate mutable store.
- Activation or effect: changes supplied model context; no observed behavioral effect.
- Evidence limits: guarantee applies to matched format, not arbitrary semantic equivalence of all possible seed text.

SRC-1, `src/jaz_evals/harnesses/ace_playbook.py`:

> for line in playbook.split("\n"):
>     match = _BULLET_COUNTS.match(line)
>     out.append(f"{match.group(1)} {match.group(2)}" if match else line)
> return "\n".join(out)
> --- `src/jaz_evals/harnesses/ace_playbook.py`

#### EPI-RTE-dedup-check
Label: Dedup similarity check

Part of: [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation)

Endpoints/progression: bullet bodies → normalized embeddings → similarity matrix → threshold groups. Owner: deterministic grouping over the distributed-parametric encoder's output. Target/domain: vector similarity of advice bodies, not truth, entailment, equivalence or benchmark success. Uses [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer); version/fixity limits remain there. No human per-group decision or advice oracle. Mode: optional dedup after additions. Grouping is greedy and order-dependent; a later member can occur in more than one group because the inner scan does not filter visited indices. Therefore even complete nonoverlapping partitioning is not licensed.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: groups of indices of length at least two.
- Later read-back: inapplicable — groups are immediate selectors for replacements, not separately retained guidance.
- Delegated visibility: merge model receives selected bullet text; later solver gets rebuilt result.
- Selection predicate: later-index similarity at least configured threshold; outer leaders skipped when visited.
- Invalidation or expiry: groups recomputed for the next playbook pass; no evidence-based falsity withdrawal.
- Activation or effect: ranking/selection for possible suppression or model merge, not semantic validation.
- Evidence limits: encoder semantics unverified; high similarity does not license interchangeable truth conditions.

SRC-1, `src/jaz_evals/harnesses/ace_dedup.py`:

> if i in visited:
>     continue
> similar = [j for j in range(i + 1, len(embeddings)) if similarity(i, j) >= threshold]
> if similar:
>     group = [i, *similar]
>     groups.append(group)
>     visited.update(group)
> --- `src/jaz_evals/harnesses/ace_dedup.py`

#### EPI-RTE-dedup-replacement
Label: Dedup replacement

Part of: [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation)

Endpoints/progression: similarity groups → keep leader without model, or request merged bullet → parse → rebuild playbook omitting absorbed members. Owner: Python with optional model author. This distinct transformation follows the check, not an evaluator of advice truth. Trigger: enabled dedup after update. Model guidance asks comprehensive concise preservation; no source comparison verifies it. Merge-free branch deletes selected nonleaders; model branch's content relation is indeterminate because neither semantic preservation nor non-entailment of a particular output is established. Neither branch accepts a new warranted claim. No human veto; software rejects unparseable merges. Mode: curriculum-local cleanup. Persists rebuilt advice for later solvers. Theory account remains in the parent; merging alone establishes no formulated criticism of a challenged theory.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rebuilt playbook plus before/after/failure counts.
- Later read-back: rebuilt result reaches later solver/adaptation invocations and snapshots through the parent route.
- Delegated visibility: merge model gets group text; downstream solver receives survivors, not all removed source bullets in its rendered advice.
- Selection predicate: similarity groups; no-model policy or parsed merged-bullet format decides replacement.
- Invalidation or expiry: parse failure leaves the whole group intact; parse success absorbs nonleaders; no semantic rollback test.
- Activation or effect: enforcing text deletion/replacement upstream of advisory delivery; actual behavioral dependence unobserved.
- Evidence limits: “merge” does not prove non-ampliative reshaping; no checked equivalence or generated merge is supplied.

SRC-1, `src/jaz_evals/harnesses/ace_dedup.py`:

> Merge them into ONE bulletpoint that captures all important information while removing redundancy.
> --- `src/jaz_evals/harnesses/ace_dedup.py`

> replacement[group[0]] = members[0]
> --- `src/jaz_evals/harnesses/ace_dedup.py`

> merged = parse_merged(merge(merge_prompt(members)))
> if merged is None:
> --- `src/jaz_evals/harnesses/ace_dedup.py`

> failed += 1
> continue
> replacement[group[0]] = merged
> absorbed.update(group[1:])
> --- `src/jaz_evals/harnesses/ace_dedup.py`

#### EPI-RTE-analysis-report
Label: Analysis report dispatch

Endpoints/progression: CLI target → discover attempt markers → invoke selected diagnostic helpers → print reports/JSON. Owner: local `analyze_cli.main`. Closest supplied record [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt) writes artifacts; this is a distinct later CLI consumer, not part of that invocation. Target/domain: retained trace/outcome diagnostics, not universal task truth or validity of an explanatory mechanism. Helper implementations remain partly uninspected. The main skips tool-name-dependent reports when tool names are unknown rather than manufacturing zeros. Human/operator supplies target; software selects helpers; printed output is advisory for operator interpretation. No automatic advice update or per-content acceptance is wired in inspected main.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: printed diagnostics and exit status; absent target returns failure.
- Later read-back: inapplicable — inspected main prints reports, not a changed artifact later reloaded as solver guidance.
- Delegated visibility: inapplicable — no solver delegation in this CLI main.
- Selection predicate: task-results or JAZ trace markers, tool-name availability, method-specific artifacts and non-None helper results.
- Invalidation or expiry: missing tool names suppress affected checks; no truth-based invalidation of stored task results here.
- Activation or effect: operator reporting channel, advisory force, horizon of inspection; no downstream automated behavioral effect established.
- Evidence limits: helper validity, historical inputs, plot/table/release consumers and operator uptake not verified.

SRC-1, `src/jaz_evals/analyze_cli.py`:

> if tool_names is None:
>     print("  (tool names unknown: pass --tool-names to include hygiene/transcript reports)")
> --- `src/jaz_evals/analyze_cli.py`

> for key, value in _extra_sections(attempt_dir).items():
>     print(_indent(f"{key}: {json.dumps(value, indent=2, sort_keys=True, default=str)}"))
> return 0
> --- `src/jaz_evals/analyze_cli.py`

### Claims

#### EPI-CLM-playbook-advice
Label: Playbook improvement and advisory use

Claimed operation: ACE improves a playbook from reflector diagnosis and curator additions; its solver-facing instruction explicitly limits reliance to applicable advice. Doctrine/design, SRC-1 `src/jaz_evals/harnesses/ace.py`. Closest supplied claim [RT-CLM-ttsi-experiment](runtime.md#rt-clm-ttsi-experiment) concerns JAZ's different batch optimization prompt, not this code-owned ACE cycle. Not a claim that every bullet is verified knowledge. The advisory boundary is implemented by text delivery, not reliable semantic compliance. Actual improved capacity is uninspected.

> ACE improves a *playbook*: a structured document of bullets that is prepended to every subagent's
> prompt. After each task a **reflector** diagnoses the trajectory and a **curator** proposes bullets to
> --- `src/jaz_evals/harnesses/ace.py`

> You have a playbook of accumulated guidance from earlier tasks. It is advisory, not authoritative: \
> follow it where it applies, and ignore any bullet that does not fit the task in front of you.
> --- `src/jaz_evals/harnesses/ace.py`
