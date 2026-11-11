# Admission to the main record: economic considerations

## Origin, purpose and status

The operator asked to retain these considerations after discussing candidate
outputs from connect, revision and the ongoing ingest refactoring. This is a
selective account of that discussion and a design checklist for continuing it,
not an adopted retention policy or a claim that the relevant costs have been
measured. It extends the [Git and retained-artifact exploration](./git-and-retained-artifacts.md)
with the question that precedes carrier selection: what information earns
admission to the main record at all?

Here, **main record** means the project's deliberately retained Git-backed
record, including versioned files and commit messages. This is the local
arrangement under discussion, not a decision to require Git in every
Commonplace KB. Being committed does not by itself make a claim true, a
proposal adopted, or an instruction operative.

## What the discussion established

The operator corrected three inadequate distinctions:

1. **Workspace isolation is not the main question.** A candidate file or
   directory lets an automated process work without immediately changing
   maintained artifacts. The larger question is which products and accounts
   of that work should enter the main record.
2. **Duration of possible usefulness does not decide retention.** Something
   may remain potentially useful for years without being valuable enough to
   commit. Something else may be useful for one operation, have its useful
   contribution incorporated into a committed result, and then have little
   remaining value as a separate artifact.
3. **Possible debugging value is not a discriminating criterion.** Practically
   every intermediate could help some future investigation. Moreover, session
   traces already supply a general process record. The comparison must not
   assume that declining to commit an intermediate necessarily loses its
   information.

The resulting question is comparative:

> What additional value does placing this material in the main record provide,
> relative to leaving it in traces or working storage, recovering it when
> needed, or retaining only a selected account of what its use produced?

No numeric threshold, retention period or mandatory record format follows yet.

## The actual alternatives

These are possible treatments, not a required sequence or mutually exclusive
stores:

| Treatment | What it preserves or makes available | What still needs accounting |
|---|---|---|
| Leave information in session traces | The recorded interaction and process history | Capture completeness, discovery, interpretation, access and expiry |
| Keep a working file or local cache | A directly usable product without reconstructing it from a trace | Local availability, collisions, staleness and eventual cleanup |
| Commit the whole artifact | The artifact and its recorded versions | Admission effort, discovery, interpretation and any maintenance obligations |
| Commit selected findings, evidence or rationale | The parts expected to support future work | Extraction cost and losses introduced by selection or summarization |
| Incorporate its contribution into another artifact | Links, an ingest, a revision or another maintained result | Whether a future task still needs the intermediate or its reasoning |
| Record an account in a commit message | Reasons and evidence associated with a change or a larger decision | How readers find the relevant commit and resolve its references |
| Recreate or reacquire later | A new result when a future need justifies the work | Reproduction cost and whether an equivalent observation remains possible |
| Delete the working copy | Avoids retaining a separate file after its use | What remains in traces or Git, and which recovery options are actually lost |

Untracked does not mean immediately deleted, short-lived or cheap to regenerate.
Tracked does not mean permanently present in the current tree: selected material
can remain in history. Current files and their Git history are not independent
stores. Nor does deleting a working copy delete the account already in a trace.

## Considerations for the economic comparison

### 1. Future use, not conceivable use

Name the future operation the material could support: ordinary reading,
implementation, revision, debugging, audit, comparison or reconsideration.
Distinguish a recurring or evidenced need from a merely possible one. Consider
both the likelihood of the need and the consequence of being unable to meet it.
A rare investigation can matter greatly; frequency alone is not the test.

A hypothetical debugging scenario must not become an automatic exemption from
selection. Equally, low measured reuse over a short period does not establish
that rare recovery evidence is worthless. The relevant horizon and acceptable
loss remain choices to make explicitly when consequential.

### 2. The marginal benefit of Git admission

Ask what committing adds over the available trace and working copy. Possible
benefits include easier retrieval, less reconstruction, a clearer explanation,
portability to another clone or operator, direct machine use, a stable reference,
and preservation beyond local trace retention.

These are possibilities to check, not benefits every commit automatically
supplies. A committed file nobody can find may add little. A well-indexed trace
may already answer the intended question cheaply. Conversely, reconstructing
an answer from a large trace may cost much more than reading a selected account.

### 3. Value before and after consumption

An intermediate can earn its production cost through the current task without
earning durable retention. A connect report can guide link authoring; a
candidate can support inspection before replacement. Once used, assess its
remaining contribution, not the value it had at production time.

Do not infer that the final result preserves everything important. It may omit
rejected alternatives, original expectations, operator constraints, failures or
reasons for a choice. But those omissions do not automatically require a separate
committed intermediate: the trace may already retain them adequately, or a small
selected account may suffice.

### 4. Session traces as the baseline process record

The operator identified session traces as the artifact already carrying the
process information. Start from that existing capture rather than designing a
second exhaustive process archive in Git.

Two questions remain distinct:

- **Was the information captured?** A recorded path is not the file's contents.
  Truncated tool output, external state and worker sessions without usable
  cross-references can leave gaps. This discussion did not audit trace coverage.
- **Will it be recoverable when needed?** A complete trace may still be local,
  difficult to find, inaccessible to another reader, or subject to deletion,
  privacy and copyright constraints.

