# Pre-migration link-authorization matrix

**Status:** historical baseline. [ADR 058](../../reference/adr/058-directional-identifiers-use-source-as-subject.md) and the evidence-label migration supersede this file's `evidence` authorizations and first decision packet. Current contracts use `evidenced-by` and `is-evidence-for`; this inventory remains unchanged below so the migration can be audited against the state it actually found.

## Purpose and method

This is an inventory of what every live `COLLECTION.md` currently says authors may link, before deciding what the rules should become. It records authorization, not corpus usage: a later migration pass may need to count actual authored edges once target semantics are settled.

The matrix treats every Markdown link as an authored edge from the artifact containing the link (**source**) to the linked artifact (**target**). That representation convention does not settle whether a label's underlying relation is directional, self-dual, or one half of an inverse pair.

Finding markers:

- **aligned** — the source→target use matches the shared catalogue closely enough to act on;
- **scope drift** — the direction is coherent, but the live collections use the label outside the catalogue's stated register or collection scope;
- **direction conflict** — the same asymmetric label names opposed source→target journeys;
- **grammar gap** — links are required or permitted without an executable authorization grammar;
- **lineage** — recorded here for completeness but routed to [the lineage contradiction ledger](../lineage-mechanisms/current-contradictions.md).

## Contract-shape inventory

| source collection | current shape | executable by write/connect? | finding |
|---|---|---:|---|
| `kb/agent-memory-systems/` | one block per destination | yes | Closest implementation of ADR 019's prescribed form. |
| `kb/agentic-systems/` | one block per destination | yes | Closest implementation of ADR 019's prescribed form. |
| `kb/articles/` | prose allows in-body KB links; labels and footer tables forbidden | partial | **Grammar gap:** no authorized destinations, label policy, or formally declared specialized override. |
| `kb/instructions/` | scan/exclusion paragraph plus one labels table | yes under current skill | Semantically organized by destination column, but not in ADR 019's required block serialization. |
| `kb/notes/` | scan/exclusion paragraph plus one labels table | yes under current skill | Semantically organized by destination column, but not in ADR 019's required block serialization. |
| `kb/reference/` | scan/exclusion paragraph plus one labels table | yes under current skill | Semantically organized by destination column, but not in ADR 019's required block serialization. |
| `kb/sources/` | artifact-class split, scan/exclusion paragraph, one labels table | yes for ingests/reviews | Snapshot exception is clear; active-surface table has direction and `any` ambiguities. |
| `kb/work/` | permissive prose plus explicitly non-authoritative suggestions | yes by judgment | Intentional workshop exception rather than a stable library grammar. |
| `kb/work/dialectical-sample/` | mandatory source-span citations, no outbound section | no | **Grammar gap:** a local collection contract requires links but supplies no destinations or relation policy. |

The working write skill already accepts all three common serializations—per-destination blocks, one table with a destination column, or prose. The contradiction is therefore between ADR/catalogue wording and the executable procedure, not an inability of the procedure to read the main contracts.

## Authorization matrix

### `kb/agent-memory-systems/`

| target | authorized labels | source→target reader journey | finding |
|---|---|---|---|
| agent-memory-systems | `part-of` / `contains`; `implements` / `implemented-by`; `compares-with`; `see-also` | structural placement, realization, peer comparison, adjacency | Inverse pairs are explicit. `compares-with` behaves as a peer relation but the catalogue does not declare its directional kind. |
| sources | `derived-from`; `evidence`; `see-also` | review → source snapshot used to produce or support it | `evidence` has the coherent claim/description→corroboration shape, but exceeds the catalogue's “theoretical → descriptive” scope. `derived-from` is **lineage**. |
| notes | `rationale`; `evidence` (rare); `defined-in`; `see-also` | review → theory it rests on, allegedly evidences, or needs defined | `rationale` and `defined-in` align. Review→claim `evidence` opposes the catalogue's claim→observation direction. |
| reference | `see-also` | review → Commonplace analogue | aligned weak navigation. |
| agentic-systems | `part-of` / `contains`; `compares-with`; `see-also` | subsystem review → whole system or peer context | Structural inverse pair is explicit; `compares-with` scope has expanded beyond its catalogue description. |
| instructions | `see-also` | review → Commonplace workflow counterpart | aligned weak navigation. |

