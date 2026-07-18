# Workshop: Adaptation vocabulary and lineage relations

## Question

How should Commonplace restore a general source-to-target relation for consumer-directed artifact transformation without weakening the narrow, claim-preserving meaning of the formal `derived-from` relation?

The change should let the KB speak naturally about adapting material across theoretical, descriptive, prescriptive, dialectical, and generated artifacts while keeping formal lineage assertions precise enough to carry maintenance consequences.

## Trigger

The [theory–methodology derivation workshop](../theory-methodology-derivation/README.md) retired *distillation* after finding that it had been used for both claim-preserving derivation and claim-amplifying discovery. That split fixed a real authority ambiguity, but the migration also removed the broader relation the old term had carried: a target artifact can be made by selecting, reorganizing, reframing, compressing, expanding, or changing the register of source material for a downstream use.

The replacement vocabulary then made `derived-from` / `abstracted-from` depend on substantive-claim reconstructibility. That distinction fits theoretical artifacts, but it does not by itself describe transformations such as methodology to procedure, repository to descriptive review, sources to dialectical map, session state to handoff, or canonical files to a generated projection.

## Settled starting point

These are operator decisions carried into the workshop, not questions to reopen without contrary worked evidence:

- **Adapt / adaptation is the preferred semi-technical prose.** Use the ordinary word consistently and extensively for reshaping source material toward a target use, without giving bare *adapt* a special formal definition or trying to prevent every broader ordinary-language use.
- **Registered hyphenated identifiers carry the formal meanings.** `adapted-from`, `derived-from`, `abstracted-from`, and any later siblings are controlled relation names when used in relation position. The spaced phrases *adapted from* and *derived from* remain ordinary prose. This composes the two strongest collision-control devices from [vocabulary collisions are prevented at write time, not resolved at read time](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) — rare compound token plus schema-defined link-label slot — rather than inventing a new one.
- **`adapted-from` is the general relation under consideration.** It records that the source was a material input to an intentionally use-shaped target. By itself it should not assert claim preservation, claim amplification, completeness, or mechanical reproducibility.
- **`derived-from` keeps its narrow meaning.** Where the formal relation applies, the target's substantive claims must be reconstructible from the source plus declared premises or consumer goal.
- **The design need not be taxonomically pure.** The goal is a useful, stable distinction with honest boundaries, not a complete ontology of every transformation.

## Placement direction

The working direction deliberately uses several surfaces at different resolutions:

1. `AGENTS.md` carries the always-loaded convention separating semi-technical prose from registered relation identifiers.
2. `kb/reference/link-vocabulary.md` carries the canonical semantics, relationship among labels, articulation tests, and maintenance consequences.
3. Each source collection's `COLLECTION.md` remains authoritative about which relations its artifacts may assert toward which destination collections, with a locally sufficient one-line truth test.

This is intentional frontloading rather than three competing authorities. The workshop must make the synchronization boundary explicit and decide whether the shipped `AGENTS.md.template` needs a generic version of the convention or whether it remains specific to this KB.

## Evaluation boundary

Evaluate the vocabulary against at least these shapes before adopting it:

| source → target | pressure on the model |
|---|---|
| theory → methodology | strict derivation may apply; operational choices may not be entailed |
| methodology → skill, checklist, or gate | use-shaped operationalization introduces ordering, defaults, and stopping conditions |
| repository or source material → descriptive review | correctness is fidelity to a referent rather than theoretical claim closure |
| attributed sources → dialectical map | synthesis and attribution need not assert the mapped claims |
| session state or trace → summary or handoff | selection and compression may be derived, judgmental, or mixed |
| canonical artifacts → index or runtime projection | generated transformation may be mechanically reproducible without being theory-shaped |
| workshop investigation → ADR | the target records an authored decision, not merely a source-derived claim |

The relation must remain distinguishable from mere citation, inspiration, evidential support, copying, and a source being the rationale for an independently authored target.

## Decisions to finish

- Write the exact truth conditions and reader need for `adapted-from`, including what makes a source a **material input** rather than background influence.
- Decide whether specific labels are subrelations of `adapted-from`, alternatives that replace it at authoring time, or both. Avoid recording redundant parent and child edges unless a concrete consumer needs both.
- Decide which additional relations have earned names now. `operationalized-from` and `generated-from` have live cases; a complete transformation taxonomy is out of scope.
- Define the weakest honest maintenance consequence of `adapted-from` and keep it separate from the stronger recomputation regime of `derived-from`.
- Decide how source-side inverse lineage is represented. Current `Derived into:` headings are reader-facing phrases without the proposed formal hyphenated cue; determine whether they remain renderings of a canonical relation or become registered inverse identifiers such as `derived-into` and `adapted-into`.
- Decide where narrow `derived-from` is authorized. Its claim-closure test should not be silently imposed on collections whose governing correctness condition is descriptive fidelity, prescriptive executability, or stance-neutral attribution.
- Determine the minimum always-loaded wording for `AGENTS.md` and the disposition of `AGENTS.md.template` without hardcoding this repository's methodology vocabulary into every consuming KB.

## Migration audit

