---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Eigenius epistemic routes: prose interpretation, scoped proof checking, statistical decisions and consequential witness consumption."
run-id: AAS-2026-10-15-eigenius-fe68ed89519b-01
reviewed-boundary: "836498ebd99733067d45aa6f7b09d4ff5035dd99"
---

# Eigenius epistemic report

## Source-and-claim boundary

This report asks which routes turn supplied or generated content into something a later consumer may rely on, and what each check actually licenses. The functional boundary, exclusions and frozen evidence identity are those of [boundary](boundary.md#boundary-and-evidence); sources resolve in its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed operation or causal experiments. The target remains a complete artifact with a partial operational loop, not an autonomous agent host.

The inspected architecture distinguishes interpretation, retention, structural admission, domain checking and later witness consumption. In particular, a proof check has a consequential consumer beyond displaying a verdict. This is not evidence that arbitrary prose is faithfully interpreted or that scientific premises are true. Public warrant claims are [RT-CLM-formalize-claims](runtime.md#rt-clm-formalize-claims), [EPI-CLM-verifiable-platform](#epi-clm-verifiable-platform), [EPI-CLM-epistemic-categories](#epi-clm-epistemic-categories) and [EPI-CLM-lean-correspondence](#epi-clm-lean-correspondence).

### Coverage

“Direct” below means source text inspected for this member, at SRC-1's frozen revision. “Supplied” means the runtime member supplies the finding and passage. Available but uninspected paths are not access failures or evidenced absences.

| Entry point or operation | Source path | Coverage and records, or remaining limit |
|---|---|---|
| CLI local/remote dispatch | `cli/src/main.rs` | Direct dispatch arms, including local validate/compile/decompile/lexicon/reflect and remote data/institution/capability/mirror/env/script/tasks/branch/merge/consolidate. Formalization/load/run details are supplied by [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize), [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission), [RT-RTE-program-execution](runtime.md#rt-rte-program-execution). Other local handlers, merge decisions and consolidation semantics remain unassessed; no complete negative about their epistemic checks follows. |
| All sixteen MCP registrations | `orchestration/src/mcp/server.ts` | Direct registration and handler reads: query, inspect, branch/tag listing, institutions, schema, topology, load, program validate/run/by-IRI, health, formalize/result, tasks/status. Most transport findings remain in supplied runtime records. Query has a write alternative: [EPI-RTE-fiber-retention](#epi-rte-fiber-retention). The Explore heading is not a read-only enforcement boundary. Schema generation internals and every query operator remain uninspected. |
| Notebook generation and optional land | `notebooks/src/runtime/notebookStore.ts` | Supplied [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize); publication/reopening and browser persistence not reassessed. Their absence cannot be inferred. |
| Parser/ranker, replay, strict/partial emission | `kernel/src/dcg/reading_ranker.rs`; `kernel/src/dcg/parse/resolve.rs`; `crates/eigenius-encoding/src/formalize.rs` | Supplied [RT-RTE-reading-selection](runtime.md#rt-rte-reading-selection), [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize). Other proposer seams, full grammar and source-to-proposition fidelity remain unassessed. No observed truth-apt conjecture instance was supplied. |
| Load, institution disposition and trusted follow-up | `kernel/src/commit/phases.rs`; `kernel/src/institution/dispatch.rs` | Direct [EPI-RTE-verdict-disposition](#epi-rte-verdict-disposition); supplied [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission). Hook effects and crash consistency beyond those records remain uninspected. |
| Lean proof checker and claim correspondence | `crates/eigenius-lean/src/institution.rs`; `crates/eigenius-lean/src/checker.rs` | Direct [EPI-RTE-lean-check](#epi-rte-lean-check). Externalization call and comparison inspected, not a full audit of `crates/eigenius-lean/src/externalize.rs`, nanoda internals or the authoring worker. This prevents an independent proof of translation/checker soundness. |
| Judgement validation and downstream witness use/withdrawal | `kernel/src/validation/rules/eigentt_value.rs`; `kernel/src/nbe/check/mod.rs`; `kernel/src/program/check_hooks.rs`; `kernel/src/layer/witness_admission.rs` | Direct selected judgement arms, witness synthesis, lookup, normalization, trace classification and dependency rebinding: [EPI-RTE-witness-consumption](#epi-rte-witness-consumption). Not an audit of the complete type checker or all validator rules. |
| Statistics institution | `crates/eigenius-statistics/src/validate.rs` | Direct entry, file/inline input seam and common result decision: [EPI-RTE-statistical-decision](#epi-rte-statistical-decision). Numerics, every design-specific arm, scope checks and downstream composite certificates remain uninspected. This prevents a complete scientific-method or statistical-correctness judgment. |
| Program execution and model components | `kernel/src/server/programs.rs`; `orchestration/src/main.ts`; `orchestration/src/components/complete_text.ts` | Supplied [RT-RTE-program-execution](runtime.md#rt-rte-program-execution), [RT-RTE-runtime-registration](runtime.md#rt-rte-runtime-registration); direct CompleteText template transformation in [EPI-RTE-prompt-interpolation](#epi-rte-prompt-interpolation). CompleteJson, mock/live alternatives beyond supplied coverage, and registered Julia/R/OCI worker semantics remain unassessed. |
| Data verify and data validate | `cli/src/data.rs` | Direct [EPI-RTE-file-verification](#epi-rte-file-verification), [EPI-RTE-layout-validation](#epi-rte-layout-validation). Resolver and worker-side full-file validation not audited. Attach/provision/import lineage remains unassessed. |
| Retrieval, maintenance and other shipped evaluators | `kernel/src/query/`; `kernel/src/task/`; `storage/`; `ontologies/`; `experiments/`; `demo/`; `scripts/` | Only the seams above and supplied runtime coverage. Full retrieval, GC, task cleanup/resume, imports, institution/comorphism alternatives, method instructions and experimental comparison designs remain unassessed. These included operations prevent a system-complete negative about acceptance, revision, knowledge production or learning. |

No target code, tests, demos or model services were executed. Missing provider transcripts and linked candidate/result instances prevent claims of exercised faithful interpretation, successful proof checking or accepted scientific discovery. Missing experiment/intervention evidence prevents causal attribution of benefit. Provider parameters and mutable endpoint identities remain bounded by [RT-CMP-proposer-model](runtime.md#rt-cmp-proposer-model), [RT-CMP-reading-model](runtime.md#rt-cmp-reading-model) and [RT-CMP-completion-model](runtime.md#rt-cmp-completion-model); no additional parameter-update inference is made here.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-formalization-artifact](runtime.md#rt-obj-formalization-artifact) | Interpreted propositions and explicit non-encoding cuts; see record | see record | see record | Emission and retention do not certify meaning or external truth. |
| [RT-OBJ-program-resource](runtime.md#rt-obj-program-resource) | Executable symbolic control; arbitrary body is not itself an individuated empirical claim | see record | see record | Its text prompts have a separate interpretation consumer below. |
| [EPI-OBJ-completion-template](#epi-obj-completion-template) | Truth-aptness depends on supplied template/input; no concrete knowledge claim identified | see record | see record | Policy instructions and factual assertions can coexist. |
| [EPI-OBJ-proof-inputs](#epi-obj-proof-inputs) | A formal proposition and an offered proof of it | see record | see record | Formal encoding fidelity and premises' real-world warrant are separate. |
| [EPI-OBJ-verification-trace](#epi-obj-verification-trace) | Checker judgement about proof and proposition; provenance about the checking occasion | see record | see record | Claimed binary identity is self-reported. |
| [EPI-OBJ-statistical-result](#epi-obj-statistical-result) | Numeric result, statistical decision and conditional encoded proposition | see record | see record | Runnable-plan verdict differs from per-effect decision. |
| [EPI-OBJ-pinned-file](#epi-obj-pinned-file) | Claim that retrievable bytes match a pin; dataset contents can contain measurements | see record | see record | Byte identity does not certify measurement origin or truth. |

## Authority-route ledger

Each row separates a consequential function, even when one canonical route performs several functions. Owned fields say “see” rather than duplicating the shared records. Architectural status is assessed here. No row asserts observed activation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize) | content transformation | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | see record | [RT-CLM-formalize-claims](runtime.md#rt-clm-formalize-claims) | Fidelity not established | Import of source prose is acquired content; its interpreted symbolic output may reshape or add claims. Selecting among parses does not establish entailment or non-entailment. A paired source/artifact semantic assessment is missing. |
| [RT-RTE-reading-selection](runtime.md#rt-rte-reading-selection) | operational admission/selection/consumption | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | [RT-CLM-formalize-claims](runtime.md#rt-clm-formalize-claims) | Membership is not fidelity | Choice changes which existing candidate is used, not its warrant. |
| [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | none | Recorded answers and artifact bytes are not accepted ampliative claims. |
| [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | [RT-CLM-formalize-claims](runtime.md#rt-clm-formalize-claims) | Pipeline-specific | Structure/retroactive validity is not scientific truth. |
| [EPI-RTE-lean-check](#epi-rte-lean-check) | check/evidence production | implemented | see record | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | see record | [EPI-CLM-lean-correspondence](#epi-clm-lean-correspondence) | README mechanism differs | Conditional on checker and encoding contracts; not an empirical inference. |
| [EPI-RTE-verdict-disposition](#epi-rte-verdict-disposition) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | [EPI-CLM-verifiable-platform](#epi-clm-verifiable-platform) | Verdict scope matters | Gate admission is not generic acceptance of all content. |
| [EPI-RTE-verdict-disposition](#epi-rte-verdict-disposition) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | none | Rejected-subject audit retention is distinct from subject admission. |
| [EPI-RTE-witness-consumption](#epi-rte-witness-consumption) | lifecycle integration | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | [EPI-CLM-epistemic-categories](#epi-clm-epistemic-categories) | Restricted to checked proof credit | Accepted proof result is connected to evidence and later certificate use; attribution traces do not inherit proof acceptance. |
| [EPI-RTE-witness-consumption](#epi-rte-witness-consumption) | lineage/freshness/recovery | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | none | Dependency rebinding can withdraw credit without deleting immutable history. |
| [EPI-RTE-statistical-decision](#epi-rte-statistical-decision) | check/evidence production | implemented | see record | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | see record | [EPI-CLM-verifiable-platform](#epi-clm-verifiable-platform) | No automatic proof grade | Derivation is bounded to a numeric decision from supplied data, parameters and algorithm, not truth of a population mechanism. |
| [EPI-RTE-statistical-decision](#epi-rte-statistical-decision) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | Gate Holds differs from effect Holds | Statistical acceptance is scoped to the encoded decision criterion, not general empirical acceptance. |
| [EPI-RTE-fiber-retention](#epi-rte-fiber-retention) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | Explore label is not a read-only guarantee | The persisted output's earlier semantic transformation is not established by this handler alone. |
| [EPI-RTE-prompt-interpolation](#epi-rte-prompt-interpolation) | content transformation | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | Text rewrite is not semantic checking | Concrete replacement is established below; truth preservation depends on template and input. |
| [RT-RTE-program-execution](runtime.md#rt-rte-program-execution) | operational admission/selection/consumption | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | Static validation is not type checking | Programs/completions need not contain truth-apt claims; when they do, generated text alone does not establish acceptance. |
| [EPI-RTE-file-verification](#epi-rte-file-verification) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | Content identity only | No durable endorsement follows from printed verified=true. |
| [EPI-RTE-layout-validation](#epi-rte-layout-validation) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | see record | none | valid=true can mean deferred or no schema | Not a universal full-file validation certificate. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-formalize-claims](runtime.md#rt-clm-formalize-claims) | see record | see record | see record | [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize), [RT-RTE-reading-selection](runtime.md#rt-rte-reading-selection), [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) | none supplied | No intervention or source/artifact fidelity evaluation | Typed structure and candidate selection, not warranted meaning | Separate load and partial cuts limit “kernel-checked claims.” |
| [EPI-CLM-verifiable-platform](#epi-clm-verifiable-platform) | see record | see record | see record | [EPI-RTE-lean-check](#epi-rte-lean-check), [EPI-RTE-witness-consumption](#epi-rte-witness-consumption), [EPI-RTE-statistical-decision](#epi-rte-statistical-decision) | none supplied | see record | see record | External premises and interpretation remain outside proof license. |
| [EPI-CLM-epistemic-categories](#epi-clm-epistemic-categories) | see record | see record | see record | [EPI-RTE-witness-consumption](#epi-rte-witness-consumption), [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize) | none supplied | see record | see record | Human-only Declared and run-output-as-ground readings do not match these routes. |
| [EPI-CLM-lean-correspondence](#epi-clm-lean-correspondence) | see record | see record | see record | [EPI-RTE-lean-check](#epi-rte-lean-check), [EPI-RTE-verdict-disposition](#epi-rte-verdict-disposition) | none supplied | see record | see record | Frozen README's three-part mirror account is superseded in implementation, not the supplied runtime records. |

## Bounded conclusion

Eigenius has implemented routes for acquiring prose, selecting symbolic interpretations, retaining decision draws and artifacts, and later using retained resources or programs. Those routes do not by themselves establish acceptance of new scientific knowledge. Source lineage can be retained, but source warrant through prose-to-proposition interpretation is unknown; neither entailment nor non-entailment of arbitrary generated propositions is established by type membership. See [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize), [RT-RTE-reading-selection](runtime.md#rt-rte-reading-selection) and [EPI-RTE-prompt-interpolation](#epi-rte-prompt-interpolation).

There is a narrower, substantive proof route. Its criterion is successful checking of an offered export and correspondence to the claim's proposition under the allowed axioms and supported correspondence domain. Its intended use is formal Verified credit, not validation of empirical premises. The Load disposition can reject the subject, retain audit evidence, and integrate a successful verification judgement into later witness-dependent checking. A dependent rebinding or tombstone can withdraw that credit. This is implemented acceptance and integration of a scoped proof result, not merely storage of an unchecked “verified” label: [EPI-RTE-lean-check](#epi-rte-lean-check), [EPI-RTE-verdict-disposition](#epi-rte-verdict-disposition), [EPI-RTE-witness-consumption](#epi-rte-witness-consumption). It depends on trusted checker/translation machinery and does not establish global soundness across uninspected routes.

The statistical common path separately computes an effect decision from observations and an authored plan. Its material criterion is p below alpha with the implemented direction guard. Operational admission of a runnable plan can still succeed when the effect does not reject. Numerical results and an optionally attached proposition are not an automatic Verified witness or evidence of a real causal mechanism. Source data, design adequacy, auxiliary assumptions and numerical validity remain distinct: [EPI-RTE-statistical-decision](#epi-rte-statistical-decision). File/hash and layout checks carry still narrower licenses: [EPI-RTE-file-verification](#epi-rte-file-verification), [EPI-RTE-layout-validation](#epi-rte-layout-validation).

No supplied candidate instance and trace establishes an accepted ampliative scientific claim. This is an evidence limit, not an architecture-wide absence. Direct policy/control effects exist through executable resources and model prompts, independently of truth-apt routes: [RT-BAP-retained-program](runtime.md#rt-bap-retained-program), [RT-BAP-completion-prompt](runtime.md#rt-bap-completion-prompt). Retention/replay supports later dependence on answers, not demonstrated improved capacity. Learning benefit is unestablished; reflection, autonomous theory building and self-improvement remain independently unassessed outside the selected paths. The method does not collapse these properties into the success or failure of proof checking. No single epistemic score or system-wide reliability verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-completion-template
Label: CompleteText completion template

Part of: [RT-OBJ-program-resource](runtime.md#rt-obj-program-resource)

The material text part of the supplied program-resource container has a different consumer from its symbolic expression body. User/system prompt strings are natural-language policy or content, stored in component arguments, and may persist with a containing resource. Input resource fields are symbolic values until inserted into text for model interpretation. Exact truth-apt propositions are not determinable without an actual template/input instance. SRC-1, `orchestration/src/components/complete_text.ts`. The downstream authority is [RT-BAP-completion-prompt](runtime.md#rt-bap-completion-prompt), not a new registry grant.

> const prompt = formatPrompt(userPrompt, req.input);
> --- `orchestration/src/components/complete_text.ts`

#### EPI-OBJ-proof-inputs
Label: Lean proof inputs

A `LeanProofTerm` references `LeanProofPayload` bytes and a target declaration, plus a claim whose `eigentt:proposition` is decoded to an EigenTT expression. These are symbolic proof/claim objects stored as chain resources or embedded payloads; the byte string is not natural-language evidence merely because its transport type is string. Closest supplied records are [RT-OBJ-formalization-artifact](runtime.md#rt-obj-formalization-artifact) and [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission): neither identifies this proof/claim pair, and the code does not establish that this pair was generated by document formalization. SRC-1, `crates/eigenius-lean/src/institution.rs`, `crates/eigenius-lean/src/checker.rs`; load-bearing extraction and checking evidence is in [EPI-RTE-lean-check](#epi-rte-lean-check).

#### EPI-OBJ-verification-trace
Label: Lean VerificationTrace

A symbolic chain resource records `holds(logic_lean4, Checked(payload), P)`, claim IRI, payload, target declaration, permitted axioms and checker identity. It is distinct from the emitted artifact in [RT-OBJ-formalization-artifact](runtime.md#rt-obj-formalization-artifact) and the executable program in [RT-OBJ-program-resource](runtime.md#rt-obj-program-resource). It is evidence emitted by a different checking route, not a renamed output of either. SRC-1, `crates/eigenius-lean/src/institution.rs`. Checker identity uses a deployment-provided image digest or a source/toolchain pin; the source explicitly calls this self-reported provenance, not independent attestation. Recomputability requires the inputs, compatible checker and interpretation contract, not just a matching string.

> let judgement = encode_judgement(LOGIC_LEAN4, &checked, &prop, &names)
>         .map_err(|e| encode_err("judgement", format!("{e:?}")))?;
> --- `crates/eigenius-lean/src/institution.rs`

> Self-reported either way: the kernel repeats what it was told. It is provenance, not warrant,
> /// and becomes load-bearing only when something outside the process vouches for the binding.
> --- `crates/eigenius-lean/src/institution.rs`

#### EPI-OBJ-statistical-result
Label: StatisticalAnalysisResult

The institution emits symbolic result resources with computed numerics, per-effect constructor and, on the common rejecting path, a canonical proposition. Chain storage occurs through institution disposition, not model weights. Closest supplied [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) is the generic Load container; this result object is a domain-specific product, not a duplicate of [RT-OBJ-formalization-artifact](runtime.md#rt-obj-formalization-artifact). SRC-1, `crates/eigenius-statistics/src/validate.rs`. Its premise data may be inline or read from content-pinned files. It is not automatically a ground of Verified credit; see [EPI-RTE-statistical-decision](#epi-rte-statistical-decision) and [EPI-RTE-witness-consumption](#epi-rte-witness-consumption).

#### EPI-OBJ-pinned-file
Label: PinnedExternalFile

A symbolic chain descriptor carries a reference/content hash and optional schemas; external bytes contain data whose form depends on the file. The descriptor is not a provider's numerical parameters or a formal proof. Closest supplied [RT-OBJ-program-resource](runtime.md#rt-obj-program-resource) can consume data but is not this descriptor or dataset. SRC-1, `cli/src/data.rs`, `crates/eigenius-statistics/src/validate.rs`. The latter's file-backed observation seam reads a named column via the content-array store; source measurement provenance and importer accuracy remain unassessed.

> .read_column(&reference, &content_hash, &media_type, &column)
> --- `crates/eigenius-statistics/src/validate.rs`

### Routes

#### EPI-RTE-lean-check
Label: Lean claim check

The in-process institution resolves proof inputs, decodes the claim's proposition, checks the export and compares the externalized proposition to the target declaration's type. SRC-1 implementation, `crates/eigenius-lean/src/institution.rs`, `crates/eigenius-lean/src/checker.rs`. It is a distinct domain evaluator from [RT-RTE-reading-selection](runtime.md#rt-rte-reading-selection); it supplies results to the generic [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) and may also be called directly through institution query. It is therefore not wholly a part of the Load route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Holds, Fails with diagnostic, or institution computation error; a named successful claim can also produce a VerificationTrace.
- Later read-back: emitted traces can persist through disposition and later ground witness synthesis; no passing run was supplied.
- Delegated visibility: checker receives payload bytes, target name, hard-coded permitted axioms, decoded proposition and candidate read layer; not a conversational history.
- Selection predicate: institution procedure must be proof_check; a supplied claim reference must resolve, carry a proposition and decode. The committed shape requires claim_iri according to the inspected institution contract; a direct query with no claim can fall back to name-only checking and produces no claim verification trace.
- Invalidation or expiry: each check reparses; correspondence checks gate the export's declared Lean major/minor to 4.29. Later credit withdrawal is handled separately by witness lookup. No temporal expiry was inspected.
- Activation or effect: implementation produces a scoped judgement only after the checker accepts; actual checking, trace commitment and downstream use are unobserved.
- Evidence limits: externalizer internals and nanoda implementation were not audited; proof validity is conditional on these trusted components, permitted axioms and encoding fidelity. A name-only check licenses no correspondence claim. Embedded proof terms without an ID can yield Holds without a retained trace.

The target domain is formal validity of this export plus definitional equality to this claim's externalized proposition. Code, not a model or mandatory human reviewer, decides. The offered proof and authored claim are supplied candidates. There is no separate empirical answer oracle; the proof/checker is the formal evaluator. The open query/load request is not an improvement experiment. The allowlist is `propext`, `Classical.choice`, `Quot.sound`, `Lean.trustCompiler`; per-environment authoring overrides are not read on this checking path.

A successful result is a checked derivation from the export's formal environment under those axioms. It does not validate data, omitted assumptions, the intended English interpretation, or a population mechanism. A checkable contradiction or counterexample is not inferred from a mere Fails: infrastructure/version/translation problems can make the claim unjudgeable rather than false. The code distinguishes CheckError and Verdict::Fails, although both can ultimately refuse admission.

> let verdict = check_proof(
>         bytes.as_bytes(),
>         &target_name,
>         &permitted_axioms,
> --- `crates/eigenius-lean/src/institution.rs`

> if let Err(p) = catch_unwind(AssertUnwindSafe(|| export.check_all_declars())) {
> --- `crates/eigenius-lean/src/checker.rs`

> if tc.def_eq(goal, info.ty) {
>             Verdict::Holds
> --- `crates/eigenius-lean/src/checker.rs`

> if expected.is_some() {
>         gate_lean_version(bytes)?;
>     }
> --- `crates/eigenius-lean/src/checker.rs`

#### EPI-RTE-verdict-disposition
Label: AutoOnLoad verdict disposition

Part of: [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission)

This is the institution-result disposition part, not a second declaration of generic resource admission. The commit phase dispatches checks over the fresh candidate layer, stamps outcomes, queues an audit sibling and decides continuation. SRC-1 implementation, `kernel/src/commit/phases.rs`, `kernel/src/institution/dispatch.rs`; generic branch progression/recovery remains owned by the supplied parent.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Continue or validation error, with dispatched verdict records and queued audit resources when construction succeeds.
- Later read-back: verdict/provenance siblings can persist even for rejected subjects; successful trace resources can reach witness consumers.
- Delegated visibility: institution query uses a read-only context over the built candidate layer; dispatch uses the already selected institution index/runtime.
- Selection predicate: the phase runs only with institution context. Handler errors reject; Fails creates validation errors. The executable end condition refuses fail_errors and otherwise continues; Undecidable is not proof acceptance.
- Invalidation or expiry: failed subject admission does not require deletion of the audit sibling. Exact durable recovery is uninspected; successful external effects are not reversed by rejection.
- Activation or effect: Fails blocks the candidate pipeline while an audit sibling is queued first. Per-effect derivations are dropped on Fails; Trace subclasses are also dropped unless the verdict Holds.
- Evidence limits: this is the WithInstitutions path, not every persistence route. A common verdict constructor has only its evaluator's domain-specific meaning; Undecidable continuation is not epistemic acceptance.

Software computes disposition; callers propose content and select policy, with no mandatory per-content human approval established. This is open admission. A Holds proof result is accepted for recorded formal-check credit; a statistics gate Holds only attests runnability. On success, downstream trace integration is a separate function, not synonymous with retention. The trusted follow-up bypass is deliberate: see the supplied structural-followup countercase and [EPI-RTE-witness-consumption](#epi-rte-witness-consumption). No universal validation guarantee is added.

> if !fail_errors.is_empty() {
>         let total = fail_errors.len();
>         return Err(CommitError::Validation {
>             errors: fail_errors,
>             total_violations: total,
>         });
>     }
> --- `kernel/src/commit/phases.rs`

> if is_trace && !matches!(dispatch.verdict, VerdictReading::Holds) {
>         return None;
>     }
> --- `kernel/src/institution/dispatch.rs`

#### EPI-RTE-witness-consumption
Label: Chain witness consumption

A later type-checking request synthesizes a witness from category, target IRI and proposition, using current chain state. SRC-1 implementation, `kernel/src/program/check_hooks.rs`, `kernel/src/layer/witness_admission.rs`, `kernel/src/validation/rules/eigentt_value.rs`, `kernel/src/nbe/check/mod.rs`. This downstream semantic consumer is distinct from the write/admission route [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) and from executing a retained program [RT-RTE-program-execution](runtime.md#rt-rte-program-execution). It overlaps their state but is not a duplicate of either.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: a ChainWitness value or a reason that the cited Grounds constructor cannot be well-typed.
- Later read-back: each later chain-attached check can consume retained proof judgements or traces. Lookup itself persists no new witness object.
- Delegated visibility: the checker hook receives expected predicate indices and a layer; lookup resolves trace target, normalized proposition and dependencies in the admitting chain.
- Selection predicate: recognized witness category, two indices, IRI and matching proposition hash; a matching local or ancestor witness is required. Pure contexts without a layer cannot admit one.
- Invalidation or expiry: a descendant redefinition or tombstone of the target or proposition dependencies refuses ancestor credit. This is conservative on any rebinding, including narrowing, not a fresh proof check. New appropriate evidence must be committed to re-earn credit.
- Activation or effect: lookup gates witness-dependent type checking; retained evidence can enable a later certificate, and dependency changes can block it. No exercised dependence or benefit was supplied.
- Evidence limits: full checker/validator correctness and all input bypasses are unassessed. Verified-trace lookup has a fallback to target proposition when judgement is missing; the standard emitted trace carries a judgement. This member does not claim that raw lookup independently rechecks nanoda or authenticates arbitrary hand-built layers.

The consumer is the type checker through DefaultCheckHooks. Its channel is category/IRI/proposition lookup. Its force is enforcing for witness-dependent constructor typing, with a horizon of subsequent checks in descendants while dependency credit remains valid. It does not confer unrestricted trust on English assertions.

Declared and Observed credit are attribution paths, not proof that the assertion is true or measurement happened. `ProgramTrace` deliberately grounds nothing. Verified can arise from a stored proof judgement or a verification trace; a certificate judgement is refused as a substitute for a proof of the proposition. Hand-authored external Checked terms are refused by the standard judgement validation path; institution-emitted Checked judgements enter through trusted build/persist follow-up instead. That split is a trust boundary, not a claim that every low-level layer construction validates.

For acceptance/integration, the upstream formal evaluator's successful judgement is connected to target/evidence and grants bounded future use. For withdrawal, code recomputes lookup and dependency conditions; neither a model nor mandatory human selects the result. This is open checking, with no curriculum or improvement trigger. No claim about theory-builder conditions 3–4 follows from rejecting a missing witness: a typing error is not necessarily content-directed empirical criticism. Localized formal content and semantic consumption are supported for these propositions, while formulated explanation, retained criticism, iteration and improved capacity require separate evidence.

> let witness_val = crate::layer::synthesize_chain_witness(layer, category, &iri, &prop_exp)?;
> --- `kernel/src/program/check_hooks.rs`

> wk::PROGRAM_TRACE => None,
>         wk::VERIFICATION_TRACE => Some(WitnessCategory::Verified),
> --- `kernel/src/layer/witness_admission.rs`

> if rebinds(query) || walked_past.iter().any(|l| rebinds(l)) {
> --- `kernel/src/layer/witness_admission.rs`

> return match crate::nbe::check::check(&mut ctx, &j.term, &typ_val) {
> --- `kernel/src/validation/rules/eigentt_value.rs`

> Exp::Checked(iri) => Err(CheckError::IllFormed(format!(
> --- `kernel/src/nbe/check/mod.rs`

#### EPI-RTE-statistical-decision
Label: Statistical effect decision

The common `do_validate_analysis_plan` path reads the sample set and authored analysis parameters, computes a test result and emits a gate verdict plus per-effect result. SRC-1 implementation, `crates/eigenius-statistics/src/validate.rs`. This domain-specific evaluator is distinct from the generic disposition route [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission); like Lean it supplies rather than duplicates that route's decisions. The common decision is inspected, not every statistical arm.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: malformed/unsupported plans can gate-Fail; a runnable common-path test returns gate Holds and a main_effect result with numerics and effect Holds/Fails.
- Later read-back: emitted result resources can be retained through institution disposition. Later plan-reproducibility/certificate construction is described in source but its full implementation was not inspected.
- Delegated visibility: plan, resolved SampleSetResource and layer-dependent codec names enter the deterministic Rust procedure. File-backed flat observations use reference, content hash, media type and column.
- Selection predicate: design dispatch and input checks precede the inspected common path. Its effect rejects only when p_value_for_alpha < alpha and direction_ok; canonical proposition attaches only on rejection and only if a derived proposition exists.
- Invalidation or expiry: later resource mutation is subject to the selected commit policy; full statistical-result refresh/recomputation semantics are uninspected. This check does not automatically rerun because a new scientific observation exists externally.
- Activation or effect: software selects whether the effect receives Holds and whether a proposition is attached; the enclosing gate can admit a non-rejecting test. Actual numerical results and downstream reliance are unobserved.
- Evidence limits: numerics, design validity, source observations, scope checks and all special arms are unassessed. A threshold result is conditional on supplied data and plan assumptions, not proof that a substantive scientific mechanism is true.

Caller-authored plan/data are the candidates; code computes and decides, with no mandatory human effect review established. The numeric formula/threshold is an evaluator, not a supplied empirical answer oracle. Mode is an open analysis request, not a bounded improvement experiment. The material criterion for the common effect is explicit and can withhold the positive proposition. A significant one-sided result in the opposite direction is a concrete countercase to a p-only rule. This is an evidence-consuming statistical decision for its encoded effect, not evidence of accepted explanatory discovery. Arithmetic derivation is conditional on input and algorithm correctness; ampliative inference to an external population would need separately warranted design/data/interpretation assumptions and an acceptance decision for that use.

> let test_rejected = p_value_for_alpha < alpha && direction_ok;
> --- `crates/eigenius-statistics/src/validate.rs`

> let canonical_for_result = if test_rejected {
>         derived_proposition.as_ref()
>     } else {
>         None
>     };
> --- `crates/eigenius-statistics/src/validate.rs`

#### EPI-RTE-fiber-retention
Label: FIBER INTO retention

The exposed query handler can turn query-produced `into_resources` into a branch commit. SRC-1 implementation, `kernel/src/server/query.rs`, `orchestration/src/mcp/server.ts`. This is an additional shipped operation omitted from the runtime's selected route records, not a correction of their identities. It resembles [RT-RTE-program-execution](runtime.md#rt-rte-program-execution) in using WithRetroactive but is initiated by EigenQL, not RunProgram; generic [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) concerns Load and does not own this route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: query rows, output resource IRIs, success/errors and branch/CAS outcome; a read-only query produces no INTO commit.
- Later read-back: committed resources can be resolved by later chain consumers; their subsequent use is unobserved.
- Delegated visibility: query evaluation receives the selected layer, institution index/runtime, component registry, execution context and embedder configuration; not all query internals were inspected.
- Selection predicate: only nonempty into_resources enters the write block. Working resources are committed through WithRetroactive with default policy and institutions: None.
- Invalidation or expiry: chain mutation rules apply; query-output-specific expiry, rollback and rerun logic are uninspected.
- Activation or effect: can retain domain output and advance the branch without AutoOnLoad on reinsertion; effects/benefit unobserved.
- Evidence limits: handler inspection does not establish semantic preservation, truth, or successful domain evaluation of every query result. It supplies no universal knowledge acceptance step.

The caller supplies the query and software evaluates/adopts its output subject to the selected commit pipeline. No human per-resource approval or general answer oracle is established. This is an open mutation-capable request, guided by query/program/institution definitions, not an improvement trigger. Rejection at commit does not retroactively undo evaluation effects. Its existence prevents treating an Explore-labelled query tool as operationally read-only or assuming all retained knowledge passes AutoOnLoad.

> crate::commit::PipelineKind::WithRetroactive,
> --- `kernel/src/server/query.rs`

> institutions: None,
> --- `kernel/src/server/query.rs`

#### EPI-RTE-prompt-interpolation
Label: CompleteText prompt interpolation

Part of: [RT-RTE-program-execution](runtime.md#rt-rte-program-execution)

This is the deterministic text-supply part of CompleteText, before the provider inference already owned by the parent. SRC-1 implementation, `orchestration/src/components/complete_text.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: formatted user prompt, supplied with the separate system prompt to generateText; response text later becomes a string-valued output resource.
- Later read-back: inapplicable — interpolation itself writes no retained state; a retained containing template can be invoked again through the parent program route.
- Delegated visibility: model receives formatted user text and systemPrompt, not the original resource as a separately typed premise.
- Selection predicate: first replace one literal {{string}} occurrence with serialized input, then globally replace non-whitespace placeholder keys found in the current text with input values; unknown keys remain.
- Invalidation or expiry: inapplicable — this transformation has only current-call working text; template replacement follows parent resource semantics.
- Activation or effect: changes model-visible input before generation; compliance and truth of the generated response are unobserved.
- Evidence limits: literal string rewriting does not establish truth preservation, entailment, or non-entailment. Template policy and factual content must be assessed per instance.

Concrete source deduction, without target execution: for template `The value is {{urn:x}}; missing {{urn:y}}.` and input `{"urn:x":"7"}`, the literal {{string}} pass does nothing; the regex pass yields `The value is 7; missing {{urn:y}}.` The implementation therefore preserves unknown placeholder syntax rather than supplying evidence for it. This hypothetical input is an illustration of executable semantics, not an observed candidate assertion. The authority channel is natural-language model guidance as in [RT-BAP-completion-prompt](runtime.md#rt-bap-completion-prompt), not a symbolic truth judgement.

> let result = template.replace("{{string}}", JSON.stringify(input));
> --- `orchestration/src/components/complete_text.ts`

> return typeof val === "string" ? val : JSON.stringify(val);
> --- `orchestration/src/components/complete_text.ts`

#### EPI-RTE-file-verification
Label: Data file verification

CLI `data verify` fetches the descriptor, calls resolve_and_materialize against its reference/hash, removes its throwaway directory and prints success or exits with error. SRC-1 implementation, `cli/src/data.rs`. No matching source-data evaluator is declared in supplied [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission); this is a standalone CLI check, not Load or proof verification.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: printed verified=true on resolver success, mismatch report/exit 1 or fetch-error exit 1 otherwise.
- Later read-back: inapplicable — this handler records no durable acceptance; its temporary verification directory is removed.
- Delegated visibility: resolver receives reference, pinned content hash and resolve options; caller receives a content identity result, not inspected measurements.
- Selection predicate: resource must resolve and contain reference/hash; resolver success versus ContentHashMismatch/error chooses the report.
- Invalidation or expiry: inapplicable — printed result has no implemented expiry or later enforcement; a later fetch is a new check.
- Activation or effect: caller continuation can depend on exit status, but no automatic serving-chain promotion or consumer of this result was found in this handler.
- Evidence limits: lower-level resolver/hash implementation and live bytes were not checked. The implemented license is byte identity under that contract, not measurement validity or scientific truth.

The target is a file-to-pin comparison. The programmatic evaluator is the resolver; the reference outcome is the caller-stored hash. This is an open diagnostic request, not an improvement experiment, and no mandatory human judgement is involved in comparison. Reporting alone supplies no implemented knowledge-admission force.

> println!("✓ verified — bytes at {reference} match {content_hash}");
> --- `cli/src/data.rs`

#### EPI-RTE-layout-validation
Label: Data layout validation

CLI `data validate` resolves attached schemas and, for supported flat text, checks a header or sampled collection rows after materialization. SRC-1 implementation, `cli/src/data.rs`. This differs in target and success semantics from [EPI-RTE-file-verification](#epi-rte-file-verification); neither is the supplied [RT-ABS-program-typecheck](runtime.md#rt-abs-program-typecheck), which concerns programs.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: valid/issues reporting or exit 1; no bound schema returns valid=true with an opaque-file note; unsupported encoding/media can return valid=true with layout deferred to worker.
- Later read-back: inapplicable — handler prints results and removes materialized temporary files without recording an acceptance decision.
- Delegated visibility: schema parser/validators receive resolved schemas and header/rows, not scientific context; at most sixteen nonempty lines are read here.
- Selection predicate: bound schemas determine work. Delimited unencoded text enters local checks; member schemas are skipped with a note. Collection versus tabular layout chooses rows versus first-line header.
- Invalidation or expiry: inapplicable — no retained validation state or expiry is implemented by this handler.
- Activation or effect: can exit nonzero on materialization or schema issues; no automatic serving-chain promotion or withdrawal is implemented here.
- Evidence limits: lower-level schema validators and deferred worker checks were not inspected. valid=true alone cannot establish full-file/schema conformance, much less truth of observations.

The check target is declared layout against locally inspected text portions; software decides against attached schema rules. No statistical answer oracle or human approval is implied. Open diagnostic mode and skipped/deferred cases differ from failed checks; the success field must be read with its note. A schema-free file is a concrete countercase to equating successful validation with evidence-consuming layout acceptance.

> "{{\"valid\":true,\"iri\":\"{iri}\",\"note\":\"no schema bound (opaque file)\"}}"
> --- `cli/src/data.rs`

> .take(16)
> --- `cli/src/data.rs`

### Claims

#### EPI-CLM-verifiable-platform
Label: Verifiable science platform

SRC-1 doctrine/design, `README.md`, claims a substrate for trustworthy scientific knowledge rather than convincing text. This is broader than the specific MCP formalization wording in [RT-CLM-formalize-claims](runtime.md#rt-clm-formalize-claims), not a duplicate claim source or scope.

- Claim conclusion status: claimed

> Modern language models can produce convincing text without producing trustworthy knowledge. Eigenius is a substrate for representing what the science actually says: typed resources with tracked provenance, replayable derivations, and — where the claim warrants it — machine-checked formal proofs.
> --- `README.md`

The inspected proof/witness routes substantiate a scoped capacity for checked formal claims and consequential use. The statistical route implements bounded decisions, not generalized trustworthy empirical conclusions. No supplied observed run or causal comparison establishes scientific accuracy, reliable source interpretation, improved model reasoning, or end-to-end warrant for arbitrary science. The mechanism is useful evidence for the narrow claim; it is insufficient for the broadest reading.

#### EPI-CLM-epistemic-categories
Label: Four epistemic categories

SRC-1 doctrine/design, `README.md`, presents an ordered four-category account. This is not the same referent as the parsing claim [RT-CLM-formalize-claims](runtime.md#rt-clm-formalize-claims).

- Claim conclusion status: claimed

> - **Declared** — a human asserts it.
> - **Observed** — measured or recorded with provenance.
> - **Derived** — produced by a typed pipeline whose steps are auditable.
> - **Verified** — derived *and* re-checked by a formal proof system (Lean 4 today).
> --- `README.md`

Countercases qualify this account. [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize) attributes served claims to an unattributed agent, not a mandatory human author. [EPI-RTE-witness-consumption](#epi-rte-witness-consumption) recognizes Declared, Observed and Verified trace categories, while ProgramTrace grounds nothing. This does not prove the Derived terminology is absent elsewhere: composite justification may express derivation. It does rule out reading the README as the exact current witness-grade implementation or as automatic credit granted merely because a program ran. Declared/Observed remain attribution premises; Verified proof does not establish their external truth. No observed category-use or benefit was supplied.

#### EPI-CLM-lean-correspondence
Label: Lean correspondence mechanism

SRC-1 doctrine/design, `README.md`, advertises a three-part AutoOnLoad correspondence mechanism. This is distinct from [RT-CLM-formalize-claims](runtime.md#rt-clm-formalize-claims): its target is proof-to-claim correspondence, not prose formalization.

- Claim conclusion status: claimed

> AutoOnLoad dispatches the three-part correspondence check (D28 §5.5) — proof validity via `nanoda_lib`, mirror correspondence between proposition's `EigeniusFFI.*` references and chain class declarations, anchor-consistency hash.
> --- `README.md`

At the same frozen revision, [EPI-RTE-lean-check](#epi-rte-lean-check) supports proof validity plus direct comparison to the claim's own externalized proposition. The source expressly says the older three-part mechanism is gone. This is a defective frozen documentation fact beside the affected finding, not a request to alter the source boundary or supersede a valid runtime container. The supported conclusion is narrower and stronger on statement identity than name-level checking: an actual proposition is compared, subject to externalization/checker contracts. No execution or independent causal evidence validates that implementation's soundness or deployed operation.

> D28 §5.5's three-part correspondence check is gone, along with `lean:mirror_iri` and
> //! `lean:proposition` (D74 §6.3.1). `def_eq` against the claim's own proposition subsumes it: the
> --- `crates/eigenius-lean/src/institution.rs`
