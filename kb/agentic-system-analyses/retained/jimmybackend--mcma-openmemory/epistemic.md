---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "MCMA-OpenMemory epistemic routes: metadata-gated reuse, owner-directed validation, optional organization and generation, and the limits of their warrant."
run-id: AAS-2026-11-08-mcma-openmemory-a023f4989e1c-01
reviewed-boundary: "556954d95f0d6d6894c5d46ffcc25a907150b0a7"
---

# MCMA-OpenMemory epistemic report

## Source-and-claim boundary

The question is how retained statements acquire authority to answer questions or inform generation, and whether that authority follows from a content check. The functional inclusions, external exclusions and frozen source are those of [boundary.md](boundary.md); source identity and evidence layers are in its [Source register](boundary.md#source-register). All direct reads below use SRC-1 at that revision. No target execution was performed. The runtime account is supplied implementation analysis, not a trace of operation.

The system's own qualification matters: [EPI-CLM-knowledge-policy](#epi-clm-knowledge-policy) distinguishes epistemic metadata from proof. It makes concrete reuse-policy claims rather than promising an automatic truth oracle. Encryption, permission checks, revision identity and similarity are not evaluated here as evidence of factual truth. They matter where they change admissibility or lineage.

| Entry point or operation | SRC-1 source path | Coverage and records, or remaining limit |
|---|---|---|
| CLI knowledge-put/check/show/validate; semantic-index/check/topk | `packages/core/src/Cli/CliApplication.php` | Direct dispatch read: [EPI-RTE-knowledge-validation](#epi-rte-knowledge-validation), [EPI-RTE-knowledge-assessment](#epi-rte-knowledge-assessment); semantic implementation supplied by [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer). CLI validation accepts supplied state, confidence, reason and optional provenance; it is not an independent factual investigation. |
| Ordinary ask, generated capture, direct exact/semantic answers | `packages/core/src/Ask/AskService.php` | Supplied [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer); directly inspected knowledge assessment and directAnswer consumer supplement it. |
| Web confirm/discard and knowledge inline edit | `packages/core/src/Web/WebApplication.php` | Direct reads of validation dispatch and editKnowledgeObject; [EPI-RTE-knowledge-validation](#epi-rte-knowledge-validation), [EPI-RTE-answer-replacement](#epi-rte-answer-replacement). Additional routes omitted from runtime's separate declarations, not contradictions of its bounded account. |
| Explicit capture and organizer | `packages/core/src/Memory/ExplicitMemoryService.php` | Direct capture/output-check/fallback reads; [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture), [RT-OBJ-organizer-instructions](runtime.md#rt-obj-organizer-instructions). |
| Interaction persistence, recovery, approval/discard and mutation | `packages/core/src/Interaction/InteractionArchiveService.php` | Supplied [RT-RTE-web-request](runtime.md#rt-rte-web-request), [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval), [RT-RTE-memory-mutation](runtime.md#rt-rte-memory-mutation). No independent execution evidence of review or synchronization. |
| Catalog classification and thematic synchronization | `packages/core/src/Interaction/InteractionCatalogService.php`; `packages/core/src/Interaction/ThematicSummaryService.php` | Direct reads; [EPI-RTE-catalog-classification](#epi-rte-catalog-classification), [EPI-RTE-thematic-summary](#epi-rte-thematic-summary). These are not generative factual criticism. |
| Canonical broad recall | `packages/core/src/Context/BroadMemoryRecallBuilder.php` | Direct canonicalRecall/canonical-item reads plus supplied ask consumer; [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer). Separate from strict knowledge policy. |
| Conversation, multi-memory and connector reference delivery | `packages/core/src/Context/ConversationContextBuilder.php`; `packages/core/src/Context/MultiMemoryContextBuilder.php` | Supplied [RT-RTE-context-supply](runtime.md#rt-rte-context-supply), [RT-BAP-memory-reference](runtime.md#rt-bap-memory-reference). Model compliance and semantic fidelity remain unobserved. |
| Permission, deployment, billing and raw library paths | `packages/core/src/Library.php`; `install.sh` | Supplied [RT-RTE-permission-change](runtime.md#rt-rte-permission-change), [RT-RTE-deploy-checkout](runtime.md#rt-rte-deploy-checkout), [RT-CLM-permission-scope](runtime.md#rt-clm-permission-scope), [RT-RTE-web-request](runtime.md#rt-rte-web-request). Operational admission, not truth evaluation. |
| Shipped evaluators | `tests/integration/ask-orchestration.php` | Selected fake embedding/generation fixture directly read; tests establish specified branch expectations, not measured natural-language accuracy. No test result or quality experiment supplied. |
| Hooks/tools and wider repository paths | `packages/core/src/Cli/CliApplication.php`; `packages/core/src/Ask/GenerationProvider.php` | CLI dispatch searched, material knowledge branches read. Connector/tool-schema account is supplied in runtime, not independently exhaustively searched here. Other tests, historical tools, full migration/recovery and all normative specifications were not exhaustively inspected. This prevents a system-complete negative about every possible evaluator or extension. |

Missing external model internals prevent an inference about internal checking or parameter learning. Missing concrete source propositions, generated outputs and evidence-consuming owner reviews prevent classifying actual generated claims as entailed or ampliative, or crediting any accepted ampliative result. Missing run/causal evidence prevents activation, reliability and benefit conclusions. Available but uninspected repository material is not an access gap or evidence of absence.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record) | Answer assertions over the record's question; symbolic metadata about their status | KnowledgeRecord | SRC-1, `packages/core/src/Knowledge/KnowledgeRecord.php` | Concrete records unprovided; confidence is not calibrated evidence. |
| [EPI-OBJ-canonical-memory](#epi-obj-canonical-memory) | User-supplied or model-organized assertions | Explicit canonical memory | SRC-1, `packages/core/src/Memory/ExplicitMemoryService.php` | Source text retained; meaning preservation of organized text not checked. |
| [EPI-OBJ-interaction-answer](#epi-obj-interaction-answer) | Question/answer assertions, when answer is truth-apt | Interaction answer | See [RT-RTE-web-request](runtime.md#rt-rte-web-request), SRC-1, `packages/core/src/Interaction/InteractionArchiveService.php` | Archive membership is not acceptance. |
| [EPI-OBJ-interaction-catalog](#epi-obj-interaction-catalog) | Attribution of topics, projects and named entities to an interaction | Catalog | SRC-1, `packages/core/src/Interaction/InteractionCatalogService.php` | Array/string checks do not verify attribution. |
| [EPI-OBJ-thematic-summary](#epi-obj-thematic-summary) | Topic label plus bounded answer excerpt | Derived thematic summary | SRC-1, `packages/core/src/Interaction/ThematicSummaryService.php` | First-sentence extraction can omit qualifications; not an independent finding. |
| [RT-OBJ-organizer-instructions](runtime.md#rt-obj-organizer-instructions) | None as a new factual finding; behavior guidance | See record | See record | Requests preservation; does not check compliance. |
| [RT-OBJ-permission-policy](runtime.md#rt-obj-permission-policy) | None required: executable grants | See record | See record | Symbolic operational authority, not evidence for answer truth. |
| [RT-CMP-ollama-generation-provider](runtime.md#rt-cmp-ollama-generation-provider), [RT-CMP-llama-cpp-generation](runtime.md#rt-cmp-llama-cpp-generation), [RT-CMP-bedrock-converse-generation](runtime.md#rt-cmp-bedrock-converse-generation) | Generated text can contain assertions; exact candidates not determinable | See records | See records | Opaque inference does not establish entailment, novelty or verification. |
| [RT-CMP-ollama-embedding-provider](runtime.md#rt-cmp-ollama-embedding-provider), [RT-CMP-llama-cpp-embedding](runtime.md#rt-cmp-llama-cpp-embedding), [RT-CMP-bedrock-titan-embedding](runtime.md#rt-cmp-bedrock-titan-embedding) | No individually stated proposition in vectors | See records | See records | Numerical retrieval representations are not answer oracles; model fixity limits remain local to each record. |

## Authority-route ledger

Each row is one function, even when its implementation record also supports another function. Generic progression/read-back fields belong to the cited declaring record: `see` retains that ownership. The classifications and warrant limits here are epistemic assessments, not copied route declarations. All statuses below concern inspected source or supplied implementation findings, not observed operation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) | content transformation | implemented | See record; [EPI-OBJ-interaction-answer](#epi-obj-interaction-answer) | truth-apt transformation: indeterminate | Question/context to generated text | Model inference; no independently supplied reference answer | See record | Candidate answer | See record | Candidate production only | See record | See record and [RT-BAP-memory-reference](runtime.md#rt-bap-memory-reference) | See record | none | none | No concrete output/premises: non-ampliative, entailed and ampliative alternatives unresolved. |
| [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) | retention | implemented | [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record) | no content change | Generated candidate to knowledge capture | Software capture rule, not a factual evaluator | See record | Unverified by default; configurable metadata | See record | Retained candidate, not accepted claim | See record | See record | See record | none | none | Default does not prevent later owner/configuration promotion. |
| [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture) | content transformation | implemented | [EPI-OBJ-canonical-memory](#epi-obj-canonical-memory) | truth-apt transformation: acquisition/import | User content enters archive; source warrant unknown | User save intent and optional organizer | See record | Source original plus normalized content | See record | Imported assertions, not newly warranted facts | See record | See record | SRC-1, `packages/core/src/Memory/ExplicitMemoryService.php` | none | none | Organizer subedge below is assessed separately. |
| [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture) | content transformation | implemented | [EPI-OBJ-canonical-memory](#epi-obj-canonical-memory) | truth-apt transformation: indeterminate | Source text to model-normalized text | Preservation instruction; semantic compliance unmeasured | See record | Organized text, or source-preserving fallback | See record | Fallback preserves source text; valid model output has unknown fidelity | See record | See record | SRC-1, `packages/core/src/Memory/ExplicitMemoryService.php` | none | none | Calling this always non-ampliative would confuse requested behavior with demonstrated preservation. |
| [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture) | check/evidence production | implemented | [EPI-OBJ-canonical-memory](#epi-obj-canonical-memory) | no content change | Organizer JSON fields, lengths and enums | PHP structural validator; schema domain only | See record | Structurally valid output or fallback | See record | Licenses parsing/classification shape, not equivalence or truth | See record | See record | SRC-1, `packages/core/src/Memory/ExplicitMemoryService.php` | none | none | sourceText parameter is not compared with content in validateOrganizerOutput. |
| [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture) | disposition/acceptance | implemented | [EPI-OBJ-canonical-memory](#epi-obj-canonical-memory) | no content change | Capture result to confirmed/verified metadata | Software assignment following explicit save, not post-organization human review | See record | Confirmed canonical; verified mirror if write succeeds | See record | User-authority convention, not evidence-consuming acceptance of the model transformation | See record | See record | SRC-1, `packages/core/src/Memory/ExplicitMemoryService.php` | none | none | Mirror and canonical commit can diverge. |
| [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture) | retention | implemented | [EPI-OBJ-canonical-memory](#epi-obj-canonical-memory), [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record) | no content change | Organized/source text to encrypted revisions | See record | See record | Durable canonical and optional mirror/index | See record | Retention carries assigned labels, not new factual evidence | See record | See record | See record | none | none | Not lifecycle integration after evidenced acceptance. |
| [EPI-RTE-knowledge-assessment](#epi-rte-knowledge-assessment) | check/evidence production | implemented | [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record) | no content change | Record admissibility for direct reuse | PHP metadata policy; state, confidence, age/current and reuse-policy domain | See record | reuse/revalidate/reject | See record | Metadata eligibility only; provenance count not independent corroboration | See record | See record | See record | [EPI-CLM-knowledge-policy](#epi-clm-knowledge-policy) | none | No evidence-source evaluation occurs in assess. |
| [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) | operational admission/selection/consumption | implemented | [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record) | no content change | Assessed exact/semantic record to terminal answer | PHP consumes assessment and semantic thresholds | See record | Direct remembered answer or fallback | See record | Direct reuse licenses dependence on stored labels, not new truth judgment | See record | See record | See record | [EPI-CLM-knowledge-policy](#epi-clm-knowledge-policy) | none | Similarity selects relevance; cannot establish that answer fits a paraphrased question. |
| [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) | operational admission/selection/consumption | implemented | [EPI-OBJ-canonical-memory](#epi-obj-canonical-memory) | truth-apt transformation: non-ampliative reshaping | Canonical items to concatenated direct answer | Broad recall: lexical subject and maturity-based mapped metadata | See record | Direct canonical recall before strict assessment | See record | Confirmed becomes verified/0.95; not a fresh truth check | See record | See record | SRC-1, `packages/core/src/Context/BroadMemoryRecallBuilder.php` | [EPI-CLM-knowledge-policy](#epi-clm-knowledge-policy) | scope distinction | currentRequired is not supplied here; strict-knowledge claim cannot be generalized to all recall. |
| [EPI-RTE-knowledge-validation](#epi-rte-knowledge-validation) | disposition/acceptance | implemented | [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record) | no content change | Caller decision to persisted validation metadata | Caller chooses state/confidence/reason; PHP shape validation | See record | Confirm/validate or retract | See record | Explicit reliance decision; evidence basis and review criterion not established | See record | See record | See record | [EPI-CLM-knowledge-policy](#epi-clm-knowledge-policy) | none | An owner decision can be meaningful without constituting an evidenced factual acceptance in supplied evidence. |
| [EPI-RTE-answer-replacement](#epi-rte-answer-replacement) | content transformation | implemented | [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record) | truth-apt transformation: acquisition/import | Owner-supplied replacement answer | Caller text; software bounds/permission checks | See record | Verified/0.95 edited answer | See record | Warrant of imported replacement unknown | See record | See record | See record | none | none | Editing is not a test of the original assertion. |
| [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval) | disposition/acceptance | implemented | [EPI-OBJ-interaction-answer](#epi-obj-interaction-answer) | no content change | Archived answer to approved/discarded status | Owner/caller choice; software transition | See record | verified/0.95 or retracted/0.0 | See record | Review decision recorded; no observed content review or named evidence criterion | See record | See record | See record | none | none | Existing knowledge can be validated without replacement by archived text. |
| [EPI-RTE-catalog-classification](#epi-rte-catalog-classification) | content transformation | implemented | [EPI-OBJ-interaction-catalog](#epi-obj-interaction-catalog) | truth-apt transformation: indeterminate | Interaction to semantic labels | Optional model with data-only/no-invention guidance | See record | Classified catalog or fallback | See record | Candidate attribution, not corroboration of answer | See record | See record | See record | none | none | Labels may be extracted or inferred; no concrete output individuates the edge. |
| [EPI-RTE-catalog-classification](#epi-rte-catalog-classification) | check/evidence production | implemented | [EPI-OBJ-interaction-catalog](#epi-obj-interaction-catalog) | no content change | Catalog JSON and label lengths/types | PHP decode/clean/list limits | See record | Sanitized metadata or fallback | See record | Structural usability only | See record | See record | See record | none | none | No factual names/relations check despite prompt prohibition on invention. |
| [EPI-RTE-thematic-summary](#epi-rte-thematic-summary) | content transformation | implemented | [EPI-OBJ-thematic-summary](#epi-obj-thematic-summary) | truth-apt transformation: non-ampliative reshaping | Archived answer to topic-prefixed first excerpt | PHP deterministic extraction, no provider | See record | Bounded derived text | See record | Carries source assertion and metadata; creates no independent corroboration | See record | See record | See record | none | none | Compression can remove qualifications; see concrete deduction in record. |
| [EPI-RTE-thematic-summary](#epi-rte-thematic-summary) | retention | implemented | [EPI-OBJ-thematic-summary](#epi-obj-thematic-summary) | no content change | Derived payload to versioned object | PHP persists and derives trusted flag from source metadata | See record | Active or superseded/untrusted object | See record | Inherited status, not acceptance | See record | See record | See record | none | none | Direct canonical recall explicitly excludes these summaries. Other downstream readers not exhaustively established. |
| [RT-RTE-memory-mutation](runtime.md#rt-rte-memory-mutation) | disposition/acceptance | implemented | [EPI-OBJ-canonical-memory](#epi-obj-canonical-memory) | no content change | User edit/delete request to update/tombstone | Deterministic target resolution and nonempty-edit checks | See record | Mutation or needs-target/content response | See record | User-authorized revision/withdrawal, not truth verification | See record | See record | See record | none | none | Retraction/index synchronization is not atomic; history persists. |
| [RT-RTE-context-supply](runtime.md#rt-rte-context-supply) | operational admission/selection/consumption | implemented | [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record), [EPI-OBJ-interaction-answer](#epi-obj-interaction-answer), [EPI-OBJ-canonical-memory](#epi-obj-canonical-memory) | truth-apt transformation: non-ampliative reshaping | Stored material to bounded provider reference | Deterministic selection/clipping; separate consumer policies | See record | Context with uncertainty fields | See record | Reference eligibility can be weaker than direct-answer eligibility | See record | See [RT-BAP-memory-reference](runtime.md#rt-bap-memory-reference) | See record | none | none | Delivery not endorsement or demonstrated influence; clipping may lose scope. |
| [RT-RTE-permission-change](runtime.md#rt-rte-permission-change) | behavior/policy adaptation | implemented | [RT-OBJ-permission-policy](runtime.md#rt-obj-permission-policy) | non-truth-apt policy/content update: role grants | Submitted policy to later access rules | PHP shape/current-policy/owner-recovery conditions | See record | Admitted or rejected grants | See record | No answer warrant | See record | See [RT-BAP-policy-decision](runtime.md#rt-bap-policy-decision) | See record | none | none | Direct operational authority without truth-apt learning; no improvement objective inferred. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-knowledge-policy](#epi-clm-knowledge-policy) | See record | See record | See record | [EPI-RTE-knowledge-assessment](#epi-rte-knowledge-assessment), [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer), [EPI-RTE-knowledge-validation](#epi-rte-knowledge-validation) | None supplied | No quality comparison; metadata can be caller-assigned | Strict knowledge retrieval enforces its policy, not factual correctness. This is consistent with the source's explicit metadata-not-proof qualification. | Canonical broad recall is a different path; current-data blocking cannot be generalized to it. “Exact miss” in the document's semantic diagram is narrower than runtime's semantic fallback after a nonreusable exact hit. |
| [RT-CLM-permission-scope](runtime.md#rt-clm-permission-scope) | See record | See record | See record | See record | See record | See record | Actor-aware authorization limits covered reads and writes, not the truth of authorized content. | See record; host and raw-API scope matters. |

## Bounded conclusion

MCMA retains imported statements and generated candidates, preserves source/lineage metadata, and makes both direct-answer and model-reference use possible. Acquisition is not production of warranted propositions. User source originals remain available in explicit memory; the organizer's output may differ, and its structural validator supplies no meaning comparison. Generated candidates default to unverified, but explicit saving, owner validation and inline editing assign stronger labels through separate routes. These are different admission mechanisms, not a universal human-review gate. See [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer), [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture), [EPI-RTE-knowledge-validation](#epi-rte-knowledge-validation), [EPI-RTE-answer-replacement](#epi-rte-answer-replacement).

The material automatic check targets **eligibility of a metadata-bearing record for direct knowledge reuse**. Its criterion is supported/verified state, sufficient confidence, acceptable freshness/current requirement and reuse policy, not independent evidence of answer truth. Its result enforces direct reuse/fallback in that scope. Semantic similarity and reranking add selection force, not new factual warrant. Canonical recall instead gives confirmed memory direct-answer authority through a maturity-to-validation mapping and does not consume currentRequired. Retraction in knowledge therefore cannot be assumed to withdraw the canonical source automatically. See [EPI-RTE-knowledge-assessment](#epi-rte-knowledge-assessment), [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer), [EPI-RTE-knowledge-validation](#epi-rte-knowledge-validation).

Owner decisions record changed reliance; their actual evidence, acceptance criterion, intended factual scope and exercise are unprovided. Thematic synchronization connects retained outputs to interaction references and topics, but this is derived organization and retention, not demonstrated lifecycle integration after evidence-consuming acceptance. Deterministic excerpt construction supports non-ampliative reshaping, not a new explanation. No inspected concrete candidate establishes an ampliative proposition accepted against evidence; this is a limit of this source/run evidence, not a verdict that every possible user review lacks warrant. See [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval), [EPI-RTE-thematic-summary](#epi-rte-thematic-summary).

Later reference consumption is a weaker authority path than direct answering. Selection can deliver material that strict direct reuse would require revalidating; connector instructions preserve its advisory/untrusted role but cannot enforce model obedience. No supplied observation demonstrates context influence or benefit. Parameter updates are not sent by the inspected inference connectors; exact model versions and provider-internal state remain uninspected as specified in the component records. Policy grants can directly change covered access behavior without any truth-apt claim route. Retention, classification and changing labels alone establish neither improved capacity, reflection, autonomous criticism nor exercised self-improvement. These remain independent questions, not one system-wide score. See [RT-RTE-context-supply](runtime.md#rt-rte-context-supply), [RT-BAP-memory-reference](runtime.md#rt-bap-memory-reference), [RT-RTE-permission-change](runtime.md#rt-rte-permission-change).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-knowledge-record
Label: KnowledgeRecord

Natural-language or JSON answer plus symbolic intent, provenance, confidence, validation history, freshness and relation fields. Storage: encrypted versioned library JSON under intent-derived knowledge references. SRC-1, `packages/core/src/Knowledge/KnowledgeRecord.php`, `packages/core/src/Knowledge/KnowledgeService.php`. Distinct from supplied policy/instruction objects: this is retained answer content consumed by [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer), not that route itself. No supplied operative-object counterpart after comparison.

> 'evidence_count' => count($provenance),
> --- `packages/core/src/Knowledge/KnowledgeRecord.php`

> if (($epistemic['evidence_count'] ?? -1) !== count($record['provenance'])) throw new RuntimeException('Knowledge evidence_count mismatch');
> --- `packages/core/src/Knowledge/KnowledgeRecord.php`

These checks establish a count of entries, not independent evidence assessment.

#### EPI-OBJ-canonical-memory
Label: Explicit canonical memory

Natural-language source and organized content with symbolic classification, retrieval and organization metadata, stored as encrypted versioned JSON under memory://user references. SRC-1, `packages/core/src/Memory/ExplicitMemoryService.php`. Output object of [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture), distinct from its static organizer instructions and from the knowledge mirror; no supplied object counterpart.

> 'source' => [
>     'type' => 'explicit-user-request',
>     'original' => $sourceText,
> ],
> --- `packages/core/src/Memory/ExplicitMemoryService.php`

#### EPI-OBJ-interaction-answer
Label: Interaction answer

Natural-language/JSON answer and question with symbolic route, provider, validation and relation metadata in the encrypted interaction archive; the storage and later consumers are supplied by [RT-RTE-web-request](runtime.md#rt-rte-web-request), SRC-1, `packages/core/src/Interaction/InteractionArchiveService.php`. Distinct from knowledge capture: archiving is independent of rememberGenerated. This declares the retained object, not a duplicate of the web route; no supplied operative-object counterpart. Evidence passages for independent archive writing and validation are in the cited runtime route and [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval).

#### EPI-OBJ-interaction-catalog
Label: Interaction catalog

Natural-language semantic labels/title consumed as symbolic lists in interaction catalog metadata, retained inside encrypted archive JSON. SRC-1, `packages/core/src/Interaction/InteractionCatalogService.php`, with persistence supplied by [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval). Distinct material part from the answer: classification affects organization, not its truth. No supplied operative-object counterpart. Its load-bearing prompt/cleaning evidence is in [EPI-RTE-catalog-classification](#epi-rte-catalog-classification).

#### EPI-OBJ-thematic-summary
Label: Thematic summary

Natural-language topic-prefixed answer excerpt plus symbolic validation, source_storage_hash and interaction references. Encrypted library JSON under topic/interaction-specific references; independently revisioned derived objects, not canonical question/answer transcripts. SRC-1, `packages/core/src/Interaction/ThematicSummaryService.php`. Distinct from the archive and knowledge mirror; supplied [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval) mentions synchronization but declares no counterpart object.

> 'source_storage_hash'=>$sourceStorageHash,
> --- `packages/core/src/Interaction/ThematicSummaryService.php`

### Routes

#### EPI-RTE-knowledge-assessment
Label: Knowledge metadata assessment

KnowledgeRecord::assess validates a record and computes eligibility; KnowledgeService::directAnswer consumes reusable before including answer/provenance/relations. Owner: PHP code, not a model or human evaluator. Context: currentRequired, minConfidence and time. Effects: returned symbolic decision, not changed source content. SRC-1, `packages/core/src/Knowledge/KnowledgeRecord.php`, `packages/core/src/Knowledge/KnowledgeService.php`. This isolates a reusable check used within [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) but also exposed by CLI knowledge-check and direct APIs; not coextensive with the supplied encompassing ask route. No supplied standalone assessment record.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reusable/decision/reasons/stale and status metadata; directAnswer includes stored answer only for reuse.
- Later read-back: inapplicable — assessment itself writes no retained result; it reads the current record on each invocation.
- Delegated visibility: inapplicable — deterministic PHP check delegates no evaluator call.
- Selection predicate: disputed/retracted or never-direct rejects; insufficient state/confidence, unacceptable age or nonimmutable current request yields revalidate; otherwise reuse.
- Invalidation or expiry: reference time is last_validated_at or captured_at; immutable bypasses age/current, always bypasses stale-only rejection, not validation/confidence/current conditions.
- Activation or effect: Direct-answer consumers enforce the reusable result; no independent factual check is licensed.
- Evidence limits: Metadata eligibility is implemented; source-truth evaluation, deployed execution and accuracy are unobserved.

> if (!in_array($state, ['supported','verified'], true)) $reasons[] = 'validation-insufficient';
> if ($confidence < $minConfidence) $reasons[] = 'confidence-below-threshold';
> --- `packages/core/src/Knowledge/KnowledgeRecord.php`

> if ($stale && $policy !== 'always') $reasons[] = 'stale';
> if ($currentRequired) $reasons[] = 'current-data-requested';
> --- `packages/core/src/Knowledge/KnowledgeRecord.php`

> if ($assessment['reusable']) {
>     $result['answer'] = $record['answer'];
>     $result['provenance'] = $record['provenance'];
>     $result['relations'] = $record['relations'];
> --- `packages/core/src/Knowledge/KnowledgeService.php`

PHP proposes the decision, the caller supplies thresholds/current requirement, and consuming PHP branches enforce it. No human per-item approval or answer oracle is invoked by this check. Mode: open retrieval requests, not an improvement experiment. Revalidate is a disposition request, not evidence of completed external research.

#### EPI-RTE-knowledge-validation
Label: Knowledge validation state update

CLI knowledge-validate and web memory confirm/discard reach KnowledgeService::validateKnowledge/validateId and KnowledgeRecord::withValidation. Caller proposes state, confidence, reason and optional additional provenance; PHP checks structure/permissions and retains a new revision. SRC-1, `packages/core/src/Cli/CliApplication.php`, `packages/core/src/Web/WebApplication.php`, `packages/core/src/Knowledge/KnowledgeService.php`, `packages/core/src/Knowledge/KnowledgeRecord.php`. Distinct from [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval): target is a knowledge record directly, not an interaction and its associated synchronization. Related [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) later consumes the result but does not own this admission route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated revision/state/confidence; web additionally returns inspection and optional semantic synchronization.
- Later read-back: Knowledge assessment and answer selection use the new state/time/confidence; history and appended provenance persist.
- Delegated visibility: Web resolves session principal then performs owner-role update; optional embedding receives content for refresh, not factual review authority.
- Selection predicate: Existing actor-readable record, valid state/confidence and nonempty reason; web restricts actions to confirm/discard, CLI accepts supported state vocabulary.
- Invalidation or expiry: New status supersedes current eligibility; web discard maps to retracted/0.0. This route does not edit canonical maturity in a related explicit memory.
- Activation or effect: State update can permit or block subsequent direct knowledge reuse; actual use unobserved.
- Evidence limits: Actor string is not evidence of human deliberation. Optional provenance and a reason do not prove evidence was inspected or a factual criterion met.

> $targetState=$action==='confirm'?'verified':'retracted';
> $targetConfidence=$action==='confirm'?0.95:0.0;
> --- `packages/core/src/Web/WebApplication.php`

> $record['epistemic']['last_validated_at'] = $at;
> --- `packages/core/src/Knowledge/KnowledgeRecord.php`

> $record = KnowledgeRecord::withValidation($record, $state, $confidence, $reason, $additionalProvenance);
> --- `packages/core/src/Knowledge/KnowledgeService.php`

Trigger: explicit caller validation. Software can reject malformed/unauthorized updates, not independently contradict an authorized factual judgment. Guidance is the state/schema vocabulary; persisted change is metadata/history/provenance. Later updates can change status again; revision lineage is not an automatic rollback transaction. No answer oracle; open owner/caller review, no improvement curriculum. No source text for an evidence-consuming truth acceptance criterion is supplied.

#### EPI-RTE-answer-replacement
Label: Owner answer replacement

Web editKnowledgeObject calls KnowledgeService::replaceAnswerId, replacing answer text and setting stable/year-long reuse metadata and verified/0.95 status. SRC-1, `packages/core/src/Web/WebApplication.php`, `packages/core/src/Knowledge/KnowledgeService.php`. Distinct from [RT-RTE-memory-mutation](runtime.md#rt-rte-memory-mutation), which targets canonical memories, and from validation-only updates above. It is not a renamed interaction-approval route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Revision hashes, verified status and optional refreshed semantic entry; web reinspection/billing result.
- Later read-back: Replaced answer and refreshed metadata reach knowledge assessment and retrieval; current hash changes.
- Delegated visibility: Caller supplies replacement; server uses owner; optional embedding provider indexes, not judges, it.
- Selection predicate: Existing valid knowledge ID; trimmed nonempty replacement no more than 32768 bytes; actor-authorized update.
- Invalidation or expiry: Old revision hash retained; freshness becomes stable with 31536000 seconds; later state changes can withdraw direct reuse.
- Activation or effect: New answer text becomes current and labelled verified without a separate content evaluator.
- Evidence limits: No observed edit, truth check, actual later use or atomic semantic-refresh guarantee.

> $record['answer']=[
>     'format'=>'text',
>     'value'=>$answer,
> ];
> --- `packages/core/src/Knowledge/KnowledgeService.php`

> $record=KnowledgeRecord::withValidation(
>     $record,
>     'verified',
>     0.95,
>     'owner-edited-in-library',
>     $additionalProvenance
> );
> --- `packages/core/src/Knowledge/KnowledgeService.php`

Caller proposes/decides content; software enforces shape and access but supplies no factual veto or answer oracle. Trigger is open user editing; bounds and permission checks guide admission, not an improvement objective. Rejection is for bad input/access; previous hashes provide history, no automatic rollback. This imports a replacement with unknown source warrant rather than deriving it from the earlier record.

#### EPI-RTE-catalog-classification
Label: Interaction catalog classification
Part of: [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval)

This is the optional classification subroute of interaction approval, not the whole approval decision. InteractionCatalogService sends question, answer and existing catalog to a generator with data-only/no-invention instructions; PHP decodes and cleans the result or uses deterministic fallback. SRC-1, `packages/core/src/Interaction/InteractionCatalogService.php`. Natural-language labels become symbolic organization fields; answer truth remains unevaluated.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Catalog with provider/usage metadata or fallback/error status.
- Later read-back: Approval persists catalog in interaction; thematic topic selection consumes topics/projects/entities. General topic correctness is unverified.
- Delegated visibility: Model receives question/answer/existing catalog, not Library access.
- Selection predicate: Configured provider attempts classification; absent provider or exception uses fallback; arrays/labels are cleaned and bounded.
- Invalidation or expiry: Empty returned topics fall back to existing topics; later classification may replace topic organization and supersede derived summaries.
- Activation or effect: Semantic labels influence retained thematic paths; they do not revise the answer or establish its truth.
- Evidence limits: No observed classification, fidelity metric or causal benefit; provider internals uninspected.

> - Do not invent names, relationships, projects, people or characters.
> --- `packages/core/src/Interaction/InteractionCatalogService.php`

> 'classification_status'=>'classified-on-owner-approval',
> --- `packages/core/src/Interaction/InteractionCatalogService.php`

> $item=self::clean($item,80);
> if($item!==''&&!in_array($item,$out,true)) $out[]=$item;
> if(count($out)>=8) break;
> --- `packages/core/src/Interaction/InteractionCatalogService.php`

Proposer: optional model, or fallback from existing catalog. Decider/veto: PHP JSON/label processing with exception fallback; owner approves interaction before this returned classification, not each new label afterward. Mode is open review, not an experiment. No answer oracle. Guidance requests source-faithful cataloging; what persists is labels/status, not checked criticisms of the answer.

#### EPI-RTE-thematic-summary
Label: Deterministic thematic synchronization

InteractionArchiveService synchronization invokes ThematicSummaryService::sync, which derives topics from catalog or canonical classification, extracts an answer excerpt, persists per-topic payloads and supersedes obsolete topic paths. SRC-1, `packages/core/src/Interaction/ThematicSummaryService.php`; archive invocation is supplied by [RT-RTE-web-request](runtime.md#rt-rte-web-request) and [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval). Distinct submechanism spanning persistence and validation triggers, not a duplicate of either encompassing route. It performs extraction/retention, not generative criticism.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Relevant/no-topic result, summary revision metadata and zero model usage.
- Later read-back: Existing derived objects are reloaded for update/supersession. Broad canonical recall excludes thematic summaries; no new direct-answer authority is established for this derived text.
- Delegated visibility: inapplicable — deterministic library operations make no model call.
- Selection predicate: Catalog topics take precedence, otherwise projects/entities and nongeneric canonical category labels, bounded to fallback topic limits.
- Invalidation or expiry: Changed desired paths mark old objects superseded and trusted_for_conclusions=false; current payload records source_storage_hash. This hash alone is not a consumer-side freshness check.
- Activation or effect: Retained topic organization and trust flag derive from existing source metadata; no observed later factual reliance.
- Evidence limits: Does not independently verify the answer; trusted flag is not evidence of a downstream consumer enforcing acceptance. Broader thematic readers were not exhaustively inspected.

> $answerText=self::excerpt($answerText,220);
> --- `packages/core/src/Interaction/ThematicSummaryService.php`

> $parts=['Tema: '.$topic.'.'];
> if($answerText!=='') $parts[]='Punto derivado: '.$answerText;
> --- `packages/core/src/Interaction/ThematicSummaryService.php`

> $sentences=preg_split('/(?<=[.!?])\s+/u',$value,2);
> $first=trim((string)($sentences[0]??$value));
> return $first!==''?$first:$value;
> --- `packages/core/src/Interaction/ThematicSummaryService.php`

> 'trusted_for_conclusions'=>$state==='verified'&&$confidence>=0.75,
> --- `packages/core/src/Interaction/ThematicSummaryService.php`

Concrete source deduction, not execution: with topic `Release` and answer `The release is ready. Only for staging.`, clean leaves the short ASCII text unchanged, excerpt splits at the first period-plus-space, and summaryText produces `Tema: Release. Punto derivado: The release is ready.` The second sentence's scope restriction is lost. This establishes deterministic non-ampliative extraction with a fidelity limit, not novel factual derivation. Source premises remain no more warranted than their input.

Supersession evidence is supplied by [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval). The canonical exclusion is an implemented countercase to treating every confirmed derived summary as a direct answer:

> if(
>     (is_array($content)&&isset($content['thematic_summary_version']))
>     || preg_match('#^memory://user/temas/[^/]+/resumenes/#',$logicalRef)===1
> ){
>     return null;
> }
> --- `packages/core/src/Context/BroadMemoryRecallBuilder.php`

### Claims

#### EPI-CLM-knowledge-policy
Label: Remembered knowledge reuse policy

SRC-1 doctrine/design, `docs/KNOWLEDGE-REUSE.md`: exact reuse is metadata-gated; semantic similarity does not override permissions or epistemic policy, and nonimmutable current requests require revalidation. This is not a proof claim. Distinct from supplied [RT-CLM-permission-scope](runtime.md#rt-clm-permission-scope): it concerns answer admissibility and qualification of epistemic metadata, not only authorization APIs.

> Only `reuse` returns the remembered answer.
> --- `docs/KNOWLEDGE-REUSE.md`

> Similarity does not override permissions or epistemic policy.
> --- `docs/KNOWLEDGE-REUSE.md`

> Confidence and provenance are epistemic metadata, not absolute proof.
> --- `docs/KNOWLEDGE-REUSE.md`

> A caller can set `currentRequired=true`. Non-immutable remembered knowledge then requires revalidation even when semantic similarity is high.
> --- `docs/KNOWLEDGE-REUSE.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
