---
description: "A derivation that is a function of its source makes a cache, repaired by recompute; a derivation that arbitrates among admissible outputs makes new ground truth at commit, repaired by supersession"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [kb-maintenance, learning-theory, constraining]
---

# A derived artifact is a cache only if its derivation is a function

"Derived" names two relations that behave oppositely under maintenance, and one word for both hides the split. The discriminator is whether the derivation is a **function** of the source — a map from source state to artifact that any conforming re-derivation reproduces. When it is, the artifact is a cache: the source stays ground truth, the copy is redundant, and it can be re-derived on demand. When it is not — when the derivation resolves a free choice among admissible outputs — nothing recovers the artifact from the source. At the moment it is committed the artifact **becomes** ground truth for what it records, and its raw material demotes to provenance.

Everything operational follows from that one property, because recompute is the repair the cache regime is built on and the projection regime cannot borrow it.

## The discriminator is arbitration, not loss

The tempting reading is that caches hold all the information and projections lose some. That reading is wrong, and getting it wrong misfiles most real cases. A hash is extremely lossy and still a perfect cache: re-run it and you get the same digest. A deterministic truncation is lossy and still a cache. Loss is orthogonal; what matters is whether the source *determines* the output.

The mechanism is the projection-versus-compilation distinction, since [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md): a compiler aims at a unique semantics for a fixed program, so any divergence counts as a bug, while a natural-language spec admits a space of valid readings and the interpreter collapses that space to one. A cache's derivation has the compiler's aim. A projection has no such aim — and crucially, no fact about the source picks out which reading got committed. Recompute needs exactly that fact. Its absence, not information loss, is what makes the projection regime a different regime.

This is also why implementation determinism does not deliver the property. An LLM at temperature zero returns the same output every time, and its output is still not a function of the source: it is a function of source *plus* model, prompt, decoding settings, and runtime, and no other conforming interpreter is expected to preserve it. Pinning the arbiter reproduces one arbitration; it does not make the source determine the answer. Freezing indeterminism and resolving underspecification are separate moves, and only the second would convert the regime.

## Whoever holds the free choice is the committer

The projection side is usually described as an LLM problem, but the arbiter's substrate is not what the argument uses. Anything that resolves the free choice occupies the same position:

- **A human accepting a decision.** Nothing in a design proposal determines which option wins. The deciding *is* the arbitration, which is why an accepted ADR is not a cache of the proposal it adopted — re-reading the proposal does not regenerate the decision.
- **A human attesting.** `user-verified: true` is not recomputable from the note it sits on; the attestation is a fact about a person's judgment, added from outside the text. That is precisely why a substantive edit must strip it and why it can only be re-granted explicitly — the field is a committed projection wearing a frontmatter field's clothes, and treating it as a checkable mark would be the category error below.
- **A human keeping a good output.** [Storing an LLM output is constraining](./storing-llm-outputs-is-constraining.md): the selection resolves the underspecification. The generator produced the candidate; the keeping produced the artifact.

So the claim states in terms of the derivation, not the deriver. A generated index and a promoted synthesis note differ in kind even though both are produced by running something over a source, and an ADR and a completeness [mark](../types/tag-readme.md) differ in kind even though both are authored by hand.

## The maintenance and disposal split

|  | recomputable cache | committed projection |
|---|---|---|
| derivation | function of source state | arbitration over admissible outputs |
| source after derivation | ground truth | provenance |
| maintenance rule | checked-or-absent | supersession |
| repair on drift | recompute | a new commitment naming the old |
| deletion cost | one bounded recomputation | irrecoverable information loss |
| worked instances | marks, generated indexes, duplicated build assets | ADRs, notes promoted from workshops, verification attestations |

Three consequences do real work.

**Enforce-or-omit is a cache-regime rule.** [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) rides on the deletion column: absence costs a recomputation, a false copy costs silent unbounded wrongness, so hand-maintained-and-trusted is forbidden. Read the columns and its own precondition 1 — mechanical re-derivability — is this note's discriminator stated as an availability condition. Push the rule across the boundary and it degenerates: with no derivation to check against, "checked or absent" reduces to "absent", which deletes the only copy of something no source recovers. The rule is not weaker in the projection regime; it does not apply there.

**Supersession is a projection-regime rule, and demanding it of a cache is over-ceremony.** You do not write a decision record to regenerate an index. Supersession exists because a superseded commitment is not wrong-relative-to-a-source — it was the ground truth for its moment, and only a later commitment can displace it. That is history, and history is not re-derivable.

