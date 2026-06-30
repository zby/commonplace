# Split and Rehome Critique: LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on

**Target:** `kb/work/agent-note-improvement/case-01-llm-generation-relaxes-goals/baseline-e242c975.md`

## Main note to preserve

**Claim:** When prose generation is used for a goal whose full conjunction of constraints has not been made concrete, an LLM can return a fluent relaxation that silently drops the unmet constraint, replacing the human writer's localized stall with a reader-side audit burden.

**Minimum argument:**

- A vague design or argument goal can be treated as a conjunction of constraints whose reachability is not yet proven.
- Writing as discovery searches for a concrete witness that satisfies the conjunction.
- A human writer's failure to continue is useful because it localizes the unmet constraint.
- LLM generation does not produce an equivalent halt signal; it can emit a plausible artifact for a weaker constraint set.
- Because the dropped conjunct is unmarked, the reader must rediscover both whether the witness is real and where the relaxation occurred.
- The claim is bounded to prose or argument-making contexts where generation is doing the constructive search, not merely rendering an already-found witness.

Material that must stay: the C/Lisp example, the witness-search framing, the Weizenbaum stall quotation, the relaxation/counterfeit-witness contrast, the reader-burden section, and the scope distinction between constructive search and post-witness rendering.

## Branch inventory

| Branch | Current location | Destination | Why |
|---|---|---|---|
| Semi-decidability of witness search | Opening section | Keep, but compress | It supports the burden-of-proof framing, but the formal label should not dominate the note. |
| Typicality-biased constraint shedding | "Why the relaxation lands on the crux" | New note | This is a distinct mechanism claim about which constraint gets dropped; it needs evidence or tighter derivation beyond the main stall-vs-relaxation contrast. |
| Reverse-compression relation | "Why the relaxation lands on the crux" | Source/workshop note | The relation is plausible but currently works as a lead into another note rather than necessary support here. |
| Friction and fluency invert at the crux | "Why the relaxation lands on the crux" | New note | This is a stronger diagnostic claim than the main note needs and requires evidence about felt difficulty, model fluency, and truth-tracking. |
| Predictions about under-witnessed throughput and difficulty falling toward chance | End of reader-burden section | Open question | Useful as a falsifiability prompt, but too large and empirical to carry inside the main argument. |
| Code oracles and training effects | "Scope and boundary" | Open question | The verifier boundary is relevant, but the extra claim that training against an oracle may make code generation more consistent is a separate hypothesis. |
| Hallucination as coherence-side sibling of relaxation | "Relation to hallucination (hypothesis)" | New note | It has a distinct taxonomy claim and correspondence/coherence split that should not compete with the original note's main mechanism. |
| Reconstructed stalls and involuntary stalls | "Open questions" | Open question | These are good research prompts, not needed in the library note unless later developed. |
| Extension to codification | "Open questions" | Open question | The extension is promising but untested; keep it as a later-work prompt rather than a branch inside the main note. |

## Rehoming candidates

- **Typicality-biased generation sheds the least typical constraint first** -- Claim: when an underspecified prompt contains one novel load-bearing constraint and several ordinary constraints, LLM generation tends to preserve the ordinary constraints and relax the novel one. Required support: examples or a mechanistic argument connecting token typicality, constraint rarity, and fluent surface completion. It should not remain in the original note because the main note only needs silent relaxation; this branch claims a predictable direction for the relaxation.
- **Machine fluency is least diagnostic at the load-bearing crux** -- Claim: in constructive prose tasks, human friction can peak where understanding fails while LLM fluency remains high at the same joint, making fluency anti-correlated with the diagnostic signal a writer would have received. Required support: a sharper account of when fluency masks unsoundness rather than merely decoupling from it, plus examples where the crux is known. It should not remain in the original note because it turns a concealment mechanism into a diagnostic theory.
- **Relaxation is the coherence-side analogue of hallucination** -- Claim: hallucination fills correspondence gaps with plausible facts, while relaxation fills coherence gaps with plausible entailments or missing witnesses. Required support: definitions of correspondence and coherence failures, examples of each, and boundaries showing when the analogy breaks. It should not remain in the original note because it reframes the phenomenon taxonomically rather than explaining the stall-to-reader-burden mechanism.

## Deletion candidates

- Remove or sharply reduce the "reverse-compression" aside; it currently imports another concept without being necessary to show why a silent relaxation burdens the reader.
- Remove the sentence predicting that code-oracle training plausibly improves code generation itself; it is a secondary hypothesis enabled by the oracle discussion, not part of this note's claim.
- Remove any phrasing that implies the model literally computes an argmax or that the constraint set lives inside the model. The current caveat helps, but the revised note should keep this as a reader-side idealization and not spend space defending it.
- Delete most of the final open-question list from the revised note. Preserve at most one compact "open question" about whether a separate adversarial pass can reconstruct the stall.

## Revision target

The revised original note should be a tighter note about one loss in LLM-assisted thinking: delegating the witness search removes the writer's localized failure signal and replaces it with a fluent relaxation whose missing constraint must be found by the reader. It should keep the Borretti and Weizenbaum grounding, define relaxation as a weaker witnessed problem, explain why the burden of proof only appears discharged, and end with the practical boundary: use LLMs to render an already-found witness, not to substitute for the constructive search that proves the goal reachable.
