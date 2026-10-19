---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ClawVault memory: transcript derivatives, fact supersession, alternate context assembly and withdrawal from retrieval."
run-id: AAS-2026-10-17-clawvault-38c16ae4ab34-01
source-identity: https://github.com/Versatly/clawvault
reviewed-boundary: bd702e9cce436bc3065827714cd576e8be20c375
---

# ClawVault memory report

## Boundary and evidence

This account covers the whole shipped memory system at the boundary revision, not only its OpenClaw injection hook. SRC-1 supplies implementation and doctrine/design, not observed operation. I directly checked checkout HEAD against the revision and inspected the source ranges named below. Supplied runtime records supply the other implementation traces; they are not newly observed execution. No target, test, provider, benchmark or example was executed.

Included memory surfaces are direct Markdown storage, capture, raw transcripts and observation derivatives, facts, handoffs/checkpoints, maintenance state, search/graph/vector selectors, explicit context builders, plugin read-back and peer/Python alternatives. External host compaction, provider internals, actual host incorporation and model compliance are excluded evidence: these prevent conclusions about successful recovery, factual accuracy, exercised influence and benefit. Available but uninspected implementation remains explicitly unresolved, not an access gap. The [boundary source register](boundary.md#source-register) identifies SRC-1.

### Coverage inventory

All source paths in this table refer to SRC-1. “Direct” means source text inspected in this attempt, sometimes bounded to the relevant methods; “supplied” means the cited runtime finding supplies the trace and quotation.

| Entry point or operation | Source and inspection basis | Record coverage / remaining limit |
|---|---|---|
| Frozen CLI dispatch, exports, plugin tools/hooks | Direct searches: `bin/clawvault.js`, `bin/register-core-commands.js`, `bin/register-query-commands.js`, `bin/register-maintenance-commands.js`, other `bin/register-*.js`; `src/index.ts`, `src/openclaw-plugin.ts` | Dispatch includes patch, context, recall, inject, replay, rebuild, archive, task/project mutation as well as runtime's primary routes. Search establishes inventory, not each branch's semantics. |
| Store, remember, inbox capture, peer admission | Supplied `src/plugin/slot.ts`, `src/lib/vault.ts`, `src/lib/tailscale.ts`; direct patch/capture methods | [RT-RTE-slot-store](runtime.md#rt-rte-slot-store), [RT-RTE-peer-sync](runtime.md#rt-rte-peer-sync), [MEM-RTE-document-patch](#mem-rte-document-patch). Quick core capture is inbox storage, not the quality-gated turn route. |
| Turn capture and entity synthesis | Supplied `src/capture/service.ts`, `src/capture/quality.ts` | [RT-RTE-capture-turn](runtime.md#rt-rte-capture-turn). Extraction/synthesis internals remain uninspected; entity-profile provenance and semantic merging are not fully established. |
| Observation, scheduled callers, compaction hooks | Direct `src/observer/observer.ts`, router constructor/route/fact branches; supplied hooks/scripts | [RT-RTE-observe-session](runtime.md#rt-rte-observe-session), [MEM-OBJ-raw-transcripts](#mem-obj-raw-transcripts), [MEM-OBJ-observations](#mem-obj-observations), [MEM-RTE-fact-context](#mem-rte-fact-context). Router category append/task conflict internals remain uninspected; no uniform dedup guarantee. |
| Historical replay | Direct `src/commands/replay.ts` in full | [MEM-RTE-history-replay](#mem-rte-history-replay). Platform normalizers uninspected; source labels do not prove original human/tool/model provenance. |
| Fact extraction, conflict and later use | Direct `src/plugin/fact-extractor.ts`, `src/lib/fact-store.ts` in full; context fact branch and orchestration | [MEM-OBJ-fact-store](#mem-obj-fact-store), [MEM-RTE-fact-context](#mem-rte-fact-context). Rule/LLM extraction accuracy unassessed. |
| Sleep, wake, checkpoints, recovery/recap | Supplied wake/sleep; direct checkpoint storage prefix in `src/commands/checkpoint.ts` | [RT-RTE-session-handoff](runtime.md#rt-rte-session-handoff), annotation below. Checkpoint scheduling/history recovery selection and session repair details uninspected. |
| Maintenance, reflection, archive | Supplied worker/reflection traces; direct `src/observer/archive.ts` and vault reindex | [RT-RTE-maintain-inbox](runtime.md#rt-rte-maintain-inbox), [RT-RTE-reflect-week](runtime.md#rt-rte-reflect-week), [MEM-RTE-observation-archive](#mem-rte-observation-archive). Archive is not erasure of all derivatives. |
| Prompt push, foreground tools, outbound filter, slot recall | Supplied plugin/injector/manager/slot paths | [RT-RTE-prompt-recall](runtime.md#rt-rte-prompt-recall), [RT-RTE-tool-recall](runtime.md#rt-rte-tool-recall), [RT-RTE-outbound-filter](runtime.md#rt-rte-outbound-filter). Their distinct selectors and authority must not be collapsed. |
| Explicit context, strategy recall, injectable rules | Direct context fact/budget/orchestration ranges, full `src/recall/service.ts`, full `src/commands/inject.ts`, selected `src/lib/inject-utils.ts` ranges | [MEM-RTE-explicit-context](#mem-rte-explicit-context). Graph expansion, deterministic matching and LLM matching parser details remain uninspected, preventing exact match/priority guarantees. |
| Embedding refresh and hybrid search | Direct `src/commands/rebuild-embeddings.ts` in full; supplied search/provider records | [MEM-OBJ-embedding-cache](#mem-obj-embedding-cache), [RT-CMP-hosted-embeddings](runtime.md#rt-cmp-hosted-embeddings). Cache serialization internals and all query compatibility branches not directly inspected. |
| Task/project, kanban import, migration, linking, rebuild, sync-bd, entity APIs | Dispatch/export inventory only, SRC-1 `bin/register-task-commands.js`, `bin/register-project-commands.js`, `bin/register-kanban-commands.js`, `bin/register-maintenance-commands.js`, `src/index.ts` | Included alternative edits/admissions. Detailed validation, source trust, migration loss, status filtering and downstream consumers unresolved; no complete write-policy inventory is claimed. |
| Python client and dashboard | Supplied `python/src/clawvault/vault.py`, `dashboard/server.js` | [RT-RTE-python-vault](runtime.md#rt-rte-python-vault); dashboard is a graph display consumer, not host-model activation. Python helper parity and dashboard parser/rendering uninspected. |
| Evaluation and product experiment records | Supplied benchmark/autoresearch; boundary's separate `eval/run_v35_full.py` trace | [RT-RTE-autoresearch-change](runtime.md#rt-rte-autoresearch-change). Evaluation adapter internals and saved scores not assessed; no production-memory benefit or independent measured observation inferred. |
| Shipped prompts/templates/instructions | Supplied compressor/worker prompts and skill, boundary inventory | Static guidance differs from use-derived memory. Remaining templates and docs uninspected; no universal rationale-preservation contract inferred. |

## Core ideas

ClawVault retains several different kinds of material. Markdown is readable content; raw JSONL preserves input strings and source metadata; facts are independently superseded symbolic records; checkpoints combine caller prose and recovery metadata. These are not interchangeable copies. Ordinary search does not include every retained file, and different consumers can apply different withdrawal rules. See [MEM-OBJ-fact-store](#mem-obj-fact-store) and [MEM-RTE-observation-archive](#mem-rte-observation-archive).

Trace-fed transformation is implemented, not merely raw logging. Existing observations condition future compression; categorized derivatives can reach search, and facts can reach the explicit context builder. The runtime's proactive hook instead uses its own short-snippet retrieval branch. Explicit `context`, strategy `recall`, command `inject`, slot recall and host push have different selectors and budgets. None establishes that a host answer followed the retained content. See [MEM-RTE-fact-context](#mem-rte-fact-context), [MEM-RTE-explicit-context](#mem-rte-explicit-context) and [RT-BAP-system-context](runtime.md#rt-bap-system-context).

Capture quality is a route-specific admission proxy. Direct store, inbox capture, patch, peer transfer and Python writes do not inherit its checks. The same principle applies to rejection and cleanup: a rejected candidate need not become a document, while archiving an observation changes ordinary retrieval without retracting previously generated facts or category documents. Supplied [RT-RTE-capture-turn](runtime.md#rt-rte-capture-turn) and the archive record support these narrower claims.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw-transcripts
Label: Raw transcript records

Distinct from the Markdown in [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents): observer input strings are retained as JSONL at ledger raw paths. SRC-1, `src/observer/observer.ts`. Message text is natural language or opaque embedded tool/output text; timestamp/source/session/transcript fields are symbolic provenance, not content-level truth. “Raw” here means the incoming trimmed strings, not necessarily original host events: drivers and replay normalizers may already have transformed them. Default raw capture precedes thresholded compression. No automatic raw-log reload into a later foreground prompt is established by this writer; it is an audit/reprocessing substrate, not by itself a demonstrated memory-consumer route.

> fs.appendFileSync(rawPath, `${records.join('\n')}\n`, 'utf-8');
> --- `src/observer/observer.ts`

#### MEM-OBJ-observations
Label: Observation Markdown

Part of: [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents)

Daily ledger Markdown contains derived natural-language observations with symbolic date/type/confidence/importance fields parsed by code. SRC-1, `src/observer/observer.ts`, `src/observer/router.ts`. It is not the raw transcript. Compression consumes prior daily text and pending input; normalized duplicate content is merged with maximum confidence/importance. Router category admission additionally skips importance below 0.4. Subsequent compression, wake, reflection, explicit context and indexed retrieval are distinct consumers, supported by [RT-RTE-observe-session](runtime.md#rt-rte-observe-session), [RT-RTE-session-handoff](runtime.md#rt-rte-session-handoff), [RT-RTE-reflect-week](runtime.md#rt-rte-reflect-week) and [MEM-RTE-explicit-context](#mem-rte-explicit-context). No required per-observation reasoning trace or verified original-message citation is established. Raw retention is not a reversible mapping from every summary bullet.

> if (item.importance < 0.4) continue;
> --- `src/observer/router.ts`

#### MEM-OBJ-fact-store
Label: FactStore records

Distinct from Markdown [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents), though derived from some of the same traces. SRC-1, `src/lib/fact-store.ts`, `src/plugin/fact-extractor.ts`, `src/commands/context.ts`. JSONL at `.clawvault/facts.jsonl` is loaded into ID/entity/relation/category maps. Entity/relation/value and validity fields form symbolic lookup and exclusion rules; `rawText` preserves readable evidence text used by keyword search, not a criticism or derivation rationale. Rule hooks also write a separate `.clawvault/entity-graph.json` display/graph representation containing all facts, including validity fields. Its later consumer is uninspected; do not equate it with the Markdown memory graph used by context assembly.

A new fact can expire a similar-valued or exclusive-relation predecessor. Active query methods filter `validUntil`; historical lookup instead applies an interval. The header calls storage append-only, but `save` rewrites the map. Reused IDs can replace entries; this is not an immutable event-history guarantee.

> existing.validUntil = fact.validFrom;
> --- `src/lib/fact-store.ts`

> fs.writeFileSync(this.factsPath, lines + '\n', 'utf-8');
> --- `src/lib/fact-store.ts`

#### MEM-OBJ-embedding-cache
Label: Embedding cache

Distinct retained numerical selector state associated with [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents), not their natural-language body or the provider's weights. SRC-1, `src/commands/rebuild-embeddings.ts`; [RT-CMP-hosted-embeddings](runtime.md#rt-cmp-hosted-embeddings) supplies provider fixity and query-consumer limits. Rebuild creates vectors from file content, records a hash and provider/model signature, prunes missing document IDs and saves through `EmbeddingStore`. Exact serialization substrate beyond the local cache API is not directly inspected. Vector interpretation is numerical/distributed representation; IDs/hashes/signature are symbolic freshness and compatibility metadata. Calling an embedding provider does not update its parameters.

The hash is computed over only the first 12,000 characters. Therefore a later-tail-only edit need not trigger regeneration without force, even though `embedText` is passed the content variable. This bounds freshness; it does not show that any actual vector was stale. Rebuild traversal also does not share vault reindex's explicit archive exclusion.

> const hash = computeEmbeddingHash(content.slice(0, 12000));
> --- `src/commands/rebuild-embeddings.ts`

### Routes

#### MEM-RTE-fact-context
Label: Fact extraction and context read-back

Distinct extension to [RT-RTE-observe-session](runtime.md#rt-rte-observe-session): independently persisted facts and a later explicit context consumer, rather than just daily/category Markdown. SRC-1, `src/plugin/fact-extractor.ts`, `src/observer/router.ts`, `src/lib/fact-store.ts`, `src/commands/context.ts`. Hook text collection sanitizes fragments to 6,000 characters and recursively selects known event fields. Rule extraction admits facts without per-item human approval. Observer router alternatively extracts from already compressed observations using off/rule/LLM/hybrid modes; default mode is LLM, with rule fallback when unavailable or failed. The LLM branch attaches asynchronous callbacks and returns zero before completion, so the returned routing count is not a durability oracle. Router LLM adapter exact model resolution/weights are uninspected here; no training is established. The hook caller's `sourceLabel` is a provenance label, not proof that every input fragment originated with a human.

Software proposes/adopts extracted records and resolves conflicts; neither confidence nor latest-write supersession is a factual answer oracle. Operating mode is ordinary trace ingestion. Guidance is extraction rules/adapter prompts, not supplied human approval. Recovery is file reload, with malformed JSON lines skipped; no atomic multi-file rollback is shown. These details concern knowledge admission, not a formulated theory criticism loop.

- Immediate return: Hook returns extracted/added/conflict/total counts; router returns a summary whose asynchronous LLM fact count may still be zero.
- Later read-back: `buildContext` loads FactStore, searches active facts, optionally adds preferences, selects up to ten before later profile/budget assembly and returns concise entity-relation-value statements.
- Delegated visibility: Router LLM receives observation-derived material; CLI context caller receives selected statements, not necessarily rawText or extraction rationale.
- Selection predicate: Known event fields/rule or configured extraction mode; same-entity/relation conflict policy; active-fact keyword matches, preference detection and context profile/budget.
- Invalidation or expiry: Superseded facts get validUntil and disappear from active search; historical API can still expose interval-valid entries. Markdown derivatives are not retracted by this operation.
- Activation or effect: Persists structured knowledge and constructs later context; no observed change to a host answer or improved capacity.
- Evidence limits: Extractor semantic accuracy, host event coverage, adapter model identity and concurrent-write consistency remain uninspected; direct APIs alone do not establish historical-query use by a foreground agent.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const factText = `${fact.entity} ${fact.relation} ${fact.value}`;
> --- `src/commands/context.ts`

#### MEM-RTE-explicit-context
Label: Explicit context assembly

Distinct from proactive [RT-RTE-prompt-recall](runtime.md#rt-rte-prompt-recall): CLI/library requested assembly, not an OpenClaw push event. SRC-1, `src/commands/context.ts`, `src/recall/service.ts`, `src/commands/inject.ts`, `src/lib/inject-utils.ts`; dispatch in `bin/register-query-commands.js`. Code owns selectors, while caller chooses task/query and options. The documented consumer role is an agent/operator obtaining prompt context; delivery into a deployed model is afforded, not established by stdout. No retained-context write, content approval or answer oracle occurs merely by reading.

`buildContext` joins search, daily notes, facts, observations and graph-derived entries, applies profile ordering/source caps/deduplication, then optional token budgeting. Its JSON context objects and truncated Markdown can differ under a very tight budget: the fallback retains a top entry object while shortening its rendered text. Strategy `recall` defaults to six 220-character snippets, seeds broader search, then uses entity/temporal/relationship/verification branches. Verification sorts scores and forces source paths; it does not adjudicate truth. Optional entity briefs take a short profile summary and up to four relationships. Command `inject` defaults to eight results and LLM fuzzy matching enabled by its config wrapper; the lower-level helper defaults LLM matching off. It returns full selected item content in Markdown. Trigger/scope/priority fields and graph links affect this selector; its detailed matching/parser semantics remain uninspected.

- Immediate return: Structured result and/or printed Markdown/JSON, not a host invocation.
- Later read-back: Previously retained documents/facts/profiles reach a later caller through task-based context, strategy recall or injectable-item matching.
- Delegated visibility: Optional fuzzy model sees ranking inputs; stdout/API caller gets the selected representation. No autonomous child-agent context is established.
- Selection predicate: Task/query, profile/source caps/graph expansion, optional budget; strategy classification; or message/trigger/scope/graph and optional LLM ranking, depending on branch.
- Invalidation or expiry: Rebuilt per call from retained state; returned text is by value and can become stale. No expiry of source documents is imposed by assembly.
- Activation or effect: Selective reload and context packaging; caller may insert it into a prompt, but actual insertion/compliance is unobserved.
- Evidence limits: Exact graph/ranking internals and some profile rules not directly inspected. Number of items or characters is not a common strict token budget across all three alternatives.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const { context, markdown } = applyTokenBudget(ordered, normalizedTask, options.budget);
> --- `src/commands/context.ts`

#### MEM-RTE-history-replay
Label: Historical replay admission

Distinct producer route into [RT-RTE-observe-session](runtime.md#rt-rte-observe-session), not a duplicate of live hook observation. SRC-1, `src/commands/replay.ts`. CLI caller chooses platform, input and date range; software normalizes, groups messages by date, sets the observer clock to historical noon, prefixes available roles, invokes observation and flush, then reflection over the date span. Observer threshold is one. No per-derived-item human approval or factual answer oracle is wired. Normalizers and compressor guidance shape proposals; code/model admission uses the existing observation/reflection mechanisms. Invalid source/date/input can reject the request; dry-run returns before observer construction. No whole-import rollback is shown.

- Immediate return: Console count/report or thrown error, not a transaction receipt proving every later derivative complete.
- Later read-back: Historical daily observations and routed facts/category documents enter subsequent compression, context and reflection consumers; reflection output follows the supplied reflection route.
- Delegated visibility: Observer receives normalized role-prefixed strings and source/transcript/date labels; original platform event structure is not delivered intact.
- Selection predicate: Supported platform files, optional date range, timestamp normalization/fallback and per-date grouping.
- Invalidation or expiry: Replaying can update existing daily content through compressor merge; subsequent archive/reflection rules apply. No importer-level retraction or idempotence guarantee established.
- Activation or effect: Imports trace-derived knowledge into normal persistence paths, without observed host use.
- Evidence limits: Normalizer fidelity and completion of asynchronous router extraction unestablished; “source” identifies the chosen adapter, not authenticated original trace origin.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> tokenThreshold: 1,
> reflectThreshold: Number.MAX_SAFE_INTEGER,
> --- `src/commands/replay.ts`

#### MEM-RTE-document-patch
Label: Document body patch

Distinct mutation of an existing document, compared with new-file [RT-RTE-slot-store](runtime.md#rt-rte-slot-store). SRC-1, `src/lib/vault.ts`, `bin/register-core-commands.js`. Caller supplies append/replace/content and optional section parameters; CLI rejects ambiguous modes. Core resolves an existing path, preserves frontmatter, applies the body patch and rejects no-change results before writing and incrementally reindexing. Caller authors the proposal; whether that caller is a human or a model remains unresolved. There is no per-patch human approval, capture-quality gate or truth oracle in this inspected path. Ordinary edit mode, not a bounded improvement experiment. Patch helper section/replacement edge cases and rollback are uninspected.

- Immediate return: Reloaded patched Document or error.
- Later read-back: Subsequent retrieval reads the altered body with existing frontmatter selectors.
- Delegated visibility: Shared filesystem clients can reload the edit; no delegated agent is launched.
- Selection predicate: Caller ID/path, patch mode and optional section; precondition of an existing file and changed body.
- Invalidation or expiry: Replaces body and refreshes that document's index; previously delivered snippets remain stale copies. Vector refresh is not established by this method.
- Activation or effect: Direct retained-content replacement, capable of changing future selected text.
- Evidence limits: No transaction/automatic rollback, semantic validation or caller-human identity established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> fs.writeFileSync(absolutePath, `${frontmatter}${updatedBody}`);
> --- `src/lib/vault.ts`

#### MEM-RTE-observation-archive
Label: Observation archival withdrawal

Distinct retention/withdrawal operation related to [RT-RTE-reflect-week](runtime.md#rt-rte-reflect-week), not the weekly reflection writer itself. SRC-1, `src/observer/archive.ts`, `src/lib/vault.ts`. Code selects dated nonarchived/legacy observations, default older than fourteen days; CLI or reflection can initiate it. Software copies to archive then removes the original, without per-file human approval or semantic evaluation. Date cutoff is the admission criterion for movement, not an answer oracle. Dry-run counts candidates without copying/removing. No universal inverse operation or multi-file transaction is shown.

- Immediate return: Scanned/archived/skipped counts and dates, with dryRun flag.
- Later read-back: Default vault reindex excludes ledger/archive, so archived originals cease contributing there; reflection/category/fact derivatives can remain separately retrievable.
- Delegated visibility: Files remain on disk for inspection or separately implemented readers; no later automatic raw-archive prompt delivery established.
- Selection predicate: Parsed observation dates below cutoff, includeLegacy true, includeArchive false, dedupeByDate true.
- Invalidation or expiry: Removes active original after copy; does not erase prior injections, facts, category copies or all external search/cache state.
- Activation or effect: Changes ordinary indexed availability while retaining an archive copy.
- Evidence limits: qmd, embedding traversal, dashboard and other consumers may enumerate differently; no universal forgetting or privacy erasure guarantee follows.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> fs.copyFileSync(file.path, archivePath);
> --- `src/observer/archive.ts`

> ignore: ['**/node_modules/**', '**/.*', '**/ledger/archive/**']
> --- `src/lib/vault.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-observe-session](runtime.md#rt-rte-observe-session)

Direct SRC-1 `src/observer/observer.ts` confirms both threshold and flush paths consume existing daily observations and clear pending buffers before subsequent write/router completion. Raw capture persists input strings first; summary/category/fact derivatives differ in rollback and consumers. Compression reduces selected input by value; it does not remove anything from the enclosing host window. Host compaction is external. Existing observations become update context for later compression, while their derivatives can become knowledge for later foreground tasks. This trace-fed architecture does not establish improved capacity or reliable retention of reasons. The runtime's compressor passage supplies backend fallback evidence; [MEM-RTE-fact-context](#mem-rte-fact-context) adds the independently persisted fact branch.

#### On [RT-RTE-session-handoff](runtime.md#rt-rte-session-handoff)

SRC-1 `src/commands/checkpoint.ts` directly shows `.clawvault/last-checkpoint.json`, timestamped history files and `dirty-death.flag`. Prose workingOn/focus/blocked content differs from symbolic timestamps/session IDs/token estimates and the dirty flag. These are alternative checkpoint forms, not compressed transcript observations. Caller-supplied checkpoint text has unresolved initial human/model control; filesystem serialization is software, not content approval. Supplied wake/sleep evidence establishes a later recovery consumer but not selection of every history file. Persistence of a checkpoint does not establish full host-state reconstruction.

> fs.writeFileSync(checkpointPath, JSON.stringify(data, null, 2));
> --- `src/commands/checkpoint.ts`

#### On [RT-RTE-maintain-inbox](runtime.md#rt-rte-maintain-inbox)

Supplied SRC-1 worker evidence distinguishes derived knowledge (category documents/extracted statements), readable reports, archive copies and symbolic processed hashes. Only processed hashes have the separately established direct decision authority in [RT-BAP-worker-state](runtime.md#rt-bap-worker-state); a generated report has no demonstrated later agent reader. Model-proposed classification plus code allowlist/fallback is software admission, not human curation per item. Selected samples stay outside the foreground context and only returned outputs escape; this resembles a separate computation frame, not proof of runtime sub-agent isolation. Archiving is distinct from erasure and automatic rollback.

#### On [RT-RTE-prompt-recall](runtime.md#rt-rte-prompt-recall)

Supplied SRC-1 injector/hook evidence establishes unsolicited selection from a prompt-derived query, four results by default, score/recency rules, 220-character memory snippets and separate recent recap. Retained document bodies and metadata are transformed into display summaries, not delivered wholesale. Session recap is a different, transient retained source with once-injected state. Static recall mandate is shipped instruction rather than use-derived memory. At the actual consumer, [RT-BAP-system-context](runtime.md#rt-bap-system-context) describes a privileged requested influence channel; path/age labels do not authenticate the underlying knowledge. Context is copied by value, not a live pointer. The separate explicit context profile/budget path must not be projected onto this hook.

## Write side

Acquisition is heterogeneous. Direct API/CLI/Python callers supply content; peer sync admits transferred files. Their content decisions are not established as human decisions merely because a person can initiate a command. Capture turns apply quality proxies; quick inbox capture simply calls store. Patch directly changes an existing body while preserving frontmatter. See [RT-RTE-slot-store](runtime.md#rt-rte-slot-store), [RT-RTE-python-vault](runtime.md#rt-rte-python-vault), [RT-RTE-peer-sync](runtime.md#rt-rte-peer-sync), [RT-RTE-capture-turn](runtime.md#rt-rte-capture-turn) and [MEM-RTE-document-patch](#mem-rte-document-patch).

Automatic trace updates have known mechanisms despite unresolved original authorship. Live observation and replay feed raw strings into daily compression; daily observations condition later compression and can produce category/task documents and facts. Direct event hooks provide a separate facts path. The fact store preserves source/rawText/validity material but the explicit context consumer emits concise statements and a confidence-based explanation, not the original rationale. Reasons need not survive all the way to a prompt. See [MEM-OBJ-raw-transcripts](#mem-obj-raw-transcripts), [MEM-OBJ-observations](#mem-obj-observations), [MEM-RTE-history-replay](#mem-rte-history-replay) and [MEM-RTE-fact-context](#mem-rte-fact-context).

Maintenance categorizes, extracts and archives; weekly reflection consolidates and uses structural heading acceptance, not a truth oracle. Product experiments use benchmark scoring to keep/discard code changes, distinct from ordinary knowledge admission. Rejection products differ: capture returns reasons, reflection can fall back to deterministic rendering, maintenance persists processed hashes, experiments retain score/Git artifacts. Their later consumers and evidence limits are supplied by [RT-RTE-maintain-inbox](runtime.md#rt-rte-maintain-inbox), [RT-RTE-reflect-week](runtime.md#rt-rte-reflect-week) and [RT-RTE-autoresearch-change](runtime.md#rt-rte-autoresearch-change). No global rejection ledger read by every knowledge writer is established.

Withdrawal is local: fact validity controls active fact queries; observation archive controls ordinary vault availability; patch replaces text; peer pull can overwrite/delete. None establishes coordinated retraction through all derivatives, vectors, external indexes and already injected copies. [MEM-OBJ-embedding-cache](#mem-obj-embedding-cache) adds a concrete freshness countercase to assuming every edit automatically refreshes every selector.

## Read-back

Requested delivery includes foreground memory tools, slot recall, wake, explicit context, strategy recall and injectable-rule selection. Unsolicited host delivery includes proactive prompt snippets/recap and the outbound-filter's independent memory lookup. These are different chains even when they query the same vault. The coverage table and route records identify selectors and budgets; raw storage APIs and historical fact query capability alone are not evidence of deployed foreground consumption.

The host owns its invocation and compaction. ClawVault's separate compressor/worker computations keep large selected inputs out of the foreground context and return derived outputs; they do not implement host-window eviction. Later reload restores selected values, not references into an object heap. Archived files remain physically reachable but ordinary vault indexing excludes them. A semantic guarantee of liveness, completeness or recovery does not follow from physical retention. See [RT-RTE-tool-recall](runtime.md#rt-rte-tool-recall), [RT-RTE-outbound-filter](runtime.md#rt-rte-outbound-filter), [MEM-RTE-explicit-context](#mem-rte-explicit-context) and [MEM-RTE-observation-archive](#mem-rte-observation-archive).

## Integration issues

1. Additive scope correction, not a contradiction: the supplied runtime leaves router/fact internals uninspected. [MEM-RTE-fact-context](#mem-rte-fact-context) establishes the raw-hook and observation-derived admission paths and the concrete `buildContext` consumer. Its asynchronous LLM branch means immediate routing counts cannot prove complete fact persistence. SRC-1 `src/observer/router.ts`, `src/plugin/fact-extractor.ts`, `src/commands/context.ts`.
2. No intentional duplicate declarations. Observation Markdown is an explicit part of [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents); raw transcripts, fact JSONL and vectors are distinct operative representations. New routes distinguish patching, replay input, fact/context admission, explicit assembly and archival from the supplied store/observe/push/reflection routes. The record bodies retain their closest supplied comparisons.
3. Uniform withdrawal remains unresolved. Archive exclusion is established for core reindex, whereas embedding rebuild has another traversal and external qmd/dashboard readers were not rechecked. Facts/category derivatives are not removed by the archive method. This prevents a system-wide forgetting claim; see [MEM-RTE-observation-archive](#mem-rte-observation-archive) and [MEM-OBJ-embedding-cache](#mem-obj-embedding-cache).
4. FactStore's append-only header is narrower than its implementation permits: `save` rewrites state. Supersession and ID overwrite are not a guaranteed immutable audit history. The separate entity-graph JSON consumer and its handling of validity are uninspected. See [MEM-OBJ-fact-store](#mem-obj-fact-store).
5. Unresolved included alternatives are retained in the inventory: task/project/kanban/sync-bd/migration/rebuild/linking/entity mutation, detailed graph/matcher logic, checkpoint scheduling/history recovery, Python semantic helpers, dashboard parser and evaluation adapter. Their missing facts prevent exhaustive admission, source trust, parity and utility claims. They do not invalidate the positively traced routes or become evidenced absences.
6. Cache provenance is more specific than the supplied runtime establishes: hosted document vectors have an inspected rebuild producer, but freshness can miss tail-only edits. No actual stale-vector incident was observed. See [MEM-OBJ-embedding-cache](#mem-obj-embedding-cache).

## Limitations and checks

The account is code-grounded, with route-specific unknowns retained rather than global claims of validation, factual warrant, uniform recall or learning. No execution evidence establishes activation, benefit, reliable rationale preservation, successful host recovery or exercised self-improvement. Source HEAD was rechecked as bd702e9cce436bc3065827714cd576e8be20c375; no other source identity or revision was used. Governing method/type/records inputs were read completely, including the supplied bounded runtime and contract ranges. Initial source inventory attempted a nonexistent `src/facts` directory; the emitted error was inspected and subsequent discovery used the actual `src/lib/fact-*` paths. No evidence rests on that failed root.

Deterministic validation: `commonplace-run validate-output` passed for this invocation (exit 0): “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Content/quotation validation establishes form and occurrence, not semantic correctness or acceptance.
