---
description: "Separates trivial human-inclusive mutability from Commonplace's stronger target: a general, self-applying affordance for warranted and operative revision across repository-defined artifacts and organizing roles"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/actionable-methodology.md
  - kb/notes/definitions/discovery-lifecycle.md
  - kb/notes/definitions/operative-change.md
  - kb/notes/definitions/reach-assessment.md
  - kb/notes/definitions/reflective-system.md
  - kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md
  - kb/notes/reflection-buys-addressability.md
  - kb/notes/compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md
  - kb/notes/reflective-leverage-is-tested-in-the-next-episode.md
  - kb/notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md
  - kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md
  - kb/notes/llm-executed-methodologies-are-metacircular-interpreters.md
  - kb/notes/a-retained-operative-path-keeps-improvement-machinery-open-to-revision.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/reference/commonplace-declared-frame.md
  - kb/reference/commonplace-as-a-reflective-system.md
  - kb/reference/storage-architecture.md
  - kb/reference/tag-readme-trace-observed-causal-connection.md
  - kb/reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md
  - kb/reference/adr/053-retire-distillation-without-a-successor-term.md
  - kb/reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md
  - kb/reference/adr/055-explanatory-reach-replaces-bare-reach-as-the-technical-term.md
  - kb/reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md
  - kb/reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md
  - kb/tasks/recurring/review-explanatory-reach.md
---

# What makes human-inclusive self-revision non-trivial?

> **Draft.** This article is circulating for comments; its claims, structure, and even its central thesis may still change. Comments are welcome below.

The systems compared in [the reflective self-improvement article](./reflective-self-improvement.md) draw their reported boundaries around agent loops, whereas Commonplace's declared boundary includes designated maintainers.

That makes raw mutability easy to establish. A maintainer with source access can edit a rule, its validator, and then the instructions governing validator changes. Including the research teams within the other systems would create the same possibility. The harder question is whether the system supplies a reusable path that makes each change explicit, warranted, operative, and available to further revision.

The working claim is:

> Commonplace gives its human–agent operator a reusable path to make any repository-defined part an explicit revision target, develop and criticize a successor, warrant its adoption over continuing with the incumbent, install it in a live behavioral path, and leave it open to further revision. The target can be theory, a definition, an objective, an evaluator, an instruction, code, an authority rule, or the revision method itself.

This draft calls that support a **general revision affordance**. *Meta* is role-relative: an evaluator is meta to the prompt it judges but becomes the target when a later episode revises the evaluator. **Recursive targetability** obtains when an artifact governing one episode can become a later target and its installed successor remains inside the governed revision domain. Each episode needs a current target and a governing process, not a permanent hierarchy of controllers.

This article asks how broadly that path reaches. Its outer limit is the declared substrate boundary; practical coverage is measured target class by target class. The main article asks whether reuse produces [leverage](../notes/compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md) and whether repeated leverage compounds.

## Why editability is not enough

Human inclusion also makes a weak claim of reflection easy: an included maintainer can hold a model of the system and act on it. The stronger claim requires a self-representation to participate in the [causal path](../notes/definitions/reflective-system.md). Its practical benefit is [addressability](../notes/reflection-buys-addressability.md): a represented commitment can be inspected, criticized, selectively revised, and reused.

The same distinction applies to revision. A maintainer and a writable repository make change possible, but a one-off edit may depend entirely on unrecorded ingenuity. A supported revision path must satisfy the following obligations:

| Requirement | What it rules out |
|---|---|
| **Declared boundary, target, and purpose** | Calling an unspecified ability to edit "self-improvement" without saying what is changing or why one result is better. |
| **Addressable representation** | A consequential part that can be changed only after someone rediscovers where and how it is encoded. |
| **Applicable revision method** | An external designer inventing the whole approach afresh for this target. The method may route to open-ended theoretical reasoning rather than prescribe fixed steps. |
| **Warrant for the transition** | Changing a governing rule merely because it is editable. The successor must earn adoption over retaining the incumbent; uncertain changes may instead earn a bounded experiment. |
| **Operative installation** | A good proposal or saved rationale that never reaches a consumer with behavioral force. |
| **Recursive targetability** | A one-off redesign after which the installed successor or an artifact governing the change falls outside the supported revision path. |

