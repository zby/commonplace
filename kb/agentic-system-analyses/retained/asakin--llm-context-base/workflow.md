---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Workflow account of llm-context-base's personal-instance capture, filing and later knowledge delivery at the frozen template revision."
run-id: AAS-2026-10-14-llm-context-base-f63a7c0fb5f2-01
reviewed-boundary: "6d01cba8e2c22f9ca2519c70073a05cd54378a8c"
---

# llm-context-base workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a user asking an initialized personal instance to capture a process, deciding whether to file it, and later asking how that process works. This is selected because the shipped capture and query protocols explicitly connect an inbox draft, type-based filing and later file consumption. It covers the system's retention purpose without treating unrelated maintenance capabilities as an executed pipeline. The initial capture can terminate in the inbox; a later query is a separate user-triggered invocation, not an automatic continuation (SRC-1, `_meta/instructions/general.md`, `_meta/instructions/knowledge-query.md`).

This is a prescribed workflow, not a supplied execution trace. All evidence comes from SRC-1 at the reviewed commit registered in [boundary](boundary.md#source-register). The inspected paths below are already included in that boundary; no new source or functional coverage is added. Source passages supply doctrine/design, including the template, not observed adherence, factual accuracy or successful delivery. The host executes file operations and owns context and permission enforcement; the repository does not run a model. The existing [RT-CMP-ai-assistant](runtime.md#rt-cmp-ai-assistant) and route records identify the participants and mechanisms, so this member annotates them rather than allocating duplicate records.

### 1. Request and startup

The user is the task principal. In the ordinary initialized personal branch, the foreground assistant loads configuration, general instructions and phase-appropriate context, checks tools and the inbox, then prints the startup gate before handling the request. Task routing loads the write protocol and document standard for capture. [RT-RTE-session-start](runtime.md#rt-rte-session-start) supplies the startup evidence and its exceptions: framework mode is not this workflow, and initialization can require preliminary questions (SRC-1, `AGENTS.md`, `_meta/instructions/general.md`).

There is no prescribed delegation to a separate agent in these inspected protocols. The consequential handoffs are user-to-assistant task input, assistant-to-host filesystem operations, and assistant-to-user filing or structure proposals. The assistant owns sequencing and interprets natural-language criteria. The files do not establish a host-enforced workflow state machine or successful tool use (SRC-1, `_meta/instructions/general.md`, `_meta/instructions/agent-write.md`; [RT-RTE-capture-file](runtime.md#rt-rte-capture-file)).

### 2. Capture and disposition handoff

The assistant creates a dated inbox file containing the capture, useful summary, tags, update date and originating-agent attribution. New agent-written files are instructed to begin as drafts. The user then receives a specific choice rather than a generic approval of all future actions:

> 1. Create a file in `_inbox/` with the metadata standard
> 2. Name it: `YYYY-MM-DD-[short-slug].md`
> 3. Ask the user: "Should I file this now or leave it in the inbox?"
> 4. If filing now, route to the correct directory based on the `**Type:**` field
> --- `_meta/instructions/general.md`

SRC-1, `_meta/instructions/agent-write.md`, supplies draft metadata and agent attribution; `_config/standard.md` supplies the knowledge type and destination. For a process guide the final destination can be `2-Knowledge/HowTo/`, which the query module explicitly uses for process questions. This is a source-supported example, not evidence that a deployment guide was actually created. User permission to file selects disposition; it does not independently verify every sentence ([RT-CLM-review-policy](runtime.md#rt-clm-review-policy)).

If the user chooses to leave it, the retained inbox draft is the capture result, not a completed knowledge article. Ordinary later startup flags inbox files older than seven days; it does not prescribe automatic filing or expiry. If content suggests a new directory during training, the assistant proposes the directory and creates it only if approved. User rejection changes the proposal path:

> **User pushback:** If the user rejects a suggestion or says "stop suggesting directories" / "just park it" — back off immediately. Shift to the next-phase threshold or stop suggesting entirely. The user sets the pace.
> --- `_meta/instructions/general.md`

These are evidenced rejection branches, not observed recoveries. They keep the user in control of filing and structural expansion; they do not amount to a universal gate on all repository mutations (SRC-1, `_meta/instructions/general.md`, `_meta/instructions/agent-write.md`).

### 3. Filing, source handling and verification

On filing, the assistant selects the destination and appropriate template, edits the working article and adds obvious related links. Before disposing of the inbox original it checks the source-preservation setting. With preservation enabled, the assistant judges whether the original warrants movement to `_sources/`; otherwise the write protocol permits normal disposal after filing. Thus retaining the derived guide does not establish retention of its full input. The user supplies the setting and can calibrate it during training; the assistant supplies the item-level importance judgment (SRC-1, `_meta/instructions/agent-write.md`; [RT-RTE-capture-file](runtime.md#rt-rte-capture-file)).

Completion is a separate criterion from merely creating a draft. For knowledge articles the prescribed checks are:

> **Done when:**
> - [ ] Content is complete and accurate
> - [ ] Metadata block is filled in (Type, Summary, Tags, Status, Updated)
> - [ ] Filed in the correct directory (not still in `_inbox/`)
> - [ ] Status changed from Draft to Active
> - [ ] Related links added if connections exist
> --- `_meta/instructions/definition-of-done.md`

The same assistant applies these criteria and nudges the user toward completion; no separate evaluator, expected-answer reference or factual verification implementation is specified here. Failure to satisfy a criterion means the article has not met the declared completion rule, not that software blocks the write. The knowledge template itself contains `status: active`, whereas the agent-write protocol requires new agent files to start as drafts. A faithful draft capture therefore requires the assistant to override that template value. Blindly copying the template could mark a file active without establishing completion; no executed resolution of this mismatch is supplied (SRC-1, `_meta/templates/knowledge-article.md`, `_meta/instructions/agent-write.md`, `_meta/instructions/definition-of-done.md`).

The prescribed completion moment updates status and final placement, with a wiki-log entry for significant additions. General instructions also require an operations-log entry for ingested knowledge. These are assistant-owned file effects, not a transactional commit protocol. The write rules prohibit deleting or overwriting existing files without explicit instruction and prefer appending during updates. They do not specify recovery after a partially completed filing or failed host I/O. [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) bounds available Git-based recovery: it depends on committed state and does not cover every newly written or ignored file (SRC-1, `_meta/instructions/general.md`, `_meta/instructions/agent-write.md`, `_meta/instructions/definition-of-done.md`).

### 4. Delivered result and later consumption

Capture delivery and knowledge completion are different outcomes. A parked draft is a valid capture disposition; the completed guide requires final filing and active status under the checklist. The source defines usefulness as someone being able to find and use the document, but the checklist and status do not demonstrate that a person actually did so (SRC-1, `_meta/instructions/definition-of-done.md`).

A later process question triggers [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query). The assistant routes to HowTo, checks the directory README, scans summaries and tags, reads one to three relevant files, and returns a synthesis with paths and update dates. Reference content older than 90 days prompts a freshness warning. For files over 500 lines the module permits focusing on the first major section, so the delivered answer need not have consumed the entire retained guide. The query module still uses bold-field summary/date terminology, while the canonical standard specifies YAML frontmatter; faithful matching depends on the assistant interpreting the retained metadata across that wording mismatch (SRC-1, `_meta/instructions/knowledge-query.md`, `_config/standard.md`).

A missing-document result has its own supported recovery, rather than permission to fabricate a guide:

> 1. Tell the user clearly: "I couldn't find documentation for [X]."
> 2. Offer to capture it: "Would you like me to add this to the inbox so we can document it?"
> 3. If it seems like a missing process doc: "This might be worth creating as a knowledge article."
> --- `_meta/instructions/knowledge-query.md`

The query response is delivered when the assistant returns the cited synthesis or explicit missing-document response. Saving a synthesis is a further write decision, not an automatic query effect. No observed run shows the capture reaching this later consumer, an answer changing a decision, or a recovery succeeding. Those conclusions remain uninspected, rather than absent, within this doc-grounded boundary (SRC-1, `_meta/instructions/general.md`, `_meta/instructions/knowledge-query.md`).

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

#### On [RT-RTE-session-start](runtime.md#rt-rte-session-start)

Workflow entry condition: an initialized personal instance, excluding framework mode. The startup gate precedes the capture request; task routing supplies the write module and standard to the same foreground assistant. This is preparation of the assistant's context, not a delegated worker handoff. Startup completion is prescribed, not observed.

#### On [RT-RTE-capture-file](runtime.md#rt-rte-capture-file)

Workflow disposition: the user can accept immediate filing or retain an inbox draft. During training, directory rejection requires the assistant to back off. Verification: the knowledge checklist distinguishes capture from completion; its accuracy criterion has no independent oracle in the inspected procedure. The knowledge template's active default requires adjustment for draft admission. Delivery: parked capture and completed article are distinct terminal outcomes. Recovery: source retention is conditional, while partial filing/tool-error recovery is unspecified in these instructions. The account above retains the supporting source passages without redeclaring the route.

#### On [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query)

Workflow continuation: a later user question, not an automatic callback, initiates read-back. The delivered product is selected-content synthesis with path/date attribution; long-file truncation and metadata wording differences limit what can be inferred about complete consumption. A search miss prompts an explicit missing-document response and optional return to capture. No observed query establishes successful use of the representative captured guide.
