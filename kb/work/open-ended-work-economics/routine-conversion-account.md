# Draft: when converting work into routine pays

Status: draft for test 3 of the [reconciliation map](./reconciliation.md).
The account is assembled from held notes; its claim to be a mechanism rather
than a list is what the retrospective below tests. Terms follow
[vocabulary.md](./vocabulary.md): "constrained" for a natural-language
routine (a prompt, skill or convention), "codified" for a symbolic one.

## The claim

Converting a recurring piece of work into a routine is a bet. The stake is
set by how often the work recurs and what each use saves; the odds are set by
how well the extracted pattern's stability is understood. The library's
existing rules for conversion (observe before committing, promote on stable
repetition, relax on failure signals, constrain in natural language before
codifying) are each a way of either lowering the stake or improving the odds.
Stated as one account, they predict one thing the rules separately do not:
a conversion justified by an explanation of why the pattern holds should need
relaxing less often than one justified by observed frequency alone.

## Terms

Seven quantities enter the decision (six in the first draft). None has a portable numeric threshold;
the library's position that such judgments are qualitative stands
(reconciliation, direction 2). The account says how they combine, not how to
measure them.

| Term | What it is | Where the library already has it |
|---|---|---|
| **Recurrence** | How often the work will recur over the horizon in which the routine would be used. Not the past count alone: conversion can itself raise recurrence by making the work cheap enough to run more often. | ADR 040's promotion signal; [increasing autonomy relocates effort](../../theory/increasing-computational-autonomy-relocates-human-effort.md) (elastic workload) |
| **Saving per use** | What the routine saves each time: the interpretation the actor no longer performs, plus the error cost the routine's reliability removes. A saving that comes from reliability needs a checker; without one the error cost is not removed, only hidden. | [constraining](../../theory/definitions/constraining.md) (reliability, speed, cost as consequences); [the boundary of automation is the boundary of verification](../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) |
| **Construction cost** | What it costs to build the routine, including the observation time spent before committing when the pattern is mined from behaviour. | [progressive constraining](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) ("you pay for this with observation time"); [spec mining](../../theory/spec-mining-as-codification.md) |
| **Use cost** | What each use of the routine costs: invoking it, checking its output, retrieving it so it is applied at all. A routine nobody retrieves saves nothing. | [codify versus LLM](../../theory/codify-versus-llm-decision-heuristics.md) repetition section; [skill discovery re-fires in every sub-agent context](../../theory/skill-discovery-re-fires-in-every-sub-agent-context.md) |
| **Carrying cost** | What keeping the routine costs while it exists: maintenance as its premises drift, and the migration cost of removing it once other things depend on it. Codified routines carry more of the second than constrained ones. | [current-task fit does not warrant costly entrenchment](../../theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md); [cheap adoption and weak retirement accumulate cost](../../theory/cheap-adoption-and-weak-retirement-accumulate-cost.md) |
| **Stability** | The conjecture that the extracted pattern is part of the task (an exact spec) rather than an accident of the observed cases (a proxy theory), over the horizon. This is the one term that is a claim about the world and can be wrong. | [codification is a bet](../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md); [relaxing signals](../../theory/operational-signals-that-a-component-is-a-relaxing-candidate.md); [exact specs versus proxy theories](../../theory/exact-implementation-does-not-validate-a-requirement.md) |
| **Exposure** | What a wrong routine costs before its failure is noticed, beyond the carrying cost of removing it. Zero when no consumer's correctness depends on the routine; large when downstream work builds on its output. Added after the retrospective (below): the first draft kept it in prose and two of four cases turned on it. | ADR 026's "accelerator, never a load-bearing wall"; [false-positive acceptance becomes operative](../../theory/false-positive-generation-is-filtered-before-retention.md) |

## How they combine

A conversion pays when, over the horizon, recurrence times the net saving per
use (saving minus use cost) exceeds construction plus carrying cost, weighted
by the chance the pattern holds; and when it does not hold, the loss is the
carrying cost plus the exposure. Three consequences follow from the shape,
not from any numbers.

**Stability sets the odds; the other terms set the stake.** Recurrence and
saving decide how much is won if the pattern holds; construction, carrying
cost and exposure decide how much is lost if it does not. Exposure is the
term a designer can drive to zero independently of stability, by letting
nothing depend on the routine's correctness; that is how a low-stability
conversion can still pay. A pattern can recur every run
and still be a bad conversion if its stability is unknown and the routine
would be expensive to remove. The reverse also holds, and the library states
it: "a sound operation can be worth implementing after one informative
case" when stability is known by specification (the arithmetic regime), and
"another may remain cheaper to interpret even after many cases because its
premises change frequently."

