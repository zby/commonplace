# Operationalization, executability, and automation

**Commissioned:** 2026-10-31 by the operator.  
**Status:** scoped conceptual investigation; findings in [exploration.md](./exploration.md).  
**Repository baseline:** `d19065b3aef33ffca92fa2f72f5203251fcae3b0` (`main` when opened).

## Problem

Commonplace wants to make open-ended, text-mediated knowledge work progressively more usable and executable by LLM-based systems. The operator asks whether *operationalizing a methodology*, *executing it*, and *automating the task* are different operations, how that difference affects architecture, and whether increased operational fitness requires increasing constraint.

The investigation must handle human checklists, pencil-and-paper algorithms, LLM research, scripts, bounded agent workflows, and human–machine systems. Treat vocabulary from mathematics, knowledge engineering, philosophy of science, organizational processes, and human-factors engineering as local to its domain unless transfer is justified.

## Scope and evaluation

- Read current repository definitions and related research before proposing vocabulary. Base this work on the specific repository revision above, rather than the published site's build.
- Compare concepts by counterexample: a proposed implication fails if a realistic case satisfies its premise but not its conclusion.
- Separate *what a method settles*, *what a particular executor can do*, *what a configured system delegates to computation*, and *whether that arrangement succeeds*.
- Compare how the work is arranged in practice; do not claim empirical gains without a trial.
- Do not implement tools, alter shipped instructions or definitions, or claim that a new term is adopted.

## Present disposition

The findings support a conceptual distinction, but much of its machinery is already named in [actionable methodology](../../theory/definitions/actionable-methodology.md), [methodological/computational closure](../../theory/methodological-and-computational-closure-track-different-changes.md), [constraining](../../theory/definitions/constraining.md), [codification](../../theory/definitions/codification.md), and [behavioral authority](../../theory/definitions/behavioral-authority.md). [ADR 054](../../reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md) already assigns a specific sense to `operationalized-from`. Do not mint a new definition or rewrite it on this evidence alone. The narrow supported claim and vocabulary risks are recorded in the findings.

## What would close this workshop

Either (a) extract a narrowly bounded, nonduplicative conclusion into the appropriate theory note with a reviewed relation to the existing definitions, or (b) record a deliberate decision that the distinction stays explanatory, not normative, with no independent definition. For a stronger empirical claim about improvement, first compare target-executor runs with and without routing, resource availability, feedback/recovery, and added step detail, under fixed acceptance conditions. No such trials were run in this investigation.

## Deliverable

- [Exploration and disposition](./exploration.md) — terminology map, counterexamples, literature, architectural predictions, and tests not yet run.
