---
description: "OMG CMMN 1.1 standard for knowledge-worker case models: separates design-time discretion catalogues, engine-tracked plan-item lifecycles, and human run-time planning and activation"
source: https://www.omg.org/spec/CMMN/1.1/
captured: "2026-10-31"
capture: pdftotext
capture_scope: full-source
genre: design-proposal
snapshot_sha256: 5ebc44b946e377b05d5e075e35f448e421dd8438a9fb9ee68f377ca3adf4b89a
ingested: "2026-10-31"
occasion: "workshop kb/work/operationalization-executability-automation asks how operationalizing knowledge for a defined task and executor relates to execution, function-level automation, and decision autonomy. This is the OMG Case Management Model and Notation 1.1 specification; capture the normative specification PDF linked from this page, not only the landing page."
type: types/ingest-report.md
domains: [case-management, cmmn, workflow-modeling, run-time-planning]
tags: [method-guided-action]
---

# Ingest: Case Management Model and Notation (CMMN) Version 1.1

## Classification

This is an adopted normative industry standard (OMG document formal/2016-12-01, 144 pages), not a research paper. It defines a metamodel, a graphical notation, XMI/XSD interchange formats, conformance classes and execution semantics. The closest genre in the vocabulary is `design-proposal`, read here as a ratified design for a class of systems rather than a proposal for one system. The capture is the full specification PDF extracted to text. Figures and the lifecycle diagrams are therefore missing, but the state tables and rule definitions survive. The embedded PDF title metadata ("Business Motivation Model") is wrong; the document text identifies CMMN 1.1.
Author: Object Management Group, with copyright holders including IBM, Oracle, SAP, TIBCO, BizAgi, Cordys and SINTEF. It is a vendor-consortium standard aimed at interoperability between case-management products.

## Summary

CMMN models work that "cannot be orchestrated by a predefined sequence of Tasks" (4.1). It positions itself as BPMN's complement for case work such as claims, permitting and diagnosis, where knowledge workers decide at run time which tasks apply and in what order. A case model has two phases. At design time, business analysts define predefined segments plus *discretionary* items, collected in PlanningTables and gated by Role authorizations and ApplicabilityRules evaluated over the CaseFile, the shared case data (5.4.9). At run time, case workers "plan" by moving discretionary items into the case instance (8.7). Execution semantics follow the guard-stage-milestone formalism (Hull 2010). Plan items have lifecycles. Sentries combine event OnParts with a CaseFile IfPart and trigger entry and exit (8.5). Behavior property rules decide whether an enabled item starts automatically or waits for a human (ManualActivationRule), whether an item must finish before its stage can complete (RequiredRule), repetition, and stage auto-completion (8.6). Task types separate who or what does the work: HumanTask (a case worker), ProcessTask (calls a business process), CaseTask and DecisionTask (5.4.10). The specification says it is "focused on modeling and notation, not run-time Case management per se". It defines execution semantics only to give state-dependent rules a meaning. 4.2 states the intended evolution: a model may start "entirely at the discretion of human participants". Analysts then fold emerging patterns back in "in the form of improved rules and more predictable patterns of Tasks".

## Quotes

No source quotes have been retained yet.

## Connections Found

For the occasion, the source serves as a **worked standard that separates the axes the workshop is trying to distinguish**. A conformant CMMN engine executes the model: it tracks plan-item states, evaluates sentries and enforces completion rules. Executing the model does not automate the work. Whether a task's function is automated is a separate per-task choice (HumanTask versus ProcessTask or DecisionTask). Who decides is separated again into run-time planning by case workers and ManualActivationRule. A non-blocking HumanTask is "manual": the engine does not track its lifecycle at all. This makes CMMN a comparison case for [Methodological and computational closure track different changes](../theory/methodological-and-computational-closure-track-different-changes.md) — compares-with: a CMMN model can settle routing and completion conditions while a human still decides content and selection, which is methodological settlement without computational closure. It also compares with the per-function allocation of [Parasuraman, Sheridan, Wickens](./model-types-levels-human-interaction-automation.ingest.md) — compares-with on the axis of human/automation allocation. PSW allocates by information-processing stage and level. CMMN allocates per plan item through task type, activation rule and discretionary planning.

