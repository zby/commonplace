---
description: "Job of an analyse-agentic-system run: the memory analyst, first round or correction round"
type: types/instruction.md
---

# Analyse memory and context as the memory analyst

Read every file under `read-first` in your invocation before any other step.

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `round` | `first` or `correction`. | Always |
| `boundary` | Absolute path of the frozen boundary and Source register. | Always |
| `runtime` | Absolute path of the current runtime report. | Always |
| `epistemic` | Absolute path of the current epistemic report. | `correction` |
| `previous-report` | Absolute path of your report as the record verifier judged it. | `correction` |
| `requests` | Absolute path of the record verification whose blockers you answer. | `correction` |
| `answers` | Absolute path where you write your answers to those blockers. | `correction` |

## Task

Produce a source-grounded account of `system`'s memory mechanisms as one typed report at `output`. Code copies the
last accepted report unchanged into the set's memory member. Reconciliation
states how its records connect to the other reports; corrections to this
report are yours to make.

Work from `boundary` and `runtime`. Treat the runtime member's records as
provisional findings to check against sources. Choose the memory scope from
those routes and state its inclusions and exclusions in Boundary and
evidence. Describe storage, form, lineage, consumers and their authority,
write agency, curation, trace-fed writes and read-back selection in
source-native terms. Do not map them to controlled comparison values. Apply the supplied record
contract's source-native coverage dimensions to all included parts, not merely
a primary store or best-understood route. Retain supported facts together with
unresolved alternatives, naming missing facts and prevented conclusions. Keep
content authorship, human admission decisions and physical I/O separate;
generic caller identity does not establish human control. Describe each
transformation, request/selection/delivery operation, original trace input and
actual later consumer independently when scope or evidence differs.
The supplied memory type fixes the report content; the shared contracts fix
evidence and record conventions.

## Inspect and explain

Work through the report's sections in the order the memory report type
gives. Trace the distinguishing mechanisms on the write side and read-back
side, then challenge strong source claims, misleading labels and partial
ontology mappings. Record corrections to supplied facts and unresolved
questions under Integration issues; explain distinguishing mechanisms under
Core ideas. Keep current Commonplace recommendations outside the report; no
comparison to other systems is needed. A thin memory boundary warrants short
sections with explicit limits.

Check the frozen source's CLI dispatch, hooks, registered tools and
exposed library/service operations against the supplied runtime routes.
Trace relevant memory operations, including evaluation, cleanup, rejection
and withdrawal, through retained results and later consumers. The runtime
is a starting account, not the inspection limit. Retain the type's coverage
table; this is a memory-scope check, not a second whole-runtime inventory.

## Record the mechanisms

Prose may cite `runtime` or the Source register, and `epistemic` in
correction rounds. Acceptance requires a valid
member with references resolved against those inputs and its own records.

Before declaring records, compare referents with supplied records under
the shared record contract. Retain each overlap disposition under
Integration issues. Separate operative parts with different checks or
consumers. Declare a part of exactly one supplied record with `Part of:`
under the shared contract; a grouping spanning several supplied records
keeps its distinct-identity comparison. Flag defective supplied findings
and any needed supersession by declared parts under Integration issues.
Declare new records with `MEM-`. Keep supplied `RT-` and `EPI-` IDs unchanged
when referring to or annotating their records.

## Correction rounds

When `round = correction`, follow **Correct a report after verification** in
the supplied worker rules; the rest of this instruction still governs the
report's content. Also read `epistemic`, which you may
now cite.

## Check

Run the acceptance check before submitting; repair refusals and retain the
result and prevented conclusions under Limitations and checks. After repair,
update the check result and check the final report again.
