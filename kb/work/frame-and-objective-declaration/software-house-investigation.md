# Investigation: what the automated software house definition supplies

Author: Claude Code agent, claude-fable-5-2, 2026-11-20. Commissioned by the
operator from a brief written by ChatGPT. The brief's last line was cut off
after "Do not rewrite the"; this note assumes it protected the existing
definitions and articles, and none was edited.

Each finding is marked **Established** (stated in a current artifact or a
commit), **Reconstruction** (my reading of how stated parts fit) or
**Conjecture** (not supported by the texts).

## Result

The software house definition does not define capability by a value function.
It defines a role boundary, takes its tasks and acceptance from users outside
that boundary, and sets adequacy by comparison with a human-staffed house on
the same requests and resources. That yields a threshold test for a capable
system. It does not yield an ordering over the system's successors, and it
stops discriminating once the system matches the human baseline.

Two of its three devices already generalize: the theory-builder definition
copied them. The third, the human-staffed baseline, generalizes only to kinds
of knowledge work that a recognizable human institution already performs. It
does not reach "arbitrary knowledge work".

The investigation also bears on this workshop. The objective under dispute is
a ratio of a capability term to an allocation term, and the repository states
a second, different ratio elsewhere. D4 may be fixing the accounting of a
measure that should be two measures.

## Sources read

- [Software house](../../theory/definitions/software-house.md) and the
  [second-test article](../../articles/an-automated-software-house-as-a-second-test-of-a-theory-builder.md),
  which states the conjecture.
- The withdrawn conjecture article, `kb/articles/automated-software-houses-with-fixed-llms.md`
  at `c0f4223af^`, which states the same conjecture at greater length.
- [Theory builder](../../theory/definitions/theory-builder.md),
  [the three obligations](../../theory/a-claim-without-external-assessment-carries-three-obligations.md),
  [the bootstrap article](../../articles/bootstrapping-an-autonomous-theory-builder.md),
  [the research-program note](../../theory/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md).
- [Self-improvement is relative to a declared objective](../../theory/self-improvement-is-relative-to-a-declared-objective.md),
  [the reallocation note](../../theory/computationally-directed-self-improvement-is-a-reallocation.md),
  [a better-factory claim](../../theory/a-better-factory-claim-compares-operative-states.md),
  [the new-domains note](../../theory/new-domains-can-turn-theory-builders-into-software-houses.md).
- The frame note, the instrument note, and this workshop.

The brief asks for "the conjectural learning and reflective learning
definitions". Neither exists now. Conjectural learning and the reflective,
autonomous and externally tested theory-builder definitions were retired on
2026-09-25 (`21021fcc9`). Their successors are the theory-builder definition,
its two qualifiers and the three-obligations note. I read the retired
conjectural-learning text from history.

## Reconstruction of the definition

**Established.** The definition has four parts.

1. *The unit.* A software house is the complete persistent system responsible
   for developing and evolving software for external users. It includes the
   software, its production knowledge and machinery, and every person or
   computational component filling an internal production role.
2. *The boundary.* Users are outside when they supply requirements, domain
   facts, preferences, observed outcomes, acceptance judgments on visible
   behaviour, or later demands. A person is inside when the house depends on
   them to interpret production knowledge, decide implementation, diagnose a
   failure, choose among internal designs, or select the retained successor.
   The boundary follows the role, not the person.
3. *Automation.* A house is automated when computation performs every internal
   production role. User participation is compatible with automation.
4. *What the definition leaves out.* No product family, no horizon, no
   retention and no learning. A house whose fixed machinery suffices for every
   demand meets the definition.

**Established.** The conjecture adds the performance claim. At least one
automated house capable of open-ended coherent software change can operate
practically with models available by 2026-09-02 and held fixed. "Practically"
means adequate performance from a declared seed, over a stated horizon, within
a stated budget, reliably. "Open-ended" means it handles whatever reasonable
requests arise, without their being listed in advance. The working standard is
comparative: on the same requests and resources, it does at least as well as a
house with people in its internal production roles. Four witness conditions
test it: holding and applying program theory, coherent revision, automated
continuation, practical reliability.

## Constants supplied by the human organization

**Reconstruction.** The texts never list what they borrow. These six items are
used without being defined.