Together, these obligations turn "a human can edit anything" into a target-relative, testable claim about support.

These are logical obligations, not required components. A proposal-selection path can compare an explicit candidate with the incumbent and reject it. A direct update may instead rely on a warranted evidence-to-successor rule. The general affordance does not require one search algorithm, evaluator, or design lifecycle for every change.

Nor must the successor be a one-for-one replacement artifact. A better arrangement may narrow a rule, split one concept into several, reroute its useful work, or remove an artifact whose role is no longer warranted. What matters is comparison with continuing the incumbent arrangement.

Like [reflective coverage](../reference/commonplace-as-a-reflective-system.md), revision-affordance coverage is relative to an aspect and an operation. Commonplace may strongly support revision of natural-language theory, types, and validators while having weaker paths for objectives, evaluator validity, authority arrangements, or external model bindings.

## What Commonplace supplies

Commonplace does not supply one universal algorithm for every change. It supplies a human–agent environment in which general theory, specialized methods, and operative artifacts work together.

- **Targets are represented.** Types, collection contracts, routing rules, instructions, review criteria, ADRs, schemas, validators, configuration, and code expose much of the repository's organization as inspectable artifacts. Representation gives the operator something specific to criticize and replace.
- **Open problems have a place to develop.** The workshop layer holds investigation before a conclusion is ready. Ampliative claims can follow the [discovery lifecycle](../notes/definitions/discovery-lifecycle.md): anomaly, conjecture, derived consequences, testing, acceptance, and integration. A proposal and ADR are one path from a mature design question to an installed decision, not the definition of revision itself.
- **Theory remains a fallback.** No finite procedure anticipates every new kind of change. Commonplace's [two-layer execution model](../notes/theory-and-methodology-form-a-two-layer-execution-system.md) keeps theory available when the fast methodology does not cover a case; recurring fallback reasoning can later be retained as method. The included human operator supplies semantic judgment where the methodology has not yet been codified.
- **Evaluation follows the claim and its form.** Natural-language theory needs criticism and semantic judgment; symbolic commitments can use tests, schemas, invariants, or proofs; mixed changes combine them. [Explanatory-reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) is a central quality criterion for transferable theory, not a universal oracle for every artifact.
- **Accepted changes can become operative.** Instructions, contracts, code, configuration, and validators give a decision a consumer, channel, and force. The [operative-change test](../notes/definitions/operative-change.md) rejects revisions that are merely written down.
- **Rationale and history support another pass.** ADRs retain accepted design reasoning; canonical source artifacts retain the result; [version control](../reference/storage-architecture.md) supports diff review, rollback, attribution, and reconstruction. History alone is not the obligatory read path, but it helps a later challenge recover what happened.

The self-application is structural. Commonplace's methodology is itself repository content, and the agents and maintainers using it can revise the contracts, skills, review criteria, definitions, and code through which they operate. This is the [metacircular-interpreter shape](../notes/llm-executed-methodologies-are-metacircular-interpreters.md): the rules are artifacts in the system they govern. Where those rules do not settle the next choice, live theory and human judgment provide the fallback rather than another permanently fixed controller.

The affordance remains human-inclusive and fallible. Its advantage is that a maintainer's intervention can become an explicit, retained change to operative revision machinery instead of remaining an undocumented action outside the system description.

## Explanatory-reach is a hard test

Explanatory-reach is not merely a note in the repository. It is named in the root vocabulary, acts as the quality goal for theoretical notes, and is implemented in a semantic review gate. It therefore helps Commonplace decide which theoretical claims deserve retention and reuse.

That importance has not made the criterion immutable. The anchor theory originally presented a harder adaptive-versus-explanatory contrast. A later revision made it a polarity, added a test against rival practices, and required observed fit to discipline the explanation. The same change propagated the revised test into the notes collection contract and the [recurring explanatory-reach review](../tasks/recurring/review-explanatory-reach.md). The later [reach-assessment definition](../notes/definitions/reach-assessment.md) reused all four parts, while [ADR 055](../reference/adr/055-explanatory-reach-replaces-bare-reach-as-the-technical-term.md) made the technical name unambiguous across the corpus.

