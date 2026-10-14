---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "EchoWiki workflow tracing watcher detection, human source approval, model-assisted compilation and persistent wiki delivery."
run-id: AAS-2026-10-14-echowiki-8d428f79523e-01
reviewed-boundary: "11446997423e88177dba62d6a3d5c1e8b4886c62"
---

# EchoWiki workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is an eligible raw text file detected by the Obsidian watcher, queued for human approval, then compiled into persistent wiki pages. It connects a shipped source-admission gate with the shared compilation and delivery path. It was selected because it exposes both the human veto and the later software admission of model-generated content. Watch mode and require-approval must be enabled for this branch; actual deployed settings and successful execution are not supplied. This is an implementation trace at the frozen revision, not an observed workflow (SRC-1: `obsidian-plugin/src/raw-watcher.ts`, `obsidian-plugin/src/main.ts`, `src/wiki/compiler.ts`; [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval), [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)).

Inspection checked watcher, approval modal, plugin main lines 100–244, the complete compiler and its parsing/concurrency helpers. These are implementation evidence within SRC-1, not additional sources. The supplied runtime records provide the broader storage and authority context. No target code, provider, example or test was executed.

### 1. Detection hands a path to the human gate

Vault create/modify events are filtered to supported raw text files and watch-enabled settings. The watcher replaces a path's outstanding timer and waits one second before handing that path to the plugin. The plugin ignores a path already in flight; otherwise require-approval queues it instead of compiling. The persisted queue holds path and insertion time, not file bytes or a proposed wiki change. This is event-driven work, not an experiment with an expected-answer oracle (SRC-1: `obsidian-plugin/src/raw-watcher.ts`, `obsidian-plugin/src/main.ts`; [RT-OBJ-pending-queue](runtime.md#rt-obj-pending-queue), [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval)).

Preview opens the file in Obsidian. Approve passes its path to `compilePendingItem`; reject removes the queue entry and reports it skipped. Rejection prevents this queued invocation, not future events or manual compilation, and does not delete the raw file. Approval authorizes compilation of the current file, not the content at detection time, a frozen preview or generated-page diffs (SRC-1: `obsidian-plugin/src/approval-modal.ts`, `obsidian-plugin/src/main.ts`).

> private async rejectItem(item: PendingItem): Promise<void> {
>     await this.plugin.removePendingItem(item.path);
>     new Notice(`Skipped ${item.path}`);
>     this.render();
>   }
> --- `obsidian-plugin/src/approval-modal.ts`

### 2. The plugin supplies a compilation request

The plugin owns the next handoff. It marks the path in flight, checks key/model settings, resolves the vault file, reads its current text and derives its document name. The request supplies that name, full text, vault-backed wiki storage, configured chat endpoint/model/credentials and optional language to the in-process compiler adapter. The human has selected the input, but does not separately approve each later page body (SRC-1: `obsidian-plugin/src/main.ts`; [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)).

