---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Company Brain's manually triggered research round: planning, isolated draft turns, review and explicit Slack delivery."
run-id: AAS-2026-10-14-company-brain-30a9e8cfaeca-01
reviewed-boundary: ef8a45ef3aed97b32599c7d8007edefab6d14e9a
---

# Company Brain workflow report

## Workflow account

This account selects the operator research round because it exposes an explicit plan → concurrent agent turns → retained drafts → separate review/send sequence. It traces the shipped agent-method boundary, not a hypothetical Slack request stitched to unrelated tools. The baseline is [RT-RTE-research-draft](runtime.md#rt-rte-research-draft). SRC-1 implementation establishes the handoffs below; no observed execution establishes research quality, actual reviewer decisions or successful Slack delivery. The frozen source and remote-service limits remain those of [boundary](boundary.md#boundary-and-evidence).

### Request and planning

The operator supplies optional free-text steering, target/person limits and a force flag. `enqueueAutoResearchRun` schedules the callback at delay zero; this returns before the research turns finish. `runAutoResearch` refuses and cancels cron-shaped callbacks left from the retired daily automation. This is a manually triggered round, despite the source-native “auto-research” name. Source comments describe an admin observatory trigger; this account does not establish an HTTP authorization gate or actual console interaction. SRC-1, `src/brain/turn/agent.ts`, `src/brain/auto-research/run.ts`.

> await this.schedule(0, AUTO_RESEARCH_CALLBACK, payload)
> --- `src/brain/turn/agent.ts`

The Durable Object orchestrator acquires an organization-local lease, captures the memory reset epoch, loads organization/Slack context and a recipient roster, and reads previous sent and pending draft bodies. An already-held lease suppresses a normal second trigger; force can replace it. The lease has a 15-minute TTL, a five-minute heartbeat during draft batches, and an owner token that guards renewal, progress and release. This coordinates local work rather than guaranteeing remote effect rollback. SRC-1, `src/brain/auto-research/run.ts`.

`derivePlan` delegates a structured proposal to the default triage model using company context, profile context, up to 40 topic/project/customer labels, roster, operator direction and prior notes. It requests a focus, external targets and recipient-specific angles. Prior sent and pending bodies are each limited to 20 in storage queries; the planner sees whitespace-normalized heads capped at 240 characters. Therefore “never repeat” is model guidance over partial history, not an exhaustive duplicate check. If company context, profile and vocabulary are all empty, planning returns `no_context`; generation/parsing failures return `failed`. Software removes empty target labels and recipient IDs absent from the roster. Schema and identity checks do not verify relevance or factual accuracy. SRC-1, `src/brain/auto-research/plan.ts`, `src/brain/auto-research/store.ts`; model selection follows [RT-CMP-triage-model](runtime.md#rt-cmp-triage-model).

> const recipient = bySlackId.get(p.slackUserId)
> return recipient ? [{ recipient, angle: p.angle }] : []
> --- `src/brain/auto-research/plan.ts`

### Delegation and draft return

The host builds person jobs first, opening the recipient's DM channel without posting a note. Channel jobs follow. Defaults cap the round at two people and three targets; caller overrides can change these limits. In an unsteered round, ranked watch targets can fill unused target slots. Each batch runs up to six jobs with `Promise.all`; person-first ordering is job construction, not a promise that person jobs finish first. Each job receives the organization, selected target/person and angle, common focus and steering, snapshots of prior sent/pending notes, Slack context and environment. Siblings do not receive each other's freshly completed drafts: shared history was loaded before the batch. Prompt requests for different note shapes therefore do not establish cross-sibling coordination. SRC-1, `src/brain/auto-research/run.ts`, `src/brain/auto-research/draft.ts`.

`runDraft` invokes a full `computeTurn` with an empty thread transcript. A person draft uses that recipient's personal connections and DM memory scope; a channel draft uses organization-shared connections and shared scope. Both set the actor read-only flag, `scheduledRun: true`, medium effort and `ephemeral: true`. The job prompt asks for investigation through connected apps and web, one concrete finding, a short message and a separate `SOURCES:` section; it permits `NOTHING_NEW` instead. Those requests are not proof of investigation or compliance. The read-only flags are scoped application controls, not a global effect guarantee: the alternate tool-path limits in [RT-RTE-sandbox-work](runtime.md#rt-rte-sandbox-work) and [RT-RTE-direct-mcp](runtime.md#rt-rte-direct-mcp) still apply. SRC-1, `src/brain/auto-research/draft.ts`.

The independent turn is a working-context boundary: selected inputs enter the draft frame; the orchestrator receives a draft result rather than the entire conversation. Ephemeral mode avoids the enclosing thread-investigation persistence described in the baseline. The returned tool trace is transformed into a review trail: public web URLs, at most eight cited source lines, and at most twelve internal tool/argument labels. Internal output excerpts are retained only for shared-channel drafts and capped at 240 characters; DM drafts omit those excerpts. This does not establish that the resulting body contains no private information. SRC-1, `src/brain/auto-research/draft.ts`; [RT-RTE-research-draft](runtime.md#rt-rte-research-draft).

### Verification and retention

The host drops noncompleted turns, replies containing `NOTHING_NEW`, and empty/placeholder bodies. It splits the model's citations from the message, strips scaffolding and normalizes house style. It flags bodies over 140 words and traces without an evidence-producing tool, but retains those drafts for review. Thus the requested under-80-word limit and investigation requirement are not hard acceptance gates. There is no expected-answer/reference-outcome oracle here; the reviewer receives evidence aids and warnings, not a machine-verified factual answer. SRC-1, `src/brain/auto-research/draft.ts`.

> if (!trace.some((entry) => toolProducesEvidence(entry.tool)))
> flags.push("no tool evidence behind this, it may be riffing from memory")
> --- `src/brain/auto-research/draft.ts`

Each settled draft is inserted immediately only if the captured reset epoch is still current and the lease still belongs to this run and has not expired. Otherwise it is discarded as ownership lost. Job exceptions are logged and do not stop siblings; the orchestrator clears heartbeat timers and releases only its own lease in cleanup. A reset can invalidate in-flight work before it enters the queue. These are admission guards on draft storage, not a replay/checkpoint protocol that resumes interrupted agent work. An operator can start another round after lease expiry or force replacement. SRC-1, `src/brain/auto-research/run.ts`.

> isBrainMemoryResetEpochCurrent(agent, resetEpoch) &&
> holdsAutoResearchLease(agent, lease)
> --- `src/brain/auto-research/run.ts`

A stored draft is not delivered. Agent methods expose list, edit, dismiss and explicit send operations. Editing accepts a nonempty trimmed body only while pending, and records an edit timestamp without regenerating source evidence; dismissal changes status and excludes the draft from sent/pending history. Withholding send is the human veto over publication. Initiating the research round is not per-draft approval. This establishes software affordances and the intended reviewer role, not reviewer diligence or a complete access-control audit. SRC-1, `src/brain/turn/agent.ts`, `src/brain/auto-research/store.ts`.

### Delivery and failure recovery

The send operation rechecks entitlement, workspace existence and organization binding before resolving the destination. DM channels are reopened for the stored recipient; channel drafts follow the current home channel, falling back to the stored channel. The resolved destination can therefore differ from the draft's review-time label. It claims the pending row as `sending`, posts only the stored body with the draft UUID as Slack's `client_msg_id`, and on an accepted Slack response records `sent`, Slack timestamp and actual channel. Only then can eligible target labels earn watchlist entries. Source/citation metadata is not part of the posted body. SRC-1, `src/brain/auto-research/send.ts`, `src/brain/slack/client.ts`, `src/brain/auto-research/store.ts`; see [WF-RTE-draft-delivery](#wf-rte-draft-delivery).

A failed post result releases the claim to `draft`, permitting a later explicit retry. A distinct crash path is not fully recovered by the inspected sender: although the store helper can retake a `sending` claim after two minutes, the send entry point rejects every status other than `draft` before reaching that helper. Therefore the helper's stale-claim affordance cannot by itself establish recovery through `sendAutoResearchDraft`. The UUID request supports intended Slack deduplication, but no remote evidence proves exactly-once publication after a lost response. SRC-1, `src/brain/auto-research/send.ts`, `src/brain/auto-research/store.ts`, `src/brain/slack/client.ts`.

**Added source coverage:** complete reads of SRC-1 `src/brain/auto-research/{run,plan,draft,send,store}.ts`; bounded passages of `src/brain/turn/agent.ts` covering research enqueue/run/list/edit/dismiss/send and `src/brain/slack/client.ts` covering idempotent posting. Searches traced named research/send symbols in `src/` and `web/`. All findings are implementation or embedded design guidance, not observed runs. Detailed console authorization, recipient-roster construction, watchlist ranking internals and outcome-reading behavior remain uninspected and support no further conclusions here.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-draft-delivery
Label: Research draft delivery

Part of: [RT-RTE-research-draft](runtime.md#rt-rte-research-draft)

This is the delivery/retry segment of the supplied research-round route, not a duplicate of its planning and drafting identity. Endpoints/progression: explicit draft-ID send request → entitlement/workspace/destination checks → SQL claim → Slack post → SQL finalization/watchlist update. Owner: reviewer selects the retained production output; software admits and posts; Slack determines external acceptance. Trigger: separate send request. Proposed change: publish the stored, possibly human-edited body and mark the retained row sent. Rejection: missing/nonpending draft, entitlement, workspace mismatch, absent destination or failed Slack result. Recovery: failed result releases the claim; crashes leaving `sending` are not recovered by this entry point. Guidance and persistence: draft prompts and human edits shaped the body; body/status/timestamp/channel persist. Operating mode: open operator-reviewed publication, not an experiment or curriculum. No expected-answer oracle; delivery acceptance is not factual verification. Human can edit, dismiss or withhold send before admission. No general rollback of a published message is established by these files.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: success with Slack timestamp/channel, or a named failure result.
- Later read-back: sent body enters later planning/drafting history; actual channel and timestamp remain on the row; eligible sent targets can enter later watchlist backfill.
- Delegated visibility: Slack receives the body converted to mrkdwn, channel and stable draft UUID; review-only sources and flags are not sent.
- Selection predicate: explicit draft ID, pending status, allowed entitlement, workspace bound to the organization and a resolvable current destination.
- Invalidation or expiry: reset can delete drafts; dismissal excludes pending admission; stale claim threshold exists in the helper but the caller rejects sending rows before that helper.
- Activation or effect: local wiring posts a Slack message and finalizes a sent record after a successful response; deployed effects remain unobserved.
- Evidence limits: Slack deduplication and delivery semantics are external; source guards do not prove exactly-once delivery, factual quality or authenticated reviewer behavior.

Evidence: SRC-1, `src/brain/auto-research/send.ts`, `src/brain/auto-research/store.ts`, `src/brain/slack/client.ts`.

> if (existing.status !== "draft")
> return { ok: false, error: `draft_already_${existing.status}` }
> --- `src/brain/auto-research/send.ts`

> if (draft.status !== "draft" && !stale) return null
> --- `src/brain/auto-research/store.ts`

> if (!res.ok) {
> releaseAutoResearchDraft(agent, draftId)
> --- `src/brain/auto-research/send.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-research-draft](runtime.md#rt-rte-research-draft)

Workflow-specific delegation: host planning selects jobs, then each independent compute turn receives common steering/history plus a recipient- or target-specific frame. The host gathers transformed draft text and a bounded review trail, not full sibling transcripts. Batch concurrency does not supply siblings' new drafts to each other. Verification is layered: schema/roster selection, terminal/empty-output rejection, advisory evidence/length flags, reset/lease storage admission, and human publication choice. Recovery differs by phase: planning failure ends the round; individual job failure does not halt siblings; lost ownership discards storage; failed delivery releases a claim, while interrupted sending has the caller/helper mismatch detailed in [WF-RTE-draft-delivery](#wf-rte-draft-delivery). A stored draft and a successful enqueue acknowledgment are both intermediate results, not delivery.
