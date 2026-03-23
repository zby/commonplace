=== SEMANTIC REVIEW: automating-kb-learning-is-an-open-problem.md ===

Claims identified: 14

1. "Every session that improves notes, sharpens connections, or discovers principles is learning in Simon's sense" (intro)
2. "The open problem is not 'the KB needs a learning loop' but automating the judgment-heavy parts" (intro)
3. "A knowledge base exists to answer questions about the project" (What is a KB for?)
4. "A KB's knowledge is in the content of its notes and in the structure of its links — neither alone is sufficient" (Knowledge lives in both notes and links)
5. "the link structure is where the most untapped value sits" (Knowledge lives in both notes and links)
6. Seven-item enumeration of boiling cauldron mutations: Extract, Split, Synthesise, Relink, Reformulate, Regroup, Retire (The boiling cauldron)
7. "Mutations differ on two axes" — generality and codifiability (Mutations differ on two axes)
8. Two-axis classification: generality (narrow/medium/wide) and codifiability (codifiable/judgment) (Mutations differ on two axes)
9. "constraining and distillation as the two mechanisms that transform accumulated knowledge" (The vocabulary gap)
10. "we need more usage before we can design the learning loop properly" (Open problems conclusion)
11. "The KB's infrastructure ... is calculator-like. The knowledge organisation ... is vision-feature-like." (Connection to codification)
12. Accumulation is "the basic learning operation" with reach as "its key property" (The vocabulary gap)
13. "not in the learning mechanism (scoring, ranking, injection are all straightforward) but in manufacturing evaluation for judgment-heavy mutations" (Oracle difficulty varies by learning type)
14. "none of it is systematic" — referring to constraining during deployment (The vocabulary gap)

---

WARN:
- [Completeness] The boiling cauldron enumeration of seven mutations omits **Merge** — the inverse of Split. If Split breaks a two-claim note into two notes, the note offers no mutation for the reverse case where two notes making closely overlapping claims should become one. Relink and Regroup don't cover this because they change connections, not content. The note later claims mutations "differ on two axes" and classifies all seven; a Merge mutation would sit in the medium-scope/judgment cell alongside Synthesise but is operationally distinct (combining existing content vs producing new content from existing premises). This is a gap in the enumeration, not merely an ambiguous boundary.

- [Completeness] The boiling cauldron enumeration omits **Verify/Validate** as a mutation type — an operation that takes an existing claim and checks it against sources or evidence. The note discusses evaluation extensively in the Open Problems section but frames it as meta-level infrastructure for the loop, not as a mutation the loop would perform. Yet verification changes a note's epistemic status (speculative -> current, or flagging a note as incorrect), which is a capacity change. The note's own framework (Simon's definition) would classify this as learning, and the note's own "Retire" mutation implicitly requires some verification to detect that a note "has outlived its usefulness."

- [Grounding alignment] The vocabulary gap section lists "constraining and distillation as the two mechanisms that transform accumulated knowledge." The source note (constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) describes these as "the two learning mechanisms" that both "trade generality for compound gains." However, the source note's framing is specifically about mechanisms that trade generality for the reliability/speed/cost compound. The note under review promotes them to "the two mechanisms that transform accumulated knowledge" — a broader claim. Accumulation can also be transformed by operations that don't clearly fit either mechanism: discovery (seeing the particular as an instance of the general, per learning-is-not-only-about-generality.md) arguably creates new knowledge rather than constraining or distilling existing knowledge. The scope upgrade from "trade generality for compound" to "transform accumulated knowledge" is the note's own move and could mislead readers into thinking the sources establish the exhaustiveness of the two-mechanism framework.

INFO:
- [Completeness] The two-axis classification places "Retire, restructure" in the wide-scope row, but the enumeration only lists seven mutations and "restructure" is not among them. "Restructure" appears only in the classification table as if it were an eighth mutation, without definition. This is an ambiguity — either the enumeration is missing an item, or the classification introduces a term that doesn't correspond to a defined mutation.

- [Completeness] The codifiability axis uses a binary split (codifiable operations vs judgment operations), but several of the enumerated mutations sit in an intermediate zone. Reformulate (improving a title) is partially codifiable — readability metrics can flag bad titles, but deciding whether a title "works better as prose when linked" requires judgment about the linking context. The binary framing elides this intermediate territory.

- [Grounding alignment] The note claims "When stale indexes suppress search entirely" and links to stale-indexes-are-worse-than-no-indexes.md. The source says "presence of a stale index suppresses search entirely" — accurate attribution. However, the source's argument is about agent navigation behavior (agents trust indexes as exhaustive), while the note uses it to support a claim about "the cost of underinvestment in link structure." The source is about index staleness specifically, not link structure underinvestment generally. Indexes are one form of link structure, so the inference is reasonable but extends the source's narrower claim.

- [Internal consistency] The note concludes "we need more usage before we can design the learning loop properly" but the boiling cauldron section provides a fairly detailed design of the learning loop (seven mutations, two-axis classification, staging and scoring). The body acknowledges this tension ("aspirational" label, "Each mutation would be speculative"), but the concluding claim that we can't design the loop yet is somewhat at odds with the level of design detail already present. The note could be read as saying "we've designed the mutation space but can't design the evaluation function" — which is more precise than the summary claim.

- [Grounding alignment] The vocabulary gap section is a dense paragraph listing six vocabulary items (accumulation, reach, constraining, distillation, generality-vs-compound trade-off, verifiability gradient, bitter lesson boundary — actually seven), each linked to a source note. The claim that "without these distinctions, 'make the system learn' is a wish, not a design specification" implies these terms collectively form a sufficient vocabulary. But the note doesn't argue why this particular set is sufficient or whether other terms are needed. This is presented as a claim but functions more as a curated list.

PASS:
- [Internal consistency] The note's central argument is internally coherent: manual learning loop exists (grounded in Simon) -> automating it requires solving the oracle/evaluation problem -> we lack the oracles for judgment-heavy operations -> wait for more usage data. Each section builds on the previous one without contradiction.
- [Grounding alignment] The use of Simon's definition ("any change in a system that produces a more or less permanent change in its capacity for adapting to its environment") is accurately attributed and correctly applied. The source note (learning-is-not-only-about-generality.md) explicitly quotes Simon and uses the same definition.
- [Grounding alignment] The reference to the bitter lesson boundary ("spec captures the problem" vs "spec encodes a theory") accurately reflects the source note (bitter-lesson-boundary.md), which distinguishes arithmetic (spec IS the problem) from vision features (spec approximates the problem). The note's application — KB infrastructure is calculator-like, knowledge organisation is vision-feature-like — is a reasonable application of the framework.
- [Grounding alignment] The connection to the-boundary-of-automation-is-the-boundary-of-verification.md is bidirectionally consistent. That note explicitly says "KB curation stalls at the same boundary — judgment-heavy mutations lack oracles," which matches this note's framing.
- [Internal consistency] The term "learning" is used consistently throughout — always in Simon's sense of capacity change, never drifting to mean only generalization or only weight updates.

Overall: 3 warnings, 4 info
===
