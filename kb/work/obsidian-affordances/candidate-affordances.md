# Candidate Obsidian Affordances

This is an initial inventory, not a recommendation. The goal is to separate "useful interface adaptation" from "representation drift."

## Likely ready to explore

- **Readable frontmatter/property ergonomics.** Commonplace already uses frontmatter heavily. Check whether small naming or formatting choices make the repo more comfortable in Obsidian without changing semantics.
- **Backlink and local-graph friendliness.** The repo already has strong links; the question is whether small compatibility tweaks improve Obsidian's existing graph/backlink surfaces without changing canonical link syntax.
- **Vault-local configuration.** A minimal `.obsidian/` config could improve reading experience, saved searches, or panes without changing the knowledge substrate itself.
- **Template support for workshop scaffolds.** Obsidian templates could make workshop setup faster for humans if they remain optional and do not become a second canonical write path.
- **Obsidian Web Clipper as the source-capture front-end.** This is the strongest concrete Obsidian affordance identified so far. It looks promising as a replacement for `/snapshot-web` in browser-driven capture workflows while preserving `/ingest` as the graph-aware analysis and recommendation layer.

## Interesting but needs a concrete use case

- **Bases-style query views.** Structured slices over frontmatter and workshop state may be genuinely useful, but only if there are recurring questions that grep and indexes answer poorly.
- **Canvas views for active workshops.** This could help design or triage work, but only if a workshop genuinely benefits from spatial arrangement rather than prose notes and links.
- **Bookmarks and workspace layouts.** These are useful for a live operator, but may be too user-specific to commit unless they encode a shared operational workflow.
- **Aliases and display names.** Helpful in Obsidian, but risky if they blur the KB's title-as-claim and filename discipline.
- **Wiki-link syntax or dual-syntax support.** Potentially valuable for Obsidian ergonomics, but only if explicit relationship semantics, migration cost, tooling updates, and canonical-syntax rules are all handled deliberately.

## Probably reject or keep non-canonical

- **Semantically thin graph usage as a substitute for relationship language.** Useful as a view, not as a replacement for articulated link meaning.
- **Obsidian-only metadata that becomes required for canonical notes.** If a field only exists to satisfy one tool and adds no retrieval or reasoning value, it should stay optional or generated.

## Evaluation criteria

- Does the affordance improve human navigation or agent navigation in a way we can describe concretely?
- Can it stay optional or generated?
- Does it preserve standard markdown links and explicit relationship semantics?
- Does it preserve clean git diffs and repo reviewability?
- Does it help the workshop layer, the library layer, or both?
- Would a simpler alternative in plain markdown or shell scripts achieve the same result?
