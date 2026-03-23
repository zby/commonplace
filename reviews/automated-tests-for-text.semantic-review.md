=== SEMANTIC REVIEW: automated-tests-for-text.md ===

Claims identified: 10

1. "Text artifacts can be tested like software if you define contracts per document type." (opening)
2. "The same test pyramid applies: cheap deterministic checks at the base, LLM-based rubric grading in the middle, cross-document corpus checks at the top." (opening)
3. "each type and trait asserts a checkable structural property — and those properties are exactly what testing contracts should verify" (para 2)
4. "The type system and the test pyramid are two sides of the same coin: types define what to check, tests do the checking." (para 2)
5. "build contracts from real failures, not from a taxonomy of possible checks" (key principle)
6. Three-level enumeration: Deterministic / LLM rubric / Corpus compatibility (bulleted list)
7. "A knowledge base is a collection of stored LLM outputs — each note is a constrained sample from a distribution." (para 4)
8. "note testing is an application of the broader artifact testing problem" (para 4)
9. "The distinction between testing the prompt ... and testing the artifact ... matters here: the pyramid above is all artifact testing." (para 4)
10. "deterministic code has no gap between instructions and output, so only output testing exists" (para 4, final sentence)

WARN:
- [Completeness] The three-level pyramid (Deterministic / LLM rubric / Corpus compatibility) is presented as a test pyramid analogy to software testing, but the analogy is structurally incomplete. A software test pyramid has unit/integration/E2E levels distinguished by scope and cost. The note's three levels mix the basis of distinction: "deterministic" is defined by check method (can it be automated without an LLM?), "LLM rubric" is defined by executor (needs an LLM), and "corpus compatibility" is defined by scope (cross-document). These are three different axes, not three levels of a single pyramid dimension. A deterministic corpus-wide check (e.g., global terminology consistency via grep) would sit at level 1 by method but level 3 by scope. The pyramid framing implies a single ordering dimension (cheap-to-expensive, narrow-to-wide) but the actual items don't consistently track one dimension.

- [Completeness] The claim "the pyramid above is all artifact testing" excludes prompt testing from the pyramid, but the note's own linked source (storing-llm-outputs-is-constraining.md) explicitly describes prompt testing and artifact testing as "complementary strategies" and says "Prompt testing tells you the distribution is worth sampling from. Artifact testing is the filter that makes a high-variance distribution usable." The note acknowledges the distinction exists but offers no pyramid-equivalent framework for prompt testing. Boundary case: a test that runs the same writing instruction 5 times and checks variance across outputs. This is prompt testing, not artifact testing, and the pyramid has no place for it. The note flags the gap but doesn't resolve it, which leaves the "test pyramid for text" incomplete as a framework — it covers only half the testing surface identified by its own linked sources.

- [Grounding] The note claims "deterministic code has no gap between instructions and output, so only output testing exists." The linked source (programming-practices-apply-to-prompting.md) says something subtly different: "In deterministic code there's no gap between what the code says and what it does, so you only test outputs." The source's claim is about the gap between specification and behavior in deterministic execution. But the note rephrases this as "instructions and output," which shifts the meaning — deterministic code does have a gap between the programmer's intent (the "instructions" in the loose sense) and what the code does; that gap is exactly what bugs are. The source's point is narrower: the code-as-specification is unambiguous, so there's no separate spec-testing concern. The note's rephrasing could mislead readers into thinking deterministic code never needs anything but output checks, which would make integration testing, contract testing, and static analysis inexplicable.

INFO:
- [Completeness] The enumeration of deterministic checks ("required sections, description present, link validity, no dangling wiki-links, length") is illustrative rather than exhaustive, which is fine for a sketch. However, boundary case: frontmatter schema validation (are tag values drawn from a controlled vocabulary? is the status field one of the allowed values?) is deterministic and structural but sits between "required sections" and "LLM rubric" — it checks semantic content (is this tag meaningful?) using deterministic means (enum membership). The list could benefit from distinguishing structural checks (section exists) from semantic-deterministic checks (field value is valid).

- [Consistency] The note says "build contracts from real failures, not from a taxonomy of possible checks" but also says "the type system and the test pyramid are two sides of the same coin: types define what to check." These two claims pull in opposite directions: the failure-driven principle says wait for breakage, but the type-system linkage says derive checks from the type definitions proactively. Both are defensible strategies, but the note doesn't acknowledge the tension or explain when each applies.

- [Grounding] The note claims "A knowledge base is a collection of stored LLM outputs." This is a strong scope claim. Human-written notes, pasted external content, and ingested sources are also KB content. The linked source (storing-llm-outputs-is-constraining.md) discusses LLM outputs specifically and doesn't claim all KB content is LLM-generated. The note may be treating "LLM output" as a superset that includes human-authored text processed through LLM-mediated workflows, but this framing is not made explicit and could confuse readers who distinguish human-authored from LLM-generated content.

- [Completeness] Boundary case for the pyramid: adversarial/red-team testing (deliberately trying to produce a note that passes all three levels but is semantically vacuous). The linked source (storing-llm-outputs-is-constraining.md) discusses exactly this under "Verbatim risk: the hardest verification failure" — output that reformats without adding insight. This failure mode sits outside all three pyramid levels as described: it passes deterministic checks, could pass LLM rubric checks (well-structured, grammatical), and might even pass corpus compatibility (no contradictions, correct terminology). The note's pyramid doesn't account for this class of failure that its own linked source identifies.

PASS:
- [Grounding] The link to document-types-should-be-verifiable.md accurately reflects that source's content. The source explicitly says "A document type should assert a structural property you can check" and gives `spec` needing Design/Implementation sections as an example. The note's claim that "each type and trait asserts a checkable structural property" faithfully represents the source's argument. The bidirectional linking is also consistent — the source links back to this note with matching semantics.

- [Grounding] The link to storing-llm-outputs-is-constraining.md correctly identifies it as the "broader artifact testing problem." That source's "Testing implications" section explicitly defines the prompt-testing vs. artifact-testing distinction that this note references, and the note accurately reports that the pyramid is "all artifact testing."

- [Grounding] The link to programming-practices-apply-to-prompting.md correctly positions this note as extending that source's testing discussion. The source explicitly says "The text testing pyramid sketches what this looks like concretely" — the two notes have a consistent mutual understanding of their relationship.

- [Consistency] The note's internal structure is coherent: it introduces the analogy (para 1), grounds it in the type system (para 2), states the design principle (para 3), enumerates the levels (list), and positions the framework within the broader testing landscape (para 4). No definition drift detected — "contract," "pyramid," and "artifact" are used consistently throughout.

- [Consistency] The compressed summary in the description field ("Text artifacts can be tested with the same pyramid as software — deterministic checks, LLM rubrics, corpus compatibility — built from real failures not taxonomy") faithfully represents the body. It captures both the pyramid structure and the failure-driven principle without eliding any tensions the body acknowledges.

Overall: 3 warnings, 4 info
===
