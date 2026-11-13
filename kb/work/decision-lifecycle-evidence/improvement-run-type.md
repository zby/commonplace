# Draft: the improvement run as a directory type

## Status

Drafted on 2026-11-13 for the
[one improvement procedure proposal](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md),
which makes a run "a typed directory". Revised the same day after a review
that separated two questions: whether the directory is structurally valid,
and whether a later reader can recover what happened from it. The
[evidence contract](#the-evidence-contract) answers the second.

This file is a workshop draft, not a type: nothing here is registered, and
no instance exists. The layout below parses with the shipped layout reader;
it has not been validated against an instance. The
[answers schema](./improvement-run-answers-schema.md) is the companion draft.

## What the directory mechanism allows

Read from the [directory artifact definition](../../reference/definitions/directory-artifact.md),
the [validation contract](../../reference/validation-contract.md#directory-artifacts)
and the one existing directory type, the
[analysis set](../../agentic-system-analyses/types/agentic-system-analysis-set.md).
Four properties shape the draft.

- **Members are direct Markdown children.** A role names one Markdown file at
  the directory root. JSON files and files in subdirectories are not members
  and get no layout check.
- **Each role expects one document type.** A copy of the note cannot fill a
  role, because notes have different types. A copy would also fail ordinary
  file validation: its relative links resolve from the wrong directory.
- **Identity comes from a member.** A role can require that named fields
  equal those of another role. The manifest cannot be an identity source, and
  the source name `run` is reserved for analysis runs. One member must
  therefore carry the run's identity.
- **Requiredness can depend on one field of one role.** The layout names a
  role and a field; each value of the field adds required roles.

The proposal listed five roles: start text, findings, operator answers,
candidate text and report. The first two properties rule out the start text
and the candidate as members. The draft keeps every text as a plain file
under `texts/`, named by its hash.

## The layout

```yaml
layout:
  membership: open
  roles:
    report:
      path: report.md
      type: reports/types/improvement-run-report.md
    findings:
      path: findings.md
      type: reports/types/improvement-run-findings.md
      identity:
        - {from: report, fields: [note, start-sha256]}
    changes:
      path: changes.md
      type: reports/types/improvement-run-changes.md
      identity:
        - {from: report, fields: [note, start-sha256, final-sha256]}
    answers:
      path: answers.md
      type: reports/types/improvement-run-answers.md
      identity:
        - {from: report, fields: [note]}
  required:
    always: [report]
    when:
      role: report
      field: ending
      values:
        stopped: [findings, changes, answers]
        applied: [findings, changes, answers]
        partly-applied: [findings, changes, answers]
```

A run directory then looks like this:

```text
kb/reports/state/improve/<note path without .md>/<YYYYMMDD-HHMMSS>/
  ARTIFACT.yaml      type only
  report.md          identity, ending, prose report
  findings.md        review results the run read, cited by review run and launch
  changes.md         the edit chain, one entry per applied edit operation
  answers.md         operator decisions and pending items
  texts/<sha256>.txt the start text and every text an edit produced
```

A closed run has all four members. An empty list in a member says "none"
explicitly: no findings acted on, no edit applied, no question asked.
Absence of a member therefore means only one thing, that the run did not
close. An open run requires the report alone.

## The members

| Role | Frontmatter it carries | Written |
|---|---|---|
| `report` | `note`, `variant`, `start-commit`, `start-sha256`, `started-at`, `ending`, `final-sha256`, `ended-at`. The body is the prose report. | Created at the start with `ending: open`; completed at the end. |
| `findings` | `note`, `start-sha256`, and `results`: one entry per review result read, with `atom`, `run`, `launch`, `output-sha256`, `text-sha256` and `outcome`. | After each review step, including a re-review after edits. |
| `changes` | `note`, `start-sha256`, `final-sha256`, and `edits`: one entry per applied edit operation, in order, with `atom`, `from-sha256`, `to-sha256` and, where an operator item authorised it, `item`. | Appended after each edit; the final hash is set at the end. |
| `answers` | `note`, and `items`: one entry per decision the run needed, with its atom, proposal, state and reason. | At each stop, and again whenever the operator answers. |

Three choices need their reason stated.

**The report is the identity source.** It is the only member that exists
from the first step, so the other members repeat its fields. Repeating the
start and final hashes in `changes` lets the existing identity check tie the
edit chain's two ends to the run.

**Higher-order results need no extra field in `findings`.** The evaluation
workshop maps the check's outcome to force: pass is no proposal, warn is
weak, fail is strong. A weak proposal additionally becomes a pending item in
`answers`; a strong one becomes the item the run stopped on.

**`ending` describes what the run did, not what is still open.** A later
session that resolves a pending item writes the decision into this run's
`answers`, so the proposal and its answer stay together. Applying an
approved item later is a new run, because the note has usually moved on and
an edit chain belongs to the text it started from. The earlier run's
`ending` never changes.

## The evidence contract

A structurally valid directory is not yet a recoverable account. A hash
identifies a text; it does not keep it. For each thing a later reader needs,
the draft names where the bytes are and what that location depends on.

| The reader needs | Where the bytes are | Depends on |
|---|---|---|
| The exact finding acted on | The review run's launch output, `<run>/calls/launches/<launch>/outputs/review.md`, cited by `run`, `launch` and `output-sha256` | Review run directories being kept, which is their current rule |
| The text before, between and after edits | `texts/<sha256>.txt` in the run directory: the start text, and each text an edit operation produced. The last one is the final text. | Nothing outside the run |
| The operator's decision and reason | The item in `answers.md` | Nothing outside the run |
| The instruction versions used | The variant and each atom, at `start-commit` | The run starting with those instructions committed |
| The link from authorization to application | The edit's `item`, and the item's `applied-in` | Both written; see below |

**Findings cite the launch, not the shared result path.** The shared result
store holds the current judgment per note and criterion, and a later review
replaces it. The file that replaces nothing is the launch output inside the
review run directory. Each stored result names its run and launch in its
frontmatter, so the citation costs nothing to produce. Checked on
2026-11-13: all 220 results in this checkout had a body identical to the
launch output their run kept. The citation is therefore recoverable as long
as review run directories are kept. No copy is made into the improvement
run.

**Every text of the chain is stored when it is produced.** The start text is
written to `texts/` at the first step, and each edit operation's output when
it returns. The final text is the last of these, and the note in the working
tree equals it at the run's close. Nothing about the texts depends on a
commit, so a stopped run, a partly applied run and a run whose result is
never committed keep the same evidence. A stopped run holds the start text
only.

**`start-commit` recovers the instructions, not the note.** The variant and
the atoms are expected to change often, so their names alone do not say
which text ran. The convention: a run starts with its variant and atoms
committed, and `start-commit` is the commit to read them at. A draft atom
that is not committed is stored under `texts/` like any other text, and the
report says so. Review results additionally carry the criterion's hash.

**One reference form links items across runs.** An item is named
`<run directory path>#<id>`. An edit's `item` uses that form, whether the
item is in the same run or an earlier one. The item's `applied-in` holds
the path of the run whose edit chain applied it. The reader's question,
what was proposed, what the operator authorized and which change
implemented it, is answered by following those two fields. `supersedes` in
the answers schema uses the same form.

## Ordinary cases

| Case | Ending | What the directory holds |
|---|---|---|
| The reviews find nothing to change | `applied` | Findings cite the passes. `edits` and `items` are empty. `final-sha256` equals `start-sha256`. |
| A weak proposal stays pending while all permitted edits finish | `partly-applied` | The proposal is a pending item. The edit chain holds the edits. |
| The operator answers every question in the session, approving some | `applied` | Items are approved or rejected with reasons; approved ones name this run in `applied-in`. |
| The operator declines every proposed edit | `applied` | Every item is rejected with its reason. The edit chain holds only edits that needed no decision, or is empty. |
| A strong higher-order proposal | `stopped` | One pending item, or its answer once given. `edits` is empty. `texts/` holds the start text. |
| The run is interrupted before the first review result | `open` | The report and the start text. Validation reports nothing missing, and the `open` ending is the signal that the run did not close. |
| An approved item is applied later, and the note has changed | a new run | The new run re-derives the edit against the current text. If the passage is unchanged, it applies the edit and cites the item. If not, the old item expires and the new run proposes again with `supersedes`. |

`applied` means the run made every edit it was permitted to make and left
no item open; it does not mean something changed. `partly-applied` means at
least one item was open when the run closed.

## What checks what

Three kinds of check exist, and the draft keeps them apart.

**The layout and the member schemas**, with no new code:

- an open run has a report; a closed run has all four members;
- each member has its declared type and satisfies its schema, which is where
  a missing reason on a rejection, deferral or expiry is caught;
- every member names the same note, and the findings and the edit chain name
  the same start text as the report.

**The variant's obligations**, which no schema can express because they
compare members or look outside the directory. The variant states them and
the agent following it carries them out:

- the ending agrees with the items: `partly-applied` when an item is open,
  `stopped` when a strong proposal ended the run;
- each text named in the edit chain is in `texts/`;
- each cited launch output exists and matches its hash when it is cited;
- the edit chain is continuous, each edit starting from the text the
  previous one produced;
- an applied item's `applied-in` and the applying edit's `item` are both
  written.

**Not checked at all:** that `final-sha256` is the note's current text after
the run's close. That is a fact about one moment.

A registered type rule, which is code, could take over some of the
variant's obligations. None is proposed until a run shows one going wrong.

The manifest names only the type. No member is pinned, because `answers`
changes after the run ends. The state repository's commit is the freeze.

## Open choices

1. **Four member types or fewer.** The draft costs five type specs: the
   directory type and four members. The cheaper form folds `findings` and
   `changes` into the report's frontmatter, leaving `report` and `answers`.
   The draft keeps four because each file is then written at one phase by
   one writer, and no step rewrites another step's frontmatter.
   Recommendation: start with four and merge after the first run if two of
   them prove trivially small. This choice is secondary to the evidence
   contract and does not change it.
2. **Where pending items converge.** The rules are in the
   [answers schema draft](./improvement-run-answers-schema.md#when-an-item-is-closed).
3. **Run identifier.** A timestamp, as the run bundles of
   [ADR 129](../../reference/adr/129-workflow-run-bundles-live-under-the-state-tree-and-are-kept.md)
   use, since no code computes a digest for an instructed run.
4. **Home of the types.** Settled by the operator on 2026-11-13: local to
   the reports collection, under `kb/reports/types/`, which its contract
   reserves for project-authored report contracts. The directory does not
   exist yet. One consequence to revisit: the collection contract keeps
   command-produced generic report types global, because they ship with
   the framework. If the improvement procedure is later shipped to
   consuming KBs, its run types must move to the shared types or be
   installed with it.
5. **Extension of stored texts.** `.txt` keeps them out of Markdown
   validation. `.md` would make them readable in a viewer but a validation
   target with broken relative links.
6. **Dependence on kept review runs.** The finding citation is recoverable
   only while review run directories are kept. If a pruning rule for them is
   ever adopted, it must spare cited launches or the improvement run must
   copy them.
