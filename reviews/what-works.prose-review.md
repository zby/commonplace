=== PROSE REVIEW: what-works.md ===

Checks applied: 8

WARN:
- [Source residue] The "Frontmatter as queryable structure" section uses `docs/notes/` in its example commands (`rg '^areas:.*architecture' docs/notes/`), but this path does not exist in the current repository — the actual path is `kb/notes/`. This is residue from an earlier directory layout that leaked through when the note was generalized.
  Recommendation: Replace `docs/notes/` with `kb/notes/` in both example commands in that section.

- [Proportion mismatch] The note's core value is cataloguing "patterns that have proven valuable in practice," yet the "Semantic search via qmd" section (~130 words of body text plus a bullet list and a maintenance note) is substantially longer than any other section. "Discovery-first as creation constraint" and "Public/internal boundary," which are arguably equally important operational patterns, get roughly one-third the space each. The qmd section reads more like a tool guide than a pattern description.
  Recommendation: Trim the qmd section to the essential insight (semantic search complements keyword search; qmd provides it locally). Move operational details (search modes, `--files` flag, `update && embed` commands) to a dedicated qmd reference note or an instruction, and link from here.

INFO:
- [Confidence miscalibration] The title "What works" and opening line "Patterns that have proven valuable in practice" assert empirical validation. Most sections back this with language like "in practice" and concrete descriptions of behavior. However, no section cites specific evidence (a project, a timeframe, a measurable outcome) for why these patterns are "proven." The confidence level is plausible but rests entirely on implied personal experience.

- [Anthropomorphic framing] "The agent fills in the template, hits the empty field, and naturally asks 'what should this be?'" — "naturally asks" attributes a human-like deliberative process to the agent. This is mild and arguably colloquial, but "is prompted to supply a value" would be more precise about what actually happens (the empty field triggers completion behavior, not curiosity).

CLEAN:
- [Pseudo-formalism] No formal notation, variables, or equation-like apparatus appears anywhere in the note. All arguments are made in prose. Check passes cleanly.

- [Orphan references] No specific figures, percentages, named studies, or empirical data points appear in the note. All claims are qualitative. Nothing to orphan.

- [Unbridged cross-domain evidence] The note stays within its own domain (knowledge-base design and agent operation) throughout. No findings from external domains (cognitive science, software engineering research) are imported without bridge. The two explicit links — to `title-as-claim-enables-traversal-as-reasoning.md` and `files-not-database.md` — are internal cross-references, not cross-domain citations.

- [Redundant restatement] Each section opens with its own new content. No section begins by re-explaining a prior section's conclusion. The note reads as a flat catalogue, so there is little opportunity for restatement, and none occurs.

Overall: 2 warnings, 2 info
===
