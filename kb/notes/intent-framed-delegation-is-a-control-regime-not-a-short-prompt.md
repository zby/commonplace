---
description: For consequential agent handoffs, explains why preserving intent while delegating means depends on governed authority, information, composition, feedback, and recovery rather than prompt length.
type: kb/types/note.md
traits:
  - title-as-claim
  - has-comparison
  - has-external-sources
---

# Intent-framed delegation is a control regime; prompt length does not establish it

In a consequential planner--executor handoff, intent-framed delegation is a
governed allocation of information and decision rights. Upstream fixes purpose
and binding boundaries. A competent, authorized executor may choose means when
execution can expose evidence that could change which permitted means serve that
purpose. Prompt text is only one carrier in this arrangement. Its length does
not establish the control regime, although a short handoff can participate in
one when the surrounding system supplies the missing controls.

## Reciprocal opposition explains the military source problem

The military problem is deeper than ordinary distributed information. The
U.S. Marine Corps'
[MCDP 1 formulation](../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md)
describes an opponent as an independent actor with its own objectives and plans
that resists and acts in return. It also directly describes war as uncertain,
dynamic, disorderly, and dominated by friction. Chance and information
unavailable in advance can also defeat advance specification without an
adversary; that boundary is synthesis here, not a direct MCDP attribution.
These conditions overlap but are not the
same. Generic friction can disrupt a non-adversarial process. Reciprocal
opposition makes the uncertainty interactive because another purpose-bearing
actor helps produce the future state.

The next step is a cross-source synthesis, not wording supplied by one source.
When an opponent can observe and respond, one side's action can change the
opponent's next choice, which changes the state for later action. Some
action-to-outcome relations therefore depend on another chooser. Friction and
information limits add further divergence. The record does not show that
opposition was the sole cause of *Auftragstaktik* or establish its weight
relative to communications, scale, technology, training, or culture.

These conditions make the source response intelligible. Complete advance
control is unavailable. Some facts that discriminate among possible means
become visible only near the point of action. Purpose can remain useful after a
task or method becomes obsolete. MCDP 1 therefore assigns a mission and purpose
without prescribing every means, while retaining guidance, authority limits,
coordination, responsibility, and reporting. The U.S. Army's
[ADRP 6-0 formulation](../sources/us-army-adrp-6-0-mission-command-2012.ingest.md)
likewise joins intent and desired results with point-of-action initiative,
resources, specified authority, coordination, supervision, accountability, and
retained upstream responsibility. The generalized chain from interactive
uncertainty to later-informed, bounded choice is cross-source synthesis; the
individual doctrinal elements are direct source claims.

