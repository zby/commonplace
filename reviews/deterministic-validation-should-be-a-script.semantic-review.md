=== SEMANTIC REVIEW: deterministic-validation-should-be-a-script.md ===

Claims identified: 9

1. "Half of /validate's checks are hard-oracle" (description)
2. "Our `/validate` skill runs all checks through an LLM (Sonnet), including checks that are purely deterministic" (para 1)
3. "Thalo's 32 validation rules... all of which are deterministic scripts" (para 1, attribution to thalo-type-comparison.md)
4. "we're spending LLM tokens on work a Python script could do in milliseconds" (para 1, efficiency claim)
5. The split follows the oracle strength spectrum (para 2, framework claim)
6. Hard oracle enumeration: 7 items (frontmatter valid, description exists, type/traits/status enum, link targets resolve, areas-topics sync, unknown frontmatter fields, required sections per type)
7. Soft oracle enumeration: 2 items (description quality, composability)
8. "A validation script could run as a pre-commit hook or in CI" (final para)
9. "The `/validate` skill would then only need to run the judgment-based checks, making it cheaper and faster" (final para)

WARN:
- [Completeness] The description says "half of /validate's checks are hard-oracle" but the note's own enumeration lists 7 hard-oracle checks and 2 soft-oracle checks -- that is roughly 78%, not half. The Thalo comparison note's split table (which covers the same decomposition in more detail) lists 8 hard and 2 soft, which is 80%. "Half" significantly understates the proportion the note itself argues for. This may have been an early approximation that was not updated after the enumeration was finalized.
- [Completeness] The hard-oracle enumeration omits two checks present in the Thalo comparison note's "Checks we have that they don't" section: **orphan detection** (notes with no inbound links) and **accumulation signals** (seedling count, text file count). The Thalo comparison note explicitly classifies orphan detection as "Hard" oracle in its split table (line 143). Accumulation signals are listed as "batch INFO" and arguably belong somewhere in the taxonomy. The reviewed note's hard-oracle list is therefore incomplete relative to its own primary source.

INFO:
- [Completeness] "Required sections per type" is listed as a hard-oracle check, but the Thalo comparison note (line 109) says unknown-section warnings are "only useful once we define expected sections per type." If the expected sections are not yet formally defined for all types, this check may be only partially implementable as a deterministic script today. The note does not hedge this.
- [Grounding] The note says the split "follows the oracle strength spectrum" and links to oracle-strength-spectrum.md. The oracle-strength-spectrum note defines five levels (hard, soft, interactive, delayed, no oracle). The reviewed note collapses this to a binary hard/soft split, which is a simplification. The two soft-oracle checks (description quality, composability) are LLM-judged, which could also be characterized as "interactive oracle" (you ask an LLM for feedback) depending on interpretation. The binary collapse is pragmatically reasonable for this context but readers following the link may expect a richer mapping.
- [Grounding] The note's final paragraph claims the split "would make `/validate` cheaper and faster." This is plausible but unstated is that the total validation cost only decreases if the script replaces (rather than supplements) the LLM checks for the hard-oracle items. If users still run `/validate` as a single command that repeats all checks, the savings are architectural but not realized without workflow changes. The inference is reasonable but has an implicit prerequisite.

PASS:
- [Grounding] The attribution "Thalo's 32 validation rules... all of which are deterministic scripts" accurately reflects the Thalo comparison note, which states "Thalo has 32 deterministic validation rules" (line 93) and "Every one of Thalo's rules is **deterministic**" (line 126).
- [Grounding] The classification of the 7 hard-oracle items matches the oracle-strength-spectrum note's definition of hard oracle ("exact, cheap, deterministic check"). Each listed item (YAML parsing, enum matching, file existence checks, sync verification) is straightforwardly deterministic.
- [Grounding] The classification of the 2 soft-oracle items (description quality, composability) as requiring LLM judgment aligns with the oracle-strength-spectrum note's definition of soft oracle ("proxy score that correlates but isn't the real thing"). Both checks require semantic judgment that cannot be reduced to a deterministic rule.
- [Internal consistency] The note's body is internally consistent. The hard/soft split in the bullet lists matches the concluding claim about what moves to a script vs. what stays in the skill. No definition drift or section-level contradictions detected.
- [Internal consistency] The note's claim that areas-topics sync "already have `sync_topic_links.py`" is consistent with listing it as a hard-oracle check -- existing script implementation is evidence of deterministic feasibility.

Overall: 2 warnings, 3 info
===
