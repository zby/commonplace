---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "ClawVault workflow account: caller-directed sleep handoff, optional observation, and next-session wake delivery."
run-id: AAS-2026-10-17-clawvault-38c16ae4ab34-01
reviewed-boundary: bd702e9cce436bc3065827714cd576e8be20c375
---

# ClawVault workflow report

## Workflow account

### Selection and evidence boundary

This account traces session continuity: an agent or operator requests `sleep`, ClawVault saves a handoff and optionally processes a transcript, and a later caller requests `wake` to receive a recovery notice and selected context. This is representative because it joins retained work state to a later agent invocation through an explicitly shipped procedure, rather than joining independent memory APIs into an invented task workflow. The underlying route is [RT-RTE-session-handoff](runtime.md#rt-rte-session-handoff); this member adds workflow-specific analysis without redeclaring it. ClawVault does not itself execute the foreground task or schedule the next session.

The source's checklist supplies the intended orchestration, not evidence of compliance:

> - [ ] Run `clawvault wake` at session start
> - [ ] Checkpoint during heavy work
> - [ ] Capture key decisions/lessons with `clawvault remember`
> - [ ] Use wiki-links like `[[person-name]]`
> - [ ] End with `clawvault sleep "..." --next "..." --blocked "..."`
> --- `SKILL.md`

Evidence is SRC-1 implementation and doctrine/design at the [boundary](boundary.md). Added inspection covers `bin/register-session-lifecycle-commands.js` sleep/wake branches, `src/commands/sleep.ts`, `src/commands/wake.ts`, handoff creation/recap selection/brief formatting in `src/lib/vault.ts`, recovery selection and flag clearing in `src/commands/recover.ts`, dirty-flag checks in `src/commands/checkpoint.ts`, and the checklist in `SKILL.md`. The code was not executed. No deployed session, host delivery, resumed task performance or benefit is established.

### Request, handoff and secondary work

The CLI receives the caller's working summary, optional next steps, blockers, decisions, questions, feeling, session key, transcript and feature switches. It resolves a vault and calls `sleep`. The function comma-splits supplied lists and rejects an empty working summary before loading the vault. Missing next steps or blockers can be requested interactively; noninteractive calls can leave them empty. The caller supplies the handoff's meaning. A generic CLI invocation does not establish whether a human or agent authored it. SRC-1, `bin/register-session-lifecycle-commands.js`, `src/commands/sleep.ts`.

The function delegates persistence to `createHandoff`, which renders Markdown plus symbolic frontmatter into a timestamp-titled document under `handoffs`. The returned document supplies the result's creation time; the function then clears the dirty flag. This is the direct storage mechanism in [RT-RTE-slot-store](runtime.md#rt-rte-slot-store), not capture-quality admission. No answer oracle checks whether the supplied work summary is accurate, complete or sufficient for resumption. SRC-1, `src/lib/vault.ts`, `src/commands/sleep.ts`.

> const document = await vault.createHandoff(handoffInput);
> const handoff: HandoffDocument = {
>   ...handoffInput,
>   created: document.modified.toISOString()
> };
> await clearDirtyFlag(vault.getPath());
> --- `src/commands/sleep.ts`

After persistence, optional qmd indexing and Git handling occur before observation. Git is a separate approval boundary: a dirty repository is committed only in interactive mode after affirmative confirmation and a nonempty message. Declining skips the commit without rejecting the handoff. The implementation stages all repository changes when approved, not merely the handoff. Noninteractive calls skip this commit path. SRC-1, `src/commands/sleep.ts`.

When an explicit or environment-selected transcript exists, `sleep` parses it and supplies message strings, source `openclaw`, transcript basename and file modification time to an `Observer`, then flushes it. This is a selected-data computation, not delegation of the caller's task to an autonomous subagent. [RT-RTE-observe-session](runtime.md#rt-rte-observe-session) and [RT-CMP-compressor](runtime.md#rt-cmp-compressor) supply the compression/admission evidence. Only its routing summary returns through `SleepResult`; durable observations remain available separately. Optional reflection receives the vault path and a fourteen-day window, as described by [RT-RTE-reflect-week](runtime.md#rt-rte-reflect-week). Neither computation receives a general grant to act in the foreground host. SRC-1, `src/commands/sleep.ts`.

### Failure, rejection and recovery ownership

The local nonempty-summary check can reject before storage. There is no analogous semantic acceptance test for next steps. Observation and reflection exceptions are swallowed individually after the handoff has been saved. This prioritizes handoff delivery over secondary memory products, but does not report a structured observation failure to the caller:

> } catch {
>   // Observational memory should never block session handoff completion.
> }
> --- `src/commands/sleep.ts`

