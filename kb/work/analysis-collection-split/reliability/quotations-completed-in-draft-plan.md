# Quotations completed in the draft: implementation plan

## Commission

Written on 2026-10-04 at the operator's request, from the
[quotation design review](./quotation-design-review.md). The operator adopted
its recommended design, including the replacement of quoted text. This file is
the commission for the executor the operator launches on it. The launch is the
authority to implement; this file alone starts nothing.

It is separate from the [collection-split plan](../plan.md) and the
[named record IDs plan](./short-named-record-ids-plan.md). It does not
authorize an analysis run or the regeneration of any system.

## Intent

An analyst should quote the way a person does: copy the passage into the
report and say where it is from. Code should do everything that has one right
answer: confirm the passage is in the frozen source, find its lines, and
write the citation in the standard form.

Today a quotation takes four steps. The analyst copies the passage into a
selection file, calls a helper, and copies the returned citation into the
report. Exact source text passes through the analyst's tools twice, and in
batch mode through hand-written JSON as well. In the retained traces about
35% of batch calls failed against about 5% of single calls, and the one
refused output for a quotation came from the second copy. The batch mode
exists because analysts need to resolve many quotations with few calls; it
was added after they built their own loops.

The change serves both needs at once. The draft becomes the batch: every
quotation is written once, where it is used, and one helper call completes
all of them.

When a choice is not settled here, choose what leaves the analyst less to
do and to learn, without weakening any invariant below.

## End state

- An analyst writes a quotation in its draft as a blockquote of the passage
  followed by an attribution line that names only the source path:

  ```text
  > for line in data:
  >     file.write(json.dumps(line) + "\n")
  > --- `run_benchmark.py`
  ```

- One helper call on the draft completes every such quotation: it finds the
  passage in the frozen source, replaces the block's text with the exact
  source text, and completes the attribution with the line range and
  revision, in the citation form accepted today.
- A passage that does not occur is reported with its location in the draft
  and left exactly as written. A passage that occurs more than once is
  reported with its candidate ranges; the analyst adds the chosen range to
  the attribution, and the helper checks that the passage occurs there.
- Running the helper again on a completed draft changes nothing.
- The JSON batch mode is gone from the helper, the worker rules and the
  command reference. The worker rules for quotation are shorter than today.
- A submitted member with an uncompleted quotation is refused with a message
  that names the block and the command to run.
- Acceptance checks every quotation against the frozen source as it does now.
- Required tests and validation pass. A decision record and a result record
  exist.

The first analysis run under the new form is the outcome check. It needs its
own commission.

## What must stay true

- Every quotation in an accepted member is verbatim text of the frozen
  source, with the correct path, line range and revision.
- The analyst chooses the passage and judges whether it supports the finding.
  A completed citation proves occurrence, not support.
- Code computes every line range and revision. An analyst never calculates a
  range; choosing among ranges the helper printed is allowed.
- **A misremembered or altered quotation fails loudly.** The replacement
  changes whitespace only. A passage that differs from the source in any
  other character is not found and is left untouched. Do not add fuzzy
  matching, nearest-match repair or any correction of quoted content.
- The uniqueness rule of
  [ADR 094](../../../reference/adr/094-quotations-require-a-unique-occurrence-or-a-containing-range.md)
  holds: one occurrence in the eligible region, or one inside a given range.
- The helper edits only quotation blocks. All other text in the draft is byte
  for byte unchanged.

## Why the quoted text is replaced

Operator decision, 2026-10-04. Acceptance does not need it: both the helper's
search and the acceptance check collapse whitespace before comparing. The
replacement is kept for three reasons. A published quotation shows the
source's exact characters, and indentation carries meaning in languages such
as Python. The same passage yields identical bytes whoever quotes it, so
differences between runs reflect the analysis. And the block shows exactly
the text at its cited range. Keep this reasoning in the decision record.

## Boundaries

- **Analytical content and evidence rules are unchanged.** This changes how a
  citation is produced, not what counts as evidence.
- **No designation by line number.** An analyst does not name a passage by
  position. A wrong position returns a genuine passage that is not the
  intended one, which is a quiet error.
- **One documented route.** Do not keep the old selection-file route in the
  worker rules beside the new one. Whether the single-passage command stays
  in the helper for other uses is the executor's choice; no worker
  instruction teaches it.
- **Frozen sets are unchanged**, and citations already in the completed form
  stay valid.
- **No net growth of worker input.** Measure the quotation rules before and
  after.
