# Prune Weak Expansions: LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on

**Target:** `kb/work/agent-note-improvement/case-01-llm-generation-relaxes-goals/baseline-e242c975.md`
**Strongest retained claim:** When an LLM cannot construct a witness satisfying every constraint in a prose-thinking task, it can still emit a plausible witness for a weakened goal with the dropped constraint unmarked, shifting a localized author-side stall into an expensive reader-side audit.

## Core support

- Opening paragraphs: define vague goals as conjunctions of constraints and composition as a search for a witness, which gives the note its burden-of-proof frame.
- "The stall and the relaxation": directly contrasts the human stall with LLM relaxation and names the hidden dropped conjunct as the central failure mode.
- "Why the relaxation lands on the crux": supports why the dropped conjunct is likely to be the important novel constraint rather than an incidental detail.
- "The check moves to the reader, and gets harder": states the practical consequence of the hidden relaxation and explains why plausibility raises inspection cost.
- "Scope and boundary": protects the central claim from overreach by limiting it to composition-as-discovery and oracle-poor prose argument.

## Weak expansions

| Location | Problem | Action | Rationale |
|---|---|---|---|
| Opening, semi-decidability paragraph | The formal semi-decidability language is useful but heavier than the note needs, and it risks inviting technical objections about whether prose composition is literally a search procedure. | compress | Keep the witness/burden-of-proof frame, but reduce the mathematical apparatus to a short claim: success proves reachability for that artifact; failure only localizes an unmet constraint within a budget. |
| Opening parenthetical on Borretti's "*ex falso* anything can be imagined" | Interesting source interpretation, but it is a side gloss and not needed to establish the mechanism. | compress | Preserve only if it helps tie the note to the source; otherwise it distracts from the witness-search claim before the main contrast has landed. |
| "The stall and the relaxation", argmax-over-plausibility caveat | The caveat is accurate, but it slows the strongest section with model-theory qualifications. | compress | Retain the reader-side idealization in one clause or footnote-like sentence; the core claim is about the output's role as a plausible relaxed witness. |
| "Why the relaxation lands on the crux", reverse-compression and confidence links | The paragraph carries a strong mechanism, but it leans on two linked notes and several abstractions at once. | keep | This is the note's best explanation for why relaxation is not just concealment; keep it, but make the dependency on novelty-as-rarity explicit and cut repeated phrasing. |
| "Friction and fluency invert at the crux" | The anti-correlation claim is sharper than the evidence in the note supports, especially "with truth" at the constraint that matters. | compress | Keep as a bounded corollary: human friction is diagnostic of the author-side search point, while LLM fluency fails to mark that same point. Avoid making truth-correlation carry more than the argument establishes. |
| "The check moves to the reader", empirical prediction paragraph | The predictions are valuable but underdeveloped and introduce measurement problems that the note does not solve. | compress | Keep one falsifiability sentence or move the prediction to open questions. The main section should end on the burden of proof looking discharged while remaining undischarged. |
| "Scope and boundary", code oracle/training paragraph | The verifier boundary is important, but the claim that training against the oracle plausibly improves generation is a separate mechanism. | compress | Keep the oracle distinction because it protects scope; remove or demote the training-effect speculation unless a separate note develops it. |
| "Scope and boundary", workflow prescription | The human-finds-witness/LLM-renders-it workflow is actionable and follows from the claim, but it starts to become prescriptive. | keep | Keep as the closing implication, because it converts the mechanism into a usable boundary without requiring a new theory branch. |
| "Relation to hallucination (hypothesis)" | This is a plausible synthesis but distinct from the main note and explicitly hypothetical. | split | It deserves its own note comparing correspondence failures and coherence failures; here it weakens the argument by expanding into another taxonomy before the main claim is fully closed. |
| "Open questions" | The questions are useful, but the second and third broaden the note into signal phenomenology and codification before the central prose mechanism is settled. | compress | Retain only the operational question about whether a separate adversarial/checking pass can reconstruct the stall; move codification and involuntary-stall questions to candidate split notes or future work. |

## Proposed shape

1. Define a prose-thinking goal as a constraint set and composition as the attempt to produce a satisfying witness.
2. Contrast the human stall with LLM relaxation: the human fault localizes the unmet constraint; the LLM emits a plausible witness for a weaker goal without marking the relaxation.
3. Explain why the relaxed-away constraint is often the crux: novelty is less typical, so typicality-biased generation preserves familiar form and drops the rare load-bearing conjunct.
4. Show the operational consequence: the reader inherits an unlocalized audit over partly implicit constraints, while the output looks as if the burden of proof has been discharged.
5. Bound the claim to composition-as-discovery in oracle-poor prose, then close with the workflow rule: keep the constructive witness search human; use LLMs after the witness exists.

## Candidate splits

- "Relaxation is the coherence-side sibling of hallucination" - would claim that hallucination fills missing correspondence while relaxation fills missing entailment; needs examples showing the same typicality mechanism across factual and reasoning gaps.
- "External oracles decide whether frictionless generation loses the stall" - would claim that verifiers can re-impose the witness burden after generation; needs contrast cases across code, formal proofs, structured data, and prose.
- "Can adversarial review reconstruct the lost stall?" - would claim that a second pass can recover some hidden dropped constraints only when it recomputes the constraint set independently; needs conditions for decorrelation and above-chance checking.
- "Friction and fluency invert at load-bearing constraints" - would carry the stronger anti-correlation claim; needs evidence that human friction and machine fluency diverge specifically at the crux, not merely that LLM confidence is poorly calibrated.

## Net effect

Pruning makes the note harder to attack by keeping one causal chain in view: constraint set, witness search, human stall, LLM relaxation, hidden dropped conjunct, reader-side audit. Compressing the formal setup and empirical predictions removes places where critics can fight side claims without touching the core mechanism. Splitting hallucination, verifier oracles, reconstructed stalls, and fluency/friction inversion lets those plausible expansions earn their own evidence instead of borrowing authority from the stronger central note.
