---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "PageIndex workflow account: local own-model document QA from a retained PDF through guided retrieval, bounded failures and answer delivery."
run-id: AAS-2026-10-15-pageindex-50056ef72767-01
reviewed-boundary: af92d9658a6a9c0ae31171b43198db28951af2f4
---

# PageIndex workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a caller asking a non-streaming question about an already submitted local PDF through `chat(question, doc_id=...)`, using its default Chat Completions protocol and a configured answering model. It is selected because it connects retained document state to a shipped answering driver, rather than stopping at a returned tree. Submission is the prerequisite described by [RT-RTE-local-submit](runtime.md#rt-rte-local-submit); the workflow itself follows [RT-RTE-document-chat](runtime.md#rt-rte-document-chat). It is one model-led retrieval loop, not a team of independently delegated agents. The external Agents SDK coordinates repeated model/tool turns. SRC-1: `pageindex/client.py`, `pageindex/local_chat.py`.

The account uses static implementation evidence at the [boundary](boundary.md). No target code, notebook, test or provider call was executed. Inspection for this member covers the chat message splitter, agent prologue/construction, non-streaming runner/envelope, facade return and turn-limit guidance; local structure/page tool implementations and dispatch; local reading/discovery instructions; and the OpenAI adapter's in-process tool handoff. These are implementation and instruction evidence from SRC-1: `pageindex/local_chat.py`, `pageindex/client.py`, `pageindex/agent_tools.py`, `pageindex/integrations/openai_agents.py`. They do not establish successful retrieval, model compliance or answer accuracy. Cloud server behavior and other protocol drivers are not inferred from this selected local path.

### Request and delegation

