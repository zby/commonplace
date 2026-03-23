=== PROSE REVIEW: claw-learning-is-broader-than-retrieval.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The four-item taxonomy of "what a Claw actually does" (Classification, Communication, Planning, Pattern recognition) is the note's own construction, but it is presented in bold-labeled list form with definitive language: "A Claw acts on behalf of the user." and "Concretely:". The same applies to the four action-oriented knowledge types (Preferences, Procedures, Judgment precedents, Voice and style) and the three proposed mutation types (Codify preference, Capture procedure, Consolidate precedents). None of these are flagged as proposed decompositions. This is somewhat mitigated by the `status: speculative` frontmatter, but a reader of the body text alone encounters these as established taxonomies.
  Recommendation: Add light hedging to the introductions of each taxonomy — e.g., "A Claw acts on behalf of the user. The accumulated context supports at least these modes of action:" or "An action-oriented KB would also need to store things like:". The mutation types section already uses "might also need:" which is well-calibrated; the other two lists should match that tone.

- [Proportion mismatch] The core claim is in the title: learning is broader than retrieval. The section that carries the most weight for this claim is "What changes for the learning loop" — it spells out the concrete implications. This section is well-developed (~280 words). However, "The retrieval frame isn't wrong, just partial" (~80 words) is thin relative to its structural importance: it's the note's main nuance, preventing misreading the note as a refutation of the retrieval-oriented learning loop note. It could be developed further — for example, which specific parts of the boiling cauldron analysis transfer to the action layer, and which don't?
  Recommendation: Expand the "retrieval frame isn't wrong" section with one or two more concrete statements about what transfers and what doesn't, to match its importance as the note's qualifying move.

INFO:
- [Anthropomorphic framing] The phrase "contextual competence" personifies the system mildly — "competence" implies an agent with skills rather than a system that produces appropriate outputs. This is borderline: the note is deliberately framing the Claw as an agent ("acts on behalf of the user"), so the language may be intentional. Similarly, "makes the agent's actions more competent" attributes competence to actions rather than describing output quality.

- [Source residue] The Koylanai Personal Brain OS paragraph ("voice guides and brand files for style, AGENT.md decision tables for procedures, decisions.jsonl and failures.jsonl for judgment precedents, and values/goals YAML for preferences") introduces very specific implementation details (JSONL files, YAML configs, AGENT.md) from a single external system. These specifics are framed as evidence ("Koylanai's Personal Brain OS already stores all four"), so they serve an illustrative purpose, but the density of implementation-level detail is higher than anything else in the note, which otherwise operates at a conceptual level. Worth checking whether the reader needs the file-format specifics or whether "stores all four types" would suffice.

CLEAN:
- [Source residue] The note was generalized from the KB learning loop note and the Koylanai source, but the overall vocabulary stays at the right abstraction level. Terms like "classification," "communication," "planning" are domain-neutral. No leaked domain-specific jargon from the sources.
- [Pseudo-formalism] No formal notation or mathematical apparatus present. The note argues entirely in prose and structured lists. Clean.
- [Orphan references] All specific claims are either the note's own reasoning or linked to sources. The Koylanai reference is linked. The "boiling cauldron" metaphor is attributed to the KB learning loop note. No unsourced data points or empirical claims.
- [Unbridged cross-domain evidence] The note does not cite cross-domain empirical findings. The Koylanai reference is used as an existence proof within the same domain (Claw-like systems), not a cross-domain transfer. Clean.
- [Redundant restatement] Section openings each introduce new content. "The narrow framing" sets up the problem; "What a Claw actually does" introduces the taxonomy; "What changes for the learning loop" draws implications; "The retrieval frame isn't wrong" qualifies. No section restates its predecessor's conclusion.

Overall: 2 warnings, 2 info
===
