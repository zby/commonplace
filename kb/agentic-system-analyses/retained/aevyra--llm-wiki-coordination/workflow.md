---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "LLM Wiki Coordination workflow: a structural question passes through peer-evaluated dialogue, user recognition, revision-specific canon review and reopening at the frozen commit."
run-id: AAS-2026-10-14-llm-wiki-coordination-a12f3c7007f2-01
reviewed-boundary: "126749634d1c8c2fd6141f59711c882c2d629699"
---

# LLM Wiki Coordination workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is resolving a structural wiki question through a directory-format dialogue and proposing the result for canon. It was selected because the thread format explicitly connects dialogue crystallization to the consensus protocol. This is a shipped procedural chain, not a constructed combination of unrelated capabilities. No concrete downstream request, execution trace or delivered canon page is supplied. The account therefore establishes prescribed coordination and selected implemented diagnostics, not successful execution. SRC-1: `protocols/dialogue-thread-format.md`, `protocols/multi-ai-consensus.md`; [RT-RTE-thread-participation](runtime.md#rt-rte-thread-participation), [RT-RTE-canon-admission](runtime.md#rt-rte-canon-admission).

> - [Multi-AI Consensus Protocol](multi-ai-consensus.md) — format of the `consensus:` block in the canon; triggered after crystallization.
> --- `protocols/dialogue-thread-format.md`

