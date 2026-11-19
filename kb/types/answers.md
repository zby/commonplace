---
type: types/type-spec.md
name: answers
description: "The operator's decision on each item of one question file: pending, approved, rejected or deferred, with reasons, bound to the question by hash"
schema: ./answers.schema.yaml
---

# Answers

An answers file records what the operator decided at one stop. A stop is a point where a procedure waits for the operator. The file holds one item per decision and names the question it answers by path and SHA-256. Use it for every operator decision over a list of proposals or findings and for a decision on one exact text, such as a plan's `stop`. Use [`edit-result`](./edit-result.md) for what an operation proposed; an answers file proposes nothing.

## Questions

A question is the file whose items the operator decides. There are three kinds:

| Question | Its items |
|---|---|
| an edit result with outcome `proposed` | its `proposals`, with ids `1`, `2` and so on in order; each item's `proposal` is the proposal's `quote`, `change` and `reason` |
| a review result with outcome `warn` or `fail` | its `findings` whose `level` is `warn` or `fail`, with the finding's position in `findings` as id (`1` for the first); each item's `proposal` is the finding's `scope`, `quotes`, `reason` and `level` |
| any other file: a text to approve | one item with id `text`, whose `proposal` names the file as `text` and its hash as `text-sha256` |

An approval of a text is therefore an answers file with one item that names the candidate's hash. `commonplace-revise answers create --from QUESTION` writes the pending file for a question, so nobody writes a hash by hand.

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
| `carried-from` | Optional. The earlier answers file this decision was copied from, when the same proposal was already decided for an earlier text of the note |
| `resolution` | Optional. What was done after the decision, when it differs from or goes beyond the proposal. A statement of fact, not a new decision |
| `refs` | Optional. Where it was done: commit hashes, file paths, a workshop directory or URLs. Not checked |

`deferred` means the operator has seen the item and has not decided it. Only the operator sets it. An agent that cannot decide an item leaves it `pending`.

## Decisions on findings

For a review result, the operator decides whether each finding stands. `approved` means the finding is right and should be acted on. `rejected` means the finding is wrong; the `reason` says why, and says whether it is wrong for this note only or because the criterion is too broad. `deferred` leaves it for later. A rejection does not change the review result. Later work on the note receives it: no fix is planned for a rejected finding, and the next review of the note against that criterion receives the operator's reason.

## Decisions carried over

A decision outlives the run it was made in. When a later run on the same note makes a proposal with the same `quote` and the same `change` as an item the operator already decided, the new answers file starts with that item decided: the earlier `state`, `reason`, `revisit`, `decided-by` and `decided-at`, and `carried-from` naming the earlier answers file. Code copies only an identical proposal. The operator sees the item at the stop and may change it; changing it removes `carried-from`. A proposal that differs in any way is asked as usual.

## What happened after the decision

A decision can lead to work the proposal did not describe. A reviewer's proposal to reword one sentence may end in a rewrite of the note and of the notes that cite it. `resolution` and `refs` record that on the decided item, so the proposal, the decision and the outcome can be compared later. They are written after the work, on a decided item only. In a run directory, keep the file again with `commonplace-revise answers record FILE` after adding them: the decision record reads the kept text.

## Acceptance

The deterministic validator accepts an answers file only when:

- `question-sha256` is the hash of the question file now;
- every item of the question appears once, with its `proposal` unaltered, and no other item appears;
- each state carries the fields the table above requires.

A consumer adds its own checks. The edit route applies only `approved` items, and refuses answers whose question is not an edit result of the same operation on the same input text. `commonplace-revise apply FILE` also refuses proposals made for another text of the note or under another write brief, and a file that approves nothing. A command that consumes or records an answers file keeps a copy of its text in its run's `answers/`; naming the file to that command is the operator's approval, and the decision record reads the kept copies. Publication reads no answers file: `commonplace-revise publish RUN` publishes a held candidate on the operator's word.

## Template

The pending file for a proposed edit result; `commonplace-revise answers create` writes it:

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
