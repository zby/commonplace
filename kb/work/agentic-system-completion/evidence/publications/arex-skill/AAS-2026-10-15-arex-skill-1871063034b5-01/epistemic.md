---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "AREX-Skill epistemic routes: operating guidance, bounded executable checks, paper recovery acceptance and later reliance."
run-id: AAS-2026-10-15-arex-skill-1871063034b5-01
reviewed-boundary: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
---

# AREX-Skill epistemic report

## Source-and-claim boundary

The question is how evidence becomes reusable operating guidance, what checks license reliance, and how results reach consequential consumers. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see its [Source register](boundary.md#source-register). SRC-1 supplies implementation, doctrine/design and attributed benchmark reports, not inspected executions or causal experiments. The frozen repository remains a complete artifact with partial-loop coverage.

The relevant claims are [EPI-CLM-verified-skills](#epi-clm-verified-skills), [EPI-CLM-benchmark-gains](#epi-clm-benchmark-gains) and [RT-CLM-mode-contract](runtime.md#rt-clm-mode-contract). No semantic reliability guarantee follows from the last claim's registry filtering.

| Entry point or operation | Source path in SRC-1 | Coverage and consequential limit |
| --- | --- | --- |
| CLI/SDK foreground, tools, hooks | `cli/packages/coding-agent/src/main.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/model-runtime.ts` | Supplied [RT-RTE-foreground-task](runtime.md#rt-rte-foreground-task); complete interactive/RPC and dependency-internal tools uninspected. No universal gate conclusion. |
| Skill discovery, explicit expansion, router | `cli/packages/coding-agent/src/core/skills.ts`, `cli/packages/coding-agent/src/core/agent-session.ts` | Supplied [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery), [RT-BAP-operating-guidance](runtime.md#rt-bap-operating-guidance). Delivery is not observed reliance. |
| Generic graph import, library install/update | `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/scripts/import_operating_skill_graph.mjs`, `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts` | Supplied [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission), [RT-RTE-library-update](runtime.md#rt-rte-library-update); structural checks, conflicts and caught-error rollback, not semantic acceptance. |
| Repository verification and native checks | `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`, `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/run_native_cases.py` | Direct complete reads; [EPI-RTE-native-checks](#epi-rte-native-checks). Specialized importer and reference rubrics not directly traced; no global verification-before-write enforcement established. |
| Paper comparison, artifact gates and reporting | `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`, `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/scripts/validate_distillation_run.py`, `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/scripts/write_final_report.py` | Direct complete reads; [EPI-RTE-paper-checks](#epi-rte-paper-checks), [EPI-RTE-paper-decision](#epi-rte-paper-decision), [EPI-RTE-final-report](#epi-rte-final-report). Experiment validator is called but its internal predicates are uninspected. |
| Paper QA scoring | `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/evaluate_qa.py` | Direct complete read; [EPI-RTE-qa-metrics](#epi-rte-qa-metrics). No frozen dataset or gold-answer provenance. |
| Paper refinement and deployment | `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/SKILL.md`, `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/SKILL.md` | Direct complete reads; refinement and post-acceptance deployment are prompt doctrine, not an executed autonomous controller. |
| Child schema return | `cli/packages/coding-agent/src/disco/dynamic-workflows/structured-output.ts` | Direct read plus supplied [RT-RTE-workflow-agent](runtime.md#rt-rte-workflow-agent). Shape and repair do not certify answers. |
| Compaction | `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/session-manager.ts` | Supplied [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction); semantic preservation not established. |
| Other shipped routes | `skills/task-oriented/`, `skills/repositories/repo-skills/`, `examples/`, `scripts/`, specialized import/export and workflow operations under `cli/` | Included but not individually assessed. No system-complete negative about knowledge production, criticism or acceptance. |
| Public claims | `README.md` | Direct scoped reads of verified-skills statement and benchmark comparison; [EPI-CLM-verified-skills](#epi-clm-verified-skills), [EPI-CLM-benchmark-gains](#epi-clm-benchmark-gains). |

Missing deployed state prevents identifying loaded skills and actual decisions. Missing run-linked provenance prevents attributing construction, testing or acceptance to a particular artifact. Missing controlled comparisons prevents a component-effect or transfer finding. External source repositories, papers and gold labels are not frozen, so acquired warrant is unknown rather than independently authenticated. Provider parameters and mutable endpoints remain see [RT-CMP-model-runtime](runtime.md#rt-cmp-model-runtime): inference routing is inspected; exact weights and parameter updates are not.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-skill-assertions](#epi-obj-skill-assertions) | Scoped claims about capability, prerequisites, commands and expected behavior | see record | SRC-1, `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md` | No individual generated assertion checked here. |
| [EPI-OBJ-skill-policy](#epi-obj-skill-policy) | None for imperatives as such; factual presuppositions belong to the preceding part | see record | SRC-1, `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/SKILL.md` | Changes can shape behavior without new knowledge. |
| [RT-OBJ-skill-registry](runtime.md#rt-obj-skill-registry) | Names/descriptions and locations; eligibility is symbolic policy | see record | SRC-1, `cli/packages/coding-agent/src/core/skills.ts` | Match is not validation. |
| [RT-OBJ-session-context](runtime.md#rt-obj-session-context) | User/model/tool statements and summaries, heterogeneous warrant | see record | SRC-1, `cli/packages/coding-agent/src/core/session-manager.ts` | Summary semantics and imported message truth uninspected. |
| [EPI-OBJ-recovery-evidence](#epi-obj-recovery-evidence) | Metrics, declared target, provenance and mechanism assertions, validation results | see record | SRC-1, `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py` | Files are evidence interfaces, not authenticated observations. |
| [RT-CMP-model-runtime](runtime.md#rt-cmp-model-runtime) | Particular latent propositions not determinable from available provider evidence | see record | SRC-1, `cli/packages/coding-agent/src/core/model-runtime.ts` | No claims about latent theory or learning from endpoint use. |

## Authority-route ledger

Ledger fields owned by cited records are given by reference. Each entry isolates one function even where one implementation performs several. All observation remains unestablished; architectural implementation does not mean an evaluator's semantic judgment is reliable.

Route ID: [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-skill-assertions](#epi-obj-skill-assertions)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: source/task evidence into scoped operating assertions.
Evaluator/condition and domain: Creator is instructed to ground, construct and verify; exact semantic edges depend on candidate content. Imported source claims are acquisition with unknown source warrant; rewriting may reshape, derive or conjecture, but no specific non-entailment witness establishes the last classification.
Activation and timing: see route; construction precedes requested verification.
Possible or observed result: see route.
Implemented force: no semantic-construction enforcement established; prompt-directed work.
Epistemic authority and scope: candidate only until evidence-consuming acceptance for a named use.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see [RT-BAP-operating-guidance](runtime.md#rt-bap-operating-guidance).
Evidence source ID and local anchor: SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`; minimum passage see route.
Claim IDs or none: [EPI-CLM-verified-skills](#epi-clm-verified-skills)
Mismatch marker or none: generation/installation is not knowledge acceptance.
Gap/limit: generic host support is implemented; the semantic workflow here is doctrine, not observed generation.

Route ID: [EPI-RTE-native-checks](#epi-rte-native-checks)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-assertions](#epi-obj-skill-assertions)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: selected command's recorded exit status under its supplied environment, not truth of all skill guidance.
Evaluator/condition and domain: see record; PASS follows exit zero, assuming subprocess reporting fidelity.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: process status and persisted report; procedural import blocking is separate.
Epistemic authority and scope: evidence of selected command completion only; no coverage, causal skill-effect or safe-command guarantee.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: verifier reads report; prompt-policy block on auto-import, invocation horizon.
Evidence source ID and local anchor: SRC-1, `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/run_native_cases.py`.
Claim IDs or none: [EPI-CLM-verified-skills](#epi-clm-verified-skills)
Mismatch marker or none: a runnable accelerator-labelled command can PASS without independent backend attestation.
Gap/limit: manifest safety/backend labels are supplied by the agent.

Route ID: [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission), [RT-RTE-library-update](runtime.md#rt-rte-library-update)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-operating-graph](runtime.md#rt-obj-operating-graph)
Content/update relation: no content change
Transition or check target: structurally eligible graph or digest-consistent staged official content enters live scope.
Evaluator/condition and domain: see records; names, links, collisions and bytes, not scientific correctness.
Activation and timing: see records.
Possible or observed result: see records.
Implemented force: importer/updater rejection and caught-error rollback; normal write/bash remains an alternate path.
Epistemic authority and scope: installation conveys no independent semantic endorsement.
Operational authority: behavior permitted, blocked, or changed: see records.
Behavioral-authority path: live files feed [RT-BAP-operating-guidance](runtime.md#rt-bap-operating-guidance), across sessions.
Evidence source ID and local anchor: SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/scripts/import_operating_skill_graph.mjs`, `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`; passages see records.
Claim IDs or none: [EPI-CLM-verified-skills](#epi-clm-verified-skills)
Mismatch marker or none: operational admission differs from epistemic acceptance.
Gap/limit: semantic approvals requested in prompts are not demonstrated by flags.

Route ID: [EPI-RTE-qa-metrics](#epi-rte-qa-metrics)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-recovery-evidence](#epi-obj-recovery-evidence)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: lexical exact match and token overlap between supplied prediction and supplied gold strings.
Evaluator/condition and domain: deterministic normalization and arithmetic; see record's concrete deduction.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: scores are written, not a mandatory acceptance decision.
Epistemic authority and scope: normalized string agreement; neither source truth nor unrestricted semantic equivalence.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: metrics file/stdout to caller; informational until caller uses it.
Evidence source ID and local anchor: SRC-1, `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/evaluate_qa.py`.
Claim IDs or none: none
Mismatch marker or none: article/punctuation removal can erase meaningful differences.
Gap/limit: no authenticated answer oracle or mandatory scorer-to-comparator linkage established.

Route ID: [EPI-RTE-paper-checks](#epi-rte-paper-checks)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-recovery-evidence](#epi-obj-recovery-evidence)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: declared recovery metrics, target consistency, recorded source/mechanism evidence and artifact predicates.
Evaluator/condition and domain: deterministic JSON/file checks and experiment-gate result; see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: check booleans reach decision consumer; artifact validator separately returns failure.
Epistemic authority and scope: conjunction over supplied evidence, not independent measurement or proof of causal mechanism.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: comparator decision and validator caller, machine-result channel, invocation horizon.
Evidence source ID and local anchor: SRC-1, `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`, `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/scripts/validate_distillation_run.py`.
Claim IDs or none: [EPI-CLM-verified-skills](#epi-clm-verified-skills)
Mismatch marker or none: checks require interpretation of truthful, correctly scoped inputs.
Gap/limit: experiment-validator internals uninspected; metric fallback and optional fields limit license.

Route ID: [EPI-RTE-paper-decision](#epi-rte-paper-decision)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-recovery-evidence](#epi-obj-recovery-evidence)
Content/update relation: no content change
Transition or check target: accept/refine label for recovery-backed generated-skill usability at declared target.
Evaluator/condition and domain: all comparator booleans must pass; intended use is bounded paper recovery, not general theory validation.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: report and exit code; downstream refinement/deployment is requested by doctrine.
Epistemic authority and scope: evidence-consuming acceptance architecture, conditional on supplied evidence and configured tolerance/proxy scope. No observed accepted instance established.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record; reports can withhold positive final status, prompts request another cycle.
Evidence source ID and local anchor: SRC-1, `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`.
Claim IDs or none: [EPI-CLM-verified-skills](#epi-clm-verified-skills)
Mismatch marker or none: comparator acceptance alone does not enforce hard-mode rules owned by another validator.
Gap/limit: no global write/release veto.

Route ID: [EPI-RTE-final-report](#epi-rte-final-report)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-recovery-evidence](#epi-obj-recovery-evidence)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: saved validation/analysis results grouped into artifact index and issues.
Evaluator/condition and domain: no new experiment; issue aggregation over fields, see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: reports persisted even when status is false; failure exit signals caller.
Epistemic authority and scope: traceable reporting of prior results, not new warrant for mechanism or transfer.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: operator/controller reads final JSON/Markdown and status, run-report horizon.
Evidence source ID and local anchor: SRC-1, `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/scripts/write_final_report.py`.
Claim IDs or none: none
Mismatch marker or none: report existence is not acceptance.
Gap/limit: missing analysis decision is tolerated by the reporter's status expression.

Route ID: [EPI-RTE-paper-decision](#epi-rte-paper-decision)
Route function: behavior/policy adaptation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-skill-policy](#epi-obj-skill-policy)
Content/update relation: non-truth-apt policy/content update: revise workflow guidance, output contracts and harness instructions in response to feedback
Transition or check target: refine result into another validation/recovery cycle within budget.
Evaluator/condition and domain: model follows paper-distiller prompt; evidence and feedback shape proposed repairs.
Activation and timing: see record; no exercised cycle supplied.
Possible or observed result: requested revisions or stop at exhausted budget.
Implemented force: prompt policy, not automatic semantic repair.
Epistemic authority and scope: direct behavior adaptation can occur without producing a truth-apt claim.
Operational authority: behavior permitted, blocked, or changed: requested repeat or stop; later graph import separately approved.
Behavioral-authority path: Creator reads analysis feedback, revises files, reruns checks; requested rounds-of-run horizon.
Evidence source ID and local anchor: SRC-1, `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/SKILL.md`.
Claim IDs or none: none
Mismatch marker or none: an iteration instruction is not observed criticism or improved capacity.
Gap/limit: individual theories and blame-directed revisions uninspected.

Route ID: [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-policy](#epi-obj-skill-policy), [EPI-OBJ-skill-assertions](#epi-obj-skill-assertions)
Content/update relation: no content change
Transition or check target: eligible stored guidance to model context, automatic discovery or explicit command.
Evaluator/condition and domain: role/name rules and model semantic matching, not assertion checking.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: executable delivery; natural-language guidance thereafter.
Epistemic authority and scope: availability for reliance, not certification.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see [RT-BAP-operating-guidance](runtime.md#rt-bap-operating-guidance).
Evidence source ID and local anchor: SRC-1, `cli/packages/coding-agent/src/core/agent-session.ts`; passages see route.
Claim IDs or none: [RT-CLM-mode-contract](runtime.md#rt-clm-mode-contract)
Mismatch marker or none: delivery is not compliance.
Gap/limit: no downstream behavior observed.

Route ID: [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction)
Route function: retention
Architectural status: implemented
Object/candidate ID: [RT-OBJ-session-context](runtime.md#rt-obj-session-context)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: old messages to summary plus retained tail, later reconstructed context.
Evaluator/condition and domain: model/extension supplies summary, completion checks admit it; no semantic preservation oracle established.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: replaces model-visible branch context.
Epistemic authority and scope: retained summary can be relied on without evidence-consuming semantic acceptance.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: reconstructed summary to next model invocation, context-channel force, saved-branch horizon.
Evidence source ID and local anchor: SRC-1, `cli/packages/coding-agent/src/core/session-manager.ts`; passages see route.
Claim IDs or none: none
Mismatch marker or none: compression intention does not establish preservation.
Gap/limit: content relation needs concrete input/output evidence; no novel claim is inferred from opacity.

Route ID: [RT-RTE-workflow-agent](runtime.md#rt-rte-workflow-agent)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-session-context](runtime.md#rt-obj-session-context)
Content/update relation: no content change
Transition or check target: child result's schema conformity.
Evaluator/condition and domain: schema validation and repair/coercion; semantics depend on caller's schema and evidence.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: final return gate or typed error, not answer correctness.
Epistemic authority and scope: machine-consumable shape only.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: child return to workflow code, enforcing shape gate, call horizon.
Evidence source ID and local anchor: SRC-1, `cli/packages/coding-agent/src/disco/dynamic-workflows/structured-output.ts`; supplied passage see route.
Claim IDs or none: none
Mismatch marker or none: schema success is not acceptance of a factual claim.
Gap/limit: hooks, custom gates and direct model calls prevent a universal semantic-gate claim.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-verified-skills](#epi-clm-verified-skills) | see record | SRC-1, `README.md`; doctrine/design | Source grounding, native checks, paper recovery and explicit limits | [EPI-RTE-native-checks](#epi-rte-native-checks), [EPI-RTE-paper-checks](#epi-rte-paper-checks), [EPI-RTE-paper-decision](#epi-rte-paper-decision) | None inspected | No route-linked corpus audit; different checks license different scopes | Concrete verification machinery and requested procedures exist | Corpus-wide verified/executable quality not established here. |
| [EPI-CLM-benchmark-gains](#epi-clm-benchmark-gains) | see record | SRC-1, `README.md`; reported operation | Description attributes gains to operating guidance | [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) is a plausible delivery path, not causal proof | No inspectable comparison trace supplied | Table compares whole packages, not independently varied components; experimental controls uninspected | Attributed benchmark claim only | No inferred component effect, mechanism or transfer. |
| [RT-CLM-mode-contract](runtime.md#rt-clm-mode-contract) | see record | SRC-1, `cli/packages/coding-agent/src/disco/modes/prompts.ts`; doctrine/design | Separate Creator/Researcher policies | [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) | None inspected | No isolation experiment | Registry role filtering plus behavioral policy | Direct file/shell paths defeat a stronger confinement reading. |

## Bounded conclusion

AREX-Skill offers more than retention: paper recovery has an implemented evidence-consuming accept/refine decision for declared target metrics, source/mechanism fields and executable-evidence gate results. Its criterion is conjunctive and its license is local to the declared recovery use. The criterion does not independently authenticate input evidence, prove the claimed mechanism, or establish transfer. Hard-mode artifact validation rejects declared proxy/fallback success, while comparator acceptance alone does not own that rule. Positive acceptance changes reporting and is intended to control refinement/deployment; no accepted run or actual later revision is evidenced here. See [EPI-RTE-paper-checks](#epi-rte-paper-checks), [EPI-RTE-paper-decision](#epi-rte-paper-decision) and [EPI-RTE-final-report](#epi-rte-final-report).

Native command checks and QA scores are different evaluators. Exit success licenses only selected-command completion under the recorded conditions. QA EM/F1 licenses normalized lexical comparison against supplied answers. Neither establishes all operating assertions, the gold labels' truth, or a producing process's explanatory correctness. Their implemented outputs have bounded consumers; scoring alone is not acceptance. See [EPI-RTE-native-checks](#epi-rte-native-checks) and [EPI-RTE-qa-metrics](#epi-rte-qa-metrics).

Imported source content has unknown upstream warrant in this frozen set. Guidance construction is requested to preserve evidence boundaries; without actual candidate inputs/outputs its semantic relation is indeterminate, not automatically ampliative. Deterministic metric/status derivations follow inspected rules over supplied premises, not independently warranted empirical premises. No produced, accepted ampliative claim is established. Reports reshape evidence and retain its references; observed lifecycle integration of an accepted claim remains unestablished. Installation and later guidance delivery are operational authority paths, not substitute acceptance. See [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission), [RT-RTE-library-update](runtime.md#rt-rte-library-update) and [RT-BAP-operating-guidance](runtime.md#rt-bap-operating-guidance).

Session summaries and installed instructions can reach future model calls without semantic acceptance at that consumer. Feedback-directed policy revision is also possible without a truth-apt update. Retention and wiring support neither observed improved capacity nor exercised self-improvement: update-determining evidence and later behavior causally depending on that update have not been supplied. Provider parameter learning remains uninspected. Reflection, autonomy and theory-builder conditions cannot be inferred from procedural iteration, packaging or model opacity; particular formulated theories and content-directed criticism were not individually assessed. These limits do not negate the independent positive findings about checks, acceptance architecture and behavioral delivery.

## Shared records

### Operative objects

#### EPI-OBJ-skill-assertions
Label: Operating guidance assertions

Part of: [RT-OBJ-operating-graph](runtime.md#rt-obj-operating-graph)

Source-native identity: factual clauses within SKILL.md, references and script explanations about capability, prerequisites and expected behavior. Representational form: natural language; storage substrate: graph files. Distinct from graph container, imperative policy and executable script behavior. Evidence: SRC-1, `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`. No individual generated clause or its provenance is authenticated here.

> synthetic assertions may test guidance and failure
> handling, but cannot prove that the backend actually runs.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`

#### EPI-OBJ-skill-policy
Label: Operating workflow instructions

Part of: [RT-OBJ-operating-graph](runtime.md#rt-obj-operating-graph)

Source-native identity: imperative workflow guidance in runtime skills. Representational form: natural language interpreted by a model; substrate: skill files. This part does not duplicate the factual clauses; factual presuppositions require separate scope and warrant. Evidence: SRC-1, `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/SKILL.md`.

> After any refinement, rerun module skill validation and recovery in the current distillation directory or a clearly versioned cycle subdirectory.
> --- `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/SKILL.md`

#### EPI-OBJ-recovery-evidence
Label: Recovery evidence bundle

Source-native identity: module_plan target, recovery_result metrics/mechanism checks, source manifest, runtime handoff, validation JSON and logs consumed by the paper helpers. Representational form: symbolic fields with natural-language explanations; storage: run-directory files, loaded JSON dictionaries. Distinct from [RT-OBJ-operating-graph](runtime.md#rt-obj-operating-graph): this is external check evidence, not installed guidance. Also distinct from [RT-OBJ-session-context](runtime.md#rt-obj-session-context): no claim of session history identity. Evidence: SRC-1, `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`.

> target = module_plan.get("fast_recovery_target", {}) or recovery.get("paper_target", {})
> --- `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`

### Routes

#### EPI-RTE-native-checks
Label: Native command evidence

Distinct identity: executable selected-case report producer, not the generic graph importer in [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission). It supplies evidence to repository-verification doctrine; it does not install content.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: writes per-case result JSON and summary; exit 1 for NATIVE_FAIL or BLOCKED_REQUIRED_BACKEND, otherwise 0.
- Later read-back: saved report is intended for verification review and import readiness; actual later use uninspected.
- Delegated visibility: subprocesses receive rendered command, cwd and environment; report exposes output tails, not full process internals.
- Selection predicate: agent-supplied manifest selects cases, safety class, backend metadata and command. Non-runnable classes or missing commands skip or block based on required-backend predicate.
- Invalidation or expiry: no expiry established; rerunning writes the chosen report path. Timeout becomes NATIVE_FAIL.
- Activation or effect: runs shell commands, persists statuses; prompt doctrine requests revision/import blocking. No execution observed.
- Evidence limits: helper trusts supplied safety/backend classification, checks exit code rather than backend use, and does not infer semantic skill correctness.

Owner/endpoints: verifier agent → manifest → Python helper → shell subprocess → result report → verifier. Answer oracle is command-specific and uninspected; code only interprets status. Mode is preselected verification, not a universal benchmark. Human chooses verification constraints/import policy through the task; agent selects commands and proposed repairs; the optional helper's failure can be ignored by another write path. Repository verification doctrine forbids auto-import on required-backend blocks and permits informed manual decisions after disclosure. Evidence: SRC-1, `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/run_native_cases.py`, `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`.

> "status": "PASS" if completed.returncode == 0 else "NATIVE_FAIL",
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/run_native_cases.py`

> A partial
>    environment handoff or required-backend block disables auto-import even if
>    the original request delegated it.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`

#### EPI-RTE-qa-metrics
Label: QA lexical scoring

Distinct identity: optional deterministic measurement helper; no counterpart in the supplied runtime's generic [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission) or [RT-RTE-workflow-agent](runtime.md#rt-rte-workflow-agent).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: metrics JSON/stdout with sample count, means, per-record normalized strings and best-over-answers EM/F1.
- Later read-back: uninspected — helper writes a metrics file but no mandatory adapter into recovery_result was traced.
- Delegated visibility: inapplicable — local scoring loop creates no child agent; input file supplies predictions and gold strings.
- Selection predicate: all input records; prediction/pred alias and answers/answer/gold alias; maximum per-record score over supplied answers.
- Invalidation or expiry: no expiry established; chosen output path overwritten on invocation.
- Activation or effect: produces scores, not acceptance or revision.
- Evidence limits: no gold-label authentication, semantic oracle, source-faithfulness check or mandatory acceptance consumer.

Owner/endpoints: caller's prediction file → Python normalizer/scorer → metrics file and stdout. Oracle here means supplied reference strings, whose provider/provenance is unknown, not model judgment. Concrete source deduction, without target execution: prediction `The cat!` and gold `cat` both lowercase, lose punctuation/articles and collapse whitespace to `cat`; EM and F1 are 1. Prediction `cat dog` and gold `cat` yield common=1, precision=1/2, recall=1 and F1=2/3. This is checked-rule derivation in the lexical domain, not a new empirical claim. Evidence: SRC-1, `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/evaluate_qa.py`.

> text = str(text or "").lower()
>     text = "".join(ch for ch in text if ch not in set(string.punctuation))
>     text = re.sub(r"\b(a|an|the)\b", " ", text)
>     return " ".join(text.split())
> --- `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/evaluate_qa.py`

> return 2 * precision * recall / (precision + recall)
> --- `cli/packages/coding-agent/src/disco/skills/recover-paper-result/scripts/evaluate_qa.py`

#### EPI-RTE-paper-checks
Label: Paper recovery checks

Distinct identity: paper-specific checks, extending coverage beyond [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission). Comparator and artifact validator share evidence inputs but do not have identical predicates.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: comparator builds target/source/validation/mechanism/metric booleans and issues; artifact validator emits ok/errors/missing and exit 0 or 2.
- Later read-back: reports persist for analysis, final validation and reporting consumers; no observed read-back supplied.
- Delegated visibility: experiment gate subprocess receives run directory and writes experiment_validation; internal predicates uninspected here.
- Selection predicate: module-plan fast target preferred, otherwise recovery target; requested metric preferred but first available metric may substitute. Validation directory contents are checked when supplied; separate artifact validator checks planned module files and tests metadata.
- Invalidation or expiry: checks recomputed on invocation; evidence file mutations can change result; no authenticated immutable snapshot enforced by these helpers.
- Activation or effect: booleans feed comparator decision; artifact validator rejects missing artifacts and declared hard-mode proxy/reduced/fallback success.
- Evidence limits: declared booleans, log presence, path existence and substring checks do not independently establish actual source abstention, real model load, training or mechanism causation.

Owner/endpoints: caller supplies plan/result/manifests → deterministic checks and experiment-gate subprocess → decision consumer or validation caller. Thresholds are caller-configurable; comparator defaults tolerance .05 and proxy minimum .8. Nonproxy paper targets are normalized if above 1, but recovered values are simply float-converted. Missing paper value falls back to recovered value >0. Thus license requires compatible units and meaningful target specification. This supplies a source-supported countercase to claiming all acceptance means faithful paper-target reproduction. Artifact validator separately defaults recovery mode to hard and rejects declared proxy/fallback flags; these checks cannot be attributed to the comparator alone. Evidence: SRC-1, `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`, `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/scripts/validate_distillation_run.py`.

> if recovered_value is None and metrics:
>         metric_name, recovered_value = next(iter(metrics.items()))
> --- `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`

> if recovered_float is not None:
>         if is_proxy:
>             metric_ok = recovered_float >= args.proxy_min
>         elif paper_value is not None:
>             gap = abs(recovered_float - paper_value)
>             metric_ok = gap <= args.tolerance
>         else:
>             metric_ok = recovered_float > 0.0
> --- `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`

> if mode == "hard":
>                 if recovery.get("is_proxy") is True:
>                     errors.append("hard recovery mode does not allow accepting proxy recovery as success")
> --- `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/scripts/validate_distillation_run.py`

#### EPI-RTE-paper-decision
Label: Paper recovery acceptance

Distinct identity: disposition over paper-check results, not the installed-byte admission owned by [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: analysis_report decision accept/refine, scoped metric/target/gap/flags and feedback; exit 0 for accept or 2 for refine.
- Later read-back: final reporter reads analysis; distiller doctrine requests refinement or approved deployment after final validation. No operated cycle supplied.
- Delegated visibility: report/feedback are filesystem artifacts; actual worker handoff uninspected.
- Selection predicate: conjunction of source_boundary_ok, validation_ok, target_consistency_ok, mechanism_ok and metric_ok.
- Invalidation or expiry: rerun can replace report; refusal leads requested rerun/repair rather than automatic removal of a live graph. No global withdrawal route established.
- Activation or effect: machine acceptance label and status affect reporting; model-directed refinement/deployment remains doctrine.
- Evidence limits: label's scope is generated-skill recovery usability under supplied checks; no claim of general scientific truth or observed accepted instance.

Owner/endpoints: comparator computes disposition → report consumer and caller; distiller prompt asks Creator to revise concrete module documents, skills, environment usage and harness on refine, rerun validation/recovery, stop on accept or exhausted budget, then seek deployment approval. User provides task/constraints and can veto deployment; model proposes repairs; comparator has a machine-result veto but not universal filesystem authority. Operating modes distinguish full target and proxy; expected paper outcome is supplied via plan, not independently authenticated. Acceptance criterion and intended use are those encoded in checks and declared recovery target. Accepted evidence and graph links are requested in handoff, but observed post-acceptance lifecycle integration is not established. Evidence: SRC-1, `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`, `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/SKILL.md`.

> decision = "accept" if source_boundary_ok and validation_ok and target_consistency_ok and mechanism_ok and metric_ok else "refine"
> --- `cli/packages/coding-agent/src/disco/skills/analyze-paper-recovery/scripts/compare_recovery.py`

> If analysis says `refine`, update the relevant workflow guidance, module documents, module skills, environment handoff usage, and recovery harness, then rerun steps 7-10. Stop when status is `accept` or the configured refinement budget is exhausted.
> --- `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/SKILL.md`

#### EPI-RTE-final-report
Label: Paper final reporting

Distinct identity: consumer and reporter of paper evidence, not semantic acceptance or the generic [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: final_report JSON and Markdown, printed ok/issues/paths; exit 0 when report ok else 2.
- Later read-back: saved organized report is available to operator/controller; actual later reliance uninspected.
- Delegated visibility: inapplicable — reads files and renders reports, without an agent delegation.
- Selection predicate: available manifest/config/plan, module validations, runtime/recovery/gate/analysis/final-validation artifacts; absent or malformed optional JSON is represented by empty/error objects.
- Invalidation or expiry: recomputation reads current artifacts and overwrites report targets; no evidence authenticity or expiry gate.
- Activation or effect: analysis nonaccept feedback/source/mechanism issues can become critical; ok requires final-validation true, no critical issues and analysis decision accept or missing.
- Evidence limits: missing analysis decision is tolerated; output files are written even on failure. Reporting alone does not integrate accepted knowledge into live guidance.

Owner/endpoints: paper artifacts → build_report/issue_bucket → report files and CLI status. Consumer is operator or prompt-directed controller; channel is persisted report/status, informational plus exit failure at this command's horizon. No new empirical oracle. It is a countercase to equating retained report existence with success. Evidence: SRC-1, `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/scripts/write_final_report.py`.

> report["ok"] = (
>         final_validation.get("ok") is True
>         and not report["issues"]["critical"]
>         and report["analysis"].get("decision") in {"accept", None}
>     )
> --- `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/scripts/write_final_report.py`

> write_json(json_path, report)
>     md_path.write_text(markdown_report(report, issues), encoding="utf-8")
>     print(json.dumps({"ok": report["ok"], "json": str(json_path), "markdown": str(md_path), "issues": issues}, indent=2, ensure_ascii=False))
>     return 0 if report["ok"] else 2
> --- `cli/packages/coding-agent/src/disco/skills/paper-skills-distiller/scripts/write_final_report.py`

### Claims

#### EPI-CLM-verified-skills
Label: Verified executable library

Claimed operation: published library contains thousands of verified executable skills. No counterpart after comparison with [RT-CLM-mode-contract](runtime.md#rt-clm-mode-contract), which concerns roles rather than corpus warrant. Source: SRC-1, `README.md`, doctrine/design public characterization. Verification machinery is inspected but no corpus-wide validation trace linked to this count is established.

> 🧠 <strong>5,000+ verified, executable skills</strong> distilled from <strong>1,000+ popular repositories</strong><br>
> --- `README.md`

#### EPI-CLM-benchmark-gains
Label: Benchmark improvement claim

Claimed operation: adding AREX-Skill improves Codex results across four autonomous research benchmarks. Distinct from [RT-CLM-mode-contract](runtime.md#rt-clm-mode-contract) and the verified-library claim. Source: SRC-1, `README.md`, reported operation. Numerical table is an attributed comparison, not an inspected causal experiment; experimental controls and trace-linked execution were not supplied.

> <em>Codex with AREX-Skill improves results across four autonomous research benchmarks.</em>
> --- `README.md`
