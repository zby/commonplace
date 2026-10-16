---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "cass_memory_system workflow account: explicit session reflection through model handoffs, admission, durable delivery and retry at the frozen revision"
run-id: AAS-2026-10-13-cass-memory-system-30c18219cf68-01
reviewed-boundary: "8aca3bbb6732321dca041b32c155617784687897"
---

# cass_memory_system workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is `cm reflect --session <transcript> --json`: turn one coding session into retained guidance, then make admitted guidance available to a later task. It is selected because the shipped reflection driver connects evidence acquisition, two model roles, rejection, concurrent-writer coordination, persistence and a later consumer. It is not a workflow for completing the original coding task. The originating agent has already produced the transcript; CM owns memory processing, while the enclosing agent owns future task execution. This account extends [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update) and its downstream [RT-RTE-context-read](runtime.md#rt-rte-context-read), rather than declaring those referents again (SRC-1: `src/commands/reflect.ts`, `src/orchestrator.ts`, `src/commands/context.ts`).

Evidence is inspected implementation at the [frozen boundary](boundary.md), not an execution trace. No target commands, tests, services or model calls were run. Successful extraction, faithful model judgment, deployed automation and useful later behavior remain unobserved. Added inspection under SRC-1 covers selected reflection CLI output and orchestration ranges, diary extraction/save, reflector formatting/iteration, prompt construction, validation, curator add/duplicate handling and retry classification in `src/commands/reflect.ts`, `src/orchestrator.ts`, `src/diary.ts`, `src/reflect.ts`, `src/llm.ts`, `src/validate.ts`, `src/curate.ts` and `src/tracking.ts`. All are implementation evidence within the registered commit, not additional sources.

### Request and coordinated preparation

The CLI passes normalized session, workspace, force and dry-run options plus a progress callback to the orchestrator. The orchestrator takes a workspace reflection lock and loads processed-session state and a merged playbook snapshot. It holds the reflection lock across model work, but defers playbook merge locks until admission. This serializes cooperating reflection runs for that workspace without holding shared playbook locks during slow model calls (SRC-1: `src/commands/reflect.ts`, `src/orchestrator.ts`).

An explicitly named new or failed session is eligible. A previously processed session needs a watermark to be reconsidered without force. With a watermark, CM exports records and supplies only newly appended records to diary generation. If the transcript was rewritten or has no new records, it skips extraction and can refresh bookkeeping. A forced full pass can regenerate rule proposals but suppresses helpful/harmful judgments on already-graded material. These controls separate new evidence from repeat grading; they do not guarantee that every historical session was found or exported correctly (SRC-1: `src/orchestrator.ts`; [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)).

### Model handoffs and information boundaries

CM delegates summarization to the diary extraction model with sanitized session content and metadata. The normal full-session branch re-exports markdown inside `generateDiary`; the earlier text export supports skip and grading decisions. The incremental branch passes its prepared continuation content directly. Code assembles the diary, adds metadata and related-history enrichment, and saves it before reflection. The diary is an intermediate durable artifact, not evidence that a playbook change has been accepted (SRC-1: `src/orchestrator.ts`, `src/diary.ts`).

CM next delegates rule proposals to the reflector. Its actual input contains diary status, accomplishments, decisions, challenges, preferences and key learnings; existing bullets carry IDs, maturity symbols and feedback counts; history supplies at most three related-session snippets. Prompt construction further truncates existing-bullet and history strings separately to 20,000 characters. Thus the reflector does not receive an unrestricted transcript or a guaranteed complete playbook. These selection and transformation steps bound any conclusion about the evidence it considered (SRC-1: `src/reflect.ts`, `src/llm.ts`; [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet)).

