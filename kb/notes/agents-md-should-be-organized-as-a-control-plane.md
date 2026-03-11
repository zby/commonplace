---
description: Theory for deciding what belongs in AGENTS.md using loading frequency and failure cost, with layers, exclusion rules, and migration paths
type: note
traits: []
areas: [kb-design]
status: current
---

# AGENTS.md should be organized as a control plane

AGENTS.md is not just a style file. It is the runtime control plane for agent behavior in a repository. Organizing it as a control plane means each instruction is placed by function, not by convenience: what must always be loaded, what can be loaded on demand, and what should be externally triggered.

The goal is to maximize decision quality per token. Every line in AGENTS.md competes with task context in every session.

Two distinct failure modes sit behind this goal:

- **Token pressure failure**: critical instructions are omitted or truncated because always-loaded context is too large.
- **Attention dilution failure**: critical instructions are present but drowned by low-value text, so execution quality drops anyway.

## Core model

Two variables determine placement:

- **Loading frequency**: does this need to be available in every session, or only for a specific operation?
- **Failure cost**: what happens if the agent misses this instruction at execution time?

Placement rule:

- **Always loaded + high failure cost** -> AGENTS.md
- **Task-specific + medium failure cost** -> skill/instruction body or task doc
- **Occasional or externally triggered** -> operations catalogue or scheduler/CI playbook

The same placement also controls both cost modes: token pressure (how much is loaded) and attention dilution (how much noise is mixed into the always-loaded layer).

## AGENTS.md layers

### Layer 1: Invariants

Rules that must hold in every session and every task:

- safety and destructive-action boundaries
- repository-wide conventions that prevent silent damage
- universal collaboration constraints

These rules are mandatory and concise.

### Layer 2: Routing

Minimal navigation for what to read and where to write:

- routing table for artifact destinations
- default fast path for uncertain cases
- references to deeper docs (`WRITING.md`, type guides, operation catalogues)

Routing should help the agent choose the next file, not execute full procedures.

### Layer 3: Escalation boundaries

Explicit "leave AGENTS.md now" triggers:

- edge-case signals
- stale-context signals

Without explicit escalation boundaries, AGENTS.md drifts into a manual.

Concrete escalation examples:

- If a task touches `kb/sources/` content and no corresponding `.ingest.md` exists, stop and run `/ingest` or load the ingestion procedure instead of improvising source classification.
- If a write target does not map cleanly through the routing table, stop and load `kb/instructions/WRITING.md` before creating or moving files.
- If a task modifies documents in a directory with a local `types/` template, stop and load that type before editing.

## Nested AGENTS.md topology

When the harness supports nested AGENTS/CLAUDE files, the control plane should be layered by scope:

- **Root file**: global invariants and top-level routing.
- **Subtree file**: local routing and local escalation triggers for that subtree.
- **Leaf file**: narrow constraints for specialized workflows in that directory.

Composition rule:

- child files may add or tighten constraints for local context
- child files should not contradict parent invariants

## Exclusion rules

The following should generally stay out of AGENTS.md:

- periodic hygiene operations (heartbeat/user/scheduler triggered)
- long procedural checklists better represented as instructions
- volatile project state (active campaign details, temporary decisions)
- high-rationale background theory that belongs in methodology notes
- capability inventories (injected or non-injected)
- externally triggered operation classes (maintenance sweeps, audits, bulk refactors)

If content is useful but not always-loaded critical, link to it instead of embedding it.

## Lifecycle of guidance

Guidance should move across artifacts as it matures:

1. Methodology note captures reasoning and tradeoffs.
2. AGENTS.md may hold a minimal invariant or routing pointer.
3. Repeated operations accumulate in a maintenance/instructions staging area.
4. Stable procedures are distilled into `kb/instructions/` or promoted to skills.
5. Deterministic high-frequency checks can codify into scripts/hooks.

This keeps AGENTS.md stable and short while the system still learns.

## Quality tests for AGENTS.md entries

Before adding a line to AGENTS.md, test:

- Is this needed in every session?
- Is omission likely to cause costly failure?
- Can the instruction be expressed in one short imperative sentence?
- Does it point to a deeper artifact instead of duplicating it?
- Does it avoid competing with task context for tokens?
- Is this a capability listing rather than an invariant/routing/escalation rule?

If most answers are "no", place it elsewhere.

## Open questions

- Should AGENTS.md include hard token budgets per section, or is that premature optimization?
- Which escalation triggers can be deterministic enough for automatic injection instead of manual judgment?
- At what reuse threshold should a staged operation move from catalogue to `kb/instructions/`?

---

Relevant Notes:

- [context-loading-strategy](./context-loading-strategy.md) — foundation: matches instruction specificity to loading frequency, the primary placement rule used here
- [agent-statelessness-makes-routing-architectural-not-learned](./agent-statelessness-makes-routing-architectural-not-learned.md) — grounds why always-loaded routing is permanent infrastructure, not optional convenience
- [periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing](./periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md) — exemplifies exclusion: periodic operations should be external to routing docs
- [maintenance-operations-catalogue-should-stage-distillation-into-instructions](./maintenance-operations-catalogue-should-stage-distillation-into-instructions.md) — operational extension: where externally triggered operations are staged before distillation
- [capability-placement-should-follow-autonomy-readiness](./capability-placement-should-follow-autonomy-readiness.md) — isolates the separate decision rule for where capabilities belong (skills vs instructions vs notes)
- [instructions-are-skills-without-automatic-routing](./instructions-are-skills-without-automatic-routing.md) — target form for mature procedures that do not need always-loaded routing
- [methodology-enforcement-is-constraining](./methodology-enforcement-is-constraining.md) — lifecycle framing for how guidance hardens from notes into deterministic enforcement
- [Context Engineering for AI Agents in OSS](../sources/context-engineering-ai-agents-oss.ingest.md) — validates: Table 1 shows 14 content categories practitioners actually put in context files, with no established structure — empirical evidence for why the control-plane model's normative layering is needed
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — exemplifies: 100-line AGENTS.md with invariants, routing, and escalation is the control-plane model in production at 1M LOC scale

Topics:

- [kb-design](./kb-design.md)
