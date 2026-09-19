---
description: "Draft article proposing observer-relative compression progress as the primary Schmidhuber-derived measure for automated review, with task gain as a separate transfer test, explicit costs, and a five-part reading as a candidate proxy for theory revisions"
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
  - kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md
---

# What an Automated Reviewer Should Measure

*A proposal: measure whether an article improves a declared reader's compression of a domain, then test whether the improvement transfers*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

Suppose an article explains why a familiar experimental method fails under
certain conditions. Before reading it, a reader needs a collection of
separate exceptions to account for the observed results. After reading it,
one revised model explains both the successes and the failures and predicts
what will happen in further experiments. That change seems like something a
reviewer should care about. Can we measure it?

Here is a proposal for automated review. Let a language model stand in for
the intended reader. Give it a fixed body of observations from the article's
domain, first without the article and then with it. Measure whether the
article lets the reader predict or encode those observations more compactly.
Call the difference *article compression progress*.

This is the measure suggested most directly by Jürgen Schmidhuber's account
of interestingness as improvement in an observer's compressor. It is not yet
a complete measure of article value. Compression of known observations may
fail to transfer, and a compact false account can fit a selected corpus.
The reviewer should therefore report three things separately:

- **Compression progress:** does the article give the observer a better
  predictive model of a fixed body of domain observations?
- **Transfer or task gain:** does that changed model improve performance on
  further cases or tasks?
- **Cost:** how much context, computation, and evaluation does the article
  require?

Correctness and warrant remain separate checks. Nothing here has been run;
the measurements and the cheaper reading proposed later are candidates to
be tested.

## Value for whom, and over what domain?

An expert and a newcomer can extract different structure from the same
article. Even readers with the same background may care about different
parts of a domain. A useful measure therefore has to declare both the
observer and the material over which improvement is assessed.

- **The observer:** a named language model, instructions, tools, and
  background corpus. Together they stand in for the intended reader.
- **The domain evidence:** a fixed collection of observations, cases, or
  records whose structure the article is supposed to help the observer
  capture.
- **The uses:** the later predictions, decisions, diagnoses, or other tasks
  on which transfer may be tested.

Because [information value is
observer-relative](../notes/information-value-is-observer-relative.md), an
article can produce substantial compression progress against one background
and none against another. A tutorial can reorganize a newcomer's knowledge
while adding nothing for a specialist.

The evidence declaration matters just as much. A narrow collection can make
a parochial regularity look powerful. A corpus containing only familiar
successes may hide an article's treatment of failures. The measurement does
not eliminate judgments about scope; it makes the chosen scope inspectable.

## Compression progress

Schmidhuber's proposal locates interestingness in improvement, not in an
object's absolute compressibility. In his formulation, old and new
compressors are tested on the same history. The retained source puts the
point directly: "The important thing are the improvements of the compressor,
not its compression performance per se"
([Driven by Compression Progress](../sources/driven-by-compression-progress.ingest.md),
verbatim).

The analogue for article review is:

> Article compression progress = predictive description length without the
> article − predictive description length with the article.

Both arms use the same observer and the same domain evidence. The article is
the intervention. If it helps the observer assign higher probability to the
observations, the observations require fewer bits under the corresponding
predictive code.

This is closer to Schmidhuber's measure than replacing description length
with answer quality. The article itself is not what should be compressed.
The article is candidate learned structure; the relevant question is whether
it compresses the domain for this observer.

A practical experiment could present a sequence of observations and record
the probability the model assigns to each next observation. Summed negative
log probabilities give predictive description length. Where the model
interface does not expose suitable probabilities, scored predictions can be
used as an approximation, but then the result is no longer a literal
compression measure and should not be named as one.

The test distinguishes an article that supplies a reusable regularity from
one that merely expands the context. But compression progress on a chosen
corpus is not enough. An article may restate outcomes contained in its text,
or fit the selected observations with a regularity that fails elsewhere.
Compression of the evidence already discussed by the article measures
assimilation of that evidence. Claims about reach require a further test.

## Transfer and task gain

The downstream question is whether the compacted understanding changes what
the observer can do:

> Task gain = task score with the article − task score without the article.

This is not the operational definition of compression progress. It is a
separate validation criterion. The empirical conjecture is that compression
progress produced by a good explanatory article predicts gain on relevant
later tasks.

An article that contains answers to a benchmark can produce task gain
without much reusable compression. Conversely, an article that reveals a
deep regularity may compress a domain before anyone has formulated all the
tasks on which that regularity will matter. Measuring both lets us study the
relationship instead of assuming that one substitutes for the other.

Earlier versions of this proposal required questions written without sight
of the article. That is too strong as a general procedure. For a novel
article, its contribution may be what makes meaningful questions visible.
A supposedly independent question writer may produce only familiar tasks
and systematically miss the new distinction the article introduces.

There are three different designs, and their evidential force should not be
confused:

1. **An existing independent benchmark** can measure gain immediately, but
   only for the uses it already represents.
2. **A preregistered task distribution** can support a prospective study,
   but usually does not exist for an article already under review.
3. **Article-informed questions** can test whether the observer understood
   the article's consequences. They are useful now, but because the article
   helped select the questions, they cannot by themselves estimate its
   general value.

The third design becomes stronger when the questions apply the article's
claims to cases it does not discuss and when their answers come from
independent evidence. It is best described as a *claim-conditioned transfer
test*, not as an unbiased sample of reader needs. The reviewer should record
how the questions were produced and avoid presenting this result as broad
article gain.

This limitation means that task gain is not currently a universal automatic
review method. It is applicable where a relevant benchmark, preregistration,
or independent outcome set exists. Elsewhere it remains a diagnostic and a
research target.

