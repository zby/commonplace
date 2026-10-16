---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Origin workflow account: explicit single-page rebuild from host-agent confirmation through daemon synthesis, admission and returned receipt."
run-id: AAS-2026-10-15-origin-805d03bc599f-01
reviewed-boundary: "61b462ea6adf019b3e27d3f58ac5a0fe055f76b1"
---

# Origin workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is `/distill rebuild <page-id>` for an existing, active, user-edited but not authored page. It was selected because the shipped skill, MCP wrapper, HTTP handler and shared refresh implementation form a directly connected request-to-return chain. It exposes explicit delegation, model-context selection, rejection and a consequential delivery limit without joining unrelated capabilities. The [boundary](boundary.md) registers SRC-1; the runtime's [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh) supplies the canonical synthesis/admission baseline.

All findings concern implementation or doctrine/design at the frozen revision. No target program, test or provider was executed. This is a conditional implemented workflow, not a successful observed rebuild. Added SRC-1 inspection covers `plugin/skills/distill/SKILL.md` (scope and rebuild instructions), `crates/wenlan-mcp/src/tools.rs` (`distill_impl`), `crates/wenlan-server/src/routes.rs` (foreground provider selection and force branch), `crates/wenlan-core/src/synthesis/distill.rs` (candidate generation and forced refresh), and `crates/wenlan-core/src/post_write/page_update.rs` (ownership staging). Skill text supplies doctrine/design; Rust paths supply implementation evidence.

### Request, consent and delegation

The user names a page to rebuild. The host agent is instructed to confirm destruction of the user's edits, call `distill(target=<page-id>, force=true)`, skip the general cluster-completion flow, and report the daemon response verbatim. That is requested host behavior, not an independently enforced user-consent check: [WF-BAP-rebuild-skill](#wf-bap-rebuild-skill).

