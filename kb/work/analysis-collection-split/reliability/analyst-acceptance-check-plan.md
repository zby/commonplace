# Analyst acceptance check: implementation plan

## Commission

Written on 2026-10-04 at the operator's request. It is the commission for the
executor the operator launches on it. The launch is the authority to
implement; this file alone starts nothing.

It replaces the earlier plan "quotations completed in the draft", which the
operator set aside the same day in favour of this simpler design, and it
absorbs one part of the [structured recovery proposal](./structured-recovery-proposal.md).
It does not authorize an analysis run or the regeneration of any system.

## Intent

An analyst should be able to find out, inside its own job, everything
acceptance would refuse. Today it cannot. It can run `commonplace-validate`
on its output, but acceptance checks more: record references across the set,
identity fields against the run, and every quotation against the frozen
source. Those run only after submission. A refusal there costs a whole new
worker attempt, and a job gets one retry before it blocks.

The second audited run shows the gap: a quotation altered on insertion passed
the analyst's local validation and was refused at acceptance.

Give the analyst the acceptance check as a tool. One check, two callers: the
analyst before submitting, the engine at acceptance. Mistakes are then found
where fixing them is cheap.

With that tool, quotation needs no helper. An analyst quotes the way a person
does: copy the passage, say which file it is from, and check. This removes
the selection files, the JSON batch and the copying of generated citations,
which caused most quotation failures in the retained traces.

When a choice is not settled here, choose what leaves the analyst less to do
and to learn, and what keeps one check behind both callers.

## End state

- An analyst can run one command on its draft that applies the same check
  the engine will apply to that job at acceptance, and prints the refusals.
  The command changes nothing: not the draft, not the run's state, not the
  job's attempt count.
- That check reports every independent failure in one run. It stops early
  only where a later check cannot run until an earlier one passes, such as
  quotation matching in a member that does not parse.
- An analyst writes a quotation as a blockquote of the passage and an
  attribution line naming the source path:

  ```text
  > for line in data:
  >     file.write(json.dumps(line) + "\n")
  > --- `run_benchmark.py`
  ```

  It writes no revision and computes no line range. The revision is the
  run's frozen source.
- A passage that does not occur in that file is refused with the block's
  location in the draft.
- **Every ambiguous quotation comes back with proposed fixes**, as the
  helper's batch mode gives today. For each passage that occurs more than
  once, the check prints a list of candidates, one per occurrence: a ready
  attribution line with its line range, and enough surrounding source text
  to tell the occurrences apart. One run covers all ambiguous quotations in
  the draft. The analyst picks a candidate by its context and pastes that
  attribution line, or lengthens the quotation until it is unique.
- A passage with more occurrences than the existing limit gets no list. The
  check asks the analyst to expand the quotation so that it is less
  ambiguous. The limit is the one the helper uses today,
  `MAX_QUOTE_OCCURRENCES`, currently ten; keep one constant for it.
- The quotation helper's generation modes are gone: single passage, JSON
  batch, and the rules that taught them. If nothing else uses the command, it
  is removed.
- Each job instruction tells the analyst to run the check before submitting,
  in place of the separate validation step where one exists. The worker's
  quotation rules are shorter than today.
- Acceptance is unchanged in authority: the engine judges the submitted
  output with the same check.
- Required tests and validation pass. A decision record and a result record
  exist.

The first analysis run with the check is the outcome check. It needs its own
commission.

## What must stay true

- Every quotation in an accepted member is verbatim text of the frozen
  source, compared as today with whitespace collapsed.
- **A misremembered or altered quotation fails.** No fuzzy matching, no
  nearest-match repair, no correction of quoted content.
- The uniqueness rule of
  [ADR 094](../../../reference/adr/094-quotations-require-a-unique-occurrence-or-a-containing-range.md)
  holds: one occurrence in the file, or one inside a given range.
- An analyst never calculates a line range. Pasting an attribution line the
  check proposed is allowed, and the check then verifies that the passage
  occurs in that range.
- The check proposes fixes only for ambiguity, where every candidate is a
  genuine occurrence of the exact passage. It proposes nothing for a passage
  that is not found; a guess there would be a fuzzy match.
- The check never chooses an occurrence. Which one supports the finding is
  the analyst's judgment.
- The analyst chooses the passage and judges whether it supports the
  finding. A passing check establishes form and occurrence, not support and
  not the correctness of the analysis. The member types' statement that a
  self-check attests neither stays.
- The check has one implementation. The tool calls what acceptance calls.
- Independent verification jobs stay as they are.

## What is given up, by the operator's decision

Published citations no longer carry a line range, except where one was needed
to tell occurrences apart, and no longer carry the revision, which the
member's frontmatter states. Readers find a passage by its text. Quoted text
is not rewritten to the source's exact spacing. ADR 094 rejected
author-written citations because they left range calculation to the author
and caught mistakes only after drafting. Path-only attribution removes the
calculation, and the tool moves the catch before submission.

## Boundaries

- **Analytical content and evidence rules are unchanged.**
- **The tool is advice to the analyst.** It records nothing in the run and
  cannot accept an output.
- **One documented route for quotation.** Do not keep the helper's old route
  in the instructions beside the new one.
- **Citations already written with a range and revision stay valid**, so
  frozen sets and their fixtures need no change. Frozen sets are not edited.
- **No net growth of worker input.** Measure the affected rules before and
  after.
- **Not in scope:** code fixing mechanical values, escalation when a refusal
  repeats, and recording refusals per rule. These stay in the structured
  recovery proposal.
