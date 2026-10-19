---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Workflow account of llmwiki-marimo's web question-to-reviewed-wiki-page path, including verification and failed-save recovery."
run-id: AAS-2026-10-18-llmwiki-marimo-58054ccd9ae7-01
reviewed-boundary: "0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7"
---

# llmwiki-marimo workflow report

## Workflow account

### Selection and evidence

The representative workflow is a web user asking a question, obtaining a grounded answer, drafting a concept page from the conversation, reviewing it, and saving it into the wiki. It was selected because it crosses the consequential boundary from transient model output to retained knowledge and exposes distinct computational and human admission decisions. It is a shipped path, not a hypothetical composition of unrelated tools: the chat routes retain answer context, pass conversation messages to drafting, and expose the draft/save dialog (SRC-1, `web/routes/chat.py`, `web/templates/_review_dialog.html`).

This account uses the supplied runtime records as its baseline and adds inspection of the web route bodies, review template, conversation formatting and save service, draft/write helpers, structuring generator and English new-concept prompt, and optional Git helper. These are implementation and doctrine/design evidence within SRC-1 at the frozen revision. No workflow, model call, test or example was executed. Successful delivery, model compliance, verification accuracy and improved future answers remain unobserved.

### 1. Request, retrieval and answer return

The human supplies a question, conversation ID, mode and optional open page. The web POST validates the mode, appends a user message, and allocates a turn ID. Its returned answer bubble opens the SSE handler, which consumes that turn and obtains cached workspace agents. Code owns this dispatch; it does not ask a planning agent to assign independent workers (SRC-1, `web/routes/chat.py`).

