---
type: kb/types/note.md
description: Bounded integration trial of the Maka memory specialist handoff
memory-comparison:
  scope: Built-in conversation-event retention and history read-back; history compaction
    including text and encrypted provider checkpoints; atomic MemoryItem extraction,
    its dedicated store and access metadata. Excludes MEMORY.md/PENDING.md, goal state,
    skill catalogs, tool-result archives and arbitrary external integrations. Copy
    handling is inspected only for the included checkpoints.
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values:
      - sqlite
      - in-memory
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-4
      - OBJ-5
      - CMP-1
      note: Runtime evidence and checkpoint projections use SQLite; atomic memory
        uses memory.sqlite. The checkpoint coordinator retains session-keyed in-memory
        copies and pending loads. SQLite files do not independently establish a files-based
        memory interface.
    representational_form:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-4
      - OBJ-5
      note: Readable content is natural language with symbolic event, provenance and
        selection metadata. V3 encryptedContent is consumed as opaque provider state;
        neither its string container nor a display representation establishes the
        payload's representational form. A complete scoped set cannot be assigned.
    lineage:
      assessment: known
      basis: afforded
      values:
      - authored
      - trace-extracted
      - other-compiled
      - imported
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-4
      - OBJ-5
      - RTE-6
      note: User-authored conversation content is captured; checkpoints and atomic
        items are automatically derived from traces; access metadata and message projections
        are compiled. The inspected copy seam imports existing text-checkpoint content
        and rebuilds its identities. Copy is an affordance here; the acquisition and
        compaction paths are wired.
    behavioral_authority:
      assessment: known
      basis: wired
      values:
      - instruction
      - knowledge
      - routing
      - validation
      - enforcement
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-5
      - RTE-1
      - RTE-2
      - RTE-3
      - RTE-4
      note: Replayed user directives supply instruction; summaries, old transcript
        excerpts and extraction evidence supply context/knowledge. Checkpoint identities
        route replay and coverage digests validate it. Retained extraction cursors,
        receipts and policy-denial records constrain subsequent processing and commits.
        Atomic item content has no established later recall authority. These values
        describe retained operative data, not generic platform permissions.
    write_agency:
      assessment: known
      basis: wired
      values:
      - automatic
      records:
      - RTE-1
      - RTE-2
      - RTE-4
      note: Runtime capture, model compaction, extraction, and metadata maintenance
        are automatic writes. User-authored input and human-triggered remember/compact
        operations do not establish manual editing of the retained memory. The generic
        mutation API has no identified manual caller.
    curation_operations:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - RTE-2
      - RTE-5
      - OBJ-3
      note: Text compaction supports consolidation and roll-forward evolution. Item
        update/archive afford evolution and invalidation, without a production caller.
        No semantic item deduplication, promotion or decay was found in the inspected
        extraction/store path. Opaque provider compaction prevents a complete operation
        set, including a judgment that it only consolidates without new claims.
    read_back_direction:
      assessment: known
      basis: wired
      values:
      - pull
      - push
      records:
      - RTE-1
      - RTE-2
      - RTE-3
      - RTE-4
      - ABS-1
      note: Automatic history/checkpoint assembly pushes retained material to later
        model calls. SearchHistory/ReadHistory and extractor-requested localization
        pull earlier conversation material. MemoryItem readItem/searchByKeys alone
        supply no additional consumer route.
    read_back_signal:
      assessment: known
      basis: wired
      values:
      - coarse
      - identifier
      records:
      - RTE-1
      - RTE-2
      - RTE-4
      note: Automatic assembly selects session/inline-run history, checkpoint coverage,
        current-turn anchors and compatible model/connection identities. Latest valid
        coverage and safe-prefix/budget selection are coarse. Extractor-requested
        lexical localization is pull and therefore does not add an inferred-lexical
        push value.
    trace_learning:
      assessment: known
      basis: wired
      values:
      - 'yes'
      records:
      - RTE-2
      - ABS-1
      note: Automatic trace-fed durable checkpoints are supplied to later continuation
        calls. This meets the report contract without requiring novel knowledge or
        measured benefit. Atomic incidental acquisition alone does not establish a
        separate learning route, because later item recall is unconnected.
    trace_source:
      assessment: known
      basis: wired
      values:
      - event-streams
      - tool-traces
      records:
      - OBJ-1
      - RTE-2
      note: Both checkpoint variants derive from RuntimeEvent history, including projected
        tool calls/results. Tool traces are a content subset of that event stream,
        not evidence of a second independent log. Atomic extraction's user-only evidence
        is not used to narrow this set.
    learning_scope:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - RTE-2
      - RTE-6
      - ABS-1
      note: The text summarizer requests continuation of the same task, but the durable
        mechanism is session/coverage based and permits validated text-checkpoint
        copying. The inspected routes do not settle the actual task horizon across
        later turns or copied sessions. Atomic global/workspace labels cannot establish
        cross-task/per-project learning without item read-back.
    learning_timing:
      assessment: known
      basis: wired
      values:
      - online
      records:
      - RTE-2
      note: The qualifying checkpoint routes generate and persist state during the
        interactive continuation/compaction lifecycle, before subsequent provider
        dispatch. Standalone manual compaction is an on-demand operation in that lifecycle;
        no offline training or separate promotion stage is established. Background
        MemoryItem acquisition is not counted as a qualifying recall route.
    distilled_form:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - OBJ-2
      - OBJ-3
      - RTE-2
      note: V2 distills natural-language continuation content with symbolic coverage
        metadata. The same qualifying route has a V3 encrypted provider-state branch
        whose decoded form is unavailable. A natural-language-only or symbolic-only
        union would omit that uncertainty.
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - CLM-1
      note: The commissioned evidence contains implementation and comments, not retained
        execution demonstrating dependence on recalled content. Structural summary
        checks, source digests, test filenames and an incident comment do not establish
        the required observed/causal evidence. This report does not claim that no
        such experiment exists elsewhere.
