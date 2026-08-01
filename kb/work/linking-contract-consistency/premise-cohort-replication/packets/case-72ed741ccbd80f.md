# Case packet

Neutral case identifier: case-72ed741ccbd80f

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Trace-extracted memory earns authority per operation, not at capture

A memory derived from a trace does not arrive as knowledge. It arrives as a record of something that happened, and the weight a future reader should give it — its **epistemic authority** — is earned through operations performed after capture. Each operation, when it succeeds, licenses a stronger reading of the artifact: a documented failure licenses only "watch for this," a verified diagnosis licenses "this is what was wrong," an abstracted rule licenses "do this by default." Capture grants none of these. A store that treats captured records as knowledge has skipped the earning.

## A witness ladder

The claim does not depend on any particular factoring of the operations, but exhibiting one shows the maturation path can be made explicit. One ladder that works:

1. **Fail** — document the failure. A correction, error, retry, or weakened guarantee is captured as a candidate. The artifact's claim is only "this happened."
2. **Investigate** — understand why it happened. The candidate gains a diagnosis: a causal story for the failure.
3. **Verify** — turn the diagnosis into a checked fact. The causal story is tested against evidence — a reproduction, a passing fix, a confirming run — so the claim becomes "this is true," not "this is plausible."
4. **Abstract** — generalize the verified fact into a bounded rule. The checked case, with a stated boundary and mechanism, becomes a transferable claim covering a class of situations. [Abstracting an experience requires stating where the lesson stops].
5. **Consult** — read the rule instead of re-deriving it. The rule is routed into future contexts so the system applies it without re-running the investigation.

The rung boundaries are free choices — investigate and verify could merge, abstract could split further — and nothing below depends on there being five. What the argument does depend on: verification is a distinct operation from capture, generalization is distinct from verification, and a rule pays off only when read back. Any factoring that preserves those distinctions is an equally good witness.

## The operations have different oracles

The ladder is not one process with intermediate save points; each rung is a different kind of work against a different oracle. Documenting a failure needs only a signal that something went wrong. Investigation needs reasoning over the trace. Verification needs an oracle that can discriminate a correct diagnosis from a plausible-but-wrong one. Abstraction needs judgment about which features of the case generalize. Consultation needs routing machinery that delivers the rule at the moment it applies.

Because the oracles differ in strength, the rungs differ in tractability. The fail rung is cheap and its signal quality is well understood: [trace extraction must respect signal quality], and the candidate-status, confidence, and source-pointer fields it prescribes are exactly the markers that keep a rung-1 artifact from being read as a rung-4 rule. Verify and abstract are where oracles get hard — the same place [automating KB learning stalls]: generation is easy, evaluation is the bottleneck.

## Stalling early accumulates guesses that masquerade as knowledge

A store that captures failures and diagnoses but never verifies or abstracts fills with rung-1 and rung-2 artifacts that *look* like knowledge. An unverified diagnosis is a guess with a confident tone. If nothing in the store's format or review process records which rung an artifact has reached, readers grant rung-4 authority to rung-2 content, and the store's apparent knowledge outruns its actual knowledge.

One candidate measure: **verification coverage** — the fraction of stored claims that have been checked rather than merely asserted. A store with high capture volume and low verification coverage is accumulating guesses, and the measure makes that legible without a per-claim audit.

## The consult rung is contextual activation

Reaching the top rung means the rule is *read instead of re-derived* — and a rule that sits in storage unread has not reached it. Climbing to "abstracted" is necessary but not sufficient, because [knowledge storage does not imply contextual activation]. The consult rung is precisely the activation step: the rule must be routed into the context where it applies and actually change what the agent does. An abstracted-but-never-activated rule is the storage-to-context failure described there, one rung short of paying off.

## Full automation is not required

The ladder describes maturation, not an automation target. Where the oracle is strong — a failure with a natural verifier such as a reproducing test or a passing fix — the climb from fail through verify can be automated. Where it is weak — verify and abstract for judgment-heavy claims — full automation is out of reach for the same reason [automating KB learning is an open problem]: the mutations lack oracles we can manufacture. A human-directed loop with automated parts is therefore a valid operating point, not a degraded one: automate the rungs that have oracles (capture, signal classification, codifiable checks), route the rest to human or agent review. The question is only which rungs the system can climb unattended.

## Boundary: epistemic maturity versus structural refinement

