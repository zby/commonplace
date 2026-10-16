---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "JEPA-Anything's task-design proposals, declared-validity gates, numerical checks and limits on scientific reliance."
run-id: AAS-2026-10-15-jepa-anything-434b01ab7774-01
reviewed-boundary: c6e6c88f3ef75a4ce7acd660d6fa5779d995512c
---

# JEPA-Anything epistemic report

## Source-and-claim boundary

The question is what reliance JEPA-Anything licenses when it converts a world-model request into a design and skeleton, and whether its checks support claims about a learned world model. Scope, exclusions and frozen evidence identity are see [boundary](boundary.md#boundary-and-evidence); the sole registered source is see [Source register](boundary.md#source-register). All direct inspection below uses SRC-1 at the frozen commit, supplying implementation or doctrine/design evidence, never observed operation.

The model-assisted compiler is a declared workflow. Its deterministic supports implement narrower checks. The relevant claims are [EPI-CLM-world-model-compiler](#epi-clm-world-model-compiler) and [RT-CLM-validation-scope](runtime.md#rt-clm-validation-scope). These are not claims that a passing configuration proves a successful world model. The source explicitly distinguishes the two.

| Entry point or operation | Source path in SRC-1 | Coverage and supporting records | Limit and prevented conclusion |
|---|---|---|---|
| Implicit/explicit host compilation and repair | `jepa-anything-skill/SKILL.md`; `jepa-anything-skill/agents/openai.yaml` | Direct complete reads; see [RT-RTE-task-compilation](runtime.md#rt-rte-task-compilation), [EPI-CLM-world-model-compiler](#epi-clm-world-model-compiler) | Reference-specific interpretation supplied by runtime; no host trace, so no exercised extraction, repair or completion finding. |
| Standalone validator CLI/API | `jepa-anything-skill/scripts/validate_design.py` | Direct dispatch/report/load and claim/output branch reads; see [EPI-RTE-design-diagnostics](#epi-rte-design-diagnostics) | Remaining schema, leakage, state and audit branches covered provisionally by runtime, not exhaustively audited here; no complete validator-correctness finding. |
| Generator CLI and direct renderer | `jepa-anything-skill/scripts/generate_scaffold.py` | Direct complete executable body; see [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission), [EPI-RTE-template-specialization](#epi-rte-template-specialization) | Direct renderer bypasses the CLI validity gate. No package-generation trace supplied. |
| Planned-claim and evidence-envelope helpers | `jepa-anything-skill/assets/scaffold/src/jepa_task/evaluation.py.tmpl` | Direct complete read; see [EPI-RTE-evidence-envelope](#epi-rte-evidence-envelope) | Metadata comparison, not empirical verification or statistical acceptance. |
| Activity, capacity, geometry helpers | `jepa-anything-skill/assets/scaffold/src/jepa_task/activity.py.tmpl`; `jepa-anything-skill/assets/scaffold/src/jepa_task/capacity.py.tmpl`; `jepa-anything-skill/assets/scaffold/src/jepa_task/model.py.tmpl` | Direct complete reads; see [EPI-RTE-measurement-checks](#epi-rte-measurement-checks) | Callers supply purported measurements; provenance and actual backend computations are not enforced. |
| Generated tests and consumers | `jepa-anything-skill/assets/scaffold/tests/test_contract.py.tmpl`; `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl` | Direct test prefix and complete dispatcher; see [EPI-RTE-evidence-envelope](#epi-rte-evidence-envelope), [RT-RTE-state-consumption](runtime.md#rt-rte-state-consumption) | Remaining tests and adapter checks supplied by runtime. Callback content and its truth conditions are not determinable from this dispatcher. |
| Core projection, QR hook, EMA | `jepa-anything-core/src/jepa_anything_core/opf.py`; `jepa-anything-core/src/jepa_anything_core/baselines.py` | Supplied runtime findings: [RT-RTE-core-projection](runtime.md#rt-rte-core-projection), [RT-CMP-orthogonal-factor-projection](runtime.md#rt-cmp-orthogonal-factor-projection) | No training/optimizer trace or parameter values; mutability does not establish improved capacity. |
| Core numerical reports | `jepa-anything-core/src/jepa_anything_core/audit.py` | Direct basis, reconstruction, round-trip and aggregate audit reads; see [EPI-RTE-numerical-audits](#epi-rte-numerical-audits) | Factor-audit internals uninspected here; aggregate wiring is not exhaustive correctness evidence. |
| Core losses and historical variance | `jepa-anything-core/src/jepa_anything_core/losses.py` | Direct tracker, streaming wrapper, prediction and composite objective reads; see [EPI-RTE-variance-history](#epi-rte-variance-history) | Primitive activity/variance loss internals not exhaustively inspected; no actual optimizer consumer supplied. |
| Synthetic audit | `recipes/synthetic-linear-dynamics/run_recipe.py` | Direct activity generator and report/CLI; supplied structural account: [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks) | Recipe audit branches remain sampled; oracle-coordinate activity cannot establish learned activity. |
| Checkpoint verifier | `checkpoints/verify_manifest.py` | Direct verification and CLI; see [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks) | File-check helper internals supplied by runtime; integrity is not performance or scientific acceptance. |
| Repository check dispatch | `Makefile`; `.github/workflows/ci.yml` | Direct Make read, supplied boundary CI wiring; see [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks) | Nonzero status constrains check completion, not independently inspected merge/publication policy. |

No target code or tests were executed. Missing host traces prevent conclusions about actual model compliance; missing measured results, weights and datasets prevent conclusions about learned task success; missing interventions prevent causal attribution. Uninspected branches above prevent a system-complete negative about all possible acceptance mechanisms. The supported negative is narrower: the inspected claim-envelope helper does not decide statistical support, and the inspected dispatcher does not require those helpers before calling callbacks. The opaque host model's internal knowledge acquisition and any task-specific learned prediction semantics remain not determinable; see [RT-CMP-host-model](runtime.md#rt-cmp-host-model).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-design-protocol](runtime.md#rt-obj-design-protocol) | Mathematical/design guidance and constraints | see record | SRC-1: `jepa-anything-skill/SKILL.md` | Delivery to host does not establish consumption or the truth of every recommendation. |
| [RT-OBJ-design-config](runtime.md#rt-obj-design-config) | Task identity, causal availability declarations, proposed architecture; diagnostic predicates are a distinct operative part | see record | SRC-1: `jepa-anything-skill/scripts/validate_design.py` | World-facing declarations remain unverified; defaults are hypotheses. |
| [EPI-OBJ-claims](#epi-obj-claims) | Planned comparison contracts, not supported comparative outcomes | see record | SRC-1: `jepa-anything-skill/scripts/validate_design.py` | Metric/direction/scope specify a future check, not a measured result. |
| [EPI-OBJ-evidence-envelope](#epi-obj-evidence-envelope) | Caller assertions of measurement identity and passed audits | see record | SRC-1: `jepa-anything-skill/assets/scaffold/src/jepa_task/evaluation.py.tmpl` | No measured score, statistical criterion or audit attestation is required by this helper. |
| [EPI-OBJ-audit-measurements](#epi-obj-audit-measurements) | Caller-supplied geometry, coordinate activity and capacity assertions, separately checked | see record | SRC-1: `jepa-anything-skill/assets/scaffold/src/jepa_task/model.py.tmpl` | Authentic measurement origin remains unknown. |
| [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest) | Specialized executable obligations, saved configuration and diagnostics | see record | SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py` | Code emission/retention is not empirical endorsement. |
| [EPI-OBJ-audit-reports](#epi-obj-audit-reports) | Computed numerical properties of supplied tensors | see record | SRC-1: `jepa-anything-core/src/jepa_anything_core/audit.py` | Numerical scope only; no world-model semantics follow. |
| [EPI-OBJ-variance-tracker](#epi-obj-variance-tracker) | Sample count, coordinate means and squared-deviation sums | see record | SRC-1: `jepa-anything-core/src/jepa_anything_core/losses.py` | Sufficient statistics describe supplied samples, not generalization. |
| [RT-CMP-orthogonal-factor-projection](runtime.md#rt-cmp-orthogonal-factor-projection) | None individuated as a world-facing proposition from available basis state | see record | SRC-1: `jepa-anything-core/src/jepa_anything_core/opf.py` | Basis mutability and geometry are inspectable; actual learned content is not. |

## Authority-route ledger

Each row separates functions even where it cites the same canonical route. Identity, endpoints, ownership and persistence fields owned by that route are see the cited record. Architectural status below is this member's assessment. No row claims observed activation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-task-compilation](runtime.md#rt-rte-task-compilation) | content transformation | doctrine only | [RT-OBJ-design-config](runtime.md#rt-obj-design-config) | truth-apt transformation: acquisition/import | User/project causal facts enter proposed contract | Host interpretation; open task domain | Requested before validation | Proposed normalized facts | Instruction only | Source warrant unknown; original project facts not supplied | Shapes proposal and questions | see [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) | SRC-1: `jepa-anything-skill/SKILL.md` | [EPI-CLM-world-model-compiler](#epi-clm-world-model-compiler) | none | No actual import trace or semantic fidelity check. |
| [RT-RTE-task-compilation](runtime.md#rt-rte-task-compilation) | content transformation | doctrine only | [RT-OBJ-design-config](runtime.md#rt-obj-design-config) | truth-apt transformation: indeterminate | Task facts plus defaults become design hypotheses | Host model guided by references | Requested during proposal/repair | Design choices and compiler assumptions | Instruction only | Candidate status, not accepted efficacy | Host selects design and repair | see [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) | SRC-1: `jepa-anything-skill/SKILL.md` | [EPI-CLM-world-model-compiler](#epi-clm-world-model-compiler) | none | No concrete task/design pair to distinguish entailed extraction, reshaping and non-entailed conjecture; defaults alone are not outcome propositions. |
| [EPI-RTE-design-diagnostics](#epi-rte-design-diagnostics) | check/evidence production | implemented | [RT-OBJ-design-config](runtime.md#rt-obj-design-config), [EPI-OBJ-claims](#epi-obj-claims) | truth-apt transformation: entailed derivation | Declared mapping satisfies coded predicates | Deterministic rule checks; schema and reciprocal evidence-plan domain | Explicit API/CLI call before rendering | Checks, counts, valid bit | Diagnostic; standalone exit status | Bounded facts about declarations under this implementation | Feedback permits host repair; does not repair itself | CLI caller/host; JSON diagnostics, advisory; current repair round | SRC-1: `jepa-anything-skill/scripts/validate_design.py` | [RT-CLM-validation-scope](runtime.md#rt-clm-validation-scope) | none | Rule completeness and factual truth not established. |
| [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission) | disposition/acceptance | implemented | [RT-OBJ-design-config](runtime.md#rt-obj-design-config) | no content change | Admission for fixed-template generation | CLI consumes report.valid; destination/format checks | Before CLI emission | Invalid rejected; valid proceeds | Enforcing CLI gate | Acceptance of declared completeness for skeleton generation only | Allows filesystem package creation | see [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission) | SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py` | [RT-CLM-validation-scope](runtime.md#rt-clm-validation-scope) | CLI-only | Direct renderer does not require valid report. |
| [EPI-RTE-template-specialization](#epi-rte-template-specialization) | content transformation | implemented | [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest) | truth-apt transformation: non-ampliative reshaping | Config values become literals and saved config/report | Fixed mapping/repr/substitution | Render call | Specialized interface declarations | Fixed code generation | Preserves selected declarations, not their empirical warrant | Sets later branch constants and checks | see [RT-BAP-generated-contract](runtime.md#rt-bap-generated-contract) | SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py` | [EPI-CLM-world-model-compiler](#epi-clm-world-model-compiler) | none | Does not certify semantic adequacy of original design. |
| [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission) | retention | implemented | [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest) | no content change | Package/report/config promoted from temporary tree | Missing/empty destination check | After rendering | Persisted package or exception cleanup | Filesystem replacement; no version rollback | Retention carries declarations and diagnostic result, not accepted scientific claims | Later import/use made available | see [RT-BAP-generated-contract](runtime.md#rt-bap-generated-contract) | SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py` | none | none | Not lifecycle integration of an accepted model-quality claim. |
| [EPI-RTE-evidence-envelope](#epi-rte-evidence-envelope) | check/evidence production | implemented | [EPI-OBJ-claims](#epi-obj-claims) | no content change | Planned claims reciprocally covered by experiments | Equality/membership; exact plan metadata | Explicit helper call | None or exception | Local enforcing exception | Plan coherence only | Blocks caller continuation if uncaught | Explicit caller/test; synchronous call; enforcing locally; current call | SRC-1: `jepa-anything-skill/assets/scaffold/src/jepa_task/evaluation.py.tmpl` | [RT-CLM-validation-scope](runtime.md#rt-clm-validation-scope) | none | No changed claim status. |
| [EPI-RTE-evidence-envelope](#epi-rte-evidence-envelope) | check/evidence production | implemented | [EPI-OBJ-evidence-envelope](#epi-obj-evidence-envelope) | no content change | Result identity matches a planned comparison | Equality/set comparisons; metadata domain | Explicit caller/test invocation | None or exception | Local exception only | Metadata alignment, not statistical support or authentic audits | Allows caller to continue when no mismatch | Explicit caller/test; synchronous call; enforcing locally; current call | SRC-1: `jepa-anything-skill/assets/scaffold/src/jepa_task/evaluation.py.tmpl` | [RT-CLM-validation-scope](runtime.md#rt-clm-validation-scope) | none | No mandatory coupling to state consumer or measurement helpers. |
| [EPI-RTE-measurement-checks](#epi-rte-measurement-checks) | check/evidence production | implemented | [EPI-OBJ-audit-measurements](#epi-obj-audit-measurements) | no content change | Shapes, full rank, condition ceiling, synthesis NMSE | Numeric/type/range predicates; supplied geometry metadata | Explicit audit call | None or exception | Local exception | Supplied envelope within declared numerical bounds | Caller continuation locally blocked on mismatch | Explicit backend/test caller; Python call; enforcing locally; current call | SRC-1: `jepa-anything-skill/assets/scaffold/src/jepa_task/model.py.tmpl` | none | none | Does not compute rank or tie evidence to a tensor. |
| [EPI-RTE-measurement-checks](#epi-rte-measurement-checks) | check/evidence production | implemented | [EPI-OBJ-audit-measurements](#epi-obj-audit-measurements) | no content change | Every supplied factor/encoder coordinate standard deviation meets floor | Finite nonnegative arrays and thresholds; coordinate activity domain | Explicit audit call | None or exception | Local exception | Threshold compliance of supplied values, not semantics | Caller blocked on low activity | Explicit caller; Python call; enforcing locally; current call | SRC-1: `jepa-anything-skill/assets/scaffold/src/jepa_task/activity.py.tmpl` | none | none | Measurement origin and sample population unverified. |
| [EPI-RTE-measurement-checks](#epi-rte-measurement-checks) | check/evidence production | implemented | [EPI-OBJ-audit-measurements](#epi-obj-audit-measurements) | no content change | Full-model parameters, predictor FLOPs, steps, scopes and baseline tolerances | Integer/scope/relative-gap predicates; declared capacity comparison | Explicit audit call | None or exception | Local exception | Supplied capacity alignment, not independent counters or performance | Caller blocked on capacity mismatch | Explicit caller; Python call; enforcing locally; current call | SRC-1: `jepa-anything-skill/assets/scaffold/src/jepa_task/capacity.py.tmpl` | none | none | Copying estimates can satisfy predicates without genuine measurement. |
| [EPI-RTE-numerical-audits](#epi-rte-numerical-audits) | check/evidence production | implemented | [EPI-OBJ-audit-reports](#epi-obj-audit-reports) | truth-apt transformation: entailed derivation | Supplied basis rank, condition number, orthogonality and completeness | Numerical linear algebra, finite values, dimensions and tolerances; supplied basis domain | Explicit basis audit call | Computed geometry report with pass/violations | Reporting, not installation gate | Numerical properties of basis, bounded by precision/tolerances | No automatic admission or parameter update | Calling program; report object; advisory; current result unless caller retains it | SRC-1: `jepa-anything-core/src/jepa_anything_core/audit.py` | none | none | Full-rank or orthogonal geometry cannot establish prediction quality or semantics. |
| [EPI-RTE-numerical-audits](#epi-rte-numerical-audits) | check/evidence production | implemented | [EPI-OBJ-audit-reports](#epi-obj-audit-reports) | truth-apt transformation: entailed derivation | Pseudoinverse round-trip reconstruction | Compare reconstructed supplied state with original; max absolute error threshold | Explicit round-trip audit call | Error summaries and threshold verdict | Reporting, not installation gate | Reconstruction of supplied samples within numerical tolerance | No automatic admission or parameter update | Calling program; report object; advisory; current result unless caller retains it | SRC-1: `jepa-anything-core/src/jepa_anything_core/audit.py` | none | none | Reconstruction is not held-out prediction. |
| [EPI-RTE-numerical-audits](#epi-rte-numerical-audits) | check/evidence production | implemented | [EPI-OBJ-audit-reports](#epi-obj-audit-reports) | truth-apt transformation: entailed derivation | Direct transpose-synthesis reconstruction | Compare reconstructed supplied state with original; normalized MSE threshold | Explicit transpose-synthesis audit call | Error summaries and threshold verdict | Reporting, not installation gate | Transpose reconstruction of supplied samples within numerical tolerance | No automatic admission or parameter update | Calling program; report object; advisory; current result unless caller retains it | SRC-1: `jepa-anything-core/src/jepa_anything_core/audit.py` | none | none | Does not license replacing pseudoinverse synthesis outside checked geometry. |
| [EPI-RTE-variance-history](#epi-rte-variance-history) | retention | implemented | [EPI-OBJ-variance-tracker](#epi-obj-variance-tracker) | truth-apt transformation: entailed derivation | Samples update sufficient statistics | Welford merge, shape/finite/overflow checks; coordinate samples | Explicit update or enabled streaming wrapper | Mutated count/mean/m2, or rejection | In-process state update | Numerical summary of admitted samples within floating precision | Changes subsequent loss inputs | Later streaming call; buffers; computational input; until reset/load/replacement | SRC-1: `jepa-anything-core/src/jepa_anything_core/losses.py` | none | none | No optimizer or saved-state trace. |
| [EPI-RTE-variance-history](#epi-rte-variance-history) | operational admission/selection/consumption | implemented | [EPI-OBJ-variance-tracker](#epi-obj-variance-tracker) | non-truth-apt policy/content update: history-dependent differentiable activity penalty | Current batch evaluated with historical sufficient statistics | Combined population variance, std floor, reduction | Streaming loss call; wrapper training flag controls default update | Scalar/tensor loss | Numeric input, not an optimizer decision | No world-facing claim license | Can shape gradients if an external optimizer uses the loss | Calling optimizer code, if supplied; loss tensor; advisory input; training step | SRC-1: `jepa-anything-core/src/jepa_anything_core/losses.py` | none | none | Potential adaptation, not observed learning or compelled optimization. |
| [RT-RTE-core-projection](runtime.md#rt-rte-core-projection) | behavior/policy adaptation | implemented | [RT-CMP-orthogonal-factor-projection](runtime.md#rt-cmp-orthogonal-factor-projection) | non-truth-apt policy/content update: externally driven basis/EMA parameter changes | Learnable geometry and target weights | Mode, step and explicit caller hooks; numerical parameter domain | External optimization/retraction/EMA calls | Changed parameters | Local numerical mutation | None for predictive truth | Later forward calls use changed values | see [RT-RTE-core-projection](runtime.md#rt-rte-core-projection) | SRC-1: `jepa-anything-core/src/jepa_anything_core/opf.py` | none | none | Exact tensor values, learned content and improved capacity unestablished. |
| [RT-RTE-state-consumption](runtime.md#rt-rte-state-consumption) | operational admission/selection/consumption | implemented | [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest) | no content change | State delivered to readout, analysis or repeated transition | Configured mode/callability/exogenous presence; not outcome truth | Explicit consume_state call | Callback result or selected horizon states | Direct callback execution | No truth license | Permits callbacks before any separate evidence audit | see [RT-RTE-state-consumption](runtime.md#rt-rte-state-consumption) | SRC-1: `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl` | none | none | Callback-generated content/update relation not determinable; earlier callbacks not rolled back on later failure. |
| [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks) | check/evidence production | implemented | see record | truth-apt transformation: entailed derivation | Synthetic fixture structure and oracle-coordinate activity | Deterministic fixture calculation; seeded synthetic state domain | Recipe driver CLI/API; Make/CI wiring | Pass/fail report/status | CLI nonzero blocks successful check completion | Fixture conclusions only | Can fail make check; no automatic model successor installation | Recipe caller/Make; JSON and exit status; diagnostic and enforcing check completion; current run | SRC-1: `recipes/synthetic-linear-dynamics/run_recipe.py` | none | none | No learned activity or empirical world-model acceptance criterion. |
| [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks) | check/evidence production | implemented | see record | truth-apt transformation: entailed derivation | Publication declarations and referenced-file integrity | Manifest consistency and hash predicates; metadata/file domain | Verifier CLI/API; Make/CI wiring | Pass/fail report/status | CLI nonzero blocks successful check completion | Integrity/publication-boundary conclusions only | Can fail make check; no scientific result acceptance | Verifier caller/Make; JSON and exit status; diagnostic and enforcing check completion; current run | SRC-1: `checkpoints/verify_manifest.py` | none | none | No model result evaluated; merge policy uninspected. |

There is no lifecycle-integration row for a scientifically accepted comparative claim: none is established by these inspected routes. This is not a system-complete absence assertion about uninspected callbacks, host processing or remaining source branches. Structural validity is an implemented, evidence-consuming admission decision for generation, not for scientific use.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-world-model-compiler](#epi-clm-world-model-compiler) | see record | SRC-1: `jepa-anything-skill/SKILL.md`; doctrine/design | see record | [EPI-RTE-design-diagnostics](#epi-rte-design-diagnostics), [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission), [EPI-RTE-template-specialization](#epi-rte-template-specialization) | None supplied | No host conversion comparison or real training evidence | A declared model-assisted compiler with executable deterministic support, not observed reliable automatic task conversion | Direct renderer bypass qualifies the public refusal statement; no contradiction with the documented CLI recipe. |
| [RT-CLM-validation-scope](runtime.md#rt-clm-validation-scope) | see record | SRC-1: `jepa-anything-skill/scripts/validate_design.py`; implementation and doctrine/design | see record | [EPI-RTE-design-diagnostics](#epi-rte-design-diagnostics), [EPI-RTE-evidence-envelope](#epi-rte-evidence-envelope), [EPI-RTE-measurement-checks](#epi-rte-measurement-checks) | None supplied | No independent test of validator completeness; no model-quality intervention | Implemented declaration checks and explicit non-scientific boundary agree | A successful generated test can use copied metadata; passing must not be promoted to measured support. |

## Bounded conclusion

**The compiler produces a candidate contract and executable obligations; its gate licenses skeleton generation, not a scientific conclusion.** Host acquisition and proposal behavior are see [RT-RTE-task-compilation](runtime.md#rt-rte-task-compilation). Imported causal facts have unknown warrant in this run. The source asks for hypotheses and assumptions; without a concrete task/design trace it does not establish which proposed propositions were entailed, reshaped or ampliative. No produced accepted ampliative model-quality claim is established.

The design-check result derives from declared input and fixed predicates, not observations of the proposed world. Acceptance has an explicit criterion and use: report.valid allows the generator CLI to emit a skeleton; destination and format checks constrain emission. See [EPI-RTE-design-diagnostics](#epi-rte-design-diagnostics) and [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission). Direct render calls are a supported countercase to a universal validity-gate claim. The renderer specializes declarations and retains config, report and code; later imports enforce only the branches actually called. See [EPI-RTE-template-specialization](#epi-rte-template-specialization) and [RT-BAP-generated-contract](runtime.md#rt-bap-generated-contract).

Planned comparison scope is inspectable, and metadata mismatches can stop a caller. Activity floors, capacity tolerances and geometry bounds are likewise material local criteria. Their intended use is contract/audit checking; none authenticates the caller's measurement process or performs statistical acceptance. See [EPI-RTE-evidence-envelope](#epi-rte-evidence-envelope) and [EPI-RTE-measurement-checks](#epi-rte-measurement-checks). The generated state consumer does not require them. Operational reliance on callback state can therefore precede any such check; see [RT-RTE-state-consumption](runtime.md#rt-rte-state-consumption).

Independent core reports compute actual numerical properties of their tensor inputs. This is stronger than checking a supplied rank assertion but still bounded to numerical geometry and sampled reconstruction, not domain truth. See [EPI-RTE-numerical-audits](#epi-rte-numerical-audits). The synthetic driver uses oracle coordinates; manifest verification licenses only provenance/integrity conclusions. See [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks).

The variance tracker is a separate historical-state route: sample summaries affect later differentiable penalties, with explicit reset and update controls. See [EPI-RTE-variance-history](#epi-rte-variance-history). Basis updates, QR retraction and EMA are separate parametric mutation affordances; see [RT-RTE-core-projection](runtime.md#rt-rte-core-projection). These support possible behavior adaptation without a truth-apt acceptance route. They establish neither observed learning nor improved capacity. Method texts are addressable guidance and requested repair is not evidenced criticism of the compiler's own method. Reflection, autonomous execution and compiler self-improvement do not follow from package generation or parameter mutability; the independently bounded runtime theory assessment is see [RT-RTE-task-compilation](runtime.md#rt-rte-task-compilation). Missing traces and causal comparisons remain local limits, not an overall epistemic score.

## Shared records

### Operative objects

#### EPI-OBJ-claims
Label: Structured planned claims
Part of: [RT-OBJ-design-config](runtime.md#rt-obj-design-config)

Source-native identity: `claims` and linked `experiments` entries in schema 2.0. Symbolic mappings in a config file/in-process mapping. This part has different checks and authority from free-text task assertions: comparison metadata must be reciprocal and status must be planned. It is not a measured outcome. Generated copies specialize the same declarations in the package described by [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest). SRC-1 implementation: `jepa-anything-skill/scripts/validate_design.py`.

> if claim.get("status") != "planned":
>     self.fail("FIELD_INVALID", f"{path}.status", "Design-time claims must have status 'planned'.")
> --- `jepa-anything-skill/scripts/validate_design.py`

#### EPI-OBJ-evidence-envelope
Label: Claim evidence envelope

Source-native identity: `evidence` argument to `audit_claim_evidence_envelope`. Symbolic caller mapping in memory. This is distinct from [EPI-OBJ-claims](#epi-obj-claims): it asserts result metadata and passed audit IDs rather than a future plan. Closest supplied object [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest) contains the checking code, not this downstream caller data. No supplied object counterpart after comparison. SRC-1 implementation: `jepa-anything-skill/assets/scaffold/src/jepa_task/evaluation.py.tmpl`.

> if set(evidence.get("passed_audit_ids", ())) != set(claim["audit_ids"]):
>     raise ValueError("Evidence audit IDs do not match the planned claim.")
> --- `jepa-anything-skill/assets/scaffold/src/jepa_task/evaluation.py.tmpl`

#### EPI-OBJ-audit-measurements
Label: Backend audit measurements

Source-native identities: separate `measurements` arguments for geometry, activity and capacity helpers. Symbolic numeric arrays/mappings supplied by callers, held in memory, with no persistence implemented by these helpers. The three operative parts have different targets: geometry rank/condition/NMSE; factor/encoder standard deviations; reference/baseline parameter/FLOPs/step counts. [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest) contains the helper programs, not their caller-provided inputs; no supplied object counterpart after comparison. SRC-1 implementation: `jepa-anything-skill/assets/scaffold/src/jepa_task/model.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/activity.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/capacity.py.tmpl`.

> ``measurements`` must be produced by the implementation's parameter/FLOPs
> counters; copying design estimates is not empirical capacity evidence.
> --- `jepa-anything-skill/assets/scaffold/src/jepa_task/capacity.py.tmpl`

#### EPI-OBJ-audit-reports
Label: Numerical geometry reports

Source-native identities: `BasisGeometryReport`, `RoundTripReport`, `TransposeSynthesisReport`, and containing `OPFGeometryReport`. Symbolic numeric report fields in Python objects, computed from supplied dense tensors. Distinct from [RT-CMP-orthogonal-factor-projection](runtime.md#rt-cmp-orthogonal-factor-projection), the numerical model being assessed, and from [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks), which covers fixture/manifest reports. No supplied object counterpart after comparison. SRC-1 implementation: `jepa-anything-core/src/jepa_anything_core/audit.py`.

> rank = int(torch.linalg.matrix_rank(work).item())
> singular_values = torch.linalg.svdvals(work)
> minimum_singular_value = float(singular_values.min().item())
> --- `jepa-anything-core/src/jepa_anything_core/audit.py`

#### EPI-OBJ-variance-tracker
Label: OnlineVarianceTracker sufficient statistics

Source-native identity: `OnlineVarianceTracker.count`, `.mean`, `.m2`. Symbolic numerical sufficient statistics indexed by factor/coordinate, not learned semantic weights; PyTorch registered buffers in process and checkpointable through module state. They retain information from prior samples. Distinct from the basis parameters in [RT-CMP-orthogonal-factor-projection](runtime.md#rt-cmp-orthogonal-factor-projection); no supplied counterpart after comparison. SRC-1 implementation: `jepa-anything-core/src/jepa_anything_core/losses.py`.

> self.mean.copy_(mean_for_storage)
> self.m2.copy_(m2_for_storage)
> self.count.fill_(int(total_count))
> --- `jepa-anything-core/src/jepa_anything_core/losses.py`

### Routes

#### EPI-RTE-design-diagnostics
Label: Design diagnostic production

Endpoints/progression: parsed mapping → `DesignValidator.validate` branch checks → `report` mapping → standalone CLI JSON/optional file, or generator CLI. Owner: deterministic validator. Context is the declared configuration; it emits facts about coded constraints, not independent world facts. Distinct checking function overlapping [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission), whose identity includes admission and emission; the standalone validator also works without generation. No supersession of that valid container is needed. SRC-1 implementation: `jepa-anything-skill/scripts/validate_design.py`.

- Immediate return: Diagnostic mapping, valid bit, counts; standalone CLI status 0/1, or load error status 2.
- Later read-back: Optional report file can be read by caller; no automatic later reload or expiry policy is implemented here.
- Delegated visibility: inapplicable — no worker dispatch.
- Selection predicate: Explicit config argument; all dispatched validator groups run for a mapping, root-type failure returns early.
- Invalidation or expiry: Recompute for changed input; no report invalidation service.
- Activation or effect: Diagnostics are wired to generator main's validity branch; host repair is instructed, not observed.
- Evidence limits: Predicate dispatch and claim/output branches inspected; not an exhaustive audit of every schema constraint.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposer is the host/caller; code judges declaration validity; host chooses revisions. No mandatory human per-field approval. The oracle is the coded constraint set, not an expected successful design. Mode is open task conversion with deterministic repair feedback. The check admits no change by itself; the separate generator gate consumes it.

Concrete implementation deduction, without execution: a parsed JSON `[]` is not a mapping. It receives `SCHEMA_REQUIRED` at `$`, one failed check, `valid: false`; standalone main returns 1 and generator main returns 1 without rendering. This licenses the proposition that this input violates the implemented root contract, not that the validator knows whether a real task is causally correct.

> if not isinstance(self.config, Mapping):
>     self.fail("SCHEMA_REQUIRED", "$", "The root value must be an object.")
>     return self.report()
> --- `jepa-anything-skill/scripts/validate_design.py`

> "valid": self.error_count == 0,
> --- `jepa-anything-skill/scripts/validate_design.py`

#### EPI-RTE-template-specialization
Label: Template specialization
Part of: [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission)

Endpoints: config fields → `_template_values` / `_python_repr` → placeholder replacement → generated modules and normalized config. Owner: renderer. This part changes representational surface, not scientific support. SRC-1 implementation: `jepa-anything-skill/scripts/generate_scaffold.py`.

- Immediate return: Rendered text internally; enclosing renderer returns generated file list.
- Later read-back: Generated literal constants are imported by downstream modules/tests; config and report copies remain on disk until caller edits/removes them.
- Delegated visibility: inapplicable — no delegated execution.
- Selection predicate: Fixed template keys select config values; every .tmpl under the shipped template root is rendered.
- Invalidation or expiry: Regeneration is explicit; missing placeholders raise; no automatic synchronization after edits.
- Activation or effect: Constants wire downstream checks and dispatcher modes; actual generated package adoption unobserved.
- Evidence limits: Non-ampliative classification applies to literal declaration transfer, not arbitrary downstream behavior of callbacks.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete text trace: for an otherwise renderer-shaped configuration with `task.id` equal to `pendulum`, `_python_repr(task["id"])` yields the Python string literal `'pendulum'`; `TASK_ID_REPR` replaces the corresponding placeholder. For `usage.mode` equal to `repeated_transition`, `USAGE_MODE_REPR` similarly becomes `'repeated_transition'`, which the dispatcher consumes through generated contracts. The emitted literal asserts no new empirical property. This deduction uses inspected text, not target execution. Generation admission and recovery are see [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission).

> "TASK_ID_REPR": _python_repr(task["id"]),
> --- `jepa-anything-skill/scripts/generate_scaffold.py`

> TASK_ID = {{TASK_ID_REPR}}
> --- `jepa-anything-skill/assets/scaffold/src/jepa_task/contracts.py.tmpl`

> for key, value in values.items():
>     rendered = rendered.replace("{{" + key + "}}", value)
> --- `jepa-anything-skill/scripts/generate_scaffold.py`

#### EPI-RTE-evidence-envelope
Label: Planned coverage and evidence-envelope checks

Endpoints: generated claims/experiments → `assert_planned_claim_coverage`; separately caller metadata → `audit_claim_evidence_envelope` → return/exception. Owner: fixed Python comparisons. Two checking functions, separately assessed in the ledger. These are material evaluator parts inside the package in [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest), distinct from the generation/admission path [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission). No supplied route counterpart after comparison. SRC-1 implementation: `jepa-anything-skill/assets/scaffold/src/jepa_task/evaluation.py.tmpl`.

- Immediate return: None on matching declarations/metadata, otherwise exception.
- Later read-back: inapplicable — helper neither retains results nor updates claim status.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: All planned claims for static coverage; explicit claim_id and experiment_id for supplied result metadata.
- Invalidation or expiry: Each call checks current imported declarations; no expiry or withdrawal record.
- Activation or effect: Generated contract test calls both; consume_state does not call either.
- Evidence limits: No score/significance test; passed audit IDs are compared as sets, not authenticated against audit results.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Caller proposes evidence; deterministic code can veto metadata mismatch by exception. There is no scientific answer oracle or statistical acceptance criterion, and no mandatory human approval. Mode is structural contract testing, not an experimental curriculum. The source's own test constructs evidence by copying claim fields, including audit IDs. Thus a successful call can occur without any measured outcome; this concrete countercase defeats an interpretation that passing means scientific support.

> This stub intentionally does not decide statistical support. It rejects a
> result measured with a different metric, direction, split, horizon, model,
> use mode, baseline set, or audit set.
> --- `jepa-anything-skill/assets/scaffold/src/jepa_task/evaluation.py.tmpl`

> "baseline_ids": claim["baseline_ids"],
> "passed_audit_ids": claim["audit_ids"],
> --- `jepa-anything-skill/assets/scaffold/tests/test_contract.py.tmpl`

#### EPI-RTE-measurement-checks
Label: Backend measurement envelope checks

Endpoints: three independent caller mappings → geometry/activity/capacity helpers → return or exception. Owners are fixed Python predicates. Each target and operational path is split in the ledger. Closest supplied [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks) concerns repository fixture/provenance drivers, not these generated downstream helpers. [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest) is their program container, not a duplicate route. SRC-1 implementation: `jepa-anything-skill/assets/scaffold/src/jepa_task/model.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/activity.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/capacity.py.tmpl`.

- Immediate return: None or target-specific ValueError.
- Later read-back: inapplicable — no result retention or claim update.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: Explicit caller chooses which audit to invoke and supplies values; configured AUDITS and capacity contracts set thresholds.
- Invalidation or expiry: Current call only; no link to changed backend weights or automatic staleness detection.
- Activation or effect: Helper exceptions constrain their explicit callers; no automatic requirement before callback consumption.
- Evidence limits: These helpers validate supplied values, not the process that measured them; no supplied measurement trace.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Caller/backend proposes measurements; code decides local threshold compliance; there is no human approval branch. Answer references are declared floors, ceilings, scopes and tolerances, not expected task predictions. Operating mode is bounded numerical envelope checking. No accepted scientific claim or model successor is installed, and rollback of external backend state is not implemented.

> if condition_number > geometry["max_condition_number"]:
>     raise ValueError("Analysis map exceeds the declared condition-number ceiling.")
> --- `jepa-anything-skill/assets/scaffold/src/jepa_task/model.py.tmpl`

> if inactive_factors:
>     raise ValueError(f"Inactive projected factor coordinates: {inactive_factors}.")
> if inactive_encoder:
>     raise ValueError(f"Inactive online-encoder coordinates: {inactive_encoder}.")
> --- `jepa-anything-skill/assets/scaffold/src/jepa_task/activity.py.tmpl`

> if steps != reference["training_steps"] or steps != contract["training_steps"]:
>     raise ValueError("Baseline and reference training steps must match exactly.")
> --- `jepa-anything-skill/assets/scaffold/src/jepa_task/capacity.py.tmpl`

#### EPI-RTE-numerical-audits
Label: Numerical tensor audits

Endpoints: basis/state/projection → detached CPU float64 geometry computations and reconstruction → reports. Owner: numerical library. Context is supplied tensors, precision and tolerances. Distinct from [RT-RTE-core-projection](runtime.md#rt-rte-core-projection), which computes/transforms state and mutates parameters; distinct from fixture/provenance checks in [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks). SRC-1 implementation: `jepa-anything-core/src/jepa_anything_core/audit.py`.

- Immediate return: Numerical reports with pass/violations; malformed/nonfinite inputs can raise.
- Later read-back: uninspected — caller may retain reports, but no later consumer of accumulated reports is established here.
- Delegated visibility: inapplicable — no worker dispatch.
- Selection predicate: Caller chooses audit and tolerances; aggregate audit invokes basis, factor, round-trip and transpose checks.
- Invalidation or expiry: Report covers supplied inputs; caller must rerun for changed tensors.
- Activation or effect: Returns diagnostics; does not alter projection, accept scientific claims or enforce a caller response.
- Evidence limits: Actual sampled numerical inputs and runs not supplied; factor-audit internals not assessed here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

For basis checking the target is a finite floating tensor with three positive dimensions; numerical rank and orthogonality/completeness errors are compared with dimensions/tolerance. For round trips the target is reconstruction of the supplied state, not prediction of an unseen world. Caller proposes tensors and criteria; program computes verdicts; no human decision is encoded. Numerical reference is the same input state/dimensional geometry, not domain labels. Reporting success has advisory force only.

> reconstructed = compose_state(decompose_state(state, basis), basis)
> max_error, rms_error, normalized_mse = _reconstruction_statistics(state, reconstructed)
> --- `jepa-anything-core/src/jepa_anything_core/audit.py`

> passed=(
>     basis_report.passed
>     and factor_report.passed
>     and round_trip_report.passed
>     and transpose_report.passed
> ),
> --- `jepa-anything-core/src/jepa_anything_core/audit.py`

#### EPI-RTE-variance-history
Label: Variance history and streaming penalty

Endpoints: factor samples → finite/shape checks → Welford update of count/mean/m2; later samples plus stored statistics → differentiable combined variance → std-floor penalty. Owner: caller-invoked tracker/loss functions. Distinct from [RT-RTE-core-projection](runtime.md#rt-rte-core-projection): these are sample-summary buffers and losses, not basis/target parameter mutations. No supplied counterpart after comparison. SRC-1 implementation: `jepa-anything-core/src/jepa_anything_core/losses.py`.

- Immediate return: update mutates buffers; streaming function returns a loss and optionally updates history.
- Later read-back: Subsequent streaming calls combine current samples with historical count/mean/m2; registered buffers make checkpoint retention possible but no actual save/reload is evidenced.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: Explicit update argument; OnlineVarianceLoss defaults to updating in training mode only.
- Invalidation or expiry: reset zeroes all accumulated statistics; invalid/nonfinite/overflowing updates reject before buffer writes; no age-based expiry.
- Activation or effect: Retained statistics directly enter later combined variance and loss; no optimizer is invoked by this route.
- Evidence limits: Floating-point summary accuracy and actual caller usage are not empirically measured here; improved future action and learning remain unestablished.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The target is per-coordinate activity over historical plus current samples. Evaluator is a numeric std-floor penalty, not a scientific accept/reject decision. Caller controls update/reset and optimizer use; no human content approval or successor selection is encoded. The separate composite objective explicitly performs no optimizer/EMA update, so differentiability is not evidence of an executed policy change. This is trace-derived numerical history with an implemented later consumer, not automatically an accepted theory or knowledge claim.

> coordinate_variance = tracker.combined_variance(factors)
> standard_deviation = torch.sqrt(coordinate_variance + eps)
> penalties = torch.relu(min_std - standard_deviation)
> loss = _reduce(penalties, reduction)
> if update:
>     tracker.update(factors)
> return loss
> --- `jepa-anything-core/src/jepa_anything_core/losses.py`

> self.count.zero_()
> self.mean.zero_()
> self.m2.zero_()
> --- `jepa-anything-core/src/jepa_anything_core/losses.py`

> This pure function intentionally performs no optimizer or EMA update.  It is
> suitable for generated task skeletons while keeping training lifecycle and
> target-encoder stop-gradient decisions explicit at the call site.
> --- `jepa-anything-core/src/jepa_anything_core/losses.py`

### Claims

#### EPI-CLM-world-model-compiler
Label: World-model compiler with bounded validation

Claimed operation: natural-language world-model task → validated design and inspectable no-training skeleton; invalid designs and nonempty destinations are refused along the documented workflow. Claimed warrant is expressly internal completeness, not empirical success. This compiler-facing claim is distinct from, and bounded by, validator-specific [RT-CLM-validation-scope](runtime.md#rt-clm-validation-scope). Source: SRC-1 doctrine/design, `jepa-anything-skill/SKILL.md`; implementation support and direct-render countercase are see [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission).

> Treat all design choices as hypotheses.
> --- `jepa-anything-skill/SKILL.md`

> The generator refuses invalid designs and non-empty destinations. Its adapter, OPF state, geometry/activity audits, mode consumer, capacity audit, claim audit, and contract tests contain no optimizer or training loop.
> --- `jepa-anything-skill/SKILL.md`

> A passing validator proves only that the declared design and evidence plan are internally complete. It does not prove activity, synthesis quality, semantics, model quality, or claim support.
> --- `jepa-anything-skill/SKILL.md`
