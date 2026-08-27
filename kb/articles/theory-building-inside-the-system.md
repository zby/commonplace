---
description: "With a judgment-capable interpreter, functions of theory building — applying, criticizing, deriving, proposing — can move from human to computational actors inside a declared boundary; records one allocation, where it stopped, and what to record next"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/computationally-directed-self-improvement-is-a-reallocation.md
  - kb/notes/increasing-computational-autonomy-relocates-human-effort.md
  - kb/notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md
  - kb/notes/methodological-and-computational-closure-track-different-changes.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
  - kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md
  - kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md
  - kb/notes/definitions/codification.md
  - kb/notes/documentation-generates-the-system-rather-than-describing-it.md
  - kb/notes/an-action-model-matters-only-through-its-consumption-path.md
  - kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md
  - kb/notes/skills-derive-from-methodology.md
  - kb/notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md
  - kb/notes/definitions/system-definition-artifact.md
  - kb/notes/definitions/context-engineering.md
  - kb/notes/evidence/tag-readme-trace-observed-causal-connection.md
  - kb/reference/commonplace-declared-frame.md
  - kb/reference/adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md
  - kb/sources/argyris-organizational-learning-and-mis-1977.ingest.md
  - kb/sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md
---

# Theory building inside the system

> **Draft.** This article is circulating for comments; its claims, structure, and central thesis may still change. Counterexamples, disputed readings of the sources, and boundary cases are welcome through the repository's issue tracker.

Naur argued that a program's theory — the capacity to map it onto the world, justify its parts, and extend it coherently — cannot be reduced to the program plus written rules, and that it therefore lives only in programmers. A [companion article](./what-bound-naurs-theory-to-programmers.md) accepts the first claim and argues that the argument for the second runs through a premise that was true of the programs Naur describes and is no longer true in general: on his own reading of "formulated," machine execution no longer requires a formulated rubric, so an interpreter inside a system can apply retained natural-language theory with a judgment the text alone does not carry. This article takes that as its premise and asks what follows for a system built around such an interpreter. It does not ask whether the system *holds* a theory. That question has a cheap answer and an unshowable one — cheap if the maintainers are counted inside the system, since any team with design documents and a change process then qualifies; unshowable if they are not, since no composite has yet passed Naur's tests without them. The question that has a measurable answer is which *functions* of theory building the computational part of the system now supplies. The article states what makes a retained theory operative rather than documentary, how an operative theory becomes learned state, which functions of that loop have moved from human to computational actors in this project and where the movement stopped, and what formalization and proof do and do not remove from the picture. The case where the retained theory is about the system that consumes it is the subject of a [further article](./when-systems-learn-theories-about-themselves.md).

## The boundary, declared

Everything below is read against a declared system boundary that includes the base model, the retained artifacts, the validators and agents that consume them, and the maintainers who admit changes — the [frame Commonplace declares](../reference/commonplace-declared-frame.md). Declaring the boundary this way makes membership uninteresting on purpose. Under a boundary-relative definition, [ordinary software maintained by humans already counts as a system that builds and revises its own theory](../notes/computationally-directed-self-improvement-is-a-reallocation.md); growing machine capability does not change that verdict, because the verdict was never about machines. What changes with a judgment-capable interpreter is the *allocation*: which of the functions that theory building requires are performed by a human, which by the computational machinery, and which jointly. That allocation can be recorded for one system at one time and re-recorded later, which is what makes "theory building inside the system" a claim with evidence rather than a slogan.

The functions come from Naur's three capabilities, decomposed at the grain at which this project can trace who did what: apply the theory to a case; criticize a claim against the theory and its gates; derive consequences from it — procedures, checks, code; propose a revision when a failure is read against it; modify the theory coherently within the structure it explains; admit the revision; and choose which demand to work on. The sections that follow describe the loop those functions belong to, then report the allocation.

## Operative, not documentary

An interpreter inside the system is necessary but not sufficient. A retained theory — one persisted as an artifact that later work can load — can be present, readable, and inert. In his work on organizational learning, Chris Argyris distinguished espoused theories, which people report as governing their actions, from theories-in-use, which actually govern them ([source analysis](../sources/argyris-organizational-learning-and-mis-1977.ingest.md)). The same distinction appears in an agent system: [an action model matters only through its consumption path](../notes/an-action-model-matters-only-through-its-consumption-path.md).

Routing and loading place a theory in a possible causal path, but they do not make it operative. A model call has a bounded context, and a theory that is absent cannot participate. [Context engineering](../notes/definitions/context-engineering.md) determines which retained artifacts reach which call, when, and at what scope. Yet presence in context is not use. A theory becomes operative only when a consumer gives it behavioral authority and uses it in a decision, route, or acceptance judgment. A note that is stored but never surfaced governs nothing; a note that is surfaced but ignored governs nothing either. In Commonplace, notes are routed individually so an agent can load the theory relevant to a decision rather than the whole theory layer.

