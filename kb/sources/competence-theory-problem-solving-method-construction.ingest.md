---
description: "Wielinga, Akkermans, and Schreiber expose the commitments introduced while refining required competence into an operational problem-solving method."
source: https://guusschreiber.nl/wp-content/uploads/2025/05/wielinga98a.pdf
captured: "2026-09-17"
capture: pdftotext
capture_scope: full-source
doi: "10.1006/ijhc.1998.0209"
genre: scientific-paper
snapshot_sha256: 69df85b44d498fa07eb94c7ff046652f598eec3f22f4cb4adc108a901e7b21ca
ingested: "2026-09-17"
occasion: "The three construction stages and the commitments each exposes; which stages the framework leaves to the designer."
type: kb/sources/types/ingest-report.md
domains: [knowledge-engineering, methodology, problem-solving-methods]
---

# Ingest: A competence theory approach to problem-solving method construction

## Classification

This is a scientific paper that proposes a formal construction method and works it through classification examples. Its evidence is analytical and example-based rather than experimental.
Author: B. J. Wielinga, J. M. Akkermans, and A. Th. Schreiber were university researchers in knowledge engineering; the paper situates the method in their earlier analyses of reusable problem-solving methods and reports partial European research-project funding.

## Summary

The paper organizes construction of a problem-solving method into three successive theories. First, the designer specifies an initial competence theory from the problem and solution spaces, domain theory, and solution criteria; this exposes commitments about what counts as input, knowledge, and an acceptable result. Second, the designer conceptually refines that theory by adding task and domain vocabulary, knowledge-base schemata, and a decomposition into inference predicates; this exposes the chosen problem-solving paradigm and assumptions about how domain knowledge is represented. Third, the designer operationalizes the refined theory as inferences, roles, and control structure; this exposes search order, stopping rules, information acquisition, and other pragmatic choices that can weaken the competence of the resulting method. The framework makes these commitments explicit and keeps them related across stages, but it does not derive the ontology, solution criteria, paradigm, or operational strategy automatically: those remain design choices constrained by the task, available domain theory, and application requirements.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a technical basis for [the claim that a methodology governs extension only where it settles the decisions raised](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md): its three-stage construction process exposes a boundary between a retained refinement framework and choices still made by the designer. It also compares with the [two-layer execution account](../notes/theory-and-methodology-form-a-two-layer-execution-system.md) by giving a more granular source-side decomposition of the move from abstract theory to executable method. Relative to [actionable methodology](../notes/definitions/actionable-methodology.md), it shows that actionability depends on commitments about the task, domain theory, inference operations, and control regime rather than following from a formal goal statement alone.

## Extractable Value

1. **Use specification, conceptual refinement, and operationalization as three separate commitment audits.** The stages distinguish commitments about required competence, the chosen reasoning paradigm and knowledge representation, and the executable strategy. This directly serves the occasion and sharpens where an extension method should ask for explicit decisions. [quick-win]
2. **Mark the designer boundary at every stage.** The framework supplies questions and a refinement discipline, while the designer still chooses the initial ontology and solution criteria, intermediate vocabulary and decomposition, and final inference and control strategy. This is concrete evidence for attributing outcomes to the actor-plus-method system when retained guidance does not settle those choices. [quick-win]
3. **Track competence loss across refinements.** Later theories are typically weaker because conceptual and operational assumptions restrict which solutions the method can produce. This gives a reusable review question: which requirement was preserved, narrowed, or abandoned when guidance became executable? [deep-dive]
4. **Treat domain representation as part of method applicability.** The conceptual-refinement stage binds inference predicates to knowledge-base schemata, so reuse depends on whether the available domain theory satisfies those representation assumptions. This adds a technical basis for assessing the operator, operations, target, and setting in the actionability relation. [deep-dive]
5. **Keep operational alternatives visible against application requirements.** The paper derives several control strategies from one refined theory and selects among them using requirements such as number of solutions and information-gathering behavior. This supports recording rejected operationalizations as evidence of what the method deliberately leaves variable. [just-a-reference]

## Limitations (our opinion)

The paper demonstrates the framework through formalized classification examples and references earlier applications, but it does not compare construction quality, effort, reuse, or performance against alternative methods in a controlled evaluation. The examples therefore show that the stages can expose commitments, not that the framework reliably helps different designers find the right commitments or produces better systems. Its own conclusion says that mapping formal theories into control specifications can require complex transformations that are difficult to formalize; this limits any claim that the staged framework itself determines the operational method. The formal treatment also assumes that task and domain knowledge can be represented precisely enough for successive logical refinement, so transfer to open-ended agent-operated knowledge bases requires an additional account of judgment, incomplete specifications, and semantic review.

## Recommended Next Action

Update [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) with a compact three-stage commitment audit—required competence, conceptual decomposition, and operational strategy—and use the paper as evidence that each stage can expose consequential choices the framework leaves to the designer.
