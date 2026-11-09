---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "MCMA-OpenMemory memory report: encrypted revisions, distinct knowledge and interaction consumers, derived indexes and bounded context reload."
run-id: AAS-2026-11-08-mcma-openmemory-a023f4989e1c-01
source-identity: https://github.com/jimmybackend/mcma-openmemory
reviewed-boundary: "556954d95f0d6d6894c5d46ffcc25a907150b0a7"
---

# MCMA-OpenMemory memory report

## Boundary and evidence

This report covers the retained-state paths inside [boundary.md](boundary.md): generic encrypted objects, canonical explicit memory, knowledge records and their access metadata, interaction transcripts, conversation discovery, thematic derivatives, semantic vectors, context traces and the context inspector's catalog. CLI dispatch and exposed service operations are included, not only web asking. Permission policy is retained machine authority; vault bytes have a different consumer boundary from ordinary memory. Deployment state and billing/account state are included in the supplied runtime account but are not classified here as answer memory. External provider weights, live storage contents and actual user review are unavailable; source text cannot establish deployed contents or model activation.

All new findings use SRC-1 implementation at the frozen commit. HEAD was rechecked as 556954d95f0d6d6894c5d46ffcc25a907150b0a7. Direct reads added the paths below to the boundary's initial inspection. Supplied runtime findings are explicitly marked; their supporting quotations need not be repeated. Available but uninspected alternatives remain limits, not absences.

