---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "AI-Context-OS workflow account tracing inbox text through optional model proposal, caller disposition and canonical memory delivery."
run-id: AAS-2026-10-18-ai-context-os-82777c0c3926-01
reviewed-boundary: "9ed263080cadf98702bebb42d5260b45bd526f6c"
---

# AI-Context-OS workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is **capture text → generate an ingestion proposal → caller applies or rejects it → optionally deliver a canonical memory for later retrieval**. It was selected because it crosses the system's capture, model-delegation, durable review and admission boundaries in one implemented chain. It is a model-assisted knowledge-ingestion workflow, not a demonstrated autonomous multi-agent task execution. The caller supplies the next command; the provider proposes content but does not control admission. The baseline records this chain as [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal), its candidate as [RT-OBJ-ingest-proposal](runtime.md#rt-obj-ingest-proposal), and later context serving as [RT-RTE-context-query](runtime.md#rt-rte-context-query).

All findings concern SRC-1 at the frozen revision in [the boundary](boundary.md). Additional implementation inspection covered text capture, heuristic/duplicate construction, inference payload and parsing, proposal generation/persistence/rejection, destination validation, memory construction/application in `src-tauri/src/commands/inbox.rs`; the corresponding wrappers in `src/lib/tauri.ts`; and serialization/I/O in `src-tauri/src/core/memory.rs`. A scoped search of `src/` found the proposal generation/apply/reject wrapper declarations, not a review-screen invocation. Thus the chain is an implemented callable workflow; neither an exercised human review process nor successful end-to-end operation was observed. No target or provider was executed.

### 1. Capture and request ownership

A command caller gives `create_inbox_text` a title, content and tags. The backend selects the active root, creates a UUID-suffixed ID, trims content, computes a content hash, derives a summary and writes an inbox item. It updates the manifest and daily log, marks a recent write and emits `inbox-changed`. The returned item is the capture result, not a canonical memory. Root inbox exclusion from later canonical scanning is supported by the boundary's quoted index implementation. [SRC-1: `src-tauri/src/commands/inbox.rs`]. See also [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal).

> write_inbox_item(&item)?;
> update_manifest_from_disk(&root)?;
> --- `src-tauri/src/commands/inbox.rs:1585-1586`

The caller separately requests `generate_ingest_proposals` with item IDs, or an empty vector for all loaded items. Generation loads persisted proposals and skips an item that already has a Pending proposal. It processes selected items sequentially, awaiting inference for each and emitting progress events. This is a code-owned batch loop, not delegation to independently scheduled agent workers. [SRC-1: `src-tauri/src/commands/inbox.rs`]

### 2. Proposal construction and model handoff

Before inference, code constructs a fallback. Matching another inbox item's content hash or nonempty source URL selects a duplicate-discard proposal. Otherwise text with a nonempty, multiline L1 gets a promotion heuristic; other text gets a needs-review heuristic. This is candidate construction under coded rules, not a quality oracle. [SRC-1: `src-tauri/src/commands/inbox.rs`]