| Constant | Where the text leans on it |
|---|---|
| The division of labour between customer and producer | The user and internal-role lists. The customer says what and accepts; the producer decides how. |
| The inventory of production roles | "Such as" lists. The roles are recognized from practice, not derived. |
| What a customer may reasonably ask | "*Reasonable* is left informal" (withdrawn article). |
| The level of adequate performance | "At least as well as" a human-staffed house. |
| That the work is feasible and worth doing | Never argued. Human houses exist and are paid, so neither needs showing. |
| Continuing responsibility for a product | "Persistence means continuity of responsibility". This is the maintenance relationship. |

## What the conjecture declares itself

**Established.** The role-based boundary rule; automation as role allocation;
the model cutoff and fixed weights; the seed, with its construction cost
reported separately from the operating budget; the horizon and budget;
reliability across repetition; the four witness conditions; a protocol
declared before the run. "Coherent" is imported from Naur's program theory and
is the one quality term the conjecture defines for itself.

## Answers to the brief's questions

**3. How the baseline defines competence.** *Reconstruction.* It replaces an
absolute quality scale with non-inferiority to a known producer. It also
controls for task difficulty: a request no house could meet within budget
fails for the baseline too, and the withdrawn article says such requests "do
not count against the house". Holding requests and resources fixed leaves role
allocation as the varied factor, so the test is a substitution experiment on
one functional boundary.

**4. Unforeseen tasks without a value function.** *Reconstruction.* Three
things are placed outside the house: choosing the task, judging the result,
and deciding the request was worth making. The house is never asked to rank
tasks. Open-endedness is defined on the demand side, as requests not listed in
advance, not on the supply side as coverage of a space. *Established:* commit
`08215a3dd` (2026-09-05) removed declared product scope from the definition
and moved scope and horizon to the evaluation, which "bound what its evidence
establishes" without defining future responsibilities. The price is also
established: no finite run establishes the open-ended claim.

**5. Automation, learning, self-improvement.** *Established:* they are three
separate claims.

- Automation is allocation. Its test is removal: withhold human decisions and
  see whether the pathway completes.
- Learning is not in the definition. It is improved capacity for future
  action, tested by its own comparison. The article says a house could meet
  all four witness conditions by outcome-scored repair and confirm the
  conjecture without being a theory builder.
- Self-improvement is operative, evidence-responsive change to the house's own
  machinery against a declared objective.

*Reconstruction.* In a house, self-improvement arises as derived demand. An
external request that the current machinery serves badly creates a need to
change the machinery. The objective for that change is inherited from the
request, and the user's acceptance of the product is an outside outcome level
for it. Attribution to the machinery change is still owed. This matches the
brief's claim that self-improvement is one application of the house's general
capability.

**6. Judgments that stay with users.** *Established:* requirements, domain
facts, preferences, observed outcomes, acceptance of visible behaviour, later
demands, task selection, and authorization of a changed objective.

**7. Ambiguities and circularities.** See the next section.

## The capable system and the improvement function

**Reconstruction.** The definition gives a predicate, not an ordering. A house
is capable when it is non-inferior to the human-staffed baseline on the
arising requests. That needs one comparison against one fixed outside
reference.

An improvement function compares a system with its successors. The house
definition says nothing about that. [The better-factory note](../../theory/a-better-factory-claim-compares-operative-states.md)
does: non-regression on the predecessor's prior scope plus a declared gain,
both fixed before development. It records that "what makes a successor
genuinely better over an open family remains unresolved".

**Conjecture.** The two have the same form with a different reference. The
capability test asks whether the house serves a request stream at least as
well as a human-staffed house given the same resources. The successor test
asks the same with the predecessor as the reference. If that holds, the
software house frame needs no separate improvement objective. It needs a
declared request stream and a declared reference.

**Established limit.** The human constant runs out at parity. Non-inferiority
says nothing about two systems that both exceed the baseline.

## Simplifications that result

- No theory of value. Value judgments are made by users, one request at a
  time.
- No enumeration of the task space.
- No absolute quality scale.
- Autonomy becomes a yes-or-no property of allocation, kept apart from
  capability.
- Learning and self-improvement become optional means, not defining
  properties.
- A person's two positions are separated by role, so one person can be both
  user and producer without contradiction.

## Unresolved problems

