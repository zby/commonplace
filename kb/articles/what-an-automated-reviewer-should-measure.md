---
description: "Draft article proposing a criterion for automated article review: score an article by how much it improves a declared model reader's answers to independently written questions, per token, with a five-part text reading as an untested proxy"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/information-value-is-observer-relative.md
  - kb/notes/reverse-compression-is-when-llm-output-expands-without-adding.md
  - kb/notes/warranted-reader-update-is-the-objective-of-substantive-writing.md
  - kb/notes/definitions/theory-refinement.md
  - kb/notes/definitions/learning-by-theory-refinement.md
  - kb/notes/definitions/reach-assessment.md
  - kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md
  - kb/notes/verifiable-subroles-before-reviewer-identity.md
  - kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md
  - kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md
---
# What an Automated Reviewer Should Measure

*A proposal: score an article by what it teaches a declared reader, per token*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** Automated review of articles needs a statement of what makes an
article valuable that a machine can apply. We propose one. An article's
value is how much it improves a declared observer's answers about the
domain, per token of the article. The *declared observer* is a named
language model together with a named background corpus, and it stands in
for the readers the article is written for. The questions are written by
someone other than the author, without sight of the article. The
alternative we deny is that an article's value is a property of its text,
which can be judged without saying for whom. Measuring the value costs a
question set and two model runs per article, so we pair the measurement
with a cheaper reading of the text alone: read the article as a proposed
revision of what the field holds, and check whether five things can be
located in it. Whether that reading tracks the measured value is a
conjecture. The measure rates value, not correctness. Nothing here has been
run.

## A case: review automated the question that had a tool

One reported case has the shape this proposal is about. At NeurIPS, an
automated screen was deployed that scored submissions for whether they were
AI-generated, and consequential decisions followed directly from that
verdict: authors "were told to produce version histories or also be
desk-rejected" ([thread on conference volume and AI-detector review](../sources/seeing-numbers-of-50k-submissions-for-iclr-2101135922666365032.ingest.md),
verbatim). At ICLR, a projected jump in submissions prompted the
expectation that "it'll probably need AI review at that scale" (same
source, verbatim). The source leaves open whether the human review layer
scales as well.

Three limits bound what this case supports. The two venues are different,
so nothing here links the NeurIPS deployment to the ICLR projection
causally. The projection is the thread author's own speculation about a
submission deadline that had not yet passed. And every figure in the thread
is relayed secondhand from blogs it does not name, so we use only the
structure of the case and none of its numbers.

That structure is a substitution. Whether a text was machine-written was
not what the review decision needed; the quality of the paper was. The
source does not say why provenance was the question automated. Our
interpretation is that a tool for it existed and produced a verdict on each
submission, while no criterion of article quality was available in a form a
machine could apply. On that interpretation, submission volume is the load
and reviewer capacity is what it strains; neither is the gap. The gap is
that quality had no operational statement, which left substitution as an
available response under load.

Two general arguments predict this. One says that [review automation should
start from narrow subroles whose outputs can be independently
checked](../notes/verifiable-subroles-before-reviewer-identity.md), before
any system is given a reviewer's authority. Here the automated question had
a tool whose outputs the source does not report being checked, and it was
not the question the review needed. The other says that [qualities a
process cannot discriminate tend to be
underselected](../notes/weakly-discriminated-qualities-tend-to-be-underselected.md).
Quality with no operational statement is the limiting case, and the process
selected on what it could discriminate.

What the case establishes is narrow: a review process under load automated
a question a machine could answer in place of the question it needed
answered. The rest of this article proposes a machine-applicable statement
of the needed question. A paper written by a machine that makes a real,
checkable contribution is a good paper, and a hand-written padded one is
not, so the statement says nothing about who wrote the text.

## The criterion

Take the value of an article to be the improvement it produces in a
declared observer's ability to answer about the domain, rather than a
property of the text. This applies to a different subject an objective from
Jürgen Schmidhuber's theory of curiosity and interestingness. He locates
the quantity in the change rather than the state — "The important thing are
the improvements of the compressor, not its compression performance per
se" — and requires that the change be measured against a held-fixed
baseline: "Note that both the old and the new compressor have to be tested
on the same data, namely, the history so far"
([Driven by Compression Progress](../sources/driven-by-compression-progress.ingest.md),
verbatim). His framework also rejects raw novelty as the measure, on the
ground that incompressible noise carries maximal Shannon novelty and allows
no compression progress.

Applying that objective to article review rather than to an agent's
exploration is our step, not his. What carries over is the form: value is
an improvement and not a state, it is measured against a fixed baseline on
the same data, and noise has none. What does not carry over is the measure.
Schmidhuber's quantity is a saving in description length. The quantity here
is an improvement in answer quality on a question set, which stands in for
it and is not shown to track it.

Two changes are needed before the objective carries over.

**The measurement moves off the article's own history.** Schmidhuber's
observer compresses the history it has experienced, which for a reader
would include the article. An article that scored by compressing its own
text would score for internal consistency. So the evaluated material is an
externally supplied question set about the domain, authored without sight
of the article. The article is an intervention on the observer, not part of
what is measured.