[Stahel's historical account](../sources/david-stahel-auftragstaktik-mission-command.ingest.md)
describes Prussian-German thought as treating war as contingent and leadership
as direction rather than complete control. It also rejects one generally valid,
uniform historical *Auftragstaktik* and treats it as distinct from modern
mission command. MCDP 1 and ADRP 6-0 can state coherent modern prescriptions on
their own terms, but they do not establish identity with historical German
practice, continuity, or effectiveness.

## Transfer requires the later-informed choice mechanism

A **causal-origin match** means the target shares the condition that generated
the source problem. A **downstream mechanism match** means the target lacks that
origin but independently has the later-informed choice problem to which bounded
discretion responds. Because
[borrowed patterns transfer only over a shared mechanism](./borrowed-patterns-transfer-only-over-shared-mechanism.md),
source warrant reaches only the match the target actually has. Neither kind of
match establishes target effectiveness.

Genuinely adversarial agent work may share the causal origin when another
capable actor has independent goals, observes or responds to the agent's
actions, and deliberately changes the state or available options. That is a
Commonplace inference from the military premises, not an agent result.
Non-adversarial work does not need hostile purpose. It shares the downstream
mechanism only when it has an independent route to later-arriving,
means-relevant information:

- a bounded choice among permitted means can affect execution;
- upstream exposes purpose, binding constraints, acceptance conditions,
  privileged facts, external commitments, and relevant coupling that execution
  cannot safely recover;
- a named observation or produced result can arrive during execution, and at
  least one possible result would change selection, timing, modification, or
  abandonment of a permitted means;
- the executor can access that evidence and is competent and authorized for the
  choice; and
- the choice remains within authority and coordination bounds, with common
  selection or coordination-bearing ownership where local choices could
  conflict.

Here, *later-arriving* means unavailable or unsettled at the relevant upstream
specification point, not merely read later. *Means-relevant* means capable of
changing the bounded choice. The more general allocation rule is to
[fix what the executor cannot determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md).
These are conditions for this transfer argument, not an experimentally proven
minimum or a sufficient implementation packet.

## Information and decision rights run in both directions

Upstream must preserve what live execution cannot recover: intent, cross-task
coupling, privileged facts, constraints, external commitments, output
ownership, and done conditions. The executor uses current state, tool results,
local failures, newly exposed constraints, and evidence produced during
execution when selecting authorized means. The executor need not know more
overall; its information advantage is specific to the delegated decision.

The open choice remains answerable to the fixed purpose and boundaries. The
executor must be able to derive feasible means, remain within authority, and
detect when evidence or authority is insufficient. Delegation changes who
holds that judgment. Deferral changes when it is made. Delegating immediately
to an actor that already has the evidence is delegation without a later
information advantage.

## A control regime governs consequential surfaces

A handoff is consequential here when the surrounding system cannot treat a
plausible execution-boundary failure as harmless. Examples include a failure
that changes acceptance of composed work, violates authority or an external
commitment, contaminates peer work, or prevents required recovery. Every
surface whose failure could produce such a consequence needs an operative
control path.

One non-exhaustive Commonplace audit heuristic checks scoped authority; usable
context and resources; output ownership and integration; feedback and
verification; accountability and an attributable authority path; and recovery
or escalation. Coupled work also needs consistency, common selection, or an
actor empowered to resolve incompatible local projections, because
[agent orchestration needs coordination guarantees](./agent-orchestration-needs-coordination-guarantees-not-just.md).
One mechanism may govern several surfaces, and a task may expose additional
ones such as timing, liveness, or concurrency.

This audit is a Commonplace inference, not a list taken from military doctrine.
The modern sources provide analogues for authority, resources, coordination,
reporting, supervision, accountability, and retained responsibility. They do
not derive a recovery protocol for agent work. Recovery remains a target-side
requirement whose form must be selected from the task's consequences.
Prompts, tool policies, sandboxes, workflow roles, and orchestrators can carry
controls, but none is sufficient merely by being present.

## Outcome wording does not supply the regime

An outcome can name a destination while leaving authority, binding upstream
facts, resource access, output ownership, verification, integration, and return
of control unsettled. A short message inside a workflow that governs those
surfaces can participate in an adequate regime. A detailed outcome description
that leaves them unsettled cannot establish one. Structural adequacy therefore
turns on the control relation, not prompt length or outcome-only wording. This
is not an empirical ranking of prompt styles. More text does not itself supply
more control, and this record does not show that a compact methodology cue
reliably activates the intended regime.

## Scope

This qualitative structural test covers later-informed delegation: the choice
is consequential, execution can expose evidence that discriminates among
permitted means, the executor is competent and authorized, and the surrounding
system governs the failure-relevant surfaces. If all choice-relevant inputs are
available and stable upstream, the later-informed rationale does not apply and
the choice may be fixed there. Waiting alone creates no information advantage.
Leaving a harmless, decoupled choice open also does not show that this mechanism
transferred. Other reasons for delegation, including isolation, specialized
access, or workload partition, are not derived here.

Hostile purpose, violence, tempo competition, military hierarchy, rank, force
structure, professional culture, and military risk doctrine are not
requirements for non-adversarial transfer. The target must independently
supply the functions it needs: competence, shared meaning, usable information
and resources, scoped authority, coordination, feedback, integration,
verification, accountability, and recovery. This functional restatement does
not claim that a prompt recreates a military institution.

The record does not select a competence test, consequence threshold, or
task-specific control implementation. It supplies no effect size, comparative
outcome, universal decentralization rule, LLM evaluation, or evidence that a
bare historical or methodology label activates the mechanism. An explicit
mechanism gloss avoids relying on *Auftragstaktik* or mission command as an
exact specification.

Operationalized into:

- [Write an instruction](../instructions/write-instruction.md) — selects delegation controls from consequential failure surfaces instead of requiring a universal packet template
- [cp-skill-write-multistage](../instructions/cp-skill-write-multistage/SKILL.md) — fixes the commission, evidence and authority boundaries, integration, review, and recovery while leaving bounded investigative and authorial means to workers
