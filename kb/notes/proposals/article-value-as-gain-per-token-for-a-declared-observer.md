---
description: "Proposal: score an article by how much it improves a named model's answers to independently written questions, per token, against a named background corpus; a five-slot text reading is an untested proxy; measures value, not correctness"
type: kb/types/note.md
traits: [has-external-sources]
---

# Article value as gain per token for a declared observer

This is a [theory proposal](./README.md): finished, unadopted, and not a
premise for other notes.

**What adoption would add.** A criterion of article value, four terms that
state it, and one pairing. The criterion: an article's value is how much it
improves a stated model's answers about the domain, per token of the
article. The alternative it denies is that an article's value is a property
of the text, which can be judged without saying for whom.

- *Declared observer*: a named model together with a named background
  corpus. An article's value is measured relative to it.
- *Article gain*: the improvement the declared observer shows on questions
  about the domain when the article is in its context. The questions are
  held out: someone other than the author writes them without seeing the
  article.
- *Gain per token*: article gain divided by the article's length in
  tokens. Context is the observer's scarce resource, so a longer article has
  to gain more to score the same.
- *Refinement reading*: a reading of the article as a proposed revision of
  the observer's background theory. It asks whether five things can be
  located in the text: the commitment the article changes, the cases against
  that commitment, what the article keeps, what the revised theory forbids,
  and which further cases it covers.

The pairing joins a proxy to an instrument. The refinement reading is the
cheap, text-only proxy for article gain. The matched run is the instrument
that measures article gain, from which gain per token follows, and would
show whether the proxy tracks it. In a matched run the same declared
observer answers the same questions with the article in context and without
it.

**What adoption would change.** The [`kb/articles/` contract](../../articles/COLLECTION.md)
states its quality goal as explanatory clarity with technical depth, and
asks reviewers whether a technical reader with no KB context can state the
claims, their support, and their limits. Adoption would add a second
question: for which declared observer, and with what gain? That commits the
collection to declaring an observer whenever it rates an article's value,
and to having held-out questions whenever it reports a gain. Adoption would
also give
[warranted reader update](../warranted-reader-update-is-the-objective-of-substantive-writing.md)
a measurable form for a model reader. That note already makes the intended
reader's prior the baseline but leaves the update unmeasured. The declared
observer's background corpus is that baseline made explicit, and article
gain measures the update.

**What adoption would not establish.** Nothing here has been run. Whether
the refinement reading tracks article gain is a conjecture, and it is the
part most likely to fail. The gain measures value, not correctness: a
persuasive false article can score well, and correctness, scope, and honesty
about limits remain separate checks.

## Trigger and cost

Import when the KB first has to rank two candidate articles, or two versions
of one article, and cannot say what it is ranking them by. Import also when
an open-ended article review needs a criterion whose scoring is something
other than the reviewer's taste. Until then the collection's present
question — can a reader state the claims, support, and limits — is assumed
to do the work. No record yet shows it failing to separate two articles the
KB had to choose between.

The cost is four terms, plus an operational burden that falls on every use:
a declared observer has to be named, and a held-out question set has to
exist and to have been authored without sight of the article. The
refinement reading also imposes a shape that not every good article has.
Adopting it risks penalising exposition, which is the case handled under
Scope.

## The motivating case: automation went where a tool existed

One reported case has the shape this proposal is about. At NeurIPS, an
automated screen was deployed that scored submissions for whether they were
AI-generated, and consequential decisions followed directly from that
verdict: authors "were told to produce version histories or also be
desk-rejected" ([thread on conference volume and AI-detector review](../../sources/seeing-numbers-of-50k-submissions-for-iclr-2101135922666365032.ingest.md),
verbatim). At ICLR, a projected jump in submissions prompted the
expectation that "it'll probably need AI review at that scale" (same
source, verbatim). The source leaves open whether the human review layer
scales as well.

