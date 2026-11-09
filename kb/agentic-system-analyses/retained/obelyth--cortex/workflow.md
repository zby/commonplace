---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Cortex workflow report tracing the scheduled groundskeeper from health gating through durable filing, human queue review and digest delivery."
run-id: AAS-2026-11-07-cortex-6101286707a0-01
reviewed-boundary: "65d449a3275eee51efd6ce0c275572806ee9d553"
---

# Cortex workflow report

## Workflow account

The representative workflow is the nightly groundskeeper, selected because it is a shipped multi-step agent procedure connecting memory consumption, maintenance and delivery. Unlike the returning Ask computation, it asks a host agent to choose and perform multiple tool calls. Its canonical route is [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance), with instructions reaching the host through [RT-BAP-maintenance-instructions](runtime.md#rt-bap-maintenance-instructions). This is a source-supported procedure, not a supplied successful execution. The template requires customized paths and registration in external Claude Code; Cortex does not supply that scheduler's execution or conversation-management guarantees. SRC-1, `ops/groundskeeper/SKILL.md`; [boundary](boundary.md).

Added inspection at the same frozen SRC-1 commit covers the complete `ops/groundskeeper/SKILL.md`, the complete `ops/groundskeeper/healthcheck.sh`, and the edit/write/capture implementation in `lib/brain.ts`. The skill supplies doctrine/design; the shell and TypeScript supply implementation. No target execution, private daily logs, configured task, maintenance artifact or live-state verification result was supplied.

### 1. Delegate a bounded maintenance session

The operator customizes and schedules the skill. The host agent receives a natural-language job list, tool names and conservative rules. It is told to use MCP writes rather than editing the private repository directly, retain correction history, and count a returned commit SHA as save evidence. There is no described subordinate agent launch: delegation is from the operator/scheduler to one host agent, then from that agent to Cortex's deterministic tools. The host selects semantic content and next actions; Cortex owns the authenticated tool implementations. These instructions do not establish that a deployed host obeys them. SRC-1, `ops/groundskeeper/SKILL.md`; [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write).

### 2. Gate the session before mutation

The first handoff is a shell invocation supplied with deployment URL and connector secret, or a configuration-file path. `healthcheck.sh` reads the trusted roster from `lib/tool-roster.json`, sends a tools/list request over the secret-URL MCP route and compares the extracted tool-name set with that roster. A match exits zero; mismatch prints UNHEALTHY and exits one. It tests the connector route and tool registration, not note correctness, model answers or all database operations. Its update lookup compares public release metadata with the local package version, not a remotely authenticated deployed version. A newer release is advisory and does not fail health. SRC-1, `ops/groundskeeper/healthcheck.sh`.

The agent must then call `brain_context`. That adds a memory-read check and supplies bounded boot context through [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). The procedure explicitly stops mutations if either half fails:

> If either fails, write
> nothing and report.
> --- `ops/groundskeeper/SKILL.md`

This is a host/model policy veto, not a prerequisite encoded into every trusted write. The health-failure branch therefore ends in an external report, not a `brain_capture` digest: the first-job prohibition governs the later digest instruction. The destination of that external report is unspecified. The agent must not run an update unattended. Neither scheduling a retry nor automatic repair is established by this procedure. SRC-1, `ops/groundskeeper/SKILL.md`; [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance).

### 3. Read activity, file durable items and mark completion

On the healthy branch, the agent requests yesterday's and today's daily logs through `brain_read`, chooses decisions/status changes/facts worth retaining, reads destination project or note pages, and submits updates. The handoff supplies paths and note text; the host interprets what deserves filing and how to preserve the destination's structure. There is no reference-answer oracle or compulsory per-item human approval for this filing. Code can reject malformed writes or unsafe edit matches, not determine whether the proposed fact is true. SRC-1, `ops/groundskeeper/SKILL.md`, `lib/brain.ts`; [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write).

The procedure keeps source logs and appends an absorption marker after filing. However, its literal skip predicate and emitted marker differ:

> Skip any log
> already containing `[groundskeeper: absorbed]`.
> --- `ops/groundskeeper/SKILL.md`

> Leave the log intact; append
> `[groundskeeper: absorbed <date>]` when done.
> --- `ops/groundskeeper/SKILL.md`

The dated form does not literally contain the closed undated token. A host could interpret the intended marker family, but exact-match completion detection is not established. More generally, filing several pages and then marking a log is not one atomic operation. Interruption can leave some pages changed and the marker unwritten; the source does not provide a durable per-log transaction or replay key. The instruction to read existing pages reduces duplication by policy, not by an exactly-once guarantee.

The persistence handoff uses [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write): `writeNote` validates and derives content, writes through GitHub, then attempts index regeneration. An index failure returns a warning beside the commit SHA, not rollback of the note. The returned SHA confirms a reported commit, whereas missing output is not proof that no write happened. That matters if the host retries after transport loss. SRC-1, `lib/brain.ts`; the runtime record retains the ordinary-write recovery limit.

### 4. Verify bounded drift and defer queue decisions

The host next selects at most four pages, prioritizing modifications in the last seven days and then least-recently-checked pages. It is asked to check live-dependent claims such as PRs, URLs and deployments. Corrections preserve old wording with a was/updated convention or SUPERSEDED marker; unverifiable claims get dated uncertainty, and clean pages get a verification date. This is a requested verification policy, not demonstrated inspection of external services. The template does not supply a complete checking algorithm or the host's external evidence grants. SRC-1, `ops/groundskeeper/SKILL.md`.

A surgical correction can use the existing edit path. `applyEdit` refuses zero or multiple exact matches; on a supported SHA-conflict retry, the write re-applies the edit against fresh content and repeats uniqueness checks. The host can recover from an exact-match rejection by rereading and supplying an unambiguous passage, but no automatic semantic correction is established. This is structural rejection of the edit target, not validation of the new assertion. SRC-1, `lib/brain.ts`; [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write).

Next, `brain_proposals` returns guest submissions for reporting. The groundskeeper flags pending proposals and those older than 21 days, but explicitly leaves accept/reject to a human. That is a restriction of this workflow, not a restriction of all trusted tools: [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission) permits a trusted caller to decide. Queue expiry after 30 days bounds the review opportunity. The prompt's phrase “only guaranteed review” is an aspiration contingent on host scheduling and completion, not an implementation guarantee. SRC-1, `ops/groundskeeper/SKILL.md`.

### 5. Deliver a digest, or deliberately deliver no write

After a healthy run, changes, breakage, pending proposals or update availability call for one short `brain_capture` entry tagged `groundskeeper`. A quiet run calls for no write. The agent must leave overflow for tomorrow and say so. SRC-1, `ops/groundskeeper/SKILL.md`:

> If it was a quiet night, write NOTHING — silence is
> the correct output.
> --- `ops/groundskeeper/SKILL.md`

`capture` converts the submitted text and tags into a timestamped entry in the current day's log, appends through GitHub and returns path, commit SHA and any index warning. The digest is therefore a retained daily-log artifact, not an ephemeral model answer. It can become input to a later groundskeeper log read or another context consumer; useful downstream action remains unobserved. Delivery of each note or digest is supported by its returned commit receipt under the tool contract, not by a separate supervisor's acceptance of the whole nightly job. SRC-1, `lib/brain.ts`; [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

The workflow thus has concrete server-side persistence and edit rejection, but host-owned semantic verification, completion tracking and recovery across calls. No supplied trace establishes that the task ran, that all selected facts were checked, that a human reviewed reported proposals, or that the resulting notes improved later answers.

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

#### On [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance)

Workflow role: the selected end-to-end maintenance procedure. Health rejection terminates before writes; semantic filing, drift checking and digest selection remain host decisions. Completion is distributed over individual tool receipts rather than one atomic nightly transaction. The absorption-marker spelling mismatch limits a literal replay-suppression reading. Delivery is conditional: report-only on failed health, retained digest on noteworthy healthy runs, and no write on a quiet healthy run. The detailed handoffs and newly inspected evidence are retained in the account above.

#### On [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write)

Workflow role: persistence and structural rejection boundary for filing, corrections and digest capture, not semantic acceptance of nightly maintenance. Added implementation evidence, SRC-1, `lib/brain.ts`:

> const n = text.split(find).length - 1;
> --- `lib/brain.ts`

> `edit failed: the text to replace appears ${n} times in ${path} — include more surrounding context so it matches exactly once`
> --- `lib/brain.ts`

The edit path checks uniqueness before mutation and on conflict re-derivation; a rejected edit needs fresh caller attention rather than guessed placement. Derived-index failure does not undo a committed note or capture:

> let indexWarning: string | undefined;
>   try {
>     await regenerateIndexes();
>   } catch (e) {
>     indexWarning = e instanceof Error ? e.message : String(e);
>   }
>   return { path, commitSha, indexWarning };
> }
>
> /** Replaying a receipt repairs the current derived index without replaying a note mutation. */
> --- `lib/brain.ts`

#### On [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission)

Workflow role: deferred decision handoff. The selected groundskeeper only reports pending and aging proposals; it does not complete acceptance itself. The human decision restriction is carried by the groundskeeper instructions, while the generic trusted acceptance route has a broader caller policy. No supplied artifact closes that human handoff.
