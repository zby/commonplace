# Harness taxonomy convergence

Five independent approaches decompose agent harnesses into named components. This workshop maps them into one table to test whether the KB's three-part decomposition (scheduler, context engine, execution substrate) is genuinely convergent or just one possible cut.

## Sources

1. **Vtrivedy10** — derives 6 components from model limitations (filesystem, bash, sandboxes, memory/search, context management, long-horizon execution)
2. **Raschka** — derives 6 components from "what makes agent-mode outperform plain chat" (live repo context, prompt shape, tool access, context bloat minimization, session memory, bounded subagents)
3. **Lopopolo** — derives 3 pillars from production practice at 1M LOC (constrain, inform, verify/correct) plus entropy management
4. **Cybernetics thread** — reframes as control theory (sensors, actuators, feedback loops, externalized judgment)
5. **This KB (commonplace)** — derives components from first principles of LLM limitations, expressed as implementation rather than taxonomy. CLAUDE.md as control-plane router, skills/instructions as on-demand context loading, review system as quality enforcement, validate as deterministic checking, file-backed notes as execution substrate, sub-agents for scoped work

## The alignment question

Each source uses different vocabulary and cuts the space differently. The runtimes-decompose note already maps Vtrivedy10 and Raschka individually. This workshop does the four-way alignment to see:

- Where do the taxonomies agree on component boundaries?
- Where do they disagree — and is the disagreement about substance or vocabulary?
- Does the three-part split (scheduler / context engine / execution substrate) capture the convergence, or does it lose distinctions the sources preserve?

## Draft alignment table

| Function | Vtrivedy10 | Raschka | Lopopolo | Cybernetics | Commonplace | KB component |
|---|---|---|---|---|---|---|
| Control flow / iteration / decomposition | Long-horizon execution (Ralph Loop) | Bounded Subagents (delegation, recursion limits) | — | Feedback loops | Sub-agents for scoped work; skill orchestration | Scheduler |
| What enters each call | Context management (compaction, progressive loading) | Live Repo Context + Prompt Shape | Context engineering (AGENTS.md as map) | Sensors (what the system observes) | CLAUDE.md as control-plane router; routing table; progressive disclosure via skills/instructions | Context engine |
| Context maintenance / bloat | Context management | Context Bloat Minimization | — | — | Instruction specificity matching loading frequency; on-demand skill bodies | Context engine |
| Working memory / retrieval | Memory/search | Structured Session Memory | — | — | MEMORY.md; /connect discovery; search patterns in CLAUDE.md | Context engine + substrate |
| Durable state | Filesystem | — | — | — | File-backed notes, sources, instructions; git as versioning layer | Execution substrate |
| Tool execution | Bash | Tool Access | — | Actuators | Python scripts (validate, review, selector); bash via harness | Execution substrate |
| Safety boundaries | Sandboxes | — | — | — | Permission modes; hooks | Execution substrate |
| Quality enforcement | — | — | Constraints (structural tests, linters) | Externalized judgment | /validate (deterministic); review gates (LLM judgment); fix system (correction) | Cross-cutting |
| Drift correction | — | — | Entropy management (cleanup agents) | Feedback loops | Review sweeps; staleness detection; ack for trivial changes | Cross-cutting |

## Observations so far

- **Lopopolo's pillars are orthogonal to components.** Constrain/inform/verify are operations that run *through* components, not components themselves. They describe what you do with the runtime, not what the runtime is made of.
- **The cybernetics framing is also orthogonal.** Sensors/actuators/feedback loops are a meta-vocabulary for describing any control system. Mapping them to components requires choosing which component plays which role in which loop.
- **Only Vtrivedy10, Raschka, and commonplace give component-level decompositions.** Lopopolo and cybernetics give framing vocabularies. The convergence story might be better stated as "three independent component decompositions converge, and two independent framing vocabularies are consistent with the result."
- **Commonplace is the only entry expressed as implementation.** The others describe or taxonomize; this KB builds the components and discovers their boundaries through use. That makes it a different kind of evidence — convergence through construction rather than analysis.
- **Quality enforcement and drift correction don't map cleanly to the three-part split.** Both cut across scheduler, context engine, and substrate. This may be a genuine gap — the three-part decomposition captures the runtime's structure but not its maintenance operations.

## Open questions

- Is the "cross-cutting" row a sign that the three-part decomposition needs a fourth component, or that operations and structure are genuinely different axes?
- Should the convergence note live in runtimes-decompose (extending its convergence section), or as a standalone note?
- Does mapping Lopopolo as "operations on the runtime" rather than "components of the runtime" dissolve the apparent disagreement?
- Commonplace fills every row including cross-cutting (validate + review + fix). Does the fact that the cross-cutting functions were built as distinct systems (not extensions of the three core components) support the "different axis" interpretation?
