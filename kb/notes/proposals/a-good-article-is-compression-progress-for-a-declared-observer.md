---
description: "Proposal: judge an article by the measured gain it gives a declared observer per token, and make that criterion readable from the text by treating the article as a proposed theory refinement; unadopted vocabulary"
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
---

# A good article is compression progress for a declared observer

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
  that commitment, what the article keeps, what the revised account forbids,
  and which further cases it covers.

The pairing joins a proxy to an instrument. The refinement reading is the
cheap, text-only proxy for the measured gain. The matched run is the
instrument that measures the gain and would show whether the proxy tracks
it. In a matched run the same declared observer answers the same questions
with the article in context and without it.

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
the refinement reading tracks the measured gain is a conjecture, and it is
the part most likely to fail. The gain measures value, not correctness: a
persuasive false article can score well, and correctness, scope, and honesty
about limits remain separate checks.

## Trigger and cost

Import when the KB first has to rank two candidate articles, or two
revisions of one article, and cannot say what it is ranking them by. Import
also when an open-ended article review needs a criterion whose scoring is
something other than the reviewer's taste. Until then the collection's
present question — can a reader state the claims, support, and limits — is
assumed to do the work. No record yet shows it failing to separate two
articles the KB had to choose between.

The cost is four terms, plus an operational burden that falls on every use:
a declared observer has to be named, and a held-out question set has to
exist and to have been authored without sight of the article. The
refinement reading also imposes a shape that not every good article has.
Adopting it risks penalising exposition, which is the case handled under
Scope.

## The motivating case: automation went where a surface existed

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
needed; quality was. The source does not say why provenance was the
question automated. This note's reading is that a tool for it existed and
produced a per-instance verdict, while no criterion of article quality was
available in a form a machine could apply.

The case is the failure mode that
[review automation should target verifiable subroles before reviewer identity](../verifiable-subroles-before-reviewer-identity.md)
predicts, seen from the side that note does not cover. The note says to
automate narrow subroles that have a checkable surface, and here the only
available surface belonged to a question nobody was asking. On the same
reading it is an instance of
[weakly discriminated qualities tend to be underselected](../weakly-discriminated-qualities-tend-to-be-underselected.md):
quality was weakly discriminated, and the process selected on what it
could discriminate.

On that reading, reviewer capacity is the load and not the gap. The gap
this proposal addresses is that quality had no operational statement, which
left substitution as a move available under load.

## The criterion

Take the value of an article to be the improvement it produces in a bounded
observer's ability to answer about the domain, rather than a property of
the text. This transposes Schmidhuber's objective. He locates the quantity
in the change rather than the state — "The important thing are the
improvements of the compressor, not its compression performance per se" —
and requires that the change be measured against a held-fixed baseline:
"Note that both the old and the new compressor have to be tested on the
same data, namely, the history so far"
([Driven by Compression Progress](../../sources/driven-by-compression-progress.ingest.md),
verbatim). His framework also rejects raw novelty as the measure, on the
ground that incompressible noise carries maximal Shannon novelty and
affords no progress.

Applying that objective to article review rather than to an agent's
exploration is this note's move, not his. What carries over is the form:
value is an improvement and not a state, it is measured against a fixed
baseline on the same data, and noise has none. What does not carry over is
the measure. Schmidhuber's quantity is a saving in description length. The
quantity here is an improvement in answer quality on a question set, which
stands in for it and is not shown to track it.

Two changes are needed to make the transposition work.

**The measurement moves off the article's own history.** Schmidhuber's
observer compresses the history it has experienced, which for a reader
would include the article. An article that scored by compressing its own
text would score for internal consistency. So the evaluated material is an
externally supplied question set about the domain, authored without sight
of the article. The article is an intervention on the observer, not part of
what is measured.

**The measurement is charged per token.** Context is the scarce resource
for the observer this criterion is written for. Dividing by length prices
expansion, so
[reverse compression](../reverse-compression-is-when-llm-output-expands-without-adding.md)
— more text with no additional extractable structure — scores at or below
zero rather than merely failing to score well.

The resulting criterion is deliberately relative. Because
[information value is observer-relative](../information-value-is-observer-relative.md),
the same article can be worth a great deal against one background corpus
and nothing against another, and the criterion has no reading until the
observer is declared. Read this way, *novel* and *significant* name the
same quantity with the baseline left out, which may be part of why they
resist automation.

## The refinement reading makes the criterion readable from the text

Running the instrument below costs a question set and two model runs per
article. A reviewer reading one article needs something cheaper, and it has
to be a proxy for the same quantity rather than a second standard.

The proposal is to read the article as a proposed
[theory refinement](../definitions/theory-refinement.md) of the declared
observer's background: a revision of an existing theory against cases,
seeking to correct error while preserving useful prior knowledge. The
reading asks which of five slots are recoverable from the text, with a
locating quotation for each:

