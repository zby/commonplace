# Known instruction baselines

This directory separates preserved operative text from modular workshop extractions.

## Preserved operative text

These files are byte-for-byte copies. Edit the source artifact, not the copy, if an immediate change to current behavior is intended.

| Workshop copy | Source | Current role |
| --- | --- | --- |
| `current-memory-review-skill.md` | `kb/instructions/write-agent-memory-system-review/SKILL.md` | Prepares a GitHub checkout, delegates a code-grounded memory review, runs QA, and validates the result. |
| `current-memory-analysis-contract.md` | `kb/agent-memory-systems/types/agent-memory-system-review.md` | Defines the current review content, memory axes, controlled values, and output structure. |
| `current-epistemic-analysis.md` | `kb/instructions/analyse-external-system-epistemic-architecture.md` | Analyses truth-apt transformations, warrant, acceptance, integration, and authority routes; accepted after cold ARC and GBrain trials. |
| `current-agentic-comparison-instruction.md` | `kb/work/pi-agent-zerostack-comparison/review-instruction.md` | A bounded whole-system comparison procedure that produced a substantive comparison; evidence that the runtime axes are usable, not a general contract. |

## Modular workshop extractions

These files are newly written for composition experiments. They have no runtime consumer and are not promoted:

| Baseline | What it owns | What it deliberately leaves elsewhere |
| --- | --- | --- |
| `prepare-code-grounded-source-baseline.md` | Safe GitHub checkout selection and refresh, revision capture, dirty-state reporting, source identity, and pinned citation forms. | Analysis, artifact lifecycle, semantic QA, publication, and doc-grounded acquisition. |
| `analyse-agent-runtime-baseline.md` | Runtime boundary, scheduling, context assembly, external state/action services, coordination, control surfaces, observability, and lens routing signals. | Detailed persistence/read-back analysis, epistemic warrant analysis, publication shape, comparison with Commonplace. |
| `analyse-memory-context-baseline.md` | Persistent material, write/maintenance routes, later consumption/read-back, context efficiency, activation evidence, provenance, and lifecycle controls. | Whether transformed truth-apt content becomes knowledge; whole-system runtime coverage; publication and comparison sections. |

The eventual public instruction should not concatenate these texts. It must decide which layer owns shared source metadata, object identity, evidence state, applicability, synthesis, and validation.