**Stability can be bought, two ways.** Observation buys it empirically:
progressive constraining spends observation time to raise confidence before
paying construction cost, and the promotion signal (repetition with a stable
interface across unrelated sessions) is the cheap form of that observation.
Explanation buys it differently: an account of *why* the pattern holds says
which changes would break it, so the conversion's scope can be stated and its
relaxing trigger named in advance. A frequency-backed routine knows only that
the pattern held so far. This is the point where the account depends on
theory building: the quality of the stability conjecture bounds the quality
of the conversion decision, and improving that conjecture is theory work,
not more observation.

**Carrying cost orders the forms.** A constrained routine (prompt, skill,
convention) has low construction cost, low removal cost and an interpreter
failure rate; a codified one has higher construction and removal cost and no
failure rate within its scope. So the account predicts the staging the
library already practises: constrain in natural language while stability is
uncertain, codify when stability is understood and a checker exists. It also
predicts that relaxing a codified routine will be recorded as a decision
(an ADR, a migration) while relaxing a constrained one often leaves no record,
which matters for test 2 in the reconciliation map.

## What the account predicts

1. **Mechanism-backed conversions relax less often than frequency-backed
   ones**, and when they do relax, the trigger is one their scope statement
   named. Frequency-backed conversions relax on surprises.
2. **Refusals to convert cite a small stake or unknown stability, and
   name the observation that would change the answer.** (Revised after the
   retrospective; the first draft predicted refusals would not cite
   recurrence, and ADR 040 does.) A refusal that names no escalation
   trigger is one the account would call a missed deferral rather than a
   decision.
3. **Conversions made without a checker save less than expected.** Where a
   routine was built without a way to reject its wrong outputs, the record
   should show the error cost reappearing downstream rather than
   disappearing.
4. **Converting raises recurrence of the converted work and the epistemic
   share of what remains**; the second is held already
   ([preferential codification](../../theory/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md)).

## What would show this is a list, not a mechanism

If applying it to recorded cases needs a term the table lacks, or if the
six terms predict a case's decision only after the decision is known (every
term can be read either way), the account adds nothing to the repetition
section of codify-versus-LLM and should be folded into it as a paragraph.

If prediction 1 fails on Commonplace's own record (mechanism-backed routines
relaxed as often as frequency-backed ones), the dependence on theory building
is not shown, and the resource-rational rival (adopt for cost, relax for
cost) explains the history as well.

## Retrospective application

Case facts are in [search/conversion-cases.md](./search/conversion-cases.md);
only what that file records is used. For each case: the terms as the record
states or omits them, what the account would have advised, what was
decided, and the outcome.

### Case 1: the tag-readme validator (ADR 026, revised by ADR 090)

| Term | Record |
|---|---|
| Recurrence | Fires on every validation of 15 marked heads; the saving's consumer (connect skipping `rg`) is uncounted. |
| Saving per use | Stated and small: "one tool call". |
| Construction | About 25 minutes from ADR to migration, four forms in one commit; thresholds from a manual calibration pass. |
| Use cost | Not measured. |
| Carrying | Accepted as cold repair at fix time; drop of the mark "cheap" by design. |
| Stability | For `complete`: stated low, with the mechanism ("inevitably grows into the gate") and the trigger (drop the mark) named. For `covered_by`: unknown; built ahead of its first case. |
| Exposure | Driven to zero: "accelerator, never a load-bearing wall: no consumer's correctness may depend on it". |

Account's advice: `complete` pays despite a small saving and low stability
because construction is cheap and exposure is zero; `covered_by` does not
pay because recurrence is zero (no consumer) and nothing bounds the bet
except deferral. Decision: both built. Outcome: `complete` held and was
revised on its named mechanism (ADR 090); `covered_by` was adopted by one
head, dropped twice, and retired because "nothing consumes the relation".
The account agrees with the record on `complete` and disagrees on
`covered_by`, and the outcome sided with the account. No extra term was
needed once exposure is in the table.

### Case 2: the artifact-run engine (ADR 113, retired by ADR 118)

| Term | Record |
|---|---|
| Recurrence | One consumer; a second never arrived. Ten days in service; 76 runs unfinished at retirement. |
| Saving per use | Recoverability and fewer correction turns (the batch 01 audit); quality compared once, cost never. |
| Construction | Unstated at build; at retirement about 3,000 lines serving the state model against 1,000 of domain logic. |
| Use cost | High and found one day after adoption: every check job needs a handler; a 498-line plan; "every copy a place to drift" (ADR 117). |
| Carrying | The consistency machinery for open attempts; migrating 76 runs declined. |
| Stability | Stated low in advance: a bridge under "the operator's expectation, not an observed fact" that harnesses would bring schedulers; the intent was to keep it "as small as possible, because it is the part expected to be discarded". |
| Exposure | Moderate: runs and worktrees depended on the engine's records; 32 published runs stranded. |

