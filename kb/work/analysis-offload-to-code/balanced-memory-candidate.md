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

## Mission and discretion

Write `output` as the source-grounded memory account and comparison profile
under the supplied type. Code retains the accepted report unchanged;
reconciliation integrates it through amendments. Verify `runtime`'s provisional
findings against `boundary`'s sources. State scope inclusions and exclusions
in both the profile and Boundary and evidence.

Choose inspection order and depth from the memory mechanisms. Trace write
and read-back paths; challenge strong claims, misleading labels and partial
ontology mappings. The type fixes sections, profile meanings and support;
shared contracts fix evidence and records. Thin boundaries warrant short,
explicitly limited sections. Exclude current Commonplace recommendations;
comparison with other systems is unnecessary.

## Coverage and integration checks

Check CLI dispatch, hooks, registered tools and exposed library/service
operations against supplied runtime routes. Follow memory evaluation,
cleanup, rejection and withdrawal through retained results and later consumers,
including routes the runtime missed. Retain the type's coverage table within
memory scope; distinguish directly read source from supplied findings.

Before new declarations, compare referents with supplied records. Separate
parts with different checks or consumers. Retain overlap dispositions,
needed canonical splits, corrections and unresolved questions under
Integration issues. Profile citations need local declarations or annotations;
other prose may cite `runtime`, the Source register and, in correction rounds,
`epistemic`.

## Correction rounds

For `first`, write the initial report. For `correction`, read
`previous-memory`, `returned-findings` and `epistemic`. Answer every returned
finding from sources: correct supported defects; retain disputed findings
with their evidence. Submit the whole replacement report.

Preserve surviving IDs and referents; give new records fresh numbers and never
reuse dropped ones. Dropped records need no withdrawal marker: only the accepted
report enters the set, while returned findings use the previous report's IDs.

## Acceptance

Run `commonplace-validate --full <output>` and repair structural defects.
Retain the result and prevented conclusions under Limitations and checks;
after repair, update the result and validate the final bytes again. References
must resolve against this report and its permitted inputs. Publication checks
set quotations; run no separate quote check. Worker rules govern authority
and problem returns.
