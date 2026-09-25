---
description: "Automated review with two testable claims: reach and economy indicate reader-relative compression progress, and that progress improves relevant task performance"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/information-value-is-observer-relative.md
  - kb/notes/reverse-compression-is-when-llm-output-expands-without-adding.md
  - kb/notes/warranted-reader-update-is-the-objective-of-substantive-writing.md
  - kb/notes/definitions/addressable-theory.md
  - kb/notes/definitions/theory-builder.md
  - kb/notes/definitions/reach-assessment.md
  - kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md
  - kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md
---

# What an Automated Reviewer Should Measure

*A proposal: assess explanatory reach and economy as evidence of compression progress*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

Suppose an article explains why a familiar experimental method sometimes
fails. Before reading it, a reader needs separate exceptions to account for
the results. Afterwards, one mechanism explains both successes and failures
and predicts what should happen in further experiments.

An automated reviewer could look for that change: what does the article
help its intended reader explain, how far does the explanation extend, and
what assumptions does it need? We propose assessing *explanatory reach* and
*explanatory economy* as evidence of compression progress—capturing more of
a domain's structure, or capturing the same structure more simply.

The three assessments have different roles. Reach and economy provide
practical evidence that the reader gains a more compact, reusable account.
Predictive coding could test whether that judgment corresponds to actual
compression savings. Task gain asks whether the change helps the reader
do useful work. These are two claims to test: whether the proxy tracks
compression progress, and whether that progress pays off on relevant tasks.

The proposal concerns explanatory articles, especially theory revisions.
It is not a general measure of publication value: a dataset can supply
important facts without explaining them.

## From compression to reach and economy

Jürgen Schmidhuber locates interestingness in an observer's improving ability
to compress its observations: "The important thing are the improvements of
the compressor, not its compression performance per se"
([Driven by Compression Progress](../sources/driven-by-compression-progress.ingest.md),
verbatim). He compares old and new compressors on the same data.

Applied to the example, compression would mean replacing separate
exceptions with a mechanism and the case-specific facts still needed to
explain each result. Omitting inconvenient evidence would not count.
The observations are what must be encoded; the reader's account supplies
structure that can make their encoding shorter. The article provides that
account.

[Explanatory reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md)
means that an explanation keeps working beyond the cases that produced it
because it captures why the pattern works. Its connection to compression
is reuse: the same structure explains different cases without needing a
separate assumption for each.

Coverage alone does not establish this. A lookup table stores a separate
answer for every case. A vague statement can appear to cover everything
while ruling out nothing. Explanatory economy asks what assumptions,
parameters, rules, and exceptions an account needs for the work it does.
Unstated assumptions still count; word count is not a measure of economy.

Reach and economy must be judged together. Broader reach can justify a more
complex theory. A simpler theory can also represent progress at unchanged
reach, if it explains the same evidence with fewer independent assumptions.
The reviewer should identify which improvement the article offers and
against which prior account.

This connection makes reach and economy plausible indicators of compression,
not established measures of it. Their use in automated review is our
proposal, not a result established by Schmidhuber's theory.

## Progress for which reader?

A principle with wide reach may teach an expert nothing while changing how
a newcomer understands a domain. [Information value is
observer-relative](../notes/information-value-is-observer-relative.md).

The review therefore needs a baseline: what the intended reader already
knows and can use. An explanation's reach and economy are not the same as
an article's contribution. The contribution is what the article makes newly
available or usable for that reader.

A textual review should state its assumed reader and prior account. An
experiment using a model as the reader should specify the model, background
material, tools, and resource budget. Reading the article can suggest what
the reader will gain; observing the reader use it provides stronger evidence.

## What the reviewer would do

First reconstruct the explanation. For a theory revision, five parts make
the proposed change inspectable:

| Part | What the reviewer should recover |
|---|---|
| Addressed commitment | Which part of the prior account changes |
| Contradicting cases | What evidence motivates the change |
| Preserved content | What still holds |
| Contradictable consequences | What the revised account rules out |
| Claimed reach | Which further cases it claims to cover |

This reading treats the prior account as an [addressable
theory](../notes/definitions/addressable-theory.md): its commitments can be
inspected and revised separately against cases while useful prior knowledge
is preserved. The reviewer should cite supporting passages and flag gaps.
These are not required headings; finding all five parts makes a revision
legible but does not establish its quality.

Next assess the explanation:

1. **What does it bring together?** Identify the previously separate cases
   or commitments it accounts for.
2. **What else follows?** Derive consequences beyond the motivating examples,
   including where the explanation should stop applying.
3. **Do those consequences survive checks?** Vary a key premise, consider a
   rival explanation, and check against evidence, executable tests, or proof.
4. **What extra assumptions were needed?** Record whether each extension
   reused the explanation or required a case-specific repair.

Suppose the article attributes failures to measurement drift during an
experiment, rather than to duration itself. A useful test separates the two:
consider long experiments with stable calibration and short experiments
with substantial drift. The explanation should constrain the expected
failures in both. Finding more long experiments that failed would not
distinguish the proposed mechanism from a correlation.

This is [reach-assessment](../notes/definitions/reach-assessment.md).
The model can propose contrasting cases, but inventing their outcomes would
not test the claim. Without evidence, a consequence remains untested.

