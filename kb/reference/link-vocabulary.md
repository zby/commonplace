---
description: "Commonplace's linking approach: collection-owned outbound rules, reader-need labels, articulation tests, connect reports, and the shared label catalogue for COLLECTION.md authors"
type: kb/types/note.md
status: current
---

# Link vocabulary and linking approach

## Approach

Commonplace treats links as authored reader aids, not automatic graph decoration. A link should tell a future reader why following it might help from the source artifact they are already reading.

The source collection owns that decision. Each `COLLECTION.md` defines which destination collections writers may link to, when an agent should search those destinations, and which labels are authorised for each source-to-destination pairing. The shared catalogue on this page is a palette; the collection's own rules are authoritative.

Labels name reader needs rather than ontology edges. A `grounds` link says "follow this if you need to verify the premise." An `implements` link says "follow this if you need the concrete realization." The label is useful only when the source, target, and reason form an articulated relationship.

The articulation test applies to every outbound link:

> `[source] connects to [target] because [specific reason].`

The [connect skill](../instructions/cp-skill-connect/SKILL.md) operationalizes this model without silently rewriting notes. It reads the source collection's `COLLECTION.md`, searches authorised destinations according to their search guidance, applies the articulation test, and writes a report of candidate links. A maintainer or later editing pass decides which candidates become authored links.

## Relationship to the control plane

`AGENTS.md` handles always-loaded routing: purpose, domain, scope boundaries, key indexes, commands, and durable operating conventions. See [control-plane goals](./control-plane-goals.md).

`COLLECTION.md` handles collection-local authoring: how artifacts in that collection should be written and how they may link outward.

This page sits below both. It explains the shared linking approach and label vocabulary, but it is not the control plane and not the authoritative vocabulary for any specific collection.

## Authoring collection link rules

Collection authors use this page when defining or revising outbound-linking rules. Note writers normally read only their collection's `COLLECTION.md`.

The architecture is deliberately loose because the link theory is still developing. Invent intra-collection labels your work needs, propose additions to the catalogue, and diverge from suggestions where it makes sense.

