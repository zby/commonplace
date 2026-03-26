=== PROSE REVIEW: baseline.md ===

Checks applied: 8

WARN:
- [confidence-miscalibration] The three-way taxonomy of trace types ("Conversation transcripts," "Tool/action traces," "Reasoning traces") is the note's own analytical construction, but it is presented as a factual decomposition: "History conflates at least three trace types with different loading profiles." The "at least" hedges on completeness but not on provenance — a reader could take this as an established classification rather than a proposed one.
  Recommendation: Flag the taxonomy as the note's own construction, e.g., "We can distinguish at least three trace types..." or add a brief qualifier like "one useful decomposition."

INFO:
- [anthropomorphic-framing] "Reveals how the agent thought, not what it concluded" — "thought" implies a mental process. In context, this refers to chain-of-thought output, which is a generated text artifact, not cognition. Similarly, "Interactive sessions want continuity and visibility" attributes desire to a software abstraction.
  Recommendation: Consider "how the agent arrived at its output" or "the agent's intermediate steps" for the first case, and "Interactive sessions are designed for continuity" for the second.

- [redundant-restatement] The final paragraph of "The practical principle" ("The default mistake is to let a chat interface or framework-owned tool loop decide what the next bounded call should inherit") closely restates the opening paragraph's formulation ("The mistake is letting a session runtime decide that stored history should automatically become the next call's context"). The two preceding sentences ("Interactive sessions want continuity and visibility. Orchestration wants selective loading.") already close the note effectively. The restatement is a deliberate bookend rather than accidental repetition, but in a note of this density it reads as redundant rather than reinforcing.

CLEAN:
- [source-residue] The note claims general applicability to agent orchestration. Domain-specific systems (Slate, Spacebot) are explicitly framed as examples and tension cases, not leaked framing. The `select(K)` notation is consistently anchored to the bounded-context orchestration model defined elsewhere in the KB. No unframed domain residue detected.

- [pseudo-formalism] `select(K)`, `K`, and `P` function as cross-reference shorthand for a model defined in a linked note, not as standalone formal apparatus. Removing them would lose specificity (e.g., "storage in `K` is cheap; bounded context is expensive" would become vague). They are not used to derive consequences or make quantitative predictions, but they carry precise referential meaning. Borderline acceptable; no action needed.

- [proportion-mismatch] The core claim (session history should not be the default next context) is developed primarily in "The right split: storage vs next-context loading," which is among the longest sections. The problem-setup sections are collectively larger but serve the argument structure (establishing what goes wrong before proposing the alternative). No section dominates at the expense of the load-bearing content.

- [orphan-references] No specific numbers, percentages, named studies, or empirical claims appear without source attribution. All system-specific claims (Slate episodes, Spacebot scrubbed conclusions) link to their respective source or related-system notes.

- [unbridged-cross-domain-evidence] All cited systems (Slate, Spacebot) and referenced notes operate within the agent orchestration domain. No cross-domain transfer is attempted.

Overall: 1 warning, 2 info
===
