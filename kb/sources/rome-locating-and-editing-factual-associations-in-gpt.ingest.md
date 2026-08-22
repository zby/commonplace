---
description: "ROME localizes factual associations to mid-layer MLPs and edits them with a rank-one weight update — the nearest approach to our named explicit-retention falsifier, but it lacks scope-addressability"
source: https://arxiv.org/abs/2202.05262
captured: "2026-07-26"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: e71d53db9109b5331c646fcea42e3a4cb678d6ea8d32c1cc529af40405b4ad55
ingested: "2026-07-26"
type: kb/sources/types/ingest-report.md
domains: [learning-theory, artifact-analysis, self-improving-systems, interpretability]
---

# Ingest: Locating and Editing Factual Associations in GPT

## Classification

A NeurIPS 2022 archival research paper (Meng, Bau, Andonian, Belinkov) with a causal-intervention method, a new editing technique, a released evaluation dataset, and quantitative comparison against prior editors. It is empirical work with published code, not a position piece.
Author: David Bau's group with Yonatan Belinkov — a central and heavily replicated line in mechanistic interpretability. Strong credibility signal; the paper spawned the model-editing subfield, which also means the strongest criticisms of it come from inside that subfield.

## Summary

ROME asks where an autoregressive transformer stores a factual association such as "the Space Needle is in Seattle," and whether that store can be written to directly. The localization half uses *causal tracing*: corrupt the subject-token embeddings, then restore individual hidden states one at a time and measure which restorations recover the correct prediction. The decisive states cluster in mid-layer feed-forward (MLP) modules at the last subject token, which the authors read as a linear associative key-value store. The editing half, Rank-One Model Editing, exploits that reading: it solves for a rank-one update to a single MLP projection matrix that maps the subject key to a chosen value, requiring no gradient fine-tuning run. On zero-shot relation extraction ROME is comparable to prior editors; on CounterFact, a new dataset of counterfactual assertions the authors introduce, ROME is the only method that holds both *generalization* (paraphrases of the edited fact also change) and *specificity* (neighbouring unedited facts do not), where fine-tuning-style baselines buy one by sacrificing the other. Evaluated on GPT-2 XL and GPT-J. The paper's own conclusion is deliberately narrow — "direct manipulation of computational mechanisms may be a feasible approach for model editing" — and worth preferring over the broader "knowledge is localized" reading it is often given.

## Connections Found

This source's role in our KB is **the nearest published instance of a named falsifier**. [Only explicit retention is durable, writable, and addressable at once](../notes/only-explicit-retention-is-durable-writable-and-addressable.md) stakes its own currency on a falsifier it states but does not cite — "interpretability-grade editing under which a weight-encoded commitment can be individually retrieved, criticized, and revised" — and ROME is the closest existing approach to it, which is why the note's `Weights, with fine-tuning → Addressable: no` row should now read as a qualified default rather than a flat impossibility. [Theory-mediated learning may improve sample efficiency under structured shifts](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) already cites this paper by bare arXiv URL for exactly that qualification, and [Reflection makes retained lessons second-order](../notes/reflection-makes-retained-lessons-second-order.md) names "model editing" twice in load-bearing scope sentences without a citation.

The falsifier is only partially met, and the shortfall is the interesting part. ROME retrieves and revises a factual association, but a rank-one update carries no stated applicability boundary, so *rescoping* — the second-order operation [reflection buys addressability](../notes/reflection-buys-addressability.md) separates from mere revision — remains unavailable even where modification succeeds. Parametric editing therefore delivers content-addressability without scope-addressability, which refines the explicit-only retention claim into a two-property test rather than overturning it.

Two secondary roles. Against [Opacity is a scale threshold, not a class property](../notes/opacity-is-a-scale-threshold.md), ROME pushes the demonstrated parametric-inspection threshold past the "toy models" parenthetical that is currently the note's only support, though narrowly and for one class of computation. And against [Reflective coverage is graded across representational forms](../notes/reflective-coverage-is-graded-across-representational-forms.md), it is an external worked case of an observation-plus-modification operation profile over distributed-parametric state, which that note asserts is possible without exhibiting. [Representational form](../notes/definitions/representational-form.md) supplies the distributed-parametric category and the "probe behaviorally" default inspection rule that causal tracing partially displaces.

Among already-captured sources, this is the write-side counterpart to [Verbalizable Representations Form a Global Workspace](./verbalizable-representations-global-workspace-llms.ingest.md) and [Reading Between the Dots](./reading-between-the-dots-decoding-hidden-computation.ingest.md), which both *read* parametric state; ROME is the only one of the three that writes to it. [KBLaM](../agent-memory-systems/reviews/KBLaM.md) is the system-level comparison: both put KB-derived facts into model internals rather than context, and KBLaM's open question about source-to-weight lineage is precisely the maintenance problem direct editing creates.

