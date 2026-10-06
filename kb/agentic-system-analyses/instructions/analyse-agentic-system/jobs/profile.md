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
| `previous-profile`, `verification` | Previous candidate and independent blockers. | Correction |

## Task

Produce a comparison profile whose every value is warranted by accepted records.
Read every supplied read-first file before any other step. The coordinator's
invocation supplies output, boundary, runtime, memory, epistemic, reconciliation,
frozen source, profile type and record/source contracts as absolute paths.

Write a revision-2 profile under the supplied profile type, with its exact
metadata and Comparison rationale section. Use `version: 2`, scoped units and
single-value findings, not revision-1 value lists or evidence maps. Choose each
axis's natural unit from the supplied type, grouping only shared scope and
coverage; keep distinct evidence bases on distinct findings. Resolve supersessions through the reconciliation before
classifying; the reports already carry their corrections. Apply the supplied definitions without extra conditions. In
particular, decay means forgetting or downweighting; it does not require a
clock, time-based policy or a named decay command.

Read the supplied set to establish scope, parts, consumers and supported routes.
Do not declare records, add quotes or evidence, edit members, reopen record
verification. Every asserted value cites
records already in the set. Where a needed fact is absent from those records,
use a warranted partial, uninspected or not-determinable assessment and name
the missing fact and prevented conclusion in the unit note, with accepted
record IDs and any cited source path already recorded. Keep unresolved included
units in the inventory. Axis `known` requires accepted coverage evidence and
all units resolved; a positive witness does not establish complete inventory.
Preserve supported positives and route-specific evidence strength.

Source reading is optional and bounded to a named ambiguity in a cited record.
Read its cited paths at the frozen revision under the supplied source rules.
Do not prospect new roots. Log each source read in Comparison rationale with path, bounded lines and
ambiguity resolved. Source understanding cannot replace a missing supporting
record. Do not read an incumbent or reference profile.

Before submission, check all ten axes, natural unit scopes, finding-specific
bases, canonical supporting IDs, inventory coverage and explicit missing facts.
Preserve local bounded trace-learning negatives without making a partial axis
system-wide negative; positive `"yes"` dominates `"no"` only in derived unions.
Do not author an additional aggregate value/evidence copy. The coordinator
checks structure and set references; the independent verifier judges support.
After blockers, read previous-profile and verification and correct only the
profile. There is one correction round. Persistent blockers stop publication.

Run the acceptance check before submitting.
