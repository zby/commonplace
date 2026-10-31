# Operationalization, executability, automation, and autonomy

**Commissioned:** 2026-10-31 by the operator. **Revised:** 2026-10-31 following operator feedback on dimensionality, automation/autonomy, source ingestion, and locating application-area generalization in task definition rather than operationalization. **Revised again:** 2026-10-31 after merge, review, and the ingestion of five candidate sources.  
**Status:** scoped conceptual investigation, not adopted vocabulary or an empirical test.  
**Repository baseline:** `d19065b3aef33ffca92fa2f72f5203251fcae3b0` (main when opened).

## Purpose

Commonplace aims to make open-ended text-mediated knowledge work progressively executable by LLM-based systems. Investigate how operationalizing a methodology, executing it, automating functions, and delegating control are related but different.

The operator's revision questions are binding on this workshop:

1. Generalizing a methodology and constraining it are different changes, but they are not the only dimensions. Distinguish the method's domain and coverage from the executor's operational support and actual reach.
2. Do not collapse automation (performed work) with autonomy (discretion, authority, and unattended continuity). Test whether operationalization suffices to make a task fully executable and fully automated by LLMs.
3. Verify which literature is already ingested and whether full sources can be ingested; do not create duplicates, assume an abstract is a full source, or assume public retrieval licenses redistribution.
4. Revise architectural implications using the multidimensional account rather than a one-way chain from methodology to code.
5. **Task definition fixes the application area**, objective, admitted cases and success criteria. Operationalization concerns how knowledge K becomes usable for this task T by executor E under specified conditions; **generalizing to T' is a separate task-scope or method-scope investigation**, not part of operationalization for T.
6. The same task-relative operation may work a theory into methodology or existing methodology into an executor-facing skill. Name source and output when discussing provenance; these are not compulsory successive stages. Preserve the narrower `operationalized-from` artifact-lineage rule.
7. Revisit vocabulary and extraction recommendations only after those distinctions are settled.

## Scope and evidence requirements

- Compare human checklists, pen-and-paper algorithms, natural-language LLM skills, deterministic scripts, agent workflows, and human–machine arrangements.
- Reuse current [actionable methodology](../../theory/definitions/actionable-methodology.md), [methodological/computational closure](../../theory/methodological-and-computational-closure-track-different-changes.md), [constraining](../../theory/definitions/constraining.md), [codification](../../theory/definitions/codification.md), and [behavioral authority](../../theory/definitions/behavioral-authority.md) before minting vocabulary.
- Respect the existing `operationalized-from` lineage meaning in [ADR 054](../../reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md).
- Read sources using the actual discipline's meaning; evaluate transfer rather than simply borrowing terminology. A check for the availability of original texts is not a completed source ingest.
- Do not implement machinery, modify shipped instructions or definitions, or claim measured comparative improvement without a trial.

## Present findings and limitations

The revised [exploration](./exploration.md) treats **task T as supplying the application area and success boundary**, while *operationalization* concerns making existing knowledge K usable by executor E to perform T in setting S. Generalizing the knowledge or broadening its task area requires a separate scope claim and, where appropriate, a revised task T'. A task-specific operationalization can entail constraining, method elaboration, method selection, tools or integration, but does not require a particular output format or a fixed sequence of steps. This is not an intrinsic rank of an artifact. Theory → methodology and methodology → skill are two possible source-to-task paths; neither is a necessary intermediate stage. The accepted `operationalized-from` label remains the narrower methodology-to-procedure **lineage** claim. The exploration also separates actual task execution, automation, discretionary autonomy, unattended completion, and warranted outcome quality. No new technical definition has been adopted.

It also distinguishes full bounded task automation by computation from decision autonomy. An LLM can supply decisions not settled by the retained method; a fully written procedure alone cannot confer required capabilities, authority or reliability.

The second revision rests on nine new ingests: [Norman](../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md), the Stanford Encyclopedia entries on the [Church–Turing thesis](../../sources/church-turing-thesis-sep.ingest.md) and [operationalism](../../sources/operationalism-sep.ingest.md), [Plotkin](../../sources/plotkin-origins-of-sos.ingest.md), [CMMN 1.1](../../sources/cmmn-1-1-specification.ingest.md), [Haynes](../../sources/surgical-safety-checklist-haynes-2009.ingest.md) and three secondary readings of Suchman ([Dittrich](../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md), [Duguid](../../sources/duguid-on-rereading-suchman-situated-action.ingest.md), and a [1997 course summary](../../sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md)), beside the three reports already in the KB. Section 6 of the exploration turns them into worked cases. Section 0 adds three conditions to the provisional relation from the operationalism literature. The Suchman book itself is not ingested; the source table records why.

The review of the merged draft found three faults, now corrected in the exploration: the findings restated the commission, the actionable-methodology relation was described as narrower than it is, and five workshop-local coordinates were introduced without saying which are new. Only generality and operational integration are new; the others reduce to existing definitions.

## Answers to the binding questions, 2026-10-31

1. **Answered and adopted.** The method's domain is the task's application area, which the [actionable-methodology definition](../../theory/definitions/actionable-methodology.md) now carries as the task element; the executor's support is the operator, operations, target and setting elements; coverage is closure without the settling condition; reach is the relation holding over the admitted cases. Exploration sections 0 and 2.
2. **Answered in the negative by cases.** Operationalization coincides with automatability only for an executor permitted no insight (the effective method, 6.1). Haynes is operationalized with nothing automated (6.5); CMMN is executable with no function automated and no engine discretion (6.3); Norman separates automating a function from automating a role (6.2). Automation, decision autonomy and unattended continuity are kept apart in section 3 and already in the closure note. No empirical test was run and none is needed for the question as posed.
3. **Done.** Nine ingests, no duplicates, abstracts distinguished from full sources, snapshots kept ignored. The Suchman book is the one gap; three secondary readings stand in.
4. **Answered in the workshop, extraction unchecked.** Section 4 replaces the one-way chain with a map of independent changes and a diagnosis-first rule. The library already holds parts of that rule in [three-way diagnosis](../../theory/llm-output-deviation-requires-three-way-diagnosis.md), [relaxing-candidate signals](../../theory/operational-signals-that-a-component-is-a-relaxing-candidate.md) and [determinability](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md). Whether the ten-mechanism table adds anything to those is the open check.
5. **Answered and adopted**, as item 1: the task is an input to the relation, and widening it is a separate claim.
6. **Answered; one sentence pending.** Theory to methodology and methodology to skill are two instances of one task-relative operation, not stages. `operationalized-from` stays the narrow lineage edge. The pending sentence would say in the actionable definition that "operationalize" stays ordinary English, that its technical content is the actionable relation, and that the lineage edge records one way of achieving it.
7. **Now open.** The distinctions are settled enough to revisit vocabulary: the recommendation is no new term. Extraction candidates are in exploration section 8.

## Closure rule

Close only after either (a) making an evidence-backed, nonduplicative theory extraction or (b) documenting why existing definitions suffice and the additional distinction stays in workshop analysis. Current position: the task-relative claim is extracted on path (a) as an amendment to the [actionable-methodology definition](../../theory/definitions/actionable-methodology.md) (disposition item 7); the remaining distinctions sit on path (b) pending the proposed tests. Strong causal claims about the benefit of operationalization require comparisons for the **same T, E and objective**, with documented changes to K, instructions or environment. Claims about generality require separate comparison on T' with its application area declared. The proposed tests are in the exploration; none were run.

## Deliverable

- [Revised conceptual account, worked cases from the ingested sources, tests, and source status](./exploration.md).
