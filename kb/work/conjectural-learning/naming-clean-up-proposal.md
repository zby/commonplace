# Proposal: separate the learning process from its accessible formulation

Status: independently reviewed by three agents; awaiting operator decision,
not adopted. The operator
requested this record and reviews on 2026-09-20. Its purpose is to settle how
the name *conjectural learning* relates to Popper's broader account and to
Commonplace's chosen system, without claiming to know opaque model internals.
Review does not authorize migration or changes to the definition's scope.

## Problem

The [current definition](./definitions/conjectural-learning.md) requires
formulated theories and criticism whose content improves future use. It also
says that unformulated internal criticism falls outside the term. That wording
can confuse absence of accessible formulation with absence of criticism.
An LLM might formulate and criticize conjectures internally without exposing
them. We cannot infer that it does, or that it does not, from opacity alone.

Allowing conjectures and criticism in traces does not itself erase the
boundary: a trace can contain explicit claims even without an index. Indexed
traces that expose these objects and separate theory documents are equivalent
implementations for this classification. But the question remains whether
accessible formulation defines the learning process or only our chosen way
of implementing and examining it.

## Source distinction and its limit

Popper distinguishes trial and error in general from the scientific practice
of seeking errors through arguments and tests of theories. In *Conjectures
and Refutations*, Chapter 1, pp. 51–52, he contrasts the amoeba with the
scientist. In *Epistemology Without a Knowing Subject*, §4, pp. 346–347,
he distinguishes dispositions from formulated theories and arguments; §9,
pp. 370–371, returns to the amoeba and critical discussion.

Use the local snapshots for these passages:

- [Conjectures and Refutations ingest](../../sources/popper-conjectures-and-refutations.ingest.md), paired snapshot `kb/sources/.snapshots/popper-conjectures-and-refutations.md`.
- [Epistemology Without a Knowing Subject ingest](../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md), paired snapshot `kb/sources/.snapshots/popper-epistemology-without-a-knowing-subject-1968.md`.
- [Popper foundation](./popper-foundation.md) for the existing attribution boundary.

These distinctions do not establish what an LLM does internally. Nor does
Popper's amoeba illustration establish a computational classification of
parameter adaptation. His references to conscious criticism require an
explicit operational interpretation when applied to our system.

The amount of input does not distinguish selection from criticism. The same
failure can lower a variant's score, count against a stated prediction, or
prompt criticism of the test. The distinction concerns the relationship to
the conjecture and the operations performed. Extra context can state that
relationship without proving that the system uses it.

## Alternatives to review

**A. Keep the name for the accessible process.** Define conjectural learning
as learning through formulated theories and criticism available to processes
inside the declared learning system for use, examination, and revision.
State explicitly that this scopes our term; it does not deny latent criticism
or learning elsewhere. Availability to the system need not mean availability
to an outside observer. Retain the causal-use and improvement requirements.

**B. Use the name for the broader critical process.** Allow internally
formulated criticism in principle, with opaque cases unclassified when the
evidence is insufficient. Describe our system in ordinary language as a
continuing system with retained, accessible conjectures and criticism.
The risk is that the broad term adds little discrimination or requires an
unsettled account of what internal formulation means.

**C. Use Popper's broad account without a new general definition.** Describe
the chosen architecture and its experiments directly. The risk is losing a
useful shared term; the benefit is avoiding a disputed universal boundary.
This would reopen the operator's settled naming choice and requires approval.

Before review, the drafting agent's provisional preference was A, provided *available to the
system* can be given a useful meaning without admitting every internal
computation. Reviewers should challenge that premise, not assume it works.

## Constraints and checks

Use all fourteen cases in the [decision record](./definition-decision-record.md).
For each alternative distinguish a scope change from a change in what the
evidence establishes. In particular, case 7 stipulates no formulated theory;
an opaque model with no visible theory is a different, underspecified case.

Also test:

- Popper's amoeba-like adaptation through dispositions.
- An opaque model whose internal use of conjectures and criticism is unknown.
- A trace containing formulated conjectures, criticisms, and testing results
  that actually improve future use, with and without an index.
- A trace of actions and outcomes that contains none of those formulations.
- A specified score-based selection operation, without treating that
  specification as proof about every computation inside a model it invokes.

Keep these settled constraints: learning requires improvement, while attempts
can fail; future use supplies the relevant time span; no episode boundary is
required; addressability of parts and fixed weights are not general membership
conditions; indexing is not mandatory; our architecture is a research choice,
not a prescription. Deterministic LLMs are an assumption of the reconstruction
thought experiment, not evidence of actual internals or automatic replay from
incomplete records. Reconstruction cost and the
[applicability-index example](./indexing-applicability-example.md) remain
practical comparisons, not universal membership tests.

## Review commission

Review independently from the proposal and repository inputs. Return the
strongest objection, a preferred alternative or correction, exact proposed
wording, and the affected boundary cases. Identify source support separately
from engineering choices. Do not edit definitions, sources, or other agents'
work, and do not add retained source quotations. Missing evidence should be
reported as a limit. The parent integrates feedback here; the operator decides
whether to adopt a naming or scope change.

## Independent review result

Three agents reviewed independently on 2026-09-20. They returned feedback
without editing the definitions. The parent integrated their findings below.

