# What is stored in this KB?

This workshop asks what Commonplace must retain, why it must retain it, and—where the choice is between the two main library collections—whether `kb/notes/` or `kb/reference/` should own it. “Stored” is not limited to knowledge claims or to files called documentation. Beliefs, choices, sources, descriptions, operative rules, rationale, and temporary work play different roles, but the other collections keep their own local routing rules.

The immediate trigger was the former theory-side text-contract definition. It defined chosen Commonplace machinery while living in the theoretical collection. The audit first checked the rest of the vocabulary, then folded the term into the [collection definition](../../reference/definitions/collection.md#text-contract) under [ADR 071](../../reference/adr/071-text-contract-is-part-of-the-collection-definition.md).

This is exploratory work. Its files record candidate distinctions and dispositions, not accepted library conclusions.

## Work so far

The investigation began with [the documentation generator/cache note](../../notes/documentation-generates-the-system-rather-than-describing-it.md). It proposed a recovery test run in both directions: documentation that can be regenerated from the system is a cache; content from which the system was worked out, but which the system cannot reproduce, is a generator. It also recognized that implementation may contain resolutions that its documentation never determined.

The first attempted content split—derived content versus committed content—failed. Commonplace can retain a new abductive or ampliative theory that is not entailed by its sources. Producing it is a commitment, but what it asserts remains a truth-apt belief. Conversely, a design can contain both consequences determined by beliefs and constraints and residual selections among options those inputs leave live.

[Artifact classification now separates three questions](../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md): content kind, production relation, and path-relative behavioral authority. A collection's local text contract supplies its intended contribution and review priority as a separate whole-artifact input. It does not determine whether a region is a belief or residual choice, whether it was derived or added, or whether a consumer treats it as advice or binding system definition.

The design-proposal discussion then established another boundary: a proposal is not a special information kind. It is a workflow surface for considering a possible process or system choice. The beliefs, requirements, alternatives, and candidate selections inside it retain their own kinds; adoption makes a residual selection operative.

The workshop then acquired its organizing rule. **`kb/notes/` holds beliefs about the design space, with particular system choices bound; `kb/reference/` holds the choices Commonplace made and the current or historical state they produced.** A note's intended contribution must remain a substantive truth-apt claim when every particular choice it names is bound universally, through equivalent generic or conditional grammar, or existentially as a witness. If binding leaves only “Commonplace selected X” or “Commonplace currently does Y,” the contribution belongs in reference. This replaces the failed counterfactual test with the formulation rule already used by the notes collection. Reusable creation text now lives only as [collection prototypes](./tasks/retire-profiles-for-collection-prototypes.md).

Two independent arguments support it. **Maintenance:** beliefs are revised against evidence and rewritten in place, while choices are superseded and the earlier choice stays a fact — different regimes the profile labels had to state as a separate convention. **Publishability:** notes are distilled into articles for readers with no KB context, so a note may name a choice only as a bound variable — universally, through generic or conditional grammar, or existentially as a substantive witness. A free choice-variable does not survive publication. A merely local assignment acquires no reach by being wrapped in an existential sentence; the witness must support a claim about feasibility, mechanism, or consequence in the design space. Consequences are worked out in [the content model](./working-content-model.md).

The text-contract audit found 30 direct backlinks from 22 files and traced the present artifact to commit `1ac2171d` (2026-07-09), which replaced the earlier `register` definition added by `7eb616d5` (2026-04-12). Its terms name the collection-contract architecture chosen by Commonplace. That makes their canonical description a reference concern even if the vocabulary is stable. No relocation has been executed; the decision is now an explicit workshop task.

The prior conversation was handed off through `/tmp/commonplace-documentation-handoff.md`. Because `/tmp` is ephemeral, the load-bearing conclusions from it are restated above rather than linked as durable evidence.

## Governing question

What kinds of retained content and system state does an agent-operated KB need, and what separates theory in `kb/notes/` from Commonplace selections and state in `kb/reference/`?

This workshop does not replace the special rules of `kb/instructions/`, `kb/sources/`, `kb/work/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, or `kb/articles/`. Their local contracts decide when an artifact's operative, source-fidelity, lifecycle, external-system, or publication role takes precedence. The binding test applies only after the live routing choice is notes versus reference.

The answer must distinguish at least:

- truth-apt beliefs, including source-grounded beliefs and the KB's own ampliative work;
- residual choices that beliefs, requirements, and constraints do not determine uniquely;
- current-state descriptions and other recoverable but useful caches;
- operative contracts, instructions, schemas, validators, configuration, and code;
- sources, evidence, lineage, rationale, alternatives, scope, and uncertainty;
- temporary work whose value should be consumed rather than accumulated.

This list is a starting inventory, not the final ontology. Requirements, inherited constraints, definitions, indexes, and historical decisions still need exact treatment where they raise a notes/reference choice; the other collection contracts continue to route their special cases.

## Working guard

The boundary is operationalized by binding, not by a counterfactual. Ask whether the artifact's intended contribution remains substantive after every particular system choice it names is treated as a variable:

- Bind it universally or through equivalent generic or conditional grammar when the claim states what follows for systems making that choice.
- Bind it existentially when the particular system is evidence for feasibility, a mechanism, or a bounded consequence.
- If nothing remains except the selected value or the current or historical state it produced, the artifact records Commonplace and belongs in `kb/reference/`.

An artifact does not belong in theory merely because it defines a stable term, nor in reference merely because it discusses machinery. Subject matter is not content kind. The test is what makes its content hold:

- A theoretical definition still names a substantive, contestable distinction after Commonplace-specific choices are replaced by variables.
- A reference definition names Commonplace's selected vocabulary, current contract, or implemented classification; abstracting the local term removes its intended contribution.
- An instruction prescribes how an operator should act.
- Mixed artifacts are decided case by case. Prefer splitting when that yields atomic, independently useful notes; do not invent a general threshold before hard cases require one.

The test has two dispositions. Bind the choice and keep the theory when a substantive claim remains with the selection as a parameter or witness. Move the artifact to reference when the selected value or resulting state is the whole intended contribution. Neither is preferred independently of what survives binding.

The structural `definition` type does not decide this placement. [Reference already contains a definition-typed artifact](../../reference/definitions/collection.md), so collection and type are demonstrably separate.

## Workstreams

- [Working content model](./working-content-model.md) — reconstruct the candidate retained payload and the tests that separate its roles.
- [Definition audit](./definition-audit.md) — initial disposition of all 23 artifacts under `kb/notes/definitions/`, including migration cost from direct backlinks.
- [Text-contract disposition](./tasks/text-contract-and-profiles.md) — after profile content is extracted in place, decide whether the remaining term belongs in the collection definition, a small standalone reference definition, or the collection/type composition document.
- [Promote the choice-binding boundary into binding artifacts](./tasks/promotion-sequence.md) — five ordered steps; steps 1 and 2 are complete, and the text-contract disposition is next.
- [Sweep kb/notes/ for free choice-variables](./tasks/bound-variable-sweep.md) — **closed 2026-08-23**, 0/27 failures; [findings](./bound-variable-sweep-findings.md) corrected the clause wording and unblocked step 2.
- [Draft ADR: notes bind choices; reference records selections and state](./draft-adr-collection-placement-follows-content-kind.md) — **promoted 2026-08-23** as [ADR 070](../../reference/adr/070-notes-bind-choices-reference-records-selections-and-state.md).
- [Applied COLLECTION.md edits](./draft-collection-contract-edits.md) — execution record for the six changes applied with ADR 070.
- [Draft: superseded choices are retained, superseded beliefs are not](./draft-superseded-choices-are-retained-superseded-beliefs-are-not.md) — **promoted 2026-08-23** into [the note](../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md); both open questions carried over.
- [Draft: a theory may name a choice only as a bound variable](./draft-a-theory-may-name-a-choice-only-as-a-bound-variable.md) — **promoted 2026-08-23** into [the note](../../notes/a-theory-may-name-a-choice-only-as-a-bound-variable.md), with the sweep's three refinements folded in (grammatical binding, the removal test, explicit local reports failing placement rather than binding).
- [Retire profiles for collection prototypes](./tasks/retire-profiles-for-collection-prototypes.md) — completed first step: profiles bound nothing at use time, so ADR 069 replaced them with one-time-copy prototypes, cleared the always-loaded gloss, and deliberately left `text-contract` in place.
- Reassess the generator/cache model against directly executed natural-language system definition and against rationale retained only for future change.
- Derive collection-contract and type-contract changes only after the content model and definition dispositions agree.

## What closes this workshop

- A content model states what Commonplace retains without conflating collection prototype, content kind, intended contribution, lineage, authority, or recoverability, and works out which payload classes cross the notes/reference boundary while preserving other collections' special rules.
- Every current definition has a reasoned disposition: keep in theory, move or fold into reference, move operational rules into instructions, split, or retire.
- The text-contract task has one selected reference owner and a complete post-profile backlink migration plan.
- Required changes to `AGENTS.md`, collection contracts, type guidance, indexes, and durable artifacts are recorded as explicit implementation handoffs.
- Accepted conclusions are promoted into the appropriate library collections, after which this workshop is deleted.

## Current status

- [x] Reconstruct the conversation and governing question.
- [x] Read and provisionally classify all 23 theory-collection definitions.
- [x] Record the text-contract disposition task.
- [x] Scope the profile retirement as a separable first step.
- [x] Adopt choice-binding as the notes eligibility test and make reference own Commonplace's selections and resulting state.
- [x] Test the bound-variable requirement against a fixed sample of `kb/notes/` (0/27 failures).
- [ ] Test the choice-binding boundary against representative notes/reference cases while confirming that other collections' special rules take precedence.
- [ ] Resolve the mixed and machinery-first definitions.
- [ ] Select and execute durable migrations.
