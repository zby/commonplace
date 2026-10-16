---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "PrimeScientist epistemic routes: benchmark evidence, conclusion reshaping and score-driven reliance at the frozen revision."
run-id: AAS-2026-10-14-primescientist-f880686cf98a-01
reviewed-boundary: "29971beac6f4f4b41309b1326762e1b83ceece98"
---

# PrimeScientist epistemic report

## Source-and-claim boundary

The question is what the shipped research-search workflow can acquire, conjecture, check and license for later use. Scope and dependencies are see [boundary](boundary.md#boundary-and-evidence); evidence identities are see [Source register](boundary.md#source-register). SRC-1 supplies implementation, doctrine/design and reported operation, not observed execution or causal evidence. External coding-agent and provider internals are excluded. No execution was performed.

The operational loop is score-directed experimentation. The consequential warrant claim is [EPI-CLM-score-correctness](#epi-clm-score-correctness). The README describes replication scored by RAGChecker F1; it does not itself establish that accepted scientific discoveries are produced. The reflector's stronger correctness language requires checking what is actually scored.

Coverage distinguishes direct inspection in this job from supplied findings. All paths below are SRC-1 at the reviewed commit. Supporting task/preparation files remain included but unassessed; this is not a system-complete negative about knowledge production.

| Entry point or operation | Source path | Coverage and records, or limit |
|---|---|---|
| Benchmark dispatch | `benchmarks/registry.py` | Direct read: AutoLab/FIRE-Bench shipped; optional terminal_bench unavailable. No inference about its evaluators. |
| Tree CLI, setup, repeated execution, skip-evaluation, pruning | `run_search.py` | Direct reads of bootstrap, pruning, node runner and result disposition; CLI option search. See [RT-RTE-search-execution](runtime.md#rt-rte-search-execution), [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission). Synthetic skip-evaluation packets are not checked results. |
| Selection, reload and Q accumulation | `search/tree.py` | Supplied findings, not independently reread: [RT-OBJ-stats](runtime.md#rt-obj-stats), [RT-BAP-score-selector](runtime.md#rt-bap-score-selector). |
| Reflector prompts, brief generation, insight copying | `search/reflector.py` | Direct reads of FIRE-Bench/proposal prompts and brief/reflection bodies; insight-write search. Session and initialization findings supplied: [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission). No verified cross-task insight-production loop. |
| Fresh/inherited worker, Codex/OpenHands context | `benchmarks/fire_bench/agents/codex/run.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`, `benchmarks/fire_bench/agents/openhands/run.py`, `benchmarks/utils.py` | Supplied routes: [RT-BAP-plan-worker](runtime.md#rt-bap-plan-worker), [RT-RTE-search-execution](runtime.md#rt-rte-search-execution). Model interpretation and internal tools uninspected. |
| AutoLab verifier/container dispatch | `benchmarks/autolab/__init__.py` | Reward/error helper search plus supplied [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation). Docker/enroot equivalence and other task oracles not independently assessed. |
| Concrete correctness/performance check | `benchmarks/autolab/tasks/gaussian_blur/tests/test.sh`, `benchmarks/autolab/tasks/gaussian_blur/tests/verify_correctness.py` | Direct complete reads: [EPI-RTE-gaussian-check](#epi-rte-gaussian-check). One task witness, not all AutoLab correctness. |
| FIRE-Bench scoring adapter and information withdrawal | `benchmarks/fire_bench/__init__.py` | Direct evaluate/attachment reads: [EPI-RTE-score-attachment](#epi-rte-score-attachment). |
| Log extraction and core-idea generation | `benchmarks/fire_bench/eval/RAGChecker/utils.py` | Direct complete function reads: [EPI-RTE-conclusion-extraction](#epi-rte-conclusion-extraction). |
| Reference checking, metric computation, evaluator CLI, optional error analysis | `benchmarks/fire_bench/eval/RAGChecker/eval.py`, `benchmarks/fire_bench/eval/RAGChecker/ragchecker/evaluator.py`, `benchmarks/fire_bench/eval/RAGChecker/ragchecker/computation.py` | Direct scoring/error-analysis/CLI bodies and extraction/check/precision/recall/F1 functions: [EPI-RTE-reference-check](#epi-rte-reference-check), [EPI-RTE-error-analysis](#epi-rte-error-analysis). Low-level extractor/checker provider behavior uninspected. |
| Linear keep/revert, replay/history | `run_vanilla.py` | CLI search and supplied [RT-RTE-vanilla-retention](runtime.md#rt-rte-vanilla-retention). |
| Paper/plan preparation | `benchmarks/fire_bench/benchmark/plan_generator.py`, `benchmarks/fire_bench/benchmark/tree_parser.py` | CLI search only; model-mediated preparation bodies unassessed. Prevents complete characterization of imported task lineage and preparatory conjecture/checking. |
| Task utility calls, other tests, task instructions/references | `benchmarks/fire_bench/utils/`, `benchmarks/fire_bench/benchmark/papers/`, `benchmarks/autolab/tasks/` | Included opaque alternatives. Other task checks, utility model calls and initial reference provenance unassessed; prevents exhaustive evaluator validity and scientific-method conclusions. |

Missing generated plans, candidate traces, result artifacts and acceptance decisions prevent identifying actual conjectures, actual criticism, acceptance and integration. Missing deployment/model revisions prevent weight-fixity conclusions. Missing interventions prevent benefit and component-level attribution. Available but unread supporting files are inspection limits, not access gaps.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-skill](runtime.md#rt-obj-skill) | Possible hypotheses, expected outcomes and methods; actual content not determinable | see record | see record | Plans are guidance, not licensed findings. |
| [RT-OBJ-sandbox](runtime.md#rt-obj-sandbox) | Mixed code, data and possible experimental outcomes | see record | see record | Successful retained code is not an explanation of its success. |
| [RT-OBJ-stats](runtime.md#rt-obj-stats) | Numeric aggregates of returned scores | see record | see record | Q incorporates descendants; neither Q nor P is a truth probability. |
| [EPI-OBJ-prior](#epi-obj-prior) | Requested hypothesis, rationale, expected improvement and risks | see record | see record | Generated content unobserved; numeric estimate is a distinct symbolic consumer path. |
| [EPI-OBJ-packet](#epi-obj-packet) | Scores and benchmark-specific diagnostics about an attempt | see record | see record | Zero can reflect missing evaluation, not falsity. |
| [EPI-OBJ-log-brief](#epi-obj-log-brief) | Selected agent narrative and tool/environment reports | see record | see record | Omits middle evidence; full log remains reachable. |
| [EPI-OBJ-core-idea](#epi-obj-core-idea) | Generalized candidate conclusion | see record | see record | Source scope/numbers/methods are deliberately omitted. |
| [EPI-OBJ-gt-answer](#epi-obj-gt-answer) | Imported expected answers to named task questions | see record | see record | Initial source warrant unknown; reference status is not independent truth verification. |

Prior text, diagnostic briefs and evaluation packets have different checks and consumers; they are separated above rather than treated as one homogeneous truth store. Metric intermediates belong to [EPI-RTE-reference-check](#epi-rte-reference-check). Their checks and consumption are separated in the ledger below.

## Authority-route ledger

Rows split functions even when one supplied container record owns several. `see` delegates the record's fields rather than redeclaring them. No observed result is claimed. License is the report's bounded assessment, distinct from operational continuation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission) | content transformation | implemented | [RT-OBJ-skill](runtime.md#rt-obj-skill) | truth-apt transformation: indeterminate | Diagnostic inputs to successor hypothesis/plan | see record | see record | see record | Requested model interpretation | Candidate only; no observed proposition to classify as entailed or ampliative | Subsequent proposal can enter worker guidance | see [RT-BAP-plan-worker](runtime.md#rt-bap-plan-worker) | see record | none | none | Prompt examples of new hypotheses do not individuate generated claims. |
| [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission) | operational admission/selection/consumption | implemented | [RT-OBJ-skill](runtime.md#rt-obj-skill) | no content change | Proposal existence/prior to selectable child | see record | see record | see record | Filesystem existence and numeric prior handling | No semantic plan warrant | Enables a plan before scientific checks | see record | see record | none | none | This is not evidence-consuming claim acceptance. |
| [EPI-RTE-conclusion-extraction](#epi-rte-conclusion-extraction) | content transformation | implemented | [EPI-OBJ-core-idea](#epi-obj-core-idea) | truth-apt transformation: indeterminate | Log fragment to generalized conclusion | see record | see record | see record | Evaluator consumes transformed narrative | Candidate source warrant degraded; semantic preservation unestablished | Determines what receives F1 credit | see record | see record | [EPI-CLM-score-correctness](#epi-clm-score-correctness) | scope-loss | Concrete quantities and methods cannot receive direct checking here. |
| [EPI-RTE-reference-check](#epi-rte-reference-check) | check/evidence production | implemented | [EPI-OBJ-core-idea](#epi-obj-core-idea), [EPI-OBJ-gt-answer](#epi-obj-gt-answer) | no content change | Extracted claims versus reference, both directions | see record | see record | see record | Produces model judgments | Reference-relative agreement, conditional on faithful extraction and judgment | Supplies score evidence, not disposition itself | see record | see record | [EPI-CLM-score-correctness](#epi-clm-score-correctness) | reference-not-world | No experiment/replay audit in this check. |
| [EPI-RTE-reference-check](#epi-rte-reference-check) | content transformation | implemented | [RT-OBJ-stats](runtime.md#rt-obj-stats) | truth-apt transformation: entailed derivation | Judgment arrays to precision/recall/F1 | see record | see record | see record | Fixed arithmetic | Arithmetic from supplied labels only; their truth is not established | Supplies scalar for adapter | see record | see record | none | none | Model entailment labels are not formal proofs. |
| [EPI-RTE-score-attachment](#epi-rte-score-attachment) | content transformation | implemented | [RT-OBJ-stats](runtime.md#rt-obj-stats) | truth-apt transformation: non-ampliative reshaping | Evaluation representation to normalized packet metrics | see record | see record | see record | Parsing, normalization, diagnostic exclusion | Carries metric meaning if attachment succeeds; no extra warrant | Driver receives scores without reference-derived diagnoses | see record | see record | none | none | Position matching and regex failure constrain lineage. |
| [EPI-RTE-gaussian-check](#epi-rte-gaussian-check) | check/evidence production | implemented | [RT-OBJ-sandbox](runtime.md#rt-obj-sandbox) | no content change | Gaussian output on fixed image and benchmark time | see record | see record | see record | Exit status and reward generation | Pixel agreement on specified test; timing conditional on binary report | Correctness failure blocks performance scoring | see record | see record | none | none | Not general Gaussian correctness or trustworthy speed on all inputs. |
| [RT-RTE-search-execution](runtime.md#rt-rte-search-execution) | disposition/acceptance | implemented | [RT-OBJ-sandbox](runtime.md#rt-obj-sandbox) | no content change | Best repeated-run packet and branch score versus parent Q | see record | see record | see record | Fixed comparison; score-pruning | Acceptance for continued search only, not acceptance of explanatory/scientific claim | Hides weak branches; eligible branches remain usable | see [RT-BAP-score-selector](runtime.md#rt-bap-score-selector) | see record | none | none | Maximum-over-repeats is not an uncertainty estimate; parent Q is aggregate. |
| [RT-RTE-search-execution](runtime.md#rt-rte-search-execution) | retention | implemented | [RT-OBJ-sandbox](runtime.md#rt-obj-sandbox), [RT-OBJ-stats](runtime.md#rt-obj-stats) | no content change | Packet/workspace to durable node state | see record | see record | see record | File persistence, including pruned packets | Retention adds no claim acceptance | Later reload/reflection/inheritance remains possible | see record | see record | none | none | Pruning withdraws normal branch use, not stored evidence or already executed actions. |
| [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission) | behavior/policy adaptation | implemented | [RT-OBJ-skill](runtime.md#rt-obj-skill) | non-truth-apt policy/content update: task guidance and prior | Result-conditioned proposal request to later guidance | see record | see record | see record | Model guidance plus symbolic selection | No demonstrated improvement or new knowledge follows | Can alter later selected procedure | see [RT-BAP-plan-worker](runtime.md#rt-bap-plan-worker) | see record | none | none | Actual evidence-response and worker compliance unobserved. |
| [RT-RTE-vanilla-retention](runtime.md#rt-rte-vanilla-retention) | disposition/acceptance | implemented | [RT-OBJ-sandbox](runtime.md#rt-obj-sandbox) | no content change | New code versus best score | see record | see record | see record | Strict improvement comparison | Accepted as next seed under benchmark objective | Keeps/reverts best workspace | see record | see record | none | none | Not framework improvement or scientific claim acceptance. |
| [RT-RTE-vanilla-retention](runtime.md#rt-rte-vanilla-retention) | retention | implemented | [RT-OBJ-sandbox](runtime.md#rt-obj-sandbox) | no content change | Iteration packets and selected workspace | see record | see record | see record | Persistence and history replay | No added warrant | Later history and best workspace seed another attempt | see record | see record | none | none | Rejected attempt evidence persists; replacement is not transactional. |
| [EPI-RTE-error-analysis](#epi-rte-error-analysis) | check/evidence production | implemented | [EPI-OBJ-core-idea](#epi-obj-core-idea) | truth-apt transformation: indeterminate | False-positive/negative claims to proposed causal diagnosis | see record | see record | see record | None in frozen CLI dispatch | No active diagnostic license | Disabled branch; no corrective consumer | see record | see record | none | disabled-analysis | Exists as callable helper, but ordinary main sets flag false. |

Route ID: [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-log-brief](#epi-obj-log-brief)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see [EPI-OBJ-log-brief](#epi-obj-log-brief)
Evaluator/condition and domain: fixed head/tail code rule, not truth evaluation.
Activation and timing: before reflection, see [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission).
Possible or observed result: see [EPI-OBJ-log-brief](#epi-obj-log-brief).
Implemented force: diagnostic input delivery.
Epistemic authority and scope: preserves selected lines, not complete evidence coverage or endorsement.
Operational authority: can inform successor planning; no new enforced criterion.
Behavioral-authority path: see [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission).
Evidence source ID and local anchor: SRC-1, `search/reflector.py`; passage see [EPI-OBJ-log-brief](#epi-obj-log-brief).
Claim IDs: none
Mismatch marker: none
Gap/limit: actual diagnostic use unobserved; full log remains reachable.

Route ID: [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [RT-OBJ-skill](runtime.md#rt-obj-skill), [EPI-OBJ-prior](#epi-obj-prior)
Content/update relation: no content change
Transition or check target: prospective guidance/rationale to durable child files.
Evaluator/condition and domain: see [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission).
Activation and timing: see [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission).
Possible or observed result: see [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission).
Implemented force: durable availability.
Epistemic authority and scope: persistence before semantic acceptance; no added warrant.
Operational authority: selected plans guide later workers and rationales are available to later reflectors.
Behavioral-authority path: see [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission).
Evidence source ID and local anchor: see [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission).
Claim IDs: none
Mismatch marker: none
Gap/limit: actual authorship/content use unobserved.

Within the inspected driver/evaluator routes, no separate lifecycle-integration function for accepted scientific claims was found. Search retention and plan reuse precede any such acceptance. Unassessed preparation/task paths prevent extending that finding to every shipped operation.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-score-correctness](#epi-clm-score-correctness) | see record | see record | see record | [EPI-RTE-conclusion-extraction](#epi-rte-conclusion-extraction), [EPI-RTE-reference-check](#epi-rte-reference-check), [EPI-RTE-score-attachment](#epi-rte-score-attachment) | None supplied | No intervention; reference-relative metric cannot identify experimental validity or mechanism | A score can indicate model-assessed agreement of generalized narrative with benchmark answer | Correctness language exceeds the checked domain. |

[RT-CLM-budget-stop](runtime.md#rt-clm-budget-stop) concerns operational budget enforcement, not truth warrant. Its qualifications remain see record; this report does not convert resource controls into epistemic guarantees.

## Bounded conclusion

PrimeScientist retains plans, code/workspaces, outcomes, numeric statistics and diagnostics, then uses them for symbolic selection and model-guided successor planning. These are independently supported operational feedback paths, not merely file storage. Force differs: numerical scores enforce branch availability and affect sampling; plans and rationales are advisory/model-interpreted. Repeated operation and resumes extend their horizon beyond one worker call. See [RT-RTE-search-execution](runtime.md#rt-rte-search-execution), [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission), [RT-BAP-plan-worker](runtime.md#rt-bap-plan-worker), [RT-BAP-score-selector](runtime.md#rt-bap-score-selector).

FIRE-Bench acquires benchmark references whose initial warrant is unknown. It extracts a log fragment, asks a model to strip numerical/method/artifact detail, extracts claims and checks reference-relative agreement. It does not establish the truth of the original experiment, faithfully encoded scope, explanation, replay safety or transfer. Arithmetic F1 is derivable from labels; those labels remain model judgments. Attachment preserves normalized metrics but deliberately withholds ground-truth-derived error lists from the reflector. The optional file-search error analysis cannot repair this gap in ordinary execution: it is disabled and has no correction consumer. See [EPI-RTE-conclusion-extraction](#epi-rte-conclusion-extraction), [EPI-RTE-reference-check](#epi-rte-reference-check), [EPI-RTE-score-attachment](#epi-rte-score-attachment), [EPI-RTE-error-analysis](#epi-rte-error-analysis).

AutoLab supplies a different kind of evidence. The inspected Gaussian task compares output against a deterministic reference on one fixed input, gates timing on that check and computes a reward from three binary-reported times. This can license the specified test result, not universal functional correctness or verified general speed. Other task evaluators may differ and remain unassessed. See [EPI-RTE-gaussian-check](#epi-rte-gaussian-check).

Tree and vanilla decisions accept artifacts for continued benchmark search: the former prunes below parent aggregate Q, and the latter requires strict improvement over the best score. These name operational criteria and intended use, but neither records evidence-consuming acceptance of an individuated ampliative scientific claim. Requested hypotheses/criticism provide candidate-making capacity; no actual generated claim here establishes conjecture, content-directed criticism, acceptance or lifecycle integration. Retention alone does not close those phases.

The runtime's independent assessments remain bounded: theory formulation/consumption are afforded, criticism is requested, reflection has a wired representation-and-guidance path, internal scheduling is computational, and exercised learning/self-improvement remain uninspected. No accessible weight-change evidence resolves provider-parametric learning or fixity: see [RT-CMP-coding-model](runtime.md#rt-cmp-coding-model), [RT-CMP-reflector-model](runtime.md#rt-cmp-reflector-model), [RT-CMP-eval-model](runtime.md#rt-cmp-eval-model), [RT-CMP-ragchecker-models](runtime.md#rt-cmp-ragchecker-models). No system-wide score or negative verdict follows from these separate findings.

## Shared records

### Operative objects

#### EPI-OBJ-prior
Label: Proposal prior
Part of: [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission)

Source-native identity: child `prior.json`, a durable filesystem JSON object produced within the parent proposal route. Its hypothesis/rationale/changes/risks are natural-language guidance to later reflectors; estimate is symbolic numeric input to bootstrap and selection. It is not the plan file [RT-OBJ-skill](runtime.md#rt-obj-skill): it describes why and what to change, whereas the skill guides execution. Different consumer paths are retained, not inferred from the JSON substrate. SRC-1, `search/reflector.py` and `run_search.py`, doctrine/design and implementation. Passage and theory-condition findings are see [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission). The inspected bootstrap defaults/clamps only the estimate; no semantic acceptance of hypothesis/rationale is established. Pruning summaries can preserve its text for later proposer guidance.

#### EPI-OBJ-packet
Label: Evaluation packet
Part of: [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation)

Source-native identity: evaluator packet, persisted as node `packet.json`; an output object contained in the parent evaluation route, not a second declaration of that route. JSON filesystem substrate mixes symbolic scores/run identifiers with natural-language error/detail fields. Numeric consumers are driver/pruning/statistics; diagnostic consumers are later reflectors. Unlike [RT-OBJ-stats](runtime.md#rt-obj-stats), this is a particular run's packet, not a descendant-averaged statistic. SRC-1, `run_search.py`, `benchmarks/fire_bench/__init__.py`, implementation. Evidence passage and adapter criteria are see [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation); score attachment limits are see [EPI-RTE-score-attachment](#epi-rte-score-attachment). Ordinary FIRE-Bench packet excludes reference-derived diagnosis; AutoLab can expose verifier diagnostics. Retention does not endorse each reported field as scientific truth.

#### EPI-OBJ-log-brief
Label: Log brief
Part of: [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission)

Source-native identity: node `log_brief.log`; natural-language/tool-result diagnostic excerpt on filesystem, produced inside the parent's reflection-input preparation route. It is distinct from [RT-OBJ-skill](runtime.md#rt-obj-skill): retrospective evidence presented to a proposer, not prospective instructions. SRC-1, `search/reflector.py`, implementation. Default 100-head/500-tail behavior and hidden-full-log access are see [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission) and supplied runtime context account. The local complete function read establishes a deterministic non-ampliative selection: for lines L1–L8 with head=2 and tail=3, the function retains L1/L2 and L6/L7/L8 with an omission notice for three middle lines. It preserves retained lines but reduces available evidential coverage; it does not evaluate their truth. The full log remains available for explicit inspection. This is a lineage/context-delivery function within the plan route, not epistemic acceptance.

> head_block = lines[:head]
> tail_block = lines[-tail:]
> omitted = len(lines) - head - tail
> --- `search/reflector.py`

#### EPI-OBJ-core-idea
Label: Core idea

Source-native identity: `core_idea` in `eval_single_log`; natural-language content, held in a Python string and RAGResults response field, then evaluator output. Distinct from [RT-OBJ-skill](runtime.md#rt-obj-skill): this is a result narrative, not prospective guidance; no supplied object counterpart after comparison. SRC-1, `benchmarks/fire_bench/eval/RAGChecker/eval.py` and `benchmarks/fire_bench/eval/RAGChecker/utils.py`, implementation and doctrine/design. Its producer is the extraction model; its consumers are RAGChecker claim extraction/checking, not the ordinary packet's agent_conclusion field.

> core_idea = extract_core_idea(raw_conclusion, client, eval_model)
> --- `benchmarks/fire_bench/eval/RAGChecker/eval.py`

#### EPI-OBJ-gt-answer
Label: Ground truth answer

Source-native identity: `gt[task]`, paired with `query[task]`; natural-language expected-answer content in the shipped `gt` dictionary, copied to RAGResults `gt_answer`. Distinct from the core idea and [RT-OBJ-skill](runtime.md#rt-obj-skill); closest supplied route is [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation), not an object counterpart. SRC-1, `benchmarks/fire_bench/eval/RAGChecker/utils.py` (definition location searched) and `benchmarks/fire_bench/eval/RAGChecker/eval.py` (consumer directly inspected), implementation. Full reference provenance not assessed. Acquired expected answer, not a claim produced by this attempt.

> "gt_answer": f"{gt[task]}",
> "response": f"{core_idea}",
> --- `benchmarks/fire_bench/eval/RAGChecker/eval.py`

### Routes

#### EPI-RTE-conclusion-extraction
Label: Conclusion extraction
Part of: [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation)

Endpoints: agent log → heuristic fragment → model core idea → RAGChecker input. Owner: evaluator utility code and extraction-model service. Local fragment selection is symbolic; core-idea generation is natural-language interpretation by [RT-CMP-eval-model](runtime.md#rt-cmp-eval-model). SRC-1, `benchmarks/fire_bench/eval/RAGChecker/utils.py`, implementation and doctrine/design. This separates the transformation part from its parent's checking.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: extracted string or None, then model response string.
- Later read-back: transformed response enters saved evaluator representations; ordinary packet excludes agent conclusion. No later diagnosis reuse established.
- Delegated visibility: extraction model receives selected fragment, not full experiment data; checker receives generalized response.
- Selection predicate: last OpenHands match, otherwise timestamp slice, otherwise last-line JSON result; core-idea prompt then controls omission.
- Invalidation or expiry: inapplicable — current scoring transform; no withdrawal or expiry policy for saved evaluator outputs shown.
- Activation or effect: transformation defines the scored text; actual semantic fidelity and provider compliance unobserved.
- Evidence limits: external model processing opaque; neither faithful non-ampliative summary nor ampliative conjecture established for an actual output.

Concrete implementation deduction without target execution: with timestamps `[2025-09-19T10:05:41] A`, `[2025-09-19T10:05:42] B`, `[2025-09-19T10:05:43] C` on successive lines and no OpenHands match, the timestamp branch selects the first two timestamped lines and excludes C. Despite its comment saying second-last boundary, the code uses the last timestamp. Thus the function name does not guarantee final-answer isolation.

> start = timestamps[-3].start()
> end = timestamps[-1].start()
> extracted = content[start:end].strip()
> --- `benchmarks/fire_bench/eval/RAGChecker/utils.py`

> "omitting all concrete values, specific numbers, background details, methods, "
> "file names, or references to artifacts. "
> --- `benchmarks/fire_bench/eval/RAGChecker/utils.py`

The prompt's no-inference instruction is a counterweight, not a semantic-preservation check:

> "DO NOT infer any detail, context information, or background knowledge that is not mentioned "
> "in the original conclusion."
> --- `benchmarks/fire_bench/eval/RAGChecker/utils.py`

#### EPI-RTE-reference-check
Label: Reference check
Part of: [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation)

Endpoints: core idea/reference/query → model-extracted claims → checker labels in both directions → metric means/harmonic mean. Owner: vendored evaluator, with external extractor/checker services; model properties see [RT-CMP-ragchecker-models](runtime.md#rt-cmp-ragchecker-models). SRC-1, `benchmarks/fire_bench/eval/RAGChecker/ragchecker/evaluator.py`, `benchmarks/fire_bench/eval/RAGChecker/ragchecker/computation.py`, implementation. Truth-apt target is agreement of answer claims with reference content, not whether experiments happened or data entail the conclusion. Human-authored benchmark answer is the oracle; initial provenance unknown. Computational code schedules checking and aggregates model decisions; no current human veto. Mode: bounded benchmark trials, triggered by completed log scoring. It produces evidence, not an acceptance decision.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: RAGResults with extracted claims, checker labels and metrics.
- Later read-back: evaluator results persist as repr strings; normalized scores enter driver packets/Q and later reflection.
- Delegated visibility: claim extractor sees query/text; checker sees extracted claims, query and opposite answer text. Retrieved context is empty in the shipped scoring entry.
- Selection predicate: task identifies query/reference; metrics specify required checking directions.
- Invalidation or expiry: inapplicable — returns judgment/metric, not retention policy.
- Activation or effect: metric is consumed by adapter and score selector; model judgment reliability unobserved.
- Evidence limits: lower-level extractor/checker internals unassessed; no independent validation of reference, extraction coverage or entailment labels.

> claims = [ret.response_claims for ret in results]
> references = [ret.gt_answer for ret in results]
> --- `benchmarks/fire_bench/eval/RAGChecker/ragchecker/evaluator.py`

> claims = [ret.gt_answer_claims for ret in results]
> references = [ret.response for ret in results]
> --- `benchmarks/fire_bench/eval/RAGChecker/ragchecker/evaluator.py`

> if isinstance(checking_results, str):
>     return checking_results == "Entailment"
> --- `benchmarks/fire_bench/eval/RAGChecker/ragchecker/computation.py`

> result.metrics[metrics.f1] = 2 * precision * recall / (precision + recall)
> --- `benchmarks/fire_bench/eval/RAGChecker/ragchecker/computation.py`

This is entailed arithmetic conditional on checker labels and nonzero means, not formally certified source truth.

#### EPI-RTE-score-attachment
Label: Score attachment
Part of: [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation)

Endpoints: newly saved evaluation file → regex/record matching → packet scores without reference-derived diagnoses → driver. Owner: FIRE-Bench adapter. SRC-1, `benchmarks/fire_bench/__init__.py`, implementation. It separates lineage and information-withdrawal behavior from the parent's evaluator. This does not revise the parent's identity.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: run records with precision/recall/F1 normalized from 0–100 to 0–1, or empty scores.
- Later read-back: packet scores enter tree statistics and reflector packets; diagnostic claim lists are not exposed through this packet route.
- Delegated visibility: driver/reflector sees normalized scores and empty agent_conclusion, not false-positive/negative claim content.
- Selection predicate: new result files; optional error-analysis log-path match, otherwise index matching; metric regex must match.
- Invalidation or expiry: inapplicable — information omission occurs during packet construction, not deletion of stored evaluator files.
- Activation or effect: primary_score consumes F1, defaults absent to zero; poor/missing attachment can affect pruning/selection without truthful negative evidence.
- Evidence limits: evaluator subprocess uses check=False; missing/malformed/mismatched results do not establish experimental failure or falsity.

> rec["agent_conclusion"] = ""
> rec["false_positives"]  = []
> rec["false_negatives"]  = []
> --- `benchmarks/fire_bench/__init__.py`

> return float(packet.get("score", {}).get("f1") or 0.0)
> --- `benchmarks/fire_bench/__init__.py`

This counters the possible inference that detailed benchmark contradiction evidence reaches the reflector. Files remain accessible; packet-level withholding is not an access-control guarantee.

#### EPI-RTE-gaussian-check
Label: Gaussian check
Part of: [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation)

Endpoints: submitted blur binary → fixed-image comparison → benchmark timing → reward JSON → AutoLab packet. Owner: task test script/reference Python program; computational admission, human contribution is shipped test/reference/constants. SRC-1, `benchmarks/autolab/tasks/gaussian_blur/tests/test.sh`, `benchmarks/autolab/tasks/gaussian_blur/tests/verify_correctness.py`, implementation. Mode: bounded benchmark trial after build. Oracle: separable Gaussian reference, five passes, sigma 3, radius 8, clamp-to-edge, deterministic 256×256 input, tolerance 4. This check has genuine content-sensitive evidence independent of the worker's narrative, so a blanket claim that all evaluation is model judgment would be false.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: correctness exit code and reward/correctness/metric/speedup JSON; build/correctness failure yields zero.
- Later read-back: AutoLab packet and verifier diagnostics reach driver/reflector; retained workspace can seed another attempt.
- Delegated visibility: verifier receives compiled workspace and protected task tests; driver receives reward/detail, not an independently repeated measurement.
- Selection predicate: fixed test input first; performance benchmark is 4096×4096 with median of three binary-reported times.
- Invalidation or expiry: inapplicable — this check reports an attempt; later artifact replacement belongs to driver.
- Activation or effect: bad correctness blocks timing reward; reward subsequently ranks/prunes artifacts, not the proposed mechanism.
- Evidence limits: finite input and tolerance; performance parses binary output rather than independent wall-clock measurement. No measured execution or resistance to benchmark-specific behavior established.

> if ! python3 /tests/verify_correctness.py 2>&1; then
>     echo "Correctness check FAILED."
>     write_reward 0.0 false null null
> --- `benchmarks/autolab/tasks/gaussian_blur/tests/test.sh`

> if diff > TOLERANCE:
>     bad_count += 1
> --- `benchmarks/autolab/tasks/gaussian_blur/tests/verify_correctness.py`

> OUTPUT=$(/app/blur "$INPUT" - 4096 4096 2>/dev/null)
> T=$(echo "$OUTPUT" | sed 's/.*time=\([0-9.]*\).*/\1/')
> --- `benchmarks/autolab/tasks/gaussian_blur/tests/test.sh`

Given a reported median of 0.25 seconds, the script's baseline 12/reference 0.25 yields speedup 48 and reward 0.5, not raw throughput ratio 48. This implementation deduction bounds the README's shorthand. Correctness success still does not warrant that performance field against a deceptive reporter.

#### EPI-RTE-error-analysis
Label: Error analysis
Part of: [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation)

Endpoints: false-positive/negative labels plus paper/log → temporary provider vector store → model/file_search → parsed error diagnoses → optional saved analysis. Owner: evaluator CLI/helper; external model is the same configured eval_model as [RT-CMP-eval-model](runtime.md#rt-cmp-eval-model). SRC-1, `benchmarks/fire_bench/eval/RAGChecker/eval.py`, implementation and doctrine/design. Distinct dormant part of the evaluator container, omitted from the supplied operational route description. Target: why a reference-relative claim is wrong/missed; possible diagnoses are themselves candidate truth-apt causal accounts. No causal comparison validates them. Main sets a literal false flag, with no enabling CLI argument in the inspected parser. No source change or target execution was made.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: helper can return parsed FP/FN diagnoses; disabled main branch produces none.
- Later read-back: uninspected — optional saved analysis has no implemented corrective consumer in the inspected driver; adapter suppresses diagnosis fields.
- Delegated visibility: helper registers paper/log in temporary vector store and exposes file_search with max_num_results 5 to eval_model.
- Selection predicate: only if local do_error_analysis flag is true; per FP/FN statement model call. It is false in frozen main.
- Invalidation or expiry: vector store requests one-day expiry from last activity; uploaded-file cleanup not established.
- Activation or effect: no active force in ordinary CLI path and no automatic revision/withdrawal consumer found in inspected adapter/driver.
- Evidence limits: callable helper exists, so absence of any diagnostic capacity would be too strong; successful provider indexing, grounding and causal diagnosis unobserved.

> do_error_analysis = False
> 
> if do_error_analysis:
> --- `benchmarks/fire_bench/eval/RAGChecker/eval.py`

> "type": "file_search",
> "vector_store_ids": [vs_id],
> "max_num_results": 5,
> --- `benchmarks/fire_bench/eval/RAGChecker/eval.py`

> expires_after={"anchor": "last_active_at", "days": 1},
> --- `benchmarks/fire_bench/eval/RAGChecker/eval.py`

### Claims

#### EPI-CLM-score-correctness
Label: Score correctness

Claimed operation: FIRE-Bench reflector prompt treats packet reward as correctness of the agent's run conclusion and instructs reliance on score over narrative. SRC-1, `search/reflector.py`, doctrine/design. No counterpart after comparison with [RT-CLM-budget-stop](runtime.md#rt-clm-budget-stop), which concerns resources. Closest supplied mechanism is [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation). Claim is bounded by extraction, generalization and reference-relative model evaluation rather than verified experiment truth.

> {pruned_section}  {node_rel}/packet.json       — reward score (precision/recall/f1) and run metadata, the reward score symbolizes the correctness of agent run conclusion.
> --- `search/reflector.py`

> — trust packet.json score, not the agent's narrative.
> --- `search/reflector.py`