| Review | Evidence examined | Main finding |
|---|---|---|
| Popper attribution | Both cited primary snapshots at the passages above, plus the current cases | Popper supports formulation and criticism of content, not a separate computational accessibility test. Internal formulation cannot be ruled out from opacity. |
| Boundary cases | All fourteen cases, five added probes, definitions, and proposal | A and B do not yet name different scopes. A private linguistic formulation can satisfy both. |
| Scope and simplification | Workshop contracts, definitions, companion, and decision record; no independent primary-source recheck | Keep the chosen name and mechanism; adding accessibility either repeats operative use or introduces an unsupported stronger condition. |

The strongest counterexample is a pair of systems with identical visible
action/outcome traces: one privately formulates and criticizes theories,
while the other only selects variants by score. Trace visibility cannot settle
their internal mechanisms. Requiring external visibility would exclude the
first; calling every causally active state an accessible theory would admit
the second.

All three reviewers prefer a minimal correction to A. Two advise dropping
availability as an independent condition; the boundary reviewer offers a
content-level explanation of availability. The parent recommends the smaller
change: keep formulation, criticism, causal use, and improvement as the
conditions, with observer access treated separately as an evidence question.
Requiring continued inspectability would add a retention condition and could
change case 6. No reviewer recommends that addition.

### Proposed wording after review

> Conjectural learning is learning in which a system uses formulated tentative
> theories, criticizes what they say, and improves future use through the
> effects of that criticism. The theory and criticism are expressed in natural
> or formal language within the declared system. An observer's access to them
> is not a condition. Where evidence does not establish formulation, criticism,
> causal use, or improvement, membership remains unestablished. Opacity alone
> establishes neither presence nor absence.

For the research choice, retain the companion's account of a continuing
system with retained theories and criticism, addressable parts, and fixed
models. Those are our choices, with empirical benefits to test. A and B need
not remain separate alternatives if both permit private linguistic
formulation. A genuinely broader alternative admitting unformulated critical
processing would need a further account of what distinguishes it from other
adaptation; these reviews do not supply or require that account.

### Case check

No existing numbered case changes class under the recommended correction.
Inside cases still assume attributable improvement.

| Cases | Classification retained |
|---|---|
| 1, 2, 3 | Inside: indexed objects, whole-theory replacement, and reconstruction from retained criticism remain eligible. |
| 4 | Retained-content comparison; the reconstructor's mechanism is unspecified. |
| 5 | The stipulated score-selection operation is outside; unknown processing inside a model it invokes is not classified by that stipulation. |
| 6 | Conditional on improved future use; later reinspection of the original theory is unnecessary. |
| 7 | Outside because absence of a formulated operative theory is stipulated. An opaque model with no visible theory is not this case. |
| 8 | Inside: formulated criticism can coexist with weight changes. |
| 9, 10 | Outside: criticism or consumption is absent. |
| 11, 12 | Inside: test survival and self-criticism can contribute to learning. |
| 13 | Unestablished by the specified test. |
| 14 | Outside as stipulated; this is not an exclusion of proof-based methods generally. |

The added probes distinguish unknown opaque processing from stipulated
adaptation without formulated criticism. Effective formulated traces qualify
with or without indexes. Action/outcome-only traces do not themselves supply
formulations, but do not classify the process consuming them. Popper's amoeba
illustration supplies no inference about neural implementation.

### Changes to make only after adoption

- Replace the definition's inference that internal criticism necessarily
  leaves nothing formulated with the evidence distinction above. Qualify the
  weight-adaptation example by its stipulated absence of formulation.
- Correct decision-record test 3: the mechanism can depend on internal
  processing even when evidence about it is unavailable. Unknown is a valid
  classification result; opacity is not a negative finding.
- Qualify the tentative-theory draft's claim that weights contain tentative
  theories with nothing formulated. Applying Popper's account of dispositions
  to weights is our interpretation, not a finding about a particular model.
- Keep the companion's conjectures and the practical reconstruction
  comparisons. No new architectural property or term is needed for this fix.

### Testing consequence

Raised by the operator on 2026-09-20: if we cannot claim that a model lacks
internal conjecture and criticism, no model-based comparison arm can be
described as lacking them. This holds under the current definition too, so
the companion was edited without waiting for adoption. Its evidence section
now states that experiments compare specified arrangements of evidence,
criticism, and retention, and that results establish differences between
those arrangements, not the presence or absence of internal criticism. What
is given up is any claim that a particular model-based baseline is not
conjectural learning. Decision-record test 3 is unaffected.

A first draft went further and was withdrawn after review. It claimed that a
fixed model makes unobserved processing common across arms, that unobserved
criticism makes a measured advantage conservative, and that a model proposer
seeing failures turns the comparison into retention against reconstruction.
None follows: different inputs produce different processing, hidden criticism
can misdiagnose, and a possible diagnosis does not fix what an experiment
measures. The draft's information-restricted and non-model baselines are
usable arrangements, but they also change evidence availability or the
proposal mechanism, so they do not isolate criticism's contribution. No
baseline identified so far does.

Second round, same day, pending review: the content conjecture was restated
at the arrangement level. It now compares an arrangement that formulates
criticism and supplies it to later steps with one that selects variants by
score with no formulated reason for a failure, which matches the definition's
black-box boundary example. A comparison arm with the same model proposer and
the same evidence, differing only in whether criticism is formulated and
supplied, identifies the effect of that formulation and supply. It does not
identify the effect of criticism as such. The conjecture's claim is narrowed
accordingly; no boundary case or membership condition changes.

The recommendation preserves the numbered cases but withdraws the current
prose's apparent categorical exclusion of unknown internal criticism. This
record does not adopt the correction or assert membership for any opaque model.
