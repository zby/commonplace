=== PROSE REVIEW: error-messages-that-teach-are-a-constraining-technique.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note asserts "the error channel is an instruction channel" and "The distinction between 'enforcement' and 'guidance' collapses" as established facts, but these are the note's own proposed framing — not cited findings. The dual-function property and the orthogonal axis of "how much context the enforcement artifact delivers" are original constructions of this note, yet they are presented with assertive language ("The insight is that...") rather than being flagged as proposed frameworks.
  Recommendation: Hedge the note's own constructions. For example, "the error channel is an instruction channel" could become "the error channel functions as an instruction channel" or be introduced as a proposed reframing. The dual-function table is the note's own taxonomy — a phrase like "one way to see this" or "a useful decomposition" before the table would calibrate it.

- [Proportion mismatch] The core claim is in the title: teaching error messages are a constraining technique. The section that carries the most weight for this claim — "The dual-function property" — is well-developed (~200 words + table). However, "Why this works in agent systems" (~150 words) does nearly as much conceptual work (it establishes that the error channel IS an instruction channel, the foundational reason the technique works) but is thinner on evidence. The opening paragraph before any section heading does substantial load-bearing work introducing the Lopopolo example, yet it is not a section — it is framing that could be mistaken for preamble when it is actually the primary evidence presentation.
  Recommendation: Consider whether the opening paragraph's evidence deserves its own section heading (e.g., "The pattern in practice") to signal its load-bearing role. The "why this works" section could benefit from a second example beyond the null-pointer-exception analogy.

INFO:
- [Anthropomorphic framing] "the agent does not need to search for or infer the fix" and "the agent's only knowledge of what went wrong" use cognitive verbs ("search," "infer," "knowledge") for the agent. These are borderline — "search" and "infer" are reasonable descriptions of what agents procedurally do, and "knowledge" here means "information available in context." But "knowledge" in particular may suggest something deeper than context window contents, especially in a KB that has notes specifically about knowledge possession vs. activation.
  Recommendation: Worth checking whether "knowledge" should be "information" or "available context" in the sentence "The agent's only knowledge of what went wrong and how to fix it is what appears in its context window." The sentence already clarifies itself by the end, so this is minor.

CLEAN:
- [Source residue] The note claims to be about constraining techniques in agent systems generally. The primary example (linter error messages from Lopopolo's report) is explicitly framed as an example and attributed to its source. The null pointer exception comparison is clearly labeled as a contrast case ("In traditional systems..."). The table uses this KB's own methodology layers as examples, which is appropriate since the note is part of this KB. No unframed domain-specific residue found.

- [Pseudo-formalism] The note uses a table to lay out the dual-function property across gradient layers. This table adds genuine clarity — it makes the "constrain-only vs. constrain+inform" distinction concrete at each layer in a way that prose alone would not. No variables, equations, or decorative notation present.

- [Orphan references] All specific claims are either attributed (Lopopolo's report, cited with link) or are the note's own constructions. No unattributed numbers, percentages, or named studies. The "1M LOC" scale figure from Lopopolo appears only in the source ingest, not in this note, so no orphan risk.

- [Unbridged cross-domain evidence] The note stays within the agent-systems domain throughout. The one cross-domain move — comparing human developers reading error messages to agents reading error messages — is the explicit point of the "Why this works in agent systems" section, which explains the mechanism difference (humans bring external knowledge; agents only have context). This is a properly bridged comparison, not an unbridged transfer.

- [Redundant restatement] The "Connection to context efficiency" section opens with a new concept (frontloading) rather than restating prior sections. The "dual-function property" section opens by referencing the gradient but immediately introduces new content (the orthogonal axis). No section opens by re-explaining what was already established.

Overall: 2 warnings, 1 info
===
