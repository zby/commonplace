# Link vocabulary — a resource for COLLECTION.md authors

> Workshop draft. Final location TBD — candidate: `kb/reference/link-vocabulary.md`.

## Audience and purpose

**Audience: `COLLECTION.md` authors** — the people defining or revising the outbound-linking rules of a collection. This document is a **catalogue of labels** plus **authoring guidance**. It helps a collection author pick labels for each destination collection their collection links to.

**Note writers do not read this document.** They read only their collection's `COLLECTION.md`, which has the authoritative vocabulary for that collection, organised by destination.

The architecture is deliberately loose. The theory of links is weak — experiment. Invent intra-collection labels your work needs, propose additions to the catalogue, diverge from suggestions where it makes sense.

("Register" means one of three content modes — theoretical, descriptive, prescriptive — that determines a collection's quality goal, title conventions, and linking rules. See [`register`](../../notes/definitions/register.md).)

## How to author a COLLECTION.md linking section

Organise the outbound-linking section **per destination collection**, not per register. For each collection your source links to, declare:

1. **Search guidance** — when the [connect skill](../../instructions/cp-skill-connect/SKILL.md) (or an author manually prospecting for links) should search this destination from the source. Concrete triggers work best: *"search when the source asserts a claim without evidence,"* not *"search when relevant."*
2. **Authorised labels** — the labels writers in the source collection may use for links to this destination. Give each a one-line reader-need context specific to this *source → destination* pairing.

If a destination isn't listed, it isn't an active link target from this collection. Adding a destination is a collection-author decision; writers cannot unilaterally link to collections outside the authorised set.

**Search latitude.** Search guidance should be specific enough to keep results within the agent's effective context, but open enough to surface serendipitous finds. Over-narrow triggers miss adjacent connections the agent might usefully make; over-broad triggers drown the connect skill in noise. When the destination is small or the query sparse, prefer slight over-retrieval — the agent can filter results in context, whereas missed links are harder to recover. Avoid phrasing that rules out whole classes of plausible connection (e.g., "only when X").

The catalogue below groups labels by register-of-origin — the kind of content they emerged to describe — but each `COLLECTION.md` picks whichever labels fit each destination. The register tagging is advisory.

## Key principles

1. **`COLLECTION.md` governs all outbound links**, organised per destination.
2. **Per-destination rules enable fine-grained experimentation.** `kb/notes/ → kb/reference/` can diverge from `kb/notes/ → kb/agent-memory-systems/`, even though both destinations share a register.
3. **Search guidance serves the connect skill.** When an agent helps a writer find link targets, it reads the source `COLLECTION.md`, enumerates authorised destinations, and uses the search-when guidance to prioritise.
4. **Labels work best when shared.** Both endpoints need to recognise the label for the link to carry its intended meaning. Use catalogue labels when they fit; add to the catalogue when your work calls for something new, and coordinate with the target-side collection.
5. **Every label names a reader-need.** See [`links-as-possibility.md`](./links-as-possibility.md) for the theory.
6. **Articulation test applies to every link.** Every outbound link should complete: *"[source] connects to [target] because [specific reason]."*

## Label catalogue

Labels cluster by register-of-origin. Each `COLLECTION.md` selects whichever labels fit each destination.

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

## What this document is not

- **Not a constraint.** Labels and authoring guidance. Add to it, adapt it, experiment. Soft pressure only: labels need shared recognition to carry consistent meaning across collections.
- **Not the authoritative vocabulary for any collection.** Each `COLLECTION.md` is authoritative for its source. This document is a palette.
- **Not a fallback for lazy labelling.** If the `COLLECTION.md` authorises specific labels for a destination, use those — don't downgrade to `see-also`.

## Open questions

- When should a collection-specific label (`compares-with`) get promoted to the catalogue at large? Current: document it here once it's in use, flagged "currently specific to X."
- Is register-of-origin the right catalogue grouping, or would alphabetical be cleaner? Register-of-origin helps authors find labels that match their source's shape; alphabetical is flatter but less suggestive.
- How should the connect skill treat authorized-but-rarely-used destinations? Speculative — probably depends on use-frequency signal.
- Should `supersedes` be restricted to intra-descriptive use? Most use is ADR chains inside `kb/reference/`; cross-collection supersession is rare.
