---
description: "Trace-derived memory arrives as a record, not knowledge — authority is earned through post-capture operations (verify, distill, consult) with increasingly hard oracles; stores that stall before verification accumulate guesses masquerading as knowledge"
type: kb/types/note.md
traits: [title-as-claim]
tags: [agent-memory, learning-theory, context-engineering]
---

# Trace-derived memory earns authority per operation, not at capture

A memory derived from a trace does not arrive as knowledge. It arrives as a record of something that happened, and the weight a future reader should give it — its **epistemic authority** — is earned through operations performed after capture. Each operation, when it succeeds, licenses a stronger reading of the artifact: a documented failure licenses only "watch for this," a verified diagnosis licenses "this is what was wrong," a distilled rule licenses "do this by default." Capture grants none of these. A store that treats captured records as knowledge has skipped the earning.

## A witness ladder

The claim does not depend on any particular factoring of the operations, but exhibiting one shows the maturation path can be made explicit. One ladder that works:

1. **Fail** — document the failure. A correction, error, retry, or weakened guarantee is captured as a candidate. The artifact's claim is only "this happened."
2. **Investigate** — understand why it happened. The candidate gains a diagnosis: a causal story for the failure.
3. **Verify** — turn the diagnosis into a checked fact. The causal story is tested against evidence — a reproduction, a passing fix, a confirming run — so the claim becomes "this is true," not "this is plausible."
4. **Distill** — generalize the verified fact into a rule. The single checked case becomes a transferable claim covering a class of situations: [distillation](./definitions/distillation.md) into a use-shaped artifact.
5. **Consult** — read the rule instead of re-deriving it. The rule is routed into future contexts so the system applies it without re-running the investigation.

The rung boundaries are free choices — investigate and verify could merge, distill could split further — and nothing below depends on there being five. What the argument does depend on: verification is a distinct operation from capture, generalization is distinct from verification, and a rule pays off only when read back. Any factoring that preserves those distinctions is an equally good witness.

## The operations have different oracles

The ladder is not one process with intermediate save points; each rung is a different kind of work against a different oracle. Documenting a failure needs only a signal that something went wrong. Investigation needs reasoning over the trace. Verification needs an oracle that can discriminate a correct diagnosis from a plausible-but-wrong one. Distillation needs judgment about which features of the case generalize. Consultation needs routing machinery that delivers the rule at the moment it applies.

Because the oracles differ in strength, the rungs differ in tractability. The fail rung is cheap and its signal quality is well understood: [trace-derived extraction must respect signal quality](./agent-memory-requirements/use-trace-derived-extraction.md), and the candidate-status, confidence, and source-pointer fields it prescribes are exactly the markers that keep a rung-1 artifact from being read as a rung-4 rule. Verify and distill are where oracles get hard — the same place [automating KB learning stalls](./automating-kb-learning-is-an-open-problem.md): generation is easy, evaluation is the bottleneck.

## Stalling early accumulates guesses that masquerade as knowledge

A store that captures failures and diagnoses but never verifies or distills fills with rung-1 and rung-2 artifacts that *look* like knowledge. An unverified diagnosis is a guess with a confident tone. If nothing in the store's format or review process records which rung an artifact has reached, readers grant rung-4 authority to rung-2 content, and the store's apparent knowledge outruns its actual knowledge.

One candidate measure: **verification coverage** — the fraction of stored claims that have been checked rather than merely asserted. A store with high capture volume and low verification coverage is accumulating guesses, and the measure makes that legible without a per-claim audit.

## The consult rung is contextual activation

Reaching the top rung means the rule is *read instead of re-derived* — and a rule that sits in storage unread has not reached it. Climbing to "distilled" is necessary but not sufficient, because [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md). The consult rung is precisely the activation step: the rule must be routed into the context where it applies and actually change what the agent does. A distilled-but-never-activated rule is the storage-to-context failure described there, one rung short of paying off.

## Full automation is not required

The ladder describes maturation, not an automation target. Where the oracle is strong — a failure with a natural verifier such as a reproducing test or a passing fix — the climb from fail through verify can be automated. Where it is weak — verify and distill for judgment-heavy claims — full automation is out of reach for the same reason [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md): the mutations lack oracles we can manufacture. A human-directed loop with automated parts is therefore a valid operating point, not a degraded one: automate the rungs that have oracles (capture, signal classification, codifiable checks), route the rest to human or agent review. The question is only which rungs the system can climb unattended.

## Boundary: epistemic maturity versus structural refinement

This is the epistemic axis. The related-but-distinct axis is structural: the [wikiwiki principle](./wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md)'s text→note→structured-claim ladder lowers *capture friction* and adds structure in place. The two are orthogonal. The wikiwiki ladder asks "how much structure has this artifact grown?"; this one asks "how much has its claim been earned?" A structurally complete `structured-claim` can sit at the fail rung — well-formatted, unverified — and a rung-3 verified fact can still be a bare `text` capture. Confusing the two lets formatting pass for authority.

Within [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md), this maturation is the across-session timescale: the path of a durable artifact from raw trace toward a consulted rule.

## Open Questions

- Origin is a paraphrased tweet (URL not captured) observing that models exit the maturation path at different stages. The model-capability-determines-exit-stage framing is excluded as too liquid; if the source is captured it belongs as a `derived-from` edge to a source snapshot, not in the claim.
- Is verification coverage measurable in practice, or does "verified" itself need gradations (reproduced once vs. survived repeated reuse)?
- Do the middle operations collapse for some claim types — e.g. preferences, where there is no diagnosis to verify, only an accumulation of accept/reject events?

---

Relevant Notes:

- [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — extends: the consult rung is the activation step; a distilled rule that is never read back is one rung short of payoff
- [Use trace-derived extraction as meta-learning](./agent-memory-requirements/use-trace-derived-extraction.md) — grounds: the fail rung's signal-quality distinctions and candidate-status fields keep early-rung artifacts from being read as mature rules
- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — grounds: the verify and distill rungs are where oracles get hard, so full automation of the climb is out of reach for judgment-heavy claims
- [distillation](./definitions/distillation.md) — defined-in: the distill rung is distillation of a verified case into a transferable rule
- [deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — extends: this maturation is the across-session timescale of deploy-time learning, from raw trace toward a consulted rule
- [the wikiwiki principle: lowest-friction capture, then progressive refinement](./wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) — contrasts: structural-refinement ladder (capture friction, structure-in-place) is the orthogonal axis to this epistemic-maturity ladder
