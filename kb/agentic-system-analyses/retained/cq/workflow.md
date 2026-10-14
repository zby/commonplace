---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "CQ workflow account: interactive session reflection, candidate approval, proposal persistence, remote review and later knowledge delivery."
run-id: AAS-2026-10-14-cq-8fb3dc41c334-01
reviewed-boundary: "5765494a3840e5f5a7223c42101f41e85cb9d898"
---

# CQ workflow report

## Workflow account

### Selected workflow and evidence basis

This account follows **interactive `/cq:reflect` with a configured remote store**, from a user's retrospective request through candidate production, user approval, software admission, remote review and later query delivery. Reflection is selected because its shipped command explicitly sequences the candidate handoffs and rejection branches. It is a backstop for missed mid-task proposals, not CQ's preferred ordinary task workflow. The skill prefers presenting a candidate as soon as an insight stabilizes. SRC-1: `sdk/go/prompts/reflect.md`, `sdk/go/prompts/SKILL.md`; [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection).

The trace combines the command's explicitly requested query/propose calls with their shipped implementations and the server's review/retrieval consumers. It does not join unrelated capabilities or claim an executed session. Natural-language steps describe doctrine/design; handler, client, browser and server steps describe implementation. No session history, model output, approval trace or service run was supplied. Successful candidate extraction, safety checking and later reliance remain unobserved. The [boundary](boundary.md) fixes SRC-1 and excludes external host execution and live deployment.

CQ does not delegate to a sub-agent. The foreground host agent owns summarization, candidate reasoning and interpretation; CQ supplies instructions and deterministic storage/transport operations. A later JWT-bearing reviewer is a separate admission principal, not an agent worker selected by CQ. The host's own model calls, task tools and context management remain outside this inspected implementation. [RT-CMP-host-model](runtime.md#rt-cmp-host-model), [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection), [RT-RTE-remote-review](runtime.md#rt-rte-remote-review).

### 1. Request becomes a candidate list

The user invokes `/cq:reflect`; the host agent is instructed to construct dense prose covering errors, resolutions, workarounds, surprising behavior and abandoned approaches. Routine edits and well-documented events are omitted. This selects what the requested summary contains; it does not establish eviction of earlier turns, an isolated context or a durable summary store. The agent then selects generalizable, non-obvious, immediately usable and novel insights from its session. Already proposed insights and retrieved insights already confirmed during the session are excluded. The handoff to candidate review consists of summary/detail/action, domain tags and optional language/framework/pattern fields—not an implemented upload of the entire session. SRC-1: `sdk/go/prompts/reflect.md`; [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection).

> Reflection is agent-led — there is no MCP tool for this step. Using your own reasoning, scan the session for insights worth sharing.
> --- `sdk/go/prompts/reflect.md`

The skill's reference subsection nevertheless says a server returns reflection candidates. That conflicts with the dedicated command and the baseline's inspected MCP registration and Python stub. This trace follows the agent-led command, not the unsupported server-extraction description. It cannot establish what a host actually does when exposed to both descriptions. SRC-1: `sdk/go/prompts/SKILL.md`, `sdk/go/prompts/reflect.md`; [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection).

### 2. Agent screening and user content approval

