=== PROSE REVIEW: automating-kb-learning-is-an-open-problem.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The "What is a KB for?" section asserts "A knowledge base exists to answer questions about the project" as settled fact, then builds the entire evaluation framework on this single function. This is a design choice, not a discovered truth — a KB could also exist to surface connections the user hasn't thought to ask about, or to preserve institutional memory that doesn't map to questions. The note's own "Synthesise" mutation ("two notes that together imply something neither says alone") is arguably not question-answering at all. The status frontmatter says "speculative," but this foundational framing reads as axiomatic.
  Recommendation: Hedge the opening claim — "In this KB, we treat question-answering as the primary value function" or similar — so the downstream evaluation discussion inherits the right epistemic status.

- [Proportion mismatch] The title claim is that automating KB learning is an open problem. The section that most directly addresses why it's open — "Open problems" — is roughly comparable in length to "The boiling cauldron (aspirational)" and "Mutations differ on two axes," which describe an aspirational solution rather than the problem itself. The "Vocabulary gap" section, which argues that the conceptual language for the problem doesn't exist yet, is compressed into a single dense paragraph despite being arguably the most novel claim in the note.
  Recommendation: The vocabulary gap paragraph carries enough distinct ideas (accumulation, reach, constraining, distillation, the compound trade-off, the verifiability gradient, the bitter lesson boundary) to warrant its own properly developed section. Currently it reads as a list of links rather than an argument for why the gap matters.

- [Proportion mismatch] The "Connection to codification" section (4 sentences) is thin relative to the weight of the claim it makes — that the calculator/vision-feature distinction tells us where a learning loop would operate. This is a significant structural claim about the design space, but it reads as an afterthought appendix.
  Recommendation: Either develop the section enough to show why the distinction is load-bearing for the note's argument, or absorb its content into the "Mutations differ on two axes" section where codifiability is already discussed.

INFO:
- [Source residue] The metaphor "boiling cauldron" is vivid but its origin is unexplained. It could be residue from a specific source or conversation. The note doesn't attribute it or explain why this metaphor was chosen over alternatives. This isn't clearly a problem — it works as a memorable label — but a reader encountering it for the first time gets no help understanding why "boiling" is the right image for what's described (continuous, speculative, background mutation proposals).

- [Redundant restatement] The "Connection to codification" section partially restates the codifiability axis already introduced in "Mutations differ on two axes" ("Codifiable operations... already automatable as scripts" vs. "The KB's infrastructure — file formats, frontmatter schema, sync scripts — is calculator-like"). The two sections make the same point through different lenses (codifiability axis vs. bitter lesson boundary) but the overlap isn't acknowledged.

- [Confidence miscalibration] The sentence "Codifiability is a separate axis — often tractable regardless of scope, because the question 'can this be made deterministic?' is itself fairly deterministic" asserts a meta-claim (that codifiability assessment is itself codifiable) without hedging. This is a neat observation but it's the note's own construction and reads as established fact rather than a proposed heuristic.
  Recommendation: Minor — consider "tends to be" or "in our experience" rather than the bare assertion.

CLEAN:
- [Source residue] The note operates at its claimed generality level (KB automation) consistently. Domain-specific examples (PageRank, betweenness centrality, DSPy, ProTeGi, Pi Self-Learning) are all appropriately framed as references or comparisons rather than assumed context. The arscontexta reference in the "Retire" bullet is explicitly attributed.

- [Pseudo-formalism] No formal notation is used. The "two axes" decomposition in "Mutations differ on two axes" uses prose categories rather than pretending to be a formal taxonomy. The by-generality and by-codifiability breakdowns are labeled as organizational frames, not formal dimensions.

- [Orphan references] Specific claims and systems are consistently linked to their source notes. The Pi Self-Learning reference, the arscontexta methodology, the adaptation taxonomy — all are linked. No floating empirical claims without attribution.

- [Unbridged cross-domain evidence] The note's evidence stays within its domain (KB systems, agent memory, learning theory). The Simon reference is bridged through the opening paragraph's application to KB improvement. The Pi Self-Learning comparison explicitly explains why the analogy holds (oracle difficulty spectrum) and where it breaks down.

- [Anthropomorphic framing] The note consistently uses system-level language ("the KB learns," "the system's adaptive capacity") rather than attributing cognitive states to models. "The agent proposing mutations" is appropriately agentive for describing what an agent does.

Overall: 3 warnings, 3 info
===
