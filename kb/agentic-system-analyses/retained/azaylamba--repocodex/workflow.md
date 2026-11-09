---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "RepoCodex workflow account: a coding change retrieves repository memory, repairs or authors explanations, and reaches staged commit checks and advisory review."
run-id: AAS-2026-11-08-repocodex-bf22ac3623d8-01
reviewed-boundary: "96978e292fcb3b100f53ac024b353e1b8b2c8af4"
---

# RepoCodex workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a coding change in a consuming repository, including the branch where changed code lacks a pinning explanation. It is selected because the packaged coding skill connects retrieval, code editing, memory admission, validation and commit in one explicit procedure. This is not a workflow reconstructed by combining unrelated commands. The canonical route is [RT-RTE-coding-loop](runtime.md#rt-rte-coding-loop). The account below adds handoff and completion detail without declaring the same route again.

All findings concern SRC-1 at the frozen revision. The packaged coding/review skills supply doctrine/design; the hook supplies executable implementation. Runtime records supply the inspected command behavior. No observed agent trace or experiment is available. A shipped request to read, repair or review does not establish that an agent complied. External hosts retain task scheduling, model selection, approvals and final user communication; RepoCodex does not become the enclosing coding runtime.

### Request, retrieval and edit

A foreground coding agent starts with a user task and intended edit paths. Installation provides the skills and rules that can direct its behavior, but actual host loading is unobserved ([RT-RTE-install-wiring](runtime.md#rt-rte-install-wiring), [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption)). Under the coding procedure, the foreground agent requests `repocodex context <paths>` before editing. The deterministic retrieval command selects retained concept bodies by those paths; related concepts arrive as titles. The agent decides whether to open a related body. The handoff therefore supplies selected explanations, not the entire memory store or a guarantee that all relevant explanations were read ([RT-RTE-context-read](runtime.md#rt-rte-context-read)).

> Read returned concept bodies. Related pages are titles only — open a body only if the edit might touch that scenario.
> --- `src/repocodex/data/skills/repocodex-coding/SKILL.md`

The procedure also requests a bounded code-side impact inspection: grep changed symbols, rank plausible callers by proximity and test status, and stop at a default cap of 12 files. This is host-agent work, not an engine-spawned reviewer or isolated worker context. It limits requested investigation, not the size of the host's accumulated context. The host then edits code, preserving institutional why unless it intends a why-change (SRC-1 doctrine/design, `src/repocodex/data/skills/repocodex-coding/SKILL.md`; [RT-RTE-coding-loop](runtime.md#rt-rte-coding-loop)).

### Verification, rejection and recovery

After editing, the agent hands the diff to `repocodex validate --diff`. The command computes classifications, impacts, patches, skipped-memory findings and a `blocking` decision. The foreground agent owns the next step; a plain validation CLI call does not itself deny a commit just because `blocking` is true ([RT-RTE-validate-change](runtime.md#rt-rte-validate-change)).

A consequential rejection branch is uncovered code. `LIVE` alone does not finish the procedure: the skill requires `skipped_memory` to be empty. On `WRITE` or nonempty `skipped_memory`, the agent must consider all four independent concept types, then write or update every applicable type. One why spanning several paths may use one concept with several anchors. Several distinct whys require separate concepts; neither one page per file nor one default decision page is the prescribed result (SRC-1 doctrine/design, `src/repocodex/data/skills/repocodex-coding/SKILL.md`).

> Do not relabel an `InvariantContract` as `TechnicalDecision` to dodge `claims`. Unanchored narrative pages do not discharge `skipped_memory`.
> --- `src/repocodex/data/skills/repocodex-coding/SKILL.md`

The write handoff supplies proposed Markdown, identity and anchors to the deterministic admission command. Anchor/claim checks can reject mechanically unsuitable content, but do not certify that the prose truthfully explains the diff. Anchorless writes can be accepted without discharging the pinning obligation. The host must correct rejected proposals and retry, then revalidate coverage ([RT-RTE-memory-write](runtime.md#rt-rte-memory-write)). This is an open coding/maintenance task, not a curriculum or comparison against a supplied expected answer. Source matching is mechanical evidence; it is not an oracle for explanation truth. Per-content human approval is not inserted by the write command; any host approval policy remains external.

Other diagnostic branches preserve different recovery responsibilities. `REANCHOR` asks the host to apply and stage an emitted patch; the patch writer is a separate path without the ordinary write gate. `RECONCILE`/`DRIFT` requests repair in the same change, and `CLAIM_BROKEN` requests restoring the literal or superseding the concept with rationale. The host remains responsible for retrying verification and not ending with `blocking` true (SRC-1 doctrine/design, `src/repocodex/data/skills/repocodex-coding/SKILL.md`; [RT-RTE-anchor-patch](runtime.md#rt-rte-anchor-patch), [RT-RTE-validate-change](runtime.md#rt-rte-validate-change)). There is no established transactional rollback: in particular, a replacement write can deprecate a predecessor before a later rejection. Repository restoration and corrective retry remain caller responsibilities ([RT-RTE-memory-write](runtime.md#rt-rte-memory-write)).

The optional `repair` command is not required by the coding procedure. If explicitly used, it transfers next-step choice to an external harness with a static prompt and repository cwd. It does not transfer the computed lost/candidate payload in that prompt, and a zero child exit is not followed by a fresh validation. It cannot replace the foreground agent's completion check with a repaired-state certificate ([RT-RTE-agent-repair](runtime.md#rt-rte-agent-repair)).

### Commit, review and delivered result

The requested delivery unit is code plus its maintained memory and generated indexes, not merely an explanation returned in chat. The coding skill states:

> **Commit** includes `.context/` **and** `.repocodex/reverse-index.md` (plus matching files under `.repocodex/reverse-index/` when shards exist) when you wrote or reanchored memory.
> --- `src/repocodex/data/skills/repocodex-coding/SKILL.md`

The installed hook hands staged-diff validation to the CLI and converts a nonzero result into commit denial. Its executable handoff is explicit (SRC-1 implementation, `src/repocodex/data/hooks/pre-commit`):

> output="$(run_repocodex validate --diff --staged --hook)" || status=$?
> status=${status:-0}
> --- `src/repocodex/data/hooks/pre-commit`

This is an invoked check boundary, not a universal guarantee against bypass or an attestation of the exact staged file contents: the runtime inspection found working-tree source reads. Posture and acknowledgment exemptions also qualify denial; shadow posture blocks skipped-memory but not every other diagnostic. Actual installation, invocation and branch protection are not observed ([RT-RTE-validate-change](runtime.md#rt-rte-validate-change), [RT-BAP-check-enforcement](runtime.md#rt-bap-check-enforcement)).

At PR review, the separately instructed review agent receives the originating diff, runs validation against a merge base, and compares new concept narratives with that diff. Its semantic findings are advisory, not a second required admission gate. There is no inspected RepoCodex scheduler automatically launching that reviewer from the coding agent. The advisory Action invokes deterministic advisory output, not an agent performing the prose comparison ([RT-RTE-review-audit](runtime.md#rt-rte-review-audit)). The skill explicitly restricts its authority:

> Findings from this skill post to the **advisory** check only. Never fail the required deterministic check.
> --- `src/repocodex/data/skills/repocodex-review/SKILL.md`

Consequently, a commit accepted by configured checks is a narrower completion event than semantic approval or merge. The prescribed workflow delivers a repository change whose explanations can be reloaded by later context calls. Actual commit success, reviewer compliance, final user acceptance and improved later coding decisions remain unobserved. Persistence and delivery opportunity do not establish activation or benefit ([RT-BAP-memory-consumption](runtime.md#rt-bap-memory-consumption)).

### Inspection coverage

This member reread the complete packaged coding skill, review skill and portable hook at `src/repocodex/data/skills/repocodex-coding/SKILL.md`, `src/repocodex/data/skills/repocodex-review/SKILL.md` and `src/repocodex/data/hooks/pre-commit` under SRC-1. These were already covered by the supplied members; no new source or functional inclusion was added. HEAD matched the frozen commit and status reported no changes. Command internals and alternative paths above rely on the cited runtime records. No target execution was performed.

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

#### On [RT-RTE-coding-loop](runtime.md#rt-rte-coding-loop)

Workflow completion: the foreground agent must resolve blocking results, revalidate first-touch coverage and include memory plus indexes in the commit. A missing pin loops back to authoring rather than becoming successful merely because the top-level verdict is LIVE. The skill supplies the protocol, not evidence of its execution (SRC-1, `src/repocodex/data/skills/repocodex-coding/SKILL.md`).

#### On [RT-RTE-review-audit](runtime.md#rt-rte-review-audit)

Workflow handoff limit: PR review requests interpretation with the originating diff in context, but no automatic coding-to-review agent launch is established. Semantic mismatch findings are advisory and do not themselves reject the required deterministic check (SRC-1, `src/repocodex/data/skills/repocodex-review/SKILL.md`).
