---
type: kb/types/note.md
description: LLM-hosted world-model design compilation with deterministic consistency
  checks and generated evidence contracts, distinct from empirical model validation
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-jepa-anything-01
source-identity: https://github.com/Gen-Verse/JEPA-Anything
reviewed-revision: c6e6c88f3ef75a4ce7acd660d6fa5779d995512c
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-jepa-anything-01/result.md
analysis-result-sha256: 77485ed84f5d5688ac1893b4b01c047d4442b397d3c03939e4cd06db79628a4a
---

# JEPA-Anything

Evidence basis: source code and shipped instructions at [c6e6c88f3ef75a4ce7acd660d6fa5779d995512c](https://github.com/Gen-Verse/JEPA-Anything/tree/c6e6c88f3ef75a4ce7acd660d6fa5779d995512c), inspected 2026-09-25. No runtime execution or causal experiment was performed.

JEPA-Anything ships an LLM-hosted world-model compiler alongside a tensor library. This analysis covers the compiler skill, design validator, scaffold generator and generated evidence contracts. The host interprets the user's task and proposes a configuration; Python checks the declared plan and emits an inspectable code skeleton. Model training and the host's own execution loop remain outside this boundary.

The useful control is a narrow admission rule: the generator CLI revalidates its input before rendering and returns diagnostics on failure. It also refuses a nonempty output directory. The renderer stages files before replacing the destination. Direct Python calls to the renderer do not repeat CLI validation, so these checks do not establish a guarantee over arbitrary host actions. See RTE-2 and RTE-3 in the [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-jepa-anything-01/result.md).

> report = validate_config(raw)
> if not report["valid"]:
>     sys.stdout.write(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
>     return 1
> --- https://github.com/Gen-Verse/JEPA-Anything/blob/c6e6c88f3ef75a4ce7acd660d6fa5779d995512c/jepa-anything-skill/scripts/generate_scaffold.py

Generated claims remain planned. An evidence-envelope checker compares supplied model, metric, split, horizon, mode, experiment and audit identifiers against the plan; it deliberately leaves statistical support undecided. This makes the output a declared research contract rather than an empirical result. See OBJ-1, OBJ-2 and RTE-4 in the exact analysis.

> This stub intentionally does not decide statistical support. It rejects a
> result measured with a different metric, direction, split, horizon, model,
> use mode, baseline set, or audit set.
> --- https://github.com/Gen-Verse/JEPA-Anything/blob/c6e6c88f3ef75a4ce7acd660d6fa5779d995512c/jepa-anything-skill/assets/scaffold/src/jepa_task/evaluation.py.tmpl

The compiler writes task products and reads current supplied configurations. A bounded search found no accumulated agent-memory recall or trace-learning route in this compiler. Static skill references and generated scaffolds are not, by themselves, memory read-back. The external host may retain conversations or reuse outputs; those facilities were excluded. The exact analysis records this boundary in ABS-1 and its memory profile.

The strongest supported contribution is code-backed checking of design consistency before file emission. Source instructions afford correction of explicit assumptions and configuration errors, but no inspected episode establishes improved future capacity from criticism. Reflection and self-improvement remain uninspected at the compiler boundary. A pinned host integration and candidate-linked experiments would be needed to establish those stronger properties.

## Scope

This is a host integration with a partial execution loop. Model identity, parameter changes, conversation persistence, approvals, tool grants and isolation belong to the external host and were not inspected. The tensor library's training behavior and scientific results are also outside this compiler analysis. Static branch inspection supports wiring, not observed operation or empirical benefit.
