---
description: "Empirical conjecture: an LLM may judge which changes are worth making in open-ended work under strict necessary preference as a working definition; traces packet vs. tool-use setups and a three-arm diagnostic test"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/theory/defining-improvement-for-open-ended-work.md
  - kb/theory/necessary-preference-can-guide-improvement-without-a-global-measure.md
  - kb/theory/selection-based-learning-needs-only-a-local-comparison.md
  - kb/theory/reversibility-can-favor-a-change-by-limiting-future-loss.md
  - kb/theory/definitions/selection-based-learning.md
  - kb/theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md
---

# Can an LLM Judge Which Changes Are Worth Making?

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

In open-ended work—maintaining a software repository, curating an internal
knowledge base, or revising a company's refund policy—someone repeatedly
faces a concrete choice: keep the current setup, adopt a proposed change,
or try a narrower version of it. No single score settles every such choice,
because gains and losses fall on different tasks and different people. Yet
maintainers make these calls every day without inventing a global formula.

This article states an **empirical conjecture**, not a new definition of
improvement: **given a stated purpose, real alternatives, and a way to
obtain relevant evidence, a large language model (LLM) may be able to judge
which change is worth making for the work ahead.** The model need not find
the best conceivable change or be right on every proposal. To be useful,
its selections only have to beat a credible baseline—such as a project's
existing admission check—over a stream of real work, once investigation
cost, human help, and mistakes before rollback are counted.

To keep that claim testable, we adopt
[strict necessary preference](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md)
as our working definition of improvement. Once the alternative, the work,
the affected parties, and the horizon are fixed, a change counts as an
**improvement** when every way of weighing the consequences compatible with
the stated purpose favors it over the alternative. When every compatible
weighting favors the current state, the change is a **loss**; when
compatible weightings pull in opposite directions or decisive facts are
missing, the comparison stays **open**. That working definition is fixed
before testing, not presented as the only meaning of *better*—and it does
not forbid acting when a comparison is open.

Three observations make the LLM conjecture worth testing rather than
dismissing on sight. First,
[selection needs only a local comparison](../theory/selection-based-learning-needs-only-a-local-comparison.md):
because proposing changes is costly, a judge never has to rank every
possible version of a system—only the candidate at hand against the current
state or a few nearby alternatives. Second, many decisive facts already
live in readable records—error logs, issue trackers, configuration files,
policy documents, and test suites—that an LLM can read or query. Third,
under necessary preference, a judge does not have to invent arbitrary
weights for genuine value conflicts; it only needs to settle clear cases
and expose the missing fact or unstated commitment when a comparison stays
open.

Most of this article uses a software-maintenance example, not because
software development is the only domain where this applies, but because
software teams already keep unusually clear records—diffs, changelogs,
tests, and support matrices—that make it easy to see where each piece of
evidence comes from. The same structure appears wherever work is guided by
retained rules or procedures, from editing an operational handbook to
deciding who may approve customer refunds.

## Inside one decision

Take a constructed example. An automated maintenance agent opens a pull
request upgrading a project's parser dependency from version 2.4 to 3.0.
The changelog says version 3.0 fixes a bug that causes malformed timestamp
fields to fail parsing, and drops support for Python 3.9. The project's
continuous-integration (CI) suite runs on Python 3.12 and passes.

Notice what those two artifacts—the changelog and a green CI run—do **not**
tell a judge:

1. **Whether the fix matters to this project.** Does the project ever
   receive inputs that trigger the malformed-timestamp bug? An upstream fix
   that never touches this project's data buys nothing here.
2. **Whether the removed runtime is a live commitment.** Does the project
   promise Python 3.9 compatibility in its packaging metadata, release
   policy, or customer contracts—and do real deployments still run on it?

A naive judge reading only the pull request sees a bug fix and green tests,
and merges. A slightly more cautious judge sees *"drops Python 3.9"* and
rejects. Neither has checked the facts that actually decide the case.

Follow what happens when a judge treats *"what would count as better work
here, and how could we tell?"*
([defining improvement for open-ended work](../theory/defining-improvement-for-open-ended-work.md))
as an investigative step rather than a guess. Under our working definition,
four different factual situations on the exact same pull request produce
four distinct verdicts and reasonable decisions:

- **Live bug, retired runtime (*improvement*).** Production error logs show
  recurring failures matching the malformed-timestamp bug; replaying one
  captured input confirms version 2.4 rejects it while version 3.0 parses
  it and produces the expected downstream output; packaging metadata and
  deployment configs show the project dropped Python 3.9 six months ago.
  Every compatible way of weighing the project's work favors merging: a
  live failure is fixed and no commitment is broken.
- **Unreached bug, active commitment (*loss*).** Searching six months of
  error logs and input schemas shows the project never passes timestamps
  through that code path, while `pyproject.toml` and the support policy
  still promise Python 3.9 through the end of the year. Breaking a standing
  commitment for zero local benefit loses under every compatible weighting,
  so rejecting is straightforward.
