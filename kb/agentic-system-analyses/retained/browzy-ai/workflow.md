---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "browzy.ai workflow: terminal question answering followed by conditional insight drafting, including fallback and rejection paths."
run-id: AAS-2026-10-15-browzy-ai-0a823a13a7b6-01
reviewed-boundary: "56c253042041ee2f483a5e9b824174d746891cf4"
---

# browzy.ai workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a terminal question against an existing wiki, followed by conditional extraction of an insight draft. It was selected because one shipped handler connects retrieval, answer generation, user delivery, a second model judgment and local persistence. This is a host-coordinated sequence of inference calls, not a team of independently acting agents. The application owns each transition; neither model call selects tools or assigns workers. The two existing route identities are [RT-RTE-answer-question](runtime.md#rt-rte-answer-question) and [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft). No duplicate workflow route is declared.

The account concerns implementation at SRC-1's frozen commit, with model instructions as doctrine/design. No execution trace, real knowledge directory or successful provider call was supplied. It establishes wired progression and gates, not successful synthesis, correct novelty judgment or reliable delivery. The inspected source paths are `src/cli/app.tsx`, `src/core/query/engine.ts`, `src/core/query/historyManager.ts`, `src/core/query/crystallizer.ts`, `src/core/prompts.ts` and, additionally, the complete `src/core/retrieval/compactor.ts`. The latter adds coverage beyond the runtime's end-to-end account. Retrieval internals are cited through the supplied runtime route rather than independently re-audited here.

### Request and first handoff: assemble an answer task

