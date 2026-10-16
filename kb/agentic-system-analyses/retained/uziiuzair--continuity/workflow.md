---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Continuity workflow account: asynchronous deep research from user request through isolated analysis, gap checking, partial recovery and report delivery."
run-id: AAS-2026-10-14-continuity-3e490e1d39f0-01
reviewed-boundary: "4ca8f6b4108aa4494e3861ed33c8019dbd662c67"
---

# Continuity workflow report

## Workflow account

### Selection and evidence boundary

This account selects desktop deep research because it supplies a connected, shipped multi-step path with explicit delegation, a model quality-review step, failure handling and two delivery surfaces. It expands [RT-RTE-deep-research](runtime.md#rt-rte-deep-research), not a new workflow referent. Its enclosing request path is [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat), and its model client is [RT-CMP-ai-client](runtime.md#rt-cmp-ai-client). All findings use SRC-1 implementation at the boundary revision. Additional inspection covers the complete `lib/ai/research-engine.ts`, `types/research.ts` and `lib/ai/research-tools.ts`, plus research dispatch, completion and explicit start/cancel handlers in `providers/chat-provider.tsx`. There is no observed execution or experiment; successful research, citation accuracy and durable delivery remain unobserved.

### Request and launch handoff

The user can ask for research in conversation or use the research button. The button prefixes the question and enters the ordinary chat path; it does not bypass model tool selection. The shipped research prompt asks the foreground model to use `deep_research` for complex or explicit research requests. The tool schema requires a question and permits optional context. The model therefore proposes the research question/context, while desktop code admits launch after obtaining a search provider and AI client. Missing search configuration or AI client returns a tool failure instead. SRC-1, `lib/ai/research-tools.ts`, `providers/chat-provider.tsx`; see [RT-RTE-deep-research](runtime.md#rt-rte-deep-research).

> // Prefix to hint the AI to use deep_research tool
> sendMessage(`[Research] ${question}`);
> --- `providers/chat-provider.tsx`

The desktop executor passes the proposed question, optional context, configured clients, progress/completion/error callbacks and cancellation predicate to `runResearch`. It immediately returns initiation text to the foreground loop rather than awaiting the report. This makes initiation and delivery different events. The captured thread ID identifies the canvas and message destination; subquestion IDs generated inside the engine associate findings/sources with their delegated work. Research is code-orchestrated independent model calls, not agents sharing the foreground message window. SRC-1, `providers/chat-provider.tsx`, `lib/ai/research-engine.ts`; the immediate-return mechanism and isolation are retained in [RT-RTE-deep-research](runtime.md#rt-rte-deep-research).

### Planning and delegated investigation

`runResearch` owns progression. Its planner receives a fresh system/user pair with the main question and optional context, not foreground history or tool schemas. The planner is instructed to produce 3–5 distinct subquestions with search queries. Code parses JSON, rejects an empty plan and truncates initial subquestions to the configured maximum. Defaults are three rounds, five initial subagents, three top sources per agent and a fifteen-read continuation threshold. These are source configuration, not observed usage or timing guarantees. SRC-1, `lib/ai/research-engine.ts`, `types/research.ts`.

> if (!plan.subQuestions?.length) {
>   throw new Error("Failed to generate research plan");
> }
> --- `lib/ai/research-engine.ts`

The orchestrator runs subagents concurrently using `Promise.allSettled`, then collects each result. Each subagent receives its subquestion/search queries, the clients, update/cancellation callbacks and source limit. Code searches its queries, deduplicates returned URLs within that agent, reads the first configured number of sources in accumulated provider order, then constructs an isolated analyst call. Search and URL-reading failures are logged and work continues. The analyst receives only successfully read sources, each truncated to 2,000 characters. Optional planner context is not explicitly included in this analyst message except insofar as the generated subquestion encodes it. These transformations limit what the analyst can verify from the original material. SRC-1, `lib/ai/research-engine.ts`; the two-message analyst passage is retained in [RT-RTE-deep-research](runtime.md#rt-rte-deep-research).

The analyst is asked to extract concrete findings and assign confidence from source quality/specificity. Code admits parsed findings without an independent factual check. When search results supply synthesized answers, it also admits those directly as high-confidence findings, without the analyst verifying them. On analysis failure it falls back to the first 500 characters of each read source as low-confidence findings. Confidence is therefore a model label or code-assigned fallback/provider label, not a measured correctness result. SRC-1, `lib/ai/research-engine.ts`.

> if (perplexityAnswers.length > 0) {
>   for (const answer of perplexityAnswers) {
>     findings.push({
>       content: answer,
>       subQuestionId: subQuestion.id,
>       confidence: "high",
>     });
>   }
> }
> --- `lib/ai/research-engine.ts`

The orchestrator marks a fulfilled subagent `answered`, stores its findings and sources, and merges findings into the accumulated collection. A rejected promise becomes an error status for that subquestion rather than aborting its peers. `answered` follows promise fulfillment, not a minimum-evidence or semantic acceptance test. Search counters add the number of planned queries for fulfilled subagents, so the displayed search count does not certify successful searches. SRC-1, `lib/ai/research-engine.ts`.

> if (result.status === "fulfilled") {
>   sq.status = "answered";
> --- `lib/ai/research-engine.ts`

### Verification and follow-up ownership

Between rounds, the engine first checks its code limits and cancellation state. If eligible to continue, a separate reviewer model receives the original question, the first 200 characters of each accumulated finding, and investigated subquestions/statuses. It does not receive the full source texts, finding confidence or per-finding source URLs in that message. The prompt requests adequacy assessment and follow-up questions, avoiding duplicates. The reviewer proposes continuation; code stops when `shouldContinue` is false or follow-ups are missing, otherwise admits at most three follow-up subquestions and runs another round. There is no reference-answer oracle or human per-round veto. This is an adequacy-driven continuation decision, not certification of every finding or final report. SRC-1, `lib/ai/research-engine.ts`.

> if (
>   !gapResult.shouldContinue ||
>   !gapResult.followUpQuestions?.length
> ) {
>   break;
> }
> --- `lib/ai/research-engine.ts`

A malformed or failed gap check also proceeds to synthesis with existing material. Reaching the configured read threshold prevents another round only after current parallel work completes; it does not reserve a remaining budget before each URL read. Thus fifteen is a continuation threshold, not a strict total-read cap. The initial-agent cap applies to the plan; follow-ups use a separate fixed cap of three. SRC-1, `lib/ai/research-engine.ts`, `types/research.ts`.

> } catch {
>   // Gap check failed — proceed to synthesis with what we have
>   break;
> }
> --- `lib/ai/research-engine.ts`

### Synthesis, admission and delivery

The synthesizer receives the question, all subquestion texts, findings truncated to 300 characters each, and a numbered title/URL list selected from sources that were read or have snippets. The findings list omits the finding objects' source URLs, confidence and subquestion IDs. A cited-looking output cannot therefore be assumed to preserve those original associations. The model is instructed to produce a standalone summary and factual, balanced markdown report with citations. Code parses JSON and substitutes placeholder text for missing summary/report fields. It does not run a post-synthesis factual/citation validator or ask for human approval before invoking completion. SRC-1, `lib/ai/research-engine.ts`.

> const findingsList = allFindings
>   .map((f) => `- ${f.content.slice(0, 300)}`)
>   .join("\n");
> --- `lib/ai/research-engine.ts`

The desktop completion callback converts report markdown into canvas blocks, appends them to the captured thread, refreshes content and opens the canvas. In Tauri mode it also displays and initiates persistence of an assistant summary, preserving a visible thinking block when replacing the last assistant message. Later thread history receives the saved summary, not a replay of analyst windows. Full report and summary are separate writes, not an atomic delivered unit. A canvas-write exception is logged, yet the summary still says the full report was written to canvas. Summary persistence uses a promise started inside a UI state update rather than an awaited completion barrier. SRC-1, `providers/chat-provider.tsx`; persistence/read-back baseline: [RT-RTE-deep-research](runtime.md#rt-rte-deep-research).

> } catch (err) {
>   console.error("Failed to write research report to canvas:", err);
> }
> --- `providers/chat-provider.tsx`

The engine emits `complete` and calls a callback whose type returns `void`; the actual desktop callback is async, and the engine does not await it. Engine completion therefore means an assembled result handed to the callback, not confirmed durable canvas/message delivery. The UI's later inactive/result state likewise does not independently verify all writes. Successful delivery would require the relevant asynchronous writes to succeed; source wiring alone does not show that they did. SRC-1, `lib/ai/research-engine.ts`, `types/research.ts`, `providers/chat-provider.tsx`.

> emit({ phase: "complete", phaseDetail: "Done" });
> callbacks.onComplete(result);
> return result;
> --- `lib/ai/research-engine.ts`

### Cancellation and failure recovery

Cancellation sets a shared predicate; workers check it between operations, not through an abort signal to in-flight model/network requests. At an engine cancellation checkpoint, `CancelledError` produces a partial report and calls the same completion callback, so cancellation can still write a partial report/summary after the cancel UI resets. Non-cancellation top-level failures emit an error, call `onError` and rethrow. The desktop launch is fire-and-forget: its error callback updates UI state, but that launch expression supplies no promise rejection handler. No automatic retry or compensating rollback is established in these inspected paths. SRC-1, `lib/ai/research-engine.ts`, `providers/chat-provider.tsx`.

> callbacks.onComplete(result);
> return result;
> }
> 
> emit({ phase: "error", phaseDetail: error instanceof Error ? error.message : "Unknown error" });
> callbacks.onError(error instanceof Error ? error : new Error(String(error)));
> throw error;
> --- `lib/ai/research-engine.ts`

This path recovers selectively: search/read errors permit remaining work, analyst errors admit raw excerpts, rejected subagents retain peer output, gap errors accept current coverage, and cancellation admits partial output. These mechanisms favor producing an artifact over rejecting uncertain evidence. They establish neither reliable completeness nor successful publication. The retained result is an external research work product; no method revision, learning benefit or self-improvement is inferred from the gap-check rounds.

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

#### On [RT-RTE-deep-research](runtime.md#rt-rte-deep-research)

Workflow-specific acceptance: the gap reviewer can stop further investigation or propose additional work; it does not veto final delivery on factual/citation grounds. Final output admission is automatic after parsing, with missing-field placeholders and a cancellation partial-result alternative.

Workflow-specific delivery boundary: engine result handoff, canvas append, summary display and summary persistence are distinct milestones. The engine does not await the desktop completion callback. The canvas failure path can continue into a summary claiming canvas delivery, so completion/status text is not a delivery receipt.

Workflow-specific recovery boundary: cooperation can stop future operations but not abort an awaited request. Local fallbacks preserve partial work; no inspected recovery path compensates already completed writes or establishes an automatic retry.
