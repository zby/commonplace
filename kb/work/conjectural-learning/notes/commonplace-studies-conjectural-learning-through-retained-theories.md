---
description: "Commonplace's choice to study a continuing system with retained theories, and the content, addressability, and efficiency conjectures that motivate it"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, learning-theory, self-improving-systems]
---

# Commonplace studies conjectural learning through retained theories

Commonplace chooses to study a continuing system that develops, uses, and
criticizes formulated theories. It retains the theories and their testing
record so that what it learns shapes future work. This is our research
choice. Whether it offers advantages over other approaches is an empirical
question.

The attraction is that formulated knowledge can itself become an object of
inquiry. The system can examine what a theory says, challenge its assumptions,
and use the result when developing further theories. This draws on
[Popper's account of formulation and criticism](../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes).
The [definition](../definitions/conjectural-learning.md) states when the term
applies; the [foundation](../popper-foundation.md) supplies the fuller
attribution.

## The continuing system

New work begins with what the system has already learned. A failed test may
prompt revision or replacement. Surviving a serious test adds to the grounds
for relying on a theory as background for further theories, or for spending
less effort repeating tests of the same vulnerability. The theory remains
tentative; its content can stay unchanged while its assessed support and
future use change.

We choose to retain addressable theories: assumptions, scope, and parts can
be inspected and revised individually. Indexed traces that expose conjectures,
criticism, and testing results are an implementation of this retained knowledge,
not a separate comparison. We also hold model weights fixed in
the research program. The theories, testing record, and other retained state
remain parts of the learning system and continue to develop. Fixed weights
rule out parameter updates as the source of improvement; they do not establish
that a particular retained change caused it.

The broader definition also admits reconstruction from retained criticisms
and systems whose weights change. Our choice is one arrangement within it.

## Three conjectures

**Content.** An arrangement that formulates criticism of what a theory says
and supplies it to later steps may yield more learning from a failure than an
arrangement that generates variants and selects them by score, with no
formulated reason for a failure. A correct diagnosis can explain why a claim
failed and direct subsequent search. The intended contrast is the effect of
formulating and supplying criticism; a model proposing variants may also
criticize them unobserved. More elaborate criticism need not supply a better
diagnosis.

**Addressability.** Criticism that identifies a suspect assumption or part
may yield more learning from a failure than criticism that leaves the target
undivided. Identifying a candidate cause can focus investigation and help
preserve useful knowledge. The comparison is with criticism directed at the
theory as a whole, which can still constrain its successor. Both arrangements
can be conjectural learning. The target of criticism is distinct from edit
size: a diagnosis of one part can lead to rewriting the whole theory.
Localization can be mistaken, and a revision may overturn a core assumption.

**Efficiency.** Retaining more of the work of conjecture and criticism may
reduce cost at comparable decision quality. The content conjecture concerns
the contribution of formulated criticism; the efficiency conjecture concerns
the cost of retaining versus reconstructing that work. We compare retaining the theory
and its testing record with two alternatives: rebuilding a theory from
retained criticisms, and rebuilding from records containing only inputs and
outcomes. The first asks what keeping the assembled theory buys;
the second asks what keeping the work of criticism buys. Retention may save
reconstruction, but still requires retrieval, interpretation, and maintenance.
Compare total cost at comparable quality and quality under matched budgets.
Vary record volume or context capacity to test whether bounded context
increases the benefit.
An [applicability-index example](../indexing-applicability-example.md) shows
how an index might save interpretation even when the original call and result
remain in the trace.

## Evidence

Reading the artifacts can establish that criticism was formulated. Showing
that its content affected future use requires causal evidence. Compare
relevant content with altered or mismatched content while controlling its
form. Removing the artifact alone cannot distinguish a content effect from
the effect of supplying text at all. These are ways to investigate membership,
not additional conditions for belonging to the class; see the
[evidence ladder](../../../notes/reflective-theory-refinement-needs-interpretation-and-retention.md#evidence-forms-a-ladder)
and [experimental contrasts](../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md).
Failure to detect an effect leaves membership unestablished by that test;
it does not by itself establish absence. Demonstrating the mechanism also
requires a separate assessment of whether future use improved before it
establishes learning. Failed attempts can occur within a process that learns;
an advantage over alternative approaches is a further claim.

Experiments compare specified arrangements of evidence, criticism, and
retention. Holding the model fixed does not hold its internal processing
fixed when its inputs differ. Unobserved criticism in a comparison arm remains
possible; results establish differences between the tested arrangements, not
the presence or absence of that internal process. Arrangements designed to
rule out unobserved criticism, by withholding failures from the proposer or
by proposing variants without a model, also change the available evidence or
the proposal mechanism.

## Scope

None of these advantages is established. The [paper comparison](../comparison.md)
records relevant findings and their limits; it supplies no result for this
continuing system. The conjectures motivate experiments without making our
choice a prescription for other systems. How much decorrelating the critic
from the proposer helps, and whether retained criticisms can be kept distinct
from a reconstructed theory in practice, remain open questions.

---

Relevant Notes:

- [Conjectural learning](../definitions/conjectural-learning.md) — defined-in: the process studied
- [Addressable theory](../definitions/addressable-theory.md) — defined-in: the structural property chosen for this research
- [Learning by theory refinement may improve sample efficiency under structured shifts](../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md) — see-also: the separate conjecture about structured shifts
