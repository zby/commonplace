---
description: "Historical survey separating domain, inference, and task knowledge while showing that reusable problem-solving methods still require human selection and adaptation."
source: https://publikationen.bibliothek.kit.edu/189497/3003
captured: "2026-09-17"
capture: pdftotext
capture_scope: full-source
doi: "10.1016/S0169-023X(97)00056-6"
genre: scientific-paper
snapshot_sha256: 9772cfeaca7941826f033aee9fe9b29e5bee9657b2843eadc4c9af32a3c89ee2
ingested: "2026-09-17"
occasion: "The domain, inference, and task knowledge layers; the problem-solving method as a reusable unit and its applicability assumptions; the reuse assumption's dependence on human construction."
type: ingest-report
domains: [knowledge-engineering, problem-solving-methods, knowledge-reuse]
---

# Ingest: Knowledge Engineering: Principles and Methods

## Classification

This is a scientific survey of knowledge engineering's shift from transferring expert knowledge to constructing explicit models, illustrated through established frameworks, specification languages, problem-solving methods, and ontologies. Author: Rudi Studer, V. Richard Benjamins, and Dieter Fensel write as active academic contributors to the field and synthesize its literature, including work in which they participated.

## Summary

The paper presents knowledge-based-system development as iterative model construction rather than extraction of a ready-made expert knowledge base. Its central organizing device is the CommonKADS Expertise Model: domain knowledge describes the subject matter, inference knowledge specifies generic reasoning actions and the roles domain knowledge plays in them, and task knowledge controls how tasks, subtasks, and inferences achieve goals. This separation is meant to support reuse in both directions, but reuse is conditional. A problem-solving method must have adequate competence for the task, its assumptions about available domain knowledge must hold, and a knowledge engineer must select, map, refine, configure, or combine components for the application. The survey therefore treats reusable methods and ontologies as inputs to an engineering process, not as self-applying artifacts.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a historical technical basis for [Actionable methodology](../notes/definitions/actionable-methodology.md): a problem-solving method supplies an intervention mapping only when an operator can connect its competence, knowledge roles, and assumptions to the target task and domain. It is also evidence for [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md), because the described reuse machinery leaves consequential selection, mapping, adaptation, and knowledge-acquisition decisions to the knowledge engineer.

## Extractable Value

1. **Separate the knowledge a system reasons about, the generic inferences it performs, and the control that organizes those inferences.** This three-layer account offers a precise historical precedent for distinguishing domain content from reusable operations and task-level orchestration. [quick-win]
2. **Describe a reusable method by both competence and applicability assumptions.** Matching a method's advertised result to a task is insufficient when its required domain knowledge or component behavior is unavailable. [quick-win]
3. **Treat reuse as an operator-mediated construction process.** The paper repeatedly assigns selection, mapping, refinement, configuration, and knowledge acquisition to a human knowledge engineer, which bounds what can be attributed to the reusable artifact itself. [deep-dive]
4. **Preserve the reusability-usability trade-off when evaluating generic artifacts.** Greater task neutrality increases potential reuse while increasing the adaptation needed before the artifact can operate in a particular application. [just-a-reference]
5. **Use knowledge roles as acquisition requirements as well as interface slots.** A method's roles state which domain knowledge must be supplied, making the reusable reasoning structure a guide for elicitation and validation. [experiment]

## Limitations (our opinion)

The paper is a broad 1998 survey, not a controlled evaluation of whether the surveyed decompositions or reuse strategies reduce cost, improve correctness, or outperform alternatives. Its examples illustrate feasibility and conceptual structure, but they do not isolate which claimed benefits follow from the three-layer decomposition itself. The account is also historically situated in knowledge-based systems and assumes substantial human knowledge-engineering work, so its categories should not be transferred unchanged to present agent-operated knowledge bases without checking their fit. As authors and participants in this research program, the authors have a natural interest in presenting model-based knowledge engineering and reusable problem-solving methods as a coherent advance.

## Recommended Next Action

Write a note titled **Reusable methods remain conditional on operator-supplied applicability work** that uses the paper's competence-and-assumptions account to distinguish reusable method content from the human selection, mapping, adaptation, and knowledge acquisition required to apply it.
