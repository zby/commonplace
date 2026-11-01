---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Ultimate workflow report: feature request through coordinator, worker, review and checked landing."
run-id: AAS-2026-11-01-ultimate-f5179584de71-01
reviewed-boundary: "e2b9fa61962f6aecd394dea1c670688fac3ec432"
---

# Ultimate workflow report

## Workflow account

### Selection and evidence boundary

This account selects the shipped feature-development workflow: user request → standing Ultimate → coordinator branch → bounded implementation and review → workspace submission → landing report → user notification. It is representative because the root and coordinator instructions explicitly name it as the normal flow after authorization, and shipped tools implement its delegation and integration boundaries. Small fixes deliberately omit workers and review. This is a source-supported protocol, not a reconstructed successful run. SRC-1: `agents/ultimate.md`, `agents/coordinator.md`; [WF-CLM-feature-protocol](#wf-clm-feature-protocol).

The account uses implementation and doctrine/design at the frozen revision in [boundary.md](boundary.md). No target execution, tests or model calls were performed; no observed execution trace was supplied. Thus wiring and requested behavior can be established, but actual compliance, completed work, test adequacy and reliable delivery cannot.

### 1. Request, assessment and authorization

The browser admits a request asynchronously to a durable conversation; its immediate receipt is not a completed answer. See [RT-RTE-browser-input](runtime.md#rt-rte-browser-input). The standing Ultimate is instructed not to change product code itself. It starts a coordinator branch with a title and a self-contained prompt containing the user's words, goal, constraints and relevant memory slugs. Root-branch creation uses a memory brief when present, not the root's entire tally; branching a branch has different history behavior. See [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch). These are distinct from worker subagents.

The coordinator first assesses a feature and builds nothing unless the request explicitly waived assessment. Its assessment covers complexity, code delta, reuse, alternatives, risks and numbered decisions. It ends its turn so Ultimate can weigh in. Ultimate may say ask the user, decided with named authority, or hold for a consolidated question. The coordinator then asks its own reply-expected question card and waits. Under a hands-off goal the standing agent is instructed to decide in the user's place; approval is therefore not universally a fresh human decision. These are model-interpreted instructions, not a software guarantee that unauthorized edits are impossible. SRC-1: `agents/ultimate.md`, `agents/coordinator.md`; [WF-CLM-feature-protocol](#wf-clm-feature-protocol), [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance).

### 2. Plan and execution handoff

After the go, the coordinator is asked to make an epic with binary acceptance criteria and one task per unit of work. It keeps requirements, architecture, acceptance criteria and final judgment. Delegation is reserved for bounded, independent, cheaply verifiable work whose cost justifies another context. Independent scouts may run in parallel; workers editing the same files must run serially by policy. Each brief supplies purpose, writable and forbidden scope, known inputs, acceptance commands, whether evidence should be a committed core test or a one-time proof, scope-escalation instructions and the expected evidence-based return. SRC-1: `agents/coordinator.md`; [WF-CLM-feature-protocol](#wf-clm-feature-protocol).

The actual child start/configuration path is [RT-RTE-subagent-start](runtime.md#rt-rte-subagent-start). By default the child has a separate conversation, selected definition and task, not all parent history; an explicit fork changes that. The worker definition requests a worktree and denies instance startup. Its task is to read surrounding code, implement only the assignment, run relevant checks, inspect its diff, make one focused commit and return status, criterion-by-criterion evidence, verification commands, SHA, divergence and risks. Missing context should produce BLOCKED rather than guessed scope. Those promises are instructions; the worktree and granted tools are not a filesystem sandbox. SRC-1: `agents/worker.md`, `extensions/subagents/children.ts`.

The context boundary resembles a separate frame with a selected result returned, but not a disposable frame: the durable child transcript, Git commit and host effects remain. The answer reporter extracts answer text plus model identity and retains an answer-entry pointer; it does not copy the full child transcript into the parent. The coordinator must fetch transcript evidence separately. An aborted/error or empty final message is not counted as an answer. SRC-1: `extensions/subagents/server.ts`; see the workflow annotation on [RT-RTE-subagent-start](runtime.md#rt-rte-subagent-start).

### 3. Verification, review and local integration

A finished child is not accepted merely because it is idle or says DONE. Coordinator policy requires inspecting its diff and citations and reading the last full test run in its transcript. A poor result is to be repaired locally or re-briefed with narrower scope or a stronger model. These are acceptance instructions for the coordinator model, not automatically enforced truth checks. SRC-1: `agents/coordinator.md`; [WF-CLM-feature-protocol](#wf-clm-feature-protocol).

For review, the coordinator supplies one reviewer with an immutable base..head range and acceptance criteria. If reviewer-* definitions exist, the reviewer is instructed to start every team member independently with the same task, withhold peer reports, merge duplicates without dropping issues, expose disagreements, and approve only if all approved. Missing or ambiguous range means NEEDS CHANGES; without a team it reviews read-only itself. Reviewers are instructed not to run mutation-capable tests and instead read test output. Model judgment can reject a candidate, but is not a known-answer oracle and does not establish correctness. SRC-1: `agents/reviewer.md`; [WF-CLM-feature-protocol](#wf-clm-feature-protocol).

Worker work first lands into the coordinator's checkout through [WF-RTE-child-land](#wf-rte-child-land), not through the final checked lander. This local path checks readiness, idleness, clean child state and Git ancestry and fast-forwards; it does not itself run the project's configured check suite. A moved/diverged target rejects and tells the caller to update and verify again. The coordinator is still responsible for review and its own affected checks. Distinguishing this local integration from [RT-RTE-change-admission](runtime.md#rt-rte-change-admission) prevents reading the tool's word “verifies” as a guarantee that each worker landing ran the final checks. SRC-1: `extensions/workspaces/workspaces.ts`, `agents/coordinator.md`.

### 4. Submission, rejection and recovery

The coordinator reports what it built, how it verified and any divergence before submitting, because a successful landing can conclude it without another run. The workspace executor restricts submission to a top-level main conversation, not an owned child or lander. Submission requires a nonempty divergence statement (including “None”), ready workspace, clean worktree and unchanged branch identity, and captures its commit tip into a persistent queue. It does not inspect whether the coordinator actually completed the prescribed review. SRC-1: `agents/coordinator.md`, `extensions/workspaces/server.ts`, `extensions/workspaces/workspaces.ts`; [RT-RTE-change-admission](runtime.md#rt-rte-change-admission).

The lander prepares a separate integration checkout at the target, optionally fetches/merges the configured remote, merges the submitted tip, runs setup and then configured checks. A merge conflict returns a repair instruction rather than inventing a resolution. Check groups run in order, with concurrent members inside a group. Each failing command gets one rerun; a passing rerun marks it flaky, while a second failure rejects. All members settle before failure handoff. Durable memos retain check outcomes, merged/prepared commits and the first landing, although a crash between a check run and its memo can rerun that check. These are implementation mechanisms, not evidence of exactly-once external effects. SRC-1: `extensions/workspaces/lander.ts`; see annotation on [RT-RTE-change-admission](runtime.md#rt-rte-change-admission).

The failure path is concrete: twice-failed check → failed outcome → follow-up input to submitting coordinator → repair and resubmit. The source tells the coordinator to fix flaky tests at their cause, not skip them or inflate timeouts. The lander also rejects a changed integration checkout after checks. It serializes target movement, retries integration if the target moved within its attempt bound, and fast-forwards only the checked commit. Its checks are software process-outcome oracles supplied by project settings, not proof of semantic acceptance. Direct shell changes remain outside this gate. SRC-1: `extensions/workspaces/lander.ts`, `agents/coordinator.md`; [RT-RTE-change-admission](runtime.md#rt-rte-change-admission).

### 5. Delivery is a landing plus routed reporting

The target's successful fast-forward establishes local integration. Push is conditional on settings; a later push failure can leave a valid local landing, which the report distinguishes from “not landed.” Delivery therefore cannot be equated with a remote push. The lander writes the outcome card into the submitting branch, concludes it only if no work remains, then wakes its starter with the card when concluded or sends a note while it remains active. Request IDs key these submissions. Checkout-release failure does not undo the landing; it is reported for later reconciliation. SRC-1: `extensions/workspaces/lander.ts`; [RT-RTE-change-admission](runtime.md#rt-rte-change-admission).

Ultimate is instructed to tell the user what landed; the root prompt distinguishes a short acknowledgment of started work from a later explicit result message. For changes in Ultimate's own server/shared paths the lander can add a restart hint, and the root is instructed to restart and mention it. Runtime replacement has its separate controls in [RT-RTE-change-admission](runtime.md#rt-rte-change-admission). Actual receipt by a user, performed restart and successful feature behavior remain unobserved. SRC-1: `agents/ultimate.md`, `extensions/workspaces/lander.ts`.

### Additional inspection and limits

This member adds doctrine/design inspection of the full `agents/coordinator.md`, `agents/worker.md` and `agents/reviewer.md`, and the feature/decision/delivery portions of `agents/ultimate.md`. Added implementation inspection covers `extensions/subagents/children.ts`, answer extraction/report submission in `extensions/subagents/server.ts`, workspace tool restrictions/prompt in `extensions/workspaces/server.ts`, child land and submission in `extensions/workspaces/workspaces.ts`, and merge/check/fast-forward/report/release portions of `extensions/workspaces/lander.ts`. All are SRC-1 under the same pin. These additions are evidence about implementation and instructions only. The runtime baseline supplies browser admission, branch creation, model configuration and external harness limits; this account does not independently audit the full scheduler, question-card transport or watchdog implementation. No successful approval, review, recovery or landing run is claimed.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-child-land
Label: Child worktree into owner checkout

Distinct from [RT-RTE-subagent-start](runtime.md#rt-rte-subagent-start), which creates and reports the child, and [RT-RTE-change-admission](runtime.md#rt-rte-change-admission), whose workspace lander checks and integrates a top-level submission. This is the intermediate subagent land action. The parent calls it for a finished worker; workspace code serializes on its source, checks child idleness/readiness, clean state, branch identities and ancestry, then fast-forwards the owner's source checkout and records the landed tip. If already integrated, it reports nothing to land. SRC-1 implementation: `extensions/workspaces/workspaces.ts`.

- Immediate return: landed SHA, commit list, changed files and possible restart hint, or error/nothing-to-land result.
- Later read-back: owner's Git checkout contains child commits; workspace document retains landed tip for subsequent status/recovery.
- Delegated visibility: parent receives integration metadata, not the child's complete conversation; transcript remains separately reachable.
- Selection predicate: requested child workspace must exist, be ready, idle and clean, retain its branch identity, and have a tip compatible with the source target.
- Invalidation or expiry: divergent/moved target rejects with update-and-verify instruction; worktree release is a separate mechanism.
- Activation or effect: fast-forward changes the owner's checkout so later coordinator checks and top-level submission consume the worker's code.
- Evidence limits: Git guards do not check semantic acceptance or prove that requested tests/review ran; no observed landing supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The model proposes the integration; software may veto it on local Git/state conditions. Human input supplies the overarching task/authorization, not mandatory per-commit approval on this route. This is open coding-task mode. Ancestry and clean state are admission predicates, not a factual expected-answer oracle. Guidance to inspect diffs and test transcripts comes from the coordinator instructions; code persists in Git. Rejected work remains for repair and renewed verification, rather than a universal automatic rollback of host effects.

> throw new Error(
>             `Target moved or diverged; update the workspace onto ${workspace.target} and verify again`,
>           )
> --- `extensions/workspaces/workspaces.ts`

> await git(source, 'merge', '--ff-only', tip)
> --- `extensions/workspaces/workspaces.ts`

### Claims

#### WF-CLM-feature-protocol
Label: Coordinator feature protocol

No counterpart after comparison with supplied runtime claims: [RT-CLM-coding-work](runtime.md#rt-clm-coding-work) gives general build/verify/report intent, whereas this claim specifies the role sequence, brief contract, review veto and reporting responsibilities. It specializes the instruction content of [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions), not a distinct instruction store. SRC-1 doctrine/design: `agents/ultimate.md`, `agents/coordinator.md`, `agents/worker.md`, `agents/reviewer.md`. Status: claimed; these texts request behavior and do not establish performance.

> You coordinate one feature, started by @ultimate for the user. You own understanding the problem, the plan, the decisions, and the final verdict. Delegate execution and reconnaissance, never judgment.
> --- `agents/coordinator.md`

> - **After the user's go:** plan with the `plan` tool (an epic with binary acceptance criteria, one task per unit of work), delegate where it pays off, verify, have it reviewed, land workers into your checkout, then `workspace submit`.
> --- `agents/coordinator.md`

> - An idle or finished worker proves nothing. Read its diff, check its citations, and read its last full test run in its transcript (`ultimate.entries(id)`): a recorded exit code is evidence, a claim in prose is not. After landing it, run only `pnpm check` and the tests covering what you changed yourself; the lander runs everything on the merged result.
> --- `agents/coordinator.md`

> Answer APPROVED only when every reviewer approved the range; otherwise NEEDS CHANGES.
> --- `agents/reviewer.md`

> Finish your report to @ultimate before you `workspace submit`: say what you built, how you verified it and its divergence from the task ("None" when it matches), since a landing reaches @ultimate as its own card and concludes you without another run. A failed submission comes back to you: fix the cause in your workspace (a flaky test at its cause, or delete it; never skip it or raise its timeout) and submit again.
> --- `agents/coordinator.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-subagent-start](runtime.md#rt-rte-subagent-start)

Workflow return interpretation: the parent receives selected final text and model identity, not an implicit full evidence dump. The coordinator policy separately requires transcript inspection before acceptance. SRC-1 implementation: `extensions/subagents/server.ts`; doctrine/design: `agents/coordinator.md`. An answer is a transport-level completion signal, not acceptance of the assignment.

> const answered = (message: AssistantMessage | undefined) =>
>   message !== undefined &&
>   message.stopReason !== 'aborted' &&
>   message.stopReason !== 'error' &&
>   textOf(message).trim() !== ''
> --- `extensions/subagents/server.ts`

#### On [RT-RTE-change-admission](runtime.md#rt-rte-change-admission)

Workflow recovery and delivery: failing checks hand control back to the submitting coordinator through an input; success writes the branch card, conditionally concludes it, then delivers to its starter. This route's software acceptance does not require a stored reviewer APPROVED verdict. Human/model judgments and configured process checks have separate roles. SRC-1 implementation: `extensions/workspaces/lander.ts`, `extensions/workspaces/server.ts`, `extensions/workspaces/workspaces.ts`. Local fast-forward, remote push and user-facing report are distinct outcomes; see the account above.

> if (outcome.outcome === 'failed') {
>           await (
>             await runtime.conversation(branch, context)
>           )?.submit(
>             {
>               type: 'input',
>               content: text,
>               entry,
>               whenBusy: 'followUp',
>               requestId: `lander:${id}`,
>             },
>             context,
>           )
> --- `extensions/workspaces/lander.ts`

> if (!(await after.working(tx, branch)))
>             try {
>               await after.conclude(tx, branch)
>               concluded = true
> --- `extensions/workspaces/lander.ts`

> if (failed !== -1)
>                 return await fail(
>                   `check failed twice: ${commands[failed]}`,
>                   results[failed].failure,
>                   'Fix it at its cause (a flaky test too: fix or delete it), verify and submit again.',
>                 )
> --- `extensions/workspaces/lander.ts`