## Extractable Value

1. **Content-addressability and scope-addressability come apart** — the highest-reach item, and it is a distinction our notes currently collapse. ROME can revise a stored association in place but exposes no applicability conditions to narrow, so "the commitment can be revised" and "the commitment can be rescoped" are separate properties with separate substrate requirements. This converts a binary falsifier into a graded test and applies well beyond model editing. [deep-dive]

2. **The specificity/generalization pair is a reusable metric for selective revision** — CounterFact operationalizes "did the edit reach the paraphrases" and "did it leave the neighbours alone" as two measurements that trade off. That is exactly the collateral-damage question [theory-mediated learning](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) lists among the things its proposed experiment must measure, and the pair transfers to natural-language-artifact revision without change. [experiment]

3. **A named, published citation for a claim our notes currently assert bare** — four notes reference model editing or interpretability-grade editing with no anchor. One capture discharges all four. [quick-win]

4. **Causal tracing is a localization method, not a licence to edit** — the paper's own method separates "where does the signal flow" from "where does an edit work," and the follow-up literature (below) found these do not coincide. The transferable lesson is that a causal-influence measurement does not by itself identify an intervention site. [deep-dive]

5. **Rank-one editing needs no training infrastructure** — the update is solved in closed form on a single matrix, which is why weight editing does not inherit the heavy-infrastructure property our comparisons attach to fine-tuning. Any cost argument that leans on "weight updates are expensive" should name whether it means gradient training or parametric writes in general. [just-a-reference]

6. **Direct editing creates a lineage problem with no format** — once weights can be written to from a knowledge source, invalidating or regenerating a parametric edit when the source record changes becomes a real obligation, and neither ROME nor KBLaM supplies a lineage format for it. [just-a-reference]

## Limitations (our opinion)

The snapshot itself is the first limitation, and it bounds everything below. This is an abstract-level web-fetch of a 35-page paper: no causal-tracing methodology detail, no CounterFact numbers, no baseline table. The snapshot's own `description` — "evidence that factual knowledge is stored as identifiable, editable computation rather than diffuse distributed representation" — is stronger than both the captured body and the paper's stated scope, and a note inheriting that phrasing would assert more than the capture preserves, [which a citation cannot do](../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md). Any note citing this ingest should restate the claim at the paper's strength: one class of subject-token factual association in two mid-size models, not knowledge in general.

What was not tested is more damaging than what was. The paper evaluates single edits on relational triples of the form (subject, relation, object). It does not test sequential editing, edits at scale, edits to non-factual dispositions, or whether an edited fact propagates to what it logically entails. Follow-up work found problems on each: Hase and colleagues ("Does Localization Inform Editing?") reported that causal-tracing localization correlates poorly with where an edit actually succeeds, which undercuts the paper's implied inference from *located here* to *editable here*; Cohen and colleagues on ripple effects found edited facts fail to propagate to entailed consequences, so the model ends up holding the new fact and its old implications simultaneously. Neither result is fatal to ROME as a technique, but together they mean the paper's localization story and its editing result are less tightly coupled than the framing suggests, and the "simpler account" worth taking seriously is that the rank-one update is a good editing heuristic whose success does not license the storage claim.

The hard-to-vary test also goes badly for the strong reading. "Facts are stored in mid-layer MLPs at the last subject token" is stated over a specific architecture, a specific probe, and a specific corruption scheme; change any of them and the localization result moves. That is characteristic of a finding indexed to its measurement rather than a mechanism that must hold.

For our purposes the decisive limitation is that ROME does not close the addressability gap it appears to. Editing a weight-encoded fact is not the same as being able to state what was retained, why, and where it stops applying. Nothing in the edit is retrievable as a criticizable commitment, and nothing carries an applicability boundary. So the falsifier in [only explicit retention](../notes/only-explicit-retention-is-durable-writable-and-addressable.md) is approached, not met, and the honest revision to that note is a qualification of its `Addressable: no` row, not a re-derivation of everything downstream. Finally, the authors have an interest in the localization framing — it is what makes the editing method look principled rather than empirical — and the strong reading has been repeated far past what the evidence carries.

## Recommended Next Action

Qualify the `Weights, with fine-tuning → Addressable: no` row in [only explicit retention is durable, writable, and addressable at once](../notes/only-explicit-retention-is-durable-writable-and-addressable.md) to record that parametric editing reaches content without reaching scope, citing this ingest — the note names interpretability-grade editing as its own falsifier without citing anything, and ROME approaches that falsifier without meeting it. The content-versus-scope distinction is carried at abstract-level fidelity; a full-text capture would be needed before leaning on the specificity/generalization numbers.
