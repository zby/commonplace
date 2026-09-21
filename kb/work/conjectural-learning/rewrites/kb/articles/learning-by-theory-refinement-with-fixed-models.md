---
description: "Lead article on conjectural learning, Commonplace's retained addressable fixed-model study arrangement, its mechanism conjectures, and the distinct externally assessed theory-builder hypotheses"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/work/conjectural-learning/definitions/conjectural-learning.md
  - kb/work/conjectural-learning/definitions/tentative-theory.md
  - kb/work/conjectural-learning/definitions/addressable-theory.md
  - kb/work/conjectural-learning/notes/commonplace-studies-conjectural-learning-through-retained-theories.md
  - kb/work/conjectural-learning/rewrites/kb/notes/definitions/theory-builder.md
  - kb/work/conjectural-learning/rewrites/kb/notes/definitions/reflective-theory-builder.md
  - kb/notes/definitions/externally-tested-theory-builder.md
  - kb/notes/definitions/autonomous-theory-builder.md
  - kb/work/conjectural-learning/rewrites/kb/notes/reflective-theory-refinement-needs-interpretation-and-retention.md
  - kb/work/conjectural-learning/rewrites/kb/notes/learning-by-theory-refinement-may-improve-sample-efficiency.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md
  - kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
  - kb/notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md
  - kb/notes/a-claim-without-external-assessment-carries-three-obligations.md
  - kb/notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md
---

# Conjectural Learning with Fixed Models

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

A system can learn by formulating theories, using them to make decisions,
and criticizing what they say. It learns when the result of that criticism
improves its capacity for future action. We call this *conjectural learning*,
a specification of Popper's process of conjecture and criticism for a
learning system. Commonplace studies one arrangement: language models
interpret retained, separately revisable theories while their weights stay
fixed. Whether retaining those theories improves learning enough to pay for
their upkeep remains an empirical question. This article explains the
process, the chosen arrangement, and the research hypotheses it motivates.
The arrangement is compared with adapting model weights and with retaining
records or summaries without retaining formulated theories and criticisms.

## A case

Consider a system that maintains a release exporter. The exporter builds a
deployment manifest from a configured list of input files. Documentation
edits do not affect the manifest, so the system checks them for syntax
only. It retains a written account of why, in two parts: an edit needs a
manifest check when an executable consumer reads the edited file, and the
configured input list identifies every file the exporter reads.

Later the exporter starts reading service definitions from named Markdown
files, and those files are added to the configured list. The account already
says what to do: the files now have an executable consumer, so their edits
need manifest checks. This is application of an existing theory to new facts.
It does not by itself show learning from criticism.

Later still, the exporter gains support for included snippets. A snippet
that a configured file includes carries a service definition, but the
configured list does not name the snippet directly. An edit to it passes
its syntax check, and a release ships with an invalid manifest. The system
investigates and formulates a criticism: the configured list identifies the
exporter's entry points, not everything it reads. It revises the second
part of its account to include every file reachable through includes. The
first part, that checks follow executable consumers, survives. The revised
account then guides checks on other snippets that have never caused a failure.

This is a hypothetical example of the mechanism, not an experimental result.
The criticism names why the earlier decision was wrong and changes what the
system would check next. If that change improves its ability to choose
appropriate checks, it has learned. The improvement can exist before another
snippet edit arrives; later decisions provide evidence of it. Revising one
part makes the example easy to inspect, but replacing the whole account
could achieve the same kind of learning.

## Conjecture, criticism, and improved capacity

Popper describes knowledge developing through problems, tentative theories,
attempted error elimination, and further problems: `P1 → TT → EE → P2`.
A [tentative theory](../../../definitions/tentative-theory.md) is a proposed
solution that remains open to criticism however well it has survived.
Tentative does not mean unsupported, and corroboration does not end that
status. Criticism can be an argument, a comparison with a rival, or a test
of a stated consequence; it need not be an empirical experiment.

[Conjectural learning](../../../definitions/conjectural-learning.md) attributes
learning to a system when a formulated theory guides decisions through what
it says and formulated criticism improves the system's capacity for future
action. Merely writing a theory, changing a decision, or recording a passing
test does not establish improvement.
Popper supplies the process and the theory's status; Commonplace supplies
these conditions for attributing learning to a particular system.

When criticism counts against a theory, the system revises or replaces it.
When a theory survives an attempted refutation, the testing result may
instead improve how the system would rely on it or choose further tests.
The text can remain unchanged. Either way, the effect of criticism must
persist for as long as the capacity claim extends. A later loss does not
undo an earlier improvement.

The learning system includes its participating people, services, models,
files, tools, and records. Retaining the assembled theory is one way for
criticism to have a continuing effect. Retaining criticism and reconstructing
a theory when needed is another. Even a theory formulated during reasoning
and then discarded can qualify if criticism improves capacity before disposal
or through a result that persists afterward.

