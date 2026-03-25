<!-- REVIEW-METADATA
note-path: kb/notes/session-history-should-not-be-the-default-next-context.md
last-full-review-note-sha: 067602599acc8adf7bc2b738136fd767979d6128
last-full-review-note-commit: d9c1119508d1d0f3ff87123fd53f189924e4f068
last-full-review-at: 2026-03-25T21:58:41+01:00
last-accepted-note-sha: 067602599acc8adf7bc2b738136fd767979d6128
last-accepted-note-commit: d9c1119508d1d0f3ff87123fd53f189924e4f068
last-accepted-at: 2026-03-25T21:58:41+01:00
last-acceptance-kind: full-review
review-type: prose-review
-->
=== PROSE REVIEW: session-history-should-not-be-the-default-next-context.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The "practical principle" section uses imperative framing ("Store more than you load," "Use trace-preserving storage early," "Move toward artifact-first loading") that reads as settled design advice rather than proposed heuristics. The note's own status is seedling and these principles are the author's construction, not cited from an established source. The hedge "For most orchestration" partially mitigates but the bullet points themselves assert without qualification.
  Recommendation: Frame as proposed guidance -- e.g., "A reasonable starting position:" or "Principles that follow from this analysis:" -- to match the seedling epistemic status.

INFO:
- [Redundant restatement] The opening of "Execution-boundary compression is a recurring design move" -- "Across several systems, the shared move is compression at the execution boundary" -- restates what the preceding section's final paragraph already concluded ("The next bounded call should see a representation chosen for its task, not the raw record of how the previous call got there"). This is mild; it functions as a one-sentence transition rather than a full restating paragraph, but the overlap is present.
- [Proportion mismatch] The "Execution-boundary compression" section is primarily a catalog of examples pointing outward to other notes (Spacebot, Slate, conversation-vs-refinement, ad-hoc prompts). It does useful corroborating work but the linking nature means its contribution is more navigational than argumentative. Not a significant imbalance -- the core-claim sections (intro, "Why transcript inheritance breaks down," and "The practical principle") carry appropriate weight -- but this section could be tightened if the note grows further.

CLEAN:
- [Source residue] The note references Slate and Spacebot as exemplifying systems, both properly framed as examples from the agent-systems domain. The term "cognitive budget" in "Why transcript inheritance breaks down" is a metaphorical import from cognitive science, but it is broadly understood by the target audience and not residue from a narrower source domain. No leaked domain-specific framing found.
- [Pseudo-formalism] The note uses `K` and `select(K)` from the bounded-context orchestration model note. These are not introduced here as new formalism -- they reference established vocabulary from a linked foundation note. `select(K)` compactly names the control point that distinguishes deliberate loading from automatic inheritance. No decorative notation found.
- [Orphan references] No unattributed specific numbers, percentages, or named studies. Empirical claims are tied to named systems (Slate, Spacebot) with links to source material. The "Random Labs' Slate" reference includes its source link.
- [Unbridged cross-domain evidence] The note stays within agent orchestration and LLM system design throughout. Slate and Spacebot are same-domain references. No human-cognition findings are cited as if they directly apply to LLMs without bridging.
- [Anthropomorphic framing] The note consistently uses mechanistic language: "stores," "loads," "inherits," "surfaces," "assembles." The phrase "the model must re-interpret prior interaction" attributes interpretive agency, but this is standard usage in the LLM literature and reasonably precise for the intended meaning. No problematic anthropomorphic verbs ("knows," "understands," "believes") found.

Overall: 1 warning, 2 info
===
