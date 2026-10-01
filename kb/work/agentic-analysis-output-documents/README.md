# Smaller authoritative outputs for agentic-system analysis

## Commission and intended outcome

On 2026-09-27 the operator commissioned this workshop after reviewing the size
of the main analysis skill, its output types and completed results. The agreed
direction is to replace the monolithic exact result with smaller authoritative
documents, with one owner for each finding and evidence passage. The purpose
is to reduce duplicated writing and reading, simplify the skill and types,
and preserve the ability to produce evidence-grounded comparisons and summaries.

This workshop owns the output design, the corresponding division of
responsibility between skill and types, and bounded acceptance trials. Later
on 2026-09-27, after a survey of the five governing files, the operator
directed that it start by cleaning up the whole procedure and removing
redundancies, under one rule: types specify what the produced documents
contain, instructions and skills specify how they are generated. Partition
design follows the cleanup. Creating the workshop does not itself change the
shipped publication contract. The exact document boundaries,
contracts and transition remain to be worked out here. Keeping the full
integrated result alongside its new components would not meet the intended
outcome.

## Starting evidence

Measurements from the current files on 2026-09-27, counting whitespace-separated
words:

| Instruction or type | Words |
|---|---:|
| Main analysis skill | 5,420 |
| Main result type | 4,409 |
| Epistemic instruction | 3,432 |
| Memory instruction | 1,140 |
| Memory report type | 929 |

| Completed run | Exact result | Local memory report |
|---|---:|---:|
| `AAS-2026-09-27-dynamic-cheatsheet-01` | 8,993 | 5,063 |
| `AAS-2026-09-27-mem0-01` | 10,962 | 5,141 |
| `AAS-2026-09-27-napkin-02` | 12,503 | 6,843 |

These are document sizes, not measured duplicate-word counts. Napkin's shared
records alone contain about 7,032 words. Its memory report is integrated into
the exact result, while its public review is a separate compact projection.
The [rerun audit](../agentic-memory-refresh/reliability-rerun-20260927.md)
records twelve truncated worker read deliveries with subsequent recovery.
The main skill read exceeded the outer delivery limit by only 218 reported
tokens; several other batches exceeded their chosen shell limits by thousands.
This establishes read friction, not context exhaustion or proof that splitting
documents will improve analysis quality.

## Candidate organization and constraints

Start by testing an overview plus runtime, memory and epistemic reports.
The overview would identify the frozen source and report set and retain the
principal conclusions and limits. The other reports would own their evidence
and findings. Another report would reference an owned finding and add its
interpretation rather than copy the record. The memory specialist's report
could become an authoritative retained component after reconciliation.

This is a candidate partition, not a fixed four-file requirement. Shared
objects and routes cross analytical boundaries; decide how their identity,
ownership, amendments and references work before defining the document types.
Do not replace the large result with an equally large common-record document
without demonstrating a useful reading and ownership boundary.

Preserve these properties:

- One frozen source boundary and one coherent completed analysis govern the
  report set. Public evidence remains usable from a clean checkout.
- Runtime analysis and both proportionate lenses remain required. The fresh
  memory specialist remains part of the workflow; splitting documents does
  not require additional agents.
- Quotations, evidence strength, uncertainty, scoped absence and conflicting
  findings remain inspectable. Reconciliation must not silently strengthen a
  specialist's conclusions.
- Memory comparisons preserve per-value evidence and coverage assessments.
  Statistics and qualitative summaries read authoritative reports directly,
  without reconstructing the old format or inferring from compact reviews.
- Output restructuring preserves historical results. Citation migration is
  separately part of implementing the quote occurrence proposal, as the
  operator confirmed on 2026-09-27; the preservation rule does not block that
  migration or its dependent hash updates. Design fixtures and citation
  migrations are not fresh analyses and do not advance corpus-refresh coverage.

## Ownership rule

Types own artifact requirements: sections, fields, controlled values, field
semantics (what a status value, a route guarantee or a decision role means),
and output regimes, including complete, blocked, out-of-scope, and brief or
full accounts where applicable. The skill and the instructions own how the
artifact is produced: work sequence, delegation, loading order, judging norms
(evidence layers, when a layer may not be upgraded, misuse guards, how to
handle conflicting findings), recovery and publication.

Analytical guidance splits along the same line. A passage that both defines a
field and tells the worker how to judge it is divided: the type states the
meaning, the instruction states the judgement and cites the type. Every
produced document has a type contract, and a type never cites an instruction
for its semantics. Each judging norm has one authoritative home, and the skill
says when to load it.

