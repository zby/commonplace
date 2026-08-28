# Planning and delegation for agent work: source-grounded evaluation

## Executive conclusion

The source comparison does not identify one complete methodology that should
replace all others. It identifies independent decisions that an adaptive plan
must make:

1. **Authority:** who should choose the means when relevant information is
   distributed between planner and executor?
2. **Detail:** how much of later work should be specified before its premises
   are available?
3. **Commitment:** when is preserving a decision worth more than acting now?
4. **Alternatives:** when should several candidates remain live, and how should
   they be eliminated?
5. **Adaptation:** what observations should cause a plan to change, and early
   enough for what response?

Auftragstaktik and modern mission tactics remain the strongest compact
methodology for the first decision: preserve intent and constraints while
delegating execution-time choice of means. Rolling-wave planning, real-options
theory, Dynamic Adaptive Policy Pathways (DAPP), and set-based design do not
displace that mechanism. They govern the other four decisions.

Real-options theory is a load-bearing part of the synthesis, not a secondary
analogy. It supplies the missing normative test for deferral. A plan should
preserve a choice only when later observation can change the decision,
commitment would destroy a valuable alternative, the opportunity remains
available, and the value preserved exceeds the cost of waiting. Pindyck also
shows why the choice is not always between passive waiting and full commitment:
a bounded early action can be valuable because it produces information.

The resulting Commonplace theory is therefore stronger than “delegate under
uncertainty”:

> Fix upstream the intent, constraints, privileged facts, and coordination
> boundaries that execution cannot safely reconstruct. Place each remaining
> decision at the stage and actor that will have its decision-relevant
> information. Preserve alternatives only while later observation or active
> testing can discriminate among them and commitment remains costly to reverse.
> Make planned adaptation governable through observation, thresholds, lead
> time, and an explicit convergence or escalation rule.

This paragraph is a Commonplace synthesis. No source states it as a unit.

## Starting theory and what the sources can establish

The investigation began from a first-principles selection argument:
predictable recurring decisions can progressively move from LLM judgment into
methodology, schemas, validators, workflows, or deterministic code. The work
left at the agent boundary is consequently selected for execution states that
are harder to anticipate. Information needed to choose means often arrives
only during execution, creating a planner-executor information asymmetry.

The external sources do not establish that selection argument. They supply
mature formulations of what to do after the asymmetry exists, conditions under
which deferral is rational, and mechanisms for preserving flexibility. They
therefore ground or refine the planning consequence of
[Preferential codification concentrates less predictable work at the agent boundary](../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md),
not its premise about how codification reshapes the residual work distribution.

That evidential boundary matters. Military doctrine is normative doctrine,
PMI's lexicon standardizes terminology, Githens reports practitioner experience,
Pindyck presents formal theory, DAPP integrates methods and illustrates them in
a model-supported case, and the set-based paper is methodological and
case-based. Together they provide independent mature-domain mechanisms and
useful limits. They do not constitute a controlled test of agent planning.

## Comparative evaluation

### 1. Auftragstaktik and mission tactics: allocate authority by information

#### Source methodology

[MCDP 1](../../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md)
derives decentralized execution from friction, uncertainty, disorder, and
distributed decision-making. A senior supplies task and purpose, intent,
support, and coordination-essential guidance; a competent subordinate chooses
means from local conditions and can continue acting when the original task no
longer fits.

[ADRP 6-0](../../sources/us-army-adrp-6-0-mission-command-2012.ingest.md)
makes the control system more explicit. Mission orders, intent, disciplined
initiative, resources, information flow, feedback, adjustable control, risk
acceptance, and retained commander responsibility operate together. Delegation
is not absence of control.

