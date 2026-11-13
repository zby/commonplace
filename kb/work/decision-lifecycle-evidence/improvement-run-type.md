# Draft: the improvement run as a directory type

## Status

Drafted on 2026-11-13 for the
[one improvement procedure proposal](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md),
which makes a run "a typed directory". This file is a workshop draft, not a
type: nothing here is registered, and no instance exists. The layout below
parses with the shipped layout reader; it has not been validated against an
instance. The member schemas are the next drafts, starting with the answers
member.

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
and the candidate as members. The draft keeps them as hashes and plain files
instead.

## The layout

```yaml
layout:
  membership: open
  roles:
    report:
      path: report.md
      type: types/improvement-run-report.md
    findings:
      path: findings.md
      type: types/improvement-run-findings.md
      identity:
        - {from: report, fields: [note, start-sha256]}
    changes:
      path: changes.md
      type: types/improvement-run-changes.md
      identity:
        - {from: report, fields: [note, start-sha256, final-sha256]}
    answers:
      path: answers.md
      type: types/improvement-run-answers.md
      identity:
        - {from: report, fields: [note]}
  required:
    always: [report, findings]
    when:
      role: report
      field: ending
      values:
        stopped: [answers]
        applied: [changes]
        partly-applied: [changes, answers]
```

A run directory then looks like this:

```text
kb/reports/state/improve/<note path without .md>/<YYYYMMDD-HHMMSS>/
  ARTIFACT.yaml      type only
  report.md          identity, ending, prose report
  findings.md        review results the run read, cited by path and hash
  changes.md         the edit chain, one entry per applied edit operation
  answers.md         operator decisions and pending items
  texts/<sha256>.txt intermediate and final texts, not members
```

## The members

| Role | Frontmatter it carries | Written |
|---|---|---|
| `report` | `note`, `variant`, `start-commit`, `start-sha256`, `started-at`, `ending`, `final-sha256`, `ended-at`. The body is the prose report. | Created at the start with `ending: open`; completed at the end. |
| `findings` | `note`, `start-sha256`, and `results`: one entry per review result read, with `atom`, `result` (path in the shared store), `result-sha256`, `text-sha256` and `outcome`. | After each review step, including a re-review after edits. |
| `changes` | `note`, `start-sha256`, `final-sha256`, and `edits`: one entry per applied edit operation, in order, with `atom`, `from-sha256`, `to-sha256` and, where an operator item authorised it, the item's id. | Appended after each edit; the final hash is set at the end. |
| `answers` | `note`, and `items`: one entry per stop, with its atom, proposal, state and reason. Its schema is the next draft. | At each stop, and again whenever the operator answers. |

Five points need their reason stated.

**The report is the identity source.** It is the only member that exists
from the first step, so the other members repeat its fields. Repeating the
start and final hashes in `changes` lets the existing identity check tie the
edit chain's two ends to the run.

**The start text is a commit and a hash, not a file.** The variant starts
from a committed note. `start-commit` and `note` recover the exact text from
Git, and `start-sha256` verifies it. A run on an uncommitted note would need
the text stored under `texts/`; the draft does not forbid this, it only makes
the committed case the cheap one.

**The candidate is the note in the working tree.** The proposal already says
the commit is the publication. The final text is the note itself, and
`final-sha256` names it. Intermediate texts go under `texts/` by hash, so an
edit operation's output stays inspectable and an edit operation can be
unit-tested from a stored input.

**Higher-order results need no extra field.** The evaluation workshop maps
the check's outcome to force: pass is no proposal, warn is weak, fail is
strong. The `outcome` on the cited result therefore carries the force. A
weak proposal additionally becomes a pending item in `answers`; a strong one
becomes the item the run stopped on.

**`ending` describes what the run did, not what is still open.** Its values
are `open`, `stopped`, `applied` and `partly-applied`, the proposal's three
endings plus the unfinished state. A later session that resolves a pending
item writes the decision into this run's `answers`, so the proposal and its
answer stay together. Applying the approved edit is a new run of a one-atom
variant, because the note has usually moved on and the edit chain belongs to
the text it started from. The earlier run's `ending` never changes.

## What validation checks and what it leaves

With the layout and four member schemas, and no new code,
`commonplace-validate <run directory>` checks:

- the report and findings exist, and the members the ending requires exist;
- each member has its declared type and satisfies its schema, which is where
  a missing reason on a strike, rejection or deferral is caught;
- every member names the same note, and the findings and the edit chain name
  the same start text as the report.

It does not check, and the draft accepts this:

- that a cited result file exists and matches its hash. A schema cannot
  follow a path. This needs a registered type rule, which is code; it is not
  proposed until a run shows the citations go wrong.
- that the edit chain is continuous, each edit starting from the text the
  previous one produced. A schema cannot compare two values.
- that `final-sha256` is the note's current text. That holds only until the
  next edit, so it is a fact about the run's end, not a standing invariant.
- anything about `texts/`.

The manifest names only the type. No member is pinned, because `answers`
changes after the run ends. The state repository's commit is the freeze.

## Open choices

1. **Four member types or fewer.** The draft costs five type specs: the
   directory type and four members. The cheaper form folds `findings` and
   `changes` into the report's frontmatter, leaving `report` and `answers`.
   The draft keeps four because each file is then written at one phase by
   one writer, and no step rewrites another step's frontmatter.
   Recommendation: start with four and merge after the first run if two of
   them prove trivially small.
2. **Where pending items converge.** A pending item or a weak proposal needs
   a rule for when it is decided or dropped, or pending items accumulate;
   [productive deferral](../../theory/productive-deferral-requires-option-evidence-and-convergence.md)
   states the requirement. The rule belongs to the answers schema and the
   variant, not to this layout.
3. **Run identifier.** A timestamp, as the run bundles of
   [ADR 129](../../reference/adr/129-workflow-run-bundles-live-under-the-state-tree-and-are-kept.md)
   use, since no code computes a digest for an instructed run.
4. **Home of the types.** `kb/types/`, beside the full-pass report type,
   once the drafts leave the workshop.
5. **Extension of stored texts.** `.txt` keeps them out of Markdown
   validation. `.md` would make them readable in a viewer but a validation
   target with broken relative links.
