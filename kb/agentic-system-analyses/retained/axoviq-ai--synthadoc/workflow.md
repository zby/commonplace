---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Synthadoc workflow account: interactive content-health discovery, proposed structural repair, confirmation, rescan, rollback and streamed delivery."
run-id: AAS-2026-10-15-synthadoc-a3cae9152fff-01
reviewed-boundary: b80d9388a3013e8051baf2854c7250942c46e91a
---

# Synthadoc workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the normal text-provider **content-health resolver**: a streamed request to repair flagged active wiki pages. It was selected because one shipped workflow joins discovery, page reading, model-generated edits, client veto, persistent writes, post-write checking and explicit recovery. It does not require joining unrelated capabilities into a hypothetical agent run. The concrete route is [WF-RTE-content-health](#wf-rte-content-health), a specialized part of [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop).

The evidence is implementation and shipped guidance under SRC-1 at the revision fixed by [the boundary](boundary.md). No workflow, provider, client or target test was executed. Consequently this account establishes wired coordination and recovery branches, not a completed repair, factual preservation or an authenticated human review. Added source coverage includes the resolver's normal and CLI-provider implementations, its content-health tools, the heuristic scanner, ActionAgent routing/delivery, confirmation helper, registry wrappers and loop dispatch (SRC-1, `synthadoc/agents/workflows/content_health_resolver.py`, `synthadoc/agents/workflows/tools/content_health_tools.py`, `synthadoc/agents/content_health_scanner.py`, `synthadoc/agents/action_agent.py`, `synthadoc/agents/workflows/_tools.py`, `synthadoc/agents/workflows/_base.py`, `synthadoc/agents/workflows/_loop.py`).

### Request and delegation

A request such as “Run content health resolver” matches workflow routing before general model intent extraction. ActionAgent creates a WorkflowContext carrying a session ID, wiki store, audit database, queue, confirmation registries and cache hooks. For a normal text provider it builds the workflow's guarded callable registry, system prompt and initial message, then runs the model/tool loop in a background task. This is delegation to a completion model for step selection and rewriting, followed by Python dispatch; it is not delegation of arbitrary filesystem authority through the registry (SRC-1, `synthadoc/agents/action_agent.py`; [RT-OBJ-workflow-protocol](runtime.md#rt-obj-workflow-protocol)).

Before that loop, Python pre-discovers active non-system pages carrying stored content-health issues. It supplies their exact slugs in the initial message and seeds a closure-held discovery set. The discovery tool returns issue details for active flagged pages sorted by severity and issue count; its wrapper verifies that returned pages remain readable. This discovery mostly selects stored findings rather than running a fresh content scan. The model is told to notify the client, read each selected page, compose a structural repair and request approval. The page-read handoff supplies the full Markdown body, title, slug and stored issues (SRC-1, `synthadoc/agents/workflows/content_health_resolver.py`, `synthadoc/agents/workflows/tools/content_health_tools.py`).

The model receives accumulating tool results and the fixed workflow guidance, not the full external raw-source corpus. The instruction to preserve facts is a requested editing constraint, not a verified semantic property. A successful read adds the slug to a set; it does not bind subsequent replacement text to that version or prove that text was derived faithfully. The loop's current messages are not themselves evidence of cross-run memory ([RT-BAP-workflow-guidance](runtime.md#rt-bap-workflow-guidance); SRC-1, `synthadoc/agents/workflows/content_health_resolver.py`, `synthadoc/agents/workflows/_loop.py`).

### Approval, checking and persistent effects

