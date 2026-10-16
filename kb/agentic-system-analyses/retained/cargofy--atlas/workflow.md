---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "ATLAS workflow account: browser question, model-directed data and knowledge tools, bounded continuation and displayed reply."
run-id: AAS-2026-10-12-atlas-b28ea1ea613f-01
reviewed-boundary: "65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988"
---

# ATLAS workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the shipped browser chat: a user question reaches a model, model-selected tools query operational records or read/write knowledge, results return to the model, and a reply reaches the browser. It was selected because it exposes an internal agent's next-step decisions and delivery in one connected implementation, rather than depending on an excluded MCP host's workflow. It is the existing [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools), not a new route. Reading or saving knowledge is an available branch, not an inevitable stage of every question.

Evidence is SRC-1 implementation at the frozen revision. This member inspected all of `src/ai/chat.js`, `src/ui/pages/chat.js` and `src/ui/lib/api.js`, plus the chat endpoint in `src/ui-server.js`. The API client adds inspection beyond the runtime's named coverage. No target execution, provider response, test result or deployment trace was supplied or produced. The account establishes wiring and source-defined limits, not successful execution, correct answers or benefit.

### Request and delegation

1. **User to browser.** The user enters text and can select a registered model. The browser adds the question to its module-singleton messages array and disables its input while awaiting the request. It sends accumulated user/assistant text, not the previous tool-result blocks. The selected model ID accompanies that history (SRC-1, `src/ui/pages/chat.js`):

   > const apiMsgs = messages
   >       .filter(m => m.role === 'user' || m.role === 'assistant')
   >       .map(m => ({ role: m.role, content: m.content }));
   > --- `src/ui/pages/chat.js`

   This omission matters: a later question can receive an earlier answer without the underlying query evidence. Durable saved knowledge has a separate read-back path; the browser's text history does not reconstruct prior tool state. See [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge).

