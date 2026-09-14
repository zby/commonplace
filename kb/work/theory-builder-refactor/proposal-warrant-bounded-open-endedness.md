# Proposal: warrant-bounded open-endedness and a fallible-theory definition

> **Status:** Earlier proposal, 2026-09-14; retained as an argument record.
> The [current definitions and review plan](./README.md) supersede its edit
> list and operator-choice list. Open-endedness became measured extension;
> separate fallible-theory and resource-bounded-interpreter drafts now exist.
> The closure, evaluator-revision, and oracle claims below remain arguments
> to assess, not established premises. The conjecture that reflection lowers
> extension cost remains untested.

## Why this proposal exists

A review of commit `67f960c8` found three problems in the revised
definitions. The discussion that followed reached conclusions that change
what the open-ended condition should say and showed that one term the
definitions lean on, *fallible theory*, has no definition of its own. The
conclusions are recorded here so that the definition edits can be made in
one pass, in a settled order, rather than one clause at a time.

## 1. Problems found at review

1. **Open-endedness has no declared axis and no boundary cases.** The
   2026-09-14 text dropped the link to
   [universal software factory needs a declared universality axis](../../notes/universal-software-factory-needs-a-declared-universality-axis.md),
   which the inventory keeps for exactly that rule. It is also the one
   condition with no boundary cases. The operator confirmed that Commonplace
   today is open-ended and not autonomous; the README still describes it
   only as reflective and non-autonomous.
2. **Reflective and open-ended overlap.** The reflective definition says the
   builder may "change the implicated machinery" when external work exposes
   a limitation. That is a machinery extension in response to a demand,
   which is what the open-ended section describes. The theory-family
   concept used to keep them apart. Section 3 below separates them by
   pathway and reachable set instead.
3. **The dropped term survives in the library.** The
   [theory-refinement definition](../../notes/definitions/theory-refinement.md)
   still says the interpreter "constructs family-specific machinery after
   the family arrives". The proposal, interface, and manipulator drafts use
   the term about forty times. The inventory does not list the library
   definition as needing a second reframe.

## 2. Bare open-endedness is cheap; the target is resource-bounded

**Extension is a diff, not a reachability claim.** An extension is machinery
retained after a declared seed that supplies a capability the seed's retained
machinery did not have. Activating a component the seed already retained, or
changing a value in a slot the seed already had, is not extension. How the
extension is produced is unrestricted: a person, a model, or a search
procedure over programs. The operator decided that exhaustive search
qualifies. In-principle reachability was rejected as the criterion: any
builder containing a general constructor reaches any machinery in principle,
so reachability distinguishes nothing. The theory-refinement definition
already makes this point about Turing-complete program search, and the
seed diff is what survives it.

