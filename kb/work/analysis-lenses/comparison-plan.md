# Plan: compare bounded analysis coverage policies

## Commission and intended result

The operator authorized this plan on 2026-10-11 to prepare the workshop's first
comparison for a separate implementing agent. Implementing this plan means
revising workshop premises and producing a decision document, **not implementing
a change to the analysis method**.

Answer: how should limited analysis resources cover repositories too large for
exhaustive inspection? Recommend the smallest sufficient change, or retaining the
current arrangement, against the goals of mapping the design space and identifying
mechanisms worth assessing for Commonplace. Preserve the recently stabilized
process and its machinery. More inspected files, more findings or more workers
are not success criteria.

The result goes back to the operator before any live method change or trial.

## Authority, inputs and write scope

Read the repository's `AGENTS.md`, [work collection contract](../COLLECTION.md),
[workshop README](./README.md), and all documents listed in its Documents table.
Also read the [analysis design brief](../../reference/agentic-system-analysis-design-brief.md),
[audit evidence framing](../analysis-audit-evidence/README.md), its five listed
audit reports, and the
[navigation trace audit](../../reports/retained/analysis-worker-code-navigation-trace-audit-2026-10-11.md).
Read the live instructions, type clauses, plan entries and code needed to check
specific baseline claims; start with the paths in `current-arrangement.md` and
the coverage-bounds proposal. Do not load unrelated history by default.

Permitted writes:

- Targeted corrections to the workshop's README, current arrangement, design
  direction, open questions, evidence base, first deliverable and coverage-bounds
  proposal where this comparison establishes a reason.
- New `coverage-policy-comparison.md` in this workshop.
- Optional small measurement outputs under `measurements/` in this workshop.

This plan is the handoff contract. If its scope needs to change, return the issue
to the operator rather than rewriting the authorization. Preserve unrelated edits;
recheck status and affected files before editing. No other writer is assigned by
this plan. No delegation is needed or authorized by this handoff.

Method files, engine and analysis code, schemas, prompts, source checkouts,
retained analyses, audit reports and run state are read-only. No analysis runs,
new coverage audits, target execution, network acquisition, transfer scans,
integration, staging, commits or worktree disposal. Do not invoke engine commands
that advance or lock audited runs. Existing audit evidence and explicitly bounded
read-only source spot checks may be used; this is not a new correctness audit.

## 1. Establish and correct the baseline

Resolve the following review concerns against the current files. These are issues
to check, not conclusions to install without evidence:

- The verification type explicitly rejects exhaustive repository inspection.
  Distinguish an unclear operational stopping rule from an actual exhaustive
  duty. Read the verifier instruction and type together.
- Accounting for all modules and entry points can still be expensive. Structural
  coverage does not cease to scale with repository size.
- Low lens-anchor divergence and few recorded coverage findings do not establish
  complete coverage. Both can reflect shared omissions or limited searching.
- Existing audits contain selected source-backed omission findings, even though
  they provide no coverage denominator or systematic completeness measurement.
- Splitting a role can duplicate discovery; it does not establish a fixed cost
  multiplier without measurement.
- The proposal allows correctness checks at lens-owned anchors. Its evidence
  against adoption must not mistakenly classify those anchors as excluded.

Make the smallest consistent workshop corrections. Preserve the operator's
proposal as an option with its attribution and status; distinguish its original
intent from qualifications established here. Record consequential corrections
and their evidence briefly in the decision document. Do not alter the live method
or turn a candidate policy into an adopted instruction.

## 2. Compare three policies against the existing baseline

Use these alternatives, refining their wording where needed without changing the
comparison's purpose:

| Policy | Bound to examine | Main concern |
|---|---|---|
| Clarify the existing rule | Consequential conclusions are supported; known material uncertainties are qualified; make the existing materiality rule operational | The worker may still lack a usable stopping decision |
| Recorded-path bound | Bound lens omission searches by runtime and lens anchors, with explicit limits; preserve correctness checking of reported claims | Shared blind spots and file boundaries that poorly represent mechanisms |
| Question-driven omission checks | Select a small, justified set of consequential claims and search for omitted mechanisms or conditions that could change them | Poor question selection can miss an important mechanism |