Three limits bound what this case supports. The two venues are different,
so nothing here links the NeurIPS deployment to the ICLR projection
causally. The projection is the thread author's own speculation about a
submission deadline that had not yet passed. And every figure in the thread
is relayed secondhand from blogs it does not name, so only the structural
shape is carried here.

That shape is a substitution. Provenance was not what the review decision
needed; quality was. The source does not say why provenance was the question
automated. This note's interpretation is that a tool for it existed and
produced a verdict on each submission, while no criterion of article quality
was available in a form a machine could apply.

The case is one that [review automation should target verifiable subroles
before reviewer
identity](../verifiable-subroles-before-reviewer-identity.md) warns against,
in a form that note does not address. The note says to automate narrow
subroles whose outputs can be independently checked. Here the automated
question had a tool whose outputs the source does not report being checked,
and it was not the question the review needed. On the same interpretation it
is an instance of [weakly discriminated qualities tend to be
underselected](../weakly-discriminated-qualities-tend-to-be-underselected.md):
quality had no operational statement, which is the limiting case of weak
discrimination, and the process selected on what it could discriminate.

On that interpretation, submission volume is the load and reviewer capacity
is what it strains; neither is the gap. The gap this proposal addresses is
that quality had no operational statement, which left substitution as an
available response under load.

## The criterion

Take the value of an article to be the improvement it produces in a declared
observer's ability to answer about the domain, rather than a property of the
text. This applies Schmidhuber's objective to a different subject. He
locates the quantity in the change rather than the state — "The important
thing are the improvements of the compressor, not its compression
performance per se" — and requires that the change be measured against a
held-fixed baseline: "Note that both the old and the new compressor have to
be tested on the same data, namely, the history so far" ([Driven by
Compression
Progress](../../sources/driven-by-compression-progress.ingest.md),
verbatim). His framework also rejects raw novelty as the measure, on the
ground that incompressible noise carries maximal Shannon novelty and allows
no compression progress.

Applying that objective to article review rather than to an agent's
exploration is this note's move, not his. What carries over is the form:
value is an improvement and not a state, it is measured against a fixed
baseline on the same data, and noise has none. What does not carry over is
the measure. Schmidhuber's quantity is a saving in description length. The
quantity here is an improvement in answer quality on a question set, which
stands in for it and is not shown to track it.

Two changes are needed before the objective carries over.

**The measurement moves off the article's own history.** Schmidhuber's
observer compresses the history it has experienced, which for a reader
would include the article. An article that scored by compressing its own
text would score for internal consistency. So the evaluated material is an
externally supplied question set about the domain, authored without sight
of the article. The article is an intervention on the observer, not part of
what is measured.

**The measurement is charged per token.** Context is the scarce resource for
the observer this criterion is written for. Dividing by length prices
expansion: [reverse
compression](../reverse-compression-is-when-llm-output-expands-without-adding.md),
more text with no additional extractable structure, spreads the same gain
over more tokens and scores lower. An article with no gain scores zero at
any length.

The resulting criterion is deliberately relative. Because [information value
is observer-relative](../information-value-is-observer-relative.md), the
same article can be worth a great deal against one background corpus and
nothing against another, and the criterion is undefined until the observer
is declared. Seen this way, *novel* and *significant* name the same quantity
with the observer left undeclared, which may be part of why they are hard to
automate.

## The refinement reading makes the criterion readable from the text

Running the instrument below costs a question set and two model runs per
article. A reviewer reading one article needs something cheaper, and it has
to be a proxy for article gain rather than a second standard.

The proposal is to read the article as a proposed
[theory refinement](../definitions/theory-refinement.md) of the declared
observer's background: a revision of an existing theory against cases,
seeking to correct error while preserving useful prior knowledge. The
reading asks which of five slots are recoverable from the text, with a
locating quotation for each:

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
  [explanatory-reach](../first-principles-reasoning-selects-for-explanatory-reach-over.md),
  and judging whether the claimed reach is genuine is
  [reach-assessment](../definitions/reach-assessment.md), which the reading
  invokes rather than replaces.

