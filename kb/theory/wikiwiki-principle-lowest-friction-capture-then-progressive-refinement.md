---
description: Ward Cunningham's wiki design principle — minimize capture friction, refine in place — drives the text→note→structured-claim refinement ladder
type: types/note.md
traits: [has-external-sources]
tags: [type-system, document-system]
---

# The wikiwiki principle: lowest-friction capture, then progressive refinement in place

The KB type hierarchy is a refinement ladder for thoughts. Its design principle comes from Ward Cunningham's original wiki: make saving a thought trivially easy, then make refining it easy — in place, not by moving it elsewhere.

## Evidence

1. **The original wiki.** Cunningham's WikiWikiWeb (1995) was built around two properties: anyone can create a page instantly (lowest capture friction), and anyone can edit it later (progressive refinement). The name "wiki" comes from Hawaiian "wikiwiki" meaning "quick" — speed of capture was the core design value. Pages started rough and improved through repeated editing, not through a draft→review→publish pipeline.

2. **Our type ladder mirrors this.** The [type system](../reference/collections-and-types.md) supports the same pattern:
   - **`text`** — no frontmatter, just write. Zero friction, like creating a wiki page.
   - **`note`** — add valid frontmatter with `description` and
     `type: types/note.md`, then develop the title and connections. Now
     findable.
   - **[`structured-claim`](./types/structured-claim.md)** — separate Evidence from Reasoning when readers benefit from inspecting them separately. Add Caveats where needed.

   Each step adds structure only when the thought has earned it. The same
   logical artifact grows structure in its current collection; conversion may
   normalize its filename and repair backlinks rather than preserving a
   mismatched path.

3. **Verification stays orthogonal.** A structurally complete `structured-claim` may still lack `user-verified`; shaping, semantic review, and explicit human attestation are distinct operations. Structure can be refined without manufacturing a commitment signal.

## Reasoning

A half-formed intuition needs to be saved before it is forgotten. When another note starts relying on it, check whether a reader can see how its evidence supports its conclusion. Sometimes [one sentence stating an assumption](./an-assumption-worth-disputing-is-worth-stating.md) is enough. Choose sections when they make that reasoning easier to inspect, not as a mark of maturity.

The key property is **refinement in place**. A `text` file becomes a `note` by
adding valid note frontmatter. A `note` becomes a `structured-claim` by adopting
that type's pointer and sections. No content migration, copy, or publication
pipeline is required. Conversion may normalize the filename within the same
collection, but it repairs backlinks and preserves the artifact's body and Git
history. This makes refinement cheap enough to actually happen — the same
insight Cunningham had about wiki pages.

Refining a document's natural-language argument is not by itself [codification](./definitions/codification.md). The argument remains interpreted even when its structure makes it easier to review. Fields or section requirements become symbolic only where a validator or other held-to reference fixes their consequences. Replacing repeated LLM checks with such a validator is a code-extraction case of codification; the broader definition also permits adopting a pinned model package as the reference, without making its behavior deterministic. The wiki principle concerns capture and refinement costs, not that form boundary.

## Caveats

- **Wikis have a decay problem.** The original WikiWikiWeb suffered from stale pages nobody maintained. Explicit replacement links, retired-note prose, and review freshness expose some decay, but the risk remains — low capture friction means high volume, and curation must keep up.
- **"In place" has limits.** A `text` file that grows into a 500-line `structured-claim` might be better split. The principle is "refine in place when possible," not "never split."
- **The ladder is a library pattern.** Refinement-in-place assumes documents move toward permanence — accumulating structure, becoming more connected, staying in the KB. [Workshop documents](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) (tasks, decision threads, experiments) follow the opposite trajectory: they consume value over time and end by being archived or discarded. The wikiwiki principle applies to knowledge capture, not work-in-motion.

---

Relevant Notes:

- [collections and types](../reference/collections-and-types.md) — the artifact-contract model that supports the text → note → structured-claim ladder
- [codification](./definitions/codification.md) — contrasts: refinement can preserve natural-language form; validator-consumed fields or checks can separately cross into symbolic form
- [constraining and extraction can trade generality for reliability, speed, or cost](./constraining-and-extraction-both-trade-generality-for-reliability.md) — the theoretical backing: each rung on the ladder trades generality for reliability, speed, and cost
- [Title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — a claim title lets readers see the point of a note without requiring a change of type.
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — boundary: the refinement ladder is specifically a library pattern; workshop documents follow the opposite trajectory (consuming value, ending in archival)
