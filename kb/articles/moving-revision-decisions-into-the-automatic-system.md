---
description: "Human-inclusive self-revision is the cheap case; moving a revision decision from maintainer to machinery costs representation — six items — and Commonplace's six-path audit shows which decisions could move and the two that cannot yet"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/computationally-directed-self-improvement-is-a-reallocation.md
  - kb/notes/methodological-and-computational-closure-track-different-changes.md
  - kb/notes/definitions/behavioral-authority.md
  - kb/notes/definitions/reflective-system.md
  - kb/notes/reflection-buys-addressability.md
  - kb/notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md
  - kb/notes/definitions/operative-change.md
  - kb/notes/definitions/discovery-lifecycle.md
  - kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md
  - kb/notes/llm-executed-methodologies-are-metacircular-interpreters.md
  - kb/notes/definitions/reach-assessment.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/improvements-can-accumulate-without-compounding.md
  - kb/notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md
  - kb/notes/evidence/commonplace-as-a-reflective-system.md
  - kb/notes/evidence/tag-readme-trace-observed-causal-connection.md
  - kb/reference/commonplace-declared-frame.md
  - kb/reference/storage-architecture.md
  - kb/reference/proposals/revise-behavioral-authority-decomposition.md
  - kb/reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md
  - kb/reference/adr/053-retire-distillation-without-a-successor-term.md
  - kb/reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md
  - kb/reference/adr/055-explanatory-reach-replaces-bare-reach-as-the-technical-term.md
  - kb/reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md
  - kb/reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md
  - kb/reference/adr/063-all-article-drafts-circulate-behind-a-banner.md
  - kb/reference/adr/069-collection-contract-bundles-become-one-time-prototypes.md
  - kb/tasks/recurring/review-explanatory-reach.md
---

# Moving revision decisions into the automatic system

> **Draft.** This article is circulating for comments; its claims, structure, and central thesis may still change. Counterexamples, disputed readings of the sources, and boundary cases are welcome through the repository's issue tracker.

A system whose declared boundary includes its maintainers revises itself easily. A team with design documents and a change process already inspects its own rules, argues about them, and installs successors; nothing about that is hard, and nothing about it needs a theory. The hard part is moving a revision *decision* — which rule to change, whether the successor earns adoption, who is entitled to install it — from the maintainer to the machinery. Each such move has a price, and the price is representation: the machinery can act only on what is addressable, apply only a method that is stated, judge only against a standard that is fixed, install only through a channel that is recorded, and continue only along a path that survives its own use. This article states the six items on that bill, reads one system's bill on six of its revision paths, and identifies the two decisions that cannot move yet because their inputs are not represented. The system is Commonplace, a framework for agent-operated knowledge bases, and the [companion article on theory building](./theory-building-inside-the-system.md) records the same kind of allocation for the functions of theory building; this one records it for the functions of revision.

A constitutional order shows why the human case is cheap and the machine case is not. Editing the authoritative text does not amend it. Recognized roles and procedures authorize the change, entry into the authoritative record installs it, and institutional application gives it force. If the order permits changes to its amendment rule, the same path can revise part of its own revision machinery. None of that needs to be written into the text, because the people in recognized roles carry it. Move any of those decisions to a machine and what the roles carried has to be written down, or the machine cannot perform them.

Commonplace's [declared boundary](../reference/commonplace-declared-frame.md) includes designated maintainers, while the systems compared in [the companion article on self-theories](./when-systems-learn-theories-about-themselves.md) report their boundaries around agent loops. Adding research teams would make those systems revisable too, and equally cheaply. The question here is not whether a human-inclusive system can revise itself but how much of its revision path is represented well enough for the machinery to take over a decision on it.

The audit tested a precise version of that readiness:

> Commonplace gives its human–agent operator a reusable path to revise any repository-defined artifact or relation through which behavioral authority or revision governance is exercised. The path supports identifying and criticizing the incumbent, developing a successor, warranting the transition, installing the successor in a live authority path, and later revising that successor.

