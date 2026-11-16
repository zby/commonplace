---
description: "RE ontology separates verifiable constraints from revisable softgoal approximations and stakeholder preferences, but leaves authority and practical revision methods open."
source: https://arxiv.org/abs/0811.4364v1
captured: "2026-11-16"
capture: pdftotext
capture_scope: full-source
doi: "10.1109/RE.2008.13"
genre: scientific-paper
snapshot_sha256: 3fd5ccf2031710b6ef8aafae9cd10dc890050d03be2207c83d2cd19c2a9895cf
ingested: "2026-11-16"
occasion: "What can requirements engineering contribute, and what are its limits, for understanding operationalization, goal authority, and revisable knowledge in agent-operated knowledge work?"
type: types/ingest-report.md
domains: [requirements-engineering, justified-approximation, softgoals, stakeholder-preferences]
learning_claims: true
---

# Ingest: Revisiting the Core Ontology and Problem in Requirements Engineering

## Classification

A theoretical scientific paper proposing an ontology and revised requirements problem through conceptual argument, definitions, and illustrative flight-booking examples, not empirical evaluation. Authors: Ivan J. Jureta, John Mylopoulos, and Stéphane Faulkner, affiliated in the captured text with Namur and Toronto. The paper identifies itself as an RE 2008 conference publication and reports a best-paper award. This observation is the arXiv 0811.4364v1 conference preprint, not the 2009 Applied Ontology journal article. The served PDF prints an October 2018 date despite its 2008 identifier; the capture does not establish original-2008 PDF bytes.

## Summary

Jureta, Mylopoulos, and Faulkner extend the requirements problem of finding a specification that, with domain assumptions, entails requirements. Starting from stakeholder communication, they distinguish beliefs, desires, intentions, and evaluative attitudes, grounding their definitions in speech-act theory and DOLCE. The resulting ontology separates goals, measurable quality constraints, subjective or ill-defined softgoals, plans, and domain assumptions. A quality constraint can stand in for a softgoal only through a project-local justified approximation supported by sufficient correlation, and new information can defeat that approximation. Optionality and preferences, including preferences over preferences, guide selection among alternatives; defeasible consequence replaces monotonic satisfaction. The result is a conceptual account of what information requirements work should represent and what a desirable specification must account for, not a tested procedure for elicitation, justification, or revision.

## Contribution assessment (our opinion)

The important contribution appears to be making normally implicit evaluative and approximation commitments explicit within the requirements problem. Compared with the Zave–Jackson baseline as presented here, distinguishing constraint satisfaction from a justified softgoal approximation gives criticism a more precise target than a loosely labeled contribution link. Definitions and counterexamples provide conceptual progress without needing an empirical benchmark. Their practical significance remains tentative: the paper leaves elicitation, preference aggregation, and adequacy of approximation justification substantially open, so it establishes a useful problem formulation rather than a demonstrated solution. The available comparisons support that narrower judgment, not a literature-wide originality claim.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a conceptual companion to [Exact implementation does not validate a requirement against its objective](../theory/exact-implementation-does-not-validate-a-requirement.md): satisfying a measurable quality constraint and establishing that it approximates a softgoal are separate obligations. Its distinctive addition is an explicit, local, defeasible approximation relation, not empirical confirmation of any particular proxy. It also provides a boundary comparison with [Revising an improvement objective is licensed from outside it or is not improvement](../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md). Preferences and preferences over preferences represent rankings, but the paper takes stakeholder inputs and an aggregate preference as given; representing these does not establish who may authorize a change of terminal ends. These two comparisons directly serve the occasion without treating the source as a complete theory of agent-operated knowledge work.

## Learning Claims (our opinion)

The source's adaptation mechanism is conceptual: new information may defeat an approximation or a conclusion about plans satisfying requirements, and the engineer can revise the approximation or specification. This is not model training. A source-side belief is communicated content classified as a domain assumption, not established truth; a plan is communicated intended action, not necessarily a stored agent workflow. Defeasible consequence permits withdrawal of conclusions but does not itself discover errors or select repairs.

