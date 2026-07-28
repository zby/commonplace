---
description: "Derivation — claims recoverable from the source, nothing added — leaves the source as ground truth; what adds unentailed resolutions becomes ground truth at commit, repaired by supersession"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [kb-maintenance, learning-theory, constraining]
---

# Commitment, not derivation, creates new ground truth

An artifact produced from source material stands in one of two relations to it, and this KB's [lineage vocabulary](../reference/link-vocabulary.md) keeps them apart deliberately. **Derivation**, in the narrow registered sense, means the artifact's substantive claims are recoverable from the source plus its declared consumer goal — nothing added. Every other production adds something the source does not determine: a generalization beyond the evidence, a decision among live options, one reading selected from a space of admissible ones. Call the act that fixes such an addition in a retained artifact a **commitment**.

The claim: this boundary settles which artifact is ground truth afterwards. A derived artifact leaves its source as ground truth and remains a dependent copy — when the source revises, the copy is stale and re-derivation is authoritative. A committed artifact *becomes* ground truth for what it adds, at the moment of commitment, and its raw material demotes to provenance. The maintenance and disposal consequences follow from that inversion, because every recompute-style repair assumes the source still holds the answer — and on the commitment side it never does.

## The discriminator is what gets added, not what gets lost

The tempting reading is that derivation keeps the information and commitment loses some. That reading is wrong, and getting it wrong misfiles most real cases. A hash is extremely lossy and fully derived: the source determines the digest, and any conforming re-derivation reproduces it. Loss is orthogonal; what matters is whether the source *determines* the artifact's substantive content.

The clearest modern case is generated code. Since [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md), a natural-language spec admits a space of valid programs and the model collapses that space to one — a projection, not a compilation. Every resolution the spec left open arrives in the output as content the source does not entail, and no fact about the spec records which resolutions were taken. Kept code is therefore not derived from its prompt; it is a committed interpretation of it — which matches how such artifacts are actually treated: the code, not the prompt, is what gets debugged, maintained, and trusted.

Determinism of the producer does not move this line. An LLM at temperature zero returns the same output every time, and the output's unentailed content is still unentailed — it is fixed by source *plus* model, prompt, decoding, and runtime, not by the source. Pinning the arbiter reproduces one arbitration; it does not make the source determine the answer. Freezing indeterminism and resolving underspecification are separate moves, and only content the source determines is derived.

## Whoever resolves the free choice is the committer

The commitment side is usually discussed as an LLM phenomenon, but the argument never uses the arbiter's substrate — and in this KB the committer is very often a person. Anything that resolves the free choice occupies the same position:

- **A human accepting a decision.** Nothing in a design proposal determines which option wins; the deciding *is* the addition. An accepted ADR is therefore not derived from the proposal it adopted — re-reading the proposal does not regenerate the decision. The [discovery lifecycle](./definitions/discovery-lifecycle.md) names this phase exactly: acceptance is *gated commitment*, a consuming workflow's recorded judgment that evidence meets a criterion — a fact about the judgment, not a consequence of the evidence.
- **A human attesting.** `user-verified: true` is recoverable from nothing in the note it sits on; it records a person's judgment, added from outside the text. That is why a substantive edit must strip it and only an explicit act can re-grant it — the field is a commitment wearing a frontmatter field's clothes, and treating it as a checkable mark would be the category error described below.
- **A human keeping a good output.** [Storing an LLM output is constraining](./storing-llm-outputs-is-constraining.md): the generator produced candidates, and the keeping resolved which one becomes the artifact.

So the claim classifies productions, not producers. A generated index and a promoted synthesis note differ in kind though both are machine-produced; an ADR and a completeness [mark](../types/tag-readme.md) differ in kind though both are authored by hand.

## Two boundaries, three zones

Derivation itself is graded, and the grading must not be confused with the commitment boundary. [Methodology and its theory form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) splits derived content by verification method: **mechanical** fragments, where a machine re-derives and a validator compares — these are recomputable copies proper — and **judgment-checked** derived natural-language, where the claims are recoverable from the source but re-derivation and comparison take judgment, so the regime is managed staleness rather than a deterministic check.