The compiler loads stored or fallback instructions and requests a summary from the configured chat model. The next model call receives system instructions, full source, draft summary and all existing concept/entity briefs. It proposes create/update/related entries. Compiler code, rather than the model, decides which phase runs next and converts accepted plan entries into generation tasks. Existing page bodies are supplied only to selected update tasks (SRC-1: `src/wiki/compiler.ts`; [RT-OBJ-agents](runtime.md#rt-obj-agents), [RT-BAP-retained-pages](runtime.md#rt-bap-retained-pages)).

### 3. Explicit task contexts delegate generation, not orchestration

Concept and entity pools execute concurrently with a separate concurrency limit for each pool. Each task receives a fresh explicit message array: instructions, full source, draft summary, known targets and its page-specific request; updates additionally receive the old body without frontmatter. Sibling generation outputs and the full planning response do not enter that array. The task returns page content and brief metadata to compiler-owned result slots. These are calls to a model service, not independently scheduled agents with tool authority (SRC-1: `src/wiki/compiler.ts`, `src/wiki/llm.ts`; [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)).

This isolates sibling output from a generation context, but does not split the input document or impose a context budget. The whole source is repeated for each task. Only explicit return values escape to the writers; there is no reloadable conversation frame. Retained briefs and selected old bodies are the later-invocation reuse path described by [RT-BAP-retained-pages](runtime.md#rt-bap-retained-pages).

### 4. Verification admits structure, not proven knowledge quality

Code filters missing names and invalid entity types, verifies related-page existence, rejects empty page bodies and strips links outside the existing-plus-planned target set. These are structural admission rules. An unparseable page response can instead be admitted as raw text; link membership does not prove target existence after failed generation. Neither these checks nor the summary rewrite compare the final pages against an expected correct answer. The rewrite receives source, draft and target names, not the generated page bodies. Thus there is no evidenced independent semantic acceptance decision in this compilation path (SRC-1: `src/wiki/llm.ts`, `src/wiki/compiler.ts`; [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)).

> if (!content.trim()) {
>       throw new Error(`Empty content for concept ${name}`);
>     }
>     return { name, content, isUpdate: false, brief };
> --- `src/wiki/compiler.ts`

The operator can veto the queued source, but no subsequent per-page human gate intercepts accepted model text. Full rewrites are persisted. Instructions requesting preservation of manual edits are model-mediated guidance, not conflict detection or a veto over physical replacement; see [RT-CLM-conflict-policy](runtime.md#rt-clm-conflict-policy) and its supporting runtime passages (SRC-1: `src/wiki/compiler.ts`, `src/wiki/page-writer.ts`).

### 5. Writes and caller completion constitute delivery

After collecting results, the compiler writes entities, rewrites/writes the summary, writes concepts, adds related and reciprocal links, updates the index and finally appends the ingest log. The resolved compiler call lets the plugin announce completion and the pending-item wrapper remove the queue entry. Delivery is persistent wiki state plus caller completion, not evidence that a user read it, a model obeyed all instructions or all planned pages succeeded. The resulting briefs and selected page bodies can feed later compilations; browsing belongs to Obsidian (SRC-1: `src/wiki/compiler.ts`, `obsidian-plugin/src/main.ts`; [RT-RTE-document-compile](runtime.md#rt-rte-document-compile), [RT-BAP-retained-pages](runtime.md#rt-bap-retained-pages)).

> await appendLog(storage, 'ingest', `Compiled ${docName} from raw/`);
>   console.log(`  Done: ${docName}`);
> --- `src/wiki/compiler.ts`

### Failure, rejection and recovery limits

A model task exception becomes an error result and its page is skipped; the rest of the compilation can still resolve and clear the pending entry. An unparseable or empty plan writes a fallback summary and index; a failed summary rewrite uses the draft. These are degraded deliveries, not retries that establish eventual completion of every planned page (SRC-1: `src/wiki/compiler.ts`, `src/wiki/llm.ts`; [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)).

A thrown compiler/storage failure propagates to the approval modal's failure notice. Normally the pending wrapper never reaches removal, and `finally` clears the in-flight marker. A human may approve again, but that recomputes using current source/wiki rather than resuming a checkpoint. Earlier writes are not rolled back by this path. There is also a coordination caveat: `compileRawPath` returns normally when the path is already in flight, so another approval can reach queue removal without awaiting that active compilation. Queue disappearance alone is therefore not a universal delivery witness (SRC-1: `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/approval-modal.ts`).

> async compilePendingItem(path: string): Promise<void> {
>     await this.compileRawPath(path);
>     await this.removePendingItem(path);
>   }
> --- `obsidian-plugin/src/main.ts`

> async compileRawPath(vaultRelativePath: string): Promise<void> {
>     if (this.inFlight.has(vaultRelativePath)) {
>       return;
>     }
> --- `obsidian-plugin/src/main.ts`

Distinct paths are not serialized against shared wiki/index/log targets. Same-path suppression is not a whole-wiki lock or multi-file transaction. Actual races, restarts, user review, provider quality and vault durability remain unobserved. These limits qualify the selected workflow without inventing recovery supplied by the external host (SRC-1: `obsidian-plugin/src/main.ts`, `src/wiki/compiler.ts`; [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)).

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

#### On [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval)

Workflow boundary: source admission precedes generation. Human rejection is queue removal; approval identifies a current file by path, not a frozen source or generated diff. In the selected sequential path, compile completion precedes queue removal. The in-flight early return qualifies that ordering as a completion guarantee: overlapping approval need not wait for the active compile. The checked implementation passages are in the workflow account.

#### On [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

Workflow delivery criterion: after code-managed generation and writes, log append and resolved caller return permit completion notices and pending removal. Failed individual generation can coexist with this delivery criterion. Recovery ownership is split: compiler code supplies fallback/skip behavior, plugin code clears its in-flight marker and surfaces thrown failure, and the user can initiate another compilation. No supplied execution establishes complete-page delivery or successful recovery.
