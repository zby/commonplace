=== PROSE REVIEW: link-contracts-framework.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents its entire framework — the five "click decision" questions, the link intent taxonomy, the annotated link pattern, the five rules — with full assertion: "Every link needs to earn a 'click decision'," "Five rules that work." None of this is cited from a source. The taxonomy (Definition, How-to, Reference, Example, Rationale, Evidence, Tool, Related, Index/Hub) and the enforcement rules ("Every new term must link to a Definition once," "Every instruction must link to a How-to") are the note's own construction presented as established best practice. The subtitle "source material" and the line "Received 2026-02-21" suggest this came from an external source, but the source is never identified — so the reader cannot assess whether the confident framing is earned.
  Recommendation: Either cite the source (who authored this framework, in what context), or reframe the prescriptive language as proposed conventions: "A useful taxonomy might include..." rather than stating categories as given. The "Received" provenance line creates an expectation of attribution that is never fulfilled.

- [Orphan references] The note states "Received 2026-02-21" and "Saved as reference for when we start building concrete link practices." This implies the content was received from an external source, but no source is identified — no author, no URL, no system, no conversation reference. The entire note is orphaned provenance: it signals that it came from somewhere without saying where.
  Recommendation: Add attribution. If the source is a conversation, tool output, or external document, name it. If the source cannot be recovered, note that explicitly ("source not recorded") so future readers don't search for it.

INFO:
- [Proportion mismatch] The title is "Link contracts framework — source material," and the opening frames the note as a reference for building concrete link practices. The "link contract" concept — the core idea — gets two short sections (the five questions and the minimal/annotated patterns, ~12 lines total). The link intent taxonomy, automated tests, and LLM/agent implications each get comparable or greater space. The "Five rules that work" section at the end compresses actionable guidance into five lines. For a note titled around "link contracts," the contract concept itself is surprisingly thin relative to the surrounding taxonomy and testing material, which could each be their own notes.
  Recommendation: If this remains a source-material reference note, the proportions are acceptable as-is (it's a dump, not an argument). If it's ever promoted to a proper note, the link contract idea needs more development relative to the supporting sections.

- [Source residue] The note's header says "source material" and the opening frames it as received reference material, not a distilled note. Several terms and patterns — "SLO policy," "CAP theorem," "Postmortem 2024-09-12," "retry logic" — are domain-specific examples from software engineering/SRE contexts. These are used as illustrative examples within the annotated-link section and are appropriately framed as examples (they appear as sample link annotations). However, the note's description ("Reference framework for systematic, testable linking") and tags suggest broader applicability than these SRE-flavored examples demonstrate. The gap is minor because the examples are clearly formatted as templates, not as the note's own claims.

CLEAN:
- [Pseudo-formalism] No formal notation, variables, equations, or symbolic apparatus. The note uses prose, bullet lists, and structured examples throughout. Clean.

- [Unbridged cross-domain evidence] No cross-domain evidence transfers attempted. The note stays within its own domain (linking practices in knowledge bases). The software engineering examples (SLO policy, CAP theorem, postmortems) are used as illustrative link-annotation samples, not as evidence claims transferred from another domain. Clean.

- [Redundant restatement] Each section opens with new content. "Link contract: minimal information" moves from the click-decision framing to concrete patterns. "Link intent taxonomy" introduces a new classification. "Making link decisions obvious" moves to presentation heuristics. "LLM/agent implications" shifts audience. No section re-explains prior sections. Clean.

- [Anthropomorphic framing] The note uses "reader" and "agents" as subjects, which are appropriate for their respective sections. The agent section uses behavioral language ("Prefer Reference/Evidence when verifying claims," "Skip Background when time/context is tight") that describes agent behavior without attributing cognitive states. No verbs implying understanding, belief, or knowledge are used for agents. Clean.

Overall: 2 warnings, 2 info
===
