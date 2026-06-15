---
description: "An LLM's next-token confidence measures how typical a continuation is, not whether it's true or valid; the two are decoupled, so soundness can't be read off confidence and needs a separate check"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, failure-modes, llm-interpretation-errors]
status: speculative
---

# An LLM's generation confidence tracks typicality, not soundness

*Speculative. The core decoupling claim is defensible; the anti-correlation case, the internal-probe conjecture, and the hallucination-parent framing are retained conjecture pending evidence.*

A token-generating model's confidence — the probability it assigns to a continuation — measures how *typical* that continuation is given the running text. It does not measure whether the continuation is *sound*: true as a matter of fact, or validly inferred from what came before. Training optimizes the likelihood of text, and fluent, plausible-looking text is high-probability whether or not it is correct. "Paris is the capital of France" and "Lyon is the capital of France" are both just typical-looking French-geography sentences to the decoder; a fluent "because X, therefore Y" is what an argument *looks like* whether or not Y follows from X.

So confidence and soundness are **decoupled** — and that is weaker than anti-correlation, a distinction that matters. Decoupling says only that confidence is *uninformative* about soundness: you learn nothing about whether a claim is true or valid from how probable the model found it. It does not by itself say confidence is *highest* where soundness is lowest. That stronger, anti-correlated case holds only under an added premise — that unsound moves are themselves *typical* (clichés, common fallacies, plausible fabrications that recur in training text). Where that premise holds, and it often does, the model is most fluent exactly at the joint where it should hesitate; but the anti-correlation is an extra empirical claim, not a consequence of decoupling.

## Consequence: soundness needs a separate check

Because the signal is not in the generation confidence, you cannot recover it by reading that confidence off — thresholding on token probability, or asking the model "how sure are you," surfaces typicality, not truth or validity. Detecting unsoundness requires a *separate operation* that recomputes what confidence fails to track: an external oracle (a compiler, a test, a retrieval check), a trained probe, or an adversarial pass that re-derives the inference instead of re-reading the prose. This is why the boundary of reliable automation tracks the [availability of a verifier](./the-boundary-of-automation-is-the-boundary-of-verification.md), not the model's apparent certainty.

Whether a *separate internal representation* of soundness exists — one a probe could read from hidden states even though it is absent from the output distribution — is genuinely open; models may encode some truthfulness signal internally, though that is an unsettled empirical question this note does not adjudicate. Even if such a representation exists, it is not the next-token signal, and recovering it is still a separate operation, not the generator volunteering its confidence. Sycophancy — deployment tuning that rewards agreement with the user over correction — adds an independent reason the signal stays hidden: that tuning can bias outputs toward agreement even where internal features could support a correction.

## Two faces

The same decoupling produces two failures, one per kind of soundness:

- **Correspondence** — a hallucinated *fact* is stated with full fluency, because fabrication is typical-looking text.
- **Coherence** — an unsupported *inference* reads smoothly, because a connective plus a plausible clause is typical-looking argument. This is the hidden "signal" in [the composition-friction loss](./llm-generation-relaxes-goals-where-human-writing-stalls.md): the stall a human would feel at a weak "because" is exactly what cannot be read off the model's confidence.

---

Relevant Notes:

- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](./llm-generation-relaxes-goals-where-human-writing-stalls.md) — applied-in: the hidden composition "signal" is this property applied to inferential validity; that note links here for why the signal can't be read off confidence
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: soundness needs a separate verifier precisely because confidence does not track it