Visibility is a separate question. A model might formulate and criticize a
theory privately. Opaque processing leaves classification open when the
evidence is insufficient; the absence of a visible theory does not prove
that no such process occurred. Nor does weight adaptation determine the
answer. A system can change its weights while formulated theories and
criticism guide its decisions.

## The arrangement Commonplace studies

Commonplace is a framework for knowledge bases operated by agents. Its
[research arrangement](../../../notes/commonplace-studies-conjectural-learning-through-retained-theories.md)
retains theories and testing records across tasks, exposes assumptions and
parts for separate revision, and holds model weights fixed. A theory with
that inspectable structure is
[addressable](../../../definitions/addressable-theory.md). These choices
make particular learning paths available for study; they are not conditions
of conjectural learning in general.

The unit under study is the [whole deployed system](../../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
With weights fixed, retrieval, scheduling, instructions, tools, and validators
can still change what the system can do. Holding weights fixed rules out
parameter updates as the source of an improvement. It does not identify
which retained change caused the improvement or hold the model's processing
fixed across different inputs.

The program pursues recursive self-improvement: improving the machinery that
performs later improvement. This places it within
[Schmidhuber's broad survey of systems that modify their own learning processes](../../../../../sources/recursive-self-improvement-since-1987.ingest.md).
Its chosen development path starts with an incomplete
methodology expressed in language. Models interpret it, experience exposes
its limits, and criticism guides changes to the methodology and the machinery
that applies it. Popper's process organizes that work; the research question
is whether the resulting system becomes better at further learning.

Natural language lets a methodological conjecture be tried before every
operation has been formalized. It also leaves interpretation to the model.
A claimed consequence or a diagnosis can depend on a mistaken reading. As
a part becomes sufficiently clear and useful, the system can
[codify it](../../../../../notes/definitions/codification.md) in a schema,
validator, test, or program. The specified consequences then become
mechanically checkable. Whether the encoding captures the intended claim
and the test measures the right property remains open to criticism.
When a new theory needs a check the system lacks, [building that
check](../../../../../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md)
is part of the work.

## Three conjectures about the mechanism

The [research companion](../../../notes/commonplace-studies-conjectural-learning-through-retained-theories.md#three-conjectures)
states three proposed benefits. The exporter example shows their possible
mechanisms without establishing their advantages.

**Content.** Formulating and supplying a criticism of what a theory says may
produce more learning from a failure than generating variants and selecting
them by score without a supplied reason for failure. “The configured list
omits included files” directs investigation differently from “this release
failed.” A correct diagnosis could save search; an elaborate wrong one
could waste it. A model generating variants may still criticize them
privately, so the comparison concerns the arrangements actually supplied,
not a guarantee about hidden processing.

**Addressability.** Criticism that identifies a suspect assumption or part
may produce more learning than criticism directed at an undivided theory.
In the example, the account of the input list can change while the consumer
condition remains available. Identifying a part can focus investigation and
help preserve useful knowledge. It can also locate the fault incorrectly.
The target of criticism is distinct from edit size: diagnosing one part can
justify rewriting the whole theory, and criticism can overturn a core
assumption.

**Efficiency.** Keeping more of the work of conjecture and criticism may
reduce cost at comparable decision quality. There are two reconstruction
comparisons. Rebuilding from retained formulated criticisms asks what keeping
the assembled theory buys. Rebuilding from records containing only inputs
and outcomes asks what retaining the work of criticism buys. For the exporter,
the latter system must recover the significance of the snippet failure;
the former already has the criticism about entry points and includes.

These distinctions concern retained content. A trace that preserves the
theory, criticism, and testing result can implement the same retained knowledge
as separate theory documents. Conversely, records containing only inputs and
outcomes do not determine what their reconstructor will formulate. The
comparison must give each arrangement competent retrieval and reconstruction
within declared resources.

## Retention has costs

An assembled theory may save repeated interpretation, but it also requires
retrieval, applicability checks, revision, validation, and maintenance.
A false abstraction can misdirect many decisions, and a correct theory that
retrieval misses supplies no help. A local textual edit can have broad
consequences through shared assumptions, so revisions and rollbacks require
checking what depends on the changed part.

Records remain useful even when theories are retained. They can expose an
omitted detail or allow a mistaken abstraction to be reconstructed, and
[a later model can re-examine the derivation](../../../../../notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md).
Bounded context creates a need to select or summarize evidence; it does not
by itself select theories as the best retained form. Search, summaries,
periodic reconstruction, and retained theories can be combined.

The chosen arrangement [makes new knowledge available without another
weight-training cycle](../../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md)
and gives readers identifiable assumptions to inspect.
Whether those properties improve continual learning or make rollback useful
depends on whether the system [governs which behavior-changing writes become
operative](../../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md).
Admission, coordination, and credit
assignment remain work: a readable explanation does not guarantee faithful
use, and a readable dependency is not necessarily an independent one.
A learner confined to a
[fixed decomposition inherits that decomposition's mistakes](../../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

A separate [sample-efficiency conjecture](../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md)
asks whether a useful theory reduces target observations after a shift that
preserves the structure it describes. The exporter case suggests why one
criticism might change many checking decisions. That benefit is separate
from whether a selector can choose useful theories by judging how far their
explanations hold beyond the observed cases. Both are separate from total cost. Construction, prior
evidence, retrieval, validation, maintenance, and mistakes must be counted
symmetrically across the compared systems.

Rich Sutton's Bitter Lesson says that general methods which scale with
computation outperform methods built from human knowledge. Written theories
receive no exemption from that pressure. The
relevant distinction is [how structure is produced and revised](../../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md),
not simply whether it is text or weights. Computational search could produce
the retained structure, making it a learned product. Search and assessment
over artifacts might nevertheless scale poorly, and a model could reconstruct
the same useful content more cheaply. The retained arrangement has to earn
its place against those alternatives.

## Requirements and responsibility

In the exporter case, the account of what the input list means is a
descriptive claim. Producing a valid manifest is a requirement. When the
system fails, it must decide whether its account of the exporter is wrong,
whether the implementation violates the requirement, or whether its checking
procedure failed. Changing a descriptive assumption and changing the product
are different responses.

Replacing or weakening a failed test requires grounds to doubt its
measurement or relevance. The failure alone supplies no such grounds.

An externally supplied requirement does not become the system's to weaken
because weakening it would make a failure disappear. Tenant isolation, for
example, changes only through whoever has authority to renegotiate it. The
same authority boundary applies when the system rewrites its own evaluators.
Its ability to modify a test does not establish that the revised test judges
the required outcome correctly.

For the continuing system responsible for this work, we use the narrower
term [theory builder](../notes/definitions/theory-builder.md). A builder
develops and revises addressable tentative theories across demands and
consequences. It includes its theories, records, machinery, and everyone
performing an internal theory-building role. A person interpreting a theory,
choosing a diagnosis, selecting a revision, or repairing the machinery is
inside that boundary. A person supplying tasks, evidence, requirements, or
outcome judgments is outside in that role.

Continuing responsibility and lineage identify the builder. No particular
theory or procedure has to survive. A successor produced through the
builder's process belongs to that lineage; a change installed from outside
is recorded as an intervention. A builder can reconstruct its theories or
attempt revisions unsuccessfully. It need not have learned successfully,
and a conjectural learner need not meet this narrower builder definition.

## Reflection and autonomy

A [reflective builder](../notes/definitions/reflective-theory-builder.md)
uses a theory of its own machinery with a two-way causal connection:
machinery changes update that theory, and theory revisions can change the
machinery. In the exporter example, this would involve an account of how
the system chooses checks, which a missed check can challenge. Revising that
account guides a change to the check selector, and the installed change is
reflected back into the account. Self-description alone does not supply
this connection.

A builder is [autonomous](../../../../../notes/definitions/autonomous-theory-builder.md)
when computation performs every internal theory-building role within the
declared boundary and horizon. Users can still supply tasks and judge
products. Reflection and autonomy are independent: people may perform a
reflective diagnosis, while a computational builder may revise its artifacts
without a causally connected theory of its own machinery. Neither condition
establishes successful learning or reliability.

## What would test it

A theory cited in a decision record may have been decorative. A changed
procedure may work for reasons other than the proposed theory. The
[evidence account](../notes/reflective-theory-refinement-needs-interpretation-and-retention.md)
therefore separates theory mediation, empirical contact, response to
criticism, and recurrent mediation: respectively, the theory affects a
decision, an outcome bears on it, formulated criticism changes its content or
role, and that result affects later operation. Claiming recurrence requires evidence
that these steps belong to the same causal path. Even a complete path needs
separate evidence that capacity improved. Conversely, capacity can improve
before another opportunity to exercise it arises.

Changing or withholding the relevant content can strengthen causal
attribution, but the result remains a comparison of the tested arrangements.
A change in task mix, computation, human assistance, or model variation can
otherwise explain a gain. Fixed weights alone remove none of those
alternatives.

The program's three whole-system hypotheses were adopted on 2026-09-17.
They concern performance under external assessment and remain distinct from
the content, addressability, and efficiency conjectures above. The
[testing supplement](./testing-the-theory-refinement-program.md#the-hypotheses)
retains their full wording; the following summarizes them. The public models
in the sufficiency hypothesis are those available as of that adoption date,
with model versions declared and weights held fixed during assessment.

- **Sufficiency.** A methodology expressed in prose and code enables an
  autonomous builder to develop, retain, and use theories and procedures
  across declared practical areas, meeting a reliability target under a
  budget and external assessment. Needing a person in an internal role or
  a new learning method for each area, or failing the target, refutes the
  assessed claim.
- **Comparison.** Under matched demands and resources, that methodology
  produces useful capability gains over the frozen seed and a baseline
  searching raw records without the learned methodology. Its downstream
  reliability is comparable to a human-staffed builder within a margin set
  before assessment. Controls doing as well at comparable cost, or a human
  builder exceeding that margin, refute the assessed claim.
- **Reflection.** Machinery changes passing through a causally connected
  self-theory produce extensions that a matched builder without one does
  not acquire under the same demands, budget, and external assessment.
  Equal extensions in the control, or records showing that the changes did
  not pass through the self-theory, refute the assessed claim. An extension
  here is a retained machinery change that demonstrates capability beyond
  the seed on a stated demand and budget.

Better downstream outcomes alone do not test the reflection hypothesis. That
requires records of a reflective episode and a matched builder that retains
content without a self-theory.

These hypotheses require more than a successful component. Better whole-system
performance does not isolate the contribution of criticism or addressability;
a component advantage does not establish the whole system's reliability.
The raw-record baseline in the comparative hypothesis remains the adopted
whole-program control. The two reconstruction comparisons above refine the
mechanism questions without silently replacing that hypothesis.

## Assessment from outside the builder

An [externally tested builder](../../../../../notes/definitions/externally-tested-theory-builder.md)
receives three things from outside its declared boundary: evidence of failed
outcomes, acceptance requirements with an authority for changing them, and
outcome judgments independent of its own evaluators. “Independent” describes
the roles; it does not guarantee correct measurement.

The arrangement allows outcome comparisons before every internal theory's
warrant has been settled. A failed release establishes a product failure,
not whether the error lay in interpretation, theory, retrieval, or a skipped
check. A claim about that cause needs its own evidence. Where a broader
claim lacks external assessment, [the builder must supply its own grounds](../../../../../notes/a-claim-without-external-assessment-carries-three-obligations.md)
for what counts as criticism and support, what licenses an objective change,
and why a proposed cause is responsible. Finite evaluations support claims
within their declared tasks, evidence, budgets, and horizons.

## The first arrangement

The proposed first run has Commonplace produce a knowledge base and its
supporting software for a consuming project. Agents in that project use the
knowledge on tasks judged by the project's own assessors. Failures can lead
Commonplace to revise the delivered product and, when diagnosis implicates
its methods, its own machinery. The consuming project's acceptance
requirements remain external.

Commonplace currently includes people in internal roles. Moving those roles
to computation is the [bootstrap supplement's](../../../../../articles/bootstrapping-an-autonomous-theory-builder.md)
subject. The proposed consuming-project run has not been performed, and the
whole-program hypotheses remain untested by it. Existing human-inclusive
[Commonplace evidence](../../../../../notes/evidence/commonplace-as-a-reflective-system.md)
establishes narrower paths within stated criteria.

The [software-house supplement](../../../../../articles/an-automated-software-house-as-a-second-test-of-theory-refinement.md)
considers a different product and evidence interface: an automated software
house whose retained program theory guides software maintenance. Visible
software failures provide a different testing opportunity; results there
would support a different bounded claim. It remains a companion arrangement,
not the replacement for the knowledge-delivery test.

## Open questions

The immediate uncertainties are whether current models interpret prose
reliably enough for diagnosis, whether particular parts can be blamed without
misleading later revision, and whether a sequence of locally supported
changes preserves a warranted lineage. The support needed for experimental
use, routine reliance, and codification may differ. Delayed failures also
make credit assignment hard: the theory, retrieval, evaluator, or skipped
check may each be responsible.

The economic question is whether retaining theories beats reconstructing
them from criticism or from inputs and outcomes at comparable quality, and
whether the full arrangement compares well with adapting weights. None of
these choices follows from defining the learning process.

## Where to go next

The [definition](../../../definitions/conjectural-learning.md) states the
learning conditions and boundary cases. The
[research companion](../../../notes/commonplace-studies-conjectural-learning-through-retained-theories.md)
separates them from Commonplace's choices. The
[testing supplement](./testing-the-theory-refinement-program.md)
develops the independently adopted hypotheses, assessment interface, and
proposed comparisons. [Nearest existing constructions](../../../../../articles/nearest-existing-constructions-to-a-witness-house.md)
reviews precedents for the companion software-house arrangement; evidence
for its parts does not establish the complete proposed system.