| Slot | What the text must make recoverable |
|---|---|
| Addressed part | Which commitment in the declared background the article proposes to change |
| Contradicting cases | The evidence that the addressed part is wrong, incomplete, or misscoped |
| Preserved content | What the article claims still holds after the change |
| Contradictable consequences | What the revised account forbids, so a later case could contradict it |
| Reach | Which cases beyond the contradicting ones the revision covers |

The slots are not section headings and impose no order. The reading asks
whether each is recoverable, not whether it is announced.

Each slot names a condition the measured gain is conjectured to depend on,
which is why the reading is offered as its proxy rather than as an
independent standard.

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
  An account that forbids nothing gives a held-out question nothing to
  turn on, so the account is not expected to show gain however true it is.
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

A matched run would tell whether the reading tracks the gain, and would
supply the gain itself where the cost is justified. It treats the article
as a change to the observer's retained theory and applies the measure that
[learning by theory refinement](../definitions/learning-by-theory-refinement.md)
uses for what was learned: the change in later behaviour attributable to
the retained change, with the model held fixed.

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
the observer toward the grader's expected answers scores well. It does not
establish transfer: the gain holds for the question set. Stratifying
questions by their distance from the article's own cases is the obvious
route to making the reach slot measurable rather than read. And the grader
is itself a discrimination problem. If a model grades the answers, the
instrument inherits the limit in
[the augmentation-automation boundary is discrimination not accuracy](../the-augmentation-automation-boundary-is-discrimination-not-accuracy.md),
and the reported gain is only as good as the grader's per-instance
discrimination.

## Scope

- The criterion is written for an LLM observer under bounded context, and
  the per-token denominator is what makes it observer-specific in that way.
  It does not claim to capture what a human reader gets from an article.
- Exposition is handled by the observer declaration rather than by the
  criterion. An article teaching something already present in a wider
  corpus still produces gain against a background corpus that lacks it.
  Whether that counts as a good article is then a question about which
  observer a venue declares, which is where the proposal wants it.
- This is a criterion of value, not of admissibility. Correctness, scope,
  and honesty about limits are separate checks that it neither performs nor
  replaces.
- Nothing here has been run. The pairing of the reading with the instrument
  is the part most likely to fail: the reading may be satisfiable by
  articles that produce no gain, and gain may appear for articles that fill
  no slot.

## Open questions

- Who grades the held-out answers, and how is the grader's discrimination
  established before the instrument is trusted? The motivating case is a
  screen acted on before its error rate was known.
- Does the per-token denominator penalise an article whose length is
  carrying a large preserved-content argument — the work of showing that
  the revision keeps what the background already had right?
- Can the reach slot be turned into a measurement by stratifying the
  question set by distance from the article's contradicting cases, or does
  that only relocate the judgment into the question author?
- Is the refinement reading the right proxy, or one proxy among several? A
  survey, a negative result, and a dataset description may fill the slots
  poorly while producing real gain.
- How does an article that changes no commitment but reorganises the
  background score? Reorganisation can produce gain by making existing
  structure reachable, which the addressed-part slot does not describe.

---

Relevant Notes:

- [Warranted reader update is the objective of substantive writing](../warranted-reader-update-is-the-objective-of-substantive-writing.md) — extends: this proposal supplies a measurable form of the reader update that note makes the objective
- [Information value is observer-relative](../information-value-is-observer-relative.md) — grounds: why the criterion has no reading until an observer is declared
- [Reverse compression is when LLM output expands without adding information](../reverse-compression-is-when-llm-output-expands-without-adding.md) — grounds: the failure mode the per-token denominator is meant to price
- [Theory refinement](../definitions/theory-refinement.md) — defined-in: the operation whose anatomy supplies the five slots
- [Learning by theory refinement](../definitions/learning-by-theory-refinement.md) — defined-in: the measure of what was learned that the instrument applies to an article as a change to the retained theory
- [Reach-assessment](../definitions/reach-assessment.md) — defined-in: the judgment the reach slot invokes rather than replaces
- [First-principles reasoning selects for explanatory-reach over adaptive fit](../first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: why a revision covering only its own cases does not compress
- [Review automation should target verifiable subroles before reviewer identity](../verifiable-subroles-before-reviewer-identity.md) — contrasts: the same case from the side where no checkable surface existed for the question being asked
- [Weakly discriminated qualities tend to be underselected](../weakly-discriminated-qualities-tend-to-be-underselected.md) — grounds: why an unoperationalised quality loses to a discriminable proxy under load
- [The augmentation-automation boundary is discrimination not accuracy](../the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — grounds: the limit the instrument inherits from whatever grades its answers
- [Driven by Compression Progress](../../sources/driven-by-compression-progress.ingest.md) — abstracted-from: the compression-progress objective and its same-data comparison, transposed from exploration to article review
- [Thread on conference volume and AI-detector review](../../sources/seeing-numbers-of-50k-submissions-for-iclr-2101135922666365032.ingest.md) — evidenced-by: the reported case of a provenance screen deployed where a quality criterion was missing