This best-effort protection is not a transaction over the whole command. Git commit failure throws outside those catches; indexing also occurs outside them. Consequently an error can prevent the CLI's final saved-handoff message even after the handoff exists and the dirty flag has been cleared. The inspected sequence has no rollback for that prior write. The caller must distinguish failed command completion from absence of a persisted handoff. SRC-1, `src/commands/sleep.ts`, `bin/register-session-lifecycle-commands.js`.

A later `wake` owns recovery-information assembly, not task repair. `checkDirtyDeath` tests the flag and, when present, reads the last checkpoint; malformed checkpoint JSON is ignored. `recover` then selects the lexically latest handoff filename and reads its full text. Without a flag, recovery returns a clean-start object with no checkpoint, though the independent recap still reads handoffs. With a flag but no handoff, the recovery message warns of possible context loss. This is diagnostic state, not proof that all lost context was reconstructed. SRC-1, `src/commands/checkpoint.ts`, `src/commands/recover.ts`.

Wake requests flag clearing before vault loading and recap generation:

> const recovery = await recover(vaultPath, { clearFlag: true });
> await clearDirtyFlag(vaultPath);
>
> const vault = new ClawVault(vaultPath);
> await vault.load();
> --- `src/commands/wake.ts`

Thus the flag acknowledges recovery processing, not successful delivery or resumed work. A subsequent load/recap error can occur after clearing. The inspected route does not automatically retry a failed wake or re-mark the flag; the caller owns retry and resumed task decisions. SRC-1, `src/commands/wake.ts`, `src/commands/recover.ts`.

### What reaches the next caller

Recap selects three handoffs by modification time by default, plus active project titles, pending commitment titles and recent decision/lesson titles. It is distinct from recovery's filename-based handoff selection. Wake defaults to brief formatting: each handoff exposes at most two working items and its first next step; full formatting adds blockers and all next steps. Neither recap mode reproduces the entire handoff body. The durable file remains independently available. SRC-1, `src/lib/vault.ts`, `src/commands/wake.ts`.

Wake separately reads a seven-day nonarchived observation window, filters importance below 0.4, and applies age-dependent selection. Formatting caps structural observations at twenty, potential observations at ten, and assembled output at a nominal hundred lines. This bounds unsolicited reload; it does not evict or reconstruct a host model's existing window. The returned text is a by-value view, not a live reference. Older or omitted material is not thereby deleted. SRC-1, `src/commands/wake.ts`.

Optional executive summarization receives only selected work/blocker/next-step strings, up to eight project titles, five commitments, ten structural observations and five potential observations. The inspected implementation calls Gemini when its key exists; merely having an Anthropic or OpenAI key does not activate an implemented fallback. It accepts nonempty returned text without checking factual preservation and otherwise uses a deterministic work/observation summary. The external distributed-parametric model is the mutable alias `gemini-2.0-flash`, not an immutable weight pin; the request performs inference, not parameter updates, and provider internals remain uninspected. Source guidance requests a short urgent-items briefing, not theory criticism. SRC-1, `src/commands/wake.ts`.

Library delivery is the returned recovery/recap/Markdown/summary/observations object. CLI delivery prints recovery information, recap Markdown and the summary; sleep prints the saved document's ID/path after returning. There is no acknowledgement that an enclosing agent incorporated these outputs or acted on the next steps. Notably, wake can deliver its report and still return a nonzero status when recovery detected a dirty death:

> process.exitCode = result.recovery.died ? 1 : 0;
> --- `bin/register-session-lifecycle-commands.js`

A runner treating every nonzero exit as absent output would misread this contract. The implemented endpoint is context delivery to the caller, not successful execution of resumed work. No task-completion reviewer, semantic handoff veto, autonomous resumption or measured continuity improvement is established by this source trace.

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

#### On [RT-RTE-session-handoff](runtime.md#rt-rte-session-handoff)

Workflow role: caller-directed bridge between sessions. The caller owns timing, handoff semantics, retries and resumed-task decisions; code owns persistence, context selection, formatting and local error handling. Optional human Git approval gates only the Git commit, not admission of the already-written handoff. Delivery consists of return values or printed context, with no downstream task acknowledgement. The workflow's verification limits are substantive: nonempty input, flag detection and nonempty model output do not verify recovered context's adequacy. Secondary-computation catches preserve the primary handoff, while failures outside those catches can leave durable effects without a completed command. Implementation remains wired; operation remains uninspected, as in the supplied record.