- **Live bug and active commitment (*open for trade-off disagreement*).**
  Captured production inputs hit the bug *and* active customers still
  deploy on Python 3.9. Compatible weightings now pull in opposite
  directions, and counting more bug reports will not settle whose loss
  takes priority. A capable judge should neither merge silently nor reject
  blindly: it can look for a different alternative (such as a narrow
  input-sanitizing workaround that keeps Python 3.9 working), or leave the
  comparison open and escalate the exact conflict to a maintainer.
- **Incomplete records (*open for missing evidence*).** Telemetry covers
  only the company's hosted service, not self-hosted installations, and
  shows zero Python 3.9 runs. **An observed absence in incomplete logs is
  not proof of no affected users.** Because a plausible answer—active
  self-hosted deployments on Python 3.9—would reverse a merge decision, the
  comparison stays open for missing evidence rather than clearing the
  upgrade.

Nothing about that four-way fork is unique to code. Consider a constructed
operational example: a branch manager proposes letting counter staff
approve routine refunds under $50 without head-office sign-off. The
proposal text alone tells a judge neither how long customers currently wait
for head-office checks nor how often branch records miss prior disputes. If
store logs track completed refunds but never record customers who walked
out while waiting—or never tie later chargebacks back to specific branch
approvals—an empty error column again leaves the comparison open for
missing evidence rather than proving safety. Whether the domain is a parser
upgrade, a refund rule, or a knowledge base, the hard part of the judgment
is locating which missing fact could reverse the verdict and knowing when
the available records cannot supply it.

## Where the evidence comes from

Saying *"an LLM judges the change"* leaves the surrounding machinery
unspecified. Two plausible designs—and a hybrid between them—divide the
work differently between the model and the system around it.

| Arrangement | What the model receives | What the model must supply | What stays outside the model |
|---|---|---|---|
| **Evidence packet** | A prepared bundle: proposed diff, stated commitments, relevant logs or test runs, their provenance, and known coverage gaps | Weighing the supplied evidence against the purpose, spotting missing facts or conflicts, and returning a verdict or escalation | Deciding which records to pull, which tests to run, and which commitments to surface |
| **Tool-using investigator** | The proposal, the stated purpose, and read/query/test/ask tools under a budget | Choosing which question could reverse the verdict, running checks, respecting coverage limits, using the answer, and stopping when inquiry stops paying off | Tool definitions, permissions, budget limits, and the records themselves |

The boundary between these two setups matters when evaluating the bet.

**Packet curation is already judgment.** If a human engineer—or a
domain-specific script written for this exact failure mode—selects the one
log query that surfaces the malformed-timestamp errors and pastes the exact
runtime-support clause into the prompt, much of the hardest diagnostic work
has already been done before the LLM runs. Calling the resulting merge
decision *"autonomous LLM judgment"* misattributes the curator's work to
the model. An honest packet-based test must record who chose the packet's
contents and treat the packet builder as part of the system being assessed.

**Tools do not by themselves confer judgment.** Giving an LLM access to a
repository, log queries, a test runner, and a messaging channel to ask
maintainers does not mean it will use them well. To earn its keep in a
tool-using loop, the judge has to clear four bars:

1. *Investigate only what could reverse the verdict.* As
   [necessary preference](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md#open-for-missing-evidence-open-for-trade-offs)
   notes, an unknown is worth checking only if a plausible answer could flip
   the choice. Running a generic linter or re-running an already-green
   Python 3.12 test suite spends budget on answers that cannot change the
   decision.
2. *Read coverage limits alongside results.* Knowing that hosted telemetry
   excludes self-hosted users is what prevents treating zero observed runs
   as zero affected users.
3. *Let the answer move the verdict.* An LLM can run a tool, cite its
   output in plausible prose, and still stick to its initial bias—the same
   gap between plausible prose and causal grounding noted in
   [rationale faithfulness](../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md).
4. *Stop when further inquiry is not worth its cost.* Exhaustive auditing
   of a trivial, easily reversible change wastes more effort than the
   change could ever save; conversely, when no record settles whose loss
   takes priority, asking a maintainer for a commitment or leaving the
   comparison open is the right place to stop.

In practice, a **hybrid** arrangement is often the most sensible starting
point: a fixed, lightweight packet supplies cheap standing context (the
diff, declared support policies, CI status, and known telemetry gaps),
while bounded tools let the model run targeted checks—like replaying a
captured failing input against the candidate dependency—and escalate when
it hits an unrecorded commitment.

## Testing the bet without asking the judge to grade itself

A judge cannot certify its own selections. Neither a persuasive
explanation, nor a thorough-looking sequence of tool calls, nor agreement
with one maintainer on a favorite example establishes that the judge's
choices improve the work.

Instead of designing a full benchmark up front, a single **three-arm paired
comparison** can expose where an LLM judge works and where it breaks. Hold
the proposed change (such as the dependency update, or a parallel policy
edit) and the stated purpose fixed, and vary one documented decisive
fact—say, whether real inputs hit the bug, or whether a promised commitment
is still active—across paired cases:

1. **Arm 1: Fact given directly.** Place the decisive fact (with its
   provenance) inside the evidence packet. Test whether flipping that fact
   flips the judge's decision cleanly between improvement and loss (or
   open).
