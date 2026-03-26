<!-- REVIEW-METADATA
note-path: kb/notes/automating-kb-learning-is-an-open-problem.md
last-full-review-note-sha: ac4409d7b7506a4366cdfb6ad2de20786e3cbb9f
last-full-review-note-commit: d1d69393d519758d93ae3c6987b3fc2350077c45
last-full-review-at: 2026-03-24T12:00:00+01:00
last-accepted-note-sha: ac4409d7b7506a4366cdfb6ad2de20786e3cbb9f
last-accepted-note-commit: d1d69393d519758d93ae3c6987b3fc2350077c45
last-accepted-at: 2026-03-24T12:00:00+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
=== SEMANTIC REVIEW: automating-kb-learning-is-an-open-problem.md ===

Claims identified: 16

1. "Every session that improves notes, sharpens connections, or discovers principles is learning in Simon's sense: a change that increases the system's adaptive capacity" (intro)
2. "The open problem is not 'the KB needs a learning loop' but automating the judgment-heavy parts of the loop we already run manually" (intro)
3. "A knowledge base exists to answer questions about the project" (What is a KB for?)
4. "New knowledge ... is valuable only insofar as it improves future question-answering" (What is a KB for?)
5. "A KB's knowledge is in the content of its notes and in the structure of its links — neither alone is sufficient" (Knowledge lives in both notes and links)
6. "the link structure is where the most untapped value sits, because it's where understanding is encoded" (Knowledge lives in both notes and links)
7. Seven-item enumeration of boiling cauldron mutations: Extract, Split, Synthesise, Relink, Reformulate, Regroup, Retire (The boiling cauldron)
8. "Mutations differ on two axes" — generality and codifiability (Mutations differ on two axes)
9. Two-axis classification: generality (narrow/medium/wide) and codifiability (codifiable/judgment) (Mutations differ on two axes)
10. "constraining and distillation as the two mechanisms that transform accumulated knowledge" (The vocabulary gap)
11. "Automating narrow-scope improvements is relatively tractable ... Automating wide-scope improvements is the hard part" (Mutations differ on two axes)
12. "we need more usage before we can design the learning loop properly" (Open problems conclusion)
13. "The KB's infrastructure ... is calculator-like. The knowledge organisation ... is vision-feature-like." (Connection to codification)
14. Accumulation is "the basic learning operation" with reach as "its key property" (The vocabulary gap)
15. "not in the learning mechanism (scoring, ranking, injection are all straightforward) but in manufacturing evaluation for judgment-heavy mutations" (Oracle difficulty varies by learning type)
16. "Codifiability is a separate axis — often tractable regardless of scope, because the question 'can this be made deterministic?' is itself fairly deterministic" (Mutations differ on two axes)

---

WARN:
- [Completeness] The seven-item boiling cauldron enumeration omits **Merge** — the inverse of Split. If Split breaks a two-claim note into two notes, no listed mutation covers the reverse case where two closely overlapping notes should be combined into one. Relink and Regroup change connections, not content. Merge would sit in the medium-scope/judgment cell alongside Synthesise but is operationally distinct: combining existing content into a single note vs producing new content that neither source note contains. This is a gap in the enumeration, not an ambiguous boundary.

- [Completeness] The boiling cauldron enumeration omits **Verify** as a mutation type. The Open Problems section discusses evaluation extensively but frames it as meta-level infrastructure for the loop, not as a mutation the loop would perform. Yet verification changes a note's epistemic status (speculative -> current, or flagging a note as incorrect), which qualifies as a capacity change under Simon's definition. The note's own "Retire" mutation implicitly depends on some verification to determine that a note "has outlived its usefulness," but the enumeration does not surface verification as a distinct operation.

- [Grounding alignment] The vocabulary gap section lists "constraining and distillation as the two mechanisms that transform accumulated knowledge." The source notes (constraining.md, constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) describe these as "two co-equal learning mechanisms" that "trade generality for compound gains in reliability, speed, and cost." The note promotes them to "the two mechanisms that transform accumulated knowledge" — a broader claim that implies exhaustiveness over all knowledge transformation. The sources frame constraining and distillation as mechanisms that trade generality for compound, not as the complete set of transformations on accumulated knowledge. Discovery — described in learning-is-not-only-about-generality.md as "the operation that produces theories" by seeing the particular as an instance of the general — arguably creates new knowledge rather than constraining or distilling existing knowledge, and is not clearly reducible to either mechanism. The scope upgrade from "trade generality for compound" to "transform accumulated knowledge" is the note's own move and could mislead readers into thinking the sources establish exhaustiveness.

INFO:
- [Completeness] The two-axis classification places "Retire, restructure" in the wide-scope row, but the boiling cauldron enumeration lists only seven mutations and "restructure" is not among them. It appears only in the classification table as if it were an eighth mutation, without definition or example. Either the enumeration is incomplete (should list restructure) or the classification introduces an undefined term that should be removed or explained.

