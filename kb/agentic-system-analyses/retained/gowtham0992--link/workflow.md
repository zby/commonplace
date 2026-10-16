---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Link workflow: human-requested arbitrary-source ingestion through agent authoring, completion validation and later context delivery."
run-id: AAS-2026-10-14-link-595f6f9cba36-01
reviewed-boundary: cc92f3632121b04063b24eaaf3a8c5429eaf2b57
---

# Link workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a human adding an arbitrary source under `raw/` and asking the foreground agent to ingest it. This path was selected because it connects source inspection, agent-authored knowledge, human interaction, explicit completion checks and later retrieval. It is a shipped multi-step agent procedure, not a successful execution trace or an internal autonomous compiler. The frozen scope and excluded host responsibilities are those in [boundary](boundary.md). The enclosing agent supplies interpretation, filesystem actions and the final response; Link supplies instructions, status, indexes, validation and retrieval. See [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki).

Added inspection at SRC-1: doctrine/design in `LINK.md` ingest rules and the complete `skills/link-ingest/SKILL.md`; implementation in `mcp_package/link_core/ingest.py`'s `build_ingest_guidance`, `mcp_package/link_core/validation.py`'s `validate_wiki`, and `link.py`'s validation wrapper. These files are at the registered commit. No target code or tests were executed. Status collection internals and every validation helper were not audited; the account does not assert complete scanning or semantic verification.

### Request and initial handoff

The human delegates processing of an identified raw source to the foreground agent. The shipped skill directs that agent to obtain the ingest plan first, read only pending files identified by it, and preserve provenance. The handoff supplies local paths and instructions, not a copied source corpus or a separately launched worker. Link's status guidance supplies a proposed next prompt and commands; the external agent remains the next-step owner. SRC-1, `skills/link-ingest/SKILL.md`, `mcp_package/link_core/ingest.py`.

> 3. Read only the pending raw files named by the ingest plan. Create or update one `wiki/sources/...` page per raw file, and update existing concept/entity/exploration/memory pages before creating thin duplicates.
> --- `skills/link-ingest/SKILL.md`

An inspected rejection path occurs before authoring: `build_ingest_guidance` returns `blocked_secrets` and no agent prompt when pending items contain detected secret-shaped values. It asks for human redaction and a status refresh. Source-access and raw-access failures also withhold the prompt. This is code-generated guidance plus an agent protocol, not a permission boundary preventing direct file reads. The detector's completeness and actual host compliance remain unestablished. SRC-1, `mcp_package/link_core/ingest.py`.

> "Do not ask an agent to ingest flagged raw files until the secret-looking values are removed or redacted.",
> "After redaction, refresh ingest status and continue with the normal ingest prompt.",
> --- `mcp_package/link_core/ingest.py`

### Interpretation and knowledge admission

Once the source is eligible, `LINK.md` asks the agent to read it completely, discuss three to five takeaways with the human, create a source page, and update or create pages for significant concepts, entities and claims. Existing pages receive new source links and metadata; new pages start at seed maturity. Contradictions are to be recorded in both pages' Open Questions. The agent must reread changed pages for coherence and maintain the index and log. These are content judgments performed by the external agent, not decisions made by Link's deterministic status command. SRC-1, `LINK.md`; [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki).

> 1. Read the source completely
> 2. Discuss key takeaways with the human (brief, 3-5 bullet points)
> 3. Create a source page in `wiki/sources/` following the template
> --- `LINK.md`

> - Every claim must link back to its source page. No orphan claims.
> - Tag confidence on claims: `high` (explicitly stated), `medium` (reasonable inference), `low` (speculative)
> --- `LINK.md`

The human's ingest request authorizes the workflow; the instructions do not require separate approval of every wiki claim. By contrast, personal memories remain proposals until approved under the skill and [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission). Confidence labels express agent-authored assessments, not reference-answer judgments. The natural-language grounding and contradiction rules have the compliance limits of [RT-BAP-agent-steering](runtime.md#rt-bap-agent-steering). No actual source corpus, contradiction-resolution episode or theory revision is supplied; the theory limits in the runtime's agent-wiki record remain unchanged.

### Verification, rejection and recovery

