---
description: Decision that kb/reports is a collection whose cache, state, and retained areas make report retention policy explicit without conflating generated output with disposable output
type: ../types/adr.md
tags: []
status: accepted
---

# 007-Reports collection separates output retention policies

**Status:** accepted
**Date:** 2026-03-24
**Amended:** 2026-08-29 — collection boundary and retention-policy areas

## Context

The original decision created `kb/reports/` for generated, regenerable
analytical snapshots. That solved a real routing problem: promotion candidates,
orphan listings, coverage views, and similar outputs are neither durable claims
nor workshop state. Their value is replaced by a fresh computation.

The directory name then became a stronger routing cue than the decision's
regenerability test. Long-lived experiments and exact evaluation records were
placed beside replaceable snapshots because they were called reports. At the
same time, ignored review evidence and full-pass packets acquired load-bearing
judgments or dispositions that could not safely be regenerated. One directory
therefore mixed three incompatible deletion policies while its broad
"generated reports" identity biased new output toward the wrong one.

The directory also carried `kb/reports/types/` without a `COLLECTION.md`.
Commonplace permits local types only under their owning collection, so reports
used collection-local structure without the collection boundary and text
contract that make that ownership valid.

## Decision

`kb/reports/` is a top-level collection for analytical outputs, evaluation
records, and local operational evidence consumed as reports. Its
`COLLECTION.md` is the text contract for the entire subtree, and
`kb/reports/types/` owns report-specific type contracts.

Every report payload lives under one retention-policy area:

| Area | Policy |
|---|---|
| `kb/reports/cache/` | Replaceable output. Its authoritative inputs and producer exist elsewhere; deleting it loses no unique evidence, decision, or unresolved state. Payloads are ignored. |
| `kb/reports/state/` | Machine-local operational evidence or state. Payloads are ignored, but the producing workflow owns cleanup because an artifact may be non-reproducible or authoritative for a live disposition. |
| `kb/reports/retained/` | Durable report records kept with the project. These outputs are tracked and remain usable from a clean checkout. |
| `kb/reports/types/` | Collection-local structural contracts; not report payloads. |

Report payloads do not live directly at the collection root. A policy change is
represented by moving the artifact. In particular, making one cache report
durable means moving it to `retained/`, not adding an exception to an ignore
rule.

The word *report* does not select this collection. A generated synthesis that
contributes a transferable claim still belongs in `kb/notes/`; a shipped-system
premise or decision belongs in `kb/reference/`; a procedure belongs in
`kb/instructions/`; and draft reasoning or run traces consumed by unfinished
work belong in `kb/work/`. Reports holds outputs whose exact result is the
consumed artifact after those routing tests.

The collection remains outside the published site and generated directory
indexes. Package-owned validation markers exclude `cache/` and `state/` from a
collection sweep because their payloads use producer-owned validation and may
be absent in a clean checkout. The markers do not hide those files from general
discovery, and explicit validation of a typed report still applies its type.

Operativity runs through three paths. Report producers write to their declared
policy paths; `kb/reports/COLLECTION.md` binds authors and reviewers choosing a
home or changing retention; and the project scaffold creates the collection,
policy directories, ignore rules, validation markers, landing, and local
types. Directory placement carries the retention contract even when Git is
absent; Git implements ignored versus project-kept storage in checkouts that
use it.

## Considered alternatives

**Create a top-level `kb/cache/`.** This gives replaceable output a strong name,
but report producers share local types and neighboring operational policies.
It would either make cache another collection solely to own those types or move
the contracts away from the artifacts they shape. Keeping policy areas under
one reports collection preserves one type and text-contract boundary.

**Keep reports as an uncontracted support directory and move its types to
`kb/types/`.** The types are report-specific rather than framework-global, and
the directory still needs a binding rule for distinguishing replaceable output
from retained evidence and state. Globalizing the types would remove the visible
inconsistency without fixing the routing error that exposed it.

**Treat every ignored or generated report as cache.** Rejected because
generation says how an artifact was produced, not whether its evidence or state
can be reconstructed. Review judgment bodies and full-pass dispositions are
the counterexamples: they can be ignored and generated while still being
load-bearing.

**Put only replaceable snapshots under reports and move durable records to a
new library collection.** Rejected because exact experiment and evaluation
records are not automatically claims, system descriptions, or decisions. A
new collection would duplicate the same report-local types and require another
boundary for ignored operational state. Retention policy is the changing axis;
first-level areas expose it directly.

**Leave durable reports at the collection root.** Rejected because an
unqualified root preserves the original ambiguity. A writer would still infer
policy from the artifact name or neighboring files instead of selecting it
explicitly.

## Consequences

Replaceable snapshots now have a deletion-safe home without making every
generated output disposable. Ignored operational state advertises that it is
local yet load-bearing, and durable reports such as the planning-delegation
corpus are visibly project-kept. Local report types now have a valid owner and
compose with one complete collection contract.

The extra path segment changes producer defaults, stored report paths, links,
tests, and operator commands. A path alone cannot prove that a cache entry is
actually reconstructable or that state cleanup is safe; producer instructions
must keep those claims true. General discovery still sees visible Markdown
under `cache/` and `state/` because validation markers are not visibility
controls under [ADR 039](./039-tool-visibility-is-package-owned-and-git-is-never-invoked.md).

This decision stops at outputs consumed as reports. It does not classify local
source snapshots, build caches, workshop-generated fixtures, or execution
traces whose owning subsystem already supplies a stronger lifecycle. It also
does not make `retained/` a second library: durable conclusions are still
extracted to the collection whose consumer and force require them.

---

Relevant Notes:

- [Storage](../storage-architecture.md) — implemented-by: distinguishes reconstructable views, retained judgment evidence, stateful packets, and canonical database state
- [Content routing](../content-routing.md) — rests-on: routes by regeneration source and consumer rather than output name
- [ADR 039](./039-tool-visibility-is-package-owned-and-git-is-never-invoked.md) — rests-on: validation markers do not make ignored report payloads invisible
- [ADR 051](./051-full-pass-packets-own-guarded-captures-and-resolutions.md) — example: generated local packets whose actionable state prevents cache treatment