The user supplies the question. `handleQuery` first requires a configured provider; without one, the application requests setup instead of beginning inference. Once available, it records the user turn, sets loading state and creates a fresh QueryEngine. `prepare` loads the schema, calculates an article budget, retrieves context and returns a prompt, system instructions, selected article slugs, confidence and gaps. Its role is preparation, not model execution (SRC-1, `src/cli/app.tsx`, `src/core/query/engine.ts`; [RT-RTE-answer-question](runtime.md#rt-rte-answer-question)).

The application separately calls `buildLLMHistory` and supplies the resulting user/assistant turns before the prepared question/context message. Host rules filter out system notices, select the last ten eligible messages and shorten long turns. The two newest turns receive a larger character cap; older turns are dropped when the running character target has been exceeded and at least two have been retained. These are input-reduction rules, not a model-authored summary or a hard token-window guarantee. Full host session messages remain distinct from the reduced input; the provider receives no tool for reloading omitted turns (SRC-1, `src/core/query/historyManager.ts`; [RT-RTE-answer-question](runtime.md#rt-rte-answer-question)).

The preparation call omits history and the configured model ID, so its budget calculation does not cover the complete actual terminal request. The selected source list identifies delivered context, not evidence that every article supported the answer. The source-count gate later reuses that distinction: two selected slugs do not prove cross-article synthesis (SRC-1, `src/cli/app.tsx`, `src/core/query/engine.ts`).

### Generation, failure recovery and answer delivery

The first inference call streams an answer with query instructions, the conversation-context instruction, selected history and the prepared prompt. Snapshots update the terminal through a throttled UI path. There is no independent acceptance test between generated answer text and the final assistant message. Confidence and gap metadata come from preparation, not a post-answer factual evaluator. The prompt's grounding policy remains a request, not an answer oracle ([RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding); SRC-1, `src/cli/app.tsx`, `src/core/query/engine.ts`).

If streaming throws, the host starts a non-streaming request. It preserves the selected messages but uses only the prepared system prompt, omitting the appended conversation-context instruction. It does not resume a partially generated answer:

> const response = await currentLlm.chat(
>           [...recentHistory, { role: 'user', content: prepared.prompt }],
>           { system: prepared.systemPrompt, maxTokens: 8192 }
>         );
> --- `src/cli/app.tsx`

On success, the application clears the stream display and adds the final answer with selected slugs to the session. This is the answer's implementation-level delivery point; downstream drafting is not required for it:

> setStreamingText('');
>       session.addMessage('assistant', finalText, fullResult.sourcesUsed);
> --- `src/cli/app.tsx`

If preparation or the fallback fails, the outer catch adds a classified system error. A classification requesting a new key clears the provider state. The handler then clears loading and refreshes statistics. This is host-owned error handling, not proof that a replacement call or credential setup succeeds (SRC-1, `src/cli/app.tsx`).

### Second handoff: answer to conditional draft proposal

After answer delivery, the host considers crystallization only if the session gate is clear and at least two source slugs were selected. It sets the ref synchronously, reloads the first five selected articles, and requires at least two loadable contents. The second call is asynchronous and not awaited by the main answer path. The host passes question, answer, all selected slugs, the reloaded subset, data directory and the same provider object (SRC-1, `src/cli/app.tsx`; [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft)).

The crystallizer sends only the first 3,000 answer characters and at most five article bodies, each capped at 2,000 characters. It does not receive the answering conversation or the entire wiki. This is a separate inference context with a bounded input handoff, not a delegated tool-using worker. Its returned saved flag and optional slug/title cross back to the application; its generated body instead goes to disk. The analogy to an isolated task frame is limited: the output persists outside the call and can outlive the session, but no autonomous worker state or pointer-based reload mechanism is exposed (SRC-1, `src/core/query/crystallizer.ts`).

The second model both judges novelty and authors a candidate. Its guidance distinguishes a connection or derived conclusion from mere restatement and instructs rejection when uncertain:

> 3. If ALL insights already exist in individual source articles, output: NONE
> 4. If you find a genuinely novel connection, extract ONLY that insight as a wiki article
> --- `src/core/prompts.ts`

That is an internal model judgment, not an independent reference outcome. Truncation limits what it can compare. No human approves each proposed draft, and user initiation of the question is not per-draft approval (SRC-1, `src/core/query/crystallizer.ts`, `src/core/prompts.ts`; [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft)).

### Rejection, draft delivery and recovery

Software can reject the model's output as `NONE`, missing article markers, missing slug/title/summary, or missing/short body. The minimum-content gate is structural, not a verification of truth or novelty:

> if (!content || content.length < 50) return { saved: false }; // Too short = not valuable
> --- `src/core/query/crystallizer.ts`

Accepted text becomes a Markdown draft with derived tags, selected source slugs, creation time and a question prefix. The writer uses `drafts`, not wiki admission or FTS indexing. A successful write returns the saved flag and the application reports “insight drafted”; this is a separate delivery endpoint from the answer. This writer supplies no transactional rollback, version history or human review gate. A same-slug write uses the ordinary overwrite behavior of `writeFileSync` (SRC-1, `src/core/query/crystallizer.ts`).

> writeFileSync(join(draftsDir, `${slug}.md`), frontmatter, 'utf-8');
>
>   return { saved: true, slug, title };
> --- `src/core/query/crystallizer.ts`

A rejected result or a loading/write exception clears the ref so another eligible question may try again. This is re-eligibility, not an immediate automatic regeneration loop. A saved result marks the session as crystallized and suppresses additional successful drafts in that session. The already-delivered answer is not withdrawn on draft failure (SRC-1, `src/cli/app.tsx`). The runtime's scoped search found no automatic draft-to-query consumer; subsequent promotion, retrieval and benefit remain unestablished rather than inferred from a persistent file ([RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft)).

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

#### On [RT-RTE-answer-question](runtime.md#rt-rte-answer-question)

Workflow completion is the assistant-session insertion, not downstream draft creation or a correctness verdict. A later optional compaction call must not be confused with the effective history reduction above. After more than twenty session messages, the handler awaits `compactConversation` with six recent messages to keep, but discards its returned object. The helper returns a summary plus kept messages; it does not install them in session state. The next answer still calls `buildLLMHistory(session.messages)`. Thus this inspected terminal path requests a summary without wiring that returned summary into later query context, despite its comment claiming future internal use (SRC-1, `src/cli/app.tsx`, `src/core/retrieval/compactor.ts`).

> await compactConversation(
>             session.messages.map(m => ({ role: m.role, content: m.content })),
>             currentLlm,
>             6,
>           );
> --- `src/cli/app.tsx`

The helper separates the older prefix, truncates each summarized message to 3,000 characters, and preserves the recent tail in its return value. It retries failed summary calls up to three times and returns the original messages if all fail. Neither that returned fallback nor a successful summary changes this caller's history, because neither is consumed. No retained-summary read-back or improved continuity is established by this call (SRC-1, `src/core/retrieval/compactor.ts`, `src/cli/app.tsx`).

#### On [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft)

The consequential workflow handoff is post-delivery and fire-and-forget: answer success permits draft consideration, while draft failure does not reject the answer. Host eligibility, the model's novelty decision and parser acceptance are distinct gates. Only the first and third are executable predicates; the novelty verdict depends on model interpretation of a truncated comparison set. Recovery resets eligibility for a future question rather than repairing the rejected proposal. The workflow establishes neither draft promotion nor an exercised improvement loop (SRC-1, `src/cli/app.tsx`, `src/core/query/crystallizer.ts`, `src/core/prompts.ts`).
