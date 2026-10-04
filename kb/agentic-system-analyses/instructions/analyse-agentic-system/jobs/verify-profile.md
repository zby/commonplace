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

## Task

Ensure every memory classification has the scope and support its type requires.
Read every supplied read-first file. Inputs are the profile, boundary, runtime,
memory, epistemic and settled reconciliation, profile type and record/source
contracts. The supplied paths and frozen source define the evidence boundary.

Write output with exactly these sections:

```markdown
### Profile verification

### Blockers
```

Check each of the ten axes against the supplied definitions and accepted records,
including amendments and supersessions. Check scope, all supported positives,
per-value evidence strength, canonical IDs and the missing facts named by weaker
assessments. No profile-only record or source quote can establish support.
Classify from the supplied definitions without added conditions; decay requires
forgetting or downweighting, not a time-based policy.

Record the checked axes and consequential limits. Write no replacement profile
and do not change records or reopen reconciliation. Under Blockers write exactly
none, or a Markdown list with one - entry per blocker, its axis, full affected
IDs and what resolves it. An unsupported value or unjustified coverage claim is
a blocker; a faithfully stated evidence limit is not. Record faults become
bounded assessments or a problem if no faithful profile is possible. Source
reading is bounded to the cited paths needed to resolve a named ambiguity;
log path, lines and purpose under Profile verification. New source facts cannot replace supporting records.
The coordinator permits one profile correction; persistent blockers stop the run.

Run the acceptance check before submitting.
