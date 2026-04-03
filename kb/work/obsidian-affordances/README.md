# Workshop: Obsidian Affordances

## Question

Which Obsidian-facing affordances would make commonplace easier to use and inspect for humans without collapsing the repo's existing agent-first semantics, explicit relationship links, and git-native workflows?

## Why this workshop exists

Commonplace already has a strong theory for document structure, retrieval filters, and link semantics, but it is comparatively thin on mainstream note-tool ergonomics. Two reviewed systems sharpen the opportunity from different sides:

- [Napkin](../../notes/related-systems/napkin.md) shows that Obsidian compatibility can be a practical adoption strategy and that agent-facing UX defaults are load-bearing.
- [LACP](../../notes/related-systems/lacp.md) shows an Obsidian-centered operations stack around local agent workflows, but also demonstrates how quickly a vault layer can sprawl into maintenance plumbing.

The goal is not "turn commonplace into an Obsidian vault." The goal is to decide which affordances are worth adding as an optional compatibility/interface layer, and which would undermine the KB's stronger commitments:

- explicit relationship semantics in links
- repo-native files reviewed through git
- workshop/library separation
- human-readable structure that agents can also traverse

There is currently no `.obsidian/` directory, no `.canvas` files, and no `.base` files in this repo. That is useful starting clarity: we are designing from first principles, not inheriting an existing vault substrate.

## Current grounding

- [Napkin](../../notes/related-systems/napkin.md) — strongest source for Obsidian-compatible agent memory affordances
- [LACP](../../notes/related-systems/lacp.md) — strongest source for Obsidian-centered local ops and memory automation
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — workshop framing for temporary design work and promotion boundaries
- [Short composable notes maximize combinatorial discovery](../../notes/short-composable-notes-maximize-combinatorial-discovery.md) — reminder that longer synthesized views belong in workshops, not in the library
- [The wikiwiki principle: lowest-friction capture, then progressive refinement in place](../../notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) — useful contrast because Obsidian inherits stronger refinement-in-place assumptions than commonplace does

## What this workshop needs to resolve

1. Which Obsidian affordances are merely interface improvements, and which would silently change the KB's representation model?
2. Which affordances can be added as optional generated/configuration artifacts, and which would force canonical content changes?
3. Which current repo conventions are genuinely load-bearing, and which are adaptable implementation choices, including link syntax?
4. What is the smallest useful Obsidian layer: tags and properties, graph/backlink navigation, Bases-style query support, Canvas, templates, daily-note patterns, or something narrower?
5. Should the target be "open this repo comfortably in Obsidian" or "generate an Obsidian-shaped view over the repo"?
6. If link syntax changes, do we want a hard switch, dual-syntax support, or one canonical syntax plus generated compatibility views?

## Working hypotheses

- Obsidian compatibility is most promising as an **interface layer**, not a new canonical storage model.
- Generated or optional artifacts are safer than changing canonical note syntax.
- Bases-style structured query support may be useful for workshop/task/state views before it is useful for the core note library.
- Canvas support is only worthwhile if it produces a real workflow gain, not just a prettier map.
- Link syntax is adaptable; the stronger invariant is preserving explicit relationship semantics, stable resolution, and readable diffs.

## Deliverables

- a ranked inventory of candidate Obsidian affordances
- an explicit list of non-negotiable commonplace constraints
- one recommended implementation path for a minimal compatibility layer
- a decision on which affordances are "ready now", "needs a concrete use case", or "reject"
- one promoted library artifact if the design stabilizes into a note, ADR, or instruction

## Starter artifacts

- [candidate-affordances.md](./candidate-affordances.md) — initial inventory of possible Obsidian-facing affordances
- [integration-constraints.md](./integration-constraints.md) — constraints that preserve commonplace's current design commitments
- [web-clipper-as-capture-layer.md](./web-clipper-as-capture-layer.md) — proposal to use Obsidian Web Clipper for source capture while keeping `/ingest` as graph-aware analysis
- [web-clipper-adaptation-plan.md](./web-clipper-adaptation-plan.md) — phased rollout plan for adapting Web Clipper into the `kb/sources/` workflow without replacing graph-aware ingestion

## Open questions

- Is "Obsidian affordance" mostly about human navigation, or also about better agent query surfaces?
- Should any Obsidian-facing layer be committed to the repo, or generated locally?
- Are properties/frontmatter affordances enough, or does the value only appear when graph/Bases/Canvas features are also present?
- What should happen when Obsidian defaults conflict with explicit relationship semantics?
