---
description: KB-internal term defined once then reused throughout the body without ongoing context — reader loses the grounding.
---

## Failure mode

A KB-internal term is defined or linked once but then reused throughout the body without context. By the third or fourth use, the reader has lost the grounding.

## Test

Track KB-specific vocabulary through the note. If a term appears more than twice after its definition point, check whether later uses still make sense without scrolling back. Terms common in the field (context window, prompt) are fine. Terms specific to this KB's framework (bounded call, select(K), clean model) need ongoing context or should be replaced with plain language after the first grounded use.

## Example (fail)

Opening defines "bounded call" then body uses it 8 more times: "the next bounded call should see..." — "bounded" adds nothing once the concept is established.

## Example (pass)

"The next call should see a representation chosen for its task" — plain language in the body, full technical term reserved for the opening and Relevant Notes.
