---
type: types/note.md
description: JAZ exposes recursive execution, hook controls and trace reuse, while correctness, faithful replay
  and learning depend on evidence outside the package.
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-26-jaz-01
source-identity: https://github.com/jaz-lang/jaz
reviewed-revision: 0803d4971be785e95b80054b02259664d70fa3da
analysis-result: kb/reports/retained/agentic-system-analysis-archive/AAS-2026-09-26-jaz-01/result.md
analysis-result-sha256: 1acb504890b03a78fe1dd17dff9d73a522ee543259631821cec4a65a1d25c932
---

# JAZ

Evidence basis: source code and shipped documentation at commit `0803d4971be785e95b80054b02259664d70fa3da`, inspected on 2026-09-26. No live model runs or benchmark reproduction.

JAZ is a Python agent runtime organized around recursive `invoke`: the model writes code, the REPL executes it, and observations drive the next turn until a value or exception returns. Inputs remain program-accessible objects; ordinary inputs belong to one invocation, while `scope` propagates bindings to descendants. The host chooses tools, model backends and optional controls. This analysis includes the package's console and replay facilities, while external providers, supplied tools and deployment isolation remain outside its boundary.

## Execution and control

The core loop separates committed code from execution and checks terminal results through hooks. A caller can reject proposed code before execution, reject a return through a type or custom predicate, or stop future instrumented queries through iteration, recursion and budget controls. Invalid returns can become feedback for another model turn. These checks establish their declared predicate; they do not certify arbitrary answers or undo earlier tool effects. See RTE-1, RTE-2 and RTE-3 in the exact result.

The Python executor restricts imports, file access and attributes, but containment depends on what the host exposes. Supplying configuration overrides allows sub-invocation reconfiguration. Supplied callables can perform effects outside the transformed-code boundary. The public entry point reached from a raw worker thread can start a new invocation root when context variables did not propagate. The package's controls therefore need to be assessed over the actual configured call paths.

The console's `%` helper has a separate change route: it reads a text view of current settings and proposes code; a human must explicitly confirm before that code executes in the console namespace. This is operational permission, not a correctness verdict (RTE-4).

## Memory and reuse

JAZ exposes several mechanisms that should not be collapsed into one memory feature:

- Each invoke has fresh history. The model can inspect that history programmatically, and a parent can pass retained objects to another invoke. Ordinary next-turn context alone is not cross-invocation memory.
- The console automatically gives later main turns previous conversation records, including live input/result objects behind capped displays. The settings helper receives text transcripts instead. Display limits do not bound all retained objects, and a live reference is not an immutable historical snapshot.
- Trajectory replay supplies saved model responses by invocation nesting and order, then re-executes their code. Its optional divergence check does not compare the seed prompt, and its stack assumes sequential nesting.
- Workflow export turns traced code into Python functions and a runnable entry point. That supports an afforded form of per-task symbolic trace learning. It does not filter for successful workflows, guarantee reconstruction of arbitrary inputs, or prove safe and faithful replay.
- Rollout export provides samples to a documented external trainer role. The package does not thereby establish that training occurred or that learned weights returned to a later invocation.

There is no shipped semantic compactor established within the inspected source boundary. Generic persistent message edits permit one to be added, and context warnings can prompt a response, but neither supplies a concrete summary policy. The exact result's memory records preserve those distinctions and opaque-payload uncertainty.

## What the evidence supports

The strongest result is an inspectable set of mechanisms for recursive execution, correction and later reuse. The framework affords localized theories and feedback-driven revision, but no inspected candidate trace establishes all four [theory-builder conditions](../../notes/definitions/theory-builder.md). Improved future capacity attributable to criticism remains uninspected.

Program-visible history affords [reflection](../../notes/definitions/reflective-system.md) over selected execution aspects; the console also wires a human-mediated configuration representation/change route. Neither establishes a reflective theory builder or autonomous self-improvement. The distinction matters especially for workflow export: converting a trace into runnable code establishes reuse, not evidence that the procedure became better.

## Scope

This is a static analysis of the framework package, not evidence for the paper's benchmark claims. Host tools, remote models and custom extensions can materially change authority, persistence and isolation. Candidate-linked traces, controlled comparisons and tests of the actual deployment boundary would be needed to strengthen learning, benefit or containment findings.

---

- [Exact analysis result](../reports/retained-archive/AAS-2026-09-26-jaz-01/result.md) — see-also: complete evidence, routes, quotations and memory comparison fields
- [Pinned framework source](https://github.com/jaz-lang/jaz/tree/0803d4971be785e95b80054b02259664d70fa3da) — evidenced-by: frozen implementation boundary