The agent is instructed to check each candidate for vulnerabilities, impact, biases and edge cases (VIBE√). Clean candidates are shown as-is; soft concerns are flagged; hard findings get original and sanitized versions. Sanitization must cover all affected proposal fields, including tags. A hard finding with no coherent sanitized lesson is excluded before presentation, with the exclusion counted in the final summary. A presented hard-finding candidate defaults to its sanitized version, but the user may explicitly select the original. Thus this policy is not an unconditional prohibition on storing hard-finding content. SRC-1: `sdk/go/prompts/reflect.md`, `sdk/go/prompts/SKILL.md`; [RT-CLM-proposal-approval](runtime.md#rt-clm-proposal-approval).

The user can approve, request edits, skip individual candidates or reject the entire batch. Edits return to field review before proposal. This is per-content human approval in the requested interactive procedure; invoking reflection alone is not approval. Neither user approval nor the model's safety classification supplies a reference answer proving that the lesson is true. The procedure uses open session experience, not a bounded evaluation curriculum. There is no supplied evidence that these reasoning and approval steps occurred.

> N              approve (sanitized version for hard-findings)
> N original     approve original instead (hard-findings only)
> edit N         revise before storing
> skip N         discard
> --- `sdk/go/prompts/reflect.md`

### 3. Approved candidate becomes a storage request

For each approved candidate, the command instructs the agent to query its domains for close matches. The agent—not a semantic-equivalence validator—decides whether a result warrants confirming the same insight, flagging a contradiction or proposing a new unit. The query returns selected knowledge, not an exhaustive novelty certificate. The local-first merge and result limits can omit relevant remote candidates; MCP also drops nonfatal query warning/source metadata. Consequently a returned empty or partial list does not prove the candidate is novel. SRC-1: `sdk/go/prompts/reflect.md`; [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query).

On the new-proposal branch, the host supplies the approved content fields to MCP. The handler parses required strings and nonempty domains, validates extension keys and delegates to the Go client's proposal validation and transport. These software checks can reject shape/bounds violations; they do not attest that user approval, VIBE√ or the novelty check happened. Direct callers and the skill's headless exception remain alternate paths around interactive approval. SRC-1: `cli/mcpserver/propose.go`, `sdk/go/client.go`; [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal), [RT-CLM-proposal-approval](runtime.md#rt-clm-proposal-approval).

With successful remote admission, the authenticated server creates a new unit with its own ID, PRIVATE tier and credential-derived creator, then persists it. The initial pending review state prevents ordinary remote query delivery until approval; PRIVATE tier is not itself the query gate or a confidentiality guarantee. The MCP result returns the created unit to the originating agent. SRC-1: `server/backend/src/cq_server/services/knowledge.py`; [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal), [RT-CLM-approved-query](runtime.md#rt-clm-approved-query).

### 4. Remote review admits or rejects later delivery

The shipped browser loads a pending queue and supplies a card to its reviewer. The card renders domains, summary, detail, action, first-observed time when present, confidence and confirmations. It does not render the originating conversation or the command's VIBE√ classification/original-versus-sanitized presentation. The reflection call shown in the command sends no explicit provenance field for those classifications. Therefore the final reflection summary's provenance annotation is a requested user-facing output, not an established safety artifact received by the remote reviewer. SRC-1: `sdk/go/prompts/reflect.md`, `server/frontend/src/components/ReviewCard.tsx`, `server/frontend/src/pages/ReviewPage.tsx`.

The browser sends a POST containing the chosen unit ID to approve or reject. Its API wrapper attaches the stored bearer token; the route derives reviewer identity from the current-user dependency. The service checks that the unit exists and is pending, then writes status, reviewer and time. This is a second admission decision controlling remote retrieval, distinct from the proposing user's approval of content. The inspected service requires no correctness oracle or textual rationale. A browser affords human judgment, but the API does not establish human presence or reviewer independence. SRC-1: `server/frontend/src/api.ts`, `server/backend/src/cq_server/api/routes/review.py`, `server/backend/src/cq_server/services/reviews.py`; [RT-RTE-remote-review](runtime.md#rt-rte-remote-review).

Rejecting a unit keeps it outside ordinary approved-only knowledge reads. Skipping changes the browser's session-local seen-ID set, not server status; skipped units remain pending. Approval enables later retrieval, but does not change the insight text or establish that the content was tested. [RT-RTE-remote-review](runtime.md#rt-rte-remote-review), [RT-CLM-approved-query](runtime.md#rt-clm-approved-query).

### 5. Delivery has three separate endpoints

1. **Reflection completion:** the host is requested to report proposed/skipped/excluded counts and stored IDs. This ends the user-facing reflection procedure; it does not wait for remote review.
2. **Remote admission completion:** an approve/reject response reports the persisted decision and the browser advances to another card. Approval permits subsequent query selection, not guaranteed selection on every query.
3. **Later knowledge delivery:** a later caller requests matching domains; server review filtering and ranking, local selection and client merging determine what reaches MCP as unit JSON. The host is instructed to verify the delivered action/detail before relying on it, then confirm or flag from experience. Tool delivery is the CQ endpoint; completing that host's application task is not.

SRC-1: `sdk/go/prompts/reflect.md`, `sdk/go/prompts/SKILL.md`, `server/frontend/src/pages/ReviewPage.tsx`; [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query), [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback), [RT-BAP-knowledge-guidance](runtime.md#rt-bap-knowledge-guidance). No supplied trace closes the path from session insight to reviewer approval to later changed behavior or benefit.

### Failure and rejection paths

**Candidate or individual proposal failure.** Unsanitizable candidates are excluded; user-skipped candidates do not proceed to proposal. For a proposal error, the command requests an inline report and continuation with the next candidate rather than aborting the batch. It does not specify an automatic content-repair retry or transactional rollback of earlier successful proposals. This is recovery owned by the foreground agent under instructions, not an executed batch controller. SRC-1: `sdk/go/prompts/reflect.md`.

> **`propose` error** — Report the error inline for that candidate and continue with the next one. Do not abort.
> --- `sdk/go/prompts/reflect.md`

**Remote failure becomes partial success.** Transport/server failure or 401/403 causes the Go client to store locally and return FallbackError; other remote client rejections do not store. MCP returns the local unit alongside a warning, allowing the agent to distinguish local retention from remote publication. A later startup drain may transfer it and delete the local copy without another per-content approval step. Its remote replacement then awaits review, so deletion can interrupt local query availability before remote admission. This is best-effort transfer, not exactly-once replication or a rollback guarantee. SRC-1: `sdk/go/client.go`, `cli/mcpserver/propose.go`; [RT-RTE-local-drain](runtime.md#rt-rte-local-drain).

> return mcp.NewToolResultText(fmt.Sprintf("warning: %s\n%s", fb, data)), nil
> --- `cli/mcpserver/propose.go`

**Review conflict or request failure.** An already-reviewed status yields 409. The browser shows “Already reviewed” and schedules another fetch; other commit errors show a retry message. These paths do not reverse an earlier decision or guarantee atomic single-winner review under concurrency. The separate pre-write check and status write remain the baseline's limit. SRC-1: `server/frontend/src/pages/ReviewPage.tsx`, `server/backend/src/cq_server/api/routes/review.py`; [RT-RTE-remote-review](runtime.md#rt-rte-remote-review).

> if (err instanceof ApiError && err.status === 409) {
>   setConflictMessage("Already reviewed")
>   setTimeout(() => fetchNext(), 1500)
> } else {
>   setError("Something went wrong \u2014 try again")
> }
> --- `server/frontend/src/pages/ReviewPage.tsx`

Direct inspection for this member adds SRC-1 implementation coverage of `server/frontend/src/components/ReviewCard.tsx` and the review wrapper in `server/frontend/src/api.ts`, and rechecks the proposal handler, Go proposal branch, review routes/services and browser commit logic. Full command and skill inspection supplies doctrine/design. These reads establish source-level handoffs only; no target, test, example or service was executed.

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

#### On [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection)

Workflow-specific progression: summary → candidate selection → safety classification → user approve/edit/skip → per-approved-candidate query → propose or feedback → inline result → aggregate summary. Empty sessions bypass presentation/proposal; individual proposal errors are requested to leave the rest of the batch running. Summarization selects content but establishes neither host compaction nor a separate worker frame. The command's user-facing final summary is completion of this procedure, not proof of remote review or later application. SRC-1: `sdk/go/prompts/reflect.md`.

#### On [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal)

Workflow-specific acceptance distinction: the proposing user's approval selects content, software admission validates and persists it, and remote review separately admits later query visibility. The first step is requested, not attested by the MCP request. Local fallback is partial publication success and must not be conflated with accepted remote content. The command's error-continuation instruction is not an all-or-nothing batch transaction. SRC-1: `sdk/go/prompts/reflect.md`, `cli/mcpserver/propose.go`, `sdk/go/client.go`.

#### On [RT-RTE-remote-review](runtime.md#rt-rte-remote-review)

Workflow-specific reviewer context: the card shows the retained lesson and selected evidence fields, not session history or VIBE√ provenance. The browser's skip decision changes only its seen-ID set; reject changes server retrieval eligibility. Conflict recovery fetches another card rather than restoring a prior pending state. Source-level rendering and handlers afford review but establish neither actual reviewer judgment nor content verification. SRC-1: `server/frontend/src/components/ReviewCard.tsx`, `server/frontend/src/pages/ReviewPage.tsx`, `server/frontend/src/api.ts`.

#### On [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query)

Workflow-specific delivery distinction: the near-duplicate check is a requested use of a limited retrieval result, not a novelty oracle. A later approved unit still competes under selectors/rankers and local-first merge. Returning its JSON completes CQ delivery; application of the action and confirmation from actual experience remain separate host-owned steps. SRC-1: `sdk/go/prompts/reflect.md`, `sdk/go/prompts/SKILL.md`.