`infer_proposal` loads the workspace provider configuration and rejects a missing or disabled provider. Its one provider call supplies a conservative JSON-only instruction plus the selected item's ID, kind, title, summary, L1/L2, URL, tags and extraction/inference flags, together with a response schema. It does not supply conversation history or assembled vault context. The shared provider component's version and mutability limits remain those of [RT-CMP-inference-provider](runtime.md#rt-cmp-inference-provider). [SRC-1: `src-tauri/src/commands/inbox.rs`]

> include_vault_context: false,
> context_prompt: None,
> context_memory_ids: Vec::new(),
> --- `src-tauri/src/commands/inbox.rs:1427-1429`

The return crossing this handoff is provider text. Code strips Markdown JSON wrapping and deserializes it as `ProposalModelResponse`; it clamps confidence, fills missing content from the item and creates a Pending proposal with provider/preset provenance. Successful inference replaces the heuristic except when the heuristic was duplicate-discard. Even that duplicate branch attempts inference, but its result cannot override the discard choice. JSON parsing verifies structure, not truth, ontology suitability or usefulness. No expected-answer/reference oracle judges the content. [SRC-1: `src-tauri/src/commands/inbox.rs`]. See [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal).

### 3. Failure recovery and durable review handoff

When inference returns an error, generation emits `inference-error`, logs the fallback and retains the prebuilt heuristic proposal; it does not retry the provider in that loop. It then writes the proposal JSON, attempts to mark the inbox item ProposalReady/Pending, and returns generated candidates. Proposal write errors propagate; the item-status update at this stage is explicitly ignored. Existing Pending proposals block regeneration until their state changes. [SRC-1: `src-tauri/src/commands/inbox.rs`]

> Err(e) => {
>     eprintln!(
>         "[inference] Fallback to heuristic for '{}': {}",
>         item.title, e
>     );
>     let _ = app.emit("inference-error", format!("{}: {}", item.title, e));
> }
> --- `src-tauri/src/commands/inbox.rs`

The candidate and rationale survive in JSON and can be reloaded with `list_ingest_proposals`. The caller owns the disposition handoff through apply/reject wrappers. Starting generation does not establish per-content human approval, and confidence is not an automatic admission threshold. These limits qualify the source's governed-ingestion language rather than imply that human review cannot occur. [SRC-1: `src/lib/tauri.ts`, `src-tauri/src/commands/inbox.rs`]. See [RT-OBJ-ingest-proposal](runtime.md#rt-obj-ingest-proposal).

Rejection finds a proposal by ID, persists Rejected, attempts to mark its item Processed/Rejected, appends a rejection log and emits a proposal-change event. It does not dispatch a canonical write. This is a persistent disposition, not an enforced irreversible veto: application independently finds a proposal by ID without testing Pending state. Thus a later caller can attempt to apply a rejected proposal. [SRC-1: `src-tauri/src/commands/inbox.rs`]. See [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal).

### 4. Admission, delivery and later consumption

Application loads the proposal and its source item. For PromoteMemory, the caller may supply a destination and memory-ID override. Destination validation canonicalizes paths and rejects a destination outside the root or equal to the designated inbox, sources or .ai directories; it is a path check, not content review. It creates a missing directory before validating its containment. This order does not support a guarantee of no filesystem effects on rejected input. The backend then constructs a memory from proposal fields, with item fallbacks and derivation ID, and writes Markdown. [SRC-1: `src-tauri/src/commands/inbox.rs`]

For RouteToSources, it writes a protected Source memory, appends original URL/file references when present, and copies available attachments. Discard changes the item state. NeedsReview and UpdateMemory only mark the item processed; they do not implement canonical review or merge despite their action names. These action boundaries are already evidenced in [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal). [SRC-1: `src-tauri/src/commands/inbox.rs`]

After action dispatch, application persists Applied. Promotion/source routing also marks the item Promoted, refreshes the index and attempts router regeneration. It appends a daily log, emits change events and returns the proposal. This successful return is the command-level delivery criterion; for promotion the consequential artifact is the written canonical file, not the returned proposal alone. Router regeneration failure is ignored, so delivery does not guarantee synchronized adapters. [SRC-1: `src-tauri/src/commands/inbox.rs`]

The writes are not a single transaction: `write_memory` serializes frontmatter/body and directly writes the target. Later proposal, status or log failures can occur after the memory exists; the inspected application body supplies no compensating rollback. The caller must inspect persisted state before retrying rather than infer that an error left nothing written. No automatic recovery owner beyond fallback generation and caller-directed subsequent commands is established on these paths. [SRC-1: `src-tauri/src/core/memory.rs`, `src-tauri/src/commands/inbox.rs`]

> fs::write(path, content).map_err(|e| format!("Failed to write {}: {}", path.display(), e))?;
> --- `src-tauri/src/core/memory.rs`

Later context queries rescan canonical files and select bodies for a consumer under [RT-RTE-context-query](runtime.md#rt-rte-context-query). A delivered memory is therefore eligible retained knowledge, not necessarily selected or behaviorally used. The workflow ends at admission/return; no supplied trace closes the subsequent retrieval → provider interpretation → correct task-result chain. Nor does the provider's separate proposal context isolate external hosts or clear already delivered text. The supported mechanism is bounded proposal inference followed by caller-controlled persistence, not demonstrated learning or self-improvement.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal)

Workflow handoffs: capture and generation are separate commands; generation serially awaits each optional model proposal, persists candidates, then returns control. Apply/reject requires another caller command. The provider receives only the selected item/schema and conservative instruction, not a sub-agent task frame with tool execution. Its text return is parsed into a candidate; admission is not delegated to that provider.

Verification and recovery: structural JSON acceptance and coded duplicate precedence constrain proposals without establishing semantic correctness. Inference errors preserve heuristic output. Caller rejection persists disposition but is not an apply-time state gate. Partial write failures can leave artifacts before a command reports failure; no transaction or automatic rollback is established.

Delivery boundary: successful promotion means canonical Markdown plus attempted index/router refresh and a returned Applied proposal. A source-route result differs from promotion; status-only actions deliver no canonical update. Later consumption is eligible through context scanning, not demonstrated activation. These workflow findings are supported by the account's inspected SRC-1 passages and do not change the route's generic identity or implementation/operation statuses.