**The regimes predict disposal, and the KB's own two disposal decisions split along the line.** Committed generated indexes were deleted outright and regenerated at build time from note frontmatter ([ADR 025](../reference/adr/025-complete-generated-indexes-are-build-time-only.md)) — safe, because the function survives the file. Adopted proposals were archived rather than deleted ([ADR 056](../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md)) — because a proposal's option space, forces, and free choices are themselves a committed projection of a design conversation, and adoption does not turn the proposal into a cache of its ADR. Two originals, neither recomputable from the other, so the only live question is attention tier rather than existence. The two decisions were reached independently, on different artifact kinds, and neither invoked this distinction; that they land on opposite operations exactly where the discriminator says they should is what makes it more than a relabelling of the cases that produced it.

## Regime membership attaches to the region, not the file

A tag-README carries curated editorial prose *and* validator-enforced `complete`/`covered_by` marks. The marks are caches; the curation is a commitment. Both live in one file, and the file's disposal behaviour is per-region: dropping a mark costs a reader one scoped sweep, dropping the curation destroys editorial judgment nothing re-derives. This is why [ADR 026](../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) could put a validator behind the marks without pretending to validate the prose around them. When classifying, ask which regime a given *claim inside* an artifact belongs to; the file is often mixed.

## The boundary is crossable in one direction

A projection can be promoted into the cache regime by codifying its arbitration — which is what [progressive constraining](./progressive-constraining-commits-only-after-patterns-stabilize.md) does: observe which reading stabilizes across many runs, then commit that reading to something with precise semantics. Afterwards the derivation is a function and recompute becomes available. The reverse move buys nothing: relaxing a functional derivation into a judged one forfeits the repair operation and gains only tolerance for inputs the function could not handle, which is sometimes worth it and never a maintenance improvement.

So the split is not a taxonomy of artifacts but a property of derivations, and a system can move a derivation across it deliberately. That also bounds the promotion: until the arbitration is actually codified, calling the artifact a cache is aspiration, and the aspiration is the exact failure mode enforce-or-omit warns about — a trusted copy with no check behind it.

## Scope

- **Semantic re-derivation is not recompute.** [Retaining the episode keeps a distilled rule re-derivable](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md) in the sense that a reader can go back to the evidence and judge whether the generalization survives. That is real recourse, and it is a *fresh arbitration* over retained provenance, not the recovery of a lost artifact. It may disagree with what it re-examines; a recompute cannot.
- **The general managed-staleness regime covers the projection side.** [Lineage recorded at the source](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) surfaces downstream artifacts when a source changes, with judgment doing the verification. This note does not add machinery there; it says why that machinery cannot be replaced by a validator on that side of the line.
- **Neither regime is better.** The claim is that the maintenance operations are not interchangeable, not that functional derivations should be preferred where a judgment is what the work needs.
- **A functional derivation still needs its ground truth to exist at check time.** Where the source is destroyed or was never recorded, recompute is unavailable in practice even though the derivation is a function — [history has one chance to become checkable](./history-has-one-chance-to-become-checkable.md).

## Open Questions

- Is there a third regime for derivations that are functions of the source *plus* evidence the run itself generates? Such an artifact is reproducible only by re-running the world, which is neither recompute nor supersession.
- Does anything checkable distinguish the two regimes, or must membership always be declared? A validator can confirm a claimed derivation reproduces its copy, but nothing detects a projection misfiled as a cache except its first silent mismatch.
- What retires a committed projection when no successor commitment is coming — the case where a note simply stops being true and no one has decided what replaces it?

---

Relevant Notes:

- [Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — grounds: the projection-versus-compilation distinction that supplies the discriminator, including why temperature-zero determinism does not convert the regime
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — extends: names the applicability boundary its precondition 1 states as an availability condition, and shows the rule degenerating rather than weakening across that boundary
- [Storing LLM outputs is constraining](./storing-llm-outputs-is-constraining.md) — grounds: the commitment-as-constraining move that makes a kept output the new ground truth rather than a cache of its prompt
- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — mechanism: how a derivation crosses from arbitration into function, making recompute available afterwards
- [Retaining the episode keeps a distilled rule re-derivable](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md) — contrasts: its re-derivability is a fresh arbitration over retained provenance, which may disagree with what it re-examines, unlike a recompute
- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — grounds: the managed-staleness machinery that governs the projection side, where verification stays judgment
- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — contrasts: the case where the derivation is a function but the ground truth needed to run it no longer exists
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: why a cache is worth materializing at all, given that its content is recoverable by definition
- [Constraining](./definitions/constraining.md) — defined-in: the narrowing operation that commitment performs
- [ADR 056: adopted and retired proposals archive out of the frontier](../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) — evidence: chose archiving over deletion for adopted proposals, the projection-side disposal operation this note predicts
- [ADR 025: complete generated indexes are build-time only](../reference/adr/025-complete-generated-indexes-are-build-time-only.md) — evidence: deleted committed generated listings outright and regenerated from frontmatter, the cache-side disposal operation
- [ADR 026: tag-readme type with completeness and coverage marks](../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) — evidence: the mixed artifact, with a validator behind the cached marks and none behind the curated prose beside them
