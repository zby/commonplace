# Workshop: Agent Memory Design

## Question

What needs to change around [Designing a Memory System for LLM-Based Agents](../../notes/designing-agent-memory-systems.md) now that the first design study exists as a durable synthesis note?

## Why this workshop is back

The original `agent-memory-design` workshop closed on 2026-04-23 by promoting its coherent argument into `kb/notes/designing-agent-memory-systems.md` with the `synthesis` trait. That was the right closure for the first pass: the workshop had become one durable design study.

The note is now active again as an object of discussion. New questions are appearing around scope, connect-report application, silent-failure extraction, store-everything assumptions, and whether the architecture is software-specific or general across agent work surfaces. Those questions should not bloat the library note directly. They need a workshop where alternatives, objections, and candidate revisions can accumulate before promotion.

This reopened workshop is therefore a **continuation workshop**, not a rollback of the prior closure. The promoted note remains the current library artifact; this space holds discussion material around its next revision or extracted companion notes.

## Current artifact

- [Designing a Memory System for LLM-Based Agents](../../notes/designing-agent-memory-systems.md) — current synthesis note under discussion.
- [Connection report](../../reports/connect/notes/designing-agent-memory-systems.connect.md) — applied on 2026-04-23 as outbound links, reverse links, and index placements.
- [Input-vs-output-driven memory](../input-vs-output-driven-memory/README.md) — upstream workshop asking whether memory design should start from observed inputs or output requirements.
- [Life-cycle management](../lifecycle-management/README.md) — records the first closure of `agent-memory-design` as a single-file promotion with a `synthesis` trait.

## Discussion threads

1. **Scope generality.** The note has moved from software-project examples toward a broader "agent work surface" framing. Check whether that generality is earned or whether some mechanisms still depend on software-specific artifacts.
2. **Store-everything premise.** Clarify how this design relates to output-driven memory. Is store-everything a capture substrate, a temporary bootstrap, or a stable architectural commitment?
3. **Observation taxonomy.** Decide whether silent failures belong as a first-class extraction type alongside corrections, preferences, procedures, and discoveries, or whether they should sit under a broader operational-health category.
4. **Activation machinery.** Make the typed cue index more operational: what fields, matching rules, and priority budgets are minimally required?
5. **Promotion oracles.** Separate signals that identify candidates from signals that justify promotion into durable artifacts.
6. **Companion-note extraction.** Identify claims inside the synthesis note that deserve standalone notes because they are being reused as premises elsewhere.

## Working conventions

- Keep exploratory objections and alternatives here until they are stable enough to revise the note or extract a companion artifact.
- Do not link from library notes into this workshop; promote first.
- Prefer dated discussion files when a thread gets substantial, for example `2026-04-23-scope-generalization.md`.
- When the workshop produces a durable change, record it under "Graduated changes" below before closing or continuing.

## Graduated changes

- None yet for the reopened workshop.

## What would close this workshop

This continuation closes when either:

- the next revision of `designing-agent-memory-systems.md` absorbs the active discussion threads and no residual questions remain, or
- the active threads split into standalone notes/workshops and this directory no longer has a coherent center.
