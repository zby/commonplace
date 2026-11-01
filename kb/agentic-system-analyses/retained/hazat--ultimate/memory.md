---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Ultimate memory: root memories, landing distillation, selective recall, tally catch-up and chapter handover, with separate context and operational ledgers."
run-id: AAS-2026-11-01-ultimate-f5179584de71-01
source-identity: https://github.com/HazAT/ultimate
reviewed-boundary: "e2b9fa61962f6aecd394dea1c670688fac3ec432"
---

# Ultimate memory report

## Boundary and evidence

Ultimate retains project knowledge as root-scoped text, work history as entries and derived abstracts, and operational state as structured documents. This member includes those surfaces, their writers, branch/read-back consumers, compaction and chapter transitions. It uses SRC-1 at the exact commit in [boundary](boundary.md). The source checkout HEAD was rechecked and its working tree was clean. Direct source reads supply implementation and doctrine/design evidence, not observed operation. No target, tests, model or service was executed.

The supplied runtime orders this account but does not limit inspection. Additional direct inspection covered SRC-1 `extensions/lineage/memory.ts`, `extensions/lineage/catchup.ts`, `extensions/lineage/server.ts` memory/API/reactor/compaction slices, `extensions/lineage/rewind.ts` context/revision/task slice, `extensions/lineage/README.md`, `extensions/recall/server.ts`, `extensions/recall/README.md`, `extensions/classify/server.ts`, `extensions/conversations/summary.ts` input/generation/admission slices, `extensions/dream/seed.ts`, `extensions/dream/DREAM.md`, `agents/ultimate.md`, `extensions/todos/server.ts`, `extensions/goal/server.ts` storage/note/tool slices, `extensions/codemode/server.ts` storage/history/output/summary slices, `lib/compaction.ts` and `server/harness.ts` compaction settings. Files read in slices are not claimed fully audited.

External Pi Durable owns portions of context assembly, compaction scheduling, transactional storage and recovery; its full implementation is not frozen here. Provider weights, TypeSafe internals, production databases, user additions and runtime traces are unavailable. These limits prevent claims about actual faithful recall, durable execution under failure, user compliance, capacity improvement or realized token savings. Static instructions and skills are configuration, not themselves acquired memory; their authority is already described in [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions).

### Coverage inventory

“Direct” means inspected source, not exercised behavior. Each row separates content admission from the mechanism writing bytes. All paths are SRC-1.