---

# Bounded memory handoff integration

This is a workshop integration excerpt, not a complete whole-system analysis
or public review. It exercises adopting the specialist report at its unchanged
Maka source boundary and limited scope. Runtime and epistemic analysis remain
outside this trial. Canonical IDs here belong to this trial only.

Source: SRC-1, https://github.com/apache/maka at
`dd7d1d595b7f9284e01fe76cf547c979a6d84a0a`.
Report SHA-256: `a753a4b989ac4d5da4c3481f01225fc9dc6f23cc4f58eccab4ac7d26c99e67fb`.

## Shared records

### CMP-1 — checkpoint coordinator and ledger loader

Proposed component. Implementation conclusion status: wired. Owns per-session
checkpoint caching, serialized loads/writes, selection from session-inline
invocations, durable recording before cache replacement, and recovery of the
latest valid checkpoint projection. Its Maps are an operative in-memory
access structure; the durable checkpoint lives in SQLite AgentRun events and
their derived projection. SRC-1
`packages/runtime/src/history-compact-checkpoint-coordinator.ts:43-120`;
`packages/runtime/src/history-compact-ledger.ts:68-169`;
`packages/storage/src/agent-run-store.ts:340-395`.

### OBJ-1 — conversation RuntimeEvents and visible message projection

Proposed object. Implementation conclusion status: wired. RuntimeEvents carry
user/model/tool/system roles and separately identify authors. They retain raw
conversation evidence, including structured tool exchanges; they are not
themselves distilled memories. Runtime persistence opens SQLite at the
operational state root. History tools read the session's visible message
projection rather than returning the entire event object. Natural-language
content and symbolic event identity/role/protocol data are distinct parts;
provider-native payloads can remain opaque. Human messages are authored;
capturing events and deriving message projections are automatic operations.
SRC-1 `packages/core/src/runtime-event.ts:96-137`;
`packages/storage/src/runtime-event-persistence.ts:35-114`;
`packages/storage/src/session-store.ts:998-1008,1064-1069`;
`packages/runtime-host/src/server/execution-composition.ts:461-480`.

### OBJ-2 — V2 text HistoryCompactCheckpoint

Proposed object. Implementation conclusion status: wired. Retains a
natural-language continuation summary, section-format identity, session/run/
turn/event coverage, source digest and source-policy version, limitations,
token estimate, previous-checkpoint ID, and optional current-turn head anchor
and extraction boundary. The symbolic metadata validates and selects replay;
the text supplies continuation context and suggested next steps. Persistence
is the AgentRun ledger and its latest-checkpoint projection, not replacement
of the raw RuntimeEvents. SRC-1
`packages/runtime/src/history-compact-checkpoint.ts:37-113,315-350,414-425`;
`packages/runtime/src/history-compact-summary-validation.ts:42-67`;
`packages/storage/src/agent-run-store.ts:371-381`.

