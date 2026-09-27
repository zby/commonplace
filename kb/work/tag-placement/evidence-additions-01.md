# Review and evidence additions

## Scope and decision

On 2026-09-27 the operator requested another chunk. This pass checks twenty-four
remaining entries on semantic review, observability, claim support, failure
modes, curation, and learning. Twenty-three entries support additions under the
live heads. ADD-039 repeats the removal already implemented through TP-012 and
is closed as a duplicate without another note edit.

Observability requires an argument about visibility, not merely a described
failure. ADD-096 qualifies through its developed use of recurring intervention
records to expose which pathway functions remain human. ADD-161 qualifies
through the contrast between silent quality degradation and visible hard-limit
errors, and the limits on observing how a model used its inputs. ADD-093 earns
claims-and-grounding through production evidence retained as provenance,
citations, and quote anchors; history in general would not be enough.

No inclusion rule changes. These decisions classify the notes' substantive
subjects; they do not certify the claims or their source grounding.

## Accepted entries

| Entry | Note | Added subject tags | Reason |
| --- | --- | --- | --- |
| ADD-007 | [A linked note discharges its own grounding, so a citing note owes representation, not re-grounding](../../notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md) | review-system | The note separates source grounding from faithful representation and analyzes the concept-attribution and misleading-link-text semantic criteria. |
| ADD-017 | [Accumulation counts dependence through the retained result, not through the evidence it caused](../../notes/accumulation-counts-dependence-through-the-retained-result.md) | learning-theory | The note defines when later improvement consumes or preserves earlier retained results and distinguishes accumulation from merely operative change. |
| ADD-022 | [Agent memory needs discoverable, loadable, composable, trusted knowledge under bounded context](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) | failure-modes | The developed failure cases distinguish undiscovered, stranded, isolated, and uncalibrated memory, plus the gap between available and activated knowledge. |
| ADD-048 | [Citing retained theory at the decision point is a mediation trace](../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) | observability | Contemporaneous decision citations expose which theory was reportedly consumed, while post-hoc and decorative citations limit what can be reconstructed. |
| ADD-063 | [Diagnostic richness constrains outer-loop learning quality](../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) | observability | The note identifies which traces, tool calls, memory reads, and drill-down paths expose mechanisms that candidate scores alone cannot reveal. |
| ADD-068 | [Domain pricing routes an exception to idealization assessment but does not decide it](../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) | claims-and-grounding | The note specifies the scope, omitted mechanism, consequence bound, and explanatory dominance an idealized claim must commit to and support. |
| ADD-071 | [Error correction works with above-chance oracles and decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) | learning-theory | The note develops verification and error correction through discriminative oracles and decorrelated checks, fitting both the broad head and its llm-reliability child. |
| ADD-079 | [Factory construction is not evidence of production-knowledge acquisition](../../notes/factory-construction-does-not-establish-knowledge-acquisition.md) | learning-theory | The construction/acquisition distinction states what evidence would establish learning of reusable production knowledge rather than realization of supplied machinery. |
| ADD-089 | [Generality bought to avoid counterexamples is paid for in precision](../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) | claims-and-grounding | The note tests what revised claim wording forbids and requires counterexamples to become explicit scope or exceptions rather than disappear into abstraction. |
| ADD-093 | [History has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md) | claims-and-grounding, observability | Provenance, citations, and quote anchors preserve evidence for later review; the production-time boundary also explains why unrecorded history cannot be reliably reconstructed. |
| ADD-094 | [Improvements can accumulate without compounding](../../notes/improvements-can-accumulate-without-compounding.md) | learning-theory | The note separates retained accumulation from causal gains in later improvement productivity and states the evidence needed for compounding. |
| ADD-096 | [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](../../notes/increasing-computational-autonomy-relocates-human-effort.md) | observability | The recurring-intervention record reveals which pathway functions remain human and where the intervention frontier lies; total hours obscure that distinction. |
| ADD-097 | [Indexes lower recall when they suppress retrieval that would find more](../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) | failure-modes | The note explains an activation failure in which a false completeness signal suppresses a retrieval route that would have found more relevant knowledge. |
| ADD-107 | [Link strength is encoded in position and prose](../../notes/link-strength-is-encoded-in-position-and-prose.md) | curation | The Note scoring and Quality signals sections use weighted links to rank notes and assess graph health as the collection grows. |
| ADD-129 | [Narrowing bought to survive review is paid for in content](../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) | review-system | The note analyzes how semantic gate/revise loops can accept empty claims and proposes contribution checks that can reject such repairs. |
| ADD-148 | [Reasoning production is not reasoning evaluation](../../notes/reasoning-production-is-not-reasoning-evaluation.md) | review-system | The note diagnoses answer reconstruction substituting for argument evaluation and applies that failure to semantic gates, critique, and fix review. |
| ADD-153 | [Decorrelated reviewers still share the field's prior, so read their findings by the claim's stance](../../notes/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) | review-system | The note centers on correlated reviewer priors, verdict interpretation, and author-side triage of semantic findings. |
| ADD-155 | [Runtime structure determines the control surfaces available to governance](../../notes/runtime-structure-determines-governance-control-surfaces.md) | observability | The scheduler, context-engine, and substrate analysis explains which decisions, loaded inputs, and state changes governance can inspect. |
| ADD-161 | [Soft degradation can bind before the hard cap even when required evidence fits](../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) | observability | The soft-bound section explains why fluent output and the absence of a hard-limit error fail to expose degraded processing; downstream quality reveals it. |
| ADD-165 | [Stale self-description conceals its own staleness](../../notes/stale-self-description-conceals-its-own-staleness.md) | observability | A consulted stale self-map can suppress evidence of its own drift; operation-triggered synchronization exposes changes that file-edit events miss. |
| ADD-183 | [Title as claim enables traversal as reasoning](../../notes/title-as-claim-enables-traversal-as-reasoning.md) | claims-and-grounding | The title convention makes each note's asserted commitment available as a premise and distinguishes claims from topical or definitional references. |
| ADD-187 | [Trace-extracted memory earns authority per operation, not at capture](../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) | failure-modes | The note develops the authority failure in which unverified diagnoses are consumed as established knowledge, and the separate failure of retained rules never being activated. |
| ADD-198 | [Review automation should target verifiable subroles before reviewer identity](../../notes/verifiable-subroles-before-reviewer-identity.md) | review-system | The Commonplace-gates section decomposes semantic review into inspectable subroles with explicit evidence targets and calibrated authority. |