The reading is checkable in a weak but useful sense: a model can report
which slots it found and quote where, and a second model can disagree with
the quotation rather than with the verdict. It settles nothing about truth:
an article can fill all five slots with a false theory.

## The instrument

A matched run would tell whether the reading tracks article gain, and would
supply the gain itself where the cost is justified. It treats the article as
a change to the observer's retained theory and applies the measure that
[learning by theory
refinement](../definitions/learning-by-theory-refinement.md) uses for what
was learned: the change in later behaviour attributable to the retained
change, with the model held fixed.

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

The instrument measures one thing and should not be read as measuring
others. It does not establish truth: a persuasive false article that moves
the observer toward the grader's expected answers scores well. Grading
against later empirical outcomes relaxes this limit for the outcomes
sampled, as the next section describes. It does not establish transfer: the
gain holds for the question set. Stratifying questions by their distance
from the article's contradicting cases is the obvious route to making the
reach slot measurable rather than read. And the grader is itself a
discrimination problem. If a model grades the answers, the instrument
inherits the limit in [the augmentation-automation boundary is
discrimination not
accuracy](../the-augmentation-automation-boundary-is-discrimination-not-accuracy.md),
and the reported gain is only as good as the grader's per-instance
discrimination.

## Declaring the observer for a literature

A named model and a named corpus are easy to write down and hard to justify
for a scientific literature. A literature has no single reader: its readers
differ in background, and they arrive over decades. This section proposes
how a venue could declare an observer anyway. It splits the declaration into
three parts, because each fails in a different way. None of it has been
tried.

**The prior is the literature up to a date.** Schmidhuber's baseline is "the
history so far", quoted above. For a submission, that is the field's
literature as of the submission date, used as the background corpus,
together with a model whose training data ends before that date. Such a
model is an approximation to what the field held on that date, not a record
of it.

**The questions define the user more than the model does.** The user of an
article is whoever later has to decide or predict something in the domain.
Held-out questions drawn from later work stand for that user: the outcomes
of later experiments, replications, and measurements. This choice changes
one limit of the instrument. When answers are graded against later empirical
outcomes, an article that moves the observer toward a false theory lowers
its score on those outcomes. The instrument then bears on correctness for
the outcomes sampled, and only for those.

**Plural readers need a panel, and time needs a date on the questions.** A
venue can declare several observers, such as a specialist, a reader from an
adjacent field, and a practitioner, and report a gain for each in place of
one number. How the venue weighs them is a statement of its scope. The date
of the questions matters as well as the date of the prior: an article can
show low gain on questions its contemporaries would have asked and high gain
on questions asked a decade later.

An observer declared this way makes the instrument retrospective, since
later outcomes do not exist when a submission is reviewed. That is the
reason for the pairing. Past articles, with the later outcomes they did or
did not help predict, are a set of labelled cases. The refinement reading
would be calibrated against the measured gain on those cases and then
applied to new submissions, which is the discipline that [calibrating
semantic gates against labelled
fixtures](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md)
proposes for the KB's own gates.

Three problems are open.

- **Leakage.** Later articles restate the article being scored, so questions
  drawn from them can be answered from the restatement. The questions have
  to be about outcomes and not about statements, and an outcome that depends
  on the article's own method is hard to separate from a restatement.
- **Contamination.** A model trained after the article appeared holds the
  article in its weights, so the arm without the article is not without it.
  Calibration on past articles is then limited to articles later than the
  model's training data, or to older models.
- **Question authorship carries the judgment of significance.** Whoever
  decides which later outcomes count as questions decides what the field
  values. The declaration makes that judgment explicit and open to audit. It
  does not remove it.

## Scope

- The criterion is written for an LLM observer under bounded context, and
  the per-token denominator is what makes it observer-specific in that way.
  It does not claim to capture what a human reader gets from an article.
