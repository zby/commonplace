---
type: types/type-spec.md
name: edit-result
description: "One completed run of an edit operation on one note text: changed, unchanged, proposed or problem, with controller-owned provenance"
schema: ./edit-result.schema.yaml
---

# Edit result

An edit result records one run of an [edit operation](./edit-operation.md) on one input text of a note. Use it for that run's outcome and report. Use [`review-result`](./review-result.md) for a judgment of a text; an edit result judges nothing.

An edit result has no freshness state. It names the hash of the text it was made from. It describes that text, and no other, so it never becomes stale. Completion means the result passed deterministic checks. It does not mean the edit is good.

## Outcomes

| `outcome` | Worker supplies | Code checks |
|---|---|---|
| `changed` | the complete candidate text as a separate output, one `changes` line per change | the candidate differs from the input; the bounds below hold |
| `unchanged` | a report saying why nothing changed | any candidate output equals the input |
| `proposed` | `proposals`, applied to nothing | each proposal's `quote` occurs exactly once in the input, by the shared prose quote matcher |
| `problem` | what blocked the operation, as the worker's problem report | no changes, proposals or candidate are present |

A `none` operation returns `changed` or `unchanged`. A `per-item` operation returns `proposed` or `unchanged` on its first run. Run again with an [answers](./answers.md) file over that result as its `answers` input, it applies the `approved` items and returns `changed`.

Each proposal holds `quote`, a passage of the input that identifies where the change applies; `change`, the proposed replacement or decision; and `reason`. A quote is matched after whitespace and typographic quote marks are normalized.

## Bounds

Code accepts a `changed` candidate only when:

- the frontmatter title, type and brief declaration and the H1 are the input's;
- `user-verified` is gone when the body changed;
- the validator finds no failure the input text did not have;
- every link target of the input is still in the candidate, or is named in `removed-links`;
- every quoted span of the input is still in the candidate. A quoted span is a Markdown blockquote or a quotation the validator pairs with a `verbatim` citation.

With an `answers` input, the validator must accept the answers file, its question must be a result of the same operation on the same input text, and every item that is not `approved` must still have its quoted passage in the candidate. Code does not detect a change outside the answered items.

An operation's own `## Preserve` section binds the worker. Code checks only the bounds above.

## Field ownership

The worker writes two outputs: the result fragment and, for `changed`, the candidate text. The fragment supplies only `type`, `outcome`, `changes`, `proposals`, `removed-links` and the body. Code completes and validates it. A worker never writes hashes, paths or identities.

| Fields | Owner and meaning |
|---|---|
| `type`, `outcome`, `changes`, `proposals`, `removed-links` | Worker content |
| `description`, `format` | Controller's result-format identity |
| `operation`, `operation-sha256` | The operation's identity and the hash of the exact operation text the worker received |
| `note`, `input-sha256` | The note's identity and the hash of the exact input text |
| `candidate`, `candidate-sha256` | The retained candidate file in the observation and its hash; null when there is no candidate |
| `observation`, `contract-sha256` | The execution observation and the captured output-contract identity |
| `profile`, `model`, `run`, `launch`, `completed-at` | Requested execution configuration and observed execution provenance |
| `raw-output`, `raw-output-sha256` | The retained worker fragment; null for a problem, whose report is the body |

The candidate text is a file in the observation, not a field of the result.

## Template

Worker fragment for a `changed` outcome; code supplies the remaining fields:

```markdown
---
type: types/edit-result.md
outcome: changed
changes:
  - "Moved the claim sentence into the opening paragraph."
removed-links: []
---

# Report

One structural move; four sentence-level edits.
```

A `proposed` fragment replaces `changes` with `proposals`, each a mapping with `quote`, `change` and `reason`, and writes no candidate.

---

Relevant Notes:

- [ADR 133 — Edit operations run alone through one typed route](../reference/adr/133-edit-operations-run-alone-through-one-typed-route.md) — depends-on: the decision that defines this result and its acceptance
