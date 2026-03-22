---
description: Ward Cunningham's wiki design principle — minimize capture friction, refine in place — drives the text→note→structured-claim codification ladder
type: note
traits: [has-external-sources]
tags: [type-system]
status: seedling
---

# The wikiwiki principle: lowest-friction capture, then progressive refinement in place

The KB type hierarchy is a codification ladder for thoughts. Its design principle comes from Ward Cunningham's original wiki: make saving a thought trivially easy, then make refining it easy — in place, not by moving it elsewhere.

## Evidence

1. **The original wiki.** Cunningham's WikiWikiWeb (1995) was built around two properties: anyone can create a page instantly (lowest capture friction), and anyone can edit it later (progressive refinement). The name "wiki" comes from Hawaiian "wikiwiki" meaning "quick" — speed of capture was the core design value. Pages started rough and improved through repeated editing, not through a draft→review→publish pipeline.

2. **Our type ladder mirrors this.** The [document classification](./document-classification.md) hierarchy follows the same pattern:
   - **`text`** — no frontmatter, just write. Zero friction, like creating a wiki page.
   - **`note`** — add frontmatter, claim title, connections. Now findable.
   - **`structured-claim`** — add Evidence/Reasoning/Caveats sections. Now [verifiable](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md).

   Each step adds structure only when the thought has earned it. The file never moves or gets copied — it grows structure in place.

3. **The status axis reinforces it.** `seedling` → `current` is orthogonal to the type ladder but serves the same principle: a structurally complete `structured-claim` can still be a seedling (not yet reviewed). Structure and commitment are independent — you can refine shape without committing to content.

## Reasoning

A half-formed intuition doesn't need Toulmin sections — it needs to exist before it's forgotten. A mature argument that other notes depend on as a premise does need sections — it's load-bearing and must be trustworthy. The wiki principle says: don't force mature structure at capture time, because friction prevents capture. Don't leave mature arguments unstructured, because you can't verify them.

The key property is **refinement in place**. A `text` file becomes a `note` by adding frontmatter. A `note` becomes a `structured-claim` by adding sections. No migration, no new file, no pipeline. The file path stays stable, links don't break, git history is preserved. This makes refinement cheap enough to actually happen — the same insight Cunningham had about wiki pages.

This connects to [codification](../notes/codification.md): codification is the general pattern (stochastic → deterministic), the wiki principle is the UX requirement that makes it work (each step must be low-friction and in-place).

## Caveats

- **Wikis have a decay problem.** The original WikiWikiWeb suffered from stale pages nobody maintained. Our `status: outdated` and seedling review process address this, but the risk remains — low capture friction means high volume, and curation must keep up.
- **"In place" has limits.** A `text` file that grows into a 500-line `structured-claim` might be better split. The principle is "refine in place when possible," not "never split."
- **The ladder is a library pattern.** Refinement-in-place assumes documents move toward permanence — accumulating structure, becoming more connected, staying in the KB. [Workshop documents](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) (tasks, decision threads, experiments) follow the opposite trajectory: they consume value over time and end by being archived or discarded. The wikiwiki principle applies to knowledge capture, not work-in-motion.

---

Relevant Notes:

- [document-classification](./document-classification.md) — the type ladder this principle animates: text → note → structured-claim
- [claim notes should use Toulmin-derived sections](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) — the structured-claim type that sits at the top of the refinement ladder
- [codification](../notes/codification.md) — the general pattern; the wiki principle is the UX requirement that makes codification practical
- [constraining and distillation both trade generality for compound](../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — the theoretical backing: each rung on the ladder trades generality for reliability, speed, and cost
- [title-as-claim-enables-traversal-as-reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — the note→structured-claim transition: a claim title is the first refinement step, Toulmin sections are the second
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — boundary: the refinement ladder is specifically a library pattern; workshop documents follow the opposite trajectory (consuming value, ending in archival)
- [Toulmin Argument (Purdue OWL)](../sources/purdue-owl-toulmin-argument.md) — enables: Toulmin's argumentation model provides the Evidence/Reasoning/Caveats sections that define the top rung of the refinement ladder