### OBJ-3 — V3 provider HistoryCompactCheckpoint

Proposed object. Implementation conclusion status: wired. Shares the coverage
envelope with OBJ-2 but carries `providerState` instead of `summary`:
`openai_codex_remote_v2`, connection ID, model ID, item ID and
`encryptedContent`. The actual later-consuming payload is the encrypted value
inside an `openai.compaction` custom assistant part. It is not a readable
summary and its form cannot be inferred from its string encoding. The
inspected local store is SQLite; the provider call does not by itself
establish provider-side durable storage. SRC-1
`packages/runtime/src/history-compact-checkpoint.ts:115-132,354-411`;
`packages/runtime/src/ai-sdk-message-projection.ts:532-541`.

### OBJ-4 — atomic MemoryItem with keys and source pointers

Proposed object. Implementation conclusion status: wired. Stored in dedicated
`memory.sqlite`, opened through an authenticated interactive storage-root
lease. Content is bounded natural-language text; typed fields record kind,
statement type, temporal bounds, global/workspace scope, lifecycle, origin,
version and hashes. Keys are access metadata (exact/entity/concept/alias/code,
with origin and normalized key), not additional memory assertions. Source
pointers identify the session/run/turn/event supporting current content.
The type describes current-content provenance; it does not retain the full
admission quotes or every superseded content version. SRC-1
`packages/core/src/long-term-memory.ts:28-127`;
`packages/storage/src/long-term-memory-store.ts:38-90`;
`packages/storage/src/sqlite-long-term-memory-store.ts:962-1008`.

### OBJ-5 — extraction coverage and settlement state

Proposed object. Implementation conclusion status: wired. SQLite retains the
per-session processed-ordinal cursor, operation/receipt identities, pending
failure range with coverage hash and original trigger, and automatic-compaction
policy-denial records. These are symbolic control/access metadata, not
learned claims. They determine which retained events are reconsidered,
prevent replay of mismatched operations or coverage, and suppress reconsideration
of denied automatic ranges. Receipts can contain the exact requested item
IDs/content returned by a remember operation. SRC-1
`packages/core/src/long-term-memory.ts:166-242`;
`packages/runtime/src/memory-extraction.ts:339-452,1272-1297`;
`packages/storage/src/sqlite-long-term-memory-store.ts:292-389,414-474,800-838`.

### RTE-1 — automatic retained-history assembly

Proposed route. Implementation conclusion status: wired. Trigger: a later
provider request or tool-continuation step. Selector: runtime history assembly
using the session's inline invocations, durable current-turn events and a
compatible checkpoint. Retained inputs: OBJ-1 plus OBJ-2 or OBJ-3.
Delivery: provider message history. Later consumer: the continuing task model.
This is push, because the task model did not request a history read. Actual
session/run/turn matching and the exact head-anchor event select the supplied
parts; latest valid coverage and verbatim-tail selection add coarse signals.
Replayed user messages preserve directive content, while summaries and
prior outputs provide context. SRC-1
`packages/runtime/src/history-compact-checkpoint-coordinator.ts:51-78,114-120`;
`packages/runtime/src/ai-sdk-turn.ts:1268-1358`;
`packages/runtime/src/history-compact-checkpoint.ts:386-411,541-650`.

### RTE-2 — compaction, persistence, and later checkpoint replay

Proposed route with two included output branches. Implementation conclusion
status: wired. Producer: the selected model's text summarizer, or the Codex
provider compactor. Inputs: a safe completed RuntimeEvent prefix, and an
eligible previous checkpoint plus newly folded events when rolling forward.
Triggers include standalone compaction, active request capacity pressure,
and reactive provider context overflow. The active selector preserves tool
call/result pairs, partial-event boundaries, steering and the current user
anchor. It waits for durable completed events, validates materializability,
then persists before applying the replacement projection.

V2 read-back is a rendered checkpoint block plus verbatim anchor/tail in
RuntimeEvents. V3 read-back omits a text block and prepends encrypted provider
state at message materialization. Both automatically supply a later provider
call, and a subsequent compaction can consume the previous checkpoint again.
Model/connection matching selects the native branch. V2's summarizer asks for
continuation of the same task; neither a session ID nor checkpoint-copy
support establishes an exclusive actual task horizon.

