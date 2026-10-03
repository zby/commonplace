# Comparison-profile job proposal

## Commission and status

On 2026-10-03 the operator decided to take the memory comparison profile out
of the memory analyst's job and produce it in an additional job. This file,
drafted by an agent, is the design for that decision. The decision to
separate is made, and so is the source-reading rule; see Decided. The
remaining design choices are agent recommendations awaiting adoption. This file authorizes no method edit, relocation or run.

Terms: the **comparison profile** is the `memory-comparison` frontmatter
mapping of the memory report. It classifies a system's memory on ten axes
with controlled values. The **profile job** is the proposed new job.

## Why

Analysis workers fail parts of their jobs, and the operator's response is to
simplify each job. The [complexity measurements](./split-drafts/complexity-measurements.md)
found the profile to be the largest simplification available in any role file:

- It is 14 of the memory job's 60 output obligations. Its only consumers are
  the cross-system comparison tools: the matrix reader, landscape synthesis
  and taxonomy refresh. No other job of the run needs it.
- Its definitions are 9.2 KB of the 16.4 KB memory type, which every memory
  job, reconciliation and record verification must read.
- Three of the four findings returned to a memory analyst in the records
  concern the profile. In the stopped Graphiti run the analyst added a
  condition to `decay` that the axis definition does not have.
- Checking it is reconciliation's deepest obligation (five files combined)
  and one of record verification's three deepest.

The memory job today holds two tasks: trace how memory works from source, and
classify the result in a vocabulary built for comparing systems. Separating
them gives each worker one task. It also follows the
[split proposal](./report-collection-split-proposal.md): an analyst holds
only the analysis.

The evidence is two audited runs of one source and one stopped run. It shows
where failures concentrate. It does not show that separation will reduce them.

## Design

### Position in the run

Run the profile job once, after the reconcile and record-verification loop
closes without blockers and before synthesis:

```text
boundary → runtime → memory ‖ epistemic → [reconcile → verify]* → profile → verify-profile → synthesize → verify-synthesis
```

The profile job then classifies reconciled, verified records. Today the
profile is written before reconciliation, so every amendment or supersession
can invalidate it, and a profile defect costs a memory correction round plus
a reconcile round. In the proposed position a profile defect costs a rerun of
the profile job only.

### Inputs and output

The profile job reads the boundary, the runtime, memory, epistemic and
reconciliation members, the record contract and the profile type. It
classifies from accepted records and cites them.

It may read the frozen source, under the shared source-reading rules, to
understand a record or to choose between two readings of it. It declares no
records and adds no evidence of its own: every profile value still cites
records of the set. The operator decided both points on 2026-10-03. This limit keeps
record grammar, quotation and ID allocation out of the job, and keeps all
evidence inside the members that reconciliation and verification checked.

Where the source shows a fact that no record carries, the job does not assert
the value. It uses the existing `partial`, `uninspected` or `not-determinable`
assessments and names the missing fact and its source path in the note. It
does not return work to the memory analyst. This keeps the run free of a new
return loop; the cost is stated under risks.

Its output is a new set member, `memory-profile.md`, with a new type. The
frontmatter carries `memory-comparison` unchanged in shape: scope, ten axes,
and per axis `assessment`, `values`, `evidence`, `records` and `note`. The
body carries the Comparison rationale. Per-value evidence bases stay, as
[ADR 093](../../reference/adr/093-memory-comparisons-keep-evidence-per-value.md)
decided.

A separate member is needed because the memory member is frozen byte for byte
and no step rewrites it. Merging the profile into its frontmatter at assembly
would break that rule.

### Verification

Add a `verify-profile` job with one bounded correction round, following the
pattern of synthesis and its verification. It checks each axis against the
profile type's definitions and the set's records. Code validation stays as
now: structure, controlled values, and every cited ID resolved against the set.

### What each existing job loses

| Job or file | Removed |
|---|---|
| Memory job and memory type | The `memory-comparison` field, the Memory comparison fields section (9.2 KB), the Comparison rationale section, scope agreement between profile and prose, and the rule that every record the profile cites be annotated locally. |
| Reconcile job | The axis-by-axis profile check. |
| Record verification job | The profile check; its memory type input can then be dropped or shrinks. |
| Reconcile-to-memory return | Profile findings as a return reason. |