| Entry point or operation | Paths in SRC-1 | Coverage and limit |
|---|---|---|
| CLI write/update/read/list/tree/temperature, migration, storage copy | `packages/core/src/Cli/CliApplication.php`, `packages/core/src/Library.php`, `packages/core/src/Storage/StorageMigrator.php` | Direct dispatch and storage reads; [MEM-OBJ-library-index](#mem-obj-library-index), [MEM-RTE-library-authoring](#mem-rte-library-authoring). Historical decryption internals and each remote adapter's concurrency semantics uninspected; no universal migration/security guarantee. |
| CLI knowledge put/check/show/validate and librarian remember/validate/deindex | `packages/core/src/Knowledge/KnowledgeService.php`, `packages/core/src/Knowledge/KnowledgeRecord.php`, `packages/core/src/Agent/Librarian.php` | Direct reads; [MEM-OBJ-knowledge-answer](#mem-obj-knowledge-answer), [MEM-OBJ-knowledge-metadata](#mem-obj-knowledge-metadata), [MEM-RTE-knowledge-editing](#mem-rte-knowledge-editing). Supplied [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) supplies generation capture. |
| Explicit web save, canonical mutation and approval/discard | `packages/core/src/Memory/ExplicitMemoryService.php`, `packages/core/src/Memory/MemoryMutationService.php`, `packages/core/src/Interaction/InteractionArchiveService.php` | Explicit capture payload directly read; mutation and approval progression supplied by [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture), [RT-RTE-memory-mutation](runtime.md#rt-rte-memory-mutation), [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval); archive validation also directly read. Canonical/mirror atomicity is not established. |
| Semantic full/incremental index, hash refresh/removal, top-K | `packages/core/src/Semantic/SemanticIndexService.php` | Direct reads of these operations through answer selection; [MEM-OBJ-semantic-vectors](#mem-obj-semantic-vectors), [MEM-RTE-semantic-maintenance](#mem-rte-semantic-maintenance). Provider internals unavailable; component identities supplied by runtime. |
| Archive, request recovery, conversation reopen, context candidates and navigation | `packages/core/src/Interaction/InteractionArchiveService.php`, `packages/core/src/Web/WebApplication.php` | Direct archive/read/recovery/candidate/index/tree reads; web recovery also supplied by [RT-RTE-web-request](runtime.md#rt-rte-web-request). [MEM-OBJ-interaction](#mem-obj-interaction), [MEM-OBJ-conversation-index](#mem-obj-conversation-index). UI execution unobserved. |
| Topic catalog and thematic synchronization | `packages/core/src/Interaction/InteractionCatalogService.php`, `packages/core/src/Interaction/ThematicSummaryService.php`, `tests/integration/thematic-interaction-summaries.php` | Direct service reads and selected test assertions; [MEM-OBJ-thematic-summary](#mem-obj-thematic-summary), [MEM-RTE-thematic-sync](#mem-rte-thematic-sync). Tests are expected behavior, not passing-run evidence. |
| Conversation/multi-memory/broad recall and generation delivery | `packages/core/src/Context/ConversationContextBuilder.php`, `packages/core/src/Context/MultiMemoryContextBuilder.php`, `packages/core/src/Context/BroadMemoryRecallBuilder.php` | Direct selector reads; wiring/connector delivery supplied by [RT-RTE-context-supply](runtime.md#rt-rte-context-supply), [RT-BAP-memory-reference](runtime.md#rt-bap-memory-reference). No tokenizer-wide bound or compliance conclusion. |
| Trace recording and context inspector | `packages/core/src/Context/ContextTraceService.php`, `packages/core/src/Web/WebApplication.php` | Direct trace/catalog implementation and GET route; [MEM-OBJ-context-traces](#mem-obj-context-traces), [MEM-OBJ-context-catalog](#mem-obj-context-catalog), [MEM-RTE-inspector-snapshot](#mem-rte-inspector-snapshot). Browser rendering remains supplied/search-level coverage, not observed operation. |
| Policy initialization/change and vault put/list/delete/use | `packages/core/src/Library.php` | Direct reads; annotations on [RT-OBJ-permission-policy](runtime.md#rt-obj-permission-policy), [MEM-OBJ-vault](#mem-obj-vault). No later model route is inferred for vault contents. |
| Static role prompts, providers, installation and evaluations | `spec/1.0/AGENTS.md`, `packages/connectors/local/src/OllamaGenerationProvider.php`, `install.sh` | Supplied runtime evidence, not additional direct reads. Static instructions are not acquired memory; deployment remains [RT-RTE-deploy-checkout](runtime.md#rt-rte-deploy-checkout). Evaluator coverage beyond the thematic assertions is uninspected here; prevents measured learning claims. |

The CLI's inspected switch contains concrete command dispatch rather than a model tool registry or event-hook memory scheduler. Its `ask` lacks the web context builders and archive wiring ([RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer)). Exposed low-level library calls remain alternative admission paths; web defaults must not be generalized to all callers.

## Core ideas

1. **One encrypted substrate does not mean one memory policy.** Canonical explicit content, its knowledge mirror, the archived interaction and topic derivative have separate representations, revisions and consumers. Canonical recall can return confirmed content even when strict knowledge freshness would require revalidation. See [MEM-OBJ-explicit-memory](#mem-obj-explicit-memory) and [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer).
2. **Knowledge admission labels govern code, not truth.** Symbolic confidence/state/freshness gates can prevent direct reuse, while less restrictive context routes still deliver marked material. The source retains reasons and provenance, but the consumer often selects only a bounded summary of them. See [MEM-OBJ-knowledge-metadata](#mem-obj-knowledge-metadata) and the context annotation.
3. **Context is reconstructed, not an ever-growing agent window.** Code reloads selected archived turns and knowledge by value. It clips fields and excludes excess candidates, leaving originals durable. These are request-driven read-back paths, not independent unsolicited push and not isolated worker stack frames. See [RT-RTE-context-supply](runtime.md#rt-rte-context-supply).
4. **Trace-derived state has different horizons.** Conversation indexes shape later discovery; thematic snippets support browsing but are excluded from canonical recall; context traces support inspection. Retention alone does not give all three model authority or demonstrate improved capacity. See [MEM-OBJ-conversation-index](#mem-obj-conversation-index), [MEM-OBJ-thematic-summary](#mem-obj-thematic-summary), [MEM-OBJ-context-traces](#mem-obj-context-traces).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-library-index
Label: Library manifest and root index

SRC-1, `packages/core/src/Library.php`. Symbolic manifest/root-index JSON maps logical refs to object IDs and current storage hashes, with temperature, cognitive layer and scope metadata. It is encrypted in content-addressed envelopes through the selected StorageAdapter; `manifest.mcma` is the replaceable entry pointer. This is access infrastructure, not readable answer content. Initialized by Library, revised on writes, consumed by later list/read/write operations across sessions. New revisions preserve old hashes, while current lookup uses the new root pointer. This is distinct from [RT-OBJ-permission-policy](runtime.md#rt-obj-permission-policy): the index locates objects; policy decides actor-aware access.

> $index['payload']['entries'][$entryPosition] = $newEntry; self::sortEntries($index['payload']['entries']); $this->replaceRootIndex($index['envelope']['protected']['object_id'], $index['payload']);
> --- `packages/core/src/Library.php`

> return 'objects/' . substr($digest, 0, 2) . '/' . substr($digest, 2, 2) . '/' . $digest . '.mcma';
> --- `packages/core/src/Library.php`

#### MEM-OBJ-knowledge-answer
Label: KnowledgeRecord intent and answer

SRC-1, `packages/core/src/Knowledge/KnowledgeRecord.php`, `packages/core/src/Knowledge/KnowledgeService.php`. The natural-language question and answer (or caller-specified JSON/XML/other allowed answer format) live inside encrypted JSON objects at question-normalization hashes. Format labels alone do not determine how arbitrary JSON answer payloads mean something to their eventual caller. The normalized intent/key are symbolic addressing units; answer text is interpreted by humans/models or copied by code. Content provenance can originate with callers, generated answers, explicit-memory mirrors or approved interactions. Direct reuse consumers copy the answer; RAG serializes selected text; inspect APIs expose content/history. Distinct from [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer), which produces/consumes this object rather than being the object.

> return 'memory://knowledge/q-' . substr(self::intentKey($question), 7);
> --- `packages/core/src/Knowledge/KnowledgeRecord.php`

> if ($assessment['reusable']) {
>     $result['answer'] = $record['answer'];
>     $result['provenance'] = $record['provenance'];
>     $result['relations'] = $record['relations'];
> --- `packages/core/src/Knowledge/KnowledgeService.php`

#### MEM-OBJ-knowledge-metadata
Label: KnowledgeRecord validation and freshness

SRC-1, `packages/core/src/Knowledge/KnowledgeRecord.php`. Distinct operative part of the same stored knowledge objects as [MEM-OBJ-knowledge-answer](#mem-obj-knowledge-answer), not a separate physical store. Symbolic state, confidence, timestamps, freshness class, max age, reuse policy and history drive `assess`; provenance entries and history reasons also contain natural-language descriptions. Reasons are retained on validation; inspectId returns history, while directAnswer primarily returns assessment reasons rather than full historical rationale. Evidence count counts supplied provenance entries, not independently verified evidence. No exact supplied object counterpart; [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval) is one updater.

> $record['epistemic']['history'][] = [
>     'at' => $at,
>     'validation_state' => $state,
>     'confidence' => $confidence,
>     'reason' => $reason,
> ];
> --- `packages/core/src/Knowledge/KnowledgeRecord.php`

> if (!in_array($state, ['supported','verified'], true)) $reasons[] = 'validation-insufficient';
> if ($confidence < $minConfidence) $reasons[] = 'confidence-below-threshold';
> --- `packages/core/src/Knowledge/KnowledgeRecord.php`

#### MEM-OBJ-explicit-memory
Label: Explicit canonical memory

SRC-1, `packages/core/src/Memory/ExplicitMemoryService.php`. Encrypted JSON under `memory://user/...`: natural-language normalized content/title plus original user text; symbolic classification, retrieval question/ref and organizer status/provider metadata. Subparts have different force: code routes by metadata, broad recall uses content as answer, the original is retained lineage rather than a guaranteed verbatim delivered answer. Source fingerprint reuses a canonical ref; revisions persist through Library. Distinct object produced by [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture), guided by [RT-OBJ-organizer-instructions](runtime.md#rt-obj-organizer-instructions); no duplicate object declaration in runtime.

> 'source' => [
>     'type' => 'explicit-user-request',
>     'original' => $sourceText,
> ],
> --- `packages/core/src/Memory/ExplicitMemoryService.php`

> 'organization' => [
>     'status' => $organization['status'],
>     'provider_id' => $organization['provider_id'],
>     'model_output_valid' => $organization['model_output_valid'],
> ],
> --- `packages/core/src/Memory/ExplicitMemoryService.php`

Confirmed maturity is software-assigned after optional organization, not proof of a human checking the rewritten text. The verified mirror can diverge or fail independently; mutation writes tombstones and keeps encrypted history ([RT-RTE-memory-mutation](runtime.md#rt-rte-memory-mutation)).

#### MEM-OBJ-semantic-vectors
Label: Semantic index entries

SRC-1, `packages/core/src/Semantic/SemanticIndexService.php`. Encrypted JSON index addressed by a hash of provider ID; numerical normalized vectors are dense representations derived from normalized questions, not learned answer weights. Symbolic provider/dimensions/ref/object/hash fields bind them to current records. These parts are distinct from readable answer text; a vector is not an opaque transcript summary. `topK` compares query vectors then rereads actor-visible current-hash knowledge for assessment. Mutable provider endpoint/weight limits are [RT-CMP-ollama-embedding-provider](runtime.md#rt-cmp-ollama-embedding-provider), [RT-CMP-llama-cpp-embedding](runtime.md#rt-cmp-llama-cpp-embedding), [RT-CMP-bedrock-titan-embedding](runtime.md#rt-cmp-bedrock-titan-embedding). The index is a distinct retained result, not those external model components.

> return 'memory://system/semantic-index/p-' . hash('sha256', $provider->id());
> --- `packages/core/src/Semantic/SemanticIndexService.php`

> $vector = VectorMath::normalize($provider->embed($record['intent']['normalized']));
> --- `packages/core/src/Semantic/SemanticIndexService.php:30-36`

> if (!hash_equals($visible[$ref]['storage_hash'], $entry['storage_hash'])) {
>     $staleEntries++;
>     continue;
> }
> --- `packages/core/src/Semantic/SemanticIndexService.php`

#### MEM-OBJ-interaction
Label: Canonical interaction archive

SRC-1, `packages/core/src/Interaction/InteractionArchiveService.php`. Encrypted JSON at dated conversation/request refs retains question/answer text or values, provider, route, relations, catalog, billing summary and independent validation history. It is an application-level transcript, not a raw provider reasoning/tool trace. Natural-language content and symbolic validation/relations have separate consumption: reopen/recovery returns answer, context builder clips question/answer, approval changes eligibility. Initial unverified/0.5 is independent of any knowledge record's validation. Producer/consumer progression already belongs to [RT-RTE-web-request](runtime.md#rt-rte-web-request); this object is not a duplicate of that route.

> $stored=$this->library->writeAs(
>     $actor,$logicalRef,$interaction,'json','hot','30-episodic','session','observed'
> );
> --- `packages/core/src/Interaction/InteractionArchiveService.php`

#### MEM-OBJ-conversation-index
Label: Conversation index

SRC-1, `packages/core/src/Interaction/InteractionArchiveService.php`. Owner-only encrypted derived JSON at `memory://system/conversation-index` holds canonical refs, recent refs/times, compact question/catalog/validation items and conversation titles. Symbolic reference/order fields determine discovery; titles/labels are natural-language display/search material. It does not replace the archived answers. Archive and validation update it; conversation/index calls can rebuild it from canonical refs. The recent list caps at 32, but original refs persist. Actual context candidate answers are reread through the requesting actor; possession of owner-discovered refs is not permission. This is distinct from [RT-RTE-context-supply](runtime.md#rt-rte-context-supply), the later delivery route.

> if(count($recent)>32) $recent=array_slice($recent,-32);
> --- `packages/core/src/Interaction/InteractionArchiveService.php`

> $detail=$this->read($actor,$logicalRef);
> --- `packages/core/src/Interaction/InteractionArchiveService.php:363-366`

#### MEM-OBJ-thematic-summary
Label: Thematic summaries

SRC-1, `packages/core/src/Interaction/ThematicSummaryService.php`, `packages/core/src/Context/BroadMemoryRecallBuilder.php`. Encrypted JSON under personal topic paths retains a bounded natural-language answer-derived snippet and symbolic source hash/ref, state, confidence, trust flag, classification and relations. Deterministic clipping is not generative reflection or a full transcript copy. The source interaction retains the full question/answer. Topic origins may include optional model catalog classification; the summarizer itself does not call a model. Consumer proven here is owner library browsing, not model recall: BroadMemoryRecallBuilder explicitly excludes these objects. Thus `trusted_for_conclusions` is stored metadata, not evidence of a model relying on it. It is a distinct derivative of [MEM-OBJ-interaction](#mem-obj-interaction); supplied [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval) names its refresh but not its object identity.

> $answerText=self::excerpt($answerText,220);
> --- `packages/core/src/Interaction/ThematicSummaryService.php`

> 'note'=>'Derived thematic summary; canonical question/answer remain only in the interaction archive',
> --- `packages/core/src/Interaction/ThematicSummaryService.php`

> (is_array($content)&&isset($content['thematic_summary_version']))
> || preg_match('#^memory://user/temas/[^/]+/resumenes/#',$logicalRef)===1
> --- `packages/core/src/Context/BroadMemoryRecallBuilder.php`

#### MEM-OBJ-context-traces
Label: Context traces

SRC-1, `packages/core/src/Context/ContextTraceService.php`. Owner-private encrypted JSON records request question, current/remember flags, route/provider, memory_attempt, context_used, storage and billing summaries. Natural-language question/context payloads coexist with symbolic diagnostics. The newest 50 entries remain in the current object; Library retains earlier encrypted revisions. Consumer established is the context inspector, not automatic parameter/rule revision. This differs from the answer transcript and from [RT-RTE-web-request](runtime.md#rt-rte-web-request), its producer.

> array_unshift($entries, $trace);
> $entries = array_slice($entries, 0, self::MAX_TRACES);
> --- `packages/core/src/Context/ContextTraceService.php`

#### MEM-OBJ-context-catalog
Label: Context knowledge catalog

SRC-1, `packages/core/src/Context/ContextTraceService.php`. Encrypted owner-private JSON cache at `memory://system/context-knowledge-catalog` stores question/display information, hash linkage, validation/confidence/temperature, captured time, reusable flag, provider provenance and validity/error fields. Symbolic counters/eligibility and natural-language labels support inspector summaries, not answer generation. Snapshot refreshes up to eight changed/missing knowledge entries per call, reports pending entries, and removes refs missing from current knowledge listing. Hash identity invalidates changed records, but unchanged hashes do not force recomputation of time-dependent freshness: the cached reusable flag is not necessarily current. Distinct from [RT-OBJ-permission-policy](runtime.md#rt-obj-permission-policy) and the live assessment in [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer).

> $cached!==null
> &&hash_equals((string)($cached['storage_hash']??''),(string)$identity['storage_hash'])
> --- `packages/core/src/Context/ContextTraceService.php`

> if($processed>=self::CATALOG_BATCH) continue;
> --- `packages/core/src/Context/ContextTraceService.php`

#### MEM-OBJ-vault
Label: Vault payload

SRC-1, `packages/core/src/Library.php`. Separate encrypted vault-container JSON, with opaque secret bytes and symbolic named-entry metadata. Secrets are not knowledge propositions, and metadata listing does not expose secret content. Management writes/deletes require manage_vault; `useVaultSecret` supplies the secret to a trusted callback under use_secret. This establishes an exposed later-use capability, not a deployed model-consumer route. Prior revisions remain through Library. Distinct from [RT-OBJ-permission-policy](runtime.md#rt-obj-permission-policy), which authorizes rather than contains secrets.

> if ($logicalRef === 'memory://access/vault') throw new RuntimeException('Vault contents cannot be read through the ordinary memory API');
> --- `packages/core/src/Library.php`

> $secret = VaultPayload::secret($payload['content'], $name);
> try {
>     return $operation($secret);
> --- `packages/core/src/Library.php`

### Routes

#### MEM-RTE-library-authoring
Label: Generic authoring and portable migration

SRC-1, `packages/core/src/Cli/CliApplication.php`, `packages/core/src/Library.php`, `packages/core/src/Storage/StorageMigrator.php`. Caller selects content/ref/metadata through CLI or library APIs; Library validates format/ref/metadata and writes encrypted revisions plus index/manifest changes. Historical import additionally records migration provenance/fingerprint and rejects duplicates; storage-copy transfers ciphertext before publishing the manifest. PHP owns persistence, caller owns supplied content. Unlike [RT-RTE-memory-mutation](runtime.md#rt-rte-memory-mutation), this surface accepts general objects and does not inherently synchronize knowledge mirrors.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Object/ref/hash/revision, temperature outcome or copy/migration metadata; CLI read later decodes stored content including binary base64url.
- Later read-back: Shipped CLI read/list/tree reopens retained library state; generic library read is also an afforded API capability, not proof of arbitrary external consumers.
- Delegated visibility: Trusted PHP host holds Library/storage; CLI actor-aware wrappers check permissions. Actor-less APIs have the supplied runtime's protocol limits.
- Selection predicate: Explicit logical ref for read/update and caller-selected metadata; index list/tree enumerate actor-visible refs rather than relevance-targeting.
- Invalidation or expiry: Update replaces current index hash, preserves previous hash; import rejects occupied refs/fingerprints; copy rejects an existing destination manifest. Temperature update alone is metadata revision, not deletion.
- Activation or effect: Later read/list/tree receives current stored content/metadata; no generic model delivery follows solely from successful write.
- Evidence limits: Source capability and shipped CLI wiring only; copy integrity checks are byte comparisons, not proof of factual correctness, remote atomicity or secure erasure.

Admission is caller proposal plus software permission/shape checks; caller may be human or software, so per-content human approval remains unresolved for direct APIs. No answer oracle or improvement curriculum is involved. Prior hashes supply recovery lineage rather than an exercised rollback. Migration preserves caller-provided plaintext content and provenance; it does not prove semantic equivalence by format labels alone.

> $metadata['logical_refs'] = $entry['logical_refs']; $metadata['revision'] = max(1, (int)($metadata['revision'] ?? 1)) + 1; $metadata['previous_storage_hash'] = $entry['storage_hash'];
> --- `packages/core/src/Library.php`

> if (!hash_equals(hash('sha256', $sourceObject['bytes']), hash('sha256', $roundTrip['bytes']))) throw new RuntimeException('Provider migration byte mismatch: ' . $locator);
> --- `packages/core/src/Storage/StorageMigrator.php`

#### MEM-RTE-knowledge-editing
Label: Direct knowledge editing and validation

SRC-1, `packages/core/src/Knowledge/KnowledgeService.php`, `packages/core/src/Agent/Librarian.php`, `packages/core/src/Cli/CliApplication.php`, `packages/core/src/Web/WebApplication.php`. CLI capture/validation and owner web answer editing bypass automatic generated-answer defaults. Caller supplies answer/state/reason; software validates and persists. Answer replacement keeps intent, marks verified/0.95, sets stable one-year freshness and adds provenance/history. Web refreshes semantic hash linkage when configured. This is distinct from [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval), which acts on an archived interaction, and [RT-RTE-memory-mutation](runtime.md#rt-rte-memory-mutation), which targets canonical memory.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Edited/validated record identity, revision and status; rename changes display_title without changing intent.
- Later read-back: Knowledge direct/semantic retrieval, browser inspect and context selectors consume the new record subject to their separate gates.
- Delegated visibility: Web edits execute as owner; Librarian validation executes as librarian; caller-supplied actor is not proof of actual human review.
- Selection predicate: Knowledge ID or normalized question targets the record; nonempty bounded edited answer and valid state/confidence/reason admit changes.
- Invalidation or expiry: New storage hash invalidates old semantic entry until refreshed/reindexed. Retraction changes eligibility without erasing text/history. Replacement resets freshness; metadata-only renaming does not rewrite normalized intent.
- Activation or effect: Symbolic status affects subsequent reuse; changed answer can become direct output. Semantic refresh preserves vector because question is unchanged.
- Evidence limits: No independent fact checker or observed user review; knowledge-only edits do not establish canonical original/mirror synchronization.

Proposal/veto belong to caller and permission/schema gates, not model judgment. Mode is open editing, not bounded experiment; no answer oracle is consulted. Existing records can be overwritten by capture, unlike AskService's existing-exact preservation. Guidance is caller content plus fixed schema. Library retains previous revisions; no automatic rollback is shown.

> $record=KnowledgeRecord::withValidation(
>     $record,
>     'verified',
>     0.95,
>     'owner-edited-in-library',
>     $additionalProvenance
> );
> --- `packages/core/src/Knowledge/KnowledgeService.php`

#### MEM-RTE-semantic-maintenance
Label: Semantic index maintenance

SRC-1, `packages/core/src/Semantic/SemanticIndexService.php`, `packages/core/src/Agent/Librarian.php`. CLI full rebuild, Librarian incremental capture/validate and web metadata refresh feed the retained index. Code selects normalized intent, calls configured embedding inference when needed, checks dimensions and persists. Deindex removes a vector entry, not knowledge. Distinct from [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer), the answer consumer.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Index/ref/hash/revision, unchanged/refreshed/removed metadata; dimensional mismatch rejects updates.
- Later read-back: topK loads provider-keyed vectors for later query embedding comparison, then reads current actor-visible knowledge; direct-answer and multi-memory routes consume its candidates.
- Delegated visibility: Embedding provider receives normalized questions, not entire answers or a library handle; current answer text is reread locally.
- Selection predicate: Full rebuild indexes actor-visible knowledge refs; incremental write targets a knowledge ref; provider ID selects the index; current-hash equality gates candidates.
- Invalidation or expiry: Changed storage hashes skip stale entries; refreshStoredEntry preserves existing vector while updating identity/hash; remove deletes only index entry. Provider ID need not change when external weights change.
- Activation or effect: Retained numerical representation affects deterministic ranking and candidate availability, not model weights.
- Evidence limits: No measured retrieval improvement or full provenance of external embedding training; same-ID weight drift may escape provider-key separation.

Caller/service invocation initiates maintenance; code admits provider vectors after shape/dimension validation, without per-vector human review or answer oracle. No improvement curriculum or automatic fact verification is implied. Library revision lineage provides prior index states, not an observed rollback transaction.

> // Validation/freshness metadata changed, but the normalized question did not.
> // Preserve the existing vector and refresh only the identity/hash linkage.
> --- `packages/core/src/Semantic/SemanticIndexService.php`

#### MEM-RTE-thematic-sync
Label: Interaction to thematic derivative

SRC-1, `packages/core/src/Interaction/ThematicSummaryService.php`, `packages/core/src/Interaction/InteractionCatalogService.php`, `packages/core/src/Interaction/InteractionArchiveService.php`, `packages/core/src/Web/WebApplication.php`. Archive/validation triggers code to choose catalog topics, else projects/entities/canonical category fallback, build deterministic snippet records and persist changed payloads. Approval's optional catalog model labels the interaction under fixed cataloger instructions; sanitized labels are admitted without separate per-label approval. Thematic derivation is a distinct downstream part of [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval), not a second declaration of approval.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Derived refs and created/updated/unchanged outcomes or caught synchronization error.
- Later read-back: Library tree lists user-topic leaves; GET library-object reads their content as owner. Canonical broad recall expressly excludes these derivatives, so a later model-summary route is not established.
- Delegated visibility: Catalog model gets question/answer/existing catalog when configured; deterministic summarizer gets archived interaction plus source hash and optional actor-readable canonical metadata.
- Selection predicate: Available topic labels or bounded fallback select topic paths keyed by interaction ID; no topic signal yields no derivative. Same payload avoids unnecessary revision.
- Invalidation or expiry: Changed topic paths mark old objects superseded and trusted_for_conclusions=false. Validation refresh copies state/confidence; discarded interaction makes derivative untrusted. Physical history persists.
- Activation or effect: New/updated browsing material and symbolic trust metadata; no evidenced model activation or demonstrated learning benefit.
- Evidence limits: Source wiring only; caught errors can leave derivatives behind current source state. A trust flag does not create a consumer that obeys it.

Admission is automatic derivation after archiving or caller approve/discard; caller approval is not approval of every subsequently model-generated topic. Malformed model output falls back; software sanitizes labels rather than establishing their truth. No answer oracle or improvement test is used. Original transcript/hash remains lineage; full rationale for a model's topic choice is not retained.

> $content['status']='superseded';
> $content['superseded_by']=$desiredRefs;
> $validation=is_array($content['validation']??null)?$content['validation']:[];
> $validation['trusted_for_conclusions']=false;
> --- `packages/core/src/Interaction/ThematicSummaryService.php`

#### MEM-RTE-inspector-snapshot
Label: Context diagnostics and catalog refresh

SRC-1, `packages/core/src/Context/ContextTraceService.php`, `packages/core/src/Web/WebApplication.php`. Web result recording stores diagnostic entries; authenticated GET context calls snapshot, which lazily refreshes a catalog and returns trace/catalog summaries. This is a diagnostic consumption route distinct from [RT-RTE-context-supply](runtime.md#rt-rte-context-supply); its result is not the generator's input selection.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: HTTP context snapshot with counts, up to 50 generated-memory display rows, system-object metadata, traces and catalog pending/completion fields.
- Later read-back: Later inspector calls reload retained traces/catalog; no automatic diagnostic-to-answer-policy update is established in the inspected methods.
- Delegated visibility: Server uses owner and installs private resource rules when missing; ordinary generation receives neither the owner catalog nor a trace-library handle through this route.
- Selection predicate: New results prepend traces; snapshot compares current knowledge hashes and processes at most eight changed/missing entries; generated rows require model provenance reference and are ordered by captured_at.
- Invalidation or expiry: Current trace list is capped at 50; catalog missing refs are removed, changed hashes refreshed incrementally. Time passing alone need not invalidate a cached reusable flag.
- Activation or effect: Operator-facing diagnostics and persisted display cache; no fact verification, weight update or exercised improvement follows.
- Evidence limits: Cache completeness concerns hash coverage, not freshness correctness; source does not establish an operator acting on diagnostics.

Admission is automatic server recording and request-triggered software catalog derivation, not human content approval. The request is a read surface with maintenance writes. No answer oracle or revision-selection experiment is used. Historical ciphertext persists beyond the current 50-trace view.

> if($method==='GET'&&$path==='/mcma/v1/context'){
> --- `packages/core/src/Web/WebApplication.php`

> 'context'=>$context->snapshot((float)($this->providerOptions['min-confidence']??0.75)),
> --- `packages/core/src/Web/WebApplication.php`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-knowledge-reuse
Label: Knowledge as direct answer and selector input

Consumer: KnowledgeRecord assessment, semantic candidate ranking and AskService direct-return branches. Channel: encrypted stored record decoded into symbolic status/freshness plus answer content. Force: deterministic gate and answer copy, unlike the model-interpreted reference force of [RT-BAP-memory-reference](runtime.md#rt-bap-memory-reference). Horizon: later requests/sessions until changed or no longer reusable. SRC-1, `packages/core/src/Knowledge/KnowledgeRecord.php`, `packages/core/src/Knowledge/KnowledgeService.php`; supplied route evidence is [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer). This BAP is distinct from the policy permission denial in [RT-BAP-policy-decision](runtime.md#rt-bap-policy-decision).

> if ($reasons !== []) {
>     return self::decision(false, 'revalidate', array_values(array_unique($reasons)), $stale, $record);
> }
> return self::decision(true, 'reuse', [], $stale, $record);
> --- `packages/core/src/Knowledge/KnowledgeRecord.php`

## Annotations

#### On [RT-OBJ-permission-policy](runtime.md#rt-obj-permission-policy)

Memory-specific persistence: Library initializes policy/vault under owner bootstrap; ensureAiRecallAccess can add missing ai read/summarize grants while preserving explicit denies. ContextTraceService and InteractionArchiveService also maintain private resource rules. These are code-mediated updates to retained access metadata, not acquired world knowledge or model-authored policy. SRC-1, `packages/core/src/Library.php`, `packages/core/src/Context/ContextTraceService.php`.

> if($changed) $this->library->setPermissions($policy,'owner');
> --- `packages/core/src/Context/ContextTraceService.php`

#### On [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture)

Retained source original and organization metadata distinguish user input from model transformation ([MEM-OBJ-explicit-memory](#mem-obj-explicit-memory)). The mirror's provenance says user and points to canonical memory; it is not sufficient alone to exclude model involvement. Canonical organization records provider/status, not the model's full reasoning. Strict mirror reuse and broad canonical recall can give different outcomes for the same retained content. SRC-1, `packages/core/src/Memory/ExplicitMemoryService.php`; supplied route retains admission evidence.

#### On [RT-RTE-context-supply](runtime.md#rt-rte-context-supply)

Direct selector inspection confirms request-driven reconstruction from durable originals. Conversation selects recent anchors/relevance, clips question to 1500 and answer to 3500 bytes, and uses a default 6000-byte accounting budget for up to six turns from twelve candidates. It excludes disputed/retracted but can include unverified turns. Multi-memory rereads knowledge, requires supported/verified with confidence threshold, excludes reject reasons, clips answer to 4500 bytes, summarizes up to four provenance entries and chooses up to four items from eight with default 8000-byte accounting. Its RAG score combines similarity, confidence, freshness, provenance and validation. Stale/current-required items can be delivered with reasons for revalidation rather than copied directly. Broad recall uses recognized subject lexical search across knowledge/canonical/interactions, deduplication and default eight items/16000 bytes; it excludes thematic summaries and deleted canonical objects. SRC-1, `packages/core/src/Context/ConversationContextBuilder.php`, `packages/core/src/Context/MultiMemoryContextBuilder.php`, `packages/core/src/Context/BroadMemoryRecallBuilder.php`.

> $candidateQuestion=self::clip((string)($candidate['question']??''),1500);
> --- `packages/core/src/Context/ConversationContextBuilder.php`

> $answer=self::clip($answer,3500);
> --- `packages/core/src/Context/ConversationContextBuilder.php`

> if(!in_array($state,['supported','verified'],true)) continue;
> if($confidence<$minConfidence) continue;
> if(in_array((string)($assessment['decision']??''),['reject'],true)) continue;
> --- `packages/core/src/Context/MultiMemoryContextBuilder.php`

Context control keeps excluded content in encrypted storage, not in a live model window. Selection/clipping removes material preferentially by score, validation and per-field limits; no later model automatically dereferences supplied logical refs. Subsequent user questions can reload other material through the same selectors, and humans can reopen canonical objects. The frame analogy therefore stops at bounded input construction: no subagent frame or return-only escape is implemented by these builders. Connector user-reference delivery and policy strength remain [RT-BAP-memory-reference](runtime.md#rt-bap-memory-reference), not proof of compliance. The budgets bound selected-item accounting, not all combined provider messages, wrappers or exact tokens.

## Write side

Acquisition and admission are deliberately separate:

| Write mechanism | Author/proposer | Admission control | Retained result and later consumer |
|---|---|---|---|
| Generic CLI/library writes/import/copy | Caller supplies content/metadata; import decrypts historical material; copy preserves bytes | Permission/shape/ref/fingerprint gates; direct actor-less API depends on trusted host; human involvement unresolved for generic caller | Generic objects/index and old revisions; shipped CLI reads; [MEM-RTE-library-authoring](#mem-rte-library-authoring) |
| Generated answer capture | Generator proposes answer; caller config supplies capture metadata | AskService remember flag, no existing exact record and Librarian; default unverified/0.5, not human per-answer approval | Knowledge answer/metadata and optional index; later strict reads/context subject to their gates; [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) |
| Explicit save | User supplies original/save intent; optional model rewrites/classifies | Software validates model output, fallback preserves source; no second semantic-approval step | Confirmed canonical plus separately attempted verified mirror/index; [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture) |
| Mutation and knowledge-only edit | Caller supplies target/content; code resolves target | Ambiguity/no-content and permission/shape rejection; not a model evaluator | Canonical revision/tombstone or independently edited knowledge; [RT-RTE-memory-mutation](runtime.md#rt-rte-memory-mutation), [MEM-RTE-knowledge-editing](#mem-rte-knowledge-editing) |
| Approval/discard and cataloging | Caller decides approve/discard; optional model proposes labels after approval | Software state transition and label sanitization; actual human review unobserved | Knowledge validation, archived history, derived navigation and thematic state; [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval) |
| Index and diagnostic maintenance | Service code and optional embedding/model catalog endpoints | Dimension/hash/shape gates and fixed derivation, not per-derived-content approval | Vectors/discovery/diagnostics; [MEM-RTE-semantic-maintenance](#mem-rte-semantic-maintenance), [MEM-RTE-thematic-sync](#mem-rte-thematic-sync), [MEM-RTE-inspector-snapshot](#mem-rte-inspector-snapshot) |
| Policy/vault management | Authorized caller plus fixed software compatibility/privacy updates | Current policy, owner recovery and specialized API gates | Access rules or named secrets; distinct machine/callback consumers, not ordinary answer text; policy annotation and [MEM-OBJ-vault](#mem-obj-vault) |

Trace-fed transformations are concrete but bounded. Archived question/answer plus validation/catalog become a conversation discovery index, which selects refs for later canonical reads. Optional approval turns archived material into verified knowledge or validates an existing record; that is a later-answer path, not evidence that the archived answer necessarily replaced the existing one. Thematic derivation retains a short answer-derived point, source ref/hash and validation, but its demonstrated later route is browsing, not generative context. Context diagnostics retain route/context information and drive an inspector cache, not an inspected automatic self-revision loop. The records above preserve these distinctions instead of classifying every log as learned memory.

Rationale retention is partial: validation reasons/provenance and original explicit text persist; model organization/catalog reasoning is not shown retained as reasoning. Knowledge inspectId exposes history; RAG chooses bounded provenance/assessment reasons rather than full historical rationale. Deletion/retraction changes current eligibility, not physical erasure. Failed mirror/index/thematic updates can leave independently current revisions, so successful canonical write is not a cross-object consistency guarantee. The counterexamples are retained in the supplied mutation/approval routes, not hidden by a single 'memory updated' label.

## Read-back

| Later consumer | Selection and delivery | Authority and limit |
|---|---|---|
| CLI read/show/check, web library leaf and conversation reopen | Explicit ref/ID/question, index enumeration or conversation lookup; decoded content returned as CLI text/JSON or HTTP JSON | Actual shipped read-back to caller; inspect/list is not automatic model use. [MEM-RTE-library-authoring](#mem-rte-library-authoring), [MEM-OBJ-interaction](#mem-obj-interaction) |
| AskService direct answer | Normalized-intent exact key, semantic ranked reusable candidate, or broad canonical selection | Deterministic output copy; strict knowledge metadata gate is not shared by every canonical recall branch. [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer), [MEM-BAP-knowledge-reuse](#mem-bap-knowledge-reuse) |
| Configured generation model | Request triggers selector reconstruction; selected turns/memories/broad-recall items serialized as reference data | Natural-language influence policy only; delivery is wired, reliance/benefit unobserved. [RT-RTE-context-supply](runtime.md#rt-rte-context-supply), [RT-BAP-memory-reference](runtime.md#rt-bap-memory-reference) |
| Request recovery | Conversation/request identity resolves prior archived result | Later invocation receives archived answer; not freshness re-evaluation. [RT-RTE-web-request](runtime.md#rt-rte-web-request) |
| Owner inspector | Snapshot request reloads traces and hash-matched catalog display rows | Diagnostic display, with stale-cache limitation; not a generator feedback route. [MEM-RTE-inspector-snapshot](#mem-rte-inspector-snapshot) |
| Policy evaluator / secret callback | Retained policy rules decoded for actor-aware operation; named vault secret supplied to trusted callback | Policy has denial force; callback capability does not establish a deployed model route. [RT-BAP-policy-decision](runtime.md#rt-bap-policy-decision), [MEM-OBJ-vault](#mem-obj-vault) |

No unsolicited memory push is established by these routes: web orchestration automatically invokes builders only as part of the caller's question request. The software chooses stored parts within that request. Direct public service methods afford other callers, but unknown callers do not establish additional consumed-memory routes.

## Integration issues

- No supported correction to a supplied runtime fact is required. This report adds a consequential qualification, not a contradiction: the thematic trust flag is not an inspected model-consumer route. Canonical recall excludes derivatives even when confirmed. Evidence: SRC-1, `packages/core/src/Context/BroadMemoryRecallBuilder.php`; [MEM-OBJ-thematic-summary](#mem-obj-thematic-summary), [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval). Reconciliation must not infer automatic answer reuse from the summary label.
- New records name objects and downstream maintenance paths not declared as objects/routes in supplied runtime. Closest overlaps are stated in each declaration. Possible broad-container overlap: [MEM-RTE-thematic-sync](#mem-rte-thematic-sync) intersects both archive and approval, and [MEM-RTE-inspector-snapshot](#mem-rte-inspector-snapshot) intersects web recording, but neither replaces [RT-RTE-web-request](runtime.md#rt-rte-web-request) or [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval). They span multiple triggers rather than being parts of exactly one supplied route. No duplicate referent requiring supersession was identified.
- Cache validity remains separate from knowledge reuse correctness: unchanged object hash skips assessment refresh while time affects freshness. Evidence: SRC-1, `packages/core/src/Context/ContextTraceService.php`, `packages/core/src/Knowledge/KnowledgeRecord.php`; [MEM-OBJ-context-catalog](#mem-obj-context-catalog), [MEM-RTE-inspector-snapshot](#mem-rte-inspector-snapshot). Inspector reusable counts must not stand in for current direct-answer eligibility.
- Cross-object coherence is unresolved operationally: canonical mutation/explicit capture, knowledge validation, index refresh and derivative writes are not shown as one transaction. Supplied routes already retain partial failure. Consequence: later consumer state must be evaluated by its actual object, not by an earlier success message. [RT-RTE-memory-mutation](runtime.md#rt-rte-memory-mutation), [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture), [MEM-RTE-thematic-sync](#mem-rte-thematic-sync).
- Human review and provider identity remain local unknowns. Owner-role calls do not establish a human checking each transformed item; provider IDs do not pin weights. Prevented conclusions are per-content human approval and stable semantic compatibility across endpoint changes, not the existence of software admission/indexing. [MEM-RTE-semantic-maintenance](#mem-rte-semantic-maintenance), [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval).

## Limitations and checks

This is source analysis, not a target run. No target tests, examples, providers or services were executed. Thematic test assertions were read as intended invariants only. Source HEAD matches the supplied frozen boundary; all additional paths belong to SRC-1 at that commit. Source writes, publication, delegation and run-record mutation were not performed. Method identity is the exact supplied job/type/worker/records files; no prior analysis was consulted.

Unavailable deployment configuration, actual archive contents, external model internals and execution evidence prevent conclusions about secure production isolation, actual model compliance, actual review, exercised learning or causal benefit. Remote adapter implementation details, historical decryption internals and exhaustive evaluator assertions were not inspected here; no universal portability, erasure or conformance claim follows. Opaque external state does not erase the supported local lineage and deterministic transformations. No formulated-theory or self-improvement claim is made merely from answer persistence or labels.

Validation: completed with the assigned role validator; form and quotation occurrence checks are not semantic acceptance.