This is substantive theory revision, not just proof that the files are editable. It also exposes incomplete installation: the current semantic gate does not carry the observed-fit part of the revised test, and no review log establishes that a later full review depended on all four parts. The affordance is visible, but the complete causal path has not been demonstrated for the entire revised criterion.

The same path could challenge the core criterion, not only refine or rename it. If counterexamples showed that explanatory-reach rejects useful explanations or rewards a rhetorical shape rather than real transfer, a successor would need to explain that failure, preserve what the old criterion got right, survive stated tests, reach every operative surface, and govern later review. Until a better successor earns adoption, retaining the incumbent is the normal result of comparing change with continuation.

## Existing cases exercise different parts of the affordance

Commonplace has already changed several kinds of load-bearing machinery:

- [ADR 042](../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) replaced the claimed exhaustive three-register taxonomy after a worked dialectical collection supplied a counterexample. The successor preserved the useful theoretical, descriptive, and prescriptive profiles inside an open text-contract model, changed the definition and root vocabulary, and later made the article collection's editorial profile possible.
- [ADR 053](../reference/adr/053-retire-distillation-without-a-successor-term.md) retired a load-bearing theory term after a 464-occurrence audit showed that it merged operations with opposite maintenance requirements. Its useful work moved to the two-layer theory, explicit lineage relations, and the discovery lifecycle rather than being preserved under a cosmetically new name. When use exposed a missing relation, [ADR 054](../reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md) revised the successor arrangement instead of defending the first repair.
- The [tag-README redesign](../reference/tag-readme-trace-observed-causal-connection.md) changed instructions, schema, validation, and rendering; later validation used the new check and exposed a defect in the associated search recipe.
- [ADR 056](../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) revised the proposal and ADR lifecycle. [ADR 057](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md) then used its new alternatives requirement, and the adopted article proposal followed its archive rule.

Together these cases are more informative than a declaration that every file may be edited. They show theory replacement, vocabulary retirement, symbolic enforcement, revision of design machinery, and later dependence on installed successors. They leave open how evenly the affordance covers different target classes and whether it improves outcomes.

## What remains to establish

The stronger claim should be tested the way reflective coverage is tested: choose hard aspects, name the required operations, and look for a missing causal edge.

The first task is to map the six requirements above onto targets most likely to expose a special-case barrier: a core objective, an evaluator, an authority rule, the revision lifecycle, a natural-language theory, and a symbolic validator. The question is not whether a maintainer can edit each one. It is whether Commonplace's represented theory and machinery support diagnosis, comparison with an incumbent, operative installation, and another later challenge without inventing an entirely external process.

The second task is to consolidate the strongest episodes into causal traces. ADR 042 is the strongest theory-replacement candidate; ADR 053 followed by ADR 054 is the clearest recursive-revision candidate; ADR 056 followed by ADR 057 is the best revision-machinery reuse candidate. The evidence should pin what prompted each change, what made the replacement better, which artifacts installed it, which later operation depended on it, and whether the successor itself later became a target.

The third task is hostile search for an unsupported target. A missing specialized procedure is not enough: live theory and the workshop path are part of the claimed support. The counterexample must be a repository-defined component for which even those general resources provide no actionable route from criticism through warranted, operative change, leaving the maintainer to invent an unrecorded external process. Extending the theory or machinery to cover that case would then move the edge of the affordance.

Coverage remains relative to the canonical repository-defined organization and the hard target classes examined. Provider weights, inference infrastructure, and hosting stay outside [Commonplace's declared frame](../reference/commonplace-declared-frame.md); a vendored read-only copy likewise lacks the source-repository affordance unless its operator supplies an override or fork path.

## Relation to the Gödel machine

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) is a formal limit case: its incumbent formalization must prove that switching is better than continuing, even when the switch revises governing machinery. Commonplace instead uses fallible semantic and empirical warrant, including for changes to its current criteria. It can therefore admit useful changes that the proof gate cannot certify, but also bad ones. The [main article](./reflective-self-improvement.md) develops the comparison.
