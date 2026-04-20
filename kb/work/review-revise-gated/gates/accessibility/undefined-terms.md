---
type: kb/types/instruction.md
description: Technical term used without inline definition — reader must follow a link or know KB context to understand the sentence.
---

## Failure mode

A technical term or concept is used as if the reader already knows it, with no inline definition or gloss. A link is not a definition — the reader should not have to follow a link to understand the sentence.

## Test

On first encounter of each technical term, ask: does the surrounding sentence define it, paraphrase it, or give enough context to infer its meaning?

Exceptions — do not flag:
- Standard technical vocabulary (LLM, context window, prompt, token, API).
- Terms defined in `kb/notes/definitions/` (distillation, constraining, codification, context engineering) when the note links to the definition. The link serves as the definition point.
- Terms whose opacity is already covered by the notation-opacity gate (e.g., "external symbolic state" when the real access barrier is the `K` notation it labels). Do not double-flag the English phrase alongside a notation-opacity finding for the same concept.

## Example (fail)

"An execution boundary usually creates two different questions"

## Example (pass)

"An execution boundary — any point where one LLM call ends and another begins — creates two distinct decisions"
