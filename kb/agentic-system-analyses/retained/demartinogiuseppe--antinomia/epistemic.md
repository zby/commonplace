---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Antinomia epistemic routes: model proposals, human admission, structural checks and retained withdrawal at the frozen plugin revision."
run-id: AAS-2026-11-08-antinomia-19694628edc2-01
reviewed-boundary: "6fafd01082fbecb2a18803500a1abe70a2bdc9f4"
---

# Antinomia epistemic report

## Source-and-claim boundary

Can this plugin's retained notes and model judgments acquire warrant, or do they organize proposals for human reflection? The functional boundary and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identity is its [Source register](boundary.md#source-register), SRC-1. The inspected revision supplies implementation and doctrine/design, not observed execution or causal experiments. The external host, provider weights and actual user decisions remain uninspected. Thus human approval is a wired opportunity, not evidence-consuming acceptance demonstrated against a criterion.

Consequential claims are [EPI-CLM-reflective-practice](#epi-clm-reflective-practice), [EPI-CLM-source-fidelity](#epi-clm-source-fidelity), [EPI-CLM-collapse-impact](#epi-clm-collapse-impact), [EPI-CLM-hunter-measure](#epi-clm-hunter-measure) and [RT-CLM-friction-scope](runtime.md#rt-clm-friction-scope). No supplied run establishes their efficacy. No supersession is needed: the supplied runtime remains a useful container account. Added maintenance coverage below qualifies how much an origin or defeated label warrants.

| Entry point or operation | SRC-1 source path | Coverage and conclusion limit |
|---|---|---|
| Command dispatch and delete hook | `main.ts` | Direct command-ID search; direct reads of delete callback, origin-repair/merge registration and mutation methods. No CLI or model tool dispatcher identified on this surface; Obsidian commands are the shipped entry points. |
| Free input, guided/empty notes, PDF and YouTube | `flows/freeInput.ts`, `flows/pdfIngest.ts`, `flows/youtubeFetch.ts` | Supplied [RT-RTE-free-input](runtime.md#rt-rte-free-input), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); not independently reread in full. Source fidelity and end-to-end operation unestablished. |
| Hunter, focused Hunter, rejection and undismiss | `flows/hunter.ts`, `ai/parseResponse.ts` | Direct full Hunter read and normalization read; [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan), [RT-RTE-pair-dismissal](runtime.md#rt-rte-pair-dismissal). Structural checks do not check contradiction truth. |
| Elevation and principle mapping | `flows/elevation.ts`, `flows/presuppositionMap.ts`, `ai/prompts.ts` | Supplied [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission); direct prompt and impact/delete-sync reads. No observed empirical rule test. |
| Tension A/B mapping | `flows/presupposti.ts` | Direct full flow read; [EPI-RTE-inline-assumptions](#epi-rte-inline-assumptions). |
| Classification, manual type/ignore/title, resolution, archive, link | `main.ts`, `flows/titleProposal.ts` | Direct classification/type/ignore/resolution/archive read; title/link account partly supplied runtime. [EPI-RTE-note-disposition](#epi-rte-note-disposition); title and general link internals not independently assessed, preventing a complete semantic-preservation verdict. |
| Schema migration and restore | `flows/migration.ts` | Supplied [RT-RTE-schema-migration](runtime.md#rt-rte-schema-migration); exact migration rewrite semantics not independently assessed. |
| Retroactive origin creation, orphan repair, merge | `main.ts` | Direct implementation reads; [EPI-RTE-origin-maintenance](#epi-rte-origin-maintenance). |
| Impact and undermining | `flows/presuppositionMap.ts`, `modals/CollapseImpactModal.ts` | Direct reads; [EPI-RTE-collapse-review](#epi-rte-collapse-review). Graph styling internals not fully inspected; no automatic principle rejection inferred. |
| Vault audit | `views/AuditVaultView.ts` | Direct full read; [EPI-RTE-vault-audit](#epi-rte-vault-audit). |
| Seeded evaluation, example creation/deletion | `flows/exampleVault.ts` | Direct key read; [EPI-CLM-hunter-measure](#epi-clm-hunter-measure). Seed creation/deletion bodies not fully reread; no executed score or effect on production settings established. |
| Prompt friction, provider requests | `core/aiFriction.ts`, `ai/callAI.ts`, `modals/FrictionCard.ts` | Direct limitation/suffix read plus supplied [RT-RTE-model-request](runtime.md#rt-rte-model-request), [RT-CLM-friction-scope](runtime.md#rt-clm-friction-scope). Self-confidence is not an external evaluator. |
| Dashboard, lists, graph, dependency map, guidance/tutorial | `views/`, `modals/GuidanceModal.ts`, `modals/TutorialModal.ts` | Supplied boundary coverage, with only audit and impact consumers deeply inspected here. Remaining advice/rendering paths prevent a system-complete negative about all possible human guidance. |
| Tests and development hooks | `tests/`, `scripts/`, `.github/` | Supplied boundary only; not executed or deeply inspected here. They cannot establish live accuracy or causal benefit. |

The table distinguishes accessible but uninspected implementation from external access limits. The bounded conclusions below concern the traced routes, not every possible interpretation by a user. Provider inference is opaque; [RT-CMP-model](runtime.md#rt-cmp-model) owns version/fixity findings. There is no basis here to infer a parameter update or exclude provider-side changes.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-note-content](#epi-obj-note-content) | See record | See record | SRC-1 `README.md`; see record | Desires and action prescriptions are not necessarily truth-apt; factual clauses can be. |
| [EPI-OBJ-hunter-pairs](#epi-obj-hunter-pairs) | See record | See record | SRC-1 `flows/hunter.ts`; see record | Confidence is not calibrated warrant. |
| [EPI-OBJ-principle-rules](#epi-obj-principle-rules) | See record | See record | SRC-1 `ai/prompts.ts`; see record | Conditional applicability can be truth-apt; prescriptions alone are not facts. |
| [EPI-OBJ-assumption-text](#epi-obj-assumption-text) | See record | See record | SRC-1 `ai/prompts.ts`; see record | Model-inferred dependency can be wrong. |
| [EPI-OBJ-note-markers](#epi-obj-note-markers) | See record | See record | SRC-1 `main.ts`; see record | Symbolic status is operative without substantiating its ordinary-language interpretation. |
| [RT-CMP-model](runtime.md#rt-cmp-model) | Not determinable internally | See record | SRC-1 `ai/callAI.ts`; see record | No accessible weights, training lineage or provider-side evaluator. |

## Authority-route ledger

Fields owned by cited records are intentionally not duplicated. Multiple ledger entries may overlay different functions of one canonical route. All architectural statuses below concern inspected implementation, including implementation evidence supplied by runtime; operation remains unobserved.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | content transformation | implemented | [EPI-OBJ-note-content](#epi-obj-note-content) | truth-apt transformation: acquisition/import | External PDF/transcript input | See route | See route | See route | See route | Source warrant unknown; transport/reference is not endorsement | See route | See route | SRC-1 `flows/pdfIngest.ts` | [EPI-CLM-source-fidelity](#epi-clm-source-fidelity) | none | Extraction model subsequently changes representation. |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | content transformation | implemented | [EPI-OBJ-note-content](#epi-obj-note-content) | truth-apt transformation: indeterminate | Model concept text | See route | See route | See route | See route | Faithful extraction requested, not checked entailment | See route | See route | SRC-1 `ai/prompts.ts` | [EPI-CLM-source-fidelity](#epi-clm-source-fidelity) | Fidelity unknown | May reshape or conjecture; no paired source/output instance supplied. |
| [RT-RTE-free-input](runtime.md#rt-rte-free-input) | content transformation | implemented | [EPI-OBJ-note-content](#epi-obj-note-content) | truth-apt transformation: indeterminate | Raw text to typed fields | See route | See route | See route | See route | Neither fidelity nor new truth licensed | See route | See route | SRC-1 `flows/freeInput.ts` | none | none | Need actual input/output and scope to distinguish reshaping from conjecture. |
| [RT-RTE-free-input](runtime.md#rt-rte-free-input), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | disposition/acceptance | implemented | [EPI-OBJ-note-content](#epi-obj-note-content) | no content change | Proposed fields/concepts for saving | See routes | See routes | See routes | See routes | Human permission to save; no required evidence-consuming truth criterion | See routes | See routes | SRC-1 `modals/ConceptsPreviewModal.ts` | [RT-CLM-friction-scope](runtime.md#rt-clm-friction-scope) | Admission is not epistemic acceptance | Human may perform additional checking; no record supplied. |
| [RT-RTE-free-input](runtime.md#rt-rte-free-input), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | retention | implemented | [EPI-OBJ-note-content](#epi-obj-note-content) | no content change | Submitted Markdown | See routes | See routes | See routes | See routes | Retention does not add warrant | See routes | See routes | SRC-1 `main.ts` | none | none | Partial writes possible; no accepted-claim integration inferred. |
| [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan) | operational admission/selection/consumption | implemented | [EPI-OBJ-note-content](#epi-obj-note-content) | truth-apt transformation: non-ampliative reshaping | Note subset/body prefixes | See route | See route | See route | See route | Restricted comparison input, not complete vault evidence | See route | See route | SRC-1 `flows/hunter.ts` | [EPI-CLM-reflective-practice](#epi-clm-reflective-practice) | none | Removed qualifiers can degrade warrant; no automatic body reload. |
| [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan) | content transformation | implemented | [EPI-OBJ-hunter-pairs](#epi-obj-hunter-pairs) | truth-apt transformation: indeterminate | Pair incompatibility description | See route | See route | See route | See route | Candidate judgment only; not checked derivation | See route | See route | SRC-1 `ai/prompts.ts` | [EPI-CLM-reflective-practice](#epi-clm-reflective-practice) | none | May follow explicit opposition or introduce interpretation; no output instance decides. |
| [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan) | check/evidence production | implemented | [EPI-OBJ-hunter-pairs](#epi-obj-hunter-pairs) | no content change | Basename membership, nonself, nonempty description, focus | See route | See route | See route | See route | Structural admissibility only; no contradiction or source-truth license | See route | See route | SRC-1 `flows/hunter.ts` | [EPI-CLM-reflective-practice](#epi-clm-reflective-practice) | none | An incorrect description between two real notes passes. |
| [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan) | disposition/acceptance | implemented | [EPI-OBJ-hunter-pairs](#epi-obj-hunter-pairs) | no content change | Structurally surviving output | See route | See route | See route | See route | Display admission, not truth acceptance | See route | See route | SRC-1 `flows/hunter.ts` | none | none | Parse repair fixes output shape, not semantics. |
| [RT-RTE-pair-dismissal](runtime.md#rt-rte-pair-dismissal) | retention | implemented | [EPI-OBJ-note-markers](#epi-obj-note-markers) | non-truth-apt policy/content update: suppress pair | User false-positive choice | See route | See route | See route | See route | Records human rejection, not its correctness | See route | See [RT-BAP-dismissal-filter](runtime.md#rt-bap-dismissal-filter) | SRC-1 `flows/hunter.ts` | none | none | No semantic reevaluation on note edits. |
| [RT-RTE-pair-dismissal](runtime.md#rt-rte-pair-dismissal) | behavior/policy adaptation | implemented | [EPI-OBJ-note-markers](#epi-obj-note-markers) | no content change | Later returned pair | See route | See route | See route | See route | No new knowledge license | See route | See [RT-BAP-dismissal-filter](runtime.md#rt-bap-dismissal-filter) | SRC-1 `flows/hunter.ts` | none | none | Source deduction: retained A→B suppresses A/B despite a changed description; undismiss allows it again. Not provider learning. |
| [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) | content transformation | implemented | [EPI-OBJ-principle-rules](#epi-obj-principle-rules) | truth-apt transformation: indeterminate | Tension to applicability/outcome proposal | See route | See route | See route | See route | Hypothesis guidance, not a checked consequence of A/B | See route | See route | SRC-1 `core/aiFriction.ts` | [EPI-CLM-reflective-practice](#epi-clm-reflective-practice) | none | Rules may contain non-truth-apt prescriptions; actual proposition instance absent. |
| [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) | disposition/acceptance | implemented | [EPI-OBJ-principle-rules](#epi-obj-principle-rules) | no content change | Edited rule for elevation | See route | See route | See route | See route | User endorsement untested against real cases | See route | See route | SRC-1 `flows/elevation.ts` | [RT-CLM-friction-scope](runtime.md#rt-clm-friction-scope) | No mandatory empirical acceptance | Origin preservation is not evidence of a successful resolution. |
| [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) | retention | implemented | [EPI-OBJ-principle-rules](#epi-obj-principle-rules) | no content change | Submitted principle and historical origin | See route | See route | See route | See route | No additional warrant | See route | See route | SRC-1 `flows/elevation.ts` | none | none | Persistence precedes any evidenced truth acceptance. |
| [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission) | content transformation | implemented | [EPI-OBJ-assumption-text](#epi-obj-assumption-text) | truth-apt transformation: indeterminate | Implicit/load-bearing assumption proposals | See route | See route | See route | See route | Proposed dependency and world claim, neither verified | See route | See route | SRC-1 `ai/prompts.ts` | [EPI-CLM-collapse-impact](#epi-clm-collapse-impact) | none | Plausibility is not necessity; existing titles are not full existing claims. |
| [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission) | disposition/acceptance | implemented | [EPI-OBJ-assumption-text](#epi-obj-assumption-text) | no content change | New/link/skip decisions | See route | See route | See route | See route | User link/content admission, not a required truth test | See route | See route | SRC-1 `modals/PresuppositionMapModal.ts` | [RT-CLM-friction-scope](runtime.md#rt-clm-friction-scope) | none | Similarity default does not prove semantic identity. |
| [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission) | retention | implemented | [EPI-OBJ-assumption-text](#epi-obj-assumption-text), [EPI-OBJ-note-markers](#epi-obj-note-markers) | no content change | Notes and bidirectional references | See route | See route | See route | See route | Stored assertion/dependency, not accepted knowledge integration | See route | See route | SRC-1 `flows/presuppositionMap.ts` | none | none | Integration in a graph is organizational; epistemic acceptance unestablished. |
| [EPI-RTE-inline-assumptions](#epi-rte-inline-assumptions) | content transformation | implemented | [EPI-OBJ-assumption-text](#epi-obj-assumption-text) | truth-apt transformation: indeterminate | See record | See record | See record | See record | See record | See record | See record | See record | SRC-1 `flows/presupposti.ts` | none | none | See record |
| [EPI-RTE-note-disposition](#epi-rte-note-disposition) | disposition/acceptance | implemented | [EPI-OBJ-note-markers](#epi-obj-note-markers) | non-truth-apt policy/content update: type/status admission | See record | See record | See record | See record | See record | See record | See record | See record | SRC-1 `main.ts` | [EPI-CLM-reflective-practice](#epi-clm-reflective-practice) | none | See record |
| [EPI-RTE-origin-maintenance](#epi-rte-origin-maintenance) | lineage/freshness/recovery | implemented | [EPI-OBJ-note-markers](#epi-obj-note-markers) | non-truth-apt policy/content update: origin reconstruction/redirect | See record | See record | See record | See record | See record | See record | See record | See record | SRC-1 `main.ts` | [EPI-CLM-reflective-practice](#epi-clm-reflective-practice) | Origin can be reconstructed | See record |
| [EPI-RTE-collapse-review](#epi-rte-collapse-review) | check/evidence production | implemented | [EPI-OBJ-note-markers](#epi-obj-note-markers) | truth-apt transformation: entailed derivation | See record | See record | See record | See record | See record | See record | See record | See record | SRC-1 `flows/presuppositionMap.ts` | [EPI-CLM-collapse-impact](#epi-clm-collapse-impact) | Graph incidence is not logical necessity | See record |
| [EPI-RTE-collapse-review](#epi-rte-collapse-review) | disposition/acceptance | implemented | [EPI-OBJ-note-markers](#epi-obj-note-markers) | non-truth-apt policy/content update: mark undermined | See record | See record | See record | See record | See record | See record | See record | See record | SRC-1 `modals/CollapseImpactModal.ts` | [EPI-CLM-collapse-impact](#epi-clm-collapse-impact) | none | No automatic principle withdrawal |
| [EPI-RTE-vault-audit](#epi-rte-vault-audit) | check/evidence production | implemented | [EPI-OBJ-note-content](#epi-obj-note-content) | no content change | See record | See record | See record | See record | See record | See record | See record | See record | SRC-1 `views/AuditVaultView.ts` | none | Health label is bounded | See record |
| [RT-RTE-schema-migration](runtime.md#rt-rte-schema-migration) | lineage/freshness/recovery | implemented | [EPI-OBJ-note-markers](#epi-obj-note-markers) | non-truth-apt policy/content update: schema rewrite/restore | See route | See route | See route | See route | See route | Schema compatibility only | See route | See route | SRC-1 `flows/migration.ts` | none | none | Restore is not semantic validation; direct migrateNote bypasses batch backup. |

No evidence-consuming epistemic acceptance or post-acceptance lifecycle integration is established for these candidates. This is not a claim that human users cannot test or integrate them outside the recorded routes. The positive counterexamples to a simplistic “nothing is evaluated” account are Hunter structural filtering, persistent human dismissal, deterministic dependency lookup and the vault audit. Their targets and domains differ from source truth.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-reflective-practice](#epi-clm-reflective-practice) | See record | SRC-1 `README.md`, doctrine/design | See record | [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [EPI-RTE-note-disposition](#epi-rte-note-disposition) | None supplied | No outcome or component comparison | Reflective proposals with human operational control | A defeated label does not demonstrate falsity; origin can be retroactive. |
| [EPI-CLM-source-fidelity](#epi-clm-source-fidelity) | See record | SRC-1 `ai/prompts.ts`, doctrine/design | See record | [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | None supplied | No paired output/fidelity evaluation | Fidelity is requested | Semantic preservation unknown. |
| [EPI-CLM-collapse-impact](#epi-clm-collapse-impact) | See record | SRC-1 `ai/prompts.ts`, `flows/exampleVault.ts`, doctrine/design | See record | [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission), [EPI-RTE-collapse-review](#epi-rte-collapse-review) | None supplied | Graph adjacency is not a test of necessity | Makes claimed dependency inspectable | “Collapse” exceeds deterministic lookup's license. |
| [EPI-CLM-hunter-measure](#epi-clm-hunter-measure) | See record | SRC-1 `flows/exampleVault.ts`, doctrine/design | See record | [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan) | None supplied | Curated sharp/subtle/noise cases; no intervention or component isolation | Human comparison key is available | Finding one subtle example cannot identify general reasoning capacity or blame a model rather than context selection. |
| [RT-CLM-friction-scope](runtime.md#rt-clm-friction-scope) | See record | SRC-1 `main.ts`, doctrine/design | See record | See record | None supplied | No measured effect on scrutiny | Local acknowledgment gate on named consumers | See record; acknowledgment itself consumes no independent truth evidence. |

## Bounded conclusion

Antinomia acquires text and retains editable typed notes. It supplies selected prefixes to a configured model and offers generated content for human admission. The ingest, free-input and implicit-assumption transformations have indeterminate semantic relations without paired inputs/outputs: requests for fidelity or inference do not prove either entailment or non-entailment. Source references preserve some lineage, not external source truth. Elevation is explicitly described as hypothesis rather than derivation. See [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-free-input](runtime.md#rt-rte-free-input), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission) and [EPI-OBJ-principle-rules](#epi-obj-principle-rules).

Hunter judgments have advisory force for current reflection, not independently checked truth. Structural filters enforce identity/shape constraints; retained dismissals enforce future display suppression, reversible by undismiss. That is a direct behavior-adaptation route, independent of whether the human rejection was correct. Neither route establishes model training, calibrated confidence or improved capacity. See [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan) and [RT-BAP-dismissal-filter](runtime.md#rt-bap-dismissal-filter).

The dependency lookup derives which stored links name principles, conditional on cached metadata and basename resolution. Its authority does not extend to the necessity of the assumptions or the real-world falsity of rules. Human marking of undermined assumptions changes a status and refreshes graph views; no automatic rejection of dependent rules follows in the inspected consumer. Origin maintenance can reconstruct or redirect provenance without proving the recorded historical relation. Audit warnings concern fixed completeness predicates and permit navigation, not content acceptance. See [EPI-RTE-collapse-review](#epi-rte-collapse-review), [EPI-RTE-origin-maintenance](#epi-rte-origin-maintenance) and [EPI-RTE-vault-audit](#epi-rte-vault-audit).

Human approval licenses note persistence or metadata changes. No inspected mandatory criterion verifies empirical correctness for an intended practical use; no supplied human decision documents such acceptance. Consequently organizational linking is not evidence of post-acceptance lifecycle integration. This fits the explicit reflective-practice disclaimer rather than constituting failure to deliver a decision-support product. Broader efficacy, causal improvement, criticism-led iteration and exercised learning remain unestablished. The independent localized-rule and consumption affordances in [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) survive those limits. Opaque model processing does not settle criticism or learning in either direction; external parameter state stays bounded by [RT-CMP-model](runtime.md#rt-cmp-model). Uninspected guidance consumers preclude a system-complete negative.

## Shared records

### Operative objects

#### EPI-OBJ-note-content
Label: Tension and substrate text

Source-native identity: note statements A/B and substrate raw content; natural-language Markdown on the Obsidian vault filesystem. Candidate truth-apt content includes reported observations, quotations and competing claims; preferences or imperatives alone need not be truth-apt. Closest supplied [RT-RTE-free-input](runtime.md#rt-rte-free-input) and [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) are producing routes, not object duplicates. SRC-1 `README.md`, doctrine/design; persistence implementation passage supplied by those routes.

> | `substrate` | Raw material (quotes, facts, observations) | `source`, `base_language` |
> --- `README.md`

#### EPI-OBJ-hunter-pairs
Label: Hunter pair judgments

Source-native identity: `HunterRun.result.pairs`; natural-language descriptions and symbolic basename/confidence fields held in view/run memory, with timestamp/count settings separately saved. Candidate claim: two selected notes are incompatible in the description's stated sense. Distinct part of the result path of [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan), not a new route or model component. SRC-1 `flows/hunter.ts`, implementation.

> const run: HunterRun = { meta, result: { pairs: filtered } };
> --- `flows/hunter.ts`

#### EPI-OBJ-principle-rules
Label: Principle conditional rules

Source-native identity: IF/THEN/GREY fields in principle Markdown, natural-language content on vault storage. Candidate factual content is conditional applicability and claimed outcomes; prescriptions are policy. Closest supplied [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) owns admission/theory assessment, not object identity. SRC-1 `ai/prompts.ts`, doctrine/design; `core/aiFriction.ts`, shipped limitation text.

> "The IF/THEN proposal is a hypothesis, not a derivation",
> "I cannot test the rule against your real cases",
> "Operational rules need lived validation",
> --- `core/aiFriction.ts`

#### EPI-OBJ-assumption-text
Label: Presupposition claims

Source-native identity: principle U-note text and separately tension A/B assumption fields. Both are natural language retained in vault Markdown; tension fields can also be frontmatter strings. Candidate claim: the world is as stated, and the parent depends on it. Split consumers: U notes have graph dependencies; A/B fields are edited inline, not the same dependency object. Closest supplied [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission) establishes the U-note route, while [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) establishes parent rules. This inventory groups prose only, not their distinct admission routes. SRC-1 `ai/prompts.ts`, doctrine/design; `flows/presupposti.ts`, implementation.

> - Phrased as a positive claim about how the world works.
> --- `ai/prompts.ts`

#### EPI-OBJ-note-markers
Label: Types statuses and references

Source-native identity: `antinomia_type`, `status`, `origin_tension`, `replaced_by`, `presupposes`, `presupposes_of`, `hunter_false_positives`. Symbolic YAML/frontmatter on vault Markdown; cache supplies selectors. These control inclusion, link traversal and suppression. They record judgments/policy but are not independently verified claims. Closest supplied [RT-RTE-pair-dismissal](runtime.md#rt-rte-pair-dismissal), [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission), [RT-RTE-schema-migration](runtime.md#rt-rte-schema-migration) are mutation routes rather than object duplicates. Different consumers are separated in the ledger. Evidence: SRC-1 `flows/hunter.ts`, `flows/presuppositionMap.ts`, `main.ts`; minimum passages supplied by those routes and new route records below.

### Routes

#### EPI-RTE-inline-assumptions
Label: Tension assumption editing

Endpoints: tension body → model proposal → editable A/B modal → body/frontmatter fields. Owner: plugin code with provider inference and human admission. Closest supplied [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission) explicitly distinguishes this older route; identity differs because it writes same-note fields, not U notes or bidirectional dependencies. SRC-1 `flows/presupposti.ts`, implementation; `ai/prompts.ts`, doctrine/design. Proposer is model or human; human submits/cancels, code checks parse/key types. No answer oracle, open editing mode, no improvement trigger. Guidance asks for assumptions which would dissolve the tension. No empirical criterion or rollback is required. The key check accepts either A or B as a string, not necessarily both. Missing/empty sides do not clear previous content. Semantic relation is indeterminate without an actual proposal instance.

- Immediate return: Modal, proposal fields or error; apply writes modified note and notice.
- Later read-back: Reopening mapping reads frontmatter first, then body fallback; retained body can reach later Hunter prefix selection.
- Delegated visibility: Provider sees supplied tension content; no worker delegation.
- Selection predicate: Tension type guard, parsed response with at least one string field; human submit determines final values.
- Invalidation or expiry: No expiry; later edit can replace nonempty fields. Empty values do not withdraw previous fields.
- Activation or effect: Code writes both frontmatter and corresponding body text; no observed semantic reliance.
- Evidence limits: Static implementation; no supplied user decision or evidence-consuming truth test.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (typeof parsed.presupposizioniA !== "string" && typeof parsed.presupposizioniB !== "string") {
> --- `flows/presupposti.ts`

> if (a) fm.presupposizioniA = a;
> if (b) fm.presupposizioniB = b;
> --- `flows/presupposti.ts`

#### EPI-RTE-note-disposition
Label: Note type and status disposition

Endpoints: human action or model classification → metadata mutation → later selectors. Owner: plugin callbacks and host vault API. Closest supplied [RT-RTE-free-input](runtime.md#rt-rte-free-input) creates new notes; this route mutates existing notes. [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) separately owns elevation. Classification proposes a type with motivation; code checks presence/type enum, human accepts or vetoes. Manual markAsType bypasses that model path; markResolved directly writes status; archive collects motive/replacement, changes type and removes status/origin. These are separate per-action predicates within a common metadata-admission family, not truth checks. Open user operations; no oracle or automatic improvement trigger. Human judgment supplies admission; criterion for actual defeat/resolution is not enforced. Recovery is user editing, not an automatic transaction/rollback. SRC-1 `main.ts`, implementation. Operational authority: resolved tensions and defeated notes cease being eligible open-tension Hunter inputs; classification to substrate can admit them. Epistemic authority: only a recorded human disposition.

- Immediate return: Confirmation/modal or notice, then metadata update on acceptance/action.
- Later read-back: Hunter type/status selection and layer views consume retained metadata.
- Delegated visibility: Classification provider sees full raw note; user review receives proposed type and motivation.
- Selection predicate: Classification parsed tipo/motivazione and valid enum then human confirmation; manual action has no model verification; archive cancellation prevents its writes.
- Invalidation or expiry: No automatic expiry; manual edits or other transitions can change labels.
- Activation or effect: Symbolic selectors change inclusion and presentation; no empirical falsity demonstrated.
- Evidence limits: Source wiring, not observed judgment quality or accurate motivation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (!validTypes.includes(parsed.tipo)) {
> --- `main.ts`

> fm.status = "resolved";
> --- `main.ts`

> fm.antinomia_type = TYPE.defeated;
> fm.motive = motive;
> fm.modified_date = todayISO();
> delete fm.status;
> delete fm.origin;
> --- `main.ts`

#### EPI-RTE-origin-maintenance
Label: Retroactive origin maintenance

Endpoints: existing principle origin section or orphan selection → new defeated note and origin link; alternatively two human-selected defeated files → redirected principle links and removal of one file. Owner: plugin deterministic code/host storage. Closest supplied [RT-RTE-schema-migration](runtime.md#rt-rte-schema-migration) is a different migration; [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) creates an origin during elevation rather than reconstructing it later. No duplicate. SRC-1 `main.ts`, implementation.

The user invokes batch retroactive creation, picks an orphan for placeholder origin creation, or chooses keep/remove for merge. Code derives titles, dates, links and motive `elevata`; no model or answer oracle verifies historical fidelity. The retroactive extractor matches the Italian heading `## Origine (tensione)`; it does not infer an origin from arbitrary prose. Orphan creation explicitly supplies A/B placeholders for later recollection. Merge redirects origin references using substring inclusion, appends a merge annotation to kept text and trashes the removed file; it does not merge the removed body. This prevents assuming preservation of both records or exact link matching. User selection is admission, no separate truth criterion; no automatic rollback. Open maintenance mode, not experimentation. Behavioral-authority path: graph/layer consumers and future origin traversal, symbolic stored links, enforcing reference change, until subsequent edit/deletion. Epistemic license is a reconstructed/edited history only, not proof that a tension was tested or defeated.

- Immediate return: Created note/count notice or redirected links and trash action.
- Later read-back: Principle origin_tension and defeated replaced_by supply future graph/history consumers.
- Delegated visibility: inapplicable — deterministic maintenance and user selection, no inference service.
- Selection predicate: Batch principles without an already-linked defeated and with matched origin text; orphan command filters missing/nondefeated origins; merge user chooses two distinct files.
- Invalidation or expiry: No expiry; merge deletes one file; underlying host trash recovery is uninspected.
- Activation or effect: New reconstructed history, changed origin references, removal of one original body on merge.
- Evidence limits: No observed migration, semantic identity check, preservation guarantee or historical authenticity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (ot.includes(removeFile.basename)) {
> --- `main.ts`

> rawKeep + `\n\n_(unito con ${removeFile.basename} il ${today})_\n`
> --- `main.ts`

> await this.app.fileManager.trashFile(removeFile);
> --- `main.ts`

#### EPI-RTE-collapse-review
Label: Dependency lookup and undermining

Endpoints: presupposition metadata and vault principle list → displayed dependency list → optional user marking of this assumption. Owner: deterministic plugin lookup and human decision. Closest supplied [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission) creates links; this is a downstream consumer and withdrawal marker, not a duplicate creation route. SRC-1 `flows/presuppositionMap.ts`, `modals/CollapseImpactModal.ts`, implementation.

Check target/domain: which cached principle metadata records the selected basename in either direction. Evaluator is exact membership, not logical implication or observation of a false assumption. Concrete source deduction: U has presupposes_of=[P], P has principle type, and P has empty presupposes. `wanted.has(f.basename)` still includes P; removing U→P alone still includes P if P→U remains. Only metadata incidence is derived, conditional on host reads and identity. The UI reads principle bodies only for an IF-line snippet. User may mark the assumption undermined without supplying a refutation, then code writes status/date and refreshes graph. No automatic dependent-principle rejection occurs in this implementation. Proposer/decider/veto: human can press Close or Mark; no model, reference oracle or automatic improvement trigger. Mode is open review. No explicit recovery button here; later manual metadata edit remains possible. Epistemic authority: dependency as encoded, not necessity or actual collapse. Behavioral path: user via advisory list/snippet during review, then graph consumers through status/refresh until edit; status itself does not enforce rule non-use.

- Immediate return: Dependency list and optional status-write notice.
- Later read-back: Future views/readers can read undermined status; graph refresh is requested, not evidence of changed human reliance.
- Delegated visibility: inapplicable — no provider or worker in lookup/mark operation.
- Selection predicate: Presupposition type guard, principle type plus forward or reverse basename membership; explicit human Mark action.
- Invalidation or expiry: No expiry or automatic unlink on undermining. Separate delete callback removes principle-side U links for deleted U-prefixed Markdown files.
- Activation or effect: Displayed list; marking changes selected assumption status only, not dependent rules.
- Evidence limits: Cached graph incidence may be stale or ambiguous by basename; necessity and real-world failure untested.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> wanted.has(f.basename) ||
> basenamesFromFrontmatter(ffm.presupposes).includes(presupFile.basename)
> --- `flows/presuppositionMap.ts`

> fm.status = "undermined";
> --- `flows/presuppositionMap.ts`

> .setButtonText("Mark this presupposition as undermined")
> --- `modals/CollapseImpactModal.ts`

#### EPI-RTE-vault-audit
Label: Vault completeness audit

Endpoints: typed notes/cached bodies → issue arrays → advisory health display and file navigation. Owner: plugin deterministic predicates. No counterpart among supplied runtime declarations; closest [RT-RTE-schema-migration](runtime.md#rt-rte-schema-migration) changes schema, whereas audit does not mutate note content. SRC-1 `views/AuditVaultView.ts`, implementation.

Target/domain: presence of title/heading, A/B and assumption text, exact uncompiled IF placeholders and defeated motive. Checks are not contradiction resolution or rule truth tests. A principle with neither IF text nor the exact placeholder can evade the placeholder predicate; “healthy” therefore means no enumerated issue, not semantic validity. No veto, candidate admission, answer oracle or content revision occurs. Advisory force reaches the human through issue lists and open-file links during the view lifetime. Human repair is outside this route.

- Immediate return: Issue counts/list or healthy message.
- Later read-back: inapplicable — body cache is current view working state, not an accumulated learning artifact; each refresh reads vault inputs.
- Delegated visibility: inapplicable — no inference service or worker.
- Selection predicate: Typed Markdown notes, mtime/path cache key, fixed content/frontmatter predicates.
- Invalidation or expiry: Body cache refreshed on modify/create/delete/rename events; metadata change rerenders. Host timing remains external.
- Activation or effect: Advisory issue display and navigation, not blocking retention or use.
- Evidence limits: No observed rendering/repair; no truth, broken-link completeness or full schema license follows from no reported issues.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const stillPlaceholder =
>   body.includes("IF [condizione A] -> [esito X]") ||
>   body.includes("IF [condizione B] -> [esito Y]");
> --- `views/AuditVaultView.ts`

> summary.setText("✅ No issues found. Vault is healthy.");
> --- `views/AuditVaultView.ts`

### Claims

#### EPI-CLM-reflective-practice
Label: Reflective practice rather than decision support

Claim: Hunter identifies contradictions for thought, while principles and defeated beliefs encode the user's epistemic history. Closest supplied [RT-CLM-friction-scope](runtime.md#rt-clm-friction-scope) concerns a specific acknowledgment policy, not the product's warrant boundary. SRC-1 `README.md`, doctrine/design. The explicit disclaimer counters a reading that every displayed pair is warranted truth.

> **Antinomia is not a decision-support system.** The pairs the Contradiction Hunter proposes are prompts for thinking, **not truths on which to base real decisions** (work, health, finance, relationships). AI models can hallucinate, oversimplify, misinterpret. Use Antinomia as a reflective practice.
> --- `README.md`

> When a belief proves false, it goes into the Defeated archive as a memory of what was not true. The graph that emerges is the map of your epistemic history.
> --- `README.md`

#### EPI-CLM-source-fidelity
Label: Faithful standalone concepts

Claimed operation: extract self-contained source claims rather than interpretations/conclusions. No counterpart among supplied claims; closest [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) implements the request/admission path. SRC-1 `ai/prompts.ts`, doctrine/design.

> - \`content\`: 1-4 sentences, faithfully reflecting the source. Preserve key wording. Do NOT rephrase aggressively, do NOT add interpretation.
> --- `ai/prompts.ts`

#### EPI-CLM-collapse-impact
Label: Load-bearing assumptions

Claimed operation: identify assumptions whose falsity would collapse a principle, and show dependent principles. No counterpart among supplied claims; closest [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission) requests and stores proposals. SRC-1 `ai/prompts.ts`, `flows/exampleVault.ts`, doctrine/design. Not a proof certificate.

> A PRESUPPOSITION is a background assumption that the principle takes for granted. The test: if the presupposition turned out to be FALSE, the principle would no longer hold — it would collapse. These are "load-bearing assumptions".
> --- `ai/prompts.ts`

#### EPI-CLM-hunter-measure
Label: Seeded Hunter measurement

Claim/design: human key names seeded contradictions, control noise and expected confidence ordering; it attributes subtle-case success to model reasoning and misses to model limits. No counterpart among supplied claims; closest [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan) supplies scan implementation. SRC-1 `flows/exampleVault.ts`, doctrine/design. The key is a possible human answer reference in this optional evaluation mode, not an oracle consumed by the ordinary Hunter code. No actual comparison results supplied. Source-native causal attribution is not established: note caps/prefix selection, prompt examples overlapping sharp cases, and provider choice can affect outputs; no independent intervention isolates the responsible component.

> - **CN5 subtle**: does it find it? -> the model reasons well; if it skips it -> model limit, not design.
> --- `flows/exampleVault.ts`

> If the Hunter pairs any of these as "contradiction", it's a FALSE POSITIVE.
> --- `flows/exampleVault.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