The current method already asks for countercases and materiality judgments.
Explain what each option actually adds, removes or clarifies; do not present
existing behavior as a new feature. The third option was the coordinator's
provisional preference, not an operator decision or a result the comparison
must confirm. Options may overlap; explain whether a useful combination is
merely a clarification rather than a fourth architecture.

For each option state:

- Analyst and verifier responsibilities, including what remains independently
  discoverable by a lens.
- A concrete stopping rule and the unresolved questions it leaves.
- The coverage promise to the reader, including how unknown differs from absence.
- How it supports design-space understanding and later transfer assessment.
- Expected work, possible lost findings, and the exact likely change footprint.

Keep discovery selection, omission checking and correctness checking distinct.
Do not use a search budget to excuse a known contradiction. Narrowing a claim
can be preferable to expanding inspection, but a disclaimer alone cannot repair
a misleading claim. Do not invent numerical budgets without a basis.

## 3. Test the reasoning against retained cases

Use the following small case set rather than commissioning another broad audit:

- Both same-revision Graphiti runs: bulk retention and provenance omissions,
  complementary coverage, and the cost of searching alternative paths.
- Letta Code: broader architecture, the successful profile repair and navigation
  measurements. Its partial audit's lack of new corrections is not proof of
  completeness.
- Napkin: retained-file versus current-run consumption, and documented versus
  implemented mechanisms.
- Read the blocked Letta audit as a boundary and early-stop counterexample; do not
  treat its short duration as a full-analysis speedup.

For each applicable case/policy pairing, identify what inspection the policy
would call for, what material conclusion it could affect, what remains unknown,
and the likely additional or avoided work. Cite audit finding IDs and distinguish
reported observations from retrospective judgments. A policy plausibly directing
attention to an error does not prove a worker would have detected it.

Use the navigation audit's role/read counts as effort context, not tokens, unique
coverage, cost savings or a prediction of latency. Preserve method, source,
profile and scope differences. The two Graphiti runs are repeat-run evidence
within one system, not two independent systems.

Optional deterministic measurements are justified only when they discriminate a
named choice. Existing anchor sets or judgment records may supply them. Record
run ID, method commit, source revision, counting rule and limitations with every
measurement; retain enough detail to reproduce it. Do not build new tooling or
extract a large dataset merely because it is available. If a needed record or
frozen source is unavailable, report the gap rather than reconstructing it.

## 4. Produce the decision document

Write `coverage-policy-comparison.md` as a short operator-facing comparison, not
an additional full audit. Include:

1. Recommendation and confidence, including retaining the current policy if that
   is best supported.
2. Checked baseline and consequential premise corrections.
3. Policy comparison and case-based evidence, with unresolved alternatives.
4. Proposed stopping language and coverage statement, clearly labelled draft and
   not operative. Show how they constrain claims rather than only add disclaimers.
5. Expected benefit, effort and risk; evidence that would count against adoption.
6. Change footprint by instructions/type prose, plan/layout, analysis code and
   engine. Identify affected consumers where relevant, but do not implement.
7. Any remaining question requiring a separately authorized trial or bounded
   coverage audit. State its scope, cost boundary, success criteria and return
   condition. Do not make a new audit an automatic prerequisite.

Do not split memory, add a verifier or change dependencies in this task. If the
comparison suggests one of those is necessary, explain why a smaller change is
insufficient and return that choice to the operator.

## Acceptance, verification and return

The deliverable is complete when the three policies have been compared against
named retained cases, the recommendation has an explicit stopping rule and
coverage promise, and its costs and uncertainty are visible. An inconclusive
result is acceptable if it identifies the specific missing evidence and the
smallest next decision. No reduction in cost or increase in detection is claimed
as measured unless the evidence actually measures it.

Add the plan and decision document to the workshop's Documents table; update open
questions only where the comparison changes their evidence or status. Unadopted
recommendations remain unadopted. Run `commonplace-validate` on every changed
Markdown file and `git diff --check`; inspect status and diff for unauthorized
changes. Markdown-only workshop work does not require pytest.

Return a concise summary of the recommendation, evidence limits, changed files,
validation results and the decision requested from the operator. Stop there.
