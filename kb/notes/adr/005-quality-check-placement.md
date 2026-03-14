---
description: Where quality checks belong — WRITING.md pre-save checklist vs post-write instructions (semantic-review, validate) — based on cost, false-positive tolerance, and whether the check blocks creation
type: adr
tags: []
status: proposed
---

# 005-quality-check-placement

**Status:** proposed
**Date:** 2026-03-14

## Context

The KB has multiple places where quality checks can live:

1. **WRITING.md checklist** — run before saving. Every note, every time. Currently: title-as-claim, description quality, tags, composability, explanatory reach.
2. **`/validate`** — structural checks (frontmatter, link health, type conformance). Deterministic, run on demand.
3. **`/semantic-review`** — content checks (completeness, grounding, internal consistency). LLM judgment, run on demand.
4. **Ingest skill** — source-specific checks (curiosity gate, limitations, reach assessment). Run during ingestion.
5. **Recurring tasks** — periodic sweeps (review-explanatory-reach). Batch, asynchronous.

There is no documented principle for deciding where a new quality check should go. When the [explanatory reach](../first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) check was added to WRITING.md and the ingest skill, the placement was ad hoc. This ADR establishes the routing criteria.

## Decision

A quality check's placement depends on three properties:

| Property | WRITING.md | /validate | /semantic-review | Skill-embedded | Recurring task |
|----------|-----------|-----------|-----------------|----------------|----------------|
| **When it runs** | Every save | On demand | On demand | During skill execution | Periodic sweep |
| **Cost of running** | Must be < 5 seconds of thought | Deterministic, cheap | Expensive (reads linked notes) | Bundled with skill cost | Amortized |
| **False positive tolerance** | Very low — false positives block note creation | Medium — warnings, not blocks | High — advisory, human reviews | Medium — embedded in larger judgment | High — batch triage |
| **Blocks creation?** | Yes (soft — "fix before saving") | No (post-hoc) | No (read-only) | No (analysis artifact) | No (async) |

**Routing criteria:**

1. **Put it in WRITING.md if** the check is fast (a writer can do it in their head), has low false-positive rate, and failing it means the note will be hard to find or link. These are *discoverability and composability* checks. The note must clear these to be useful at all.

2. **Put it in /validate if** the check is deterministic and structural — it can be run by a script without LLM judgment. Frontmatter conformance, link health, required sections.

3. **Put it in /semantic-review if** the check requires reading linked sources and making judgment calls about content quality. These are expensive and advisory — they improve notes but shouldn't gate creation.

4. **Embed in a skill if** the check is specific to that skill's workflow and benefits from the skill's context (e.g., the ingest skill's reach assessment benefits from having just read the source and its connections).

5. **Make it a recurring task if** the check is retrospective — it audits existing notes rather than gating new ones, or it's too expensive to run on every note.

**The explanatory reach check** straddles the boundary. The lightweight version ("does this explain why, not just what?") belongs in WRITING.md — it's fast, rarely false-positive on notes that genuinely explain a mechanism, and catches the most common failure mode (pattern recording without mechanism). The full three-part test (vary / reach / criticize) is too expensive for pre-save — it stays in the recurring task and could be added to semantic-review.

## Consequences

**Easier:**
- New quality checks have a clear home — check the routing criteria before adding.
- WRITING.md stays lightweight — only fast, low-false-positive checks that gate discoverability.
- Expensive checks don't slow down note creation.

**Harder:**
- The "lightweight version" of a check (WRITING.md) may drift from the "full version" (semantic-review/recurring task). Need to track which notes distill from which.
- Judgment calls remain on borderline checks — the routing criteria help but don't eliminate ambiguity.

---

Relevant Notes:

- [first-principles reasoning selects for explanatory reach](../first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — the quality criterion that prompted this ADR; its three-part test is split across WRITING.md (lightweight) and recurring tasks (full)
- [methodology enforcement is constraining](../methodology-enforcement-is-constraining.md) — the enforcement gradient (instructions → skills → hooks → scripts) parallels the placement gradient here; both trade flexibility for reliability
- [ad hoc prompts extend the system without schema changes](../ad-hoc-prompts-extend-the-system-without-schema-changes.md) — WRITING.md checks are the lightest form of enforcement; this ADR defines when to keep a check at that level vs. promoting it
