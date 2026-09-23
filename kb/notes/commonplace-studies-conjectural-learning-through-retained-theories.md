---
description: "Commonplace's RSI research uses interpreted methodology, selective codification, and retained theories; content, addressability, and efficiency remain conjectured benefits"
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

The [definition](./definitions/conjectural-learning.md) states when the term
applies; the [precedents note](./conjectural-learning-has-distinct-precedents.md) supplies the fuller
attribution.

## Research program and development path

Commonplace pursues recursive self-improvement within the broad research
program developed by Schmidhuber. His account starts from programs: "True
RSI is about encoding the initial learning algorithm in a universal
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
The interpreter supplies judgments where the method leaves choices open.
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
with every LLM-era attempt. Second, the start. An improvement to learning
machinery
[pays through the later episodes that reuse it](./an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md),
and [a bootstrap is the running system itself](./a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md),
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
and criticism. Natural language alone does not make a procedure Popperian;
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

The direction does not add a membership condition to conjectural learning.

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
not additional conditions for belonging to the class; see the
[evidence ladder](./a-complete-theory-path-does-not-establish-improved-capacity.md#evidence-forms-a-ladder)
and [experimental contrasts](./an-experiment-identifies-only-the-contrast-it-actually-runs.md).
Failure to detect an effect leaves membership unestablished by that test;
it does not by itself establish absence. Demonstrating the mechanism also
requires a separate assessment of whether the system's capacity for future
action improved before it establishes learning. Observed action provides
evidence of that capacity; lack of exercise alone establishes neither its
presence nor its absence. Failed attempts can occur within a process that
learns; an advantage over alternative approaches is a further claim.

Experiments compare specified arrangements of evidence, criticism, and
retention. Holding the model fixed does not hold its internal processing
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

- [Conjectural learning](./definitions/conjectural-learning.md) — defined-in: the process studied
- [Addressable theory](./definitions/addressable-theory.md) — defined-in: the structural property chosen for this research
- [Retained theories may improve sample efficiency under structured shifts](./retained-theories-may-improve-sample-efficiency.md) — see-also: the separate conjecture about structured shifts
- [An optimal long-run learning strategy invests in its own machinery](./an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md) — grounds: why a working system's stream of episodes makes machinery improvements pay from the first day
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](./a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) — grounds: the bootstrap is the running system, with people supplying functions not yet automated
- [System use selects theory fit without a fixed oracle](./system-use-selects-theory-fit-without-a-fixed-oracle.md) — grounds: use as the selection environment that a system people want to use can sustain
