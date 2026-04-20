---
type: kb/types/instruction.md
description: Workshop review gate for checking anthropomorphic framing during review-revise experiments
gate_id: prose/anthropomorphic-framing
name: Anthropomorphic framing
lens: prose
watches: [body]
staleness: changed
---

## Failure mode

The note attributes human-like mental properties to models where more precise technical language would be more accurate.

## Test

Scan the entire note for verbs and nouns such as `possesses knowledge`, `understands`, `believes`, or `knows`. For each occurrence, ask whether it implies internals or agency claims the note does not mean to defend. Report all instances.

Prefer technical alternatives like `stores`, `encodes`, `produces`, or `surfaces` unless the note is explicitly arguing about cognitive status.

**Exception:** Conventional metonymy applied to software systems is not anthropomorphism. Phrases like "the system wants," "the API expects," "sessions are optimized for," "the protocol requires" are standard technical shorthand — do not flag these unless the note is making literal claims about system cognition.