Where capture and access are adequate, a second artifact principally earns its
place through improved use or durability, not by being the sole copy of the
information. Where they are inadequate, name the particular gap instead of
assuming that all traces are useless or all intermediates must be committed.

### 5. Recovery and regeneration are different

Recovering an old candidate from its trace is not the same as generating another
candidate from the same prompt. A later run can use another model, changed
instructions or changed sources, and need not reproduce the earlier output.
Likewise, current external access may not recover the observation available at
the time. Determine whether the future use needs exact historical evidence, a
functionally equivalent product, or merely a current answer.

### 6. Total cost of each treatment

Count costs on both sides rather than treating Git as expensive and traces as
free:

- capture, extraction, checking and description;
- storage, transfer and retention administration;
- indexing, searching, reading and reconstructing;
- keeping maintained accounts applicable and distinguishing them from history;
- reference upkeep and the cost of later cleanup;
- duplicated or stale material that misleads readers or consumes attention;
- privacy, confidentiality, licensing and access restrictions;
- regeneration, failed recovery and the consequences of missing evidence.

Raw storage may be cheap. A historical artifact need not incur the maintenance
cost of a current instruction. Material only in Git history need not clutter
ordinary file search. These differences depend on the actual arrangement; do
not charge every possible cost to every retained item.

Production cost is already incurred when deciding what to retain. It is not by
itself a reason to commit the output. It matters prospectively when losing the
output would require paying again for a use that is worth serving.

### 7. Selection and compression have costs and failure modes

A shorter retained account may make future work easier, but authoring and checking
it cost effort. Selection can erase the expectation that a later outcome refuted,
a consequential operator contribution, or an alternative needed for
reconsideration. A summary should not silently replace contemporaneous evidence
with hindsight.

Compare the benefit of the selected account with using the original trace, and
state what the selection deliberately leaves there. Do not assume that every
run needs a hand-written summary or that a complete transcript is a usable
substitute for an explanation.

### 8. Adoption and retention remain different decisions

An accepted change may be committed while its disposable intermediate reports
remain outside Git. A rejected candidate or failed experiment may nevertheless
earn retention as evidence. Retention does not establish endorsement; adoption
does not establish that the rationale was corroborated.

The authority to produce, apply and commit must be clear for each workflow.
It may be granted conditionally in advance; this discussion does not impose a
fresh human-approval gate everywhere. A file's location alone supplies neither
publication authority nor a sandbox.

### 9. Policies may be cheaper than repeated item-level decisions

It would be costly and unreliable to make an agent invent a future-use argument
for every generated file. Class-level defaults may be preferable, with exceptions
for identified evidence needs. That is a design possibility, not a selected
classification or threshold.

Defaults should be revisable from actual experience: investigations blocked by
missing material, repeated expensive reconstruction, unused retained outputs,
and misleading duplicates. Retaining measurements about retention also costs
something; this does not commission a new telemetry system.

## Current workflow examples and limits

- **Connect:** a report supports later authoring. Once useful connections have
  been incorporated, ask what additional use justifies retaining the report
  beyond its cache and session trace. Applying connections is not copying the
  report into the library.
- **Revision:** a candidate, report and diff support inspection and controlled
  publication. Their production and approval roles do not by themselves decide
  whether they belong in Git after publication.
- **Ingest:** the ongoing refactoring separates a working candidate from the
  tracked ingest. Its checks and publication mechanism govern replacement;
  they do not alone settle retention of intermediate material.
- **Agentic-system analysis:** set aside as the operator requested. Its worktree
  and currently automatic merge have a different integration model; do not use
  it to imply a universal manual approval boundary.

These examples motivate the questions. They are not measured demonstrations of
an optimal retention policy or claims that their traces preserve every byte.

## Relationship to existing workshop work

The [workshop framing](./README.md) asks how decision accounts survive sessions,
are discovered and remain applicable across ADRs and Git commits. This account
adds the upstream admission question. The existing requirement to compare
carriers with equivalent content still holds: first decide what is worth
retaining, then compare the means of retaining and accessing it.

[Lineage mechanisms](../lineage-mechanisms/README.md) already owns general
derived-artifact retention and merge-back provenance. Coordinate any policy
proposal there rather than building a competing taxonomy here. No common
workflow engine, new record type or Git-required framework policy is adopted.

## Questions left open

1. For the actual debugging and reconsideration tasks, what is captured in the
   existing traces, and what can intended readers recover at reasonable cost?
2. Which classes of intermediate have their primary value consumed by their
   committed results, and which repeatedly support a separate later use?
3. What additional value justifies a current file, an account in a commit,
   retention only in history, or no additional Git record?
4. What trace and cache lifetime is economical, and which losses are acceptable
   when they expire? Do not assume one universal duration.
5. When does extracting a small account pay for itself, and how do we check that
   it preserves what the intended future operation needs?
6. Which class-level defaults would reduce decision cost without turning either
   possible debugging value or automatic cleanup into an indiscriminate rule?

Continue with concrete uses and comparisons only when they can discriminate
between these choices. This record commissions no paid trial, implementation,
cleanup or deletion of existing evidence.
