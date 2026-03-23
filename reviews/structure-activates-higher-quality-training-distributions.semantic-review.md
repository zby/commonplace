=== SEMANTIC REVIEW: structure-activates-higher-quality-training-distributions.md ===

Claims identified: 12

1. [Para 1] "When the context contains sections like `## Evidence` and `## Reasoning`, the model's output will resemble the training data that had similar structure: scientific papers, legal analyses, peer-reviewed arguments."
2. [Para 1] "These documents are, on average, higher quality for reasoning purposes than the bulk of internet text."
3. [Para 2] "The structure acts as a distribution selector."
4. [Para 2] "A Toulmin-shaped template steers the model toward the subset of its training data where authors were already doing rigorous argumentation."
5. [Para 3] "This argument is independent of failure-mode transfer."
6. [Para 3] "And it's independent of readability for humans."
7. [Para 4, epiplexity] "Epiplexity measures structurally learnable content within computational bounds, and one of its core results is that data ordering affects learning."
8. [Para 4, epiplexity] "Structured templates work by the same mechanism: they reorder and partition the generation task so that at each point, the model's bounded computation can extract more structure from its training distribution."
9. [Para 4, epiplexity] "The distribution-selection metaphor is what epiplexity formalises."
10. [Status note] "Ugare & Chandra (2026) show that semi-formal reasoning templates yield 5-12pp accuracy gains on code verification tasks."
11. [Status note, Lampinen] "chain-of-thought prompting partially restores content-independent reasoning -- improving performance on abstract/unfamiliar conditions without degrading familiar ones. This is the distribution-selection effect observed directly."
12. [Status note, final para] "The evidence supports 'structure helps, and the need for it doesn't dissolve with scale' but not the stronger thesis that it works specifically via activating higher-quality training subsets."

---

WARN:

- [Grounding alignment / domain coverage] The note claims "The distribution-selection metaphor is what epiplexity formalises" (para 4), but this overstates the connection. The epiplexity source (Finzi et al.) formalises why data ordering affects extractable structure for bounded learners -- a result about training data ordering and curriculum design. It does not address inference-time prompting or how context steers generation toward training subsets. The note bridges from "data ordering affects learning" (a training-time phenomenon about what structure a learner can extract from sequences) to "structured templates reorder the generation task" (an inference-time claim about which training subsets get activated). This is a domain jump: epiplexity operates in the domain of learning/training, while the note's central claim operates in the domain of inference/generation. The note's analogy may be apt, but the source does not formalise the distribution-selection mechanism -- it formalises something adjacent. Readers following the link will find a paper about measuring learnable content, not about how prompt structure selects from learned distributions.

- [Grounding alignment / vocabulary mismatch] The note says "Structured templates work by the same mechanism: they reorder and partition the generation task so that at each point, the model's bounded computation can extract more structure from its training distribution" (para 4). The epiplexity source never discusses inference-time context, prompt templates, or generation tasks. Its "data ordering" result is about the order in which training examples are presented to a learner, not about how structured sections in a prompt affect autoregressive token prediction. The note's use of "the same mechanism" asserts an identity between training-time data ordering and inference-time context structure that the source does not establish.

- [Completeness / boundary case] The note's central metaphor -- structure as distribution selector -- implies that the quality improvement comes from activating a different subset of training data. But a competing mechanism exists that the note only acknowledges in the final paragraph and does not adequately integrate: structure may improve output by constraining the output format (forcing the model through specific reasoning steps), not by selecting from higher-quality training data. The [process-structure-and-output-structure-are-independent-levers](../kb/notes/process-structure-and-output-structure-are-independent-levers.md) note explicitly separates these two mechanisms and notes that process constraints "force specific reasoning work that a heading-only constraint would not." The boundary case is: if you give a model a template with `## Evidence` and `## Reasoning` headings but no instructions about what reasoning work to perform, does the output quality still improve? If the gain comes primarily from process constraint (being forced to state evidence before concluding) rather than distribution activation, the note's title claim is naming the wrong mechanism. The note's own status section concedes this ("doesn't confirm the causal claim that the mechanism is distribution selection rather than simply constraining output format"), but the title and the first four paragraphs present distribution selection as the operative mechanism, not as one of two competing hypotheses. The concession is buried.

