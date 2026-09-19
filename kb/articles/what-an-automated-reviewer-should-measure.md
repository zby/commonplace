---
description: "Draft article proposing automated review through a model reader's gain on declared tasks, with gain per token as an efficiency measure and a five-part reading as a candidate proxy for theory revisions"
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

*A proposal: measure what an article helps a declared reader do*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

Suppose an article explains why a familiar experimental method fails under
certain conditions. Before reading it, a reader predicts the wrong outcome
for those conditions. After reading it, the reader predicts correctly,
including for experiments the article never discusses. That improvement
seems like something a reviewer should care about. Can we measure it?

Here is a proposal for automated review. Let a language model stand in for
the intended reader, and give it questions about the domain twice: once
with the article in context and once without it. Keep its background
material the same, and score the difference. The questions should represent
tasks the intended reader cares about, and should be written independently
of the article.

Call the difference *article gain*. It measures one kind of value: how much
the article helps this reader with these tasks. Report gain per token as
well, to show how efficiently the article uses the reader's context. For
articles that, like the one in the example, propose a revision to an
existing theory, we also suggest a cheaper reading of the text that might
predict gain. Nothing here has been run; both the experiment and the
cheaper reading are proposals to be tested.

## Value for whom, and for what?

An expert and a newcomer can learn different amounts from the same
article. Even readers with the same background may need different things:
one wants to predict experimental outcomes, another to diagnose failures,
and another to choose a method. A useful measure has to say which reader
and which tasks it represents.

The proposal therefore needs two declarations:

- **The observer:** a named language model and the background corpus
  supplied to it. Together they stand in for the intended reader.
- **The tasks:** the kinds of questions the article is meant to help that
  observer answer, sampled by a question set written independently of the
  article.

Article gain is the improvement in that observer's performance on those
tasks, so it is relative to both declarations. Because [information value
is observer-relative](../notes/information-value-is-observer-relative.md),
an article can produce substantial gain against one background and none
against another. A tutorial can be valuable for a newcomer even when it
adds nothing to the literature.

The tasks matter just as much. Choosing questions about replication,
method selection, or practical diagnosis expresses a judgment about what
counts as useful knowledge. The measurement makes that judgment explicit;
it does not make it for us.

## The experiment

The experiment has two arms. In one, the model receives the background
corpus and the questions. In the other, it also receives the article.
Everything else stays the same: model version, instructions, decoding
settings, and grading method.

The questions should be about the domain, not about what the article says.
For the experimental-method example, ask the model to predict outcomes or
identify conditions in which the method will fail. Asking it to repeat the
article's explanation would mainly test whether it can find that explanation.

The questions should also be written by someone other than the author,
without sight of the article. That keeps the question set a sample of the
declared tasks, including cases beyond the article's own examples, and not
a sample of what the article happens to cover.

The result is a difference:

> Article gain = score with the article − score without the article.

Gain can be negative: an article can confuse the observer or move it toward
worse answers. Because a model's answers vary between runs, repeated runs
would help distinguish a small gain from that variation.

The grader needs as much care as the questions. A persuasive false article
can score well if the grader rewards the same false answers. Empirical
outcomes make stronger answer keys where they are available. If a model
grades the answers, [its ability to distinguish better answers needs
checking](../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md).
Even with a sound grader, the measured gain supports a claim about the
sampled tasks; it does not certify the article's correctness as a whole.

The form of this comparison comes from Jürgen Schmidhuber's theory of
curiosity and interestingness. He locates the relevant quantity in
improvement: "The important thing are the improvements of the compressor,
not its compression performance per se". He also requires a common test:
"Note that both the old and the new compressor have to be tested on the
same data, namely, the history so far"
([Driven by Compression Progress](../sources/driven-by-compression-progress.ingest.md),
verbatim). What we borrow is the comparison of two states of an observer on
the same material: here the article changes the observer's context, while
the questions stay fixed. Applying the comparison to article review is our
step. His measure is a saving in description length; ours is a gain in
answer quality.

The same comparison is the measure of learning in our research program on
[learning by theory refinement with fixed
models](./learning-by-theory-refinement-with-fixed-models.md), applied here
to one article. The model stays fixed; what changes is the material it can
use and the performance that follows.

## How much gain, at what cost?

Context is a scarce resource for a language-model reader, so article length
belongs in the report:

> Gain per token = article gain ÷ article length in tokens.

This ratio penalizes [reverse
compression](../notes/reverse-compression-is-when-llm-output-expands-without-adding.md):
text that grows without adding useful structure. Padding spreads the same
gain over more tokens and lowers the ratio.

But efficiency alone is not enough. A 100-token article that adds one
point scores better per token than a 2,000-token article that adds ten.
A reader with room for either may prefer the larger improvement. The
report should therefore show both total gain and gain per token. Which
matters more depends on the reader's context budget and alternatives.