Moving repeated paragraphs between those homes is not a reduction by itself.
The cleanup deletes the second statement. Its measure is the total word count
across the five governing files together with no requirement stated twice.

## Starting survey (2026-09-27)

A read of the five files against the ownership rule found, in rough words:
the skill holds about 2,200 words of content specification; the result type
holds about 500 words of procedure; the epistemic instruction's "Required
output" block is about 1,800 words of content specification with no type; and
about 1,800 words in the skill mirror the result type, mostly the skill's
step 3 and steps 4.5–4.9 against the type's record-field sections. Defects
the cleanup must resolve:

- The result type defers its record vocabulary to the skill's step 3 and does
  not enumerate the `target-class` values the skill lists.
- The epistemic ledger and the public review have no type contract; the
  epistemic instruction's output block and the skill's review frontmatter
  paragraph are their only specifications.
- The epistemic instruction relies on an invoking packet the skill forbids,
  and keeps stop branches and a standalone mode the unified run never takes,
  against the skill's rule that both lenses always run.
- The memory instruction says to follow the legacy review's analytical
  progression while forbidding loading the legacy material.
- Nothing tells the coordinator to read the epistemic instruction before
  steps 3–4, although step 4's route records feed the ledger.
- Quote rules, full-ID rules, scoped-absence rules, the blocked regime and
  the specialist-integration rule each appear in three to five files.

## Cleanup progress (step 1)

Extractions committed on 2026-09-27, each alone, in the order planned. All
five files, the three retained results named above, and a local memory
report validated after each.

| File | Start | After 1 | After 2 | After 3 | After 4 | After 5 | End |
|---|---:|---:|---:|---:|---:|---:|---:|
| Main analysis skill | 5,445 | 4,433 | 4,138 | 3,962 | 3,946 | 3,946 | 3,487 |
| Main result type | 4,605 | 4,775 | 4,856 | 4,802 | 6,134 | 6,174 | 6,145 |
| Epistemic instruction | 3,432 | 3,432 | 3,432 | 3,371 | 1,536 | 1,536 | 1,465 |
| Memory instruction | 1,184 | 1,184 | 1,184 | 1,088 | 1,088 | 742 | 738 |
| Memory report type | 1,035 | 1,035 | 1,035 | 918 | 918 | 876 | 866 |
| Total | 15,701 | 14,859 | 14,645 | 14,141 | 13,622 | 13,274 | 12,701 |

1. Theory-route vocabulary: skill step 3 keeps judging norms and register
   ownership; the type owns the definitions, guarantee-strength values and
   `target-class` values, and no longer defers to the skill.
2. Runtime fields: skill step 4 names the record it writes and points at the
   type's Runtime account, Routes, Components and preflight fields.
3. Quotations: the result type's Source register is the one home for the
   quote contract; the memory report type and the epistemic instruction cite
   it; tool behaviour lives in the command reference.
4. Epistemic lens: the instruction is overlay-only, invoked by every run, with
   no standalone mode, packet reference or stop branches; the type's Lens
   outputs section owns the six blocks, their fields and controlled values,
   and the Source register owns the evidence-layer definitions. The result
   type is now the largest file at 6,134 words; step 2 partitions it.
5. Memory pair: the instruction keeps commission, source handling, quote
   generation, classification norms and return protocol; the report type
   owns the section contents, and the result type's comparison contract owns
   the curation-operation definitions. The report type's Integration contract
   is deleted; the skill's steps 5 to 8 already state that procedure.

Resisted the rule: the Git inspection commands and the truncation rule appear
in both the skill (step 2) and the memory instruction, because the worker
does not load the skill and the two actors inspect the same frozen source.
A shared source-inspection instruction both would load is the clean answer;
left for step 2, where the worker set may change.

6. Cross-cutting sweep: the blocked regime, evidenced-absence content and
   full-ID rule are stated once in the result type; the skill sends a blocked
   or out-of-scope run to step 7, keeps one absence-judging norm, and states
   specialist integration once in step 6 and prior-analysis exposure once in
   step 1.

7. Independent duplicate hunt: a fresh Opus reader audited the five files
   against the rule and found twelve restatements, one type deferring to an
   instruction for which fields a lens owns, four tooling or integration
   sentences inside the types, and one dangling phrase; all were removed or
   rephrased as content (commit `70ce51e9`).

Accepted per-actor duplicates, not counted as violations: the Git inspection
commands, the truncation rule and the quote-generation procedure appear in
both the skill and the memory instruction because the worker does not load
the skill; the coordinator and the worker each have their own agent-listing,
notification and exit-status rules.

