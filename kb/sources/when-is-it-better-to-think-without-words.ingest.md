---
description: "Karlsson decomposes human thinking into wordless exploration and written testing, stabilization, and relay, while leaving the neuroscience and LLM analogy speculative"
source: https://www.henrikkarlsson.xyz/p/wordless-thought
captured: "2026-08-10"
capture: web-fetch
genre: conceptual-essay
snapshot_sha256: b4a7b5f52254c05a62811b8e3c1e84bdbf491d1e0c0e00ba05aa7bce5c0e20b7
ingested: "2026-08-10"
type: kb/sources/types/ingest-report.md
domains: [writing-as-thinking, epistemic-writing, cognitive-offloading, human-agent-transfer]
---

# Ingest: When is it better to think without words?

## Classification

A synthesis of historical testimony, cited research, analogy, and first-person reflection that proposes a model of human thought rather than testing one.
Author: Henrik Karlsson is an independent essayist reflecting on sustained writing practice and his reading of Jacques Hadamard. He repeatedly marks the neuroscience as speculation and does not claim research authority for either human cognition or LLM internals.

## Summary

Karlsson presents this essay as a complement to [How to think in writing](https://www.henrikkarlsson.xyz/p/writing-to-think). Drawing on Hadamard's reports of mathematicians who worked without clear words, images, or equations, he proposes that expert wordless thought can search a rich conceptual space faster and more broadly than sequential language, but with more unnoticed error. Writing then performs different functions: it forces intuition through explicit logic, stabilizes results enough to test them, and creates “relay results” that can be offloaded from working memory and reused in longer reasoning chains. Precision can also arrive too early, however, filling genuine uncertainty with plausible guesses and making them look settled. The resulting account is an alternation between exploratory vagueness and textual stabilization, not a claim that either words or wordlessness should dominate all thought.

## Quotes

No source quotes have been retained yet.

## Connections Found

The essay is the explicit counterweight to Karlsson's earlier [writing procedure](https://www.henrikkarlsson.xyz/p/writing-to-think): it retains writing as a test surface but moves exploratory search partly outside language. It also qualifies [Graham's stronger verbal-formation claim](https://paulgraham.com/words.html), which it quotes, by distinguishing an intuition's generation from its later validation and use as a stable building block. Its warning that prose can impose false precision compares with [progressive constraining](../notes/progressive-constraining-commits-only-after-patterns-stabilize.md): both delay commitment until a pattern is ready to stabilize, though one concerns human cognition and the other LLM-generated code. For agent-operated systems, the transferable value is functional rather than architectural, as [human analogies can motivate functions without determining component boundaries](../notes/human-analogies-suggest-functions-not-component-boundaries.md). The [J-space experiments](verbalizable-representations-global-workspace-llms.ingest.md) provide the closest empirical model-side comparison: externalized chain-of-thought can relieve a limited internal workspace, but that does not establish Karlsson's broader human-to-LLM latent-thought analogy.

## Extractable Value

1. **Writing is several epistemic operations, not one medium-level cause** -- The essay separates broad search, explicit testing, stabilization, offloading, and reuse. This is new relative to sources that treat concretization as the whole writing-is-thinking mechanism, and it gives the proposed writing workshop a more discriminating functional vocabulary. [deep-dive]

2. **Exploration and commitment can require different representational states** -- Keeping an uncertain idea “accurately vague” preserves alternatives that premature prose would silently fill with guesses; later inscription deliberately gives up that latitude to gain reviewability. This adds a human-side case to the KB's warning that [constraining is not automatically improvement](../notes/definitions/constraining.md). [quick-win]

3. **Relay results explain how inscriptions support longer thought** -- A result that has survived explicit checking can leave working memory and become a dependable premise for the next step. The agent-operated analogue is not generation alone: a candidate must be evaluated, retained, and made available to later work before it performs the relay function. [deep-dive]

4. **The useful process may alternate between expansion and compression** -- Wordless thought is proposed as faster, higher-branching search, while wording serializes and compresses enough structure to expose errors. This suggests that a writing or agent loop should ask which phase currently needs breadth and which needs commitment instead of applying maximal explicitness at every step. [experiment]

5. **Expertise is the claimed precondition for productive wordless search** -- Karlsson's examples imply that non-verbal speed becomes useful only after deep reading, writing, and domain practice have built a sufficiently constrained mental model. That is a testable boundary for human studies, not evidence that an unstructured search mode is generally superior. [experiment]

6. **The LLM comparison identifies a question, not an answer** -- The footnote contrasts token scratchpads with high-dimensional internal state and points to latent chain-of-thought as a possible alternative. The durable question is when externalized tokens help by stabilizing state versus hurt by bottlenecking it; the cited analogies do not resolve that tradeoff. [just-a-reference]

## Limitations (our opinion)

The core evidence is introspective and selectively historical. Hadamard's survey reports how accomplished mathematicians described their experience; it does not establish what representations performed the computation, how common the mode is, or whether wordlessness caused their success. The Feynman counterexample in Karlsson's own footnote also shows that expert mathematical work can occur on paper rather than first becoming complete internally. “Wordless,” “non-linguistic,” “subconscious,” and “blurry” therefore should not be treated as one measured cognitive state.

The neuroscience does not carry the proposed mechanism. Karlsson explicitly labels the simultaneous default-mode/executive-control account as speculation. Evidence that both networks can co-activate during some creative tasks does not show that this is what Hadamard's subjects did, that language ordinarily inhibits the relevant search, or that practice creates the proposed “tense subconscious processing.” The simpler account is that expertise supports rapid pattern manipulation and that writing supplies external memory and error checking; the network story is not needed for those functional claims.

The LLM footnote is likewise analogical. A high-dimensional activation vector and a sampled token differ in dimensionality, but vector width is not by itself an information measure, and token generation does not imply that a single scalar contains everything the model retained. The empirical [J-space](verbalizable-representations-global-workspace-llms.ingest.md) and [filler-token](reading-between-the-dots-decoding-hidden-computation.ingest.md) studies show narrower facts: some causally relevant internal computation can be decoded, and externalized steps can sometimes reduce internal-workspace demand. They do not establish that human wordless thought and LLM latent reasoning share a mechanism or that feeding continuous states back is generally better than token scratchpads.

Finally, changed human understanding, a stabilized page, and durable agent-system learning are different outcomes. A human may learn even if the page is discarded; an agent-generated page may persist without being selected, retrieved, or behaviorally effective. Any automated analogue should transfer the essay's functions separately and preserve those causal boundaries rather than calling all written output “learning.”

## Recommended Next Action

The written-artifacts-in-learning-loops workshop that used this source has run and closed. This source served as the boundary case keeping “learning through writing” from collapsing the changed human, the retained artifact, and the later agent consumer, or assuming all productive thought is verbal — a distinction the KB already carries in [knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) and [Continual learning requires governing behaviour-changing writes, not just storing content](../notes/continual-learning-requires-governing-behaviour-changing-writes.md), so it warranted no separate promotion.