## Duplicate removal

ADD-039 repeats [TP-012](./assigned-tag-issues.md#tp-012--artifact-analysis).
The live note already carries only document-system. Its opening still concerns
preserving the reference/range and role of named choices for a document's
consumers. This confirms the existing disposition in the
[single-field scope decision](./artifact-analysis-scope-decision.md): remove
artifact-analysis and keep document-system. No new removal or parent-gap
closure is counted; PG-035 was already resolved.

## Parent checks and accounting

Nine original learning-theory gaps close after checking the existing children:

- PG-020 / ADD-017: dependence through retained results is a developed
  accumulation mechanism within self-improving-systems.
- PG-041 / ADD-048: evidence that retained theory guided a system's own
  changes concerns the mechanism and attribution of self-improvement. The
  theory-consumption analysis also fits the existing theory-builder child.
- PG-059 / ADD-071: oracle discrimination and decorrelated checks directly
  develop LLM error correction, supporting llm-reliability.
- PG-070 / ADD-079: the distinction between realizing supplied factory
  knowledge and acquiring reusable production knowledge is a substantive
  boundary analysis of self-improvement, without certifying that a given
  constructor learns.
- PG-076 / ADD-094: retained changes and their effects on later improvement
  distinguish accumulation from compounding within self-improving-systems.
- PG-077 / ADD-096: the note analyzes human/computational allocation in an
  improvement pathway and what makes increased unattended work warranted,
  fitting self-improving-systems and its warranted-autonomy child.
- PG-098 / ADD-148: answer-confirmation bias and independent reasoning checks
  concern faulty model judgments and their correction, fitting llm-reliability.
- PG-110 / ADD-165: synchronizing a consumed self-description after a system
  changes itself fits self-improving-systems. The source-dependency and lineage
  analysis also draws maintenance consequences from an artifact-analysis field.
- PG-122 / ADD-198: narrow checks, calibrated reviewers, and evidence-preserving
  aggregation directly address unreliable model review, fitting llm-reliability.

The proposed learning-theory additions on ADD-017, ADD-071, ADD-079, and ADD-094
already supply four of these parents. The other five are additional repairs.

Eight accepted child assignments also require kb-maintenance: review-system
on ADD-129, ADD-148, ADD-153, and ADD-198; claims-and-grounding on ADD-089,
ADD-093, and ADD-183; and curation on ADD-107. These notes substantively address
semantic checks, supportable claims, or collection navigation as described in
their accepted-entry reasons. Those repairs are outside the frozen
learning-theory gap inventory and do not create additional PG closures.

This pass adds thirty-seven assignments across twenty-three notes: five
review-system, seven observability, four claims-and-grounding, three
failure-modes, one curation, nine learning-theory, and eight kb-maintenance.
Twenty-four implement suggestions; thirteen other assignments supply required
parents. No assignments are removed. All twenty-four inspected note bodies
remain unchanged, including the duplicate-removal note's tags.

Four complete heads gain thirteen member links: review-system gets five,
claims-and-grounding four, failure-modes three, and curation one. Existing
head prose, links, and inclusion rules remain unchanged. Nine other head inputs
remain unchanged; learning-theory and kb-maintenance route through supported
children.

The workshop now records 188 accepted addition entries, four duplicate removal
closures, and 14 open additions. All 68 original placement findings remain
resolved. PC-07 has 58 resolved and 71 open parent-gap entries.

## Verification

`commonplace-validate` passed on all thirty-three changed files and the tags
collection, with no failures or warnings. Separate checks confirmed thirty-seven
added assignments, no removals, twenty-four unchanged note bodies, nine
unchanged heads, thirteen new member links as the only changes to four heads,
preserved reviewer suggestions and evidence links, queue counts, and all
thirty-seven recorded final hashes. `git diff --check` passed. These are direct
semantic judgments, not new independent assays. Changes remain uncommitted.

The earlier Naur compiler-case filename failure is outside this batch and
remains recorded in the context and document additions pass; this result does
not clear that pre-existing issue.

## Checked versions

SHA-256 hashes identify the live inputs checked and the resulting artifacts.
Original reviewer wording, evidence links, and frozen baseline records remain
unchanged. The duplicate-removal note is included with identical hashes.

| Artifact | Before | After |
| --- | --- | --- |
| [notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md](../../notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md) | `ff7566991165990676e52064344ca7a0629779b46c9736bcdb8cba4db369db0d` | `8e56c189e1c29ad3b38e44410348291150b8b175a06f4d0f04d7003d22af2695` |
| [notes/accumulation-counts-dependence-through-the-retained-result.md](../../notes/accumulation-counts-dependence-through-the-retained-result.md) | `59b9ae66ee8d9dd00c06898c03a31a629513c8b9f9e3ce161a0c4ae24d17eca8` | `d47022ff781690358ed9fdda03c95631129859c712f95d640aadd1d77a91d99e` |
| [notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) | `a3b308fa1ff44788daf1b06031419afea98d988eb5447fc60494083fd7b141be` | `1535a4a397df163f0016d292af645df3795910de3c19da221b8fd2f13fb0ffd4` |
| [notes/artifacts-must-preserve-named-choice-scope.md](../../notes/artifacts-must-preserve-named-choice-scope.md) | `8e04afe83c261ecdb5e6853627f1e6ee2d555430e1ed26b3b2044dd2f09bab80` | `8e04afe83c261ecdb5e6853627f1e6ee2d555430e1ed26b3b2044dd2f09bab80` |
| [notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md](../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) | `fb542adbd7cd0365f5e9ec7aa4850c6d9f581c8cdf5db2a25ace1c989be18285` | `a4c247608a4ee3bff01b3aebcf18e998987bedf6b81026131924246b06cb668a` |
| [notes/diagnostic-richness-constrains-outer-loop-learning-quality.md](../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) | `12c3486a00129f99c48e0149cbcf59b582caeffd8ab0a7c247f4f41fe700fa4c` | `4c5e3939fa7021d48e0503cb513352486703d804ad1ec9026a649fb8eec86bf6` |
| [notes/domain-pricing-routes-an-exception-to-idealization-assessment.md](../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) | `94690a0814808791c4302e5a09fbb07a9ebd416ba8cd0e8757a1d7b61a481a1e` | `4990b42c126d5618553700747f871e9c9cff7f9bfb8521d5c4201bdbbdd7228f` |
| [notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) | `e8b465a9a93d2efd9ac43187a1f1781eca2071fdad572d1f82687a2e1fe2c76d` | `e5e48ec2c2c4354db91b507a71799a7b77605c925d590bd5f6e9fb21ff6d35ba` |
| [notes/factory-construction-does-not-establish-knowledge-acquisition.md](../../notes/factory-construction-does-not-establish-knowledge-acquisition.md) | `8cf7809dbb68facebd77336cc725d69021a52f3de9cb2e7a9ab51a590bee6ebf` | `f28bda79998347f9ec0a0f8b70720f424d44bca7a03d240310ee4829360443d3` |
| [notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md](../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) | `41ab11c14161ff89ef2580cd68a98891e106d6c1112ebba4be4737b5e6c8c16a` | `489d95e70d92ced5dc934d131de29fe07ea9a544667e0252b314d148e025583c` |
| [notes/history-has-one-chance-to-become-checkable.md](../../notes/history-has-one-chance-to-become-checkable.md) | `5bd379ab9a34075d7d7e837f6daa776409e3019f3ae45ad041f293810e97d071` | `8cd5a2772fffa4f3bb0097aa30cc2b39bf57483221c9a33e6e65a499d1f6eb8c` |
| [notes/improvements-can-accumulate-without-compounding.md](../../notes/improvements-can-accumulate-without-compounding.md) | `4e070c832be65b95e1eb17972bacd5ba9720ed9dc09a5fbbb2f1fced96d2f632` | `7b42ce0dffbe4ad3a5e62970ec9ca96266ad315d24ed8ec188bf4a48def53ed0` |
| [notes/increasing-computational-autonomy-relocates-human-effort.md](../../notes/increasing-computational-autonomy-relocates-human-effort.md) | `116745e6ca6a026c8849c4300bdf7063c44406be7d77305edd76bc774134698f` | `eabd5225916c88619f5d09cd5c96c00b209de1b1b27cf4a31cff86c0b20963ca` |
| [notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md](../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) | `8bbfd0dcc0f521029c8ba6271b7acd9197b3824ffde04e2c9165b6d961a68e09` | `48d063add315432a7b77fd78c04135941dddeac0e78e57f5c5e18dc14e0b1065` |
| [notes/link-strength-is-encoded-in-position-and-prose.md](../../notes/link-strength-is-encoded-in-position-and-prose.md) | `23b6ae22b15f958a624f0b6aafd4c806e84b228b71d69913fc9f1e171563406b` | `010f5fffaf64a8facbb2956812e263db738755054aca3cea91562b8a11f6fd37` |
| [notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md](../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) | `168be117c7cbdd266aecdb368d3d9c7d842c5df01ee54b20487c64bae662c602` | `18d0bfd2ea2c47efd30df095cf20d6da642b15ff905e7264cc5a460cec3d7337` |
| [notes/reasoning-production-is-not-reasoning-evaluation.md](../../notes/reasoning-production-is-not-reasoning-evaluation.md) | `3a69c358bab30bb914cf461dc6e30ad02980fcc643d5361f0786443f405070f0` | `45ab733f2ef2c61bab87486069b12fef1a2ec209e5f12c2dece0fb634db56988` |
| [notes/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md](../../notes/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) | `cecb65b6d6a6b39b88e550437abc89a5c5e1705177d31095bd1db16c53857bbd` | `1773a2ab612c2c5b0220592a02660fd011953bb11463317b1471907f5e73eefd` |
| [notes/runtime-structure-determines-governance-control-surfaces.md](../../notes/runtime-structure-determines-governance-control-surfaces.md) | `624bd82b4979511c1df10422d612964ca0588dad98fed4dfd776d9404a8bb99c` | `8470a4ac2009cc421a37703ff3b77b97782ebb765c14a50d5abbae4d625776c0` |
| [notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md](../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) | `2763844b2dedef4c87c2a1dca03642d31a2eb5b8e939a67ed2dcc87fc93266b8` | `036fc3e98a5cd6edc9c154a1522016590ee5dcfbc06f8d48f6023a21ad10fa08` |
| [notes/stale-self-description-conceals-its-own-staleness.md](../../notes/stale-self-description-conceals-its-own-staleness.md) | `1b9200517f4796d832d9b1484e0a5aec80d677d8d854f069745c72024d69709e` | `4e6b17ebadca4eb6651c4c11f54510d5c542f066453a9698313bae3ff6891777` |
| [notes/title-as-claim-enables-traversal-as-reasoning.md](../../notes/title-as-claim-enables-traversal-as-reasoning.md) | `46fe0fa79e597505f7c9f110f080ea3c2bc1b1fd59d574340920ab3596b9d4f6` | `132ae5bd94dfcfac675704bb9c9a5c22ec08f23343a497d61a5940fa4c726b0e` |
| [notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md](../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) | `e046e352a1482a64001a33b7e2c3bf55932986793082e51595d7a5c01ce270b5` | `b97a91c838a8a9bcd306e2ff04f9946cacbcf9c33da2d92b5f748a257e75769b` |
| [notes/verifiable-subroles-before-reviewer-identity.md](../../notes/verifiable-subroles-before-reviewer-identity.md) | `411989b9173446bd0515882eb6af3e080fee3dce287974f5befc58eebd77271a` | `1ae08955661d29b2e42bc76102fa218a4735d74eda39cdc44d6799b20c2ef00e` |
| [tags/review-system-README.md](../../tags/review-system-README.md) | `f2f4184c0f7c4c24999cf005e2fa36a791e21485d99995206d94d7197b187a80` | `3933a2b46d4c79e4570926cdb061d2954bff62a5b8661cdc142ffdbcb8946220` |
| [tags/observability-README.md](../../tags/observability-README.md) | `2d42ea9e40ccf022ccfd8893fe4025f4e7186855a12f9e69a7be7e0222459aa9` | `2d42ea9e40ccf022ccfd8893fe4025f4e7186855a12f9e69a7be7e0222459aa9` |
| [tags/claims-and-grounding-README.md](../../tags/claims-and-grounding-README.md) | `4bba94a1166cb4d6d683c58def867090547ab8a01367ab6b2da7c122ea2915bd` | `5b94296941f464674b4d754deb6f23308857efaa3e9ccd3b70df253f167a1a99` |
| [tags/failure-modes-README.md](../../tags/failure-modes-README.md) | `b5505ed4356c530e91f0fed5aec5151879472bbe8c5986255fe5d2635eaa687c` | `29873a14b315560453f4f8172889bfe374bc6d40753c25c138f9568fe08ee354` |
| [tags/curation-README.md](../../tags/curation-README.md) | `9edf98764c198ac8ded0a38782fa44b34f05c28552337d13d9c8ada710c40699` | `7300cd06d82a651097965a0a898d61c734516b0e3eb4e656d6d2c9c27fbfba0b` |
| [tags/kb-maintenance-README.md](../../tags/kb-maintenance-README.md) | `01a93c13dded3a6e13f65199ea21cc8062d18fe091cee0c9471b8903368c9157` | `01a93c13dded3a6e13f65199ea21cc8062d18fe091cee0c9471b8903368c9157` |
| [tags/learning-theory-README.md](../../tags/learning-theory-README.md) | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` |
| [tags/self-improving-systems-README.md](../../tags/self-improving-systems-README.md) | `22dbb0008ce2d7d556c2f1927ecf30378e227eb2c11b8c53a1164be49b5143fe` | `22dbb0008ce2d7d556c2f1927ecf30378e227eb2c11b8c53a1164be49b5143fe` |
| [tags/llm-reliability-README.md](../../tags/llm-reliability-README.md) | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` |
| [tags/theory-builder-README.md](../../tags/theory-builder-README.md) | `e36f94cf460cb072bfb88602c5e35be25a8514c42e2a2d938609005d5bc7bd5c` | `e36f94cf460cb072bfb88602c5e35be25a8514c42e2a2d938609005d5bc7bd5c` |
| [tags/warranted-autonomy-README.md](../../tags/warranted-autonomy-README.md) | `4a693f29f636c359df3fae3e2855d44c155243058955a792607929b80239021b` | `4a693f29f636c359df3fae3e2855d44c155243058955a792607929b80239021b` |
| [tags/artifact-analysis-README.md](../../tags/artifact-analysis-README.md) | `d421dbfa1a9db73fe34181fa7ed0dde4ff5593d61424b5ad3e35667d270e635d` | `d421dbfa1a9db73fe34181fa7ed0dde4ff5593d61424b5ad3e35667d270e635d` |
| [tags/document-system-README.md](../../tags/document-system-README.md) | `5d0f5de7f082fedfe8be6038f71e2f1386e008ae77feca5906e14c354b45d1da` | `5d0f5de7f082fedfe8be6038f71e2f1386e008ae77feca5906e14c354b45d1da` |
