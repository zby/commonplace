---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Claude Context Guard's itemisation workflow: confirmed scope, delegated insertions, sidecar checks, source restoration and delivery."
run-id: AAS-2026-10-13-claude-context-guard-357cd90664df-01
reviewed-boundary: efcd0a1815887483a862b32bfb3fbfd6aac79aa6
---

# Claude Context Guard workflow report

## Workflow account

The representative workflow is `/itemise`, especially its large-file branch. It is selected because one shipped procedure connects human scope approval, foreground planning, delegated edits, verification, failure recovery and a final report. This is not a reconstruction from unrelated capabilities. The procedure belongs to [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code); this member adds workflow detail rather than declaring that same route again. Evidence is doctrine/design in SRC-1, `.claude/commands/itemise.md`, read completely at the frozen revision. The runtime record supplies the retained passages for delegation and integrity rejection. No consumer execution, worker transcript, modified source, sidecar or verification result was supplied. The account therefore describes requested coordination, not successful delivery.

### Request and human acceptance of scope

A user invokes `/itemise` in Claude Code. The foreground model first locates Context Guard's `CLAUDE.md` and checks `ITEMISATION:`. A disabled setting stops the procedure with an activation message; an enabled or absent setting proceeds. The agent asks for files or directories, supplies default code extensions and exclusions, lists exact candidate files and waits for confirmation before touching them. The human can narrow scope or decline. Existing numbered comments trigger a further continue-or-skip question; `/itemise force` skips that warning, not initial scope confirmation. These are model-interpreted gates, not executable package checks (SRC-1, `.claude/commands/itemise.md`; [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code)).

> Wait for their answer. Then list the exact files you will process and ask them to confirm before touching anything.
> --- `.claude/commands/itemise.md`

### Preparation and consequential delegation

For each accepted file, the foreground agent is instructed to copy a sibling `.itemise-backup`, read the source in full, decide labels and end-marker insertion points, and preserve existing code and comments. Labels express the source's “one job, one address” navigation rule; language-specific comments and optional `[calls: N.M]` references provide the addressing surface. The task is labelling, not refactoring. The human approves files, while the agent decides the individual numbering and descriptions (SRC-1, `.claude/commands/itemise.md`; [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code)).

Small files are edited directly. The large-file branch assigns insertion work to a host sub-agent: the foreground agent determines the insertion list, then supplies the filename, specific labels and target locations, Edit-only instructions, bottom-to-top ordering and a prohibition on changing existing content. Planning and later verification stay with the foreground agent. This divides execution from acceptance; the delegated completion is not itself proof of correctness (SRC-1, `.claude/commands/itemise.md`; [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code)).

The threshold text is inconsistent at the boundary: the heading says “500+ lines”, the mandatory sentence says “over 500”, and the direct-edit sentence says “under 500”. Exactly 500 lines has no unambiguous branch. This limits a precise threshold claim, not the established existence of large-file delegation. The command's allowed-tools header also omits the requested Agent tool. Whether the host permits that handoff, and what context or isolation it supplies, remains uninspected. The explicit task packet does not establish the worker's complete model-visible context (SRC-1, `.claude/commands/itemise.md`; [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code)).

### Verification is retained by the foreground agent

After editing, the procedure requests three distinct checks. First, a model self-check asks whether each number identifies one job; overly coarse regions receive additional sub-numbers. This evaluates granularity, not source preservation, and is not an independent critic. Second, the agent generates or updates a neighboring `<source>.index.md`. New descriptions are written for sections shorter than 50 lines; longer ones receive a blank placeholder. Existing descriptions are preserved verbatim, rows for missing numbers are deleted, new rows added and changed rows dated. Third, source marker numbers and sidecar row numbers must have identical sets before integrity checking proceeds (SRC-1, `.claude/commands/itemise.md`).

> **Why this step is mandatory:** the Step 5 integrity check verifies that no code was changed, but it does NOT verify granularity. An agent can apply the rules mechanically and end up with one number covering 30 lines of multiple distinct concerns, and Step 5 will still pass. Granularity is a separate failure mode and must be caught here.
> --- `.claude/commands/itemise.md`

