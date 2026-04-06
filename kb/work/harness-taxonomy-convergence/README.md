# Harness taxonomy convergence

Four independent practitioner sources decompose agent harnesses into named components. This workshop maps them into one table to test whether the KB's three-part decomposition (scheduler, context engine, execution substrate) is genuinely convergent or just one possible cut.

## Sources

1. **Vtrivedy10** — derives 6 components from model limitations (filesystem, bash, sandboxes, memory/search, context management, long-horizon execution)
2. **Raschka** — derives 6 components from "what makes agent-mode outperform plain chat" (live repo context, prompt shape, tool access, context bloat minimization, session memory, bounded subagents)
3. **Lopopolo** — derives 3 pillars from production practice at 1M LOC (constrain, inform, verify/correct) plus entropy management
4. **Cybernetics thread** — reframes as control theory (sensors, actuators, feedback loops, externalized judgment)

## The alignment question

Each source uses different vocabulary and cuts the space differently. The runtimes-decompose note already maps Vtrivedy10 and Raschka individually. This workshop does the four-way alignment to see:

- Where do the taxonomies agree on component boundaries?
- Where do they disagree — and is the disagreement about substance or vocabulary?
- Does the three-part split (scheduler / context engine / execution substrate) capture the convergence, or does it lose distinctions the sources preserve?

## Draft alignment table

| Function | Vtrivedy10 | Raschka | Lopopolo | Cybernetics | KB component |
|---|---|---|---|---|---|
| Control flow / iteration / decomposition | Long-horizon execution (Ralph Loop) | Bounded Subagents (delegation, recursion limits) | — | Feedback loops | Scheduler |
| What enters each call | Context management (compaction, progressive loading) | Live Repo Context + Prompt Shape | Context engineering (AGENTS.md as map) | Sensors (what the system observes) | Context engine |
| Context maintenance / bloat | Context management | Context Bloat Minimization | — | — | Context engine |
| Working memory / retrieval | Memory/search | Structured Session Memory | — | — | Context engine + substrate |
| Durable state | Filesystem | — | — | — | Execution substrate |
| Tool execution | Bash | Tool Access | — | Actuators | Execution substrate |
| Safety boundaries | Sandboxes | — | — | — | Execution substrate |
| Quality enforcement | — | — | Constraints (structural tests, linters) | Externalized judgment | Cross-cutting |
| Drift correction | — | — | Entropy management (cleanup agents) | Feedback loops | Cross-cutting |

## Observations so far

- **Lopopolo's pillars are orthogonal to components.** Constrain/inform/verify are operations that run *through* components, not components themselves. They describe what you do with the runtime, not what the runtime is made of.
- **The cybernetics framing is also orthogonal.** Sensors/actuators/feedback loops are a meta-vocabulary for describing any control system. Mapping them to components requires choosing which component plays which role in which loop.
- **Only Vtrivedy10 and Raschka give component-level taxonomies.** The other two give framing vocabularies. The convergence story might be better stated as "two independent component taxonomies converge, and two independent framing vocabularies are consistent with the result."
- **Quality enforcement and drift correction don't map cleanly to the three-part split.** Both cut across scheduler, context engine, and substrate. This may be a genuine gap — the three-part decomposition captures the runtime's structure but not its maintenance operations.

## Open questions

- Is the "cross-cutting" row a sign that the three-part decomposition needs a fourth component, or that operations and structure are genuinely different axes?
- Should the convergence note live in runtimes-decompose (extending its convergence section), or as a standalone note?
- Does mapping Lopopolo as "operations on the runtime" rather than "components of the runtime" dissolve the apparent disagreement?
