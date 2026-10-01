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
| `runtime` | Absolute path of the runtime member. | Always |
| `previous-memory` | Absolute path of the previous memory report. | `correction` |
| `returned-findings` | Absolute path of the reconciliation requesting this correction. | `correction` |
| `epistemic` | Absolute path of the epistemic member. | `correction` |

## Task

Produce a source-grounded account of `system`'s memory mechanisms and comparison classifications as one typed report at `output`. Code copies the accepted report unchanged into the set's memory member. The reconciliation owns integration and records its corrections as amendments in the reconciliation member.

Work from `boundary` and `runtime`. Treat the runtime member's records as provisional findings to check against sources. Choose the memory scope from those routes and state its inclusions and exclusions in the profile's `scope` and the report's Boundary and evidence. The supplied memory type fixes the report content and comparison profile;
the shared contracts fix evidence and record conventions.

## Inspect and explain

Work through the report's sections in the order the memory report type gives. Trace the distinguishing mechanisms on the write side and read-back side, then challenge strong source claims, misleading labels and partial ontology mappings. Record corrections to supplied facts and unresolved questions under Integration issues; explain distinguishing mechanisms under Core ideas. Keep current Commonplace recommendations outside the report; no comparison to other systems is needed. A thin memory boundary warrants short sections with explicit limits.

Check the frozen source's CLI dispatch, hooks, registered tools and
exposed library/service operations against the supplied runtime routes.
Trace relevant memory operations, including evaluation, cleanup, rejection
and withdrawal, through retained results and later consumers. The runtime
is a starting account, not the inspection limit. Retain the type's coverage
table; this is a memory-scope check, not a second whole-runtime inventory.

## Classify and record

Use the memory type's comparison definitions. Profile citations must be
declared or annotated locally; other prose may cite `runtime` or the Source
register, and `epistemic` in correction rounds. Acceptance requires a valid
member with references resolved against those inputs and its own records.

Before declaring records, compare referents with supplied records under
the shared record contract. Retain each overlap disposition under
Integration issues. Separate operative parts with different checks or
consumers and flag any needed canonical split for reconciliation.

## Correct returned findings

When `round = first`, write the initial report. When `round = correction`, read `previous-memory`, `returned-findings`, and `epistemic`. Answer each returned finding from the sources: correct the report where the finding holds, and keep your finding with its evidence where it does not. Write the whole report again; it replaces the previous report.

A surviving record keeps its ID and referent. A new record gets a new number; never reuse a number from a dropped record. No withdrawal marker is needed for a dropped record: only the accepted report enters the set. The returned findings still refer to the previous report's IDs.

## Check

Validate `output` with `commonplace-validate --full <output>` and correct structural errors. Code checks the written quotations before accepting the report, and publication checks them again; run no separate quote check. Retain the validation result and prevented conclusions under Limitations and checks.

After repair, update the check result and validate the final report again.
