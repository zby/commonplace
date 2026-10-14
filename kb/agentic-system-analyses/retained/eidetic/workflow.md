---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Eidetic workflow: asynchronous session-signal extraction, compounding and selected delivery into a later session."
run-id: AAS-2026-10-14-eidetic-0e54f3c114b3-01
reviewed-boundary: "67506b62fdd0944c243537c3cb10938f7343b6b2"
---

# Eidetic workflow report

## Workflow account

### Selection and evidence

The representative workflow is a completed coding session becoming durable signals that may reach a later coding session. It is selected because the shipped installer connects both ends: asynchronous Stop extraction and SessionStart context injection. It is a memory-service workflow, not an enclosing task planner or a foreground coding-task delegation tree. Its request is the host's lifecycle event; its delivered product is retained content and, after later selection, a generated rules file. The host remains responsible for loading that file and using it. See [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound) and [RT-RTE-context-injection](runtime.md#rt-rte-context-injection). SRC-1: `install.sh`, `hooks/session-signals.sh`, `hooks/smart-memory-inject.sh`.

This account uses implementation and doctrine/design evidence at the frozen revision in [boundary](boundary.md#source-register). Added inspection traced the hook's excerpt builder, filtering, provider progression and spool drain; compounding's protected-card handling, History writer and daily signal writer; the injection hook; and project-context selection in assembly. No target code, tests or providers were executed. Neither successful execution nor improved subsequent coding behavior is established.

### 1. Host event to bounded extraction request

Claude Code supplies a transcript path through the Stop payload. Hook code rejects missing/nonexistent transcripts, sessions smaller than 1000 bytes and empty parsed excerpts. The extractor receives complete JSONL records from at most the final 2 MB, restricted to the last 20 user/assistant text turns with 1500 characters per turn. Typed tool-result blocks do not pass the text-block selector. This controls the extractor's context, not the foreground conversation: the original transcript remains on disk, while the separate invocation receives a lossy excerpt. SRC-1: `hooks/session-signals.sh`; [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound).

The handoff supplies the excerpt and a natural-language extraction contract: actual technical events only, no hypotheticals, pasted-source material or sensitive personal data, and one of five signal prefixes or EMPTY. The model proposes content; it receives no authority to decide the card destination through this protocol. Model-route identity and mutability are recorded in [RT-CMP-session-extractor](runtime.md#rt-cmp-session-extractor). These instructions request factuality and privacy; the following format check cannot verify either. SRC-1: `hooks/session-signals.sh`.

### 2. Proposal acceptance and provider failure

The shell owns provider progression. It ordinarily tries Claude first; failure or no accepted signal lines permits configured alternatives. A successful local or Antigravity result, including EMPTY, ends that provider progression. Local-only configuration prevents remote fallback after a failed local attempt. Codex has its own fallback-model branch. This is execution recovery, not independent verification of a successful model's assertions. SRC-1: `hooks/session-signals.sh`; [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound).

Only recognized prefixes followed by nonempty text survive. EMPTY or a wholly malformed response ends the extraction path without a card write:

> filter_signal_lines() {
>     printf '%s\n' "${1:-}" | awk '
>         /^(Decision|Rule|Worked|Failed|Knowledge):[[:space:]]+[^[:space:]]/ { print }
>     '
> }
> --- `hooks/session-signals.sh`

Acceptance therefore means protocol-shaped proposal, not verified memory. A human can configure the hook or subsequently edit content, but this workflow has no per-signal approval step. The separately enabled M3 driver is launched before extraction in the background. Its support gate does not validate these signals: it is a different route, [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing), not another stage in this workflow. SRC-1: `hooks/session-signals.sh`.

### 3. Coordination and deferred work

After extraction, the hook hands accepted text to a shared-lock executor. Under the lock it attempts incremental indexing, then invokes compounding with the current working directory. Index failure is ignored, so candidate selection can use stale derived state. The modern lock-runner branch spools already-extracted text when the lock reports busy; another nonempty extraction invocation can drain it. This preserves expensive proposals in a bounded retry mechanism, not an exactly-once queue. SRC-1: `hooks/session-signals.sh`; [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound).

The spool handoff has an important limit: each file contains signal text, not the originating project directory. Drain concatenates old text with current input and uses the draining invocation's CWD. Unmatched older signals can consequently be filed into that invocation's project. This is visible in the text-only enqueue and single-CWD executor call:

> printf '%s\n' "$RESULT" > "$SPOOL_DIR/$(date +%s)-$$.txt" 2>/dev/null || return 1
> --- `hooks/session-signals.sh`

> ' _ "$INDEX" "$COMPOUND" "$(pwd)" "$SPOOL_DIR" || LOCK_RC=$?
> --- `hooks/session-signals.sh`

Drain retains at most 20 spool files, dropping oldest excess. It removes remaining files only after the compound subprocess succeeds. A partially completed compound invocation can leave some durable updates before failure; retry can repeat History appends because that writer has no content-deduplication test. Daily signal addition instead checks whether each signal already occurs in the file. The legacy lock branch spools on contention but does not itself drain the spool. Thus recovery is conditional on a later invocation reaching the modern drain branch; it is neither lossless nor guaranteed eventually to run. SRC-1: `hooks/session-signals.sh`, `bin/compound.py`.

### 4. Candidate selection to durable delivery

Compounding owns destinations. It normalizes lines, extracts keywords and selects candidates through FTS and overlap/vector fallback, as established by [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound). It skips protected existing feedback/user cards. An eligible successful match receives a dated History entry; failure to absorb the signal leads to a new daily project signal entry, with possible-duplicate diagnostics where applicable. Rejecting an existing destination therefore need not reject the proposed content. SRC-1: `bin/compound.py`.

The History update does not advance `last_verified`. For managed cards, an additional best-effort Evidence event can be emitted; its source-native `observed` label is a software event, not this analysis's observation of execution. Unmatched signals are stored as project, agent-extracted entries even when the proposed line begins Rule:. No human reviews each write and no expected-answer oracle intervenes. These are bounded session extraction and matching, not an evaluation curriculum. SRC-1: `bin/compound.py`; [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound).

Temporary-file replacement makes each successful card update durable without a partially written replacement. It does not make the whole batch atomic or restore prior meaning after a bad proposal. The extraction hook is asynchronous and mostly silent: persistence, not a foreground acknowledgement, is the first delivery boundary. Summary logs or optional session-scoped signal output are not proof that a later agent received the card. SRC-1: `bin/compound.py`, `hooks/session-signals.sh`.

### 5. Later consumption and final delivery limit

A subsequent SessionStart hook attempts lexical refresh and assembly. Assembly selects project chunks by project match, recency, weighting and budget. Even when a signal or History section is indexed, it need not survive this selection, and a selected chunk is truncated:

> snippet = content[:500] if len(content) > 500 else content
> text = f"**{name or heading}** ({card_kind or typ}{status_tag}) — {short_path}\n{snippet}\n\n"
> --- `bin/assemble_context.py`

The generated file contains selected text by value and card paths as reload cues. The host's rules loader must read it for delivery into the next agent context; model compliance and changed action remain unobserved. The strict feedback-name visibility rule concerns a different card type and does not guarantee delivery of these project signals. See [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context), [RT-CLM-feedback-visibility](runtime.md#rt-clm-feedback-visibility) and [RT-RTE-context-injection](runtime.md#rt-rte-context-injection). SRC-1: `bin/assemble_context.py`, `hooks/smart-memory-inject.sh`.

Busy injection can skip; failed refresh can retain the prior index; failed assembly can leave prior generated context. The hook's final status message therefore does not certify fresh signal delivery. Cards remain available for later reindex and requested recall, but recall is an alternate consumption route, not a mandatory completion step in this workflow: [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall). SRC-1: `hooks/smart-memory-inject.sh`, `bin/assemble_context.py`.

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

#### On [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound)

Workflow checkpoint: rejection of malformed proposal text stops this path; rejection of a protected destination redirects rather than vetoing the content. The compound subprocess's successful exit is the modern spool-drain acknowledgement, not a factuality verdict or confirmation of downstream consumption. Recovery belongs to subsequent hook invocations and local operators; provider fallback and spool retry address different failure stages. Text-only deferred work does not preserve originating-project routing, and retries can repeat History updates after partial failure.

#### On [RT-RTE-context-injection](runtime.md#rt-rte-context-injection)

Workflow completion: a successful card write completes retention, while successful assembly completes only selected file delivery. End-to-end completion additionally needs the external host rules load. No inspected status message establishes that a particular newly extracted signal survived project selection and snippet truncation or changed the next agent's actions.
