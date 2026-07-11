---
description: Once work is split across sub-agents, the per-window feasibility ceiling becomes per-agent — set by the heaviest fork's net load (what decomposition leaves on it after work is pushed across to siblings or up to the parent), which comes apart from the operation's summed cost
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, foundations]
---

# Under sub-agent decomposition, feasibility is the heaviest fork's net load

[Context efficiency's binding face is per-window feasibility](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — a capability ceiling rather than a cost, because the [soft bound degrades competence before the hard limit](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md). That framing assumes a single window. This note develops what the ceiling becomes once work is split across sub-agents.

## Feasibility is per-agent, set by the heaviest fork

The per-window ceiling is per *agent*. When work is split across [lexically scoped sub-agent frames](./llm-context-is-composed-without-scoping.md), no single agent ever holds the whole operation; each fork starts from a fresh budget and they fail independently. So feasibility is set by the *heaviest single fork*, not by the operation total. Two things follow:

- **Decomposition is a feasibility strategy, not just tidiness.** A load that cannot fit one window can be made to fit across several — and each sibling carries only its slice (less volume) free of the others' state (less interference). Sub-agent isolation earns its place here as a way to stay under the ceiling, not only as scope hygiene.
- **Aggregate cost and feasibility come apart.** An operation can be cheap in total yet infeasible (one bloated fork), or expensive in total yet entirely feasible (load spread thin across many light forks). Optimizing the summed cost can even *worsen* feasibility — merging steps to avoid re-paying setup piles load back onto a single context. The two must be judged separately.

A fork's *load* is more than its token count. It is how heavily the window taxes the model across the [soft bound's dimensions](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md): the volume of tokens, the complexity of using them, and the interference from material that competes with the task. The same volume of context is a heavier load when the tokens are harder to use — deeper indirection, more dependent reasoning steps — or when irrelevant state crowds the task, so it can cross the ceiling at a token count that cleaner, simpler content would clear. Feasibility therefore tracks load, not raw token count.

## A fork's net load is what decomposition leaves on it

Splitting an operation across sibling forks is only one direction of decomposition. A parent can also absorb part of a fork's work and hand down a leaner task. [Frontloading](./frontloading-spares-execution-context.md) is exactly this move: the parent — or an earlier build- or install-time step — performs the derivation and gives the fork the result, so the fork receives an answer instead of the procedure for reaching it. [Distillation](./definitions/distillation.md) pushes the sifting of raw material up the same way; [navigation by description](./agents-navigate-by-deciding-what-to-read-next.md) lets a fork shed an irrelevant body before it competes with the task.

What is left on the fork is its *net* load — the residual after work has been pushed off it, across to siblings or up to the parent. Measure that residual by what the fork *realizes*, not by the size of the instruction. A pointer — "read file X, derive Y" — is short, yet executing it eventually drags all of file X and the derivation into the window; frontloading hands over the result instead, so the fork loads neither the sources nor the steps. The saving falls largely on the complexity dimension.

This makes the system non-additive. A parent that absorbs more work than it imposes leaves leaner children — a feasibility-*enabler*, not overhead. Counting only what the parent adds to a fork both overstates the burden and misses the cases where the parent's work is what makes the sub-task fit at all.

---

Relevant Notes:

- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: the two-faces split and the feasibility-binds-first ranking this note specializes to the decomposed case
- [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: the per-window soft bound and its volume, complexity, and interference dimensions, which this note specializes to the per-agent decomposed case
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — grounds: sub-agent forks are the independent scoped frames that make the ceiling per-agent
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: a sparing lever that lowers a fork's net load
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — mechanism: sparing by declining to load a body
- [distillation](./definitions/distillation.md) — mechanism: sparing by use-shaped compression
- [symbolic scheduling over bounded LLM calls](./bounded-context-orchestration-model.md) — extends: decomposition into bounded forks is the orchestration model this feasibility claim operates within
