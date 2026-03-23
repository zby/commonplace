=== PROSE REVIEW: title-as-claim-enables-traversal-as-reasoning.md ===

Checks applied: 8

WARN:
- [Source residue] The opening example uses a domain-specific claim title — "approvals guard against LLM mistakes not active attacks" — that belongs to a security/approval-system domain entirely unrelated to the note's topic (knowledge management, note titling). The example is presented in a blockquote without any framing that identifies it as an illustrative example from a different domain. A reader encountering this note for the first time may wonder what approvals and security boundaries have to do with note-taking conventions.
  Recommendation: Either replace the example with one drawn from the knowledge-management domain the note actually addresses (e.g., linking to a claim about distillation or document structure), or add a brief framing sentence before the blockquote: "For example, in an unrelated project you might write:".

- [Proportion mismatch] The core claim — that claim-titled notes enable traversal-as-reasoning — is developed across a brief opening section (~7 lines) and the "Why it works" section (~12 lines of prose plus a 3-item bullet list). The boundary analysis in "Where it breaks: multi-claim documents" is substantially longer (~20 lines of prose plus a table plus a multi-line discussion of definitional notes and the two-layer coexistence). The exception analysis receives more development than the primary mechanism. The note's title promises a positive claim ("enables traversal as reasoning"), but the longest section is about where it does not work.
  Recommendation: Develop the "Why it works" section further — the grammatical composability argument and the progressive disclosure argument each deserve more space. Consider whether the definitional-notes discussion (lines 57-61) should be extracted into its own note or at least shortened here.

INFO:
- [Source residue] The programming-language metaphor ("typed signature," "undocumented function," "return value") in the opening paragraph is internally consistent and well-developed, but it is dense. Since the note's audience is anyone working with knowledge systems (not necessarily programmers), readers without programming background may find "undocumented function" and "return value" opaque. This is borderline — the metaphor does real work, but it assumes a specific audience.

- [Confidence miscalibration] The "Prior work" section states that "Propositional titles are established practice in several fields" and lists four traditions, but the TODO at the end acknowledges "This survey is from the agent's training data, not systematic." The body text presents the survey with the confidence of established fact while the TODO caveat is easy to miss. The tension between the assertive framing and the acknowledged limitation is minor but worth noting.

- [Anthropomorphic framing] Line 36 says "agents can curate what to load based on what each note argues" — "argues" attributes intentional argumentation to a note. This is mild and arguably conventional (notes "argue" in the same way papers "argue"), but strictly speaking, notes contain arguments; they do not perform arguing. Similarly "what they argue" could be "what they contain" or "what claims they make." This is a stylistic choice, not a clear error.

CLEAN:
- [Pseudo-formalism] No formal notation or symbolic apparatus present. The table in "Where it breaks" is a classification aid, not pseudo-formalism — it organizes a taxonomy that the prose already develops. Clean.

- [Orphan references] No unsourced specific numbers, percentages, or named studies. The references to Matuschak, Luhmann, Toulmin, and arscontexta are all either linked or flagged as needing ingestion (the TODO). Clean.

- [Unbridged cross-domain evidence] The prior-work references (academic writing, journalism, Zettelkasten) are presented as analogous practices, not as direct evidence that the mechanism works in knowledge bases. The note does not claim "because journalism does X, therefore KB design should do X" — it claims these are instances of the same principle. The Toulmin model is cited as providing formal structure, with a link to the source. No unbridged transfer detected. Clean.

- [Redundant restatement] Each section opens with new content. "Why it works" does not re-explain the opening; it introduces the grammatical composability argument. "Where it breaks" does not restate "Why it works"; it immediately identifies the boundary condition. "The shadow side" adds a new epistemic point (some ideas resist single-sentence formulation). Clean.

Overall: 2 warnings, 3 info
===
