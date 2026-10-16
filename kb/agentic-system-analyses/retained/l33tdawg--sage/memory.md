---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "SAGE memory: governed text, serving indexes, trace capture, correction, feedback and later context consumers at the frozen source boundary."
run-id: AAS-2026-10-15-sage-d3843de6d2dd-01
source-identity: https://github.com/l33tdawg/sage
reviewed-boundary: e2e0242a421afbd356ed135d7d754a35b0ad5f14
---

# SAGE memory report

## Boundary and evidence

SAGE retains agent-authored knowledge, imported material, selected conversation text and operational decisions for later callers. This report uses SRC-1, the repository and revision registered in [boundary](boundary.md#source-register). Direct inspection rechecked HEAD and clean checkout status. It adds implementation reads of memory models, SQLite retrieval and gate storage, scoped canonical content, correction/reflection tools, hooks and capture encoding, import paths, re-embedding, federation copy admission, quorum feedback and benchmark consumers. Supplied runtime findings remain provisional evidence for admission, co-commit, provider identity, boot guidance, bridge distillation and cleanup; they are identified separately below. No target, test, example or provider was executed.

The memory boundary includes state that can affect later service or agent invocations, not just recalled prose. It includes the material admission and withdrawal alternatives. It excludes the external host's actual conversation-window policy, model weights and deployed services from implementation attribution, as boundary does. Those omissions prevent claims about actual context completeness, provider behavior, instruction compliance or useful learning. Available but uninspected recovery, transport and evaluation branches remain named coverage limits, not access failures.

| Entry point or memory operation | SRC-1 paths | Coverage and conclusion limit |
| --- | --- | --- |
| CLI and MCP surface inventory | `cmd/sage-gui/main.go`; `internal/mcp/tools.go` | Direct dispatch and registered-tool scan: seed/import/export/backup/restore, hooks, nevercompact; remember/recall/forget/reinstate/reflect/list/timeline/tasks/corroborate/link and message/pipeline tools. No separate registered automatic semantic compactor established by this inventory; it does not prove absence elsewhere. |
| Ordinary turn, signed submit, voter, semantic gate | `internal/mcp/tools.go`; `api/rest/memory_handler.go`; `internal/voter/gate.go` | Supplied [RT-RTE-turn-cycle](runtime.md#rt-rte-turn-cycle), [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission); direct remember/evidence and gate-store inspection adds retained parts below, including [MEM-OBJ-review-decision](#mem-obj-review-decision). Correction-round reads rechecked `web/write_gate.go`, `web/handler.go`, `internal/store/sqlite_gate.go` and `internal/voter/gate.go` for its admission, persistence and later consumer. |
| Committed text, hashes, envelopes, vectors, task state | `internal/memory/model.go`; `internal/abci/scoped_memory.go`; `internal/store/sqlite.go`; `internal/store/memory_disclosure.go` | Direct [MEM-OBJ-memory-record](#mem-obj-memory-record), [MEM-OBJ-memory-indexes](#mem-obj-memory-indexes). PostgreSQL driver exists per boundary; implementation parity, all legacy envelopes and state-sync forms not exhaustively traced. |
| Co-commit alternate admission | `internal/abci/app.go`; `internal/memory/model.go` | Supplied [RT-RTE-co-commit](runtime.md#rt-rte-co-commit), direct supplementary-content model. Hash-only consensus envelope differs from locally staged readable content. Remote content completeness not established. |
| Correction, forgetting, reinstatement, corroboration | `internal/mcp/tools.go`; `internal/abci/app.go`; `internal/memory/confidence.go` | Direct [MEM-RTE-correction-cycle](#mem-rte-correction-cycle), [MEM-RTE-lifecycle-change](#mem-rte-lifecycle-change), [MEM-RTE-verdict-feedback](#mem-rte-verdict-feedback). All version-specific challenge/recovery branches not audited. |
| Explicit reflection and bridge-generated lessons | `internal/mcp/tools.go`; `integrations/levelup/sage_bridge.py` | Direct [MEM-RTE-reflection-storage](#mem-rte-reflection-storage); supplied [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation). No actual generated lesson or its subsequent use captured. |
| SessionStart, SessionEnd, PreCompact and resume | `cmd/sage-gui/hook.go`; `cmd/sage-gui/mcp.go`; `cmd/sage-gui/hook_precompact.go`; `cmd/sage-gui/nevercompact_recall.go`; `cmd/sage-gui/nevercompact.go` | Direct [MEM-OBJ-capture-unit](#mem-obj-capture-unit), [MEM-OBJ-capture-progress](#mem-obj-capture-progress), [MEM-RTE-session-lifecycle](#mem-rte-session-lifecycle); annotations on [RT-RTE-hook-context](runtime.md#rt-rte-hook-context). Host checkpoint summary is external; selected transcript text is not a full tool trace. |
| Local recall/search/hybrid, list/detail/timeline, backlog and links | `api/rest/memory_handler.go`; `internal/store/sqlite.go`; `internal/mcp/tools.go` | Direct selector/index and link inspection; supplied [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall). Full task-board/timeline consumer parity remains uninspected. No graph traversal in ordinary recall inferred from link availability. |
| Browser, SDK and Level Up consumers | `extension/chrome/background.js`; `sdk/python/examples/full_lifecycle.py`; `integrations/levelup/sage_bridge.py` | Supplied runtime/boundary findings; browser drops dispute/status fields, unlike MCP. SDK variants and external agent response behavior not directly traced here. |
| Dashboard multi-format import; CLI vault import/export; seed | `web/import.go`; `cmd/sage-gui/vault.go`; `cmd/sage-gui/seed.go` | Direct [MEM-RTE-import-material](#mem-rte-import-material), bounded parser/seed inventory. Every parser's semantic fidelity and backup/restore policy uninspected; no lossless round-trip claim. |
| Re-embedding and unreadable material | `web/embeddings_handler.go`; `internal/store/sqlite.go` | Direct [MEM-RTE-reembed-index](#mem-rte-reembed-index). Recovery-preview/rekey and deprecate-unreadable endpoints inventoried, not fully traced; no automatic deletion or complete recovery guarantee. |
| Operator cleanup and boot preference edits | `web/cleanup.go`; `web/handler.go`; `internal/mcp/tools.go` | Supplied [RT-RTE-maintenance-cleanup](runtime.md#rt-rte-maintenance-cleanup), [RT-OBJ-boot-instructions](runtime.md#rt-obj-boot-instructions), [RT-RTE-boot-guidance](runtime.md#rt-rte-boot-guidance). Operator policy and guidance are separate from knowledge content. |
| Federated remote recall, copy sync, removal | `api/rest/memory_handler.go`; `internal/federation/sync_server.go`; `internal/federation/sync_removal.go`; `internal/federation/sync_emit.go` | Direct bounded copy-admission trace [MEM-RTE-sync-copy](#mem-rte-sync-copy); runtime supplies requested remote recall. Removal journal, outbox, relay authorization and every revocation consumer not fully traced; cannot promise global erasure or identical remote/local views. |
| Evaluators and retained metrics | `bench/locomo/run.py`; `bench/longmemeval/run_with_llm.py` | Direct [MEM-RTE-evaluation-readback](#mem-rte-evaluation-readback). Other benchmark and judge-qualification paths/results remain available but uninspected. No measured effectiveness claim or universal evaluation-to-production update path. |
| Durable messaging, pipe history and task workflow state | `internal/mcp/tools.go`; `cmd/sage-gui/hook.go`; `internal/store/store.go` | Registered tools, payload-free hook probes and store interfaces inspected. Payload/history admission, encryption, retention, claiming and consumer continuation not traced end to end; full coordination-memory characterization prevented. This is an included unresolved operative family, not an evidenced absence. |
| Deployment, snapshots, recovery, legacy adoption and binary upgrades | Paths inventoried in boundary; `internal/store/memory_disclosure.go`; `web/embeddings_handler.go` | Runtime supplies machinery-change route; direct disclosure checks identify additional projection constraints. Complete checkpoint alternatives, repair authorities and export visibility remain uninspected; no universal durability/restore/privacy guarantee. |

## Core ideas

1. **Retained text and permission to disclose it are different objects.** Content, canonical hash/envelope, serving projection, embedding and access/lifecycle metadata have different consumers. An accepted transaction need not be an accepted memory; an accepted memory need not have a usable semantic vector. A co-commit can retain a hash on-chain while readable bytes are staged locally. These distinctions prevent equating consensus with truth or universal readability. [MEM-OBJ-memory-record](#mem-obj-memory-record), [MEM-OBJ-memory-indexes](#mem-obj-memory-indexes), [RT-RTE-co-commit](runtime.md#rt-rte-co-commit).
2. **Context arrives through several independent selectors.** Requested topic recall uses authorization, confidence and search ranking. SessionStart independently pushes ten recent excerpts. Resume reconstructs eligible tagged conversational text. Bridge summarization feeds selected prior lessons into another model. These are delivery mechanisms, not demonstrated changes in behavior. [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall), [RT-RTE-hook-context](runtime.md#rt-rte-hook-context), [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation).
3. **Some curation changes content; other curation changes reliance.** Reflection formats caller-authored lessons; the bridge requests model distillation; correction proposes replacement before challenging the original. Confidence decay, disputes, gate verdicts and quorum history instead change eligibility or decision weight. Reasons supplied for a gate decision are retained locally, but supporting evidence is deliberately temporary. [MEM-RTE-reflection-storage](#mem-rte-reflection-storage), [MEM-RTE-correction-cycle](#mem-rte-correction-cycle), [MEM-OBJ-gate-material](#mem-obj-gate-material), [MEM-RTE-verdict-feedback](#mem-rte-verdict-feedback).
4. **Trace capture is not semantic summarization.** Capture encodes selected user/assistant text with sequence and byte lengths; tool bodies and metadata are omitted, malformed conversational rows can produce gap units. It preserves a reloadable subset outside the host window. The name nevercompact does not mean the host stops compacting. [MEM-OBJ-capture-unit](#mem-obj-capture-unit), [RT-RTE-hook-context](runtime.md#rt-rte-hook-context).

## Shared records

### Components

#### MEM-CMP-benchmark-models
Label: Benchmark provider roles

Source-native identities: `ANSWER_MODEL`, `JUDGE_MODEL`, `EMBED_MODEL` and the separately configured `LONGMEMEVAL_EXPANSION_MODEL` in SRC-1, `bench/longmemeval/run_with_llm.py`. This is a role container, not one shared model: answer generation and grading have distinct inputs; optional expansion selects retrieval queries; benchmark embedding produces vectors. Representational form for each is distributed-parametric inference; prompts/model-name settings and score parsing are symbolic or natural language. Storage substrate: uncaptured external OpenAI services for weights, temporary client responses and retained metric JSON for outputs. For each role, no parameter-training request occurs in the inspected calls; provider-side parameter changes are uninspected. No immutable weight version is pinned; defaults are mutable model-name strings and a mutable service may resolve them to changed weights. These are distinct from the runtime's SAGE embedding, gate, reranker and bridge-model components, which use other configured clients.

> EMBED_MODEL = os.environ.get("LONGMEMEVAL_EMBED_MODEL", "text-embedding-3-small")
> ANSWER_MODEL = os.environ.get("LONGMEMEVAL_ANSWER_MODEL", "gpt-4o-mini")
> JUDGE_MODEL = os.environ.get("LONGMEMEVAL_JUDGE_MODEL", "gpt-4o-mini")
> --- `bench/longmemeval/run_with_llm.py`

> model=os.environ.get("LONGMEMEVAL_EXPANSION_MODEL", "gpt-4o-mini"),
> --- `bench/longmemeval/run_with_llm.py`

### Operative objects

#### MEM-OBJ-memory-record
Label: MemoryRecord content and envelope

Source-native identity: `memory.MemoryRecord`, plus scoped `scope.Content` and hash-only co-commit supplementary content. Representational form: natural-language `Content` interpreted by agents/humans; symbolic ID, content hash, parent hash, type, domain, classification, timestamps, task state and lifecycle. Storage substrate: SQL serving records (SQLite personal node, PostgreSQL daemon per supplied boundary/runtime); canonical Badger state and, for active scopes, retained canonical content/ballot. Raw inputs may be agent assertions, imported text or trace text; type names fact/observation/inference do not independently establish their truth or provenance. Initial content is caller-controlled and not known for a deployed node. Later transformation paths are separately established below.

SRC-1, `internal/memory/model.go`, `internal/abci/scoped_memory.go`, `internal/store/memory_disclosure.go`. This object spans the products of [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), [RT-RTE-co-commit](runtime.md#rt-rte-co-commit) and [RT-RTE-hook-context](runtime.md#rt-rte-hook-context); none declares this operative object. It is not a duplicate of the operator boot preference.

> Content:           submit.Content,
> ParentHash:        submit.ParentHash,
> Classification:    byte(submit.Classification),
> TaskStatus:        submit.TaskStatus,
> --- `internal/abci/scoped_memory.go`

Co-commit is a material alternative to that full canonical content: local raw bytes can be supplementary rather than consensus data. This limits what another node can reconstruct from a hash alone, as [RT-RTE-co-commit](runtime.md#rt-rte-co-commit) also establishes.

> // Content backfills the off-chain record for txs that carry only a
> // ContentHash on-chain (co-commit envelopes): the REST layer stages the raw
> // content here so the local SQLite record is recallable. Off-chain mirror
> // only — never consulted by any consensus branch or badger write.
> --- `internal/memory/model.go`

Later consumers read disclosed content, while service code uses metadata to filter or update it. `ParentHash` carries lineage, not proof that a replacement successfully retired its parent. Task lifecycle metadata has an additional board/assignment consumer rather than being merely prose. Exact task and legacy recovery paths remain bounded by the coverage table.

#### MEM-OBJ-memory-indexes
Label: Memory embedding and retrieval metadata

Source-native identity: `MemoryRecord.Embedding`, `EmbeddingHash`, `EmbeddingProvider`, SQL text indexes, tags and confidence/lifecycle fields used through `QueryOptions`. Storage substrate: SQL serving database; inference model weights remain separate in [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider). Representational form: dense numerical vectors are distributed-parametric representations; space stamps, tags, confidence arithmetic, authorization and index selection rules are symbolic. The text consumed by a model remains natural language, not an embedding. SRC-1, `internal/memory/model.go`, `internal/store/sqlite.go`, `internal/memory/confidence.go`.

> // EmbeddingProvider records which EMBEDDER produced Embedding ("ollama",
> // ...; empty = none/unknown, i.e. needs re-embed). Distinct from Provider,
> // which is the submitting agent's LLM identity.
> --- `internal/memory/model.go`

Vectors derive from retained content, with unknown legacy provenance represented by an empty stamp. Subsequent re-embedding is known even where initialization is not. They give search code ranking authority, not an agent instruction. Hash mode supports keyword matching, not learned semantic similarity. Confidence is computed from initial confidence, time/domain decay and corroboration; open tasks bypass decay in the inspected helper. It is not a truth posterior or model training signal. No counterpart operative object is declared by runtime; this is the retained input to its targeted-recall route.

> if rec.IsOpenTask() {
> return rec.ConfidenceScore // No decay for open tasks
> }
> --- `internal/memory/confidence.go`

#### MEM-OBJ-gate-material
Label: Local gate evidence, verdict and review records

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

These are retained parts of admission, not a replacement route. Source-native identities: SQLite `memory_evidence`, semantic verdicts keyed by memory/judge version, and operator review decisions. Storage substrate: node-local SQLite. Representational form: uploaded evidence and verdict reasons/notes are natural language; random evidence IDs, version keys, probability, decision enum and expiry markers are symbolic. Evidence derives from the submitter; verdict derives from configured judges; review derives from an operator and is separately represented by [MEM-OBJ-review-decision](#mem-obj-review-decision). Their lineage is not interchangeable with memory content or on-chain proof. SRC-1, `api/rest/memory_evidence.go`, `internal/store/sqlite_gate.go`; the supplied admission record retains gate-consumption passages.

> memoryID, version).Scan(&v.Verdict, &v.P, &v.Reason)
> --- `internal/store/sqlite_gate.go`

Evidence upload is a separate authenticated write with a 32 KiB limit and per-agent cap. It is claimed by one submission, not broadcast as plaintext evidence. Software enforces claim/expiry; generic submitting identity does not establish human review. A provably unsent submission can release its claim. The judge and review UI consume plaintext while eligible. Retention is deliberately shorter than memory lifetime:

> //   - claimed, memory proposed (judged or held for review): kept;
> //   - claimed, memory committed, rejected or deprecated: deleted — the vote
> //     it informed is final and the gate never judges that memory again;
> --- `internal/store/sqlite_gate.go`

Unclaimed evidence expires after one hour; an orphaned claimed text is cleared after 24 hours with an expired marker, so a late-arriving memory is held rather than silently judged without its promised support. Verdict reasons remain locally inspectable under version keys; the gate later reads verdict/review decisions. This is evidence-responsive admission state, not proof that later recalling agents receive the reasons or supporting evidence. The ordinary recall content path has no established automatic inclusion of this gate dossier. All-node replication of evidence is not established.

#### MEM-OBJ-review-decision
Label: Operator semantic review decision

Part of: [MEM-OBJ-gate-material](#mem-obj-gate-material)

Source-native identity: `memory_review_decisions`, written by `SetReviewDecision`. Storage substrate: node-local SQLite, not consensus state. Representational form: symbolic memory ID, accept/reject decision, decided-by marker and timestamp; optional natural-language note. Lineage: an operator resolves a held memory through the dashboard, rather than a judge generating a verdict or a submitter uploading evidence. This is the human-decision part of the valid gate-material container. The peer [EPI-OBJ-semantic-verdict](epistemic.md#epi-obj-semantic-verdict) instead represents model output keyed by memory and judge version; it is not a duplicate or substitute. SRC-1, `internal/store/sqlite_gate.go`, `web/write_gate.go`, `web/handler.go`, implementation evidence.

> `INSERT OR IGNORE INTO memory_review_decisions (memory_id, decision, decided_by, note, created_at)
> 		 VALUES (?, ?, ?, ?, ?)`,
> --- `internal/store/sqlite_gate.go`

Admission is a human content decision on the operator-gated dashboard route, not merely human initiation of automatic judgment. Software can veto it: the handler requires an enabled gate and supported store, readable non-internal target, readable or expired evidence, and valid applicable projection. The store requires accept/reject, a current-version abstaining verdict and proposed memory status; an existing decision is not overwritten. The supplied gate-admission route remains responsible for later voting and consensus, not this local record. An optional note records the operator's stated reason, but no note or independent expected-answer oracle is required. SRC-1, `web/handler.go`, `web/write_gate.go`, `internal/store/sqlite_gate.go`.

> r.With(h.cerebrumOperatorGate).Post("/v1/dashboard/memory/{id}/review", h.handleReviewDecision)
> --- `web/handler.go`

> if !ok || v.Verdict != memory.VerdictAbstain || status != string(memory.StatusProposed) {
> 		return ErrNotAwaitingReview
> 	}
> --- `internal/store/sqlite_gate.go`

Actual later consumer: `Gate.Apply` on a later voter tick reads the decision by memory ID before consulting the versioned model verdict, but only after fresh baseline acceptance and in-scope checks. It consumes the decision enum, not the stored note, decided-by marker or timestamp. Accept resolves the semantic question; it cannot override a failed baseline or itself commit the memory. Reject supplies a negative node decision. Read errors hold voting. This gives the retained human resolution conditional admission authority at this node, not direct authority over a foreground model or all validators. SRC-1, `internal/voter/gate.go`; [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission).

> if decision, ok, err := gs.ReviewDecision(ctx, mem.MemoryID); err != nil {
> 		logger.Warn().Err(err).Str("memory_id", mem.MemoryID).Msg("memory gate review lookup failed — held for review")
> 		return gateHold, Decision{}
> 	} else if ok {
> 		if decision == memory.VerdictAccept {
> 			return gateOverride, Decision{Accept: true, Reason: baseline.Reason + "; semantic check resolved by operator review"}
> 		}
> 		return gateOverride, Decision{Accept: false, Reason: "rejected by operator review"}
> 	}
> --- `internal/voter/gate.go`

Persistence/invalidation differs from evidence expiry and model cache versioning: no judge-version key invalidates this decision, and the inspected setter rejects replacement. Subsequent terminal lifecycle state ends ordinary pending voting; retained decision existence does not imply continuing application. No rollback or deletion route for review decisions is established by these reads. Persistence across judge changes is explicit, while actual use and useful semantic resolution remain unobserved.

> // checks still run when the node votes. A decision is final — once voted it is
> // on-chain — and survives later judge-version changes.
> --- `internal/store/sqlite_gate.go`

#### MEM-OBJ-capture-unit
Label: Encoded conversational capture units

Part of: [RT-RTE-hook-context](runtime.md#rt-rte-hook-context)

This object is a material retained part of the combined capture/recall route. Source-native identities: `captureUnit` and `preCompactChunk`. Storage substrate: observation memory content in the ordinary governed store. Form: symbolic self-delimiting sequence/part/role/byte-length headers plus natural-language text; not model-generated summary or opaque embedding. Lineage: host transcript JSONL → selected conversational text → split units → deterministically identified chunks → admitted memory. SRC-1, `cmd/sage-gui/hook_precompact.go`, `cmd/sage-gui/nevercompact_recall.go`.

> return fmt.Sprintf("%s%d\t%d\t%s\t%d\n%s", unitHeaderPrefix, u.Seq, u.Part, u.Role, len(u.Text), u.Text)
> --- `cmd/sage-gui/hook_precompact.go`

> // non-conversational roles (→ caller excludes). Only text blocks are kept;
> // tool_use/tool_result are excluded (re-derivable, may carry secrets) — a turn
> // consisting solely of them decodes to empty text, which is excluded, not a gap.
> --- `cmd/sage-gui/hook_precompact.go`

Thus raw trace retention is selective and re-encoded, not full-fidelity transcript retention. User/assistant malformed content can produce explicit gap units; summary/meta rows are excluded. Repeated text at different sequence positions has distinct chunk identities. The decoder later supplies text ordered by sequence/part; it does not interpret or summarize the text. The host then receives role-labelled prose on stdout, not original privileged message objects. Captured reasons survive only if present in selected text. No model-derived behavioral rule is created by capture itself.

#### MEM-OBJ-capture-progress
Label: Capture progress and gap bookkeeping

Part of: [RT-RTE-hook-context](runtime.md#rt-rte-hook-context)

Source-native identity: `captureProgress` and `chunkRecord`, stored in per-thread local progress files under the capture directory described by `neverCompactHomeDir`; this is not the governed content store. Representational form: symbolic IDs, sequence spans, memory IDs and observed status. Derived from capture attempts and subsequent reconciliation, these control retry/cursor movement, not agent knowledge. SRC-1, `cmd/sage-gui/hook_precompact.go`. They are a distinct operative part from chunk text because loss or stale outcome affects retry, while text affects resume context.

> if status != memoryStatusCommitted {
> status = "proposed"
> }
> --- `cmd/sage-gui/hook_precompact.go`

The supplied [RT-RTE-hook-context](runtime.md#rt-rte-hook-context) establishes progress locking, rejected-chunk reconciliation and later consumers. Deterministic chunk tags can reconcile an ambiguous attempt; deprecated copies are not blindly adopted as successful capture. Persistence of progress is not proof that its content reached an admitted memory or a host window.

#### MEM-OBJ-memory-relationships
Label: Parent pointers, typed links and triples

Source-native identities: `ParentHash`, `MemoryLink` and `KnowledgeTriple`. Storage substrate: parent field in memory/envelope, SQL relationship/triple tables for local serving. Form: symbolic endpoint/hash fields and relation strings; natural-language subjects/predicates/objects may still require interpretation. Lineage: caller-supplied relationships, correction inheritance, and supplementary triples staged from REST requests; no universal automatic knowledge extraction established. SRC-1, `internal/memory/model.go`, `api/rest/memory_handler.go`, `internal/store/sqlite.go`, `internal/mcp/tools.go`.

> // toolGetLinks reads the typed links among a set of memories (the read side of the
> // knowledge graph). It wraps POST /v1/memory/links, which returns only links whose
> // both endpoints the caller may read.
> --- `internal/mcp/tools.go`

Linking is an explicit caller-directed write accepted through endpoint checks, not independent criticism or verification of a supports/contradicts label. Authorized later link reads are wired; triple insertion/storage alone establishes a capability, not a traced agent consumer. Ordinary vector/text retrieval does not thereby become a graph-reasoning route. Relative to supplied recall and admission routes this is additional retained structure, not a duplicate of either route. Complete graph/triple consumer and deletion semantics remain unresolved.

#### MEM-OBJ-validator-stats
Label: Consensus verdict feedback statistics

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

These are retained feedback parts of admission. Source-native identities: canonical `vstats` / domain validator statistics and PoE weights in SRC-1, `internal/abci/app.go`. Storage substrate: Badger consensus state. Form: symbolic counters and EWMA accumulators, not dense weights or linguistic theories. Lineage: recorded accept/reject votes matched against the first terminal memory verdict. Later quorum code reads these factors to weight votes, so they have decision authority at that consumer even though agents do not receive them as lessons.

> matches[vid] = votedAccept == finalAccepted
> --- `internal/abci/app.go`

Matching consensus is the reference here, not independent factual ground truth. The distinct route below traces how this can affect later admissions.

### Routes

#### MEM-RTE-correction-cycle
Label: Memory correction cycle

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Replacement proposal result and correction state; original unchanged, replacement pending, old retained after error, or completed challenge request.
- Later read-back: Independent detail polling observes replacement status; future recall may deliver replacement and, while still live, the original.
- Delegated visibility: Calling agent receives results; no new conversational worker is launched.
- Selection predicate: Explicit replaces_memory_id, readable live original, inherited domain/type/classification, then observed replacement status committed before challenge.
- Invalidation or expiry: Replacement rejection/pending/deadline prevents destructive follow-up; challenge authority or quorum may leave original live.
- Activation or effect: New governed content and lineage are proposed; only after read-back is an old-memory challenge attempted. No atomic replacement guarantee.
- Evidence limits: No exercised correction; all downstream challenge versions not audited. Completion of tool choreography does not guarantee old-memory terminal deprecation.

SRC-1, `internal/mcp/tools.go`. Distinct from [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission): it composes admission with independent observation and withdrawal. Caller authors correction/reason; code controls sequencing; prevalidation, server, voters and consensus can veto. Human per-content control is unresolved for a generic caller. Mode is open correction, no expected-answer oracle. Guidance is supplied corrected prose and reason, not software-derived verification. Recovery is conservative coexistence, not rollback of a successfully admitted replacement.

> // Never challenge the old record until that independent observation sees
> // the replacement committed. If the caller's deadline lands here, the old
> // record remains live: at worst correction leaves both records, never
> // neither.
> --- `internal/mcp/tools.go`

Parent hash and replacement reason preserve some revision lineage, but the supplied replacement body need not state a blame-bearing criticism, and later ordinary recall is not established to retrieve the whole correction rationale. This route affords addressable record replacement; actual theory-builder conditions 1–4, learning and reflection remain independently uninspected for unspecified content.

#### MEM-RTE-reflection-storage
Label: Caller reflection storage

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts of stored/skipped components, partial failure/degradation, or error if all attempted storage fails.
- Later read-back: Independently admitted summary, DO and DON'T records can be retrieved on subsequent authorized calls.
- Delegated visibility: Caller supplies the reflection text; the tool itself invokes no reflective model.
- Selection predicate: Required task_summary and optional dos/donts, resolved writable domain; individual ordinary storage checks apply.
- Invalidation or expiry: Duplicate components skip; errors can leave partial retention; ordinary lifecycle, confidence and index eligibility govern later recall.
- Activation or effect: Formats and submits up to three records, not an in-place method edit or parameter update. Later changed behavior unobserved.
- Evidence limits: Reflected is a return label, not evidence that content-directed criticism occurred or that future capacity improved.

SRC-1, `internal/mcp/tools.go`. No supplied route has this referent; [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation) instead calls a summarizer and reuses prior knowledge. Here the caller proposes all substantive content. Software supplies labels/types/confidence and admission; no per-content human approval is established. Operating mode is open lesson submission; answer oracle none. Ordinary write rejection/recovery applies independently to each component.

> store(fmt.Sprintf("[Task Reflection] %s", taskSummary), "observation", 0.85)
> if dos != "" {
> store(fmt.Sprintf("[DO] %s", dos), "fact", 0.90)
> }
> if donts != "" {
> store(fmt.Sprintf("[DON'T] %s", donts), "observation", 0.90)
> }
> --- `internal/mcp/tools.go`

The fact label and high assigned confidence are not proofs that a DO was proven. Reasons survive only when the caller includes them; the tool does not require them or link every component into one argument. Formulated theory, content consumption, criticism and iteration each remain uninspected for actual outputs. Persistent lesson capacity is wired without establishing learning, reflection, autonomy or exercised self-improvement.

#### MEM-RTE-session-lifecycle
Label: Session lifecycle observation

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Signed submission response or hook error, with shell fallback outside this function.
- Later read-back: Admitted lifecycle text is eligible for later authorized requests in session-lifecycle; the ordinary home-domain prefetch need not select it.
- Delegated visibility: Hook sees bounded host payload session_id and reason; no conversational transcript or model worker is required.
- Selection predicate: SessionEnd hook, bounded stdin, fallback unknown/ended fields, fixed domain and tags.
- Invalidation or expiry: Ordinary memory admission/lifecycle and access rules; failed submission does not establish retained event.
- Activation or effect: Code formats an event observation, not a distilled lesson. Automatic event storage alone is not trace-fed improvement.
- Evidence limits: Later admissibility is wired through ordinary storage, but no later selected event or changed behavior observed.

SRC-1, `cmd/sage-gui/hook.go`. This is distinct from the capture/prefetch route [RT-RTE-hook-context](runtime.md#rt-rte-hook-context): a different trigger, payload and domain. Host triggers; code authors fixed wording; service/consensus admit and can reject. No per-event human approval or answer oracle is established; mode is routine lifecycle recording. Recovery is hook failure/fallback, not guaranteed durable retry.

> "Claude Code session %s ended (%s). "+
> "Direct-write SessionEnd hook recording the lifecycle event; "+
> "per-turn content is captured by the agent's own sage_turn calls.",
> --- `cmd/sage-gui/hook.go`

#### MEM-RTE-import-material
Label: Import retained material

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Dashboard counts/progress/errors or CLI imported/skipped counts, not universal semantic acceptance.
- Later read-back: Consensus-materialized imports become ordinary memory candidates; legacy dashboard paths can also insert serving rows directly.
- Delegated visibility: Uploaded/exported material and embeddings cross file, dashboard and provider boundaries. External origins are user-supplied, not authenticated by parser labels.
- Selection predicate: Selected file/format, parsed records/domain/content, request actor/domain authority before remote embedding on app-v23, per-record submission; CLI vault import constructs fresh signed requests.
- Invalidation or expiry: Authorization/parse/embedding/signing/admission failure can skip or stop a batch; lifecycle and retrieval filtering govern later visibility.
- Activation or effect: Converts external material into memory proposals and local serving representations. It is not an unqualified restoration of old IDs, votes or truth status.
- Evidence limits: Bounded process/CLI trace and parser inventory, not every parser, legacy path or round-trip test; encrypted-file and host behavior unobserved.

SRC-1, `web/import.go`, `cmd/sage-gui/vault.go`, `cmd/sage-gui/seed.go`. This is an alternate producer entering ordinary admission, not a duplicate of [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission). Operator/file caller initiates and chooses material; parsers and software split/format records and submit each. Initiation is not per-record semantic approval. App-v23 requires exact current control actor and domain-write authority, then confirmed consensus projection. Pre-v23 dashboard branches can insert locally after optional fire-and-forget broadcast, so universal consensus-first import is false across historical version paths.

> // Authorization must precede embedding. A remote embedding provider is an
> // external data boundary, so content for a domain the current actor cannot
> // write must never be sent there merely because it appeared in an import.
> --- `web/import.go`

> if insertErr := h.store.InsertMemory(r.Context(), rec); insertErr != nil {
> --- `web/import.go`

The latter insertion is inside the inspected legacy branch, not the app-v23 path. CLI vault import takes content/type/domain/confidence and re-embeds/re-submits; it does not simply copy a committed database row. Open bulk ingest has no answer oracle. Rejection is per record; ambiguous/held signing can stop a batch, not justify blind resubmission. Source text may contain rationale, but import does not establish that it is retained as explicit criticism or consumed as such.

#### MEM-RTE-reembed-index
Label: Re-embed retained content

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Operator-started job/progress; counts and error state are not a promise every record became semantically reachable.
- Later read-back: Search reads regenerated vectors and target-space stamp on subsequent queries; skipped/error states influence future maintenance selection.
- Delegated visibility: Readable retained text is sent to selected embedding provider, not a conversational worker. Provider data handling remains external.
- Selection predicate: Target provider/space and next batch outside that target, readable content, unlocked vault; pages of 100 in inspected dashboard implementation.
- Invalidation or expiry: Space changes require new vectors; unreadable and provider-error cases are marked separately; lock or write failure stops rather than endlessly fetching unchanged work.
- Activation or effect: Changes search representation/eligibility without revising prose or training provider weights.
- Evidence limits: No migration observed; exact provider choice authorization and every recovery lane not exhaustively traced. No improvement in retrieval quality measured.

SRC-1, `web/embeddings_handler.go`, `internal/store/sqlite.go`. No counterpart route in runtime; [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider) supplies model identity/fixity. This trace covers the operator-started migration lane: human initiates that migration and chooses configuration; code selects records and accepts vectors/errors. It is not a complete trigger inventory or an all-re-embedding human-initiation requirement; the supplied verification also identifies automatic provider-ready repair in `cmd/sage-gui/node.go` and `web/embeddings_handler.go`, not independently retraced here. Per-vector human approval absent from inspected worker. Operating mode is maintenance, no expected-answer oracle. Guidance is target-space compatibility, not a learned recommendation. Errors are retryable separately from unreadable material; a failed vector is not itself grounds for deprecation.

> // markUnreadable: content can't be read (undecryptable / empty) — a deprecation
> // candidate. markErrored: content IS readable but the embed failed (retryable),
> // kept distinct so it's never deprecated.
> --- `web/embeddings_handler.go`

#### MEM-RTE-lifecycle-change
Label: Challenge and reinstatement

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Challenge/reinstate transaction result and status; the MCP forget verb forwards challenge rather than issuing a physical delete.
- Later read-back: Canonical challenge state/electorate and serving dispute/status affect subsequent challenge/reinstate requests and authorized recall; deprecated content leaves ordinary live recall.
- Delegated visibility: Caller and service see explicit target/reason; further endorsers supply transactions, not spawned model workers.
- Selection predicate: Explicit memory ID, current authority, target state, activated challenge policy, pinned electorate and distinct endorsements where required.
- Invalidation or expiry: Reinstate is for challenged, not already deprecated records; terminal deprecation is not a generic reversible soft-delete operation.
- Activation or effect: Changes reliance/eligibility rather than body text; some challenges mark disputed while retaining recallability, others resolve deprecation immediately or after threshold.
- Evidence limits: Source branches and supplied dispute findings, not full protocol verification or observed withdrawal. No guarantee of erasure from backups, peers or host context.

SRC-1, `internal/mcp/tools.go`, `internal/abci/app.go`. Distinct from [RT-RTE-maintenance-cleanup](runtime.md#rt-rte-maintenance-cleanup), which is an operator-authorized producer/continuation of these challenges; overlaps correction follow-up but is not its replacement sequencing. Caller proposes challenge/reason; authority, versioned canonical rules and required endorsers decide/veto. Human control is unresolved for generic caller; cleanup's human policy authorization is separately supplied. This open lifecycle operation has no factual answer oracle. Reinstate cancels a live challenge under its checks, not arbitrary rollback of deprecated knowledge.

> if status != string(memory.StatusChallenged) {
> return &abcitypes.ExecTxResult{Code: 94, Log: fmt.Sprintf("reinstate: memory %s is not challenged (status=%s)", rein.MemoryID, status)}
> }
> --- `internal/abci/app.go`

Counterexample to challenge-equals-delete: [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall) retains the explicit IncludeDisputed selector and MCP warning. Latest inspected challenge branches freeze eligible participants and count distinct challengers; no semantic claim that a challenged assertion is false follows merely from state. Purge of captured chunks also submits governed challenges, not guaranteed immediate removal.

#### MEM-RTE-verdict-feedback
Label: Verdict feedback weighting

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Canonical statistics update on the first proposed-to-terminal verdict transition, conditional on version gates and successful terminal write.
- Later read-back: Subsequent quorum calculations use global and domain statistics to compute validator vote weights.
- Delegated visibility: Consensus code consumes votes and state, not a separate model worker.
- Selection predicate: Prior proposed status, terminal result, recorded vote match; domain feedback applies to recorded non-shared domains under its fork.
- Invalidation or expiry: Replayed terminal votes do not credit again; domain/chain rules determine later interpretation. Full epoch/reputation lifecycle uninspected.
- Activation or effect: Derived symbolic experience statistics can change subsequent admission weighting. Not provider fine-tuning or proof of truth learning.
- Evidence limits: Source-level feedback closed through later quorum reads; no observed weight trajectory, improved admission quality or independent factual oracle.

SRC-1, `internal/abci/app.go`. This is the feedback subroute within ordinary admission, with its own result/consumer rather than a duplicate whole admission route. Software admits computed accumulators; validators supply votes, but no per-statistic human approval exists in this code. Operating mode is routine consensus feedback. Reference outcome is the collective terminal verdict; this is not an externally supplied correct answer. Recovery/idempotence uses successful terminal transition and prior-status gating.

> if creditVerdict && becameTerminal && priorStatus == string(memory.StatusProposed) {
> --- `internal/abci/app.go`

> weights[v.ID] = poe.ComputeWeight(acc, domainScore, rec, corr)
> --- `internal/abci/app.go`

This is a qualifying automatic raw-vote → derived-statistic → later-decision chain. Its effect is different from retaining a raw log. It does not retain formulated reasons for why a consensus verdict was factually right. Improved capacity remains uninspected; consensus agreement as feedback can reinforce agreement without establishing correctness.

#### MEM-RTE-sync-copy
Label: Federated copy admission

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Accepted/duplicate/retry or scoped rejection outcome for a remote copy; accepted broadcast is not yet ordinary voter acceptance.
- Later read-back: Durable pending envelope controls recovery; sync_origin records admitted origin identity and drives replay/digest/provenance. Eligible local copy content can later reach local recall after ordinary admission and disclosure.
- Delegated visibility: Peer supplies signed/origin-scoped item; receiver wraps it in a locally authorized memory submit. No model worker is created by sync.
- Selection predicate: Active agreement/domain/classification and origin checks, suppression, replay, visible duplicate checks, unlocked vault, deterministic origin-based local ID and exact pending projection match.
- Invalidation or expiry: Local suppression can bar re-admission; rejected cross-domain duplicates are not permanently ledgered, so changed eligibility permits retry. Existing admitted-origin ledger prevents resurrection by simple redelivery after deprecation.
- Activation or effect: Creates a local memory proposal plus durable provenance/recovery metadata; ordinary receiver voter remains distinct from transport admission.
- Evidence limits: Bounded receiver trace, not all journal/outbox/transport/removal branches or deployed peers. Cannot claim global deletion, universal relay rules or immediate semantic availability.

SRC-1, `internal/federation/sync_server.go`. Distinct from [RT-RTE-co-commit](runtime.md#rt-rte-co-commit): copying uses MemorySubmit and receiver voting, while co-commit is already ratified and bypasses that voter. It is also distinct from requested federated read merging in [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall), which need not persist a local copy. A peer proposes content; operator agreement sets scope; receiver software and consensus can veto. No per-item human review follows from agreement consent. Mode is asynchronous replication, no factual answer oracle.

> // Unknown or empty types default to fact — the copy still goes through the
> // receiver's voter, and "task" deliberately maps to fact too: a synced copy
> // must never appear on the receiver's live task board as claimable work.
> --- `internal/federation/sync_server.go`

Stored copy lineage is split: local submitting authority and ID differ from origin chain/ID/signature in a separate off-consensus ledger. Copying preserves bytes, not originating task authority. Metadata is operational: pending quarantine prevents a crash gap from falsely attaching unrelated local content to an origin; only exact matching projections promote provenance. A duplicate admission outcome can name an already matching native row without converting it into a synced copy.

#### MEM-RTE-evaluation-readback
Label: Benchmark memory read-back

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Retrieval metrics, and in the LLM harness generated answer/grade plus timing and provenance fields written as benchmark results.
- Later read-back: Seeded conversation/session text reaches subsequent query invocations and, in LongMemEval LLM mode, the answer model. Result aggregation reads per-question metrics; a production policy update from those metrics is uninspected.
- Delegated visibility: Configured external providers receive embedding inputs, optional expansion question, retrieved context or question/gold/generated answer according to role.
- Selection predicate: Dataset conversation/question IDs, per-run or per-question domains, top_k and optional expansions, status filter, prefixed evidence/session IDs; retrieved text stripped of bookkeeping prefix before answering.
- Invalidation or expiry: Seed/API/model errors and dataset alignment checks constrain results; later model aliases can change. No automatic production-memory withdrawal from a failed score is established.
- Activation or effect: An explicit later model prompt consumes retrieved text as answer context; code scores retrieval and requests answer judgment. Answer dependence and benefit unobserved here.
- Evidence limits: Harness source, not executed experiments, validated datasets or independently checked result artifacts. Gold labels are supplied evaluation references, not proof of ordinary memory truth.

SRC-1, `bench/locomo/run.py`, `bench/longmemeval/run_with_llm.py`. No supplied runtime route has this referent; boundary initially identifies evaluators but does not supply their complete consumer chain. Caller selects dataset/options; code seeds records, retrieves, assembles context and writes results. Models propose expansions/answers/grades, not production policy. Ordinary service gates can reject seeds; malformed or empty model output can score as failure. Mode is a bounded dataset benchmark. Oracle: LoCoMo evidence-turn IDs for set/rank metrics; LongMemEval answer-session IDs for retrieval and dataset gold answer supplied to judge for answer grading.

> context = "\n<->\n".join(retrieved_text[:top_k])
> llm_answer, answer_seconds = generate_answer(openai, question["question"], context, question_date=question_date)
> llm_score = llm_judge(openai, question["question"], gold_answer, llm_answer) if gold_answer else 0
> --- `bench/longmemeval/run_with_llm.py`

LoCoMo retains returned turn IDs and computes overlap/reciprocal rank; it is not by itself an answer-quality experiment. LLM answer failure and judge failure can return empty answer/zero, so zero is not exclusively a memory-retrieval failure. No theory revision, online weight update or improvement attribution follows from retained scores.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall)

Read-back uses content plus access/index metadata, not raw serving-row presence. Direct SRC-1, `internal/store/sqlite.go` inspection adds hybrid selection: text and vector leaves oversample, reciprocal-rank fusion merges, optional cross-encoder reorders, and the result trims to requested K. Malformed reranker output falls back to healthy fused ordering rather than silently dropping unscored candidates. The inspected SQLite hybrid path bounds fused output at 1,000 and leaf candidate K at 100; these are item/candidate bounds, not a model context-token guarantee. Vault-active search does not use plaintext FTS; when only text is supplied it can fail rather than pretending the encrypted text index is available.

> if query != "" && !vaultActive {
> r, err := s.SearchByText(ctx, query, subOpts)
> --- `internal/store/sqlite.go`

> // A reranker must score every candidate exactly once with a finite
> // score. Reject the whole malformed response before changing the
> // healthy RRF ordering, rather than dropping unscored candidates.
> --- `internal/store/sqlite.go`

Consumer authority remains informational at an external model; server selection authority is enforced by code. The runtime's dispute-warning/browser-omission findings remain material after selection. No single returned confidence/status label proves true content or complete store visibility.

#### On [RT-RTE-hook-context](runtime.md#rt-rte-hook-context)

Direct SRC-1, `cmd/sage-gui/hook.go`, `cmd/sage-gui/hook_precompact.go`, `cmd/sage-gui/nevercompact_recall.go`, `cmd/sage-gui/mcp.go` separates two checkpoint alternatives. One is requested client reflection and durable facts before host compaction; the other is opt-in encoded text capture. The shell emits a reflection nudge even when capture is disabled or fails. These are not the host's own continuation summary, which SAGE does not control or persist through these functions.

> echo "MANDATORY before compaction: Call sage_reflect with a concise summary of (dos, don'ts) from this session, then sage_remember for any durable facts you want to keep. Once the context compacts, the per-turn detail is gone — only what you've committed to SAGE will survive."
> --- `cmd/sage-gui/mcp.go`

Recent prefetch independently selects up to ten newest committed records in explicit/home domain, flattens each and truncates at 200 bytes. It does not retain IDs as dereferenceable pointers in this display; targeted tools remain the reload route. Thread recall instead selects the durable first-row session identity and exact thread tag/domain, pages 200 committed chunks at a time, decodes/deduplicates sequence parts and reconstructs text under one deadline. Default recall deadline is 8 seconds, capped at 20 seconds; no SAGE token budget ensures all stdout fits the host window. Error/timeout can suppress thread output, while ordinary prefetch still runs.

> q.Set("tag", neverCompactThreadTagPrefix+threadID)
> q.Set("status", "committed")
> q.Set("domain", domain)
> q.Set("sort", "oldest")
> --- `cmd/sage-gui/nevercompact_recall.go`

Capture enablement is consent to automatic selection/admission attempts, not approval of every resulting chunk. Disable stops future capture, not existing reads; purge challenges existing chunks. Raw-to-derived chain here is selected trace → encoded retained text → reconstructed context. Unlike bridge distillation or verdict statistics, encoding alone adds no derived recommendation. This route manages material outside the host window and reloads it by value; SAGE does not own eviction. No isolated model-worker context or call-frame return is implemented by these hook functions, and a chunk ID in a database is not an automatically followed in-window reference.

#### On [RT-OBJ-boot-instructions](runtime.md#rt-obj-boot-instructions)

This retained natural-language guidance is separate from knowledge memories and vector indexes. Supplied [RT-RTE-boot-guidance](runtime.md#rt-rte-boot-guidance) establishes human/operator text admission and replacement, preference storage, and later inception delivery. Mode selection is symbolic; custom text is interpreted by the external model. The actual consumer receives appended text as tool-response guidance, not a newly privileged system message. No gate evidence dossier, consensus vote or model-training operation is established for this preference.

#### On [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation)

The retained result is model-produced natural-language observation derived from bounded raw challenge/outcome data and selected prior retained knowledge, not merely raw trace. Its later consumers are query callers and another summarization call supplied prior knowledge. The supplied record retains both the source passage and its independent theory/learning limits; those are not strengthened here. Automatic proposal admission is ordinary SAGE software, with no required per-output human approval. Raw field truncation and bounded recalled excerpts mean reasons not passed into the summary model cannot be assumed preserved. No in-place replacement of old advice follows from a new summary.

#### On [RT-RTE-maintenance-cleanup](runtime.md#rt-rte-maintenance-cleanup)

The durable policy, target list, signed pending bytes and observed confirmation state are symbolic continuation memory for the worker. They are not knowledge text or independent semantic criticism. Human policy authorization and current-authority checks are distinct from software target selection. Cleanup's retained intent later feeds a challenge; downstream recall is controlled by actual challenge resolution, not by a UI count or log. Indeterminate outcome is retained for reconciliation. The supplied passage establishes confirmation_pending rather than blind retry; no immediate physical erasure follows.

## Write side

Authorship, admission and physical persistence must remain separate. On ordinary MCP/REST writes, a caller supplies content, confidence, type and optional evidence. The MCP prevalidator may skip exact duplicates or reject weak material; server/ABCI enforce current authority and transaction checks; the voter supplies a baseline and optionally obtains a semantic verdict; quorum decides ordinary terminal state. The caller need not be human, and a fact type is caller intent rather than verification. Physical insertion occurs in serving projections under canonical rules. A successful submission transaction still starts proposed. [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), [MEM-OBJ-gate-material](#mem-obj-gate-material).

Alternative admission cannot be collapsed into that path. Coauthor signatures and consensus inclusion directly admit co-commit; optional semantic judging is bypassed. Current dashboard imports use control-actor consensus admission while historical dashboard branches insert serving material. CLI seed/vault import creates new submissions. Federation copies enter locally signed ordinary submit, preserving origin separately; that is not co-commit. Operator boot guidance uses preference mutation, not knowledge voting. [RT-RTE-co-commit](runtime.md#rt-rte-co-commit), [MEM-RTE-import-material](#mem-rte-import-material), [MEM-RTE-sync-copy](#mem-rte-sync-copy), [RT-RTE-boot-guidance](runtime.md#rt-rte-boot-guidance).

Automatic transformation ranges from preserving selected trace to deriving decisions. Capture selects conversational text and encodes/reconstructs it; lifecycle hooks synthesize fixed event text; reflection formats caller lessons; bridge distillation calls a model with raw outcomes and prior advice. Verdict feedback turns raw vote outcomes into statistics that weight later votes. Re-embedding derives a new serving representation from retained text without changing its meaning by design. Unknown initialization of existing content, vectors or external models does not suppress those known later transformations. [MEM-OBJ-capture-unit](#mem-obj-capture-unit), [MEM-RTE-session-lifecycle](#mem-rte-session-lifecycle), [MEM-RTE-reflection-storage](#mem-rte-reflection-storage), [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation), [MEM-RTE-verdict-feedback](#mem-rte-verdict-feedback), [MEM-RTE-reembed-index](#mem-rte-reembed-index).

Maintenance can change body, index or reliance independently. Correction preserves domain/classification and parent hash, admits new text first, then independently observes commitment before challenging old content. Challenge/reinstate and cleanup alter recall eligibility; confidence decay changes later selection without rewriting content; re-embedding repairs reachability. Rejection or dispute is not necessarily physical removal, and challenged content may still be delivered. Capture disable does not withdraw existing chunks. [MEM-RTE-correction-cycle](#mem-rte-correction-cycle), [MEM-RTE-lifecycle-change](#mem-rte-lifecycle-change), [MEM-OBJ-memory-indexes](#mem-obj-memory-indexes), [RT-RTE-maintenance-cleanup](runtime.md#rt-rte-maintenance-cleanup).

Retention of reasons is uneven. Gate verdicts store reason/probability; supporting evidence is pruned after terminal decision. Operator review stores an optional note separately from the versioned verdict; the later voter reads only its decision enum, not that rationale. [MEM-OBJ-review-decision](#mem-obj-review-decision). Parent hash, challenge reason and optional correction reason can retain lineage, but ordinary recall need not deliver a complete revision dossier. Reflection requires no rationale; bridge prompt requests insights but does not prove they contain criticism. Captured text preserves reasons only within selected text, excluding tools. Numerical consensus feedback retains no formulated factual explanation. These limits prevent attributing a system-wide iterative theory-revision process merely from labels such as reflect, fact, validated or consensus. No such theory-builder conclusion is needed to establish the implemented memory pathways.

## Read-back

The system has several distinct later consumers:

- **Foreground agent request:** explicit query/topic/domain and K enter deterministic service selection, embedding/FTS/hybrid and optional reranking; authorization, lifecycle, confidence and space stamps constrain results. Full content plus metadata reaches MCP, while browser turn loses some warning fields. Direct ID/list/timeline/backlog/link operations are alternative selectors, not necessarily identical recall policies. [RT-RTE-turn-cycle](runtime.md#rt-rte-turn-cycle), [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall), [MEM-OBJ-memory-relationships](#mem-obj-memory-relationships).
- **Host-triggered context push:** SessionStart automatically selects recency excerpts, independently of foreground model topic. Thread reconstruction selects tagged captured units instead. These delivery paths can reload material the host evicted, but SAGE neither controls that eviction nor guarantees host token capacity or preserved instruction hierarchy. [RT-RTE-hook-context](runtime.md#rt-rte-hook-context).
- **Transformation consumer:** bridge summarizer receives bounded prior knowledge as input to another retained observation proposal. Admission gate receives local pending content/evidence and cached verdict/review; those inputs have admission authority, not foreground user authority. The separately retained human review decision survives judge-version changes and is read before model verdicts, subject to fresh baseline checks; its note is not consumed by this voter path. [MEM-OBJ-review-decision](#mem-obj-review-decision). [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation), [MEM-OBJ-gate-material](#mem-obj-gate-material).
- **Service continuation/decision consumer:** capture progress, cleanup signed bytes, sync pending/origin ledgers and validator statistics feed later code invocations. These are genuine retained operational inputs, but most do not themselves teach a model a new claim. The statistics chain specifically derives behavior-shaping numerical state. [MEM-OBJ-capture-progress](#mem-obj-capture-progress), [RT-RTE-maintenance-cleanup](runtime.md#rt-rte-maintenance-cleanup), [MEM-RTE-sync-copy](#mem-rte-sync-copy), [MEM-RTE-verdict-feedback](#mem-rte-verdict-feedback).
- **Evaluation consumer:** dataset-seeded text reaches later retrieval and the answer prompt; metrics and gold-judgment results reach aggregation. This closes a source-level retained-text-to-answer-input path, not an observed causal claim about answers or production improvements. [MEM-RTE-evaluation-readback](#mem-rte-evaluation-readback).
- **Instruction consumer:** inception reloads operator guidance and mode. Unlike remembered knowledge, this text explicitly asks the host model to operate differently, but remains delivered guidance rather than an enforced privileged message. [RT-BAP-client-guidance](runtime.md#rt-bap-client-guidance), [RT-OBJ-boot-instructions](runtime.md#rt-obj-boot-instructions).

Plain storage APIs, triple insertion, exports and untraced SDK variants do not independently establish additional consumers. Supplied [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) remains the behavioral-authority container for delivery to external models; this report adds no duplicate behavioral-authority declaration. None of these implementation findings establishes reliable compliance, successful learning, reflection or exercised self-improvement.

## Integration issues

1. **No correction of a supplied fact is required by these reads.** Runtime already distinguishes submitted transaction commitment, memory acceptance, dispute eligibility, partial turn failure, co-commit bypass, optional capture and model compliance. New details refine rather than reverse those findings. [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall), [RT-RTE-hook-context](runtime.md#rt-rte-hook-context).
2. **Containment and overlap:** gate material and validator statistics/feedback are parts of ordinary admission; capture units/progress are parts of the combined hook route. Their Part of fields preserve those identities. Correction, lifecycle change, reflection, import, re-embedding, sync copy, SessionEnd and evaluation have distinct triggers/products/consumers, not alternate labels for supplied whole routes. The memory-record/index/relationship objects span multiple supplied routes and have no supplied operative-object counterpart. Benchmark provider roles are not the runtime service or bridge components. The correction adds [MEM-OBJ-review-decision](#mem-obj-review-decision) as a part of gate material, not a replacement container. Its human producer, memory-only key, non-replacement and voter precedence distinguish it from peer [EPI-OBJ-semantic-verdict](epistemic.md#epi-obj-semantic-verdict), whose supplied fragment establishes version-keyed model output. No possible duplicate remains asserted after comparison. [MEM-OBJ-gate-material](#mem-obj-gate-material), [MEM-OBJ-validator-stats](#mem-obj-validator-stats), [MEM-RTE-verdict-feedback](#mem-rte-verdict-feedback), [MEM-OBJ-capture-unit](#mem-obj-capture-unit), [MEM-OBJ-capture-progress](#mem-obj-capture-progress).
3. **Admission label is not universal quality:** consensus co-commit bypasses the semantic voter, copy acceptance records transport admission before ordinary lifecycle resolution, and historical import branches can write locally. Reconciliation must not generalize ordinary semantic checks across these producers. [RT-RTE-co-commit](runtime.md#rt-rte-co-commit), [MEM-RTE-sync-copy](#mem-rte-sync-copy), [MEM-RTE-import-material](#mem-rte-import-material).
4. **Included unresolved state families:** durable messages/pipeline history, complete task-board state and triple consumers remain incompletely traced. Tool and store-interface inventory establishes their presence but not complete admission, retention or return behavior. This prevents a whole-system claim that all retained knowledge is memory-record content or that every stored relationship has a later model reader. [MEM-OBJ-memory-record](#mem-obj-memory-record), [MEM-OBJ-memory-relationships](#mem-obj-memory-relationships); coverage rows identify evidence and limits.
5. **Recovery/withdrawal limits:** not all snapshot/restore, legacy adoption/reanchor, key recovery or federation removal/journal consumers were inspected. Canonical envelopes and off-chain content can differ; local deprecation does not imply global deletion or removal from already injected context. These are available evidence limits, not missing source access. [MEM-OBJ-memory-record](#mem-obj-memory-record), [MEM-RTE-lifecycle-change](#mem-rte-lifecycle-change), [MEM-RTE-sync-copy](#mem-rte-sync-copy), [MEM-RTE-reembed-index](#mem-rte-reembed-index).
6. **Unobserved model use and benefit:** external host/provider operation, actual lesson content, benchmark results and downstream actions were not captured or executed. The report can establish explicit model-input supply and numerical feedback architecture, not useful capacity improvement, reliable critique or end-to-end behavioral activation. [MEM-RTE-reflection-storage](#mem-rte-reflection-storage), [MEM-RTE-verdict-feedback](#mem-rte-verdict-feedback), [MEM-RTE-evaluation-readback](#mem-rte-evaluation-readback), [RT-BAP-retained-context](runtime.md#rt-bap-retained-context).

## Limitations and checks

The frozen source identity was rechecked with Git HEAD and working-tree status before source inspection. All direct source reads and searches stayed within SRC-1 at the registered checkout; no new source identity, execution trace or experimental result is introduced. The supplied runtime and boundary were read in full, including bounded runtime ranges. The invocation, member types, collection, worker rules and record contract were read before analysis. Model/effort identity is recorded separately from source identity.

Correction-round checks directly re-read the frozen SQLite review schema/setter/lookup, dashboard review handler and operator-gated registration, and gate application order. They confirm the missing distinct human-review part without weakening conditional baseline checks or conflating operator notes with later voter input. Broader graph/task/journal, recovery/removal and all-client parity limits remain unchanged. The re-embedding account is explicitly scoped to its manual lane, not a complete maintenance-trigger inventory.

Counterexample checks changed the scope of conclusions before drafting: co-commit and historical import prevent universal ordinary-voter admission; gate evidence expiry prevents permanent-support claims; challenge/reinstate restrictions prevent reversible-delete claims; selective capture and host deadlines prevent full-transcript/window claims; reranker fallback and vault FTS restrictions prevent universal semantic/text parity; explicit benchmark answer input does not establish benefit. Uninspected branches are exposed in coverage and Integration issues rather than called absent.

Deterministic validation: the required invocation-specific validate-output command passed for this corrected candidate with exit status 0: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Its scope is member form and quotation occurrence, not analytical correctness, execution, efficacy or acceptance.