[Stahel's historical reassessment](../../sources/david-stahel-auftragstaktik-mission-command.ingest.md)
prevents treating *Auftragstaktik* as a timeless stable package. Its meaning and
application changed; initiative varied with period, level, competence,
communications, personality, and command culture. The source supports a core
logic while contesting an uncomplicated lineage into modern mission command.

#### Shared mechanism

The transferable mechanism is **intent-preserving delegated adaptation**:
communicate the purpose and non-negotiable boundaries the executor cannot
infer, then leave situation-dependent means to a competent executor with a
real information advantage at the point of action.

The information asymmetry is bidirectional. The executor does not simply “know
more.” The planner may hold the purpose, cross-task coupling, privileged facts,
risk limits, and external commitments. The executor may hold live state,
tool results, local failures, and evidence produced by earlier steps. A sound
plan transmits the first category and avoids freezing the second.

#### Commonplace consequence

Mission tactics is the best compact operative methodology for delegation when
execution states cannot be usefully enumerated. It is not a complete planning
method. It does not say when waiting is economically justified, how many
alternatives to retain, or how to encode observable adaptation conditions.

It also cannot be reduced to a short outcome prompt. Agent-side analogues must
provide appropriate authority, resources, accessible context, feedback,
verification, isolation, and upstream accountability. Military hierarchy,
lawful command, rank, force structure, professional formation, shared danger,
staff organization, synchronization doctrine, and combat risk machinery do not
transfer merely because the abstract mechanism does.

The historical ambiguity creates a second boundary: a bare
“Use *Auftragstaktik*” cue may activate incompatible historical and modern
representations. Weight-resident use needs an activation-fidelity test or a
short explicit gloss.

### 2. Rolling-wave planning: allocate detail by information horizon

#### Source methodology

The [PMI Lexicon, Version 4](../../sources/pmi-lexicon-project-management-terms-v4.ingest.md)
defines progressive elaboration as increasing plan detail as information and
estimate accuracy improve. It defines rolling-wave planning as detailing
near-term work while leaving future work at a higher level.

[Githens](../../sources/githens-manage-innovation-programs-rolling-wave.ingest.md)
adds a practitioner implementation: establish a top-down structure, elaborate
the near horizon, execute, learn, and replan at explicit points. Future work is
not omitted; it remains visible at an intentionally coarser resolution.

#### Shared mechanism

The transferable mechanism is **progressive commitment of detail as its
premises become available**. It is temporal rather than organizational. The
same planner may elaborate the work later; no delegation is required.

#### Commonplace consequence

Plans should distinguish an intentionally coarse future from missing thought.
Deferral should normally include a relearning or replanning commitment rather
than an unowned placeholder. The mechanism supports
[An author should fix what the executor can't determine, not what it will](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md)
and the execution-discovery phase in
[Specification strategy should follow where understanding lives](../../notes/specification-strategy-should-follow-where-understanding-lives.md).

PMI does not establish effectiveness or prescribe a universal cadence.
Work-breakdown structures, Gantt charts, baselines, phase gates, change-control
regimes, and approval chains are additional governance machinery, not part of
the minimal transfer.

### 3. Real options: decide when preserving choice has value

#### Source methodology

[Pindyck](../../sources/pindyck-irreversibility-uncertainty-investment.ingest.md)
argues that conventional investment rules omit the option surrendered by an
irreversible commitment. When an opportunity can remain open and later-observed
conditions can change whether or when investment is desirable, committing now
has an opportunity cost in addition to its direct cost.

Waiting is not automatically optimal. Current benefits forgone, expiry,
competitive pre-emption, and other delay costs can favor immediate action.
Nor must uncertainty disappear for waiting to have value. The relevant fact is
that action can later be conditioned on an observed state. Sequential early
investment can also be rational when the early stage produces information.

#### Shared mechanism

The transferable mechanism is **conditional preservation of a costly-to-reverse
choice**. Four questions decide whether it applies:

1. Would commitment materially destroy an alternative or create costly
   dependencies?
2. Will later observation or a bounded experiment be capable of changing the
   preferred choice?
3. Will the opportunity to choose still exist then?
4. What present benefit, coordination value, or expiring opportunity is lost
   by waiting?

This is more precise than “uncertainty favors flexibility.” Uncertainty without
a later discriminating observation does not create the relevant option value.
Reversibility without meaningful switching cost weakens the case for delay.

#### Commonplace consequence

Real options supplies the decision rule missing from both mission tactics and
rolling-wave planning. It grounds a refinement to
[Current-task fit alone does not warrant costly structural entrenchment](../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md):
replaceability has value when future evidence can alter the decision, but that
value must be compared with foregone coordination and current-use benefits.

It also separates three agent-planning moves that should not be conflated:

- **commit now** when evidence already discriminates or delay is costly;
- **wait** when a later observation will discriminate and passive delay is
  cheap; and
- **stage a probe** when a bounded action can cheaply produce the missing
  information without committing the whole course.

Financial-option valuation, complete-market assumptions, hedging portfolios,
Brownian-motion models, discount-rate machinery, and monetary calibration are
not needed for this qualitative transfer. The formal source identifies
variables and relationships; Commonplace still needs target-side evidence for
operational thresholds.

### 4. DAPP: make deferred adaptation observable and timely

#### Source methodology

[Haasnoot et al.](../../sources/haasnoot-dynamic-adaptive-policy-pathways-2013.ingest.md)
combine Adaptive Policymaking's monitoring and contingency actions with
Adaptation Pathways' sequences, alternatives, lock-ins, and path dependencies.
An adaptation tipping point is the condition under which an action no longer
meets its objectives. A signpost is monitored information. A trigger is a
critical signpost condition that activates a contingency early enough to
account for implementation lead time. A trigger and a tipping point are related
but are not synonyms.

#### Shared mechanism

The transferable mechanism is **state-conditioned later commitment among
prepared alternatives**. A stable objective coexists with near-term action,
monitored variables, thresholds, response lead time, and successor actions.

#### Commonplace consequence

“Decide later” becomes an adaptive plan only when the system knows what it will
observe, what condition matters, which alternatives remain viable, and how
early it must act. This differs from rolling-wave planning's scheduled increase
of detail and from mission tactics' delegation of unanticipated choice.

DAPP is especially relevant to the starting selection argument. Recurring
adaptation conditions that can be named as signposts and triggers should move
out of open-ended LLM judgment into workflow, validation, or deterministic
control. States outside the prepared pathway set remain at the agent boundary
or trigger reassessment of the plan itself.

Climate scenario ensembles, water-system models, metro-style pathway diagrams,
scorecards, stakeholder procedures, and the complete ten-step policy method do
not transfer by default.

### 5. Set-based design: preserve and actively discriminate alternatives

#### Source methodology

[Kennedy, Sobek, and Kennedy](../../sources/kennedy-sobek-kennedy-set-based-rework.ingest.md)
formulate set-based work as a front-end system rather than the slogan “keep
options open.” Requirements and candidates are represented as bounded ranges
or sets; knowledge gaps are tested; qualitatively different alternatives remain
in parallel; weak options are eliminated with evidence; coupled specialties
communicate feasible sets and minimum constraints; and the work converges by a
latest safe commitment date.

This later peer-reviewed methodological paper was used because the preferred
1999 Sobek, Ward, and Liker article could be verified but not captured as usable
text without OCR. The substitution is sufficient for the planning mechanism,
but not for direct attribution of the original article's canonical
three-principle wording.

#### Shared mechanism

The transferable mechanism is **preserve an evaluable feasible set, actively
produce discriminating evidence, and converge by an explicit deadline**.

It differs from rolling wave because it defers selection rather than merely
detail. It differs from DAPP because it narrows candidates through tests and
compatibility evidence before a commitment boundary rather than switching
pathways when an external state crosses a trigger. It extends Pindyck by showing
how active information generation and multiple live candidates can be
organized.

#### Commonplace consequence

Set-based work applies when tests are cheap and informative, reversal or rework
is expensive, alternatives interact, and maintaining what is learned has reuse
value. Point selection can be better when evidence already discriminates,
alternatives are independent or cheap to reverse, parallel maintenance is
expensive, or no credible evaluation surface exists.

The result bounds
[Solve low-degree-of-freedom subproblems first](../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md).
That heuristic applies when the feasible sets and constraints are sufficiently
known. If the feasible set itself remains epistemically uncertain, an early
apparently constrained choice may be exactly the premature commitment that
testing should prevent.

Toyota's roles and supplier relationships, V-model restructuring,
customer/business-interest paperwork, CAD/CAE, prototypes, design-of-experiment
machinery, trade-off curves, phase gates, and claims that rework can be
eliminated do not transfer as necessary parts of the mechanism.

## Integrated theory claims

### Decision placement should follow information availability

The planner-executor boundary should not be described as a simple hierarchy in
which one side knows more. Planning distributes decisions across complementary
information positions. Upstream fixes stable intent, constraints, global
coupling, privileged facts, and conventions whose shared selection carries
coordination value. Execution chooses means whose premises depend on live state
or evidence produced by the run. A harmless decoupled choice may remain open;
being arbitrary does not by itself assign the choice upstream.

This claim refines the existing executor-boundary note. In particular, “the
executor is guaranteed to know more” should be narrowed: the executor is
normally later-informed along execution-dependent variables, while the planner
may retain information the executor cannot recover.

### Deferral is a decision with premises, not a general virtue

Deferral is warranted when later evidence can change a costly-to-reverse
choice, the choice will remain available, and delay costs less than the option
preserved. Otherwise the plan should decide now. When cheap action can produce
the discriminating evidence, a staged probe can dominate both waiting and full
commitment.

This claim is the largest theoretical addition exposed by the source pass. It
connects real options to rolling-wave planning, set-based design, reversible KB
structure, experimentation, and agent execution without importing financial
valuation.

### Productive deferral requires an option, evidence, and convergence

A deferred item is not automatically flexible. The plan must preserve a viable
alternative, identify how later evidence will discriminate, and state when or
how the decision will converge. Depending on the problem, that convergence can
be:

- a scheduled replanning horizon;
- an observed trigger with sufficient response lead time;
- an evidence-gated elimination process with a latest safe decision date; or
- delegated judgment bounded by intent when consequential states cannot be
  pre-enumerated.

These are different control forms. Treating all of them as “be agile” would
discard the mechanisms that justified borrowing them.

### Intent-framed delegation remains a control regime

The planner retains responsibility for the goal, authority boundary,
coordination requirements, resources, monitoring, and response to failure.
Delegation transfers the choice of means; it does not transfer away the need to
make execution observable or to provide recovery and accountability paths.

## Implications for existing Commonplace theory

### Grounding and revision disposition

- [An author should fix what the executor can't determine, not what it will](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md)
  was revised as the main integration point. It now separates bidirectional
  information allocation, active evidence production, temporal deferral, and
  actor delegation while preserving competence and coupling conditions.
- [Current-task fit alone does not warrant costly structural entrenchment](../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md)
  now carries the real-options conditions, bounded-probe alternative, and
  explicit delay-cost term without treating delay cost as an independent
  warrant for entrenchment.
- [Specification strategy should follow where understanding lives](../../notes/specification-strategy-should-follow-where-understanding-lives.md)
  remains a candidate for a later rolling-wave and set-based fold concerning
  discovered-during-execution understanding and tests that move information
  earlier.
- [Solve low-degree-of-freedom subproblems first](../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md)
  now separates actor ownership from temporal deferral. Its known-feasible-set
  boundary remains unresolved.
- [A capable agent needs methodology selection, not just relevant knowledge](../../notes/capable-agents-need-methodology-selection.md),
  [Weight-resident methodologies provide context-efficient behavioral compression](../../notes/weight-resident-methodologies-compress-behavior-in-context.md),
  and [Borrowing can operate through retained artifacts or weight activation](../../notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md)
  now require a disambiguating gloss or target-model evidence when an ambiguous
  methodology cue could change consequential choices.

### Compare but do not claim direct grounding

- [Progressive constraining commits only after patterns stabilize](../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md)
  shares a commitment-under-learning shape, but its evidence object is repeated
  interpretation stability rather than project information arrival.
- The real-options and set-based sources compare with
  [Solve low-degree-of-freedom subproblems first](../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md)
  but do not establish its computational sequencing rule.
- DAPP's fixed scenarios, objectives, indicators, and action sets reinforce the
  scope warning in
  [Learning inside a fixed decomposition inherits its mistakes](../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md);
  they do not prove that Commonplace claim.

### Promoted theory notes

The pass promoted two atomic claims rather than one catalogue of source
methodologies:

1. [Intent-framed delegation is a control regime, not a short prompt](../../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md).
2. [Productive deferral requires a preserved option, discriminating evidence,
   and a convergence rule](../../notes/productive-deferral-requires-option-evidence-and-convergence.md).

“Information-producing action can dominate both waiting and full commitment”
is probably a mechanism section of the second note rather than a third note.

## Methodology verdict

No neighboring methodology is better suited to the whole agent-planning
problem because none addresses the whole problem.

Auftragstaktik remains the best compact methodology for allocating
unanticipatable execution-time choice while preserving intent. It is not the
best standalone planning instruction. A more reliable current cue is the
explicit transfer gloss **“preserve intent and constraints; delegate
execution-time choice of means”**, optionally paired with the historical name
after activation fidelity has been tested.

The complementary sources also reveal where Auftragstaktik should cease to be
used. If a recurring choice can be captured as a deterministic trigger, a
scheduled elaboration, an evidence-gated test, or a reversible staged probe,
then that choice should move out of unconstrained delegated judgment. Mission
tactics governs the residual cases that remain consequential and hard to
pre-enumerate after those moves.

That conclusion supports the starting theory while making it operational:

1. codify stable recurring decisions;
2. preplan identifiable contingencies and observation surfaces;
3. preserve explicit options while evidence can still change the choice;
4. use bounded probes to acquire missing information where worthwhile; and
5. delegate the remaining situation-dependent means under stable intent and
   constraints.

## Deliberate exclusions

OODA and effectuation were inspected but did not earn ingestion for this
question. OODA's distinctive mechanism is adversarial tempo and the disruption
of an opponent's orientation; its useful delegation material duplicates the
mission-tactics core. Effectuation begins from available means, emphasizes
affordable loss and stakeholder commitments, and permits goals to emerge. That
goal plasticity is poorly matched to intent preservation. Either may deserve a
future source unit for adversarial agent work or exploratory goal formation,
but neither improves the current mechanism enough to enter this source set.

The Dixit and Pindyck book was not ingested because Pindyck's paper establishes
the required option-value mechanism and limitations. The book should be added
only if a later claim depends on a distinction the paper cannot support.

## Source revisit queue

- **PMI Lexicon Version 5:** the complete pinned source is Version 4. Revisit if
  current wording rather than the established paired definitions becomes
  load-bearing.
- **Sobek, Ward, and Liker (1999):** revisit if Commonplace needs direct
  attribution of the original three-principle formulation or historical Toyota
  performance claims. The available archive was image-only.
- **ADRP 6-0 (untouched 2012 edition):** revisit if edition-specific wording,
  the omitted glossary, or source lineage matters. The retained substantive
  chapters incorporate later changes.
- **Pindyck's published JEL version:** revisit only for publication-specific
  wording or pagination, not for the minimal mechanism.
- **Empirical effectiveness:** none of the current ingests warrants a claim
  that the combined methodology improves LLM-agent outcomes. That requires
  target-side tests.

## Machinery revision brief

The theory should not be pasted wholesale into every planning prompt. The next
pass must locate each decision at the cheapest representation that can enforce
or reliably activate it.

Candidate obligations to test against current machinery are:

1. A planner distinguishes fixed intent and constraints from deferred choices.
2. Every deferred consequential choice names why later information will help,
   or is explicitly delegated because the state cannot be enumerated.
3. Where commitment is costly, the plan records the preserved alternative and
   the cost of delay.
4. Where a bounded probe can buy discriminating evidence, the plan considers it
   separately from passive waiting and full commitment.
5. A coarse future item has a replanning horizon, evidence condition, trigger,
   convergence rule, or explicit executor authority; it is not an unowned
   placeholder.
6. Adaptation triggers identify the observation, threshold, and lead time.
7. Multiple alternatives are maintained only when an evaluation surface and
   convergence boundary justify their carrying cost.
8. Delegation states intent, constraints, authority, resources or accessible
   context, coordination boundaries, feedback, and escalation or recovery.
9. A compact methodology cue is used only where its activation fidelity has
   been established or an explicit gloss supplies the intended mechanism.

The audit should decide separately whether each obligation belongs in natural
language methodology, a schema field, deterministic validation, workflow
control, an assay, or runtime code. Predictable checks should not remain LLM
judgment merely because the theory was discovered in prose.

## Evidence and artifact status

The eight ingest reports linked above pass deterministic validation. Seven are
clean; the PMI lexicon has one deliberate warning for the accurate
open-vocabulary genre `reference-lexicon`. Every retained snapshot checksum
matches its ingest frontmatter. Subsequent grounding passes retained a minimal
`## Quotes` section in each ingest before promoting the two source-dependent
claims. Future promotions may use those extracts where they support the exact
claim, but must still run the normal source-grounding guard rather than treating
the ingest analysis as evidence.
