---
description: For consequential agent handoffs, explains why preserving intent while delegating means depends on governed authority, information, composition, feedback, and recovery rather than prompt length.
type: kb/types/note.md
traits:
  - title-as-claim
  - has-comparison
  - has-external-sources
---

# Intent-framed delegation is a control regime; prompt length does not establish it

In a consequential planner--executor handoff, intent-framed delegation preserves
upstream purpose and non-negotiable boundaries while allowing a competent
executor with a relevant execution-time information advantage to choose means
within a governed relation. The operative object is the allocation of
information and decision rights across the execution boundary. Prompt text is
only one possible carrier within that arrangement. Its brevity does not show
that the arrangement can preserve intent under the relevant failure modes; a
short handoff can still be structurally adequate when the surrounding system
supplies the control relation.

## The source methodologies formulate bounded delegation

The U.S. Marine Corps'
[MCDP 1 formulation](../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md)
assigns a mission and purpose, leaves situation-dependent means to a competent
actor near the action, limits authority, constrains method where coordination
requires it, and expects reporting. The U.S. Army's
[ADRP 6-0 formulation](../sources/us-army-adrp-6-0-mission-command-2012.ingest.md)
combines objective-oriented orders and resources with point-of-action
initiative, specified authority, coordination, supervision, accountability, and
retained upstream responsibility. Their overlap shows bounded delegation.
[Stahel's historical account](../sources/david-stahel-auftragstaktik-mission-command.ingest.md)
warns that older *Auftragstaktik* and later mission-command principles are not
identical, so the overlap should not be recast as one timeless doctrine. The
retained extracts formulate source-side control patterns; they do not provide
an LLM-agent outcome comparison.

## The shared mechanism is intent-preserving delegated adaptation

For this note, **intent-preserving delegated adaptation** is present when
upstream fixes a purpose-bearing result and non-negotiable decision boundaries,
grants a defined executor authority to choose execution-dependent means, and
keeps that choice answerable to the fixed intent and boundaries. The executor
must meet the capability requirements of the delegated decision: it can derive
feasible means from the assignment and available evidence, keep its actions
within bounds, and detect when the evidence or authority is insufficient for a
safe decision. Its information advantage is also decision-specific.
Execution-time facts must be absent or stale upstream and capable of changing
which permitted means best serve the intent; the executor need not know more
overall. These are proposed truth conditions for the narrow transfer, not an
experimentally proven minimum or a sufficient implementation packet.

## Transfer requires the same mechanism in the target

Because [borrowed patterns transfer only over a shared mechanism](./borrowed-patterns-transfer-only-over-shared-mechanism.md),
an agent system must independently instantiate the relevant information and
authority relation. Upstream must hold purpose or binding constraints that the
executor cannot safely reconstruct. The executor must have access to execution
evidence that can affect its choice of means and a real boundary over that
choice. Its result must also have a governed route into the surrounding system,
whether through integration into composed work or authorized external action.
This match makes the source pattern relevant; it does not carry over
source-domain machinery or establish target-domain effectiveness.

## The information asymmetry runs in both directions

Upstream must preserve what live state cannot recover: intent, cross-task
coupling, privileged facts, constraints, external commitments, output
ownership, and done conditions. The executor should use current state, tool
results, local failures, newly exposed constraints, and evidence produced
during execution when selecting authorized means. This applies the principle
from [fix what the executor cannot determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md).
It explains why the executor cannot be expected to recover missing upstream
intent from local evidence and why upstream should leave a method open when the
delegated choice is meant to turn on later evidence.

## A control regime governs the consequential surfaces

In this note, a handoff is consequential when the surrounding system cannot
treat a plausible execution-boundary failure as harmless. Examples include
failures that change acceptance of composed work, violate an authority or
external commitment, contaminate peer work, or prevent required recovery. The
derived requirement is failure-indexed: every control surface whose failure
could produce one of those consequences needs an operative mechanism. Without
one, the handoff has no structural route to preserve fixed intent through that
failure.

One non-exhaustive Commonplace audit heuristic names five surfaces: the worker's
authority boundary; access to relevant context and resources; ownership and
integration of its output; feedback or verification; and recovery or
escalation. It does not claim that every consequential handoff decomposes into
exactly five categories. Timing, liveness, concurrency, or another surface
belongs in the audit whenever its failure is consequential. One mechanism may
govern several surfaces by providing an input or decision right, constraining
action, routing output, exposing deviation, or returning control.

The heuristic is a Commonplace synthesis, not a list taken from the military
sources. The sources supply analogues for authority, resources, coordination,
reporting, and supervision; the author--executor information boundary supplies
live evidence; and
[coordination guarantees](./agent-orchestration-needs-coordination-guarantees-not-just.md)
supply ownership, verification, composition, and accountability. This mixed
provenance explains the selected categories but does not establish their
exhaustiveness. Prompts, tool policies, sandboxes, workflow roles, or
orchestrators can implement the required controls in forms selected by the
handoff's failure modes.

## Outcome wording does not supply the regime

An outcome can name a destination while leaving authority, binding upstream
facts, resource access, output ownership, verification, integration, and return
of control unsettled. A short message inside a workflow that already governs
the failure-relevant surfaces can participate in an adequate regime; a detailed
outcome description that leaves them unsettled cannot. Structural adequacy for
preserving stated intent and boundaries therefore turns on the control
relation, not on prompt length or outcome-only wording. This is not an
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
determine the exact delegation mechanism. When the distinction matters, an
explicit mechanism gloss avoids relying on the ambiguous label to choose among
different doctrines. A compact cue can still be adequate when target-side
evidence shows that it reliably activates the intended mechanism. This is a
target-side inference, not a claim made by the historical source.

## Scope

This qualitative structural test covers the later-informed delegation subtype:
the execution choice is consequential, the executor is competent and has a
means-relevant information advantage, and the surrounding system can govern the
failure-relevant surfaces. Delegation for isolation, specialized access, or
workload partition can also require controls, but this note does not derive
those cases from the same information mechanism. The record does not select a
competence test, a consequence threshold, or the task-specific control
mechanisms. Whether a bare methodology cue reliably activates the intended
mechanism remains a target-side question.
