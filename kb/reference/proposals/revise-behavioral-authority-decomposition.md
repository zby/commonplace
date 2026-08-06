---
description: "Proposal: revise behavioral authority's applicability, path topology, and force taxonomy while keeping authorization, warrant, provenance, realization, and dependency closure in neighboring records"
type: ../types/design-proposal.md
tags: [artifact-analysis, learning-theory]
---

# Revise the behavioral-authority decomposition

The [behavioral authority](../../notes/definitions/behavioral-authority.md) definition's core claim — authority attaches to a consumption path, not to bytes — is sound and heavily load-bearing. Its subdivisions are not equally developed: the consumer, channel, and force lists were enumerated rather than derived, and use has exposed three internal misfits. The same cases also exposed neighboring questions about authorization, epistemic warrant, provenance, realization, and dependency closure. This proposal owns the structure of effective artifact consumption, not a general governance or evidence record. A literature survey remains the first gate: [a carve that inherits a tested ontology is in a better position than one chosen freely](../../notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md), as the reflective-system definition demonstrated with Maes and Smith.

## Current state (as of 2026-08-04)

- The definition records three components: consumer, channel, force, each as a flat example list. Two clarifications were adopted directly as uncontested: authority paths compose (one consumer's act is the next path's channel), and placement within a channel is part of effective force.
- Dozens of library and workshop files link directly to the definition. Separately, 158 agent-memory review artifacts carry controlled behavioral-authority leads, and the generated comparison matrix currently contains 152 code-grounded rows. The review type and matrix parser make changes to that controlled vocabulary an operative migration, not only a citation update.
- [Lineage](../../notes/definitions/lineage.md) is already an independent artifact-analysis field. It records review-relevant source dependencies and derivation status rather than every production or admission event. The four-field risk account locates security in the behavioral-authority-plus-lineage conjunction without making lineage part of behavioral authority.
- The authority-failure note is live and builds the contrast between force a channel delivers and force the artifact earned entirely in prose. No general record binds an authorization event to the exact content version, role, scope, and use that a channel would need to check. Such a record would preserve history; it would not itself authorize the event, establish that the content is good, or prove that a consumer checked it.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) already records scope as local consumption-path metadata outside the authority triple, so the proposal must decide whether to promote that existing qualifier or change the record itself.
- A [six-path Commonplace audit](../../notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md) found that consumer, channel, and force can stay constant while the target cohort or activation trigger changes. Its explanatory-reach and tag-validator cases require applicability to identify the authority path, but do not decide whether applicability is a fourth component or a required qualifier. The same audit separates authorization and admission, runtime realization, and dependency closure from behavioral authority itself.

## Problem

Three internal misfits have been observed in use rather than conjectured:

1. **The force list mixes kinds.** Advice/instruction/enforcement form a bindingness gradient read by an interpreting consumer; validation/routing/ranking influence are executed mechanically; learning input lands in weights with delayed, non-addressable effect. The definition's own hedge on audit triggers ("no force by themselves") signals the heterogeneity. Claims built on the vocabulary inherit it: the authority-failure note's countermeasures hold for interpretive and mechanical force but break for parametric force, where "rollback" means retraining.
2. **Channel is one slot; real paths are staged.** Retrieval selects, assembly positions, the consumer acts — one consumption event spans several list entries, and the countermeasures in the authority-failure note land at different stages (entrance, placement, consumption, after-the-fact). The note had to invent entrance-side/consuming-side vocabulary the definition does not supply.
3. **Applicability is implicit.** A semantic gate may apply only to notes carrying one trait, and a validator rule only to a canonical type, affected cohort, and invocation trigger. Consumer, channel, and force do not distinguish these scoped uses. An authority-path inventory therefore needs the target cohort, aspect, or operation and the condition under which force activates.

The cases also require a clean boundary around the authority record. These questions can all matter to one use, but they ask for different evidence and must not become one generic warrant field:

