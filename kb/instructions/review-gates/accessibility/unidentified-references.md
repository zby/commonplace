---
gate_id: accessibility/unidentified-references
name: Unidentified References
description: Named system, tool, or organization introduced without enough context for the reader to know what it is.
type: instruction
lens: accessibility
watches: [body]
staleness: changed
---

## Failure mode

A named system, tool, person, or organization is introduced without enough context for the reader to know what it is.

## Test

For each proper noun (system name, product name), check: does the note say what it is on first mention?

A link to a dedicated page (e.g., a related-system review note) provides navigational context but does not substitute for inline identification — the reader should not have to follow a link to know what kind of thing a name refers to. A brief inline gloss ("Spacebot, a concurrent agent framework") is required even when a link exists.

Only recommend identification if the information is stated in the note itself or its linked sources. Do NOT guess or fabricate attributions. If the note doesn't say who made a system, recommend that the author add the identification — do not supply it yourself.

## Example (fail)

"Slate is the main tension case."

## Example (pass)

"Random Labs' Slate, an agent orchestration system, is the main tension case."