Why preserve a model instead of acting directly? In his 1943 account of thought, Kenneth Craik argued that a working model lets an organism try alternatives before committing in the world because the model is cheaper, faster, or safer to run ([source analysis](../sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md); cited from the source, no passage is quoted here). A retained theory of a design likewise lets an agent test a proposed change against the design's rationale before changing the codebase. This explains what operative theory can do; it says nothing yet about who does it.

## From operative theory to learned state

Consulting an operative theory need not change it. The theory becomes learned state only through a governed, behavior-changing loop. That loop attributes a failure to a premise or boundary in the current theory, proposes a correction, evaluates the correction against evidence and rival explanations, and admits the result. It then retains the revised theory and changes later behavior by consuming the new version or regenerating derived procedures. If a revision is not evaluated, admitted, retained, and reused, the system has recorded a candidate or patched a case; it has not completed the learning pathway claimed here.

Call a learning pathway [theory-mediated](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) when it represents a candidate theory as an intermediate object and changes behavior by adopting, applying, rejecting, or revising it. A direct response to a failure patches the case. A theory-mediated response first revises an explanation and then derives consequences from the revision. What makes the intermediate object a theory rather than a rule is not that it can be edited but that consequences are derived from it and the next failure is read against it, so that revising one premise reaches every case derived from it.

Suppose a coding agent observes that several documentation-only changes need no integration tests. It can retain the rule "documentation files are safe," or the theory "a changed file cannot affect integration behavior when no executed process consumes it." When a build tool starts reading one documentation file as configuration, the rule offers no explanation for the exception and invites case-by-case enumeration. The theory instead identifies the changed premise and supports a precise revision: the exemption applies only to files that no executable tooling consumes. Every later decision that consumes the current theory, or every derived procedure that the system regenerates from it, can inherit that revision. Derivatives that have already been materialized remain stale until the system regenerates them.

That reach is both the gain and the risk. A broad theory that is wrong fails as widely as it would have been useful, and a theory that fits every failure so far can still be the wrong one. The pathway therefore needs an evaluator that tests candidate revisions against evidence and rival explanations beyond the cases that produced them.

One common consequence of a retained theory is a procedure. Repeating the same reasoning on every occasion is expensive, so recurring reasoning can be promoted into a skill, checklist, or review criterion that handles the common case directly. The [two-layer execution system](../notes/theory-and-methodology-form-a-two-layer-execution-system.md) keeps the derived procedure as the fast path while leaving the theory available for cases the procedure cannot decide. Repeated fallback reasoning signals another promotion opportunity. This is *theory-mediated methodology*, and [skills derived from methodology](../notes/skills-derive-from-methodology.md) are its concrete realization in Commonplace. It is only one form of theory-mediated learning: a theory can also guide diagnosis, experiment choice, or the interpretation of a result.

## Who supplies each function

The loop above names functions, and each has an actor. Recording who performs each function against the declared boundary is the reading of autonomy that [avoids scoring a system as a percentage](../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md): decision content is continuous, so "the machine does 40% of the theory building" has no principled meaning, while "the machine applies and criticizes, a human admits" does. [Computational closure](../notes/methodological-and-computational-closure-track-different-changes.md) is the name for a function whose execution needs no human decision; a pathway is computationally closed only when every function is.

The table records the allocation in Commonplace as its traced episodes show it. A row is *computational* when the traced instances were performed by model calls without a human decision, *human* when a person performed them, and *joint* when the machinery proposed and a person decided.

| Function of theory building | Actor in traced episodes | Evidence |
|---|---|---|
| Apply the theory to a case | computational | routed notes consumed in deciding calls; the operative section above |
| Criticize a claim against the theory and gates | computational | the repair episode below: the critique was correct in both cycles |
| Derive consequences — procedures, validators | computational, human-admitted | skills derived from methodology; the [topic-index convention codified as a validator](../notes/evidence/tag-readme-trace-observed-causal-connection.md) |
| Propose a revision to the theory | computational | the repair episode: each cycle produced a candidate repair |
| Modify the theory coherently within its structure | human | the repair episode: the machinery's repairs were patches; one maintainer sentence fixed each |
| Admit a revision | joint, human-decided | the pass hands claim-level changes back [by design](../reference/adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) |
| Choose which demand to work on | human | every traced case: the maintainer noticed the strain and initiated the change |

The repair episode that fills three rows is reported in full in the [companion article on Naur](./what-bound-naurs-theory-to-programmers.md); what matters here is where it places the boundary. The project's automated improvement pass was run twice over the note behind that article. In both cycles the pass criticized correctly — it found a genuine overreach with a counterexample that held — and proposed a repair. In both cycles the repair retreated to a true, gate-proof claim that was no longer the claim the note was for, although the note's purpose was stated in its inputs. One sentence from the maintainer restored the intended claim each time. Criticism and proposal had moved to the computational side; coherent modification within the structure had not. That is one function, located by one episode, and it is the datum this article rests on. It is also Naur's third capability — extending the theory coherently when a demand arrives — and his own compiler case predicts exactly this pattern for a bearer that has the text and not the theory.