- Exposition is handled by the observer declaration rather than by the
  criterion. An article teaching something already present in a wider corpus
  still produces gain against a background corpus that lacks it. Whether
  that counts as a good article is then a question about which observer a
  venue declares, and the proposal treats that as the venue's question, not
  the criterion's.
- This is a criterion of value, not of admissibility. Correctness, scope,
  and honesty about limits are separate checks that it neither performs nor
  replaces. Questions graded against later outcomes bear on correctness for
  the outcomes sampled and leave the rest of that check where it was.
- Nothing here has been run. The pairing of the reading with the instrument
  is the part most likely to fail: the reading may be satisfiable by
  articles that produce no gain, and gain may appear for articles that fill
  no slot.

## Open questions

- Who grades the held-out answers, and how is the grader's discrimination
  established before the instrument is trusted? The motivating source
  reports a screen whose verdicts were acted on with no appeal, and reports
  no error rate for it.
- Does the per-token denominator penalise an article whose length is spent
  on a large preserved-content argument — the work of showing that the
  revision keeps what the background already had right?
- Can the reach slot be turned into a measurement by stratifying the
  question set by distance from the article's contradicting cases, or does
  that only move the reach judgment to the question author?
- Is the refinement reading the right proxy, or one proxy among several? A
  survey, a negative result, and a dataset description may fill the slots
  poorly while producing real gain.
- How does an article that changes no commitment but reorganises the
  background score? Reorganisation can produce gain by making existing
  structure reachable, which the addressed-part slot does not describe.
- How is the declared observer's background theory read off its background
  corpus, and do commitments the model holds in its weights count as part
  of it? The addressed-part slot points at a commitment, and the
  declaration names only a model and a text.

---

Relevant Notes:

- [Warranted reader update is the objective of substantive writing](../warranted-reader-update-is-the-objective-of-substantive-writing.md) — extends: this proposal supplies a measurable form of the reader update that note makes the objective
- [Information value is observer-relative](../information-value-is-observer-relative.md) — grounds: why the criterion is undefined until an observer is declared
- [Reverse compression is when LLM output expands without adding information](../reverse-compression-is-when-llm-output-expands-without-adding.md) — grounds: the failure mode the per-token denominator is meant to price
- [Theory refinement](../definitions/theory-refinement.md) — defined-in: the operation the first four slots are drawn from
- [Learning by theory refinement](../definitions/learning-by-theory-refinement.md) — defined-in: the measure of what was learned that the instrument applies to an article as a change to the retained theory
- [Reach-assessment](../definitions/reach-assessment.md) — defined-in: the judgment the reach slot invokes rather than replaces
- [First-principles reasoning selects for explanatory-reach over adaptive fit](../first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: why a revision covering only its contradicting cases does not compress
- [Review automation should target verifiable subroles before reviewer identity](../verifiable-subroles-before-reviewer-identity.md) — contrasts: a case that note warns against, where the automated question had a tool and the needed question had none
- [Weakly discriminated qualities tend to be underselected](../weakly-discriminated-qualities-tend-to-be-underselected.md) — grounds: why a quality with no operational statement is underselected next to a discriminable substitute under load
- [Calibrating semantic gates against labelled fixtures](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) — see-also: the known-case calibration that the refinement reading would need against past articles
- [The augmentation-automation boundary is discrimination not accuracy](../the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — grounds: the limit the instrument inherits from whatever grades its answers
- [Driven by Compression Progress](../../sources/driven-by-compression-progress.ingest.md) — abstracted-from: the compression-progress objective and its same-data comparison, applied to article review instead of exploration
- [Thread on conference volume and AI-detector review](../../sources/seeing-numbers-of-50k-submissions-for-iclr-2101135922666365032.ingest.md) — evidenced-by: the reported case of a provenance screen deployed where a quality criterion was missing
