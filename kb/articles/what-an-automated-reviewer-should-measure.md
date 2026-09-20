---
description: "Draft article proposing assessed explanatory reach and economy as candidate proxies for observer-relative compression progress, with article-informed tests and possible calibration through predictive coding and task gain"
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

*A proposal: assess explanatory reach and economy as evidence of compression progress*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

Suppose an article explains why a familiar experimental method fails under
certain conditions. Before reading it, a reader needs separate exceptions
to account for the observed results. After reading it, one mechanism
explains both the successes and the failures and predicts what should happen
in further experiments. The reader has acquired more than another answer:
the same explanation now does work that previously required several accounts.

That suggests a proposal for automated review. Ask what an article helps a
declared reader explain, how far that explanation holds beyond its motivating
cases, and how much additional machinery it requires. We propose assessing
*explanatory reach* together with *explanatory economy* as evidence of
compression progress: a reader capturing more of a domain's structure, or
capturing the same structure more simply.

Compression progress supplies the motivation, not a measurement already
available for arbitrary articles. Reach and economy are candidate proxies.
The practical proposal is to examine explanations and test their
consequences; predictive coding and downstream task performance are possible
ways to calibrate that assessment. None of these proposals has been tested
here.

## Why compression?

Jürgen Schmidhuber locates interestingness in improvement in an observer's
ability to compress its observations. The retained source states:
"The important thing are the improvements of the compressor, not its
compression performance per se"
([Driven by Compression Progress](../sources/driven-by-compression-progress.ingest.md),
verbatim). Old and new compressors must be compared on the same data.

For article review, the relevant object is the reader's account of the
domain, not the article's word count. A longer explanation can help a reader
replace many unrelated facts with one reusable structure. A shorter article
can merely omit necessary information.

In the experimental-method example, compression would come from replacing
separate exceptions with a mechanism and the remaining case-specific facts
needed to explain each result. Those facts still count: a theory has not
compressed the evidence by leaving its inconvenient parts unexplained.

Applying this motivation to review is our proposal. It does not follow from
Schmidhuber's account that explanatory reach is a reliable proxy, or that an
LLM can assess it. Those are claims the proposed reviewer needs to test.

## Why reach needs economy

[Explanatory reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md)
means that an explanation keeps working beyond the cases that produced it
because it captures why the pattern works. The connection to compression is
reuse: one explanatory structure accounts for several genuinely different
cases without needing a new assumption for each.

Coverage alone is insufficient. A lookup table can cover thousands of cases
by storing a separate answer for each. A vague statement can appear to cover
everything while ruling out nothing. Neither establishes the reusable
structure we are looking for.

Explanatory economy asks what commitments, parameters, auxiliary rules, and
exceptions the account needs for the explanatory work it performs. It is not
a count of sentences. Leaving an assumption unstated does not eliminate it,
and a precise longer explanation may require fewer independent commitments
than a short ambiguous one.

Reach and economy should be considered together, not forced into a ratio.
Broader reach can justify a more complex theory. A simpler theory can also
represent progress without extending reach at all, if it accounts for the
same evidence with fewer independent assumptions. A review should identify
which improvement is being claimed and what comparison supports it.

## Progress for which reader?

Because [information value is
observer-relative](../notes/information-value-is-observer-relative.md), a
principle with wide reach may teach an expert nothing. A tutorial may give a
newcomer access to that same principle for the first time.

The reviewer therefore needs a declared reader and baseline: what the reader
already knows, which explanations they can use, and what the article adds.
For a model-reader experiment, specify the model, its background material,
tools, and resource budget. For a textual review, state the assumed reader
and the prior account being improved.

This separates assessing a theory from assessing an article's contribution.
The first asks whether the explanation has reach and economy. The second
asks whether the article makes that structure newly available or usable for
its intended reader. Textual assessment can estimate that change; observing
the reader use the explanation provides stronger evidence.

## What the reviewer would do

The reviewer first reconstructs the explanation and its baseline. For an
article proposing a theory revision, a five-part reading can make that
reconstruction inspectable:

| Part | What the text should make recoverable |
|---|---|
| Addressed commitment | Which part of the prior account changes |
| Contradicting cases | What evidence motivates the change |
| Preserved content | What still holds after the change |
| Contradictable consequences | What the revised account rules out |
| Claimed reach | Which further cases the account claims to cover |

This reading follows [theory
refinement](../notes/definitions/theory-refinement.md): revising a theory
against cases while preserving useful prior knowledge. The reviewer can
cite passages for each part and flag missing information. These are not
required headings, and filling them establishes legibility, not quality.

The substantive assessment then asks four questions:

1. **What does the explanation bring together?** Identify the previously
   separate cases or commitments it accounts for.
2. **What else follows from the same commitments?** Derive consequences
   outside the motivating examples, including where the explanation should
   stop applying.
3. **Do those consequences survive checks?** Vary a load-bearing premise,
   consider a rival explanation, and check against evidence, executable
   tests, or proof where available.
4. **What extra assumptions were needed?** Record whether each extension
   reused the explanation or required another case-specific repair.

