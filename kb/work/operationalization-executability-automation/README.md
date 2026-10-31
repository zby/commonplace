# Operationalization, executability, automation, and autonomy

**Commissioned:** 2026-10-31 by the operator. **Revised:** 2026-10-31 following operator feedback on dimensionality, automation/autonomy, source ingestion, architectural implications, and executor-relative operationalization.  
**Status:** scoped conceptual investigation, not adopted vocabulary or an empirical test.  
**Repository baseline:** `d19065b3aef33ffca92fa2f72f5203251fcae3b0` (main when opened).

## Purpose

Commonplace aims to make open-ended text-mediated knowledge work progressively executable by LLM-based systems. Investigate how operationalizing a methodology, executing it, automating functions, and delegating control are related but different.

The operator's revision questions are binding on this workshop:

1. Generalizing a methodology and constraining it are different changes, but they are not the only dimensions. Distinguish the method's domain and coverage from the executor's operational support and actual reach.
2. Do not collapse automation (performed work) with autonomy (discretion, authority, and unattended continuity). Test whether operationalization suffices to make a task fully executable and fully automated by LLMs.
3. Verify which literature is already ingested and whether full sources can be ingested; do not create duplicates, assume an abstract is a full source, or assume public retrieval licenses redistribution.
4. Revise architectural implications using the multidimensional account rather than a one-way chain from methodology to code.
5. Operationalization is **relative to the executor** and task: distinguish the source-to-artifact lineage claim from situated usability by a specified human, model or mixed system.
6. Distinguish a methodology worked out from a theory from an executor-specific procedure worked out from a methodology. The verb 'operationalize' can refer to both; identify source and target rather than silently making the stages an identity or a compulsory regress.
7. Revisit vocabulary and extraction recommendations only after those distinctions are settled.

## Scope and evidence requirements

- Compare human checklists, pen-and-paper algorithms, natural-language LLM skills, deterministic scripts, agent workflows, and human–machine arrangements.
- Reuse current [actionable methodology](../../theory/definitions/actionable-methodology.md), [methodological/computational closure](../../theory/methodological-and-computational-closure-track-different-changes.md), [constraining](../../theory/definitions/constraining.md), [codification](../../theory/definitions/codification.md), and [behavioral authority](../../theory/definitions/behavioral-authority.md) before minting vocabulary.
- Respect the existing `operationalized-from` lineage meaning in [ADR 054](../../reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md).
- Read sources using the actual discipline's meaning; evaluate transfer rather than simply borrowing terminology. A check for the availability of original texts is not a completed source ingest.
- Do not implement machinery, modify shipped instructions or definitions, or claim measured comparative improvement without a trial.

## Present findings and limitations

The revised [exploration](./exploration.md) separates properties of methodology (domain, constraints, coverage), runtime (activation, operations, state and authority), and actor/outcome (executability, automation, decision autonomy, required human interventions, warranted quality). **Operationalization is a source-to-use claim relative to an intended executor and task, not an intrinsic rank of a document**. It has at least two potentially confused senses: theory → prescriptive methodology for an operator class, and methodology → procedure or skill for a particular executor. A methodology may contain native guidance not derived from a single theory; some executors need no additional procedure. The accepted `operationalized-from` label remains the narrower methodology-to-procedure lineage claim. Deployment/integration is another operation and does not necessarily create new lineage. No new technical definition has been adopted.

It also distinguishes full bounded task automation by computation from decision autonomy. An LLM can supply decisions not settled by the retained method; a fully written procedure alone cannot confer required capabilities, authority or reliability. The literature table identifies three already-ingested sources and full-text paths for further candidates; **no new primary sources were ingested as part of this availability check**.

## Closure rule

Close only after either (a) making an evidence-backed, nonduplicative theory extraction or (b) documenting why existing definitions suffice and the additional distinction stays in workshop analysis. Strong causal claims about the benefit of any route require target-executor comparisons holding task boundaries and accepted results fixed. The proposed tests are in the exploration; none were run.

## Deliverable

- [Revised conceptual account, tests, and source-availability audit](./exploration.md).
