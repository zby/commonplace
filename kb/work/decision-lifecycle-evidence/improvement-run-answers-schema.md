# Draft: the answers member of an improvement run

## Status

Drafted on 2026-11-13 as the second type draft for the
[one improvement procedure proposal](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md),
after the [run type](./improvement-run-type.md). It is a workshop draft:
nothing is registered and no instance exists. The schema below was run
against the example in this file and against nine invalid variants of it;
it accepted the first and refused the others. It is a starting point, not
a contract.

## What the member is for

`answers.md` holds every point where a run needed the operator. It serves
three readers:

- **The operator**, in the session that resolves items: each item must be
  understandable from the file and the note alone.
- **The decisions command**, which lists decisions and what is still open
  per note. It should need no knowledge of the variant.
- **Later calibration** of an atom: which of its proposals the operator
  accepted or rejected, and why.

An edit that needs no operator decision creates no item. It appears only in
the run's edit chain.

## One item per decision

The unit is the smallest thing the operator can accept or reject by itself.
A strike list with twenty candidate replacements is twenty items, not one.
A split proposal is one item. This is the "item" unit of
[ADR 130](../../reference/adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md);
the "bundle" unit disappears, because no stop approves a whole text any more.

| Field | Meaning |
|---|---|
| `id` | Stable within the run. The edit chain cites it when an approved item is applied. |
| `atom` | Path of the instruction that produced the proposal. Decisions key to the atom, never to the variant. |
| `kind` | `higher-order` for a proposal about what the note is; `edit` for a proposed change to how it says it. |
| `force` | `strong` or `weak`. Required for a higher-order item and absent on an edit. |
| `change` | `split`, `merge`, `rehome`, `reject` or `claim`. Required for a higher-order item and absent on an edit. The first calibration round found the kind carried only by a convention in the finding text. |
| `proposal` | What would change, in words the operator can judge. |
| `where` | Optional: the passage or section the proposal applies to. |
| `text-sha256` | The note text the proposal was made against. |
| `state` | `pending`, `approved`, `rejected`, `deferred` or `expired`. |
| `reason` | Why. Required for `rejected`, `deferred` and `expired`; optional for `approved`. |
| `revisit` | Required for `deferred`: the condition under which the item is taken up again. |
| `decided-by` | `operator`, or `rule` when the procedure expired the item. Absent while pending. |
| `decided-at` | Timestamp of the decision. Absent while pending. |
| `applied-in` | The directory path of the run whose edit chain applied an approved item, this run's or a later one's. Null until then. A higher-order change is not made by an improvement run; there the field holds the commit that made it. |
| `repeats` | Optional: the earlier rejected item this proposal returns to, in the same reference form. Set whenever the same atom proposes the same `change` on a note where the operator rejected it before. |
| `supersedes` | Optional: the earlier run's item this one re-proposes, as `<run directory path>#<id>`. The edit chain's `item` uses the same form, so one reference names an item from any run. |

The body is free prose. A session may use it to show the operator longer
context than a field holds; nothing reads it mechanically.

"Struck" from the strike lists is `rejected` here. One word covers a
rejected replacement and a rejected split, so the record needs no mapping.

## When an item is closed

Deferral without a convergence rule is unmanaged indecision; that is the
requirement of
[productive deferral](../../theory/productive-deferral-requires-option-evidence-and-convergence.md).
Without a rule, pending items and weak proposals accumulate across runs and
nobody reads them. The draft proposes three rules. The first is schema; the
other two are the variant's, because a schema cannot see other runs.

1. **A deferral names its condition.** `deferred` requires `reason` and
   `revisit`. A deferral that cannot say when it will be revisited is a
   rejection.
2. **Open items live only in the latest run of a note.** An item is open
   while it is `pending`, `deferred`, or `approved` with no `applied-in`. A
   variant starts by listing the open items of earlier runs on the note.
   For each it either re-proposes the item in the new run, with
   `supersedes`, or leaves it out. Either way it sets the old item to
   `expired`, decided by `rule`, with the reason. The operator therefore
   reads one file per note to see everything open.
3. **A changed text expires what was proposed against it.** When the
   note's hash differs from the item's `text-sha256`, the proposal is
   re-derived or dropped under rule 2, never carried over unchanged. Review
   results already go stale the same way. An approved item that was not
   yet applied gets one more test: if the passage it names is unchanged,
   the new run applies it and cites it; otherwise it expires like the rest.

### Undecided: a proposal that returns after a rejection

The operator rejects a weak proposal. The text changes, the same check runs
again and makes the same kind of proposal. Whether to ask again, show the
earlier rejection beside the new item, or suppress the repeat is not
decided. The operator's direction on 2026-11-13 is to decide from examples
once they exist, so the draft only makes the examples easy to find.

A returning proposal carries `repeats`, naming the earlier rejected item.
The variant sets it: before recording a higher-order item it reads the
note's earlier decisions and looks for a rejected item from the same atom
with the same `change`. Every example is then one search away: the items
that have `repeats`, each pointing at the rejection and its reason. Until
the rule is decided, a returning proposal is recorded and asked like any
other. This is an item of the
[unresolved frontier](../../reference/definitions/unresolved-frontier.md),
held here until the types are registered.