**The bare condition is therefore prior art.** The
[Gödel machine](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
is computational, so autonomous; holds a causally connected
self-representation it rewrites, so reflective; and can rewrite any part of
its code, including the searcher, so open-ended. It meets all three bare
conditions. The README currently says the Gödel ingest and note are "no
longer needed". They are needed as the witness that the bare three-condition
target is not the advance.

**Two limits, both inherited from the formal case.** The Gödel note's
"three different limits" section separates a rewrite that is unprovable
under the axioms from one that is provable but not found within available
resources. Both limits carry over to the fallible builder:

- **Cost.** Exhaustive search is open-ended and would demonstrate almost no
  extensions under real resources. The evaluable content of open-endedness
  is the record of demonstrated extensions and what each cost in compute,
  elapsed time, and evidence consumed. The comparative standard, extension
  at a cost comparable to a builder with people in its internal roles, is
  the target rather than a side question.
- **Warrant closure.** Section 3.

The parallel with the autonomous file is exact: bare autonomy is free and
the target is warranted autonomy; bare open-endedness is free and the target
is extension within the resources a demand affords, under the warrant bound.

## 3. The warrant-closure bound

**Statement.** In the Gödel machine, the reachable rewrites are the deductive
closure of the initial axioms and utility. In the fallible machinery, the
warrantedly reachable extensions are the closure of the seed under
evidence-licensed proxy revision, rooted in the seed's terminal objective and
the kinds of evidence it admits. Evaluators rotate, so the bound is not the
seed evaluators. It is the seed objective, which plays the role the axioms
play.

**Where the KB already has the pieces.** The Gödel note supplies the two
limits. The
[self-revision boundary map](../self-revision-design-space/boundary-map.md)
states that a properly warranted incumbent evaluator can govern its own
replacement, names the Gödel machine as "the limiting formal case", and
records the fallible-side cost: an incumbent "can rubber-stamp a successor,
share its errors, or apply a candidate-authored criterion whose probative
force presupposes the candidate".
[Revising an improvement objective is licensed from outside it](../../notes/revising-an-improvement-objective-is-licensed-from-outside-it.md)
fixes what stays pinned: proxies are revised against the unchanged objective,
and no change to the terminal objective can be warranted as an improvement
from inside. The objective can still change; what the closure bounds is
warranted reach, not reachable states.
[Warranted autonomy is bounded by oracle domain](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md)
gives the per-step bound. The
[proposal-selection loop note](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
leaves as an open question whether a fallible evaluator can govern its own
acceptance criteria "without either an external criterion or the
axiomatization that buys formal closure". This proposal answers it in part:
it can govern changes to its criteria against an unchanged objective, and it
cannot govern changes to that objective, with or without axiomatization.

**Two differences from the formal case.** The Gödel machine's axioms also
bound admission, since a candidate must be expressible in the proof
language; the fallible machinery's interpreter admits anything, so its bound
is on warrant only. And, after the operator's correction in section 4, the
fallible builder does not retain unwarranted claims. Its library reach equals
its warranted reach at the consumption threshold, and its excess over that
is a frontier, not retained theory.

**Consequence for the research target.** Commonplace today escapes the
seed-objective closure only because the operator is inside the boundary and
licenses objective changes from outside it. Remove the operator and no
objective change is licensed, so the warranted closure is rooted in the seed
objective. An autonomous open-ended builder is therefore in the
Gödel machine's situation with fallible checks in place of proofs, and its
extensions have two limits: the cost of finding one, and the warrant closure
of its seed objective and admitted evidence.

## 4. Fallible theory must be defined first

The theory-refinement definition defines *theory* by three properties:
consequences a case can contradict, parts available as repair locations, and
parts editable separately. It uses *fallible* in its description line and
opening sentence and never says what the word adds. The closure bound cannot
be stated without it. Three clauses are needed.

1. **Retention at partial warrant, as a frontier.** The operator rejected
   the reading that fallible theories extend through unwarranted claims. A
   claim enters with starting warrant, from derivation or from a first case,
   and the scope it claims beyond its evidence is what the next tests
   target. Retention above the consumption threshold requires warrant.
   Below it, a claim is held as a target for the search that could raise its
   warrant, not as theory.
   [Derivation and inheritance give starting warrant; evidence earns scope](../../notes/derivation-and-inheritance-give-starting-warrant-earns-scope.md)
   already says this for claims. The
   [workshop layer](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md)
   is the structural implementation, and a workshop that accretes untested
   candidates is its known failure.
2. **Warrant per claim and scope, from evidence.** Passing cases confer
   warrant on the claims and scopes they exercise, not on the theory.
   [Theory warrant is tracked at the finest granularity evidence licenses](../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md)
   has this as a tracking rule; it needs to become part of what a fallible
   theory is.
3. **Revision licensed by evidence relative to an unchanged objective.** A
   revision is warranted when evidence shows it corrects errors and
   preserves fit on tested cases, judged against an objective the revision
   does not change. This is what makes warranted revisions chain into a
   closure rooted in the seed objective.

With these, two sets are definable: the theory states reachable by any
revision, and the states reachable by warranted revision from a seed under
an objective. Fallibility is then two things: warrant is never total,
because claimed scope always exceeds tested scope; and the assessment of
warrant is itself a fallible evaluator's output. The characteristic failure
is misassessed warrant,
[false-positive acceptance becoming operative](../../notes/false-positive-generation-is-filtered-before-retention.md),
not unwarranted retention.

**Consumption gated by warrant.** The boundary map's distinction between
improvement-warranted reach and bounded-experiment reach gives the grades a
home. A partially warranted claim may license actions whose cost of being
wrong is bounded, such as a trial, and not
[costly entrenchment](../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md)
such as codification or a machinery change.

**What not to do.** A mathematical formalization is the codification move,
and
[semantic work can be relocated but not eliminated](../../notes/semantic-work-can-be-relocated-but-not-eliminated.md):
a formal model of fallible theories would need checking against the
interpreted case it was built to explain. Formalize only what the closure
claim consumes: the three clauses and the two reachable sets, in prose, with
a short set-theoretic sketch only if it makes the closure exact.

**Check the literature before writing it.** From recollection rather than
from snapshots, and so to be verified by ingest: AGM belief revision
formalizes revising a fallible theory under minimal change, which is the
"preserve useful prior knowledge" clause; formal learning theory (Gold,
Kelly's reliable inquiry) formalizes which hypotheses a method can converge
to from an evidence stream, which is the closure bound as a theorem,
relative to a hypothesis space fixed in advance. Neither is ingested; the
KB's hits on "AGM" are substrings of other words. The automated-scientist
systems (the Robot Scientist, the AI Scientist, POPPER,
[FunSearch](../../sources/mathematical-discoveries-program-search-large-language-models.ingest.md),
AlphaEvolve, the
[model-discovery agent](../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md),
the
[Darwin Gödel Machine](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md))
implement the loop with the evaluator or objective fixed at the seed. They
exhibit the closure bound rather than state it, and they formalize warrant
of a single hypothesis, not of a revision to the evaluators. Two ingests,
each with one question: AGM, asking whether the three theory properties and
minimal change are its postulates restated; Kelly, asking whether the
seed-rooted closure is a stated result and what it assumes about the
hypothesis space. Closing condition 3 forbids claiming generic refinement or
fallibility as new, and the ingests are the evidence the claim was checked.

## 5. What a sandbox test buys

The operator asked whether the Gödel machine could add a search step that
performs the rewrite in a sandbox and checks whether it is good. That is the
Darwin Gödel Machine, which its paper describes as relaxing the proof
requirement in favour of empirical evidence. The step swaps the kind of
warrant, not the existence of a bound: proof under axioms becomes performance
under an evaluator, and the closure moves from the axioms to the evaluator's
oracle domain. The check establishes partial warrant on the tested cases for
the tested scope, which is the evaluate operation over a fixed case set with
its known local-maximum failure. Two things the step cannot check: the
checker, since a rewrite that changes the evaluator cannot be checked by it
without circularity (the ingest records an agent that maximized its
hallucination score by deleting the marker its detector keyed on, with every
containment safeguard holding); and the bridge from sandbox performance to
deployment utility, which is an inductive premise no proof and no sandbox run
supplies. The step is necessary for the fallible builder, because it is how a
frontier claim earns warrant. The target differs from the Darwin Gödel
Machine in what surrounds it: a revisable evaluator bounded by the objective
rather than by a fixed benchmark, a self-theory that selects which rewrites
to test, and warrant tracked per claim and scope so that "better on these
cases" is what gets retained.

## 6. The ideal-interpreter layering

The operator proposed that doing semantic work is what distinguishes the
builder from the Gödel machine, that LLMs cannot fully do it, and that an
ideal machine could be postulated with LLMs as approximations, as physical
computers approximate Turing machines. The session's assessment: the
idealization is useful, but its axis is reliability, not finiteness. An LLM
with a harness and external memory already has unbounded tape in the relevant
sense
([context is limited by soft degradation, not hard token limits](../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md)).
What a stronger model supplies is fewer interpretive errors over a wider
domain, which is the
[oracle-strength gradient](../../notes/oracle-strength-spectrum.md). The
ideal is an interpreter of unbounded oracle strength over a declared domain,
Turing's oracle machine in the KB's terms.

What the device buys is a separation of architecture results from
approximation results, as computability separates from complexity. Under an
ideal interpreter: the objective closure survives, since it comes from the
licensing structure; the inductive frontier survives, since interpretation
says what a claim commits to and not whether it holds beyond tested scope;
the admission limit does not survive, and this is the real content of
"semantic work distinguishes us". The Gödel machine's semantic work was done
at design time by whoever chose the axioms
([supplied provenance fixes the pre-formal stage in the designer](../../notes/open-ended-theory-learning-and-factory-learning-close-the-same.md));
the builder moves the
[pre-formal stage](../../notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md)
inside its boundary.

Where the analogy breaks: a Turing machine has an observer-independent
syntactic definition, so approximation is well-defined; a semantic oracle is
defined by the commitment it preserves, which belongs to someone, so the
ideal is not definable without declaring whose commitment it tracks. And the
definition must take a fork: if interpretation is oracle-shaped, an ideal
machine returns the right answer; if it is conjecture-shaped, as the
[discovery lifecycle](../../notes/definitions/discovery-lifecycle.md) and
[explanatory-reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md)
notes treat it, no machine completes it and the LLM performs the same
fallible process with less reach. The KB's commitments lean to the second.
The oracle is still usable as an analytic device, stated as one.

## 7. A conjecture: reflection buys cheap extension

An exhaustive searcher pays for extension by searching all programs. A
builder whose self-theory has explanatory-reach can localize which part of
its machinery a demand exposes as inadequate and search only over candidate
repairs to that part: the locate operation applied to the self-theory. If
that holds, reflection is the mechanism that converts in-principle
open-endedness into resource-feasible open-endedness, and the program's
central claim is that a self-theory with reach buys extension cheaply enough
to compete with the human-staffed baseline. This is untested. It is recorded
so that the interface reconciliation knows what the locate operation has to
support.

## 8. Proposed edits, in order

1. **Write the fallible-theory definition** (section 4), after the two
   ingests, as a new `kb/notes/definitions/` note or a section of the
   theory-refinement definition, which already claims to define *theory*.
2. **Rewrite the open-ended section** of [theory builder](./theory-builder.md):
   extension as seed diff and added capability, mechanism-neutral; the
   declared axis restored as the machinery space assessed by that diff; a
   sentence parallel to the autonomy file, that bare open-endedness is free
   and the target is extension within the resources a demand affords,
   measured against the human-staffed baseline; the warrant-closure bound
   citing the fallible-theory definition; and boundary cases: FORTE closed
   (its four operators and evaluation procedure are the whole machinery), a
   program-search builder open-ended but neither reflective nor persistent,
   Commonplace today open-ended and not autonomous with the ADR set as its
   extension record, and the research target.
3. **Sharpen the reflective independence clause**: reflection is about
   whether machinery changes pass through a causally connected self-theory;
   open-endedness is about whether capability-adding changes happen and are
   retained. A builder that refines a self-theory but only retunes values
   within existing capabilities is reflective and not open-ended.
4. **Add to the autonomous file** the objective-pinning consequence: with
   no person inside the boundary, no change to the terminal objective is
   licensed, and warranted extension is bounded by the closure of the seed
   objective. The objective may still change unlicensed.
5. **README**: restate the research target as the resource-bounded and
   warrant-bounded version; name the Gödel machine as the prior-art instance
   of the bare combination; revise the two Gödel inventory rows to "needed as
   prior-art witness" and fix the ingest's snapshot hash rather than retire
   it; add the theory-refinement definition to the inventory as needing a
   second reframe for the family wording; record the section 7 conjecture as
   the candidate central claim, untested; state the two-layer form of the
   target (architecture layer under an ideal interpreter, approximation
   layer for a given model's oracle strength and the resource constraint).
6. **Reconcile the interface material** after the above, since evaluate for
   an interpreted theory now means "raises warrant on tested scope" and the
   sandbox case (section 5) is its worked example.

## Relation to the Gödel-machine comparison

The [Gödel-machine comparison](./goedel-machine-comparison.md), written in a
parallel session on the same day, places the distinction in the grounds for
a machinery change: proof under a formalization against evidence relative to
an objective. This proposal agrees and adds the two limits that survive the
change of grounds. The comparison's closing section reserves judgment on
one claim made here: that all future warrant is the closure of the seed
objective and evidence rules. It reads the objective-revision note as
limiting what licenses an improvement claim, not as establishing that an
autonomous builder's objective cannot change. Section 3 has been worded to
match that reading: the closure bounds warranted reach, and an unlicensed
objective change remains possible. Whether the closure claim needs the
separate argument the comparison asks for, before it enters a definition, is
listed below as an operator choice.

## Choices left to the operator

- Whether the warrant-closure bound (section 3) enters the open-ended
  section on the strength of the notes cited there, or waits for the
  separate argument the Gödel-machine comparison asks for.

- Whether interpretation is treated as oracle-shaped or conjecture-shaped
  (section 6). The definitions can use the ideal interpreter as a device
  either way, but the README's statement of the target reads differently.
- Whether "full warrant" is a level or a relation to a stated consumption
  path at a required confidence. The proposal assumes the relation.
- Whether zero-warrant material (log entries, open questions) counts as the
  frontier's lowest rung, so that "no unwarranted claims" does not read as
  "no unresolved questions".
- Whether the two ingests precede the fallible-theory draft or the draft is
  written first and checked against them.
- The term for the resource-bounded target, parallel to *warranted*
  autonomy. None is proposed here.
