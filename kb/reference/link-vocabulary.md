---
description: "Commonplace's linking approach: collection-owned outbound rules, reader-need labels, articulation tests, connect reports, and the shared label catalogue for COLLECTION.md authors"
type: kb/types/note.md
---

# Link vocabulary and linking approach

## Approach

Commonplace treats links as authored reader aids, not automatic graph decoration. A link should tell a future reader why following it might help from the source artifact they are already reading.

The source collection owns that decision. Each `COLLECTION.md` defines which destination collections writers may link to, when an agent should search those destinations, and which labels are authorised for each source-to-destination pairing. The shared catalogue on this page is a palette; the collection's own rules are authoritative.

Labels name reader needs rather than ontology edges. A `grounds` link says "follow this if you need to verify the premise." An `implements` link says "follow this if you need the concrete realization." The label is useful only when the source, target, and reason form an articulated relationship.

The articulation test applies to every outbound link:

> `[source] connects to [target] because [specific reason].`

Markdown's title attribute (`[text](url "grounds")`) could technically carry a label inline, but it doesn't solve the actual problem. The label alone isn't the payload — the articulation test requires label *plus* a specific reason, and a reason clause doesn't fit an attribute. And mechanizing the label wouldn't resolve the harder call every author already faces regardless of syntax: whether a relationship is significant enough to name as a formal edge at all, not just what to call it once named.

The [connect skill](../instructions/cp-skill-connect/SKILL.md) operationalizes this model without silently rewriting notes. It reads the source collection's `COLLECTION.md`, searches authorised destinations according to their search guidance, applies the articulation test, and writes a report of candidate links. A maintainer or later editing pass decides which candidates become authored links.

## Relationship to the control plane

`AGENTS.md` handles always-loaded routing: purpose, domain, scope boundaries, key indexes, commands, and durable operating conventions. See [control-plane goals](./control-plane-goals.md).

`COLLECTION.md` handles collection-local authoring: how artifacts in that collection should be written and how they may link outward.

This page sits below both. It explains the shared linking approach and label vocabulary, but it is not the control plane and not the authoritative vocabulary for any specific collection.

## Authoring collection link rules

Collection authors use this page when defining or revising outbound-linking rules. Note writers normally read only their collection's `COLLECTION.md`.

The architecture is deliberately loose because the link theory is still developing. Invent intra-collection labels your work needs, propose additions to the catalogue, and diverge from suggestions where it makes sense.

("Register" means one of three content modes — theoretical, descriptive, prescriptive — that determines a collection's quality goal, title conventions, and linking rules. See [`register`](../notes/definitions/text-contract.md).)

Organise the outbound-linking section **per destination collection**, not per register. For each collection your source links to, declare:

1. **Search guidance** — when the [connect skill](../instructions/cp-skill-connect/SKILL.md) (or an author manually prospecting for links) should search this destination from the source. Concrete triggers work best: *"search when the source asserts a claim without evidence,"* not *"search when relevant."*
2. **Authorised labels** — the labels writers in the source collection may use for links to this destination. Give each a one-line reader-need context specific to this *source → destination* pairing.

If a destination isn't listed, it isn't an active link target from this collection. Adding a destination is a collection-author decision; writers cannot unilaterally link to collections outside the authorised set.

**Footer inclusion is a separate decision from label choice.** Each `COLLECTION.md` also states the collection's inline-vs-footer convention (typically: inline for the strongest, argument-bearing commitment; footer for labelled links — `- [title](path) — label: context phrase`). Authorised labels govern what a footer link may be *called*; they don't decide whether a given relationship earns a footer entry at all. That weight call — is this corroboration formal enough to belong in the note's evidence map, or better left as an inline example in the body — has no validator and is left to the note's author, per the collection's own quality goal. A footer is a curated subset of what a note could link, the same selective-by-default shape as a tag-README's curated head: exhaustiveness is never the assumed default, and if a collection ever wants a footer to be a complete listing of a relation, that has to be an explicit, checked claim, not an implicit one.

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
| `derived-from` | asymmetric | wants the source this was worked out from; asserts no claims beyond it (lineage semantics below) |
| `abstracted-from` | asymmetric (general → evidence) | wants the instances this generalization came from; the claim exceeds them (lineage semantics below) |

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

## Lineage semantics (derived vs abstracted)

Two lineage relations with different maintenance semantics replace the retired `Distilled into:` footer. These labelled edges are the one place the distinction is formally made — prose can describe an artifact's origin loosely, but only a labelled edge asserts which maintenance regime governs it (rationale: [vocabulary collisions are prevented at write time, not resolved at read time](../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md)).

**Derived** — `derived-from` (labelled link) and `Derived into:` (footer section at the source). The edge asserts that the artifact's substantive claims are recoverable from the source plus its declared consumer goal — nothing added. That makes the artifact a recomputable copy with the maintenance regime stated in [theory and methodology form a two-layer execution system](../notes/theory-and-methodology-form-a-two-layer-execution-system.md): checkable by re-deriving and comparing, stale-until-rechecked when the source revises, with checkability graded by the source's coherence.

**Abstracted** — `abstracted-from` and `Abstracted into:`. The edge asserts that the artifact posits claims beyond the source — instances generalized into a rule, observations into a pattern. The source is evidence, not a generator: the artifact's authority is earned by later testing, not inherited from the source, and when the source changes the generalization is re-examined, not recomputed.

The classifying question: could another agent reconstruct the artifact's substantive claims from the source plus stated premises? Yes → derived; no → abstracted. A mixed artifact is labelled by its dominant regime — an explicit, revisable call; the mixed case is real (see the structure note's caveat: part of a methodology is native to its own level of description and belongs to neither pure regime).

Recording direction is unchanged from the retired footer: the dependency is recorded at the **source**, in a dedicated footer section below `Relevant Notes:`:

```markdown
Derived into:

- [cp-skill-write SKILL.md](../instructions/cp-skill-write/SKILL.md) — the duplicate-check rule
```

The downstream artifact carries no backlinks to its sources by default. Its reader is the consumer it was shaped for — not always an executor (a paper, a reference doc), but the executor case is demanding and common enough to set the default: provenance links dilute focus and add indirection cost exactly where the artifact must work unassisted. The forward pointer sits where change happens — editing a source note surfaces "these downstream artifacts may now need attention" with zero hops: for derived artifacts, recheck or re-derive; for abstracted artifacts, re-examine whether the generalization still holds. The reverse query ("what informed this artifact?") is rare and runs as a search: `rg "<artifact-name>" kb/notes/`.

Rationale: [source changes should surface downstream review targets, while reverse lineage can remain searchable](../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md).

**Migration status.** `Distilled into:` is retired — write no new instances. Existing `Distilled into:` footers and pre-existing `derived-from` edges predate this boundary; they are classified into the new labels during the vocabulary-migration passes. Until reclassified, treat them as unclassified lineage — carrying neither regime's semantics.

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
- [Theory and methodology form a two-layer execution system](../notes/theory-and-methodology-form-a-two-layer-execution-system.md) — rationale: the maintenance regime the derived side of the lineage semantics asserts
- [Load-bearing vocabulary collisions should be prevented or visibly scoped at write time](../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) — rationale: why the derived/abstracted boundary is drawn at labelled edges rather than in prose
- [Register](../notes/definitions/text-contract.md) — defined-in: content-mode groupings used to organise the catalogue