Revisit the retirement range from the first semantic wave through commit `593c60af`, concentrating on places where a theory-specific derivation mechanism was generalized to other registers. The audit should classify formal edges and load-bearing mechanism links, not mechanically replace every ordinary occurrence of *derive*.

Two sub-agent passes have covered `f7aac9e6`, `4175dbb3`, `757d6daa`, `9e252b41`, and `593c60af`; results are in [migration-audit-findings.md](./migration-audit-findings.md). Headline: "condense" and "extraction" were both reintroduced ad hoc as an unnamed 4th operator in the same migration that retired distillation for having too many senses, the same operation gets DER and AMP treatment in different files, the migration's own flagship derivation case (`skills-derive-from-methodology.md`) may itself be judgment rather than derivation, and the original "ad-hoc distillation" term still lives untouched in `kb/work/lineage-mechanisms/`. Remaining unaudited: `b35ea92c`, `c7cc78f4`, `4c0c3cf8`, `b0b775c7`.

Known candidates include:

- `Derived into:` footers pointing from theory notes to instructions, checklists, review tasks, and generated views;
- summaries, handoffs, titles, descriptions, and precomputed views explained through the two-layer theory–methodology note;
- the binary lineage choice required by `cp-skill-write`;
- `write-instruction.md` treating methodology-to-procedure conversion as claim derivation and emitting a note-to-note `derived-from` edge not authorized by the current notes collection contract;
- the stale `/connect` "Phase 5 logging" lineage description introduced during the conjecture-note migration; and
- current prose that equates use-shaping with `derived` / `abstracted` lineage.

Preserve the valid outcomes of the earlier migration: the discovery lifecycle for trace-to-rule amplification and the strict derived/abstracted distinction wherever their truth tests genuinely apply.

## Non-goals

- Preventing ordinary English uses of *adapt*, *derive*, or related words.
- Restoring *distillation* as Commonplace's umbrella term.
- Defining bare *adaptation* as a globally exact operation with validator-checkable boundaries.
- Naming every possible transformation before a worked case needs the distinction.
- Building a new graph store, schema, or validator solely to represent the vocabulary.
- Reopening the two-layer theory–methodology mechanism where it is already an accurate model.

## Expected durable outputs

- An ADR amending or superseding the no-successor part of [ADR 053](../../reference/adr/053-retire-distillation-without-a-successor-term.md).
- Updated formal semantics in [link-vocabulary.md](../../reference/link-vocabulary.md).
- The minimal global usage convention in `AGENTS.md`, with an explicit decision about `AGENTS.md.template`.
- Updated outbound-link rules in each collection that adopts `adapted-from` or a more specific sibling.
- Focused corrections to instructions and lineage footers proven wrong by the migration audit.
- A transferable theory note only if the orthogonality of transformation, epistemic authority, artifact contract, and maintenance proves to carry a claim beyond the vocabulary decision itself. Bare *adaptation* does not need a definition note.

## What closes the workshop

1. `adapted-from` has an exercised formal meaning that distinguishes it from strict derivation, abstraction, evidence, rationale, and weak inspiration.
2. The always-loaded, canonical-catalogue, and collection-local responsibilities are implemented without competing full definitions.
3. Representative cases from the evaluation boundary classify honestly, and any case that does not fit is left outside rather than forced into the relation.
4. The identified false or over-broad lineage assertions from the distillation-retirement migration are corrected or explicitly retained with reasons.
5. The governing ADR and authoring instructions describe the resulting vocabulary and maintenance behavior.
6. Validation and relevant tests pass; the workshop's durable conclusions are promoted, its active-workshop entry is removed, and this directory is deleted.

## Bookkeeping

Working files are plain Markdown. Record operator decisions as settled starting points, corpus findings with commit/path anchors, and unresolved design choices as questions. Do not use workshop links as durable library provenance.

The active-workshop index already had unrelated uncommitted edits when this workshop was created, so its entry is intentionally deferred to a later navigation cleanup, following the `kb/work/COLLECTION.md` rule.

## Grounding

- [Theory–methodology derivation workshop](../theory-methodology-derivation/README.md) — triggering migration and retained audit evidence.
- [ADR 053: retire distillation without a successor term](../../reference/adr/053-retire-distillation-without-a-successor-term.md) — decision this workshop may amend or supersede.
- [Link vocabulary and linking approach](../../reference/link-vocabulary.md) — canonical label catalogue and current derived/abstracted semantics.
- [ADR 019: collection-owned link vocabulary](../../reference/adr/019-collection-owned-link-vocabulary.md) — authority boundary for collection outbound relations.
- [Vocabulary governance workshop](../vocabulary-governance/README.md) — global, collection-local, and type-specific vocabulary placement.
- [Vocabulary collisions are prevented at write time, not resolved at read time](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) — device-ranking theory behind the settled hyphenated-identifier-in-link-label-slot convention above.
- [Text-contract profiles](../../reference/text-contract-profiles.md) — different correctness conditions across theoretical, descriptive, prescriptive, and dialectical artifacts.
- [Theory and methodology form a two-layer execution system](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) — narrow derivation mechanism to preserve within its valid scope.