After writes, the agent rebuilds the index and backlinks, invokes validation and, in the official skill, health. [WF-RTE-wiki-validation](#wf-rte-wiki-validation) establishes the concrete validation part. It checks structural conditions, links and detected secrets in the current wiki. Default validation can pass with warnings; strict validation additionally requires zero warnings. Neither result proves faithful paraphrase, truth, meaningful contradiction handling or human approval.

> - After rebuilding index/backlinks, run MCP `ingest` action `validate`, `python3 link.py validate .`, or `GET /api/validate` when available. Treat validation errors as blockers before reporting ingest complete.
> --- `LINK.md`

A failed check returns findings to the calling agent. The completion protocol blocks its success report; it does not undo the already-written files. The foreground agent must repair affected pages or generated graph data and rerun checks before claiming completion. The inspected ordinary authoring/validation path has no automatic whole-workflow rollback. Journaled memory recovery in [RT-RTE-local-recovery](runtime.md#rt-rte-local-recovery) is a separate mechanism, not a guarantee for these host-authored edits. Source-only inspection cannot establish that an agent actually repairs rather than ignores findings.

### Delivery and later use

Delivery has two boundaries. Immediate delivery is the updated local wiki plus the external agent's completion report, which the instructions condition on validation. The source does not establish an executed final report or successful checks. Later delivery is selected source-backed wiki content returned through [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), with the interpretation limits of [RT-BAP-context-packet](runtime.md#rt-bap-context-packet). Raw retention alone is not that delivery: a source must be represented in wiki pages for this workflow's ordinary wiki-retrieval result.

The receiving agent gets a bounded packet, not the entire ingested source or wiki. It can request more context; Link does not evict earlier host turns or isolate authoring in a separate model frame. Thus the workflow supports an inspectable route from admitted pages to later selected context, not evidence that all original details survive selection or improve a subsequent answer. Retrieval wiring and its retained verbatim support are in the supplied context-recall record.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-wiki-validation
Label: Wiki completion validation

Part of: [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki)

This is the post-authoring validation step of the parent workflow, separately established from implementation. It is not another ingest route or an admission mechanism that stages agent writes before persistence. Endpoints/progression: agent invokes validation after authoring/rebuild → CLI resolves wiki directory → `validate_wiki` reads current pages and backlinks → findings and pass/fail → agent completion decision. Owner: software decides structural pass/fail; the agent decides repair and reporting, constrained by the completion instruction. Context/state: current Markdown, required directories, metadata, sections, wikilinks and backlink index. Effects: inspected validator reads and returns findings, without reverting pages. SRC-1, `mcp_package/link_core/validation.py`, `link.py`, `LINK.md`.

- Immediate return: structured pass/fail, error and warning counts, and individual findings; the CLI JSON branch returns exit code 0 on pass and 1 on failure.
- Later read-back: inapplicable — this validator does not persist a report or behavioral update; later validation independently rereads the wiki.
- Delegated visibility: findings reach the invoking foreground agent or human; no additional worker or host-wide result propagation is established.
- Selection predicate: current wiki Markdown pages and required paths, category/type rules, required metadata and sections, detected secret-shaped values, resolved wikilink targets and expected versus stored backlinks; strict mode additionally rejects warnings.
- Invalidation or expiry: inapplicable — the result describes the inspected filesystem state; subsequent edits require a fresh check rather than updating a retained validation object.
- Activation or effect: a failed result is available to block the completion report under the instructions; code does not prevent agent file writes or establish compliance with that reporting constraint.
- Evidence limits: implementation and instructions only; structural checks and secret heuristics do not constitute a semantic source-grounding oracle; no check execution or recovery episode supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The agent proposes changed knowledge. Software can veto structural acceptance, while the human can request correction or withdraw the task through the external host. The operating mode is open requested ingestion, not a benchmark or adaptive improvement curriculum. There is no expected-answer oracle: the validator compares structural properties and graph data, not an authored reference answer. Guidance shaping the proposal is `LINK.md` and the official ingest skill; changed pages, provenance and log/index data persist, while this check's returned findings are not persisted by the inspected function. Rejection leaves already-written pages in place; manual agent correction and rerunning checks own recovery.

> error_count = sum(1 for finding in findings if finding["severity"] == "error")
> warning_count = sum(1 for finding in findings if finding["severity"] == "warning")
> passed = error_count == 0 and (warning_count == 0 if strict else True)
> --- `mcp_package/link_core/validation.py`

> if json_output:
>     print(json.dumps(payload, indent=2))
>     return 0 if payload["passed"] else 1
> --- `link.py:820-822`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki)

Workflow-specific coordination: the human's source-processing request starts the work; the status plan supplies file identities and next actions; the foreground agent retains authoring and completion responsibility throughout. Takeaway discussion is an intermediate human interaction, not evidenced per-claim approval. The concrete completion check is [WF-RTE-wiki-validation](#wf-rte-wiki-validation). Secret/access guidance interrupts the procedure for user remediation; post-write structural failure returns repair responsibility to the same agent. Delivery requires distinguishing persisted wiki pages, instructed success reporting, and later selected retrieval: none supplies observed execution of the others. There is no inspected handoff to a second agent within this selected procedure.
