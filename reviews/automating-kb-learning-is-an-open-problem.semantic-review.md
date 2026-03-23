<!-- REVIEW-METADATA
note-path: kb/notes/automating-kb-learning-is-an-open-problem.md
last-full-review-note-sha: a8e8dbe4e2c2f9557e0656bb558ed85f999b846b
last-full-review-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-full-review-at: 2026-03-23T09:32:55+01:00
last-accepted-note-sha: a8e8dbe4e2c2f9557e0656bb558ed85f999b846b
last-accepted-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-accepted-at: 2026-03-23T09:32:55+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
=== SEMANTIC REVIEW: automating-kb-learning-is-an-open-problem.md ===

Claims identified: 15

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

---

WARN:
- [Completeness] The seven-item boiling cauldron enumeration omits **Merge** — the inverse of Split. If Split breaks a two-claim note into two notes, no listed mutation covers the reverse case where two notes making closely overlapping claims should be combined. Relink and Regroup change connections, not content. Merge would sit in the medium-scope/judgment cell alongside Synthesise but is operationally distinct: combining existing content vs producing new content from existing premises. This is a gap in the enumeration rather than an ambiguous boundary case.

- [Completeness] The boiling cauldron enumeration omits **Verify** as a mutation type — an operation that checks an existing claim against sources or evidence. The note discusses evaluation extensively in the Open Problems section but frames it as meta-level infrastructure for the loop, not as a mutation the loop would perform. Yet verification changes a note's epistemic status (speculative -> current, or flagging a note as incorrect), which is a capacity change under Simon's definition. The note's own "Retire" mutation implicitly depends on some form of verification to detect that a note "has outlived its usefulness," yet the enumeration does not surface this as a distinct operation.

- [Grounding alignment] The vocabulary gap section lists "constraining and distillation as the two mechanisms that transform accumulated knowledge." The source notes (constraining.md and constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) describe these as "the two learning mechanisms" that "trade generality for compound gains in reliability, speed, and cost." The note under review promotes them to "the two mechanisms that transform accumulated knowledge" — a broader claim. The sources frame them as mechanisms that trade generality for compound, not as the exhaustive set of transformations on accumulated knowledge. Discovery — seeing the particular as an instance of the general, which learning-is-not-only-about-generality.md describes as "the operation that produces theories" — arguably creates new knowledge rather than constraining or distilling existing knowledge. The scope upgrade from "trade generality for compound" to "transform accumulated knowledge" is the note's own move and could mislead readers into thinking the sources establish exhaustiveness.

INFO:
- [Completeness] The two-axis classification places "Retire, restructure" in the wide-scope row, but the boiling cauldron enumeration lists only seven mutations and "restructure" is not among them. It appears only in the classification as if it were an eighth mutation, without definition or example. Either the enumeration is incomplete or the classification introduces an undefined term.

- [Completeness] The codifiability axis uses a binary split (codifiable operations vs judgment operations), but several enumerated mutations occupy an intermediate zone. Reformulate (improving a title so it "works better as prose when linked") is partially codifiable — readability metrics and pattern matching can flag bad titles, but evaluating linking-context fit requires judgment. The binary framing elides this intermediate territory, though the note partly acknowledges this by noting codifiability "is itself fairly deterministic."

- [Completeness] The claim that "Automating narrow-scope improvements is relatively tractable" and "Automating wide-scope improvements is the hard part" implies the difficulty axis aligns cleanly with the generality axis. But Extract — classified as narrow-scope — can be quite hard when deciding *what* to extract requires judgment about what is worth keeping (the note itself lists "is this claim worth keeping?" as a hard problem under Open Problems). The difficulty of automation depends on oracle availability, not just scope. The note's own oracle-difficulty discussion in Open Problems implicitly acknowledges this, but the Mutations section presents the scope-difficulty alignment as cleaner than it is.

- [Grounding alignment] The note claims "When stale indexes suppress search entirely" and links to stale-indexes-are-worse-than-no-indexes.md. The source says "presence of a stale index suppresses search entirely" — accurate attribution. However, the source's argument is about agent navigation behavior (agents trust indexes as exhaustive), not about link structure underinvestment generally. The note uses it to support a broader claim about "the cost of underinvestment in link structure." Indexes are one form of link structure, so the inference is reasonable but extends the source's scope.

- [Internal consistency] The note concludes "we need more usage before we can design the learning loop properly" but the boiling cauldron section provides substantial design: seven mutations, a two-axis classification, a staging and scoring mechanism. The body acknowledges this tension with the "aspirational" label and "Each mutation would be speculative," but the concluding claim reads as stronger than what the body supports. A more precise reading is "we've designed the mutation space but can't design the evaluation function" — which the Open Problems section articulates well, but the final summary conflates the two.

- [Grounding alignment] The vocabulary gap paragraph lists seven vocabulary items (accumulation, reach, constraining, distillation, generality-vs-compound trade-off, verifiability gradient, bitter lesson boundary) and claims "without these distinctions, 'make the system learn' is a wish, not a design specification." This implies the listed terms collectively form a sufficient vocabulary for the design specification. But the note does not argue sufficiency — it does not show that these terms, taken together, cover the full design space. The claim functions more as a curated reading list than as an argued sufficiency claim.

PASS:
- [Internal consistency] The note's central argument is internally coherent: manual learning loop exists (grounded in Simon) -> automating it requires solving the oracle/evaluation problem -> we lack oracles for judgment-heavy operations -> wait for more usage data. Each section builds on the previous without contradiction.
- [Grounding alignment] The use of Simon's definition ("any change in a system that produces a more or less permanent change in its capacity for adapting to its environment") is accurately attributed. The source note (learning-is-not-only-about-generality.md) explicitly quotes Simon and uses the same definition. The note's application — "every KB improvement is learning" — follows directly.
- [Grounding alignment] The reference to the bitter lesson boundary ("spec captures the problem" vs "spec encodes a theory") accurately reflects bitter-lesson-boundary.md, which distinguishes arithmetic (spec IS the problem) from vision features (spec approximates the problem). The note's application — KB infrastructure is calculator-like, knowledge organisation is vision-feature-like — is a sound application of the framework.
- [Grounding alignment] The Pi Self-Learning reference accurately characterizes the source's oracle strategy: mistakes have a natural verifier (the fix), so the system sidesteps oracle construction. The note uses this to clarify where the hard end of the oracle spectrum is — judgment-heavy mutations that lack natural verifiers. The attribution and inference are both sound.
- [Internal consistency] The term "learning" is used consistently throughout — always in Simon's sense of capacity change. It never drifts to mean only generalization, only weight updates, or only knowledge acquisition.

Overall: 3 warnings, 5 info
===