Open items for step 2, from the hunt and the plan:

- The public review keeps `type: types/note.md`; the skill's step 8 lists
  its frontmatter fields because no type owns them, and the collection
  contract holds the rest. A dedicated review type waits for the partition.
- The result type's paragraph on how CSV readers count values and assess
  coverage describes consumer processing rather than document content; it
  belongs with the consumer contracts the partition redraws.
- The result type's "selected by the producing skill" phrases for runtime
  routes and checks hand selection, not meaning, to the skill; left as is.
- The transfer-scan disposition sentence in the result type and the
  side-channel sentence in the report type are routing rules of marginal
  procedural character; left as is.

The [regression test](./cleanup-rerun-test.md) ran on 2026-09-27 and its
[record](./cleanup-rerun-20260927.md) reports no gap: no worker asked for
missing instruction content, invented a controlled value, or followed a type
pointer that lacked what the step needed, across four audited traces. All
three runs validated, published and passed the independent handoff. Step 1
is accepted on that basis (operator, 2026-09-28). Two findings carry over:

- Two profile classifications the type still requires were dropped while
  their prose survived: `other-compiled` lineage in Dynamic Cheatsheet and
  `promote` curation in Napkin. Structural validation cannot catch a value
  the frontmatter omits but the body supports. Step 2's consumer contracts
  need a semantic check for profile values against the records they cite.
- The test froze the source pin but not the functional scope, so two pilots
  chose narrower boundaries than their baselines and breadth could not be
  compared. Step 4's trial fixes the functional scope alongside the pin.

An independent Opus review of the six governing files on 2026-09-28 found
no flat contradiction and a dozen line-level defects, applied in one commit:
step 4 no longer asks for specialist findings before the specialist runs;
the skill no longer claims the run state binds the memory report hash; the
result type's table and template carry `memory-comparison`; the report type
has a template fixing level-two headings and lists prior-analysis exposure
as a blocked cause; a blocked or out-of-scope run now has a stated completion
path and skips steps 2 to 6; the curiosity pass has a destination; the
run-state type stops repeating the skill's failure and incumbent rules; and
one term, local proposal ID, replaces four. The reviewer's overengineering
findings (unexercised probe capsules, reader rules for CSV consumers,
supervisor choreography) are recorded for the partition; the supervisor
text stays because it encodes tested recovery. Five-file total after the
review: 12,795 words.

A separate consequence, handled outside this workshop: every worker wrapped
the quote generator in a per-quote loop, so `commonplace-quote` gained a
`--selections` batch mode (`e984a460`), verified by a specialist-only trial
in the memory-refresh workshop.

## Step 2 progress

The [partition candidate](./partition-candidate.md) (2026-09-28) settles
the ownership model first: one run namespace, each record declared once in
the member that established it, each evidence passage once in the member
whose finding it supports, amendments attached to the declaring member,
bare-ID references resolved through the overview's manifest. It proposes
four members (overview, runtime, finalized memory report, epistemic), a
manifest-chained completion rule with explicit rejection cases, and a
scripted fixture split of two retained results as the next test.

The [fixture split](./fixture-split-20260928.md) (2026-09-28) ran on the
Napkin and Dynamic Cheatsheet results: no duplicated declaration, no
duplicated passage, every reference resolving, the dropped memory lens
section a verbatim copy of the specialist's paragraphs, and the
coordinator's versions of specialist records reducible to their deltas. It
adds three contract rules: finalization appends deltas; amendments attach
to the declaring member while cross-lens annotations live in the annotating
member keyed `On <ID>`; the overview holds the only source register. It
also found that specialists re-declare seeded records with the proposal
heading form, which the report type must turn into annotation headings.

The [draft contracts](./contracts/README.md) (2026-09-28) cut the cleaned
result type into five members. Words: overview 2,018, runtime 1,697, memory
report 1,767, epistemic 1,472, generated review 343; 7,297 together against
7,011 in today's result and report types, so the contract text is
redistributed rather than grown, and the largest contract is a third of
today's result type. Decisions the drafts embed, to confirm before step 3:
the overview owns every set-wide convention and the `members` manifest;
records declare at heading level four under level-three kinds, annotations
as `#### On <ID>`, amendments as `Amendment:` paragraphs under the
declaring record; probe capsules move to a `## Probe evidence` section of
the runtime report; the memory report gains `finalized-from` and a
finalized-only `## Amendments` section and carries the comparison contract;
the review gets its own type under `kb/agentic-systems/types/` pinning
`analysis-overview`. Step 2 closes when the operator confirms these and the
three open choices in the candidate, after which step 3 plans the code and
consumer transition.