For example, suppose the article attributes failures to measurement drift
during an experiment, rather than to experiment duration itself. A useful
test would separate duration from drift: consider long experiments with
stable calibration and short experiments with substantial drift. The
explanation should constrain the expected failures in both cases. Finding
more long experiments that failed would not distinguish the mechanism from
the correlation.

This is [reach-assessment](../notes/definitions/reach-assessment.md), not just
checking whether a case meets a stated condition. A model can propose the
contrasting cases, but inventing their outcomes would not test the claim.
Where evidence is unavailable, the review should report an untested
consequence or proposed test.

The output should distinguish the claimed reach, the reach supported by
checks, and the assumptions needed to obtain it. It should also record failed
checks and unresolved alternatives. This gives the reader an argument to
inspect rather than an unexplained quality score.

## The questions need not be blind

A reviewer may need to read an article before seeing which questions are
meaningful. A new explanation can introduce the distinction worth testing,
as drift versus duration does in the example. Requiring all questions to be
written without sight of the article would exclude such tests.

The important separation is between deriving a consequence from the article
and checking it. The article may suggest the experiment; the observed result
must not be supplied by assuming the article is right. In a formal argument,
a proof must establish the consequence from explicit premises rather than
repeat the conclusion.

These article-informed tests assess particular claims and boundaries. They
are not an unbiased sample of everything readers might need. A reviewer
should expose how cases were selected and look for failures and rival
explanations, not only easy confirmations.

An existing independent benchmark can supply a broader comparison within its
own scope. Preregistration can fix case selection and scoring before further
results are observed. Neither is a prerequisite for criticism now, and
preregistration does not make an article-informed question set independent
of the article.

## Could compression be measured directly?

Predictive coding is one possible calibration experiment. Fix an observer,
an encoding of domain observations, and their order. At each step, score the
probability assigned to the actual next observation, with and without the
article. Summed negative base-two log probabilities give predictive code
lengths. Higher probability for the observed outcomes means fewer bits.

This is a conditional coding benefit: it treats the supplied article as
already available. A table containing every outcome could therefore produce
large savings without supplying a compact explanation.

To claim net compression, the accounting must also charge for the added
representation. With a common background and a specified code, compare the
baseline encoding of the observations with the encoding of the added
representation plus the observations conditional on it. Article tokens are
not automatically that representation's length in bits.

We have not specified a workable general protocol for doing this with
scientific articles. It needs a domain corpus, suitable probabilities, an
encoding, and a rule for charging the added representation. These choices
can favor some accounts over others. Predictive coding should therefore
remain a possible calibration experiment in suitable domains, not a ready
compression meter that every review is expected to run.

## Does the explanation improve later work?

Task gain supplies a different check:

> Task gain = task score with the article − task score without the article.

Keep the model, background, instructions, resource budget, and scoring method
fixed between the two arms, and repeat runs to assess variation. This tests
whether access to the article helps on the selected tasks. It does not
measure compression: a supplied answer can improve performance without
providing a reusable explanation.

For article-informed cases, the comparison can test whether the observer
uses the proposed explanation successfully beyond its examples. An
independent task set can test usefulness within a separately chosen scope.
Neither result should be generalized beyond the cases and selection process
that support it. If a model grades the answers, [its discrimination needs
checking](../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md).

This connects to [learning by theory refinement with fixed
models](./learning-by-theory-refinement-with-fixed-models.md): retained
material changes later behaviour while model weights remain fixed. The
review experiment tests one artifact's effect, not the whole learning loop.

Reading cost also belongs in the report. Context, computation, and retrieval
can matter even when the explanation is economical. [Reverse
compression](../notes/reverse-compression-is-when-llm-output-expands-without-adding.md)
adds text without adding usable structure, but not every long explanation
does that. Report benefits and costs separately rather than treating gain
per token as the objective.

## What would validate the reviewer?

The immediate study would ask whether assessments of reach and economy
predict independently checked transfer better than a simpler model judgment
of usefulness. It could compare the five-part reconstruction alone, the
substantive assessment, and direct judgment. That would test whether the
additional work earns its cost.

A retrospective study could use later experimental outcomes to check
predictions from articles and their prior literature. It must account for
model exposure to the articles or outcomes during training. Later research
may itself have been shaped by an article, so the result would concern
usefulness for the research that followed, not what would have happened
without it. Where predictive coding is feasible, it could separately test
whether the reach-and-economy assessment tracks coding savings.

The scope is explanatory articles, especially theory revisions, not every
valuable publication. Datasets can supply missing facts; descriptions can
preserve observations without explaining them. Even within scope, the
assessment is tentative. The broader objective remains a [warranted reader
update](../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md).
Checking consequences contributes to warrant, but a favorable reach assessment
does not certify all the article's evidence, reasoning, or reporting.

The proposal is therefore to assess how much additional explanatory work the
same structure supports, at what cost in assumptions, for which reader.
Whether an automated reviewer can judge that reliably is the first question
to test.

## Where to go next

[Information value is
observer-relative](../notes/information-value-is-observer-relative.md)
develops the reader-relative baseline.
[Explanatory reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md)
and [reach-assessment](../notes/definitions/reach-assessment.md) develop the
property and its assessment.
[Learning by Theory Refinement with Fixed
Models](./learning-by-theory-refinement-with-fixed-models.md) develops the
research program behind the retained-artifact comparison.
