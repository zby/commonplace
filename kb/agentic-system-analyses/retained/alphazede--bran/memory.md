---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "BRAN memory: caller-selected repository context, retained query diagnostics, connected results and separately afforded derived-state storage."
run-id: AAS-2026-11-08-bran-2be75f1c9e69-01
source-identity: https://github.com/alphazede/bran
reviewed-boundary: "7bc428b2ccdfad38e05caa0c0cba2bb19041993a"
---

# BRAN memory report

## Boundary and evidence

BRAN selects repository evidence and optionally executes a grounded connected request. This report covers the whole-system boundary in [boundary](boundary.md#boundary-and-evidence), including shipped callers, instructions, maintenance and storage alternatives. All direct evidence is SRC-1 at the reviewed commit. Implementation reads establish wiring or API capacity, not exercised use or benefit. The source register supplies no observed execution or causal experiment.

The memory scope includes reusable repository material, query-use records, retained connected results, effective settings, source replacement, document projections, existing SCIP evidence, derived rebuilds, state-store APIs and portable export. It excludes external host/provider internals, external compression internals and index production, exactly as the boundary does. Static skill text is guidance, not use-derived memory. Ordinary scan structs, packet assembly buffers and structural-coordinator outcomes are working state unless another consumer retains them. No inference about external session retention follows from local storage or the no-session echo.

Direct reads added the following implementation coverage to the supplied runtime account. Available files not audited below are not access gaps.

| Entry point or operation | SRC-1 path | Coverage and supported conclusion |
|---|---|---|
| CLI dispatch; query recording; evidence summarize/propose/replay/clear | `crates/bran-cli/src/main.rs` | Direct dispatch search and reads of query-evidence structs, codecs, persistence, gap analysis and replay. [MEM-RTE-evidence-feedback](#mem-rte-evidence-feedback). `check`, `doctor`, `agents list`, `body-preserved` and smoke were dispatch-inventoried, not fully audited as memory producers; their presence alone establishes no additional memory loop. |
| Query/packet scan, rank, closure and bounds; connected request and retry | `crates/bran-cli/src/main.rs`, `crates/bran-core/src/packet/mod.rs` | Supplied [RT-RTE-query-packet](runtime.md#rt-rte-query-packet), [RT-RTE-connected-request](runtime.md#rt-rte-connected-request); direct reads additionally cover symbol selection and result retrieval. Not an exhaustive audit of ranking relevance. |
| Document inspect/query/packet | `crates/bran-cli/src/document_evidence.rs`, `crates/bran-document/src/admit.rs` | Direct admission types and document selection/excerpt code. [MEM-RTE-document-selection](#mem-rte-document-selection). Native parser internals and every conformance fixture remain uninspected; no complete format-fidelity conclusion. |
| Existing index.scip | `crates/bran-cli/src/main.rs` | Direct `SymbolNavigation::resolve`, retained filtering and output encoding; [MEM-RTE-symbol-reload](#mem-rte-symbol-reload). Core decoder/freshness algorithm not fully audited; index correctness and production provenance remain unresolved. |
| Connected publish/get/expiry/cancellation | `crates/bran-cli/src/main.rs`, `crates/bran-core/src/agent/coordinator.rs` | Direct filesystem store, `do_get`, batch publication/read verification; [MEM-OBJ-result-answer](#mem-obj-result-answer), [MEM-OBJ-result-support](#mem-obj-result-support), [MEM-OBJ-lossless-artifact](#mem-obj-lossless-artifact); annotations on connected route. |
| Settings apply and source maintenance | `crates/bran-cli/src/main.rs`, `crates/bran-tui/src/settings.rs`, `crates/bran-core/src/repair/mod.rs` | Supplied [RT-RTE-settings-apply](runtime.md#rt-rte-settings-apply), [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply). No second declaration of these referents. |
| Derived rebuild | `crates/bran-core/src/derived_state.rs` | Direct deterministic transformations and `rebuild_artifact`. [MEM-RTE-derived-rebuild](#mem-rte-derived-rebuild). Classification internals and every caller not exhaustively audited; no automatic production consumption established. |
| Database evidence port | `crates/bran-core/src/database/evidence.rs`, `crates/bran-core/src/database/mod.rs` | Direct extraction gate, evidence/provenance types and packet conversion. [MEM-CMP-database-evidence](#mem-cmp-database-evidence). Detailed collection/DLP internals, actual engines and deployed callers not audited; prevents claims of live database retrieval or retained feedback. |
| FileStateStore | `crates/bran-core/src/database/state.rs` | Direct open/put/get/verify; [MEM-OBJ-file-state](#mem-obj-file-state). Opaque payload lineage/consumer unresolved, not automatically agent memory. |
| Export/reparse | `crates/bran-core/src/export/mod.rs`, `examples/obsidian/usage.rs` | Direct export types/validation entry and complete example. [MEM-CMP-obsidian-export](#mem-cmp-obsidian-export). Reparse implementation not fully audited; example establishes in-memory round-trip call, not persistent deployment. |
| Agent consumption instructions | `skill/use-bran/SKILL.md` | Direct complete read; [RT-BAP-evidence-supply](runtime.md#rt-bap-evidence-supply). Instruction compliance unobserved. |
| Evaluators, deployment and release | `tools/ci/check.sh`, `benches/context_packet.rs`, `deploy/systemd/bran-check@.service` | Boundary/runtime-supplied coverage only. Fixtures, benchmarks and CI are source-defined evaluators, not measured successful runs or a learned store. No exhaustive evaluator-internal audit. |

CLI dispatch exposes named commands rather than an inspected autonomous memory-tool planner. The registered-root restrictions, optional SQZ port, generic `AgentRuntime` port and structural `ConnectedCoordinator` alternatives remain as supplied in runtime. No new hook or registered-tool loop is inferred from documentation. Searching CLI source for `FileStateStore`, `rebuild_artifact` and `EvidenceEngine` found no matches; this bounds the missing integration evidence to that source tree, not the entire repository or possible external callers.

## Core ideas

1. **Repository context is selected afresh.** Query/packet supplies bounded evidence by request, metadata and dependency rules. The caller can request more; BRAN does not automatically reload every omitted file into an ongoing conversation. Settings, document excerpts and SCIP supplements change what reaches a consumer, but do not establish semantic correctness. See [RT-RTE-query-packet](runtime.md#rt-rte-query-packet), [MEM-RTE-document-selection](#mem-rte-document-selection) and [MEM-RTE-symbol-reload](#mem-rte-symbol-reload).
2. **Query history is diagnostic, not an automatic ranking update.** The retained request and ranking descriptors feed gap summaries, proposal candidates and replay against live files. Candidates deliberately lack replacement content and authority. This is a trace-to-diagnostic chain, not evidence of a durable, automatically adopted behavior-shaping revision. See [MEM-RTE-evidence-feedback](#mem-rte-evidence-feedback).
3. **Connected completion keeps evidence products locally.** Canonical answers, support records and opaque lossless artifacts are separate retained parts. The CLI `get` consumer decodes an inline result; it does not indiscriminately return every stored artifact. Retrieval by digest is identity lookup, not relevance selection. Local publication remains independent of the provider's no-session contract. See the annotation on [RT-RTE-connected-request](runtime.md#rt-rte-connected-request).
4. **Admission differs by surface.** TUI Apply expresses operator configuration choice; maintenance accepts caller-supplied content and asserted authority; derived-only rebuilding can synthesize its own authority token; query and result storage use software gates without per-content human approval. None of these mechanisms by itself demonstrates improved capacity. See [RT-RTE-settings-apply](runtime.md#rt-rte-settings-apply), [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply) and [MEM-RTE-derived-rebuild](#mem-rte-derived-rebuild).

## Shared records

### Components

#### MEM-CMP-database-evidence
Label: DatabaseEvidence extraction interface

Source-native identity: `EvidenceEngine`, `extract` and `DatabaseEvidence::packet_evidence`. Form: symbolic descriptors, SQL gates and canonical provenance, with separately held typed row cells whose text may be interpreted as natural language when supplied to an agent. Storage: Rust values returned by extraction; external engine state remains behind a port. No persistence or trace-fed update follows merely from extraction. Unlike [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet), this is a producer API, not the assembled evidence payload. No supplied counterpart after comparison.

SRC-1, `crates/bran-core/src/database/evidence.rs`, `crates/bran-core/src/database/mod.rs`, implementation: request access/allowlist gates can reject before contacting the engine; admitted outcomes can become node/content inputs. The provenance `record` omits rows and credentials, while packet content explicitly joins the record with `rows_text`; those are different retained-information possibilities, not interchangeable summaries. Actual engine enforcement, payload origins, durable admission and later invocation consumer remain uninspected. The API affords bounded extraction; it does not establish a deployed memory route.

> /// Canonical provenance JSON. It never holds rows or credential material.
> --- `crates/bran-core/src/database/evidence.rs`

> let content = format!("{}\n{}", self.record, rows_text(&self.rows));
> --- `crates/bran-core/src/database/evidence.rs`

#### MEM-CMP-obsidian-export
Label: Obsidian portable export interface

Source-native identity: `export_to_obsidian`, `ObsidianBundle`, `reparse_obsidian`. Form: natural-language Markdown body plus symbolic scalar frontmatter, wikilinks and embedded graph records; substrate: an in-memory map of path to Markdown strings, not intrinsically a filesystem write. Lineage: caller-supplied nodes/edges, validated then serialized; unknown scalar fields are retained as strings. No supplied counterpart after comparison with [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet): this is portable export rather than query selection.

SRC-1, `crates/bran-core/src/export/mod.rs`, `examples/obsidian/usage.rs`, implementation. The example constructs one node and edge, calls export then reparse, and prints keys. This is an explicit shipped immediate consumer, not evidence that an external Obsidian user later reloaded modified documents. Export admission rejects invalid identity/path/public-boundary material rather than repairing it. Human authorship, long-term persistence, later agent uptake and semantic improvement remain unresolved.

> let bundle: ObsidianBundle = export_to_obsidian(&[n], &[e]).unwrap();
> let _ = reparse_obsidian(&bundle);
> --- `examples/obsidian/usage.rs`

### Operative objects

#### MEM-OBJ-evidence-request
Label: Recorded query request

Source-native identity: `QueryEvidenceRecord.request`. Form: natural-language request stored in an escaped symbolic record; substrate: `.bran/cache/query-evidence` under the first requested root. Lineage: caller's query, retained only with recording enabled. Consumer: replay reuses the request to run current selection; summary/propose can also expose requests in stale gaps. It is not source-document content or a derived answer. Admission is caller-enabled software persistence, with caller humanity unresolved. Distinct from the current evidence payload [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet); no supplied object counterpart.

SRC-1, `crates/bran-cli/src/main.rs`, implementation. The file is versioned `BRAN-QUERY-EVIDENCE/1`; request cap 4096 bytes, eight roots, 32 records, 64 KiB encoded file. Exact request/root-list identity replaces an earlier record; a full store rejects new identity rather than automatically aging it out. See [MEM-RTE-evidence-feedback](#mem-rte-evidence-feedback).

> query_evidence_from_live(
>     roots,
>     record.request.clone(),
>     record.requested_roots.len() > 1,
> )
> --- `crates/bran-cli/src/main.rs`

#### MEM-OBJ-evidence-rankings
Label: Recorded query access descriptors

Source-native identity: the other operative fields of `QueryEvidenceRecord`: roots, semantic outcome, matched/unmatched terms and `QueryEvidenceRanking` entries. Form: symbolic access/selection metadata; substrate: same local file as [MEM-OBJ-evidence-request](#mem-obj-evidence-request), but different content and consumers. Lineage: deterministic projection of the query invocation, not full raw event logs or copied document bodies. Consumers: gap analysis, candidate generation, comparison with replay rankings. Authority: diagnostic input to CLI output; no automatic replacement admission or ranking-weight update established. Closest supplied [RT-OBJ-packet-receipt](runtime.md#rt-obj-packet-receipt) is current packet accounting, not this retained query trace.

SRC-1, `crates/bran-cli/src/main.rs`, implementation. Match reason, rank, bundle/locator, exact/partial counts and active/canonical/public-safe/confidence/freshness fields survive. Their existence does not prove retained source truth, full enterprise-document anchor coverage or long-term relevance. Document matches extend term coverage in replay, but are not separately serialized as `QueryEvidenceRanking` anchor records by the inspected builder.

> let (matched, unmatched) = query_term_coverage(&request, matched_terms);
> --- `crates/bran-cli/src/main.rs`

#### MEM-OBJ-result-answer
Label: InlineResult answer text

Source-native identity: `InlineResult` answer. Form: natural-language answer; substrate: canonical encoded inline result in a content-addressed filesystem batch under `.bran/results`. Producer: accepted provider response after runtime validation/SQZ constraints. Consumer: `do_get` decodes canonical bytes and emits the answer. This is derived output, not a raw conversation transcript. It is distinct from [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet), the input evidence; its containing publication route is [RT-RTE-connected-request](runtime.md#rt-rte-connected-request).

SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/agent/coordinator.rs`, implementation. Retention does not prove later model consumption. `get` checks stored-byte integrity, not freshness of cited repository files at retrieval time. Outer caller determines whether to reuse it.

> let result = match InlineResult::decode_canonical(&bytes) {
> --- `crates/bran-cli/src/main.rs`

#### MEM-OBJ-result-support
Label: InlineResult citations and claims

Source-native identity: `InlineResult` citations/claims, mechanically distinct from its answer text [MEM-OBJ-result-answer](#mem-obj-result-answer). Form: symbolic IDs, locator and content digest plus natural-language claim/support strings interpreted by a reader and constrained by fixed equality/fidelity rules during completion. Substrate: same canonical inline-result bytes. Lineage: accepted provider claims checked under the grounded route; generic ungrounded calls have weaker requirements as [RT-RTE-runtime-port](runtime.md#rt-rte-runtime-port) explains. Consumer: `get` returns IDs, text, material flag, locator, content digest and support; there is no inference that support strings retain the model's reasons or deliberation.

SRC-1, `crates/bran-cli/src/main.rs`, implementation. Distinct from [RT-OBJ-packet-receipt](runtime.md#rt-obj-packet-receipt): these fields ground an output, not packet-selection accounting. The shared source file's JSON formatting reads `claim.text()`, `claim.content_digest()` and `claim.support()` into returned claims. The supplied runtime's exact-support passages establish the admission checks, not a new semantic truth oracle.

> json_escape(claim.content_digest()),
> json_escape(claim.support())
> --- `crates/bran-cli/src/main.rs`

#### MEM-OBJ-lossless-artifact
Label: LosslessArtifact retained bytes

Source-native identity: provider `LosslessArtifact` bytes and digest. Form: opaque payload; its encoding and semantic meaning cannot be classified from a generic byte container. Symbolic content IDs are not readable payload summaries. Substrate: separate content-addressed item in the result publication batch. Lineage: provider-produced artifact, checked for digest consistency and public DLP in the inspected coordinator. Consumer: runtime immediately reads every published item back for byte equality; later library `ResultStore::get` affords access, but `do_get` expects canonical `InlineResult`, not arbitrary artifact decoding. No specific later agent artifact-consumer route established. No supplied counterpart after comparison with [RT-RTE-connected-request](runtime.md#rt-rte-connected-request), which contains publication but does not separately classify this part.

SRC-1, `crates/bran-core/src/agent/coordinator.rs`, implementation.

> for artifact in artifacts {
>     batch.push(artifact.bytes());
> }
> --- `crates/bran-core/src/agent/coordinator.rs`

#### MEM-OBJ-derived-index
Label: Derived index and cache hashes

Source-native identity: `DerivedArtifactKind::Index` and `Cache` outputs. Form: symbolic sorted key-to-content-identity lines, not embeddings or copied source content. Substrate: returned bytes, optionally written at a classified derived path by [MEM-RTE-derived-rebuild](#mem-rte-derived-rebuild). Both use the same hash projection and admission mechanism; consumers beyond caller/repair validation remain unestablished. Lineage: caller-supplied bytes, not inherently execution traces. No supplied counterpart after comparison with [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply).

SRC-1, `crates/bran-core/src/derived_state.rs`, implementation.

> // Cache: same as index format (key\tdigest\n).
> --- `crates/bran-core/src/derived_state.rs`

#### MEM-OBJ-derived-snapshot
Label: Derived snapshot bytes

Source-native identity: `DerivedArtifactKind::Snapshot`. Form: symbolic key/length framing around unchanged opaque input bytes; substrate: returned buffer or classified derived file. Unlike [MEM-OBJ-derived-index](#mem-obj-derived-index), content survives, but input provenance and later semantic consumer are unspecified by the API. This alternative checkpoint is not established as conversational compaction. No supplied counterpart after comparison with [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply).

SRC-1, `crates/bran-core/src/derived_state.rs`, implementation.

> // Snapshot: key\nlen\ncontent\n per entry.
> --- `crates/bran-core/src/derived_state.rs`

#### MEM-OBJ-derived-report
Label: Derived report display

Source-native identity: `DerivedArtifactKind::Report`. Form: display text with a header and key/value summaries; substrate: returned bytes or classified derived file. Lineage: deterministic lossy display of caller inputs, not model-written synthesis. Values over 128 bytes are shortened and carry total byte count. The output is not equivalent to the raw snapshot [MEM-OBJ-derived-snapshot](#mem-obj-derived-snapshot); later human/model reading is possible but not wired by this function. No supplied counterpart after comparison with [RT-OBJ-packet-receipt](runtime.md#rt-obj-packet-receipt).

SRC-1, `crates/bran-core/src/derived_state.rs`, implementation.

> let display = if val.len() > 128 {
> --- `crates/bran-core/src/derived_state.rs`

#### MEM-OBJ-generated-validator
Label: GeneratedValidator bytes

Source-native identity: `DerivedArtifactKind::GeneratedValidator`. Form: sorted caller keys and opaque input content with a symbolic content-identity footer; substrate: returned bytes or classified derived file. The label does not establish synthesized checks, executable meaning or execution by a later validator. Unknown input semantics and consumer prevent capability-learning attribution. Distinct from [MEM-OBJ-derived-report](#mem-obj-derived-report) because content is not display-truncated. No supplied object counterpart after comparison with [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply).

SRC-1, `crates/bran-core/src/derived_state.rs`, implementation.

> // Generated-validator: sorted key→content, with content-identity footer.
> --- `crates/bran-core/src/derived_state.rs`

#### MEM-OBJ-file-state
Label: FileStateStore opaque objects

Source-native identity: `FileStateStore` objects. Form: opaque caller bytes named by symbolic SHA-256 ID; substrate: `<state root>/<location>/<namespace>/objects`, alongside layout version and staging directory. Lineage: generic `StateStore::put` caller; not necessarily agent traces or knowledge. Consumer: caller-directed `get` and integrity `verify`, not a demonstrated later invocation route. Different store from [MEM-OBJ-result-answer](#mem-obj-result-answer): generic namespace/quota store rather than the CLI's bounded result batches. No supplied counterpart after comparison with [RT-RTE-runtime-port](runtime.md#rt-rte-runtime-port).

SRC-1, `crates/bran-core/src/database/state.rs`, implementation. Open refuses unsupported backend/encryption/layout, checks directory/file kinds, removes abandoned staging files. Put admits nonempty bytes within quota, stages/syncs/renames, can replace a damaged hash-named object; get rehashes. Source comments retain check/use races and missing parent-directory fsync as limits. Generic caller identity leaves human approval unresolved; payload meaning and later behavioral authority are uninspected.

> if ResultId::sha256(&bytes) != *id {
>     return Err(StateStoreError::Corrupt);
> }
> --- `crates/bran-core/src/database/state.rs`

### Routes

#### MEM-RTE-evidence-feedback
Label: Recorded query diagnostic feedback

Endpoints/progression: opt-in query recording projects request/outcome/rankings into a local store; later explicit evidence commands load it, scan current roots, derive gaps/candidates or rerun recorded requests and compare rankings. Code owns each transformation; caller owns invocation and any subsequent content edit. Related to [RT-RTE-query-packet](runtime.md#rt-rte-query-packet) but distinct: this route begins with its retained query-use result and ends in later diagnostic output, not ordinary fresh packet emission. Objects are [MEM-OBJ-evidence-request](#mem-obj-evidence-request) and [MEM-OBJ-evidence-rankings](#mem-obj-evidence-rankings). SRC-1, `crates/bran-cli/src/main.rs`, implementation.

- Immediate return: query output plus recording success/error; evidence commands return summary, candidates, replay differences or clear receipt.
- Later read-back: explicit summarize/propose/replay loads persisted request/roots/access descriptors; summary uses unmatched terms and ranked locators plus current inventory; replay resubmits the recorded request against live roots. Not automatic prompt injection.
- Delegated visibility: inapplicable — these commands perform deterministic processing and return JSON, with no model delegation in this chain.
- Selection predicate: opt-in query recording; same request and ordered roots replace prior identity; later evidence commands load all stored records within caps. Gap analysis groups unanswered terms, path-only retrieval, never-retrieved/unclassified documents and stale/missing/unavailable evidence.
- Invalidation or expiry: no clock expiry in inspected evidence store; explicit clear removes the file. Same-identity recording replaces prior data; new identity at 32 records rejects. Stale locators are diagnostics, not automatic record withdrawal. Invalid/unsafe/oversized stores fail closed.
- Activation or effect: deterministic diagnostic output is wired. Candidate production does not change source, rank policy or settings; downstream authoring/adoption is not established.
- Evidence limits: no observed commands or benefit; replay compares outcome/ranking descriptors, not answer correctness, full source bodies or every native-document anchor. API input origin does not establish human per-record approval.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller enables recording, software checks field/file/path bounds and writes through private temporary file plus rename. Deduplication is exact request/root equality, not semantic consolidation. Summarize/propose/replay are read-only with respect to source content; clear is caller-triggered withdrawal. Replay turns evaluation errors into an unavailable current record for comparison rather than retaining a new baseline. Candidate proposals contain null replacement and authority, so a separate author and admission route would be needed to affect source. Reference outcome: the recorded outcome/ranking baseline, not a trusted expected answer. Operating mode: open requests and explicit retrospective diagnostics, not a bounded experimental curriculum.

> records.retain(|existing| {
>     existing.request != record.request || existing.requested_roots != record.requested_roots
> });
> --- `crates/bran-cli/src/main.rs`

> "{{\"kind\":\"{}\",\"target\":{},\"term\":null,\"replacement\":null,\"authority\":null}}",
> --- `crates/bran-cli/src/main.rs`

#### MEM-RTE-document-selection
Label: Admitted document evidence selection

Endpoints/progression: document discovery or inspect reads bounded native bytes, routes format adapter admission, obtains anchors/fidelity, then query/packet matches anchor text and serializes source metadata, matches and optional excerpts. Code is producer/selector; caller decides use. Distinct material subpath of the supplied combined query/packet route.
Part of: [RT-RTE-query-packet](runtime.md#rt-rte-query-packet)

SRC-1, `crates/bran-cli/src/document_evidence.rs`, `crates/bran-document/src/admit.rs`, implementation. Natural-language anchor text is distinct from symbolic source digest/locator/fidelity. Admission constructs projections in memory, not durable learned documents. Authoring/source ingestion control remains with file producers; starting query is not approval of each anchor. Adapter/parser safety and envelope admission are software gates, not semantic truth adjudication.

- Immediate return: document envelope for inspect; sources/matches/refusals/unsupported and omission accounting for query/packet, optionally excerpt text.
- Later read-back: later query/packet explicitly rereads repository document bytes; no admitted-anchor history store established. File creation and revision provenance are uninspected.
- Delegated visibility: outer agent receives selected JSON/excerpts; no document-parser model delegation established by this path.
- Selection predicate: query terms/entities score anchor text by case-insensitive substring; positive embedded anchors sort by score then bundle/path/ID; OCR-derived positives follow without byte-derived rank; total matches are truncated. Excerpts obey shared remaining and per-excerpt byte budgets, backing off UTF-8 boundaries.
- Invalidation or expiry: each invocation reads files again and computes source digest; typed refusals prevent admission for invalid inputs. No time-based anchor cache expiry applies to this builder.
- Activation or effect: selected metadata/excerpts are delivered; no trace establishes agent reliance or fidelity of all native conversions.
- Evidence limits: text may be normalized or derived; digest identity and admission are not source truth. No external OCR execution or full parser-fidelity audit was performed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if candidate.anchor.derivation == Derivation::Ocr {
>     derived.push(index);
> } else {
>     embedded.push((index, candidate.score));
> }
> --- `crates/bran-cli/src/document_evidence.rs`

> .min(budget.remaining_bytes)
> .min(budget.per_excerpt_bytes);
> --- `crates/bran-cli/src/document_evidence.rs`

#### MEM-RTE-symbol-reload
Label: Existing SCIP evidence reload

Endpoints/progression: query/packet resolves existing `index.scip`, checks/decode/freshness, selects symbol evidence for requested candidates and ranked sources, filters to retained sources and encodes symbol details/payload lines. Owner: CLI selection code. This is an additional material subpath, not an independently trained store.
Part of: [RT-RTE-query-packet](runtime.md#rt-rte-query-packet)

SRC-1, `crates/bran-cli/src/main.rs`, implementation; `skill/use-bran/SKILL.md`, doctrine/design. Storage: externally produced on-disk index; form: symbolic symbol IDs, roles, spans and relations, not embeddings. Numerical field values are not distributed parameters. Initial producer/version provenance remains external/uninspected.

- Immediate return: retained per-source symbols, symbol navigation hit/miss/unavailable and freshness diagnostics; packet may receive formatted symbol lines.
- Later read-back: explicit query/packet rereads the existing file on each call; this is reload of an external retained index, not conversation recall or query-history feedback.
- Delegated visibility: returned symbol annotations go to the packet/query consumer; no external indexing invocation is performed by the inspected resolve path.
- Selection predicate: request-derived symbol candidates, ranked source paths/ranks and maximum 64 evidence items; subsequent selected-source filtering can remove evidence before delivery. Symbol matches do not change source ranking according to shipped instructions.
- Invalidation or expiry: stale index yields no symbol evidence; unverified freshness is partial, not proof of currency; missing/unreadable index reports unavailable. Index regeneration belongs to producer outside this path.
- Activation or effect: supplementary navigation evidence is wired; actual navigation correctness or agent use is unobserved.
- Evidence limits: index producer and decoder/freshness internals not fully inspected; external source-to-index derivation correctness and operational freshness not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> scip::Freshness::Stale => return Self::unavailable("stale", "index_stale"),
> --- `crates/bran-cli/src/main.rs`

> index.evidence(&symbol_candidates(query_text), &ranked, MAX_SYMBOL_EVIDENCE);
> --- `crates/bran-cli/src/main.rs`

#### MEM-RTE-derived-rebuild
Label: Derived-only deterministic rebuild

Endpoints/progression: library caller provides target and keyed bytes; `classify` restricts target; `rebuild` sorts/deduplicates, rejects conflicting keys and emits a kind-specific projection; `rebuild_artifact` proposes then applies through caller-supplied repair coordinator and validator. Distinct from CLI [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply): a derived-only helper can create default authority automatically; this is not the fixture-gated CLI invocation. SRC-1, `crates/bran-core/src/derived_state.rs`, implementation.

- Immediate return: typed rebuild refusal or receipt with artifact kind/target/input digest/output hash/authority tag; pure rebuild returns bytes.
- Later read-back: an admitted derived file remains available to its caller, but no specific later agent invocation consumer is established by this helper. Storage capability alone is not an integrated memory route.
- Delegated visibility: inapplicable — deterministic rebuild performs no model delegation.
- Selection predicate: caller-selected keyed inputs and classified derived target; sort and identical-key/value deduplication, conflicting values reject. Kind determines hash projection, raw snapshot, lossy report or validator-framed content.
- Invalidation or expiry: rebuilt target replaces its prior derived artifact under coordinator checks; validation failure follows repair refusal/recovery. Automatic time expiry is not established.
- Activation or effect: helper wires derived-file publication through repair; production invocation and downstream behavioral effect remain unobserved/unestablished.
- Evidence limits: arbitrary input origin, incomplete caller inventory and unknown later consumers prevent attribution of trace learning, executable validator adaptation or automatic production self-improvement.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission/proposal owner: software computes the output; caller chooses inputs/coordinator; absent explicit authority, helper constructs `derived-rebuild-auto`. Validator can reject; recovery inherits coordinator limits in [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply), not an unconditional I/O rollback guarantee. Human review is not a prerequisite expressed by this helper. No expected task-answer oracle; validator success is its local admission criterion. Mode: explicit deterministic rebuild API. Outputs are separately classified as [MEM-OBJ-derived-index](#mem-obj-derived-index), [MEM-OBJ-derived-snapshot](#mem-obj-derived-snapshot), [MEM-OBJ-derived-report](#mem-obj-derived-report) and [MEM-OBJ-generated-validator](#mem-obj-generated-validator). Input provenance is not supplied by the type, so none is presumed trace-fed.

> let authority = authority.unwrap_or_else(|| MaintainerAuthority::new("derived-rebuild-auto"));
> --- `crates/bran-core/src/derived_state.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-diagnostic-supply
Label: Query-use diagnostics to caller

Consumer: caller of evidence summarize/propose/replay. Channel: JSON gaps, candidate targets and replay differences derived from retained query metadata and current roots. Force: diagnostic evidence, not source-writing permission, enforced instruction or adopted policy. Horizon: later command invocations across uses of a repository, until replacement/clear; only potential downstream agent/human interpretation is afforded. SRC-1, `crates/bran-cli/src/main.rs`; see [MEM-RTE-evidence-feedback](#mem-rte-evidence-feedback) for passages. Distinct from [RT-BAP-evidence-supply](runtime.md#rt-bap-evidence-supply), which supplies selected repository evidence, not retrospective access diagnostics. No demonstrated behavior change or benefit.

## Annotations

#### On [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet)

Memory consumers: explicit outer-agent packet/query reader or current connected model, not a demonstrated recurrent history consumer. Direct document/symbol reads show additional by-value evidence can be omitted or rendered without full source bytes: document excerpt budgets truncate text; symbol evidence is filtered to selected source locators. These mechanisms supplement the supplied closure/item/byte/token bounds; they do not create automatic reload of omitted parts. SRC-1, `crates/bran-cli/src/document_evidence.rs`, `crates/bran-cli/src/main.rs`; evidence in [MEM-RTE-document-selection](#mem-rte-document-selection) and [MEM-RTE-symbol-reload](#mem-rte-symbol-reload).

#### On [RT-RTE-connected-request](runtime.md#rt-rte-connected-request)

Retained parts: [MEM-OBJ-result-answer](#mem-obj-result-answer), [MEM-OBJ-result-support](#mem-obj-result-support) and [MEM-OBJ-lossless-artifact](#mem-obj-lossless-artifact). Storage uses SHA-256 item identity, batch directories, operation lock, temporary private files and rename. Code checks item/batch limits and immediately retrieves each item to confirm bytes. Direct filesystem reads confirm expired batches and abandoned transactions are removed during enumeration; oldest batches are selected for capacity eviction after new publication with recovery logic. Maxima: 16 entries, 4 MiB total, 1 MiB/item and 86,400 age ticks. These are local storage controls, not external host-session guarantees. SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/agent/coordinator.rs`.

Read-back trigger/selector/delivery: caller supplies result ID to `get`; lookup searches surviving batches newest first, rehashes bytes, then CLI decodes `InlineResult` and returns answer/citations/claims JSON. Identifier lookup has no semantic targeting beyond requested content identity. Retained results are not automatically added to future connected prompts in the inspected path. `get` does not repeat source-file freshness validation, so stored support can describe an earlier repository state. Opaque artifact IDs afford library retrieval but do not establish a dedicated CLI artifact-display or later agent-use route. Curation here is canonical encoding and acceptance, not retrospective semantic consolidation. No execution or activation is observed.

> for (stored_id, payload) in stored_ids.iter().zip(batch.iter()) {
>     if store.get(stored_id, now_tick).ok().as_deref() != Some(*payload) {
>         return None;
>     }
> }
> --- `crates/bran-core/src/agent/coordinator.rs`

> if now.saturating_sub(tick) >= RESULT_STORE_LIMITS.max_age_ticks {
>     fs::remove_dir_all(entry.path()).map_err(|_| ResultStoreError::Unavailable)?;
>     continue;
> }
> --- `crates/bran-cli/src/main.rs`

#### On [RT-RTE-settings-apply](runtime.md#rt-rte-settings-apply)

Memory-specific classification: retained symbolic configuration, not natural-language knowledge or use-derived rationale. Software resolution and physical persistence follow an operator Apply choice in TUI, while lower-level API humanity remains unresolved. Later packet/connected consumers give executable configuration force to effective values across invocations. The report's supplied passages and [RT-BAP-settings-consumption](runtime.md#rt-bap-settings-consumption) support these points; no trace-responsive settings revision or learning benefit is established. SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-tui/src/settings.rs`.

#### On [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply)

Memory-specific classification: replacement content inherits its form from caller bytes; publication can change natural-language repository knowledge, but admission success does not establish criticism or improved knowledge. Retained reasons for the content change and a later rationale-reader are not specified by the coordinator. Successful source replacement becomes available to subsequent scans; failed validation restores or exposes recovery failure as supplied. The separate derived-only default-authority helper is [MEM-RTE-derived-rebuild](#mem-rte-derived-rebuild), not an override of the CLI fixture marker. SRC-1, `crates/bran-core/src/derived_state.rs`, `crates/bran-core/src/repair/mod.rs`.

## Write side

**Repository content and acquisition.** Initial source authorship and per-file human approval are uninspected for arbitrary repositories. This does not suppress known subsequent transformation: deterministic scan/graph/ranking and native document admission select and project existing bytes. Source metadata such as canonical/public-safe/confidence/freshness affects selection, not an independent warrant for claims. The shipped instruction explicitly distinguishes semantic query outcome from process success and asks the consumer to preserve provenance. SRC-1, `skill/use-bran/SKILL.md`; [RT-RTE-query-packet](runtime.md#rt-rte-query-packet), [MEM-RTE-document-selection](#mem-rte-document-selection).

**Query-use transformation.** Raw query invocation → request plus selected access/outcome descriptors → persisted record → later gap summary/candidate/replay JSON is the demonstrated implementation chain. It retains match reasons and baseline fields, not full source bodies, model reasoning or a complete raw event trace. Replay reruns current files; summarize/propose combine history with current document coverage and stale diagnostics. Candidates do not contain proposed replacement bytes or authority. There is therefore no established automatic trace → durable instruction/knowledge revision → later agent consumption chain. A caller could author a repair, but no inspected handoff automatically supplies that missing content/admission. [MEM-RTE-evidence-feedback](#mem-rte-evidence-feedback).

**Connected result admission.** Provider supplies an answer and optional artifacts; runtime software validates before publication. The grounded production path's exact-support requirements must not be generalized to ungrounded library calls. No human approval gate is required per answer in the supplied production route. Local storage canonicalizes and integrity-checks accepted products; no-session does not suppress this write. Cleanup is age/capacity-driven, cancellation gates publication, and errors can leave a retained result even if later CLI packaging fails as runtime notes. This retains evidence products, not a model-weight update or demonstrated summarization of a conversation. [RT-RTE-connected-request](runtime.md#rt-rte-connected-request), [RT-RTE-runtime-port](runtime.md#rt-rte-runtime-port), connected annotation above.

**Editing, maintenance and alternate storage.** TUI Apply and maintain apply retain configuration or supplied replacement content under different gates; neither proves human per-content approval at every API. Derived rebuild additionally offers automatic authority within a derived-only target class. Its hash-only index/cache, raw snapshot, truncated report and validator-framed bytes must not be conflated as one memory representation. Generic `FileStateStore` can retain arbitrary opaque bytes, and database extraction can form bounded evidence without a durable store. Neither supplies a demonstrated later agent consumer. Obsidian export/reparse is a shipped immediate representation round trip, not proof of persisted knowledge adoption. [MEM-RTE-derived-rebuild](#mem-rte-derived-rebuild), [MEM-OBJ-file-state](#mem-obj-file-state), [MEM-CMP-database-evidence](#mem-cmp-database-evidence), [MEM-CMP-obsidian-export](#mem-cmp-obsidian-export).

## Read-back

Read-back is predominantly **caller-requested**, not unsolicited recall. Query/packet targets repository material using the request; recorded evidence commands target retained query-use history plus current roots; `get` targets an exact retained result ID. These differ in both selector and consumer. A direct `get` is targeted identity lookup, but not query-conditioned relevance ranking. Default packet generation is new retrieval from files, not history injection. The later evidence/replay commands do consume use-derived retained material. Their JSON return does not establish that a subsequent model changed its decisions. [RT-RTE-query-packet](runtime.md#rt-rte-query-packet), [MEM-RTE-evidence-feedback](#mem-rte-evidence-feedback), connected annotation.

The outer agent is a documented consumer role in the shipped skill: one initial packet, focused follow-up queries, honest interpretation of semantic outcomes, then its own decisions and implementation. This establishes an afforded external consumption route without proving deployed use. Connected execution wires evidence to one provider invocation per attempt; no provider-internal recurrent tool/session mechanism is available for inspection. SQZ is an optional transformation with external fidelity limits, not an established memory consolidation mechanism. [RT-CLM-evidence-location](runtime.md#rt-clm-evidence-location), [RT-RTE-connected-request](runtime.md#rt-rte-connected-request), [RT-RTE-structural-connected](runtime.md#rt-rte-structural-connected).

Working-context control is by **pre-invocation selection**, not plain accumulation and not an inspected conversation-compaction loop. Code decides scan/rank/closure/budget inclusion; document excerpts and symbol filtering supply additional omission points. Full files remain reachable through another explicit query or inspect command; no pointer automatically dereferences them. A packet resembles a returned by-value selection, not a shared heap. BRAN's external host call can keep outer deliberation outside BRAN's request, but it does not establish a fresh model stack frame, session erasure, verbatim tail, or summary escaping a popped subagent context. The supplied max delegation depth is a control field, not proof of an implemented separate-context subagent loop. [RT-RTE-query-packet](runtime.md#rt-rte-query-packet), [MEM-RTE-document-selection](#mem-rte-document-selection), [MEM-RTE-symbol-reload](#mem-rte-symbol-reload), [RT-RTE-connected-request](runtime.md#rt-rte-connected-request).

## Integration issues

- **No supplied fact correction is required.** Runtime's explicit-authority statement is scoped to maintain CLI/core apply. [MEM-RTE-derived-rebuild](#mem-rte-derived-rebuild) adds a derived-only helper that creates default authority; integration must preserve this alternative rather than generalizing mandatory human approval over all derived writes. Evidence: SRC-1, `crates/bran-core/src/derived_state.rs`, quoted default authority.
- **Containment, not replacement:** [MEM-RTE-document-selection](#mem-rte-document-selection) and [MEM-RTE-symbol-reload](#mem-rte-symbol-reload) are material parts of [RT-RTE-query-packet](runtime.md#rt-rte-query-packet). Their separate selector, representation and failure semantics motivate separate records. Other declarations have no supplied referent counterpart after the comparisons stated in their bodies; no possible-duplicate candidate is identified.
- **Native-document history is narrower than output:** [MEM-OBJ-evidence-rankings](#mem-obj-evidence-rankings) stores Markdown/source-ranking descriptors while document matches can affect term coverage. Replay differences compare recorded outcome/rank fields, not a complete anchor-level history. Evidence: SRC-1, `crates/bran-cli/src/main.rs`, inspected `query_evidence_from_live`. Prevented conclusion: exhaustive document retrieval regression evaluation from the record alone.
- **Stored result versus current source:** [MEM-OBJ-result-support](#mem-obj-result-support) preserves old support/digests; `get` verifies store bytes and decoding, not current cited files. Prevented conclusion: retrieval itself re-attests current repository support. Opaque [MEM-OBJ-lossless-artifact](#mem-obj-lossless-artifact) has immediate integrity read-back but no established dedicated later agent consumer.
- **Unresolved integration:** [MEM-RTE-derived-rebuild](#mem-rte-derived-rebuild), [MEM-OBJ-file-state](#mem-obj-file-state) and [MEM-CMP-database-evidence](#mem-cmp-database-evidence) expose operations, but direct CLI-tree search did not identify their production integration. Missing facts: actual caller, payload/trace provenance, persistence policy and next invocation consumer. These prevent treating every library storage or generated-validator label as an active learning loop; they do not erase the implemented APIs.
- **Parser/index fidelity and external hosts remain limited:** detailed native-parser conformance and SCIP freshness internals were not audited here; model, SQZ and index-producer internals remain outside the frozen source as boundary specifies. [MEM-RTE-document-selection](#mem-rte-document-selection), [MEM-RTE-symbol-reload](#mem-rte-symbol-reload), [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model). Prevented conclusions: complete source fidelity, exercised no-retention, real model identity/version or actual benefit.

## Limitations and checks

Source HEAD was rechecked as `7bc428b2ccdfad38e05caa0c0cba2bb19041993a`, equal to boundary. Source identity, run identity and reviewed boundary are unchanged. This member follows the supplied memory type, job, worker rules and records contract; only assigned outputs were written. No target code/tests/examples/services were executed. Direct source reads and supplied runtime findings are distinguished in the coverage table. A failed exploratory search for CLI-local `scip.rs` was corrected by locating the module at `crates/bran-core/src/scip.rs`; CLI symbol selection, not an invented local file, supports the findings.

No causal claim of improved learning, autonomous theory revision or exercised self-improvement is made. The query-use diagnostic chain and configuration/source publication capacities coexist with missing downstream adoption and outcome evidence. No negative claim about hidden model cognition follows from source opacity.

Deterministic validation: the assigned `commonplace-validate` command with `--artifact` and `--role memory` passed (exit status 0): “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” A pass establishes form and quotation occurrence, not semantic support or workflow acceptance.
