---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "SIGN epistemic routes: structural compilation admission, provenance doctrine, maintenance signals and the unimplemented agent-consumption boundary."
run-id: AAS-2026-11-09-sign-lang-379ffbdd642c-01
reviewed-boundary: "f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba"
---

# sign-lang epistemic report

## Source-and-claim boundary

The question is whether SIGN's governed knowledge notation and preparation toolchain acquire, derive, check and authorize truth-apt content, and how those results reach consequential consumers. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register), not redeclared here. This is a complete artifact, partial loop, ending before external ingestion and model consumption. No observed run or causal experiment was supplied. Implementation deductions below are not target executions.

The declared agent contract is [RT-CLM-agent-contract](runtime.md#rt-clm-agent-contract). The additional claims about inference, constraints and provenance are [EPI-CLM-governed-inference](#epi-clm-governed-inference) and [EPI-CLM-provenance-authority](#epi-clm-provenance-authority). SIGN expresses both truth-apt domain statements and non-truth-apt instructions; their common file format does not give them common warrant.

| Entry point or operation | Source path, SRC-1 | Coverage and limits |
|---|---|---|
| CLI dispatch: validate, compile, coverage, drift, diff, import | `validator/bin/sign.js` | Direct full read confirms all six dispatch branches; supplied routes below cover their consumers. No additional CLI operation was found in this file. |
| Parser and structural checks | `validator/src/parse.js`, `validator/src/rules.js` | Direct full reads; [EPI-RTE-infer-check](#epi-rte-infer-check) separates an evaluator from compile disposition. Other checks remain in [RT-RTE-validate-source](runtime.md#rt-rte-validate-source) and [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon). |
| Compile, index, bundle, manifest and hash | `validator/src/compile.js` | Direct full read; [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon). File-level bundle selection and rereading prevent a document-level exclusion or snapshot guarantee. |
| Validation orchestration | `validator/src/validate.js` | Supplied [RT-RTE-validate-source](runtime.md#rt-rte-validate-source), not directly reread; zero-document success limits meaning of a CLI pass. |
| Coverage and source drift | `validator/src/coverage.js`, `validator/src/drift.js` | Supplied [RT-RTE-source-signals](runtime.md#rt-rte-source-signals), with directly inspected CLI consumer. No inference of semantic correctness or completed review from either metric. |
| Change classification | `validator/src/diff.js` | Direct full read plus CLI consumer; [RT-RTE-corpus-diff](runtime.md#rt-rte-corpus-diff). Selected textual signatures, not a semantic equivalence evaluator. |
| Import | `validator/bin/sign.js` | Direct dispatch read; [RT-RTE-import-delegation](runtime.md#rt-rte-import-delegation). External importer excluded; prevents assessment of its transformations and admission. |
| Intended delivery, human authority and rule execution | `README.md`, `spec/skill-reference.md`, `spec/sign-v1.0.md` | First two read fully; main spec read at provenance/inference sections. [RT-BAP-canon-guidance](runtime.md#rt-bap-canon-guidance), [EPI-CLM-governed-inference](#epi-clm-governed-inference), [EPI-CLM-provenance-authority](#epi-clm-provenance-authority). Host retrieval and constraint enforcement remain outside source. |
| Shipped corpus | `.agent/sign/src/SL-ARCH.sign`, `.agent/sign/src/SL-DEPS.sign`, `.agent/sign/src/SL-OVERVIEW.sign`, `.agent/sign/src/SL-STANDARDS.sign` | Direct full reads; [EPI-OBJ-sign-content](#epi-obj-sign-content). Availability is not a trace of generation, checking or human acceptance. |
| Worked rule and provenance examples | `examples/04-inference-rules.sign`, `examples/05-crosswalk-provenance.sign` | Direct full reads; [EPI-OBJ-infer](#epi-obj-infer), [EPI-OBJ-edge-provenance](#epi-obj-edge-provenance). Illustrations, not observed derivations or reviews. |
| Editor contributions | `editor-support/vscode/package.json` | Direct full manifest read: declarative language/grammar/icon contributions, no registered execution command or extension entry point here. Highlighting correctness unassessed. |
| CI and tests | `.github/workflows/ci.yml`, `validator/package.json`, `validator/test/` | Supplied runtime wiring only; test bodies not inspected. Prevents claims about test coverage, passing tests or evaluated agent reasoning. |
| Remaining specification, examples, proposals and editor files | `spec/`, `examples/`, `proposals/`, `editor-support/` | Available but not exhaustively inspected; prevents exhaustive language/doctrine reconciliation, not the narrower conclusions on inspected toolchain. No system-complete negative is asserted. |

Missing host code prevents assessing model choice, parameters, model adherence, retrieval scope and action enforcement. Missing importer code prevents classifying its imported content or source warrant. Missing run/review evidence prevents attributing creation, acceptance or benefit to the supplied corpus. None of these gaps is evidence that an external deployment lacks those capabilities.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-sign-content](#epi-obj-sign-content) | see record | see record | SRC-1, `.agent/sign/src/SL-ARCH.sign` | see record |
| [EPI-OBJ-infer](#epi-obj-infer) | see record | see record | SRC-1, `examples/04-inference-rules.sign` | see record |
| [EPI-OBJ-edge-provenance](#epi-obj-edge-provenance) | see record | see record | SRC-1, `examples/05-crosswalk-provenance.sign` | see record |
| [EPI-OBJ-canon-index](#epi-obj-canon-index) | see record | see record | SRC-1, `validator/src/compile.js` | see record |
| [EPI-OBJ-canon-bundle](#epi-obj-canon-bundle) | see record | see record | SRC-1, `validator/src/compile.js` | see record |
| [EPI-OBJ-canon-manifest](#epi-obj-canon-manifest) | see record | see record | SRC-1, `validator/src/compile.js` | see record |

## Authority-route ledger

Each compact entry is one function, not a declaration of another route. Repeated route citations identify separate functions within the supplied route; declaring records retain ownership of implementation details. Architectural status here is independent of activation.

Route ID: [EPI-RTE-infer-check](#epi-rte-infer-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-infer](#epi-obj-infer)
Content/update relation: no content change
Transition or check target: see route record.
Evaluator/condition and domain: see route record.
Activation and timing: see route record.
Possible or observed result: see route record.
Implemented force: see route record.
Epistemic authority and scope: see route record.
Operational authority: see route record.
Behavioral-authority path: see route record.
Evidence source ID and local anchor: SRC-1, `validator/src/rules.js`.
Claim IDs: [EPI-CLM-governed-inference](#epi-clm-governed-inference).
Mismatch marker: completeness is not derivation or truth checking.
Gap/limit: see route record.

Route ID: [RT-RTE-validate-source](runtime.md#rt-rte-validate-source)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-sign-content](#epi-obj-sign-content)
Content/update relation: no content change
Transition or check target: see route record.
Evaluator/condition and domain: see route record; structural program checks, not source-truth evaluation.
Activation and timing: see route record.
Possible or observed result: see route record.
Implemented force: see route record.
Epistemic authority and scope: a result addresses recognized syntax and structural rules only; the supplied zero-document case prevents treating success as absence of parse diagnostics.
Operational authority: see route record.
Behavioral-authority path: CLI diagnostics and status are consumed by caller; no compulsory semantic review follows.
Evidence source ID and local anchor: SRC-1, `validator/src/validate.js` (supplied route).
Claim IDs: [EPI-CLM-governed-inference](#epi-clm-governed-inference).
Mismatch marker: pass is not epistemic acceptance.
Gap/limit: see route record.

Route ID: [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-sign-content](#epi-obj-sign-content)
Content/update relation: no content change
Transition or check target: recognized parse/rule errors before artifact writes; see route record.
Evaluator/condition and domain: fixed software veto, not an evidence-consuming acceptance of domain propositions; see route record.
Activation and timing: see route record.
Possible or observed result: abort or continue; see route record.
Implemented force: enforcing on this compiler path; warnings permit continuation.
Epistemic authority and scope: structural admissibility only, not human endorsement or semantic truth.
Operational authority: permits the compiler to construct and write artifacts, or blocks that invocation's writes; see route record.
Behavioral-authority path: compiler consumes diagnostic arrays in a pre-write branch; enforcing for this call, not external actions.
Evidence source ID and local anchor: SRC-1, `validator/src/compile.js`.
Claim IDs: [EPI-CLM-provenance-authority](#epi-clm-provenance-authority), [EPI-CLM-governed-inference](#epi-clm-governed-inference).
Mismatch marker: admission does not implement human provenance review.
Gap/limit: see route record, including nontransactional writes and mutable-input reread.

Route ID: [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-sign-content](#epi-obj-sign-content) → [EPI-OBJ-canon-index](#epi-obj-canon-index), [EPI-OBJ-canon-bundle](#epi-obj-canon-bundle)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: source projection and raw-file assembly; see route record.
Evaluator/condition and domain: not an evaluator of source propositions; fixed active selection and formatting rules.
Activation and timing: see route record.
Possible or observed result: see route record; possible outputs, no observed build.
Implemented force: see route record.
Epistemic authority and scope: bundle retains supplied words under stable input; index is a lossy locator, not substitute authority for rule scope or anchor exclusions. No proposition is warranted just because it survived projection.
Operational authority: prepares possible later context; host loading remains unwired here.
Behavioral-authority path: see [RT-BAP-canon-guidance](runtime.md#rt-bap-canon-guidance) for intended, not implemented model consumption.
Evidence source ID and local anchor: SRC-1, `validator/src/compile.js`.
Claim IDs: [RT-CLM-agent-contract](runtime.md#rt-clm-agent-contract).
Mismatch marker: active identity filtering is not per-document bundle filtering.
Gap/limit: see route record and output object records.

Route ID: [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-canon-index](#epi-obj-canon-index), [EPI-OBJ-canon-bundle](#epi-obj-canon-bundle), [EPI-OBJ-canon-manifest](#epi-obj-canon-manifest)
Content/update relation: no content change
Transition or check target: construction to persisted files; see route record.
Evaluator/condition and domain: filesystem write, not claim acceptance.
Activation and timing: see route record.
Possible or observed result: see route record.
Implemented force: see route record.
Epistemic authority and scope: persistence and checksum supply no endorsement or authenticated lineage.
Operational authority: files available to later consumers, not demonstrated model activation.
Behavioral-authority path: see route record and [RT-BAP-canon-guidance](runtime.md#rt-bap-canon-guidance).
Evidence source ID and local anchor: SRC-1, `validator/src/compile.js`.
Claim IDs: [RT-CLM-agent-contract](runtime.md#rt-clm-agent-contract).
Mismatch marker: retention is not lifecycle integration after epistemic acceptance.
Gap/limit: no such acceptance decision or later host use supplied.

Route ID: [RT-RTE-source-signals](runtime.md#rt-rte-source-signals)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-sign-content](#epi-obj-sign-content), its anchor bindings to repository files
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: current path coverage and Git-change intersection, not correctness of a governing statement.
Evaluator/condition and domain: see route record; deterministic set/glob computations under their selected current-file universe and Git comparison.
Activation and timing: see route record.
Possible or observed result: see route record.
Implemented force: see route record; CLI prints metrics/signals, drift uses status, coverage exits zero.
Epistemic authority and scope: warrants only the implemented comparisons under supplied filesystem/Git premises; completeness and governed-content accuracy do not follow.
Operational authority: caller can use signals for review; no automatic revision or withdrawal.
Behavioral-authority path: caller receives output/status for this invocation; further review consumer external.
Evidence source ID and local anchor: SRC-1, `validator/src/coverage.js`, `validator/src/drift.js` (supplied); `validator/bin/sign.js` (direct).
Claim IDs: [RT-CLM-agent-contract](runtime.md#rt-clm-agent-contract).
Mismatch marker: freshness signal is not renewed acceptance.
Gap/limit: see route record; premises not independently warranted by a run.

Route ID: [RT-RTE-corpus-diff](runtime.md#rt-rte-corpus-diff)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-sign-content](#epi-obj-sign-content)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: textual signature and anchor-set differences; see route record.
Evaluator/condition and domain: fixed comparison program; its labels denote its comparison domain, not verified semantic equivalence.
Activation and timing: see route record.
Possible or observed result: see route record.
Implemented force: CLI exits nonzero for meaning-breaking, but does not itself reject a content edit or merge.
Epistemic authority and scope: only implemented textual/set classification; not preserved source truth, deletion completeness or version compliance.
Operational authority: see route record.
Behavioral-authority path: see route record; advisory printed class and process status to caller for this invocation.
Evidence source ID and local anchor: SRC-1, `validator/src/diff.js`, `validator/bin/sign.js`.
Claim IDs: [EPI-CLM-provenance-authority](#epi-clm-provenance-authority).
Mismatch marker: a change to edge provenance alone can be called additive.
Gap/limit: see route record and concrete source deduction below.

Route ID: [RT-RTE-import-delegation](runtime.md#rt-rte-import-delegation)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: not determinable for external import output
Content/update relation: no content change
Transition or check target: importer executable discovery and process dispatch only, not import semantics.
Evaluator/condition and domain: see route record.
Activation and timing: see route record.
Possible or observed result: see route record.
Implemented force: see route record.
Epistemic authority and scope: none established for the external content; acquisition classification and source warrant unresolved beyond dispatch.
Operational authority: see route record.
Behavioral-authority path: see route record.
Evidence source ID and local anchor: SRC-1, `validator/bin/sign.js`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: excluded importer prevents examination of its evaluator, provenance, retention and consumers.

Route ID: [RT-BAP-canon-guidance](runtime.md#rt-bap-canon-guidance), [EPI-CLM-governed-inference](#epi-clm-governed-inference)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-infer](#epi-obj-infer), [EPI-OBJ-edge-provenance](#epi-obj-edge-provenance), [EPI-OBJ-canon-bundle](#epi-obj-canon-bundle)
Content/update relation: no content change
Transition or check target: intended host delivery and agent reliance, not an inspected evaluator.
Evaluator/condition and domain: external agent/ontology layer unspecified; not determinable as an implemented rule executor within this artifact.
Activation and timing: see behavioral-authority record; intended on-demand full text after index orientation.
Possible or observed result: intended constraint-conforming decisions and derivations; none observed.
Implemented force: no implemented host force established within boundary.
Epistemic authority and scope: source claims governed commitments and revisable inferences; actual granted reliance unresolved.
Operational authority: intended model guidance, not tool-action enforcement by compiler.
Behavioral-authority path: see [RT-BAP-canon-guidance](runtime.md#rt-bap-canon-guidance).
Evidence source ID and local anchor: SRC-1, `README.md`, `spec/sign-v1.0.md`.
Claim IDs: [RT-CLM-agent-contract](runtime.md#rt-clm-agent-contract), [EPI-CLM-governed-inference](#epi-clm-governed-inference), [EPI-CLM-provenance-authority](#epi-clm-provenance-authority).
Mismatch marker: expressed rules do not establish checked inference or acceptance.
Gap/limit: no supplied premises, resulting domain fact, evaluator decision or later use trace.

Concrete comparison deduction: take before text `@edges skill:a\n  skill:a depends_on skill:b [type:inferred]` and after text replacing only `type:inferred` with `type:asserted`. In inspected `meaningSignature`, `edges` is outside `MEANING_SIGILS`, so both signatures are empty. Neither text supplies an anchor; `anchorOf` returns null for each. Dropped includes and added excludes are empty; `classifyDocChange` returns additive. This is a source-level deduction, not an executed test. It falsifies the stronger interpretation that this classifier detects every epistemically consequential change. It does not demonstrate an actual unauthorized promotion. SRC-1, `validator/src/diff.js`; see [RT-RTE-corpus-diff](runtime.md#rt-rte-corpus-diff).

> const MEANING_SIGILS = ['def', 'include', 'exclude', 'rules', 'rel', 'constraints', 'infer'];
> --- `validator/src/diff.js`

> return { changeClass: 'additive', droppedPatterns: [] };
> --- `validator/src/diff.js`

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-agent-contract](runtime.md#rt-clm-agent-contract) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon) | none supplied | No causal comparison; external loading not shipped | Context artifacts can be prepared; source does not establish their successful use | Runtime token savings and agent compliance unresolved |
| [EPI-CLM-governed-inference](#epi-clm-governed-inference) | see record | SRC-1, `spec/sign-v1.0.md`; doctrine/design | see record | [EPI-RTE-infer-check](#epi-rte-infer-check), [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon) | none supplied | No supplied graph-state/result pair or host evaluator | Rules and constraints are expressed and retained; field presence is checked | Does not establish a derivation engine, entailed domain conclusion or enforced domain constraint |
| [EPI-CLM-provenance-authority](#epi-clm-provenance-authority) | see record | SRC-1, `spec/skill-reference.md`, `spec/sign-v1.0.md`; doctrine/design | see record, including differing asserted conventions | [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon), [RT-RTE-corpus-diff](runtime.md#rt-rte-corpus-diff) | none supplied | No evidence-consuming human approval/review trace | Raw provenance can survive bundling; syntax is not authenticated history | Prefix checks do not verify human source; edge-property promotion can evade meaning-breaking classification |

## Bounded conclusion

SIGN's inspected implementation prepares retained context and structural diagnostics. Compilation can reject recognized structural errors before writing, but that license is limited to the implemented checks. It does not accept a domain proposition against evidence for an intended use. A compiler pass, active status, asserted label and checksum each have different meanings; none supplies that missing decision. See [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon), [EPI-RTE-infer-check](#epi-rte-infer-check), [EPI-CLM-provenance-authority](#epi-clm-provenance-authority).

The index reshapes and omits authored material; full-bundle assembly preserves contributing raw file text under stable inputs, including supplied provenance labels, but not authenticated source warrant. The external importer is not assessed, so no conclusion about its acquired claims or warrant follows. No observed acquired or produced accepted ampliative claim is established. Retained artifacts are not evidence of acceptance followed by lifecycle integration. See [EPI-OBJ-canon-index](#epi-obj-canon-index), [EPI-OBJ-canon-bundle](#epi-obj-canon-bundle), [RT-RTE-import-delegation](runtime.md#rt-rte-import-delegation).

Coverage, drift and diff derive bounded reports from filesystem/Git/text premises. Their consequences are output and process status, not automatic correction, withdrawal or reacceptance of governed claims. Their implemented comparison results can be deduced, but those premises and downstream use are not independently evidenced by a run. See [RT-RTE-source-signals](runtime.md#rt-rte-source-signals), [RT-RTE-corpus-diff](runtime.md#rt-rte-corpus-diff).

Inference and constraint semantics are declared for the external consumer. Neither evaluating domain premises nor consuming a derived fact is implemented by the inspected compiler/parser/rules path. The checks do establish a useful narrower capability: machine-enforced structural conditions for artifact preparation. Distributed-parametric inference, parameter updates, reflective criticism, learned improvement and autonomous revision are not inferable from these deterministic routes or from the static corpus. There is no inspected trace-fed policy adaptation in these routes; this is not a system-wide denial about excluded hosts. The claimed consumer path remains [RT-BAP-canon-guidance](runtime.md#rt-bap-canon-guidance), not observed behavioral change.

## Shared records

### Operative objects

#### EPI-OBJ-sign-content
Label: SIGN source content

Distinct identity: source content consumed by [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon) and [RT-RTE-validate-source](runtime.md#rt-rte-validate-source), not the executing [RT-CMP-validator](runtime.md#rt-cmp-validator). No supplied object counterpart.

Identity/form/substrate: authored `.sign` files on disk. Domain definitions and descriptive prose are truth-apt natural-language content; imperative rules are policy instructions, not truth-apt merely because they are in SIGN. Headers and link IDs have symbolic fixed-rule compiler consumers. The shipped four-document corpus includes assertions about the toolchain and instructions for maintainers; the corpus is a candidate instance, not a traced accepted output. SRC-1, `.agent/sign/src/SL-ARCH.sign`, `.agent/sign/src/SL-STANDARDS.sign`, `.agent/sign/src/SL-OVERVIEW.sign`, `.agent/sign/src/SL-DEPS.sign`; doctrine/design for desired authoring and implementation evidence from `validator/src/parse.js` for parsed fields. Parts with different checks are declared below. Missing authorship/review trace prevents assigning actual human acceptance.

> Regex-based validator and compiler for SIGN v1.0 documents. The toolchain is
>   dependency-free (zero npm dependencies) and runs on Node.js >=18. It provides six
>   CLI commands: validate, compile, coverage, drift, diff, and import.
> --- `.agent/sign/src/SL-ARCH.sign`

> 6. Parse-validate separation: parse.js produces structured objects; rules.js checks
>      them; validate.js orchestrates; compile.js builds output artifacts
> --- `.agent/sign/src/SL-STANDARDS.sign`

#### EPI-OBJ-infer
Label: infer blocks

Part of: [EPI-OBJ-sign-content](#epi-obj-sign-content)

Identity/form/substrate: rule text in source files and raw bundles; the parser reduces each block to ID and Boolean field-presence flags in transient symbolic objects. The conditional relation can express a truth-apt rule over a domain; its example consequent is not evidence of an actual derived skill fact. A confidence string does not individuate checked premises. Claimed role: graph-state inference. Actual inspected consumer: completeness checks, not rule evaluation. SRC-1, `examples/04-inference-rules.sign` (doctrine/design), `validator/src/parse.js` (implementation).

> @infer skill-trajectory-eroding
>   applies-to: skill
>   when: skill.lifecycleStatus = Declining
>   and: skill.AIImpactCategory = Automated
>   then: skill.trajectorySignal = Eroding
>   confidence: derived
>   src: ontology-rule-007
> --- `examples/04-inference-rules.sign`

> const fields = { when: false, then: false, confidence: false, src: false, appliesTo: false };
> --- `validator/src/parse.js`

#### EPI-OBJ-edge-provenance
Label: edges provenance properties

Part of: [EPI-OBJ-sign-content](#epi-obj-sign-content)

Identity/form/substrate: edge claims and property-bag text in `.sign` files/raw bundles. Domain relations and histories are potentially truth-apt; parser-consumed subject/predicate/target and rule/cluster reference strings are symbolic. Provenance history receives meaning through intended human/model interpretation, not an authenticated review log. Distinct from infer blocks: edge field values, claimed review history and consumer are different. Claimed role is tracking assertion, inference, review and validation. SRC-1, `examples/05-crosswalk-provenance.sign` (doctrine/design), `validator/src/parse.js` (implementation). The parser's edge result does not retain provenance/status/confidence properties as checked values. Example labels do not establish that the named SME panel or O*NET actually reviewed the claim.

> skill:workforce-planning depends_on skill:data-analysis
>     [str:0.8, conf:high, status:validated, type:asserted,
>      provenance:inferred:relationship-miner-v2 -> reviewed:sme-panel-2026Q1 -> validated:onet]
> --- `examples/05-crosswalk-provenance.sign`

> return { subject, predicate, target };
> --- `validator/src/parse.js`

#### EPI-OBJ-canon-index
Label: canon-index

Distinct identity: output projection of [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon), not source content or validator component. No supplied object counterpart. Form/substrate: symbolic document IDs/links and natural-language summaries in `canon-index.sign` on disk. Claimed role: orientation/locator, not complete rule authority. Summary truth remains inherited from unverified authored text. Omitted rule bodies and exclusions cannot be reconstructed from the index alone. SRC-1, `validator/src/compile.js` implementation, with intended consumption in [RT-BAP-canon-guidance](runtime.md#rt-bap-canon-guidance).

> // Layer 1 has a hard token budget (spec §8). An @anchor block is summarised into the index,
> // never copied whole: excludes are dropped (Layer 1 is a locator, not an authority) and the
> // include list is capped. (RFC §1.4)
> const INDEX_ANCHOR_MAX = 4;
> --- `validator/src/compile.js`

#### EPI-OBJ-canon-bundle
Label: canon-bundle

Distinct identity: raw-file output of [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon), separate from the lossy index. No supplied object counterpart. Form/substrate: source-native natural-language content and symbolic sigils in `canon-bundle.sign` on disk. Claimed role: full documents for later retrieval. Its warrant remains that of supplied content; no source authentication is added. Minimum implementation evidence, selection/reread and non-active-file-part caveat are supplied by that route (SRC-1, `validator/src/compile.js`). Rereading after validation without stable inputs can break correspondence between checked projection and written raw text; no snapshot or rollback is established.

#### EPI-OBJ-canon-manifest
Label: canon-manifest and checksum

Distinct identity: build metadata/hash outputs of [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon), not domain propositions in the index/bundle. No supplied object counterpart. Form/substrate: symbolic JSON and hexadecimal strings on disk. Content is truth-apt only about the assembled bytes, selected document metadata and build time; hash does not establish author identity, domain truth or a checked deployment. Claimed role: artifact integrity/identification. SRC-1, `validator/src/compile.js` implementation; no downstream verification consumer supplied.

> const sha256 = crypto.createHash('sha256').update(bundleContent, 'utf8').digest('hex');
>   const shortSha = sha256.slice(0, 6);
> --- `validator/src/compile.js`

### Routes

#### EPI-RTE-infer-check
Label: Infer completeness check

Part of: [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon)

This is the check subroute, not duplicate disposition. The same check is reused in [RT-RTE-validate-source](runtime.md#rt-rte-validate-source). Endpoints: parsed `doc.infers` → `checkInferCompleteness` → error list → `runAllRules` aggregate → compiler pre-write branch or validate diagnostics. Owner: deterministic code. Context/state/action effects: transient field-presence diagnostics; no rule execution or claim revision. SRC-1, `validator/src/parse.js`, `validator/src/rules.js`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: errors for absent required prefixes, no warnings from this checker.
- Later read-back: inapplicable — no retained evaluation or changed source is written by this checker.
- Delegated visibility: inapplicable — no human or model worker is invoked.
- Selection predicate: each parsed infer block in each parsed document passed to runAllRules.
- Invalidation or expiry: inapplicable — result computed per call with no retained verdict.
- Activation or effect: errors join aggregate and can block compilation; no observed execution or downstream behavior supplied.
- Evidence limits: prefix presence is not populated-field validity, source authentication, rule entailment, premise truth or accepted domain conclusion.

Check target/domain: presence of `when:`, `then:`, `confidence:`, `src:` prefixes in parsed infer blocks. Evaluator: Boolean tests, not an external truth oracle. Possible result: missing-field error or empty errors. Force: enforcing only through the compiler error consumer, diagnostic on validate; zero-document validate caveat belongs to supplied route. Epistemic authority: at most completeness of these recognized fields. Operational authority/behavioral path: checker → aggregate error array → compiler pre-write branch, enforcing for this call; no license to promote inferred facts to asserted. No human acceptance criterion, intended-use decision or evidence-consuming domain judgment is represented. It is not a diagnosis/candidate-selection route: no proposal is chosen, and source authorship remains external.

> if (!infer.when)       missing.push('when:');
>     if (!infer.then)       missing.push('then:');
>     if (!infer.confidence) missing.push('confidence:');
>     if (!infer.src)        missing.push('src:');
> --- `validator/src/rules.js`

> if (t.startsWith('src:'))        fields.src = true;
> --- `validator/src/parse.js`

The counterexample to a stronger human-provenance guarantee is direct: even an empty `src:` satisfies this parser Boolean; `confidence:` values and source identities are not examined by this checker. General constraint bodies have no corresponding evaluation case in inspected `processBlock`. This bounded implementation claim does not deny external enforcement.

### Claims

#### EPI-CLM-governed-inference
Label: Governed inference and constraints

Distinct identity: specific inference/constraint warrant within the broader [RT-CLM-agent-contract](runtime.md#rt-clm-agent-contract), which concerns delivery. Claimed operation: rules derive new graph facts and constraints govern agent decisions. SRC-1, `spec/sign-v1.0.md`, `examples/04-inference-rules.sign`, doctrine/design. Operation unobserved. Inspected implementation expresses and checks field structure, not premise evaluation. Intended rule theories are locally inspectable as text, but the supplied example is not a trace of consumption, criticism or iteration; those theory-builder properties are not established by its notation.

> Inference rules express the governed logic that derives new facts from graph state. Constraints express the structural rules agents must enforce. Together they give agents the reasoning layer — not just the data, but what it means and what follows from it.
> --- `spec/sign-v1.0.md`

#### EPI-CLM-provenance-authority
Label: Provenance authority and promotion

Distinct identity: authority/promotion claim rather than the delivery claim [RT-CLM-agent-contract](runtime.md#rt-clm-agent-contract). Claimed operation: asserted content has human authority, inference stays marked until human review; provenance chains document derivation and validation. SRC-1, `spec/skill-reference.md`, `spec/sign-v1.0.md`, doctrine/design. No corresponding human review operation is established in inspected CLI/parser/rules/compiler. The source itself qualifies a universal human-only reading: main specification permits human or expert-system assertion, and describes a proposed machine-drafted convention allowing mechanically verifiable asserted facts. These differences limit the claim; they are not silently normalized into one enforced rule.

> `confidence: asserted` — validated by human authority (requires `src:` with human reviewer)
> --- `spec/skill-reference.md`

> LLM-estimated facts must carry `confidence: derived` or `confidence: estimated`
> and cannot be promoted to `confidence: asserted` without human review.
> --- `spec/skill-reference.md`

> The `type:asserted` / `type:inferred` distinction marks the epistemic status of every edge — explicitly declared by a human or expert system vs derived by an inference rule. Agents treat these differently: asserted edges are governed commitments, inferred edges are soft and revisable.
> --- `spec/sign-v1.0.md`

> > `type:asserted` — only mechanically-verifiable facts (e.g. `@edges` from csproj,
> > `[type:asserted, src:csproj]`) may. Such documents carry a provisional `machine-drafted`
> > landing-status token in the `@doc` bag until a human landing step clears it. See
> > `proposals/2026-07-codebase-canon-reinforcement.md` (open decisions D-1/D-2).
> --- `spec/sign-v1.0.md`
