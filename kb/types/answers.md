---
type: types/type-spec.md
name: answers
description: "The operator's decision on each item of one question file: pending, approved, rejected or deferred, with reasons, bound to the question by hash"
schema: ./answers.schema.yaml
---

# Answers

An answers file records what the operator decided at one stop. A stop is a point where a procedure waits for the operator. The file holds one item per decision and names the question it answers by path and SHA-256. Use it for every operator decision over a list of proposals and for every approval of an exact text. Use [`edit-result`](./edit-result.md) for what an operation proposed; an answers file proposes nothing.

## Questions

A question is the file whose items the operator decides. There are two kinds:

| Question | Its items |
|---|---|
| an edit result with outcome `proposed` | its `proposals`, with ids `1`, `2` and so on in order; each item's `proposal` is the proposal's `quote`, `change` and `reason` |
| any other file: a text to approve | one item with id `text`, whose `proposal` names the file as `text` and its hash as `text-sha256` |

An approval of a text is therefore an answers file with one item that names the candidate's hash. `commonplace-review answers create --from QUESTION` writes the pending file for a question, so nobody writes a hash by hand.

## Items

| Field | Meaning |
|---|---|
| `id` | The item's id in the question |
| `proposal` | The question's item, copied unaltered |
| `state` | `pending`, `approved`, `rejected` or `deferred` |
| `reason` | Why, in the operator's words. Required for `rejected` and `deferred`; optional for `approved` |
| `revisit` | The condition under which a `deferred` item is taken up again |
| `decided-by` | `operator` on every decided item; absent while `pending` |
| `decided-at` | The decision's timestamp; absent while `pending` |
| `resolution` | Optional. What was done after the decision, when it differs from or goes beyond the proposal. A statement of fact, not a new decision |
| `refs` | Optional. Where it was done: commit hashes, file paths, a workshop directory or URLs. Not checked |

`deferred` means the operator has seen the item and has not decided it. Only the operator sets it. An agent that cannot decide an item leaves it `pending`.

## What happened after the decision

A decision can lead to work the proposal did not describe. A reviewer's proposal to reword one sentence may end in a rewrite of the note and of the notes that cite it. `resolution` and `refs` record that on the decided item, so the proposal, the decision and the outcome can be compared later. They are written after the work, on a decided item only. In a run directory, approve the file again after adding them: the decision record reads the approved text.

## Acceptance

The deterministic validator accepts an answers file only when:

- `question-sha256` is the hash of the question file now;
- every item of the question appears once, with its `proposal` unaltered, and no other item appears;
- each state carries the fields the table above requires.

A consumer adds its own checks. The edit route applies only `approved` items, and refuses answers whose question is not an edit result of the same operation on the same input text. Publication writes a candidate only when its `text` item is `approved` and the note still holds the text the run started from.

## Template

The pending file for a proposed edit result; `answers create` writes it:

```markdown
---
type: types/answers.md
description: The operator's answers to kb/reports/state/review/runs/v2/<run>/artifact/edits/<observation>/results/<launch>/result.md
question: kb/reports/state/review/runs/v2/<run>/artifact/edits/<observation>/results/<launch>/result.md
question-sha256: <64 hex>
items:
- id: '1'
  proposal:
    quote: the passage
    change: the replacement
    reason: why
  state: pending
---

# Answers
```

A decided item, rejected:

```yaml
- id: '1'
  proposal: {quote: the passage, change: the replacement, reason: why}
  state: rejected
  reason: the operator's reason
  decided-by: operator
  decided-at: '2026-11-15T12:00:00Z'
```

---

Relevant Notes:

- [ADR 134 — Stops record the operator's answers in one typed file](../reference/adr/134-stops-record-the-operators-answers-in-one-typed-file.md) — depends-on: the decision that defines this type and its acceptance
