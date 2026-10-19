---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "ModularRSI epistemic routes: trajectory evidence, causal conjectures, candidate admission and later executable reliance."
run-id: AAS-2026-10-18-modularrsi-4218ceff5530-01
reviewed-boundary: b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9
---

# ModularRSI epistemic report

## Source-and-claim boundary

The question is how execution experience becomes a claim about harness behavior, how that claim or its proposed implementation is checked, and what later behavior the result controls. The functional scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); all source references below resolve to SRC-1 in its [Source register](boundary.md#source-register). This is an improvement plane including its solver, not an assessment of Harbor as an independent product.

The consequential public claim is [RT-CLM-harness-improvement](runtime.md#rt-clm-harness-improvement). The account below distinguishes task-verifier outcomes, model causal judgments, software admission and actual transfer. None licenses the others automatically. There was no target execution, provider call or test execution in this analysis. Implementation and prompt evidence establish available routes, not their successful exercise. No new source identity is introduced.

| Entry point or operation | Source path in SRC-1 | Coverage and records | Remaining limit |
|---|---|---|---|
| Evolution and evaluation launch, Phase0, task dispatch | `scripts/evolve.sh`, `scripts/evaluate.sh`, `src/harbor/agents/terminus_2_modular/self_evo/phase0.py`, `src/harbor/agents/terminus_2_modular/self_evo/task_runner.py` | Supplied [RT-RTE-solver-task](runtime.md#rt-rte-solver-task), [RT-RTE-generation-change](runtime.md#rt-rte-generation-change) | Launch wiring, not observed evolution. |
| Harbor CLI dispatch | `src/harbor/cli/main.py` | Direct full read: `run` aliases job start; task/trial/job commands are exposed. [RT-RTE-solver-task](runtime.md#rt-rte-solver-task) supplies task execution wiring. | Standalone generic `check`, `analyze`, sweep and publishing commands are not traced as ModularRSI update consumers; no all-Harbor epistemic negative follows. |
| Investigator, summary extraction, review instruction | `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py` | Direct reads of `summarize_trial`, contrast builder/preamble and review builder/preamble; [EPI-RTE-summary-extraction](#epi-rte-summary-extraction), [EPI-OBJ-contrast-finding](#epi-obj-contrast-finding) | Model compliance and actual generated claims uninspected. |
| Routing, intervention comparison, successor coverage | `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`, `src/harbor/agents/terminus_2_modular/self_evo/routing.py`, `src/harbor/agents/terminus_2_modular/self_evo/clustering.py` | Direct reads: evidence hooks, route-one, collect-evidence; routing validator/prompt; cluster-finding. [EPI-RTE-semantic-checks](#epi-rte-semantic-checks), [EPI-RTE-finding-disposition](#epi-rte-finding-disposition) | Semantic checks are model judgments, not proofs of causal diagnosis. |
| Disposition retention and routing suppression | `src/harbor/agents/terminus_2_modular/self_evo/dispositions.py`, `src/harbor/agents/terminus_2_modular/self_evo/backlog.py`, `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` | Prior disposition read; correction directly traces snapshot construction, ingestion and culprit selection; [EPI-RTE-finding-disposition](#epi-rte-finding-disposition) | Retryable status does not schedule older unattached findings. Cross-module file exists as a handoff, but automatic receiving-run consumption not established. |
| Editor registered actions: read, grep, glob, archive, validate, edit/create/edit-lines, commit, review verdict | `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py` | Direct dispatch and review/archive handler reads; supplied [RT-BAP-module-execution](runtime.md#rt-bap-module-execution); [EPI-RTE-review-decision](#epi-rte-review-decision) | Archive fallback exposes staging-derived metadata, not authenticated evolution history. File policy is not a candidate Python sandbox. |
| Smoke, action/niche checks, forced sanity, routing probe, repair and promotion | `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/smoke_tests.py`, `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py` | Supplied [RT-RTE-generation-change](runtime.md#rt-rte-generation-change); direct read of review-edit for fail-open counterexamples | No measured reward-improvement admission invariant. Other gate detail is supplied runtime evidence, not a new direct full audit. |
| Confirmation and status withdrawal | `src/harbor/agents/terminus_2_modular/self_evo/confirm.py` | Direct paired-statistics, regression predicate and variant rollback reads; helper path supplied by [RT-RTE-generation-change](runtime.md#rt-rte-generation-change); [EPI-RTE-paired-confirmation](#epi-rte-paired-confirmation) | No randomized component intervention; no deletion or universal replay veto. |
| Solver model, terminal/helper execution, completion, verifier and context handoff | `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`, `src/harbor/agents/terminus_2_modular/modules/agent_loop/baseline.py`, `src/harbor/agents/terminus_2_modular/modules/verification/baseline.py`, `src/harbor/verifier/verifier.py`, `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py` | Supplied [RT-RTE-solver-task](runtime.md#rt-rte-solver-task), [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) | Baseline does not individuate all claims in arbitrary task answers or all evolved alternatives. |
| Descriptions, archive filters, static/cached/forced selection and executable loading | `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py`, `src/harbor/agents/terminus_2_modular/library.py` | Supplied [RT-RTE-bundle-selection](runtime.md#rt-rte-bundle-selection), [RT-BAP-description-selection](runtime.md#rt-bap-description-selection), [RT-BAP-module-execution](runtime.md#rt-bap-module-execution) | Selection is not efficacy validation; imports precede ordinary choice. |
| Released library and bundled evaluation artifacts | `generations/merged_active/`, `trajectories/mergefinal/` | Boundary inventory only; individual trial bodies and variant bodies not newly inspected | Prevents observed diagnosis/admission attribution, complete variant-specific coverage and independent gain estimates. |
| Public transfer and gain narrative | `README.md` | Direct full read; [RT-CLM-harness-improvement](runtime.md#rt-clm-harness-improvement) | Reported operation, not an independent causal experiment. |

The supplied refusal also identifies optional solver skill-catalog injection through SRC-1 `src/harbor/agents/terminus_2_modular/modules/tools/baseline.py` and `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`. This operation is not directly inspected here. Complete comparisons of solver instruction discovery and subsequent skill-body consumption are therefore withheld; the existing compression account remains local, not a complete working-context inventory.

External model weights, provider behavior, unfrozen task tests and omitted evolution/verifier traces prevent assessing internal reasoning, oracle adequacy for particular tasks, full lineage and actual causal benefit respectively. Available but unread bundled trials are not access failures. Uninspected released module alternatives prevent a system-complete negative about truth-apt production or acceptance. The implemented routes below can nevertheless be assessed separately.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-trial-summary](#epi-obj-trial-summary) | see record | see record | see record | see record |
| [EPI-OBJ-contrast-finding](#epi-obj-contrast-finding) | see record | see record | see record | see record |
| [EPI-OBJ-routing-judgment](#epi-obj-routing-judgment) | see record | see record | see record | see record |
| [EPI-OBJ-behavioral-delta](#epi-obj-behavioral-delta) | see record | see record | see record | see record |
| [RT-OBJ-module-library](runtime.md#rt-obj-module-library) | Executable policy, not by itself an asserted proposition | see record | see record | A particular body may encode checkable assumptions; all bodies are not assessed here. |
| [RT-OBJ-module-description](runtime.md#rt-obj-module-description) | Capability and applicability assertions can be true or false of named variants | see record | see record | Particular assertion truth and selection compliance uninspected. |
| [RT-RTE-solver-task](runtime.md#rt-rte-solver-task) | Task input, observations and generated answers may contain truth-apt claims; exact claims not determinable here | see record | see record | Scope varies by unfrozen task. Completion signal is a control decision, not a correctness certificate. |
| [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) | Model summary/questions/answers may assert task state | see record | see record | Fidelity and individual claims not inspected. |
| [RT-CMP-lite-llm](runtime.md#rt-cmp-lite-llm) | Provider-parametric content not individually accessible | see record | see record | No weight-level conclusion about acquisition, derivation or truth checking. |

## Authority-route ledger

Rows sharing a record distinguish its consequential functions rather than declaring duplicate referents. Fields owned by a shared record are reached through `see`; the relation and architectural assessments below are local to this overlay.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-solver-task](runtime.md#rt-rte-solver-task) | content transformation | implemented | see record | truth-apt transformation: acquisition/import | Task and observed tool results enter chat | see record | see record | see record | see record | Source warrant unknown for unfrozen tasks and external tool outputs | see record | see record | see record | none | none | Transmission is not endorsement; generated answer semantics not determinable without the task and content. |
| [RT-RTE-solver-task](runtime.md#rt-rte-solver-task) | content transformation | implemented | see record | truth-apt transformation: indeterminate | Model-generated task answer or assertion | Configured model inference; no semantic preservation rule established | see record | see record | see record | Candidate content only; exact propositions and warranted premises not determinable without a task/answer pair | see record | see record | see record | none | none | Actual answer may import, reshape, derive or conjecture. Missing input/output evidence prevents deciding among them, not the implementation finding that generation is wired. |
| [RT-RTE-solver-task](runtime.md#rt-rte-solver-task) | check/evidence production | implemented | see record | no content change | Task output versus task-provided test criterion | Harbor executes configured verifier; reference outcome is task-provided, not self-completion | see record | see record | see record | At most correctness under that test's domain; encoding, coverage and hidden assumptions remain external | see record | see record | see record | none | none | No particular omitted verifier execution audited. |
| [EPI-RTE-summary-extraction](#epi-rte-summary-extraction) | content transformation | implemented | [EPI-OBJ-trial-summary](#epi-obj-trial-summary) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Preserves the selected recorded fields, not full evidence or its truth | see record | see record | see record | none | none | Bound to inspected extraction, not all heuristic failure labels. |
| [RT-RTE-generation-change](runtime.md#rt-rte-generation-change) | content transformation | implemented | [EPI-OBJ-contrast-finding](#epi-obj-contrast-finding) | truth-apt transformation: ampliative conjecture | Counterfactual effect of a module edit | Investigator asked to explain observed divergence; not an intervention experiment | see record | see record | see record | Candidate causal hypothesis only | see record | see record | see record; SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py` | none | none | Prompt's proposed change was not applied to the compared same-code rolls; its effect does not follow from their outcomes. Actual output and soundness uninspected. |
| [RT-RTE-generation-change](runtime.md#rt-rte-generation-change) | behavior/policy adaptation | implemented | [EPI-OBJ-behavioral-delta](#epi-obj-behavioral-delta) | non-truth-apt policy/content update: proposed module behavior becomes candidate Python | see record | see record | see record | see record | see record | Executability does not certify causal rationale | see record | see record | see record | none | none | Model code generation may additionally make claims; those are not individually assessed. |
| [EPI-RTE-semantic-checks](#epi-rte-semantic-checks) | check/evidence production | implemented | [EPI-OBJ-routing-judgment](#epi-obj-routing-judgment) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Responsibility, redundancy or successor coverage judgment, not task-success or transfer proof | see record | see record | see record | none | none | Reply may repeat input or add a new semantic claim; actual replies absent, so reshaping versus conjecture unresolved. |
| [EPI-RTE-finding-disposition](#epi-rte-finding-disposition) | disposition/acceptance | implemented | [EPI-OBJ-routing-judgment](#epi-obj-routing-judgment) | no content change | see record | see record | see record | see record | see record | Procedural admissibility/placement only, not acceptance of a causal claim as true | see record | see record | see record | none | none | Terminal invalidity can remove a real finding because syntax failed; it does not refute its content. |
| [EPI-RTE-finding-disposition](#epi-rte-finding-disposition) | retention | implemented | [EPI-OBJ-contrast-finding](#epi-obj-contrast-finding) | no content change | see record | see record | see record | see record | see record | Findings and reasons retained as candidates/dispositions, before causal acceptance | see record | see record | see record | none | none | Clustering links support without supplying independent confirmation. |
| [RT-RTE-generation-change](runtime.md#rt-rte-generation-change) | check/evidence production | implemented | [RT-OBJ-module-library](runtime.md#rt-obj-module-library) | no content change | Syntax, import, bundle/static contracts, declared niche/action, required activation and code crashes | see record | see record | see record | see record | Bounded compatibility and execution evidence, not improved accuracy | see record | see record | see record | [RT-CLM-harness-improvement](runtime.md#rt-clm-harness-improvement) | Quality interpretation exceeds these checks | Failure of a task alone need not reject; ordinary routing probe never gates. |
| [EPI-RTE-review-decision](#epi-rte-review-decision) | check/evidence production | implemented | [RT-OBJ-module-library](runtime.md#rt-obj-module-library) | truth-apt transformation: indeterminate | Plausible causal link and absence of task-specific overfit | see record | see record | see record | see record | Evidence-consuming model assessment, bounded by supplied trajectories and intended module use | see record | see record | see record | [RT-CLM-harness-improvement](runtime.md#rt-clm-harness-improvement) | No generalization certificate | A yes judgment is fallible; execution/compliance unobserved. |
| [EPI-RTE-review-decision](#epi-rte-review-decision) | disposition/acceptance | implemented | [RT-OBJ-module-library](runtime.md#rt-obj-module-library) | no content change | see record | see record | see record | see record | see record | Actual accept channel requests evidence-based acceptance for trying the module; skipped pass grants no epistemic acceptance | see record | see record | see record | [RT-CLM-harness-improvement](runtime.md#rt-clm-harness-improvement) | Review pass is not always reviewer acceptance | Later sanity repair can change reviewed bytes. |
| [RT-RTE-generation-change](runtime.md#rt-rte-generation-change) | retention | implemented | [RT-OBJ-module-library](runtime.md#rt-obj-module-library) | no content change | Candidate becomes numbered generation | see record | see record | see record | see record | Retained admitted executable, not necessarily an accepted causal theory | see record | see record | see record | none | none | Atomic rename does not transact archive synchronization. |
| [RT-RTE-bundle-selection](runtime.md#rt-rte-bundle-selection) | operational admission/selection/consumption | implemented | [RT-OBJ-module-description](runtime.md#rt-obj-module-description) | no content change | Per-task choice of strategies and helpers | see record | see record | see record | see record | Catalog/task judgment without reference reward; no validated capability inference | see record | see [RT-BAP-description-selection](runtime.md#rt-bap-description-selection), [RT-BAP-module-execution](runtime.md#rt-bap-module-execution) | see record | none | none | Static/cache/forced paths bypass parts of fresh selection. |
| [EPI-RTE-paired-confirmation](#epi-rte-paired-confirmation) | check/evidence production | implemented | [EPI-OBJ-trial-summary](#epi-obj-trial-summary) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | Arithmetic pass-rate difference over recorded shared-task samples only | see record | see record | see record | none | none | Observational differences do not isolate component effect. |
| [EPI-RTE-paired-confirmation](#epi-rte-paired-confirmation) | behavior/policy adaptation | implemented | [RT-OBJ-module-library](runtime.md#rt-obj-module-library) | non-truth-apt policy/content update: archive status becomes superseded | see record | see record | see record | see record | see record | Harm-screening rule, not a proposition that all remaining variants improve | see record | see record | see record | none | none | Best-effort withdrawal from normal selection, not universal rollback. |
| [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) | content transformation | implemented | see record | truth-apt transformation: indeterminate | Model summary/questions/answers replace active history | see record | see record | see record | see record | Fidelity unchecked in supplied route; non-ampliative compression cannot be assumed | see record | see record | see record | none | none | Requires actual input/output comparison to establish preservation, entailment or novel claim. |
| [RT-RTE-generation-change](runtime.md#rt-rte-generation-change) | lifecycle integration | no route found within boundary | [EPI-OBJ-contrast-finding](#epi-obj-contrast-finding) | no content change | Integration after acceptance of the causal claim as warranted | None established in the inspected finding/routing/review chain | No such causal-claim acceptance established | Retention, support linking and executable installation do occur; see records above | No distinct force established for this function | No accepted causal knowledge claim established by this chain | Other functions carry operational authority, not this asserted phase | see record | see record; [EPI-RTE-finding-disposition](#epi-rte-finding-disposition) | none | none | Scoped absence of an established phase, not a complete-system negative or denial of candidate curation. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-harness-improvement](runtime.md#rt-clm-harness-improvement) | see record | see record; SRC-1 `README.md`, reported operation | see record | [RT-RTE-generation-change](runtime.md#rt-rte-generation-change), [RT-RTE-bundle-selection](runtime.md#rt-rte-bundle-selection), [EPI-RTE-review-decision](#epi-rte-review-decision), [EPI-RTE-paired-confirmation](#epi-rte-paired-confirmation) | README reports gains; no individual bundled run audited here | Shared-task confirmation is not independent module variation; admission is not reward superiority; full training trace and external tasks absent | An experience-responsive harness-change and later-consumption mechanism exists | Reported transfer and gains remain attributed. The reading that every promotion has substantive reviewer approval or validated superiority is contradicted by fail-open review and crash/activation-only sanity. This does not refute reported benchmark outcomes. |

The search for counterexamples changed the interpretation of the gates, not the frozen public numbers: an explicit structured reject can veto, so review is not merely decorative; a timeout can pass, so it is not universal acceptance. Required activation can reject a non-crashing candidate, so sanity is not merely a crash test; nevertheless activation is not benefit. Retryable comparison failures are nonterminal, so not every failed check suppresses eligibility; this does not schedule reconsideration in a later window. Malformed routing can be terminal. These distinctions are carried in the records rather than collapsed into a system-wide verdict.

## Bounded conclusion

ModularRSI acquires task observations and task-verifier outcomes, extracts selected trace facts, and requests counterfactual explanations of why a module change would help. The recorded reward's source warrant remains task-dependent. Deterministic extraction preserves particular fields, not the entire trajectory. Its shared-task statistics derive a descriptive difference from recorded premises, not a causal explanation or transferable effect. See [RT-RTE-solver-task](runtime.md#rt-rte-solver-task), [EPI-RTE-summary-extraction](#epi-rte-summary-extraction) and [EPI-RTE-paired-confirmation](#epi-rte-paired-confirmation).

Its diagnosis instructions explicitly seek ampliative causal conjectures: a proposed intervention's effect goes beyond outcomes of the unchanged harness. Findings can be retained and clustered before evidence-consuming acceptance of that causal claim. Responsibility, redundancy and successor-coverage checks govern proposal organization and continuation, not truth of the underlying mechanism. Their force includes suppressing routing when the finding is supplied again, or leaving it eligible for another attempt without scheduling that attempt. See [EPI-OBJ-contrast-finding](#epi-obj-contrast-finding), [EPI-RTE-semantic-checks](#epi-rte-semantic-checks) and [EPI-RTE-finding-disposition](#epi-rte-finding-disposition).

There is a material evidence-consuming acceptance route for a proposed executable change: the reviewer is asked to judge trajectory-linked effectiveness and task-specific overfit for module use. That is a bounded, fallible model decision, not a causal experiment. A skipped review is operational permission without that decision; software checks and forced execution provide different licenses. Promotion installs code with later Python authority even when substantive review was skipped, and sanity repair can alter previously reviewed bytes. Descriptions separately influence task-level selection. See [EPI-RTE-review-decision](#epi-rte-review-decision), [RT-RTE-generation-change](runtime.md#rt-rte-generation-change), [RT-BAP-module-execution](runtime.md#rt-bap-module-execution) and [RT-BAP-description-selection](runtime.md#rt-bap-description-selection).

Confirmation can directly adapt policy by retiring a variant on a descriptive deficit, without accepting a natural-language explanation. This is a real downstream consumer of outcomes. Its best-effort archive status does not erase files or close static/cache/forced replay paths. Context summarization likewise grants later model-visible authority without a separately evidenced fidelity check. See [EPI-RTE-paired-confirmation](#epi-rte-paired-confirmation) and [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff).

These architecture findings coexist with the runtime's separately bounded reflection, theory-builder, autonomous-operation and improvement-directed self-change findings; none establishes improved future capacity or exercised causal self-improvement. In particular, no inspected trace closes the link from a particular retained edit to later changed behavior and benefit. Provider parameters and exact served versions remain opaque; the inspected clients invoke inference rather than weight training. Uninspected bundled trials and released alternatives prevent a complete-system negative about accepted claim production. The public transfer/gain claim remains attributed rather than independently reproduced: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change), [RT-CMP-lite-llm](runtime.md#rt-cmp-lite-llm), [RT-CLM-harness-improvement](runtime.md#rt-clm-harness-improvement).

## Shared records

### Operative objects

#### EPI-OBJ-trial-summary
Label: TrialSummary evidence fields

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

This object is the selected evidence part transported by that route, not a competing name for the entire route. Source-native identity: `TrialSummary.reward`, task/trial names, exception fields and bundle identity. Representational form: symbolic JSON-derived fields and typed summary fields; natural-language last messages remain a separately selected excerpt, not a claim of semantic equivalence. Substrate: trial `result.json` and optional `agent/trajectory.json`, then dataclass instances and rendered investigation context. Truth-apt content: what reward was recorded for this task/trial and which bundle was recorded, not independently whether the real-world task succeeded. The claimed role is evidence for contrastive diagnosis and confirmation. Provenance and oracle correctness are not established by extraction. Evidence: SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`, `summarize_trial`; passage in [EPI-RTE-summary-extraction](#epi-rte-summary-extraction). No supplied operative-object counterpart; contained in the supplied generation-change route.

#### EPI-OBJ-contrast-finding
Label: Contrast finding causal content

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

Source-native identity: `contrast_finding`, including `divergence`, `would_change_outcome`, and proposal `causal_hypothesis`. Form: natural-language descriptive and counterfactual assertions in symbolic field envelopes. Substrate: investigator output, persisted findings and proposal support, then lane briefs. This is the causal-content part of the generation-change route, distinct from its proposed behavioral instruction. Intended scope is a named locked module and task, sometimes efficiency on a passed task rather than correctness recovery. No actual generated finding is inspected, so particular truth and observed theory formulation remain uninspected. The prompt requests an effect under an edit not present in the compared same-code samples: this is conjecture, not entailed derivation. Evidence: SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`; later persistence and consumer supplied by [RT-RTE-generation-change](runtime.md#rt-rte-generation-change).

> You get the
> SAME task solved on one roll and FAILED on another (same code, different
> sampling).
> --- `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`

> 2. **The counterfactual (this IS the verdict)**: picture a concrete change to
>    `{locked}` — the specific thing our `{locked}` lacks vs the yardstick above.
>    Ask: *with that change in place, would the failing roll plausibly have reached
>    what the passing roll reached — i.e. this task moves fail → pass (or clearly
>    closer)?*
> --- `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`

#### EPI-OBJ-behavioral-delta
Label: Proposal behavioral delta

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

Source-native identity: `behavioral_delta` and proposed action/target. Form: natural-language prescription with symbolic lane/action/target identifiers. Substrate: routed output and proposal fields, then implementer brief. Role: specify what to change, not by itself assert a true causal mechanism. Its separately stored causal hypothesis belongs to [EPI-OBJ-contrast-finding](#epi-obj-contrast-finding); its executable replacement is not a part of the existing module object until installed. Evidence: SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/routing.py`, validator and template; supplied brief consumption in [RT-RTE-generation-change](runtime.md#rt-rte-generation-change). Actual proposed deltas uninspected.

> if lane != LANE_OUT_OF_SCOPE and not behavioral_delta:
>         raise InvalidRouting("behavioral_delta is required — what would change?")
> --- `src/harbor/agents/terminus_2_modular/self_evo/routing.py`

#### EPI-OBJ-routing-judgment
Label: Routing and comparison judgments

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

Source-native identities: routing responsibility/dismissals, `same_intervention`, `successor_covers`, and disposition kind/reason. Form: model-interpreted natural-language rationales plus software-consumed symbolic booleans and categories. Substrate: model replies, audit rows, proposal links and `dispositions.jsonl`. These differ from causal findings: they assert responsibility, intervention equivalence or current coverage, and govern whether an existing finding gets work rather than whether its causal explanation is true. Different targets and consumers are split in [EPI-RTE-semantic-checks](#epi-rte-semantic-checks) and [EPI-RTE-finding-disposition](#epi-rte-finding-disposition). The object is a part of the supplied broad route, with no supplied object counterpart. Evidence: SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`, `src/harbor/agents/terminus_2_modular/self_evo/clustering.py`, `src/harbor/agents/terminus_2_modular/self_evo/dispositions.py`; quotations in those route records. Particular judgment truth remains uninspected.

### Routes

#### EPI-RTE-summary-extraction
Label: Trial evidence extraction

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `TrialSummary` or None when the result is missing/unparseable.
- Later read-back: selected fields enter persisted findings/proposal evidence through the parent route; exact persisted field coverage is not fully audited here.
- Delegated visibility: investigator context receives selected summary fields, reward and trace; reviewer formatting omits reward, as supplied in the parent route.
- Selection predicate: existing parseable result; optional trajectory contributes bundle and excerpts when present.
- Invalidation or expiry: missing or invalid result prevents summary; absent trajectory leaves bundle unknown; summaries do not invalidate the original recorded result.
- Activation or effect: selected task evidence becomes available for diagnosis, not independent authentication of the test outcome.
- Evidence limits: implementation deduction only; source correctness and actual model reliance unobserved.

Owner/endpoints: driver-side `summarize_trial` maps trial files to diagnosis evidence. This is a material part of, not an alternative declaration for, the generation-change route. For a concrete static input deduction, a result object with `task_name: "t"`, `trial_name: "r"`, and `verifier_result: {rewards: {reward: 0}}` yields those names and reward zero. With no trajectory, bundle remains None; reward zero is not replaced by a fabricated pass. This preserves those selected facts conditionally on the input. It neither validates the verifier nor entails that a module caused the failure. Evidence: SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`.

> task_name = result.get("task_name") or trial_dir.name.split("__")[0]
>     trial_name = result.get("trial_name") or trial_dir.name
>     reward = (result.get("verifier_result") or {}).get("rewards", {}).get("reward")
> --- `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`

> return TrialSummary(
>         task_name=task_name,
>         trial_name=trial_name,
>         reward=reward,
> --- `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`

#### EPI-RTE-semantic-checks
Label: Routing semantic checks

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: routing decision, same-intervention boolean/reason, or successor-coverage boolean/reason.
- Later read-back: comparison and routing audit data can persist; proposal links and dispositions carry the consequential result through the disposition route.
- Delegated visibility: responsibility router receives finding and active variant descriptions; sameness judge receives deltas/hypotheses; successor judge receives finding text capped at 3000 characters and successor code capped at 6000.
- Selection predicate: active variants and locked type bound responsibility; open candidates bound comparison; mapped retired incumbent triggers successor coverage.
- Invalidation or expiry: active archive can change; already-attached or terminal findings skip future routing. A comparison exception becomes unknown, not false.
- Activation or effect: outputs are consumed by clustering and disposition, not merely logged.
- Evidence limits: model/provider semantic accuracy unobserved; textual prefix parsing is not verification of the explanation.

The owner is the evidence-pass driver; computation proposes and judges categories, with no per-finding human approval and no answer oracle. Domain and check target are separate: routing asks whose responsibility the gap is, not how well it performs; same-intervention asks whether one edit makes another redundant; successor coverage asks whether the current code closes a previously alleged gap. These are not the investigator's pass/fail oracle and do not test transfer. The structural validator checks lane/action membership, active targets and required dismissal coverage, not whether each reason is true. The implemented judge request is not proof of good judgment.

Counterexample to an unconditional fail-closed interpretation: `_yes` treats any non-YES reply as false. In particular an empty ordinary reply yields false, whereas an exception during sameness comparison is recorded as None and blocks creating a competing proposal. Successor NO allows continued work. Concrete deduction: `_yes("YES, already covered")` is true and `_yes("uncertain")` is false under the inspected function. No target execution is needed. Evidence: SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`, `src/harbor/agents/terminus_2_modular/self_evo/routing.py`; distinct semantic-check part of the supplied parent, not duplicate of its whole diagnosis/admission loop.

> def _yes(text: str) -> bool:
>     return (text or "").strip().upper().startswith("YES")
> --- `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`

> gap=str(finding.raw_finding)[:3000],
>             code=(self._source(successor_qual) if self._source else "")[:6000],
> --- `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`

> Responsibility, not quality. Ask "whose job is this?", never "is it done well?".
> --- `src/harbor/agents/terminus_2_modular/self_evo/routing.py`

#### EPI-RTE-finding-disposition
Label: Finding placement and withdrawal

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: created/linked proposal or already-clustered, out-of-scope, stale, covered, invalid or unresolved outcome, with reason/audit.
- Later read-back: proposal membership and terminal disposition IDs enter collect-evidence's placed set, filtering findings returned from the supplied snapshot. Open proposals remain available for later selection through the parent route. Retryable disposition does not cause old unattached findings to be loaded for routing; cross-module handoff writes a module-specific file, whose automatic receiving consumer is uninspected.
- Delegated visibility: clusterer receives validated routing and resolved semantic answers; future implementer briefs receive proposal/finding evidence through the parent route, not the entire judge context.
- Selection predicate: existing attachment first; then lane/live lineage/successor coverage; first same-intervention match links; unresolved candidates block creation; otherwise create.
- Invalidation or expiry: terminal kinds suppress routing if the finding is supplied again, while retryable does not; retryable status supplies no scheduling mechanism. No automatic reconsideration of a terminal semantic judgment established here. Write failures are best effort and may leave less durable state.
- Activation or effect: linkage increases a proposal's support and terminal IDs remove findings from later routing eligibility; no accepted causal claim is required.
- Evidence limits: disposition truth and successful writes unobserved; semantic false negatives and malformed outputs can affect continuation without refuting content.

Owner: deterministic clustering/ledger code, using model decisions from [EPI-RTE-semantic-checks](#epi-rte-semantic-checks). This is the disposition/retention part of the supplied parent route, not a new diagnosis loop. In this bounded curriculum, software can veto new work as invalid, stale or already covered; humans do not approve each placement. There is no reference answer for redundancy or responsibility. Trigger is a newly ingested culprit finding not already placed. Guidance, causal hypotheses and proposed deltas remain in findings/proposals; outcome reasons remain in audit/disposition state. Retention starts before any causal-claim acceptance. An unresolved comparison leaves the finding unattached, records a retryable disposition and blocks creation of an untested duplicate. This preserves the finding and outcome without terminal suppression, but does not establish next-window reconsideration. The clustering comment promising that consequence is stronger than the inspected caller: `ingest_step` returns records of the supplied snapshot, and `collect_evidence` routes only eligible culprits among those records; the online caller supplies its newly generated window snapshot, not a sweep of older unattached findings. Re-supplying an old snapshot could make a retryable finding eligible again, but this path does not schedule that resupply. Open-proposal reuse remains supported separately by the parent route. An out-of-scope disposition is a handoff, not evidence that the other module fixed anything.

Evidence: SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/clustering.py`, `src/harbor/agents/terminus_2_modular/self_evo/dispositions.py`, `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`, `src/harbor/agents/terminus_2_modular/self_evo/backlog.py`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`. This qualification agrees with the supplied [MEM-RTE-evidence-brief](memory.md#mem-rte-evidence-brief): nonterminal eligibility is distinct from scheduled reconsideration.

> TERMINAL_KINDS = frozenset({OUT_OF_SCOPE, COVERED, STALE, INVALID})
> --- `src/harbor/agents/terminus_2_modular/self_evo/dispositions.py`

> placed |= _dispositions.terminal_finding_ids(archive_root)
>     culprits = [r for r in records if r.is_culprit and r.finding_id not in placed]
> --- `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`

> records: list[FindingRecord] = []
>     for index, finding in enumerate(findings):
>         if not isinstance(finding, dict):
>             continue
>         rec = _record_of(
>             step, index, finding, prov_by_task.get(finding.get("task") or "")
>         )
>         records.append(rec)
> --- `src/harbor/agents/terminus_2_modular/self_evo/backlog.py`

> return records
> --- `src/harbor/agents/terminus_2_modular/self_evo/backlog.py`

> records = _backlog.ingest_step(archive_root, snapshot, provenance=provenance)
> --- `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`

> snapshot = {"step": step_id, "router": route.buckets, "findings": findings}
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`

> evidence_report = await _evidence.collect_evidence(
>             archive_root,
>             snapshot=snapshot,
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`

#### EPI-RTE-review-decision
Label: Review evidence and admission decision

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: accept, reject, skipped or blocked review result with reason; substantive reject can specify proposal versus implementation blame and a repair brief.
- Later read-back: outer gate consumes `passed`; parent route can route an implementation defect into a fresh build; accepted/skipped results permit later checks, not immediate guaranteed promotion.
- Delegated visibility: reviewer receives diff, intent and reward-omitting trajectory summaries in disposable staging; raw allowed trajectories remain readable. Implementer and reviewer are separate sessions.
- Selection predicate: configured review stage after earlier checks; only executed valid verdict file supplies a substantive decision, not free prose.
- Invalidation or expiry: review copy is discarded after result; skipped missing verdicts can trip circuit breaker, but timeout/exception returns precede that accounting. Sanity repair can change final bytes without renewed review in the parent gate.
- Activation or effect: explicit rejection blocks this candidate; accept and some skips allow continuation. This is permissive/enforcing gate force, not an efficacy certificate.
- Evidence limits: reviewer compliance and soundness unobserved. Architecture permits admission without evidence-consuming reviewer acceptance; actual promoted histories uninspected.

This distinct review part is contained in the supplied generation-change route. Trigger is a candidate diff; proposer is the implementer model, decider the reviewer model plus driver, with no per-content human approval in the shipped loop. Intended acceptance criterion: for MODIFY, concrete link between touched code path and observed failure; for ADD, observed failure mode, plausible mechanism and description likely to route; also no task-specific overfit. Intended use/scope: admit a module strategy into the continuing bounded task experiment. The model is asked to consume evidence, so actual structured acceptance is more than storage or novelty. It still warrants only that bounded judgment, not demonstrated causality, source truth or transfer. There is no reference answer oracle for the review; verifier rewards are intentionally omitted. The reviewer can challenge the direction or its code implementation, and implementation blame can guide repair. These are affordances for content-directed criticism, not observations that a sound theory was criticized.

Theory account for this review part: guidance asks the reviewer to criticize a causal proposal against trajectories and distinguish a bad direction from defective code; rejection reason and repair brief can survive into the next implementation attempt. Under `theory-builder conditions 1–4`, condition 1 conclusion status: afforded — intent/hypothesis is a localized unit, but actual formulated theory is uninspected; condition 2 conclusion status: wired — intent and diff reach the decision procedure, while semantic dependence in an actual decision remains uninspected; condition 3 conclusion status: afforded — requested criticism names challenged mechanism, evidence and proposal/implementation blame, but a sound criticism is not observed; condition 4 conclusion status: wired — implementation-class rejection can feed the next build, while actual iterative theory revision is uninspected. Addressability is at proposal and code-unit level, not provider-internal assumptions. Persistence reaches later builds/windows through findings, proposals and outcomes. Learning and exercised self-improvement remain uninspected; this review subroute alone establishes neither reflection nor autonomous performance of every theoretical operation. The whole-boundary, independently assessed properties remain those of [RT-RTE-generation-change](runtime.md#rt-rte-generation-change), not consequences of these four conditions.

Evidence: SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`, `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`; later repair bypass and promotion are supplied by [RT-RTE-generation-change](runtime.md#rt-rte-generation-change).

> * **MODIFIED an existing module** — is there a concrete causal link
>        between the touched code path and an actual failure you can see in the
>        trajectories? A change that targets something the trajectories don't
>        show as a problem is NOT effective.
> --- `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`

> * **NEW variant / new helper (ADD)** — it cannot have run yet (see
>        Architecture facts), so judge three things instead: (i) the failure
>        MODE it targets is actually visible in the trajectories, (ii) its
>        mechanism would plausibly change that outcome, and (iii) its
>        DESCRIPTION would lead the composer to select it on tasks resembling
>        those failures. Reject if any of the three fails — never for "it did
>        not run in this batch".
> --- `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`

> verdict = review_verdict.read_verdict_file(review_staging)
>     discard_staging(review_root)
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`

> return _ReviewResult(
>             passed=True, verdict="skipped", reason="review timed out (infra)"
>         )
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`

#### EPI-RTE-paired-confirmation
Label: Paired outcome confirmation and retirement

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: per-variant stats, shared-task delta/regressions and rolled-back names.
- Later read-back: superseded archive status affects ordinary future dynamic selection; parent runtime records editor-memory outcome use, without requiring a validated causal explanation.
- Delegated visibility: program receives task/bundle/reward tuples from retained records; provider reasoning and individual component mechanisms are not inputs to the statistic.
- Selection predicate: nonmissing reward and bundle; shared tasks for candidate and baseline, active candidates, default at least three shared tasks and delta below minus 0.34. Helper comparison instead uses presence/absence, as supplied by parent route.
- Invalidation or expiry: status change is best effort; old records remain. Dynamic filtering can avoid retired variants, but static/cache/forced routes and import-time execution are not universal vetoed paths.
- Activation or effect: `set_status` can retire the variant from normal later dynamic selection; no actual retirement or behavior change observed here.
- Evidence limits: matching task names does not randomize variant choice, time, other modules or sampling; neither arithmetic nor threshold establishes isolated causal effect or generalization.

The check target is descriptive performance of a named variant against baseline on their recorded shared tasks. Evaluator: deterministic reward thresholding and mean arithmetic. The policy target is later ordinary routing eligibility; evaluator: software margin rule. The force is archive-mediated exclusion, horizon later dynamic selections. No human chooses each retirement. The answer oracle is the recorded task-verifier reward, not the investigator's hypothesis or the model's completion assertion. A concrete implementation deduction: three tasks each with variant reward zero and baseline reward one produce three shared tasks, rates zero and one, delta minus one, hence a regression under defaults; this says nothing about the same unobserved intervention with all else held constant. Rewards below one are binarized as failure and missing rewards are skipped. The check does not require a natural-language theory to adapt behavior. This is a material subroute of the supplied generation-change record, with its own evaluator and consumer, not a duplicate for the entire admission loop.

Evidence: SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/confirm.py`; ordinary and bypass consumers from [RT-RTE-bundle-selection](runtime.md#rt-rte-bundle-selection).

> def _passed(reward) -> float:
>     return 1.0 if (reward or 0) >= 1.0 else 0.0
> --- `src/harbor/agents/terminus_2_modular/self_evo/confirm.py`

> v_rate = statistics.mean(statistics.mean(tv[(t, variant)]) for t in shared)
>     b_rate = statistics.mean(statistics.mean(tv[(t, baseline)]) for t in shared)
> --- `src/harbor/agents/terminus_2_modular/self_evo/confirm.py`

> if d and d["shared_tasks"] >= min_shared and d["delta"] < -margin:
>             out.append({"variant": v, **d})
> --- `src/harbor/agents/terminus_2_modular/self_evo/confirm.py`

> if _arch.set_status(
>                 archive_root, f"{module_type}/{reg['variant']}", "superseded"
>             ):
>                 rolled.append(reg["variant"])
> --- `src/harbor/agents/terminus_2_modular/self_evo/confirm.py`
