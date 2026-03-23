=== PROSE REVIEW: backlinks.md ===

Checks applied: 8

WARN:
- [Source residue] The note refers to "the new `docs/sources/` directory" (line 29), but the actual path in this KB is `kb/sources/`. The `docs/sources/` path looks like residue from an earlier directory layout or a draft where the prefix was different. This appears in use case 2, which builds an argument around source-to-theory bridging — the stale path undermines the concreteness of that argument.
  Recommendation: Replace `docs/sources/` with `kb/sources/`.

- [Orphan references] The claim "44% of notes currently lack Relevant Notes sections at all" appears twice (lines 76 and 90) with no source, date, or methodology. It reads as a measured statistic — was it computed by a script at some point? If so, it may be stale. If it was an estimate, the precision of "44%" overstates confidence.
  Recommendation: Either link to or describe how the number was computed (e.g., "as of [date], a grep for 'Relevant Notes' found..."), or soften to an approximation ("roughly half of notes").

- [Confidence miscalibration] Use case 2 states: "That's a signal about the claim's empirical grounding — and a synthesis opportunity when enough sources converge." This frames a speculative future benefit as a definitive statement. The note's own frontmatter marks it `status: speculative`, but the prose in several use cases uses assertive framing ("That changes how carefully they read it," "Backlinks would surface tensions from both sides") rather than proposing these as expected effects.
  Recommendation: Add light hedging to the use-case descriptions. For example: "That would change how carefully they read it" or "Backlinks could surface tensions from both sides." The note already hedges well in the Open Questions section — matching that tone in the use cases would improve calibration.

INFO:
- [Proportion mismatch] The four use cases (lines 19-45) take roughly 27 lines, while the four design options (lines 55-84) take roughly 30 lines. Both sections are well-developed relative to their role in the note. However, the "Trade-offs to consider" section (lines 88-92), which synthesizes the design options against practical constraints, gets only 3 short paragraphs. Given that the note's title frames this as "use cases and design space," the trade-offs section is arguably the load-bearing synthesis and could benefit from more development — particularly around how the trade-offs interact (e.g., does the readability concern apply differently to options A vs B?).

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus present. The note uses numbered lists and lettered options, which are organizational rather than formal. Clean.

- [Unbridged cross-domain evidence] The note stays within its own domain (agent-operated knowledge bases). The one near-transfer — citing how `sync_topic_links.py` works as precedent for option B — is valid because it references a tool in the same codebase. No cross-domain leaps found.

- [Redundant restatement] Each section opens with new content. The gap section establishes the problem, use cases enumerate specific benefits, non-use-cases scope the proposal, design options present alternatives. No section re-explains a prior section's conclusion before making its own point.

- [Anthropomorphic framing] The note discusses "agents" throughout, but in this KB's context, agents are the actual operators of the system — attributing actions to them ("an agent lands on a note," "agents add backlinks") is literal, not anthropomorphic. No language attributes mental states to models. Clean.

Overall: 3 warnings, 1 info
===