Both zones sit on the derivation side of the ground-truth question: a judgment-checked summary that restates its source in new words has added no claims, and when the source revises, the summary is stale and the source wins. The commitment boundary is different in kind, not merely harder to check — on its far side the artifact outranks its raw material, and "stale against the source" stops being a meaningful state because the source was never the authority for what was added.

Keeping the two boundaries apart prevents two opposite misfilings: judgment-checked derivation mistaken for commitment (it is not — nothing was added, and the source remains authoritative), and a committed artifact mistaken for a checkable copy (there is no derivation to check it against).

## The maintenance and disposal split

|  | derivation | commitment |
|---|---|---|
| substantive content | recoverable from source plus declared consumer goal | includes resolutions the source does not determine |
| ground truth after production | the source | the artifact; source demotes to provenance |
| maintenance rule | checked-or-absent where mechanical; managed staleness where judgment-checked | supersession |
| repair on drift | recompute, or judged re-derivation | a new commitment naming the old |
| deletion cost | recomputation work — bounded and mechanical, or dear but claim-preserving | irrecoverable loss of the only record |
| worked instances | marks, generated indexes, duplicated build assets; derived summaries and reshaped natural-language | ADRs, notes promoted from workshops, verification attestations, kept generated code |

Three consequences do real work.

**Enforce-or-omit is a mechanical-zone rule.** [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) rides on the deletion column: absence costs a recomputation, a false copy costs silent unbounded wrongness, so hand-maintained-and-trusted is forbidden. Its precondition 1 — mechanical re-derivability — is the mechanical zone's admission test stated as an availability condition. Pushed past the commitment boundary the rule degenerates rather than weakens: with no derivation to check against, "checked or absent" reduces to "absent", which deletes the only copy of something no source recovers. The rule is not weaker there; it does not apply there.

**Supersession is a commitment rule, and demanding it of a derivation is over-ceremony.** You do not write a decision record to regenerate an index. Supersession exists because a superseded commitment is not wrong-relative-to-a-source — it was the ground truth for its moment, and only a later commitment can displace it. That is history, and history is not re-derivable.

**The boundary predicts disposal, and the KB's own two disposal decisions split along it.** Committed generated indexes were deleted outright and regenerated at build time from note frontmatter ([ADR 025](../reference/adr/025-complete-generated-indexes-are-build-time-only.md)) — safe, because the derivation survives the file. Adopted proposals were archived rather than deleted ([ADR 056](../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md)) — because a proposal's option space, forces, and free choices are themselves committed records of a design conversation, and adoption does not make the proposal derivable from its ADR. Two originals, neither recoverable from the other, so the only live question is attention tier rather than existence. The two decisions were reached independently, on different artifact kinds, and neither invoked this distinction; that they land on opposite operations exactly where the boundary says they should is what makes it more than a relabelling of the cases that produced it.

## Regime membership attaches to the region, not the file

A tag-README carries curated editorial prose *and* validator-enforced `complete`/`covered_by` marks. The marks are mechanical derivations; the curation is a commitment. Both live in one file, and the file's disposal behaviour is per-region: dropping a mark costs a reader one scoped sweep, dropping the curation destroys editorial judgment nothing re-derives. This is why [ADR 026](../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) could put a validator behind the marks without pretending to validate the prose around them. The [lineage vocabulary](../reference/link-vocabulary.md) handles the same fact at the artifact scale by labelling a mixed artifact by its dominant regime — an explicit, revisable call. When classifying, ask which regime a given *claim inside* an artifact belongs to; the file is often mixed.

## The boundary is crossable by committing once

A recurring arbitration can be retired by codifying it — which is what [progressive constraining](./progressive-constraining-commits-only-after-patterns-stabilize.md) does: observe which resolution stabilizes across many runs, then commit that resolution to an artifact with precise semantics. The codified artifact is itself a commitment — it becomes the new source — but everything regenerated from it afterwards is derivation, with recompute available as the repair. Commit once, derive thereafter. The reverse move — relaxing a codified rule back into judgment — reopens the free choice and forfeits the repair, which is sometimes worth it and never a maintenance improvement.

