---
gate_id: accessibility/undefined-terms
name: Undefined Terms
description: Technical term used without inline definition — reader must follow a link or know KB context to understand the sentence.
type: kb/types/instruction.md
lens: accessibility
watches: [body]
staleness: changed
---

## Failure mode

A technical term or concept is used as if the reader already knows it, with no inline definition or gloss. A link is not a definition — the reader should not have to follow a link to understand the sentence.

## Test

On first encounter of each technical term, ask: does the surrounding sentence define it, paraphrase it, or give enough context to infer its meaning?

Exceptions — do not flag:
- Standard technical vocabulary (LLM, context window, prompt, token, API).
- Terms whose opacity is already covered by the notation-opacity gate (e.g., "external symbolic state" when the real access barrier is the `K` notation it labels). Do not double-flag the English phrase alongside a notation-opacity finding for the same concept.

KB vocabulary terms (`kb/notes/definitions/` — currently: distillation, constraining, codification, context engineering) are NOT exempt. Authors know these terms from CLAUDE.md, but external readers do not. On first mention, provide both an inline gloss and a link to the definition note. The gloss lets the reader keep reading; the link lets them go deep.

## Example (fail)

"An execution boundary usually creates two different questions"

## Example (fail — KB vocabulary without gloss)

"The skill is produced by distillation from the methodology notes."

## Example (pass)

"An execution boundary — any point where one LLM call ends and another begins — creates two distinct decisions"

## Example (pass — KB vocabulary with gloss and link)

"The skill is produced by [distillation](./definitions/distillation.md) (directed context compression) from the methodology notes."
