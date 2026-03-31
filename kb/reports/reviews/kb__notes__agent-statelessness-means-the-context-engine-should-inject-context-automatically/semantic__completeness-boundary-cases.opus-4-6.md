The note presents two frameworks: a four-row injection candidate table (definitions, area indexes, ADRs, specs) and a four-level loading hierarchy extension (always → on reference → on invoke → on demand). The definition type proposal is also tested.

---

**Framework 1: Four injection candidates**

Grounding: "Each row is a hypothesis about what context is needed when."

- Simplest: auto-injecting one small definition on first reference. The note establishes this as the cleanest case with four supporting properties (small, stable, referential, once-per-session). ✓
- Most extreme: auto-injecting full specs whenever implementing related features. The note lists this as a candidate. ✓
- Between: auto-injecting area indexes when "entering a topic area." The trigger "entering" is less well-defined than "first reference" — what counts as entering an area? INFO — the trigger for area index injection is vaguer than for definitions. The note acknowledges mechanism is open but this row has a softer trigger condition than the others.
- Adjacent: **convention/style guides** — when the agent is writing, it may need writing conventions injected. These are reference-like (similar to definitions) but broader. Not listed. The table is presented as illustrative, not exhaustive. ✓

**Framework 2: Four-level loading hierarchy**

1. Always (CLAUDE.md, skill descriptions), 2. On reference (definitions, ADRs, indexes), 3. On invoke (skill bodies), 4. On demand (methodology, source reviews).

- This extends the existing hierarchy by inserting a new layer. The insertion is clean — "on reference" sits naturally between "always" and "on invoke." ✓
- Boundary: when does "on reference" become "always"? If a term is referenced in nearly every document, auto-injection on every load approaches always-loaded. The note's once-per-session tracking handles definitions but not other types. INFO — the boundary between "on reference" and "always" isn't explicitly addressed for high-frequency references.

**Caveats coverage**

The note lists four caveats (requires own runtime, context budget, staleness, granularity) plus a discovery problem. These are well-calibrated for a speculative note. ✓

No WARN. Two INFOs: vague area-index trigger, and on-reference/always boundary for high-frequency terms.
