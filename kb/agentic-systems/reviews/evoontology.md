---
type: types/note.md
description: "EvoOntology's semantic memory and host-led evolution, with supplied-score admission, direct mutation alternatives and content-only version recovery"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-evoontology-01
source-identity: https://github.com/ruc-datalab/EvoOntology
reviewed-revision: ddbb1c991de5a33e27eb32bc86a4212a7537e01e
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-evoontology-01/result.md
analysis-result-sha256: aa9766294d0d76b819168cc4d430077f219929da7689d5b5effeedb374ce105d
---

# EvoOntology

**Evidence basis:** source code, shipped host instructions and attributed README results at commit `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`, inspected 2026-09-25. No target execution or performance reproduction.

EvoOntology supplies a persistent semantic layer for data agents and an evolution workflow for revising that layer. Its core stores and serves domain meanings, records task observations and controls selected publication transitions. External Claude Code or Codex agents perform semantic construction, diagnosis, candidate editing and much evaluation. The reviewed boundary is the complete artifact and a partial operational loop: core, plugin instructions/hooks and benchmark adapter interfaces. Host/provider interiors and full benchmark task-agent runtimes are excluded. The root core and both bundled plugin copies match by Git blob identity. See the [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-evoontology-01/result.md) — see-also: source register, canonical records and both mandatory lenses.

## Runtime and memory

The Content Layer stores Terms, Mappings, Relations, Constraints and Evidence in five JSON families. A data agent requests browse or resolve results and uses returned meanings, source mappings and evidence while querying actual data. Browse requires a query and uses lexical ranking; resolve handles at most five mentions and expands linked content. Entry limits do not guarantee a total context-size limit. Constraint severity is returned as advice; it does not itself veto native SQL. [Semantic runtime](https://github.com/ruc-datalab/EvoOntology/blob/ddbb1c991de5a33e27eb32bc86a4212a7537e01e/evoontology/runtime/runtime.py) — evidenced-by: RTE-2 and BAP-1 in the exact result.

Task recording is explicit. The built-in SQLite path executes bounded read-only queries and records results; other host tools require submitted observations. The recorder retains observable calls/results and final answers, clipping large outputs. It does not certify caller-supplied evidence or recover clipped suffixes. Later evolvers can read those trajectories and prior explanations. Claude's SessionStart hook automatically supplies a coarse reminder when accumulated state makes evolution due; the Codex instructions request a status check. Neither starts evolution automatically. [Workflow](https://github.com/ruc-datalab/EvoOntology/blob/ddbb1c991de5a33e27eb32bc86a4212a7537e01e/evoontology/workflow.py) and [Claude reminder](https://github.com/ruc-datalab/EvoOntology/blob/ddbb1c991de5a33e27eb32bc86a4212a7537e01e/plugins/claude-code/scripts/check-reminder.py) — evidenced-by: RTE-3 and RTE-9.

The memory comparison records files and in-memory objects, natural-language and symbolic representations, requested retrieval plus coarse reminder push, and trace learning at **afforded** strength. The qualifying learning route is host-directed transformation of task evidence into reusable semantic claims, explanations and code or instruction revisions. Raw logging and clipping are acquisition. The intended horizon is later tasks within a project, through offline, staged evolution. Actual dependence on recalled content remains not determinable.

## What publication establishes

Initial publication validates structure, references and loadability. Formal evolution acceptance consumes a recorded comparison: ground-truth mode requires paired finite score vectors with unique case IDs and a strictly higher candidate mean; judge mode requires more candidate wins and no candidate critical error. It also requires an explicit no-regression assertion and respects a configured protocol. The code recomputes those predicates. It does not thereby verify external observations, matched experimental conditions or the truth of the no-regression assertion. Saved evaluation is not bound to candidate content by a digest. [Evolution session](https://github.com/ruc-datalab/EvoOntology/blob/ddbb1c991de5a33e27eb32bc86a4212a7537e01e/evoontology/evolution/session.py) — evidenced-by: RTE-5.

The gate is route-specific. Exposed lower-level save and active-version operations can overwrite content or change the selected version without formal evolution acceptance. Formal publication protects an existing official destination against different content, but that protection does not cover every mutation path. [Store operations](https://github.com/ruc-datalab/EvoOntology/blob/ddbb1c991de5a33e27eb32bc86a4212a7537e01e/evoontology/ontology/store.py) and [MCP operations](https://github.com/ruc-datalab/EvoOntology/blob/ddbb1c991de5a33e27eb32bc86a4212a7537e01e/evoontology/runtime/ops.py) — evidenced-by: RTE-7.

The host skill permits revisions to Content, Tool and Schema, including related prompts, workflows and runtime code. Content publication copies the five stored families; it does not snapshot executable Schema/Tool definitions or provide their rollback. Their views derive current code. Candidate annotations also live outside the copied version directory, so official-version display cannot be assumed to inherit the candidate's report filename. [Evolution skill](https://github.com/ruc-datalab/EvoOntology/blob/ddbb1c991de5a33e27eb32bc86a4212a7537e01e/plugins/evoontology-codex/skills/evolve-ontology/SKILL.md) — evidenced-by: RTE-8 and its recovery boundary.

## Learning and warrant

The host method explicitly asks for competing causal explanations, a falsifiable hypothesis, a localized reversible intervention, capability tests and retention of rejected explanations. Those are substantive affordances for criticism. Core fields retain hypotheses and rejection notes; richer explanation retention and later reliance are host obligations. Structural validity, returned evidence and comparative score success are distinct from warrant for a semantic or causal claim.

A standing self-improvement route is **afforded**, with content adoption and later read-back **wired**. Actual improvement and attributable future capacity remain **uninspected**. Conjectural learning remains **uninspected** because operative theory use, content-directed criticism and resulting capacity were not observed. Reflection is **afforded** in the host's representation of its own layer's limitations and proposed changes; actual representation-mediated change is uninspected. These are separate findings, not a maturity grade. [Conjectural learning](../../notes/definitions/conjectural-learning.md) and [reflective system](../../notes/definitions/reflective-system.md) — defined-in: the distinctions used here.

## Scope

README benchmark gains remain attributed reports. The inspected adapter interfaces do not reproduce them or isolate effects of recalled semantics. Candidate-linked observations, trustworthy evaluation provenance, controlled recall interventions and tested code/schema recovery would resolve the main uncertainties. The analysis establishes concrete storage, retrieval and admission behavior while keeping host compliance and experimental benefit outside the demonstrated boundary.
