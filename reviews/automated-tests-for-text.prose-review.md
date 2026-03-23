=== PROSE REVIEW: automated-tests-for-text.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] "The same test pyramid applies" — this asserts an established equivalence between software test pyramids and text testing, but the note's own final line acknowledges "We haven't built any of this yet." The test pyramid for text is a proposed analogy, not a validated structure. The opening sentence presents it as settled ("applies"), and the three-level breakdown ("deterministic checks at the base, LLM-based rubric grading in the middle, cross-document corpus checks at the top") reads as an established architecture rather than a hypothesis. The hedge only arrives in the last paragraph, after the reader has already absorbed the framework as fact.
  Recommendation: Flag the pyramid as proposed from the start. Something like "A plausible layering mirrors the software test pyramid" instead of "The same test pyramid applies." The closing "We haven't built any of this yet" then reinforces rather than contradicts the opening framing.

- [Proportion mismatch] The core claim is that text can be tested like software using a pyramid of checks. The note's most important idea — what each level actually does and how they compose — gets a single bullet list with one-line descriptions per level. Meanwhile, the paragraph on prompt-vs-artifact testing and the doubled testing surface gets substantially more development (the entire second half of the note). The pyramid itself, which is what other notes cite this note for (both `document-types-should-be-verifiable.md` and `programming-practices-apply-to-prompting.md` reference "the text testing pyramid"), is underdeveloped relative to the secondary testing-surface argument.
  Recommendation: Either develop the pyramid levels with more specificity (what kinds of deterministic checks? what rubric dimensions? what corpus checks?) or split the prompt-vs-artifact discussion into its own note. Currently, the note that other notes point to for "the testing pyramid" gives that pyramid only a bullet list.

INFO:
- [Source residue] The note's title and opening claim generality over "text artifacts," but the body vocabulary drifts toward this specific knowledge base: "required sections, description present, link validity, no dangling wiki-links" are all properties of this KB's note format, not of text artifacts in general. "Contradiction check against existing notes, terminology alignment" similarly assumes a KB corpus. The note could be about testing text artifacts broadly, but the examples are all about testing notes in this particular system. This may be intentional — the note lives in a KB about KB methodology — but a reader coming from the title "Automated tests for text" might expect broader applicability than the examples deliver.

- [Unbridged cross-domain evidence] "Same way you build a test suite — add a test when something breaks, not before" draws on test-driven development's "red-green-refactor" / failure-first convention from software engineering. The note presents this as directly transferable without explaining why the same strategy works for text quality checks. In software, a failing test has a clear signal (assertion failure); for text, "something breaks" is ambiguous — how do you detect a quality failure in a note without the check already existing? The analogy may hold, but the bridge is missing.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus in the note. The three-level pyramid is presented as a prose list. No decorative formalism.

- [Orphan references] No specific figures, percentages, named studies, or empirical claims appear without context. The note is entirely framework-level with no unsupported data points.

- [Redundant restatement] The note is short (five paragraphs) and each paragraph advances a distinct point: the claim, the type-system connection, the build-from-failures principle, the pyramid levels, the prompt-vs-artifact distinction, and the "haven't built this" closer. No section restates a prior section's conclusion.

- [Anthropomorphic framing] No language attributing human-like properties to models. The note discusses testing infrastructure, not model cognition.

Overall: 2 warnings, 2 info
===