The default mode is [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat). Code shapes history and selects context; an optional model condenser returns a rewritten question when the original follow-up lacks coverage. The answer agent receives selected passages and shaped history, not the entire UI conversation or an unrestricted workspace. The code gate and branch-specific post-checks can substitute refusal. Model phrasing and any permitted data-tool calls remain delegated to the answer agent. Strict and streaming modes are real alternatives, with different output enforcement; this account does not transfer strict grounding to streaming ([RT-RTE-strict-chat](runtime.md#rt-rte-strict-chat), [RT-RTE-streaming-chat](runtime.md#rt-rte-streaming-chat)).

On a successful service return the web handler stores an assistant message with answer text, retrieved context, path and token totals. It renders the answer and emits `done`; that is answer delivery, not wiki admission. A caught answer exception removes the pending question, emits an error and ends the stream. Optional answer verification runs after answer storage/display and can mark unsupported sentences; its failure leaves the answer visible (SRC-1, `web/routes/chat.py`). This is annotation, not a universal answer veto, consistent with [RT-CMP-local-nli-verifier](runtime.md#rt-cmp-local-nli-verifier).

### 2. Conversation-to-draft handoff

A separate human action supplies a page title and requests a draft. The service serializes answered question/answer exchanges, excluding refused exchanges and a trailing unanswered question. It raises `EmptyConversation` if nothing remains. It does not simply submit the answer agent's full message/tool transcript. Drafting uses a separate OpenAI call with localized structuring instructions; existing same-slug page content is loaded for a merge, with frontmatter stripped before model input. Code then injects See-also links and returns a `PageDraft`, without writing the page (SRC-1, `base/services/chat.py`, `base/domain/chat/wiki_tools.py`, `base/domain/ingestion/wiki_generator.py`; [RT-RTE-chat-save](runtime.md#rt-rte-chat-save)).

The English new-page prompt requests section structure and claim-linked citation preservation:

> Keep every inline citation from the content above attached to the exact claim it supports — carry them verbatim into the Definition, Key Characteristics, and Context sections. Do NOT strip citations when reshaping into this structure, and do NOT replace them with a generic "Chat synthesis" line. Output only the markdown.
> --- `prompts/chat_concept_new_template.en.md`

That is guidance for a model proposal, not enforcement of preservation or proof that the synthesized claims follow the sources. The generator returns model text after stripping wrapping fences. A model-call failure propagates to the draft route, which presents an error instead of a review dialog (SRC-1, `base/domain/ingestion/wiki_generator.py`, `web/routes/chat.py`).

### 3. Review, optional criticism and veto

The route renders the draft body in an editable textarea and warns when saving will replace an existing page. The human can edit, preview, verify or cancel. Cancel closes the dialog without initiating save. Preview renders current editor text; it does not validate claims. The normal UI thus places a human decision between generated proposal and persistence, unlike the service convenience path and marimo save described by [RT-RTE-chat-save](runtime.md#rt-rte-chat-save) (SRC-1, `web/templates/_review_dialog.html`).

Draft verification uses the Markdown currently submitted from the editor and passages retained on assistant messages from the named conversation. It does not re-retrieve sources or ask the drafting model to certify its own text. Its output marks unsupported sentence spans and reports counts; missing verifier, missing passages and verifier exceptions produce notices. These are bounded support checks against retained passages, not a reference-answer oracle. No pass result or verification token is required for save (SRC-1, `web/routes/chat.py`).

> passages = tuple(p for m in state.conversations.get((wiki_id, conversation_id), [])
>                      if m.role == "assistant" for p in m.context)
> --- `web/routes/chat.py`

The human can withhold submission, but the server's save endpoint does not establish that this human reviewed a particular generated draft. It accepts title and Markdown directly. The review boundary is therefore a caller protocol, not an invariant enforced by draft provenance ([RT-RTE-chat-save](runtime.md#rt-rte-chat-save)).

### 4. Admission, persistence and delivery

Save rejects empty title/body and a busy workspace lock. Otherwise the route delegates to `save_reviewed_page` and releases the lock in `finally`. The service passes submitted Markdown to the writer without another structuring call. Code derives the title slug, creates or replaces a concept page with `sources=["chat"]`, attempts reference synchronization, updates the index and runs scoped post-save repair. The web call supplies no model client, so this repair is deterministic. Submitted text is not guaranteed to remain byte-identical after file metadata generation and repairs (SRC-1, `web/routes/chat.py`, `base/services/chat.py`, `base/domain/chat/wiki_tools.py`; [RT-RTE-chat-save](runtime.md#rt-rte-chat-save)).

The service then requests a `chat: <title>` Git commit. This request is not a delivery prerequisite: Git helpers can be disabled or gracefully skip unavailable Git. The helper's contract states:

> No-op when WIKI_AUTOCOMMIT is disabled; graceful skip when git is unavailable.
>     A git failure here never propagates — it must not fail an ingest.
> --- `base/domain/tools/git_ops.py`

A normal save return causes a created/updated notice, an open-page link when the path is recognized, and refreshed index navigation. The page is retained input for subsequent retrieval and same-slug merges; merely returning a draft or displaying an answer does not create this retained result. Downstream successful retrieval and behavioral activation were not observed ([RT-RTE-chat-save](runtime.md#rt-rte-chat-save); SRC-1, `web/routes/chat.py`).

### Failure and recovery boundary

A rejected empty submission or unavailable lock returns an error before calling the writer. For a caught save exception, the normal success retarget does not occur: the error remains in the dialog and the user's editor content remains available for a human retry. The code does not automatically retry or delegate recovery to another agent (SRC-1, `web/routes/chat.py`, `web/templates/_review_dialog.html`).

> On success return the notice, and the index column again, out of band, so the
>     new page is listed at once; the notice replaces the dialog (`HX-Retarget`). On
>     failure the message stays inside the dialog, which keeps the user's edits.
> --- `web/routes/chat.py`

Retaining editor contents is not a storage rollback. The writer saves the page before reference synchronization, index update and repair. Reference-sync errors are logged and swallowed; post-save repair failures can also leave the primary save successful, as recorded in [RT-RTE-chat-save](runtime.md#rt-rte-chat-save). An exception after a file write can therefore leave partial effects despite an error notice. No all-artifact transaction or compensating rollback appears in the inspected save sequence (SRC-1, `base/domain/chat/wiki_tools.py`). The ingestion compensation mechanism must not be imported into this different route. History restoration is a separate user-initiated maintenance path with prerequisites, not an automatic failed-save recovery step ([RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)).

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

#### On [RT-RTE-chat-save](runtime.md#rt-rte-chat-save)

Workflow role: This is the selected workflow's knowledge-admission boundary. The normal web protocol transfers control from conversation selection and model synthesis to an editable human proposal, then to code-owned persistence. The human can edit or cancel; optional verifier markings inform that decision but do not veto save. Endpoint validation establishes nonempty input and lock availability, not prior review or factual correctness. Completion is a successful writer/service return and rendered notice/index refresh; a Git commit is attempted but optional. On a caught save failure the dialog retains edits for human recovery, without guaranteeing rollback of already-written page/index state. The workflow account above supplies the inspected handoffs and their limits; no additional agent hierarchy, automatic correction loop or successful execution is inferred.