("Register" means one of three content modes — theoretical, descriptive, prescriptive — that determines a collection's quality goal, title conventions, and linking rules. See [`register`](../notes/definitions/register.md).)

Organise the outbound-linking section **per destination collection**, not per register. For each collection your source links to, declare:

1. **Search guidance** — when the [connect skill](../instructions/cp-skill-connect/SKILL.md) (or an author manually prospecting for links) should search this destination from the source. Concrete triggers work best: *"search when the source asserts a claim without evidence,"* not *"search when relevant."*
2. **Authorised labels** — the labels writers in the source collection may use for links to this destination. Give each a one-line reader-need context specific to this *source → destination* pairing.

If a destination isn't listed, it isn't an active link target from this collection. Adding a destination is a collection-author decision; writers cannot unilaterally link to collections outside the authorised set.

**Search latitude.** Search guidance should be specific enough to keep results within the agent's effective context, but open enough to surface serendipitous finds. Over-narrow triggers miss adjacent connections the agent might usefully make; over-broad triggers drown the connect skill in noise. When the destination is small or the query sparse, prefer slight over-retrieval — the agent can filter results in context, whereas missed links are harder to recover. Avoid phrasing that rules out whole classes of plausible connection (e.g., "only when X").

Per-destination rules enable fine-grained experimentation. `kb/notes/ -> kb/reference/` can diverge from `kb/notes/ -> kb/agent-memory-systems/`, even though both destinations share a register.

## Label catalogue

Labels cluster by register-of-origin: the kind of content they emerged to describe. Each `COLLECTION.md` selects whichever labels fit each destination. The register grouping is advisory.

### Theoretical-shaped labels

Inference relations. Commonly used for outbound links to theoretical destinations; some connect theoretical ↔ descriptive or prescriptive.

| label | kind | reader-need |
|---|---|---|
| `extends` | asymmetric | wants to see the argument developed further |
| `grounds` | asymmetric | wants to verify the premise / check the basis |
| `enables` | asymmetric | wants to check the operational prerequisite |
| `exemplifies` | asymmetric (instance → general) | wants the general claim this instance falls under |
| `mechanism` | asymmetric | wants to understand how the claim operates |
| `contradicts` | symmetric | wants to resolve a disagreement |
| `contrasts` | symmetric | wants to see the neighbouring-shape distinction |
| `rationale` | asymmetric (descriptive/prescriptive → theoretical) | wants the claim this design/rule rests on |
| `evidence` | asymmetric (theoretical → descriptive) | wants corroborating observation |
| `derived-from` | asymmetric (theoretical → descriptive) | wants abstraction provenance |

### Descriptive-shaped labels

Structural relations. Commonly used for outbound links to descriptive destinations.

| label | reader-need |
|---|---|
| `part-of` / `contains` | wants to situate this in the larger system |
| `implements` / `implemented-by` | wants the concrete realization or the abstract contract |
| `supersedes` / `superseded-by` | wants the current or prior version |
| `compares-with` | wants parallel design-axis analysis with another system (currently specific to `kb/agent-memory-systems/`) |
| `procedure` | (descriptive → prescriptive) wants the how-to to act on this |

### Prescriptive-shaped labels

Operational relations. Commonly used for outbound links to prescriptive destinations.

| label | reader-need |
|---|---|
| `composition` | wants the next step in a chain |
| `precondition` | needs to confirm something is true/done before proceeding |
| `invokes` | needs to execute a subroutine |
| `applies-when` | branch condition tells them to go elsewhere |
| `operates-on` | (prescriptive → descriptive) wants to know what system the procedure acts on |

### Universal / weak

Usable from any source to any destination.

| label | reader-need |
|---|---|
| `defined-in` | reader doesn't know the term; target is under `kb/notes/definitions/` |
| `see-also` | reader might benefit but author can't name a specific need; escape hatch — use only after ruling out a more specific label |

## Distillation tracking (`Distilled into:`)

When an artifact is distilled from one or more source notes — a skill from methodology notes, a `COLLECTION.md` rule from a design note, a reference doc from a workshop conclusion — the dependency is recorded at the **source**, in a dedicated footer section below `Relevant Notes:`:

```markdown
Distilled into:

- [cp-skill-write SKILL.md](../instructions/cp-skill-write/SKILL.md) — the duplicate-check rule
```

The distilled artifact itself carries no backlinks to its sources: its reader is an executor, and provenance links dilute focus and add indirection cost. The forward pointer sits where change happens — editing a source note surfaces "these downstream artifacts may now be stale" with zero hops. The reverse query ("what informed this artifact?") is rare and runs as a search: `rg "<artifact-name>" kb/notes/`.

Rationale: [distilled artifacts need source tracking at the source](../notes/distilled-artifacts-need-source-tracking-at-the-source.md).

## Limits

The catalogue is guidance, not a closed enum. Add to it, adapt it, or ignore it where a collection has a better local vocabulary. Labels still need shared recognition to carry stable meaning across collections.

Do not use this page as a fallback for lazy labelling. If the source `COLLECTION.md` authorises specific labels for a destination, use those rather than downgrading to `see-also`.

## Open questions

- When should a collection-specific label (`compares-with`) get promoted to the catalogue at large? Current: document it here once it's in use, flagged "currently specific to X."
- Is register-of-origin the right catalogue grouping, or would alphabetical be cleaner? Register-of-origin helps authors find labels that match their source's shape; alphabetical is flatter but less suggestive.
- How should the connect skill treat authorized-but-rarely-used destinations? Speculative — probably depends on use-frequency signal.
- Should `supersedes` be restricted to intra-descriptive use? Most use is ADR chains inside `kb/reference/`; cross-collection supersession is rare.

---

Relevant Notes:

- [ADR 019 — collection-owned link vocabulary](./adr/019-collection-owned-link-vocabulary.md) — rationale: the architecture this catalogue serves
- [ADR 009 — link relationship semantics](./adr/009-link-relationship-semantics.md) — rationale: the original theoretical vocabulary whose core labels seed this catalogue
- [ADR 020 — theoretical-default additions (contrasts, mechanism)](./adr/020-theoretical-default-contrasts-mechanism.md) — rationale: the audit outcomes adding `mechanism` and `contrasts` and stating directional asymmetry
- [Links encode conditional possibilities, not obligations](../notes/links-encode-conditional-possibilities-not-obligations.md) — rationale: the reader-need theory behind the label test
- [Register](../notes/definitions/register.md) — defined-in: content-mode groupings used to organise the catalogue
