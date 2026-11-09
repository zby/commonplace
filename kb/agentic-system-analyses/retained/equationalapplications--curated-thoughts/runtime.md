---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Curated Thoughts runtime: file deposits, librarian proposals, review, recall and alternate control paths at the frozen commit."
run-id: AAS-2026-11-08-curated-thoughts-00ab3a770403-01
reviewed-boundary: "433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd"
---

# Curated Thoughts runtime report

## Runtime account

Curated Thoughts is a file-to-retained-knowledge system with model-assisted proposal generation, not an enclosing general-purpose agent executor. Its declared work is to make ordinary files into short facts that later agents can recall (SRC-1, `INTENT.md`; [boundary](boundary.md#boundary-and-evidence)). The ordinary agent-facing loop is deposit → ingest → librarian → proposal admission → later recall. The caller owns when to deposit or recall; Rust owns the intervening sequence. The generation model proposes content but does not select arbitrary next tools in the inspected librarian loop. See [RT-RTE-deposit-kick](#rt-rte-deposit-kick), [RT-RTE-librarian-synthesis](#rt-rte-librarian-synthesis), [RT-RTE-proposal-admission](#rt-rte-proposal-admission) and [RT-RTE-context-recall](#rt-rte-context-recall).

### Shipped entry paths and ordinary invocation

The desktop executable selects `--mcp` before GUI dispatch, also handling onboard/doctor subcommands. The full MCP server resolves configuration, attempts migrations, opens a read-only query connection and constructs a `local-mcp` dispatch context with lazy write access. Its primary connection being read-only does not make the server read-only. The independent tools MCP binary has a narrower catalog and a separate best-effort write connection for logging. `ct` supplies headless ingest, librarian, recall, review, repair and deposit operations. SRC-1, `src-tauri/src/main.rs`, `src-tauri/src/mcp_server.rs`, `tools/src/bin/curated_thoughts_mcp.rs`, `tools/src/bin/ct.rs`.

For a normal `wisdom_deposit` call, an external agent supplies a vault-relative path, title and body. The dispatcher checks the deposit lane and writes a new file exclusively, then records audit and kick state. It launches a blocking ingest/librarian task and immediately returns path, `pending: true` and a kick label. With generation unconfigured, it returns `no_ingest_host` rather than claiming successful synthesis. The CLI counterpart requires `--yes` and waits for the kick so shutdown cannot strand a merely queued blocking task. Neither starting the CLI nor passing `--yes` proves a human authored or reviewed each fact. SRC-1, `src-tauri/src/wisdom_deposit.rs`, `tools/src/bin/ct.rs`.

The kick acquires the vault lock with bounded contention retries, resolves a canonical document key, ingests bytes from the vault, records `chunked`, and calls `generate_summary` when generation is configured. Persistent lock contention records `queued_watcher`, delegating actual progress to a running watcher. The desktop pipeline similarly calls `generate_summary` after successful ingest and records errors without terminating its whole job loop. Epoch checks prevent superseded workers proceeding at stage boundaries; this is not evidence of arbitrary thread termination or provider cancellation. SRC-1, `src-tauri/src/wisdom_deposit.rs`, `src-tauri/src/pipeline/mod.rs`.

The librarian applies folder mode, tier and note-level suppression gates, loads ordered chunks, then skips an unchanged content-hash/model pair unless forced. It builds candidate entity/fact context, numbered chunks and structural context; truncates the assembled input; calls configured generation; parses JSON; filters proposals; and inserts bundles. Folder rules determine whether bundles await review or are auto-approved. Seeded agent-deposit rules request synthesis with auto-approval, while the fallback is summarize without auto-approval. Consequently a mandatory per-fact human review is not the shipped default for every source. SRC-1, `src-tauri/src/librarian/mod.rs`, `src-tauri/src/librarian/synthesis.rs`, `src-tauri/src/db/connection.rs`.

Admission converts accepted proposal items into database mutations through the shared commit resolver. The GUI supports item decisions and edited payloads; automatic synthesis constructs accept-all decisions. The shared transaction is a structural consistency boundary, not an answer oracle for factual truth. Later `curated_recall_context` returns keyword-ranked wiki entries plus cosine-ranked code chunks as JSON, not a generated answer. The external calling agent decides what to do with them. Source inspection establishes delivery wiring, not compliance, use or improvement. SRC-1, `src-tauri/src/db/commit.rs`, `src-tauri/src/proposals_api.rs`, `src-tauri/src/tool_dispatch.rs`.

### Selected forcing routes and guarantees

Four forcing cases qualify the baseline; none was executed here.

1. **Suppressed or unavailable synthesis.** Index mode and tiers that skip fact extraction return before model work; readable `wisdom: false` also suppresses it, but file-read failure falls toward extraction. The hash/model gate is only a named-model gate: an endpoint changing its weights behind the same name need not dirty the document. Malformed model JSON gets one corrective retry. Failure logs and can return `Ok(())` without writing a proposal, so neither a successful Rust return nor the kick's `ingested` ledger alone proves knowledge was produced. Empty validated output also writes a watermark. SRC-1, `src-tauri/src/librarian/mod.rs`, `src-tauri/src/librarian/synthesis.rs`, `src-tauri/src/wisdom_deposit.rs`.
2. **Automatic versus manual admission after source deletion.** `resolve_proposal` rejects auto-approval if deleted-source provenance exists, inside the transaction. The librarian recognizes the typed refusal and can leave that proposal pending while processing other bundles. Manual resolves do not pass that auto-only guard. CLI review reaches a non-auto, non-human-surface resolver; its terminal check is expressly hygiene, not authentication. Thus “only a person can resolve a vanished-source proposal” would overstate this enforcement. GUI manual resolves set the human-surface flag, CLI review does not. Source attestation can independently give `user_stated` provenance when its conditions hold. SRC-1, `src-tauri/src/db/commit.rs`, `src-tauri/src/db/proposals_review.rs`, `src-tauri/src/proposals_api.rs`, `tools/src/cmds.rs`.
3. **Read-only MCP is not equivalent to full MCP.** The full dispatcher fails curated read calls when their required audit insert fails. The separate tools MCP performs recall and logs best-effort, allowing results even when logging is unavailable. It opens a read-only primary connection but also an audit write connection and optionally starts an outbox worker. “Read-only” describes its knowledge tool surface, not an invariant that the process makes no writes. SRC-1, `src-tauri/src/tool_dispatch.rs`, `tools/src/bin/curated_thoughts_mcp.rs`.
4. **Cloud capability exclusion and alternate paths.** The shared dispatcher denies names beginning `curated_` or `wisdom_` for `clanker-bridge` before deserialization. The production bridge context actually supplies that label. But legacy `wiki_search`, `wiki_context`, graph operations and vault write operations are separate match arms not covered by this prefix deny. This is a tool-family gate, not proof that cloud sessions cannot access any retained knowledge or write any vault file. Nor is a client string an authenticated principal across every possible caller. SRC-1, `src-tauri/src/lib.rs`, `src-tauri/src/tool_dispatch.rs`, `src-tauri/src/cloud_bridge/mod.rs`.

The load-bearing guarantees have different strengths:

| Owner and enforcement point | Strength and coverage | Required external contract and limits | Implementation conclusion status | Operation conclusion status |
| --- | --- | --- | --- | --- |
| Deposit core: lane validation and exclusive create | invariant within this write route: refuse existing destination instead of overwrite | Filesystem exclusive-create semantics; not OS-wide isolation against arbitrary shell/host writes, and not a multi-resource atomic transaction | wired | uninspected |
| Shared commit resolver: immediate transaction and auto-only deleted-source guard | invariant for transaction rollback; policy for which resolves must refuse deleted sources | SQLite locking/rollback; manual routes differ and downstream truth is not checked by transactionality | wired | uninspected |
| Shared dispatcher: bridge client-prefix deny | policy over this dispatcher and its tagged context | Correct host context construction; legacy names remain separate capabilities | wired | uninspected |
| Shipped recall/deposit skill interpreted by external agents | protocol, not a code invariant | External agent must load and follow it; CTI and host permissions are outside the frozen sources | claimed | uninspected |

The capability surface includes file writes, knowledge admission, model calls, local inference machinery and optional remote services. The current grants depend on entry path, configuration and client context. No deployed sandbox, shell restriction or actual granted filesystem envelope was supplied. Do not infer deployed confinement from the tool catalog. The GUI also exposes a distinct wiki-engine callback route, [RT-RTE-wiki-maintenance](#rt-rte-wiki-maintenance); librarian validation cannot be generalized to that returning-computation path. SRC-1, `src/lib/wiki.ts`, `src-tauri/src/inference/mod.rs`.

### Context, recovery and evidence boundary

Librarian generation is a fresh system/user request, not a persistent chat transcript. Candidate selection uses chunk mean embeddings and name hits, limits entity candidates, clips summary snippets, limits recent candidate facts and then truncates the whole context to 4,000 characters (`char_indices().nth`, despite the constant's byte-oriented name). Candidate text precedes document text and structural context, so the suffix can be omitted. Validation still receives the untruncated candidate and numbered-chunk collections: it checks identifiers against those collections, not proof that every cited chunk survived model-input truncation. SRC-1, `src-tauri/src/librarian/synthesis.rs`. This is bounded input assembly, not observed adaptive compaction. No retained conversational summary or delegated sub-agent context is established by this route.

Recovery is distributed: file retention plus kick ledger, watcher handoff, dirty-document watermark retries, logged synthesis errors, transaction rollback, and best-effort embedding backfill. They do not jointly establish exactly-once end-to-end processing. In particular, the filesystem deposit cannot share the audit transaction; audit failure attempts compensating file removal. Provider or embedding failure can leave pending work or committed entries without embeddings. SRC-1, `src-tauri/src/wisdom_deposit.rs`, `src-tauri/src/librarian/synthesis.rs`, `src-tauri/src/proposals_api.rs`.

All source findings here use SRC-1's implementation layer unless explicitly called intent or instruction. Added inspection beyond the boundary's initial entry-point coverage includes `src-tauri/src/db/commit.rs`, `src-tauri/src/db/proposals_review.rs`, folder-rule seeding in `src-tauri/src/db/connection.rs`, `src-tauri/src/embedder/mod.rs`, `src-tauri/src/inference/mod.rs`, deposit kick/write ranges, dispatcher read/write/deny branches and CLI terminal-review ranges. No supplied run or causal experiment was used; target binaries, tests and model endpoints were not executed. External wiki-engine internals, CTI and provider implementations remain outside the frozen source. Memory revision semantics, evaluator outcomes and theory-building assessments are left for the specialists rather than inferred from names such as “wisdom” or “synthesis.”

## Shared records

### Components

#### RT-CMP-generation-provider
Label: Configured generation provider

The generation model is distributed-parametric content hosted behind HTTP or a configured local model/sidecar. Model name, URL, key and path are symbolic configuration on disk; system/user messages are natural-language inputs. The inspected calls perform inference, not parameter updates. Exact weight versions are not pinned by the request's model-name string. A mutable external endpoint can resolve to another model; local model identity depends on the deployed file, not just the recorded label. Provider internals and actual weight mutability are uninspected. SRC-1, `src-tauri/src/librarian/synthesis.rs`, `src-tauri/src/inference/mod.rs`.

> let body = serde_json::json!({
>             "model": self.model_name,
>             "messages": [
>                 { "role": "system", "content": system },
>                 { "role": "user", "content": user }
>             ],
> --- `src-tauri/src/librarian/synthesis.rs`

#### RT-CMP-embed-profile
Label: Configured embedding model

`EmbedProfile` selects local Ollama or an external embedding endpoint; the Cloud variant explicitly returns an implementation error. Learned embedding parameters are distributed-parametric; returned vectors are dense numerical representations persisted separately from chunk text. Production inference paths inspected do not update weights. Names and endpoints are configurable rather than immutable weight pins; a mutable local service or remote endpoint can change the served model. Provider internals remain uninspected. The test stub takes precedence over profile selection, and FastEmbed MiniLM is separately retained for benchmarks, so not every vector-producing branch is production learned inference. SRC-1, `src-tauri/src/embedder/mod.rs`.

> EmbedProfile::Cloud { .. } => Err(anyhow!("cloud embed not implemented")),
>             EmbedProfile::External { profile } => profile.embed(texts),
> --- `src-tauri/src/embedder/mod.rs`

### Operative objects

#### RT-OBJ-folder-rules
Label: Folder rules

SQLite `folder_rules` is symbolic mode/auto-approval policy. Ancestor lookup tries source-path candidates, including a vault-relative derivation when resolvable; default is summarize without automatic approval. Migration inserts agent-lane synthesis/auto-approval only if absent and after the required schema gate, not an unconditional override of every deployment's rules. SRC-1, `src-tauri/src/librarian/mod.rs`, `src-tauri/src/db/connection.rs`.

> "SELECT librarian_mode, auto_approve FROM folder_rules WHERE folder_path = ?1",
> --- `src-tauri/src/librarian/mod.rs`

#### RT-OBJ-synthesis-prompt
Label: Synthesis prompts

Rust string constants contain natural-language librarian instructions mixed with a symbolic JSON schema, selected by summarize/synthesize mode and extended with ontology vocabulary. They reside in shipped source, not a model-written prompt store. The model interprets the prose; Rust parses and filters the response. Contradiction instructions are requests, not proof of criticism occurring. SRC-1, `src-tauri/src/librarian/synthesis.rs`.

> - Do not modify ANCHOR TRUTH chunks; contradictions become fact_update or fact_archive proposals with reasoning.
> --- `src-tauri/src/librarian/synthesis.rs`

### Routes

#### RT-RTE-deposit-kick
Label: Deposit and ingest kick

External caller → file writer → audit/ledger → blocking kick → shared ingest and librarian. Rust owns progression; the caller authors the proposed source text. The capability admits a new source file, not direct arbitrary brain-row insertion through this tool. Shape/path validation can reject it; model and folder policies decide downstream proposals. Correction is a new deposit or supersession request, not an overwrite. Rollback across file and SQL resources is compensating removal, not atomicity. Open-request mode; no expected-answer oracle. SRC-1, `src-tauri/src/wisdom_deposit.rs`, `tools/src/bin/ct.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: MCP returns path, pending and kick label; CLI waits for the kick but retains the initial response shape.
- Later read-back: file, ledger and derived indexed content persist for later processing/status/recall.
- Delegated visibility: blocking kick receives vault/database paths and configuration; no separate model-agent context is created by spawning the worker.
- Selection predicate: valid new path in the agent lane, excluding supersessions; nonempty title/body; configured generation controls kick spawning.
- Invalidation or expiry: no overwrite; supersession is a separate proposal route; downstream retention is not guaranteed by file creation.
- Activation or effect: source-file creation and scheduling are wired; later behavioral activation is unobserved.
- Evidence limits: contention can hand responsibility to a watcher; ledger success is not proof of a committed fact or deployment progress.

> .create_new(true)
>         .open(&validated)
> --- `src-tauri/src/wisdom_deposit.rs:854-855`

#### RT-RTE-librarian-synthesis
Label: Librarian proposal generation

Indexed document → gates/context assembly → [RT-CMP-generation-provider](#rt-cmp-generation-provider) → JSON parsing/filtering → stored proposals → optional admission. Rust owns sequence; model proposes summaries/facts/edges/tasks under [RT-OBJ-synthesis-prompt](#rt-obj-synthesis-prompt). Software rejects unknown entity/fact identifiers and invalid/empty items, but resolution of evidence labels can drop unknown references without dropping a nonempty added fact. This is not a semantic truth validator. [RT-OBJ-folder-rules](#rt-obj-folder-rules) chooses summarize/synthesize and automatic admission. Open-document processing with dirty/forced modes, not a curriculum; no answer oracle. Source text and existing candidates guide proposals; reasoning and proposals persist in database records. Rejection/manual editing and transaction recovery belong to [RT-RTE-proposal-admission](#rt-rte-proposal-admission). SRC-1, `src-tauri/src/librarian/mod.rs`, `src-tauri/src/librarian/synthesis.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: unit result; model/validation errors may be logged and converted to a successful unit return without proposals.
- Later read-back: admitted content can enter later candidate context and recall; successful/empty output writes the hash/model watermark.
- Delegated visibility: model receives a system prompt and truncated user context; not arbitrary database access or arbitrary tool execution in this call.
- Selection predicate: folder/tier/note gates, nonempty chunks and dirty watermark unless forced; candidates selected by name and embedding similarity.
- Invalidation or expiry: changed hash or active model name dirties a document; force bypasses watermark but not earlier extraction gates.
- Activation or effect: proposal insertion and optional auto-resolution are wired; correctness and changed downstream behavior remain unobserved.
- Evidence limits: identifier validation uses full pre-truncation collections; model compliance and provider internals are uninspected.

> if !candidate_ids.contains(existing_id.as_str()) {
>                     continue;
>                 }
> --- `src-tauri/src/librarian/synthesis.rs`

#### RT-RTE-proposal-admission
Label: Proposal resolution and provenance

Pending proposal plus per-item decisions → shared resolver → immediate transaction → committed entries, resolution state and outbox effects. GUI operator can accept/edit/reject; automatic synthesis accepts all constructed decisions; CLI terminal review permits approve/reject/detail/skip/quit but calls the agent-surface resolver. Software has vetoes for transaction failures and auto-only vanished-source checks. No expected-answer oracle; the content judge is the operator/model/caller according to entry path, not SQLite. This is knowledge admission, not product-code self-modification. Proposal reasoning and decisions are retained; failed transactional mutations roll back and pending proposals can be retried. Post-commit embedding recovery is best-effort. SRC-1, `src-tauri/src/db/commit.rs`, `src-tauri/src/db/proposals_review.rs`, `src-tauri/src/proposals_api.rs`, `tools/src/cmds.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: commit/review outcome or refusal/error; GUI wrapper attempts embedding sweep after commit.
- Later read-back: committed live entries become candidates and retrieval results; resolution/provenance remain available beyond this invocation.
- Delegated visibility: embedding precomputation sends accepted text to the configured embedding service; GUI releases its main database mutex around that work.
- Selection predicate: pending proposal with items and caller decisions; provenance considers human_surface, auto_approve, accepted edits and source attestations separately.
- Invalidation or expiry: rollback on transaction failure; non-pending proposals rejected; later archival/heal/prune are separate mechanisms.
- Activation or effect: accepted item mutations change retained knowledge; no supplied trace establishes subsequent behavior or benefit.
- Evidence limits: terminal presence does not authenticate a human; human-tier metadata does not prove factual correctness; manual resolves are outside the auto-only deleted-source guard.

> if options.auto_approve {
>         let vanished: i64 = tx.query_row(
>             "SELECT EXISTS(SELECT 1 FROM curated_proposal_deleted_sources
>               WHERE proposal_id = ?1)",
> --- `src-tauri/src/db/commit.rs`

> human_surface: false,
>             reviewed_by: Some(reviewed_by.to_string()),
> --- `src-tauri/src/db/proposals_review.rs`

#### RT-RTE-context-recall
Label: Recall result delivery

Caller query → [RT-CMP-embed-profile](#rt-cmp-embed-profile) → keyword wiki ranking plus cosine code ranking → structured response. Full MCP uses the shared dispatcher and a fail-closed audit write; the tools MCP implements a separate handler and best-effort logging. Wiki terms shorter than two bytes are omitted; live entries rank by term overlap, then confidence ordinal, then update time. Calling this recall “semantic wiki search” would confuse it with the distinct `wiki_search` route. SRC-1, `src-tauri/src/tool_dispatch.rs`, `tools/src/bin/curated_thoughts_mcp.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON wiki_entries, code_chunks and query; no generated answer.
- Later read-back: this invocation reads previously retained entries and indexed code; it does not itself revise their content.
- Delegated visibility: embedding service receives the query; the requesting external agent receives only selected results, not the full brain.
- Selection predicate: matching title/body terms for non-deleted wiki entries; cosine-ranked AST code chunks; caller limits default to five wiki and ten code results.
- Invalidation or expiry: deleted wiki entries omitted; query-dependent selection recomputed each call; host caching is outside this source boundary.
- Activation or effect: delivery is wired, but external use/compliance is unobserved. Full dispatcher also emits unverified-match prompt files before returning results.
- Evidence limits: no end-to-end host trace; embedding failure can prevent the whole recall even though wiki ranking itself is lexical; audit behavior differs between servers.

> let result = dispatch_curated_recall_context(ctx, p).await?;
>             log_curated_access_rw(ctx, "curated_recall_context", entity_id.as_deref(), "read")
>                 .await?;
> --- `src-tauri/src/tool_dispatch.rs`

#### RT-RTE-wiki-maintenance
Label: Wiki engine callbacks and scheduled maintenance

Frontend `ingestDocumentByPath` routes to external `wiki.ingestDocument`; its options supply generation/embedding callbacks through Tauri and an optional classifier only when available. Generated text returns directly from the inference HTTP adapter to the engine; it does not pass through the librarian's proposal parser. Internal engine admission/rejection is uninspected, not presumed equivalent. Separately, frontend deletion events debounce a native heal call and startup/daily timers request native prune unless busy. These native commands update status, call the backend heal/prune functions and report errors; heal attempts embedding repair. SRC-1, `src/lib/wiki.ts`, `src-tauri/src/inference/mod.rs`, `src-tauri/src/lib.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: engine result or callback text/error; scheduled native maintenance returns success/error and status changes.
- Later read-back: intended downstream wiki/maintenance effects concern retained entries; exact external-engine transformation internals remain uninspected.
- Delegated visibility: external engine receives selected document parameters and model callbacks; model sees supplied system/user strings, not a granted shell.
- Selection predicate: routed entity for document path; configured classifier availability; deletion event for heal, startup/daily timer and not-busy check for prune.
- Invalidation or expiry: cleanup removes subscriptions/timers; maintenance entry retention predicates are separate backend policy, not model-output validation.
- Activation or effect: callback, scheduling and native calls are wired; actual engine operation and benefit are unobserved.
- Evidence limits: external package implementation was not acquired; no answer oracle established for its model-generated changes, and no claim of universal proposal-gate coverage.

> return await invoke<string>("generate_text", { systemPrompt, userPrompt });
> --- `src/lib/wiki.ts`

### Claims

#### RT-CLM-agent-workflow
Label: Agent recall and deposit protocol

Shipped skill instructs external agents to recall before coding and deposit after non-trivial work. This is doctrine/design, not an observed invocation or an enforced ordering constraint. The separate tools MCP lacks the deposit surface, so skill availability must not be equated with an actual configured write grant. SRC-1, `.skills/curated-thoughts/skill.md`, `tools/src/bin/curated_thoughts_mcp.rs`.

> Call `curated_recall_context` with the task description to fetch relevant wisdom and code patterns. Example:
> --- `.skills/curated-thoughts/skill.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-librarian-guidance
Label: Librarian prompt authority

Consumer: configured generation model. Channel: system/user HTTP messages carrying shipped guidance, source chunks and retained candidate facts. Force: natural-language interpretation with downstream symbolic parsing and admission checks, not guaranteed compliance. Horizon: one synthesis invocation; the admitted output may affect later synthesis/recall through [RT-RTE-librarian-synthesis](#rt-rte-librarian-synthesis) and [RT-RTE-context-recall](#rt-rte-context-recall). SRC-1, `src-tauri/src/librarian/synthesis.rs`; supporting passage in [RT-CMP-generation-provider](#rt-cmp-generation-provider).

#### RT-BAP-bridge-tool-gate
Label: Bridge dispatcher capability gate

Consumer: shared Rust dispatcher. Channel: symbolic tool name and host-set client label. Force: immediate rejection before tool deserialization for curated/wisdom families on the bridge context. Horizon: every dispatch through that context, not all processes or alternate legacy tool names. Production context construction supplies the label; this is more than a documentation-only restriction, but it is not OS isolation. SRC-1, `src-tauri/src/tool_dispatch.rs`, `src-tauri/src/lib.rs`.

> if client == "clanker-bridge" && (tool.starts_with("curated_") || tool.starts_with("wisdom_")) {
>         anyhow::bail!("curated memory tools are not available to cloud-bridge sessions: {tool}");
>     }
> --- `src-tauri/src/tool_dispatch.rs`

## Annotations

none