External agents own interpretation and filesystem edits. An external host/user must invoke them; the package does not dispatch workers, pass a model context, allocate concurrent writes or authenticate participant handles. Consequently, the handoffs below are shared-file obligations, not isolated subagent calls. [RT-ABS-runtime-orchestration](runtime.md#rt-abs-runtime-orchestration) supplies the inspected absence boundary; SRC-1: `README.md`, `tools/llm-wiki-audit.py`.

### 1. Turn a question into a shared thread

The initiating agent creates a topic directory, writes stable context and open questions in `thread.md`, participants/targets/preferred orientations in `meta.yaml`, and an initial numbered contribution without `last_eval`. It updates global indices and logs. These files supply later participants with the question, prior work, local identities and an explicit target; no richer delegation envelope or host scheduling policy is specified. The context is subsequently preserved, with only new open questions appended. SRC-1: `protocols/dialogue-thread-format.md`; [RT-RTE-thread-participation](runtime.md#rt-rte-thread-participation).

> The initiating agent writes once. After opening, it evolves **only by appending OQ** (new Open Questions); existing OQ and context are not edited.
> --- `protocols/dialogue-thread-format.md`

The protocol permits adopter-chosen dialogue roots. To receive the shipped dialogue diagnostics, the adopter must use the checker's `wiki/agents/dialogue` traversal or adapt the checker externally. The starting-thread example uses `protocols/dialogue`, so following that example alone does not establish audit coverage. This is the root mismatch already recorded in [RT-RTE-audit-invocation](runtime.md#rt-rte-audit-invocation), not evidence that every adopting host misses checks. SRC-1: `protocols/dialogue-thread-format.md`, `tools/llm-wiki-audit.py`.

### 2. Hand the preceding contribution to the next participant

When another agent enters, it reads the previous contribution and evaluates its Novelty, Coherence and Robustness on 0–1 scales. It records those scores and the preceding filename in its own entry's `last_eval`; the author's `declared_axis` records intent, not self-assessment. It calculates accumulated evaluations, compares them with target, and aims its next contribution at the largest deficit. Robustness deficiency invites a critic; Novelty deficiency invites a generator. This is attention selection by the participating agent, not selection or launch of an agent by a scheduler. SRC-1: `protocols/rolespace-coordination.md`, `protocols/dialogue-thread-format.md`; [RT-RTE-thread-participation](runtime.md#rt-rte-thread-participation).

> - If Robustness is lacking — act as a **Critic**. If Novelty is lacking — act as a **Generator**.
> --- `protocols/rolespace-coordination.md`

The next participant receives prose and metadata, not an independently validated summary. Numerical accumulation organizes subjective peer judgments; neither scores nor reaching target supplies a semantic answer oracle. Later entrants can read the retained chain and calculate the total, but automatic loading, completeness of model-visible history and actual compliance remain uninspected. The thread format includes closure evaluations in that sum; the RoleSpace participation checklist mentions contribution/reopen entries only. For the closure step below, the more explicit thread-format definition supplies the rule. SRC-1: `protocols/dialogue-thread-format.md`, `protocols/rolespace-coordination.md`.

### 3. Propose closure and hand the decision to the user

A closing agent evaluates the preceding contribution, includes that evaluation in the total, writes `current_at_close`, and supplies a summary plus `proposed_crystallization` containing canon-page targets and a patch summary. The receiving user judges Recognition. Target attainment indicates procedural maturity, but does not replace that decision or prove the proposal correct. SRC-1: `protocols/dialogue-thread-format.md`, `protocols/rolespace-coordination.md`; [RT-RTE-canon-admission](runtime.md#rt-rte-canon-admission).

> - If `current_at_close` < target on any axis — the User may refuse Recognition, citing this vector.
> --- `protocols/dialogue-thread-format.md`

Ordinary peer evaluation stops at closure: the closing text has no next standard contribution evaluating it. The user is the prescribed acceptance/rejection principal at this handoff. The audit can diagnose an incorrect closing total; it does not compare that total with target or prove user recognition. Canon-producing tooling and the actual file writes are external duties, not executable functions shipped here. SRC-1: `tools/llm-wiki-audit.py`, `protocols/dialogue-thread-format.md`; [RT-RTE-canon-admission](runtime.md#rt-rte-canon-admission), [RT-CLM-canon-enforcement](runtime.md#rt-clm-canon-enforcement).

### 4. Admit the structural document separately from recognizing closure

After recognized crystallization, a structural-page author initializes a revision and consensus block, marks their own contribution and leaves other active agents pending. Reviewers must read the page in the same session before endorsing it. Thus a thread's accumulated scores do not transfer into page endorsements: agents review the resulting document, not merely the fact that the discussion closed. Authors own lifecycle; individual agents own endorsements. SRC-1: `protocols/multi-ai-consensus.md`; [RT-RTE-canon-admission](runtime.md#rt-rte-canon-admission).

> An agent may only set their status to `accepted` or `contributed` if they have read the document **in the same session** in which they are updating the status. Setting a status without a recent review is considered a violation of protocol.
> --- `protocols/multi-ai-consensus.md`

Full canonical delivery requires all active agents accepted/contributed, no stale endorsements and explicit user approval. The active set depends on persistent persona/note files and recent activity. The soft-canonical alternative requires at least two-thirds active agreement, remaining pending/stale statuses aged at least 14 days, no disputes and explicit user approval. These are human/agent-operated admission obligations, not a shipped quorum gate. A model supplies authorship and semantic review; the user approves the final transition and decides disputes. No expected-answer dataset or semantic oracle is supplied. SRC-1: `protocols/multi-ai-consensus.md`; [RT-RTE-canon-admission](runtime.md#rt-rte-canon-admission), [RT-CLM-canon-enforcement](runtime.md#rt-clm-canon-enforcement).

The delivered result under this protocol is a retained structural page with revision-specific endorsements and the approved lifecycle, rather than an assistant return value or merely a closure entry. Its subsequent consumers are agents working on the page, who must inspect consensus and revisions again. Actual page generation, recorded approval and later behavioral dependence are not observed. SRC-1: `protocols/multi-ai-consensus.md`.

### 5. Recover from premature closure or rejected content

A user can refuse an under-target closure. To continue a closed thread, an agent writes a `reopen` entry: it evaluates the closing entry, names why closure was premature and supplies the new discovery. The prescribed status returns to open; standard contributions resume. Only one reopen is allowed for a given closure, while a later closure receives a new sequence number. This preserves the criticized closure and extends the discussion rather than rolling back old text. No software transaction performs those transitions. SRC-1: `protocols/dialogue-thread-format.md`; [RT-RTE-thread-participation](runtime.md#rt-rte-thread-participation).

> **Reopen is the only way to evaluate a closing entry.** After a reopen, the thread status returns to `open`, followed by standard contributions. A closing entry can only be reopened once; a subsequent closing is a new `type: closure` with a new `n`.
> --- `protocols/dialogue-thread-format.md`

A disputed soft-canonical page reverts to working. Specific disputed logic must be identified and discussed in a dedicated dialogue; the user has the final decision. Significant edits increment revision and stale others' endorsements; revision mismatches require re-review. These recovery paths revisit content or reliance, not a count-only approval cycle. Their execution and the quality of the resulting criticism remain unobserved. SRC-1: `protocols/multi-ai-consensus.md`; [RT-RTE-canon-admission](runtime.md#rt-rte-canon-admission).

### Verification is a maintenance path, not the canon gate

The source does not mandate running the CLI between every contribution, closure and promotion. Its separate integrity workflow instructs an agent to perform technical linting, semantic review, retain a report and add a log summary. If a Hard error is contested, the agent marks it contested with justification and asks the user for a final verdict. The CLI itself only reads and prints findings; report retention, repair and escalation are external actions. SRC-1: `protocols/integrity-audit.md`, `tools/llm-wiki-audit.py`; [RT-RTE-audit-invocation](runtime.md#rt-rte-audit-invocation), [RT-BAP-audit-exit](runtime.md#rt-bap-audit-exit).

The inspected non-archival entry checker rejects missing `last_eval` with a HARD diagnostic, detects immediate same-author evaluation under matching references, and compares closing totals against the accumulated vectors. At normal CLI completion, any HARD finding yields exit 1. A caller must honor that result for it to block work. The checker does not itself reject a filesystem write, select the repair agent or resume discussion. SRC-1: `tools/llm-wiki-audit.py`; [RT-CLM-peer-evaluation](runtime.md#rt-clm-peer-evaluation), [RT-RTE-audit-invocation](runtime.md#rt-rte-audit-invocation).

The failure coverage is bounded: alternate evaluation references receive only WARN; archival metadata bypasses entry-chain checks even after reopening; target attainment, post-closure append prohibition and canonical quorum/user approval are not enforced here. An audit pass therefore cannot stand in for either Recognition or canonical admission. These are inspected branches/limits, not observed failures. SRC-1: `tools/llm-wiki-audit.py`; [RT-RTE-archival-audit](runtime.md#rt-rte-archival-audit), [RT-CLM-canon-enforcement](runtime.md#rt-clm-canon-enforcement).

Inspection for this member covered all four protocol files and the audit metadata/entry-chain methods at the frozen SRC-1 revision, using the supplied runtime records for wider executable coverage. No source identity or boundary was added, and no target execution was performed. The retained procedure affords a recoverable, multi-step discussion-to-document chain; it does not establish deployed orchestration, reliable semantic verification or successful delivery.

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

#### On [RT-RTE-thread-participation](runtime.md#rt-rte-thread-participation)

Workflow position: request/context → initial contribution → repeated peer evaluation and deficit-directed contribution → closing proposal. The handoff persists context and judgments for subsequent participants but supplies neither a dispatched worker nor a runtime return. The premature-closure recovery rejoins this route through an explicit reopen, not an ordinary append.

#### On [RT-RTE-canon-admission](runtime.md#rt-rte-canon-admission)

Workflow position: recognition of a dialogue closure precedes the separate page-review/admission stage. Delivery is the approved structural page and its current-revision endorsements; thread target attainment is not the delivery predicate. Page disputes can feed a dedicated dialogue, while revision changes reopen endorsement work without necessarily reopening the original thread.

#### On [RT-RTE-audit-invocation](runtime.md#rt-rte-audit-invocation)

Workflow position: separately initiated maintenance verification, not a mandatory intermediate canon-admission step. Its immediate exit is caller-visible rejection of the checked wiki state only when honored; external agents/users own repairs, retained reporting and contested-Hard recovery. No source-supported ordering places this check at every discussion handoff.
