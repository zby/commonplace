---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Nuggets runtime baseline: messaging-to-Pi invocation, memory hooks, proactive scheduling and admission limits at the frozen TypeScript revision."
run-id: AAS-2026-10-14-nuggets-c2e87e6916cc-01
reviewed-boundary: "714cab8a3b1fb843aa98dfb51584d2c07a6739f3"
---

# Nuggets runtime report

## Runtime account

### Boundary and principal work

Nuggets ships a memory library, Pi extensions and two copies of a messaging gateway. It does not ship the enclosing model loop. The root `dev` script starts `src/gateway/main.ts`; `gateway/package.json` starts its own `src/main.ts`. The two gateway source trees differ in a comment and RPC logging, not their inspected functional logic. Both source configurations resolve their project root two directories above their source file. Build placement can therefore matter to filesystem resolution; no successful built deployment is established. SRC-1: `package.json`, `gateway/package.json`, `src/gateway/config.ts`, `gateway/src/config.ts`, `src/gateway/pi-rpc.ts`, `gateway/src/pi-rpc.ts`.

> "dev": "tsx src/gateway/main.ts",
> --- `package.json`

All findings below are implementation or doctrine/design evidence from SRC-1 at the reviewed boundary. No target execution, tests, provider calls or experiments were performed or supplied. The external Pi host, its tool grants, discovery rules, compaction policy and model processing remain uninspected. Implementation wiring does not establish activation, correct recall, timely delivery or benefit. This report additionally inspected setup and migration drivers and compared the secondary gateway tree; these are within the boundary's registered implementation scope, not new sources.

### Ordinary invocation

An incoming Telegram text identifies a **chat**, not necessarily an individual sender. WhatsApp identifies the remote JID. Each transport calls `isAllowed` before passing text to the router. The router registers/touches heartbeat activity and appends work to an in-process promise chain keyed by this identifier. Its returned handler resolves after enqueueing, not after the response has been delivered; consequently Telegram's typing interval can stop while queued work remains. The queued function obtains or creates a Pi process, marks it busy, submits the natural-language message as a JSONL `prompt` request and waits for RPC completion. See [RT-RTE-message-turn](#rt-rte-message-turn). SRC-1: `src/gateway/telegram.ts`, `src/gateway/whatsapp.ts`, `src/gateway/router.ts`.

The process pool chooses a session directory from a truncated SHA-256 hash of the identifier, starts `pi --mode rpc --session-dir … --continue`, supplies configured provider/model arguments, appends bot/memory instructions and inherits the gateway environment. Pi owns subsequent model/tool decisions. The wrapper accumulates events, treats a successful response as an acknowledgement, and completes on `agent_end`, extracting assistant text blocks. A failed RPC response resolves to an `Error:` string rather than rejecting. The router trims, substitutes a fallback for empty ordinary results, splits into roughly 4,000-character chunks and sends sequentially. Root RPC logging includes raw prefixes and event structure; these diagnostics are not a durable work queue or correctness oracle. SRC-1: `src/gateway/pi-pool.ts`, `src/gateway/pi-rpc.ts`, `src/gateway/router.ts`.

