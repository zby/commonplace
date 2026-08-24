---
description: "A seven-artifact Commonplace sweep found that direct source access removed exact-fact prose while discovery maps and cross-component boundaries survived; it does not establish a universal documentation ratio"
type: kb/types/note.md
traits: [title-as-claim]
tags: [artifact-analysis, kb-maintenance]
---

# Seven documentation cases left routing and synthesis

A 2026-08-24 disposition sweep tested seven Commonplace reference artifacts
after agents gained a reliable path to the exact installed source. Two
artifacts were retired and five were reduced. What survived answered one of two
questions: where to look before the reader knows an implementation name, or
how several implementation units relate. Exact fields, arguments, schemas,
module inventories, and local behavior moved to live source, command help, or
an already stronger contract.

This is a bounded Commonplace casebook. It supports a default for
source-readable software KBs, not a claim that software documentation in
general is redundant.

## Casebook

| Artifact | Exact recovery result | Retained value | Disposition |
|---|---|---|---|
| `lib-modules.md` | Task-vocabulary search reached all 15 modules; the prose map named 9 | Two unique change-loop facts moved beside the code they constrain | retire |
| `commands.md` | `--help` and source answered invocation and behavior after two help paths were repaired | A checked 22-name catalogue discovers commands before the reader knows their names | reduce and keep checked |
| `freshness-schemas.md` | Serializers and parsers owned every exact field and exposed two prose discrepancies | One cross-command acknowledgement invariant moved to freshness architecture | retire |
| `review-architecture.md` | Source search outperformed an incomplete module and schema map | Execution ownership, canonical-state, finalization, and freshness boundaries | reduce |
| `storage-architecture.md` | Live schema exposed a table omitted from the prose inventory | Authority and lifecycle across files, views, evidence, packets, and SQLite | reduce |
| `architecture.md` | The scaffold manifest and init source owned exact topology and behavior | Approximate topology, ownership, runtime, projection, and path-invariance boundaries | reduce |
| `freshness-architecture.md` | Store, schema, source, and help exposed four inventory omissions | Target identity, discovery ownership, transition semantics, and the complete concurrency guard | reduce |

For the six cases with recorded byte counts, the candidate pages fell from
63,396 to 29,867 bytes, a 53 percent reduction. The retired module reference is
additional to that total because its original byte count was not recorded in
the worked case. Byte reduction was not the decision rule: storage and
freshness gained or clarified cross-component distinctions even while exact
inventories disappeared.

## What the cases establish

Direct access to the executing implementation removed the accessibility reason
for paraphrasing exact behavior. A known command routed to `--help`; a known
task term routed through `commonplace-source` and source search; exact schema
and serialization questions selected small executable units. In those cases a
prose answer was additive because an exact consumer still had to inspect the
implementation.

Recoverability attached to content units rather than whole documents. Four
architecture pages survived after their module, schema, command, or option
catalogues were removed. Their retained claims composed ownership, authority,
transition, or concurrency relations across several source units. Conversely,
the two retired pages each had a small semantic residue, but that residue had a
stronger home in code or architecture rather than justifying the original
file.

Routing value also survived when live lookup required a name the reader did
not yet possess. Command-local help cannot reveal an unknown command, so the
complete command-name catalogue remained and exact set parity stayed tested.
The installed topology remained as approximate orientation, but explicitly
stopped claiming manifest exactness. The cases therefore separate discovery
from exact description instead of treating both as “documentation.”

The audit found an incompleteness, incorrect claim, or broken live-read
prerequisite in every case. Examples included partial module maps, a missing
store table and revision module, an obsolete store version, omitted CLI help,
an incorrect byte-identity claim, and an installed-tree claim that confused a
template with its practitioner-created control plane. This does not show the
pages were broadly neglected: the pre-sweep baseline found only 0–3 commits of
lag. It shows that co-maintained exact prose creates a separate obligation even
when maintainers usually pay it.

## What the cases do not establish

The sweep did not measure reader frequency, task success, or long-term
maintenance time. Its discovery decisions used representative lookup tests,
not production telemetry. It covered one Python CLI repository whose agents
can inspect the exact installed package; a public API, external compliance
contract, source-inaccessible product, human tutorial, or differently routed
system may justify another content layer.

No stable percentage of a document is recoverable. Rationale, rejected
alternatives, intent, and commitment boundaries were outside the sweep because
running code cannot in general reproduce them. Even within the selected pages,
new irrecoverable content can accrete after this dated disposition.

The cases also do not show that every recoverable copy should be deleted. A
checked copy can pay when it removes repeated reconstruction, and a
judgment-dependent synthesis can pay when it closes a recurring question.
The result is a default read path plus a burden of demonstrated value, not an
omit-only rule.

## Commonplace consequence

Commonplace's [reference collection contract](../../reference/COLLECTION.md)
now sends exact implementation questions to the live package and lets authored
reference prose justify itself through orientation, architecture boundaries,
cross-component invariants, rationale, or demonstrated routing. Its economy
tests ask whether another artifact already owns the content and whether the
reader would still need source for the same answer.

That rule is narrower than “documentation is a cache over source.” The sweep
found checked routing caches, unique synthesis, and local warnings as different
retention forms. It also found that source access is a prerequisite for this
default: `commonplace-source` and side-effect-free command help had to work
before exact prose could be removed safely.

---

Relevant Notes:

- [Attempted recovery identifies informational gaps, not provenance or authority](../documentation-generates-the-system-rather-than-describing-it.md) — grounds: supplies the per-unit recovery assay and prevents successful reconstruction from deciding authority or history
- [A derived copy of recomputable truth must be checked or absent](../a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: supplies the safety boundary for exact copies whose source remains authoritative
- [Opposed recompute factors do not decide documentation segmentation](../opposed-recompute-factors-do-not-decide-documentation-segmentation.md) — grounds: explains why source readability alone does not decide whether a useful cache pays
- [Addressability grain sets a matched selective-read floor](../addressability-grain-sets-a-matched-selective-read-floor.md) — grounds: supplies the source-unit versus document-unit comparison used in the retrieval experiments
- [An insufficient summary precedes the source rather than replacing it](../an-insufficient-summary-precedes-the-source-rather-than-replacing.md) — exemplifies: exactness prose that did not license stopping left live implementation in the path and added its own read cost
- [A linked note's durable payload is what its consumption path cannot reliably supply](../linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) — exemplifies: the seven cases retained unknown-name routing and cross-component relations after a guaranteed live-source path supplied exact facts
