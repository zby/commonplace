---
gate_id: sentence/misleading-link-text
name: Misleading Link Text
description: Markdown link text implies a concept but the linked note discusses something different — reader gets wrong impression.
type: kb/types/review-gate.md
lens: sentence
watches: [body]
staleness: changed
---

## Failure mode

The text of a markdown link implies a concept, but the linked note discusses something different. The reader who follows the link will be confused; the reader who doesn't will have a wrong impression of what the link supports.

## Test

For each markdown link, read the link text and the sentence it appears in. What
does the reader expect to find at the target? Then read the target's title and
opening paragraph. Does the target match the expectation? Open more of the
target only when its head does not settle the question.

Check every link. Repeated links to the same target are one check. Name any
target that cannot be resolved.

## Example (fail)

`"This is the [return-value problem](./llm-context-is-composed-without-scoping.md) in architectural form"` — link text says "return-value problem" but the target's "return value problem" section discusses interface typing, not trace leakage.
