# What is stored in this KB?

This workshop asks what Commonplace must retain, why it must retain it, and which durable collection should own it. “Stored” is not limited to knowledge claims or to files called documentation. It includes beliefs, choices, sources, descriptions, operative rules, rationale, and temporary work when those play different roles in the system.

The immediate trigger was [the text-contract definition](../../notes/definitions/text-contract.md). It defines chosen Commonplace machinery but lives in the theoretical collection. Moving that one file without checking the rest of the vocabulary could preserve the same category error elsewhere.

This is exploratory work. Its files record candidate distinctions and dispositions, not accepted library conclusions.

## Work so far

The investigation began with [the documentation generator/cache note](../../notes/documentation-generates-the-system-rather-than-describing-it.md). It proposed a recovery test run in both directions: documentation that can be regenerated from the system is a cache; content from which the system was worked out, but which the system cannot reproduce, is a generator. It also recognized that implementation may contain resolutions that its documentation never determined.

The first attempted content split—derived content versus committed content—failed. Commonplace can retain a new abductive or ampliative theory that is not entailed by its sources. Producing it is a commitment, but what it asserts remains a truth-apt belief. Conversely, a design can contain both consequences determined by beliefs and constraints and residual selections among options those inputs leave live.

[Artifact classification now separates three questions](../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md): content kind, production relation, and path-relative behavioral authority. A collection's local text contract supplies its intended contribution and review priority as a separate whole-artifact input. It does not determine whether a region is a belief or residual choice, whether it was derived or added, or whether a consumer treats it as advice or binding system definition.

The design-proposal discussion then established another boundary: a proposal is not a special information kind. It is a workflow surface for considering a possible process or system choice. The beliefs, requirements, alternatives, and candidate selections inside it retain their own kinds; adoption makes a residual selection operative.

The workshop then acquired its organizing rule. **`kb/notes/` holds beliefs; `kb/reference/` holds choices** — notes are about the design space, reference about the selections Commonplace made within it. This promotes the content-kind axis to the collection boundary and removes the former communicative-profile axis; reusable creation text now lives only as [collection prototypes](./tasks/retire-profiles-for-collection-prototypes.md). It also survives the objection that killed the derived/committed split, because it asks what content *is* rather than how it was produced.

Two independent arguments support it. **Maintenance:** beliefs are revised against evidence and rewritten in place, while choices are superseded and the earlier choice stays a fact — different regimes the profile labels had to state as a separate convention. **Publishability:** notes are distilled into articles for readers with no KB context, so a note may name a choice only as a bound variable — universally quantified, or existentially as a witness. A free choice-variable does not survive publication, and binding it is what produces explanatory-reach. Consequences are worked out in [the content model](./working-content-model.md).

The text-contract audit found 30 direct backlinks from 22 files and traced the present artifact to commit `1ac2171d` (2026-07-09), which replaced the earlier `register` definition added by `7eb616d5` (2026-04-12). Its terms name the collection-contract architecture chosen by Commonplace. That makes their canonical description a reference concern even if the vocabulary is stable. No relocation has been executed; the decision is now an explicit workshop task.

The prior conversation was handed off through `/tmp/commonplace-documentation-handoff.md`. Because `/tmp` is ephemeral, the load-bearing conclusions from it are restated above rather than linked as durable evidence.

## Governing question

What kinds of retained content and system state does an agent-operated KB need, and which collection should own each kind?

The answer must distinguish at least:

- truth-apt beliefs, including source-grounded beliefs and the KB's own ampliative work;
- residual choices that beliefs, requirements, and constraints do not determine uniquely;
- current-state descriptions and other recoverable but useful caches;
- operative contracts, instructions, schemas, validators, configuration, and code;
- sources, evidence, lineage, rationale, alternatives, scope, and uncertainty;
- temporary work whose value should be consumed rather than accumulated.

This list is a starting inventory, not the final ontology. Requirements, inherited constraints, definitions, indexes, and historical decisions still need exact placement.

## Working guard

The boundary is belief versus choice, and the operative question is the counterfactual: **would this still be true if Commonplace had chosen differently?** A belief survives it; a choice is what it varies.

An artifact does not belong in theory merely because it defines a stable term, nor in reference merely because it discusses machinery. Subject matter is not content kind. The test is what makes its content hold:

- A theoretical definition sharpens a transferable distinction needed by truth-apt claims about possible systems.
- A reference definition names Commonplace's chosen architecture, current contract, or implemented classification.
- An instruction prescribes how an operator should act.
- A mixed artifact is split or routed proposition by proposition rather than assigned by its dominant vocabulary.

Failing the test has two repairs, not one. A theory claim that depends on a Commonplace choice can be moved to reference, or the choice can be bound as a variable and the claim kept — the second is usually better, because it adds reach instead of relocating content.

The structural `definition` type does not decide this placement. [Reference already contains a definition-typed artifact](../../reference/definitions/collection.md), so collection and type are demonstrably separate.

## Workstreams

- [Working content model](./working-content-model.md) — reconstruct the candidate retained payload and the tests that separate its roles.
- [Definition audit](./definition-audit.md) — initial disposition of all 23 artifacts under `kb/notes/definitions/`, including migration cost from direct backlinks.
- [Text-contract disposition](./tasks/text-contract-and-profiles.md) — after profile content is extracted in place, decide whether the remaining term belongs in the collection definition, a small standalone reference definition, or the collection/type composition document.
- [Retire profiles for collection prototypes](./tasks/retire-profiles-for-collection-prototypes.md) — completed first step: profiles bound nothing at use time, so ADR 069 replaced them with one-time-copy prototypes, cleared the always-loaded gloss, and deliberately left `text-contract` in place.
- Reassess the generator/cache model against directly executed natural-language system definition and against rationale retained only for future change.
- Derive collection-contract and type-contract changes only after the content model and definition dispositions agree.

## What closes this workshop

- A content model states what Commonplace retains without conflating collection prototype, content kind, lineage, authority, or recoverability, and works out the belief/choice boundary's consequences for every payload class.
- Every current definition has a reasoned disposition: keep in theory, move or fold into reference, move operational rules into instructions, split, or retire.
- The text-contract task has one selected reference owner and a complete post-profile backlink migration plan.
- Required changes to `AGENTS.md`, collection contracts, type guidance, indexes, and durable artifacts are recorded as explicit implementation handoffs.
- Accepted conclusions are promoted into the appropriate library collections, after which this workshop is deleted.

## Current status

- [x] Reconstruct the conversation and governing question.
- [x] Read and provisionally classify all 23 theory-collection definitions.
- [x] Record the text-contract disposition task.
- [x] Scope the profile retirement as a separable first step.
- [x] Adopt belief/choice as the collection boundary and align the content model to it.
- [ ] Test the candidate content model against representative artifacts in every collection.
- [ ] Resolve the mixed and machinery-first definitions.
- [ ] Select and execute durable migrations.
