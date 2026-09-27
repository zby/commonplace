---
description: "AIDE's pinned journal implementation separates stored plans, execution feedback, metric selection, and summary generation; it supplies bounded evidence for evaluating a theory-builder loop."
source: https://github.com/WecoAI/aideml/blob/60b3978ddf65b71f86eb7c64506965048a1398cf/aide/journal.py
captured: "2026-09-27"
capture: git-show
capture_scope: full-source
genre: code-repository
snapshot_sha256: de75c36c6f22de8db786112ec73662864ebf6a290b3d23cebde9e8eb277eb715
ingested: "2026-09-27"
occasion: "Prepare source evidence for adding Weco/AIDE² to which-existing-self-improving-systems-are-theory-builders.md, examining reflective improvement, fixed-model learning, outer/inner loops, criticism, evaluation and compounding without presupposing theory-builder membership."
type: types/ingest-report.md
domains: [agent-learning, experiment-memory, program-search]
learning_claims: true
---

# Ingest: AIDE's experiment journal at 60b3978

## Classification

A complete implementation file at a pinned WecoAI/aideml commit. It is direct evidence of declared data structures and method bodies, without execution traces or performance results. Author signal: the project's own implementation; authorship of individual lines is outside the capture.

## Summary

The [AIDE journal implementation](https://github.com/WecoAI/aideml/blob/60b3978ddf65b71f86eb7c64506965048a1398cf/aide/journal.py) represents candidate programs as nodes containing code, a plan, parent-child links, execution details, analysis, a metric, and a bug flag. A journal collects these nodes, exposes subsets and metric history, selects a best candidate, and constructs a summary for an agent. The summary includes plans, analyses, and validation metrics from nodes marked non-buggy, with code included only on request. This establishes a concrete interface between stored experiment state and possible later context. The file does not show who populates the analysis, who consumes the summary, or how either changes subsequent proposals.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the Weco/AIDE² comparison, this source supplies bounded implementation evidence for retaining experiment state, while leaving the complete learning loop open. It makes the distinction in [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) concrete: storing plans and feedback, constructing a summary, and using that summary to change a proposal are separate operations, and only the first two appear here. Parent-child links associate candidate ancestry, but do not identify which criticism caused a child; this illustrates the evidential boundary in [Disconnected witnesses do not establish a full causal path through theory](../notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md). Neither connection establishes theory-builder membership or identifies this revision as the implementation evaluated in an AIDE² paper.

## Learning Claims (our opinion)

On its own terms, the file implements the state of a solution tree. The mutable content includes candidate code and plans, execution outcomes, analyses, and evaluation values. A node's stage is inferred from its ancestry: no parent means draft; a buggy parent means debug; otherwise the stage is improve. These labels classify nodes; they do not implement the proposal operations they name.

Against the [theory-builder conditions](../notes/definitions/theory-builder.md), the evidence divides as follows:

- **Localized content:** code, plans, and analyses have explicit fields attached to identifiable nodes. This supplies places for stated conjectures and criticisms, but the capture contains no populated example establishing what a plan or analysis actually says.
- **Consumption:** best-node selection reads bug flags and metric values, and summary construction reads plans and analyses. Those implementations establish data dependence inside the journal. They do not establish that a later decision uses what a plan or analysis says; the consumer is outside the file.
- **Content-directed criticism:** execution exceptions, analysis text, and metrics can be stored together. No method here produces a criticism or connects an identified program commitment to a stated reason for rejecting or revising it. Metric ranking alone does not supply that condition.
- **Iteration:** append operations, parent links, and summary generation provide machinery for retaining earlier results and exposing them to another round. No call sequence here establishes that a criticism shapes that round. Within-run retention is supported structurally; actual cross-run or cross-problem persistence is not shown by inheriting a serialization mixin.

The file therefore sharpens what remains to inspect without settling membership. It contains no model-weight update mechanism, but cannot establish a fixed-model configuration for the enclosing system. Nor does it show an outer loop revising the journal, prompts, search policy, or evaluation rules. Reflective improvement and compounding remain unestablished, as does improved capacity for future action.

The summary's selection of non-buggy nodes and optional omission of code are consequential representation choices. The complete journal retains more fields than that projection exposes. Under the [fixed-decomposition distinction](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), any benefit from downstream search would need to be separated from evidence favoring this summary design. Other consumers could access omitted information; this file does not establish the whole learner's effective information boundary.

## Extractable Value

1. **A precise limit on journal-based membership evidence.** The implementation establishes candidate state and a possible context projection, while criticism and subsequent semantic use require evidence from outside this file. This prevents a stored `analysis` field from carrying the entire Weco/AIDE² classification. [quick-win]
2. **A concrete stored-state versus exposed-context distinction.** The default summary emits non-buggy candidates' plans, analyses, and scores, excluding their code and the execution-detail fields. This is a reusable inspection question for experiment-memory systems, although its effects remain untested here. [just-a-reference]
3. **Candidate ancestry is weaker than criticism provenance.** Parent links and step numbers can join candidates structurally, but cannot identify which retained reason governed the revision. This narrows what an implementation-backed account may infer from a solution tree. [quick-win]

## Limitations (our opinion)

The capture is complete for one file, not for the repository. Imported metric comparison, serialization, output truncation, interpreter behavior, prompt construction, callers, and example runs remain outside it. No code was executed. Comments describe intended semantics but are not independent evidence of runtime enforcement: for example, the comment tying the bug flag to exceptions or invalid metrics has no corresponding assignment rule in this file.

No benchmark, ablation, or controlled comparison is present. An improving sequence of best scores, even if supplied elsewhere, would not by itself establish semantic uptake of criticism or a better improvement process. The summary excludes buggy nodes, but that does not show failed experiments are unavailable through other paths. Finally, this fixed commit is a point-in-time observation of AIDE; transferring its details to AIDE² or to a historical evaluation requires a separate version match.

## Recommended Next Action

Use this ingest when reviewing the planned Weco/AIDE² case in `kb/articles/which-existing-self-improving-systems-are-theory-builders.md` to limit journal-based claims to retained candidate state and summary construction, leaving criticism, subsequent use, and version correspondence to separate evidence.
