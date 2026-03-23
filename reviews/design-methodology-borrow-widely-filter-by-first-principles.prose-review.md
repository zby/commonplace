=== PROSE REVIEW: design-methodology-borrow-widely-filter-by-first-principles.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The programming fast-pass bet is presented with assertive framing that outpaces the note's own epistemic status. "both are bounded processors composing text under constraints" and "these aren't metaphors — they describe the same mechanisms operating on different substrates" assert structural identity as established fact, but the note itself calls this "the bet" and labels the Thalo convergence as merely "stronger evidence than any single design argument." The assertive sentences read as if the bet has already been validated; the framing sentences say it hasn't. These coexist in tension.
  Recommendation: Choose one register. Either strengthen the evidence section to justify the assertive language (e.g., cite more convergence cases or articulate why the structural mapping is tight enough to treat as established), or soften the assertive sentences to match the "bet" framing ("we treat these as the same mechanisms" rather than "these aren't metaphors — they describe the same mechanisms").

- [Proportion mismatch] The core claim is the adoption filter (title: "borrow widely, filter by first principles"). The adoption filter section covers four tiers in roughly equal depth (~1 paragraph each). The "Why the asymmetry" section then spends three substantial paragraphs elaborating on just one of those tiers — the programming vs. cognitive science distinction — and adds a fourth paragraph on empirical observation that introduces a new dimension (quantity vs. weight) not mentioned in the adoption filter section at all. The asymmetry explanation has become the heaviest part of the note, even though it's subordinate to the main claim. Meanwhile, the first-principles filter itself — the title concept — gets one paragraph in the adoption section and no further development.
  Recommendation: Either develop the first-principles filter more (what counts as a first principle? how do you know you've derived something vs. rationalized it?) or consider whether the empirical-observation-vs-first-principles weight discussion belongs in a separate note, since it introduces a distinct axis (evidence weight) that the adoption filter doesn't set up.

INFO:
- [Orphan references] "Arscontexta's 249 research claims grounded in cognitive psychology" — the number 249 is specific enough to want a source. The link to the Ars Contexta related-system review presumably contains this, but within this note the figure appears without attribution. A reader who doesn't click through has no way to evaluate it.

- [Redundant restatement] The opening of "Why the asymmetry" restates the adoption filter's content: "The asymmetry between programming and cognitive science isn't about one field being better. It's about the nature of the target system." This recaps a point already clear from the prior section's structure (programming gets a fast pass, cognitive science doesn't). The section would lose nothing by starting directly with "Human cognition is associative, embodied, affective."

CLEAN:
- [Source residue] The note claims to be about design methodology for knowledge bases. All examples (context windows, directory-scoped types, frontmatter schemas, markdown files) are native to that domain. References to cognitive science and programming are explicitly framed as source domains, not leakage. No residue detected.

- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus present. The note argues entirely in prose. Clean.

- [Unbridged cross-domain evidence] Every cross-domain reference includes an explicit bridge. Tulving's taxonomy: "because it maps to a real architectural need." Programming patterns: "both are bounded processors composing text under constraints." Legal drafting: "operates in the same medium as prompts." Cognitive science: "analogies need independent justification." The note is unusually self-aware about bridging requirements — it is, in fact, a note about when and how to bridge.

- [Anthropomorphic framing] "Agents interpreting prompts" and "agents reason over text" use agency language, but these are standard terms of art for agent-based systems and the note is explicitly about LLM agents as a target system. No anthropomorphic language is used to smuggle in claims about model internals. Clean.

Overall: 2 warnings, 2 info
===
