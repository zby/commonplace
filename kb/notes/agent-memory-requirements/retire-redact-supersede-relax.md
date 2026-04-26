---
description: "Memory systems need lifecycle operations for redaction, decay, supersession, retirement, relaxation, and temporal validity"
type: kb/types/note.md
traits: [has-external-sources]
tags: [agent-memory, context-engineering]
status: current
---

# Retire, Redact, Supersede, And Relax Memory

Learning is incomplete without forgetting and revision. Raw traces can contain secrets or obsolete assumptions. Observations can be duplicates, wrong, low-value, or superseded. Cues can grow stale. Policies can become too broad. Tests can fossilize temporary workarounds.

Append-only capture is useful for provenance. Indexes, extracted observations, and activated policy surfaces still need redaction, decay, supersession, retirement, and relaxation. This is context efficiency as lifecycle work: every stale artifact competes for attention, search rank, review time, or behavioral authority.

## Methods

- Retention classes and redaction status on traces before model extraction.
- Candidate, accepted, superseded, rejected, and retired states on extracted observations.
- Periodic triage for observation inboxes: promote, fold into an existing artifact, keep, reject, or delete.
- Duplicate clustering and source consolidation for repeated observations.
- Recency decay tempered by consequence and recurrence, so old high-impact corrections do not disappear merely because they are old.
- Retirement tests for cues that fire often but do not change behavior or produce too many false positives.
- Relaxation paths from rigid enforcement back to prose guidance when a codified rule proves brittle.

## Temporal Memory

Some domains also need queryable temporal memory, not only lifecycle labels. Supersession answers "what is current?"; temporal memory answers "what was true then?" Graphiti's bi-temporal edge model, summarized in the [comparative review](../../agent-memory-systems/agentic-memory-systems-comparative-review.md), is the clearest reviewed case: validity and invalidation timestamps support point-in-time queries and temporal contradiction handling. Flat files can approximate this with provenance, dated decisions, and git history, but systems that need temporal recall should treat time as a query dimension.

## Related Systems

Reviewed systems show both partial fulfillment and a common failure mode. cass-memory has candidate/established/proven/deprecated states, harmful-feedback weighting, and decay. REM defines `active`, `contradicted_by`, and `superseded` columns but does not wire them into an actual update path. Lifecycle metadata becomes memory management only when some process reads and acts on it.

## Evaluation Questions

- Does lifecycle metadata drive actual processes?
- Can the system redact sensitive traces before extraction or reuse?
- Are obsolete cues, policies, and generated views retired or relaxed?
- Can the system answer temporal questions when current-state memory is insufficient?

---

Relevant Notes:

- [Context efficiency is the central design concern in agent systems](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) - explains why stale memory has a real cost
- [Designing a Memory System for LLM-Based Agents](../designing-agent-memory-systems.md) - derives lifecycle from context pressure and source authority