That also bounds the promotion: until the arbitration is actually codified, treating its outputs as derived is aspiration, and the aspiration is the exact failure mode enforce-or-omit warns about — a trusted copy with no check behind it.

## Scope

- **Judged re-derivation is not recompute, and re-examination is neither.** Re-deriving judgment-checked natural-language reproduces claims in possibly different words; it stays inside derivation. [Retaining the episode keeps a distilled rule re-derivable](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md) describes a third thing: going back to the evidence behind an *abstracted* — committed — rule and judging whether the generalization survives. That is real recourse, and it is a fresh arbitration over retained provenance which may disagree with what it re-examines; a recompute cannot.
- **The managed-staleness machinery is taken as given.** [Lineage recorded at the source](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) surfaces downstream artifacts when a source changes, with judgment doing the verification for the non-mechanical zone. This note adds no machinery there; it says why nothing on the commitment side can be repaired by that machinery or any validator.
- **Neither relation is better.** The claim is that the maintenance operations are not interchangeable, not that derivation should be preferred where a judgment is what the work needs.
- **A derivation still needs its ground truth to exist at check time.** Where the source is destroyed or was never recorded, recompute is unavailable in practice even though nothing was added — [history has one chance to become checkable](./history-has-one-chance-to-become-checkable.md).

## Open Questions

- Is there a third relation for artifacts determined by the source *plus* evidence the run itself generates? Such an artifact adds nothing by judgment, yet is reproducible only by re-running the world — which is neither recompute nor supersession.
- Does anything checkable distinguish the relations, or must membership always be declared? A validator can confirm a claimed derivation reproduces its copy, but nothing detects a commitment misfiled as a derivation except its first silent mismatch.
- What retires a commitment when no successor commitment is coming — the case where a note simply stops being true and no one has decided what replaces it?

---

Relevant Notes:

- [Link vocabulary and linking approach](../reference/link-vocabulary.md) — evidenced-by: the registered narrow semantics of `derived-from` (nothing added) against the ampliative lineage labels; this note supplies the mechanism behind that boundary and its ground-truth consequence
- [Discovery lifecycle](./definitions/discovery-lifecycle.md) — grounds: the entailed-reshaping exclusion that keeps derivation out of the conjecture path, and acceptance as gated commitment — the human committer named as a lifecycle phase
- [Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — grounds: the projection-versus-compilation distinction behind the generated-code case, including why temperature-zero determinism does not entail the additions
- [Methodology and its theory form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — grounds: the mechanical / judgment-checked grading inside derived content that this note distinguishes from the commitment boundary
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — extends: locates its rule as the mechanical zone's enforcement rule and shows it degenerating rather than weakening past the commitment boundary
- [Storing LLM outputs is constraining](./storing-llm-outputs-is-constraining.md) — grounds: the keeping-as-commitment move that makes a kept output the new ground truth rather than a dependent copy of its prompt
- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — mechanism: how a recurring arbitration is committed once into a codified source, after which production from it is derivation
- [Retaining the episode keeps a distilled rule re-derivable](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md) — contrasts: re-examining a committed generalization against its retained evidence is a fresh arbitration that may disagree with it, unlike a recompute
- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — grounds: the managed-staleness machinery that governs derivation's judgment-checked zone
- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — contrasts: the case where nothing was added but the ground truth needed for recompute no longer exists
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: why the dear-but-claim-preserving deletion cost of judged derivation still differs in kind from the irrecoverable loss of a commitment
- [Constraining](./definitions/constraining.md) — defined-in: the narrowing operation commitment performs
- [ADR 056: adopted and retired proposals archive out of the frontier](../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) — evidenced-by: chose archiving over deletion for adopted proposals, the commitment-side disposal operation this note predicts
- [ADR 025: complete generated indexes are build-time only](../reference/adr/025-complete-generated-indexes-are-build-time-only.md) — evidenced-by: deleted committed generated listings outright and regenerated from frontmatter, the derivation-side disposal operation
- [ADR 026: tag-readme type with completeness and coverage marks](../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) — evidenced-by: the mixed artifact, with a validator behind the derived marks and none behind the committed natural-language beside them
