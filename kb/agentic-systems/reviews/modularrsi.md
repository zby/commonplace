---
type: types/note.md
description: "ModularRSI's proposal backlog, gated module evolution, dynamic composition, and the limits of its runtime and learning guarantees."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-modularrsi-01
source-identity: https://github.com/IQuestLab/ModularRSI
reviewed-revision: b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-modularrsi-01/result.md
analysis-result-sha256: 1a1508b4847328bc2746c7f71397814f98386abc1e5da2c69b5367a7865955ac
---

# ModularRSI

Evidence basis: pinned implementation, repository documentation, released modules and bounded retained task-run artifacts at `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`, inspected 2026-09-25. No target code or model calls were executed for this analysis.

ModularRSI evolves a library of agent-harness modules and selects implementations for later tasks. Its retained proposal backlog connects execution evidence and causal hypotheses to code-producing editors. Promotion combines structural checks, model review and execution checks; later composition decides whether promoted code runs. This review covers the named improvement subsystem and modular solver within the Harbor-derived repository. Other agents, benchmark evaluators, provider internals and deployed infrastructure are outside the boundary. [Exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-modularrsi-01/result.md) — see-also: complete records, source excerpts and both lenses.

## Evolution and admission

The launcher chooses a task set and one module type to evolve. The controller runs repeated task attempts, holding each task's selected bundle fixed after its first dynamic composition. Periodic background diagnosis pairs successful and failed trajectories when possible, reuses historical successes, or investigates failures alone. Model investigators inspect permitted traces and module code. Findings enter a backlog; routing and semantic grouping assemble proposals. Fixed ranking selects open proposals by attempts, age and breadth of support, with at most one per lane. Each implementer receives the proposal's behavioral change, causal reason and referenced evidence. [Evolution controller](https://github.com/IQuestLab/ModularRSI/blob/b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9/src/harbor/agents/terminus_2_modular/self_evo/online_evo.py) — evidenced-by.

Editors modify staged Python modules. Load/contract checks, intended-action and niche checks, model review and sanity execution can reject a candidate. Successful lanes become new generations; a second lane rebases onto the first and reruns applicable gates. Later comparison can retire variants that perform substantially worse than baseline on enough shared tasks. This is a regression policy over accumulated observations, with possible confounding from other changes.

Admission does not require a higher task score. Sanity checks focus on code crashes and evidence that the changed implementation ran. Normal composer selection is observed separately and does not gate. Review timeout or raised error passes through as skipped; missing structured verdicts have a separate breaker. Later crash repair reruns smoke/sanity but does not repeat every earlier judgment on the repaired bytes. These branches bound the claim that all promoted changes passed substantive scrutiny.

Editor file tools restrict writes to staging and the permitted module, protect baseline/pin files, and restrict trajectory reads. Candidate discovery and smoke checks nevertheless import Python in the host process. File-path enforcement therefore supplies a narrower guarantee than execution isolation. [Module loader](https://github.com/IQuestLab/ModularRSI/blob/b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9/src/harbor/agents/terminus_2_modular/library.py) — evidenced-by.

## Later use and memory

Dynamic composition filters module status and declared niches, respects pins, and asks a model to choose using task text and descriptions. Static composition and optional instruction-keyed cache replay are distinct paths; replay bypasses normal dynamic filtering and does not pin source-tree bytes. Selected modules become executable loop, observation, tool, context and completion policy. The sampled retained fix-git trace records `planning_with_guard` selection and invocation. It establishes use at that grain, not the module's causal benefit.

Within a task, context management can produce a summary, question-and-answer continuation, short summary or raw-screen fallback. Derived continuations reach later solver calls. Released and installed baseline implementations differ: fallback history resets and protocol restoration are not uniform, and some released variants import the installed loop. A generation directory alone therefore does not fix all runtime behavior.

Across tasks, proposal evidence and retained code supply the active learning route. The separately named `editor_memory.jsonl` has automatic writes and a formatter, but the bounded production-subtree search found no consumer of that formatter. The proposal backlog does retain and deliver causal rationale. Storage uses files and memory; retained content includes prose and executable/symbolic state. Trace learning is wired for staged cross-task evolution and online per-task continuation. Faithfulness testing remains undetermined: inspected logs show invocation, without a recalled-content intervention.

## Scope of the learning claim

The strongest supported contribution is a wired evidence-to-proposal-to-code-to-later-use pathway, including consequential review and rejection. Specific conjectural learning remains uninspected: no candidate-linked chain establishes that criticism of an operative theory caused improved future capacity. Reflection is wired through representations of the system's own modules, status and execution, which guide subsequent changes. That does not establish a validated self-theory of its theory-building organization. Self-improvement is an implemented pathway and reported empirical benefit; attributable improvement is not independently established here.

The README reports accuracy and transfer gains. The bounded retained-run inspection does not reproduce those comparisons or link every released module to its evolutionary history. Candidate-linked gate records, exact module/provider/dataset identity and controlled held-out comparisons would strengthen those conclusions.

- [Conjectural learning](../../notes/definitions/conjectural-learning.md) — defined-in: theory, criticism and attributable improvement.
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: causally connected self-representation.
