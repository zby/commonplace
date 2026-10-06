---
description: Use after a profile submission to independently check memory-axis coverage and value support against the accepted records
type: types/instruction.md
---

# Verify the memory profile

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `boundary` | Frozen boundary and source register. | Always |
| `runtime`, `memory`, `epistemic`, `reconciliation` | Accepted record members. | Always |
| `profile` | Profile candidate to check independently. | Always |

## Situation

The record loop has passed: the analyst reports and the reconciliation were
judged against the frozen source. A profile job has since classified the
memory findings into the comparison axes of the supplied profile type, from
those accepted records and nothing else. Nobody has yet checked that
classification independently.

## Mission

Judge the profile against the accepted records and the profile type, and
write the verification to `output` under the supplied verification type,
with `verifies: profile`, `run-id` and the `reviewed-boundary` of `boundary`.

When you are done, every axis has been checked for scope, support and
coverage: each asserted value rests on accepted records, each unit's scope is
the type's natural unit, inventory coverage is established independently of
positive witnesses (`known` needs resolved included units and coverage
evidence, not one established existence), unresolved included parts stay in
the inventory rather than being omitted, classified absent or made
inapplicable by a known alternative, and the classification follows the
supplied definitions without added conditions. The profile type and the
record contract fix those definitions; this instruction adds none.

## Boundaries

You mark and explain; you write no replacement profile and change no record.
A blocker is an unsupported value or an unjustified coverage claim; a limit
is admissible only where the profile value already expresses the uncertainty
(`partial`, `not-determinable`, `uninspected`), since an overview caveat does
not travel with an extracted value. A faithfully stated evidence limit is
neither. No profile-only record or source quotation can establish support;
read the source only for the cited paths needed to resolve a named ambiguity,
and log each such read under Verification. New source facts cannot replace
supporting records.

Code permits one profile correction; blockers after it stop the run.

Run the acceptance check before submitting.
