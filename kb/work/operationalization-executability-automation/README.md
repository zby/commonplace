# Operationalization, executability, automation, and autonomy

**Commissioned:** 2026-10-31 by the operator. **Revised:** 2026-10-31 following operator feedback on dimensionality, automation/autonomy, source ingestion, and locating application-area generalization in task definition rather than operationalization.  
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

It also distinguishes full bounded task automation by computation from decision autonomy. An LLM can supply decisions not settled by the retained method; a fully written procedure alone cannot confer required capabilities, authority or reliability. The literature table identifies three already-ingested sources and full-text paths for further candidates; **no new primary sources were ingested as part of this availability check**.

## Closure rule

Close only after either (a) making an evidence-backed, nonduplicative theory extraction or (b) documenting why existing definitions suffice and the additional distinction stays in workshop analysis. Strong causal claims about the benefit of operationalization require comparisons for the **same T, E and objective**, with documented changes to K, instructions or environment. Claims about generality require separate comparison on T' with its application area declared. The proposed tests are in the exploration; none were run.

## Deliverable

- [Revised conceptual account, tests, and source-availability audit](./exploration.md).