- **Other sessions edit this repository.** Start from the committed state,
  which includes named record IDs. Check status before each commit and stage
  only this work's files.
- **Repository rules apply**, as in the collection-split plan.

## Priorities and partial results

The completion mode with its round-trip test comes first; nothing else can be
judged without it. Then the worker rules and the removal of the batch mode
together, so that workers are never taught a route that no longer exists or
left without one. Then the refusal for an uncompleted quotation.

If work stops early, the helper and the worker rules must agree on one route
and required checks must pass. A state in which the batch mode is removed and
the completion mode is not usable is not acceptable. Record what remains.

A negative result is a result. If the round-trip test cannot be made to
pass, report why; do not loosen it.

## Supported route

One workable route. Take another if it reaches the end state while keeping
what must stay true, and say what you changed.

1. **Fixed: establish the round-trip test first.** Take the retained members
   as read-only input. Copy them, strip the line range and revision from
   every citation, run the completion on the copies, and require
   byte-identical members back. This is the acceptance test for the mode and
   needs no model. It also shows how many passages are ambiguous without a
   range. It is fixed because it is the only cheap evidence that completion
   reproduces what code generates today.
2. Build the completion mode on the existing matching and rendering code:
   `parse_blockquotes`, `quote_occurrences` and `render_quote`. Cover a
   passage with altered whitespace, a passage not found, an ambiguous passage
   with and without a chosen range, an already completed citation, a
   blockquote that is not a quotation, a capture source, and several
   quotations of one file.
3. Rewrite the Quotation section of the worker rules and the related
   passages of the source contract and the boundary job. Remove the batch
   mode from the helper and from `kb/reference/commands.md`.
4. Refuse a submitted member that contains an uncompleted quotation, naming
   the block and the command.
5. Check the design against ADR 094. That record says the author inserts the
   generated citation unchanged and that no authoring-time source-check
   command is required. The decision record for this work revises those
   clauses and keeps the uniqueness rule.
6. Measure, verify, write the decision record and the result record.

## Left to the executor

The option name and report format of the completion mode; how a block's
location is reported; the stub form for a capture source, which has no
commit-relative path; whether the path may be omitted when the passage is
unique across the source; whether the helper writes the draft in place or to
a new file; exit statuses; test structure; wording of the rules; commit
granularity.

## Return to the operator

Stop and ask when:

- the round-trip test cannot be made byte-identical for the retained members;
- completion would need to change text outside quotation blocks, or correct
  quoted content beyond whitespace;
- a stub cannot be told apart from an ordinary blockquote without a new
  marker in the analyst's text;
- another consumer of the batch mode appears;
- the change conflicts with a decision record other than ADR 094;
- worker input grows in net.

Otherwise proceed without asking.

## Verification

- `uv run pytest -q` and `uv run ruff check .` pass.
- The round-trip test passes on every retained member that contains
  quotations.
- Targeted `commonplace-validate` passes for the changed instructions and the
  command reference.
- A member with an uncompleted quotation is refused; the same member after
  completion is accepted by the existing quotation check.
- The helper run twice yields the same bytes as run once.
- Bytes of the worker's quotation rules before and after.

Fixtures show that the helper behaves as specified. They do not show that
analysts quote with fewer failed calls; that is for the first run to show.

## Revisit condition

Carry this into the decision record with a literal `TODO` marker.

**TODO: revisit draft-completed quotations** after the first few analyses
under them, or earlier if one of these is observed:

- "not found" reports at a rate near or above the old batch failure rate,
  which would mean retyping the passage is itself the problem;
- analysts editing a completed citation by hand;
- completion altering text outside a quotation block;
- analysts building their own loops or selection files again;
- ambiguous passages costing more calls than before.

Count per job: quotations written, completed on the first call, not found,
ambiguous, and refused at submission. If retyping proves to be the problem,
the alternative to weigh is a helper-supplied numbered view with designation
by position, which this plan rules out for now.

## Records

- **Result record:** one file in this directory, written as work proceeds:
  what was implemented, each executor choice with its reason, the round-trip
  result, measurements, deviations and what remains.
- **Decision record:** one ADR, numbered when written, after implementation.
  It revises the affected clauses of ADR 094, states the three reasons for
  replacing quoted text, names its consumption paths and considered
  alternatives, and keeps the `TODO` revisit marker. The
  [design review](./quotation-design-review.md) holds the alternatives.
- **Commits:** the repository's commit rules, with `Workshop:`, `Decision:`
  and `Model:` trailers where they apply.