1. **"Same requests" under path dependence.** Later requests depend on the
   product earlier requests produced. Two houses diverge after the first
   change. Commit `08215a3dd` pins request-selection rules before the run;
   that does not make the streams identical.
2. **"Same resources" needs a common unit.** Salaries and compute are compared
   only through price. This is the one place where economics is needed to
   state the test at all. It is commensuration, not optimization.
3. **Which human house.** Human houses vary widely. The baseline is not
   specified as median, competent or best.
4. **Reasonableness is endogenous.** A cheaper producer changes what customers
   ask for. The baseline's request distribution is not the automated house's.
5. **The user and producer line depends on the product.** "Visible behaviour"
   is clear for software. A user who must specify in unusual detail is doing
   design.
6. **Acceptance can track a proxy.** The three-obligations note says so.
   Coherence shows only in later changes, so the horizon must be long.
7. **The seed.** "Its seed must already be a working house." Competence shown
   in a run is not separated from competence built into the seed.
8. **No ordering beyond parity**, as above.

## What might generalize to knowledge work

**Established: two devices already generalized.** Commit `694a78bef`
(2026-09-09) drafted the theory-builder definition "by copying the
software-house definition clause by clause". The role-based boundary and the
outside user who supplies problems and judges products are both in the current
[theory builder](../../theory/definitions/theory-builder.md#boundary)
definition.

**Established: the falsifier does not generalize.** On 2026-09-17 the operator
declined the software-house label for Commonplace and demoted the house to a
companion arrangement (`21216abd3`, `d17b5a772`). The stated differences are
product, falsifier strength, claim form and required machinery. A knowledge
product has no build that breaks. A rejection is evidence about the task, the
consumer and the knowledge together.

**Established: the baseline was not carried over.** The theory-builder
definition "has no success condition". No comparative standard replaced the
human-staffed house.

**Conjecture: the baseline generalizes per institution.** The device needs a
recognizable human organization doing the same job. Kinds of knowledge work
have one: a documentation team, an analyst desk, a research group. "Arbitrary
knowledge work" does not. A definition for knowledge work would name the
institution it automates, as the house does.

**Conjecture: product and machinery must be separable.** In a house the
customer's product and the house's tooling are different artifacts, so
production and self-improvement are different activities. This repository is
a methodology KB whose content is its own method, so the two coincide here.
They separate again for a consuming project's KB. That is the conflation the
brief names: improvement of Commonplace against Commonplace's purpose of
supporting other knowledge work.

## Consequences for this workshop

1. **The objective is a ratio of two separate things.** *Reconstruction.*
   "More useful and better-warranted knowledge work per unit of human judgment
   spent" divides a capability term by an allocation term. A ratio fixes a
   trade-off between them that no artifact argues for.
   [The objective note](../../theory/self-improvement-is-relative-to-a-declared-objective.md)
   says the profile's dimensions "cannot determine how to trade them off" and
   that a combination used as an objective needs a linking claim.
2. **The repository states two ratios.** *Established.* The instrument note
   measures knowledge work per unit of human judgment. The bootstrap article
   measures "human decisions each completed, verified improvement requires"
   and rejects operator hours as a measure. The first is about operation, the
   second about the improvement pathway. Neither artifact mentions the other's
   measure.
3. **D4 "whose judgment" has a role-based answer.** *Reconstruction.* Position
   C worried that a boundary-tied denominator rewards moving diagnosis to an
   outside contributor, and proposed counting everyone's judgment. Under the
   role rule, a contributor who diagnoses fills an internal production role
   for that act and is inside. A user's requirement or acceptance judgment is
   outside and is not a production cost. That agrees with position D's point
   that reader cost belongs in the numerator.
4. **The declared frame is partly person-based.** *Established.* The frame
   note puts "designated maintainers" inside and "arbitrary contributors,
   readers, and advisers" outside. The software-house and theory-builder
   definitions both say the boundary follows the role. An adviser who
   diagnoses is outside under the first and inside under the second.

Items 1 to 3 are a reason to hold the D4 ruling until the operator has decided
whether the objective stays one ratio. Item 4 is a new discrepancy that no
position raised.

## What I did not do

- I did not read the lead article or the testing supplement in full; I relied
  on the research-program note and the second-test article for how learning is
  tested.
- I did not check whether any retained analysis or review already compares a
  system against a human-staffed baseline.
- I did not test the conjectures above against cases.