- [Grounding alignment / inference validity] The note claims that the Lampinen et al. finding -- "chain-of-thought prompting partially restores content-independent reasoning" -- is "the distribution-selection effect observed directly." But the Lampinen source does not frame CoT as distribution selection. The source frames CoT as enabling "slow, deliberative reasoning" analogous to dual-process System 2 engagement. The distribution-selection interpretation (CoT activates training data where rigorous reasoning was performed) is the note's own inference layered onto the source's finding. The source is compatible with this interpretation but equally compatible with the alternative that CoT works by forcing step-by-step computation that reduces errors, regardless of which training data is activated. Claiming this is the distribution-selection effect "observed directly" overstates the evidential support.

INFO:

- [Completeness / boundary case] The note assumes structured documents in training data are "higher quality for reasoning purposes" (para 1). Boundary case: highly structured but low-quality documents exist in abundance in training data -- formulaic academic papers with weak arguments, legal filings that are procedurally correct but substantively poor, boilerplate reports. Structure correlates with quality on average, but the note treats this as a reliable selector rather than a noisy one. The "on average" qualifier in the note partially addresses this, but the rest of the argument proceeds as if the selection is clean.

- [Completeness / boundary case] The note claims the argument is "independent of failure-mode transfer" (para 3). But if the distribution-selection mechanism works because structured training data was written by authors who avoided specific reasoning failures (the same failures LLMs exhibit), then distribution selection and failure-mode transfer may share a common cause rather than being truly independent. The note's framing of three independent arguments (distribution selection, failure-mode transfer, readability) may overstate their independence -- the first two could be two descriptions of the same underlying phenomenon (structured training data is better because the structures prevented failures).

- [Internal consistency / tension] The note's title and opening paragraphs present distribution selection as the primary mechanism ("The structure acts as a distribution selector"), while the status section at the end says "the evidence supports 'structure helps' but not the stronger thesis that it works specifically via activating higher-quality training subsets." This creates a tension: the note reads as advocating for a specific causal mechanism in its body, then retreating from that mechanism in its status section. The seedling status partially resolves this (it's a developing idea), but a reader who stops after the first four paragraphs would take away a stronger claim than the evidence supports.

- [Grounding alignment] The note cites Ugare & Chandra accurately -- "5-12pp accuracy gains on code verification tasks" and "Sonnet gains nothing from templates on code QA (84.8% vs 85.3%)" both check out against the ingest. However, the note also mentions "past experience with `structured-claim` type showed that imposing structure can degrade quality" without citing a source. This appears to be internal KB experience, which is fine, but it is presented alongside empirical citations without distinguishing its evidential status.

PASS:

- [Grounding alignment] The Ugare & Chandra citation is accurately attributed. The 5-12pp accuracy gain figure, the Sonnet non-improvement on code QA, and the characterisation of semi-formal reasoning templates all match the source ingest. The note correctly positions this as "partial empirical support" rather than confirmation.

- [Grounding alignment] The Lampinen et al. citation accurately reports the key findings: CoT improves performance on abstract/unfamiliar conditions without degrading familiar ones, and content effects survive scaling and instruction tuning. These claims match the source ingest.

- [Internal consistency] The independence claims (para 3) are internally consistent -- the note correctly distinguishes its argument from failure-mode transfer and from readability, and the linked notes confirm they are framed as separate arguments in the broader KB structure.

- [Internal consistency] The status section faithfully represents the note's evidential situation. The concessions about the epiplexity connection being "suggestive" and the evidence not confirming the causal mechanism are honest and aligned with what the sources actually provide.

- [Completeness] The note identifies a meaningful boundary condition (Sonnet's non-improvement on code QA) and the historical structured-claim degradation, rather than presenting only supporting evidence. This balanced treatment strengthens the note's credibility as a seedling.

Overall: 4 warnings, 4 info
===
