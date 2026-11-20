---
description: "Shared meanings and directions for formal link labels, local permission by destination, and the maintenance consequences of lineage relations"
type: types/note.md
---

# Link vocabulary and linking approach

## Approach

The catalogue defines what a shared formal label asserts. The source collection decides whether its writers may use that label for a given destination. For example, a collection may authorise `derived-from` for links to tracked sources; it cannot use that name for a source that merely inspired the work.

Collection authors follow the [outbound-link rules](../types/collection-contract.md#authoring-outbound-link-rules). They may introduce a local label under an unreserved name. Writers normally consult their collection’s `COLLECTION.md`; an entry in this catalogue is not permission to use a label.

Labels name reader needs rather than ontology edges. A `grounds` link says "follow this if you need to verify the premise." An `implements` link says "follow this if you need the concrete realization." The label is useful only when the source, target, and reason form an articulated relationship.

Every authored direction is a separate reader-aid decision. A link back from the target is welcome when it independently helps readers there; it may use an inverse label such as `contains` / `part-of`, or the same label when the relation is self-dual. Do not add it merely to mirror the first edge. Symmetry means the relation reads the same from either endpoint, not that both endpoints must author it; asymmetry does not prohibit a useful return link with its own reader need.

The articulation test applies to every outbound link:

> `[source] connects to [target] because [specific reason].`

## Label catalogue

Labels cluster by the source shape they emerged to describe. Each `COLLECTION.md` selects whichever labels fit each destination. The grouping is advisory and does not classify collections.

Every directional identifier completes `source <label> target`: the artifact containing the link is the grammatical subject and the linked artifact is the target. A catalogue entry therefore states what the source asserts about the target, not merely what role the target serves. Omitted helper verbs such as “is” are acceptable when they do not reverse the endpoints. Pre-existing identifiers that fail this invariant are explicit migration debt and retain their declared meaning until their own scoped migration; new or changed identifiers must satisfy it ([ADR 058](./adr/058-directional-identifiers-use-source-as-subject.md)).

When adding a name to the catalogue, check live collection contracts and specialised type rules for earlier local uses. If a local use means the same thing, its existing permission can stand. If it means something else, choose another shared name or agree on a migration before reserving it. Registration alone must not change what existing links assert.

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
| `rests-on` | asymmetric (descriptive/prescriptive/system-definition → theoretical) | source design, rule, description, or contract depends on the target claim; reader wants the theory whose change would trigger reconsideration |
| `evidenced-by` | asymmetric (assertion → observation/source) | source assertion is evidenced by target; reader wants the corroborating, qualifying, or boundary observation. The target corroborates only if it reports a test the assertion could have failed; evidence the assertion was generalized from is `abstracted-from` instead |
| `is-evidence-for` | asymmetric (observation/source → assertion) | source bears materially on target assertion; reader wants where this observation lands, without implying target-side uptake |
| `derived-from` | asymmetric | wants the source this was worked out from; asserts no claims beyond it (lineage semantics below) |
| `abstracted-from` | asymmetric (general → evidence) | wants the instances this generalization came from; the claim exceeds them (lineage semantics below) |

### Descriptive-shaped labels

Structural relations. Commonly used for outbound links to descriptive destinations.

| label | reader-need |
|---|---|
| `part-of` / `contains` | wants to situate this in the larger system |
| `implements` / `implemented-by` | wants the concrete realization or the abstract contract |
| `supersedes` / `superseded-by` | wants the current or prior version |
| `decided-by` | (description → ADR) source describes a state the target decision fixed; reader wants the decision and its reasons before changing that state. The ADR records a choice, not an observation, so this is not `evidenced-by` |
| `compares-with` | self-dual; wants a parallel analysis of the target on the named comparison axis |
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

### Lineage-shaped labels

| label | reader-need |
|---|---|
| `adapted-from` | wants the material source worked up into this target for a use the source did not natively serve; no claim-preservation or generalization guarantee |
| `operationalized-from` | wants the methodology or source worked into an executable shape whose ordering, defaults, or stopping conditions are target-added; no substantive claims beyond the source |

### Universal / weak

Not restricted to a particular source or destination shape. Use only where authorised.

| label | reader-need |
|---|---|
| `defined-in` | reader doesn't know the term; target is a definition authorized by the source collection |
| `see-also` | reader might benefit but author can't name a specific need; escape hatch — use only after ruling out a more specific label |

## Lineage semantics

Four lineage relations with different maintenance semantics replace the retired `Distilled into:` footer. These labelled edges are the one place the distinction is formally made — natural-language content can describe an artifact's origin loosely, but only a labelled edge asserts which maintenance regime governs it (rationale: [vocabulary collisions are prevented at write time, not resolved at read time](../theory/vocabulary-collisions-prevented-at-write-time-not-read-time.md)). `operationalized-from` is a narrower authoring-time alternative to `adapted-from` for the same edge, not a child relation to stack with it.

**Adapted** — `adapted-from` and `Adapted into:`. The edge asserts that the target's specific content — its selection, structure, or wording — was substantially worked up from the source's specific content for a use the source did not natively serve. It does not assert completeness, entailment, generalization beyond the source, or mechanical reproducibility.

If the source were removed or materially changed, the target's actual content would need judgmental rewriting, not merely a change to its rationale. A source change therefore flags a fit recheck; it does not authorize automatic recomputation or a fresh-evidence retest.

Record this edge at the source in a dedicated `Adapted into:` footer, using the same forward-pointer and context-phrase convention as the other lineage footers. Do not use it when the source only motivated, corroborated, or inspired an independently authored target; use `rests-on`, `evidenced-by`, `is-evidence-for`, `grounds`, or `see-also` instead.

**Operationalized** — `operationalized-from` and `Operationalized into:`. The edge narrows the adapted test: the target adds ordering, defaults, or stopping conditions the source does not fix, while adding no substantive claims beyond it. It is currently authorized for the `kb/theory/` methodology → `kb/instructions/` procedure pairing; the truth condition is portable, but a new source pairing needs its source collection's authorization before a footer is written.

This is an authoring-time alternative to `adapted-from` for one relationship, never a second edge stacked on the same source and target. Its maintenance consequence is the same as adaptation: a source change flags a judgmental recheck rather than a recomputation. Record it at the source in an `Operationalized into:` footer with a reader-need context phrase.

**Derived** — `derived-from` (labelled link) and `Derived into:` (footer section at the source). The edge asserts that the artifact's substantive claims are recoverable from the source plus its declared consumer goal — nothing added. That makes the artifact a recomputable copy with the maintenance regime stated in [theory and methodology form a two-layer execution system](../theory/theory-and-methodology-form-a-two-layer-execution-system.md): checkable by re-deriving and comparing, stale-until-rechecked when the source revises, with checkability graded by the source's coherence.

**Abstracted** — `abstracted-from` and `Abstracted into:`. The edge asserts that the artifact posits claims beyond the source — instances generalized into a rule, observations into a pattern. The source is evidence, not a generator: the artifact's authority is earned by later testing, not inherited from the source, and when the source changes the generalization is re-examined, not recomputed.

The classifying sequence is:

1. If the target would be unchanged when the source changes because the source only motivated or corroborated it, use a non-lineage label.
2. If the target's substantive claims are reconstructible from the source plus stated premises, use `derived-from` where the source collection authorizes that pairing.
3. If the target generalizes beyond the source, use `abstracted-from`.
4. If the target is an executable shape that adds operational choices without substantive claims, use `operationalized-from` where authorized.
5. Otherwise, if the source materially shaped the target's use-shaped content, use `adapted-from` where authorized (no collection currently authorizes `adapted-from`, though the catalogue defines its semantics for future authorization).

A mixed artifact is labelled by its dominant regime — an explicit, revisable call; the mixed case is real (see the structure note's caveat: part of a methodology is native to its own level of description and belongs to neither pure regime).

Recording direction is unchanged from the retired footer: the dependency is recorded at the **source**, in a dedicated footer section below `Relevant Notes:`:

```markdown
Adapted into:

- [descriptive review](../reference/review.md) — the source material was reshaped for the review's descriptive contract

Operationalized into:

- [procedure](../instructions/procedure.md) — the methodology was worked into executable ordering and stopping conditions

Derived into:

- [cp-skill-write SKILL.md](../instructions/cp-skill-write/SKILL.md) — the duplicate-check rule
```

The downstream artifact carries no backlinks to its sources by default. Its reader is the consumer it was shaped for — not always an executor (a paper, a reference doc), but the executor case is demanding and common enough to set the default: provenance links dilute focus and add indirection cost exactly where the artifact must work unassisted. The forward pointer sits where change happens — editing a source note surfaces "these downstream artifacts may now need attention" with zero hops: for derived artifacts, recheck or re-derive; for abstracted artifacts, re-examine whether the generalization still holds. The reverse query ("what informed this artifact?") is rare and runs as a search: `rg "<artifact-name>" kb/theory/`.

Rationale: [source changes should surface downstream review targets, while reverse lineage can remain searchable](../theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md).

**Migration status.** `Distilled into:` is retired — write no new instances. Existing `Distilled into:` footers and pre-existing `derived-from` edges predate this boundary; they are classified into the new labels during the vocabulary-migration passes. Until reclassified, treat them as unclassified lineage — carrying neither regime's semantics. `derived-from` is tested per source-to-destination pairing against its reconstructibility condition; it is not banned merely because a source or target is descriptive, prescriptive, or generated content. A pairing remains eligible when the target is genuinely mechanically reconstructible and the source collection authorizes it.

## Limits

Only formal uses of a label assert its registered relation. An inline citation or a mention of a label in ordinary prose does not by itself assert one. A local reader-need example may clarify a shared meaning, not replace it.

When a pre-existing directional identifier is replaced, use [Migrate a directional link label](../instructions/migrate-directional-link-label.md) after semantic review supplies an adopted assertion and complete disposition ledger.

Do not use this page as a fallback for lazy labelling. If the source `COLLECTION.md` authorises specific labels for a destination, use those rather than downgrading to `see-also`.


---

Relevant Notes:

- [ADR 019 — collection-owned link vocabulary](./adr/019-collection-owned-link-vocabulary.md) — evidenced-by: the architecture this catalogue serves
- [ADR 059 — external is a reserved outbound destination](./adr/059-external-is-a-reserved-outbound-destination.md) — evidenced-by: external targets remain collection-authorized without becoming a search surface
- [ADR 009 — link relationship semantics](./adr/009-link-relationship-semantics.md) — evidenced-by: the original theoretical vocabulary whose core labels seed this catalogue
- [ADR 020 — theoretical-default additions (contrasts, mechanism)](./adr/020-theoretical-default-contrasts-mechanism.md) — evidenced-by: the audit outcomes adding `mechanism` and `contrasts` and stating directional asymmetry
- [ADR 058 — directional identifiers use the source as subject](./adr/058-directional-identifiers-use-source-as-subject.md) — evidenced-by: the naming invariant and evidence inverse pair
- [Links encode conditional possibilities, not obligations](../theory/links-encode-conditional-possibilities-not-obligations.md) — rests-on: the reader-need theory behind the label test
- [Theory and methodology form a two-layer execution system](../theory/theory-and-methodology-form-a-two-layer-execution-system.md) — rests-on: the maintenance regime the derived side of the lineage semantics asserts
- [Load-bearing vocabulary collisions should be prevented or visibly scoped at write time](../theory/vocabulary-collisions-prevented-at-write-time-not-read-time.md) — rests-on: why the derived/abstracted boundary is drawn at labelled edges rather than in unstructured natural-language content
- [Collection and text contract](./definitions/collection.md) — defined-in: collections own the binding local link rules that select from this catalogue