SRC-1 `packages/runtime/src/history-compaction.ts:73-109,263-299`;
`packages/runtime/src/history-compact-summarizer.ts:71-148,178-218`;
`packages/runtime/src/openai-codex-history-compactor.ts:54-140,151-174`;
`packages/runtime/src/ai-sdk-compaction.ts:287-401,912-940,1023-1118,1143-1178`;
`packages/runtime/src/history-compact-checkpoint.ts:541-650`;
`packages/runtime/src/ai-sdk-message-projection.ts:532-541`.

### RTE-3 — requested conversation search and bounded read

Proposed route. Implementation conclusion status: wired. Requesting consumer:
the main agent through the registered `SearchHistory` and `ReadHistory`
tools. Retained input: OBJ-1's visible transcript and session catalog.
Search returns message-level hits from logical sessions; the optional second
call selects surrounding turns by message/turn identity. Delivery: structured
tool results to the requesting agent. Read limits are five turns, 32 KiB
overall and 8 KiB per message. Current-turn material is excluded from a
same-session read; hidden reasoning and raw arguments/results are not exposed
by ReadHistory. Search can include bounded tool-result hits. The route is
pull; its lexical search is not a push selector. SRC-1
`packages/runtime/src/history-tools.ts:42-48,74-202,280-335`;
`packages/runtime-host/src/server/execution-composition.ts:461-480`.

### RTE-4 — atomic extraction and source-history localization

Proposed route. Implementation conclusion status: wired. Producers: runtime
extractor and auxiliary calls using the source session's model authority.
Triggers: zero-argument `memory_remember` following explicit user intent,
agent-requested `memory_extract` after terminal persistence, and eligible
automatic compaction. The host serializes work per session; explicit remember
is foreground, incidental/compaction work is background. The host gate excludes
incognito, disabled memory, archived sessions and subagents. A native Responses
guard can prevent automatic dispatch; this is not an unconditional every-provider
feature.

Retention: OBJ-4 and OBJ-5, committed atomically after schema, evidence,
secret and canonicalization checks. The cursor defines fresh source coverage;
receipts enable idempotent retry. Source-history supply to the first extraction
call is automatic. If that model returns `search_required` with terms/roles,
the runtime searches same-session user/assistant text and supplies a bounded
localization context to the extractor's next call. That subroute is pull by
the extractor, not a free-standing task-model search tool. It establishes a
later consumer of raw history, not recall of already stored MemoryItems.
Explicit remember returns a receipt to its caller; that acknowledgment does
not establish cross-task item retrieval.

SRC-1 `packages/runtime/src/memory-extraction.ts:283-330,339-452,878-958,1120-1139`;
`packages/runtime/src/memory-extraction-evidence.ts:260-329`;
`packages/runtime/src/ai-sdk-turn.ts:768-788,2550-2559`;
`packages/runtime-host/src/server/memory-extraction-coordinator.ts:101-184`;
`packages/runtime-host/src/server/execution-composition.ts:701-733`;
`packages/runtime-host/src/server/execution-model-authority.ts:158-211`.

### RTE-5 — item store retrieval and lifecycle affordances

Proposed capability record, not an established later-agent route. Conclusion
status: afforded. The store supports ID reads and normalized exact/prefix
key search, including workspace and archived-item filters. Default search
limit is 20. It also supports create/update/archive/restore under atomic,
idempotent operations and expected versions. Update replaces content, keys
and sources; archive keeps the item while removing it from default search;
restore reactivates it. These support evolution and invalidation as storage
capabilities. No identified production caller turns those capabilities into
automatic curation, human editing or agent recall. SRC-1
`packages/storage/src/sqlite-long-term-memory-store.ts:245-289,842-890,904-1042`;
`packages/storage/src/long-term-memory-store.ts:132-159`;
`packages/core/src/long-term-memory.ts:130-158,311-331`.

### RTE-6 — checkpoint copy admission

Proposed capability record. Conclusion status: afforded. The inspected
conversation-copy seam drops opaque V3 checkpoints, superseded source policies
and nonmatching coverage. A valid V2 checkpoint is rebuilt with copied raw
events and new identities while preserving its summary content. This supplies
an imported-content/compiled-metadata lineage for text checkpoints; it does
not reveal the task relationship between source and destination sessions or
establish a new learning transformation. SRC-1
`packages/runtime/src/conversation-copy.ts:896-957`.

### ABS-1 — no atomic item recall or curation caller found