The report should distinguish claimed reach from reach supported by checks.
It should identify the assumptions needed, failed checks, and unresolved
alternatives, then say what has improved over the reader's prior account.
In the drift example, the proposed improvement is one mechanism replacing
separate exceptions while handling unfamiliar combinations of drift and
duration. This is the compression claim that the later experiments would
examine.

## Choosing tests after reading the article

A new explanation can reveal which questions matter, as drift versus
duration does in the example. The reviewer need not be blind to the article.
What matters is separating the derivation of a consequence from its check.

The article may suggest an experiment, but its result must not be supplied
by assuming the article is right. A proof must establish a consequence from
explicit premises rather than repeat the conclusion. In either case,
the reviewer should seek failures and distinguish rival explanations,
not just collect confirmations.

Article-informed tests assess particular claims and boundaries. They do
not sample everything readers might need, so the review should explain how
cases were selected. An existing independent benchmark can offer a
comparison within its own scope. Preregistration can fix case selection
and scoring before further results are observed, but does not make
article-informed questions independent of the article. Neither is a
prerequisite for criticism now.

## Testing the two claims

The tests should concern the same article, declared reader, and domain.
First record the reviewer's assessment of the improvement over the prior
account. Then test its relation to compression and to task performance.
Neither relation follows automatically from the other.

### Does the assessment track compression progress?

In a domain where predictive coding is feasible, fix a model reader, an
encoding of observations, and their order. With and without the article,
measure the probability assigned to each next observation before revealing
it. Summed negative base-two log probabilities give predictive code lengths:
higher probability for the observed outcomes means fewer bits.

That saving treats the article as already available. Net compression must
also count the added representation. Compare the baseline encoding of the
observations with the encoding of the added representation plus the
observations conditional on it, using a common background and specified
code. Article tokens are not automatically the representation's length
in bits.

For the drift explanation, this asks whether the mechanism and remaining
case-specific details encode the experimental results more economically
than the reader's prior account. Across articles, do favorable assessments
of reach and economy predict these net savings? Compare the full assessment
with the five-part reconstruction alone and a direct model judgment of
compression benefit.

This would test the first claim: whether our practical assessment tracks
compression progress. We do not yet have a general protocol. Choosing the
observations, encoding, probabilities, and representation costs is
substantial work and can favor some accounts over others. Coding experiments
could calibrate the assessment in suitable domains; they are not required
for every review.

### Does compression progress improve relevant task performance?

The second claim concerns practical benefit. In the same example, does
access to the drift explanation help the reader diagnose unfamiliar
failures or choose when to recalibrate?

> Task gain = task score with the article − task score without the article.

Keep the model, background, instructions, resource budget, and scoring method
fixed between the two conditions. Repeat runs to assess variation. If a
model grades the answers, [check its ability to distinguish better
answers](../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md).

Article-informed cases can test the applications the explanation suggests.
An independent task set tests usefulness within a separately chosen scope.
Where compression has also been measured, compare its progress with gain
on tasks that use the learned structure. Where it has not, this tests whether
the reviewer's assessment predicts usefulness, leaving its compression
interpretation unconfirmed.

Even a correlation between compression progress and task gain would not show
that the former caused the latter. Comparisons with an article containing
only case-specific answers could help distinguish a benefit from reusable
structure from a benefit from supplied answers. That attribution requires
additional controls.

The results can disagree. An answer table can improve task scores without
offering net compression. A compact explanation can improve compression
while leaving tasks that do not use its structure unchanged. Task gain
measures usefulness; establishing a payoff from compression requires evidence
of both compression progress and its use.

Report reading and computation costs alongside gain. A longer article may
make a compact explanation easier to use, or it may add text without useful
structure—the failure called [reverse
compression](../notes/reverse-compression-is-when-llm-output-expands-without-adding.md).
Gain per token alone would hide the trade-off between total benefit and cost.

This experiment connects to [building a theory builder from today's
LLMs](./can-a-theory-builder-running-on-fixed-weight-llms-learn.md): that research program
tests whether retained theories change later behaviour while model weights
remain fixed. This experiment tests one article's effect, not whether
criticizing and revising retained theories improves a whole system's
capacity for future action.

A retrospective study could use later experimental results for both coding
and task tests. It must address model exposure to the article or results
during training. Later research may also have been shaped by the article,
so the study would concern usefulness for the research that followed, not
what would have happened without it.

## What the assessment can establish

The broader objective is a [warranted reader
update](../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md).
Checking consequences contributes to warrant, but a favorable reach
assessment does not certify all of an article's evidence, reasoning, or
reporting.

The reviewer proposes that an article gives its reader a more compact,
reusable account. Reach and economy are the practical grounds for that
judgment. Coding experiments test whether it tracks compression progress;
task experiments test whether the change is useful. Keeping those claims
distinct lets us learn whether the reviewer measures what we intend and
whether that measurement matters.

## Where to go next

[Information value is
observer-relative](../notes/information-value-is-observer-relative.md)
develops the reader-relative baseline.
[Explanatory reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md)
and [reach-assessment](../notes/definitions/reach-assessment.md) develop the
property and its assessment.
[Can a Theory Builder Running on
Fixed-Weight LLMs Learn?](./can-a-theory-builder-running-on-fixed-weight-llms-learn.md) develops the
research program behind the retained-artifact comparison.
