---
description: "Every tacit retention form — in-context conditioning, weights under selection or fine-tuning, human expertise — fails addressability, so governed retention currently runs through explicit artifacts"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, synthesis]
tags: [learning-theory, self-improving-systems, agent-memory]
---

# Only explicit retention is currently durable, writable, and addressable at once

A system that learns during operation must retain what it learned in some form, and the candidate forms differ on three properties that decide whether the retention can be governed. **Durability**: the retention survives the session or run that produced it. **Writability**: the system's own operation can change it. **Addressability**: processes inside the boundary can treat a retained commitment as an object — retrieve it, say what it claims, criticize it, revise it selectively, carry it to a new problem — since [reflection buys addressability](./reflection-buys-addressability.md). Cutting across all three is the tacit/explicit divide of [representational form](./definitions/representational-form.md): explicit forms (prose, symbolic) encode commitments readably; tacit forms (distributed-parametric state, conditioned context state, embodied human expertise) encode competence that cannot be read out as commitments.

| Retention form | Durable | Writable | Addressable |
|---|---|---|---|
| In-context conditioning | no — dies with the session | yes — every token writes it | no — the transcript is addressable; the competence it induces is not |
| Weights, selection-only profile | yes | no — swapping the sealed component is the only lever | no |
| Weights, with fine-tuning | yes | yes | no — no per-commitment retrieval, criticism, selective revision, or rollback |
| Human expertise | yes | yes — practice writes it | no — stable, perhaps, but not inspectable, diffable, or transferable |
| Explicit artifacts (prose, symbolic) | yes | yes | yes |

Addressability here is comparative, not absolute — the reflection note is explicit that opaque retention still admits indirect handles (behavioral probing, wholesale rollback, retraining, steering). The column records whether any handle operates on the retained commitment *as an object*, and for every tacit row the answer is no.

Two rows deserve unpacking. **In-context conditioning looks explicit because its medium is text.** But the readable transcript and the induced competence are different objects: no sentence of the transcript contains the calibration the whole context conditions into the model, so the competence cannot be excerpted, revised, or transferred sentence-wise — the transcript is the explicit trace of a tacit state. **Fine-tuned weights and human expertise fail the same property**, and the symmetry is the point: both are durable, writable (by training, by practice), and rich, and in neither can a single retained commitment be diffed, cited, criticized, or rolled back. Verification collapses to behavioral probing in both cases, exactly as the per-form review obligation in [reflective coverage](./reflective-coverage-is-graded-across-representational-forms.md) predicts for the parametric form. So when [methodological closure](./methodological-and-computational-closure-track-different-changes.md) declines to count a maintainer's tacit-but-stable criterion as retained methodology, and when a knowledge system declines to retain lessons by fine-tuning, they apply one criterion, not two special rules: closure and governance read the addressable channel.

## Externalization is the transport, not a preliminary

The conversion of a human-held decision to computational execution puts settlement — making the criterion explicit — before allocation. The table shows that ordering is forced, twice over. In a system whose [operation profile](./reflective-coverage-is-graded-across-representational-forms.md) over the parametric form is selection-only, explicit artifacts are the only durable *writable* channel there is: nothing else inside the boundary can receive the criterion at all. And even where fine-tuning adds parametric writability, the transfer is unaddressable — what was allocated can no longer be stated, reviewed, or revised as a commitment, so the allocation escapes governance at the moment it succeeds. Either way, a criterion moves to a computational actor only through an explicit representation. Externalization is the transport mechanism of allocation, not preparation for it.

## The claim is current, and its falsifier is named

This is an empirical claim about existing substrates, so its application to a particular system should be stated as a profile line over the parametric form, not as a fact about technology at large — [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) records a selection-only line, and everything this note forces (explicit-only retention, externalization as transport) is downstream of that line. What would break the claim is not more writability: fine-tuning exists now, and continual-learning pipelines only add write channels. The falsifier is addressability of a tacit form — interpretability-grade editing under which a weight-encoded commitment can be individually retrieved, criticized, and revised. A system whose profile line crosses that boundary owes every artifact derived from this claim a re-derivation.

## Scope

- Not a ranking. Tacit forms hold what explicit ones cannot: the residue — calibration, situational feel, style — that resists articulation and is often the competence that matters. The trade runs both ways, and the consequences for what to retain in which form are developed in [retaining the episode keeps a distilled rule re-derivable](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md).
- Retention through an actor the system neither observes nor selects — a provider training on usage data — is excluded: whatever returns through later model versions is not a retention pathway of the system, and no property in the table applies to it.

## Open Questions

- Whether behavioral probing, evals, and activation steering constitute a graded middle — partial addressability worth naming — or stay indirect handles in kind.
- Host binding: the tacit-knowing literature (Polanyi's "we know more than we can tell"; Nonaka's externalization step) is the natural host for the tacit/explicit side of this claim. Inheritance is deferred until the sources are ingested and a canonical statement chosen.
- Whether the conditioned-state/transcript split recurs often enough to need a registered term.

---

Relevant Notes:

- [Reflection buys addressability](./reflection-buys-addressability.md) — grounds: defines addressability and its comparative reading; this note extends the comparison across all current retention forms
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — grounds: the operation-profile vocabulary the frame-indexed corollary is stated in, and the per-form verification obligation the tacit rows collapse to
- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — extends: supplies the shared ground for its tacit-expertise and substrate-dependency resolutions
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — extends: adds the addressability property and the human row to its three-timescale media comparison
- [Retaining the episode keeps a distilled rule re-derivable](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md) — extends: what the explicit-only regime should retain in which explicit form
- [Representational form](./definitions/representational-form.md) — defined-in: the prose / symbolic / distributed-parametric axis the tacit/explicit divide runs across
- [Retained artifact](./definitions/retained-artifact.md) — defined-in: the umbrella term for durable behavior-shaping state this note's rows instantiate
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: the recorded selection-only profile line this claim's application rests on
