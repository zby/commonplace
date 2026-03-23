=== SEMANTIC REVIEW: always-loaded-context-has-two-surfaces-with-different-affordances.md ===

Claims identified: 9

1. "Both CLAUDE.md and skill descriptions are always loaded" (scope claim)
2. "CLAUDE.md is imperative" (definition)
3. "Skill descriptions are suggestive" (definition)
4. Always-loaded context has exactly "two surfaces" (enumeration — title claim)
5. CLAUDE.md is "Good for universal constraints (git conventions, guardrails) and routing" (function claim)
6. Skill descriptions are "Good for task-specific workflows that the agent should know about but not always execute" (function claim)
7. "The overlap is intentional but serves different purposes" — "one pushes, the other pulls" (mechanism claim)
8. Decision rule: "If the agent must always follow it, CLAUDE.md. If the agent should know it's available and choose when to use it, skill description + skill body." (design rule)
9. Linked note is "foundation: the loading hierarchy that establishes why always-loaded context must be slim" (attribution)

WARN:
- [Completeness] The "two surfaces" enumeration may undercount. The actual always-loaded context in Claude Code includes additional surfaces beyond CLAUDE.md and skill descriptions — notably memory files (e.g. MEMORY.md) and project settings, which are also injected every session. These are neither imperative instructions nor capability advertisements; they are contextual state. The note's binary framing excludes them without acknowledging the boundary.
- [Completeness] The imperative/suggestive binary strains at routing instructions. The note classifies routing under CLAUDE.md's imperative affordance ("when you need X, look here"), but routing is conditional and informational rather than imperative — it tells the agent where to look when a condition is met, not what to always do. This makes routing a third affordance mode (conditional/declarative) that the binary doesn't cleanly accommodate. The note's own example — "before creating notes, read WRITING.md" — is a conditional trigger, not an unconditional constraint like "never use wiki-links."
- [Internal consistency] The decision rule ("If the agent must always follow it, CLAUDE.md") conflicts with the routing examples. Routing instructions in CLAUDE.md are not things "the agent must always follow" — they are conditional pointers the agent consults when relevant. Meanwhile, the skill description affordance ("the agent should know it's available and choose when to use it") also describes routing. The note acknowledges "overlap" but the decision rule presents a clean binary that the body's own examples undermine.

INFO:
- [Completeness] The note does not address descriptive/definitional content in CLAUDE.md (e.g., the Vocabulary section in the actual CLAUDE.md). Definitions are neither imperative constraints nor suggestive capabilities — they are reference material. This is a third content type that doesn't map to either surface's stated affordance, though it could arguably be subsumed under "routing" if routing is interpreted very broadly.
- [Completeness] The "push vs pull" mechanism framing implies the agent has genuine choice with skill descriptions but not with CLAUDE.md. In practice, agents also exercise discretion about which CLAUDE.md instructions to prioritize (attention is finite), so the push/pull distinction may be one of degree rather than kind.

PASS:
- [Grounding alignment] The link to "Instruction specificity should match loading frequency" is accurately attributed. The linked note does establish a 4-level loading hierarchy and explicitly references the current note as extending it by distinguishing two always-loaded surfaces. The current note correctly describes this as a foundation relationship. No vocabulary mismatch, no scope inflation.
- [Internal consistency] The imperative/suggestive definitions are used consistently throughout the note — CLAUDE.md is consistently described as imperative and skill descriptions as suggestive. No definition drift on these core terms.
- [Internal consistency] The overlap paragraph is internally coherent. It gives a concrete example (CLAUDE.md says "read WRITING.md" while a skill says "/connect") that accurately illustrates how both surfaces can point toward the same work through different mechanisms.

Overall: 3 warnings, 2 info
===