The operator confirmed the embedded decisions and the three open choices on
2026-09-28: no split of the runtime report yet, the review's pin field is
renamed `analysis-overview`, and the finalized memory member keeps the
specialist's section order. Step 2 is closed; step 3 opens with a consumer
inventory against the live code.

## Step 3 progress

The [consumer inventory](./consumer-inventory-20260928.md) (2026-09-28)
lists every reader of the result, the review pin, the run state and the
memory report, with the literals, the identifier and quote checks, and
the tests that pin them. Its decisive finding: only three of forty
generated reviews load under today's contract, so the matrix build
already fails on the corpus and historical results are already retained
bytes rather than loadable inputs. The [transition plan](./transition-plan.md)
fixes the producer, validator and consumer changes in eight ordered
commits, proposes no compatibility code and no migration, and leaves
three items to the operator: that decision, whether init repins by
cascade or freezes retained directories, and the trial target's class.

## Work sequence and decision points

1. Clean up the current procedure before drawing any partition. Working from
   the survey above, assign every requirement in the skill, the two
   instructions and the two types to one home under the ownership rule, and
   delete the other statements. Give the epistemic ledger and the public
   review a type contract, decide whether the epistemic instruction keeps a
   standalone mode, resolve the listed contradictions, and make the loading
   points explicit. Edit the live files in place without changing the shape
   of the produced documents, so retained results still validate. Record a
   before and after word count per file, and record any requirement that
   resisted the rule as an open choice for step 2. Start with the largest
   overlap, the skill's step 3 and steps 4.5–4.9 against the result type's
   record-field sections.
2. Produce a concrete candidate partition and smaller draft contracts inside
   this workshop, from the cleaned files. Identify evidence ownership and
   actual consumer dependencies. Use retained results as structural fixtures to test shared
   findings and cross-report references. Before implementation, settle which
   documents are authoritative, how completion identifies the set, and how
   readers reject missing, changed or mismatched members. Revisit the partition
   if it merely relocates the bulk or creates substantial duplicate records.
3. Plan the bounded producer and consumer transition from that candidate.
   Inspect live code before fixing implementation details. Publication,
   handoff, comparison, synthesis and transfer readers must agree on the
   completed evidence set. Keep trials isolated from published incumbents
   until the replacement contract can be verified.
4. Trial the resulting workflow on a bounded source-grounded case, then test
   downstream readers and inspect session traces. Choose the case after the
   candidate exposes the uncertainty it must resolve. Fresh analysis workers
   receive source-only inputs; prior results and this audit belong to the
   evaluating coordinator. Replan after that trial before expanding coverage.

## Acceptance and closure

The cleanup step is accepted when the five files validate, every requirement
has one home under the ownership rule, no type cites an instruction for its
semantics, every produced document has a type contract, the listed
contradictions are resolved, the loading points are explicit, and the total
word count fell rather than moved. This cleanup leaves retained results
unchanged and valid; citation changes belong to the coordinated quote
migration. A cleaned type may still describe the single integrated result
until step 2 replaces it.

Compare the candidate with the baseline on total authoritative output size,
largest document, duplicated evidence or requirements, and instructions each
worker actually loads. Record read truncation, retries, reconciliation effort
and missing or weakened findings. A smaller largest file alone is insufficient;
added coordination cost must be disclosed alongside any reduction.

Acceptance requires valid component artifacts and a verified complete set,
resolving references with preserved evidence and uncertainty. Exercise missing
members, changed bytes, mixed run/source identities and unresolved references;
none may be accepted as a complete analysis. A bounded matrix, table,
statistics and summary trial must recover their claims from that same set.
Check the transfer reader's completion and source-identity assumptions too.
Numerical equality with an older independently authored analysis is not the
criterion; evidence and counting rules must remain recoverable.

Close when the design is settled, the accepted contracts and consumers are
implemented and validated, bounded producer/consumer trials and trace checks
are recorded, and the corpus-refresh workshop has the resulting execution
requirements. Promote durable decisions and independently useful acceptance
evidence to their owning collections, then remove this workshop and its index
entry. If the candidate fails acceptance, retain the unresolved choice here
rather than declaring the reorganization complete.

## Coordination and starting paths

- [Analysis construction](../analyse-agentic-system/README.md) retains the
  original methodology and trial history. This workshop owns the newly
  commissioned replacement of the single-result organization.
