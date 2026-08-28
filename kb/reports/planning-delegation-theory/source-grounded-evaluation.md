# Planning and delegation for agent work: source-grounded evaluation

## Executive conclusion

Military command is a high-yield source domain for agent planning and
delegation in a narrow sense: it is a justified place to search for mechanisms,
not a source of wholesale prescriptions. Modern doctrine makes a
planner--executor information problem central. Consequential work proceeds
under friction, uncertainty, changing local conditions, and limited ability to
specify means in advance. The doctrine then describes how stable intent and
control can coexist with locally chosen means.

Agent work can expose the same narrow problem for an independent reason. Under
the conditions in
[Preferential codification concentrates less predictable work at the agent boundary](../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md),
symbolic enforcement removes more operationally predictable cases from agent
judgment. The residual cases are then selected toward choices whose relevant
state can arrive during execution or whose branches are cheaper to resolve
then. This is a candidate mechanism match. It is not a claim that war and agent
work are generally alike.

The comparison separates five decisions that an adaptive plan can make:

1. **Authority:** who chooses means when the planner and executor hold
   different decision-relevant information?
2. **Detail:** when should later work become more specific?
3. **Commitment:** when should a costly-to-reverse choice remain open?
4. **Alternatives:** when should several candidates remain feasible, and what
   evidence will narrow them?
5. **Adaptation:** what observation should select a prepared response, and how
   early must it do so?

Mission tactics, rolling-wave planning, real-options reasoning, Dynamic
Adaptive Policy Pathways (DAPP), and set-based practice contribute different
mechanisms to those decisions. A Commonplace method can compose their bounded
contributions around a target problem. No source states the composite as a
unit, and the comparison does not establish that it improves agent outcomes.

## Why military command is a productive source domain

### Source-domain reason

[MCDP 1](../../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md)
and
[ADRP 6-0](../../sources/us-army-adrp-6-0-mission-command-2012.ingest.md)
are modern normative systems organized around friction, uncertainty,
unanticipated change, distributed information, and decisions made near the
point of action. They make the allocation of information and decision rights
across a planner--executor boundary a first-order design problem. They also
make intent, authority, resources, coordination, reporting, supervision, and
responsibility explicit parts of the answer.

