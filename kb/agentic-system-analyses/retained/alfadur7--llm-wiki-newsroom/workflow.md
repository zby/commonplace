---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "llm-wiki-newsroom workflow: batch source ingestion through shared-state integration, qualitative rejection, repair and delivery."
run-id: AAS-2026-11-08-llm-wiki-newsroom-ea04687a5ff6-01
reviewed-boundary: "8e209cab483da544852d7213f0e25291d06d8a88"
---

# llm-wiki-newsroom workflow report

## Workflow account

### Selection and evidence boundary

This account selects folder ingestion with at least three genuinely new sources. It is representative because it connects the product's raw-to-wiki transformation to parallel authorship, serial shared-state integration, independent review and final reporting in one shipped command. It expands [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), not a separate workflow assembled from unrelated capabilities. Its coordination is a natural-language protocol executed by an external agent host, not a repository-implemented scheduler. No invocation trace was inspected and no target execution was performed; successful compliance and quality remain unobserved.

Additional SRC-1 inspection covered `.claude/commands/wiki-ingest.md`, `.claude/agents/reporter.md`, `.claude/agents/desk.md`, the escalation section of `.claude/agents/README.md`, the human gate in `CLAUDE.md`, and `_claim_id` in `tools/_build/contradictions.py`. The first five supply doctrine/design; the last supplies implementation and its explanatory comments. All refer to the frozen revision, not another source.

### Request, selection and author handoff

The operator requests `/wiki-ingest <folder>`. Empty arguments stop at usage. The Editor-in-Chief first invokes the deterministic prefilter: URL matching precedes normalized raw-path matching; zero-byte files and the legacy Raindrop subtree are excluded. Only genuine-new candidates enter this batch fanout. This differs from the single-file procedure, where a duplicate match selects an existing page for update rather than creating a second page. SRC-1: `.claude/commands/wiki-ingest.md`; implementation baseline in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest).

Main reads `wiki/index.md` and `wiki/overview.md` once for shared context. Each Reporter receives one candidate, reads the raw and dedup state, and writes its source page. Its role contract additionally supplies the source guide/rubric, adjacent source/hub/backlink material and, for applicable person stubs, current-position verification. The output combines persistent file edits with a report: proposals for entities/concepts, connection links, contradictions and missing quote speakers. SRC-1: `.claude/commands/wiki-ingest.md`, `.claude/agents/reporter.md`.

> File outputs persist on the shared FS, but without the report the Editor-in-Chief cannot hand off to the next stage.
> --- `.claude/agents/reporter.md`

