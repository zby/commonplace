---
gate_id: complexity/connection-inflation
name: Connection inflation
lens: complexity
watches: [body]
staleness: changed
---

## Failure mode

Relevant Notes entries add no navigational value beyond what the body already provides.

## Background

In this KB, inline links and footer entries serve different functions (see `kb/notes/link-strength-is-encoded-in-position-and-prose.md`). Inline links are part of the argument — they carry weight from the surrounding prose. Footer entries are typed navigation edges — they carry explicit relationship semantics (extends, grounds, contradicts, etc.) that help agents decide what to read next without loading the target.

A note that uses `[X](./x.md)` inline as evidence AND has a footer entry `[X](./x.md) — extends: ...` is **not** automatically inflated. The footer entry adds a typed relationship and a context phrase that the inline citation does not carry. Inflation occurs when the footer entry restates the same relationship the body already articulates — same link, same framing, no new information.

## Test

For each Relevant Notes entry, ask two questions:

1. Does the body already link to the same note AND fully articulate the same relationship the footer describes? If yes, the footer entry is inflated.
2. Does the footer entry add relationship semantics (extends, grounds, contradicts), navigational context, or a framing absent from the body's inline usage? If yes, the footer entry is not inflated, even if the body also links to the same note.

Report entries that fail both questions. Do not flag footer entries merely because the body also links to the same note — that alone is not inflation.
