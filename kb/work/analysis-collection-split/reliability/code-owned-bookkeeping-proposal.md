# Code-owned bookkeeping proposal

Agent draft, 2026-10-04, at the operator's request. Awaiting adoption.
Authorizes nothing.

## Revise after named record IDs

The operator decided on 2026-10-04 to implement
[short named record IDs](./short-named-record-ids-plan.md) first. Revise this
proposal against the implemented state before adopting it:

- Record ID allocation stops being bookkeeping. Choosing a name needs
  judgment and stays with the analyst; drop it from the candidates below.
- A code-supplied record index for reconciliation and verification gains a
  second purpose: names lose the order and count that numbers gave, so the
  index is what shows that every record was covered.
- Recount the obligations per role; the range rules and their guidance are
  gone for record IDs.

## Problem

Analysts do two kinds of work in one output. Semantic work has no unique
right answer: tracing a mechanism, judging what evidence supports. Bookkeeping
has exactly one right answer given the inputs: copying an identity field,
numbering a record, formatting a selection file.

The KB's argument is that these fail differently.
[Scheduler-LLM separation](../../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)
notes that bookkeeping can be fully specified and checked by a hard oracle,
yet models still make residual errors on it. Each bookkeeping obligation also
adds to the worker's load without adding analysis. An obligation that code
performs cannot be done wrong by the worker and costs the worker no input.

Observed bookkeeping failures: a selection batch with a missing key and an
empty selection; frontmatter with broken YAML indentation; ID ranges; a ledger
column filled with the wrong category of reference; wrong-path source reads.
All were recovered or caught, each at the cost of a retry or a correction.

## Current state (as of 2026-10-04)

Code already owns some bookkeeping: quotation citations and line ranges,
reading batches and oversized-file ranges in the packet, the amendment index,
the manifest and its hashes, and assembly of the set.

Workers still perform, and code then checks:

- **Identity fields in member frontmatter.** The worker copies `run-id` and
  `reviewed-boundary`; `pass_refusals` refuses a mismatch.
- **Record ID allocation.** The worker numbers its records under its prefix;
  code refuses wrong prefixes and duplicates.
- **The quotation selection file.** The worker writes the JSON by hand.
- **Source path discovery.** The worker finds or guesses file paths in the
  frozen checkout.
- **Frontmatter as YAML text.** The worker writes nested YAML by hand.

Not yet established: which of each role's other output obligations are
bookkeeping. The [complexity measurements](../evidence/complexity-measurements.md)
list every output obligation per role with its consumer, in
`evidence/complexity-measurements.json` under `obligations`. That list is the
inventory to classify.

## Proposal

1. **Classify every output obligation** in that inventory as semantic,
   bookkeeping, or mixed. Bookkeeping means: given the job's inputs, exactly
   one correct value exists and code can compute it.
2. **For each bookkeeping obligation, choose the cheapest form that removes
   it from the worker:**
   - *Code writes it.* The worker omits the field and code adds it at
     acceptance. Candidates: identity fields in frontmatter.
   - *Code supplies it.* The packet or a scratch file carries a computed
     input. Candidates: an inventory of files in the frozen checkout; for
     reconciliation and verification, an index of every declared record with
     its kind, member and part relation.
   - *A command produces it.* The worker calls a helper instead of formatting
     by hand. Candidates: building the quotation selection file; setting a
     structured frontmatter field.
   - *Left with the worker, checked by code.* Where removal costs more than
     the failures do. Probable case: record numbering.
3. **Delete the instruction text** that told the worker how to do each
   removed obligation. The gain is counted in obligations and bytes removed
   per role, using the measures of the complexity measurements.

Mixed obligations stay with the worker. Do not split a judgment from its
record merely because part of it is mechanical.

## Constraints

- A frozen member is byte for byte what code accepted. If code adds fields,
  it adds them before acceptance, and validation judges the result.
- No obligation moves to code if computing it needs a judgment. A wrong
  computed value is worse than a refused one, because nothing rejects it.
- Supplied inputs count against the worker's read budget. A file inventory or
  record index must replace discovery work, not add to it.

## Check before adoption

Classify the obligations of two roles first, memory and reconcile, and count
how many are bookkeeping. If the count is small, stop: the gain does not
justify the change, and the remaining load is semantic. If it is material,
build the two cheapest removals and compare refusal counts and packet
measures on the next commissioned run against the recorded baseline.

A fixture shows that code computes the value. It does not show that analyses
improve.

## Costs and risks

- More workflow code and tests to maintain for a research method that is
  still changing.
- Code-written fields change the member type contracts and their templates.
- An input computed by code can be stale or wrong for an unusual source, and
  the worker may trust it. The file inventory must come from the frozen
  checkout the run registered, not from a search at another revision.