### `kb/agentic-systems/`

| target | authorized labels | source→target reader journey | finding |
|---|---|---|---|
| sources | `derived-from`; `evidence`; `see-also` | system analysis → source snapshot grounding it | `evidence` has the description→corroboration shape but broader register scope than the catalogue. `derived-from` is **lineage**. |
| notes | `rationale`; `see-also` | system analysis → transferable theory it rests on | aligned. |
| agent-memory-systems | `part-of` / `contains`; `compares-with`; `see-also` | whole system → reviewed subsystem or comparison context | Direction is explained for the structural pair. `compares-with` scope has expanded. |
| reference | `see-also` | external system → Commonplace analogue | aligned weak navigation. |
| instructions | `procedure`; `see-also` | external system analysis → corresponding Commonplace workflow | `procedure` aligns with descriptive→prescriptive. |

### `kb/articles/`

| target | authorized labels | source→target reader journey | finding |
|---|---|---|---|
| unspecified paths under `kb/` | none; in-prose links only | article → deeper KB material | **Grammar gap:** deliberate navigation exists without declared destinations or relation types. This conflicts with ADR 009's unqualified “every link” rule unless the article profile becomes a formal override. Article `source_notes` is **lineage**, not part of this navigation matrix. |

### `kb/instructions/`

| target | authorized labels | source→target reader journey | finding |
|---|---|---|---|
| instructions | `composition`; `precondition`; `invokes`; `applies-when`; `see-also` | next step, prerequisite, subroutine, conditional branch, exceptional fallback | aligned prescriptive relations. |
| reference | `operates-on` | procedure → system component it changes | aligned prescriptive→descriptive. |
| notes | `rationale` | procedure → theory needed by maintainers | aligned prescriptive→theoretical. |
| agent-memory-systems; agentic-systems; work | none; explicitly excluded | no authored journey | exclusion is clear. |

### `kb/notes/`

| target | authorized labels | source→target reader journey | finding |
|---|---|---|---|
| notes | `extends`; `grounds`; `enables`; `exemplifies`; `mechanism`; `contradicts`; `contrasts` | inference, prerequisite, instance/general, mechanism, disagreement, peer distinction | aligned theoretical defaults; `contradicts` and `contrasts` are explicitly self-dual. |
| notes/definitions | `defined-in` | claim → definition needed to read it | aligned. |
| reference; agent-memory-systems; agentic-systems; sources | `evidence`; `derived-from`; `abstracted-from`; `see-also` | claim → observation/source or adjacent descriptive material | `evidence` matches claim→corroboration. The two `*-from` labels are **lineage**. |
| instructions | `operationalized-from`; `see-also` | methodology note → procedure that operationalizes it, or adjacent procedure | `operationalized-from` is **lineage** and its surface direction requires normalization; `see-also` is ordinary navigation. |
| work | none; explicitly excluded | no authored journey | exclusion is clear. |

### `kb/reference/`

| target | authorized labels | source→target reader journey | finding |
|---|---|---|---|
| reference | `part-of` / `contains`; `implements` / `implemented-by`; `supersedes` / `superseded-by` | structural placement, realization, version chain | aligned inverse pairs. |
| notes | `rationale` | shipped design → theory it rests on | aligned. |
| notes/definitions | `defined-in` | reference → needed definition | aligned. |
| sources; agent-memory-systems; agentic-systems | `derived-from`; `abstracted-from`; `evidence` | Commonplace design/description → external source or system | `evidence` has description→corroboration shape but wider scope than the catalogue. The `*-from` labels are **lineage**. |
| instructions | `procedure` | reference → how-to for acting on the system | aligned. |
| `any` | `see-also` | reference → adjacent companion | **Internal ambiguity:** the same contract says not to link into `kb/work/`, so `any` cannot literally mean any destination. |

### `kb/sources/`

Snapshots author no new links. The rows below apply only to ingest reports and source reviews.