On the design-time/run-time boundary, the source is a **pre-LLM, human-executor counterpart** to several theory notes. It is a standardized way of leaving bounded choices to an executor with live case evidence, as [An author should fix what the executor can't determine, not what it will](../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) recommends — compares-with on design-time fixing versus run-time discretion. Its engine/judgment split parallels [Scheduler-LLM separation](../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — compares-with: lifecycle bookkeeping and sentry evaluation sit in the engine, and selection and ordering stay with humans. The analyst cycle in 4.2 is a prescribed instance of [progressive constraining](../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) — is-evidence-for: an independent industry practice of committing rules only after patterns emerge. It extends the claim's scope beyond LLM code generation, but as a recommendation, not a measured outcome. The analysts' rule-formalization is [codification](../theory/definitions/codification.md) in the KB's sense only at the engine-evaluated end — defined-in.

On representation, the source is a **counter-case** for [Statecharts and programs differ in what they show, not compute](../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) — compares-with on drawing control whose plan is produced at run time. CMMN draws the planning *scope* (catalogue plus PlanningTables) and never draws the instance plan. It also offers a mature formalism for the open question in [A functioning KB needs a workshop layer](../theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — compares-with on how much lifecycle formalism work-in-motion needs. Plan-item states, RequiredRule and autoComplete give an explicit account of when unfinished work may leave the active set, as discussed in [Active work state is not retrospective memory or chat history](../theory/active-work-state-is-not-retrospective-memory-or-chat-history.md) — compares-with on closure criteria for live work.

No existing KB artifact treats CMMN, BPMN or guard-stage-milestone directly.

- [CMMN 1.1 specification](https://www.omg.org/spec/CMMN/1.1/) — derived-from: this analysis is worked out from the normative OMG document formal/2016-12-01.

## Extractable Value

1. **Model execution, function automation and decision allocation are separate dials in a deployed standard** -- CMMN separates (a) an engine that executes the model's state semantics, (b) per-task choice of performer type (HumanTask versus ProcessTask or DecisionTask), (c) per-item choice of who starts enabled work (ManualActivationRule), and (d) who selects and orders work (discretionary planning by authorized Roles). That gives the workshop a concrete non-LLM example: an operationalized, executable case model with no function-level automation and no decision autonomy for the engine. It supports keeping "executable", "automated" and "autonomous" as separate predicates. [quick-win]
2. **Operationalization is relative to a named executor, in the standard's own structure** -- the same knowledge appears in different forms depending on who consumes it. Engine-evaluated sentries and rules over the CaseFile are for the engine; PlanningTables, applicability filters and Role authorizations shape what a human planner sees; tacit knowledge stays with participants (4.1 lists all four knowledge sources). This is a usable case for the workshop's "defined task and executor" framing. [quick-win]
3. **Discretion as a declared, bounded catalogue rather than an absence of specification** -- PlanningTables plus ApplicabilityRules make the discretion boundary a versionable design object. Read with progressive constraining and preferential codification, this suggests a candidate claim: mature human-work standards already institutionalize a two-phase discretion boundary (declared catalogue, then iterative codification of observed patterns). The claim needs testing before promotion. [deep-dive]
4. **Guard-stage-milestone as a reference design for KB workshop lifecycles** -- sentries over shared state instead of sequence edges, plus required/optional completion rules, are a candidate formalism or cautionary comparison when deciding whether workshop artifacts need validated state machines. [experiment]
5. **Retrieval vocabulary** -- "discretionary item", "planning table", "manual activation", "required rule" and "case file" name distinctions the KB currently describes informally for agents. [just-a-reference]

## Limitations (our opinion)

This is a design standard, not evidence that the design works. It shows no outcome data on whether discretionary catalogues or iterative analyst codification improve case results. 4.2's evolution story is aspirational ("should be expected to evolve"), so using it as support for progressive constraining shows only that the practice was institutionalized, not that it was validated. The specification is explicitly about modeling and notation, "not run-time Case management per se". It says nothing about how case workers actually use PlanningTables, how often discretion is exercised, or how the discretion boundary was chosen. It gives no warrant account for which items stay discretionary, so it cannot ground claims about warranted autonomy. It is a vendor-consortium standard: features reflect what member products could agree to interchange, and the gap between conformance claims and real deployments is not shown. The executors are human case workers. Transfer to LLM executors holds only where the mechanism is shared (engine-enforced state versus judgment); it does not carry over assumptions about tacit knowledge or organizational accountability. The text capture drops all figures, including the lifecycle state diagrams, so any claim about exact transition graphs should be checked against the PDF.

## Recommended Next Action

Add CMMN 1.1 to the operationalization workshop's exploration as a worked case. Map its four separated dials (engine-executed model, performer type, manual activation, discretionary planning) onto the workshop's distinctions between operationalization, execution, function-level automation and decision autonomy, and record where the mapping fails.
