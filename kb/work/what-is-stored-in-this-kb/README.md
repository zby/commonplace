# What is stored in this KB?

This workshop asks what Commonplace must retain, why it must retain it, and which durable collection should own it. “Stored” is not limited to knowledge claims or to files called documentation. It includes beliefs, choices, sources, descriptions, operative rules, rationale, and temporary work when those play different roles in the system.

The immediate trigger was [the text-contract definition](../../notes/definitions/text-contract.md). It defines chosen Commonplace machinery but lives in the theoretical collection. Moving that one file without checking the rest of the vocabulary could preserve the same category error elsewhere.

This is exploratory work. Its files record candidate distinctions and dispositions, not accepted library conclusions.

## Work so far

The investigation began with [the documentation generator/cache note](../../notes/documentation-generates-the-system-rather-than-describing-it.md). It proposed a recovery test run in both directions: documentation that can be regenerated from the system is a cache; content from which the system was worked out, but which the system cannot reproduce, is a generator. It also recognized that implementation may contain resolutions that its documentation never determined.

The first attempted content split—derived content versus committed content—failed. Commonplace can retain a new abductive or ampliative theory that is not entailed by its sources. Producing it is a commitment, but what it asserts remains a truth-apt belief. Conversely, a design can contain both consequences determined by beliefs and constraints and residual selections among options those inputs leave live.

[Artifact classification now separates four questions](../../notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md): communicative profile, content kind, production relation, and path-relative behavioral authority. A theoretical, descriptive, or prescriptive profile says what contribution and review priority an artifact has. It does not determine whether a region is a belief or residual choice, whether it was derived or added, or whether a consumer treats it as advice or binding system definition.

The design-proposal discussion then established another boundary: a proposal is not a special information kind. It is a workflow surface for considering a possible process or system choice. The beliefs, requirements, alternatives, and candidate selections inside it retain their own kinds; adoption makes a residual selection operative.

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

An artifact does not belong in theory merely because it defines a stable term, nor in reference merely because it discusses machinery. The test is what makes its content hold:

- A theoretical definition sharpens a transferable distinction needed by truth-apt claims about possible systems.
- A reference definition names Commonplace's chosen architecture, current contract, or implemented classification.
- An instruction prescribes how an operator should act.
- A mixed artifact is split or routed proposition by proposition rather than assigned by its dominant vocabulary.

The structural `definition` type does not decide this placement. [Reference already contains a definition-typed artifact](../../reference/definitions/collection.md), so collection and type are demonstrably separate.

## Workstreams

- [Working content model](./working-content-model.md) — reconstruct the candidate retained payload and the tests that separate its roles.
- [Definition audit](./definition-audit.md) — initial disposition of all 23 artifacts under `kb/notes/definitions/`, including migration cost from direct backlinks.
- [Text contract and profile disposition](./tasks/text-contract-and-profiles.md) — decide whether to fold the vocabulary into the profile catalogue, keep a small reference definition, or retire the standalone artifact.
- Reassess the generator/cache model against directly executed natural-language system definition and against rationale retained only for future change.
- Derive collection-contract and type-contract changes only after the content model and definition dispositions agree.

## What closes this workshop

- A content model states what Commonplace retains without conflating profile, content kind, lineage, authority, or recoverability.
- Every current definition has a reasoned disposition: keep in theory, move or fold into reference, move operational rules into instructions, split, or retire.
- The text-contract/profile task has one selected target and a complete backlink migration plan.
- Required changes to `AGENTS.md`, collection contracts, type guidance, indexes, and durable artifacts are recorded as explicit implementation handoffs.
- Accepted conclusions are promoted into the appropriate library collections, after which this workshop is deleted.

## Current status

- [x] Reconstruct the conversation and governing question.
- [x] Read and provisionally classify all 23 theory-collection definitions.
- [x] Record the text-contract/profile disposition task.
- [ ] Test the candidate content model against representative artifacts in every collection.
- [ ] Resolve the mixed and machinery-first definitions.
- [ ] Select and execute durable migrations.

