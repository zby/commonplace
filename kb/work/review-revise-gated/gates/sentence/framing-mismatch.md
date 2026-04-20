---
type: kb/types/instruction.md
description: Sentence frames its claim in terms of X but the actual mechanism is Y — narrows or misdirects the reader.
---

## Failure mode

A sentence frames its claim in terms of X, but the actual mechanism is Y. The framing narrows or misdirects the reader's understanding.

## Test

For each sentence that gives a reason or explains a mechanism, ask: is the stated framing the right level of generality? Is the mechanism correctly identified?

**Severity:** WARN when the framing *excludes* cases the mechanism actually covers (e.g., "for orchestration" when the mechanism applies to any bounded call). INFO when the framing merely *emphasizes* one domain without excluding others.

## Example (fail)

"For orchestration, that is usually the wrong trade" — frames the problem as orchestration-specific, but the mechanism (LLMs degrade with context complexity) applies to any call needing full cognitive capacity.

## Example (pass)

"LLMs degrade with context complexity — every token spent parsing irrelevant history is cognitive budget not spent on the actual task."
