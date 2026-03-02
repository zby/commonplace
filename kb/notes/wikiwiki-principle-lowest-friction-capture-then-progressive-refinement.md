---
description: Ward Cunningham's wiki design principle — minimize capture friction, then refine in place — is the animating idea behind the text→note→structured-claim crystallisation ladder
type: note
traits: [has-external-sources]
areas: [document-system]
status: seedling
---

# The wikiwiki principle: lowest-friction capture, then progressive refinement in place

The claw type hierarchy is a crystallisation ladder for thoughts, and the design principle behind it is Ward Cunningham's original wiki idea: make it trivially easy to save a thought, then make it easy to refine it — in place, not by moving it somewhere else.

## Evidence

1. **The original wiki.** Cunningham's WikiWikiWeb (1995) was designed around two properties: anyone can create a page instantly (lowest capture friction), and anyone can edit it later (progressive refinement). The name "wiki" comes from Hawaiian "wikiwiki" meaning "quick" — the speed of capture was the core design value. Pages started rough and improved through repeated editing, not through a pipeline of draft→review→publish.

2. **Our type ladder mirrors this.** The [document classification](./document-classification.md) hierarchy follows the same pattern:
   - **`text`** — no frontmatter, just write. Zero friction, like creating a wiki page.
   - **`note`** — add frontmatter, give it a claim title, connect it. Now findable.
   - **`structured-claim`** — add Evidence/Reasoning/Caveats sections. Now [verifiable](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md).

   Each step adds structure only when the thought has earned it. The file never moves, never gets copied — it grows structure in place.

3. **The status axis reinforces it.** `seedling` → `current` is orthogonal to the type ladder but serves the same principle: you can have a structurally complete `structured-claim` that's still a seedling (not yet reviewed). Structure and commitment are independent — you can refine the shape without committing to the content.

## Reasoning

A half-formed intuition doesn't need Toulmin sections — it needs to exist before it's forgotten. A mature argument that other notes depend on as a premise does need sections — because now it's load-bearing and we need to trust it. The wiki principle says: don't force the mature structure at capture time, because the friction will prevent capture. And don't leave the mature argument unstructured, because then you can't verify it.

The key property is **refinement in place**. A thought captured as `text` becomes a `note` by adding frontmatter to the same file. A `note` becomes a `structured-claim` by adding sections to the same file. No migration, no new file, no pipeline. The URL (file path) stays stable, links don't break, git history is preserved. This is what makes refinement cheap enough to actually happen — the same insight Cunningham had about wiki pages.

This connects to [crystallisation](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md): crystallisation is the general pattern (stochastic → deterministic), the wiki principle is the UX requirement that makes it work (each step must be low-friction and in-place).

## Caveats

- **Wikis have a decay problem.** The original WikiWikiWeb eventually suffered from stale pages nobody maintained. Our `status: outdated` and seedling review process are meant to address this, but the risk remains — low friction for capture means high volume, and curation must keep up.
- **"In place" has limits.** A `text` file that grows into a 500-line `structured-claim` might be better split. The principle is "refine in place when possible," not "never split."
- **The ladder is a library pattern.** The refinement-in-place trajectory assumes documents move toward permanence — accumulating structure, becoming more connected, staying in the KB. [Workshop documents](./a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) (tasks, decision threads, experiments) follow the opposite trajectory: they consume value over time and end by being archived or discarded. The wikiwiki principle applies to knowledge capture, not to work-in-motion.

---

Relevant Notes:
- [document-classification](./document-classification.md) — the type ladder this principle animates: text → note → structured-claim
- [claim notes should use Toulmin-derived sections](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) — the structured-claim type that sits at the top of the refinement ladder
- [three distinct mechanisms](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) — the general pattern; the wiki principle is the UX requirement that makes crystallisation practical
- [learning-is-capacity-change](../notes/learning-is-capacity-change.md) — the theoretical backing: each rung on the ladder is a capacity change in Simon's sense, trading generality for reliability
- [title-as-claim-enables-traversal-as-reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — the note→structured-claim transition: a claim title is the first refinement step, Toulmin sections are the second
- [a functioning claw needs a workshop layer](./a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) — boundary: the refinement ladder is specifically a library pattern; workshop documents follow the opposite trajectory (consuming value, ending in archival)

Topics:
- [document-system](./document-system.md)