- **Other sessions edit this repository.** Start from the committed state.
  Check status before each commit and stage only this work's files.
- **Repository rules apply**, as in the collection-split plan. Removing a
  command's entry point follows the editable-installation instructions in
  `INSTALL.md`.

## Priorities and partial results

The tool comes first and is useful alone: it closes the gap between local
validation and acceptance for every existing check. Reporting all independent
failures comes second, because a tool that shows one class of error per run
needs several runs. Path-only quotation and removal of the helper come third
and go together, so that analysts are never taught a route that no longer
exists or left without one.

If work stops after the first or second part, that is an acceptable result:
quotation stays as it is today, with the helper. A state in which the helper
is removed and path-only quotations are not accepted is not acceptable.
Record what remains.

A negative finding is a result. If a check fails, report it; do not loosen
the check.

## Supported route

One workable route. Take another if it reaches the end state while keeping
what must stay true, and say what you changed.

1. Expose the check. Each job's check is the validator its job definition
   carries in `src/commonplace/lib/agentic_workflow.py`; the engine applies
   it in `src/commonplace/workflow/engine.py`. Find how a command can obtain
   the same validator for a named job of a run without advancing the run.
   Prove with a test that the tool and acceptance return the same refusals
   for the same file.
2. Report independent failures together. `pass_refusals` returns at the first
   failing stage: schema or references, then identity, then prefixes, then
   quotations. Decide for each stage whether it truly depends on the earlier
   ones, and run the rest together. Check the other jobs' validators for the
   same pattern.
3. **Fixed: measure ambiguity before changing quotation.** Take the retained
   members as read-only input, strip the line range and revision from every
   citation in copies, and run the quotation check. Report how many
   quotations pass and how many are ambiguous without their range. It needs
   no model. It is fixed because it is the only cheap evidence of how often
   an analyst will have to lengthen a quotation or copy a range.
4. Accept path-only attribution: take the revision from the run, treat a
   range as optional, and make the two refusals state the block's location.
   For an ambiguous passage, reuse what the batch mode produces today in
   `generate_quote_batch`: per occurrence, the range, the source context
   that distinguishes it, and the attribution to paste.
5. Rewrite the Quotation section of the worker rules and the related
   passages of the source contract, the boundary job and the job files that
   name a validation step. Remove the helper's generation modes and their
   entry in `kb/reference/commands.md`.
6. Measure, verify, write the decision record and the result record.

## Left to the executor

The command's name and where it lives; how it finds the job and its draft;
its output format and exit statuses; how much source context a candidate
shows; the attribution form for a capture
source, which has no commit-relative path; which stages are truly dependent;
whether the quotation command is removed or reduced; test structure; wording
of the rules; commit granularity.

## Return to the operator

Stop and ask when:

- the tool cannot use the same validator as acceptance without changing the
  engine's handling of attempts or run state;
- the ambiguity measurement shows that a large share of quotations need a
  range, which would make path-only attribution costly;
- another consumer of the quotation helper appears;
- a job's check needs inputs the analyst may not read;
- the change conflicts with a decision record other than ADR 094;
- worker input grows in net.

Otherwise proceed without asking.

## Verification

- `uv run pytest -q` and `uv run ruff check .` pass.
- For each job kind, a test shows the tool and acceptance give identical
  refusals on the same file, and that running the tool leaves the run's
  state and the file unchanged.
- A member with two unrelated defects is reported with both in one run.
- Quotation fixtures: a path-only citation that is unique passes; one not
  found is refused with its location and no proposal; an ambiguous one is
  refused with one proposed attribution and context per occurrence, and
  passes once a proposed line is pasted; a draft with several ambiguous
  quotations gets a list for each of them in one run; a passage with more
  occurrences than the limit gets a request to expand the quotation and no
  list; a citation in
  the old complete form still passes; altered content fails.
- The ambiguity measurement of step 3, recorded with its counts.
- Targeted `commonplace-validate` passes for the changed instructions and
  the command reference.
- Bytes of the worker's quotation and validation rules before and after.

Fixtures show that the tool behaves as specified. They do not show that
analysts use it or submit fewer refused outputs.

## Revisit condition

Carry this into the decision record with a literal `TODO` marker.

**TODO: revisit the analyst acceptance check and path-only quotation** after
the first few analyses under them, or earlier if one of these is observed:

- refused outputs at acceptance for failures the tool would have reported,
  which means analysts do not run it or do not act on it;
- analysts presenting a passing check as evidence that findings are correct;
- quotations not found at a rate near the old batch failure rate, which
  would mean retyping the passage is itself the problem;
- readers or reviewers needing line ranges that citations no longer carry;
- analysts writing ranges or revisions by hand.

Count per job: check runs before submission, refusals at acceptance,
quotations written, not found and ambiguous. The alternatives to weigh are a
tool that completes citations in the draft, and designation by position with
a numbered view; the [design review](./quotation-design-review.md) describes
both.

## Records

- **Result record:** one file in this directory, written as work proceeds:
  what was implemented, each executor choice with its reason, the ambiguity
  measurement, other measurements, deviations and what remains.
- **Decision record:** one ADR, numbered when written, after implementation.
  It revises the clauses of ADR 094 on the citation constructor and
  authoring-time checking and keeps its uniqueness rule. It states what was
  given up and why, names consumption paths and considered alternatives, and
  keeps the `TODO` revisit marker.
- **Commits:** the repository's commit rules, with `Workshop:`, `Decision:`
  and `Model:` trailers where they apply.