**The measurement is charged per token.** Context is the scarce resource
for a language-model reader. Dividing by length prices expansion:
[reverse compression](../notes/reverse-compression-is-when-llm-output-expands-without-adding.md),
more text with no additional extractable structure, spreads the same gain
over more tokens and scores lower. An article with no gain scores zero at
any length.

Three terms name the parts. The *declared observer* is the named model
together with the named background corpus. *Article gain* is the
improvement the declared observer shows on the held-out questions when the
article is in its context. *Gain per token* is article gain divided by the
article's length in tokens.

The resulting criterion is relative by design. Because
[information value is observer-relative](../notes/information-value-is-observer-relative.md),
the same article can be worth a great deal against one background corpus
and nothing against another, and the criterion is undefined until the
observer is declared. Seen this way, *novel* and *significant* name the
same quantity with the observer left undeclared, which may be part of why
they are hard to automate.

## Reading the article as a proposed revision

Measuring article gain costs a question set and two model runs per article.
A reviewer reading one article needs something cheaper, and it has to be a
proxy for article gain rather than a second standard.

The proposal is to read the article as a proposed
[theory refinement](../notes/definitions/theory-refinement.md) of the
observer's background theory. Theory refinement is an established learning
operation: revise an existing explicit theory against cases, seeking to
correct error while preserving useful prior knowledge. We call this the
*refinement reading*. It asks which of five slots are recoverable from the
text, with a locating quotation for each:

| Slot | What the text must make recoverable |
|---|---|
| Addressed part | Which commitment in the declared background the article proposes to change |
| Contradicting cases | The evidence that the addressed part is wrong, incomplete, or wrongly scoped |
| Preserved content | What the article claims still holds after the change |
| Contradictable consequences | What the revised theory forbids, so a later case could contradict it |
| Reach | Which cases beyond the contradicting ones the revision covers |

The slots are not section headings and impose no order. The reading asks
whether each is recoverable, not whether it is announced.

Each slot names a condition that article gain is conjectured to depend on,
which is why the reading is offered as its proxy.

- **Addressed part** says what the gain would be measured against. An
  article that identifies no commitment to change leaves the reader to
  guess which background it revises, so a reviewer working from the text
  cannot say what gain to expect.
- **Contradicting cases** are what make the change more than a preference.
  Without them the article proposes a substitution, and a substitution
  moves the observer's answers with no reason to expect them to improve.
- **Preserved content** is what keeps a gain on one question set from being
  a loss on another. Refinement seeks limited change for this reason. An
  article that discards the background rather than revising it owes the
  larger argument that a replacement owes.
- **Contradictable consequences** are what a held-out question can turn on.
  A theory that forbids nothing gives a held-out question nothing to turn
  on, so the theory is not expected to show gain however true it is.
- **Reach** is what separates compression from patching. A revision that
  covers only its own contradicting cases lengthens the observer's
  background by roughly what it adds, so its gain is bounded by how often
  those cases recur. A revision whose consequences extend to unseen cases
  can also gain on questions nobody wrote it for. This is
  [explanatory reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md).
  Judging whether the claimed reach is genuine is a
  [separate assessment](../notes/definitions/reach-assessment.md), which the
  reading invokes rather than replaces.

The reading is checkable in a weak but useful sense: a model can report
which slots it found and quote where, and a second model can disagree with
the quotation rather than with the verdict. It settles nothing about truth:
an article can fill all five slots with a false theory.

## The instrument

A matched run would tell whether the reading tracks article gain, and would
supply the gain itself where the cost is justified. In a matched run the
same declared observer answers the same questions with the article in
context and without it. The run treats the article as a change to what the
observer retains and measures the change in later behaviour attributable to
it, with the model held fixed. That is the measure of learning in our
research program on [learning by theory refinement with fixed
models](./learning-by-theory-refinement-with-fixed-models.md), applied to
one article.

- **Fixed model.** One model identifier and one decoding configuration
  across both arms. The criterion is defined relative to an observer, so
  changing the model changes the quantity rather than estimating it better.
- **Declared background corpus.** What the observer is assumed already to
  hold, either supplied in context or named as a condition of the run. This
  is the other half of the observer and the baseline the gain is measured
  from.
- **Externally supplied held-out questions.** Authored by someone other
  than the article's author, without sight of the article, about the domain
  rather than about the article. A question set written from the article
  restates it, so the gain that set shows is built in and uninformative.
- **Two arms.** The article in context, and nothing in its place, with
  everything else identical.
- **Gain per token.** The score difference between the arms, divided by the
  article's token count.

The instrument measures one thing. It does not establish truth: a
persuasive false article that moves the observer toward the grader's
expected answers scores well. Grading against later empirical outcomes
relaxes this limit for the outcomes sampled, as the next section describes.
It does not establish transfer: the gain holds for the question set.
Stratifying questions by their distance from the article's contradicting
cases is the obvious route to making the reach slot measurable rather than
read. And the grader is itself a discrimination problem. If a model grades
the answers, [the reported gain is only as good as the grader's
discrimination on each
answer](../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md).