- [Completeness] The codifiability axis uses a binary split (codifiable operations vs judgment operations), but several enumerated mutations occupy intermediate ground. Reformulate ("improve a title so it works better as prose when linked") is partially codifiable — readability heuristics and pattern matching can flag bad titles, but evaluating whether a title works well in link context requires judgment. Extract similarly ranges from codifiable (pull a direct quote) to judgment-heavy (decide what is worth extracting). The binary framing elides this intermediate territory. The note partly acknowledges the issue by asserting codifiability "is itself fairly deterministic," but that meta-claim is itself undefended.

- [Completeness] The claim that "automating narrow-scope improvements is relatively tractable" and "automating wide-scope improvements is the hard part" implies the difficulty axis aligns cleanly with the generality axis. But Extract — classified as narrow-scope — includes the judgment-heavy decision of *what* to extract, which the note's own Open Problems section lists as hard ("is this claim worth keeping?"). The difficulty of automation depends on oracle availability, not just scope. The note's oracle-difficulty discussion in Open Problems implicitly acknowledges this tension, but the Mutations section presents the scope-difficulty alignment as cleaner than it is.

- [Grounding alignment] The note claims "When stale indexes suppress search entirely" and links to stale-indexes-are-worse-than-no-indexes.md. The source says "presence of a stale index suppresses search entirely" — accurate attribution of the mechanism. However, the source's argument concerns agent navigation behavior specifically (agents trust indexes as exhaustive and stop searching), not link-structure underinvestment in general. The note uses the reference to support the broader claim about "the cost of underinvestment in link structure." Indexes are one form of link structure, so the inference is reasonable but extends the source's narrower scope.

- [Internal consistency] The note concludes "we need more usage before we can design the learning loop properly," but the boiling cauldron section provides substantial design: seven mutations, a two-axis classification, a staging and scoring mechanism. The body mitigates this tension with the "aspirational" label and "each mutation would be speculative," but the concluding claim reads as stronger than what the body supports. A more precise reading is "we've designed the mutation space but cannot yet design the evaluation function" — which the Open Problems section articulates well, but the final summary conflates design-of-mutations (already done) with design-of-evaluation (still blocked on usage).

- [Grounding alignment] The vocabulary gap paragraph lists seven vocabulary items (accumulation, reach, constraining, distillation, generality-vs-compound trade-off, verifiability gradient, bitter lesson boundary) and claims "without these distinctions, 'make the system learn' is a wish, not a design specification." This implies these terms collectively form a sufficient vocabulary for the design specification. But the note does not argue sufficiency — it does not show that these terms, taken together, cover the full design space. The claim functions more as a curated reading list than as an argued sufficiency claim. In particular, the note's own discussion of oracle difficulty (a central concept in the Open Problems section) is not represented in the vocabulary list.

- [Completeness] The "What is a KB for?" section defines KB value exclusively through question-answering: "a note is valuable if it helps answer a question." This is a strong scope claim. A boundary case: a note that serves as a generative prompt — something an agent reads not to answer a known question but to discover a question worth asking. The note's own "Synthesise" mutation ("two notes that together imply something neither says alone") presupposes this kind of generative use. If a note's value is strictly question-answering, the value of a note that enables synthesis is indirect at best and the note needs to account for that indirection. This is a tension rather than a contradiction — question-answering could be defined broadly enough to include "answering a question I didn't know I had" — but the note doesn't address it.

PASS:
- [Internal consistency] The note's central argument is internally coherent: manual learning loop exists (grounded in Simon) -> automating it requires solving the oracle/evaluation problem -> we lack oracles for judgment-heavy operations -> wait for more usage data. Each section builds on the previous without contradiction.
- [Grounding alignment] The use of Simon's definition ("any change in a system that produces a more or less permanent change in its capacity for adapting to its environment") is accurately attributed. The source note (learning-is-not-only-about-generality.md) explicitly quotes Simon and uses the same definition. The note's application — "every KB improvement is learning" — follows directly from the definition.
- [Grounding alignment] The reference to the bitter lesson boundary ("spec captures the problem" vs "spec encodes a theory") accurately reflects bitter-lesson-boundary.md, which distinguishes arithmetic (spec IS the problem) from vision features (spec approximates the problem). The note's application — KB infrastructure is calculator-like, knowledge organisation is vision-feature-like — is a sound application of the framework.
- [Grounding alignment] The Pi Self-Learning reference accurately characterizes the source's oracle strategy: mistakes have a natural verifier (the fix), so the system sidesteps oracle construction. The note uses this to clarify where the hard end of the oracle spectrum is — judgment-heavy mutations that lack natural verifiers. The attribution and inference are both sound.
- [Grounding alignment] The reference to constraining-during-deployment-is-continuous-learning.md is accurate. That source says constraining is "one concrete way continuous learning happens outside weights" and describes the same informal accumulation pattern (Claude memory files, Cursor rules, AGENTS.md conventions) the note references. The note's claim that "none of it is systematic" faithfully represents the source's distinction between existing practice and systematised learning.
- [Internal consistency] The term "learning" is used consistently throughout — always in Simon's sense of capacity change. It never drifts to mean only generalization, only weight updates, or only knowledge acquisition. The opening explicitly sets the definition and every subsequent section adheres to it.

Overall: 3 warnings, 7 info
===
