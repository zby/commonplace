---
description: "Compare ways to handle unfinished agent workflows after code changes: pin the implementation, preserve replay compatibility, migrate state or restart, accounting for repeat costs and surviving effects."
type: types/note.md
traits:
  - has-comparison
tags: []
---

# Workflow compatibility across implementation changes

When an agent workflow's implementation changes while a run is unfinished, what should happen to the work already done? The run can finish under the old implementation, continue under compatible revised code, resume from migrated state, or restart. The choice depends on the cost of preserving unfinished work compared with repeating it, and on effects that cannot simply be repeated or discarded.

For agent-operated KB workflows, this includes changes to source checking, drafting, review and publication. The compatibility problem concerns what the old run's progress means under the revised workflow, not just whether its records can still be read.

## What continuation must preserve

An unfinished run contains decisions and partial results produced under one implementation. A changed implementation may expect different stages, record formats, validation conditions or meanings for completion markers. Continuing under the new implementation requires establishing which parts of the old state remain valid and which need further work.

Suppose a KB-writing workflow previously drafted before checking its sources. A revision moves source checking before drafting. An old run's “draft complete” marker does not establish that the new prerequisite was satisfied. The existing draft might still be usable, but continuation must account for the missing check. Reading the marker successfully is not enough.

Persisting state outside the worker does not settle this issue. A short-lived worker still has to interpret the long-lived records it receives. Separating data from code can make state easier to inspect and migrate; it does not establish compatibility between old records and new behavior.

## Options for an unfinished run

| Option | How it handles the change | Main cost or obligation |
|---|---|---|
| Pin the old implementation | Finish the run under the implementation that started it | Keep the old execution environment available; the run does not receive the revision |
| Preserve replay compatibility | In a replay-based workflow, keep revised code consistent with the run's recorded execution history | Maintain version branches or other constraints required for safe replay |
| Migrate intermediate state | Translate old records into state the new implementation can consume | Check record structure, meaning and whether completed work meets the revised requirements; repeat work where needed |
| Restart | Abandon intermediate execution state and execute the revised workflow from declared inputs | Repeat model calls, tool use and elapsed work; account for effects the old run already produced |

Pinning avoids interpreting old progress under new rules, but it is unsuitable when the revision must apply to the unfinished run—for example, when the old implementation has an unacceptable validation defect. Replay compatibility and migration preserve work by carrying explicit compatibility obligations. Restart discards that work to avoid those obligations for the discarded state.

The options can be combined. A system can restart analysis while retaining a downloaded source whose validity is independent of the changed workflow. Selective reuse moves the compatibility check to each reused artifact: its assumptions and validation must still hold.

## Effects that survive the choice

Abandoning a run does not undo a published note, sent message or external mutation. Restarting can duplicate those effects; migration or replay can also repeat them if the revised workflow misinterprets their completion state.

The relevant boundary is between private intermediate work and effects visible outside the run. Isolated drafts can be discarded. Published results and external effects need reconciliation regardless of how execution continues. A new run also needs isolation from stale intermediate outputs so it does not mistake them for its own validated results.

Restart additionally depends on recoverable inputs. If repeated access to an external system changes the task, restarting is not simple recomputation. Even with identical inputs, nondeterministic model behavior can produce a different result. The new run must meet its acceptance conditions independently.

## Comparing the costs

The comparison includes token expenditure, elapsed time, human review, compatibility maintenance and reconciliation of surviving effects. Preserving progress is valuable only relative to the work it saves and the obligations it adds.

For a KB workflow whose main repeat cost is affordable model usage, restarting may be cheaper than maintaining continuation across implementation changes. That is a design hypothesis, not a measured result. Expensive human approvals, scarce observations or long delays can make preserving completed work more valuable. Irreversible effects constrain every option; they are not by themselves a reason that continuation is safe.

## Scope

This note concerns implementation changes, not recovery from ordinary process interruption. A workflow can persist progress for crash recovery while rejecting continuation after a relevant implementation change.

Central versus distributed coordination is a separate choice. Either arrangement can pin implementations, migrate records or restart work. Moving state out of a long-running worker does not by itself require abandoning a central coordinator.

## Open Questions

- Which implementation changes invalidate continuation, and which leave the unfinished run's assumptions intact?
- At what observed repeat cost does selective reuse become cheaper than full restart, including the cost of checking reuse validity?