2. **Browser to server.** POST `/api/chat` carries messages and model. The endpoint rejects a missing, empty or non-array messages value with HTTP 400; otherwise it calls `handleChat` with the shared Atlas instance and current registry. The handler selects an explicit model if supplied, otherwise the chat role, then falls back to the default role. Model services and mutability are already recorded in [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client). User initiation and model choice do not constitute human approval of individual tool calls or knowledge content. The endpoint does not add a per-user tool grant; the bounded authorization finding is [RT-ABS-rest-auth](runtime.md#rt-abs-rest-auth) (SRC-1, `src/ui-server.js`, `src/ai/chat.js`).

3. **Server to model.** The handler builds a fresh system prompt from record counts, current knowledge filenames and response guidelines, then supplies that prompt, submitted messages and tool schemas. Knowledge contents are not bulk-loaded at this handoff; the model must request reads. The prompt asks for grounded answers and comparisons through repeated tool calls, but does not prescribe a deterministic plan. [RT-BAP-chat-guidance](runtime.md#rt-bap-chat-guidance) retains the grounding instruction. The provider decides which named tools and arguments to propose, or whether to answer immediately. There is one selected model client per invocation, not a coordinator delegating to separate specialist agents (SRC-1, `src/ai/chat.js`).

### Tool execution and continuation

The JavaScript handler owns dispatch; the model owns the proposed next step. The fixed switch maps each recognized name to an Atlas operation. Data queries return records; `read_knowledge` returns requested file text; `save_knowledge` directly writes supplied content. These latter effects and their persistence are retained in [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools) and [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge). The chat write does not pass through KnowledgeEngine's comparison/enrichment procedure or acquire its attribution policy. The separate engine route is [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment), and its add-only policy must not be attributed to this chat workflow (SRC-1, `src/ai/chat.js`).

Calls returned within a round execute sequentially. The handler serializes each result, records name/arguments/result in the tool log, and adds provider-specific continuation messages: Claude receives assistant tool-use blocks followed by user tool-result blocks; the OpenAI branch receives assistant function calls followed by tool-role messages. The next model call therefore receives execution results from this invocation, not merely the requested tool names. This feedback permits another query or a revised answer, but establishes neither actual correction nor factual verification (SRC-1, `src/ai/chat.js`).

The handler caps tool-enabled model rounds at five. Each round can request several calls, so the bound limits rounds rather than database accesses or knowledge writes. If the model returns no tool calls, the handler returns its text immediately; otherwise it executes the calls and continues. Exhaustion triggers a final model call with an empty tool list, whose text is returned. The runtime retains the final-call passage in [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools). None of these terminal conditions requires that a query was made, a knowledge read occurred, or the answer was independently checked (SRC-1, `src/ai/chat.js`).

### Verification, rejection and recovery

Verification here is mechanical acceptance of requests and effects, not an answer-quality review. The endpoint checks the messages envelope. The executor recognizes tool names and relies on Atlas operations for effects/errors; it does not contain a separate per-call JSON Schema validation pass. Its unknown-name rejection is explicit (SRC-1, `src/ai/chat.js`):

> default:
>       return { error: `Unknown tool: ${name}` };
> --- `src/ai/chat.js`

An executor exception is converted into an error result and delivered back to the same model. Both provider branches use this pattern. The Claude branch provides the following witness (SRC-1, `src/ai/chat.js`):

> try {
>           result = executeTool(tc.name, tc.input, atlas);
>         } catch (e) {
>           result = { error: e.message };
>         }
> --- `src/ai/chat.js:325-329`

The model, not a separate recovery supervisor, chooses what to do with that error on a later round. A fixed recovery action or successful retry is not established. The batch continues after an individual tool error. A successful earlier save is not rolled back merely because another tool or later provider call fails; the direct file writer has no version/rollback store in the supplied [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge).

Errors escaping `handleChat` reach the endpoint catch and produce HTTP 500 with `ok: false`. The browser API helper throws on a non-success HTTP status rather than returning that body as an ordinary chat result (SRC-1, `src/ui/lib/api.js`):

> const data = await res.json();
>   if (!res.ok) throw new ApiError(res.status, data);
>   return data;
> --- `src/ui/lib/api.js`

Consequently the shipped page's catch appends a `Connection error` message for this path and reenables the controls in `finally`; it does not automatically resubmit. The wording covers server rejection as well as transport failure. Recovery from that terminal failure belongs to a subsequent user action, with any prior successful knowledge effect still present (SRC-1, `src/ui/pages/chat.js`, `src/ui-server.js`).

There is no independent expected-answer oracle or acceptance gate before final text. Operational records and requested files are evidence delivered to the model, not a verified reference answer. Prompt compliance and error interpretation are unobserved. The configured-model fallback can also return `No AI model configured.` as ordinary reply text: the HTTP wrapper's `ok: true` marks handler return, not achievement of the user's task (SRC-1, `src/ai/chat.js`, `src/ui-server.js`).

### What counts as delivered

At the server boundary, delivery is a JSON response containing reply, tool log and accumulated reported usage (SRC-1, `src/ui-server.js`):

> json({ ok: true, reply: result.reply, tool_calls: result.tool_calls, usage: result.usage });
> --- `src/ui-server.js`

At the shipped browser boundary, the returned text is appended as an assistant message and rendered as Markdown. Tool badges expose arguments and a result preview; the page truncates each visible result preview after 500 characters. This is display truncation, not truncation of the result earlier fed to the model. The full tool log reaches the page in the API response, while later chat requests resend only conversational text. The page shows token counts, not a verification verdict (SRC-1, `src/ui/pages/chat.js`).

A knowledge save is a separate delivered filesystem effect, not proof that the answer was delivered or accepted. Later invocations can see its filename in the rebuilt prompt and request its contents through the same tools. This persistence-to-consumption connection is wired; actual later selection, behavior change and useful answers remain unobserved. Browser rendering, user receipt and deployment storage survival are likewise not established by source text alone.

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

#### On [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools)

Workflow delegation: user supplies the question/history/model preference; server supplies current prompt and tool schemas; model proposes calls; fixed dispatch executes; serialized results return to the same model. There is no required specialist handoff or independent reviewer in the inspected handler.

Workflow verification: message-envelope rejection and unknown-tool/error handling are mechanical checks. Final answer acceptance is simply a no-tool response or completion of the final tool-free call, not an oracle comparison. Human initiation is not per-write approval.

Workflow recovery: individual execution errors enter model continuation; endpoint-level failure ends the invocation and the browser reenables its controls. The API helper's HTTP rejection reaches the page's catch, producing `Connection error` text. No automatic request resubmission occurs in that inspected path.

Workflow delivery: API JSON supplies text/log/usage; the browser renders reply text and shortened result previews. Subsequent browser requests omit earlier tool-result blocks. Persisted knowledge is independently eligible for later index/read delivery. These are SRC-1 implementation findings at `src/ai/chat.js`, `src/ui-server.js`, `src/ui/pages/chat.js` and `src/ui/lib/api.js`, not observed successful operation.
