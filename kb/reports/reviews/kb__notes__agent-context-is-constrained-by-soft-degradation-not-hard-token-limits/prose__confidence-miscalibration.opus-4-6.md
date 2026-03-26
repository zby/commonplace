<!-- GATE-REVIEW
note-path: kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
gate-id: prose/confidence-miscalibration
model: opus-4.6
gate-hash: d8c22b55baba280c0855649ad07cf5a65927898e
recorded-commit: b34b33c12f7199564136b76b6124efb69f6be91b
watched-hash: 2bb82ffde2f8ccb2643ff41fb89d22b79519c0b2
recorded-at: 2026-03-26T23:14:38+01:00
-->
## Confidence miscalibration review

### Framework-by-framework check

**Volume/Complexity dimensions** — The note's own synthesis. Wording: "driven by at least two dimensions: volume and complexity." The "at least" hedges the enumeration's completeness. Each dimension is grounded in multiple cited sources. Confidence level: appropriate for a well-sourced synthesis.

**Three-level invisibility analysis (practitioner/benchmarker/market)** — The note's own analytical contribution. Wording: "The soft bound is invisible at every level." Assertive language, but each sub-point is argued from the evidence (no model signal, task-dependent surface, marketing incentives). The assertion follows from the premises. Appropriate confidence.

**"The soft bound is the binding constraint"** — Core claim. Assertive ("is," not "appears to be"). Supported by five independent sources showing degradation below hard limits. Confidence level: appropriate given the convergent evidence.

**Open Questions section** — Uses tentative language: "may be an independent dimension," "not empirically isolated," "our inference, not the paper's." Well-calibrated for speculative content.

**Consequences section** — "Silent degradation makes heuristic design rational" and "Programmatic constructability is the genuine advantage." Both are inferences from the evidence. The language is assertive ("makes...rational," "is the genuine advantage"). These follow logically from the premises. Appropriate.

### Findings

**INFO — "proportional" in Complexity section implies unestablished quantitative relationship.** The note says "LLMs pay interpretation overhead proportional to context complexity." The word "proportional" implies a specific mathematical relationship (possibly linear) between complexity and overhead. ConvexBench shows a non-linear collapse (F1 from 1.0 to ~0.2 across depth 2 to 100). The relationship is qualitatively established (more complexity, more overhead) but "proportional" overstates the quantitative precision. Consider "that scales with" or "that increases with" instead.
