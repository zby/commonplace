---
description: "Commonplace builds a system meeting the theory-builder conditions and tests whether it learns; criticism of content is compared against trial and error, and fine-grained addressability and high persistence against builders with less of each"
type: note
traits: [title-as-claim, has-external-sources]
tags: [foundations, learning-theory, self-improving-systems]
---

# Commonplace builds a theory builder and tests whether it learns

Commonplace builds a [theory builder](./definitions/theory-builder.md): a
continuing system whose theories are stated in localized units, guide what it
does through what they say, are criticized for what they say, and are
revised through iteration, where the result of criticism shapes the next
round. The definition has no
success condition. Whether the system learns, in the sense of improving its
capacity for future action
([Simon's criterion](./learning-is-not-only-about-generality.md)), is the
hypothesis under test. Membership does not establish it.

Beyond the four conditions, Commonplace builds for the high end of two
graded properties, addressability and persistence, and holds model weights
fixed as a study condition. Whether these commitments pay is an empirical
question, stated as three conjectures below. One asks whether criticism, the
core of membership, pays against trial and error. The other two ask whether
each high end pays against a builder with less of it. The
[precedents note](./theory-building-has-distinct-precedents.md) supplies the
fuller attribution.

## Research program and development path

The first research claim is that an autonomous theory builder learns, which
it could do with a fixed method. Commonplace pursues it alongside a practical
goal, an LLM wiki that people use for their own work, and the two reinforce
each other: learning is what makes the wiki's memory worth keeping, and real
use supplies the problems and criticism the builder learns from, as the
second difference below explains.

Commonplace's approach to building a theory builder is
reflective from the start: the builder criticizes and revises its own stated
method, and people perform many of its operations until they move to
computation. The approach rests on the return to investing in the method:
[an improvement to the learning machinery is reused by every later episode](./an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md),
so over a long horizon it can pay more than immediate learning. That return
requires method changes to compound, making later improvement better, which
is the claim of recursive self-improvement. Reflection is not sufficient for
it, and it is not necessary for recursive self-improvement in general:
Schmidhuber's realizations select self-modifications by reward rather than
by criticizing a stated method. Commonplace takes the reflective route, where
compounding comes through criticism of the stated method.

The program sits within the broad research program on recursive
self-improvement developed by Schmidhuber. His account starts from programs:
"True RSI is about encoding the initial learning algorithm in a universal
programming language", whose instructions can modify that code itself
([RSI retrospective](../sources/recursive-self-improvement-since-1987.ingest.md#quotes)).
His example of such a language is a "recurrent neural network or RNN". On
this reading a network's weights are a program, and his neural realizations
let a network rewrite its own weights and so its own learning algorithm.

We extend the same reading one step further: a natural-language prompt that
an LLM interprets is also a program. The fixed-weight model and harness are
its interpreter, and the prompt can describe how to revise prompts,
including itself. Unlike code, such a program has no formal semantics; the
interpreter's judgments fix what it does where the text leaves choices open.
This is our interpretation, not Schmidhuber's claim. Our chosen realization
therefore uses natural language as the retained, revisable carrier of
knowledge and learning procedures, with LLMs supplying interpretation and
criticism. Retained theories can guide diagnosis, test
selection, and procedure revision; the research objective includes making
subsequent improvement work more productive.

We start with an incomplete, criticizable account of how to learn and use it
through interpretation. The LLM and harness supply executable machinery;
the methodology need not specify every operation before it can be tried.
This reduces the up-front specification needed to expose a methodological
conjecture to failure. Whether the resulting judgments support useful
improvement remains an empirical question.

Two differences from earlier realizations may explain why this one could get
further; both are conjectures, not results. First, the seed. Schmidhuber's
seed improver must contain, in executable form, all the competence the first
improvement needs, and the general routes to that competence, program
enumeration and proof search, are expensive; the realizations that ran stayed
within bounded domains. With an LLM the seed is a delta over pretrained
competence: it directs what it need not encode. This difference is shared
with every LLM-era attempt. Second, the start. An improvement to the method pays
through the later episodes that reuse it, and
[a bootstrap is the running system itself](./a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md),
so starting from a working system supplies that stream from the first day,
with people supplying the functions not yet automated. Any program could in
principle close its loop with human judgment. Sustaining that requires a
system people want to use, so that the judgments are part of work they would
do anyway; Commonplace has this, because its operators build and use the
knowledge base for their own work, and
[that use is the initial selection environment](./system-use-selects-theory-fit-without-a-fixed-oracle.md)
where no fixed oracle exists. The price is warrant. A proof or a reward-rate
guarantee certified each accepted change in the earlier realizations. Here
the interpreter's judgments are hidden, and human contributions must be
recorded rather than credited to computation.

Popper's epistemology organizes this development process: treat the
methodology's claims as tentative theories, criticize their content, test
their consequences, and let the resulting problems guide further work
([formulation and criticism](../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes)).
This follows from our choice to develop the methodology through conjecture
and criticism, which makes the method part of what the builder criticizes
(the [reflective qualifier](./definitions/theory-builder.md#qualifiers)).
Natural language alone does not make a procedure Popperian;
an instruction, a theory about its effects, and a criticism have different
roles even when they share one artifact.

Codify parts when their intended meaning and operation become sufficiently
clear and the commitment is useful. [Codification](./definitions/codification.md)
assigns consequences through a symbolic consumer; it does not merely make
prose more precise. Other parts can remain interpreted and criticizable.
Codification can therefore follow learning, part by part, without making the
underlying theory true or exempt from criticism. Whether it preserves useful
behavior while reducing cost or error is a separate question from whether
the interpreted methodology improves learning.

This direction does not add a condition to the definition. Interpreted
methodology and selective codification are how Commonplace realizes a theory
builder, not what makes a system one.

## The continuing system

New work begins with what the system retained from earlier problems.
Condition 4 of the definition, iteration, requires only that the result of
criticism shape the next round, which can happen within one run.
[Persistence](./definitions/theory-builder.md#persistence) is graded: within
one reasoning episode, across the rounds of one run, across runs, or across
problems and sessions. We choose the high end: a library of retained theories
that later work on other questions takes up. A failed test may
prompt revision or replacement. Surviving a serious test adds to the grounds
for relying on a theory as background for further theories, or for spending
less effort repeating tests of the same vulnerability. The theory remains
tentative; its content can stay unchanged while its assessed support and
future use change.

The definition requires only that some unit carry content, even if that unit
is the whole theory. We choose the high end of
[addressability](./definitions/theory-builder.md#addressability): assumptions,
scope, and parts can be inspected and revised individually. Indexed traces
that expose conjectures, criticism, and testing results are an implementation
of this retained knowledge, not a separate comparison. We also hold model
weights fixed in the research program. The theories, testing record, and other
retained state remain parts of the builder and continue to develop. Fixed
weights rule out parameter updates as the source of improvement; they do not
establish that a particular retained change caused it.

The definition also admits theories criticized and replaced whole, theories
rebuilt from retained criticism, builders whose results do not outlast a run,
and builders whose weights change. Our choice is one arrangement within it.

## Three conjectures

**Criticism of content** (membership core). An arrangement that formulates
criticism of what a theory says and supplies it to later steps may yield more learning from a failure than an
arrangement that generates variants and selects them by score, with no
formulated reason for a failure. The second arrangement is trial and error,
outside the definition (condition 3), so this conjecture asks whether the
criticism condition pays. A correct diagnosis can explain why a claim
failed and direct subsequent search. The intended contrast is the effect of
formulating and supplying criticism; a model proposing variants may also
criticize them unobserved. More elaborate criticism need not supply a better
diagnosis.

**Addressability** (graded). Criticism that identifies a suspect assumption or
part may yield more learning from a failure than criticism that leaves the target
undivided. Identifying a candidate cause can focus investigation and help
preserve useful knowledge. The comparison is with a builder whose criticism is directed at the
theory as a whole, which can still constrain its successor. Both arrangements
are theory builders: a theory with no stated parts that is criticized and
replaced whole meets the definition at its minimum, and it is the baseline for
this conjecture
([checks, case 26](./definitions/theory-builder-checks.md)). The target of criticism is distinct from edit
size: a diagnosis of one part can lead to rewriting the whole theory.
Localization can be mistaken, and a revision may overturn a core assumption.

**Persistence** (graded). Keeping more of the work of conjecture and
criticism, for longer and across more problems, may reduce cost at comparable
decision quality. The criticism conjecture concerns the contribution of
formulated criticism; the persistence conjecture concerns the cost of
retaining versus reconstructing that work. We compare retaining the theory
and its testing record across problems with builders whose results persist
less, and with two reconstruction alternatives: rebuilding a theory from
retained criticisms, and rebuilding from records containing only inputs and
outcomes. The first alternative is still a theory builder, so it asks what
keeping the assembled theory buys. The second carries nothing that criticism
produced across runs; it is the baseline for the persistence conjecture
([checks, case 4](./definitions/theory-builder-checks.md)) and asks what
keeping the work of criticism buys. A reconstructor that states, criticizes,
and revises within a run is still a builder at that run's grade, and it may
learn in the ordinary sense. Retention may save
reconstruction, but still requires retrieval, interpretation, and maintenance.
Compare total cost at comparable quality and quality under matched budgets.
Vary record volume or context capacity to test whether bounded context
increases the benefit.
For example, an earlier result may say that retrying a timed-out write
can duplicate an operation already committed. A later task about duplicate
charges after reconnecting may not name that call or reuse its wording.
An index retaining “applies when completion is uncertain” can save
reconstructing the applicability condition. Deciding whether the current
case meets it still needs interpretation or suitable structured inputs.
If the trace already exposes that condition, the index may save only
lookup. This is an illustration; any cost comparison must count creating,
maintaining, and consuming the index, and give reconstruction competent
access to the records.

## Evidence

Reading the artifacts can establish that criticism was formulated. Showing
that its content affected later action requires causal evidence. Compare
relevant content with altered or mismatched content while controlling its
form. Removing the artifact alone cannot distinguish a content effect from
the effect of supplying text at all. These are ways to investigate membership,
not additional conditions of the definition; see the
[evidence ladder](./a-complete-theory-path-does-not-establish-improved-capacity.md#evidence-forms-a-ladder)
and [experimental contrasts](./an-experiment-identifies-only-the-contrast-it-actually-runs.md).
Failure to detect an effect leaves membership unestablished by that test;
it does not by itself establish absence. Demonstrating the mechanism establishes
membership at most. Learning needs a separate assessment of whether the
system's capacity for future action improved. Observed action provides
evidence of that capacity; lack of exercise alone establishes neither its
presence nor its absence. Failed attempts can occur within a process that
learns; an advantage over alternative approaches is a further claim.

Experiments compare specified arrangements of evidence, criticism, and
persistence. Holding the model fixed does not hold its internal processing
fixed when its inputs differ. Unobserved criticism in a comparison arm remains
possible; results establish differences between the tested arrangements, not
the presence or absence of that internal process. Arrangements designed to
rule out unobserved criticism, by withholding failures from the proposer or
by proposing variants without a model, also change the available evidence or
the proposal mechanism.

## Scope

None of these advantages is established. The conjectures motivate experiments without making our
choice a prescription for other systems. How much decorrelating the critic
from the proposer helps, and whether retained criticisms can be kept distinct
from a reconstructed theory in practice, remain open questions.

---

Relevant Notes:

- [Theory builder](./definitions/theory-builder.md) — defined-in: the kind of system built and studied, and its four conditions
- [Theory-builder checks](./definitions/theory-builder-checks.md) — grounds: the baseline cases the addressability and persistence conjectures compare against
- [Addressable theory](./definitions/addressable-theory.md) — defined-in: the graded property whose high end is chosen for this research
- [Learning is not only about generality](./learning-is-not-only-about-generality.md) — grounds: the sense of learning the program tests
- [Retained theories may improve sample efficiency under structured shifts](./retained-theories-may-improve-sample-efficiency.md) — see-also: the separate conjecture about structured shifts
- [An optimal long-run learning strategy invests in its own machinery](./an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md) — grounds: why a working system's stream of episodes makes machinery improvements pay from the first day
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](./a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) — grounds: the bootstrap is the running system, with people supplying functions not yet automated
- [System use selects theory fit without a fixed oracle](./system-use-selects-theory-fit-without-a-fixed-oracle.md) — grounds: use as the selection environment that a system people want to use can sustain