That concentration makes the domain productive to inspect. It does not show
that the doctrines cause better results, that decentralization is generally
superior, or that the military and agent domains are broadly similar.
[Stahel's historical reassessment](../../sources/david-stahel-auftragstaktik-mission-command.ingest.md)
adds a further limit: *Auftragstaktik* varied by period, command level,
circumstances, communications, training, doctrine, institutional culture, and
personalities. The name does not identify one timeless portable package or an
uncomplicated lineage into modern mission command.

### Independent target-side premise

The military sources do not establish why agent work has this shape. That
premise comes from the Commonplace account of preferential codification. Its
selection claim has strict conditions: hold the incoming workload and routing
policy fixed, codify a nonzero share of recurring decision cases, and require
every removed case to be more operationally predictable than every case left
to agent judgment. Only then does the residual distribution concentrate toward
the less predictable end.

Operational predictability is relative to the system being compared. The
state-to-action mapping and an acceptable result must be specifiable and
verifiable more cheaply and reliably there. Codification also has a precise
boundary: code, a schema, validator, grammar, or another symbolic consumer must
apply the mapping without asking the agent to choose it again. Natural-language
methodology can constrain a choice without codifying it.

This selection effect concerns the composition of residual cases. It does not
show that an individual case becomes intrinsically harder or that aggregate
effort, duration, token use, or cost increases. Nor does it show that deployed
agent systems usually satisfy the selection conditions.

The planning consequence needs another condition. Execution-time choice is
favored when decision-relevant state appears only during execution, or when
execution can cheaply resolve the branch that matters while advance planning
would elaborate many unused branches. Detailed advance planning remains
appropriate when state is stable and available, branch resolution is
economical, coordination requires a shared sequence, or the choice is
predictable enough to settle. Weak verification or expensive symbolic
implementation can leave a choice with an agent without creating an
execution-time information advantage.

### Search heuristic, transfer warrant, and inference

The governing transfer rule is that
[borrowed patterns transfer only over a shared mechanism](../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md).
Analogy, shared terminology, conceptual resemblance, maturity, longevity,
severity, and institutional prestige can motivate a search. None warrants an
import. The target must independently instantiate the particular mechanism and
its premises, and warrant stops where that mechanism stops.

Here the proposed match is **intent-preserving delegated adaptation**. Upstream
fixes a purpose-bearing result and non-negotiable decision boundaries. A
competent executor receives real authority to choose execution-dependent means
using decision-relevant live evidence. The choice remains answerable to the
fixed intent and bounds. The executor's advantage is specific to the decision;
the executor need not know more overall.

This search discipline has precedents in Commonplace. One survey searches
[soft-bound traditions organized around a matching problem](../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md)
and then tests optimization target, feedback, and failure-mode conditions.
Another evaluates
[human writing structures by the failure modes they share with LLM work](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md).
Those precedents support per-mechanism testing. They add no military warrant.

Military command is therefore a promising source domain because it retains an
explicit concentration of mechanisms for consequential later-informed,
intent-bounded choice of means. Preferential codification supplies an
independent reason that an agent boundary can increasingly retain the same
narrow information problem under its selection conditions. The conjunction
justifies a search priority, not a general analogy or a transfer.

`High-yield` has only that qualitative meaning here. The authorized record does
not compare source domains, measure search yield, show how often agent work has
this composition, or test a military-derived method in agents. Domain maturity
may make a tradition worth inspecting; only a target-side mechanism match can
license a bounded import.

## Comparative evaluation

The retained Commonplace synthesis of
[productive deferral](../../notes/productive-deferral-requires-option-evidence-and-convergence.md)
keeps the neighboring methods distinct. This table is a map; the substantive
evaluations follow it. The source links preserve navigation, but the target-side
composition is a Commonplace construction rather than a method claimed by any
one source.

| Target decision | Source method | Bounded contribution |
|---|---|---|
| Who chooses execution-dependent means? | Mission tactics | Purpose-bearing assignment and bounded local judgment over means. |
| When is later work elaborated? | Rolling-wave planning | Coarse later horizons with an explicit replanning return. |
| When should a future choice remain live? | Real-options reasoning | Option preservation under costly reversal, expiry, and waiting cost. |
| How does observed change select a response? | DAPP | Monitored signposts, mapped triggers, responses, and lead-time awareness. |
| How are several candidates kept and narrowed? | Set-based practice | Feasible alternatives, discriminating tests, narrowing, and a convergence point. |

### 1. Mission tactics: allocate bounded authority over means

#### Source methodology

[MCDP 1](../../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md)
treats war as disorderly, uncertain, dynamic, and affected by friction. A
subordinate at the point of decision can have a fresher view of the current
situation than a remote senior. Mission tactics therefore assign a mission
without prescribing every means. The senior supplies the task and its purpose,
prescribes method where coordination requires it, and normally intervenes by
exception. The subordinate chooses means from the live situation, reports,
acts in conformity with intent, and remains inside the assigned authority.

The source distinguishes a task's `what` from intent's `why`. A changed
situation can make the former unfit while the latter continues to guide action.
It also treats competence, trust, familiarity, shared doctrine, training,
support, coordination, reporting, and tolerance for good-faith error as
enabling conditions. This is bounded local judgment inside a control system,
not a rule to maximize autonomy.

[ADRP 6-0](../../sources/us-army-adrp-6-0-mission-command-2012.ingest.md)
gives a compatible but more explicit control account. It places some fast
decisions at the point of action and joins freedom over means in specified
areas to purpose, key tasks, desired end state, resources, broad guidance,
coordination, communication, feedback, risk management, supervision, and
accountability. Disciplined initiative applies when unanticipated circumstances
make prior orders unfit. Delegated authority does not move ultimate
responsibility away from the commander in the source system.

These publications are normative institutional statements. Their overlap is
good evidence that two modern doctrines formulate bounded delegation around
uncertainty and distributed information. It is not evidence of causal
effectiveness or agent applicability.

[Stahel](../../sources/david-stahel-auftragstaktik-mission-command.ingest.md)
prevents the two modern formulations from becoming a timeless historical
package. Historical variation limits claims about identity, lineage, and a
generally valid degree of delegation. It does not invalidate the modern
doctrines as descriptions of what those institutions prescribed.

#### Shared mechanism

The shared mechanism is **intent-preserving delegated adaptation**. Upstream
retains the purpose-bearing result, non-negotiable bounds, cross-task coupling,
privileged facts, external commitments, ownership, and done conditions that an
executor cannot safely reconstruct. A competent executor receives actual
authority over means when live evidence can change which permitted means best
serve the intent. The result has a defined route into composed work or
authorized action.

The information relation is bidirectional. The executor may hold current state,
tool results, local failures, or evidence produced by earlier steps. The
planner may hold purpose and global constraints. Delegation follows the
decision-specific information difference; it does not assume that one side
knows more overall.

#### Commonplace consequence and non-transfer boundary

An agent handoff instantiates the mechanism only when intent, authority,
resources and accessible context, ownership and integration, feedback or
verification, and recovery or escalation are operative for the consequential
surfaces involved. Timing, liveness, and concurrency also matter when their
failure is consequential. This is why
[intent-framed delegation is a control regime, not a short prompt](../../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md).

Mission tactics contributes the one mechanism in this comparison that
allocates bounded execution-time judgment over means. It does not decide
whether waiting is worthwhile, when later detail returns, how several
alternatives narrow, or how an observed condition maps to a prepared response.

The transfer excludes military hierarchy, rank, force structure, professional
military culture, lethal-risk doctrine, adversarial purpose, and organizational
machinery. Source functions such as competence, resources, communication,
feedback, and accountability matter only where the target mechanism
independently requires them; their military embodiments do not transfer. The
comparison supports neither a general preference for decentralization nor an
empirical agent-effectiveness claim.

### 2. Rolling-wave planning: allocate detail by information horizon

#### Source methodology

The retained source records are the
[PMI Lexicon](../../sources/pmi-lexicon-project-management-terms-v4.ingest.md)
and a
[practitioner account by Githens](../../sources/githens-manage-innovation-programs-rolling-wave.ingest.md).
At the level supported by the retained reconstruction, rolling-wave planning
makes near-term work detailed while later work remains at a higher level and is
elaborated as information improves. A stronger form adds a fixed replanning
date, an assessment of what has been learned, and planning of the next horizon.
Later work stays visible; its detail is deliberately deferred.

#### Shared mechanism

The shared mechanism is **progressive commitment of detail as its premises
become available**. The return path is part of the mechanism. A coarse horizon
without an owned replanning event is indistinguishable from missing thought
once the work has moved past it.

This allocation is temporal. The same planner may add the later detail. No
transfer of authority is required.

#### Commonplace consequence and non-transfer boundary

An agent plan can leave later work coarse when the necessary state is not yet
available or when resolving every branch in advance would be uneconomical. It
should name the replanning date or other explicit return at which learning is
assessed and the next horizon is elaborated.

Rolling-wave planning says when detail is added. It does not itself preserve a
materially exercisable option, show that delay is worthwhile, delegate
judgment, or determine which response follows an observation. The authorized
evidence supplies no universal replanning cadence and no effectiveness claim.

### 3. Real options: preserve a costly-to-reverse choice conditionally

#### Source methodology

The retained
[Pindyck source record](../../sources/pindyck-irreversibility-uncertainty-investment.ingest.md)
supports the bounded real-options formulation used here. When present
commitment is irreversible or costly to reverse, delaying commitment can
preserve a materially live future choice and an opportunity to observe. The
option can expire, and waiting can forgo present benefit or incur other costs.
The mechanism does not require several alternatives.

#### Shared mechanism

The shared mechanism is **conditional preservation of a costly-to-reverse
choice**. The future choice must remain feasible, and a possible later
observation must be capable of changing the decision. Mere uncertainty does
not supply that relation. Mere postponement does not preserve an option if the
choice will no longer be exercisable.

#### Commonplace consequence and non-transfer boundary

Real-options reasoning contributes the `option` part of productive deferral and
forces delay costs into view. It does not by itself supply the evidence process
or convergence rule. A bounded test can be useful when its possible results
would discriminate among later choices, but the authorized record does not show
that testing dominates passive waiting or present commitment.

Option, discriminating evidence, and convergence are necessary for productive
deferral; together they still do not prove that waiting is worthwhile.
Foregone benefit, delay, carrying cost, pre-emption, lead time, or expiry can
favor present commitment or abandonment. The source supplies no universal
threshold and no agent-effectiveness result.

### 4. DAPP: map observed change to a prepared response

#### Source methodology

The retained
[DAPP source record](../../sources/haasnoot-dynamic-adaptive-policy-pathways-2013.ingest.md)
supports a bounded formulation built from monitored signposts, triggers,
mapped responses, and lead-time-aware action. A signal alone is not enough. A
trigger must connect an observed condition to a response early enough for that
response to be carried out.

#### Shared mechanism

The shared mechanism is **state-conditioned later commitment among prepared
responses**. A stable objective coexists with monitored variables, target-
defined trigger conditions, mapped responses, and the lead time needed to act.

This is mapped control rather than open judgment. When the trigger condition is
met, the mapping selects a prepared response; the executor is not choosing
freely among unspecified means.

#### Commonplace consequence and non-transfer boundary

For agent planning, `decide later` becomes governable only when the plan names
the observation, the condition that matters, the mapped response, and the lead
time. This differs from a scheduled rolling-wave return and from mission
tactics' allocation of unanticipated choice.

A mapped trigger can remove executor judgment, but the existence of a recurring
condition does not automatically justify codifying it. Symbolic control requires
an independently predictable and verifiable mapping. The report does not
transfer climate-policy machinery, establish that a prepared response is
correct, or show empirical agent benefit.

### 5. Set-based practice: preserve alternatives while evidence discriminates

#### Source methodology

The retained
[Kennedy--Sobek--Kennedy source record](../../sources/kennedy-sobek-kennedy-set-based-rework.ingest.md)
supports the bounded set-based formulation used here. Several alternatives
remain feasible while focused tests address a named knowledge gap. Test results
eliminate or narrow alternatives before a latest convergence point. Activity
counts as evidence-producing only when a possible result can change the later
decision.

#### Shared mechanism

The shared mechanism is **preservation of an evaluable feasible set while
evidence discriminates**. It requires live alternatives, tests connected to the
decision, a way to compare results, and a boundary by which the choice
converges.

This differs from rolling-wave planning because it defers selection, not only
detail. It differs from DAPP because evidence narrows candidates rather than an
observed trigger selecting a mapped response. It can use active evidence
generation without assigning the final judgment to an executor.

#### Commonplace consequence and non-transfer boundary

An agent plan should not label parallel activity `set-based` unless possible
test results can alter the choice and the alternatives remain feasible until
the convergence boundary. The plan must also account for the cost of carrying
several candidates.

Set-based practice does not establish that multiple alternatives are worth
retaining in a particular case, provide a universal latest point, or decide who
owns the final choice. Source-specific organizational and engineering machinery
does not become an agent requirement merely because it accompanies the source
method. No causal effectiveness claim transfers.

## Constructing a target method from bounded mechanisms

The five evaluations show how a target method can be constructed mechanism by
mechanism rather than adopted as a named source package. One possible
Commonplace construction is:

1. Fix stable intent, constraints, interfaces, acceptance evidence, authority,
   and convergence rules upstream.
2. Leave later work coarse only when its premises are unavailable or resolving
   all branches now would be uneconomical, and give it an explicit replanning
   return.
3. Preserve a costly-to-reverse choice only while the later option remains
   feasible, and identify evidence whose possible results can change it.
4. Use monitored signposts and mapped responses where a target-defined state
   can select a prepared action; use bounded tests where evidence must narrow
   several feasible alternatives.
5. Give an authorized executor judgment over means only where live evidence
   genuinely changes which permitted means best serve fixed intent.
6. Return each deferred choice through a replanning date, mapped trigger,
   evidence-gated test, latest safe decision point, or authorized procedure
   before the option expires.

Productive deferral connects several of these contributions without erasing
their differences. It requires a materially preserved option, evidence whose
possible outcomes can change the named decision, and a convergence rule that
joins a return condition to a response while the option remains feasible. The
response can select, modify, abandon, authorize more bounded work, or transfer
the reopened choice to an authorized procedure.

Each component keeps its own premises, costs, and limit. Composition also needs
interaction checks. A mapped trigger can remove the executor's judgment. A
convergence deadline can constrain local adaptation. An authority allocation
can determine who may exercise an option. Component warrant does not
automatically become warrant for their combination.

This construction is a Commonplace inference. It is not a doctrine attributed
to a military, project-management, finance, policy, or design source. The
authorized evidence supports it as a design proposal, not as an empirically
settled agent effect.

## Present Commonplace disposition

The durable notes in the authorized evidence set have distinct current roles.
This report uses those roles; it does not claim that the notes were changed by
this workshop.

| Durable note | Current role in this report | Supported gap or boundary |
|---|---|---|
| [Preferential codification concentrates less predictable work at the agent boundary](../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) | Supplies the conditional target-side selection effect and the boundary between natural-language constraint and symbolic codification. | Does not establish prevalence, aggregate difficulty, or agent effectiveness. |
| [Borrowed patterns transfer only over a shared mechanism](../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) | Supplies the transfer gate and separates search priority from import warrant. | Does not itself prove that a source and target share a mechanism. |
| [Intent-framed delegation is a control regime, not a short prompt](../../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) | Owns the bounded military-to-agent reconstruction, target-side truth conditions, and non-exhaustive control surfaces used here. | The conditions are not an experimentally proven minimum or a sufficient implementation packet. |
| [Productive deferral requires option, evidence, and convergence](../../notes/productive-deferral-requires-option-evidence-and-convergence.md) | Owns the cross-source necessary conditions and the bounded distinctions among rolling-wave planning, real options, DAPP, set-based practice, and mission tactics. | The three conditions do not prove that waiting is worthwhile or effective for agents. |
| [Soft-bound traditions as sources for context-engineering strategies](../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) | Supplies an advisory precedent for searching a tradition by a matching problem and then testing optimization target, feedback, and failure mode. | Adds no direct military evidence or warrant for this composite. |
| [Human writing structures transfer to LLMs because failure modes overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) | Supplies an advisory precedent for evaluating a borrowed convention by the failure it prevents and whether that failure exists in the target. | Adds no warrant for a different pattern without a fresh match. |

[Problem matches guide method search; mechanism matches bound transfer](../../notes/problem-matches-guide-method-search-mechanism-matches-bound-transfer.md)
now owns the additional durable synthesis exposed by this comparison. It uses
problem match to select candidate source responses, mechanism match to bound
transferred warrant, and interaction checks to bound a target method composed
from several responses. That note earned its scope through a separate brief,
source-first reconstruction, authorship pass, and independent review; it does
not inherit this report as a durable premise.

## Source revisit and future-evidence queue

- **Modern Marine Corps formulation:** the retained MCDP record supports an
  official 1997 formulation. Revisit it or a current successor if present
  doctrinal currency becomes material.
- **Army formulation:** the retained ADRP capture is partial and records a 2012
  publication with changes through 2014. Revisit a complete edition or current
  successor if exact edition wording, omitted material, lineage, or present
  currency becomes load-bearing.
- **Historical variation:** Stahel is a historiographical synthesis. A causal
  claim about which condition produced a historical result needs stronger
  historical evidence.
- **Neighboring methods:** this revision uses the bounded reconstruction in the
  productive-deferral note while retaining direct source links for navigation.
  Revisit the exact source records before making source-specific wording,
  edition, lineage, or effect claims beyond that reconstruction.
- **Agent outcomes:** no authorized evidence shows that any single mechanism or
  the composite improves agent effectiveness. That question requires
  target-side tests.

## Machinery revision handoff

A later method-design pass can use the comparison as a checklist without
copying the report wholesale into an instruction:

1. **Separate stable material from deferred choice.** Mission tactics exposes
   the bidirectional information boundary: upstream can hold purpose and global
   constraints while execution holds later means-relevant state.
2. **For each consequential deferral, state why later evidence can alter the
   choice and how the option remains feasible.** Real-options reasoning makes
   irreversibility, expiry, foregone benefit, and waiting cost visible; it does
   not make delay a virtue.
3. **Give deliberately coarse future work an owned return.** Rolling-wave
   planning supplies a replanning horizon at which learning is assessed and the
   next detail is added. A coarse item without a return is an unowned
   placeholder.
4. **For mapped adaptation, name the observation, response, and lead time.**
   DAPP explains why a signal alone is insufficient and why a trigger is
   different from open executor judgment.
5. **Maintain several alternatives only behind a real evaluation surface.**
   Set-based practice requires tests whose possible results can change the
   choice, a convergence boundary, and explicit attention to carrying cost.
6. **For delegated judgment, supply the control regime.** State purpose,
   constraints, authority, accessible context and resources, ownership and
   integration, feedback or verification, and recovery or escalation for the
   consequential failure surfaces.
7. **Check component interactions.** A trigger can remove judgment, a deadline
   can constrain adaptation, and authority can determine who may exercise an
   option. Do not infer composition warrant from component warrant alone.

This handoff advises later method design. It does not decide implementation or
change any planning machinery in this report revision.

## Evidence and artifact status

The evidence roles in this report are explicit. The MCDP, ADRP, and Stahel
ingests supply the military source formulations and historical boundary. The
six Commonplace notes in the present-state disposition supply the target-side
selection premise, transfer gate, bounded delegation and deferral syntheses,
and advisory precedents. The five neighboring-method source links preserve
source navigation; the bounded claims used here come through the authorized
productive-deferral reconstruction.

This is a frontmatter-free workshop report. This revision changes no cited
note, source ingest, tag, instruction, index, or sibling artifact. Independent
verification for this revision ran `commonplace-validate` on all eight linked
ingests. All eight pass; seven are clean; the PMI lexicon has the known
`frontmatter.genre: reference-lexicon` warning. Across the eight ingests, all 30
retained source quotes resolve against their pinned snapshots. These checks
establish current deterministic validation and quote-to-pinned-snapshot
resolution. They do not establish present doctrinal currency or broader
snapshot assurance.

The substantive evidence limits are also unchanged. The MCDP record supports a
1997 institutional formulation, not present currency or effectiveness. The
ADRP record is partial and does not provide a complete lineage audit or present
currency. Stahel cannot isolate which historical condition caused a result.
The authorized evidence does not establish empirical effectiveness for the
military doctrines or the proposed agent composite, compare them with detailed
command, validate a competence test, set a consequence threshold, or supply
domain-independent numeric rules for delegation or deferral.