The reflector returns schema-constrained deltas. Code normalizes nullable fields, injects session provenance on additions, deduplicates proposals and stops according to configured iteration limits or early-exit policy. Repeated calls use the same formatted snapshot and history; the later-pass instruction asks for missed insights, but does not pass accepted revisions or prior criticism into the next prompt. The loop is therefore a repeated proposal pass, not evidence of iterative criticism. Provider selection and structured-response retries belong to [RT-CMP-generation-model](runtime.md#rt-cmp-generation-model); they do not supply factual verification (SRC-1: `src/reflect.ts`, `src/llm.ts`).

### Verification and decision ownership

The orchestrator submits each proposed delta to `validateDelta`. Non-add changes, disabled validation and very short additions bypass the historical gate. Other additions encounter a retrieved-evidence heuristic; some are automatically accepted, uncorroborated draft candidates can be accepted without a validator call, and remaining candidates go to a model validator. A false validity result excludes that delta; an accepted refinement can replace proposed addition text. The software decides whether returned judgments permit progression. No expected correct rule or independent answer oracle is supplied, and starting reflection is not human approval of each proposed rule (SRC-1: `src/orchestrator.ts`, `src/validate.ts`; [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)).

Validation is not the final writer. Under global-then-repository locks, CM reloads fresh playbooks, decomposes merge proposals, routes changes to their targets and invokes curation. The curator rejects malformed additions and skips duplicates of deprecated rules. Active exact duplicates in the writable target can instead reinforce an existing rule; duplicates confined to another layer are skipped. In the inspected add branch, conflict detection produces warnings, not a blanket veto. Consequently “validation passed,” “delta generated,” “new rule saved” and “rule shown to a later agent” are different milestones (SRC-1: `src/orchestrator.ts`, `src/curate.ts`).

Inline feedback extracted from eligible transcript text is appended separately from validated reflector proposals. IDs with explicit inline feedback are excluded from automatic outcome classification to avoid duplicate grading. Outcome-derived feedback runs after the merge. These labels are source-fed judgments, not independent proof that the referenced rule caused success or failure (SRC-1: `src/orchestrator.ts`; [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update)).

### Rejection, recovery and delivery

A reflector error before any completed iteration becomes a session failure rather than permanent “processed with zero deltas.” The orchestrator records the error, failure count and retry state while preserving an earlier watermark. Discovery retries failures immediately below its configured threshold, then uses exponentially increasing cooldown capped at 30 days. An explicit failed-session request bypasses discovery cooldown. If a later reflector iteration fails after a completed pass, earlier proposals remain available for validation; that is partial progress, not an all-or-nothing computation (SRC-1: `src/reflect.ts`, `src/orchestrator.ts`, `src/tracking.ts`).

Rejecting a proposal does not itself fail the session. A successful reflection whose proposals are all filtered can still be committed as processed. A missing export instead throws; very short sessions and CM's own marked model-subprocess transcripts are skipped and recorded with zero deltas. These different paths prevent conflating no useful proposal, unavailable evidence and suppressed self-generated input (SRC-1: `src/orchestrator.ts`).

For committing runs, playbook saves precede processed-log append. Routing to another repository can fall back to project-scoped global storage if that repository cannot be written. These are recovery mechanisms, not a transaction spanning all files: repository/global saves, processed-state append and post-merge outcome work are separate effects. Outcome failure is caught and reported after the core persistence step. A failure between saves and the processed mark can leave durable work eligible for retry; duplicate handling mitigates repeated additions but does not prove crash-safe semantic rollback (SRC-1: `src/orchestrator.ts`; [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)).

Delivery has two boundaries. The CLI returns global/repository/project curation results, errors and automatic-outcome metadata; per-session failures are also envelope warnings. Durable delivery means admitted playbook changes have been saved for subsequent readers. A later context request reloads current state and selects active applicable guidance; it need not select every newly admitted rule. External-agent use and task completion are outside CM's delivery guarantee. Likewise a detached hook's PID is only initiation, not this completion milestone (SRC-1: `src/commands/reflect.ts`, `src/orchestrator.ts`; [RT-RTE-context-read](runtime.md#rt-rte-context-read), [RT-CLM-automatic-learning](runtime.md#rt-clm-automatic-learning)).

Dry-run is a bounded alternative: it returns collected deltas before merge and processed-log commit, but diary generation/save has already occurred. It previews proposed rule changes, not a guarantee of zero filesystem effects (SRC-1: `src/orchestrator.ts`, `src/diary.ts`).

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

#### On [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)

Workflow-specific milestones are diary persistence, proposal production, validation, fresh-state curation, playbook persistence, processed-log append and terminal reporting. The orchestrator owns sequencing and recovery; model roles supply extracted descriptions or judgments. No per-delta human approval is wired into this path. Witnesses below establish implementation, not successful operation (SRC-1: `src/orchestrator.ts`, `src/diary.ts`, `src/llm.ts`, `src/reflect.ts`, `src/curate.ts`, `src/tracking.ts`, `src/commands/reflect.ts`).

Diary delivery precedes rule admission:

> await saveDiary(enrichedDiary, config);
> --- `src/diary.ts`

The reflector's bullet/history view is additionally bounded at prompt construction:

> const safeExistingBullets = truncateForContext(existingBullets, { maxChars: 20000 });
> const safeCassHistory = truncateForContext(cassHistory, { maxChars: 20000 });
> --- `src/llm.ts`

Admission of an individual proposal is conditional; rejected validity does not enter the validated list:

> if (validation.valid) {
>   // Apply LLM refinement if suggested
>   if (validation.result?.refinedRule && delta.type === "add") {
>     delta.bullet.content = validation.result.refinedRule;
>   }
>   validatedDeltas.push(delta);
> }
> --- `src/orchestrator.ts`

Curation's malformed-add veto and warning-only conflict treatment are distinct:

> logDecision(decisionLog, "add", "rejected", "Missing required content or category", {
> --- `src/curate.ts`

> // Conflict detection (warnings only)
> --- `src/curate.ts`

Partial reflector progress can survive a later iteration error; only failure before a completed iteration sets the failure result:

> if (completedIterations === 0) {
>   failure = err instanceof Error ? err.message : String(err);
> }
> --- `src/reflect.ts`

Discovery's retry delay is state-dependent rather than a permanent failure veto:

> const exponent = Math.min(failures - policy.maxFailures, 20);
> const cooldown = Math.min(policy.cooldownMs * 2 ** exponent, MAX_SESSION_RETRY_COOLDOWN_MS);
> return last + cooldown;
> --- `src/tracking.ts`

The parent record retains the processed-after-persistence witness. Post-merge outcome failure is separately surfaced rather than rolling back playbooks:

> errors.push(`Auto-outcome recording failed: ${msg}`);
> --- `src/orchestrator.ts`

CLI delivery exposes errors both in result data and envelope warnings:

> { startedAtMs, warnings: result.errors.length > 0 ? result.errors : undefined },
> --- `src/commands/reflect.ts`

Dry-run returns before the merge, after the diary stage:

> if (options.dryRun) {
>   return {
>     sessionsProcessed,
>     deltasGenerated: allDeltas.length,
>     dryRunDeltas: allDeltas,
>     errors,
>   };
> }
> --- `src/orchestrator.ts`
