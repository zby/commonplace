---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of Agent Skills for Context Engineering: source review, mechanism admission, routing evaluation and trace-fed instruction revision."
run-id: AAS-2026-10-19-agent-skills-for-context-engineering-7e663338370b-01
reviewed-boundary: "9ff0c99108b36d3b886defd825d8ac1f47dba374"
---

# Agent Skills for Context Engineering epistemic report

## Source-and-claim boundary

The question is how acquired research, evaluation results and revised instructions acquire reliance and affect later behavior. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and layers are see its [Source register](boundary.md#source-register). This is a complete artifact, partial loop, not an enclosing runtime. All source findings below use SRC-1 at the frozen revision. Direct inspection adds implementation and doctrine/design evidence, not observed operation or causal experiments. No target program was executed.

The consequential warrant claims are see [RT-CLM-maintenance-guarantees](runtime.md#rt-clm-maintenance-guarantees), [EPI-CLM-research-protocol](#epi-clm-research-protocol) and [EPI-CLM-trace-analysis](#epi-clm-trace-analysis). These claims concern different consumers. Source suitability, lexical overlap, fixture agreement and model-assigned trace quality must not be treated as one evaluator of truth.

| Entry point or operation | Source path, SRC-1 | Coverage and record | Limit and conclusion prevented |
| --- | --- | --- | --- |
| Skill discovery and activation | `.plugin/plugin.json`, `.claude-plugin/marketplace.json`, `skills/context-fundamentals/SKILL.md` | Supplied [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) | External loader and compliance uninspected; no demonstrated behavioral effect. |
| Scheduled discovery, retrieval and parking | `researcher/scripts/loop_step.py` | Supplied [RT-RTE-research-step](runtime.md#rt-rte-research-step) | Actual fetched bytes and review actions not supplied. |
| Manual research CLI, including alternate dispatch | `researcher/scripts/research_loop.py` | Direct: retrieval through promotion and complete parser/dispatch; [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion), [EPI-RTE-novelty-check](#epi-rte-novelty-check) | Initialization helpers only supplied through runtime; record-state labels are not semantic reviews. |
| Source rubric and publication-readiness checks | `researcher/rubrics/content-curation.md`, `researcher/runbooks/autonomous-research-loop.md`, `researcher/scripts/validate_run.py`, `researcher/scripts/validate_repo.py` | Direct: full rubric/runbook/run validator; repository source-evaluation validation functions; [EPI-RTE-source-review](#epi-rte-source-review), [EPI-RTE-rubric-arithmetic](#epi-rte-rubric-arithmetic), [EPI-RTE-run-readiness](#epi-rte-run-readiness) | Remaining repository validator domains not independently traced; arithmetic consistency does not establish evidence truth. |
| Novelty comparison and report retention | `researcher/scripts/novelty_check.py`, `researcher/scripts/research_loop.py` | Direct full novelty implementation and report consumer; [EPI-RTE-novelty-check](#epi-rte-novelty-check) | No semantic novelty oracle. |
| Router model calls, exact-match scoring, result reuse | `researcher/benchmarks/sdk-runner/src/runRouter.ts`, `researcher/benchmarks/sdk-runner/src/common.ts` | Supplied [RT-RTE-router-benchmark](runtime.md#rt-rte-router-benchmark) | No supplied item-level run evidence or independent verification of reference labels. |
| Effectiveness execution | `researcher/benchmarks/sdk-runner/src/runEffectiveness.ts` | Supplied [RT-ABS-effectiveness-executor](runtime.md#rt-abs-effectiveness-executor) | Absence is limited to this runner, not every evaluation in the artifact. |
| Prompt optimization, stop/selection, artifact and skill output | `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py` | Direct full analyzer, loop capture-to-finalization and scoring/convergence; other internals supplied [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization); new [EPI-RTE-trace-analysis](#epi-rte-trace-analysis) | No independently judged task outcome or qualifying produced theory inspected. |
| Retained idea/bookmark/post consumption | `examples/digital-brain-skill/agents/scripts/idea_to_draft.py` | Direct full script; [RT-RTE-idea-draft](runtime.md#rt-rte-idea-draft) | Its upstream write/review process and downstream publication untraced. |
| CI dispatch | `.github/workflows/validate.yml` | Direct full workflow; [EPI-CLM-research-protocol](#epi-clm-research-protocol) | Declared check invocations, not supplied successful CI results or required-branch protection. |
| Other exposed evaluators, export and artifact operations | `researcher/scripts/compare_skill_revisions.py`, `researcher/scripts/skill_health.py`, `researcher/scripts/check_activation_cases.py`, `researcher/scripts/run_benchmarks.py`, `researcher/scripts/validate_export.py`, `researcher/scripts/artifact_store.py` | Paths identified, selected symbol searches and CI entry calls only; semantic implementations unassessed | Prevents a complete account of selection, export lineage, freezing and rejection across the researcher plane. |
| Other published guidance and helpers | `skills/`, `template/` | Included but not individually assessed beyond supplied skill-delivery witness | Prevents corpus-wide claims about evaluation, memory revision, belief checks or policy adaptation. |
| Other shipped examples | `examples/book-sft-pipeline/`, `examples/llm-as-judge-skills/`, `examples/long-horizon-prompt-lab/`, `examples/x-to-book-system/` | Available but uninspected; CI names the prompt-lab build/validation | Prevents system-complete negatives about learning, training, acceptance and judging. |
| Governance, claims, schemas and retained research instances | `governance/`, `researcher/claims/`, `researcher/schemas/`, `researcher/runs/`, `researcher/exports/` | Protocol references and selected consumers inspected, not complete data/lineage audits | No individual accepted research claim, authenticated reviewer, privacy invariant or observed lifecycle integration established. |

External research originals, host internals, model parameters, private runtime state and provider execution are not supplied. These gaps prevent external-source verification, distributed-parametric learning conclusions and observed benefit attribution. Available but uninspected paths above are not access failures or evidenced absences. The coverage does not license a system-complete negative.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-skill-body](runtime.md#rt-obj-skill-body) | Advice includes empirical assertions about attention and loading; instructions themselves prescribe behavior | see record | SRC-1, `skills/context-fundamentals/SKILL.md` | Delivery is not verification of its empirical assertions. |
| [EPI-OBJ-source-evaluation](#epi-obj-source-evaluation) | Source suitability, gate judgments, mechanism summaries and evidential strength | see record | SRC-1, `researcher/rubrics/content-curation.md` | No particular completed evaluation inspected. |
| [EPI-OBJ-mechanism-proposal](#epi-obj-mechanism-proposal) | Activation conditions, predicted behavior changes and failure modes; status/reviewer fields are symbolic control data | see record | SRC-1, `researcher/scripts/research_loop.py` | Registry projection carries evidence IDs, not checked evidence semantics. |
| [EPI-OBJ-novelty-result](#epi-obj-novelty-result) | Computed overlap values over selected tokens; semantic novelty remains a separate judgment | see record | SRC-1, `researcher/scripts/novelty_check.py` | Lexical statistics are truth-apt about the algorithm's inputs, not proof of novelty. |
| [EPI-OBJ-trace-analysis](#epi-obj-trace-analysis) | Claimed failures, quoted trace evidence, quality scores and recommendations | see record | SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py` | Output can contain fallback scores rather than model judgments. |
| [RT-RTE-router-benchmark](runtime.md#rt-rte-router-benchmark) | Ranking and exact agreement with fixture primary labels | see route for embedded result objects | SRC-1, `researcher/benchmarks/sdk-runner/src/runRouter.ts` | No new object declared for the same supplied result container. |
| [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization) | Revised prompts/skills mix policies with possible explanatory assertions; individual truth-apt units not determinable without outputs | see route for prompt/artifact objects | SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py` | No inspected candidate output proves novel explanation or accepted knowledge. |
| [RT-RTE-idea-draft](runtime.md#rt-rte-idea-draft) | Imported idea, source link and first bookmark insight, where present | see route for retained input objects | SRC-1, `examples/digital-brain-skill/agents/scripts/idea_to_draft.py` | File content can be selected into “Supporting Evidence” without evidential assessment. |
| [RT-CMP-cursor-model](runtime.md#rt-cmp-cursor-model), [RT-CMP-minimax-model](runtime.md#rt-cmp-minimax-model) | Parameters not individually accessible | see components | SRC-1, `researcher/benchmarks/sdk-runner/src/runRouter.ts`, `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py` | No local weight update inspected; mutable provider identities do not pin exact weights. |

## Authority-route ledger

Fields owned by a declaring record are given by linked references rather than duplicated. Multiple rows may reference the same valid route container while separating its consequential functions. “Implemented” below concerns caller wiring, not reliable model compliance or observed execution.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-research-step](runtime.md#rt-rte-research-step) | content transformation | implemented | [EPI-OBJ-source-evaluation](#epi-obj-source-evaluation) | truth-apt transformation: acquisition/import | External source to raw file/pointer | see route; byte cap, HTTP(S) and caller input, not source truth | see route | Retrieved/parked state; see route | Local file/state writes | Source warrant unknown; retrieval label grants no truth license | Later selection may advance or park work | see route | SRC-1, `researcher/scripts/loop_step.py` | none | Manual retrieve permits no file | Byte completeness and original source authenticity not established. |
| [EPI-RTE-source-review](#epi-rte-source-review) | check/evidence production | doctrine only | [EPI-OBJ-source-evaluation](#epi-obj-source-evaluation) | truth-apt transformation: indeterminate | Source suitability and mechanism evidence | see record | see record | see record | Prescribed review | Suitability for research, not every claim's truth | Reviewer supplies proposal/rejection | see record | SRC-1, `researcher/rubrics/content-curation.md` | [EPI-CLM-research-protocol](#epi-clm-research-protocol) | none | Human/judge execution unobserved. |
| [EPI-RTE-source-review](#epi-rte-source-review) | disposition/acceptance | doctrine only | [EPI-OBJ-source-evaluation](#epi-obj-source-evaluation) | no content change | Admission to research pipeline | see record | After evidence review, as prescribed | APPROVE/HUMAN_REVIEW/REJECT; see record | Advisory protocol until external actor acts | Named criterion/intended use exist for source admission, not universal truth | Reject failed gates; prepare change only after review | see record | SRC-1, `researcher/runbooks/autonomous-research-loop.md` | [EPI-CLM-research-protocol](#epi-clm-research-protocol) | none | No observed evidence-consuming acceptance decision inspected. |
| [EPI-RTE-rubric-arithmetic](#epi-rte-rubric-arithmetic) | check/evidence production | implemented | [EPI-OBJ-source-evaluation](#epi-obj-source-evaluation) | truth-apt transformation: entailed derivation | Recorded gate/score/decision consistency | see record | see record | Expected verdict and mismatch errors | Error report/nonzero exit | Arithmetic and rubric-rule consistency only | Can fail repository validation | see record | SRC-1, `researcher/scripts/validate_repo.py` | [EPI-CLM-research-protocol](#epi-clm-research-protocol) | none | Does not establish accurate scores or honest evidence. |
| [EPI-RTE-novelty-check](#epi-rte-novelty-check) | check/evidence production | implemented | [EPI-OBJ-novelty-result](#epi-obj-novelty-result) | truth-apt transformation: entailed derivation | Selected-token overlap with registry/corpus | see record | see record | pass/human_review/likely_duplicate | Return code and report | Lexical overlap only | Non-pass needs rationale at active readiness | see record | SRC-1, `researcher/scripts/novelty_check.py` | [EPI-CLM-research-protocol](#epi-clm-research-protocol) | none | Semantic novelty needs separate judgment. |
| [EPI-RTE-novelty-check](#epi-rte-novelty-check) | retention | implemented | [EPI-OBJ-novelty-result](#epi-obj-novelty-result) | no content change | Report for subsequent readiness | see record | CLI novelty command | Stored report plus optional rationale | Persists caller-readable result | No promotion to semantic acceptance | Later validator can continue based on verdict/rationale | see record | SRC-1, `researcher/scripts/research_loop.py` | none | none | State advances even when checker returns non-pass. |
| [EPI-RTE-run-readiness](#epi-rte-run-readiness) | check/evidence production | implemented | [EPI-OBJ-mechanism-proposal](#epi-obj-mechanism-proposal) | truth-apt transformation: entailed derivation | Active-run required artifacts or closed-run state | see record | see record | ok/errors | Promotion consumes predicate | Structural readiness in checked branch only | Default accepted/candidate branch can be blocked | see record | SRC-1, `researcher/scripts/validate_run.py` | [RT-CLM-maintenance-guarantees](runtime.md#rt-clm-maintenance-guarantees) | Closed-state/override exceptions | No claim-truth or authenticated-review check. |
| [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion) | disposition/acceptance | implemented | [EPI-OBJ-mechanism-proposal](#epi-obj-mechanism-proposal) | no content change | Caller recommendation and mechanism ID | see route | see route | Registry admission or rejected ledger | Symbolic append/exception | Records a recommendation; semantic acceptance not established by CLI | Allows accepted and candidate entries; blocks some invalid/duplicate inputs | see route | SRC-1, `researcher/scripts/research_loop.py` | [RT-CLM-maintenance-guarantees](runtime.md#rt-clm-maintenance-guarantees) | Candidate and accepted share append branch | Review string/rationale need not demonstrate evidence-consuming decision. |
| [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion) | retention | implemented | [EPI-OBJ-mechanism-proposal](#epi-obj-mechanism-proposal) | truth-apt transformation: non-ampliative reshaping | Projection to registry and ledgers | see route | see route | Registry fields plus separate reviewer/rationale event | File append | Evidence links retained, warrant not independently strengthened | Registry becomes input to later novelty checking | see route; deterministic novelty reader also see [EPI-RTE-novelty-check](#epi-rte-novelty-check) | SRC-1, `researcher/scripts/research_loop.py` | [EPI-CLM-research-protocol](#epi-clm-research-protocol) | none | Retention before demonstrated acceptance is not lifecycle integration. |
| [RT-RTE-router-benchmark](runtime.md#rt-rte-router-benchmark) | check/evidence production | implemented | see route | truth-apt transformation: entailed derivation | Predicted top-1/top-3 against primary fixture label | see route | see route | Correct flags, aggregate accuracy | Scoring/report writes | Agreement for the fixture and supplied descriptions | No automatic publication or skill activation | see route | SRC-1, `researcher/benchmarks/sdk-runner/src/runRouter.ts` | none | none | Reference labels and resume identity bound inference; not task correctness. |
| [EPI-RTE-trace-analysis](#epi-rte-trace-analysis) | check/evidence production | implemented | [EPI-OBJ-trace-analysis](#epi-obj-trace-analysis) | truth-apt transformation: indeterminate | Trace failures and quality | see record | see record | Parsed model judgment or fallback | Output feeds optimizer and scores | Candidate diagnosis, no calibrated truth license | Can change next prompt and stopping | see record | SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py` | [EPI-CLM-trace-analysis](#epi-clm-trace-analysis) | Truncated tool results/fallback | Requested diagnoses not evidence they occurred correctly. |
| [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization) | content transformation | implemented | see route | non-truth-apt policy/content update: rewritten system instructions; embedded truth-apt assertions remain indeterminate | Trace/analysis to prompt and optional skill | see route | see route | Revised instruction candidate | Caller/model proposal; length guard | No independent acceptance of factual assertions | Next round receives current_prompt | see route | SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py` | none | none | Specific non-entailment not established; no blanket conjecture classification. |
| [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization) | operational admission/selection/consumption | implemented | see route | no content change | Continue/stop, best/final prompt | see route | see route | Score-based continuation or selected prompt | Enforcing orchestration, not epistemic endorsement | Task-loop proxy score only | Stops calls or supplies changed system text | see route | SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py` | none | Score can be attached to successor not tested input | Final score is not independent final-prompt validation. |
| [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization) | behavior/policy adaptation | implemented | see route | non-truth-apt policy/content update: trace-fed prompt replacement | Prompt-controlled agent behavior | see route | On continued round | Updated current_prompt, optional durable artifacts/skill | System-prompt channel on next capture | No factual warrant added by prompt authority | Later capture policy can change | see route | SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py` | none | none | Live execution and improvement unobserved. |
| [RT-RTE-idea-draft](runtime.md#rt-rte-idea-draft) | content transformation | implemented | see route | truth-apt transformation: non-ampliative reshaping | Retained content to scaffold | see route | see route | Source links and first insights printed | Formatting and selection | Original source warrant unknown; evidence heading is not evaluation | Caller gets scaffold, not published claim | see route | SRC-1, `examples/digital-brain-skill/agents/scripts/idea_to_draft.py` | none | none | Omitted insights and no freshness check limit completeness. |
| [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) | operational admission/selection/consumption | doctrine only | [RT-OBJ-skill-body](runtime.md#rt-obj-skill-body) | no content change | Task-relevant instruction loading | see route | see route | Intended activated body | see [RT-BAP-skill-instruction](runtime.md#rt-bap-skill-instruction) | Delivery grants no evidential warrant | Intended guidance during host session | see behavioral-authority record | SRC-1, `README.md` | none | none | Manifest packaging is implemented; host loading itself uninspected. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-maintenance-guarantees](runtime.md#rt-clm-maintenance-guarantees) | see record | SRC-1, `README.md`, doctrine/design | see record | see [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion), [EPI-RTE-run-readiness](#epi-rte-run-readiness) | Uninspected | No execution or comparison; see record for supported forcing cases | Default protocol, not authenticated human review or universal readiness invariant | Override and closed-state branches; paid callers exist outside conservative step driver. |
| [EPI-CLM-research-protocol](#epi-clm-research-protocol) | see record | SRC-1, `researcher/runbooks/autonomous-research-loop.md`, doctrine/design | Source evidence, failed-gate rejection, semantic novelty and explicit approval prescribed | see [EPI-RTE-rubric-arithmetic](#epi-rte-rubric-arithmetic), [EPI-RTE-novelty-check](#epi-rte-novelty-check), [EPI-RTE-run-readiness](#epi-rte-run-readiness), [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion) | No reviewed research instance inspected | Rule arithmetic and lexical metrics are not independent research replication | Protocol distinguishes evidential review from deterministic gates | Source review remains external; CLI state progression is not mandatory semantic review. |
| [EPI-CLM-trace-analysis](#epi-clm-trace-analysis) | see record | SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`, doctrine/design and implementation | Explicit demand for concrete evidence and quality scores | see [EPI-RTE-trace-analysis](#epi-rte-trace-analysis), [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization) | No analysis instance supplied | No independent oracle; sampled/model-visible trace is not proof of internal causal reasoning | A model is asked to diagnose exposed traces; output can guide prompt revision | “FULL” claim does not include full tool-result payloads; parse fallback can supply a neutral score. |

## Bounded conclusion

**Acquisition and source review.** The scheduler can capture source bytes, while the manual CLI can record retrieval without bytes. Source warrant remains unknown. The rubric supplies criteria and intended use for source admission into the research pipeline: mechanism specificity, implementable artifacts, advanced relevance and identifiable source, followed by weighted scoring and overrides. This is not a criterion for accepting every proposition as true. A human or judge must apply it; the scheduler parks that work. No particular evidence-consuming acceptance decision or post-acceptance lifecycle integration was inspected. See [RT-RTE-research-step](runtime.md#rt-rte-research-step), [EPI-RTE-source-review](#epi-rte-source-review) and [EPI-RTE-run-readiness](#epi-rte-run-readiness).

**Deterministic derivations and their consumers.** Rule arithmetic derives a rubric verdict from caller-entered gates and scores; novelty derives overlap and threshold labels from selected tokens; router scoring derives fixture agreement. These are checked implementation-domain deductions, not independent confirmation of source truth, semantic novelty or task correctness. The concrete deductions in [EPI-RTE-rubric-arithmetic](#epi-rte-rubric-arithmetic) and [EPI-RTE-novelty-check](#epi-rte-novelty-check) establish this without executing the target. Active readiness consumes novelty's verdict/rationale; default promotion consumes run readiness. The supported override and closed-state routes narrow their enforcing authority. See also [RT-RTE-router-benchmark](runtime.md#rt-rte-router-benchmark).

**Retention is not acceptance.** Promotion persists mechanism fields/evidence IDs and a separate review event. Both accepted and candidate statuses enter the registry. Subsequent novelty code reads both and uses their text in overlap scoring. That gives retained records a real selection role, not a new evidential license. Rejected recommendations are retained in a rejected ledger; the inspected novelty loader reads the registry, not that ledger, so preservation of rejection does not itself implement avoidance of rediscovery. Rollback or withdrawal from the registry is not supplied by the inspected promotion function. No broader absence is asserted. See [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion) and [EPI-RTE-novelty-check](#epi-rte-novelty-check).

**Trace-fed authority is operational.** The analyzer asks for trace-grounded diagnoses, but its interpreted output and fallback numbers are not calibrated evidence of correctness. The optimization loop nevertheless consumes scores and recommendations, revises instructions and supplies them as the next round's system prompt. This implements behavior-shaping authority without a separate factual-acceptance decision. It can retain artifacts and emit a skill, but neither output label nor final score proves final-prompt improvement. Specific produced truth-apt theories, their entailment/non-entailment, claim-specific criticism and resulting acceptance are not determinable from inspected requests alone. See [EPI-RTE-trace-analysis](#epi-rte-trace-analysis) and [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization).

For the prompt-controlled optimizer boundary and within-run horizon, evidence-responsive instruction replacement is wired and a next-capture authority path exists. Actual exercise and causal dependence of subsequent behavior on that replacement are unobserved, preventing exercised self-improvement attribution; successful improvement is separately unestablished. The runtime's independent theory-builder conditions remain see [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization): localized produced theory and content-specific criticism uninspected, consumption afforded, qualifying iteration uninspected. Reflection is afforded by trace representation feeding prompt revision; fidelity and exercise remain unobserved. Learning is uninspected because no capacity gain is demonstrated. Autonomous orchestration is not evidence of autonomous theory building. Distributed-parametric parameter change remains uninspected at the provider; this does not negate the text-update route. See [RT-CMP-minimax-model](runtime.md#rt-cmp-minimax-model).

**Other reuse remains bounded.** The digital-brain consumer selects and prints retained insights under an evidence heading, preserving some text/URLs but checking neither truth nor freshness. Static skill delivery supplies behavioral guidance if an external host activates it, not proof that the guidance is warranted or followed. Available uninspected evaluators, training examples, export machinery and skill helpers prevent extending these route conclusions into a system-wide negative or a single epistemic verdict. See [RT-RTE-idea-draft](runtime.md#rt-rte-idea-draft), [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery), and the coverage table.

## Shared records

### Operative objects

#### EPI-OBJ-source-evaluation
Label: Source evaluation

Source-native identity: completed `sources/evaluations/*.json` records. Natural-language gate evidence, mechanism descriptions and limitations are carried in symbolic JSON fields consumed by deterministic checks. Storage: run-local files. SRC-1, `researcher/scripts/validate_run.py`, `researcher/rubrics/content-curation.md`. No counterpart object is declared in supplied runtime; [RT-RTE-research-step](runtime.md#rt-rte-research-step) parks the work, rather than owning the completed evaluation's semantics.

> Every approved or reviewed source must include:
> --- `researcher/rubrics/content-curation.md`

> Specific quoted or paraphrased evidence for every passing gate.
> --- `researcher/rubrics/content-curation.md`

#### EPI-OBJ-mechanism-proposal
Label: Mechanism proposal

Source-native identity: run-local `proposals/mechanism-proposal.jsonl` and its projected fields. Form: natural-language activation scenario, behavior change, evidence references and failure modes within symbolic status/ID structure. Storage: JSONL files; accepted/candidate projection goes to the registry, review rationale to a ledger. This is the material candidate object traversing [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion), not a duplicate route or new source of approval. SRC-1, `researcher/scripts/research_loop.py`.

> "activation_scenario": proposal.get("activation_scenario", ""),
> "behavior_change": proposal.get("behavior_change", ""),
> "evidence": proposal.get("evidence_claim_ids", []),
> "failure_modes": proposal.get("failure_modes", []),
> --- `researcher/scripts/research_loop.py`

#### EPI-OBJ-novelty-result
Label: Novelty result

Source-native identity: `reports/novelty-result.json`, with verdict, threshold, maximum scores, shared terms and optional human rationale. Symbolic numeric and label fields plus natural-language token/rationale strings on disk. No counterpart result object is declared in runtime; it is distinct from mechanism-admission outputs in [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion). SRC-1, `researcher/scripts/novelty_check.py`, `researcher/scripts/research_loop.py`.

> "top_mechanism_overlaps": mechanism_overlaps[:10],
> "max_corpus_score": max_corpus_score,
> "top_overlaps": overlaps[:10],
> --- `researcher/scripts/novelty_check.py`

#### EPI-OBJ-trace-analysis
Label: Trace analysis

Source-native identity: `AnalysisResult` returned by `TraceAnalyzer.analyze`. Form: natural-language diagnoses, quoted evidence and recommendations within symbolic score/type/severity fields. Storage: in-memory result; formatted text can be persisted by the optimization container. Different from the provider parameters in [RT-CMP-minimax-model](runtime.md#rt-cmp-minimax-model); supplied [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization) names the container but declares no separate analysis object. SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`.

> result = self._parse_analysis_response(analysis_text, trace.session_id)
> result.analyzer_thinking = analyzer_thinking
> result.analyzer_model = self.model
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`

### Routes

#### EPI-RTE-source-review
Label: Source evidence review

The external human or judge agent is prescribed to read retrieved evidence, apply content-curation gates/scoring and record a source decision. This is distinct from the deterministic scheduler [RT-RTE-research-step](runtime.md#rt-rte-research-step) and promotion append [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion). Endpoints: source and rubric to completed evaluation, then proposal/rejection. The rubric is a source-suitability procedure, not a proof that every imported assertion is true. SRC-1, `researcher/rubrics/content-curation.md`, `researcher/runbooks/autonomous-research-loop.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: uninspected — external evaluator execution is not supplied.
- Later read-back: completed evaluation can be consumed by evaluate/readiness; actual later review of rationale is unobserved.
- Delegated visibility: run-local evaluation/proposal files are available to subsequent agents/reviewers.
- Selection predicate: all gates, weighted score thresholds and O1–O4 overrides; failed gates reject, with human override described by rubric introduction.
- Invalidation or expiry: source refresh and conflicting-claim handling are instructed, not an automatic expiry implementation here.
- Activation or effect: prescribed rejection, human review or source approval for research/proposal work.
- Evidence limits: rubric and runbook do not establish executed evidence review, independent replication or individual claim acceptance.

Decision roles: human/judge supplies gate and dimensional judgments and decides disposition; failed gates prescribe rejection. Human override is stated. Mode: open research candidates, no reference-answer oracle. Trigger: retrieved research candidate. Proposed product change: mechanism extraction and skill proposal. Admission to published product remains a later instructed review/PR step. Preservation of rejected rationale and conflicting claims is prescribed; transactional product rollback is not supplied by this review instruction.

> If any gate fails, record `REJECT` with the failed gate and stop.
> --- `researcher/rubrics/content-curation.md`

> | Conflicting sources | Record both claims and prefer no published change until resolved |
> --- `researcher/runbooks/autonomous-research-loop.md`

#### EPI-RTE-rubric-arithmetic
Label: Rubric arithmetic validation

Endpoints: recorded evaluation booleans/numbers to recomputed total, expected rubric verdict/override and validation errors. Owner: `Validator.validate_source_eval_shape` and `expected_content_decision`; context is selected non-draft JSON with required evaluation keys in runs/fixtures. This checks the consistency of supplied judgments, not their evidential accuracy. Distinct from [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion): it runs in repository validation, whereas promotion's readiness subprocess calls the run validator. SRC-1, `researcher/scripts/validate_repo.py`, `researcher/scripts/research_loop.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: accumulated validation findings; research CLI can store repository validation reports and forward exit status.
- Later read-back: uninspected — no subsequent semantic consumer of the stored repository report was traced.
- Delegated visibility: report/stdout and repository CI check are visible to caller/reviewer; deployment enforcement is external.
- Selection predicate: non-draft JSON with required source-evaluation keys under runs/fixtures; rule mismatches produce errors.
- Invalidation or expiry: recalculated from current recorded inputs; no assurance those inputs reflect current sources.
- Activation or effect: validation errors and nonzero return can block a compliant CLI/CI workflow.
- Evidence limits: no observed run; the arithmetic license assumes the encoding and recorded inputs, not truth of gate explanations.

Decision roles: evaluator/human authors scores; code calculates rule consequences; reviewer acts on report. Answer oracle: rubric rules, not empirical ground truth. Mode: deterministic consistency check. A concrete implementation deduction: with all gates true and D1=D2=D3=D4=2, the total is 2.0, no O1–O4 branch applies, and `expected_content_decision` returns APPROVE. The same recorded inputs can be supplied without sound supporting evidence; arithmetic alone cannot detect that semantic defect. This is a code deduction, not target execution.

> if total >= 1.4:
>     return {"verdict": "APPROVE", "override_triggered": None}
> --- `researcher/scripts/validate_repo.py`

> if abs(float(recorded_total) - recomputed_total) > 0.011:
> --- `researcher/scripts/validate_repo.py`

#### EPI-RTE-novelty-check
Label: Novelty overlap check

Endpoints: selected proposal sections and registry/corpus text to token sets, Jaccard overlaps, threshold verdict and persisted report. Owner: Python checker, then research CLI recorder and run-readiness consumer. No counterpart check route in supplied runtime; [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion) supplies registry writes but is not this comparator. SRC-1, `researcher/scripts/novelty_check.py`, `researcher/scripts/research_loop.py`, `researcher/scripts/validate_run.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON/text report; exit zero for pass and two otherwise. Wrapper forwards code but records novelty_checked regardless.
- Later read-back: active run validator reloads report and requires human_review_rationale for non-pass; future novelty invocations reload accepted/candidate registry entries.
- Delegated visibility: report and shared terms available to human/judge; top lists limited to ten entries, shared terms to thirty.
- Selection predicate: structured proposal sections or salient-text fallback; accepted/candidate registry entries; skill, fixture and run Markdown, with specified exclusions.
- Invalidation or expiry: current comparator inputs are read on invocation; saved report is not automatically recomputed by readiness.
- Activation or effect: verdict/rationale controls active readiness, not automatic semantic duplicate rejection or publication.
- Evidence limits: lexical similarity can miss paraphrase or flag shared vocabulary; no observed semantic review supplied.

Decision roles: caller authors proposal and optional rationale; code derives overlap; human/LLM semantic novelty review is prescribed separately. No answer oracle beyond comparator rules. Mode: open research proposals against a finite current corpus. The check does not admit changes itself or roll them back.

Concrete text transformation: proposal text `## Mechanism\nalpha beta` yields tokens {alpha, beta}. A comparator text `alpha gamma` yields {alpha, gamma}; Jaccard is 1/3, rounded to 0.3333. If that is the maximum at default threshold 0.18, it exceeds both 0.18 and 0.315, so verdict is likely_duplicate. This follows inspected token extraction, rounding and branches; it says nothing about whether the two mechanisms are semantically duplicates. No target execution is needed.

> return len(a & b) / len(a | b)
> --- `researcher/scripts/novelty_check.py`

> if max_score >= args.threshold * 1.75:
>     verdict = "likely_duplicate"
> --- `researcher/scripts/novelty_check.py`

> if verdict != "pass" and not data.get("human_review_rationale"):
>     self.error(path, "non-pass novelty verdict requires human_review_rationale")
> --- `researcher/scripts/validate_run.py`

#### EPI-RTE-run-readiness
Label: Run readiness check
Part of: [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion)

This predicate is the check portion of promotion, not its disposition or append. It is also exposed through validate-run. Endpoints: run files to ok/findings/exit status, consumed by `run_readiness_ok`. Owner: deterministic validator. Active mode checks state, queue, evaluation status, proposal placeholders, novelty rationale and PR headings. Closed mode skips those active checks. SRC-1, `researcher/scripts/validate_run.py`, `researcher/scripts/research_loop.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON/text ok report and process exit status; wrapper can save reports and set validated state on success.
- Later read-back: report storage is wired; promotion recomputes the predicate rather than trusting a saved report.
- Delegated visibility: findings available to caller/reviewer through stdout or stored reports.
- Selection predicate: current_state selects active versus closed checks; first sorted completed evaluation supplies source status.
- Invalidation or expiry: recalculated at promotion; no automatic freshness assessment of underlying sources.
- Activation or effect: failed readiness blocks default accepted/candidate promotion; allow-unready bypasses it.
- Evidence limits: declared retrieval status, headings and rationale presence do not authenticate source bytes, approval or claim truth.

Decision roles and override/recovery are see the parent route. No independent answer oracle. For active runs the evidence-consuming computation checks recorded fields, not the cited research. The closed-state branch plus supported close CLI confirms the runtime's default-path limitation. The closure validator returns when the file is absent; it does not require a closure file even though the runtime describes closed runs as checked through closure. This refines, rather than overturns, its less-than-active-readiness conclusion. No supersession is needed for the valid promotion container.

> def validate_closure(self) -> None:
>     path = self.run_dir / "reports" / "closure.json"
>     if not path.exists():
>         return
> --- `researcher/scripts/validate_run.py`

> if current_state == "closed":
> --- `researcher/scripts/validate_run.py`

#### EPI-RTE-trace-analysis
Label: Trace analysis check
Part of: [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization)

The analysis call is a material part with different target and epistemic license from capture, rewriting and successor selection. Endpoints: exposed task/system prompt/thinking blocks, tool-call summaries and final outcome to model diagnosis, parsed patterns/scores/recommendations. Owner: `TraceAnalyzer` requests [RT-CMP-minimax-model](runtime.md#rt-cmp-minimax-model) judgment; code parses/falls back. SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: AnalysisResult from model text or fallback parser; quick_score separately returns clamped numeric result or 50.
- Later read-back: inapplicable — this subroute returns current-iteration analysis; parent owns durable artifact storage/reload.
- Delegated visibility: separate analyzer call receives thinking text, task/prompt and tool-call summaries with at most 200 characters per tool result.
- Selection predicate: prompt asks for failure-pattern evidence and quality scores; invalid pattern enums/keys can be skipped, parse failure triggers fallback.
- Invalidation or expiry: each analysis is tied to trace session ID; no independent source verification or expiry check.
- Activation or effect: parent uses overall score in continuation/ranking and analysis in prompt rewriting.
- Evidence limits: no observed diagnosis; input/result truncation and synthetic fallback weaken any score-as-measurement interpretation.

Target/domain: exposed trace behavior, not full hidden model computation, final-answer correctness or transfer. Decision roles: model proposes diagnoses/scores; parser decides usable fields; loop decides continuation. No reference-answer oracle supplied. Mode: one trace or batch of traces; optimization parent repeatedly uses one caller task. Theory-specific criticism is requested only to the extent failure descriptions/evidence/suggestions might instantiate it; no particular claim/blame/revision unit was inspected. The parent's independent theory/learning statuses are unchanged.

Concrete fallback deduction: response text `unparseable` fails JSON parsing, matches none of the fallback numeric patterns, and produces overall_score 50 with parse-failure recommendations. This number can enter weighted iteration scoring, although it is not an evidence-based quality judgment. A different supported branch parses valid JSON scores directly; therefore not every score is synthetic. The distinction must remain local.

> if result.overall_score == 0:
>     result.overall_score = 50  # Neutral default instead of 0
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`

> result = self._fallback_parse_analysis(response_text, trace_id, str(e))
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`

> f"  Result: {tc.result[:200] if tc.result else 'None'}..."
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`

### Claims

#### EPI-CLM-research-protocol
Label: Research evidence protocol

Claimed operation: evidence review and failed-gate rejection precede mechanism extraction, novelty assessment, validated proposed corpus changes and human-approved merge. Distinct from the guarantee assertions in [RT-CLM-maintenance-guarantees](runtime.md#rt-clm-maintenance-guarantees): this is the epistemic review procedure, not queue atomicity or reviewer authentication. SRC-1, `researcher/runbooks/autonomous-research-loop.md`, doctrine/design. Direct CI inspection adds only that named gates are dispatched on push/PR/manual workflow; implementations and branch-protection requirements are not implied.

> Reject failed gates immediately and log why.
> --- `researcher/runbooks/autonomous-research-loop.md`

> Use `novelty_check.py` as a fast mechanism-overlap gate, then apply human or LLM judgment for semantic novelty.
> --- `researcher/runbooks/autonomous-research-loop.md`

> Every source cited in the change was retrieved.
> --- `researcher/runbooks/autonomous-research-loop.md`

#### EPI-CLM-trace-analysis
Label: Full trace analysis

Claimed operation: the analyzer has the full reasoning trace, including thinking blocks, and should identify failure patterns with evidence. Distinct from [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization), which is a route container, not this claim. SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`, doctrine/design embedded in an implemented request. The formatter exposes all stored thinking blocks but truncates each tool result and formats selected fields, so “full” does not license complete observation of environment state or hidden reasoning.

> You have access to the FULL reasoning trace including all thinking blocks between tool calls.
> This gives you unique insight into HOW the agent reasons, not just what it outputs.
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
