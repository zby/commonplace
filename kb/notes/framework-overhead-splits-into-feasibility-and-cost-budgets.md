---
description: When operations fork into clean-context sub-agents, the heaviest single agent's net load decides whether a task is possible at all, while summed overhead only decides token cost — so framework overhead must be evaluated per agent
type: kb/types/note.md
traits: [title-as-claim]
tags: [evaluation, foundations]
status: seedling
---

# Sub-agent decomposition splits framework overhead into feasibility and cost budgets

A framework imposes overhead: to perform an operation inside it, an agent must read framework instructions (routing rules, collection contracts, type specs, skill bodies, indexes) on top of the source material the task actually concerns. The naive way to score that overhead is to sum it over the whole operation. That number is real but it answers only one question — total token cost. It hides the question that usually matters more: *can the operation run at all?*

The two questions come apart as soon as an operation is **decomposed into sub-agents with clean contexts**. When the work is split across [lexically scoped sub-agent frames](./llm-context-is-composed-without-scoping.md), no single agent ever holds the whole operation. Each fork starts from a fresh budget and pays its own overhead from scratch — the orchestrator's loaded instructions do not carry into the child. So the operation has no single context whose size is the binding constraint. It has *N* contexts, and they fail independently.

This yields two distinct budgets with two distinct governors:

- **Per-agent net load → feasibility.** Each agent attends through one window bounded by [soft degradation, not a hard token limit](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md). For a given sub-agent the constraint is *overhead + the content it must read + room to reason ≤ usable budget*. If framework overhead crowds out the content the agent needs, the sub-task does not get more expensive — it becomes **impossible**, or degrades past usefulness. Feasibility is set by the *heaviest single agent*, not the sum. This is why the threshold is task-relative: usable budget is [not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a.md), so the same overhead can be feasible for one sub-task and fatal for a harder one.
- **Summed overhead → cost.** Re-paying routing rules, vocabulary, and skill bodies in every fork is pure token spend. It scales with how many sub-agents run and matters for budget, but a high sum with low per-agent peaks is still entirely feasible.

A framework can be cheap in total and still infeasible (one bloated agent), or expensive in total and perfectly feasible (overhead spread thin across many light forks). Optimizing the sum can even *worsen* feasibility — merging steps to avoid re-paying overhead piles load back onto a single context. The two budgets must be scored separately.

## Overhead is a net quantity, not an additive tax

Per-agent load is not framework-instructions added to a fixed content cost, because the framework also *changes the content the agent must read*. [Frontloading](./frontloading-spares-execution-context.md) hands the agent a precomputed answer instead of the sources to derive it. Retrieval-oriented titles and descriptions let it [decide not to load a body](./agents-navigate-by-deciding-what-to-read-next.md). [Distillation](./definitions/distillation.md) replaces raw material with one use-shaped artifact. So the framework moves *both* terms of the feasibility inequality: it adds instruction load and subtracts content load.

The quantity that governs feasibility is therefore the agent's **net load** — framework overhead minus the content the framework spared — not overhead alone. A framework whose instructions cost more than its frontloading saves is a net tax on that agent; one that saves more than it costs is a net feasibility-*enabler*. Measuring only the instruction side would both overstate the burden and miss the cases where the framework is what makes the sub-task fit at all. (The instruction side is not free either: each layer of pointer-chasing is [costly in context though free in code](./indirection-is-costly-in-llm-instructions.md), so overhead is itself partly a function of how the instructions are structured.)

## Consequence for evaluation

An overhead evaluation grounded on this claim reports per *operation*, but indexed by *agent*, not by linear step:

- a **feasibility signal** — the heaviest single fork's net load, checked against a usable-budget threshold;
- a **cost signal** — gross overhead summed across all forks (not net: the spared-content credit applies only to the feasibility signal, where fitting is at stake, not to the cost total, where every re-paid token is real spend);

and it credits content the framework spared, rather than counting only the instruction tax. An evaluation that amortizes fixed costs across the whole operation — counting an always-loaded file "once" because it "stays in context" — measures cost while silently assuming the feasibility question away. It is wrong precisely when forking makes feasibility bind.

## Scope

The split depends on genuine context isolation between sub-agents. Where an operation runs in a single accumulating context (no forking, full history retained), the two budgets collapse into one and summed overhead is the whole story. The claim generalizes past LLM frameworks to any runtime that decomposes work across bounded-resource workers that fail independently: there, too, the per-worker ceiling governs feasibility and the sum governs cost, and conflating them mis-prioritizes.

---

Relevant Notes:

- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: context as the single scarce per-agent resource is the premise this note splits into two budgets
- [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: the soft per-agent budget is what the feasibility constraint is measured against
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — grounds: sub-agent forks are the lexically scoped frames that make per-agent budgets independent
- [effective context is task-relative and complexity-relative not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a.md) — grounds: why the feasibility threshold is per-task, not a single number
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: how the framework subtracts content load, making overhead a net quantity
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — mechanism: navigation-by-description spares content without loading bodies
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — mechanism: the instruction side of overhead is itself shaped by how indirection is structured
- [symbolic scheduling over bounded LLM calls](./bounded-context-orchestration-model.md) — extends: the decomposition that creates per-agent budgets is the orchestration model this note evaluates
