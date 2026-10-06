---
description: Use after independent record verification to classify the accepted records into a memory comparison profile
type: types/instruction.md
---

# Classify the verified memory records

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `boundary` | Frozen boundary and source register. | Always |
| `runtime`, `memory`, `epistemic`, `reconciliation` | Accepted record members. | Always |
| `round` | `first` or `after-blockers`. | Always |
| `previous-profile`, `verification` | Previous candidate and independent blockers. | `after-blockers` |

## Situation

The record loop has passed: the analyst reports and the reconciliation are
accepted, and no record will change. Comparison consumers need the memory
findings classified into the supplied profile type's axes, with the
uncertainty each value carries expressed in the value itself.

## Mission

Write a revision-2 profile to `output` under the supplied profile type, every
value warranted by accepted records. The type fixes the axes, the natural
units, the controlled values, the metadata and the Comparison rationale
section; the record contract fixes the coverage and uncertainty rules; both
are applied as written, without added conditions.

When you are done, every asserted value cites records already in the set;
where a needed fact is absent from them, the unit carries a warranted
`partial`, `uninspected` or `not-determinable` assessment naming the missing
fact and the prevented conclusion; unresolved included units stay in the
inventory; an axis is `known` only with accepted coverage evidence and all
units resolved, since a positive witness does not establish complete
inventory; and supported positives and route-specific evidence strength are
preserved beside the unresolved parts.

## Boundaries

Declare no records, add no quotes or evidence, edit no member, and do not
reopen record verification. Resolve superseded records through the
reconciliation; the reports already carry their corrections. Source reading
is bounded to a named ambiguity in a cited record, at its cited paths and the
frozen revision; log each read under Comparison rationale with path, lines
and the ambiguity resolved. Source understanding cannot replace a missing
supporting record. Do not read an incumbent or reference profile.

After blockers, read `previous-profile` and `verification` and correct only
the profile; there is one correction round.

Run the acceptance check before submitting.
