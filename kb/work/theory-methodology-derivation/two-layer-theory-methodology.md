# The two-layer theory–methodology structure

The core thread: the general pattern the [source passage](./source-passage.md) gestured at, stated in KB vocabulary. This is the likely primary durable note.

## The structure

A **generator theory** and a **derived methodology** form a two-layer execution system:

- The methodology is derived from the theory and shaped for action: cheaper to execute, strictly less general. It handles the covered region of cases.
- The theory is retained and shipped *with* the methodology, not archived after derivation. Corner cases — inputs outside the methodology's covered region — are handled by dropping back to the theory and re-deriving from first principles. This is an expected operation, not a failure.
- Recurring corner cases are the learning signal: when the same re-derivation happens repeatedly, its result is promoted into the methodology. The methodology grows at its boundary, driven by use.

Three claims from the source passage, kept close to their original form:

1. Theory and methodology have a generator–derivative relationship: derived, cheaper, strictly less general.
2. The theory ships with the methodology because the corner-case distribution is open-ended — the methodology never converges to covering it. Fallback only works if the executing agent actually understands the theory.
3. Promotion has a testable criterion: a corner case is promoted when its handling no longer requires consulting the theory — checkable by whether the agent resolves it from the methodology alone.

## Why this is a new note and not a restatement

The KB has the two directions for the *code* case — [codification and relaxing](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — but there the general-purpose fallback layer is the LLM itself, always present for free. Here the general layer is a *retained artifact* that is too costly to apply per-case yet must be kept, understood, and maintained. Distillation names the operator that produces the methodology, but nothing names the runtime architecture: fast path, fallback semantics, promotion at the boundary.

The relationship to spec mining inverts the current framing. [Spec mining](../../notes/spec-mining-as-codification.md) already notes that "the maturation trajectory is spec mining applied to methodology" — but keeps spec mining primary and methodology as the analogy. The two-layer structure is the general idea; spec mining and the [maturation trajectory](../../notes/methodology-enforcement-is-constraining.md) are the special cases where promotion crosses the codification line into a symbolic artifact. In the general case the methodology stays prose and the promotion is prose-to-prose.

## Physics vocabulary for the moving parts

From the [effective-theory thread](./effective-theory-borrowing.md), the useful loans:

- **matching** — the promotion step: compute the corner case in the full theory at the boundary, commit the result into the methodology, never recompute
- **cutoff** — the declared validity boundary: a good methodology states its own breakdown region rather than having it discovered by failure
- **correspondence** — the constraint running the other way: a revised theory must reproduce the established methodology on its home turf, or one of them is wrong

## The derivation bet (operator position)

Creating the derived layer at all is a bet — and it is a *coverage* bet, not a correctness bet: **simplifying a big theory into an effective one is warranted only if the cases where the simplification still applies are frequent enough to pay for the complication.** The complication is real and ongoing: a second artifact to build, maintain, keep consistent with its generator (matching, correspondence), and route around. The payoff structure is cache economics: per-case savings × hit rate against build cost + upkeep + staleness risk + routing overhead.

This is distinct from the existing "every codification is a bet" (which is about *correctness* — is the extracted regularity load-bearing or a proxy theory?). The two bets fail differently and are detected differently:

- The correctness bet fails by **wrongness**: the artifact breaks under distribution shift — detected by relaxing signals (paraphrase brittleness, isolation-vs-integration gaps).
- The coverage bet fails by **uselessness**: the artifact is right but rarely applicable — most real cases fall outside its cutoff, so you pay for two layers while living in the expensive one. Detected by the **fallback rate**: if corner-case traffic to the general layer stays high, the effective theory isn't earning its keep. That makes the bet measurable, ongoing, and adjudicated by use — not by review.

Each individual promotion is a miniature of the same bet: is *this* corner case recurrent enough to promote? The source passage's "recurring corner cases are the learning signal" is exactly the evidence-gathering that de-risks the mini-bet — promote on recurrence, not on first occurrence. The KB already runs this doctrine in miniature: YAGNI, and the quality bar's "worth a log entry on first occurrence and a note when the mechanism is understood." Physics runs it too: an effective theory gets constructed for regimes physicists actually live in (thermodynamics exists because macroscopic equilibrium is ubiquitous), not for every derivable slice.

In the [polation thread](./polation-structure-of-generalization.md)'s hull language: the coverage bet is a bet about where the *future query distribution* lies relative to the distillate's hull. (A different, assistant-proposed bet — classifying a mixed artifact by its dominant regime — lives in the [vocabulary thread](./derivation-selection-vocabulary.md); that one is about where an artifact's *claims* lie relative to its source. Same geometry, different random variable.)

## Caveat: mixed artifacts

Batterman's singular-limits point (see the effective-theory thread) suggests real methodologies are mixed: partly derived from the theory (recomputable, checkable by matching), partly organizing concepts that exist only at the methodology's level of description (load-bearing, needing semantic review). The derived/non-derived split *within one artifact* determines which maintenance regime each part gets — that is itself a testable claim, and it connects to the [vocabulary thread](./derivation-selection-vocabulary.md)'s gradedness caveat.

## Open questions

- Is the note one claim ("theory and methodology form a two-layer execution system with fallback and promotion") or two (the structure; the open-endedness argument for why the theory can never be discarded)?
- Does the promotion criterion (claim 3) belong in the note or as a separate review-gate-shaped artifact once someone actually wants to measure it?
- Terminology depends on the [vocabulary thread](./derivation-selection-vocabulary.md): "generator–distillate" vs "generator–derivative".

---

Working links:

- [spec mining as codification](../../notes/spec-mining-as-codification.md) — extends: this workshop generalizes its methodology-level aside into the primary structure
- [codification and relaxing navigate the bitter lesson boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — contrasts: same promote/demote dynamics, but with the LLM (not a retained theory artifact) as the general layer
- [methodology enforcement is constraining](../../notes/methodology-enforcement-is-constraining.md) — instance: the instruction → skill → script trajectory is the symbolic-crossing special case of promotion
- [constraining and distillation both trade generality for reliability](../../notes/constraining-and-distillation-both-trade-generality-for-reliability.md) — grounds: the trade the fast path makes
- [first-principles reasoning selects for explanatory reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: reach is what the theory layer contributes; the passage's "the theory is the reach"
- [distillation](../../notes/definitions/distillation.md) — defined-in: the operator that produces the methodology
