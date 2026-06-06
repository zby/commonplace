---
description: Once work is split across sub-agents, the per-window feasibility ceiling becomes per-agent — set by the heaviest fork's net load (what the system adds minus what it spares), which comes apart from the operation's summed cost
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, foundations]
status: seedling
---

# Under sub-agent decomposition, feasibility is the heaviest fork's net load

[Context efficiency has two faces — a binding per-window feasibility and a secondary aggregate cost](./context-efficiency-is-the-central-design-concern-in-agent-systems.md). The feasibility face is a per-window capability ceiling: because the [soft bound degrades competence well before the hard limit](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), a task whose load exceeds the usable budget becomes impossible, not merely costly. This note develops one consequence those framing notes leave open: what the feasibility ceiling becomes once work is split across sub-agents.

## Feasibility is per-agent, set by the heaviest fork

The per-window ceiling is per *agent*. When work is split across [lexically scoped sub-agent frames](./llm-context-is-composed-without-scoping.md), no single agent ever holds the whole operation; each fork starts from a fresh budget and they fail independently. So feasibility is set by the *heaviest single fork*, not by the operation total. Two things follow:

- **Decomposition is a feasibility strategy, not just tidiness.** A load that cannot fit one window can be made to fit across several. Sub-agent isolation earns its place here as a way to stay under the ceiling, not only as scope hygiene.
- **Aggregate cost and feasibility come apart.** An operation can be cheap in total yet infeasible (one bloated fork), or expensive in total yet entirely feasible (load spread thin across many light forks). Optimizing the summed cost can even *worsen* feasibility — merging steps to avoid re-paying setup piles load back onto a single context. The two must be judged separately.

Because the usable budget is itself [task-relative](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), the heaviest-fork threshold is per-task: the same load can be feasible for one sub-task and fatal for a harder one.

## The per-agent load that matters is net

What occupies a fork's window is not fixed. A system adds to it — instructions, raw material — but can also spare it: [frontloading](./frontloading-spares-execution-context.md) hands the agent a precomputed answer instead of the procedure to derive it; [navigation by description](./agents-navigate-by-deciding-what-to-read-next.md) lets it decline to load a body; [distillation](./definitions/distillation.md) replaces raw material with one use-shaped artifact. So the quantity that decides a fork's feasibility is its *net* load — what the system adds minus what it spares — not gross input.

This is what makes the feasibility face non-additive. A system whose sparing outweighs what it adds is a net feasibility-*enabler*, not a tax; one that adds more than it spares is the reverse. Judging only the added side both overstates the burden and misses the cases where the system is what makes a sub-task fit at all. The full catalogue of sparing levers — progressive disclosure, context management, instruction-notes over data dumps — is the [architectural-response set in the soft-degradation note](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md).

---

Relevant Notes:

- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: the two-faces split and the feasibility-binds-first ranking this note specializes to the decomposed case
- [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: the per-window soft bound, its task-relative threshold, and the architectural-response catalogue this note points back to
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — grounds: sub-agent forks are the independent scoped frames that make the ceiling per-agent
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: a sparing lever that lowers a fork's net load
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — mechanism: sparing by declining to load a body
- [distillation](./definitions/distillation.md) — mechanism: sparing by use-shaped compression
- [symbolic scheduling over bounded LLM calls](./bounded-context-orchestration-model.md) — extends: decomposition into bounded forks is the orchestration model this feasibility claim operates within