| target | authorized labels | source→target reader journey | finding |
|---|---|---|---|
| notes | `evidence`; `abstracted-from`; `rationale` | source analysis → claim it corroborates, claim allegedly abstracted from it, or theory it rests on | `rationale` aligns. `evidence` reverses the catalogue and notes-collection journey. `abstracted-from` is a **lineage direction conflict** routed to the lineage ledger. |
| notes/definitions | `defined-in` | source analysis → needed definition | aligned. |
| sources; agent-memory-systems; agentic-systems | `compares-with` | source analysis → parallel source/system | Live scope contradicts the catalogue's “currently specific to agent-memory-systems” wording. The relation behaves as peer comparison but is not declared self-dual. |
| `any` | `see-also` | source analysis → adjacent companion | **Internal ambiguity:** the same contract excludes `kb/work/` and `kb/instructions/`, so `any` is not literal. |

### `kb/work/`

| target | suggested labels | source→target reader journey | finding |
|---|---|---|---|
| notes | `extends`; `grounds`; `mechanism`; `contradicts`; `contrasts`; `rationale`; `defined-in` | workshop → scaffolding theory or vocabulary | Suggestions are intentionally non-authoritative; stable semantics come from eventual promotion rather than workshop enforcement. |
| reference; agent-memory-systems; agentic-systems; sources | `evidence`; `abstracted-from` | workshop → corroborating or shaping descriptive/source material | `evidence` wording (“this artifact corroborates”) is directionally ambiguous; `abstracted-from` is **lineage**. |
| any | `draws-on`; `tests`; `depends-on`; `produces`; `supersedes`; `see-also` | local work-state relation | Intentional workshop-local vocabulary, outside the stable library catalogue. |

### `kb/work/dialectical-sample/`

| target | authorized labels | source→target reader journey | finding |
|---|---|---|---|
| local `sources/` excerpts | none | proposition → attributed source span | **Grammar gap:** citations are mandatory and semantically rich, but the collection gives neither link labels nor an explicit citation-as-specialized-override rule. |

## Cross-contract findings

### `evidence` currently names two opposed journeys

The dominant use is **claim or description → corroborating observation**:

- notes → reference, systems, or sources;
- reference → external systems or sources;
- external-system analysis → source snapshot.

The minority inverse use is **source or descriptive review → claim corroborated**:

- source ingest/review → note;
- agent-memory review → note (rare).

These are both useful reader journeys, but one asymmetric identifier cannot name both without losing direction. This is the best first decision case because it requires no lineage carrier decision.

### `compares-with` has stable use but unstable declaration

It is used for peer comparisons among memory systems, between memory and whole agentic systems, and from source analyses to sources or systems. The catalogue still calls it specific to agent-memory systems and does not say whether it is self-dual. Its live use suggests a general descriptive/source peer-comparison label whose semantics are self-dual even though each authored direction remains an independent reader aid.

### `any` weakens collection ownership

`see-also | any` appears in reference and source tables while prose in the same contracts excludes `kb/work/` or `kb/instructions/`. If collection-owned authorization is load-bearing, destination cells must name the permitted set or define `any` as “any otherwise permitted destination,” not silently override exclusions.

### Specialized citations and editorial links need an override shape

Articles and the dialectical sample demonstrate legitimate links whose primary contract is not a footer relationship label: editorial invitations and attributed source-span citations. Treating them as accidental omissions would flatten real text-contract differences; treating them as implicit exceptions leaves generic skills unable to act. The architecture needs a declared override form, not necessarily one universal label table.

## Historical first decision packet: `evidence`

The pre-migration candidate rule was:

> `evidence` is asymmetric and authored from a claim or descriptive assertion to the observation, system analysis, or source that corroborates it.

That rule matches the majority of collection authorizations and the reader need “I am evaluating this assertion; show me corroboration.” Under it, source/review → claim links need a different label or ordinary prose. Candidate inverse names should be tested against reader need rather than ontology—possibly `supports`, `corroborates`, or no formal footer edge if the ingest prose already names where the source lands.

The corpus review in [evidence direction review](./evidence-direction-review.md) found 26 inverse uses across ingest reports, a source review, and an agent-memory review; 19 had no return link. [ADR 058](../../reference/adr/058-directional-identifiers-use-source-as-subject.md) subsequently retained both journeys as `evidenced-by` and `is-evidence-for` under the source-as-subject invariant.