> 5. **Fail:** report which numbers are unmatched and on which side. Do not proceed to Step 5 until parity is restored.
> --- `.claude/commands/itemise.md`

The integrity reference is the backup, not an external correct answer. The instructed shell comparison removes matching numbered-comment lines from both versions, removes carriage returns and ignores blank-line differences. No diff output is the requested pass condition; output means failure and immediate restoration. The check can reject remaining source differences, but it does not prove byte preservation or semantics. It intentionally disregards some comments and whitespace. Sidecar parity checks number-set correspondence, not description accuracy or whether preserved descriptions still identify the same job after renumbering. The source supplies no separate semantic correspondence check for that latter case (SRC-1, `.claude/commands/itemise.md`; [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code)).

### Failure ownership and recovery limits

A rate limit or timeout in the delegated branch returns responsibility to the foreground agent: it logs outstanding insertions and retries. The source does not specify a retry bound, durable retry-ledger format or automatic determination of which partial edits already landed. Recovery therefore requires correct foreground accounting; there is no evidenced exactly-once insertion guarantee (SRC-1, `.claude/commands/itemise.md`).

> 4. If the sub-agent fails (rate limit, timeout), log remaining insertions and retry
> --- `.claude/commands/itemise.md`

A source/sidecar disagreement stops generation and is reported to the human rather than admitting a partial sidecar. A parity failure blocks integrity verification until repaired. An integrity failure restores that file from its backup, deletes its backup after restoration and reports the reason and diff. Successful files remain edited even when another fails: this is per-file recovery, not batch rollback. Sidecar generation occurs before the source integrity check, and the restoration command names only the source. There is no paired sidecar-restoration instruction in these steps, so restoring source does not establish restored pair consistency. These limits qualify recovery without claiming that inconsistency occurred in a supplied run (SRC-1, `.claude/commands/itemise.md`; [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code)).

> If at any point during sidecar generation you cannot reconcile a numbered marker in the source with a sidecar row (for example, the marker pattern doesn't parse, or a row has a number you can't find in the source), stop and report the mismatch to the user. Do not write a partial sidecar.
> --- `.claude/commands/itemise.md`

> - Leave successfully-itemised files in place
> --- `.claude/commands/itemise.md`

### What counts as delivered

Requested successful completion comprises edited source, a corresponding sidecar, granularity/parity/integrity checks, backup cleanup and the final summary. The summary lists updated files, section/function counts, sidecar row and blank-description counts, failures/restorations and usage advice. It permits mixed success rather than requiring all files to succeed. No final human acceptance or automatic Git commit is specified by this command. Delivery is thus local filesystem changes plus a foreground report, not a worker completion signal or published artifact (SRC-1, `.claude/commands/itemise.md`; [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code)).

The intended later consumer reads the compact sidecar, chooses a relevant number, greps source boundaries and loads only those lines. This gives an on-demand file-loading path: the full source remains reachable on disk, rather than being erased from storage. Large-file delegation does not spare the foreground its initial full-file read; the handoff isolates insertion work only to the extent the opaque host supplies a separate worker context. Claimed token savings, actual later consumption and fidelity of subsequent navigation remain unobserved (SRC-1, `.claude/commands/itemise.md`; [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code)).

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

#### On [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code)

Workflow-specific acceptance sequence: scope confirmation precedes backups; foreground planning precedes delegated insertions; granularity review precedes sidecar generation; number-set parity precedes filtered source comparison; cleanup and summary follow the per-file result. The foreground agent owns planning, retries, acceptance checks and delivery. The worker is assigned insertions, not acceptance authority. Worker failure leads to remaining-insertion logging and retry; integrity failure leads to source restoration with successful peers retained. Exactly-500-line routing and paired sidecar restoration are unresolved by the local procedure. These are refinements of the supplied route, not a distinct referent. Evidence and minimum retained passages are in the workflow account above, from SRC-1, `.claude/commands/itemise.md`.