This is the epistemic axis. The related-but-distinct axis is structural: the [wikiwiki principle]'s text→note→structured-claim ladder lowers *capture friction* and adds structure in place. The two are orthogonal. The wikiwiki ladder asks "how much structure has this artifact grown?"; this one asks "how much has its claim been earned?" A structurally complete `structured-claim` can sit at the fail rung — well-formatted, unverified — and a rung-3 verified fact can still be a bare `text` capture. Confusing the two lets formatting pass for authority.

Within [deploy-time learning], this maturation is the across-session timescale: the path of a durable artifact from raw trace toward a consulted rule.

## Open Questions

- Origin is a paraphrased tweet (URL not captured) observing that models exit the maturation path at different stages. The model-capability-determines-exit-stage framing is excluded as too liquid; if the source is captured it belongs as an `abstracted-from` edge to a source snapshot, not in the claim.
- Is verification coverage measurable in practice, or does "verified" itself need gradations (reproduced once vs. survived repeated reuse)?
- Do the middle operations collapse for some claim types — e.g. preferences, where there is no diagnosis to verify, only an accumulation of accept/reject events?

---

Relevant Notes:

## Artifact B

# Use Trace Extraction As Meta-Learning

Trace extraction is the parallel path for memory that was not captured while understanding was live, or that only becomes visible across later traces. Session logs contain latent memory-creation opportunities, but those opportunities differ by oracle strength.

Corrections are strongest because the log contains both a negative and positive signal. Silent failures are weaker: the task appears completed, but the trace shows errors, retries, fallback paths, warning output, or weakened guarantees. Preferences are distributed over many accept/reject events. Procedures show up as recurring action sequences. Discoveries and broad syntheses have the weakest immediate oracle; their value often appears only through later reuse.

Without an explicit signal-quality distinction, automated or semi-automated extraction can give weak-signal discoveries, preferences, or syntheses the same apparent authority as corrected errors. That creates trust and lifecycle failures: low-confidence memories look durable, reviewers cannot tell which candidates need stronger evidence, and activation mechanisms may spend context on lessons that were never well grounded.

## Readable-Artifact And Distributed-Parametric Learning

This requirement mainly describes readable memory artifacts because they can be inspected, diffed, promoted, and rolled back. Systems such as [AgeMem] show a different path: traces train a distributed-parametric policy for Add/Update/Delete/Retrieve/Summary/Filter actions. That path belongs where the oracle is strong enough to justify learned memory-management policy; it should not be smuggled in as ordinary artifact promotion.

## Memory Evolution

Extraction needs an evolution operation, not only creation. New memory may update, split, merge, re-tag, or contextualize nearby old memory. The comparative review flags [A-MEM's evolution step] because new notes update neighboring notes' context and tags, while [Hindsight] and [Cludebot] show CRUD and dream-cycle variants. The requirement is not that every system automate this immediately; it is that the architecture leave room for old memory to be revised by new evidence instead of only appending candidates.

## Methods

- Narrow, schema-constrained extraction prompts for one signal type at a time.
- Classifiers or simple rules for explicit events: user correction, command failure, retry, fallback, approval, rejection, or repeated tool sequence.
- Batch analysis over many sessions for preferences, procedures, and recurring failure patterns.
- Manual observation inboxes that let agents record noticed improvement opportunities without interrupting the current task.
- Human or agent review queues for weak-oracle candidates such as discoveries, broad design principles, or high-impact policy changes.
- Confidence, source pointers, and candidate status fields so extracted items do not masquerade as durable knowledge.
- Evolution proposals that update tags, context summaries, links, nearby notes, or existing observations when new evidence changes how older memory should be read.

## Evaluation Questions

- Does extraction distinguish strong corrections from weak discoveries?
- Are weak-oracle candidates prevented from gaining durable authority by default?
- Can new evidence update nearby old memory rather than only appending new records?
- Is distributed-parametric or policy learning limited to domains with sufficiently strong feedback?

---

Relevant Notes:

- [Trace-learning techniques in related systems] - surveys trace-mining systems across artifacts, policies, and procedures
- [Codification and relaxing navigate the bitter lesson boundary] - frames when learned policy can replace artifact-side control

## Under-review context phrase

the fail rung's signal-quality distinctions and candidate-status fields keep early-rung artifacts from being read as mature rules