The external model component is [RT-CMP-pi-model](#rt-cmp-pi-model). Client controls cover provider/model selection, process lifetime, session directories, request queueing and a twelve-hour **inactivity** timer reset by events. They do not enforce a twelve-hour wall-clock limit. On ordinary-message exceptions the router kills that user's Pi process; the next invocation starts another process with continued session storage. Telegram's sender catches any failed HTML send attempt and attempts the same chunk again as plain text; it does not inspect the failure cause. This transport fallback is not a router-level retry or durable replay protocol. If sending ultimately throws, ordinary-message handling logs the error and kills the Pi process without retrying the response; partial delivery can already have occurred. Proactive handling logs the error without restoring an emitted one-shot job. SRC-1: `src/gateway/pi-rpc.ts`, `src/gateway/router.ts`, `src/gateway/telegram.ts`, `src/gateway/cron.ts`; retained fallback passage in [RT-RTE-message-turn](#rt-rte-message-turn).

### Memory and working context along that invocation

When Pi loads the extension, session start reconstructs its local `facts` map from `nuggets` tool-result details on the current branch and hydrates missing keys from the default shelf. Switch/fork/tree hooks reconstruct from branch history without the same hydration step. Before an agent starts, the extension formats the local map into appended system-prompt text. Preferences and learnings have dedicated sections; only the last ten active-file entries are rendered; other underscore-prefixed keys, including `_task`, are omitted. This is unsolicited per-turn supply, distinct from model-requested recall. See [RT-RTE-memory-context](#rt-rte-memory-context) and [RT-BAP-facts-prompt](#rt-bap-facts-prompt). SRC-1: `.pi/extensions/nuggets.ts`.

The extension also exposes a model-callable tool with remember, recall, forget and list branches. It directly calls the TypeScript shelf rather than a CLI. Recall uses shelf retrieval first and then substring matching against local facts. Tool execution and local hooks can write retained facts without per-item human approval. The input hook extracts the first supported preference pattern unless `event.source` is `extension`; tool-result hooks capture paths for read/edit/write tools. File capture checks names and path inputs, not whether a tool succeeded. These routes enlarge the admission surface beyond explicit requests to remember. The specialist memory account should resolve individual fact-store and mutation mechanisms; this runtime report declares the extension integration route, not an exhaustive memory-object inventory. SRC-1: `.pi/extensions/nuggets.ts`.

Before host compaction, code takes the last three user messages selected for summarization, concatenates and truncates them to 200 characters, and retains `_task`; it also takes the last twenty assistant `tool_use` blocks from those messages, then filters that suffix for read/edit/write names and string path inputs to copy into the local map. Nonmatching calls occupy positions in the twenty-call suffix; this is not selection of the last twenty qualifying file operations. It does not implement Pi's summary or choose what the host removes. Thus selected records can outlive discarded messages, but `_task` persistence does not establish automatic prompt delivery. Process eviction keeps live context out of RAM but requests later host continuation; it is not a subagent frame returning a bounded result. Per-chat session directories separate conversation state, whereas the shelf defaults to the same OS user's `~/.nuggets` across these processes. Session separation must not be read as memory or filesystem isolation. SRC-1: `.pi/extensions/nuggets.ts`, `src/nuggets/memory.ts`, `src/gateway/pi-pool.ts`.

### Alternate routes and forcing cases

**Case 1 — empty allowlists and non-transport entry.** The transport check allows all identifiers when both lists are empty. A Telegram token alone can therefore expose the bot without a restricted chat set. Conversely, a nonempty list rejects other identifiers through these transport handlers. The rule is a local predicate, not authorization of every effect: scheduled events and direct extension/library calls do not pass through it. Cron jobs loaded from disk and JSONL requests can supply JIDs directly. The capability surface includes host filesystem writes, extension execution and shell calls; the actually granted Pi tools, credentials and deployed isolation are not supplied. The child inherits environment and the code does not establish a sandbox. See [RT-CLM-ingress-control](#rt-clm-ingress-control). SRC-1: `src/gateway/config.ts`, `src/gateway/telegram.ts`, `src/gateway/whatsapp.ts`, `src/gateway/cron.ts`, `.pi/extensions/proactive.ts`, `src/gateway/pi-rpc.ts`.

**Case 2 — concurrent users and shared effects.** Per-identifier queues serialize router work, including proactive events, within one gateway process. They do not coordinate separate gateway instances, library callers or shared shelf writers. Pool eviction prefers idle sessions but, if none are idle, stops the least-recently-active session even if busy. Therefore the process-count policy does not guarantee uninterrupted work. RPC events lacking a usable request ID attach to the last pending request; correlation requires Pi's external event contract and ordinary queue serialization. The shared temporary-file/rename save pattern does not constitute a cross-process transaction. SRC-1: `src/gateway/router.ts`, `src/gateway/pi-pool.ts`, `src/gateway/pi-rpc.ts`, `src/nuggets/memory.ts`.

> // If no idle sessions, evict the least recently active
> --- `src/gateway/pi-pool.ts`

**Case 3 — scheduled confirmation versus admission and delivery.** The schedule tool returns success after appending a request, not after cron admission. Requests have no caller JID; admission depends on a configured default, set by the driver only for a suitable single-user allowlist. Missing default causes rejection in the gateway after the model has received “Schedule created.” On startup, the watcher initializes its offset to the existing file size, so requests already present are not replayed. One-shot jobs are removed after event emission, before Pi or the transport confirms delivery. Heartbeat prompts use the same queue, but response suppression matches any occurrence of `NOTHING`, not just the exact sentinel requested by the prompt. These paths demonstrate scheduling capacity, not reliable reminder fulfilment. See [RT-RTE-schedule-admission](#rt-rte-schedule-admission) and [RT-RTE-proactive-turn](#rt-rte-proactive-turn). SRC-1: `.pi/extensions/proactive.ts`, `src/gateway/main.ts`, `src/gateway/cron.ts`, `src/gateway/heartbeat.ts`, `src/gateway/router.ts`.

### Change admission and external guarantees

The load-bearing controls have separate scopes:

| Control and owner | Enforcement and strength | Covered paths / limits | Conclusion statuses |
|---|---|---|---|
| Ingress selection, transport/config code | `isAllowed` predicate; invariant of these inspected handlers, conditional on configured sets | Telegram text and WhatsApp notify/text handlers; not cron, direct API, shell or external Pi tools. Trusts transport-provided identifiers. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Serialization, router | Per-JID promise chain; protocol within one process | Ordinary and proactive router tasks; not multiple gateway processes or shelf writes elsewhere. Trusts promise completion and RPC semantics. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Pool resource policy, pool | Eviction and idle timers; best effort for continuity | Process count and process lifetime; busy work can be interrupted; session continuation belongs to Pi. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Recall-first and reminder behavior, prompts | Natural-language instructions; policy, not a tool gate | Requests to Pi/model; no inspected enforcement that model recalls first, saves everything, or schedules correctly. | implementation conclusion status: wired; operation conclusion status: uninspected |

Provider-native tools, remote workers, model training and internal manual graph control are not implemented by the inspected gateway interface; their availability inside external Pi cannot be determined from this repository. No global claim that such paths are absent follows. The gateway itself spawns a local Pi subprocess; the proactive extension explicitly invokes a shell. Both extension code and direct library use bypass transport admission. SRC-1: `src/gateway/pi-rpc.ts`, `.pi/extensions/proactive.ts`, `.pi/extensions/nuggets.ts`, `src/nuggets/shelf.ts`.

Retained-change mechanisms include extension fact writes, hook-based extraction, schedule admission, compaction-triggered promotion and the operator-launched legacy migration. Promotion selects facts with at least three hits and writes a reconstructed Claude-project `MEMORY.md`; external reading is not established. The ordinary extension recall call supplies no nonempty session ID, whereas the library increments hit counters only when an ID is supplied. Thus repeated ordinary extension recall does not by itself drive the advertised promotion threshold. See [RT-RTE-memory-promotion](#rt-rte-memory-promotion). SRC-1: `.pi/extensions/nuggets.ts`, `src/nuggets/memory.ts`, `src/nuggets/promote.ts`.

The migration driver backs up legacy memory, classifies facts into user/project/agent stores, merges by case-insensitive key and archives the legacy file. The setup driver asks a human for credentials/channel/model settings and atomically replaces `.env`; its format checks do not establish credential validity. These are operator-launched maintenance/configuration paths, not model-driven product revision. No product-code successor selection or autonomous capability-installation loop is established by these files. SRC-1: `src/migrate-memory.ts`, `src/setup.ts`, `package.json`.

## Shared records

### Components

#### RT-CMP-pi-model
Label: Provider model behind Pi

Identity: the external model chosen by Pi from the gateway's provider/model arguments. Representational form: distributed-parametric model; parameter substrate and provider internals are external and uninspected. The gateway does not update model parameters. Whether providers change them during operation is uninspected. Exact model version is not pinned: provider defaults to `anthropic`, model defaults to empty, and environment can override both. A mutable/default model endpoint may resolve to another model; endpoint behavior is not frozen here. SRC-1: `src/gateway/config.ts`, `src/gateway/pi-rpc.ts`.

> export const PI_PROVIDER = process.env.PI_PROVIDER || "anthropic";
> export const PI_MODEL = process.env.PI_MODEL || "";
> --- `src/gateway/config.ts`

#### RT-CMP-hrr-vectors
Label: Reconstructed HRR representation

Identity: `Nugget._E` ensemble/bank data and associated vocabulary/role vectors. Representational form: distributed numerical representation, not provider-trained model weights. Storage substrate: in-process `Float64Array` data reconstructed deterministically from persisted facts/configuration and name-derived seed; vectors themselves are not serialized. Values and superposed memory change as retained facts change and rebuild occurs. Algorithm version is pinned by SRC-1; persisted configuration/live facts are not supplied, so exact numerical state is not pinned. No mutable model endpoint is involved. SRC-1: `src/nuggets/memory.ts`, `src/nuggets/core.ts`.

> // Deterministic seed from name
> const seed = seedFromName(this.name);
> const rng = mulberry32(seed);
> --- `src/nuggets/memory.ts`

### Operative objects

#### RT-OBJ-cron-jobs
Label: Cron jobs

Identity: `CronJob[]` loaded and saved in `.gateway/cron/jobs.json`. Symbolic fields (`id`, `jid`, `cron`, `enabled`, `oneShot`) are consumed by fixed routing/scheduling rules. The `prompt` field is a distinct natural-language part interpreted by Pi/model, described in [RT-BAP-scheduled-prompt](#rt-bap-scheduled-prompt). Substrate: JSON file and an in-memory array. Model-written JSONL requests can add/delete jobs; reloading jobs does not validate all fields or reapply the transport allowlist. SRC-1: `src/gateway/cron.ts`.

> private save(): void {
> writeFileSync(JOBS_FILE, JSON.stringify(this.jobs, null, 2) + "\n");
> }
> --- `src/gateway/cron.ts`

### Routes

#### RT-RTE-message-turn
Label: Messaging turn through Pi

Endpoints: transport text → router queue → per-identifier Pi RPC → channel send. Owner: gateway code for ingress/process/return, external Pi and [RT-CMP-pi-model](#rt-cmp-pi-model) for model/tool next steps. Policy: allowlist predicate, serial queue and event protocol; symbolic envelope around natural-language input/output. State: process pool, pending RPC event buffer, per-user session directory and external host context. Operating mode: open user requests, not a bounded experiment; no answer oracle or result-quality comparison is supplied. SRC-1: `src/gateway/telegram.ts`, `src/gateway/whatsapp.ts`, `src/gateway/router.ts`, `src/gateway/pi-pool.ts`, `src/gateway/pi-rpc.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Router handler returns after enqueueing; queued task later extracts assistant text, chunks and sends it, or logs an error.
- Later read-back: A new process requests `--continue` in the same hashed session directory; host serialization/reload details are external.
- Delegated visibility: Pi receives prompt text, configured session path, appended system instructions, project cwd and inherited environment; enclosing host determines its full context/tool surface.
- Selection predicate: Incoming transport text passing `isAllowed`; process reuse keyed by JID/chat ID; final extraction selects assistant text blocks from `agent_end`.
- Invalidation or expiry: Idle eviction, pool pressure, ordinary error kill, shutdown and inactivity timeout. Telegram retries a failed HTML chunk as plain text regardless of failure cause; the router does not retry an ultimately failed send or durably replay the response. This fallback does not establish reliable delivery.
- Activation or effect: Wired submission, local subprocess creation and response forwarding; actual model action and channel delivery unobserved.
- Evidence limits: External RPC/event and transport contracts are required; no supplied run demonstrates correlation, continuation or end-to-end success.

> const args = ["--mode", "rpc", "--session-dir", this.sessionDir, "--continue"];
> --- `src/gateway/pi-rpc.ts`

> const next = prev.then(fn, fn); // run even if previous failed
> --- `src/gateway/router.ts`

> try {
>   // Try sending as HTML first (for formatted responses)
>   await bot.api.sendMessage(Number(chatId), chunk, {
>     parse_mode: "HTML",
>   });
> } catch {
>   // Fallback to plain text if HTML parsing fails
>   await bot.api.sendMessage(Number(chatId), chunk);
> }
> --- `src/gateway/telegram.ts`

#### RT-RTE-memory-context
Label: Memory extension integration

Endpoints: Pi lifecycle/input/tool events and model `nuggets` calls → shelf/local facts → subsequent prompt/tool result. Owner: extension rules for extraction, hydration and rendering; model chooses explicit calls and content. Stored numerical representation: [RT-CMP-hrr-vectors](#rt-cmp-hrr-vectors). Operating mode: ordinary open use. Admission: model proposes key/value or deletion; code checks required fields/kind and writes directly. Input/file/compaction hooks propose and admit by fixed extraction rules, without per-content human veto. Guidance requests brief facts, preferences, useful discoveries and recall before searching. No truth/reference answer oracle is used. Recovery includes later overwrite and intended forget, but this is not a guaranteed durable retraction: `facts.delete(...) || shelfForget(...)` short-circuits the shelf call when the local key exists. Memory specialists should assess this and session-history reconstruction consequences. SRC-1: `.pi/extensions/nuggets.ts`, `src/nuggets/memory.ts`, `src/nuggets/shelf.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Explicit tool gives text and a local-facts snapshot in details; hooks continue the event or append prompt text.
- Later read-back: Session start hydrates default shelf facts; branch reconstruction reads retained tool details; before-agent hook renders local facts; explicit recall reads shelf then local substring matches.
- Delegated visibility: Model receives rendered selected facts or tool-return text, not the entire shelf's JSON metadata; external Pi receives the extension callbacks' return values.
- Selection predicate: First matching preference regex; named read/edit/write path fields; precompaction path capture filters the last twenty assistant tool-use blocks, not the last twenty matching file operations; current session branch; prefix-based injection groups and last ten files; explicit recall key matching and HRR decoding.
- Invalidation or expiry: Overwrites/deletions and session branch replacement alter local state; durable forget can be skipped by short-circuiting; underscore facts are excluded from ordinary injection. Default stores are not isolated per gateway user.
- Activation or effect: Retention and prompt/tool delivery are implemented; model compliance, correct answers and future-action benefit remain unobserved.
- Evidence limits: Pi extension loading/event execution and full host context are external; no live facts or traces were supplied. This record covers integration, not every memory transformation.

> return {
> systemPrompt: event.systemPrompt + injection,
> };
> --- `.pi/extensions/nuggets.ts`

> const existed = facts.delete(params.key) || shelfForget(params.key, nuggetName);
> --- `.pi/extensions/nuggets.ts`

> for (const tc of toolCalls.slice(-20)) {
> const fp = tc.input?.file_path || tc.input?.path;
> if (fp && typeof fp === "string") {
> const basename = fp.split("/").pop() || fp;
> const toolName = tc.name || "";
> if (["edit", "write"].includes(toolName)) {
> facts.set(`edited:${basename}`, fp);
> } else if (toolName === "read") {
> facts.set(`file:${basename}`, fp);
> }
> }
> }
> --- `.pi/extensions/nuggets.ts`

#### RT-RTE-schedule-admission
Label: Schedule request admission

Endpoints: model `schedule` call → shell append of JSONL → polling gateway → [RT-OBJ-cron-jobs](#rt-obj-cron-jobs). Model proposes cron/prompt/one-shot or deletion; extension validates presence, gateway decides admission using fields/default JID; operator can change files/config but has no built-in per-request approval. Operating mode: open requests. Guidance says to schedule reminders/follow-ups and confirm them. No answer oracle checks intended time, recipient or successful creation. Rejection: missing fields/default logged; malformed JSON logged; invalid cron shape simply fails matching. Deletion is the shipped reversal, not an acknowledgement/retry protocol. SRC-1: `.pi/extensions/proactive.ts`, `src/gateway/cron.ts`, `src/gateway/main.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Tool confirms file append success as schedule creation/deletion, before gateway acceptance.
- Later read-back: Gateway polls new request suffixes; accepted jobs persist and reload; list tool reads the full jobs file without per-user filtering.
- Delegated visibility: Gateway gets serialized action/cron/prompt/oneShot, no originating chat ID from this tool; downstream Pi later gets the stored prompt.
- Selection predicate: File growth since startup offset; add requires cron, prompt and request/default JID; remove uses ID globally.
- Invalidation or expiry: Removal by ID; one-shot deletion on emission; existing request bytes are skipped at scheduler startup; no transactional rollback or receipt acknowledgement.
- Activation or effect: Persistent job mutation and deferred execution are wired, not observed; tool confirmation alone does not establish admission.
- Evidence limits: No evidence establishes correct recipients in multi-user use, cron interpretation by a model, or successful delivery.

> const jid = request.jid || this.defaultJid;
> --- `src/gateway/cron.ts`

> this.lastRequestSize = this.getRequestFileSize();
> --- `src/gateway/cron.ts`

#### RT-RTE-proactive-turn
Label: Cron and heartbeat turns

Endpoints: timer or persisted job → synchronous event emitter → per-identifier router queue → Pi → optional send. Code owns eligibility; external model decides what to say and whether to follow the heartbeat request to check memory. Symbolic schedule selection supplies natural-language prompts. Operating modes: recurring/one-shot cron and inactivity heartbeat, not evaluation curricula. No answer oracle judges relevance or completion. SRC-1: `src/gateway/cron.ts`, `src/gateway/heartbeat.ts`, `src/gateway/event-queue.ts`, `src/gateway/router.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Event emission enqueues work; later nonempty Pi text is chunked and sent, except heartbeat suppression.
- Later read-back: Cron consumes retained job prompts; Pi requests continued session context and can use the memory integration. Heartbeat registration itself is in-memory only.
- Delegated visibility: Same Pi session/process path as ordinary messages; heartbeat receives a static request to check memory, cron receives the job prompt without a separate authorization wrapper.
- Selection predicate: Enabled cron matching all five fields, once-per-minute evaluation; heartbeat interval, local quiet hours and inactivity guard. Heartbeat output is suppressed when uppercase text contains `NOTHING` anywhere.
- Invalidation or expiry: One-shot job removed after event push; no durable event queue or restoration after failed delivery. Telegram's HTML-to-plain-text send fallback also applies to proactive responses; an ultimately failed send is not retried by the router. Proactive errors are logged but unlike ordinary errors do not kill the process; process may later expire idle.
- Activation or effect: Timer-to-Pi and response-to-channel paths exist; actual unsolicited memory use and useful follow-up are unobserved.
- Evidence limits: No run establishes timer precision, host clock assumptions, model sentinel compliance or recovery after failed one-shot delivery.

> if (!response || response.toUpperCase().includes("NOTHING")) {
> --- `src/gateway/router.ts`

#### RT-RTE-memory-promotion
Label: Compaction-triggered memory promotion

Endpoints: Pi `session_compact` callback → `promoteFacts(shelf)` → Claude-project `MEMORY.md`. Owner: extension triggers; deterministic writer proposes/adopts threshold-qualified entries. Operating mode: opportunistic maintenance during normal use. Guidance is the source's three-recall rule; selection uses hits, not an answer oracle or human approval. Existing parseable entries are merged by section/key; reconstructed output and atomic replacement are not a general preservation guarantee for free-form prior prose. Rejection: missing Claude project directory or no candidates returns zero; callback suppresses thrown errors. No automatic rollback is supplied. SRC-1: `.pi/extensions/nuggets.ts`, `src/nuggets/promote.ts`, `src/nuggets/memory.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Writer returns newly promoted count; extension discards the result and catches failures.
- Later read-back: External Claude host is the intended reader of written Markdown; no included consumer establishes its loading or effects.
- Delegated visibility: Writer sees the extension's current shelf object and existing recognized Markdown entries; host would receive rendered text, not hit metadata or admission history.
- Selection predicate: Each shelf fact with hits at least three; output location derived from current working directory and home. Ordinary extension recall omits session ID and therefore does not increment library hits.
- Invalidation or expiry: Repeated merge updates values; missing candidates do not remove old promoted facts; no implemented expiry/rollback. Atomic rename concerns replacement, not factual validity or cross-process serialization.
- Activation or effect: File-writing pathway implemented conditionally; actual promotion and external behavioral use unobserved.
- Evidence limits: Live hit data and host reader are unavailable; threshold comments do not demonstrate functioning cross-session promotion through ordinary extension use.

> if (sessionId) {
> const pos = this._tagToPos.get(tag)!;
> --- `src/nuggets/memory.ts`

> const result = shelfRecall(query, nuggetName);
> --- `.pi/extensions/nuggets.ts`

> if ((fact.hits || 0) >= PROMOTE_THRESHOLD) {
> --- `src/nuggets/promote.ts`

### Claims

#### RT-CLM-ingress-control
Label: Transport admission scope

Claimed operation: transport handlers reject non-allowlisted identifiers, but their shared predicate is open when both lists are empty. Source: SRC-1 `src/gateway/config.ts`, with callers in `src/gateway/telegram.ts` and `src/gateway/whatsapp.ts`. Guarantee owner: local transport/config code. Enforcement point: before router handoff. Guarantee strength: invariant of the inspected predicate/caller paths, conditional on identifiers and configured lists. Covered: these incoming text handlers. Alternate paths: cron, direct extension/library calls, host tools and filesystem modification are outside this predicate. Required external contract: channel library supplies authentic chat/JID identity; this is not verified here. Current grants and deployment sandbox are uninspected. This is not a global action-authorization guarantee.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (ALLOWLIST.size === 0 && TELEGRAM_ALLOWLIST.size === 0) return true;
> return ALLOWLIST.has(id) || TELEGRAM_ALLOWLIST.has(id);
> --- `src/gateway/config.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-facts-prompt
Label: Facts in system prompt

Consumer: external Pi/model. Channel: `before_agent_start` appends formatted local facts to `event.systemPrompt`. Force: natural-language context/instruction supply, not guaranteed compliance; preferences can shape requested behavior, file facts provide context. Horizon: current turn, repeated while local facts remain and across sessions through hydration/reconstruction. Actual interpretation/activation remains unobserved. SRC-1: `.pi/extensions/nuggets.ts`; passage in [RT-RTE-memory-context](#rt-rte-memory-context).

#### RT-BAP-scheduled-prompt
Label: Retained job prompt as later request

Consumer: per-recipient Pi/model. Channel: `CronJob.prompt` becomes `event.prompt`, then `rpc.promptAndWait(event.prompt)`. Force: a retained natural-language request entering the same prompt interface as user messages; this is distinct from the symbolic job fields controlling when/where it enters. Horizon: later scheduled turns and restarts while a job persists. Runtime delivery is wired; compliance and benefit unobserved. SRC-1: `src/gateway/cron.ts`, `src/gateway/router.ts`.

> const result = await rpc.promptAndWait(event.prompt);
> --- `src/gateway/router.ts`

## Annotations

none