[Behavioral authority](../notes/definitions/behavioral-authority.md) describes how a retained artifact shapes operation: who consumes it, through which channel, and with what force. **Complete addressability of behavioral authority** means that the human–agent process can inspect, criticize, and selectively revise every repository-defined artifact and relation in those paths, including the machinery governing revision. It does not require access to a maintainer's unarticulated judgment — but any decision that depends on that judgment stays with the maintainer.

A revision decision that has moved needs, besides addressability, an applicable revision method, warrant for adoption, operative installation, and continuity of the revision path. Substantive warrant and admission are distinct. Warrant supplies reasons to prefer the successor; admission identifies the actor or decision entitled to install it and binds that authorization to the installed version. Admission therefore cuts across the declared authority path and operative installation rather than serving as another evaluation criterion.

*Meta* remains a role within an episode, not a permanent layer. The process can repeat: each revision episode can apply the same addressability requirement to the authority-bearing arrangement left by the previous one.

The [six-path audit](../notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md) found the representation needed for a move present but uneven on the paths it examined. It did not establish complete coverage, and it says nothing about whether improvements compound.

## What a moved decision needs represented

Including humans makes a weak reflection claim easy: a maintainer can model the system and act on that model. A stronger claim requires a [self-representation to affect operation](../notes/definitions/reflective-system.md). The practical value of such a representation is [addressability](../notes/reflection-buys-addressability.md): a represented commitment can be inspected, criticized, selectively revised, and reused — by machinery as well as by people.

Editability is where the machine case starts, not where it ends. A revision decision performed by the machinery needs six things represented:

| Requirement | What its absence leaves with the maintainer |
|---|---|
| **Declared boundary, authority path, and purpose** | What is changing, how it shapes behavior, who may authorize the transition, and why one result is better — all reconstructed by a person each time. |
| **Complete addressability of behavioral authority** | Any repository-defined artifact or relation that shapes operation but is exempt from inspection and selective revision, or whose role and encoding must be rediscovered. |
| **Applicable revision method** | Inventing the approach afresh for this target. The method may route to open-ended theoretical reasoning rather than prescribe fixed steps, but the routing itself must be stated. |
| **Warrant for the transition** | Deciding whether the successor earns preference over the incumbent, or whether an uncertain change earns a bounded experiment instead. |
| **Operative installation** | Getting a warranted and authorized successor to a consumer with behavioral force. |
| **Continuity across successors** | Keeping the determination, admission, installation, and later-use path usable after a revision, so that the next change is not the maintainer's to arrange again. |

The narrower [repeatable-path test](../notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) traces representation, determination, admission, installation, dependence, and continuity for one redesign class.

These are logical requirements, not required components. A proposal-selection path can compare an explicit candidate with the incumbent and reject it. A direct update may instead use evidence under a rule that warrants the successor. Nothing here requires one search algorithm, evaluator, or design lifecycle for every change. Nor must the successor be a one-for-one replacement: a better arrangement may narrow a rule, split one concept into several, reroute its useful work, or remove an artifact whose role is no longer warranted. What matters is comparing the successor with continued use of the incumbent — and a decision that compares them is one the machinery can only make if the comparison's terms are represented.

Complete addressability, like [reflective coverage](../notes/evidence/commonplace-as-a-reflective-system.md), is relative to a declared boundary and an operation profile. Commonplace strongly supports inspection and revision of natural-language theory, types, and validators. Its paths for objectives, evaluator validity, and authority arrangements are weaker. A repository-defined model request can also diverge from the model that actually executes.

## How the revision path works

Commonplace does not rely on one universal revision algorithm. Instead, it combines general theory, specialized methods, and operative artifacts. The audit found four recurring parts on the paths it examined:

