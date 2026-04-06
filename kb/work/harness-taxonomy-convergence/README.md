# Harness taxonomy convergence

Five sources address agent harness architecture, but they split into two kinds: **component decompositions** (what a runtime is made of) and **operational/control vocabularies** (how a runtime is steered and corrected). The alignment question is narrower and more defensible once this split is explicit.

## Sources

### Component decompositions

1. **Vtrivedy10** — derives 6 components from model limitations (filesystem, bash, sandboxes, memory/search, context management, long-horizon execution)
2. **Raschka** — derives 6 components from "what makes agent-mode outperform plain chat" (live repo context, prompt shape, tool access, context bloat minimization, session memory, bounded subagents)
3. **This KB (commonplace)** — derives components from first principles of LLM limitations, expressed as implementation rather than taxonomy. CLAUDE.md as control-plane router, skills/instructions as on-demand context loading, file-backed notes as execution substrate, sub-agents for scoped work

### Operational / control vocabularies

4. **Lopopolo** — derives 3 pillars from production practice at 1M LOC (constrain, inform, verify/correct) plus entropy management
5. **Cybernetics thread** — reframes as control theory (sensors, actuators, feedback loops, externalized judgment)

## The alignment question

The three component decompositions were developed independently. Do they converge on the same structural boundaries?

Separately: the operational vocabularies describe what you *do* with a runtime, not what it's *made of*. Do they describe a second axis (governance/maintenance) that the structural decomposition doesn't capture?

## Structural convergence table

| Function | Vtrivedy10 | Raschka | Commonplace | KB component |
|---|---|---|---|---|
| Control flow / iteration / decomposition | Long-horizon execution (Ralph Loop) | Bounded Subagents (delegation, recursion limits) | Sub-agents for scoped work; skill orchestration | Scheduler |
| What enters each call | Context management (compaction, progressive loading) | Live Repo Context + Prompt Shape | CLAUDE.md as control-plane router; routing table; progressive disclosure via skills/instructions | Context engine |
| Context maintenance / bloat | Context management | Context Bloat Minimization | Instruction specificity matching loading frequency; on-demand skill bodies | Context engine |
| Working memory / retrieval | Memory/search | Structured Session Memory | MEMORY.md; /connect discovery; search patterns in CLAUDE.md | Context engine + substrate |
| Durable state | Filesystem | — | File-backed notes, sources, instructions; git as versioning layer | Execution substrate |
| Tool execution | Bash | Tool Access | Python scripts (validate, review, selector); bash via harness | Execution substrate |
| Safety boundaries | Sandboxes | — | Permission modes; hooks | Execution substrate |

## Governance / maintenance axis

The operational vocabularies and commonplace's own systems populate a second axis that runs *across* the structural components:

| Function | Lopopolo | Cybernetics | Commonplace |
|---|---|---|---|
| Quality enforcement | Constraints (structural tests, linters) | Externalized judgment | /validate (deterministic); review gates (LLM judgment) |
| Correction | — | — | Fix system (applies corrections from review findings) |
| Drift detection / staleness | Entropy management (cleanup agents) | Feedback loops | Review sweeps; staleness detection; ack for trivial changes |
| Informing | Context engineering (AGENTS.md as map) | Sensors (what the system observes) | CLAUDE.md routing; skill descriptions |

## Observations

- **The category error is productive.** This workshop started as if there were five peer decompositions. The observations reveal a cleaner split: three component taxonomies and two operational vocabularies. The real convergence claim is narrower and more defensible.
- **The three component decompositions converge.** Vtrivedy10, Raschka, and commonplace independently land on something like scheduler, context engine, and execution substrate. They use different vocabulary and granularity, but the structural boundaries align.
- **The runtimes-decompose note's three questions are structural, not operational.** "What happens next?" (scheduler), "what does this call see?" (context engine), "where do exact state and actions live?" (substrate). They don't answer "how is the system monitored and corrected over time?" — that's the governance axis.
- **Governance emerged as a separate axis, not a fourth component.** Commonplace's validate/review/fix systems were built as distinct machinery, not as extensions of the scheduler, context engine, or substrate. Lopopolo's pillars (constrain/inform/verify) and the cybernetics vocabulary (sensors/actuators/feedback) describe the same axis from outside. This is evidence for two axes (structure × governance), not a missing fourth structural component.
- **Commonplace is convergence-through-construction, not independent corroboration.** The KB was built on the same first principles it uses to analyze external sources. This is strong construct validity (the split was operationally useful enough to build against) but weaker than outside evidence. Vtrivedy10 and Raschka are the independent corroboration; commonplace confirms the split is buildable.

## Outcome paths

- **If the claim stays structural:** fold the three-way convergence table into the convergence section of `agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md`. Mention commonplace as construct validity, not peer evidence.
- **If the stronger claim emerges — runtime structure and runtime governance are separate axes:** that's a standalone note. The structural decomposition answers "what is the runtime made of?" The governance axis answers "how is the runtime monitored and corrected?" Both are needed; neither subsumes the other. The review/fix system documentation we just wrote is evidence that governance needed its own machinery.

Current workshop artifacts for the stronger claim:

- [Runtime structure determines the control surfaces available to governance](./runtime-structure-determines-the-control-surfaces-available-to-governance.md)
- [Structure x governance matrix (commonplace)](./structure-governance-matrix.md)