MCP supplies only the target and force flag to `/api/distill`; it does not synthesize this page in the host session. The daemon resolves the target, rejects non-page force targets with a hint, and selects the first available provider in foreground order: Anthropic slot, external OpenAI-compatible slot, then on-device slot. Thus foreground rebuild can use a provider different from a background pin. If none is available, the handler returns `status: skipped`, `updated: false` and setup guidance. The caller must configure availability and retry; no host-synthesis fallback is present in this force branch. See [WF-RTE-rebuild-request](#wf-rte-rebuild-request).

### Model handoff and candidate verification

The daemon calls `force_redistill_single`, which enters the shared refresh route with `UserForced`. Before generation it reads a source-revision/incarnation fence, loads the page and refuses a draft. Source IDs come from current page-source links, falling back to the page's stored source list. No sources, orphaned source contents or empty model output yield no-write outcomes rather than invented prose (SRC-1, `crates/wenlan-core/src/synthesis/distill.rs`; [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh)).

The model receives task guidance and numbered, capped source snippets, not the entire host conversation or necessarily complete source documents. Code fixes the supplied context and asks for candidate prose; the provider returns text, not mutation authority. The candidate path strips think tags, processes citation markers, and discards output with zero verified citations or a majority unverified. The runtime record retains the load-bearing gate passage and its lexical, non-semantic limitation. This is open page recompilation, not an answer-key experiment; neither model judgment nor citation overlap supplies an expected-answer oracle.

### Commit, rejection and recovery ownership

A verified candidate reaches the canonical page-write path. For the selected non-authored page, forced mode may replace user-edited prose; it does not clear protection before generating. Revision/incarnation fencing lets a concurrent edit or page recreation defeat the stale candidate. Ordinary machine-write protection differs, as described by [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh). An authored page remains a review-card branch even under force; a force request is not universal permission to overwrite.

On citation rejection, refresh leaves prose unchanged and attempts to persist a blocked reason only against the captured fence. If the page changed, the obsolete discard marker is dropped. A real source change rearms automatic retry; a successful canonical write clears the marker. On provider error, the error propagates without an advance release of edit protection. These are source-level recovery provisions, not demonstrated recovery after process failure (SRC-1, `crates/wenlan-core/src/synthesis/distill.rs`).

> /// never cleared ahead of generation: `user_edited`, `stale_reason`, and any
> /// pending revision card survive a provider failure, a dropped future, and
> /// discarded or unavailable output. Only the UPDATE that lands the new body
> /// releases them, under the source-revision fence read before generation.
> --- `crates/wenlan-core/src/synthesis/distill.rs`

There is no retry loop in the inspected foreground request envelope. The daemon owns preservation and fenced admission; the caller owns a fresh foreground attempt. Scheduler retries are a separate route, [RT-RTE-ambient-work](runtime.md#rt-rte-ambient-work), and do not establish eventual completion of this request.

### What counts as delivered

For a changed page, the retained effect is a canonical page body with citation state, followed by summary maintenance. The selected request returns a receipt, not that body: `status`, `force`, `page_id` and `updated`. MCP pretty-prints the response as tool text, and the skill asks the host to report it verbatim. Later content delivery requires another page/read or recall invocation; recall applies its own scope and selection, [RT-RTE-recall-search](runtime.md#rt-rte-recall-search). A rebuild receipt therefore establishes neither downstream use nor improved answers.

The receipt loses detail from the internal refresh outcome. It exposes `wrote` as `updated` and adds a reason only for a discard. It omits `gated`, `revision_card_id` and `acknowledged`. Consequently `status: ok, updated: false` does not distinguish an authored-page review card, identical output, a fenced-out candidate or unavailable source/output. The traced force response alone cannot let the host resolve those cases or deliver an actionable review-card identifier. Review acceptance remains outside this selected workflow; no automatic acceptance is inferred. SRC-1, `crates/wenlan-server/src/routes.rs`; [WF-RTE-rebuild-request](#wf-rte-rebuild-request).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-rebuild-request
Label: Foreground rebuild request envelope

Distinct from [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh): this record identifies the MCP-to-HTTP request and response envelope, provider selection and information loss, not the contained synthesis/write operation. It is also distinct from [RT-RTE-ambient-work](runtime.md#rt-rte-ambient-work): this is caller-triggered foreground work rather than a scheduler slice. SRC-1, `crates/wenlan-mcp/src/tools.rs`, `crates/wenlan-server/src/routes.rs`.

The external caller proposes a forced page rebuild; MCP forwards target/force, and daemon code resolves scope, selects an available provider and delegates to shared refresh. Mode: explicit open request. The caller can withhold the request; the daemon can skip or reject it, and downstream admission can refuse mutation. The skill asks for human confirmation, but this request handler does not obtain an item-level confirmation token. No answer oracle is used. Proposed replacement guidance and recovery are owned by the delegated refresh route, not by this transport envelope.

- Immediate return: JSON receipt rendered as MCP tool text; unresolved targets instead produce target/hint text, and HTTP errors become tool errors.
- Later read-back: successful delegated writes can be read later through page or recall routes; the returned receipt is not itself retained page prose.
- Delegated visibility: daemon receives target and force; chosen provider receives the shared refresh's selected prompt/snippets, not the full host session.
- Selection predicate: target resolves to a single page; force is true; foreground provider selection takes the first available Anthropic, external compatible or on-device slot.
- Invalidation or expiry: each invocation re-resolves target/provider; the downstream page fence can invalidate a candidate. No automatic foreground retry is implemented in the inspected branch.
- Activation or effect: delegates possible page replacement and returns `outcome.wrote` as `updated`; host receipt consumption and later content use remain unobserved.
- Evidence limits: response omits internal gate/card/acknowledgement fields; source inspection establishes wiring, not confirmed user consent, successful mutation or operational recovery.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let mut response = serde_json::json!({
>     "status": "ok",
>     "force": true,
>     "page_id": page_id,
>     "updated": outcome.wrote,
> });
> --- `crates/wenlan-server/src/routes.rs`

> if !outcome.wrote {
>     if let Some(reason) = outcome.discard_reason {
>         response["reason"] = serde_json::json!(reason);
>     }
> }
> return Ok(Json(response));
> --- `crates/wenlan-server/src/routes.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### WF-BAP-rebuild-skill
Label: Host-agent rebuild instructions

Distinct from [RT-BAP-recall-skill](runtime.md#rt-bap-recall-skill): the consumer is again the external host agent, but the guidance authorizes a destructive rebuild request and prescribes receipt presentation, rather than retrieval judgment. Distinct from [RT-BAP-task-prompts](runtime.md#rt-bap-task-prompts): this text guides the host before the daemon's inference request, not the synthesis provider.

Consumer: host agent running `/distill`. Channel: shipped natural-language skill text. Force: requested confirmation, target/force selection, exclusion of cluster-finishing work and verbatim reporting; not software-enforced consent. Horizon: one invocation, with static instructions reusable across sessions. SRC-1, `plugin/skills/distill/SKILL.md` (doctrine/design); actual host compliance is unobserved.

> - Reserved keyword sequence `rebuild <page-id>` → call
>   `distill(target=<page-id>, force=true)`. This is destructive:
>   user-edited page prose is wiped and regenerated from source memories.
>   Confirms "Rebuild page <id>? Your edits will be wiped, page regenerates
>   from sources." before proceeding. Skip the rest of this skill — single-page rebuild does
>   not produce `pending` clusters; the daemon's response shape is
>   `{"status": "ok", "force": true, "page_id": ..., "updated": true}`.
>   Report verbatim.
> --- `plugin/skills/distill/SKILL.md`

## Annotations

#### On [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh)

Workflow role: delegated model-and-admission stage between the foreground force request and its receipt. The selected path's user confirmation is instructed upstream, while code verification and fencing remain daemon-owned. Completion must be interpreted through `wrote`, not merely a successful function return; the foreground envelope preserves that flag but drops review-card and acknowledgement details. The receipt is terminal delivery for this invocation, not evidence of page-body delivery to the requesting agent.