Anonymous role calls return final text under the target's stated host contract; fresh invocation contexts keep internal author processing out of main's context, but shared files escape that isolation. Resume and named-teammate modes are separate, as recorded in [RT-RTE-role-delegation](runtime.md#rt-rte-role-delegation). Neither fresh contexts nor source-slug ownership establish filesystem locks or transactional writes.

### Integration and verification

Reporters first lint their own source pages and fix failures before handing off. Stub schema/body lint is corpus-wide, but each author must check that no diagnostic names its own file. Main then deduplicates proposals and re-evaluates corpus-wide entity/concept thresholds: new sources can make an existing plain-text subject eligible even when no Reporter proposed it. Main owns cross-source threshold decisions and serial coordination; approved authoring targets go to the Reporter. New stubs still fall under the operator gate. Full synthesized hub rewrites are Columnist work, not permission for Reporters to expand their remit. SRC-1: `.claude/commands/wiki-ingest.md`, `.claude/agents/reporter.md`, `CLAUDE.md`.

Shared hub source lists, links and log updates are serialized; rebuild produces graph, clusters, contradictions, index and dependencies. The baseline records the code-backed rebuild and lint effects in [RT-RTE-build-lint](runtime.md#rt-rte-build-lint). Main directly runs deterministic batch checks here; a separate Copy Editor invocation is not mandatory for every such tool call. Source and stub writes already exist before the qualitative gate. SRC-1: `.claude/commands/wiki-ingest.md`.

Desk receives all changed L2-2 targets at their applicable review scope, plus sources selected by the lint advisory threshold of at least seven fact claims and three citations. The source review requires the raw original, not just the newly authored paraphrase. The Desk contract limits originals above 40KB to quotation spans and speaker sentences. This is selective grounding, not a promise of full-original review for every source. SRC-1: `.claude/agents/desk.md`.

Desk reads the page, applicable layer and craft guidance, and language policy. It uses two reader personas and returns actionable defects with severity, location, issue, suggested fix and evidence, plus explicit lists of sources opened and not opened. Its refusal power is procedural: it reports qualitative defects to be repaired; it does not directly edit the page. Deterministic lint checks format/count constraints, while Desk judges framing, argument and reader-facing defects. Neither is an expected-answer oracle for the raw document's substantive truth. SRC-1: `.claude/agents/desk.md`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest).

### Rejection, recovery and closing order

A supported failure branch is a Desk defect followed by Reporter ADAPT. The author marks each response `as-advised` or `diverged`; leaving a defect untreated also counts as divergence. Main sends only diverged defects back for one restricted re-adjudication. That pass can flag remaining defects and factual/attribution errors introduced by the treatment; another treatment and deterministic regression check close the round without another Desk pass. This bounds review cost, but does not establish that every qualitative defect has objectively disappeared. SRC-1: `.claude/agents/reporter.md`, `.claude/agents/desk.md`.

> Anything still open or newly created is treated once more in the same ADAPT round and closes at VERIFY₁ without another desk pass — the cap of one keeps the loop from growing.
> --- `.claude/agents/desk.md`

Main maintains the escalation count. First same-cause failure retries; second requires choosing wider grounding, conceding only an advisory grade with disclosure, or narrowing scope; third stops further iteration that turn and escalates to the operator. A required criterion is not waived by the advisory-grade option. SRC-1: `.claude/agents/README.md`.

> | 3rd FAIL on same cause | **escalate to human**, no further iteration this turn |
> --- `.claude/agents/README.md`

Contradiction integration must follow Desk edits and a rebuild whenever the cycle adds or changes a `contradicts:` line. This order has a concrete dependency: theme assignments refer to IDs calculated from claim text. The implementation hashes that text, and explicitly makes rewriting invalidate an earlier judgment. SRC-1: `.claude/commands/wiki-ingest.md`, `tools/_build/contradictions.py`.

> Editing the claim text still changes the id, and that orphaning is deliberate
> — a judgment was made about that wording, so a rewrite must be re-judged
> rather than silently inherited.
> --- `tools/_build/contradictions.py`

Before consolidation, the command temporarily exempts exactly three expected contradiction diagnostics: source-count mismatch, unassigned-ID coverage gap and root head-matter drift. Other failures remain actionable and logged. Final rebuild and all-group lint must reach rc=0 after consolidation; the temporary exemption is not the final acceptance bar. Main appends the operation log and batch-logs escaped lint failures and actionable Desk defects. This route retains failures for later diagnosis, but does not itself authorize changing the guides; instruction-change admission remains [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change). SRC-1: `.claude/commands/wiki-ingest.md`.

### Delivery and its limits

The command's delivered response reports pages added/updated, contradictions, verification results and cluster-health impact. Retained Markdown and rebuilt indices are already filesystem products intended for later use; [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) supplies the subsequent consumption route. A report alone is not external publication. Commit/push requires explicit operator approval for ingest outputs; the inbox queue-file exception does not approve the wiki/graph artifacts. Strong theme-changing contradiction flags also require a human gate. SRC-1: `.claude/commands/wiki-ingest.md`, `CLAUDE.md`.

> - External commit / push (exception: the system-managed inbox queue files `raw/_inbox.md`·`raw/_archive.md`, which `/wiki-ingest` Inbox Mode commits·pushes automatically)
> --- `CLAUDE.md`

Recovery in this account means author repair, re-grounding, rebuild and operator escalation, not an inspected atomic rollback. The runtime baseline bounds tool-name restrictions and shell bypasses: [RT-BAP-role-guidance](runtime.md#rt-bap-role-guidance) is interpreted guidance and [RT-BAP-hook-feedback](runtime.md#rt-bap-hook-feedback) provides scoped blocking/advisory channels, not proof that every path passes this workflow. Private raw originals and missing invocation traces prevent independent source-fidelity and execution conclusions. The supported result is a specified end-to-end protocol with code-backed derived-state operations, not demonstrated reliable delivery.

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

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Workflow-specific ordering: batch integration serializes shared-state updates after source fanout. Desk divergence handling bounds qualitative re-review to one extra pass on diverged defects. Contradiction consolidation follows any relevant claim-text edits and rebuild, with the final all-group lint closing the temporary contradiction-diagnostic exemption. Completion report, persisted working files and operator-approved external publication are separate milestones.

#### On [RT-RTE-role-delegation](runtime.md#rt-rte-role-delegation)

Workflow-specific handoff sufficiency: successful file writing alone does not move this chain forward. The Reporter report supplies collected proposals and findings for main's integration decisions, while Desk's structured report supplies the repair agenda. Fresh contexts do not remove these shared-file and explicit-report dependencies.