- **The governing arrangement is represented.** Collection contracts, routing rules, instructions, review criteria, ADRs, schemas, validators, configuration, and code expose both authority-bearing artifacts and many of the relations through which they shape operation.
- **Candidates can be developed and evaluated.** Workshops hold open problems until their results are ready for the library. Established changes can follow specialized methods; new ones can use the [discovery lifecycle](../notes/definitions/discovery-lifecycle.md) and Commonplace's [two-layer execution model](../notes/theory-and-methodology-form-a-two-layer-execution-system.md), which keeps theory and human semantic judgment available when no method settles the case. Evaluation follows representational form: natural-language theory needs criticism and semantic judgment, while symbolic commitments can use tests, schemas, invariants, or proofs.
- **Accepted changes can become operative.** Instructions, contracts, code, configuration, and validators give an admitted decision a consumer, channel, and force. The [operative-change test](../notes/definitions/operative-change.md) rejects revisions that are merely written down.
- **The result remains available for another pass.** ADRs retain accepted design reasoning, canonical artifacts retain the result, and the [storage layer](../reference/storage-architecture.md) supports diff review, rollback, attribution, and reconstruction. History is not the obligatory read path, but it can help a later challenge recover what changed and why.

Agents and maintainers work through contracts, skills, review criteria, definitions, and code that they can also revise. Those artifacts exercise behavioral authority when agents and maintainers use them to govern their work. This self-application structurally resembles a [metacircular interpreter](../notes/llm-executed-methodologies-are-metacircular-interpreters.md): the rules are artifacts inside the system they govern. When those rules do not settle the next choice, live theory and human judgment provide the fallback — which is to say the decision has not moved, and retaining the result in operative artifacts is what makes it a candidate to move next time.

## A governing criterion revised in practice

Explanatory-reach is the property that an explanation keeps working beyond the cases that produced it because it captures why the pattern works. Commonplace's root vocabulary names it, the notes collection uses it as a quality goal, and a semantic review gate applies it when deciding which theoretical claims deserve retention and reuse.

That criterion has itself been revised. The anchor theory replaced a sharp contrast between adaptive and explanatory claims with a polarity, added a test against rival practices, and required observed fit. The revised account entered the notes collection contract and the [recurring explanatory-reach review](../tasks/recurring/review-explanatory-reach.md). The later [reach-assessment definition](../notes/definitions/reach-assessment.md) reused all four parts, and [ADR 055](../reference/adr/055-explanatory-reach-replaces-bare-reach-as-the-technical-term.md) made the name unambiguous across the corpus.

This is substantive theory revision, not just proof that the files are editable, and it shows where the decisions sat. The criticism that motivated the revision, the candidate replacement, and the tests it had to pass were produced with agents in the loop; the decision to adopt was the maintainer's. The audit confirms that the semantic gate is routinely invoked — the *application* of the revised criterion has moved. But the gate omits the revised test's observed-fit requirement, and no retained review shows later dependence on all four parts. The evidence therefore shows that the criterion can be revised and reused, not that later evaluation depends on every part of the revision.

The same path could challenge the core criterion, not just refine or rename it. If counterexamples showed that explanatory-reach rejects useful explanations or rewards a rhetorical shape rather than real transfer, a successor would need to explain that failure and preserve what the old criterion got right. It would then need to survive stated tests, be installed across its authority paths, and govern later review. Until a better successor earns adoption, retaining the incumbent is the normal result of comparing change with continuation.

## Other revision cases

Commonplace has already changed several kinds of load-bearing machinery:

| Change | What it shows |
|---|---|
| [ADR 042](../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) replaced a claimed exhaustive taxonomy after a worked collection supplied a counterexample; [ADR 069](../reference/adr/069-collection-contract-bundles-become-one-time-prototypes.md) later corrected its successor. | A conceptual framework and its replacement can both be challenged. |
| [ADR 053](../reference/adr/053-retire-distillation-without-a-successor-term.md) retired a load-bearing term whose uses had opposite maintenance requirements; [ADR 054](../reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md) later extended the replacement arrangement. | Revision can remove a category and redistribute its useful work instead of preserving it under a new name. |
| The [tag-README redesign](../notes/evidence/tag-readme-trace-observed-causal-connection.md) changed instructions, schema, validation, and rendering; later validation exposed a defect in the associated search recipe. | A symbolic rule can become operative, be reused, and force another correction — and once codified, its application needs no maintainer. |
| [ADR 056](../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) revised the proposal and ADR lifecycle; [ADR 057](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md) used the new requirement, and [ADR 063](../reference/adr/063-all-article-drafts-circulate-behind-a-banner.md) later revised the resulting article lifecycle. | Revision machinery can govern a later decision and remain open to another change. |

