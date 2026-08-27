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

Naur argued that a program's theory — the capacity to map it onto the world, justify its parts, and extend it coherently — cannot be reduced to the program plus written rules, and therefore lives only in programmers. A [companion article](./what-bound-naurs-theory-to-programmers.md) argues that his case for the second claim runs through a premise no longer true in general — that a machine judges only by criteria someone has formulated — so an interpreter inside a system can apply retained natural-language theory with a judgment the text alone does not carry. This article takes that as given and asks what follows for a system built around such an interpreter. It does not ask whether the system *holds* a theory. The question with a measurable answer is which *functions* of theory building the computational part of the system now supplies. In this project the answer is: applying a theory to a case, criticizing a claim against it, deriving procedures from it, and proposing revisions are performed by model calls; modifying the theory coherently, admitting a revision, and choosing what to work on are not. The article says what makes a retained theory operative, how it becomes learned state, where that allocation was located and by what, and what formalization does and does not remove.

## The boundary, declared

Everything below is read against a declared system boundary that includes the base model, the retained artifacts, the validators and agents that consume them, and the maintainers who admit changes — the [frame Commonplace declares](../reference/commonplace-declared-frame.md). Declaring the boundary this way makes membership uninteresting on purpose. Whether the system holds a theory has a cheap answer if the maintainers are counted in — any team with design documents and a change process then qualifies, and [ordinary maintained software already counts](../notes/computationally-directed-self-improvement-is-a-reallocation.md) — and an unshowable one if they are not, since no composite has yet passed Naur's tests without them. What changes with a judgment-capable interpreter is the *allocation*: which of the functions theory building requires are performed by a human, which by the machinery, and which jointly. An allocation can be recorded for one system at one time and re-recorded later. The functions come from Naur's three capabilities, decomposed at the grain at which this project can trace who did what; the table below introduces them.

## Operative, not documentary

An interpreter inside the system is necessary but not sufficient. A retained theory — one persisted as an artifact that later work can load — can be present, readable, and inert. In his work on organizational learning, Chris Argyris distinguished espoused theories, which people report as governing their actions, from theories-in-use, which actually govern them ([source analysis](../sources/argyris-organizational-learning-and-mis-1977.ingest.md)). The same distinction appears in an agent system: [an action model matters only through its consumption path](../notes/an-action-model-matters-only-through-its-consumption-path.md).

Routing and loading place a theory in a possible causal path, but presence in context is not use. A model call has a bounded context, and [context engineering](../notes/definitions/context-engineering.md) determines which retained artifacts reach which call, when, and at what scope; a theory becomes operative only when a consumer gives it behavioral authority and uses it in a decision, route, or acceptance judgment. In Commonplace, notes are routed individually so an agent can load the theory relevant to a decision rather than the whole theory layer.

Why preserve a model instead of acting directly? Kenneth Craik's 1943 answer, paraphrased from the [source](../sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md), is that a working model lets an organism try alternatives before committing in the world, because the model is cheaper, faster, or safer to run. A retained theory of a design likewise lets an agent test a proposed change against the design's rationale before changing the codebase.

## From operative theory to learned state

Consulting an operative theory need not change it. The theory becomes learned state only through a governed, behavior-changing loop: a failure is attributed to a premise or boundary in the current theory, a correction is proposed, evaluated against evidence and rival explanations, and admitted; the revised theory is retained and changes later behavior by being consumed or by regenerating derived procedures. A revision that is not evaluated, admitted, retained, and reused leaves a candidate or a patched case.

Call a learning pathway [theory-mediated](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) when it represents a candidate theory as an intermediate object and changes behavior by adopting, applying, rejecting, or revising it. A direct response to a failure patches the case; a theory-mediated response first revises an explanation and then derives consequences from the revision. What makes the intermediate object a theory rather than a rule is not that it can be edited but that consequences are derived from it and the next failure is read against it, so that revising one premise reaches every case derived from it.

Suppose a coding agent observes that several documentation-only changes need no integration tests. It can retain the rule "documentation files are safe," or the theory "a changed file cannot affect integration behavior when no executed process consumes it." When a build tool starts reading one documentation file as configuration, the rule offers no explanation for the exception and invites case-by-case enumeration. The theory identifies the changed premise and supports a precise revision: the exemption applies only to files that no executable tooling consumes. Every later decision that consumes the current theory, and every derived procedure the system regenerates from it, inherits that revision; derivatives already materialized stay stale until regenerated.

That reach is both the gain and the risk. A broad theory that is wrong fails as widely as it would have been useful, and a theory that fits every failure so far can still be the wrong one. The pathway therefore needs an evaluator that tests candidate revisions against evidence and rival explanations beyond the cases that produced them.

One common consequence of a retained theory is a procedure. Recurring reasoning is expensive to repeat, so it can be promoted into a skill, checklist, or review criterion that handles the common case directly. The [two-layer execution system](../notes/theory-and-methodology-form-a-two-layer-execution-system.md) keeps the derived procedure as the fast path while leaving the theory available for cases the procedure cannot decide. This is *theory-mediated methodology*, and [skills derived from methodology](../notes/skills-derive-from-methodology.md) are its concrete realization here; methodology is only one consequence a theory can have.

## Who supplies each function

