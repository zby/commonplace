---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Talorys workflow tracing an owner-requested note rewrite from model tools through human approval, stale-target rejection and persisted delivery"
run-id: AAS-2026-10-15-talorys-7bce41ba9401-01
reviewed-boundary: c5da440010402ed4c1b9789ae22eab96a8f0f379
---

# Talorys workflow report

## Workflow account

### Selection and evidence

The representative workflow is an owner-requested rewrite of an existing note: find/read the note, propose replacement text, obtain owner approval, commit or reject, and expose the outcome. It is selected because the shipped `replace_note_content` tool connects model-generated content to an explicit human decision and a checked mutation. This is a source-supported possible sequence, not an observed request or a mandatory model plan. The model can receive an ID directly, skip search, or fail to read before proposing. All evidence is static implementation or shipped guidance from SRC-1 at the revision fixed in [boundary](boundary.md); no target execution establishes activation, successful completion or rewrite quality. [SRC-1: `apps/agent/src/tools/notes.ts`, `apps/agent/src/tools/registry.ts`]

Inspection adds detail to the runtime baseline at `apps/agent/src/tools/notes.ts`, `apps/agent/src/tools/registry.ts`, `apps/agent/src/db/repositories/pending-actions.ts`, `apps/agent/src/db/repositories/notes.ts`, `apps/agent/src/api/routes/chat.ts`, `apps/agent/src/agent/runner.ts`, `apps/agent/src/ai/workers-ai.ts`, `apps/web/src/pages/ChatPage.tsx` and `apps/web/src/components/ApprovalCard.tsx`. These supply implementation evidence; tool descriptions and receipt instructions also supply declared guidance. They introduce no new source or evidence layer. Existing runtime records cover the referents, so workflow-specific findings appear in Annotations rather than duplicate declarations.

### Request, delegated work and proposal