## The schema

The frontmatter part, to be nested under `frontmatter` as the other typed
state files do.

```yaml
type: object
required: [type, note, items]
properties:
  type:
    const: reports/types/improvement-run-answers.md
  note:
    type: string
    pattern: '^[^/].*\.md$'
  items:
    type: array
    items:
      type: object
      required: [id, atom, kind, proposal, text-sha256, state, applied-in]
      additionalProperties: false
      properties:
        id: {type: string, minLength: 1}
        atom: {type: string, pattern: '\.md$'}
        kind: {enum: [higher-order, edit]}
        force: {enum: [strong, weak]}
        change: {enum: [split, merge, rehome, reject, claim]}
        proposal: {type: string, minLength: 1}
        where: {type: string, minLength: 1}
        text-sha256: {type: string, pattern: '^[0-9a-f]{64}$'}
        state: {enum: [pending, approved, rejected, deferred, expired]}
        reason: {type: string, minLength: 1}
        revisit: {type: string, minLength: 1}
        decided-by: {enum: [operator, rule]}
        decided-at: {type: string, minLength: 1}
        applied-in: {type: [string, "null"]}
        supersedes: {type: string, pattern: '#.+$'}
        repeats: {type: string, pattern: '#.+$'}
      allOf:
        - if: {properties: {kind: {const: higher-order}}}
          then: {required: [force, change]}
          else: {not: {anyOf: [{required: [force]}, {required: [change]}]}}
        - if: {properties: {state: {const: pending}}}
          then:
            not: {anyOf: [{required: [decided-by]}, {required: [decided-at]}]}
          else: {required: [decided-by, decided-at]}
        - if: {properties: {state: {enum: [rejected, deferred, expired]}}}
          then: {required: [reason]}
        - if: {properties: {state: {const: deferred}}}
          then: {required: [revisit]}
        - if: {properties: {state: {const: expired}}}
          then: {properties: {decided-by: {const: rule}}}
          else: {properties: {decided-by: {const: operator}}}
        - if: {properties: {state: {enum: [pending, rejected, deferred, expired]}}}
          then: {properties: {applied-in: {type: "null"}}}
```

It cannot check that item ids are unique, that an `atom` path exists, or
that `supersedes` and `applied-in` point at something real. A schema
compares neither two values nor a path with the file system.

## Example

A partly applied run: one weak split proposal left pending, one replacement
approved and applied in the run, one rejected, one deferred.

```yaml
type: reports/types/improvement-run-answers.md
note: kb/theory/example-note.md
items:
  - id: "1"
    atom: kb/instructions/review-gates/higher-order/split-check.md
    kind: higher-order
    force: weak
    change: split
    proposal: Split the section on caching into its own note; it argues a second claim.
    text-sha256: 9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c
    state: pending
    applied-in: null
  - id: "2"
    atom: kb/instructions/simplification-passes/plain-wording.md
    kind: edit
    proposal: Replace "leverages" with "uses" in the second paragraph.
    where: "## Mechanism, paragraph 2"
    text-sha256: 9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c
    state: approved
    decided-by: operator
    decided-at: "2026-11-13T15:02:00Z"
    applied-in: kb/reports/state/improve/kb/theory/example-note/20261113-150000
  - id: "3"
    atom: kb/instructions/simplification-passes/abstractions.md
    kind: edit
    proposal: Replace "retention economics" with "what keeping a file costs".
    text-sha256: 9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c
    state: rejected
    reason: It is the registered term of the workshop; the plain phrase loses the link.
    decided-by: operator
    decided-at: "2026-11-13T15:03:00Z"
    applied-in: null
  - id: "4"
    atom: kb/instructions/simplification-passes/abstractions.md
    kind: edit
    proposal: Replace "carrier" with "file or commit message".
    text-sha256: 9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c9f2c
    state: deferred
    reason: The term may be registered; the vocabulary decision is not made.
    revisit: When the vocabulary unification ledger decides on "carrier".
    decided-by: operator
    decided-at: "2026-11-13T15:04:00Z"
    applied-in: null
```

The atom paths in the example are illustrative; no higher-order check has a
catalog path yet.

## What the decisions command reads

Each item maps to one entry of the existing record without interpretation:
`note` from the file, the run and variant from the report, `class` from
`atom`, `decision` from `state`, and `item`, `reason` and the time from the
item's own fields. The code that parses strike lists, publication
manifests and packets is then needed only for runs made before this type.

## Open choices

1. **An approved change the operator rewords.** The strike lists forbid
   editing an entry, so a reworded replacement is a rejection plus a new
   item. The draft keeps that; an `amended` state is left out until a run
   shows the operator wanting it.
2. **Reasons on approvals.** Optional here. Requiring them would double the
   operator's typing for the common case and is not proposed.
3. **Who may expire an item.** The draft lets the procedure do it under
   rule 2. The operator sees the expiry in the new run's report, not as a
   question.