Recording who performs each function against the declared boundary is the reading of autonomy that [avoids scoring a system as a percentage](../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md): decision content is continuous, so "the machine does 40% of the theory building" has no principled meaning, while "the machine applies and criticizes, a human admits" does. [Computational closure](../notes/methodological-and-computational-closure-track-different-changes.md) names a function whose execution needs no human decision; a pathway is closed only when every function is.

The table records the allocation in Commonplace as its traced episodes show it. A row is *computational* when the traced instances were performed by model calls without a human decision, *human* when a person performed them, and *joint* when the machinery proposed and a person decided.

| Function of theory building | Actor in traced episodes | Evidence |
|---|---|---|
| Apply the theory to a case | computational | routed notes consumed in deciding calls; the operative section above |
| Criticize a claim against the theory and gates | computational | the repair episode below: the critique was correct in both cycles |
| Derive consequences — procedures, validators | computational, human-admitted | skills derived from methodology; the [topic-index convention codified as a validator](../notes/evidence/tag-readme-trace-observed-causal-connection.md) |
| Propose a revision to the theory | computational | the repair episode: each cycle produced a candidate repair |
| Modify the theory coherently within its structure | human | the repair episode: the machinery's repairs were patches; one maintainer sentence fixed each |
| Admit a revision | joint | the pass hands claim-level changes back [by design](../reference/adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) |
| Choose which demand to work on | human | every traced case: the maintainer noticed the strain and initiated the change |

The repair episode that fills three rows is reported in full in the [companion article on Naur](./what-bound-naurs-theory-to-programmers.md); what matters here is where it places the boundary. The project's automated improvement pass was run twice over the note behind that article. In both cycles the pass criticized correctly — it found a genuine overreach with a counterexample that held — and proposed a repair. In both cycles the repair retreated to a true, gate-proof claim that was no longer the claim the note was for, although the note's purpose was stated in its inputs. One sentence from the maintainer restored the intended claim each time. Criticism and proposal had moved to the computational side; coherent modification within the structure had not. That is one function, located by one episode. It is also Naur's third capability — extending the theory coherently when a demand arrives — and his own compiler case predicts exactly this pattern for a bearer that has the text and not the theory.

An allocation is not a disposition. A function performed by model calls in one episode is not thereby *closed*: reliability across occasions is one of Naur's tests. And a function performed by a person is not thereby fixed: a maintainer holds it here because nothing in the machinery has been shown to hold it.

## Formalization moves the open question; it does not remove it

Once part of a theory stabilizes, [codification](../notes/definitions/codification.md) can encode the projection a formal consumer needs as a schema, validator, or code while leaving the wider theory open to revision. A [pre-formal prototype stage](../notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) keeps unsettled concepts available for criticism before a formal consumer fixes one projection of them; codifying too early raises the cost of replacement once downstream machinery depends on that projection.

A stronger formalization gives a stabilized part a model whose consequences can be proved: a specification and a proof that an implementation satisfies it, or a verified property of a protocol. [Formal systems assess a theory's reach through causal and proof obligations](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md), and within a supplied formal language they discharge those obligations with a certainty natural-language criticism cannot match. What a proof establishes remains conditional: a property follows from stated assumptions, and nothing in the proof shows that those assumptions describe the relevant affairs of the world. Stronger verification therefore raises the relative importance of the mapping between the informal theory and the formal model.

Language models act on both sides of that mapping. They make informal theory operative, and they make formalization cheaper to produce, though acceptance stays [bounded by what can be verified](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md). What they do not supply is a check that the formal assumptions match the world. In the allocation above, that check is one more function, and it sits on the human side: derivation inside the model has moved to the machinery because it can be checked; the theory–model correspondence is where the check, and the reallocation, currently run out.

## What a later profile must record

The allocation above is one system at one time. The claim that the computational share is *growing* is a hypothesis the profile makes testable, not something one snapshot shows, and three constraints govern the comparison.

The comparison grain must be fixed in advance. A function recorded coarsely — "criticism" — can hide a reallocation inside it, such as a new noticing channel replacing a human's reading; a function recorded finely may not be commensurable with an earlier profile. State the function list before the next profile is taken, and record changes of mechanism inside a function separately from changes of actor.

Measure improvement per human judgment, not per human hour. When a routine function closes, the system can attempt harder improvements, and [human attention moves to the new frontier rather than disappearing](../notes/increasing-computational-autonomy-relocates-human-effort.md). The right test is whether the decisions a human still makes are fewer, later, or higher.

Pre-register what would move a function. For coherent modification, Naur's third test supplies it: state in advance how many occasions of coherent extension, on demands the machinery did not choose, would count as the function having moved. The episode above was visible as a boundary only afterwards; pre-registering the test would have made it a measurement.

The endpoint question — whether the boundary can eventually be contracted to exclude the maintainers — is the question the reallocation frame poses and this article does not answer. What it claims is that the profile is the right thing to record.

## Where this leads

Moving functions of theory building to the computational side does not by itself make a system reflective or self-improving. A theory of a market can mediate learning without describing the agent, and a system can rewrite its prompts from a score without holding any theory. Theory building becomes reflective when the retained theory describes the system that consumes it, the system's own failures revise that theory, and the resulting changes alter the organization the theory explains. [*When systems learn theories about themselves*](./when-systems-learn-theories-about-themselves.md) develops that case and reads this article's allocation as one of its inputs; the [article on moving revision decisions](./moving-revision-decisions-into-the-automatic-system.md) records the same allocation for the functions of revision and explains why the admission row is human. The notes linked above carry the fuller arguments.
