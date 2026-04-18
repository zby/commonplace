---
gate_id: accessibility/notation-opacity
name: Notation Opacity
description: Formal notation from another note used in prose without local definition — opaque to readers who haven't read the source model.
type: instruction
lens: accessibility
watches: [body]
staleness: changed
---

## Failure mode

Formal notation or variable names from another note appear in prose. The reader must read the linked note to decode the sentence.

## Test

For each piece of notation (`K`, `select(K)`, `P`, etc.), check: is it defined in this note, or does the sentence only make sense if you already know the notation from elsewhere?

Prefer recommending replacement with plain language over glossing. "The scheduler's accumulated state" is better than "the scheduler's accumulated state `K`" — the backtick notation signals "you should already know this symbol." Only keep notation if the note uses it in formal arguments (equations, pseudocode).

## Example (fail)

"Storage in `K` is cheap; bounded context is expensive."

## Example (pass)

"The scheduler's state can store everything — but the prompt for the next call should be assembled by a deliberate selection step."