| Concern or account | Question | What it does not establish |
|---|---|---|
| Behavioral authority | Which operative part shapes whose behavior, through which channel, with what force, and under which applicable conditions? | Legitimate admission, substantive correctness, realized execution, or dependency completeness |
| Authorization and admission | Which actor or decision may install a change, and which admission act made this exact content version incumbent for this role, scope, and use? | That the content is true, improves the objective, or reaches a later consumer |
| Epistemic warrant | Why should this content or transition be accepted over the incumbent for the stated claim, objective, and risk? | That it was authorized, installed, or later consumed |
| Provenance and attestation | What retained evidence states how the artifact, decision, or execution came about? | The record's authenticity, the recorder's authority, or the truth of the recorded claim by itself |
| Realization and operativity | Did the requested configuration reach the actual consumer and affect later behavior? | Legitimate admission or a favorable effect |
| Dependency and revision closure | Which derivatives, interfaces, and checks must change or be revalidated with this revision? | Authorization, correctness, or realized use |

These rows do not imply six new schemas. [Operative change](../../notes/definitions/operative-change.md) already owns the later-use test, while lineage and revision-closure work own dependency propagation. The behavioral-authority definition may need to name these neighbors so readers do not infer them from effective force. Any missing schemas, enforcement mechanisms, or lifecycle rules belong to their own design work when a concrete consumer requires them.

## Design space

The behavioral-authority choices are orthogonal axes rather than peer alternatives. A revision may combine one choice from each axis.

1. **Applicability placement.** Make target cohort, aspect, or operation and activation condition additional record components; or require them as a predicate over the path only when individuating or comparing uses. The component choice makes path identity explicit but enlarges the migration surface. The qualifier choice is cheaper but risks continuing to omit applicability where scoped gates and triggers are load-bearing.
2. **Path topology.** Preserve the current atomic consumer-channel-force link and add stage or position vocabulary for composing links; or make a path an ordered chain of stages whose position is part of the record. The minimal option supplies entrance, selection, assembly, consumption, and recovery locations without replacing every existing link. The chain option resolves the retriever/retrieval double-listing more completely but touches every record's shape.
3. **Force taxonomy.** Keep a flat force list; or organize force independently from its delivery or consumption mechanism. Interpretive, mechanical, and parametric may be mechanism families rather than force families: the same selection influence can be delivered through any of them. The survey must test the cross-product before deriving either axis from [representational form](../../notes/definitions/representational-form.md).
4. **Ontology source.** Inherit a tested external decomposition where the bridge holds, with inherited purchase and local extension separated; otherwise retain a local carve whose unsupported choices remain explicit.

No option adds authorization, epistemic warrant, provenance, realization, or dependency closure as a behavioral-authority component. The revised definition may state their relation to effective authority and link to their definitions. If later design makes a channel authorization-aware, that design must separately name the authorization policy, the provenance or attestation it checks, and the consumer capable of withholding force. A model merely reading provenance as prompt text still receives advice; it does not mechanically enforce admission.

Free choices, marked as such: whether applicability belongs inside the record or in a predicate over it; the stage vocabulary and whether a chain replaces or composes local links; the force taxonomy and any separate delivery or consumption-mechanism taxonomy; and which external ontology, if any, supplies each carve. The names *warrant*, *earning*, *authorization*, and *backing* are not interchangeable placeholders: any later vocabulary must preserve the distinctions above.

## Survey targets

The gate before choosing is a question-indexed survey, not a search for one ontology that absorbs every neighboring record. For each thread, record what it decomposes, whether the bridge to retained-artifact consumption holds, what it supplies, and which tempting inference it does not license.

| Thread | Question it tests | Boundary to preserve |
|---|---|---|
| Access-control policy applicability and attribute-based access control | Whether target, action, condition, and effect supply applicability or path-identity structure | A policy's applicability and decision effect do not establish epistemic warrant |
| Speech-act theory | Whether illocutionary force sharpens the interpretive portion of the force taxonomy | Speech-act force does not classify mechanical or parametric delivery mechanisms |
| LangSec | Whether staged parsing and data/instruction separation sharpen channel topology | Separating channels does not establish authorization or content quality |
| Capability security, including CaMeL | Whether carried capabilities explain how a reference can constrain later operations | A capability grants operational permission; it is not evidence that the operation is wise or true |
| Clark–Wilson integrity | How certified transformations and separation of duty relate admission policy to operative state | Procedural integrity does not establish semantic correctness |
| Biba and taint tracking | How integrity labels propagate through composed paths | Integrity ordering is not a general force ordering |
| PolicyMaker/KeyNote and SPKI/SDSI | How credentials, delegation, and policy decisions represent authorization | Authorization is not epistemic warrant |
| in-toto, SLSA, and sigstore | How attestations bind production events to exact artifacts and declared roles | Attestation supplies retained history, not authorization or truth by itself |
| W3C PROV | Whether entity/activity/agent structure is sufficient for authority-relevant history | General provenance does not bind force or define an admission policy |