The caller supplies the question, target document, optional history and model/run settings. The wrapper splits system/developer text from user/assistant history. It rejects unsupported message roles on this lane rather than accepting tool transcripts. It constructs managed instructions, prepends a document-targeting block to the history, and passes a separately computed local document scope into agent construction. The model therefore receives question/history and target context; the tool dispatcher receives the scope that controls document lookup. Targeting prose and lookup authority are different handoffs. This is the scoped case already established in [RT-RTE-document-chat](runtime.md#rt-rte-document-chat), not a universal document authorization claim. SRC-1: `pageindex/local_chat.py`, `pageindex/agent_tools.py`.

> items = ([{"role": "user", "content": block}] if block else []) + history
> --- `pageindex/local_chat.py`

The configured agent receives model settings, composed instructions and PageIndex tools. The in-process adapter supplies tool schemas and callbacks to the SDK; tool callbacks run through the adapter and return structured MCP results. The answering model chooses the semantic next step, while code resolves and executes a chosen read. This is delegation of evidence access to functions, not delegation of a separately instructed research task. No shell tool is granted by this construction. Default read-only registration and broader caller-owned integration limits are covered by [RT-RTE-framework-tools](runtime.md#rt-rte-framework-tools). SRC-1: `pageindex/local_chat.py`, `pageindex/integrations/openai_agents.py`.

> blocks, is_error = await asyncio.to_thread(
>     self._invoke[tool_name], arguments or {})
> return mcp_types.CallToolResult.model_validate(
>     {"content": blocks, "isError": is_error})
> --- `pageindex/integrations/openai_agents.py`

### Retrieval and consequential decisions

The shipped instructions ask for discovery, comparison of document names/descriptions against intent, and clarification when several documents are equally relevant. They request structure-first reading for documents over twenty pages and direct page access for smaller documents. The loop is not a deterministic browse → structure → pages state machine: these are model-interpreted instructions, and the model can choose tools or answer. Delivery of this guidance is established by [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions) and [RT-BAP-managed-guidance](runtime.md#rt-bap-managed-guidance); compliance is unobserved. SRC-1: `pageindex/agent_tools.py`, `pageindex/local_chat.py`.

A structure request resolves the document under the supplied scope, requires completed processing, and asks the tree getter for summaries without full text. Formatting and pagination intervene before delivery. A returned outline is therefore a navigation aid, not the whole stored document. Page reading is another model-selected call, with explicit page ranges. It loads stored page data and assembles only selected entries. These transformations bound what evidence reaches the answering model; merely having indexed a PDF does not put all of it in the answer context. SRC-1: `pageindex/agent_tools.py`; see [RT-RTE-document-chat](runtime.md#rt-rte-document-chat).

> tree = client.get_tree(entry["id"], node_summary=True,
>                        include_text=False).get("result")
> --- `pageindex/agent_tools.py`

Page response budgeting can omit requested pages. The success envelope distinguishes requested from returned ranges and supplies instructions for requesting remaining pages. At least the first valid requested page is admitted even if it exceeds the nominal budget, as already quoted in the runtime account. Neither success nor a requested range establishes that every requested page reached the model. The caller's history and subsequent tool outputs accumulate within the runner; this driver does not demonstrate automatic history compaction. Omitted source pages remain accessible through another tool request. SRC-1: `pageindex/agent_tools.py`, `pageindex/local_chat.py`; [RT-RTE-document-chat](runtime.md#rt-rte-document-chat).

### Verification, rejection and recovery

Code checks tool inputs and document readiness, not the correctness of the final answer. A concrete rejection occurs when every requested page exceeds the document's maximum page index: the tool returns an `INVALID_INPUT` failure with valid bounds and a suggestion to check the document page count. Mixed valid/out-of-range requests can instead produce a partial success, so recovery must attend to the returned ranges and options. SRC-1: `pageindex/agent_tools.py`.

> "summary": "All requested pages are out of range for this document",
> "options": [
>     f"Request pages between 1 and {max_page}",
>     "Use get_document() to check document page count",
> ],
> --- `pageindex/agent_tools.py`

The loop can receive this failure through the adapter's error flag and payload. Local dispatch also strips model-supplied private keys before injecting its own scope; a model cannot widen that scope by supplying `_allowed_ids`. Signature failures and unexpected local tool exceptions become guided error envelopes. The prompt tells the model to present error options instead of retrying blindly; it does not prove that the model will retry correctly or present them. Recovery ownership is split: code reports a bounded failure, the model interprets next steps within the remaining run, and the caller can correct inputs or retry a failed invocation. SRC-1: `pageindex/agent_tools.py`, `pageindex/integrations/openai_agents.py`.

> kwargs = {key: value for key, value in (arguments or {}).items()
>           if not key.startswith("_") and value is not None}
> --- `pageindex/agent_tools.py`

The wrapper validates positive turn limits before starting. If the SDK raises a turn-limit exception, the wrapper translates it to caller-facing guidance rather than delivering a successful answer. It does not automatically start a second run with a higher cap. The runner's coroutine is wrapped in backend cleanup even on failure. These are inspected error paths, not observed recoveries. SRC-1: `pageindex/local_chat.py`.

> f"The agent did not finish within max_turns ({limit}). Raise "
> "max_turns, or narrow the question."
> --- `pageindex/local_chat.py`

### Delivery and remaining limits

The SDK's final output becomes the assistant content of a completion envelope, with finish reason and summed usage. The high-level facade extracts that content and returns answer text, or an empty string when content is empty. Delivery here means returning that value to the caller, not independent acceptance of an answer. The inspected success branch does not compare it with an expected answer or require a separate reviewer. Page content supplies evidence, not an answer oracle. Optional grounding/citation guidance likewise does not constitute a correctness gate. SRC-1: `pageindex/local_chat.py`, `pageindex/client.py`; [RT-RTE-document-chat](runtime.md#rt-rte-document-chat).

> return envelope["choices"][0]["message"]["content"] or ""
> --- `pageindex/client.py`

Stored document data can be reloaded on later questions. This Chat Completions workflow does not itself persist a chat session or return appendable tool turns; later conversation history is caller-owned. The separate [RT-RTE-protocol-history](runtime.md#rt-rte-protocol-history) describes alternatives that do expose tool transcripts, not an implicit feature of this lane. No execution evidence establishes which pages a real run selected, whether any failure was repaired, or whether the final answer depended faithfully on the supplied evidence. SRC-1: `pageindex/local_chat.py`, `pageindex/client.py`.

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

#### On [RT-RTE-document-chat](runtime.md#rt-rte-document-chat)

Workflow selection: the local, non-streaming Chat Completions lane above is the representative case. The handoff to the SDK delegates progression, not a second agent's independent assignment. Verification distinguishes structural tool acceptance, partial evidence delivery and final-answer correctness; only the first two have inspected code checks in this selected path. Error options permit model/caller recovery without guaranteeing it. Completion is the facade's returned answer value, not a reviewed or persisted conversation product. The source quotations and bounds in the Workflow account support these workflow-specific distinctions.
