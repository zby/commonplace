=== PROSE REVIEW: llm-learning-phases-fall-between-human-learning-modes.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The "Deploy-time learning as a further intermediate" section presents the cultural evolution analogy as descriptive fact: "It resembles cultural evolution — knowledge accumulated in books, tools, and institutions rather than in individual minds — more than it resembles individual human learning." This is the note's own analogy (not Amodei's), but it's stated with the same assertive confidence as the Amodei-sourced framing. The cultural evolution parallel is suggestive but unargued — what shared mechanism makes deploy-time learning more like cultural evolution than like, say, an engineer's reference shelf?
  Recommendation: Hedge the cultural evolution claim ("One way to read this is as resembling cultural evolution...") or add a sentence identifying the shared mechanism that justifies the analogy.

- [Proportion mismatch] The core claim is that LLM phases fall *between* human modes rather than mapping onto them. The section that carries the most weight for this claim is "Why the non-mapping matters" — it explains the consequences and gives the three specific ways the 1:1 mapping fails. Yet this section is roughly comparable in length to the two setup sections ("Why pre-training is between evolution and learning" and "Why in-context learning is between long-term and short-term") which establish the spectrum positions. The "Deploy-time learning" section, which extends the claim to a KB-specific framework, gets thinner treatment than either setup section despite being the note's original contribution beyond Amodei. The Amodei-sourced material (the two "Why..." sections) is well-developed, while the note's own extension (deploy-time learning as cultural evolution analogue) is underdeveloped.
  Recommendation: Develop the deploy-time learning section to match the depth of the pre-training and in-context sections — it's where the note goes beyond its source and should carry proportional weight.

INFO:
- [Unbridged cross-domain evidence] The note's entire structure is a cross-domain comparison (human cognition vs. LLM behavior), so bridging is inherently its subject matter. The bridges are generally present — e.g., "Pre-training must do double duty: it acquires both the kinds of structural priors that evolution gives humans... *and* the kinds of world knowledge that humans acquire through experience." However, point 2 in "Why the non-mapping matters" makes a claim about human short-term memory mechanics: "Human short-term memory mostly *retrieves* from long-term stores. LLM in-context 'learning' is doing something different — it's conditioning the model's entire distribution, not accessing a separate store." The claim about human short-term memory being primarily retrieval is a specific cognitive science position (not universally held — some models emphasize active maintenance and transformation), presented without qualification or source.
  Recommendation: Either soften "mostly *retrieves*" to acknowledge it's one model of working memory, or cite the retrieval-based framing (e.g., Cowan's embedded-processes model vs. Baddeley's active workspace).

- [Anthropomorphic framing] The note uses "cognitive architecture" to describe what pre-training builds: "it shapes the basic cognitive architecture, not just the knowledge available to an already-formed mind." This is borderline — the note is explicitly comparing human and LLM learning, so "cognitive architecture" may be deliberate metaphor rather than unintentional anthropomorphism. Still, "computational architecture" or "processing architecture" would be more precise for the LLM side, since "cognitive" carries implications about the nature of the processing that the note doesn't intend to assert.
  Recommendation: Consider whether "cognitive architecture" is doing deliberate analogical work here or whether "computational architecture" would be more precise without losing the comparison.

CLEAN:
- [Source residue] The note is built from the Amodei interview but handles its source cleanly. The Amodei quote is explicitly attributed with a link, and the rest of the note develops the framework in domain-neutral terms about learning mechanisms. No interview-specific framing (podcast context, conversational artifacts, Amodei-specific vocabulary) leaked into the analytical sections.

- [Pseudo-formalism] No formal notation, variables, or mathematical apparatus present. The note argues entirely in prose, which is appropriate for the kind of comparative-framework claim it makes.

- [Orphan references] All specific claims are either sourced or clearly marked as the note's own reasoning. The Amodei quote has a link. The KB's three-timescale framework links to its note. The Tulving taxonomy links to its note. The open questions section speculates but doesn't smuggle in unsourced specifics — the OpenClaw-RL reference has a link to its ingest. No orphan data points or uncited empirical claims found.

- [Redundant restatement] Each section opens with new material rather than restating the prior section's conclusion. The "Why in-context learning..." section opens by defining human long-term learning properties, not by recapping the pre-training conclusion. "Why the non-mapping matters" opens with the temptation of 1:1 mappings, not by summarizing the two intermediate positions. The sections read as independently entered, which is appropriate for the parallel structure.

Overall: 2 warnings, 2 info
===
