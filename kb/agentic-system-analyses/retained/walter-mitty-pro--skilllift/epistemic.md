---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "SkillLift epistemic routes: rubric judgments, benchmark-backed selection, receipt calibration and unchecked fusion at the frozen revision."
run-id: AAS-2026-10-14-skilllift-0f350bf64418-01
reviewed-boundary: "599358b4d4c4a27c0e004df8228ab93026600653"
---

# SkillLift epistemic report

## Source-and-claim boundary

The question is what SkillLift checks and licenses for later reliance when it improves skills and their scoring receipts. The scope is the improvement plane in the supplied [boundary](boundary.md#boundary-and-evidence), not the external agent or benchmark grader. The evidence identity is SRC-1 in the boundary's [Source register](boundary.md#source-register). All new source inspection below is implementation, except README claims, which are doctrine/design or attributed reported operation. No target execution, trace or experiment was supplied or performed.

Skills are primarily instructions, not necessarily propositions. Receipts contain evaluative rules; verifier hits assert that a specified skill satisfies those rules. Benchmark scores assert results over a particular evaluation configuration. These are different check targets. A score that licenses an instruction for the next trial does not certify every factual claim in it. Concrete generated skill claims cannot be individuated from the inspected source alone; their truth-apt content and semantic transformation are **not determinable** without candidate artifacts linked to a generating/checking trace.

Consequential claims are [RT-CLM-mode-a](runtime.md#rt-clm-mode-a), [EPI-CLM-local-safety](#epi-clm-local-safety), [EPI-CLM-ranking-surrogate](#epi-clm-ranking-surrogate) and [EPI-CLM-ablation-mechanism](#epi-clm-ablation-mechanism). The implementation qualification [RT-CLM-refinement-replay](runtime.md#rt-clm-refinement-replay) is not a public performance claim.

| Entry point / operation | Source path, SRC-1 | Coverage and evidence basis | Remaining limit / conclusion prevented |
|---|---|---|---|
| WildClaw task dispatch and local host launch | `skilllift_eval/cli.py`; `skilllift_eval/runners/wildclaw_engine/run_batch.py` | Supplied [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution); direct CLI audit reads below | External task/host/grader source unavailable; no end-to-end correctness judgment |
| Task Mode A/B, conversion and rollback | `skilllift/skilllift/coordinator/modes.py` | Supplied [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement), [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision); direct Mode B and portfolio-conversion reads | No observed model compliance or independently warranted diagnosis |
| Rubric checking, fallback and arithmetic | `skilllift/skilllift/verifier.py`; `skilllift/skilllift/normalization.py` | Direct [EPI-RTE-verifier-check](#epi-rte-verifier-check) | Matching rubric text or calculating scores cannot certify task success |
| Receipt validation, evidence removal and evidence packing | `skilllift/skilllift/rubricator.py` | Direct [EPI-RTE-receipt-check](#epi-rte-receipt-check), [EPI-RTE-evidence-packing](#epi-rte-evidence-packing) | References are structurally required, not semantically authenticated |
| Task patch admission, store replay and adapter reward association | `skilllift/skilllift/portfolio/ref.py`; `skilllift/skilllift/portfolio/store.py`; `skilllift_eval/runners/skillsbench_portfolio_adapter.py` | Supplied runtime account and [RT-RTE-cell-recovery](runtime.md#rt-rte-cell-recovery) | Association checks do not establish evaluator validity; replay qualification retained |
| SkillsBench task route | `skilllift_eval/runners/skilllift_skillsbench_tasks.py` | Supplied runtime account | Benchmark submodule unavailable |
| SkillsBench category dispatch, training, fusion, final testing | `skilllift_eval/skillsbench_cli.py`; `skilllift_eval/runners/skilllift_skillsbench.py` | Dispatch/function search; supplied [RT-RTE-category-training](runtime.md#rt-rte-category-training); direct train/test/fusion reads [EPI-RTE-category-fusion](#epi-rte-category-fusion) | No semantic gate on fused content established by parse/name checks |
| tau2 training/fusion/held-out route and evaluator hook | `scripts/skilllift_tau2_run_domain.py`; `skilllift_eval/runners/skilllift_tau2.py` | Supplied [RT-RTE-domain-fusion](runtime.md#rt-rte-domain-fusion); direct NL-assertion defaults and reward-conversion reads [EPI-RTE-tau2-evaluator](#epi-rte-tau2-evaluator) | Sibling evaluator unavailable; cannot classify all tau2 checks as deterministic |
| Post-run audit CLI | `skilllift_eval/cli.py` | Direct [EPI-RTE-artifact-audit](#epi-rte-artifact-audit), omitted from supplied route inventory | Artifact assertions and process exit status, not optimizer withdrawal |
| Other baselines, batch launchers, injection branches, bounded-edit internals | `skilllift/skilllift/baselines/`; `scripts/`; `packages/bounded-edits/` | Included but not fully inspected; no exhaustive registered-tool/hook inventory established | Prevents a system-complete negative about other checks, cleanup or routes |

No live provider state, model-weight identity, activation trace or controlled comparison is accessible. These gaps prevent observed-operation, reliable semantic verification, generalization and causal-benefit conclusions; they do not erase the implemented checks. Available but uninspected files are not access gaps. No new source ID or expanded boundary is proposed.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-portfolio-ref](runtime.md#rt-obj-portfolio-ref) | Concrete factual claims not determinable; instructions and artifact identity coexist | see record | SRC-1, `skilllift/skilllift/portfolio/ref.py` | Skill generation may alter factual claims; no linked candidate instance inspected |
| [RT-OBJ-receipt](runtime.md#rt-obj-receipt) | Criteria encode hypotheses about useful visible behavior, plus symbolic scoring policy | see record | SRC-1, `skilllift/skilllift/rubricator.py` | Alignment on a finite batch does not warrant universal prediction |
| [EPI-OBJ-verifier-score](#epi-obj-verifier-score) | Criterion-hit assertions, rationale and arithmetic score | see record | SRC-1, `skilllift/skilllift/verifier.py` | Parse validity is not truth of the hit assertions |
| [EPI-OBJ-evidence-package](#epi-obj-evidence-package) | Imported task/skill text and attributed verifier/oracle results | see record | SRC-1, `skilllift/skilllift/rubricator.py` | Auxiliary evidence may be truncated; hidden material and trajectories excluded |

Remote model state remains the separate distributed-parametric component [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client): see that record for parameter mutability, version pinning and endpoint substitution. No inspected local weight-update call establishes provider fixity, and no weight inference is needed to establish text-mediated adaptation.

## Authority-route ledger

Each repeated generic route field below says see and cites its owner. Row suffixes label distinct functions of an existing route, not additional record IDs. No observed execution is claimed.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs | Mismatch marker | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-evidence-packing](#epi-rte-evidence-packing) | content transformation | implemented | see [EPI-OBJ-evidence-package](#epi-obj-evidence-package) | truth-apt transformation: non-ampliative reshaping | see route | see route | see route | see route | see route | see route | see route | see route | SRC-1, `skilllift/skilllift/rubricator.py` | none | none | Imported warrant remains attributed, not upgraded |
| [EPI-RTE-verifier-check](#epi-rte-verifier-check), judgment | check/evidence production | implemented | see [EPI-OBJ-verifier-score](#epi-obj-verifier-score) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | see route | see route | see route | SRC-1, `skilllift/skilllift/verifier.py` | see [EPI-CLM-ranking-surrogate](#epi-clm-ranking-surrogate) | Judgment is not an outcome oracle | Semantic faithfulness unobserved |
| [EPI-RTE-verifier-check](#epi-rte-verifier-check), arithmetic | content transformation | implemented | see [EPI-OBJ-verifier-score](#epi-obj-verifier-score) | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | see route | see route | see route | SRC-1, `skilllift/skilllift/normalization.py` | none | none | Entails numeric policy result, not premise truth |
| [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement), edit | content transformation | implemented | see [RT-OBJ-portfolio-ref](runtime.md#rt-obj-portfolio-ref) | non-truth-apt policy/content update: instruction patch; embedded factual changes indeterminate | see route | see route | see route | see route | see route | Surrogate preference only | see route | see [RT-BAP-receipt-scoring](runtime.md#rt-bap-receipt-scoring) | SRC-1, `skilllift/skilllift/coordinator/modes.py` | see [RT-CLM-mode-a](runtime.md#rt-clm-mode-a) | none | No target claim established by an edit |
| [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement), keep/reject | disposition/acceptance | implemented | see [RT-OBJ-portfolio-ref](runtime.md#rt-obj-portfolio-ref) | no content change | see route | see route | see route | see route | see route | Nondecreasing verifier score, not task correctness | see route | see [RT-BAP-receipt-scoring](runtime.md#rt-bap-receipt-scoring) | SRC-1, `skilllift/skilllift/coordinator/modes.py` | see [EPI-CLM-local-safety](#epi-clm-local-safety) | Safety exceeds metric scope if read semantically | Rejection retains prior branch |
| [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution), successor | disposition/acceptance | implemented | see [RT-OBJ-portfolio-ref](runtime.md#rt-obj-portfolio-ref) | no content change | see route | see route | see route | see route | see route | Measured reward improvement or tie plus verifier gain | see route | see [RT-BAP-skill-delivery](runtime.md#rt-bap-skill-delivery) | SRC-1, `skilllift/skilllift/coordinator/modes.py` | see [EPI-CLM-local-safety](#epi-clm-local-safety) | Tie permits surrogate influence | No general content-truth or transfer license |
| [EPI-RTE-receipt-check](#epi-rte-receipt-check) | check/evidence production | implemented | see [RT-OBJ-receipt](runtime.md#rt-obj-receipt) | no content change | see route | see route | see route | see route | see route | see route | see route | see route | SRC-1, `skilllift/skilllift/rubricator.py` | none | Structural acceptance label is not semantic acceptance | Removal declarations do not authenticate reasons |
| [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision), proposal | content transformation | implemented | see [RT-OBJ-receipt](runtime.md#rt-obj-receipt) | non-truth-apt policy/content update: scoring-policy revision; predictive assertions indeterminate | see route | see route | see route | see route | see route | Evidence-conditioned candidate scoring policy | see route | see [RT-BAP-receipt-scoring](runtime.md#rt-bap-receipt-scoring) | SRC-1, `skilllift/skilllift/coordinator/modes.py` | see [EPI-CLM-ranking-surrogate](#epi-clm-ranking-surrogate) | none | No proof of content-directed diagnosis |
| [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision), selection | disposition/acceptance | implemented | see [RT-OBJ-receipt](runtime.md#rt-obj-receipt) | no content change | see route | see route | see route | see route | see route | Best tested finite-set alignment, not guaranteed threshold attainment | see route | see [RT-BAP-receipt-scoring](runtime.md#rt-bap-receipt-scoring) | SRC-1, `skilllift/skilllift/coordinator/modes.py` | see [EPI-CLM-ranking-surrogate](#epi-clm-ranking-surrogate) | README convergence wording too strong | Iteration cap/errors may preserve old receipt |
| [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision), reuse | retention | implemented | see [RT-OBJ-receipt](runtime.md#rt-obj-receipt) | no content change | see route | see route | see route | see route | see route | No independent warrant from persistence | see route | see [RT-BAP-receipt-scoring](runtime.md#rt-bap-receipt-scoring) | SRC-1, `skilllift/skilllift/coordinator/modes.py` | none | none | Operational integration of policy, not proven integration of accepted knowledge |
| [RT-RTE-cell-recovery](runtime.md#rt-rte-cell-recovery) | lineage/freshness/recovery | implemented | see [RT-OBJ-portfolio-ref](runtime.md#rt-obj-portfolio-ref) | no content change | see route | see route | see route | see route | see route | Identity/reward association, not evaluator validity | see route | see route | SRC-1, `skilllift/skilllift/portfolio/store.py` | see [RT-CLM-refinement-replay](runtime.md#rt-clm-refinement-replay) | Refined in-memory branch may not match replay | No exactly-once remote effects |
| [EPI-RTE-category-fusion](#epi-rte-category-fusion), generation | content transformation | implemented | see [RT-OBJ-portfolio-ref](runtime.md#rt-obj-portfolio-ref) for contrast, not identity | non-truth-apt policy/content update: fused instruction package; embedded claims indeterminate | see route | see route | see route | see route | see route | see route | see route | see route | SRC-1, `skilllift_eval/runners/skilllift_skillsbench.py` | see [EPI-CLM-local-safety](#epi-clm-local-safety) | Distinct from portfolio patch gate | Complementarity requested, not checked |
| [EPI-RTE-category-fusion](#epi-rte-category-fusion), final delivery | operational admission/selection/consumption | implemented | see route | no content change | see route | see route | see route | see route | see route | see route | see route | see route | SRC-1, `skilllift_eval/runners/skilllift_skillsbench.py` | none | Operational admission precedes semantic acceptance | No pre-test oracle gate established |
| [RT-RTE-domain-fusion](runtime.md#rt-rte-domain-fusion) | operational admission/selection/consumption | implemented | see route | no content change | see route | see route | see route | see route | see route | Bundle equality and hashes do not prove fused skill truth | see route | see [RT-BAP-skill-delivery](runtime.md#rt-bap-skill-delivery) | SRC-1, `skilllift_eval/runners/skilllift_tau2.py` | none | none | Nonempty parse is not an evidence-consuming content acceptance |
| [EPI-RTE-tau2-evaluator](#epi-rte-tau2-evaluator) | check/evidence production | implemented | see route | truth-apt transformation: acquisition/import | see route | see route | see route | see route | see route | see route | see route | see route | SRC-1, `skilllift_eval/runners/skilllift_tau2.py` | none | none | External source warrant unknown |
| [EPI-RTE-artifact-audit](#epi-rte-artifact-audit) | check/evidence production | implemented | see route | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | see route | see route | see route | SRC-1, `skilllift_eval/cli.py` | none | Diagnostic failure is not withdrawal | No optimizer rollback consumer in inspected audit path |

External task/seed import and benchmark reward acquisition are endpoints of [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution); source warrant is unknown beyond inspected association checks. They are not produced knowledge merely because stored locally. Lifecycle integration of an accepted ampliative factual claim is **not determinable**: no linked claim instance, named semantic acceptance decision or subsequent evidence organization was supplied. This does not negate implemented policy retention and consumption.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-mode-a](runtime.md#rt-clm-mode-a) | see record | SRC-1, `skilllift/skilllift/coordinator/modes.py`, doctrine/design | see record | see [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement) | none supplied | No execution needed to bound inspected inner method | Verifier-only inner loop is wired | Outer round still spends oracle calls |
| [EPI-CLM-local-safety](#epi-clm-local-safety) | see record | SRC-1, `README.md`, doctrine/design | see record | see [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement), [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution), [EPI-RTE-category-fusion](#epi-rte-category-fusion) | none supplied | No intervention demonstrates semantic non-degradation | Nondecreasing surrogate and outer reward comparison are narrower safeguards | Verifier ties, task failures and separate fusion prevent broad safety reading |
| [EPI-CLM-ranking-surrogate](#epi-clm-ranking-surrogate) | see record | SRC-1, `README.md`, doctrine/design | see record | see [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision), [EPI-RTE-verifier-check](#epi-rte-verifier-check) | none supplied | Finite-batch agreement is not held-out prediction or causal explanation | Rank calibration and criterion-level model feedback implemented | Threshold not guaranteed; task portfolio may require multiple skill-scoring calls |
| [EPI-CLM-ablation-mechanism](#epi-clm-ablation-mechanism) | see record | SRC-1, `README.md`, reported operation | see record | see [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision) for mechanism only | No inspectable comparative runs supplied | Reported contrasts lack run-level design/control evidence here | An attributed ablation claim exists | Component benefit and generalization not independently established |

## Bounded conclusion

SkillLift implements two kinds of operative evaluation. Verifier judgments concern visible skill text against receipt criteria; benchmark reward concerns delegated task outcomes. Code enforces score arithmetic, output shape, patch scopes, receipt bookkeeping and finite-set selection. These checks have real permissive/enforcing consequences without licensing broader factual truth. The distinction is supported by [EPI-RTE-verifier-check](#epi-rte-verifier-check), [EPI-RTE-receipt-check](#epi-rte-receipt-check) and [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution).

The outer selector licenses a portfolio as the next parent using valid measured reward improvement, or equal reward plus a verifier advantage. The inner selector licenses continued experimentation after nondecreasing surrogate scores. Mode B licenses a scoring policy by its best tested alignment on the available champion/candidate set. None of these criteria certifies a skill's complete causal explanation, replay identity, hidden factual claims or transfer. Rejected edits keep the old branch; invalid receipt revisions can keep the old receipt; failures/iteration limits need not reach the README's alignment threshold. See [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement), [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision) and the replay qualification [RT-CLM-refinement-replay](runtime.md#rt-clm-refinement-replay).

Retained receipt text changes later verifier prompts, criterion-hit feedback and enforced threshold decisions. Retained skill text reaches later task agents as advisory instructions, not capability enforcement. This is policy adaptation with a concrete behavioral-authority path, independently of whether a factual knowledge claim was produced. See [RT-BAP-receipt-scoring](runtime.md#rt-bap-receipt-scoring) and [RT-BAP-skill-delivery](runtime.md#rt-bap-skill-delivery). Category fusion additionally admits newly composed instructions for later tests after package/name checks, rather than inheriting a winner's measured performance. tau2 master hashes certify identity, not semantic quality. The separate tau2 evaluator hook leaves the truth of imported reward dependent on an unavailable evaluator.

Imported task text, candidate files and public scores retain attributed provenance but no upgraded source warrant. Evidence packing can omit auxiliary content; it does not turn that content into a supported explanation. Arithmetic derives conditional numeric conclusions from declared hits and points. Actual ampliative factual conjecture, evidence-consuming acceptance and post-acceptance lifecycle integration remain unestablished without individuated output/trace evidence. Novel generated policy need not itself be a factual conjecture.

For theory properties, see the separately scoped account in [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision): inspectable criteria, consumption and iterative retention are wired; content-directed criticism is requested, not demonstrated. Reflection has a supported policy-feedback architecture, not observed accuracy or benefit. Learning, autonomy, reflective theory building and exercised self-improvement do not follow from alignment alone. Specifically, retained receipt policy is capable of affecting SkillLift's own subsequent operation, but no observed subsequent causal dependence or independently assessed improvement closes the exercised self-improvement pathway. Opaque provider parameters remain independently unresolved. The README's reported ablations are not a substitute for accessible run comparisons. These conclusions are route-specific, not a single epistemic score or an exhaustive system-wide negative.

## Shared records

### Operative objects

#### EPI-OBJ-verifier-score
Label: VerifierScore hit assertions and calculated score

Source-native identity: `VerifierScore` from `parse_verifier_output` or `fallback_score_skill`. Natural-language rationale/evidence expresses judgments; symbolic rubric IDs, booleans, points and ranks drive fixed score/selection rules. Substrate: Python schema objects and score artifacts persisted by the coordinator. Distinct from [RT-OBJ-receipt](runtime.md#rt-obj-receipt): this is the result of applying receipt policy to a skill, not that policy. Closest route counterpart is [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement), which consumes it. SRC-1, `skilllift/skilllift/verifier.py`.

> hits = _parse_criterion_hits(payload, receipt)
>     raw_score = compute_raw_score(receipt, hits)
>     normalized = normalize_score(raw_score, receipt.minimum_score, receipt.maximum_score)
>     rationale = str(payload.get("rationale", ""))
> --- `skilllift/skilllift/verifier.py`

#### EPI-OBJ-evidence-package
Label: Public skill evidence package

Source-native identity: return value of `build_skill_evidence_package`. Natural-language task/skill content and explanations coexist with symbolic manifests, hashes, scores and scope labels. Substrate: request dictionaries serialized for rubricator calls. It combines task, skills and score views, rather than being a material part of exactly one supplied record. Compared with [RT-OBJ-portfolio-ref](runtime.md#rt-obj-portfolio-ref) and [RT-OBJ-receipt](runtime.md#rt-obj-receipt), it is a derived multi-input evidence view, not an alternate portfolio or receipt. SRC-1, `skilllift/skilllift/rubricator.py`.

> "seed": "complete_portfolio" if budget is None else "manifest_plus_SKILL.md_plus_budgeted_auxiliary_files",
>             "trajectory": "excluded",
>             "private_evaluator_material": "excluded",
> --- `skilllift/skilllift/rubricator.py`

### Routes

#### EPI-RTE-evidence-packing
Label: Skill evidence packing and truncation

Distinct transformation supplying [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision), not a duplicate revision route. Endpoints: task, skills and score maps → `build_skill_evidence_package` → rubricator evidence. Owner: rubricator helper code. State/action: creates a public evidence view; no environment execution. SRC-1, `skilllift/skilllift/rubricator.py`. Model-side semantic preservation is not established by this deterministic packing step.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: dictionary containing public task, manifests, full SKILL.md fields, auxiliary prefixes, attributed scores and scope labels.
- Later read-back: inapplicable — this helper does not establish persistence; surrounding revision persistence is owned by the supplied route.
- Delegated visibility: complete SKILL.md under the exact key; auxiliary files sorted entrypoint-first, then referenced paths, then others, within remaining global/per-file character budget.
- Selection predicate: sorted skill/file order and configured character budget, not semantic truth selection.
- Invalidation or expiry: inapplicable — recomputed view; no independent expiry mechanism.
- Activation or effect: limits the evidence supplied for subsequent receipt proposals; does not accept their explanation.
- Evidence limits: portfolio conversion preserves paths with top-level prefixes; a package's nested SKILL.md need not occupy the exact `SKILL.md` key. Thus a complete-portfolio label is not proof every full body survives a budget. Source warrants remain attributed/unknown, not upgraded.

Concrete deduction from inspected code, not execution: a positive auxiliary budget of 4 characters and file body `abcdef` yields content `abcd`. Any claim about the omitted `ef` is unavailable through that field. This is prefix truncation, not semantic summarization. The inspected `_portfolio_to_single_skill` preserves manifest paths rather than rebasing SKILL.md. SRC-1, `skilllift/skilllift/coordinator/modes.py`.

> remaining -= limit
>             aux_files.append({"path": path, "content": content[:limit]})
> --- `skilllift/skilllift/rubricator.py`

> str(entry["path"]): (portfolio.root / str(entry["path"])).read_text(encoding="utf-8")
>         for entry in portfolio_manifest(portfolio.root)
> --- `skilllift/skilllift/coordinator/modes.py`

#### EPI-RTE-verifier-check
Label: Criterion judgment parsing and score derivation

Distinct check/arithmetic part feeding [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement) and [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision); those records own selection. Endpoints: task/skill/receipt → model judgment or lexical fallback → parser → computed score. Owner: verifier and normalization code. Context: explicitly supplied text, not benchmark execution. Output is [EPI-OBJ-verifier-score](#epi-obj-verifier-score). Check target: whether a visible skill satisfies each receipt criterion. Model evaluator domain is textual rubric interpretation; parser checks expected IDs and boolean types, not entailment. SRC-1, `skilllift/skilllift/verifier.py`; `skilllift/skilllift/normalization.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: score with hits, normalized arithmetic, rationale and optional criterion evidence; agent_skill invalid-output errors propagate.
- Later read-back: score artifacts are retained by surrounding coordinator routes; this function itself performs no durable write.
- Delegated visibility: model sees task, skill and receipt through verifier prompt; downstream consumers see scores/hits and rationale fields, not a demonstrated task execution.
- Selection predicate: client absent selects lexical fallback; invalid output for non-agent_skill can also fall back; agent_skill errors are re-raised. Parser requires exact rubric-ID set and bool values; criterion evidence is optional and strings are bounded.
- Invalidation or expiry: new scoring uses supplied receipt version; no independent semantic invalidation test.
- Activation or effect: scores feed refinement, outer tie selection and rank alignment; arithmetic is enforcing through those consumers, natural-language judgments advisory until consumed.
- Evidence limits: truth of model judgments unobserved; lexical matches are not execution evidence. This does not contradict task-path error handling because fallback conditions and skill format differ.

Proposer: model supplies hits, or code fabricates heuristic hits. Decider/veto: parser and caller error policy; no per-hit human approval. Answer oracle: none in this method; benchmark rewards are separate inputs to outer routes. Mode: static skill-text judgment, triggered by scoring/refinement/calibration. No admission of a new factual claim occurs merely through successful parse. Whether natural-language hit judgments are entailed or ampliative is indeterminate without the particular skill/criterion/response; the arithmetic relation is separately entailed.

Counterexample deduction: for a positive criterion `reconcile invoices` and skill text `check`, `_fallback_hit` returns true despite zero criterion-token matches, because any occurrence of `check` suffices. This disconfirms a universal semantic-verification reading; it does not establish that ordinary model-backed task scoring used this fallback.

> if points > 0:
>         return ratio >= 0.2 or any(word in skill_text for word in ["verify", "validate", "check", "deadline"])
> --- `skilllift/skilllift/verifier.py`

> if set(value) - expected:
>         raise VerifierError("criterion_evidence contains unknown rubric ids")
>     if not all(isinstance(item, str) for item in value.values()):
>         raise VerifierError("criterion_evidence values must be strings")
>     return {key: str(value[key])[:500] for key in value}
> --- `skilllift/skilllift/verifier.py`

For a receipt with positive point +2 and negative point -1, hits true/false give raw 2, bounds -1/2 and normalized 1.0. This follows inspected arithmetic, conditional on the supplied receipt/hits; no benchmark or source truth follows.

> normalized = (raw_score - minimum_score) / (maximum_score - minimum_score)
>     return max(0.0, min(1.0, float(normalized)))
> --- `skilllift/skilllift/normalization.py`

#### EPI-RTE-receipt-check
Label: Receipt structural validation and removal declarations

Distinct check part within the broader [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision); it does not select best rank alignment. Endpoints: proposed receipt and optional predecessor → `validate_receipt` → ValidationReport. Owner: rubricator code. Check target/domain: receipt structure, score bounds, version delta and declared removals. Context/state: old and candidate criteria; no task execution. SRC-1, `skilllift/skilllift/rubricator.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: report with boolean ok, error codes and messages.
- Later read-back: validation report and candidate are saved as revision-attempt artifacts by surrounding revision code; rationale read-back into later reasoning remains uninspected.
- Delegated visibility: retry prompt can receive previous validation report; later verifier receives selected receipt, not proof its evidence references are true.
- Selection predicate: 5–15 criteria; unique IDs, nonempty criteria, nonzero signed points within five, correct score bounds/range, version/removal bookkeeping and literal hidden-answer marker check.
- Invalidation or expiry: invalid candidate cannot pass the revision admission branch; retries may keep old receipt. Declared removed IDs must match actual removals.
- Activation or effect: report.ok permits candidate return; rejection vetoes structural admission, not every semantically bad criterion.
- Evidence limits: removed reasons and evidence_refs must be nonempty strings/list entries; implementation does not resolve and validate their semantic support in this check. Nonbinary wording may only generate a warning. Hidden-answer marker search is not comprehensive leakage detection.

Proposer: rubricator model; decider/veto: validator and retry policy; human input is caller configuration, not per-revision approval. Answer oracle: none in validation. Mode/trigger: bounded receipt proposal repair after invalid output or rank disagreement. Proposed change: whole receipt, with removals explicitly declared; old receipt remains recovery fallback. Guidance: public evidence, score contrast and previous validation feedback; persisted policy/attempts as in the supplied revision route. Theory account remains owned by that route; this structural subcheck does not establish criticism quality.

> if not _looks_binary(rubric.criterion):
>             messages.append(f"{rubric.rubric_id}: criterion may not be binary")
> --- `skilllift/skilllift/rubricator.py`

> if (
>             not isinstance(evidence_refs, list)
>             or not evidence_refs
>             or any(not isinstance(ref, str) or not ref.strip() for ref in evidence_refs)
>         ):
>             errors.append("removed_rubric_evidence_missing")
> --- `skilllift/skilllift/rubricator.py`

#### EPI-RTE-category-fusion
Label: Category winner fusion and final admission

Part of: [RT-RTE-category-training](runtime.md#rt-rte-category-training)

This is the separate final-fusion subroute, not task-portfolio refinement or tau2 master fusion. Endpoints: multiple category batch winners → model JSON → parse package/name check → final_skills replacement → held-out test. Owner: SkillLiftSkillsBenchRunner. Context/state/action: category training task overview and winners; writes a new multi-file package, then later submits it to benchmark execution. SRC-1, `skilllift_eval/runners/skilllift_skillsbench.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: EvoSkill with strategy fusion; train writes it as final category skill.
- Later read-back: test computes directory hash, reads final_skills via its command adapter and may reuse matching test scores.
- Delegated visibility: fusion model receives winners, runtime name and training-task overview; prompt requests complementary workflows and exclusion of test tasks. Test execution receives materialized final directory.
- Selection predicate: more than one category batch invokes fusion; parse_skill_package and validate_agent_skill_name precede return. No new oracle result is required between this return and final write in inspected train.
- Invalidation or expiry: parse/name failures prevent returned package; final write deletes any existing category directory before materializing replacement. Downstream score reuse checks configuration/skill hash.
- Activation or effect: admits newly generated instructions to held-out execution, with model-interpreted instruction force; no semantic benefit established.
- Evidence limits: parse/name internals uninspected here; code establishes their invocation, not every invariant they enforce. Final write has no demonstrated semantic rollback or pre-write evidence-consuming acceptance. Later testing is evaluation, not prior certification.

Proposer: fusion model; decider/veto: package/name checks and train branch, no per-content human admission. Answer oracle: none before fused final content is written; held-out benchmark is a later evaluator. Mode: post-training composition, not a bounded oracle-improvement selection loop. Proposed change: a complete package; guidance asks to preserve complementary workflows. Rejection can raise on invalid package/name; previous directory is removed during successful final materialization. Concrete factual content and whether fusion adds rather than reshapes claims remain indeterminate without a linked output. No content-specific theory or criticism is established from the imperative fusion request alone.

> package = parse_skill_package(payload, skill_format="agent_skill")
>         validate_agent_skill_name(package, runtime_name)
>         return EvoSkill(SkillKey(0, 1), runtime_name, package.files, package.entrypoint, {**package.metadata, "strategy": "fusion"})
> --- `skilllift_eval/runners/skilllift_skillsbench.py`

> self._write_final_skill(category, winner)
>         summary = {
>             "status": "completed",
>             "categories": categories,
>             "batches": batch_results,
> --- `skilllift_eval/runners/skilllift_skillsbench.py`

#### EPI-RTE-tau2-evaluator
Label: tau2 evaluator configuration and reward import

Part of: [RT-RTE-domain-fusion](runtime.md#rt-rte-domain-fusion)

This subroute isolates external evaluator dependence from skill fusion. Endpoints: run configuration → external NL-assertion defaults; simulation → _reward → OracleScore and threshold pass. Owner: tau2 wrapper for configuration/import, external tau2 for evaluation. Check target: task outcome under tau2's domain evaluators, not skill-text truth. Context/state: agent model/filtered args assigned to NL-assertion defaults; structured reward imported and attributed. SRC-1, `skilllift_eval/runners/skilllift_tau2.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: imported score and thresholded pass with tau2_structured_reward metadata; configuration helper mutates external evaluator defaults.
- Later read-back: surrounding training/held-out route persists results/checkpoints; evaluator-internal read-back uninspected because dependency unavailable.
- Delegated visibility: external assertion evaluator defaults receive model and filtered agent LLM args; training consumes scalar outcomes and public feedback.
- Selection predicate: score >= threshold sets pass; surrounding domain route selects/revises on aggregate reward and alignment.
- Invalidation or expiry: uninspected — unavailable external evaluator controls assertion validity; local import supplies no independent truth recheck.
- Activation or effect: imported reward can alter training selection and receipt revision; configured model could participate in external NL assertion judgment.
- Evidence limits: setting defaults does not establish any task exercised NL assertions. Actual evaluator implementation, assertion set and correctness unavailable; source warrant unknown.

No additional model component is inferred from the hook alone: the requested agent model name is copied, not a newly authenticated model instance. Role/version/provider uncertainty remains as [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client). This is a positive implementation witness against treating all benchmark-oracle machinery as inspected deterministic proof, not a claim that all tau2 rewards are model judgments.

> tau2_config.DEFAULT_LLM_NL_ASSERTIONS = model
>     tau2_config.DEFAULT_LLM_NL_ASSERTIONS_ARGS = dict(llm_args)
>     nl_assertions.DEFAULT_LLM_NL_ASSERTIONS = model
>     nl_assertions.DEFAULT_LLM_NL_ASSERTIONS_ARGS = dict(llm_args)
> --- `skilllift_eval/runners/skilllift_tau2.py`

> score = _reward(simulation)
>     passed = 1 if score >= threshold else 0
> --- `skilllift_eval/runners/skilllift_tau2.py`

#### EPI-RTE-artifact-audit
Label: Post-run artifact audit reporting

Distinct from [RT-RTE-cell-recovery](runtime.md#rt-rte-cell-recovery): audit checks existing output artifacts, not logical trial recovery or skill promotion. Endpoints: CLI audit run_root → summary/cell checks and secret scan → reports/exit status. Owner: CLI code. Check target/domain: selected artifact existence, record count, source labels and source-specific audit conditions; not task-answer correctness. SRC-1, `skilllift_eval/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: audit_report.json, audit_report.md, printed finding count and zero/nonzero exit status.
- Later read-back: uninspected — no downstream automatic withdrawal consumer traced; reports remain caller-readable files.
- Delegated visibility: caller receives findings/warnings and process status; audit reads summaries and record paths, not model-hidden reasoning.
- Selection predicate: findings empty gives passed/0, otherwise failed/1; smoke summaries generate limited-scope warning. external_cited cells only require mean_score in the inspected branch.
- Invalidation or expiry: inapplicable — no skill deletion, score rollback or expiry is implemented by inspected handle_audit/_audit_cell.
- Activation or effect: diagnostic/reporting force and enforcing CLI return status; any pipeline admission use remains uninspected.
- Evidence limits: no claim of complete secret scanning or complete audit branch coverage; reports are conditional deductions from local artifact fields, not authentication of the producing execution.

> write_json(run_root / "audit_report.json", report)
>     (run_root / "audit_report.md").write_text(_audit_markdown(report), encoding="utf-8")
>     print(f"audit {report['status']}: {len(findings)} finding(s), {len(warnings)} warning(s)")
>     return 0 if not findings else 1
> --- `skilllift_eval/cli.py`

### Claims

#### EPI-CLM-local-safety
Label: Non-degradation and oracle-selected champion claim

Distinct public claim extending the inner-mode claim [RT-CLM-mode-a](runtime.md#rt-clm-mode-a); compared with [RT-CLM-refinement-replay](runtime.md#rt-clm-refinement-replay), it concerns selection safety, not persistence identity. SRC-1, `README.md`, doctrine/design. The plausible narrow reading is nondecreasing *rubric score*. A stronger task-quality reading is unsupported: surrogate checks are not task executions, ties can promote on verifier advantage and final category fusion is not the measured winner itself.

> Each branch is refined only
>   while its rubric score is non-decreasing, so local refinement can never degrade a candidate.
> --- `README.md`

> A misaligned rubric degrades guidance quality, never the final output — the champion is always
>   selected by oracle score.
> --- `README.md`

#### EPI-CLM-ranking-surrogate
Label: Oracle preference surrogate and alignment claim

Distinct from [RT-CLM-mode-a](runtime.md#rt-clm-mode-a): concerns warrant/generalization and alignment, not just absence of inner oracle calls. SRC-1, `README.md`, doctrine/design. Model-call feedback and measured rank comparison are supported by implementation; universal single-call portfolio scoring, guaranteed threshold and out-of-sample preference reproduction are not established. The inspected mode scores each portfolio through helper calls and can stop below threshold; see [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision).

> a set of binary criteria with signed weights — that reproduces the oracle's *preference
> order* over skills. Once aligned, the rubric scores any candidate with a **single LLM call**, giving
> the skill generator dense, criterion-level feedback at zero oracle cost.
> --- `README.md`

> a
>   *rubricator* revises the rubric until its ranking agrees with the oracle's (Kendall's τ ≥ 0.9).
> --- `README.md`

Counter-witness: measured-best selection survives budget/error exits, not necessarily convergence.

> if mode_iter == self.config.mode_b_iters - 1:
>                 break
> --- `skilllift/skilllift/coordinator/modes.py`

> if best_alignment is not None:
>             current_receipt = best_receipt
> --- `skilllift/skilllift/coordinator/modes.py`

#### EPI-CLM-ablation-mechanism
Label: Reported ablation confirms mechanism

No supplied claim record has this referent; closest [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision) describes the mechanism without supplying comparative run evidence. SRC-1, `README.md`, reported operation. Claimed comparison: remove oracle-aligned revision or replace rank alignment by regression at identical oracle budget. Accessible README narrative supports attribution only, not independently verified component causality or design adequacy.

> **Ablations confirm the mechanism.** Removing oracle-aligned rubric revision collapses pass rates
> to within +1.4 pp of the static-skill baseline; replacing ranking-based alignment with direct score
> regression costs 3–5 pp at identical oracle budget — absolute oracle scores are noisy and
> non-comparable across tasks, ordinal information is not.
> --- `README.md`
