=== PROSE REVIEW: document-classification.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note states "A document has exactly one type" as a hard rule, and describes `structured-claim` as having a "promotion path" from `note` — "when a note's argument matures enough to fill Evidence/Reasoning sections, it earns the type." The word "earns" anthropomorphizes the document and smuggles in an evaluative judgment about maturity without stating the criteria. More importantly, the promotion path framing asserts a process convention as established fact, but it is this note's own construction. No source or ADR is cited for the promotion workflow.
  Recommendation: Hedge the promotion path as a convention: "The intended promotion path is `note` -> `structured-claim`" and replace "earns" with a neutral verb like "receives" or "is assigned."

INFO:
- [Proportion mismatch] The core claim of the note is the classification taxonomy itself (the base types table), which gets adequate treatment. However, `structured-claim` receives a full dedicated paragraph of explanation below the table while all other types (including `spec`, `review`, `adr`) get only their table-row descriptions. If `structured-claim` warrants expanded explanation, the other non-trivial types may too — or the `structured-claim` paragraph could be moved to its own type file, which already exists at `types/structured-claim.md` (linked from the table).
- [Source residue] The migration table references old type names (`design`, `insight`, `analysis`, `research`, `comparison`) without context about where these old types came from or when they were in use. A reader encountering this note fresh has no frame for why this migration section exists. This is mild — the section is clearly labeled "Migration" — but the old names are residue from an earlier internal state of this KB that is not explained.

CLEAN:
- [Pseudo-formalism] No formal notation is used. The tables are plain reference tables, not decorative formalism. Clean.
- [Orphan references] No specific figures, data points, or empirical claims appear. All references are to other notes in the KB, which are linked. Clean.
- [Unbridged cross-domain evidence] The note does not cite evidence from external domains. It is an internal specification. Clean.
- [Redundant restatement] The note is compact. No section re-explains what a prior section established. The opening sentence references two other notes for rationale and details, then proceeds directly to new content. Clean.
- [Anthropomorphic framing] The word "earns" (noted under Confidence miscalibration) has a mild anthropomorphic quality, but the note is about documents and type systems, not models. No model-directed anthropomorphism is present. Clean.

Overall: 1 warning, 2 info
===