The memory report keeps its records, annotations, Write side and Read-back
sections. These already require the descriptive facts the axes classify:
storage, form, lineage, consumers and their authority, write agency, curation,
trace-fed writes and read-back selection. The memory instruction must say
that the analyst describes these in source-native terms and does not map them
to controlled values.

### Consumers that change

- `src/commonplace/lib/agentic_workflow.py`: two job constructors, the run
  order, assembly and the manifest's member list.
- `src/commonplace/lib/systems_matrix.py` and `validation.py`: read and
  validate the profile from the new member. The memory type's own rule that
  calls `memory_member_comparison` moves to the new type.
- `agentic_set.py`, the analysis-set type and `ARTIFACT.yaml`: a sixth member.
- The overview type, which says record verification covers the memory profile.
- `properdocs.yml`, which lists each retained member that is published.
- Landscape synthesis, taxonomy refresh and the matrix scripts.
- Two new job instructions and one new type with its schema.

No reader keeps the old location. The operator plans to regenerate all
reviews, so current sets leave the comparison population when replaced, and
no consumer needs a reader for both layouts.

## Decided

- The profile leaves the memory job and is produced by an additional job.
- The profile job may read the frozen source. It adds no evidence: it
  declares no records, and every value cites records of the set. The replay
  can reopen the second point: if many axes weaken because the source has
  facts the records lack, the operator chooses between a stricter memory type
  and letting the profile job declare records.

- The profile member, its type and both new job instructions belong to the
  analysis collection, which is self-contained. The profile is frozen and
  pinned with the records it cites. Comparison tools in `kb/agentic-systems/`
  read it from the retained set.

- `verify-profile` is a separate job, to keep independent review. Operator
  decision, 2026-10-03, adopting the agent's recommendation.
- The profile job is implemented after the collection relocation, so its
  type and instructions are written once in the new collection. The `decay`
  repair from the Sol plan's item 5 moves into the profile job's instruction.

- The profile job lands before regeneration starts, so each system is
  regenerated once. It gets its own decision record, separate from the
  collection split's.

No design decision remains open. Implementation still needs the replay
below, the ADR check and the operator's explicit commission.

## Costs and risks

- Two more jobs per complete run, plus at most one profile correction.
- **Evidence loss.** The profile job can see a fact in the source but cannot
  assert a value that no record supports. The replay below tests how often
  this matters.
- **Scope creep and input volume.** Source reading is the largest input of
  the analyst jobs. A profile job that reads widely becomes a second memory
  analysis. Its instruction must bound reading to the records' cited paths
  and what is needed to resolve a named ambiguity.
- **Underspecified records.** Once the axes leave the memory type, the
  analyst no longer sees what the classifier will need. The memory type's
  record and annotation fields must stay sufficient; the replay tests this too.
- A sixth member changes the set type, the manifest and the published member
  list. Retained sets in the old shape stop validating as current sets.
- [ADR 083](../../reference/adr/083-agentic-analysis-carriers-follow-exact-result-consumers.md)
  and ADR 093 bear on where results are carried. Read both before drafting
  the decision; this proposal has not checked it against them clause by clause.

## Check before adoption

Run a replay before changing the live method. It needs separate commission
because it starts model jobs.

1. Draft the profile type and the profile job instruction in this workshop.
2. Take the two retained Dynamic Cheatsheet sets. Give a worker the set's
   members with the `memory-comparison` mapping and Comparison rationale
   removed from the memory member, plus the drafts and the frozen source.
3. Compare the produced profile with the retained one, axis by axis: same
   values, weaker assessment, or different values. For each difference, decide
   from the records which profile is right.
4. Count the axes that fell to `partial`, `uninspected` or `not-determinable`
   only because the records lacked a fact the retained profile used.

Keep the no-new-evidence limit if those axes are few and each names a fact
the memory type can require. If many axes weaken, return the choice named
under Decided to the operator. Also
record how much source the worker read.

The retained records were written by analysts who had the axes in view, so
the replay overstates how well future records will support classification.
The first live run after adoption is the real test and is separately
commissioned.

Also measure the memory, reconcile and verify packets before and after with
the five measures of the complexity measurements, and the two new packets on
their own. The simplification claim fails if the new jobs carry the
obligations that the old ones lost without any role getting simpler.

## What closes this proposal

An accepted decision record, the implemented jobs and type with their tests,
and a recorded replay result; or a recorded rejection with the reason.