## Cost is not one ratio

Context is scarce for a language-model reader, so article length belongs in
the report. Computation, retrieval burden, and the cost of constructing the
evaluation may matter too. But a single gain-per-token ratio is not a safe
objective.

A 100-token article that adds one point can beat a 2,000-token article that
adds ten points on the ratio while contributing much less. Ratios also
reward extreme compression and become unstable around small gains. Instead,
report total compression progress or task gain alongside their costs. Where
several artifacts are compared, show what each achieves under the same
context budget, or compare their gain-cost trade-offs.

Token count remains a useful cost proxy. It helps expose [reverse
compression](../notes/reverse-compression-is-when-llm-output-expands-without-adding.md):
text that grows without making more usable structure available. It is not the
only cost and need not combine with gain into one number.

## A cheaper reading for theory revisions

Predictive coding experiments and transfer tests need domain evidence,
scorers, and repeated model runs. Could a reviewer identify textual
properties likely to produce compression progress before those measurements
are available?

For articles that propose a theory revision, one candidate is to check
whether five slots can be filled from the text. We call this the *refinement
reading*, after [theory
refinement](../notes/definitions/theory-refinement.md): revising an existing
theory against cases while preserving useful prior knowledge.

| Slot | What the text should make recoverable |
|---|---|
| Addressed part | Which existing commitment the article proposes to change |
| Contradicting cases | Evidence that the commitment is wrong, incomplete, or wrongly scoped |
| Preserved content | What still holds after the change |
| Contradictable consequences | What the revised theory rules out, so later evidence could contradict it |
| Claimed reach | Which cases beyond the motivating ones the revision claims to cover |

The slots are things a reviewer should be able to locate, not required
section headings. A model could quote the passage supporting each slot,
making its reading open to inspection and disagreement.

In the experimental-method example, the addressed part is the commitment
that the method works across a range of conditions. The contradicting cases
are the failed experiments. The preserved content is where the method still
works. Contradictable consequences identify further conditions under which
failure is predicted. Claimed reach says how far beyond the observed cases
the revised account is supposed to apply.

The first four slots make the revision legible: what changes, why, what
survives, and what follows. The fifth records an assertion, not a result.
[Assessing whether the claimed reach is
real](../notes/definitions/reach-assessment.md) requires interventions,
independent cases, proofs, or another check beyond locating the passage.

The conjecture is that legible theory revisions tend to produce more
compression progress, and that revisions with real reach tend to transfer.
The reading does not establish either. A false argument can fill all five
slots, and useful tutorials, surveys, and datasets need not have this shape.
The refinement reading should therefore be tested against measured
compression progress and transfer where those measurements are possible.
It should also be compared with the simpler baseline of asking a model
directly how useful the article will be.

## Compression, learning, and warrant

The comparison also connects to [learning by theory refinement with fixed
models](./learning-by-theory-refinement-with-fixed-models.md). The model
weights remain fixed while an added retained artifact changes later
behaviour. Compression progress asks whether the artifact improves the
observer's model of evidence. Transfer asks whether that improvement changes
later work.

That connection does not make every useful article a warranted theory
revision. Compression progress and task gain measure effects on an observer.
They do not show that the observer should have changed in that direction. A
persuasive false article can compress a biased sample or improve performance
under a mistaken grader.

The broader writing objective is a [warranted reader
update](../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md).
This proposal measures parts of the update: improved compression and its
behavioral consequences. The quality of the evidence and reasoning that
warrant the update needs its own assessment. These dimensions should remain
separate until there is evidence for a defensible way to combine them.

## Could a scientific venue use this?

A venue would need to declare whose understanding and which domain it serves.
It could use several observers—a specialist, an adjacent-field reader, and a
practitioner—with different backgrounds and costs.

Compression progress may be tested retrospectively on a domain corpus fixed
by a protocol rather than selected for each article. Transfer may be tested
against later empirical outcomes. Did the article make those outcomes more
predictable than the prior literature did? This avoids requiring reviewers
to invent blind questions, although it introduces other problems.

A model trained on the article or the later results already carries some of
the intervention or answer in its weights. A clean comparison needs an older
model, or articles and outcomes that postdate the model's training data.
Later research may also have been shaped by the article. A retrospective
test can measure usefulness for the research that followed, but cannot tell
us what would have happened without the article.

Even a clean retrospective test arrives too late for submission review. Its
nearer use is to create evidence for testing cheaper review methods,
including the refinement reading. A first study could stay within one
domain, predefine its evidence corpus and outcomes, and compare textual
predictions with measured compression progress and transfer.

## What this leaves open

The largest question is whether compression progress in a model observer
tracks a valuable change in human understanding. The observer declaration
makes the proxy inspectable but does not validate it.

The second is whether predictive description length is practical for current
model interfaces and rich scientific observations. Turning an observation
into a scorable prediction can itself impose a representation that favors
some theories.

The third is how compression progress relates empirically to transfer. The
proposal expects a deep regularity to help on further cases, but the
relationship has to be measured rather than assumed.

Correctness, honest reporting, and fit for a venue still need their own
checks. The immediate research question is narrower: can an article's
observer-relative compression progress be measured reliably, and does it
predict useful transfer better than direct model judgment?

## Where to go next

The argument that a text's value depends on who reads it is developed in
[information value is
observer-relative](../notes/information-value-is-observer-relative.md).
[Warranted reader update is the objective of substantive
writing](../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md)
states the writer's side: the intended reader's prior is the baseline.
[Learning by Theory Refinement with Fixed
Models](./learning-by-theory-refinement-with-fixed-models.md) develops the
research program behind the retained-artifact comparison.
