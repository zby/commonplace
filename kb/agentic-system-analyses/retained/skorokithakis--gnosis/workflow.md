---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Gnosis workflow account: external coding-agent search, conflict handling, immediate recording and pre-commit review at the frozen revision."
run-id: AAS-2026-10-15-gnosis-5bfb42422ce3-01
reviewed-boundary: "429528bf98e424b40837d2dbe3631d0fb42da6fd"
---

# Gnosis workflow report

## Workflow account

The representative workflow is a coding task that consults retained decisions before implementation, records a new decision during work, and reviews knowledge before committing. It is selected because the embedded planning doctrine explicitly joins these steps as “THE AGENT LOOP”; it is not a sequence inferred from unrelated CLI capabilities. Gnosis coordinates this workflow through instructions and command returns, not an internal agent scheduler. The external coding agent owns every transition between commands and the implementation task itself. The inspected evidence is SRC-1 implementation and doctrine/design at the frozen revision, not an observed task run. SRC-1: `internal/doctrine/plan.txt`, `internal/doctrine/review.txt`, `cmd/gn/main.go`.

### Request and planning handoff

The setup contract asks the operator to place two instructions in the file the external agent reads at session start: request planning help at the start of a task and review help after finishing. Thus the request, current plan, shell permission and model context come from the external host; Gnosis does not construct or dispatch them. `gn help plan` returns embedded planning text and the shared command reference without opening a knowledge store. The caller then interprets it and chooses the next command. This is [RT-RTE-doctrine-delivery](runtime.md#rt-rte-doctrine-delivery), with advisory authority characterized by [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance). SRC-1: `README.md`, `cmd/gn/main.go`, `internal/doctrine/plan.txt`.

The detailed planning instruction places search after an initial plan and before implementation. README's shorthand says “before it plans”; the detailed instruction is the timing used in this trace. Neither wording installs an executable precondition on code editing. SRC-1: `README.md`, `internal/doctrine/plan.txt`.

> 1. After planning, before implementing:
>    You've read the task and laid out a plan. Before writing any code,
>    run "gn search" with keywords from your plan — system names,
>    feature areas, technical concepts you're about to touch.
> --- `internal/doctrine/plan.txt`

### Retrieval and conflict decision

The agent supplies plan-derived keywords joined with uppercase OR. In [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read), command code sanitizes the query, refreshes the lexical index as needed and returns ranked snippets, with a default limit of 20. The agent receives IDs, dates, primary topics and snippets, not necessarily the complete rationale. An explicit `gn show <id>` is available for full-entry read-back; it is a caller-selected continuation, not an automatic expansion or mandatory step in the doctrine. A zero-hit search returns successfully without text. That outcome does not certify that no relevant decision exists. SRC-1: `internal/commands/search.go`; the supplied runtime record supplies the index and show evidence and quotation.

The next decision is semantic: does a returned decision conflict with the proposed work? The doctrine assigns detection to the agent and requires surfacing conflicts to the user before proceeding. It allows the retained decision to remain valid, be stale, or need explicit supersession. It supplies no automatic adjudicator, required user-response format or machine-enforced veto. No trace establishes that the user resolved a conflict or that the agent changed its plan. SRC-1: `internal/doctrine/plan.txt`; [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance) supplies the verbatim conflict instruction.

### Work and immediate retention

Implementation remains external to Gnosis. When a decision is made or an alternative explicitly rejected, planning doctrine requests immediate recording rather than waiting for end-of-session review, because context may be lost. It also asks the agent to read review criteria before recording. Those criteria prefer human context or unreconstructable empirical observations, exclude conclusions recoverable from code/docs, and route locally anchored explanations to code comments. This is instruction-shaped candidate selection, not a software test of provenance or usefulness. The caller supplies topics, body and optional related IDs/author to [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission). SRC-1: `internal/doctrine/plan.txt`, `internal/doctrine/review.txt`, `internal/commands/write.go`.

The implementation verifies command structure, nonempty text, normalized topics and related-ID resolution. Accepted text reaches JSONL through AppendNew; the command subsequently rereads entries and returns the new ID. The runtime record supplies storage-lock scope and its limits. The caller is both proposer and semantic admission decision-maker; no internal reviewer or per-content human approval stage is inserted. An author string does not establish who supplied or approved the knowledge. SRC-1: `internal/commands/write.go`; [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission).

### Rejection and recovery branch

A concrete supported rejection is unquoted multiword text reaching Write as several positional arguments. The command rejects it before related-ID reads or AppendNew, rather than silently saving only part of the proposed entry. The dispatcher prints the error to stderr and exits 1. The external caller must correct quoting and reissue the command; there is no automated repair or retry worker. This checks input shape, not whether a rejected design alternative was actually tried or whether the retained explanation is sound. SRC-1: `internal/commands/write.go`, `cmd/gn/main.go`.

> if len(remaining) > 1 {
> return fmt.Errorf("write takes a single text argument but received %d; quote multi-word text with single or double quotes", len(remaining))
> }
> --- `internal/commands/write.go`

The timing of failure matters: a later `reading entries after write` error occurs after AppendNew has returned successfully. Therefore exit 1 is not a universal assertion that no entry was retained. The caller owns checking the store before retrying such a failure; the command implements no automatic rollback of that append. This is the recovery limit already identified by [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission), not an additional transactional guarantee. SRC-1: `internal/commands/write.go`.

### Review, sharing and delivery boundary

After external task completion, `gn help review` supplies selection examples and asks for a pre-commit review of the session. The same agent decides which candidates to omit, place in code comments or retain. For stale knowledge, it requests removal or a new related entry explaining the change. The latter preserves both entries unless one is separately removed; the relation does not itself resolve contradictions for future consumers. Maintenance and its rollback limits belong to [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance). SRC-1: `internal/doctrine/review.txt`, `internal/commands/write.go`.

> Commit the .gnosis directory along with your work — entries are shared
> knowledge, and nothing in there needs to be ignored. If this was the
> repo's first entry, .gnosis/ is new and untracked; add it.
> --- `internal/doctrine/review.txt`

There are three distinct completion boundaries. A successful write returns an ID after local retention; subsequent explicit reads can deliver that retained text to another invocation. Sharing with collaborators additionally depends on the caller following the commit instruction and distributing the repository. Delivery of the coding task's final answer, tests or product is outside Gnosis's command dispatcher: this workflow specifies no Gnosis acceptance gate for that product. Source wiring establishes these available handoffs, not that an entry was committed, consumed later, or improved a task. SRC-1: `internal/commands/write.go`, `internal/doctrine/review.txt`, `cmd/gn/main.go`; [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read).

Inspection for this member revisited the full `README.md`, `cmd/gn/main.go`, `internal/doctrine/plan.txt`, `internal/doctrine/review.txt`, `internal/commands/search.go` and `internal/commands/write.go` in SRC-1. These are already within the supplied boundary/runtime coverage; no new source or execution evidence is added. Other storage, index, show and maintenance details above rely on the cited supplied runtime records. Agent compliance and later decision effects remain unobserved, as distinct from the implemented CLI returns and the shipped instructions.

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

#### On [RT-RTE-doctrine-delivery](runtime.md#rt-rte-doctrine-delivery)

Workflow role: startup and post-task instruction handoffs. Each returns control to the same external caller. Printed doctrine is neither a worker assignment with managed execution nor proof that the next requested step occurred.

#### On [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read)

Workflow role: pre-implementation consultation. The caller chooses terms and whether to expand snippets; conflict interpretation and any user escalation occur after the CLI returns. Empty results do not discharge an exhaustive conflict check.

#### On [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission)

Workflow role: checkpoint a decision while session context is still available. Structural rejection returns repair responsibility to the caller. Successful local retention is not equivalent to repository sharing or delivery of the enclosing coding task.

#### On [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance)

Workflow role: pre-commit cleanup of the knowledge produced or invalidated by the task. Review doctrine requests this cleanup but does not schedule it or make completion a prerequisite for subsequent reads or commits.
