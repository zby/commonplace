# Scaffolding Relaxation

## Question

What, if anything, did Fable make obsolete in agent scaffolding, and does that agree with our current theory?

The point of this workshop is to avoid prematurely promoting a clean note. The current discussion suggests the first formulation was too broad: "stronger models obsolete model-management scaffolding" hides multiple mechanisms.

## Source Context

Recent ingests that triggered the question:

- [claude-workstream-kit-fable-agent-scaffolding](../../sources/claude-workstream-kit-fable-agent-scaffolding.ingest.md) -- Fable reportedly made a larger private scaffolding system shrink to a small workstream kit; what survived was project-scoped state, evidence gates, human closure, lifecycle, and session-start activation.
- [building-a-good-vertical-agent](../../sources/building-a-good-vertical-agent-2065190286519906657.ingest.md) -- argues that strong vertical agents still need carefully engineered context tiers, compressed hot-path wrappers, curated specs, and raw-reference escape hatches.

Relevant theory already in the KB:

- [fixed artifacts split into exact specs and proxy theories](../../notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md)
- [codification and relaxing navigate the bitter lesson boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)
- [system-definition artifacts are crystallized reasoning under context scarcity](../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md)
- [operational signals that a component is a relaxing candidate](../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md)
- [session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md)
- [symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md)

## Current Working Distinction

The likely distinction is not "old model vs new model" or "scaffolding vs no scaffolding." It is closer to:

> Scaffolding recedes when a task moves inside the model's reliable competence envelope, but reappears at the frontier.

That makes model-management scaffolding relative to the task/model pair. A stronger model may follow short principle-level instructions for yesterday's hard tasks. When pushed to today's hard tasks, decomposition, checklists, verification, scoped subagents, and enforcement may become useful again.

This differs from state/context scaffolding. Better models cannot recover work state that is not present. If the session was compacted, switched machines, or closed, the model does not know the project's current workstream state and may not know what to ask for. This supports the symbol-availability bound: context selection can react to available symbols, but missing project state needs an external surface that makes it observable.

## Candidate Categories

**Competence scaffolding**

Helps the model do work near the edge of its current capability: procedural checklists, decomposition prompts, compliance scripts, retry structures, verification passes. This category is likely to relax as model capability improves, then reappear at the new edge.

**State/context scaffolding**

Makes external state available: active work pointers, decisions, blockers, current next action, open questions, archive state, project-specific memory. This does not disappear with better models because the missing information is outside the model's context.

**Authority scaffolding**

Defines who may decide, close, approve, or certify. Better models do not remove this because it is governance, not intelligence. The Fable source's "no self-certifying closure" and human close decision belong here.

**Verification scaffolding**

Evidence gates, tests, cited command output, commit hashes, fresh-context verifier passes. Better models may fail less often, but higher stakes still require independent evidence. This may thin in low-stakes cases but persists where correctness or accountability matters.

**Context-economy scaffolding**

Compression, progressive disclosure, cache tiers, hot-path wrappers, and raw-reference search skills. The vertical-agent source suggests this category remains central even for strong models because context is still scarce and domain distributions remain long-tailed.

## Tensions

- The Fable source may be reporting a task becoming easy, not a general reduction in scaffolding need.
- The phrase "model-management scaffolding" is probably too coarse. Some model-management artifacts are competence aids; others encode authority or verification.
- The Shortcut source cuts against a naive "stronger models need less scaffolding" conclusion: high-performing vertical agents may need more domain-specific context engineering, not less.
- Stronger models might increase the importance of state scaffolding because they can act more autonomously once correctly resumed, making stale or missing work state more consequential.

## What Would Close This Workshop

Close this workshop when one of these happens:

- A note is written with a careful claim, likely along the lines of `Competence scaffolding recedes with model capability, but state scaffolding does not`.
- The theory is split across existing notes instead: update the scaffold-relaxation theory, the system-definition-artifact note, and the session-history/state notes with this distinction.
- We decide the evidence is too thin and leave the ingests as source-only references until a code-grounded review of `claude-workstream-kit` supplies stronger evidence.

## Next Useful Step

Inspect `claude-workstream-kit` with a code-grounded related-system review or lightweight agent-memory-system coverage. The open question is whether the implementation actually separates competence scaffolding, state scaffolding, authority scaffolding, verification scaffolding, and lifecycle surfaces as cleanly as the announcement claims.