The owner submits a chat request through the browser. Protected HTTP routing and per-conversation active-run coordination lead to a persisted owner message and an assistant identity. The runner supplies selected memories, optional semantic items, summary and recent eligible history to the provider, plus permitted tool descriptions, schemas and callbacks. These are the existing [RT-RTE-owner-chat](runtime.md#rt-rte-owner-chat) and [RT-RTE-context-window](runtime.md#rt-rte-context-window) paths. The application delegates next-tool choice and proposed replacement wording to the model; it does not delegate another worker or an independent reviewer. The provider SDK advances model steps, and TypeScript callbacks retain effect authority. [SRC-1: `apps/agent/src/agent/runner.ts`, `apps/agent/src/ai/workers-ai.ts`]

If the model uses `search_notes`, the base tool returns up to eight IDs, titles and 400-character excerpts. `read_note` returns at most 8000 characters even though its description calls this the full content. Neither read is a precondition enforced by the rewrite tool. Replacement accepts 1–20000 characters and replaces the whole body, so a proposal can omit material the model never saw. These are content-visibility limits, not an observed loss. Semantic wrappers can change search delivery; this account does not generalize the base keyword results to enabled semantic search. The eventual human preview, not a complete-input guarantee, is the workflow's content review opportunity. [SRC-1: `apps/agent/src/tools/notes.ts`]; [RT-RTE-semantic-hooks](runtime.md#rt-rte-semantic-hooks).

The model calls `replace_note_content` with the note ID and complete proposed body. Executor checks tool availability, global/per-tool caps, schema and duplicate-call signature. Preparation resolves the note, constructs the owner-readable summary and stores the proposed body as both payload and preview; a hash covers current title, content and project ID. The pending action belongs to the conversation. The tool returns a proposal receipt rather than executing replacement, as [RT-RTE-action-approval](runtime.md#rt-rte-action-approval) establishes. Tool descriptions and the receipt explicitly guide the model not to announce completion before approval. No expected rewrite or automated semantic-correctness oracle is provided. [SRC-1: `apps/agent/src/tools/notes.ts`, `apps/agent/src/tools/registry.ts`]

### Human decision, commit and delivery

The runner attaches the pending action to tool activity, streams it and saves it with the assistant response. The browser renders an ApprovalCard with the summary, full replacement preview as plain text, and Approve/Decline controls. The owner can reject this exact content or allow the protected approval endpoint to attempt commit. This is content-specific human admission in an open request, not merely permission to start a workflow. It does not prove the owner actually reads the preview. [SRC-1: `apps/agent/src/agent/runner.ts`, `apps/web/src/pages/ChatPage.tsx`, `apps/web/src/components/ApprovalCard.tsx`]

Approval is a separate HTTP request, not a continuation tool callable by the model. The handler conditionally claims the pending, unexpired action, checks the current snapshot hash, and dispatches the stored payload to the original destructive tool. For note replacement, commit validates the stored body again, updates the note and records `note.rewritten` activity. The repository issues a SQLite update and returns the new note. The handler returns the action status; the card updates and invalidates notes and conversation queries. Thus delivered replacement means an accepted commit to retained note state plus an exposed outcome, not just an assistant answer or a successful proposal callback. Platform durability and actual browser receipt remain unobserved. [SRC-1: `apps/agent/src/api/routes/chat.ts`, `apps/agent/src/tools/registry.ts`, `apps/agent/src/tools/notes.ts`, `apps/agent/src/db/repositories/notes.ts`, `apps/web/src/components/ApprovalCard.tsx`]

Later conversation reads refresh the action status from its durable row. On a later chat turn, the runner adds short approval-outcome notes to eligible history before context-window selection. It does not automatically rerun the model after the button click or supply the replacement body through that status note. The changed note remains available to later note reads/search. History eviction and summary selection still limit which outcome reaches a later model invocation. This is the later read-back already covered by [RT-RTE-action-approval](runtime.md#rt-rte-action-approval) and [RT-RTE-context-window](runtime.md#rt-rte-context-window), not evidence that a future answer used it. [SRC-1: `apps/agent/src/db/repositories/pending-actions.ts`, `apps/agent/src/agent/runner.ts`, `apps/agent/src/tools/notes.ts`]

### Rejection and recovery

A concrete rejection path is an owner edit or import changing a snapshot field after proposal and before the approval check. Claiming the action does not bypass the hash check: mismatch marks it failed without calling this tool's commit. The UI shows the failure reason. The owner must ask again for a fresh proposal; the consumed ID is not reopened. Decline cancels a still-pending action; expiry after 30 minutes or a prior resolution prevents approval. The owner owns content reconsideration and resubmission, while code owns rejection and status persistence. There is no automatic rewrite repair or generic undo in this path. [RT-RTE-action-approval](runtime.md#rt-rte-action-approval); SRC-1: `apps/agent/src/tools/registry.ts`, `apps/agent/src/db/repositories/pending-actions.ts`, `apps/web/src/components/ApprovalCard.tsx`.

The hash is a checked pre-commit snapshot, not a demonstrated transaction spanning asynchronous hashing, row claim and every subsequent effect. Claim precedes commit, so a crash between them can leave an approved row without completed work. The source supports at-most-one approval attempt through this handler, not crash-safe exactly-once completion. Cancellation or retry of chat also does not undo an already created proposal or earlier immediate tools. A new turn has fresh duplicate-call counters. These limits remain local to the approval and chat records, rather than being converted into a system-wide reliability judgment. [SRC-1: `apps/agent/src/tools/registry.ts`, `apps/agent/src/agent/runner.ts`]; [RT-RTE-owner-chat](runtime.md#rt-rte-owner-chat).

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

#### On [RT-RTE-action-approval](runtime.md#rt-rte-action-approval)

Workflow-specific visibility and admission: note replacement presents the exact proposed body to the owner, but does not ensure the proposing model saw all existing content. The base read callback is bounded:

> return { id: note.id, title: note.title, content: note.content.slice(0, 8000) };
> --- `apps/agent/src/tools/notes.ts`

Preparation binds payload and preview to the same proposed text:

> return { targetId: note.id, summary: `Rewrite note ${quoteTitle(note.title)} (${size})`, payload: { content: i.content }, preview: i.content };
> --- `apps/agent/src/tools/notes.ts`

The owner preview is plain text, not rendered Markdown. This is a review surface, not an automatic truth or preservation check. [SRC-1: `apps/web/src/components/ApprovalCard.tsx`]

> {/* Plain text, never rendered as Markdown: this is exactly what will be saved. */}
> --- `apps/web/src/components/ApprovalCard.tsx`

The versioned target for this workflow is content plus title and project membership, rather than the note timestamp or every database field:

> return n && [n.title, n.content, n.project_id];
> --- `apps/agent/src/tools/notes.ts`

The runtime record's mismatch passage supplies the rejection rule. The durable admission condition is:

> `UPDATE tal_pending_actions SET status = ?, resolved_at = ? WHERE id = ? AND status = 'pending' AND expires_at > ?`,
> --- `apps/agent/src/db/repositories/pending-actions.ts`

This supports a single claim of the ID, not proof that commit finished before interruption. The failure card and owner resubmission are the workflow recovery boundary. [SRC-1: `apps/agent/src/tools/registry.ts`, `apps/web/src/components/ApprovalCard.tsx`]

#### On [RT-RTE-owner-chat](runtime.md#rt-rte-owner-chat)

Workflow completion must distinguish proposal success from mutation success. Tool activity receives `success` whenever the provider emits a tool-end without error, including a successfully created approval proposal. In addition, a textless successful-tool turn gets a generic fallback:

> text = tools.some((t) => t.status === "success") ? "Done." : "I wasn't able to produce a response. Please try rephrasing.";
> --- `apps/agent/src/agent/runner.ts`

Consequently the receipt's instruction not to claim completion does not enforce all displayed assistant wording: this fallback can say “Done.” while an approval is still pending. The approval card still conveys pending state and the effect gate remains intact. A `complete` assistant record or successful tool chip therefore cannot verify delivered note replacement. This is a static reachable fallback, not an observed misleading reply. [SRC-1: `apps/agent/src/agent/runner.ts`, `apps/agent/src/tools/registry.ts`, `apps/web/src/components/ApprovalCard.tsx`]