- [Consumer migration](../agentic-analysis-consumer-migration/README.md) owns
  the broader downstream queue. Coordinate the consumers affected by this
  output change; do not start a competing migration.
- [Corpus refresh](../agentic-memory-refresh/README.md) owns inventory and
  scheduling. This workshop does not launch the remaining 159 refreshes.
- [Quote verification decision](../../reference/adr/094-quotations-require-a-unique-occurrence-or-a-containing-range.md)
  owns the citation design and migration. Its implementation will migrate
  citations and update affected integrity records under its migration scope.
  This workshop consumes the resulting uniqueness and range-containment
  contract; it does not define a competing matcher. Freeze instruction, tool
  and input versions for each trial so a concurrent migration cannot silently
  change its evidence baseline.
- Start from the [main skill](../../agentic-systems/instructions/analyse-agentic-system/SKILL.md),
  [epistemic instruction](../../agentic-systems/instructions/analyse-agentic-system/jobs/epistemic.md),
  [memory instruction](../../agentic-systems/instructions/analyse-agentic-system/jobs/memory.md),
  [result type](../../types/agentic-system-analysis-result.md),
  [memory report type](../../agentic-systems/types/agent-memory-analysis-report.md), and live
  publication and comparison code under `src/commonplace/`. The three retained
  results named above are under `kb/reports/retained/agentic-system-analysis/`.

Preserve unrelated checkout edits. If later work is delegated, assign disjoint
outputs and name the intended result, input boundary, acceptance checks and
stop conditions. The coordinator owns integration and recovery. Commit only
when separately requested.

Quote verification migrated the current result format on 2026-09-27, with operator authorization to synchronize current-run copies and hashes. Preserve the corrected citations and pinned source identities when changing the output format. The [migration audit](../../reports/retained/quote-verification-migration/README.md) records the affected runs; superseded runs were left unchanged.

## Cleanup regression execution

The [2026-09-27 cleanup rerun](./cleanup-rerun-20260927.md) records the three pinned analyses, trace audit, baseline comparison and bounded consumer checks.

## Step 3 execution (2026-09-28)

Commits landed on the approved plan: `6f0c5e7b` (run state pins the
overview), `7ae02a4e` (run-state verification reads the set; publication,
loader and bundle moved with it because one fixture serves all three),
`4009cb08` (init treats retained analysis directories as frozen bytes).
The mid-flight direction to move set checks into the validator was
implemented as `6d8d9fd0` and reverted the same day; the operator judged
extending validation from notes to directories an architectural change
and opened [directory artifacts](../../reference/adr/095-directory-artifacts-add-shared-set-validation.md) to plan
it. Remaining for the transition: the skill's steps 1, 7, 8 and 10, the
memory and epistemic instructions, the run-state type prose, the collection
contract, the comparisons README, the two downstream skills, retirement
of the result type with its schema and docs test, the site config's
publication patterns, and the redirect map entry. Worker findings for the
trial: a rejected specialist proposal needs a disposition the mapping
grammar can carry; the finalization check fails on any coordinator
paraphrase of the specialist's body by design; the memory type's quote
minimum is now enforced at set level only.

## Batch 01 follow-ups (2026-09-28)

The first refresh batch (`kb/work/agentic-memory-refresh/batch-01-2026-09-28.md`,
on branch `refresh-batch-01`) published all three sets and recorded the
friction workers met. Astra is simplifying the identifier grammar. Five
further fixes were commissioned:

1. Plain source references are path-only; only quote attributions carry
   line ranges, and a range in a plain reference fails member validation
   with a clear message. Removes the out-of-bounds range failures and the
   binary-file range failure.
2. Drop the overview's `## Run identity` section and its schema patterns;
   the run state and the review pin already record what it projected.
3. Library resolution uses the working checkout's `kb/` when the command
   runs inside a Commonplace source checkout, removing the worktree type
   collision.
4. The quote generator emits no trailing whitespace.
5. Skill step 7 carries one table of member files, types and schemas.

Items 3 to 5 run now in an isolated worktree. Items 1 and 2 edit the same
files as the directory-artifact implementation currently uncommitted on
main and wait for it to land. Batch 02 runs two systems at a time with a
slimmer acceptance record, after all five land.


## Directory artifacts implemented (2026-09-28)

[ADR 095](../../reference/adr/095-directory-artifacts-add-shared-set-validation.md)
now governs the validator and analysis output layout. The directory-artifacts
workshop is closed. Its shared checker includes cross-member declarations
and references; it does not restore exact finalization derivation or a quote
minimum. The batch-01 follow-ups above remain a separate commission.
