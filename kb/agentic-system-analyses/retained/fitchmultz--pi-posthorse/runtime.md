---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Pi Posthorse runtime baseline: foreground reset admission, automatic recovery, request guidance and bounded retained-state retrieval at the frozen extension boundary."
run-id: AAS-2026-10-14-pi-posthorse-58b9647d2f29-01
reviewed-boundary: "307ef6bf05bc8bd8d718725761ffdf2f2ef72539"
---

# Pi Posthorse runtime report

## Runtime account

### Work and entry paths

Posthorse continues Pi tasks across fresh context windows. It replaces eligible automatic model-generated summaries with bounded input/recovery records, offers a foreground-agent reset tool, and makes notes and earlier journal entries recoverable. It is an extension, not the scheduler, model client or physical request boundary. The [boundary](boundary.md) fixes this distinction. The claimed work is recorded in [RT-CLM-context-continuation](#rt-clm-context-continuation).

The shipped package loads `index.ts`; its default export invokes `createPosthorse()`. SDK consumers can instead inject a live compaction policy reader. Each installation creates shared page reservations, registers presentation, rollover hooks, notes and history. The default reader uses Pi's effective settings and current model. Active tool declarations contribute a serialized character-based overhead estimate, not a tokenizer-exact provider measurement (SRC-1, `package.json`, `index.ts`, `src/budget.ts`).

> /** Use Pi's live effective settings by default; SDK hosts can inject a policy reader. */
> --- `index.ts`

Pi supplies the user problem, foreground model decisions, tool scheduling, turn events, current projection and append-only journal. Posthorse supplies symbolic hook rules and natural-language guidance. The current model component is [RT-CMP-active-model](#rt-cmp-active-model); its weights, exact version and deployment grants are not frozen here. Installation does not establish that every tool is currently active. The host can select tools, register other extensions, route models or override prompts (SRC-1, `index.ts`, `src/rollover.ts`, `test/official.test.mjs`).

### An ordinary invocation end to end

1. Pi starts a session/run and calls Posthorse's hooks. Session/turn start clears callback requests and page reservations; session/tree changes invalidate reminder lookup. Before each model request, Posthorse builds current capacity/policy guidance and inserts it into a named system section, or a request-local custom message for a forced full prompt. These instructions are model-interpreted, not an enforced work plan ([RT-RTE-request-guidance](#rt-rte-request-guidance); SRC-1, `src/rollover.ts`, `src/budget.ts`).
2. The foreground model performs host-owned work. Near the enabled, supported rollover line, an eligible working turn can receive one steer reminder per window/configuration fingerprint. The requested policy is to save concise current-state notes, preserve decisions and safety constraints, and then request a fresh context. A final-answer turn does not receive this wakeup. Large turns can skip the reminder band altogether (SRC-1, `src/rollover.ts`, `src/reminders.ts`).
3. The model writes or edits a note. Posthorse's `notes write/append` executes ordinary local filesystem mutation; its guidance also expressly permits host editors at the returned absolute note path. The note write result reports publication, not correctness of its content ([RT-RTE-note-admission](#rt-rte-note-admission); SRC-1, `src/notes.ts`, `src/files.ts`, `src/budget.ts`).
4. The model calls `new_context` with readable continuation prose. The callback checks the current fresh-window capacity and records its own call ID and handoff in a turn-local map. Its returned card says **requested**, not committed. At turn end, Posthorse requires a matching callback ID in the foreground results, no sibling error, no already-visible assistant error/abort, no aborted event/signal, and sufficient capacity after pending input. It then returns a retain-none compaction draft and `continue: true`. Pi owns committing the draft and scheduling the next model call ([RT-RTE-explicit-reset](#rt-rte-explicit-reset); SRC-1, `src/context-tools.ts`, `src/rollover.ts`).
5. The fresh model receives the handoff as host-projected compaction summary and regenerated guidance. Earlier conversation is removed from active input but remains reachable through Pi's journal and Posthorse history. The model can restore note pages and query/read entry IDs. Retrieval uses one shared per-turn estimated budget for notes/history, including sibling reservations and images ([RT-RTE-retained-retrieval](#rt-rte-retained-retrieval); SRC-1, `src/history.ts`, `src/paging.ts`, `src/history-pages.ts`).
6. The host continues until its agent stops or a user intervenes. Terminal artifacts are tool results, notes, host journal entries and the model's answer. Posthorse has no independent task-success oracle. Guidance asks the model to verify live state before consequential work; neither a handoff nor a note proves task progress (SRC-1, `src/budget.ts`, `src/recovery.ts`).

This is an implementation trace, not a supplied run trace. No target tests, examples or providers were executed. Operation, activation and benefit remain unobserved. Evaluator source supports intended assertions only.

### Material alternatives and forcing cases

**Case 1 — explicit request with failed or foreign work.** A failed sibling prevents the explicit draft; a foreign tool with the same name cannot authorize it without an ID already recorded by Posthorse's own callback. A successful earlier write is not rolled back merely because another sibling fails. Background jobs are outside this batch and continue across reset. Later turn-end handlers are an important counterexample to an unconditional abort guarantee: Posthorse checks the signal when its handler runs, not after all handlers. A shipped test expects an official-host draft to commit after a later handler aborts. This is source-native evaluator intent, not observed host behavior (SRC-1, `src/rollover.ts`, `src/context-tools.ts`, `test/official.test.mjs`).

> "official Pi commits drafts after a later turn_end abort",
> --- `test/official.test.mjs`

**Case 2 — automatic threshold/overflow versus manual or unsupported budgets.** Pi's successful compaction preparation triggers `session_before_compact`. For a supported budget, Posthorse builds recovery from branch entries plus the live session projection, appends an invisible sentinel, and returns a custom compaction. It makes no summary-model call on this handler path. Cancellation or construction failure returns `cancel: true`; errors notify the UI or stderr. Manual compaction returns without intervention, and an unsupported budget returns no custom result, leaving the host's native path available. Posthorse therefore does not promise summary-free behavior on every route ([RT-RTE-automatic-recovery](#rt-rte-automatic-recovery); SRC-1, `src/rollover.ts`, `src/budget.ts`).

> if (event.reason === "manual") {
> 	return;
> }
> --- `src/rollover.ts`

A narrower turn-end threshold fallback applies only to completed, non-length, non-aborted turns without compaction/context-edit drafts, known supported enabled usage at threshold, and a projected fresh compaction window with no later turn-start input. It preserves `event.continue`; it does not force another response after a final answer. Other spans, overflowing initial requests and native recovery eligibility remain Pi-owned (SRC-1, `src/rollover.ts`, `docs/reference.md`).

**Case 3 — edited/provenance-sensitive recovery and later hook edits.** Automatic recovery omits projected-away inputs, uses context-edit replacements and replacement IDs, distinguishes direct owner inputs from visible coordination, and recognizes `ask_question` answers only when a successful unnamespaced result links to a projected unnamespaced call and an effective registered tool. Tool receipts preserve identifiers and bounded excerpts, not certified progress. Synchronous receipts are selected from the trailing batch; projected orphan/legacy async results can also remain eligible. Earlier automatic records are not nested wholesale: an ancestry walk carries owner anchors or reaches a nonautomatic checkpoint, with pointers to skipped records. Payload construction can omit older index lines, result headers or text; retrieval remains necessary (SRC-1, `src/recovery.ts`, `src/recovery-results.ts`).

The native automatic hook reads the host projection at its hook time. The eager turn-end fallback cannot see later same-phase edits; later editors must replace/remove its draft. Competing compaction extensions can also displace a result under the documented host last-result rule. Neither result is a deployment-independent invariant (SRC-1, `src/rollover.ts`, `docs/reference.md`).

> // ponytail: turn_end drafts are eager. Later projection editors must replace/remove this draft;
> // upgrade to a host post-boundary hook if recovery must include later handler edits.
> --- `src/rollover.ts`

**Case 4 — forced prompts, alternate I/O and physical overflow.** Forced prompts cause Posthorse guidance to enter as hidden custom conversation content rather than a system section. Direct model transports, raw payload replacements and unrelated host tools do not pass through Posthorse's page admission. Character/token approximations cannot certify provider rejection limits. Notes' lexical path checks are not a filesystem sandbox: publication follows symlinks, and available host editors are alternative note writers. Nested subagent journals can be retrieved, but Posthorse neither launches those agents nor controls what they initially receive (SRC-1, `src/rollover.ts`, `src/budget.ts`, `src/notes.ts`, `src/files.ts`, `src/session-files.ts`, `docs/reference.md`).

> The host owns physical request sizing and output clamping; custom transports and raw payload replacements remain responsible for their request sizes.
> --- `docs/reference.md`

These four cases cover callback admission, automatic/native alternatives, projection/hook ordering and bypassing request/I/O paths. Host persistence internals, actual grant sets, subprocess execution isolation, provider-native tools and deployed scheduling remain uninspected outside the frozen extension source. Source inspection establishes neither their absence nor isolation.

### Guarantees, authority and change

**Foreground reset admission:** Posthorse owns the map/result/error/capacity checks at its callback and turn-end handler. Guarantee strength: **protocol**. Implementation conclusion status: **wired**. Operation conclusion status: **uninspected**. Coverage is its own foreground reset request, not background synchronization, sibling side-effect rollback or later-handler aborts. Required external contract: truthful foreground result identities/errors, event ordering, host compaction projection/persistence and continuation (SRC-1, `src/context-tools.ts`, `src/rollover.ts`; [RT-RTE-explicit-reset](#rt-rte-explicit-reset)).

**Supported automatic recovery avoids silent summarizer fallback on construction error:** owner is Posthorse; enforcement is the automatic hook's try/catch and cancellation return. Guarantee strength: **protocol**. Implementation conclusion status: **wired**. Operation conclusion status: **uninspected**. It covers a reached supported automatic hook, not manual compaction, unsupported budgets or failed host preparation. The host must honor cancellation/custom compaction (SRC-1, `src/rollover.ts`; [RT-RTE-automatic-recovery](#rt-rte-automatic-recovery)).

**Bounded page delivery:** owner is shared `PageReservations`; enforcement precedes tool delivery and accounts for sibling returns. Guarantee strength: **best effort**. Implementation conclusion status: **wired**. Operation conclusion status: **uninspected**. Budgeting uses native estimated usage, length/4 estimates, fixed image cost and margins; headers/continuation text are additional considerations, not provider-exact token accounting. It covers notes/history callbacks, not arbitrary tools, full notes writes, shell output or raw transport replacement. The host must supply current usage/configuration and preserve delivery semantics (SRC-1, `src/paging.ts`, `src/budget.ts`, `src/history-pages.ts`).

**Note publication:** owner is `publishFile`; enforcement is staging and rename in the resolved target directory. Guarantee strength: **protocol**. Implementation conclusion status: **wired**. Operation conclusion status: **uninspected**. Pre-publication failure preserves the old file; same-process mutation ordering depends on Pi's queue. It does not certify semantic validity, cross-process merge, hardlink identity, ACL preservation or power-loss durability (SRC-1, `src/files.ts`, `src/notes.ts`, `docs/reference.md`).

The capability surface includes reset, capacity reporting, notes and history hooks/tools. The current active tools and host permissions are deployment-specific. Code executes with the hosting Node process's filesystem access; no separate isolation envelope is established by this source. Guidance and reminders exercise model-interpreted authority, while compaction drafts and page refusals exercise host-mediated symbolic controls ([RT-BAP-model-guidance](#rt-bap-model-guidance), [RT-BAP-compaction-draft](#rt-bap-compaction-draft)).

Retained task-state admission is model/caller-authored text with software publication checks, not per-content human approval. Full replacement and append are available; host editors can make sectional changes. None of these checks judges whether the note is true. The exact note lineage, later revisions and memory properties are left to the memory analyst ([RT-RTE-note-admission](#rt-rte-note-admission)).

Product changes are operator-mediated at the documented installation/update interface: update the package, restart to load new code, and remove duplicate copies or competing rollover policies. Documentation supplies this admission procedure, not an inspected updater implementation. Removing Posthorse leaves retained notes/journals. Package verification commands and shipped evaluator drivers are proposed engineering checks, not model-driven capability acquisition or observed successful release admission. No runtime self-modification or improvement conclusion is needed to explain these paths (SRC-1, `docs/reference.md`, `package.json`).

> Restart Pi after installing or updating Posthorse to load the new extension code.
> --- `docs/reference.md`

### Inspection coverage and limits

Runtime source reads covered `index.ts`, `package.json`, `docs/reference.md`, complete `src/context-tools.ts`, `src/budget.ts`, `src/rollover.ts`, `src/recovery.ts`, `src/recovery-results.ts`, `src/notes.ts`, `src/files.ts`, `src/history.ts`, `src/paging.ts`, `src/contracts.ts`, `src/reminders.ts` and `src/history-pages.ts`. Additional bounded reads covered active-context exclusion, archive/branch search selection in `src/history-search.ts`, session membership/enumeration in `src/session-files.ts`, and the later-abort forcing test in `test/official.test.mjs`; test declaration searches also covered `test/native.test.mjs`. All are SRC-1 at the registered commit. These add implementation and evaluator-design coverage, not new observed-run evidence. Remaining history-normalization/prefilter internals were not independently audited here; exact normalized retrieval completeness remains limited by that inspection and the external host. No excluded engineering checker or release machinery was silently added to the functional boundary.

## Shared records

### Components

#### RT-CMP-active-model
Label: Active Pi model

Source-native identity: Pi's current `ctx.model`, used by the default settings reader and host model execution. Representational form: distributed-parametric inference model, external to Posthorse; model/tool choices are interpreted in the host loop. Storage substrate: external provider/host weights and endpoint, uninspected. Posthorse stores no model parameters in the inspected entry/admission code (SRC-1, `index.ts`, `src/rollover.ts`, `package.json`).

Parameters changing during operation: uninspected — provider internals are outside the frozen source. Exact model version pinned: not established; Posthorse resolves current host configuration, not a fixed deployment checkpoint. Mutable endpoint resolving to another model: uninspected — host/provider routing is external; shipped SDK evaluator source includes model changes and virtual-model routing, so analysis must not assume one immutable foreground model (SRC-1, `test/official.test.mjs`, `src/budget.ts`). The extension's fixed source revision does not pin the model.

#### RT-CMP-page-reservations
Label: Shared page reservations

Source-native identity: one `PageReservations` instance allocated by `createPosthorse`, shared by notes/history. Representational form: symbolic counters, usage snapshots and arithmetic. Storage substrate: Node process memory; reset at turn/session boundaries. It subtracts newly observed usage growth from outstanding reservations to avoid counting serial delivery twice, while still reserving sibling results (SRC-1, `index.ts`, `src/paging.ts`).

> /** Shared by note and history tools. Reservations precede delivery and reset at a turn boundary. */
> --- `src/paging.ts`

### Operative objects

#### RT-OBJ-reset-requests
Label: Foreground reset requests

Source-native identity: `resetRequests`, a map from tool callback ID to admitted handoff. Representational form: symbolic authorization index; handoff values are natural-language content interpreted by a later model, not map rules. Storage substrate: process memory for one turn. Turn/session start and settlement clear it; it is not the durable boundary. The map authenticates origin within Posthorse's own callback, not a human's approval (SRC-1, `src/rollover.ts`).

> const resetRequests = new Map<string, string>();
> --- `src/rollover.ts`

#### RT-OBJ-context-guidance
Label: Context self-management guidance

Source-native identity: `buildGuidance` output and checkpoint reminder prose. Representational form: natural language for foreground model interpretation; symbolic window/configuration fingerprints are separate routing metadata. Storage substrate: regenerated request-local system/custom content; reminders also become host journal entries. Guidance states capacity uncertainty, checkpoint procedure and restoration/verification requirements. Its delivery does not establish compliance (SRC-1, `src/budget.ts`, `src/rollover.ts`, `src/reminders.ts`).

> After a rollover, earlier conversation stays in history. Restore notes and todos, then verify live state before stateful or external work; automatic handoffs record inputs, not progress.
> --- `src/budget.ts`

### Routes

#### RT-RTE-request-guidance
Label: Request guidance and checkpoint reminder

Endpoints/progression: host start/context/turn hooks → Posthorse guidance and eligibility rules → model-visible section/custom message or steer reminder. Owner: Posthorse determines delivery; the foreground model decides compliance. Current system options, native usage, effective compaction settings, pending messages and leaf-certified reminder ancestry determine control (SRC-1, `src/rollover.ts`, `src/budget.ts`, `src/reminders.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Modified request context, or a queued steer reminder on an eligible working turn; no tool return is required.
- Later read-back: Persisted reminder fingerprints affect later reminder eligibility and filtering; guidance itself is regenerated, not recalled from a stored learning record.
- Delegated visibility: uninspected — Posthorse controls this installed host's hooks, not independently configured remote/subagent model input.
- Selection predicate: Enabled supported budget, known usage inside the final min(32,000 tokens, 10% usable) band below rollover, non-final turn, and no matching window/context/reserve fingerprint already recorded or pending.
- Invalidation or expiry: Stale or disabled reminders are filtered from active input, not deleted from history; session/tree changes invalidate lookup and settled runs clear saved forced-prompt options.
- Activation or effect: Request-local prose is inserted or a reminder queued; actual checkpoint compliance and changed behavior are unobserved.
- Evidence limits: Hook and model interpretation contracts belong partly to Pi; reminder delivery cannot guarantee receipt before a large turn crosses threshold.

Working-context control is code-decided filtering and injection. Forced system prompts use custom conversation content; normal prompts use a named system section. No theory revision is admitted by this route. It applies fixed shipped instructions to open-ended user tasks, not a bounded experiment with an answer oracle (SRC-1, `src/rollover.ts`).

> { deliverAs: "steer" },
> --- `src/rollover.ts`

#### RT-RTE-explicit-reset
Label: Foreground explicit reset admission

Endpoints/progression: foreground model → `new_context` callback → turn-local ID map → turn-end foreground checks → host compaction draft → fresh model call. Owner: foreground model proposes natural-language continuation; Posthorse decides whether to draft; Pi commits/persists/schedules. Human contribution: initiating tasks or supplying text is possible, but there is no per-handoff human approval gate in this callback (SRC-1, `src/context-tools.ts`, `src/rollover.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: A requested-reset tool result after capacity admission; oversized handoffs throw an error before recording the request.
- Later read-back: If the host commits the boundary, the handoff becomes compaction-summary input for a later invocation; earlier journal entries remain reachable through history.
- Delegated visibility: Foreground reset does not stop/background-synchronize work; what separate workers receive is uninspected outside the host contract.
- Selection predicate: First foreground `new_context` result whose call ID is in Posthorse's map, no sibling error, no prior assistant error/abort, non-aborted event/signal and handoff fitting the freshly computed pending-input-aware limit.
- Invalidation or expiry: Requests are consumed/cleared at turn settlement and cleared at turn/session start; queued-input overflow yields a visible deferred-reset message without changing current context.
- Activation or effect: Draft uses `firstKeptEntryId: null` and continuation, removing prior active context under the host's retain-none contract; it does not roll back earlier tool effects.
- Evidence limits: Later-handler abort/edits, host commit semantics and all background work are outside this enforcement point; no executed trace establishes actual commitment.

Operating mode: open-ended foreground task continuation. Answer oracle: inapplicable — ID/error/capacity admission is not a correctness test of handoff content. Posthorse can reject oversized payloads or decline the draft; the caller can retry with notes plus a shorter handoff. Rollback/recovery is preservation of current context before admission, not undo of a committed boundary; history and notes support continuation afterward. Proposal guidance asks for readable prose, concise notes and preserved constraints (SRC-1, `src/context-tools.ts`, `src/budget.ts`).

> if (summary !== undefined && !event.toolResults.some((result) => result.isError)) {
> 	return explicitReset(event, ctx, summary, () =>
> 		freshPayloadChars(host, activeToolTokens(), event.context.pendingMessages),
> 	);
> }
> --- `src/rollover.ts`

#### RT-RTE-automatic-recovery
Label: Automatic recovery admission

Endpoints/progression: host automatic compaction preparation → supported-budget hook → branch/projection filtering → bounded recovery text → sentinel/custom compaction result → host persistence and later model. An eligible fresh-window threshold turn-end fallback produces an equivalent retain-none draft through a narrower path. Owner: Posthorse code proposes/selects text and drafts; host determines native eligibility and final admission. No runtime summarizer model selects these recovery records (SRC-1, `src/rollover.ts`, `src/recovery.ts`, `src/recovery-results.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Native hook returns a custom compaction with recovery summary and sentinel ID, returns cancellation on failure/abort, or declines manual/unsupported cases; threshold fallback returns a draft preserving normal continuation.
- Later read-back: Committed bounded recovery reaches the next model as compaction summary; later automatic ancestry can carry selected owner anchors and checkpoint pointers rather than nested automatic records.
- Delegated visibility: Coordination prose and projected legacy async results can be included; this is retained evidence delivery, not control of delegates or proof their work finished.
- Selection predicate: Projection omissions/replacements govern inputs; direct user and provenance-linked registered unnamespaced `ask_question` answers are owner inputs. First/latest owner and latest overall inputs become anchors; other inputs get budgeted index lines. Projected eligible tool results get bounded evidence excerpts.
- Invalidation or expiry: Context edits remove/replace source evidence; window boundaries change the current set. Older checkpoints and carried inputs are explicitly labeled possibly stale/already handled; later fallback-phase edits require another handler to replace/remove the draft.
- Activation or effect: A custom retain-none draft replaces accumulated model input with bounded recovery and leaves journal retrieval available; reliable task continuation is not established.
- Evidence limits: Hook reachability, persistence, later handler ordering and provider overflow remain host-dependent. Missing observations prevent benefit or current-progress conclusions.

Operating mode: emergency context continuation under host policy, not an experiment or improvement curriculum. Answer oracle: inapplicable — recovery preserves selected evidence without an expected-task-answer comparator. Computational proposal/admission dominates; humans need not approve each record. Veto/rejection is code cancellation/capacity checks and host competing handlers. Recovery construction failure cancels rather than silently falling into host summarization; unsupported/manual cases deliberately leave native behavior available. A sentinel can be appended before subsequent failure, so cancellation of compaction is not a transaction over every journal append (SRC-1, `src/rollover.ts`).

The persisted proposal contains inputs, provenance, bounded results, IDs and a fixed warning, not certified progress or a newly evaluated theory. The stack-frame analogy fits discarding a whole active window and keeping a bounded continuation value; it breaks because the remaining history pointers require explicit retrieval and provide no automatic live references (SRC-1, `src/recovery.ts`, `src/history.ts`).

> // Hook errors are swallowed by Pi, which would run its summarizer; cancel instead.
> --- `src/rollover.ts`

#### RT-RTE-note-admission
Label: Durable note admission

Endpoints/progression: caller/model `notes write/append` → relative-path checks and shared location → host mutation queue → local filesystem publication → tool result. Owner: caller proposes content; software admits I/O. Representational form of content: natural-language text, potentially task instructions; path/operation/schema are symbolic controls. Substrate: plaintext files at the shared notes location, with package-checkout migration when needed (SRC-1, `src/notes.ts`, `src/files.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `Wrote` or `Appended to` the actual absolute file path, or an exception; publication is not a truth judgment.
- Later read-back: Files remain available to future notes reads/searches and host editors across resets/worktrees; the actual later content and revision findings belong to the memory analyst.
- Delegated visibility: Shared filesystem location permits linked-worktree/process access under OS grants; no delegate-specific delivery or isolation is established.
- Selection predicate: Caller-selected relative path, required content, lexical traversal rejection and resolved filesystem target; no semantic approval selector.
- Invalidation or expiry: Write replaces all text including empty clears; append adds newline-terminated records. No automatic task-state expiry is implemented in this admission path; external writers can alter files.
- Activation or effect: Changes retained plaintext accessible to later model retrieval; downstream reliance or correct task-state restoration is unobserved.
- Evidence limits: Symlink following and host editor alternatives prevent treating lexical checks as containment/isolation. Same-process queue ordering does not imply cross-process merge or power-loss durability.

Operating mode: open task-state maintenance. Answer oracle: inapplicable — no expected-answer comparator. Human contributions: optional authorship/edits, not mandatory per-content approval. Software rejects invalid paths, missing content, aborts or failed filesystem publication; it does not reject false prose. Pre-rename errors preserve the previous note; there is no semantic version rollback. Available host editors are an alternate admission path expressly recommended by shipped guidance, outside this tool's publication guarantees. Documentation identifies package removal as preserving notes and update migration as protecting agent-installed Git checkout notes (SRC-1, `src/notes.ts`, `src/files.ts`, `src/budget.ts`, `docs/reference.md`).

> /** Same-directory replacement; pre-rename failures preserve the old note and its metadata. */
> --- `src/files.ts`

#### RT-RTE-retained-retrieval
Label: Budgeted notes and history retrieval

Endpoints/progression: foreground model request → notes file selection or history branch/project archive selection → text/image normalization and matching → page budget → foreground tool result. Owner: foreground caller chooses query/path/ID; Posthorse selects and pages; host delivers to the current provider context. Tools do not automatically reload every earlier message after rollover (SRC-1, `src/notes.ts`, `src/history.ts`, `src/history-search.ts`, `src/session-files.ts`, `src/history-pages.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Bounded note content/list/search rows, or history match excerpts/entry text and stored images with continuation positions; insufficient capacity refuses the page.
- Later read-back: Explicit reads deliver persisted notes or journal material to a later invocation. The read operation itself does not revise retained knowledge.
- Delegated visibility: `all: true` can include nested subagent journals whose parent belongs to the project; that does not expose the foreground context to those agents or grant delegation authority.
- Selection predicate: Notes use caller path or case-insensitive literal text, newest-file ordering and binary/size filters. History uses query/scope/cursor or exact entry ID, excludes fully visible matching entries, and limits archives to current/project sessions plus nested descendants.
- Invalidation or expiry: Pages reset reservations each turn; serial native usage growth reduces pending reservations. History cursor requires unchanged query/scope; files/searches remain live and external edits/reordering can change results. Callers retain positions and can retry after reset.
- Activation or effect: Selected retained text/images enter a host tool result and can inform later model decisions; delivery is wired, actual behavioral reliance unobserved.
- Evidence limits: Budget estimates are not provider-exact; normalization/prefilter completeness was not independently audited in this member, and OS/host/provider access contracts are external.

Original-content matching precedes recovery echoes; active-context exclusion compares projected content rather than only IDs. Project file membership requires a valid header and current working-directory match, except selected current-session inclusion and inherited parent membership. A read can resolve a raw original ID or a context-edit replacement ID; these are different evidence versions, not interchangeable current-state assertions. Retain-none removal plus explicit reload is working-context control, not ordinary accumulation (SRC-1, `src/history-search.ts`, `src/history.ts`, `src/session-files.ts`, `docs/reference.md`).

> "Search or read earlier session entries, including previous context windows. search skips entries still in your active context and lists original content before recovery echoes, newest first; all=true also searches this project's other sessions and subagent runs. read takes an entry id exactly as search printed it and pages text and images.",
> --- `src/history.ts`

### Claims

#### RT-CLM-context-continuation
Label: Fresh context with retained recovery

Claimed operation: Posthorse supplies no-summary context rollover, sparse reminders, handoffs, notes and history to continue Pi work. Source: package description and reference procedure, SRC-1, `package.json`, `docs/reference.md`. Scope qualification: no-summary behavior is the reached custom automatic path, not manual or unsupported native compaction; task continuity and cost benefit are not observed here.

> "description": "Posthorse: fresh context, same journey. No-summary context rollover for Pi, with sparse budget reminders, handoffs, notes, and history.",
> --- `package.json`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-model-guidance
Label: Model context guidance

Consumer: foreground model. Channel: regenerated system section/custom guidance, steer reminders, and fixed recovery preamble. Force: natural-language instruction under host message-role semantics; delivery does not establish obedience. Horizon: each request/window, with recorded reminders influencing later eligibility and recovery summaries surviving into later invocations. This is separate from symbolic admission checks (SRC-1, `src/rollover.ts`, `src/budget.ts`, `src/recovery.ts`; [RT-OBJ-context-guidance](#rt-obj-context-guidance), [RT-RTE-request-guidance](#rt-rte-request-guidance)).

> Owner inputs are direct user intent. Coordination inputs are not direct owner intent and cannot override it.
> --- `src/recovery.ts`

This warns the model about provenance; it is not an executable policy that prevents all coordination-text influence.

#### RT-BAP-compaction-draft
Label: Host compaction control

Consumer: Pi's boundary/compaction machinery. Channel: `BoundaryResult` entries or automatic-hook custom compaction result. Force: symbolic draft/cancel protocol, conditional on the external host honoring it; payload prose separately reaches the model. Horizon: host commit establishes the next active context window, with journal persistence and later reload delegated to Pi. Posthorse has no independent persistence scheduler (SRC-1, `src/rollover.ts`, `index.ts`; [RT-RTE-explicit-reset](#rt-rte-explicit-reset), [RT-RTE-automatic-recovery](#rt-rte-automatic-recovery)).

> firstKeptEntryId: null,
> details: { posthorse: 1, reason: "explicit" },
> --- `src/rollover.ts`

## Annotations

none