2. **Arm 2: Fact discoverable with tools under a stated budget.** Remove
   the fact from the packet—leaving the case initially open for missing
   evidence—keep the fact in the repository, logs, or replay fixtures, and
   give the judge tools plus a fixed call or cost budget. Test whether it
   asks the discriminating question, finds the fact within budget, and
   reaches the same decision as in Arm 1.
3. **Arm 3: Fact unknowable from the available tools.** Remove the
   decisive record or restrict logs to incomplete coverage (open for
   missing evidence), or leave a genuine priority conflict unstated in any
   document (open for trade-off disagreement). Test whether the judge keeps
   the comparison open, asks for the missing commitment, or proposes a
   bounded check—rather than fabricating certainty from absent logs.

Those three arms diagnose failures cleanly. A model that fails Arm 1 cannot
weigh evidence already in front of it. A model that passes Arm 1 but fails
Arm 2 can weigh evidence once handed to it, yet fails at active inquiry
under a budget. A model that passes Arms 1 and 2 but fails Arm 3 handles
closed puzzles while overclaiming when real-world records have holes or
unstated priorities.

Passing paired case checks is still only an intermediate diagnostic. To
test whether the judge actually helps, compare the system using the LLM's
selections against a credible alternative—such as the project's existing
admission check (for example, merging any dependency PR whose CI passes, or
holding every major-version bump for manual review)—and evaluate **fresh
downstream work independently** under the same fixed working definition.
Count the full bill: investigation compute and latency, maintainer time
spent answering escalations, and any breakage or rework incurred before a
bad change is rolled back.

No completed run of this comparison is reported here. And when runs are
carried out, a failure in one configuration—one model, tool set, budget,
and domain—counts against that setup, not against every possible LLM or
machinery design. What would count against the bet broadly is a repeated
pattern across strong models and clean evidence interfaces where
investigation costs, false confidence on incomplete records, or
misdirected selections leave the LLM-judged system no better than the
simpler baseline.

## Three claims to keep apart

Evaluating this bet stays clear only if three separate questions are not
collapsed into one:

1. **What counts as improvement is fixed for the test.** Adopting
   [strict necessary preference](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md)
   as our working definition fixes the standard before running the test,
   without demanding that every decision have a robust winner. Open
   comparisons still allow a maintainer or system to act—including by
   running a bounded trial—provided the decision names what gets installed
   now, what evidence will be watched, and what triggers reconsideration
   ([reversibility can limit future loss](../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md)).
   Not every change admits a cheap trial: shipping a Python 3.9 drop to
   live self-hosted users breaks them immediately on upgrade, so a safe
   trial there means a pre-release deprecation check or opt-in canary
   rather than merging straight to default.
2. **Whether an LLM can make useful selections is this article's empirical
   bet.** Strict necessary preference could be completely sound as an
   evaluation standard while current LLMs still fail as judges—because they
   miss diffuse costs, fail to query the right logs, or ignore coverage
   gaps.
3. **Whether explicitly teaching the decision-analysis framework improves
   those selections is a separate empirical question.** Adopting necessary
   preference as the test's working definition does not assume the judge
   itself must be prompted with it. Because a framework stated in prose—naming
   compatible measures, necessary versus possible preference, or the split
   between missing evidence and contested trade-offs—can be handed directly
   to an LLM, it is easy to assume that prompting with the framework makes
   the model a better judge. Presenting a method in language establishes
   neither competence nor benefit; whether framework-guided prompting beats
   giving the model the plain purpose and tools requires its own controlled
   comparison.

## Where to go next

- [Defining Improvement for Open-Ended Work](../theory/defining-improvement-for-open-ended-work.md)
  — explores what a usable definition of improvement has to handle across
  editors, releases, dependencies, knowledge bases, and operational
  policies, starting from the expected stream of work.
- [Necessary preference can guide improvement without a global measure](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md)
  — states the strict necessary preference working definition adopted here,
  with its six verdicts and the split between missing evidence and
  contested trade-offs.
- [Selection-based learning needs only a local comparison](../theory/selection-based-learning-needs-only-a-local-comparison.md)
  — explains why costly search means a selection step compares only the
  alternatives reached rather than ranking every possible state, grounded
  in [selection-based learning](../theory/definitions/selection-based-learning.md).
- [Testing Autonomous Selection-Based Learning](./testing-autonomous-selection-based-learning.md)
  — sets out the broader experimental program beyond admission and inquiry:
  targeted correction, criterion revision (including a proposed first
  routing-check experiment), whole-loop net gain, and the current state of
  evidence.
