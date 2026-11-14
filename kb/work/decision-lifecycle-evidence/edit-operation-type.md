# Draft: the edit-operation type

## Status

Drafted on 2026-11-13 as the third type draft for the
[one improvement procedure proposal](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md),
after the [run type](./improvement-run-type.md) and the
[answers schema](./improvement-run-answers-schema.md). It is a workshop
draft: nothing is registered and no instruction declares the type. The
frontmatter schema below was run against the frontmatter of
[plain wording](../../instructions/simplification-passes/plain-wording.md)
with one field added, and against four invalid variants.

## What the type is for

An edit operation is one of the procedure's three kinds of atom. It takes
one text of a note and returns a changed text, or a list of changes it
proposes. Review gates have a type, so a gate can be run, stored and
calibrated by itself. Edit operations have none: the eight
[simplification passes](../../instructions/simplification-passes/README.md)
share a shape by habit, and the ten fix strategies are sections of
[one file](../../instructions/fix-warnings/fix-strategy-taxonomy.md).

The type makes three things true of every edit operation:

- a variant can run it without knowing anything the file does not say;
- it can be run alone on one note as a one-atom variant, which is how it is
  tested;
- a decision or an edit recorded in a run names it, so evidence about it
  survives a change of variant.

Unlike the run types, this type belongs with the shared types in
`kb/types/`, beside the review-gate type. Edit operations are instructions
that ship with the framework, and their type has to ship with them.

## The contract every edit operation shares

These rules hold for all instances, so no instance repeats them. Most are
today in [execute a revision pass](../../instructions/simplification-passes/execute-a-revision-pass.md),
which stays the instruction a worker follows.

**Reads.** Files only: the text to edit, and where the variant supplies
them, a purpose, a scope, the claims to protect, the findings that selected
the operation, and the approved items. An operation that needs something a
file does not carry, such as the session's memory of an earlier step, does
not meet the contract.

**May change.** The note's body, within the kind of change its goal names.

**Must preserve.** The title, the H1, the type and the brief declaration:
no edit operation makes a claim-level change
([ADR 080](../../reference/adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md)).
Also quoted text, links, and every claim, qualification and example the
instance does not explicitly permit changing. An operation that sees a
needed title or claim change reports it; the variant records it as a
higher-order item.

**Returns.** One of three things, and nothing else:

- the complete changed text, with a report of what changed;
- a list of proposed changes, applied to nothing, when the operation asks
  before it edits;
- a problem, when it cannot proceed within these bounds.

It does not edit the checkout, commit, launch other work or choose another
operation. The unchanged text is a valid return.

## What an instance declares

Frontmatter, beyond the instruction type's `description` and `type`:

| Field | Meaning |
|---|---|
| `effort` | `simple` or `judgment`: whether a fresh worker on a cheaper setting can run it, or it needs the session's model. Already on every pass. |
| `depth` | Optional integer; 1 runs first. The order of concerns among edit operations. Already on six passes. |
| `decision` | `none` when the operation applies its changes, `per-item` when it returns a list and the operator decides each entry. This is what the operation does today. A variant may ask where the operation says `none`; it may not skip the question where the operation says `per-item`. |
| `responds-to` | Optional list of review criteria or lenses whose findings select this operation. An operation without it is selected by a plan or by the variant. |

Body, after an opening paragraph that states the goal:

| Section | Content |
|---|---|
| `## Steps` | What the worker does. |
| `## Report` | What the report lists, one line per change, and what is reported but not applied. For a `per-item` operation, what one entry of the list contains. |
| `## Preserve` | What this operation keeps beyond the shared contract, and any removal it permits. |

The passes already carry `Report:` and `Preserve:` as paragraphs. Making
them headings lets the schema check that they exist.

`decision` records today's behaviour and settles nothing about authority.
Which operations may move from `per-item` to `none`, and on what evidence,
is the question of the
[authority grades proposal](../../reference/proposals/authority-grades-and-learning-from-operator-decisions.md).
That proposal still weighs whether grades are declared on atoms or named
in variants; this field is the atom-side default either way.

## The schema

The frontmatter part, nested under `frontmatter` and combined with the
instruction schema as the other types do. The three headings are a
body-shape rule beside it.

```yaml
type: object
required: [description, type, effort, decision]
properties:
  type:
    const: types/edit-operation.md
  effort: {enum: [simple, judgment]}
  depth: {type: integer, minimum: 1}
  decision: {enum: [none, per-item]}
  responds-to:
    type: array
    minItems: 1
    items: {type: string, minLength: 1}
```

## How the existing material fits

| Material | Fit | What it needs |
|---|---|---|
| readability-and-flow, narrow-overclaims | Fits. | The type, `decision: none`, the three headings. |
| plain-wording, abstractions | Fits. | The type, `decision: per-item`, the three headings. Their strike step is the `per-item` return. |
| audit-a-prior-pass, place-external-systems | Fits, with inputs to name. | Each reads more than the note: a prior pass's findings, generated review files. Those are files, so the contract holds once the steps name them as inputs. |
| opening-and-title | Partly. | Its TL;DR edits fit. Its title proposals are claim-level and become higher-order items, which the shared contract already routes to the report. |
| split-out-a-treatment | Does not fit as drafted. | It writes a second file. The run's edit chain holds one note's texts. See the open choices. |
| The ten fix strategies | Fit as one operation. | See below. |
| The full pass's body edits and copyedit | Not yet operations. | They are steps inside the full pass's instruction. Each would be written as an instance when a variant needs it. |
| execute-a-revision-pass, revise-an-article-or-note, resolve-a-strike-list | Not edit operations. | The worker's executor, a variant and a stop. |

**The fix strategies start as one operation.** Each strategy is a pattern
and a typical fix, a few lines long, with no preserve rules of its own.
Ten files of that size would be ten type instances with nothing to say in
two of their three sections. The draft wraps the taxonomy as one edit
operation, "fix a finding by a named strategy", with `responds-to` naming
the gate lenses. A run cites the strategy by anchor,
`fix-strategy-taxonomy.md#stale-paths`, so decisions and edits still key to
the strategy. A strategy becomes its own file when it needs its own steps
or preserve rules, or when its record shows it should be calibrated apart.
This requires the `atom` fields of the run types to accept a path with an
anchor.

## Testing one operation

An edit operation is tested as a one-atom variant: a start text goes in, and
a run directory comes out with the candidate under `texts/` and the edit
chain naming the operation. Two kinds of evidence accumulate per operation
without further machinery:

- for a `per-item` operation, the operator's accept and reject decisions
  with reasons, in the answers of every run that used it;
- for any operation, the review results on the text before and after,
  since both texts are stored and review results key to a text hash.

No labelled set of good edits exists, and none is proposed here. The
operator's decisions are the first calibration evidence.

## Open choices

1. **Operations that write a second file.** Split-out-a-treatment creates a
   treatment file beside the note. Either the type admits a declared
   second output and the run stores it under `texts/`, or such operations
   stay outside the type. Recommendation: keep them outside until a
   variant needs one, since the contract of "one text in, one text out" is
   what makes an operation testable alone.
2. **Wrapping or splitting the fix strategies.** Recommended above: wrap
   now, split on evidence.
3. **Whether `responds-to` belongs on the atom.** It keeps selection
   knowledge with the operation. The alternative is a table in each
   variant, which lets two variants select differently. Recommendation:
   keep it on the atom as a default that a variant may override.
4. **Renaming the headings in eight shipped passes.** Small, but the revise
   workflow still reads those files. The change waits until the first
   variant runs, so that the shipped workflow is not edited for a draft.