The normal proposed-edit path asks the model to show BEFORE/AFTER sections to the client and then call the write tool. Python enforces a confirmation gate around that tool even if the model omits its explicit confirmation call. Content-health configures per-call gate reset. A session-keyed confirmation response opens the gate; timeout or failure to send the confirmation event returns false. The implementation waits 300 seconds, although the workflow prompt says 120. The gate assures an accepted client response on this registered path, not that a human authored it, reviewed all replacement text or approved exactly the subsequently submitted bytes ([RT-CLM-confirm-scope](runtime.md#rt-clm-confirm-scope); SRC-1, `synthadoc/agents/workflows/_tools.py`, `synthadoc/agents/workflows/_base.py`, `synthadoc/agents/workflows/content_health_resolver.py`).

After approval and read/discovery guards, the helper snapshots the current page body, records the newest snapshot ID, replaces the body, records fix metadata, rescans the proposed text and writes the page. It then bumps the cache epoch when supplied. The scanner checks duplicate headings, empty/thin sections, fence parity, misplaced H1 headings and list indentation. It has no expected factual answer. Crucially, remaining issues update metadata and the returned count; they do **not** reject or roll back the proposed body. Thus “success” means the helper reached its write/return branch, not that every issue disappeared or every fact survived (SRC-1, `synthadoc/agents/workflows/tools/content_health_tools.py`, `synthadoc/agents/content_health_scanner.py`).

### Rejection, failure and recovery

Three distinct mechanisms must not be conflated:

- **Client veto:** a declined fallback confirmation returns cancellation before invoking the write helper. In the explicit-confirm sequence, the prompt tells the model to skip a declined page; a subsequent write attempt encounters the still-closed wrapper and asks again. Declining one request is not a permanent authorization ban on that slug (SRC-1, `synthadoc/agents/workflows/_base.py`, `synthadoc/agents/workflows/content_health_resolver.py`).
- **Tool rejection:** writes require a prior successful content read; a nonempty discovery set also constrains the target slug. A failed read tells the model to skip that page. The nonempty-set condition matters: the code does not enforce universal membership when discovery found nothing. These checks do not validate the rewrite's meaning (SRC-1, `synthadoc/agents/workflows/content_health_resolver.py`).
- **Post-write recovery:** a later “roll back <slug>” request can restore the snapshot referenced by the page's fix record. The helper resolves the stored stable ID to a current index; if not found it falls back to the stored index. It returns an error if the selected snapshot has no content. Otherwise it restores the body, clears the fix record, rescans and writes. This is an explicit compensating write, not an automatic all-pages transaction or a guarantee against intervening edits (SRC-1, `synthadoc/agents/workflows/tools/content_health_tools.py`).

The workflow also exposes a separate dismissal tool. Shipped guidance requests notification before dismissing issues that need new factual prose; the helper clears stored issue flags and records a reason without changing the body or making a snapshot. Dismissal is not in the resolver's gated write set and has no corresponding discovery/read guards in its registration. Therefore the per-page content-replacement approval claim cannot be extended to all metadata changes (SRC-1, `synthadoc/agents/workflows/content_health_resolver.py`, `synthadoc/agents/workflows/tools/content_health_tools.py`).

Loop-level recovery is bounded: malformed tool attempts receive two corrective retries; unknown names and invalid arguments become tool results; the resolver budgets 200 tool attempts. Budget exhaustion emits an incomplete-work message, not rollback. ActionAgent surfaces normal-loop exceptions as user-visible error text. Existing effects can remain when the workflow stops ([RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop); SRC-1, `synthadoc/agents/workflows/_loop.py`, `synthadoc/agents/action_agent.py`).

### Delivery and alternate execution

Ordinary plain text ends the loop. The prompt asks for a final inventory of fixed, dismissed and skipped pages, but Python does not compare that inventory against an independently verified task ledger before termination. The loop streams token chunks and emits an internal final_text event. ActionAgent consumes that event and emits a noncacheable done event with hints instead of duplicating the text. An incomplete-work hint can start another invocation; it is not an automatically resumed durable continuation. Persistent delivery is the page/fix-record write; conversational delivery is the streamed text and done event. Neither transport completion nor a “Complete” heading proves successful repair of the entire discovered set (SRC-1, `synthadoc/agents/workflows/_loop.py`, `synthadoc/agents/action_agent.py`, `synthadoc/agents/workflows/content_health_resolver.py`).

Coding-tool providers take a distinct Python-driven implementation rather than this JSON loop. The resolver declares support, gathers flagged pages in Python, asks an opening confirmation, calls the provider for a rewrite and shows only 400-character before/after excerpts before approval and a direct helper call. Its list/rollback intents bypass rewrite generation. Those implementation branches were read, but provider return compatibility and successful execution were not established here. They do not inherit normal-registry read-set enforcement or establish complete diff review; external child-agent effects remain bounded by the limits in [RT-RTE-provider-delegation](runtime.md#rt-rte-provider-delegation) (SRC-1, `synthadoc/agents/workflows/content_health_resolver.py`, `synthadoc/agents/action_agent.py`).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-content-health
Label: Interactive content-health repair

Part of: [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop)

This record identifies the content-health specialization of the supplied generic interactive loop, not a second identity for its protocol, provider or confirmation mechanism. Endpoints are a streamed maintenance request and flagged active wiki pages → model-directed discovery/read/proposal → registered approval/write tools → persisted body and issue/fix metadata → streamed result. Python owns registry execution, guard state, scanning, persistence and termination; the model proposes edits and normally selects the next tool. The caller supplies a request; client confirmation can veto a gated replacement. Whether that client is human is unresolved. The operating mode is open maintenance, triggered by stored page issues and a request, not an experiment or reference-answer curriculum. There is no expected-answer oracle in the inspected scanner or helper (SRC-1, `synthadoc/agents/workflows/content_health_resolver.py`, `synthadoc/agents/workflows/tools/content_health_tools.py`, `synthadoc/agents/content_health_scanner.py`).

Guidance requests structural-only rewriting, per-page reading and approval, skip on rejection, and reporting or dismissal when factual expansion would be necessary. The executable guards cover prior reads, conditional discovery membership and accepted confirmation, not semantic preservation. Persistent products are Markdown bodies, issue lists, fix records and audit snapshots; shipped workflow guidance is not revised by this route. Explicit rollback is available subject to snapshot resolution; scan findings do not themselves block admission. No claim that arbitrary repaired page content is a formulated explanatory theory is made.

- Immediate return: Progress, confirmation and token events, followed by client done metadata on normal final-text termination; tools return structured outcomes to the current loop.
- Later read-back: Page reads and later eligible queries can reload repaired content; list/rollback tools reload fix metadata and snapshots on a later request. Actual later use is unobserved.
- Delegated visibility: Model receives exact pre-discovered slugs, fixed guidance, issue records, complete bodies returned by page reads and accumulated tool results. Client review text is model-supplied or wrapper-generated, not necessarily the complete submitted replacement.
- Selection predicate: Request routes to this workflow; active status plus stored issue flags select pages; severity/count sort discovery; parsed tool names choose functions; read/discovery/confirmation checks constrain replacement.
- Invalidation or expiry: Per-loop read/discovery sets disappear with the invocation; the gate resets after a gated call returns normally; confirmation expires after 300 seconds. Writes bump epoch when configured. Later edits or snapshot retention can affect rollback.
- Activation or effect: Implemented helper writes replace page content and issue/fix metadata, with pre-write body snapshots. Code wires later loading; observed model reliance or improved answers is unestablished.
- Evidence limits: Source inspection only; no observed workflow, verified factual preservation, independently authenticated approval or end-to-end client delivery. Rescan measures structural heuristics, not truth, and does not veto remaining issues.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Minimum implementation passages establish the consequential distinction between requested constraints, admission and post-write checks (SRC-1):

> 2. NEVER modify factual content — only fix structural/formatting issues.
> --- `synthadoc/agents/workflows/content_health_resolver.py`

> if slug not in read_slugs:
> --- `synthadoc/agents/workflows/content_health_resolver.py`

> if found_slugs and slug not in found_slugs:
> --- `synthadoc/agents/workflows/content_health_resolver.py:457-465`

The gate enforcement passage is retained in [RT-CLM-confirm-scope](runtime.md#rt-clm-confirm-scope); per-call reset is retained in [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop).

> # Re-scan to verify and update the stored issue list.
> remaining = scan_page(slug, content)
> page.content_health_issues = [asdict(i) for i in remaining]
>
> ctx.store.write_page(slug, page)
> --- `synthadoc/agents/workflows/tools/content_health_tools.py`

Recovery uses stored identity with a positional fallback, not unconditional restoration of an immutable reference:

> resolved_index = next(
>     (s["index"] for s in snapshots if s.get("id") == stored_snapshot_id),
>     stored_snapshot_index,  # fallback to stored index if id not found
> )
> --- `synthadoc/agents/workflows/tools/content_health_tools.py`

Terminal output is a control signal rather than an acceptance test:

> # Plain-text response — stream as token chunks, then emit final_text.
> --- `synthadoc/agents/workflows/_loop.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

none
