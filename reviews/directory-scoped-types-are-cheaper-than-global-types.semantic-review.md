=== SEMANTIC REVIEW: directory-scoped-types-are-cheaper-than-global-types.md ===

Claims identified: 14

**Claims extracted:**

1. "The document classification spec defines seven global base types" (opening paragraph)
2. "Every global type is a permanent tax on context, loaded every session whether relevant or not" (opening paragraph)
3. "Most structural affordances are directory-local" (opening paragraph + "Where affordances actually live" section)
4. "The global type mostly says `note` — which tells an agent almost nothing about what it can do with the document" (end of affordances table)
5. "In programming, types are global (at least fully qualified names are) — and cheap" because "only the ones you import are in scope" (programming section)
6. "In an LLM context, there's no compiler and no import mechanism. Every type the agent needs to reason about must be in the context window" (programming section)
7. "Directory-scoping is a workaround for this: the directory README is a primitive import mechanism" (programming section)
8. "[Instruction specificity should match loading frequency] establishes the loading hierarchy: always-loaded surfaces should be slim, task-specific detail loads on demand" (economic argument)
9. "A thin global layer might be just the maturity ladder" of `text` and `note` (economic argument)
10. "Everything else — adr, source-review, structured-claim, review, index — is a directory-local specialisation of note" (economic argument)
11. "The types that genuinely move are text and note... The non-portable types are the ones currently paying global cost for no global benefit" (portability section)
12. "CLAUDE.md gets thinner" / "Directory READMEs become type definitions" / "Validation becomes directory-aware" / "Templates stay where they are" (what would change section)
13. "The CLAUDE.md routing table and content workflow now implement this proposal" with global types (`text`, `note`) and directory types loaded on demand (current implementation section)
14. "This is progressive disclosure applied to the type system" (current implementation section)

---

WARN:
- [Completeness — boundary case: structured-claim portability] The note claims "The types that genuinely move are text and note" and that everything else is directory-local. But `structured-claim` is explicitly designed to work across directories. The note's own linked source (document-types-should-be-verifiable.md) says traits and types are directory-independent, and the orthogonality note (referenced in this note's "What moves between directories?" section) argued that "a structured-claim works identically in notes/, claw-design/, or anywhere." The note acknowledges this counter-argument but only as a quote it then dismisses with "But in practice, how many documents actually move?" This is a rhetorical dismissal rather than a refutation. If structured-claim is genuinely portable (which the note concedes), then the claim that only text and note are portable is false by the note's own admission. The open questions section partially acknowledges this ("Does structured-claim stay global?") but the body's assertion is stated categorically.

- [Grounding — scope mismatch with why-directories-despite-their-costs.md] The note cites why-directories-despite-their-costs.md as supporting the idea that "directories already carry local conventions; this note proposes making that load-bearing for types." However, the directories note contains an explicit section titled "Types and directories are orthogonal" which directly argues the opposite: "If types depended on directories, you'd need to redefine types whenever someone creates a new subdirectory." and "The document classification system should work across any directory structure." The cited source actively opposes the proposal this note makes. The note is borrowing the directories note's observation about local conventions while ignoring its explicit argument that types should NOT be directory-scoped. This is selective attribution.

- [Grounding — claim count mismatch with document-classification.md] The note states "the document classification spec defines seven global base types: text, note, structured-claim, spec, review, index, adr." The actual document-classification.md lists exactly seven rows in its base types table, so the count is correct. However, the note frames these as types that are all "loaded every session whether relevant or not." But document-classification.md itself has already been updated to acknowledge directory-scoped types: "The type field is a free-form string. The table below lists the common values; directory-scoped types/ folders document the structural expectations for each." The source already accommodates directory-local definitions — the note frames the source as more rigid than it currently is.

INFO:
- [Completeness — boundary case: index type] The note proposes that `index` is a "directory-local specialisation of note." But indexes are cross-cutting navigation artifacts. A tags-index.md or links-index.md serves the entire KB, not a single directory. Indexes don't belong to any one directory the way an ADR belongs to adr/. The note's framework doesn't clearly account for types that are structurally specialized but not directory-local in their scope of service.

- [Completeness — boundary case: on-demand loading already exists] The note frames the situation as a binary: either types are loaded globally upfront or they are directory-scoped. The note itself acknowledges a third option — "If we had real on-demand type resolution... types could be global names with on-demand definitions, just like programming" — but treats it as hypothetical. In practice, the CLAUDE.md routing table + escalation boundaries already implement partial on-demand resolution: the agent sees type names in the routing table and loads type definitions only when about to write one. This is closer to the "import" mechanism than the note acknowledges, which weakens the framing that directory-scoping is the only available workaround.

- [Internal consistency — tension between "current implementation" and body argument] The "Current implementation" section claims the proposal is already implemented: "The CLAUDE.md routing table and content workflow now implement this proposal." But the body argues for reducing the global type vocabulary to just text and note, while document-classification.md still lists seven base types and CLAUDE.md's routing table still references `structured-claim` as a type. The implementation section describes progressive disclosure (load specialized types on demand), which is a weaker claim than the body's proposal (eliminate most global types). The note quietly shifts from "shrink the global vocabulary" to "load definitions on demand" without marking this as a different proposal.

- [Internal consistency — "What stays global" list vs. body] The "What stays global" section lists "Status ladder — seedling/current/speculative/outdated" as a global affordance. But the body's thin global layer table lists only `text` and `note` as global types, and the status ladder is a property of `note`, not a separate type. This is not a contradiction, but the note conflates two different meanings of "global": global types (the type field vocabulary) and global conventions (properties that all notes share). The "What stays global" section is about conventions, not types, but this distinction is never made explicit.

PASS:
- [Completeness — affordances table] The "Where affordances actually live" table accurately maps structural expectations to their actual locations. Cross-checking: related-systems, adr, tasks, sources, and structured-claim structural requirements are indeed defined in directory-local READMEs/templates, not in the global type field. The observation that the global type field mostly says `note` for these is accurate.
- [Grounding — instruction-specificity-should-match-loading-frequency.md] The note cites this as establishing "the loading hierarchy: always-loaded surfaces should be slim, task-specific detail loads on demand." The source confirms this: "match instruction specificity to loading frequency. Universal rules load always. Task-specific rules load when doing that task." The attribution is accurate and the economic argument for types correctly extends this principle to the type system domain.
- [Grounding — ADR-002] The note cites ADR-002 as the decision to inline the note template in WRITING.md. ADR-002 confirms: "Inline the note and structured-claim templates directly into kb/instructions/WRITING.md." The attribution is accurate.
- [Grounding — workshop layer note] The note cites a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md for the claim that "workshop subsystems (tasks, queues) already define their own types locally." The source confirms: "Each temporal subsystem (tasks, decision threads, experiments, queues) has its own state machine... local conventions per subsystem... is likely the right default." The attribution is accurate.
- [Internal consistency — programming analogy] The programming section's argument is internally coherent: it identifies that the cost difference between programming types and LLM types comes from the resolution mechanism (compiler import vs. context pre-loading), and correctly identifies directory-scoping as a workaround for the lack of an import mechanism. The analogy holds without contradiction.
- [Internal consistency — open questions] The open questions section honestly surfaces tensions that the body does not fully resolve (structured-claim's status, the type field's future, searchability). This is appropriate for a seedling-status note.

Overall: 3 warnings, 4 info
===