Proposed bounded-absence record. Conclusion status: absent. At SRC-1 the
non-test tree's `readItem` and `searchByKeys` occurrences are the core contract,
interactive facade and SQLite implementation only. `applyMutations` likewise
has only those declarations/forwarding/implementation occurrences. The host
extractor wires cursor/receipt reads and `commitExtraction`, and history
tools read session messages. This rules out treating the inspected atomic
store API as a wired item recall route or manual-edit surface. It does not
rule out an external integration, reflective caller, or future release.
SRC-1 `packages/core/src/long-term-memory.ts:311-331`;
`packages/storage/src/long-term-memory-store.ts:132-159`;
`packages/storage/src/sqlite-long-term-memory-store.ts:245-289,842-890`;
`packages/runtime-host/src/server/memory-extraction-coordinator.ts:90-98`;
`packages/runtime-host/src/server/execution-composition.ts:461-480,701-733`.

### CLM-1 — admission checks do not establish semantic faithfulness

Proposed claim. Implementation conclusion status: wired. Coverage digests
verify the effective source prefix; summary predicates check structure,
truncation signals and a conditional size floor. They do not test whether
the continuation depends correctly on recalled facts. Item admission verifies
that a normalized quote occurs in its source and delegates assertion support
to a prompted canonicalization call. Quote presence is not entailment.
The summary-validator's comment reports a prior short-summary failure, but
does not supply retained execution evidence for this run. SRC-1
`packages/runtime/src/history-compact-checkpoint.ts:541-616,732-771`;
`packages/runtime/src/history-compact-summary-validation.ts:69-107`;
`packages/runtime/src/memory-extraction-proposal.ts:201-221,308-365`.


## Runtime account

Not commissioned in this bounded integration exercise.

## Memory/context lens


Maka preserves source events while changing the projection supplied to the
next model call. A text checkpoint states the goal, progress, next steps and
critical context; its source coverage is digest-bound. The original ledger
remains available when wording matters. Compaction therefore establishes
trace-fed continuation memory even though the source describes it as shaping.
The useful guarantee is a wired continuation route, not proven semantic
fidelity or better task performance. See OBJ-1, OBJ-2 and RTE-2.

The provider-native alternative is materially different. It retains an
encrypted value tied to a model and connection, supplies it as a custom
assistant message, and excludes it from text-checkpoint copying. It must not
inherit the readable summary's representational classification. A provider
failure can select a portable text fallback under specified conditions.
See OBJ-3 and RTE-2.

Atomic MemoryItem acquisition has stricter evidence admission than ordinary
continuation history. Only stable user-authored text qualifies as supporting
evidence. Assistant text can resolve a reference but cannot substitute for a
user citation. A second, isolated model call canonicalizes candidates, after
which runtime code rechecks admission. This is a concrete acquisition path;
the store's item retrieval methods have no identified production recall caller
at the pin. See RTE-4 and ABS-1.


## Reconciliation

All fourteen proposed records are accepted with their original source status
and limits. The mapping is:

| Specialist ID | Canonical ID |
|---|---|
| MEM-CMP-1 | CMP-1 |
| MEM-OBJ-1 | OBJ-1 |
| MEM-OBJ-2 | OBJ-2 |
| MEM-OBJ-3 | OBJ-3 |
| MEM-OBJ-4 | OBJ-4 |
| MEM-OBJ-5 | OBJ-5 |
| MEM-RTE-1 | RTE-1 |
| MEM-RTE-2 | RTE-2 |
| MEM-RTE-3 | RTE-3 |
| MEM-RTE-4 | RTE-4 |
| MEM-RTE-5 | RTE-5 |
| MEM-RTE-6 | RTE-6 |
| MEM-ABS-1 | ABS-1 |
| MEM-CLM-1 | CLM-1 |

The fourteen-axis profile is adopted by substituting IDs only. Its scope,
values, bases, rationale and uncertainties are unchanged. RTE-5 remains a
storage capability without an established item-recall consumer; RTE-6 remains
a checkpoint-copy affordance. Neither becomes a wired recall route. Actual
pull is supported separately by history tools and extraction localization.

The unresolved provider payload form and curation, checkpoint task horizon,
and faithfulness evidence remain explicit unknowns. No supplied canonical
memory finding conflicted with the report because the frozen register held
SRC-1 only. A trial involving existing parent findings is still needed to
exercise substantive disagreement and rerun handling in practice.
