# Motivation, alternatives and pre-decision checks

Record of the reasoning behind the [collection design](../../collection-design.md),
kept as source material for the decision record. The text below was written
before the operator's decisions of 2026-10-03 and is not design. Where it
names a choice as open, the collection design's Decisions section governs.
The checks it describes were run; their results are the measurement files
beside this one.

## Motivation

Analysis workers fail parts of their jobs. The audited runs show refused
submissions, retries, rules read and not applied, wrong-path reads and
classifications returned by reconciliation; see the
[fresh-run audit](../../analyse-agentic-system-amendments/history/fresh-run-audit.md), the
[second-run audit](../../analyse-agentic-system-amendments/history/second-run-audit.md) and the
[Sol run follow-up plan](../../analyse-agentic-system-amendments/sol-run-follow-up-plan.md). The operator's response
is to simplify the analyst's job. The split serves that goal: an analyst should
hold only the analysis. Fewer bytes are one part of the simplification. The
larger part is complexity: how many concerns an analyst must hold, how many
references it must resolve, and how many instructions it must reconcile.

The system must also be coherent: the instructions a worker receives must agree
with the doctrine that binds it. Today the root doctrine requires every writer
to read the collection contract, and the job packets omit it. No observed job
resolved that contradiction cleanly. A contradiction is a complexity cost by
itself, and it is sufficient reason to change the structure. The context
argument below explains why the repair should be a small analysis-only
contract and not the full shared one.

The operator's working hypothesis is that analysis jobs are context bound.
The binding limit is not the provider window. It is the
[soft degradation boundary](../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md):
the point at which a worker misses instructions or leaves context unused while
its output stays fluent. That note names three pressures that move the
boundary: volume, interference and complexity. Analysts already carry a heavy
load of all three from the task itself. They trace source behavior, apply
several distinctions, preserve evidence and produce mutually consistent
records. The design objective is therefore to remove every mandatory input
that does not serve the assigned job, and to try each available reduction.

The current collection contract adds to each pressure:

| Pressure | Current cost | Effect of the split |
|---|---|---|
| Volume | Every writer of a collection member must read the 13.7 KB contract of `kb/agentic-systems/`. | The draft analysis contract is 2.2 KB. The modelled saving is 11.5 KB per job, 14–30% of the mandatory method files, by role. |
| Interference | That contract also governs reviews, comparisons, method authoring, publication and outbound linking. An analyst must hold those rules and rule them out. | The analyst's contract contains only rules for analysis members. Rules for other artifact classes cannot enter it later. |
| Complexity | The root doctrine tells writers to read the target collection contract, but packets do not supply it. Each worker must [resolve the reference itself](../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) and decide whether the root rule or the packet's reading list governs. The contract then mixes analysis rules with publication, review and comparison rules that the worker must separate. | Each packet supplies the contract as a literal `read-first` path, so the root rule and the packet agree. The contract addresses one concern, analysis. Publication stays in `kb/agentic-systems/`. |

Interference is the argument for a separate collection. Shortening the shared
contract can recover much of the volume, and a packet entry removes the lookup
without any relocation. But a contract shared by several artifact classes must
keep rules for each of them, so only separate ownership leaves the analyst with
no rules for other classes. The volume saving is real but modest, and it is not
the reason to prefer the split over shortening.

The contract is a small share of an analyst's mandatory input, so the split
alone removes a small share of the job's complexity. Its lasting effect is the
boundary: the analysis collection and the analyst packets address analysis
only, and publication, comparison and method authoring cannot add rules to
them later. Whether that reduction is real must be measured on the analyst
jobs themselves, not on the contract's size; see the check below.

The retained records show the current structure failing in every observed
job. The root doctrine requires the contract read, and each job packet gives an
explicit reading list that omits the contract. The two instructions
contradict each other, and workers resolved the contradiction differently:

- In the two Dynamic Cheatsheet runs, all 30 worker sessions had the root rule
  in context and none read the contract. Both accepted sets were written
  outside the required write path, and no check detected it.
- In the stopped Graphiti run, both parallel analysts tried to follow the
  rule, guessed a wrong path, and then read the whole contract.

No observed job produced a clean read. A general rule that a specific packet
silently contradicts is itself an interference cost: the worker must decide
which authority governs, and the system cannot tell which choice it made. The
root delegation rule already forbids this: a parent may omit a supplied rule
only after verifying delivery. The repair is to make the packet and the
doctrine agree, and a small contract makes agreement cheap enough to keep the
reading rule without an exception.

The records do not support a volume explanation. Peak worker context in the
Dynamic Cheatsheet runs was 18–44% of the provider window. Refused submissions
did not concentrate in the largest contexts, and retries passed at about the
same size. The recurring lapse was a rule read and not applied when writing,
such as the prohibition on record ranges in the
[fresh-run audit](../../analyse-agentic-system-amendments/history/fresh-run-audit.md). It stopped in verification jobs once
their packets stated the rule conspicuously, and it then appeared in
reconciliation and synthesis, whose packets did not. This supports the
interference and complexity pressures, in two runs of one source on one model.
It does not establish that the contract's content caused any analytical error,
because no worker in those runs loaded it.