## Declaring the observer for a literature

A named model and a named corpus are easy to write down and hard to justify
for a scientific literature. A literature has no single reader: its readers
differ in background, and they arrive over decades. This section proposes
how a venue could declare an observer anyway. It splits the declaration
into three parts, because each fails in a different way. None of it has
been tried.

**The prior is the literature up to a date.** Schmidhuber's baseline is
"the history so far", quoted above. For a submission, that is the field's
literature as of the submission date, used as the background corpus,
together with a model whose training data ends before that date. Such a
model is an approximation to what the field held on that date, not a record
of it.

**The questions define the user more than the model does.** The user of an
article is whoever later has to decide or predict something in the domain.
Held-out questions drawn from later work stand for that user: the outcomes
of later experiments, replications, and measurements. This choice changes
one limit of the instrument. When answers are graded against later
empirical outcomes, an article that moves the observer toward a false
theory lowers its score on those outcomes. The instrument then bears on
correctness for the outcomes sampled, and only for those.

**Plural readers need a panel, and time needs a date on the questions.** A
venue can declare several observers, such as a specialist, a reader from an
adjacent field, and a practitioner, and report a gain for each in place of
one number. How the venue weighs them is a statement of its scope. The date
of the questions matters as well as the date of the prior: an article can
show low gain on questions its contemporaries would have asked and high
gain on questions asked a decade later.

An observer declared this way makes the instrument retrospective, since
later outcomes do not exist when a submission is reviewed. That is the
reason for pairing it with the refinement reading. Past articles, with the
later outcomes they did or did not help predict, are a set of labelled
cases. The refinement reading would be calibrated against the measured gain
on those cases and then applied to new submissions.

Three problems are open.

- **Leakage.** Later articles restate the article being scored, so
  questions drawn from them can be answered from the restatement. The
  questions have to be about outcomes and not about statements, and an
  outcome that depends on the article's own method is hard to separate from
  a restatement.
- **Contamination.** A model trained after the article appeared holds the
  article in its weights, so the arm without the article is not without it.
  Calibration on past articles is then limited to articles later than the
  model's training data, or to older models.
- **Question authorship carries the judgment of significance.** Whoever
  decides which later outcomes count as questions decides what the field
  values. The declaration makes that judgment explicit and open to audit.
  It does not remove it.

## Limits

- The observer is a language model under bounded context, standing in for
  the article's readers. Whether its gain tracks what a human reader gets
  from the article is untested, and the per-token charge is specific to a
  reader for whom context is the scarce resource.
- Exposition is handled by the observer declaration rather than by the
  criterion. An article teaching something already present in a wider
  corpus still produces gain against a background corpus that lacks it.
  Whether that counts as a good article is then a question about which
  observer a venue declares, and we treat that as the venue's question, not
  the criterion's.
- This is a criterion of value, not of admissibility. Correctness, scope,
  and honesty about limits are separate checks that it neither performs nor
  replaces, apart from what outcome-graded questions cover.
- The refinement reading imposes a shape that not every good article has. A
  survey, a negative result, and a dataset description may fill the slots
  poorly while producing real gain.
- Nothing here has been run. The pairing of the reading with the instrument
  is the part most likely to fail: the reading may be satisfiable by
  articles that produce no gain, and gain may appear for articles that fill
  no slot.

## Open questions

- Who grades the held-out answers, and how is the grader's discrimination
  established before the instrument is trusted? The source for the case
  above reports a screen whose verdicts were acted on with no appeal, and
  reports no error rate for it.
- Does the per-token denominator penalise an article whose length is spent
  on a large preserved-content argument, the work of showing that the
  revision keeps what the background already had right?
- Can the reach slot be turned into a measurement by stratifying the
  question set by distance from the article's contradicting cases, or does
  that only move the reach judgment to the question author?
- Is the refinement reading the right proxy, or one proxy among several?
- How does an article that changes no commitment but reorganises the
  background score? Reorganisation can produce gain by making existing
  structure reachable, which the addressed-part slot does not describe.
- How is the observer's background theory read off its background corpus,
  and do commitments the model holds in its weights count as part of it?
  The addressed-part slot points at a commitment, and the declaration names
  only a model and a text.

## Where to go next

The argument that the value of a text depends on who reads it is developed
in [information value is
observer-relative](../notes/information-value-is-observer-relative.md), and
[warranted reader update is the objective of substantive
writing](../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md)
states the writer's side of the same idea: the intended reader's prior is
the baseline. Article gain is a way to measure that update for a model
reader. The [theory refinement](../notes/definitions/theory-refinement.md)
definition gives the operation the refinement reading borrows, and
[Learning by Theory Refinement with Fixed
Models](./learning-by-theory-refinement-with-fixed-models.md) is the
research program whose measure of learning the instrument applies.
