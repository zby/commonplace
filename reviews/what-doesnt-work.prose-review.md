=== PROSE REVIEW: what-doesnt-work.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The auto-commits section asserts "Agents should not commit without explicit human approval" as a general rule derived from a single project's experience. The note's own framing ("manual observation log") acknowledges these are local observations, but this sentence reads as an established best practice rather than a project-specific conclusion. The leap from "created a mess" in this project to a universal prescription is unhedged.
  Recommendation: Scope the claim to the project: "In this project, agents should not commit without explicit human approval" or add a hedge: "Our experience suggests agents should not commit without explicit human approval."

- [Proportion mismatch] The core claim implied by the title ("What doesn't work") covers two areas: auto-commits and observations needing more evidence. The auto-commits section (the only item with a clear verdict) gets 3 sentences, while the "observations needing more evidence" section (explicitly marked as inconclusive) gets 5 bullet points with more total prose. The section that carries the title's claim — things that definitively don't work — is thinner than the section of open questions.
  Recommendation: Either develop the auto-commits section with more specifics (what the mess looked like, what the removal effort involved) or retitle the note to reflect that it is primarily an anti-pattern observation log with mostly open questions rather than settled verdicts.

INFO:
- [Source residue] The second paragraph of the auto-commits section ("Together with what works...") shifts from describing the anti-pattern to describing the note's role in a KB learning loop. This is meta-commentary about the note's purpose rather than content about what doesn't work. It reads like editorial framing that leaked from a planning context into what is otherwise a practitioner-facing observation log. It doesn't misrepresent a domain, but it does break the note's voice.

- [Orphan references] "orphan rate reached ~90%" in the last bullet is a specific quantitative claim with no source, methodology, or timeframe. When was this measured? How was "orphan" defined — notes with zero inbound links, or notes not connected to any index? The precision of "~90%" implies measurement, but nothing in the note supports it.
  Recommendation: Either add context (when measured, how defined, what the denominator was) or soften to a qualitative statement like "the vast majority of notes remained unconnected."

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus present. The note uses plain prose throughout.
- [Redundant restatement] Each section opens with its own content. No section re-explains what the previous section established.
- [Unbridged cross-domain evidence] No cross-domain evidence is cited. All observations are from the project's own experience.
- [Anthropomorphic framing] The note refers to "agents" in the context of software agents performing commits, which is the correct technical usage. No anthropomorphic language is applied to models.

Overall: 2 warnings, 2 info
===
