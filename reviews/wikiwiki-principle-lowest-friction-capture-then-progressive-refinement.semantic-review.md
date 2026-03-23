=== SEMANTIC REVIEW: wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md ===

Claims identified: 12

1. "The KB type hierarchy is a codification ladder for thoughts." (opening paragraph)
2. "Its design principle comes from Ward Cunningham's original wiki." (opening paragraph)
3. "The name 'wiki' comes from Hawaiian 'wikiwiki' meaning 'quick' — speed of capture was the core design value." (Evidence, item 1)
4. "Pages started rough and improved through repeated editing, not through a draft->review->publish pipeline." (Evidence, item 1)
5. The type ladder mirrors the wiki pattern: text (zero friction) -> note (findable) -> structured-claim (verifiable). (Evidence, item 2)
6. "Each step adds structure only when the thought has earned it. The file never moves or gets copied — it grows structure in place." (Evidence, item 2)
7. The status axis (seedling -> current) is orthogonal to the type ladder: "Structure and commitment are independent." (Evidence, item 3)
8. "The wiki principle says: don't force mature structure at capture time, because friction prevents capture." (Reasoning)
9. "A text file becomes a note by adding frontmatter. A note becomes a structured-claim by adding sections. No migration, no new file, no pipeline." (Reasoning)
10. "codification is the general pattern (stochastic -> deterministic), the wiki principle is the UX requirement that makes it work (each step must be low-friction and in-place)." (Reasoning)
11. "Low capture friction means high volume, and curation must keep up." (Caveats, item 1)
12. "The ladder is a library pattern" — workshop documents follow the opposite trajectory and the wikiwiki principle does not apply to them. (Caveats, item 3)

---

WARN:
- [Completeness] The note calls the type hierarchy a "codification ladder" (claim 1), but the codification note defines codification as "constraining that crosses a medium boundary from natural language to a symbolic medium (code)." The text -> note -> structured-claim progression never leaves natural language. All three rungs remain markdown consumed by an LLM. By the codification note's own definition, this ladder is constraining within natural language, not codification. The note does link to codification and says "codification is the general pattern (stochastic -> deterministic)," but codification.md is specific: it is NOT the general pattern — constraining is the general pattern, and codification is the far end where a medium boundary is crossed. Using "codification ladder" to describe promotions that stay in markdown overstates what the linked source supports.

- [Grounding alignment / domain coverage] The note claims the relationship to codification is: "codification is the general pattern (stochastic -> deterministic), the wiki principle is the UX requirement that makes it work." But codification.md says "Codification is not a separate mechanism from constraining; it's what constraining looks like when it goes all the way." The general pattern is constraining, not codification. The note inverts the relationship — it should say constraining is the general pattern and the wiki principle is the UX requirement, with codification being the far end the ladder never actually reaches (since structured-claims are still natural language).

INFO:
- [Completeness / boundary case] The note claims "The file never moves or gets copied — it grows structure in place" (claim 6) and "No migration, no new file, no pipeline" (claim 9). The Caveats section acknowledges splitting as a limit case, but there is a more common boundary case the note does not address: a note that gains structure may also gain connections and get re-indexed, which can change its effective location in the conceptual graph even though the file path stays stable. More importantly, the document-classification note shows types beyond the three on the ladder (spec, review, index, adr). A note that matures into an ADR or spec does not climb the text -> note -> structured-claim ladder — it moves laterally to a different type. The ladder is presented as THE refinement path, but the actual type system has branching paths, not a single ladder.

- [Completeness / boundary case] The simplest instance of "lowest-friction capture" would be not writing a file at all — e.g., appending a line to kb/log.md, which CLAUDE.md explicitly recommends for improvement opportunities noticed during traversal. This is lower friction than creating a text file. The note's ladder starts at text, but the KB already has a capture mechanism below text. This does not break the argument, but the ladder's bottom rung may not actually be the lowest-friction option the system offers.

- [Grounding alignment] The note says the type ladder mirrors the wiki: "text — no frontmatter, just write. Zero friction, like creating a wiki page." But creating a wiki page on WikiWikiWeb was collaborative and public by default — the friction was low for a different reason (no approval gate, not no structure). A text file in this KB is private, local, and has no metadata. The analogy holds on the "speed" axis but diverges on the "social editing / refinement by others" axis that was central to Cunningham's design. The note frames wiki as being about speed of capture, but Cunningham's wiki was equally about communal refinement — and this KB's refinement is done by a single author (or agent), not a community. The analogy is partial.

- [Internal consistency] The note positions "refinement in place" as the key property (Reasoning section) and says "The file path stays stable, links don't break, git history is preserved." But claim 7 says status is "orthogonal to the type ladder." If status changes (seedling -> current) are orthogonal refinement, and type changes (text -> note -> structured-claim) are the ladder refinement, then the note actually describes two independent refinement axes, both happening in place. This is not a contradiction, but the note's framing of "the key property is refinement in place" blurs these two distinct in-place refinements into one narrative without acknowledging that they serve different purposes (structure vs. endorsement).

PASS:
- [Internal consistency] The three Evidence items are mutually consistent: the wiki history (item 1), the type ladder mapping (item 2), and the status axis (item 3) each address different aspects without contradicting each other. The Reasoning section faithfully synthesizes all three.
- [Internal consistency] The Caveats section is well-calibrated. Each caveat genuinely limits the main claim rather than being pro-forma hedging. The wiki decay problem (caveat 1), the splitting limit (caveat 2), and the library-only scope (caveat 3) each identify a real boundary. Caveat 3 is especially well-grounded — the workshop note confirms the library/workshop distinction and explicitly says "the refinement ladder is specifically a library pattern."
- [Grounding alignment] The link to the workshop note is accurate. The workshop note says "The wikiwiki principle animates this ladder: capture with zero friction, then refine in place" and "workshop documents follow the opposite trajectory." The bidirectional references are consistent and neither note misrepresents the other.
- [Grounding alignment] The link to the Toulmin/structured-claim note is accurate. That note confirms "The promotion path is note -> structured-claim: when a note's argument matures enough to fill Evidence/Reasoning sections, it earns the type," which is exactly how the wikiwiki principle note describes the top rung.
- [Grounding alignment] The link to document-classification is accurate for what it claims. The type table shows text (no frontmatter), note (has frontmatter), and structured-claim (has Evidence/Reasoning sections), matching the three-rung ladder described in the note.

Overall: 2 warnings, 4 info
===