| Entry point or operation | Source paths and inspection | Content admission, retained part and later consumer; coverage record or limit |
|---|---|---|
| Onboarding and `remember`; extension API; user forget | Direct: `agents/ultimate.md`, `extensions/lineage/server.ts`, `extensions/lineage/memory.ts` | Model-authored batch, executor caller check and software validation; extension API does not share that caller check; user can delete. [MEM-RTE-memory-edit](#mem-rte-memory-edit). No per-content user approval gate for ordinary remember. |
| Landing event | Direct: `extensions/lineage/server.ts`, `extensions/lineage/memory.ts` | Summary model proposes; normalization and atomic validation admit without user approval. [MEM-RTE-landing-distil](#mem-rte-landing-distil). Raw landing/abstract → changed memory → future brief/read/recall. |
| Memory review and dream passes | Direct doctrine: `extensions/lineage/README.md`, `extensions/dream/DREAM.md`, `agents/ultimate.md` | Proposed ops with reasons, user choice under ordinary policy, Ultimate applies; hands-off goals can substitute Ultimate's decision. [MEM-RTE-review-memory](#mem-rte-review-memory). No observed review report. |
| Root branch/reset, branch fork | Direct memory brief builder; supplied fork wiring: `extensions/lineage/server.ts`, `extensions/lineage/memory.ts` | Code pushes index and 10 landings, not bodies. Root without memory and branch-from-branch are alternatives. [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch), [MEM-RTE-memory-read](#mem-rte-memory-read). |
| `memory` index/full-body tool | Direct: `extensions/lineage/server.ts`, `extensions/lineage/memory.ts` | Agent requests root/slug, receives current snapshot and source breadcrumb. [MEM-RTE-memory-read](#mem-rte-memory-read). Exact slug lookup is not semantic targeting. |
| Recall hook and classifier service | Direct: `extensions/recall/server.ts`, `extensions/classify/server.ts` | Code gating + external probabilistic choice select up to three bodies for standing Ultimate. [MEM-RTE-recall-message](#mem-rte-recall-message). Opaque classifier training/weights; no deployed success evidence. |
| Conversation summary and tally abstract | Direct: `extensions/conversations/summary.ts`, `extensions/lineage/README.md`; supplied root context | Model transforms selected text; stale/failed/disabled results do not update abstract. [MEM-RTE-summary-tally](#mem-rte-summary-tally). Sidebar summaries are not interchangeable with abstracts. |
| Idle-input catch-up | Direct: `extensions/lineage/catchup.ts`, hook in `extensions/lineage/server.ts` | Code chooses other branches' latest state and target commits; no per-note human decision. [MEM-RTE-tally-catchup](#mem-rte-tally-catchup). |
| Stored entries/search, cross-chapter history | Direct local read implementation/declarations: `extensions/codemode/server.ts`; seed guidance `extensions/dream/seed.ts` | Requested fork-aware entries or case-sensitive substring match over entry JSON; output is script-selected/budgeted. [RT-RTE-codemode-tools](runtime.md#rt-rte-codemode-tools), [MEM-OBJ-tally](#mem-obj-tally). Cross-project/chapter dispatch internals not fully traced, so no remote completeness guarantee. |
| Manual/automatic compaction and side chat | Direct local compaction settings/hook; supplied side-chat implementation account | Summary plus recent tail or selected side-chat return. [RT-RTE-context-return](runtime.md#rt-rte-context-return). External default compactor for owned subagents remains opaque; not inferred absent. |
| Go back / optional set-aside summary | Direct task/context slices: `extensions/lineage/rewind.ts`; admission boundaries also documented in `extensions/lineage/README.md` | User chooses context omission and optional summary; final revision guard rejects changed context. [MEM-RTE-rewind-context](#mem-rte-rewind-context). Files, commits and dependents are not rolled back. |
| `store`/`load`, call summaries | Direct: `extensions/codemode/server.ts` | Script supplies JSON, successful completion admits store writes. Derived call line is display/access metadata, not full retained execution payload. [MEM-OBJ-store](#mem-obj-store), [MEM-OBJ-call-summaries](#mem-obj-call-summaries). |
| To-dos and hands-off goals | Direct: `extensions/todos/server.ts`, `extensions/goal/server.ts` | Human actions and checked Ultimate tools; selected open state is pushed as per-input notes. [MEM-RTE-operational-notes](#mem-rte-operational-notes). Goal decisions retain reasons but note delivers count, not decision bodies. |
| Dream prepare/asleep/new chapter | Direct: `extensions/dream/seed.ts`, `extensions/dream/DREAM.md`; supplied user-only switch wiring | Prepared handoff + software-selected memories/open work; user transition gate, then direct document assignment. [MEM-RTE-chapter-seed](#mem-rte-chapter-seed). No summary-model rewrite during seed construction. |
| Other task receipts, messages, automations, plans, file changes and UI | Supplied runtime routes plus bounded source relevance searches | Existing [RT-RTE-browser-input](runtime.md#rt-rte-browser-input), [RT-RTE-subagent-start](runtime.md#rt-rte-subagent-start), [RT-RTE-automation-run](runtime.md#rt-rte-automation-run), [RT-RTE-change-admission](runtime.md#rt-rte-change-admission) cover persistence/return/configuration. Fine-grained message grouping, plan presentation, voice transient injection, cloud backup/reset/restore and all other extension note selectors were not audited here; no exhaustive claim about every context injection, archive lifecycle or opaque external state. Known transient entries are explicitly excluded by local compaction. |

## Core ideas

1. **Small root knowledge, not transplanted transcripts.** A root memory brief gives new root branches a slug index, dates and recent landings. Full bodies remain behind an explicit lookup; the tally remains reachable in storage. Branch forks are a separate path and can inherit a much larger context. [MEM-RTE-memory-read](#mem-rte-memory-read), [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch).
2. **Two different automatic selections.** Landing distillation changes what is retained; recall changes which retained bodies reach a particular standing-agent request. Distillation sees full current memory and a landing/abstract, whereas recall's classifier sees one-line memory descriptions and a capped incoming message. Neither label establishes truth. [MEM-RTE-landing-distil](#mem-rte-landing-distil), [MEM-RTE-recall-message](#mem-rte-recall-message).
3. **Work-state compression is separate from project knowledge.** Abstracts, catch-up notes, compaction and chapter handoff preserve different projections of history. Raw history remains separately addressable; derived representations can omit or truncate information. Retaining it does not ensure the model rereads it. [MEM-RTE-summary-tally](#mem-rte-summary-tally), [MEM-RTE-tally-catchup](#mem-rte-tally-catchup), [MEM-RTE-chapter-seed](#mem-rte-chapter-seed).
4. **Tool permission is not a universal memory-write monopoly.** `remember` checks the standing caller, but the same store also admits automatic distillation, an exposed extension API, user deletion and chapter seed assignment. Authorship, approval and physical persistence differ on these paths. [MEM-RTE-memory-edit](#mem-rte-memory-edit), [MEM-RTE-chapter-seed](#mem-rte-chapter-seed).

## Shared records

### Components

#### MEM-CMP-jev
Label: Jev recall classifier

External TypeSafe service inference is distributed-parametric; weights and storage substrate are not captured. Local request/response JSON is symbolic. It is distinct from the summary/foreground provider integrations in [RT-CMP-provider-models](runtime.md#rt-cmp-provider-models): `classify` makes a direct HTTP request rather than a foreground model tool round. SRC-1: `extensions/classify/server.ts`.

Parameter change during operation: uninspected — provider internals unavailable. Exact version pinned: request names `jev-1.14.0`, but immutable weights are not independently established. Mutable endpoint: base URL is provider-configurable and server response reports its model; alias/version semantics remain opaque. No local update/training mechanism is established. Its choice scores guide [MEM-RTE-recall-message](#mem-rte-recall-message), not knowledge admission or an expected-answer oracle.

> body: JSON.stringify({ model: 'jev-1.14.0', ...request }),
> --- `extensions/classify/server.ts`

### Operative objects

#### MEM-OBJ-memory
Label: Root memory content

Root-scoped `lineage.memory` holds decisions/facts/lessons by slug. Natural-language line and body are interpreted by summary, recall and work models; these are derived knowledge/instruction content, not raw transcripts or provider weights. The substrate is a Pi Durable document in the active chapter's SQLite store, as in [RT-OBJ-agent-doc](runtime.md#rt-obj-agent-doc); distinct identity is this separately defined root document rather than AgentDoc configuration or the conversation entry sequence. Forks initialize it empty and history is latest. Initial content is model-authored under onboarding policy from project inspection and user instructions; later sources include landing text/abstracts and explicit memory edits. Exact deployed provenance is unavailable. SRC-1: `extensions/lineage/memory.ts`, `agents/ultimate.md`.

> /** A root's project memory. A fork starts empty: memories live on roots only. */
> --- `extensions/lineage/memory.ts`

Index, full-body, recall and distiller consumers receive different projections; see [MEM-RTE-memory-read](#mem-rte-memory-read), [MEM-RTE-recall-message](#mem-rte-recall-message). A body may retain a decision's reasons, but no schema requires rationale or criticisms. Sources are optional pointers, not verified entailment. Latest document replacement/deletion is not a per-slug revision ledger. Existing context copies need not update when the root changes.

#### MEM-OBJ-memory-addresses
Label: Memory addresses and provenance metadata

Part of: [MEM-OBJ-memory](#mem-obj-memory)

The symbolic part comprises slug keys, kind, updated timestamp and optional `#conversation/entry` source strings in the same document. Fixed rules validate shape, cap membership and sort the index. It is not a vector index. Bodies and lines retain natural-language consumption even though keyed symbolically. Source validation checks syntax, not referenced entry existence or factual support. Distillation overrides the model's proposed source with its actual landing breadcrumb; manual additions can omit it. SRC-1: `extensions/lineage/memory.ts`. This is a material part, not a duplicate of the supplied broad conversation-state object.

> if (typeof source !== 'string' || !/^#\d+(\/\d+)?$/.test(source))
>       return fail('source must be #<conversation>/<entry>')
> --- `extensions/lineage/memory.ts`

#### MEM-OBJ-tally
Label: Tally and derived abstracts

Root entry sequence plus `lineage.tally` bookkeeping are distinct from AgentDoc configuration in [RT-OBJ-agent-doc](runtime.md#rt-obj-agent-doc), though they share durable storage. Natural-language intents, abstracts, notes, frozen landing state and compaction text are interpreted by models; symbolic entry kinds, anchors, edits, branch IDs and watermarks determine visibility. Raw branch transcripts remain separate from these derived summaries. SRC-1: `extensions/lineage/README.md`, `extensions/lineage/catchup.ts`, `extensions/conversations/summary.ts`.

> Storage stays append-only.
> --- `extensions/lineage/README.md`

An open abstract's anchor is updated by carrier-entry edits rather than an ever-growing model-visible series; a landing freezes its latest state and omits the open anchor. New anchors are used if old ones fell behind a head marker or compaction is running. Later consumers include root forks without memories, explicit entries/search reads, catch-up and landing distillation. Abstract update semantics are distinct from immutable source history and from sidebar titles/summaries. Available raw history does not imply the active context contains superseded anchors.

#### MEM-OBJ-store
Label: Codemode Store

Part of: [RT-OBJ-agent-doc](runtime.md#rt-obj-agent-doc)

This part of broad conversation state is the `codemode.store` document, not AgentDoc's tool/model fields. Symbolic JSON keys/values are passed into a later sandbox; embedded strings can be natural language if the script emits them for model interpretation. Durable substrate: conversation document, `fork: 'asOf'`, `history: 'rewindable'`. A script chooses content; no semantic curation or user per-value approval is required. Later scripts load saved values, but no automatic foreground injection of all stored values is established. [RT-RTE-codemode-tools](runtime.md#rt-rte-codemode-tools) already owns this route. SRC-1: `extensions/codemode/server.ts`.

> // Pi Durable has no result transaction, so this commits separately: a crash can retain writes while reporting the call interrupted.
> --- `extensions/codemode/server.ts`

#### MEM-OBJ-call-summaries
Label: Codemode call display summaries

Derived natural-language call lines plus symbolic effect flags live in SummaryDoc; at most 1000 retained summaries, with older calls falling back to script headers. Raw call arguments/results and script-selected model output are not identical to these lines. Summary model receipts are memoized; failed/unavailable summary leaves the fallback. The inspected consumer purpose is display, with a `Summarized` event carrying line/effect, not a demonstrated subsequent agent memory route. Distinct from Store values and from [RT-RTE-auxiliary-model](runtime.md#rt-rte-auxiliary-model)'s conversation-summary referent. SRC-1: `extensions/codemode/server.ts`.

> for (const old of ids.slice(0, Math.max(0, ids.length - KEPT))) delete doc.calls[old]
> --- `extensions/codemode/server.ts`

#### MEM-OBJ-todos
Label: Project Todos

`todos` holds text/owner/id/timestamps and completion state on conversation 1, in latest-history fork-initial durable storage. Natural-language task text advises Ultimate; symbolic ownership/completion fields determine selection. This is open-work memory, not a learned project claim. Model tool and user actions independently supply/edit membership. Done retention caps at 50 when another item is ticked. Later consumers are user UI, `todo list`, changed-list notes and chapter seed. Distinct logical document from [RT-OBJ-agent-doc](runtime.md#rt-obj-agent-doc). SRC-1: `extensions/todos/server.ts`.

> /** Done to-dos kept; older ones are dropped when another is ticked. */
> --- `extensions/todos/server.ts`

#### MEM-OBJ-goals
Label: Hands-off Goals

`goal` document retains goals, criteria, decisions and ending/waiting state. Latest-history, fork-initial conversation document on conversation 1; text/reasons are natural-language, IDs/states/counters are symbolic. User start grants a goal; Ultimate tools record criteria, decisions and progress under caller checks. Rationale is retained in decisions, but `noteText` supplies goal/criteria, instructions, waiting state and decision count, not full decision reasons. The note's consumer can act under this authorization; no inspected automatic replay of each decision body is established. Distinct from automation run state and [RT-OBJ-agent-doc](runtime.md#rt-obj-agent-doc). SRC-1: `extensions/goal/server.ts`.

> goals: Goal[]
> --- `extensions/goal/server.ts`

#### MEM-OBJ-seed
Label: Dream chapter seed

`seed.json` is a filesystem JSON snapshot, with a separate `dream.seed` application/automation receipt document in the destination chapter. Natural-language parts: memories, three learned lines, handoff, task/question text and saved prompts. Symbolic parts: counts, origin chapter, automation settings, IDs and timestamps. New-chapter consumers differ by part: memories become root memory; handoff/learned lines become waking input; to-dos become list membership; automation configurations become scheduler state. Thus it is neither a whole transcript nor only a prose summary. Distinct from [RT-RTE-context-return](runtime.md#rt-rte-context-return)'s within-conversation compaction and side chat. SRC-1: `extensions/dream/seed.ts`.

> export const writeSeed = (dir: string, seed: Seed) => writeJson(join(dir, 'seed.json'), seed)
> --- `extensions/dream/seed.ts`

### Routes

#### MEM-RTE-memory-edit
Label: Explicit root memory editing

Ultimate proposes ops from onboarding, user instructions or ongoing work. `remember` checks standing conversation identity, resolves root and invokes atomic validation. The user-only forget action deletes through the same validator; `LineageApi.remember` exposes host-extension writes without that tool caller check. These are open operational updates, not a curriculum or truth oracle. Software validates syntax/limits/membership, not whether decisions are warranted. Humans can supply content/corrections and directly delete; ordinary model-authored remember does not require a separate human approval. SRC-1: `agents/ultimate.md`, `extensions/lineage/server.ts`, `extensions/lineage/memory.ts`; closest supplied control is [RT-RTE-change-admission](runtime.md#rt-rte-change-admission), but this is a separate text-admission mechanism.

- Immediate return: batch change summary, or error without the batch's writes.
- Later read-back: new current memory through brief, lookup, recall and next distillation.
- Delegated visibility: branches receive index or requested bodies, not the entire editing exchange by default.
- Selection predicate: listed root, valid ops, existing/nonexisting slug rules and final cap of 150; line ≤120 and body ≤2000 characters.
- Invalidation or expiry: add/update/delete replace latest membership; no TTL; existing context copies are not recalled or erased.
- Activation or effect: store content changes; later delivered natural-language material can guide decisions, but compliance is unobserved.
- Evidence limits: caller check is tool-local; trusted API/seed/automatic paths prevent inferring a universal human or standing-agent monopoly.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> remember: (root, ops, ctx, now) =>
>       host.harness().commit((tx) => applyMemoryOps(tx, root, ops, now), ctx),
> --- `extensions/lineage/server.ts`

> if (standing?.ultimate !== api.conversationId)
> --- `extensions/lineage/server.ts`

Rejected content can be repaired and resubmitted. Earlier content is not restored automatically: recovery is a subsequent edit or available historical/storage recovery outside this validator. Guidance asks for durable decisions/facts/lessons and against remembering live configuration; onboarding nevertheless asks for architecture/how-to-run material, so this is interpreted guidance with a tension, not a consistent enforced content filter.

#### MEM-RTE-landing-distil
Label: Landing distillation into project memory

A `SubmissionLanded` event for a non-root member of a listed tree creates a background root task, deduplicated by permanent per-submission receipt, from newly seen events. The task memoizes summary model, landing input and responses. Input includes landing note, frozen or open submitter abstract and all current memories in full. Model proposes add/update/delete; code normalizes then validates. It overrides non-delete source pointers with the landing breadcrumb. No user per-batch approval. This is distinct from [RT-RTE-change-admission](runtime.md#rt-rte-change-admission): admission of a code landing triggers a second, independent memory admission. SRC-1: `extensions/lineage/memory.ts`, `extensions/lineage/server.ts`.

- Immediate return: background task completion; no summary model means no write.
- Later read-back: changed root text reaches new branch briefs, requested bodies, recall and later distillation inputs.
- Delegated visibility: future workers receive retained projection, not automatically the full landing transcript or distiller reasoning.
- Selection predicate: tree-member non-root landing; full root memory plus one landing/abstract; default requested answer is no ops; output budget 16384 tokens including reasoning.
- Invalidation or expiry: model may delete/update obsolete memories; permanent receipt prevents redispatch for the same submission; rejected batch retries once then leaves notice/no update.
- Activation or effect: automatic trace-fed write to behavior-shaping memory; actual use and improved capacity not observed.
- Evidence limits: summary/landing accuracy is not checked by an answer oracle; deduplication depends on external transaction/task contracts; historical landings are not backfilled at fresh installation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> - When the landing removes or replaces something, delete or rewrite every memory that names it.
> --- `extensions/lineage/memory.ts`

> .map(normalizeMemoryOp)
> --- `extensions/lineage/memory.ts`

Normalization collapses lines, clips long bodies/lines at word boundaries and kebab-cases malformed slugs before strict validation. It can discard content rather than merely reject it. Length/non-stop/parse failures and invalid batches are refused; one retry sees the refusal and prior answer. These are computational admission and repair steps, not evidence-based criticism of a project's proposition. Retained memories can carry reasons if the model writes them; only source breadcrumb is forcibly retained. Model reasoning and refusal are task memo/checkpoint material, not automatically delivered to later work models. `learning`: improved capacity is unestablished; the wired raw-to-derived-to-future-consumer path establishes a trace-fed update mechanism only.

#### MEM-RTE-memory-read
Label: Root memory delivery and lookup

Two complementary endpoints: code-selected brief at root branch/reset; agent-requested `memory` index or slug body. Root resolution uses explicit root, caller tree or only listed root. This augments, rather than duplicates, [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch): its fork/reset progression remains runtime-owned. SRC-1: `extensions/lineage/memory.ts`, `extensions/lineage/server.ts`.

- Immediate return: index or full item to tool caller; branch creation receives brief text before first input.
- Later read-back: durable root memory accumulated by edits/landings reaches later branch/model requests; brief is a snapshot, not a live reference.
- Delegated visibility: new root branch gets all sorted index lines, at most ten recent landing lines and lookup pointers; body/source require lookup; branch-from-branch inherits its selected source context.
- Selection predicate: root-with-memory selects brief; no memory preserves tally path; explicit read slug is exact-key selection, not query similarity or semantic relevance.
- Invalidation or expiry: root update changes future reads, not old brief or already-delivered bodies; no expiry timer.
- Activation or effect: natural-language material enters branch/user-role reset context or tool result; actual obedience and work changes unobserved.
- Evidence limits: 150 item/line/body caps bound stored content; no separate semantic ranking or dynamic token budget in brief builder; external context assembly may further constrain consumption.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const landings = await recentLandings(tx, root, 10)
> --- `extensions/lineage/memory.ts`

The index retains kind/line/date, not body/source; `memoryText` adds source when present and the body. Full source conversations remain separately accessible through explicit entries/search. Metadata and pointers enable navigation, not automatically reason retention at the consumer.

#### MEM-RTE-recall-message
Label: Message-triggered memory recall

Before a standing Ultimate request, code identifies newest user/branch input, context usage and unseen input state. It asks [MEM-CMP-jev](#mem-cmp-jev) which lines specifically fit the sender's intended situation. The hook selects bodies and places a durable user-role entry after input, appending it to the current request too because its cutoff predates that entry. SRC-1: `extensions/recall/server.ts`. No supplied runtime route has this selector identity.

- Immediate return: picked user-role recall message appended to current request, or no modification.
- Later read-back: stored `recall.memories` message enters subsequent requests; restart logic conditionally reappends newest placed recall without making a second classifier decision.
- Delegated visibility: only standing Ultimate is automatically targeted; no automatic equivalent for every child/branch.
- Selection predicate: classify available, usage known and ≥20%, nonempty root memory, new pi.user/board.message input; message capped at 4000 characters plus all memory lines; probability ≥0.25, highest three, excluding recalls in last 30% of context window.
- Invalidation or expiry: last-input marker avoids repeats; recent recall exclusion uses live context, so compacted recalls fade; non-abort service failure/3-second timeout leaves no recall and marks input checked.
- Activation or effect: full line/body text delivered with instruction to act when applicable and acknowledge changed action; this is advisory model interpretation, not enforced action change.
- Evidence limits: classifier scores are not truth or benefit measures; no supplied live request trace; deleted/updated root content does not retract earlier recall messages.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> .slice(0, TOP)
> --- `extensions/recall/server.ts`

> [`${slug} [${item.kind}] — ${item.line}`, item.body].join('\n'),
> --- `extensions/recall/server.ts`

The recalled payload omits `source` and `updated` even though the API describes it as “in full”; stored data keeps slug/line/confidence, not body provenance. This is a concrete consumer-side omission: evidence lineage can remain in root storage while disappearing from the immediate reasoning context. A chip opens current memory for the user, which need not equal the injected historical snapshot. The recall README's tuned precision/recall is an attributed reported-operation claim, not independent execution evidence in this run.

#### MEM-RTE-summary-tally
Label: Conversation summaries into tally state

The conversation summarizer derives activity/sidebar metadata and, for branch replies, a separate abstract. Model receives selected visible user/assistant text, previous summary/abstract, original request/intent where available, and optional delegation. It excludes host pause notes, caps each message (start/end) and recent transcript text. Software checks completed/current answer, pending/revision state, automatic-summary setting and parse/stop conditions before publishing. It calls Trees.abstract for usable branch results. SRC-1: `extensions/conversations/summary.ts`; specializes [RT-RTE-auxiliary-model](runtime.md#rt-rte-auxiliary-model) without redeclaring its general inference operation.

- Immediate return: background task settles with accepted summary/abstract, discarded stale/error record, or no result when no model.
- Later read-back: abstract reaches root tally, later catch-up and landing distillation; sidebar metadata reaches human/browser and conversation listings, not necessarily foreground context.
- Delegated visibility: an abstract is ≤1200 characters, not full worker transcript; raw history remains separately stored.
- Selection predicate: summary task revision and current completed reply; source text only, message cap 2400 characters and recent transcript suffix 12000; branch original intent/request separately capped.
- Invalidation or expiry: superseded/newer work/reset or disabled summaries veto result; accepted abstract updates existing anchor or opens a new one; landing freezes it.
- Activation or effect: trace-derived text becomes later coordination knowledge; correctness/complete preservation unobserved.
- Evidence limits: metadata names such as activity or assessment do not prove evaluation; no expected-answer oracle, human review or model truth guarantee at this admission.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> transcriptText(messages).slice(-12000),
> --- `extensions/conversations/summary.ts`

> const outcome = !result ? 'error' : usable ? 'ready' : 'stale'
> --- `extensions/conversations/summary.ts`

> if (checkpoint.abstract && result.abstract && completed !== undefined) {
> --- `extensions/conversations/summary.ts`

Guidance requests Ask/Diverged/State/Areas/Open and no invented facts. The software's stale/error veto rejects unusable results, not supported-but-wrong summaries. Retained original intent and previous abstract enable continuity but are already filtered inputs; no faithful-transcript guarantee follows.

#### MEM-RTE-tally-catchup
Label: Idle-input catch-up from retained work

Transactional beforeInput runs only for ownerless conversations. Code reads Seen baselines, target Git tip and other branches' tally changes, synthesizes a note, advances baselines and places note with input. No model proposes this note and no human per-note approval occurs. Distinct from branch creation and [RT-RTE-context-return](runtime.md#rt-rte-context-return), though all control model-visible context. SRC-1: `extensions/lineage/catchup.ts`, `extensions/lineage/server.ts`.

- Immediate return: user-role lineage.note before input, or no note when no new material/commits.
- Later read-back: persisted catch-up text participates in later model invocations and inherited tally-position bookkeeping.
- Delegated visibility: excludes own activity and already inherited ancestor prompts; chooses other conversations' current abstracts, fallback prompts, frozen landing state, landings, notes and new root distillation.
- Selection predicate: new entries beyond tally baseline; newest activities prioritized within approximately 6000 estimated tokens; older activities collapse to one-line pointers then count; target commits capped at 30, overlap-first.
- Invalidation or expiry: seen baselines advance atomically; entries behind root head marker are replaced by available distillation; no expiration or semantic repair of old injected note.
- Activation or effect: automatically pushes selected retained work into next model context with request to check relevance; no observed adjustment of work.
- Evidence limits: overlap uses workspace diff or own edit/write calls, not all possible shell effects; not a full semantic conflict detector; mid-run inputs do not establish this idle-placement route.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> export const TALLY_BUDGET = 6000
> --- `extensions/lineage/catchup.ts`

> const pointer = `Earlier, collapsed (read them in full with codemode \`ultimate.entries(${root})\`):`
> --- `extensions/lineage/catchup.ts`

There is no independent request for these particular memories by the foreground model. The code's selector and input trigger constitute push read-back, unlike foreground `memory {read}`. Full content remains reachable by a new explicit read, not by dereferencing an automatic pointer inside the model window.

#### MEM-RTE-review-memory
Label: Review and dream memory proposals

Shipped instructions afford a review branch reading memory, old conversations, code and Git history; dream adds six specialized passes over handoff and operational evidence. Review proposes add/update/delete with evidence and reasons, writes nothing, and returns decisions. Ultimate weighs in; normally branch asks user and Ultimate applies chosen ops. Hands-off goal policy allows Ultimate to decide instead. This procedure is distinct from automatic landing distillation, and uses ordinary [RT-RTE-subagent-start](runtime.md#rt-rte-subagent-start) and branch mechanisms rather than a special optimizer. SRC-1: `extensions/lineage/README.md`, `extensions/dream/DREAM.md`, `agents/ultimate.md`.

- Immediate return: requested journal/change set and decision block, not automatically adopted memory.
- Later read-back: chosen ops persist through remember and reach ordinary memory consumers; rejected proposals need not become project knowledge.
- Delegated visibility: passes get handoff as primary input and are instructed to verify against retained evidence; no evidence of an actual pass execution supplied.
- Selection predicate: user/Ultimate initiates review; dream asks for outdated/contradicted/duplicated/vague memories and unremembered lessons, preserving user memory.
- Invalidation or expiry: chosen deletes/updates withdraw old membership; codified memory stays until its change branch lands; no guaranteed removal from old contexts.
- Activation or effect: afforded evidence-directed editorial correction and instruction/code proposals; implemented tools provide means, not reliable compliance with the protocol.
- Evidence limits: doctrine/design procedure, no review artifact or passing outcome; proposal rejection is distinct from batch schema rejection; no answer oracle established.
- procedure conclusion status: afforded
- operation conclusion status: uninspected

> A codified memory (`retire` on the proposal) stays until its branch lands; then delete or update it with `remember`.
> --- `extensions/dream/DREAM.md`

Rationale is requested in the returned change set/journal, but applying only ops need not transfer all reasons into the memory body. Its retained source transcript can remain readable through entries/search; later rereading is optional. This route affords criticism of text against later evidence but does not alone establish all theory-builder conditions or exercised learning.

#### MEM-RTE-operational-notes
Label: To-do and goal read-back

User actions or Ultimate checked tools write operational documents. Before standing Ultimate input, code pushes changed open to-dos, and pushes open-goal text/criteria/rules on every applicable run. Human start controls goal authorization; model subsequent criteria/decisions/progress are not individually user-approved. Content checks validate types, length and state, not whether tasks are truly complete or decisions correct. SRC-1: `extensions/todos/server.ts`, `extensions/goal/server.ts`. Distinct from [RT-RTE-automation-run](runtime.md#rt-rte-automation-run)'s scheduled child loop.

- Immediate return: action/tool result; later input hook supplies user-role note.
- Later read-back: open retained task/goal state reaches next standing invocation; chapter seed also carries unfinished to-dos, not a wholesale goal-decision replay.
- Delegated visibility: standing-target hooks, not every branch; other projects can request documents; goal note includes decision count rather than all retained reasons.
- Selection predicate: to-dos open and rendered-list key changed; goal first unended goal for standing Ultimate, with reminder-specific instruction when applicable.
- Invalidation or expiry: done/reopen changes selection; oldest completed to-dos drop beyond 50; goal finish/end stops open-goal note; existing historical notes remain stored.
- Activation or effect: advisory task reminders and natural-language hands-off authority; code state controls eligibility but does not enforce every modeled decision.
- Evidence limits: no operation trace; full reminder delivery machinery and all state constraints not audited; retained rationale is not proof it is in each subsequent model request.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if ((seen.key ?? '') === key) return undefined
> --- `extensions/todos/server.ts`

> const goal = await openGoal(tx)
>           if (!goal) return undefined
> --- `extensions/goal/server.ts`

#### MEM-RTE-chapter-seed
Label: Dream seed across chapters

Ultimate proposes prepared learned lines/handoff under dream policy; user-only asleep transition gates chapter change as supplied in [RT-BAP-extension-code](runtime.md#rt-bap-extension-code). `buildSeed` deterministically gathers all roots' memory, unresolved user questions, unfinished to-dos and selected enabled automations/scripts. Same slug across roots chooses greatest updated time, not semantic reconciliation. Destination seed application directly assigns memory, creates operational state and wakes standing Ultimate with handoff/learned lines. SRC-1: `extensions/dream/seed.ts`, `extensions/dream/DREAM.md`.

- Immediate return: prepared card/transition or seed application; wake-up input scheduled once through receipt.
- Later read-back: new chapter's root memory and to-dos feed normal consumers; handoff/learned lines reach new Ultimate invocation; carried eligible automation settings affect future scheduling.
- Delegated visibility: no complete old transcript in new context; wake text points to old chapter entries/search/conversations; user questions become to-dos.
- Selection predicate: all root memories deduplicated by slug/update time; undone to-dos; delivered unanswered user messages; selected enabled triggers; numeric-conversation conditions and unsuitable triggers become recreation tasks.
- Invalidation or expiry: applied receipt prevents repeated document seed; automation-name receipts/key deduplicate re-creation; incompatible old seed is refused with switch-back advice; old chapter remains on disk.
- Activation or effect: selected state installed into fresh chapter, with subsequent model/scheduler consumers; successful handover and preserved behavior unobserved.
- Evidence limits: user transition approval is not independent verification of each carried memory; direct assignment bypasses applyMemoryOps validation and may merge multiple capped roots into more than one-root cap.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (!memories[slug] || memory.updated > memories[slug].updated) memories[slug] = memory
> --- `extensions/dream/seed.ts`

> Object.assign(memory.memories, seed.memories)
> --- `extensions/dream/seed.ts`

This is a counterexample to describing applyMemoryOps as the universal physical write path. It preserves each carried memory's source/timestamp, but adds no new rationale. Learned/handoff content is authored, not generated by `buildSeed`. Human approval and backup/journaled switching are separate from semantic admission of those texts. Old source pointers can still name historical conversations; retrieval guidance does not prove successful cross-chapter resolution or use.

#### MEM-RTE-rewind-context
Label: Go-back context withdrawal

User-only go-back chooses a stored point and optional summary. Task reads current/past context, gathers changed files/commits/dependents, optionally summarizes selected set-aside messages and then checks refusal/revision before appending context edits and note. This is a distinct withdrawal path from [RT-RTE-context-return](runtime.md#rt-rte-context-return)'s compaction/side chat. SRC-1: `extensions/lineage/rewind.ts`, `extensions/lineage/README.md`.

- Immediate return: rewind entry/result or refusal if context changed/admission fails.
- Later read-back: next invocation sees surviving prefix and note, optionally a summary of removed path; stored omitted history remains accessible.
- Delegated visibility: dependent conversations receive display markers and continue independently; their context/effects are not rewound with the caller.
- Selection predicate: user target point, own context entries after it; optional summary serializes set-aside non-system contributions with 60000-character suffix cap.
- Invalidation or expiry: final revision check prevents omitting newer unseen work; roots/busy/compacting/pre-head-marker points refused under documented admission.
- Activation or effect: context suffix withdrawn through edits, not storage deletion; files and commits remain and model must decide whether to undo them.
- Evidence limits: default external context-edit semantics and complete admission implementation not independently audited; no executed rewind proof or effect rollback guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "They're still there; decide whether to keep or undo them."
> --- `extensions/lineage/rewind.ts`

### Claims

#### MEM-CLM-recall-tuning
Label: Reported recall tuning

SRC-1 `extensions/recall/README.md` attributes threshold/question tuning to 55 labeled messages from three chapters, reporting precision 0.77, recall 0.62 and variability across repeated classifier calls. Evidence layer: reported operation in documentation, not a supplied run/causal experiment. This is distinct from [RT-CLM-coding-work](runtime.md#rt-clm-coding-work)'s general product claim. Dataset composition, independent reproduction and attribution are not established by this member.

> Classify answers vary by up to 0.13 between calls, so borderline messages can flip; each input is asked once.
> --- `extensions/recall/README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-memory-guidance
Label: Memory text to future decisions

Consumer: branch model, standing Ultimate, and summary model updating memory. Channels: brief/reset, memory tool output, recalled user-role input, and distillation input. Force: natural-language interpretation and instructions, not a fixed rule compelling an action. Horizon: later invocations within conversation, future branches and seeded chapters. Current index/body delivery differs by route; source/reasons need not accompany it. SRC-1: `extensions/lineage/memory.ts`, `extensions/recall/server.ts`, `extensions/dream/seed.ts`. Distinct from static [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance), sharing the same interpretive consumer class rather than identity of content.

> Recalled from project memory for the message above. Act on each that applies, and say so in one line when it changes what you do:
> --- `extensions/recall/server.ts`

Memory content can influence both later action and the next memory update; delivery and a request to acknowledge are not evidence it actually did so. Symbolic keys/caps/selection operate by software rules, not this advisory force.

## Annotations

#### On [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch)

Memory-specific read-back: root branch brief includes index lines/dates/kinds and ten recent landings, but no body/source. Retained root memories are acquired/changed through use; the brief is a later-consumer snapshot with a tally tip watermark. Root with no memory and branch-from-branch preserve alternative history paths. Full text can be requested via [MEM-RTE-memory-read](#mem-rte-memory-read). Source: SRC-1 `extensions/lineage/memory.ts`; branch/reset evidence is supplied by the annotated record.

#### On [RT-RTE-context-return](runtime.md#rt-rte-context-return)

Local compaction has more inspectable selection than the opaque upstream default alone suggests. Ownerless conversation hook builds source from the current model view with edits applied, intersects entries selected for compaction, excludes transient-marked entries, and requests exact paths/names/errors/breadcrumbs. Standing Ultimate summary appends current project memory brief and asks the summary model not to repeat it. Owned subagents return undefined from this hook, retaining external default compaction. Thus raw selected entries → memoized local summary (+ standing brief when available) → later invocation is a wired trace-fed derived-memory path, separate from project memory updates. SRC-1: `extensions/lineage/server.ts`.

> .filter((entry) => !(entry.data as { transient?: unknown } | undefined)?.transient)
> --- `extensions/lineage/server.ts`

> brief ? `${answer}\n\n${brief.text}` : answer,
> --- `extensions/lineage/server.ts`

Answer reserve/recent-tail/background settings are symbolic model-specific controls; settings merge field-by-field with shipped overrides. Exact replaced range and recent-tail behavior still depend on external compactor. Manual own compaction rejects owned subagents because its separate wake-up would not be the run answer delivered to parent; automatic compaction continues that run. Source: SRC-1 `server/harness.ts`, `extensions/lineage/server.ts`, `lib/compaction.ts`. Summary quality, rationale completeness and observed use remain uninspected. Supplied side-chat return evidence establishes selected-summary injection or discard, not restoration of files or erasure of its durable conversation.

#### On [RT-RTE-subagent-start](runtime.md#rt-rte-subagent-start)

Working-context boundary: default task-only child keeps detailed work outside parent window; explicit fork is the counterexample to universally fresh context. Return/report crosses back, not every tool result. Frame analogy fits selected inputs and return; it breaks at durable child retention, background lifetime and persistent host effects. Raw child transcript remains available as history. No general project-memory write permission follows from retaining a child conversation. Evidence is the supplied record's passages and SRC-1 `extensions/lineage/server.ts` remember executor.

#### On [RT-RTE-codemode-tools](runtime.md#rt-rte-codemode-tools)

Script-selected output is a context filter, not a summary of every nested result. Local text budget uses configured max-output-tokens times four characters, default 10000, while intermediate results stay VM-local unless emitted. Successful store changes commit separately; yield discards pending store but not earlier host effects. Store lineage/fork/history are in [MEM-OBJ-store](#mem-obj-store). Entry APIs can recover pre-reset/compaction history; search is case-sensitive `JSON.stringify(entry).includes(text)`, not embedding retrieval. SRC-1: `extensions/codemode/server.ts`.

> if (JSON.stringify(entry).includes(text)) matches.push(entry)
> --- `extensions/codemode/server.ts`

## Write side

[MEM-RTE-memory-edit](#mem-rte-memory-edit) separates model authorship from caller enforcement and atomic structural checks. Onboarding is instruction-governed acquisition from project reading and the user's words; neither actual content nor human per-item approval is supplied. Subsequent edits are known even though deployed initial content is unknown. Source pointers are optional and syntactic.

[MEM-RTE-landing-distil](#mem-rte-landing-distil) is the clearest automatic trace-fed transformation: merged-work note and abstract plus prior memory produce ops, normalized/validated into durable root text, later exposed by brief/read/recall. Its source is operational mixed text, not solely user instructions or raw model reasoning. It can update/delete and defaults to no ops; it is not unconditional accumulation. The all-or-nothing check is structural. Normalization may truncate a reason; accepted content has no independent warrant check.

[MEM-RTE-summary-tally](#mem-rte-summary-tally) derives bounded coordination text from already selected model-visible history. Rejected/stale results are recorded without replacing live abstract; a later landing freezes accepted state. Compaction produces an alternative checkpoint form (summary plus recent tail and optional memory brief), while go-back can retain a different summary of set-aside history. Neither is identical to the raw stored entries.

[MEM-RTE-review-memory](#mem-rte-review-memory) affords evidence-based cleanup, with rationale in proposals and human choice under normal policy. It is not an enforced gate on landing distillation or ordinary remember. Hands-off authority is an explicit counterexample to universal human approval of proposals. Code/instruction codification follows ordinary change admission; the protocol retains memory until the change lands. No performed codification or exercised self-improvement is inferred.

Withdrawal has multiple horizons: memory deletion affects current root membership; done to-dos leave open selection and eventually bounded history; rewind changes a conversation's active view; compaction substitutes a summary; chapter seed chooses what crosses into the new store. None retroactively removes every old context copy. Seed construction directly assigns carried memories and thus is an alternative admission path, not another call to the strict batch validator. [MEM-RTE-chapter-seed](#mem-rte-chapter-seed).

## Read-back

The retained-content chain must be traced to the actual consumer:

- **Request → lookup → delivery:** foreground `memory` chooses root/exact slug, returns current item with source; codemode entries/search can recover history but only script-selected output reaches the model. This is not unsolicited recall or semantic vector selection.
- **Automatic branch supply:** root memory presence triggers an index/landing brief, replacing root tally at context start. The selector uses identity/recency, not task relevance. Index/body bounds limit storage; branch brief has no independent relevance-token budget. No-memory branches and branch forks retain alternative context paths.
- **Automatic message supply:** recall uses capped sender/message text and all memory lines to select at most three bodies, thresholded and freshness-filtered. Actual delivered payload lacks source/date. Selection asks relevance to action, not correctness. [MEM-RTE-recall-message](#mem-rte-recall-message).
- **Automatic operational supply:** idle catch-up chooses changed tally/Git state within budget; to-do hook chooses changed open list; goal hook chooses open authorization/criteria. These are different predicates and should not be collapsed into one memory relevance engine. [MEM-RTE-tally-catchup](#mem-rte-tally-catchup), [MEM-RTE-operational-notes](#mem-rte-operational-notes).
- **Context replacement and chapter supply:** locally generated compaction and optional rewind/side-chat summaries carry selected derivatives; seed sends handoff/learned text, installs root memory and selects open work. Old chapters remain reachable by requested history APIs rather than fully loaded. [MEM-RTE-rewind-context](#mem-rte-rewind-context), [MEM-RTE-chapter-seed](#mem-rte-chapter-seed), [RT-RTE-context-return](runtime.md#rt-rte-context-return).

All delivered prose has model-interpretive authority unless a symbolic rule separately acts on it. Saved goal/automation configuration can also have fixed-rule authorization/scheduling effects. A retained rationale is not necessarily delivered: memory brief omits body, recall omits source, goal note omits decision reasons, and review adoption need not copy its editorial reasoning. These distinctions prevent inferring critique retention or reflective learning from a storage label.

## Integration issues

1. **No supplied fact requires withdrawal, but local compaction deserves refinement.** [RT-RTE-context-return](runtime.md#rt-rte-context-return) rightly limits the external algorithm; the ownerless hook is independently inspectable and filters current edited view/transient entries, generates summary and appends standing brief. The annotation distinguishes local producer from opaque range-selection/default subagent machinery. Source: SRC-1 `extensions/lineage/server.ts`.
2. **Standing-only write restriction is route-local, not universal.** The supplied runtime already labels it an executor safeguard. [MEM-RTE-memory-edit](#mem-rte-memory-edit), [MEM-RTE-landing-distil](#mem-rte-landing-distil), [MEM-RTE-chapter-seed](#mem-rte-chapter-seed) establish extension API, automatic model admission and direct seed writes. Reconciliation should not expand the tool check into system-wide write ownership. In particular SRC-1 `extensions/dream/seed.ts` falsifies the source comment that every write goes through applyMemoryOps.
3. **“In full” recall is qualified at the consumer.** [MEM-RTE-recall-message](#mem-rte-recall-message) delivers line/body, not source/date; lookup does supply source. SRC-1 `extensions/recall/server.ts`, `extensions/lineage/memory.ts`. This limits immediate evidence lineage, not existence of underlying provenance.
4. **Source documentation drift, not a new behavior claim.** Recall README describes injected-token bookkeeping, but inspected recall uses last/pending plus live-context scanning; quoted tuning numbers remain attributed only. [MEM-CLM-recall-tuning](#mem-clm-recall-tuning), [MEM-RTE-recall-message](#mem-rte-recall-message). SRC-1 `extensions/recall/README.md`, `extensions/recall/server.ts`.
5. **No intended duplicate declarations.** Memory brief/fork, compaction/side chat, generic auxiliary inference, subagent start and codemode execution retain supplied route identity and receive annotations/citations. [MEM-RTE-summary-tally](#mem-rte-summary-tally) adds publication/admission after generic auxiliary inference, not a replacement for [RT-RTE-auxiliary-model](runtime.md#rt-rte-auxiliary-model). New memory/tally/Todos/Goals objects are distinct logical documents from AgentDoc, despite the broad wording of [RT-OBJ-agent-doc](runtime.md#rt-obj-agent-doc); Store is explicitly a part of that state container. Containment wording may need reconciliation, but no semantic supersession is proposed.
6. **Unresolved validation boundary across seed roots.** [MEM-RTE-chapter-seed](#mem-rte-chapter-seed) merges multiple roots by timestamp and directly assigns resulting memory. It does not apply the ordinary 150-item batch cap at this point; reachable merged size and next-edit consequences depend on actual state. No over-cap production seed is claimed. Source: SRC-1 `extensions/dream/seed.ts`, `extensions/lineage/memory.ts`.
7. **Unresolved external/default and less-inspected mechanisms.** Full external compaction/storage/provider behavior, remote history completeness, every extension's prompt injection, backup/restoration lifecycle and deployed memory content remain unestablished. Coverage inventory names these limits; no complete classification of all persistent bytes or every working-context selector is implied. These do not erase the directly traced memory paths.

## Limitations and checks

The frozen repository identity and HEAD were checked against the boundary; git status was clean. Source evidence remained within SRC-1, including additional paths recorded above. The member was checked against its supplied type, worker rules and records contract. Searches of write callers and alternate exposed APIs challenged the strongest tempting claims: standing-only writes, uniform validation, full-provenance recall, always-fresh child contexts and universal human approval. Each is limited at the actual path rather than inferred system-wide.

No live traces, production memory examples or experiments establish activation, summary fidelity, improvement or successful autonomous operation. Doctrine supplies review/dream procedures, not their execution. Provider/model versions and upstream guarantees remain externally bounded. Content validation checks structure, relation syntax and quotation occurrence, not analytical correctness or job acceptance.

Validation: the assigned role-specific commonplace-validate command passed (exit 0): “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” No validation-driven narrowing or withdrawal was required.
