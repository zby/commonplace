---
description: For consequential agent handoffs, explains why preserving intent while delegating means depends on governed authority, information, composition, feedback, and recovery rather than prompt length.
type: kb/types/note.md
traits:
  - title-as-claim
  - has-comparison
  - has-external-sources
---

# Intent-framed delegation is a control regime; prompt length does not establish it

In a consequential planner--executor handoff, intent-framed delegation
preserves upstream purpose and non-negotiable boundaries while a competent
executor with a relevant execution-time information advantage chooses means
inside a governed relation. The operative object is the allocation of
information and decision rights across the execution boundary. Prompt text is
one possible carrier within that arrangement. Its brevity does not establish
that the arrangement can preserve intent under the relevant failure modes; a
short handoff can be structurally adequate when the surrounding system supplies
the control relation.

## The source methodologies formulate bounded delegation

The [MCDP 1 formulation](../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md)
assigns a mission and purpose, leaves situation-dependent means to a competent
actor near the action, limits authority, constrains method where coordination
requires it, and expects reporting. The
[ADRP 6-0 formulation](../sources/us-army-adrp-6-0-mission-command-2012.ingest.md)
combines objective-oriented orders and resources with point-of-action
initiative, specified authority, coordination, supervision, accountability,
and retained upstream responsibility. Their overlap witnesses bounded
delegation. [Stahel's historical account](../sources/david-stahel-auftragstaktik-mission-command.ingest.md)
warns that older *Auftragstaktik* and later principles are not identical, so
the overlap should not be recast as one timeless doctrine. The retained
extracts formulate source-side control patterns; they do not supply an
LLM-agent outcome comparison.

## The shared mechanism is intent-preserving delegated adaptation

For this note, **intent-preserving delegated adaptation** is present when
upstream fixes a purpose-bearing result and non-negotiable decision boundaries,
gives a defined executor authority to choose execution-dependent means, and
keeps that choice answerable to the fixed intent and boundaries. The executor
must be competent for the delegated decision: it can interpret the assignment,
assess feasible means from available evidence, stay within bounds, and
recognize when it cannot decide safely. Its information advantage is also
decision-specific. Execution-time facts must be absent or stale upstream and
capable of changing which permitted means best serve the intent; the executor
need not know more overall. These are proposed truth conditions for the narrow
transfer, not an experimentally proven minimum or a sufficient implementation
packet.

## Transfer requires the same mechanism in the target

Because [borrowed patterns transfer only over a shared mechanism](./borrowed-patterns-transfer-only-over-shared-mechanism.md),
an agent system must independently instantiate the relevant information and
authority relation. Upstream must hold purpose or binding constraints that the
executor cannot safely reconstruct. The executor must have access to execution
evidence that can affect its choice of means, a real boundary over that choice,
and a governed route by which its result affects the surrounding system,
whether through integration into composed work or authorized external action.
This match makes the source pattern relevant; it does not carry over
source-domain machinery or establish target-domain effectiveness.

## The information asymmetry runs in both directions

Upstream must preserve what live state cannot recover: intent, cross-task
coupling, privileged facts, constraints, external commitments, output
ownership, and done conditions. The executor should use current state, tool
results, local failures, newly exposed constraints, and evidence produced
during execution when selecting authorized means. This applies the principle
to [fix what the executor cannot determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md).
It explains both why the executor cannot reconstruct the commission from local
evidence and why upstream should not precompute a method that later evidence
may overturn.

## A control regime governs the consequential surfaces

In this note, a handoff is consequential when the surrounding system cannot
treat a plausible execution-boundary failure as harmless. Examples include a
failure that changes acceptance of composed work, violates an authority or
external commitment, contaminates peer work, or prevents required recovery.
At such a boundary, delegation is structurally adequate for preserving intent
only if it supplies an operative mechanism for every control surface whose
failure matters: the worker's authority boundary; access to relevant context
and resources; ownership and integration of its output; feedback or
verification; and recovery or escalation. Depending on the surface, an
operative mechanism may provide a needed input or decision right, constrain
action, route or own output, expose deviation, or return control.

These surfaces are a Commonplace consequence of the shared mechanism, not a
formulation taken from the military sources. The source formulations supply
the authority, resource, coordination, reporting, and supervision analogues.
The live-evidence premise comes from the author--executor information boundary,
while [coordination guarantees](./agent-orchestration-needs-coordination-guarantees-not-just.md)
supply the ownership, verification, composition, and accountability concerns.
A prompt, tool policy, sandbox, workflow role, or surrounding orchestrator may
supply a control. The required controls and their implementations depend on
the handoff's failure modes; the five categories are not five mandatory prompt
fields.

## Outcome wording does not supply the regime

An outcome can name a destination while leaving authority, binding upstream
facts, resource access, output ownership, verification, integration, and
return of control unsettled. Conversely, a compact message can participate in
an adequate regime when those controls are supplied elsewhere. Structural
adequacy for preserving stated intent and boundaries therefore turns on the
control relation, not on prompt length or outcome-only wording. This is not an
empirical ranking of prompt styles, and more text does not by itself supply
more control.

## Nearby adaptation patterns change different things

Temporal deferral changes when a choice is made; delegation changes who holds
the judgment. Rolling-wave elaboration adds detail over time without
necessarily transferring authority. A trigger selects a mapped response,
whereas intent-framed delegation leaves a bounded, judgment-bearing choice of
means open. Broader autonomy may permit an actor to choose the goal or expand
its own decision boundary; intent-framed delegation retains a supplied purpose
and authority limit. These patterns can coexist in one workflow, but none
substitutes for the defined mechanism.

## The historical label is not an exact specification

The [historical account](../sources/david-stahel-auftragstaktik-mission-command.ingest.md)
describes variation across periods and settings and rejects identity between
the older concept and later mission command. The bare label therefore cannot
determine the exact delegation mechanism.
For Commonplace, the consequence is to use an explicit mechanism gloss when
the distinction matters, unless target-side evidence shows that the compact
cue reliably activates it. That prescription is a target-side inference, not
a claim made by the historical source, and it does not rule out compact cues
in general.

## Scope

This claim applies only when the execution choice is consequential, the
executor is competent and later-informed for that choice, and the surrounding
system can govern the control surfaces that matter. It supplies a qualitative
structural test, not an empirical performance result or a universal handoff
checklist. The record does not select a competence test, a universal
consequence threshold, or the right verification, permission, isolation,
recovery, or escalation mechanism for a particular task. Reliable activation
by a bare methodology cue also remains a target-side question.
