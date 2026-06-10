# Scenario Instructions

Describe a recurring agent task as the chain of clean-context forks it runs as, and the loads each fork pays. The evaluation reads this to measure framework overhead in **bytes** and **hops**.

## Decompose by fork, not by step

Every `cp-skill-*` runs `context: fork`. The unit that matters is the individual agent's context: feasibility is set per agent (the heaviest fork must fit one usable window with room to reason) and cost is paid per fork (overhead is re-paid from scratch in each). So list **forks**, not linear steps. The orchestrating main agent is Fork 1; each skill invocation is a further fork.

## Classify every load

- **overhead** — read only because of the framework. Give a real file path so the harness can measure bytes: AGENTS.md, the target COLLECTION.md, the selected type-spec, the invoked skill body, curated indexes / scoped `rg` listings, a validate invocation.
- **content** — task/source material read regardless of framework. Usually "variable"; give a byte estimate in Notes.
- **spared** — content the framework let this fork skip (a description line instead of a body, frontloaded answer, distilled artifact). Record as a credit (a negative content load).

## Count hops

A hop is one read the agent performs. `0` = injected or already in this fork's context — a skill body is injected (0 hops, but its bytes still count). `1` = one read. A range (`2-4`) = a variable count; the harness uses the midpoint.

## Two signals the evaluation computes

- **Feasibility** — the heaviest single fork's net load (overhead + content − spared), in bytes and hops. This decides whether the operation can run at all: if one fork can't fit a usable window with room to reason, the task is infeasible at any price, not merely costly.
- **Cost** — framework-overhead bytes and hops summed across all forks (**gross**: the spared credit applies to feasibility, not cost — every re-paid token is real spend).

Do **not** amortize a load across forks ("count AGENTS.md once"): each fork is a fresh context and re-pays its overhead.

## Sections

- `Forks` — the fork tables, in execution order, with a Notes line per fork.
- `Variants` — environment/workflow differences that change the fork set or the loads.
