---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Harness² epistemic routes: execution evidence, lesson warrant, operational admission and separate benchmark measurement."
run-id: AAS-2026-10-22-harness2-d5a180ba559c-01
reviewed-boundary: "1cfe254e8d25b15f37048c3730134686abe60335"
---

# Harness² epistemic report

## Source-and-claim boundary

The question is whether Harness²'s execution contrasts and reflection establish warranted reusable lessons, or primarily generate candidates with operational authority. Scope and exclusions follow the [boundary](boundary.md#boundary-and-evidence); evidence identities follow its [Source register](boundary.md#source-register). SRC-1 is the sole source. No supplied observed runs or causal experiments establish actual model criticism, lesson acceptance, later activation or improved capacity. External benchmark evaluators and provider internals are not frozen; their correctness and exact weight identity remain unassessed, not absent.

The supplied runtime is provisional implementation evidence. Direct additional reads below establish independent judging/reporting and the deterministic demo, which defeat a blanket claim that the system has no expected-answer check. They do not supersede the runtime's explicitly benchmark-scoped selector account. All new source reads are implementation evidence, except README and prompt passages, which supply doctrine/design or reported claims. Available but uninspected runner internals prevent a system-complete negative about all tool-level evaluators.

| Entry point or operation | Source path (SRC-1) | Coverage and records | Limit |
|---|---|---|---|
| Installed dispatch | `pyproject.toml` | Direct read: seven entry points | Dispatch is not observed execution |
| Sweep, agg/seq, proposal, solver, context transport | `harness2/cli/run_sweep.py`, `harness2/core/recursion.py`, `harness2/core/context.py`, `harness2/core/proposer.py` | Supplied [RT-RTE-task-recursion](runtime.md#rt-rte-task-recursion), [RT-RTE-solver-execution](runtime.md#rt-rte-solver-execution); context tripwire directly read | External tools, network and hidden reasoning uninspected |
| Proposed-tree admission, hooks and plugins | `harness2/core/tree.py`, `harness2/core/prompts.py`, `harness2/substrate/codex.py`, `third_party/wb_runner/agents/oc_harness_agent.py` | Supplied [RT-RTE-edit-admission](runtime.md#rt-rte-edit-admission), [RT-BAP-harness-consumption](runtime.md#rt-bap-harness-consumption) | Installation capability is not observed callback firing; arbitrary generated hook logic cannot be assessed without candidates |
| Output selection | `harness2/core/selection.py` | Supplied [RT-RTE-output-selection](runtime.md#rt-rte-output-selection); reflection/parser directly read | Artifact choice is not component-effect acceptance |
| Reflection, admission, library removal/index | `harness2/core/selection.py`, `harness2/core/library.py`, `harness2/core/prompts.py` | Direct reads: [EPI-OBJ-experience](#epi-obj-experience), [EPI-RTE-lesson-parse](#epi-rte-lesson-parse); supplied [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission) | Later semantic use unobserved |
| Resume | `harness2/core/schedule.py` | Supplied [RT-RTE-resume-reuse](runtime.md#rt-rte-resume-reuse) | Identity checks do not certify truth |
| Judge, including --bases | `harness2/cli/judge.py`, `harness2/core/judge.py`, `harness2/benchmarks/jobbench.py`, `harness2/benchmarks/lab.py`, `harness2/benchmarks/workbuddy.py` | Direct scoring/parser/merge reads: [EPI-RTE-judge-result](#epi-rte-judge-result), [EPI-RTE-score-cache](#epi-rte-score-cache) | Complete external rubrics, verifier internals and data unavailable |
| Report | `harness2/cli/report.py`, `harness2/core/report.py` | Direct read: [EPI-RTE-score-report](#epi-rte-score-report) | Reports conditioned on graded rows, not all attempted tasks |
| Demo | `harness2/cli/demo.py`, `harness2/demo.py` | Direct read: [EPI-RTE-demo-check](#epi-rte-demo-check), [EPI-OBJ-demo-ledger](#epi-obj-demo-ledger) | Scripted arithmetic example, not model efficacy evidence |
| Setup, check, bridge | `harness2/cli/setup.py`, `harness2/cli/check.py`, `harness2/cli/bridge.py` | Direct CLI reads: setup invokes install; check prints readiness without exercising model access; bridge writes endpoint configuration and execs LiteLLM | Installation/preflight internals not independently audited here; no conclusion that readiness proves semantic correctness or model accessibility |
| Remaining shipped overlays, baseline tools, tests and documentation | `third_party/`, `tests/`, `docs/` | Supplied boundary/runtime scope only except paths above | No exhaustive negative about every baseline evaluator, callback or test oracle; tests not run |

Consequential claims are [RT-CLM-answer-free](runtime.md#rt-clm-answer-free), [EPI-CLM-evidence-lessons](#epi-clm-evidence-lessons) and [EPI-CLM-benchmark-gains](#epi-clm-benchmark-gains).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-harness-text](runtime.md#rt-obj-harness-text) | Procedures may embed factual explanations; imperatives alone are not truth-apt | see record | see record | Generated content unavailable |
| [RT-OBJ-harness-code](runtime.md#rt-obj-harness-code) | Usually behavioral machinery rather than assertions | see record | see record | Code validity does not establish the truth of implicit domain assumptions |
| [EPI-OBJ-execution-evidence](#epi-obj-execution-evidence) | Task/source assertions, rendered actions/results, deliverable claims | see record | see record | Imported source warrant unknown; rendering may omit material |
| [EPI-OBJ-experience](#epi-obj-experience) | Claimed edit effects, transferable lesson, evidence and confidence | see record | see record | Model-written support labels are not independent corroboration |
| [EPI-OBJ-score-rows](#epi-obj-score-rows) | Counts/points and evaluator outcome for a particular run | see record | see record | Heterogeneous metrics; external evaluation validity uninspected |
| [EPI-OBJ-demo-ledger](#epi-obj-demo-ledger) | Signed amounts and derived total | see record | see record | Synthetic source, bounded arithmetic domain |
| [RT-CMP-proposer](runtime.md#rt-cmp-proposer), [RT-CMP-selector](runtime.md#rt-cmp-selector), [RT-CMP-solver](runtime.md#rt-cmp-solver), [RT-CMP-judge](runtime.md#rt-cmp-judge) | Individuated truth-apt parameter content not determinable | see records | see records | External distributed-parametric state; no inspected weight update path or exact weight pin |

## Authority-route ledger

Fields owned by a cited declaring record are given by reference. Content relations below assess edges, not the whole system. All routes are source-grounded capacities; none has observed-run support.

Route ID: [RT-RTE-task-recursion](runtime.md#rt-rte-task-recursion)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-harness-text](runtime.md#rt-obj-harness-text), [RT-OBJ-harness-code](runtime.md#rt-obj-harness-code), [EPI-OBJ-execution-evidence](#epi-obj-execution-evidence).
Content/update relation: non-truth-apt policy/content update: edited instructions and executable helpers; embedded truth-apt explanations remain indeterminate without candidate content.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route.
Epistemic authority and scope: candidate generation, not established warranted ampliation.
Operational authority; behavioral-authority path: see route and [RT-BAP-harness-consumption](runtime.md#rt-bap-harness-consumption).
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-evidence-lessons](#epi-clm-evidence-lessons).
Mismatch marker: none; gap/limit: request for contrastive reasoning is not observed criticism.

Route ID: [RT-RTE-edit-admission](runtime.md#rt-rte-edit-admission)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-harness-text](runtime.md#rt-obj-harness-text), [RT-OBJ-harness-code](runtime.md#rt-obj-harness-code).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route for structural/adapter/marker checks.
Epistemic authority and scope: bounded conformance only; no semantic truth or improvement license.
Operational authority; behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [RT-CLM-answer-free](runtime.md#rt-clm-answer-free).
Mismatch marker: none; gap/limit: validation and its downstream admission are separate functions of the same implementation.

Route ID: [RT-RTE-edit-admission](runtime.md#rt-rte-edit-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [RT-OBJ-harness-text](runtime.md#rt-obj-harness-text), [RT-OBJ-harness-code](runtime.md#rt-obj-harness-code).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route for acceptance, retry and fallback.
Epistemic authority and scope: admission of a runnable candidate, not an accepted causal explanation.
Operational authority; behavioral-authority path: see route and [RT-BAP-harness-consumption](runtime.md#rt-bap-harness-consumption).
Evidence source ID and local anchor: see route.
Claim IDs: none. Mismatch marker: none; gap/limit: inherited fallback can execute without a new successful edit.

Route ID: [RT-RTE-output-selection](runtime.md#rt-rte-output-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-execution-evidence](#epi-obj-execution-evidence).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route.
Epistemic authority and scope: task-deliverable preference; not evidence that the chosen harness caused superiority. The k=1 path is delivery without comparative evaluation.
Operational authority; behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-evidence-lessons](#epi-clm-evidence-lessons).
Mismatch marker: none; gap/limit: choice criterion is not an expected-answer oracle or controlled component comparison.

Route ID: [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-experience](#epi-obj-experience).
Content/update relation: truth-apt transformation: indeterminate. The model is asked to infer edit effects and transfer conditions; actual content is missing, so non-ampliative restatement, entailed inference and ampliative conjecture cannot be distinguished. A transfer claim beyond the observed tasks would require additional premises or be conjectural.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route and [EPI-RTE-lesson-parse](#epi-rte-lesson-parse).
Epistemic authority and scope: generated candidate explanations, not independently established acceptance.
Operational authority; behavioral-authority path: see route.
Evidence source ID and local anchor: see route and [EPI-OBJ-experience](#epi-obj-experience).
Claim IDs: [EPI-CLM-evidence-lessons](#epi-clm-evidence-lessons).
Mismatch marker: evidence-supported is requested, not machine-verified; gap/limit: no generated lesson supplied.

Route ID: [EPI-RTE-lesson-parse](#epi-rte-lesson-parse)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-experience](#epi-obj-experience).
Content/update relation: truth-apt transformation: indeterminate; a deterministic line parser can remove qualifying continuation lines. See the concrete deduction in the record.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: surviving strings retain model-attributed provenance but need not preserve complete meaning.
Operational authority; behavioral-authority path; evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-evidence-lessons](#epi-clm-evidence-lessons).
Mismatch marker: lossy parser; gap/limit: this is a reachable implementation case, not an observed malformed response.

Route ID: [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-experience](#epi-obj-experience).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route and [EPI-RTE-lesson-parse](#epi-rte-lesson-parse).
Epistemic authority and scope: required strings and marker exclusions license storage; the model is requested to abstain without a concrete reusable contrast. Code does not check cited evidence, confounding verdicts, confidence or whether the criterion was satisfied. No separate evidence-consuming acceptance of lesson truth is established by these gates.
Operational authority; behavioral-authority path; evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-evidence-lessons](#epi-clm-evidence-lessons).
Mismatch marker: requested warrant versus admission predicate; gap/limit: model compliance unobserved, not disproved.

Route ID: [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-experience](#epi-obj-experience), [RT-OBJ-harness-text](runtime.md#rt-obj-harness-text), [RT-OBJ-harness-code](runtime.md#rt-obj-harness-code).
Content/update relation: truth-apt transformation: non-ampliative reshaping; parsed fields are formatted into EXPERIENCE.md and cue into INDEX.md.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route and [EPI-OBJ-experience](#epi-obj-experience).
Epistemic authority and scope: operationally admitted library entry; retention does not establish epistemic acceptance or lifecycle integration after acceptance.
Operational authority; behavioral-authority path; evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-evidence-lessons](#epi-clm-evidence-lessons).
Mismatch marker: none; gap/limit: forget/retain delete entries and rebuild index, not retract a lesson from already copied contexts or undo descendant harnesses.

Route ID: [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-experience](#epi-obj-experience).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route for same-domain/mode preceding-task delivery.
Epistemic authority and scope: advisory evidence for another improver, not automatic installation or endorsement by future solvers.
Operational authority; behavioral-authority path: see route and [RT-BAP-harness-consumption](runtime.md#rt-bap-harness-consumption).
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-evidence-lessons](#epi-clm-evidence-lessons).
Mismatch marker: none; gap/limit: library delivery alone does not prove reading, reliance or improved capacity.

Route ID: [RT-RTE-resume-reuse](runtime.md#rt-rte-resume-reuse)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-execution-evidence](#epi-obj-execution-evidence), [EPI-OBJ-experience](#epi-obj-experience).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path; evidence source ID and local anchor: see route.
Epistemic authority and scope: identity/integrity predicates, not revalidation of truth or fixed provider state.
Claim IDs: none. Mismatch marker: none; gap/limit: recovery can reinstate operationally admitted content without a new semantic check.

Route ID: [EPI-RTE-judge-result](#epi-rte-judge-result)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-score-rows](#epi-obj-score-rows).
Content/update relation: truth-apt transformation: acquisition/import; warrant remains external and unverified, not upgraded by normalization.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-benchmark-gains](#epi-clm-benchmark-gains).
Mismatch marker: none; gap/limit: outcome evaluation cannot identify which edit caused success.

Route ID: [EPI-RTE-score-cache](#epi-rte-score-cache)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-score-rows](#epi-obj-score-rows).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-benchmark-gains](#epi-clm-benchmark-gains).
Mismatch marker: none; gap/limit: preserving a previous graded row against a failed re-judge is not withdrawal or fresh confirmation.

Route ID: [EPI-RTE-score-report](#epi-rte-score-report)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-score-rows](#epi-obj-score-rows).
Content/update relation: truth-apt transformation: entailed derivation; arithmetic aggregation follows imported numeric fields and the explicit graded-row predicate, not independently warranted benchmark truth.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-benchmark-gains](#epi-clm-benchmark-gains).
Mismatch marker: none; gap/limit: reporting warnings do not enforce an admissible comparison or remove mixed units.

Route ID: [EPI-RTE-demo-check](#epi-rte-demo-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-demo-ledger](#epi-obj-demo-ledger).
Content/update relation: truth-apt transformation: entailed derivation; signed Decimal sum under the supplied CSV interpretation.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see record.
Claim IDs: none. Mismatch marker: none; gap/limit: substring matching licenses less than whole-answer correctness and is bypassed by trivial selection at k=1.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-answer-free](runtime.md#rt-clm-answer-free) | see record | see record | see record | see record | none supplied | see record | Copied-context exclusions and tripwires, not universal contamination isolation | Reachable external acquisitions remain outside the gate |
| [EPI-CLM-evidence-lessons](#epi-clm-evidence-lessons) | see record | see record | see record | [RT-RTE-task-recursion](runtime.md#rt-rte-task-recursion), [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission), [EPI-RTE-lesson-parse](#epi-rte-lesson-parse) | none supplied | see record | Evidence-oriented generation and retention are wired | Neither supported causal effect nor transfer acceptance is established by entry membership |
| [EPI-CLM-benchmark-gains](#epi-clm-benchmark-gains) | see record | see record | see record | [EPI-RTE-judge-result](#epi-rte-judge-result), [EPI-RTE-score-cache](#epi-rte-score-cache), [EPI-RTE-score-report](#epi-rte-score-report) | none supplied | see record | Machinery can measure and report outcomes conditional on grader availability | Published gains and component attribution not reproduced |

## Bounded conclusion

Harness² separates behavioral admission from task-outcome measurement. Structural checks admit instructions and executable helpers; a selector delivers a final output; reflection proposes lessons; required text fields and marker checks admit entries for future improvers. These are real authority paths, but none alone establishes accepted knowledge about which edit worked or will transfer. The reflection prompt explicitly recognizes this distinction and requests confounding-aware abstention. See [RT-RTE-edit-admission](runtime.md#rt-rte-edit-admission), [RT-RTE-output-selection](runtime.md#rt-rte-output-selection), [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission) and [EPI-CLM-evidence-lessons](#epi-clm-evidence-lessons).

Acquired task/evidence warrant is unknown, not manufactured by context copying. Candidate lesson content is unavailable: one cannot identify an actual ampliative claim, its acceptance or post-acceptance integration. Even syntactically valid reflection may lose a qualifying continuation during parsing. Retention and index linkage precede any established epistemic acceptance; deletion prevents future library supply but does not undo descendant use. See [EPI-OBJ-execution-evidence](#epi-obj-execution-evidence), [EPI-OBJ-experience](#epi-obj-experience), [EPI-RTE-lesson-parse](#epi-rte-lesson-parse).

Independent judging has consequential report consumers, not a wired role as adaptation's answer oracle. Benchmark grades establish at most the external evaluator's scoped outcome; aggregation derives conditional means, excludes ungraded rows and can retain stale-but-graded results after re-judge failure. The deterministic demo does contain a source-derived answer check; that narrow counterexample prevents equating the framework with model judgment alone. See [EPI-RTE-judge-result](#epi-rte-judge-result), [EPI-RTE-score-cache](#epi-rte-score-cache), [EPI-RTE-score-report](#epi-rte-score-report), [EPI-RTE-demo-check](#epi-rte-demo-check).

Behavior/policy adaptation is wired independently of truth-apt learning: changed trees can enter fresh solver runs, and retained lessons can guide subsequent edits. Model parameters are externally hosted and not trained by inspected framework routes; internal content and weight identity remain opaque. The runtime's separate learning, reflection, theory-builder and dispositional self-change limits stand; there is no observed criticism cycle, improved-capacity evidence or exercised causal self-improvement attribution here. A route's operational availability does not establish reliable compliance, empirical benefit or transfer. See [RT-RTE-edit-admission](runtime.md#rt-rte-edit-admission), [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission), [RT-CMP-proposer](runtime.md#rt-cmp-proposer), [RT-CMP-selector](runtime.md#rt-cmp-selector), [RT-CMP-solver](runtime.md#rt-cmp-solver), [RT-CMP-judge](runtime.md#rt-cmp-judge).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-execution-evidence
Label: Task and execution evidence

Source-native identity: task/source files, RunView trajectories and deliverable renderings supplied to model sessions. Mixed natural-language/domain assertions and symbolic action/result records stored in local context directories. Closest supplied records are [RT-RTE-task-recursion](runtime.md#rt-rte-task-recursion), [RT-RTE-solver-execution](runtime.md#rt-rte-solver-execution), [RT-RTE-output-selection](runtime.md#rt-rte-output-selection): this object spans their payloads, not their control flow, and has no supplied object counterpart. Evidence: SRC-1 `harness2/core/context.py`, `harness2/core/selection.py`; supplied routes provide load-bearing passages for construction, names-only omission and rendering limits. Warrant of imported task facts is unknown; logs are attributed executor reports, not independently authenticated observations. Different consumers receive different projections, not necessarily judge-equivalent renderings.

#### EPI-OBJ-experience
Label: Reflected experience fields

Part of: [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission)

This is the retained payload part of that route, not a duplicate route. Source-native identity: parsed cue/lesson/evidence/confidence and optional edits, later EXPERIENCE.md and cue in INDEX.md. Natural-language form, UTF-8 local files and dictionary strings. Edit verdicts and explanatory prose can be truth-apt; cue and lesson can combine scope conditions and behavioral prescriptions. Model attribution is retained, but underlying truth and component effect are not validated by labels. SRC-1 `harness2/core/selection.py`, `harness2/core/library.py`, `harness2/core/prompts.py`.

> "The `evidence` field cites the edit rows the lesson rests on. A lesson resting only "
> "on `confounded` rows is a guess: narrow it to what the record does show, or decline. "
> --- `harness2/core/prompts.py`

> if exp.get("lesson"):
>     lines += ["## Transferable lesson"]
>     lines += [
>         f"- **{f}**: {str(exp[f]).strip()}"
>         for f in ("cue", "lesson", "evidence", "confidence")
>         if exp.get(f)
>     ]
> --- `harness2/core/library.py`

Cleanup/withdrawal: forget removes an entry directory; retain selects a preceding-task prefix and invokes forget; rebuilding the index removes those pointers. No retraction of already copied evidence or descendant edits is implemented by these methods. This is an implementation-local conclusion, not an exhaustive negative about external consumers.

> if d.is_dir():
>     shutil.rmtree(d, ignore_errors=True)
>     removed = True
> --- `harness2/core/library.py`

#### EPI-OBJ-score-rows
Label: Benchmark scoring records

Source-native identity: Scored, judged.json and derived Summary. Symbolic field records/numbers stored in memory and JSON, printed as text. Different semantic parts remain explicit: JobBench weighted points or labelled unweighted fallback; LAB pass counts/all_pass; WorkBuddy rounded percentage with raw_score; errors/ungraded status. No supplied object counterpart; [RT-CMP-judge](runtime.md#rt-cmp-judge) is the external model component, not these returned records. SRC-1 `harness2/core/judge.py`, `harness2/benchmarks/jobbench.py`, `harness2/benchmarks/lab.py`, `harness2/benchmarks/workbuddy.py`.

> "n_passed": round(sc * 100),
> "n_criteria": 100,
> "all_pass": sc >= 1.0,
> "raw_score": sc,
> --- `harness2/benchmarks/workbuddy.py`

> "n_passed": total,
> "n_criteria": mx,
> "all_pass": bool(n_c > 0 and n_p == n_c),
> "metric": "weighted",
> --- `harness2/benchmarks/jobbench.py`

#### EPI-OBJ-demo-ledger
Label: Demo ledger and totals

Source-native identity: two shipped ledger fixtures, BASE_SCRIPT, edited scripts/summarize.py and answer.txt. Symbolic CSV decimal amounts/code, natural-language task and formatted total, on disk. Distinct from benchmark/model payloads in [EPI-OBJ-execution-evidence](#epi-obj-execution-evidence); closest supplied [RT-OBJ-harness-code](runtime.md#rt-obj-harness-code) describes the general executable surface, not this arithmetic fixture. SRC-1 `harness2/demo.py`.

> ("ledger-1", "100.25\n-20.10\n5.00\n"),
> ("ledger-2", "35.50\n-10.25\n-5.00\n"),
> --- `harness2/demo.py`

> return "Sum every signed amount in ledger.csv. Return Total: with two decimal places."
> --- `harness2/demo.py`

Implementation deduction, not execution: the shipped positive-only base computes 105.25 for ledger-1; removing ` if amount > 0` gives 85.15, the signed sum. The premises are synthetic fixture values, not claims about real accounts.

> total = sum((amount for amount in amounts if amount > 0), Decimal(0))
> print(f'Total: {total:.2f}')
> --- `harness2/demo.py`

> script.write_text(script.read_text().replace(" if amount > 0", ""), encoding="utf-8")
> --- `harness2/demo.py`

### Routes

#### EPI-RTE-lesson-parse
Label: Parse reflection response

Part of: [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission)

Endpoints: reflection Reply.text → _distil dictionary → selection/library consumers. Code owns extraction after the model returns; this is the parsing subroute, not a replacement for the supplied admission container. SRC-1 `harness2/core/selection.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: required fields plus optional confidence/edits, or empty mapping; edits.md can survive without an experience block.
- Later read-back: parsed values are persisted in selection and EXPERIENCE.md for later task improvers through the parent route.
- Delegated visibility: model response is reduced to allowed fields, not preserved wholesale as lesson content.
- Selection predicate: first experience regex match; colon-delimited allowed keys; nonempty cue, lesson and evidence; marker scan.
- Invalidation or expiry: missing block/required fields yields empty result; parent route governs retained-entry deletion.
- Activation or effect: strings become admissible library payload; later behavior is unobserved.
- Evidence limits: no semantic preservation check, verification of evidence citations, confidence gate or observed generated response.

> for line in m.group(1).strip().splitlines():
>     if ":" in line:
>         key, _, val = line.partition(":")
>         key = key.strip().lower()
>         if key in ("cue", "lesson", "evidence", "confidence"):
>             out[key] = val.strip()
> --- `harness2/core/selection.py`

> if not all(out.get(key) for key in ("cue", "lesson", "evidence")):
>     return {}
> --- `harness2/core/selection.py`

Concrete counterexample traced through this code: a response block containing `cue: multi-act instrument`, `lesson: Put the termination last`, a separate next line `only when the earlier acts require that authority`, and `evidence: row A` retains the lesson but drops its unkeyed qualifying line. Whitespace stripping is harmless in isolation; ignoring continuation content is not guaranteed semantic preservation. This establishes a reachable degradation of warrant, not that actual responses were degraded. Repeated allowed keys also overwrite earlier values. Content generation is model-owned; admission veto is code-owned, with no per-content human check. This parser carries no independent answer oracle or improvement criterion.

#### EPI-RTE-judge-result
Label: Acquire benchmark judgement

Endpoints: selected run (or --bases reference run) → adapter.score → Scored. The separate judge CLI and benchmark adapters own progression. Closest supplied [RT-RTE-output-selection](runtime.md#rt-rte-output-selection) ends in choice and [RT-CMP-judge](runtime.md#rt-cmp-judge) names a component; neither declares this post-selection measurement route. SRC-1 `harness2/core/judge.py`, `harness2/cli/judge.py`, `harness2/benchmarks/jobbench.py`, `harness2/benchmarks/lab.py`, `harness2/benchmarks/workbuddy.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: normalized counts/points/all_pass/raw result or ungraded/error Scored.
- Later read-back: judged.json feeds the separate report CLI, not the inspected adaptation scheduler.
- Delegated visibility: LAB invokes external evaluation.run_eval; JobBench reads cached details or launches its judge; WorkBuddy reads verifier/score.json.
- Selection predicate: normal path requires a successful chosen selection; --bases instead enumerates recorded reference runs.
- Invalidation or expiry: adapter caches can avoid fresh evaluation; missing/unparseable results fail as ungraded, except actual no-output JobBench scoring can assign a benchmark-defined zero.
- Activation or effect: results populate reporting fields; no inspected consumer uses these grades to revise the task's admitted lesson or harness.
- Evidence limits: external judging internals/criteria and historical runs unavailable; results are evaluator-attributed outcome assessments, not certified truth or component-effect measurements.

Target/domain: benchmark task output against its own rubric/verifier, not harness edit causality, lesson truth or transfer. Evaluator: benchmark-dependent external program/model/hybrid; exact correctness not established. Answer references, where used internally, belong to those external graders, not a supplied adaptation oracle. Operational mode is post-hoc measurement, with operator-triggered judging; no human per-grade approval wired. Operational authority: permissive reporting admission; consumer report CLI, channel scored JSON, horizon later reports. Epistemic license is bounded to imported grader outcomes and arithmetic interpretation.

> got = adapter.score(run_dir, task_id)
> --- `harness2/core/judge.py`

> if not got:
>     s.error = "judge returned nothing"
>     return s
> s.raw = dict(got)
> s.n_passed = got.get("n_passed")
> s.n_criteria = got.get("n_criteria")
> --- `harness2/core/judge.py`

> if not self.delivered(run_dir):
>     return self._no_output_score(task_id)
> --- `harness2/benchmarks/jobbench.py`

> if not self.delivered(run_dir) and self._killed(run_dir):
>     return None
> --- `harness2/benchmarks/workbuddy.py`

These last two branches prevent conflating all missing outputs with either zero or judge failure across benchmarks.

#### EPI-RTE-score-cache
Label: Merge judged cache

Endpoints: prior judged.json plus fresh Scored rows → keyed merge → judged.json. Code owns progression; no model decision or human per-row veto. No supplied route counterpart; distinct from summary/rollout reuse in [RT-RTE-resume-reuse](runtime.md#rt-rte-resume-reuse). SRC-1 `harness2/cli/judge.py`, `harness2/core/judge.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: merged rows sorted by task/mode/k, persisted to judged.json.
- Later read-back: report CLI reloads rows, discarding saved derived frac/graded and recomputing them.
- Delegated visibility: inapplicable — local records, no delegated model call in merge.
- Selection predicate: changed run replaces; for same run preserve old graded row over a newly ungraded row unless error starts with selection.
- Invalidation or expiry: changed chosen run and selection failure can replace prior grade; ordinary failed re-judge of the same run does not withdraw it.
- Activation or effect: controls which score future reports consume and can preserve an earlier grade after attempted re-evaluation fails.
- Evidence limits: run_id equality is not authenticated output identity or new judge confirmation; caches do not establish endorsement/freshness.

Epistemic scope: continuity of previously reported evaluator outcome only. Operational authority: enforcing cache selection; consumer report, channel JSON, horizon later reports. No new evidence-consuming epistemic acceptance occurs.

> if (
>     prev is not None
>     and prev.run_id == r.run_id
>     and prev.graded
>     and not r.graded
>     and not r.error.startswith("selection")
> ):
>     continue
> by_key[key] = r
> --- `harness2/cli/judge.py`

#### EPI-RTE-score-report
Label: Aggregate graded outcomes

Endpoints: judged rows → per-mode/k Summary → printed report and warnings. Code owns grouping, predicates and arithmetic. No supplied route counterpart; distinct from [EPI-RTE-judge-result](#epi-rte-judge-result), which produces the inputs. SRC-1 `harness2/core/report.py`, `harness2/core/judge.py`, `harness2/cli/report.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: summaries with graded/ungraded counts, mean normalized score, all-pass rate, choice provenance, fallback and mixed-unit warnings.
- Later read-back: inapplicable — this CLI prints a report; no retained report consumer is implemented here.
- Delegated visibility: inapplicable — deterministic local computation without model delegation.
- Selection predicate: requested modes/scales; within each group only graded rows enter score denominator.
- Invalidation or expiry: re-running reloads current cache; warnings do not delete or re-judge rows.
- Activation or effect: makes numeric outcomes available to the operator; warnings are advisory and do not block reporting mixed metrics.
- Evidence limits: no inference from conditional mean to all attempts, population performance, mechanism, transfer or independent component effect.

Evaluator/domain: deterministic arithmetic under imported Scored fields and positive n_criteria predicate. Epistemic license: aggregate of those records only. Operational authority: advisory operator display, terminal text, horizon current report; no downstream adaptation consumer inspected.

> good = [r for r in group if r.graded]
> --- `harness2/core/report.py`

> s.score = round(100 * st.mean(r.frac for r in good), 2)
> s.all_pass = round(100 * sum(1 for r in good if r.all_pass) / len(good), 2)
> --- `harness2/core/report.py`

Concrete implementation deduction: one graded row with n_passed=1, n_criteria=2 and one ungraded row gives n=1, n_ungraded=1 and score=50.00, not 25.00. This is correct for the conditional denominator, not evidence that all attempts average 50 percent. The checked arithmetic does not certify the imported outcome's truth.

> if len(s.metrics) > 1:
> --- `harness2/core/report.py`

#### EPI-RTE-demo-check
Label: Demo signed-total oracle

Endpoints: context source/ledger.csv → Decimal expected sum → candidate text substring match → choice. Scripted DemoProposer owns the decision, no model service. Closest [RT-RTE-output-selection](runtime.md#rt-rte-output-selection) describes ordinary benchmark selector roles; this is a distinct deterministic implementation used by the shipped demo. SRC-1 `harness2/demo.py`, `harness2/cli/demo.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: choice text identifying first sorted candidate containing the formatted expected total.
- Later read-back: choice passes through ordinary selection persistence; demo experience can enter the library but is scripted, not independently inferred from trajectories.
- Delegated visibility: inapplicable — local deterministic proposer, not an external session.
- Selection predicate: label starts with select.; source-derived expected signed sum occurs in candidate text; k=1 trivial selection bypasses selector invocation.
- Invalidation or expiry: no match raises through next(); common selection error/fallback handles failure.
- Activation or effect: recognized choice determines delivered candidate and potential library harness.
- Evidence limits: substring test accepts extra contradictory text; synthetic fixtures and no execution evidence cannot establish model learning or professional-task improvement.

Target: presence of the correct two-decimal signed total in candidate text over the supplied ledger values. Evaluator: Decimal summation and substring check; answer oracle is computed from that same source, not externally supplied ground truth. Admission veto is software; no per-choice human contribution. Mode: bounded deterministic demonstration. Epistemic license: source-relative arithmetic and occurrence, not whole-document correctness. Behavioral-authority path: selection parser, choice text, permissive recognized-ID admission, horizon demo task. The non-selection branch applies a fixed string replacement; reflection decides helped merely from script inequality, so its edit-effect explanation is not independently established by executing this source trace.

> expected = sum(
>     (Decimal(row["amount"]) for row in csv.DictReader(source)), Decimal(0)
> )
> --- `harness2/demo.py`

> chosen = next(
>     path.stem for path in candidates if f"Total: {expected:.2f}" in path.read_text()
> )
> --- `harness2/demo.py`

> changed = (context / "harness/scripts/summarize.py").read_text() != (
>     context / "base_harness/scripts/summarize.py"
> ).read_text()
> --- `harness2/demo.py`

### Claims

#### EPI-CLM-evidence-lessons
Label: Evidence-supported persistent lessons

Claimed operation: task contrasts produce refinements without ground-truth feedback; adopted harnesses and evidence-supported lessons update persistent improvement context. SRC-1 `README.md` (doctrine/design). Closest [RT-CLM-answer-free](runtime.md#rt-clm-answer-free) concerns information exclusion, not whether retained lessons have warrant. Distinct claim, overlapping routes.

> * **Harnessing-level recursion** updates a persistent *improvement harness*
>   with adopted harnesses and evidence-supported lessons from each task to guide
>   future refinement.
> --- `README.md`

Design support includes supplied [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission) and the explicit confounding/NO_ENTRY instructions in [EPI-OBJ-experience](#epi-obj-experience). Implementation supplies contrasts and retains generated text, but checks shape/markers rather than causal adequacy. No observed lesson, evidence-consuming acceptance result or independently varied component comparison is supplied. Supported conclusion is an implemented evidence-oriented candidate and retention path. Reliable causal attribution and transfer remain unknown, not falsified by missing runs.

#### EPI-CLM-benchmark-gains
Label: Reported benchmark improvement

Claimed operation: a step improves the named models over bases, with larger recursion budgets yielding further gains. SRC-1 `README.md`: reported operation; frozen text is not inspectable experimental evidence. No supplied claim counterpart; [RT-RTE-task-recursion](runtime.md#rt-rte-task-recursion) establishes the procedure, not these outcomes.

> Across three professional benchmarks and four model–harness configurations, a
> single Harness² step improves GLM-5 and Gemini 3.5 Flash over their base
> harnesses, with gains of up to 11.5 points on WorkBuddy-Bench, 4.5 points on
> JobBench, and 11.8 percentage points on LAB's partial pass rate. Increasing the
> task-level recursion budget brings further gains.
> --- `README.md`

Implemented measurement/report routes can support bounded comparisons if suitable run evidence is supplied; --bases can score reference executions. None is supplied here. Outcome gains alone would not isolate a component, explanation, persistent-lesson contribution or transfer mechanism. The external paper was not acquired. No causal reproduction or numerical endorsement follows from the source trace.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