Together, these cases establish breadth across theory, vocabulary, symbolic enforcement, and design machinery. In every one of them the adoption decision was a maintainer's. What has moved is the work around that decision: noticing, drafting, checking, and — for codified rules — application.

## The two decisions that cannot move yet

The audit examined global goals, the explanatory-reach criterion, tag-README validation, the revision lifecycle, model bindings, and maintainer admission. It found inspectable goals, contracts, criteria, procedures, validator rules, and model requests. The validator and lifecycle cases also showed installed machinery being reused and revised. That supports readiness on the examined paths, not complete coverage, and two paths show a decision whose inputs are not represented at all.

The first is generic maintainer admission. In the constitutional analogy, Commonplace resembles an order with several amendment procedures that refer to designated officials. But no general record states who holds office, what the grant covers, which conditions admit a proposed change, or which approval authorized the operative text. The installed artifact can still govern behavior, but the admission path that made it incumbent is not represented. That is not a defect in human-inclusive self-revision — the maintainers know who they are — but it is the reason the admission decision cannot move: there is nothing for the machinery to read. The [companion article on theory building](./theory-building-inside-the-system.md) records admission as a human row for the same reason.

The second is model realization. The repository makes the requested model, alias, and freshness partition addressable. But retained evidence shows a divergence between requested or recorded model identity and actual execution. Any decision that depends on which model actually ran — whether a review result is comparable with another, whether a baseline still applies — cannot be made by machinery reading the record, because the record can be wrong. This is an operative-realization gap, not an addressability failure of the request.

A third limit is in the representation scheme itself. A gate's target cohort can change while its consumer, channel, and force stay fixed; a validator's target type and invocation trigger can change under the same conditions. The current three-part decomposition of behavioral authority therefore does not fully identify an authority path, and a decision that depends on applicability cannot be made from it. The live [decomposition proposal](../reference/proposals/revise-behavioral-authority-decomposition.md) leaves one choice open: whether applicability should be a fourth field or a required qualifier. Authorization, runtime realization, and dependency closure remain separate questions.

The audit covers six paths within [Commonplace's declared frame](../reference/commonplace-declared-frame.md). Provider weights, inference infrastructure, and hosting lie outside that frame. Wider coverage may reveal another unrepresented input.

## Warrant and compounding are separate questions

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md), a proof-governed self-modifying architecture, provides a contrast in warrant. Its incumbent formalization must prove that switching is better than continuing, even when the switch revises governing machinery; every revision decision has moved, at the price of admitting only provable ones. Commonplace instead uses fallible semantic and empirical warrant. It can therefore admit useful changes that the proof gate cannot certify, but also bad ones, and the warrant decision has stayed with a person. This contrast concerns which changes may be admitted and who admits them, not whether improvement compounds.

Even complete representation would not establish compounding. That requires evidence that retained benefits [help produce later improvements](../notes/improvements-can-accumulate-without-compounding.md), directly or through reinvested savings, and that this feedback persists across episodes. The [companion article on self-theories](./when-systems-learn-theories-about-themselves.md) develops both the compounding test and the Gödel-machine comparison.

## Where to go next

The [six-path audit](../notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md) is the evidence this article reads. The [reallocation note](../notes/computationally-directed-self-improvement-is-a-reallocation.md) states why the interesting transition runs inside the category of self-revising systems rather than across it, and the [closure note](../notes/methodological-and-computational-closure-track-different-changes.md) separates a decision settled by method from a decision that needs no human. The [companion article on theory building](./theory-building-inside-the-system.md) records the same allocation for the functions of theory building, and [*When systems learn theories about themselves*](./when-systems-learn-theories-about-themselves.md) develops the reflective case and the compounding test.