Two things follow from reading the boundary this way. The functions on the computational side are not thereby *closed*: reliability across occasions is one of Naur's tests, and one episode shows an allocation, not a disposition. And the functions on the human side are not thereby fixed: a maintainer holds them in this project because nothing in the machinery has been shown to hold them, which is an observation about the current profile and not an argument that it cannot move.

## Formalization moves the open question; it does not remove it

Once part of a theory stabilizes, [codification](../notes/definitions/codification.md) can encode the projection a formal consumer needs as a schema, validator, or code while leaving the wider theory open to revision. A [pre-formal prototype stage](../notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) keeps unsettled concepts available for criticism before a formal consumer fixes one projection of them. Codifying too early raises the cost of replacement once downstream machinery depends on that projection.

A stronger formalization gives a stabilized part a model whose consequences can be proved: for example, a specification and a proof that an implementation satisfies it, or a verified property of a protocol. [Formal systems assess a theory's reach through causal and proof obligations](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md). Within a supplied formal language, they can discharge those obligations with a certainty that natural-language criticism cannot match.

What a proof establishes remains conditional. It shows that a property follows from stated assumptions; it does not show that those assumptions describe the relevant affairs of the world. The proof removes uncertainty from the derivation, but not from the mapping between the informal theory and the formal model. Stronger verification therefore increases the relative importance of that boundary instead of removing it.

Language models act on both sides of the boundary. They make informal theory operative, and they make formalization cheaper to produce — though warranted acceptance of a formalization stays [bounded by what can be verified](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), so cheaper generation is not cheaper acceptance. What they do not supply is a check that the formal assumptions match the world. In the allocation of the previous section, that check is one more function, and it sits on the human side: derivation inside the model has moved to the machinery because it can be checked; the theory–model correspondence is where the check, and the reallocation, currently run out.

## What a later profile must record

The allocation above is one system at one time. The claim that the computational share is *growing* is a hypothesis the profile makes testable, not something one snapshot shows, and three constraints govern the comparison.

The comparison grain must be fixed in advance. A function recorded coarsely — "criticism" — can hide a reallocation inside it, such as a new noticing channel replacing a human's reading; a function recorded finely may not be commensurable with an earlier profile. State the function list before the next profile is taken, and record changes of mechanism inside a function separately from changes of actor.

Measure improvement per human judgment, not per human hour. When a routine function closes, the system can attempt harder improvements, and [human attention moves to the new frontier rather than disappearing](../notes/increasing-computational-autonomy-relocates-human-effort.md). Falling hours would be the wrong test; the right one is whether the decisions a human still makes are fewer, later, or higher.

Pre-register what would move a function. For coherent modification, Naur's third test supplies it: state in advance how many occasions of coherent extension, on demands the machinery did not choose, would count as the function having moved. The episode in this article was visible as a boundary only afterwards; pre-registering the test would have made it a measurement.

The endpoint question — whether the boundary can eventually be contracted to exclude the maintainers — is the question the reallocation frame poses and this article does not answer. Its evidence is one profile and one located boundary; what it claims is that the profile is the right thing to record.

## Where this leads

Moving functions of theory building to the computational side does not by itself make a system reflective or self-improving. A theory of a market can mediate learning without describing the agent, and a system can rewrite its prompts from a score without holding any theory. Theory building becomes reflective when the retained theory describes the system that consumes it, the system's own failures revise that theory, and the resulting changes alter the organization the theory explains. [*When systems learn theories about themselves*](./when-systems-learn-theories-about-themselves.md) develops that case and the evidence it requires, and reads this article's allocation as one of its inputs.

## Where to go next

The [companion article on Naur](./what-bound-naurs-theory-to-programmers.md) carries the argument this article rests on and the repair episode that locates its boundary. The [reallocation note](../notes/computationally-directed-self-improvement-is-a-reallocation.md) states why the interesting transition runs inside the category rather than across it, and the [closure note](../notes/methodological-and-computational-closure-track-different-changes.md) gives the actor-allocation reading the table uses. The [theory-mediated learning note](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) states the general pathway as a conjecture and designs the experiment that would test it. The [two-layer execution note](../notes/theory-and-methodology-form-a-two-layer-execution-system.md) is the fuller statement of theory-mediated methodology, and the [pre-formal stage note](../notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) the argument for keeping unsettled theory in prose. The [human-inclusive revision article](./moving-revision-decisions-into-the-automatic-system.md) develops the boundary and admission machinery the table's human rows depend on.