The collection contract is the smallest mandatory method input. Role files are
24–69 KB per job in the [input coverage draft](./input-coverage.md).
The same three-pressure check applies to them and is likely to yield more. That
work is separate from this proposal and does not depend on it.

## Observation

Observed in the stopped run `AAS-2026-10-03-graphiti-05`: both parallel
analysts guessed `kb/agentic-systems/reports/COLLECTION.md`, received a
missing-file error, located the real contract and read it whole. The cost
was two failed calls and two 13.7 KB reads. Anchors are in the
[Sol run follow-up plan](../../analyse-agentic-system-amendments/sol-run-follow-up-plan.md), item 1.

That plan's item 1 would supply the whole contract in every job packet.
This fixes discovery but makes the full reading cost routine. It is a valid
immediate repair, not necessarily the desired permanent input structure.

## Alternatives

**Shorten the existing contract.** Extract specialist authoring, maintenance
and migration procedures into separately loaded instructions. This can reduce
mandatory input without relocation. It retains one shared contract for several
artifact classes, so keeping irrelevant rules out of analyst input requires
continuing discipline across those consumers.

**Separate the analysis collection.** Preferred for the operator's optimization
priority: give workflow-produced analysis artifacts their own small contract
and a boundary against unrelated input growth. Relocation and ownership changes
are costs to manage, not reasons by themselves to retain a costly input
structure. The contract prototype must demonstrate the expected reduction.

**Exempt workers from the collection read.** A narrow, explicitly authorized
exception could reduce input immediately, but adds a special consumption rule
and requires another account of how workers receive all binding requirements.
It is not adopted here and must not appear as an implicit stopgap.

## Checks defined before the decision

The soft boundary is not directly observable and is not one stable number, so
no byte count shows that it was relieved. Check each pressure separately, then
check outcomes in a live run.

**Volume.** Measure the complete mandatory packet for each role before and
after, so that moving text into another always-loaded file cannot count as a
saving. Draft the shortened single contract and measure the same packets with
it. Do not compare the split against the unshortened incumbent alone. The
[input coverage draft](./input-coverage.md) holds both
measurements.

**Interference.** For each clause a worker must read, name the decision in that
worker's output that the clause governs. A clause with no such decision moves
to a type, a role instruction or a coordinator input. Run the same check on
the shortened candidate and count the clauses that address other artifact
classes and cannot be removed. Prefer the split if that count stays above
zero. Do not omit a binding rule to pass this check: confirm that each removed
clause is loaded with binding force by every role that needs it.

**Complexity.** Measure the analyst jobs, not the contract. For each analyst
role (boundary, runtime, memory, epistemic) take the complete mandatory packet
and count, for the incumbent, the shortened candidate and the split:

| Measure | What is counted | Target |
|---|---|---|
| Concerns | Activities other than the role's own analysis that the mandatory input gives rules for: publication, public selection, review authoring, comparison writing, method authoring, migration. | Zero |
| Model-resolved references | References the worker must resolve to act: a rule naming a file the packet does not supply, a path the worker must derive, a definition reachable only by following a link. | Zero |
| Authority conflicts | Pairs of loaded instructions that give different answers, so the worker must choose which governs. The root reading rule against the packet's reading list is one. | Zero |
| Output obligations | Required sections, fields, record kinds, controlled classifications and cross-record constraints in the role's output, each with the consumer it serves. | Record; flag every obligation whose only consumer is publication or comparison |
| Composition depth | For each output obligation, the number of separate files the worker must combine to satisfy it. Report the maximum and the count above two. | Record |

These counts are judgments. Retain the itemized list behind each count, so a
second reader can dispute an item, and apply one counting rule to all three
candidates. Run the same measures on reconcile, verify and synthesis packets
as a secondary result.

The first three measures are what the split can change. The last two describe
the complexity of the analysis task itself, which the split does not change.
Record them anyway: they show where the remaining complexity sits and give the
baseline for simplifying role files. Report the result per role as "before,
after shortening, after split". If the first three measures are equal for
shortening and the split, the split has no measured complexity advantage for
analysts.

**Outcome.** Run one analysis with the reduced inputs and compare it with the
audited runs. Count failed reads of supplied or derived paths, validation
failures before acceptance, refused submissions and retries, and verifier
rejections, alongside coverage and acceptance. Record them per job, with the rule or
obligation each failure concerns, so that failures can be matched to the
complexity measures of that role. Count separately the lapses in which a
worker read a rule and did not apply it. One run cannot attribute a
difference to the contract, so record the result as an observation. The run
needs separate commission. The operator decides whether a trial run with the
draft contract supplied in the packet precedes relocation, or whether the
first run after the split serves as this check. A trial before relocation is a
scoped exception to the root reading rule and must be authorized as one.

If the shortened contract reaches the same concern, reference and conflict
counts for analyst roles as the split, choose shortening. If the split's
counts are lower, state the difference per role in the decision. If sufficiency and
reduction conflict, return the trade-off to the operator before relocation.

Settle current-set/review pins, archive navigation, and sequencing after the
isolation changes are committed. Demonstrate that an accepted analysis is
readable through its report or overview without the generated review; that
comparison consumers can resolve the selected set and provenance; and that
unaccepted work remains unpublished. Check initial publication, replacement,
and interrupted link updates without changing accepted bytes. These are
migration obligations, not evidence against input optimization.

