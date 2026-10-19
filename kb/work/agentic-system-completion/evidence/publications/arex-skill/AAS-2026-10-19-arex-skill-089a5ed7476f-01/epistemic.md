---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "AREX-Skill's evidence, verification and reliance routes, including paper-recovery acceptance and the limits of verified guidance."
run-id: AAS-2026-10-19-arex-skill-089a5ed7476f-01
reviewed-boundary: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
---

# AREX-Skill epistemic report

## Source-and-claim boundary

The question is how source material becomes operating guidance, what checks license reliance, and how results reach later behavior. Scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). SRC-1 is the only source. This is a complete artifact with partial loop inspection, not a system-wide audit.

The [runtime](runtime.md#runtime-account) is the provisional baseline. Direct source inspection adds paper-recovery scoring, experiment-evidence validation, acceptance, refinement instructions, importer helper semantics, summary generation and tool-result interception. These are implementation or doctrine/design findings, not observed operation. No target execution, example trace inspection or causal experiment was performed.

Consequential claims are [EPI-CLM-verified-skills](#epi-clm-verified-skills), [EPI-CLM-accepted-graph](#epi-clm-accepted-graph) and [EPI-CLM-benchmark-gains](#epi-clm-benchmark-gains). The strongest counterexample to a blanket absence of acceptance is the implemented paper-recovery accept/refine decision. Conversely, a passing scalar or successful import is not enough to warrant every proposition in a skill.

| Entry point or operation | Source path, all SRC-1 | Coverage and records, or uninspected limit |
| --- | --- | --- |
| CLI interactive/print/RPC dispatch | `cli/packages/coding-agent/src/main.ts` | Direct read of mode dispatch; supplied [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt) covers ordinary requests. No general answer oracle established. |
| Registered tools and hooks; direct RPC shell | `cli/packages/coding-agent/src/core/agent-session.ts` | Direct read of tool-call/result hook wiring; supplied [RT-RTE-tool-grants](runtime.md#rt-rte-tool-grants), [RT-RTE-user-bash](runtime.md#rt-rte-user-bash). Arbitrary extension handlers and provider-native operations uninspected; prevents universal evaluator or no-execution claims. |
| Creator scope/ground/construct/verify | `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md` | Direct read; [EPI-CLM-accepted-graph](#epi-clm-accepted-graph), supplied [RT-BAP-creator-guidance](runtime.md#rt-bap-creator-guidance). Actual generated propositions and their source entailment not individuated here. |
| Repository content/native verification | `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md` | Direct complete reference read; [EPI-RTE-refine-guidance](#epi-rte-refine-guidance). Agent-executed grading and native runner internals not traced; no collection-wide verified-execution conclusion. |
| Managed repository import, manual-unrouted alternative, cleanup | `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs` | Direct complete script read; [EPI-RTE-import-check](#epi-rte-import-check), supplied [RT-RTE-repo-import](runtime.md#rt-rte-repo-import). License helper and router updater internals uninspected. |
| Official library install/update | `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts` | Supplied [RT-RTE-library-update](runtime.md#rt-rte-library-update), not newly read. Snapshot authenticity and full inventory semantics unresolved. |
| Discovery, explicit invocation, router-guided reads | `cli/packages/coding-agent/src/core/skills.ts` | Supplied [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery), not newly read. No inference from delivery to compliance. |
| Session persistence and compaction | `cli/packages/coding-agent/src/core/compaction/compaction.ts` | Direct bounded read of summary generation; [EPI-RTE-summary-generation](#epi-rte-summary-generation), supplied [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction). Exact serialization, tail selection and branch-summary variants not fully traced. |
| Paper QA evaluation | `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/evaluate_qa.py` | Direct complete read; [EPI-RTE-qa-normalization](#epi-rte-qa-normalization), [EPI-RTE-qa-scoring](#epi-rte-qa-scoring). Supplied answers are references, not authenticated truth. |
| Paper recovery evidence, comparison and disposition | `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`; `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/validate_recovery_experiment.py` | Direct complete reads; [EPI-RTE-recovery-check](#epi-rte-recovery-check), [EPI-RTE-recovery-decision](#epi-rte-recovery-decision). Logs are inspected as data, not independent execution authentication. |
| Final paper gate and iterative consumer | `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/SKILL.md`; `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/scripts/validate_distillation_run.py` | Direct complete skill read and bounded final-validator read; [EPI-RTE-refine-guidance](#epi-rte-refine-guidance). Hard-mode rejection exists separately from the comparison script. Full final/report orchestration uninspected. |
| Task-oriented PassNet | `skills/task-oriented/PassNet/skills/passnet-skill/SKILL.md` | Direct opening procedure read: proposes GPU passes, matching/correctness/speedup checks and iteration. Actual evaluator implementation and later selection not traced; cannot judge kernel correctness or speedup warrant. |
| Other specialized operations | `cli/packages/coding-agent/src/disco/skills/`; `skills/task-oriented/FrontierCS/`; `skills/task-oriented/PaperBench/` | File inventory only for refresh, extension, meta-skill generation, generic import, cross-host export and other task graphs. These remain relevant, available but unassessed; prevents system-complete negatives about criticism, training, acceptance or policy adaptation. |

Missing execution traces prevent claims that the selected routes actually generated, checked, accepted or improved a particular skill. Missing per-skill source/evaluation correspondence prevents a verdict over the published collection. Uninspected external model internals prevent conclusions about parameter updates or exact weights; see [RT-CMP-model-runtime](runtime.md#rt-cmp-model-runtime). Benchmark summaries lack an inspected experimental record; they cannot establish component-level causal effects.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-skill-graph](#epi-obj-skill-graph) | Conditional claims about applicability, commands, APIs and failure recovery; individual generated claim not determinable | see record | see record | Instructions and descriptive propositions must not be conflated. |
| [EPI-OBJ-qa-records](#epi-obj-qa-records) | Predictions and supplied answers; derived EM/F1 values | see record | see record | Gold correctness, scope and dataset provenance unknown. |
| [EPI-OBJ-recovery-report](#epi-obj-recovery-report) | Recovery metric, provenance/mechanism flags, accept/refine result | see record | see record | Truth of logged execution is not independently certified. |
| [EPI-OBJ-compaction-summary](#epi-obj-compaction-summary) | Claims about prior work, decisions and remaining tasks | see record | see record | Summary fidelity not checked by a reference-answer comparison in the inspected generation function. |
| [RT-CMP-model-runtime](runtime.md#rt-cmp-model-runtime) | Internal truth-apt content not determinable | see record | see record | Distributed-parametric state is opaque; component is not itself a retained natural-language assertion. |

## Authority-route ledger

All owned fields below reside in the cited records. Repeated `see` references avoid restating their evidence and operational fields. Architectural status is this report's assessment. No row asserts observed activation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-summary-generation](#epi-rte-summary-generation) | content transformation | implemented | [EPI-OBJ-compaction-summary](#epi-obj-compaction-summary) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | none | Intended summarization is not demonstrated preservation. |
| [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction) | retention | implemented | [EPI-OBJ-compaction-summary](#epi-obj-compaction-summary) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | none | Retaining the summary is separate from accepting its assertions. |
| [EPI-RTE-import-check](#epi-rte-import-check) | check/evidence production | implemented | [EPI-OBJ-skill-graph](#epi-obj-skill-graph) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | [EPI-CLM-verified-skills](#epi-clm-verified-skills) | structural versus semantic verification | Evidence existence does not establish support. |
| [RT-RTE-repo-import](runtime.md#rt-rte-repo-import) | operational admission/selection/consumption | implemented | [EPI-OBJ-skill-graph](#epi-obj-skill-graph) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | see record | see record | see record | see record | [EPI-CLM-accepted-graph](#epi-clm-accepted-graph) | operational admission is not content acceptance | Source warrant unknown; portable guidance excludes review artifacts by policy. |
| [RT-RTE-library-update](runtime.md#rt-rte-library-update) | retention | implemented | [EPI-OBJ-skill-graph](#epi-obj-skill-graph) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | see record | see record | see record | see record | [EPI-CLM-verified-skills](#epi-clm-verified-skills) | digest integrity versus truth | Source warrant unknown. |
| [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) | operational admission/selection/consumption | implemented | [EPI-OBJ-skill-graph](#epi-obj-skill-graph) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | [EPI-CLM-accepted-graph](#epi-clm-accepted-graph) | none | Selection and prompt presence do not certify claims. |
| [EPI-RTE-qa-normalization](#epi-rte-qa-normalization) | content transformation | implemented | [EPI-OBJ-qa-records](#epi-obj-qa-records) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | semantic collision | Lexical equivalence need not preserve answer meaning. |
| [EPI-RTE-qa-scoring](#epi-rte-qa-scoring) | check/evidence production | implemented | [EPI-OBJ-qa-records](#epi-obj-qa-records) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | metric versus truth | Entailed scores are conditional on input records and normalization, not warranted gold. |
| [EPI-RTE-recovery-check](#epi-rte-recovery-check) | check/evidence production | implemented | [EPI-OBJ-recovery-report](#epi-obj-recovery-report) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | see record | [EPI-CLM-accepted-graph](#epi-clm-accepted-graph) | record checks versus execution proof | Conditional computations over supplied artifacts. |
| [EPI-RTE-recovery-decision](#epi-rte-recovery-decision) | disposition/acceptance | implemented | [EPI-OBJ-skill-graph](#epi-obj-skill-graph), [EPI-OBJ-recovery-report](#epi-obj-recovery-report) | non-truth-apt policy/content update: accept/refine label | see record | see record | see record | see record | see record | see record | see record | see record | see record | [EPI-CLM-accepted-graph](#epi-clm-accepted-graph) | proxy versus full recovery | Acceptance for declared recovery use, not blanket scientific validation. |
| [EPI-RTE-refine-guidance](#epi-rte-refine-guidance) | behavior/policy adaptation | doctrine only | [EPI-OBJ-skill-graph](#epi-obj-skill-graph) | non-truth-apt policy/content update: requested revision and deployment | see record | see record | see record | see record | see record | see record | see record | see record | see record | [EPI-CLM-accepted-graph](#epi-clm-accepted-graph) | requested versus enforced iteration | No executed revision or lifecycle integration established. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-verified-skills](#epi-clm-verified-skills) | see record | see record | see record | [EPI-RTE-import-check](#epi-rte-import-check), [RT-RTE-library-update](runtime.md#rt-rte-library-update) | none inspected | No per-skill runtime-evidence audit; library count not independently recounted | Structural gates and verification instructions exist | Does not establish every published capability is executable/correct on its intended backend. |
| [EPI-CLM-accepted-graph](#epi-clm-accepted-graph) | see record | see record | see record | [EPI-RTE-recovery-check](#epi-rte-recovery-check), [EPI-RTE-recovery-decision](#epi-rte-recovery-decision), [RT-RTE-repo-import](runtime.md#rt-rte-repo-import) | none inspected | Checks license only their domains; no generated proposition's evidence-consuming acceptance traced | Recovery acceptance is implemented; broader construction/revision is model-mediated policy | Source support, mechanism fidelity and transfer remain bounded or uninspected. |
| [EPI-CLM-benchmark-gains](#epi-clm-benchmark-gains) | see record | see record | see record | [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) supplies a plausible delivery path, not an experiment | Reported operation only, see record | No inspected intervention record, variance, task traces or independent component variation | Authors report gains for skill-equipped agents | Cannot infer causal contribution of routing, self-refinement or an individual skill. |

## Bounded conclusion

AREX-Skill supplies durable natural-language operating guidance and symbolic scripts/metadata to later model requests. The implemented import/update/delivery routes establish operational use capacity, not epistemic endorsement of each assertion; see [RT-RTE-repo-import](runtime.md#rt-rte-repo-import), [RT-RTE-library-update](runtime.md#rt-rte-library-update) and [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance). Acquired source warrant remains unknown across generated paraphrase and packaging. Provenance and digest checks preserve reference/integrity relations without proving the referenced source supports a command or explanation.

The paper route does more than store candidates. It computes lexical QA scores and checks recovery artifacts, then records an evidence-consuming accept/refine decision for generated-skill usability on the declared full/proxy target; see [EPI-RTE-qa-scoring](#epi-rte-qa-scoring), [EPI-RTE-recovery-check](#epi-rte-recovery-check) and [EPI-RTE-recovery-decision](#epi-rte-recovery-decision). Its concrete criteria, use, force and horizon are in those records. Scores are derivable within the program's lexical domain from supplied references; neither reference truth nor scientific mechanism fidelity follows. The QA normalizer can collapse distinct numerical answers. Artifact existence and success labels are weaker than independent execution attestation. The separate hard-mode gate matters: a proxy comparison can say accept while a full distillation remains ineligible.

Creator's source grounding, content criticism, native verification and module refinement are substantive policies, not absent merely because execution was not inspected; see [EPI-RTE-refine-guidance](#epi-rte-refine-guidance). No particular novel operating proposition was traced from conjecture through acceptance and lifecycle integration. Its content relation is therefore not determinable, rather than automatically ampliative. Compaction separately generates and retains claims about prior work without a semantic acceptance comparison in the inspected generation function; see [EPI-RTE-summary-generation](#epi-rte-summary-generation) and [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction).

The source supports a dormant route for revising durable behavior-shaping instructions, not demonstrated improved capacity. For the selected Creator-to-Researcher pathway, exercised self-improvement lacks a traced evidence-to-update link and subsequent behavior causally depending on that update; delivery capacity alone closes neither. Reflection and autonomous theory building are not established by the same evidence and are not inferred absent. No generated theory's localized content, dependent decision, content-directed criticism and next-round use were jointly inspected. Unassessed task graphs and workflow machinery prevent system-complete negatives. Opaque provider parameters remain independently unresolved. Reported benchmark gains do not close these gaps or yield a system-wide epistemic verdict.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-skill-graph
Label: Operating skill graph

Natural-language `SKILL.md` and references carry commands, applicability claims and recovery procedures; symbolic scripts and metadata have fixed computational consumers. They reside in staged/project/managed filesystem trees. This object is the candidate artifact shared across construction, import and later use, not a new inference component. Closest supplied routes are [RT-RTE-repo-import](runtime.md#rt-rte-repo-import) and [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery); neither declares an object counterpart. SRC-1: `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`.

> Each root and sub-skill needs a clear
> responsibility, progressive-disclosure route, evidence boundary, checks, and
> recovery behavior.
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`

Candidate generation and grounding are doctrine/design here. No concrete generated claim is individuated; import is acquisition from an external staged graph, while construction could reshape, derive or conjecture claims. That distinction cannot be resolved from a stage name.

#### EPI-OBJ-qa-records
Label: QA prediction records

JSON/JSONL text records contain natural-language predictions/answers and symbolic indices, normalized strings and floating-point EM/F1. Input files and output metric files are filesystem objects. No counterpart after comparison with the supplied runtime records; ordinary [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt) does not identify this task evaluator. SRC-1: `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/evaluate_qa.py`.

> new_record["normalized_prediction"] = normalize_answer(prediction)
> --- `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/evaluate_qa.py`

The record preserves the original fields by copying the input dictionary before adding metrics. Source truth and reference-answer authorship are not determined by the evaluator.

#### EPI-OBJ-recovery-report
Label: Recovery analysis report

Symbolic JSON fields retain target/metric, provenance and mechanism booleans, validation results and decision; natural-language feedback requests corrections. Stored in the configured output file, conventionally `analysis/analysis_report.json`. Distinct from the general session persistence in [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt); no supplied object counterpart. SRC-1: `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`.

> "decision": decision,
> "is_proxy": is_proxy,
> "metric": metric_name,
> "recovered_value": recovered_float,
> --- `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`

#### EPI-OBJ-compaction-summary
Label: Compaction summary

Natural-language text in a symbolic compaction session entry, stored through SessionManager and later projected into model context. Closest supplied record is the route [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction), not a duplicate object declaration. SRC-1: `cli/packages/coding-agent/src/core/compaction/compaction.ts`; persistence evidence is supplied by that runtime record.

> return { text: textContent, usage: response.usage };
> --- `cli/packages/coding-agent/src/core/compaction/compaction.ts`

### Routes

#### EPI-RTE-summary-generation
Label: Compaction summary generation
Part of: [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction)

This part owns the model transformation, not the parent's retention/retry/disposition semantics. AgentSession's compaction invokes the default summarizer unless an extension substitutes/cancels. `generateSummaryWithUsage` converts current messages, serializes them, adds an optional previous summary and focus, and requests model text. SRC-1 implementation: `cli/packages/coding-agent/src/core/compaction/compaction.ts`.

> const llmMessages = convertToLlm(currentMessages);
> const conversationText = serializeConversation(llmMessages);
> --- `cli/packages/coding-agent/src/core/compaction/compaction.ts`

> const textContent = contentText(response.content);
>
> return { text: textContent, usage: response.usage };
> --- `cli/packages/coding-agent/src/core/compaction/compaction.ts`

- Immediate return: summary text and provider usage, or thrown error on error stop reason.
- Later read-back: parent appends accepted compaction text and rebuilds later context; this part returns the text for that retention.
- Delegated visibility: summarizer receives converted/serialized conversation, optional previous summary and focus; downstream receives summary plus retained tail via the parent.
- Selection predicate: parent overflow/threshold/manual compaction route and default summarization branch.
- Invalidation or expiry: subsequent compaction/branch projection changes active summary use; parent cancellation prevents this path.
- Activation or effect: summary generation and later delivery are wired; semantic preservation or behavior change is unobserved.
- Evidence limits: no semantic comparison against source conversation in the inspected generation function; serialization, full partition logic and extension content are not fully inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Content relation is indeterminate: intended compression does not prove non-ampliative preservation, and no output demonstrates non-entailment. Check target here is model-request completion, not summary truth. Force is permissive content supply to the parent's session projection; no new epistemic license. Consumer/channel/horizon: later model requests through summary context, advisory natural language within and across restored sessions.

#### EPI-RTE-import-check
Label: Repository import checks
Part of: [RT-RTE-repo-import](runtime.md#rt-rte-repo-import)

This part is the check within the parent's transaction, distinct from mutation and rollback. The Node importer checks portable regular files, canonical metadata, relative Markdown links, license helper result and routing identity/hash/assignment/evidence shape. For classified handoffs it verifies evidence paths and valid line ranges. It does not read those passages to decide whether they support the assignment. SRC-1 implementation: `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`.

> if (handoff.skill_content_sha256.toLowerCase() !== digestPortableTree(skillRoot).toLowerCase()) throw new ImportError("routing handoff skill_content_sha256 does not match the verified runtime skill");
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`

> validateMarkdownLinks(skillRoot, markdownFiles);
> return { skillId, metadata, license };
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`

- Immediate return: skill identity, routing metadata and license result, or ImportError.
- Later read-back: inapplicable — this check returns current transaction data; the parent installs the retained files.
- Delegated visibility: license helper sees the tree; parent/router updater receives validation result and handoff path.
- Selection predicate: explicit staged import; normal routing handoff or explicit manual-unrouted branch requiring unclassified metadata.
- Invalidation or expiry: check is repeated after staging and live installation; changed input requires revalidation.
- Activation or effect: invalid structure/identity/link/evidence ranges can reject before or during mutation; no target operation observed.
- Evidence limits: no native-test report or semantic source-support comparison is consumed by validateRepoSkill; helper license semantics and router regeneration internals remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Target/domain: portable tree integrity, formatting, links and routing-handoff consistency. Owner/evaluator is deterministic importer code. Proposer/caller supplies skill and handoff and can select manual-unrouted; code vetoes failures, with no separate authenticated human content approval. No task answer oracle. Mode is explicit admission, not curriculum. Force: enforcing exception consumed by parent transaction; scope lasts until import completes. It licenses structural consistency, not API correctness, legal interpretation, scientific truth or informed overwrite authorization. Parent recovery restores prior skill/router/index after caught mutation failures; successful cleanup removes the private transaction directory. This is rollback of installation, not withdrawal of an epistemic claim from every already running consumer. See the parent's supplied transaction record for recovery guarantees.

#### EPI-RTE-qa-normalization
Label: QA answer normalization

A deterministic part of the QA evaluator maps prediction and reference strings to normalized tokens. No supplied counterpart after comparison with [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt); this is a specialized evaluator, not conversation completion. SRC-1 implementation: `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/evaluate_qa.py`.

> text = str(text or "").lower()
> text = "".join(ch for ch in text if ch not in set(string.punctuation))
> text = re.sub(r"\b(a|an|the)\b", " ", text)
> return " ".join(text.split())
> --- `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/evaluate_qa.py`

- Immediate return: normalized answer string.
- Later read-back: normalized predictions/answers are written in evaluated records; later scoring/report inspection can read them.
- Delegated visibility: same normalized strings go to EM/F1 computations and output records.
- Selection predicate: every prediction and reference processed by the QA script.
- Invalidation or expiry: rerunning with changed inputs or normalizer replaces output values; no independent expiry.
- Activation or effect: deterministic string transformation is implemented; no supplied run was executed.
- Evidence limits: lexical normalization is not a semantic equivalence proof over unrestricted QA answers.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete deduction, not target execution: `The Eiffel Tower!` lowercases, loses `!`, drops the article and collapses whitespace to `eiffel tower`. But `1.0` becomes `10`, while `10` stays `10`. As answers to a numerical-value question these can differ, yet normalize identically. Therefore the unrestricted truth-apt relation is indeterminate, not certified meaning-preserving reshaping. Remaining possibilities include faithful reshaping on restricted text domains and meaning-changing transformation; deciding an instance needs question/answer semantics. The transformation changes the check target and can affect equality/overlap scores. Consumer/channel/force/horizon: scoring functions via normalized strings, enforcing within one evaluation; no independent epistemic license.

#### EPI-RTE-qa-scoring
Label: QA exact-match scoring

The QA script computes normalized exact equality and token multiset F1, taking the best reference score per record and arithmetic means over records. It copies records, adds metrics and writes JSON. Distinct from normalization's transformation; no supplied specialized evaluator counterpart. SRC-1 implementation: `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/evaluate_qa.py`.

> best_em = max(exact_match(prediction, answer) for answer in answers)
> best_f1 = max(f1_score(prediction, answer) for answer in answers)
> --- `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/evaluate_qa.py`

- Immediate return: metrics printed and JSON output; ordinary successful completion returns zero.
- Later read-back: persisted metrics/records can inform recovery_result and subsequent analysis; automatic file-to-file import into recovery_result is not established.
- Delegated visibility: recovery agent is instructed to use this evaluator for QA; output includes originals, normalized forms and scores.
- Selection predicate: explicit QA evaluation call with predictions path and required output path.
- Invalidation or expiry: changed predictions/references or rerun changes scores; no semantic truth expiry policy.
- Activation or effect: numeric comparison/aggregation is implemented; recovery downstream consumption is instructed, not observed.
- Evidence limits: no supplied gold provenance or checked correspondence from this file to a concrete recovery metric; no general factuality oracle.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Check target/domain is normalized string equality/token overlap against caller-supplied answers, not unrestricted answer correctness. Reference answers are the answer oracle in this limited mode; the program does not authenticate them. Conditional derivation is entailed by inputs and formulas, not ampliative knowledge of the world. A consumer must populate recovery metrics before the separate comparison route gives it disposition force. No admission/acceptance is performed here. Policy connection, SRC-1 doctrine/design:

> If the task is QA, use `scripts/evaluate_qa.py` for EM/F1.
> --- `cli/packages/coding-agent/src/disco/skills/recover-paper-result/SKILL.md`

#### EPI-RTE-recovery-check
Label: Recovery evidence checks

The analyzer computes target consistency, source-boundary, module-validation, mechanism and metric predicates. Its subprocess invokes the experiment gate, which requires artifacts, nonempty command/invocation lists, reported successful commands, numeric metrics and additional reduced-training traces. This is distinct from the decision consumer below and has no supplied runtime counterpart after comparison with [RT-RTE-repo-import](runtime.md#rt-rte-repo-import). SRC-1 implementation: `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`; `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/validate_recovery_experiment.py`.

> elif not any(command_succeeded(item) for item in commands if isinstance(item, dict)):
>     errors.append("experiment command log contains no successful command")
> --- `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/validate_recovery_experiment.py`

> if is_proxy:
>     metric_ok = recovered_float >= args.proxy_min
> elif paper_value is not None:
>     gap = abs(recovered_float - paper_value)
>     metric_ok = gap <= args.tolerance
> else:
>     metric_ok = recovered_float > 0.0
> --- `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`

- Immediate return: booleans, issues, gap and experiment-gate result fed into the analysis report/decision.
- Later read-back: predicates and issues persist in analysis_report and experiment_validation JSON for review/refinement.
- Delegated visibility: subprocess receives attempt directory; it reads artifacts, not a fresh scientific experiment; controller gets report and feedback.
- Selection predicate: explicit analyzer call; optional manifest/validation inputs enable extra checks; experiment gate always invoked.
- Invalidation or expiry: changed recovery/plan/evidence requires rerun; script does not retract prior downstream decisions automatically.
- Activation or effect: boolean checks are wired to disposition; operations are unobserved.
- Evidence limits: log success and invocation labels do not independently prove execution, module causation, exhaustive coverage or paper-mechanism fidelity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evaluator/target: deterministic code over recovery artifacts and caller-declared metric/domain. Default tolerance is 0.05 and proxy minimum 0.8. Paper target values over 1 are divided by 100; recovered values are not equivalently normalized here. Thus target/metric encoding is a condition of meaningful comparison. A missing requested metric can fall back to the first available metric. These are implementation conditions, not evidence that a particular run misused them. Source checks rely on declared forbidden-source flags and evidence availability, not exhaustive forensic source detection. Gate success supports artifact-contract consistency only; all derivations remain conditional on the truth and encoding of inputs. No human evaluator or independent reference outcome is introduced by boolean labels. The predicates enforce only through the following decision consumer.

#### EPI-RTE-recovery-decision
Label: Recovery acceptance decision

Analyzer code consumes the predicates and writes `accept` or `refine`, feedback and exit status. It is not a duplicate of the check: its function is disposition of generated skills for the declared recovery use. No counterpart in supplied runtime admission routes, which concern installing trees. SRC-1 implementation: `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`.

> decision = "accept" if source_boundary_ok and validation_ok and target_consistency_ok and mechanism_ok and metric_ok else "refine"
> --- `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`

> return 0 if decision == "accept" else 2
> --- `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`

- Immediate return: written/printed report, accept/refine label, feedback and exit 0/2.
- Later read-back: analysis_report is the controller's instructed input for continuing/refining; no automatic deployment by this script.
- Delegated visibility: controller/user sees target, proxy flag, gap, issues and decision, not independently authenticated execution.
- Selection predicate: conjunction of source, validation, target-consistency, mechanism and metric checks.
- Invalidation or expiry: later rerun can replace decision; accepted report does not itself invalidate installed or in-flight guidance.
- Activation or effect: disposition label/status is implemented; model compliance with continuation/deployment policy unobserved.
- Evidence limits: scope is declared recovery/proxy adequacy, not acceptance of every skill proposition or proof of full-paper reproduction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposer is the recovery-producing agent/caller; deterministic code decides and vetoes failed predicates. Caller chooses target, files and thresholds; human supervision is not authenticated here. Mode is bounded recovery comparison, not open conversational completion. Oracle is the declared paper metric/target or proxy threshold plus artifact predicates, not an independent mechanism oracle. Intended use is deciding whether generated skills are usable enough for that recovery target. This is a real evidence-consuming acceptance mechanism, but a fallible, input-conditional one. Operational path: report/exit status to controller, enforcing for script success and advisory natural language for later agent decisions, lasting into the next refinement/finalization cycle. Rollback is not performed; rejection requests another cycle.

The final validator supplies a separate gate, so proxy acceptance here does not override hard recovery mode. SRC-1 implementation: `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/scripts/validate_distillation_run.py`.

> if mode == "hard":
>     if recovery.get("is_proxy") is True:
>         errors.append("hard recovery mode does not allow accepting proxy recovery as success")
> --- `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/scripts/validate_distillation_run.py`

Its result uses `ok: not missing and not errors` and exit 0/2; actual orchestration and compliance remain unobserved.

#### EPI-RTE-refine-guidance
Label: Evidence-directed refinement guidance

The paper controller instructs an agent to revise specific guidance/modules/skills/harness/environment use when analysis returns refine, rerun validation/recovery, and stop at accept or budget exhaustion. The repository verification reference independently asks for evidence-graded content review, native examples, SKILL_GAP correction and blocking backend honesty. Distinct from [RT-BAP-creator-guidance](runtime.md#rt-bap-creator-guidance): this record owns specific feedback-consuming revision contracts, not the general Creator entry point. SRC-1 doctrine/design: `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/SKILL.md`; `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md`.

> If analysis says `refine`, update the relevant workflow guidance, module documents, module skills, environment handoff usage, and recovery harness, then rerun steps 7-10. Stop when status is `accept` or the configured refinement budget is exhausted.
> --- `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/SKILL.md`

> If any assertion fails or the qualitative review reveals a gap, revise the generated skill before finishing and repeat the focused check.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md`

- Immediate return: requested revised artifacts, feedback and renewed validation, not a guaranteed executable controller return.
- Later read-back: instructed revision persists in module guidance/skill files, reports and eventual project/managed graph; later Researcher consumers are implemented by runtime delivery.
- Delegated visibility: fresh agents may receive only generated skills for usability tests; review notes are not default runtime content.
- Selection predicate: failing assertions, qualitative gaps, recovery refine or blocked required backend; user budget and hard/soft mode constrain continuation.
- Invalidation or expiry: further evidence/refinement may replace guidance; policy stops at budget exhaustion and forbids unapproved deployment/overwrite.
- Activation or effect: natural-language revision/continuation policy exists; no exercised criticism/revision cycle or later dependence traced.
- Evidence limits: model obedience and particular generated theory content remain uninspected; policy is not a software-enforced semantic gate.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Agent proposes/revises and grades evidence-backed assertions; code supplies checks; user can approve deployment or accept exact backend limitations. Native outcomes and assertion contracts are references within their stated cases, not universal answer oracles. The verification reference prohibits auto-import when required backend evidence remains blocked; source/CPU/synthetic checks cannot clear that block. This is bounded workflow policy, with explicit scope-narrowing/manual-acceptance alternatives rather than an unqualified correct/incorrect label. Review artifacts remain outside runtime skills by policy; no automatic claim-evidence integration in the runtime graph is established by that separation.

Behavioral-authority path: Creator model consumes report/feedback and verification instructions as advisory/procedural natural language during construction rounds; approved installed guidance can later influence Researcher sessions via [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance). No automatic scientific acceptance or exercise of this later path is established. Admission/recovery remains with specialized importers and their rollback routes, not the prose loop. No particular formulated theory unit or whole content-directed criticism was inspected, so theory-builder conditions 1–4, learning, reflection and autonomy are independently uninspected for exercised construction; file revision and iteration requests do not establish them.

### Claims

#### EPI-CLM-verified-skills
Label: Verified executable skills

SRC-1 doctrine/design claim in `README.md`, with verification procedures in the repository verification reference. No supplied claim counterpart.

> 🧠 <strong>5,000+ verified, executable skills</strong> distilled from <strong>1,000+ popular repositories</strong><br>
> --- `README.md`

The claim concerns collection scale and operational readiness. It is not, by itself, evidence of per-skill correctness, backend coverage or observed verification. [EPI-RTE-import-check](#epi-rte-import-check) supplies narrower structural checks; [EPI-RTE-refine-guidance](#epi-rte-refine-guidance) supplies richer verification policy.

#### EPI-CLM-accepted-graph
Label: Verified accepted graph

SRC-1 doctrine/design: `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`. Closest supplied [RT-BAP-creator-guidance](runtime.md#rt-bap-creator-guidance) concerns behavioral guidance rather than declaration of this warrant claim.

> The result is accepted graph `G` plus construction record `R`, or a
> candidate with explicit unverified blockers.
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`

The stated scope includes static, source-support, executable, graph/link and applicable task-level or representative-use checks. [EPI-RTE-recovery-decision](#epi-rte-recovery-decision) establishes a narrower implemented recovery decision; general source-supported acceptance depends on the model-mediated verification contract, not the import-success label.

#### EPI-CLM-benchmark-gains
Label: Skill-equipped benchmark gains

SRC-1 reported operation in `README.md`, distinct from all supplied runtime records. Authors assert fixed setup/harness/budget and report gains across four benchmarks; no inspected run/experimental record establishes the comparison design.

> We keep the agent setup, harness, and execution budget fixed, and change only
> whether the agent has AREX-distilled skills.
> --- `README.md`

> Codex with AREX-Skill improves results across four autonomous research benchmarks.
> --- `README.md`

Even a supported aggregate skill treatment would not isolate routing, verification, refinement or individual skill effects without additional variation. No component-level causal conclusion follows here.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; supplied [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) and [RT-BAP-creator-guidance](runtime.md#rt-bap-creator-guidance) cover delivery. New evaluator-to-decision and report-to-refinement consumers are specified in their route records above.
