---
gate_id: accessibility/jargon-persistence
name: Jargon Persistence
description: KB-internal term defined once then reused throughout the body without ongoing context — reader loses the grounding.
type: kb/types/review-gate.md
lens: accessibility
watches: [body]
staleness: changed
---

## Failure mode

A KB-internal term is defined or linked once but then reused throughout the body without context. By the third or fourth use, the reader has lost the grounding.

## Test

Track KB-specific vocabulary through the note. If a term appears more than twice after its definition point, check whether later uses still make sense without scrolling back. Terms common in the field (context window, prompt) are fine. Terms specific to this KB's framework that have plain-language equivalents need ongoing context or should be replaced with plain language after the first grounded use.

Note: if a term's qualifier carries meaning that plain language alone doesn't recover (e.g., "bounded call" vs "call"), this gate does not apply — the fix there is glossing or refreshing context, not stripping the qualifier.

## Example (fail)

Opening defines "external symbolic state" then body uses it 6 more times: "The scheduler can afford to keep many artifact kinds in external symbolic state" — the phrase is opaque without scrolling back to the definition.

## Example (pass)

"The scheduler can afford to keep many artifact kinds in its stored state" — plain language in the body, full technical term reserved for the opening and Relevant Notes.
