---
description: "Pinned AIDE agent code exposes solution generation, execution review and feedback routing, while leaving realized criticism, persistence and self-improvement outcomes unverified."
source: https://github.com/WecoAI/aideml/blob/60b3978ddf65b71f86eb7c64506965048a1398cf/aide/agent.py
captured: "2026-09-27"
capture: git-show
capture_scope: full-source
genre: code-repository
snapshot_sha256: bc66c232c031d825bc6bb7271e3919ad844247949e08411aa69c44d0b76ba6ca
ingested: "2026-09-27"
occasion: "Prepare source evidence for adding Weco/AIDE² to which-existing-self-improving-systems-are-theory-builders.md, examining reflective improvement, fixed-model learning, outer/inner loops, criticism, evaluation and compounding without presupposing theory-builder membership."
type: types/ingest-report.md
domains: [agentic-systems, automated-machine-learning, learning-theory]
learning_claims: true
---

# Ingest: AIDE agent implementation at 60b3978

## Classification

One complete Python file from WecoAI's AIDE repository, pinned to commit `60b3978ddf65b71f86eb7c64506965048a1398cf`. It is primary implementation evidence for the operations defined in that file. The project authors supply executable control flow and prompts; imported implementations, actual model responses and measured outcomes are outside this observation.

## Summary

AIDE's agent generates a natural-language solution plan and Python program, executes the program through a callback, asks a feedback model to interpret its output, and appends the resulting node to a journal. Its search policy first drafts solutions, sometimes selects eligible failed leaves for debugging, and otherwise requests the journal's best node for improvement. Improvement prompts request one atomic change; debugging prompts supply the failed program and execution output. Drafting and improvement receive a generated journal summary, whose contents are defined outside this file. Review results supply a summary, bug judgment and validation metric, with exceptions and missing or invalid metrics marking a node as buggy. This establishes a designed feedback path for task-solution search, not observed learning, an AIDE² outer loop, or autonomous revision of AIDE's own search machinery.

## Quotes

No source quotes have been retained yet.

## Connections Found

This source is an implementation anchor for assessing the Weco/AIDE case against the four conditions of a [theory builder](../notes/definitions/theory-builder.md). Its distinctive contribution is the visible distinction between stored evaluation and supplied feedback: the review summary is assigned to `node.analysis`, whereas debugging directly receives code and execution output, and improvement receives code plus an externally defined journal summary. That comparison sharpens [knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md). The source also supports the evidential caution in [disconnected witnesses do not establish a full causal path through theory](../notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md): deterministic call sites can identify some joins, but the missing generated summaries and model responses prevent reconstruction of a realized criticism-to-revision path.

## Learning Claims (our opinion)

The visible adaptation operates on task-solution programs and their retained results. Configured models propose and assess candidates through inference calls; no update to those models' weights appears in this file. A generated solution may itself train an ML model, which is a different object of adaptation. This distinction permits fixed-model agent improvement in principle without treating the trained task model and the agent as one learner.

**Localized content:** strong implementation evidence. Nodes are constructed with a textual plan and executable code, and child nodes identify a parent. These are candidate localized theories about how to solve the task. Their actual content and the precision of their stated expectations remain unobserved.

**Consumption:** strong implementation evidence for program consumption. The generated code is passed to the execution callback, and selected parent code enters improvement or debugging prompts. A separate claim that the prose plan governs the code is weaker: both are generated in one call, and the file contains no check that the implementation follows the plan.

**Content-directed criticism:** a supported design affordance, with realized performance unresolved. Review prompts expose the implementation and execution output, ask for bugs and empirical findings, and request a fix when buggy. Debugging then asks for a reasoned repair against the failed program and its output. These inputs can support criticism of what code does. Successful candidates are also ranked by metrics, however, and metric selection alone does not establish a stated reason bearing on a candidate's content. The atomic-change instruction makes a discriminating experiment possible; it does not show that generated changes obey it or that reviews formulate attempted refutations.

**Iteration:** strong evidence of scheduled reuse within a journal, partial evidence of criticism reuse. Each step appends the reviewed node; later selection uses bug status and the journal's best-node interface. Debugging supplies the parent's output, and drafting and improvement load a journal summary. Whether the stored review reasoning reaches those summaries cannot be established here. Persistence across separate runs or problems is also unestablished. A runtime trace is needed to classify a realized process rather than its available interfaces.

The file adds a concrete boundary to the current account: task-level program revision can be broad while the agent's search policy, review schema and prompt construction remain unchanged by the visible loop. Consistent with [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), any improvement obtained through this loop would not by itself validate those fixed choices. No measured improvement is supplied, and the code shows neither reflective revision of the agent's method nor compounding through improved improvement machinery. Their absence from this file does not establish their absence from a larger Weco system.

## Extractable Value

1. **Bound the implementation evidence in the Weco/AIDE case.** Separate visible generation, execution and feedback routing from unobserved content-directed criticism, cross-run persistence and AIDE² outer-loop behavior. This avoids using a functioning search skeleton as proof of theory-builder membership. [quick-win]
2. **Identify the decisive feedback question.** The code stores a review summary but debugging directly reloads the raw execution output; improvement depends on the unseen journal summarizer. A focused trace can test which criticism actually reaches and changes the next candidate. This is a reusable inspection method, while these particular paths are revision-specific. [experiment]
3. **Keep improvement objects distinct.** Candidate ML programs, models trained by those programs, inference models proposing them, and the agent's own machinery occupy different revision boundaries. This file directly exposes the first and references the next two; it supplies no outer process modifying the fourth. [quick-win]

## Limitations (our opinion)

The capture covers the complete named file, not the repository. The backend, execution callback, journal summarization, metric comparison and configuration implementations were not inspected or executed. No code was run. The file defines helpers for choosing a consistent task metric, but their invocation is outside the captured file; it therefore cannot establish end-to-end enforcement of that choice.

The revision is a point-in-time implementation observation, not an identified historical evaluation revision. It must not be attributed to AIDE² or a paper's experimental setup without further provenance. No benchmark, ablation or runtime trace is included. Even an observed score increase could follow ordinary candidate sampling and ranking; attributing it to formulated criticism would require stronger evidence. Static prompts alone do not establish reliable adherence, learning, reflective method revision or compounding.

## Recommended Next Action

Use this bounded implementation evidence when adding the Weco/AIDE case to `which-existing-self-improving-systems-are-theory-builders.md`, explicitly separating the visible inner loop from unverified AIDE² outer-loop and realized-criticism claims.