Account's advice: with stability stated low and the obsoleting condition
named, the stake had to stay small; the construction and carrying cost
built were not small, so the bet was mispriced against its own stated
odds. Decision: built at full size. Outcome: retired on the named
condition (every harness gained a headless mode), with the retirement ADR
using the account's own comparison ("3,000 lines serving that model
against about 1,000 of domain logic") and declining future requirements
"bindingly" to cap carrying cost. The account disagrees with the
construction decision and the outcome sided with it. The relaxing trigger
was the one the stability conjecture named: prediction 1 holds here.

### Case 3: grounding promoted to `cp-skill-ground` (ADR 076)

| Term | Record |
|---|---|
| Recurrence | 264 claim uses across ten cohorts before promotion; ongoing invocation by writers after ADR 078, uncounted. |
| Saving per use | One advertised route instead of two; transcription checking moved to code. |
| Construction | Near zero: "body and result protocol ... unchanged". |
| Use cost | Skill discovery; the `context: fork` caveat that promotion isolates nothing. |
| Carrying | Three later amendments (ADR 078, 081, 094), each a decision without an effort figure. |
| Stability | Asserted from repeated autonomous runs; "promotion changes discovery and invocation, not the procedure itself". |
| Exposure | Near zero: promotion "forecloses nothing". |

Account's advice: convert. Decision: converted, on the day one request had
two advertised surfaces. Outcome: still in use and extended. The account
agrees with the record. The amendments are interface revisions, not
relaxings, so prediction 1 is not tested here. The case does confirm the
staging the account predicts: notes, then instruction, then skill, with
construction and exposure near zero at each step.

### Case 4: refusal to codify `scripts/` cleanup and promotion (ADR 040)

| Term | Record |
|---|---|
| Recurrence | One stale script in six over 15 months. |
| Saving per use | Unstated. |
| Construction, carrying | Unstated for the declined sweep. |
| Stability | For the promotion signal: "stabilization across uses", resting on progressive constraining. |
| Exposure | Unstated. |

Account's advice: do not build; the stake is too small for any construction
cost, and name what would change that. Decision: declined, with "a
scheduled sweep is the escalation path, not adopted now". Outcome: norms
unchanged; no sweep adopted; whether the monthly triage happened is
unrecorded. The account agrees with the record. The stated reason is
recurrence, which refutes the first draft's prediction 2 as written; the
revised prediction 2 fits.

### Result of the test

- **A list or a mechanism?** The seven terms predicted all four decisions
  without a further term, after exposure was promoted from the prose to the
  table. In two cases (`covered_by`, the engine) the account's advice
  differed from the decision taken and the outcome sided with the account,
  which is what distinguishes a mechanism from a post-hoc reading. The
  account therefore does not fold into the codify-versus-LLM note; it
  extends it.
- **Prediction 1** (mechanism-backed conversions relax on named triggers):
  both recorded relaxings (`complete` revised on its named drift; the
  engine retired on its named obsoleting condition) fit; `covered_by`,
  which had no mechanism, relaxed on a surprise. Three instances, no
  counterexample; too few to separate from the resource-rational rival,
  which also fits the engine case (a cheaper method arrived). What the
  rival does not explain is why ADR 118 names declined requirements
  bindingly: that is pricing future carrying cost from a theory of what
  the machinery was for.
- **Prediction 2** was wrong as drafted and is revised.
- **Prediction 3** (routines without a checker leak error cost) is untested:
  case 1 contained exposure instead of adding a checker, case 3 added one.
- **A pattern the cases share:** both losing bets were built ahead of
  observed recurrence (`covered_by` "deferred to the first real case"; the
  engine's second consumer). The account's cheapest advice is the one the
  library already gives for scripts and did not apply to types and engines:
  do not construct before the recurrence is observed unless exposure is zero.
- **Evidence limits.** Four cases from one repository, chosen by a search
  worker for having dated records; no case has measured use cost or
  per-use saving; recurrence is counted in only one case.

### What changes in the workshop

Test 3 passes with a correction (exposure). The account is a candidate for
extraction as a theory note once test 2 (classify relaxings by trigger
across more cases) has run, since prediction 1 is what makes it more than
the repetition section of codify-versus-LLM.