Reuse the existing captured and ingested W3C PROV and in-toto material before new sourcing. Reuse the existing speech-act investigation before deciding whether a deeper survey is warranted. The new work should concentrate first on access-control applicability and trust-management authorization because those are the least developed local threads and the easiest place to test the separation.

## Forces

- **Migration surface**: authority and lineage are required controlled leads in the agent-memory review type and feed a generated matrix. Changing their controlled values is an operative parser migration; making applicability required re-opens every existing record. Cited from [use tests a decomposition locally](../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md): the current record's local success does not license it, but replacement must price the evidence already built on it.
- **Separation cost**: one use may require an authority record plus authorization, warrant, provenance, realization, and dependency evidence. Keeping the jobs separate increases coordination cost, but merging them creates false entailments exactly where the audit found gaps.
- **Evidence is not enforcement**: provenance can support an authorization decision but cannot grant force, prove truth, or make a path check it. Any separate admission design must name the policy and consumer that turn retained history into a gate; otherwise richer lineage improves audit only.
- **Ontology warrant**: a freely chosen replacement carve is no better warranted than the freely chosen current one; the survey exists to make the revision derived or inherited rather than a second free choice ([rationale](../../notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md)).
- **Context cost**: full provenance in a model context competes with the task and remains interpretive. A compact identity, attestation, approval binding, or checked mark consumed outside the prompt may preserve the evidence while moving enforcement to the channel boundary.
- **Naming risk**: axis names carry hidden dichotomies; expect multiple naming rounds before any force family, delivery-mechanism family, or authorization term is fixed.
- **Applicability cost**: a component makes every record more precise at recurring context cost; a conditional qualifier is cheaper but may fail exactly where scoped gates and triggers are load-bearing. Authorization coverage also cannot be checked unless its scope and the path's applicability are comparable.

## Operativity and warrant

A revised definition is consumed by review authors and note writers through the definition-lookup channel with authoring-instruction force. The agent-memory review type and template already require controlled behavioral-authority leads, and the matrix parser consumes them mechanically; changes to their vocabulary become operative through those surfaces. Existing review records are the migration surface.

Naming the neighboring records prevents readers from treating effective force as proof of legitimate admission, good reasons, actual execution, or complete propagation. It adds no general authorization, provenance, realization, or dependency consumer. Those mechanisms remain YAGNI until a separate design names a concrete consumer and consequence.

No option adds automated evaluation. Human review of the definition remains the adoption oracle. A future mechanical admission check could establish that retained values match an authorization policy for exact content identity, version, role, and applicability. Its warrant would stop at that equality relation: it would not establish the authorization record's authenticity, the issuer's entitlement, or the substantive quality of the approved content.

## Adoption criteria

- The survey is complete with a per-thread verdict — inherit, adapt, or reject — and a bridge argument for anything inherited, purchase separated from local extension.
- The definition distinguishes effective behavioral authority from authorization, epistemic warrant, provenance or attestation, realization, and dependency closure without making any of them a component by implication.
- The chosen account states whether applicability is part of the local record or a required predicate over an individuated path, and it distinguishes both target from activation condition.
- Any inherited force taxonomy passes the cross-product test against interpretive, mechanical, and parametric delivery or consumption mechanisms instead of treating correlated families as one axis.
- The chosen decomposition re-derives the current consumer/channel/force lists as instances rather than discarding them.
- The migration path for existing review records is stated and priced before any record-shape option is adopted.
- The authority-failure note can be re-grounded on the revised vocabulary without losing any of its three moves (unification, gate-bypass separation, countermeasures-as-one-operation).
- The chosen account distinguishes the audit's trait-scoped gate and type/trigger-scoped validator paths without conflating applicability with authorization, runtime realization, or dependency closure.
- Any concrete provenance, admission, execution-attestation, or dependency mechanism is routed to its own proposal with a named consumer rather than smuggled into this vocabulary revision.