Against the [theory builder](../theory/definitions/theory-builder.md) conditions, localized content is explicitly supported by separately represented assumptions, plans, constraints, softgoals, and approximation claims. Consumption is prescribed: these contents determine specification acceptability and preference. Content-directed criticism is illustrated by discovering that screen count does not explain stakeholders' convenience evaluations, but no working criticism process is demonstrated. Iteration is anticipated through revision after new information, not documented through a retained criticism-and-repair sequence. Persistence within a development project is compatible with the account; retention across projects or runs is not specified. Improved capacity for future action is therefore a possible consequence, not an observed learning result.

The comparison with [learning inside a fixed decomposition](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) matters at the approximation boundary: choosing better plans under one fixed quality constraint cannot establish that the constraint captures the softgoal. The paper explicitly allows that mapping to change. It does not show a process that can revise its own ontology, stakeholder boundary, or preference aggregation. Our interpretation is that the ontology supplies objects for criticism in a knowledge system, not sufficient machinery to make that system a functioning theory builder.

## Extractable Value

1. **Operationalization needs its own revisable claim.** The justified-approximation relation separates checking a constraint from assessing whether it serves a softgoal. For KB methodology, a validator threshold or review rubric can be treated as an operational measure whose relation to the intended quality needs separate scope and criticism. This adds a concrete conceptual comparison to the existing exact-implementation note; the source does not empirically validate the transfer. [quick-win]
2. **Ranking is not goal authority.** Optionality, preferences, and preferences over preferences make selection criteria explicit. They do not determine legitimate stakeholders or authorize an agent to replace the ends it was given. This bounds what requirements engineering contributes to the occasion: it represents evaluative inputs more clearly than it warrants them. [just-a-reference]
3. **Revisability needs more than defeasible notation.** Separately recording domain assumptions and softgoal approximations gives later criticism identifiable targets. A useful KB experiment would check whether retaining those targets and their defeat conditions improves later repairs, rather than assume that non-monotonic inference alone produces learning. The paper supplies the distinction, not outcome evidence. [experiment]

## Limitations (our opinion)

No intervention, benchmark, or controlled comparison tests whether this ontology improves elicitation, specification quality, or later revision. Flight-booking examples explain the definitions but do not establish their coverage of real stakeholder communication. Coverage relative to a speech-act taxonomy is also narrower than completeness of a project's relevant concerns: uncommunicated needs and mistaken interpretations remain possible.

The critical approximation relation requires justification and sufficient correlation, but adequacy is left project-specific and the paper acknowledges missing methodological support. Shared measurement makes a constraint checkable; it does not establish that the measurement captures the desired quality. Local justification may be mistaken, and correlation alone does not show that changing a measure will improve the softgoal.

The treatment of preferences assumes aggregation and leaves properties of preference orders outside scope. It consequently cannot settle stakeholder conflict, authority to institute rules, or legitimate changes of ends merely by representing preferences. Declarative and asserted content can enter the same domain-assumption category without resolving the different grounds on which an adopted rule and an empirical claim should be criticized.

The critique of monotonic consequence should not be accepted as a general logical result. Monotonicity does not itself require a sound and complete description of the real environment, nor prevent revising premises between analyses. Defeasible consequence is one way to represent retractable conclusions, not by itself a repair method or a demonstration that the baseline cannot support revisable engineering. These limits narrow the revised formulation's claimed superiority without removing its useful distinction between satisfaction and approximation warrant.

## Recommended Next Action

Update [Exact implementation does not validate a requirement against its objective](../theory/exact-implementation-does-not-validate-a-requirement.md) with a bounded comparison to this paper's project-local, revisable softgoal approximation, explicitly distinguishing its conceptual proposal from empirical validation.