Reporting both also treats supporting detail fairly. A long explanation
showing where a method remains reliable may lower average gain per token
while still providing enough additional benefit to justify its length.

## A cheaper reading for theory revisions

Running the experiment requires a question set, a grader, and model runs.
Could a reviewer predict some of the gain by reading the article alone?

For articles that propose a theory revision, one candidate is to check
whether five slots can be filled from the text. We call this the
*refinement reading*, after [theory
refinement](../notes/definitions/theory-refinement.md): revising an existing
theory against cases while preserving useful prior knowledge.

| Slot | What the text should make recoverable |
|---|---|
| Addressed part | Which existing commitment the article proposes to change |
| Contradicting cases | Evidence that the commitment is wrong, incomplete, or wrongly scoped |
| Preserved content | What still holds after the change |
| Contradictable consequences | What the revised theory rules out, so later evidence could contradict it |
| Reach | Which cases beyond the motivating ones the revision covers |

The slots are things a reviewer should be able to locate, not required
section headings. A model could quote the passage supporting each slot,
making its reading open to inspection and disagreement.

In the experimental-method example, the addressed part might be the
commitment that the method works across a certain range of conditions. The
contradicting cases are the failed experiments, which motivate a narrower
claim. The preserved content is where the method still works. The
contradictable consequence is a prediction of where further failures should
occur, and the reach is that this prediction covers conditions not yet
tested.

There is a reason to expect this structure to help. It tells the reader
what to change, why to change it, what to keep, and what follows. The reach
slot connects most directly to the experiment: independently written
questions include cases the article never discusses, and a revision helps
with those only if it holds beyond the cases that motivated it. That
property is [explanatory
reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md);
[judging whether the claimed reach is
real](../notes/definitions/reach-assessment.md) takes more than finding a
passage that asserts it.

The conjecture is that articles making these parts recoverable tend to
produce more gain on relevant tasks. It is not a claim that every useful
article has this shape. A tutorial can explain an accepted method; a survey
can make scattered knowledge easier to use; a dataset description can
supply missing facts. All could improve answers without correcting a
prior theory. And within theory revisions, the reading does not check
truth: a false argument can fill all five slots.

The refinement reading therefore needs testing against measured gain. It
should also be compared with a simpler alternative: asking a model directly
how useful the article will be for the declared reader and tasks. If the
five slots predict no better, there is little reason to insist on them. The
experiment remains useful even if the refinement reading fails.

## Could a scientific venue use this?

A venue would need to say whose tasks it serves. It could declare several
observers—a specialist, an adjacent-field reader, and a practitioner—and
report gain for each. Their backgrounds and questions would differ. How the
venue weighs those results would express its scope.

For research articles, a retrospective test could use empirical answer
keys: take the literature available before an article as the background
corpus, and the outcomes of later experiments as the answers. Did the
article help predict what happened next? Questions about later outcomes
could test contributions that a contemporary reviewer would have struggled
to recognize.

There are two practical difficulties. First, a model trained on the article
or the later results already has part of the article or the answers in its
weights. A clean comparison needs either an older model, or articles and
outcomes that postdate the model's training data. Second, later research
may itself have been shaped by the article. Writing the questions without
sight of the article does not remove that dependence. Such a test can
measure usefulness for the research that followed, but cannot tell us what
research would have happened without the article.

Even a clean retrospective test arrives too late for submission review. Its
use is to supply cases for testing cheaper review methods, including the
refinement reading. A useful first study would stay within one domain,
choose a manageable set of articles, and compare the reading's predictions
with measured gain.

## What this leaves open

The largest question is whether a model reader's gain tracks what the
intended human readers learn. The observer declaration makes the proxy
inspectable, but does not validate it. The question applies to gain per
token as well: that measure is motivated by a model reader's limited
context, and a human reader's cost of reading need not follow token count.

Question selection remains a substantive judgment. A benchmark dominated
by familiar tasks may miss an article that enables a new kind of question.
Reporting the tasks alongside the scores lets readers see what the
experiment is capable of valuing.

Correctness, honest reporting, and fit for a venue still need their own
checks. This proposal concerns the contribution an article makes to a
reader's ability to answer and act. The first thing to find out is whether
that contribution can be measured reliably enough to improve review.

## Where to go next

The argument that a text's value depends on who reads it is developed in
[information value is
observer-relative](../notes/information-value-is-observer-relative.md).
[Warranted reader update is the objective of substantive
writing](../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md)
states the writer's side: the intended reader's prior is the baseline.
[Learning by Theory Refinement with Fixed
Models](./learning-by-theory-refinement-with-fixed-models.md) develops the
research program behind the experiment.
