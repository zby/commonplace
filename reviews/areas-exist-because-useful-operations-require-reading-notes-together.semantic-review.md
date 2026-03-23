=== SEMANTIC REVIEW: areas-exist-because-useful-operations-require-reading-notes-together.md ===

Claims identified: 14

1. "Two operations justify areas" — orientation and comparative reading (§ The operations)
2. Comparative reading produces seven concrete outputs: redundancy, contradiction, tension, complementarity, merge candidates, missing connections, gaps (§ The operations)
3. "Orientation is read-only… Comparative reading is the write operation" (§ The operations)
4. "Both operations impose the same two constraints on the note set" — context is finite, yield depends on relatedness (§ The constraints)
5. "Yield also depends on maturity" (§ The constraints)
6. "The split threshold of ~40 notes isn't arbitrary — it's the approximate point where an area stops fitting in working context" (§ Areas are the mechanism), citing WRITING.md
7. "Misplaced notes are actively harmful, not neutral" (§ Areas are the mechanism)
8. "Orphaned notes are invisible to both operations" (§ Areas are the mechanism), citing stale-indexes note
9. "Single-area membership is the default" (§ Areas are the mechanism)
10. "Area splits are yield optimisations, not taxonomic refinements" (§ Areas are the mechanism)
11. "Tag the most precise useful area" — the `areas:` field generates Topics footer links (§ Conventions that follow)
12. "Don't dual-tag parent and child" (§ Conventions that follow)
13. "Multiple areas are fine for independent dimensions" (§ Conventions that follow)
14. "areas.md stays flat" (§ Conventions that follow)

WARN:
- [Grounding alignment — scope mismatch] The note claims "The split threshold of ~40 notes" is specified in WRITING.md (two links: "split threshold of ~40 notes" and "~40 note threshold" both point to `../instructions/WRITING.md`). WRITING.md does not contain any mention of a 40-note threshold, a split threshold, or indeed any area-related conventions. The `areas:` frontmatter field has been replaced by `tags:` per ADR 004. WRITING.md now references tags and tag indexes exclusively. A reader following these links will not find the claimed content.

- [Grounding alignment — domain drift] The entire "Conventions that follow" section (claims 11-14) prescribes rules for an `areas:` frontmatter field that no longer exists in the system. ADR 004 (status: proposed, 2026-03-13) replaces `areas:` with freeform `tags:` and explicitly lifts several constraints this note establishes — the parent/child prohibition, the single-area default, the ~40 note split pressure. The note's conventions section describes a system state that has been superseded. Readers encountering this note will receive guidance that contradicts current WRITING.md and ADR 004.

- [Grounding alignment — attribution accuracy] The "Distilled into" footer states: "[WRITING.md](../instructions/WRITING.md) — area assignment rules, lifecycle split threshold, and areas field description." WRITING.md contains none of these three items. The distillation link claims a downstream relationship that does not hold; either the distillation was undone when WRITING.md migrated to tags, or it never occurred.

INFO:
- [Completeness — boundary case] The note claims "Two operations justify areas" and treats this as exhaustive. A boundary case: **incremental update** — an agent opens an area not to orient or to do comparative reading, but to add a single new note and decide where it fits. This is closer to a classification operation than either orientation or comparative reading. The note could argue this is a sub-case of orientation (you must orient to classify), but the distinction is worth examining because the constraints differ: incremental update needs the index and descriptions, not necessarily every note body loaded.

- [Completeness — boundary case] The seven outputs of comparative reading (claim 2) include "missing connections" and "gaps." These two are discovery operations, not strictly comparative — they involve noticing what is absent rather than comparing what is present. The note could argue they emerge naturally from comparative passes, but a boundary case like "the area has no note about X" is qualitatively different from "these two notes contradict." The enumeration blurs the line between comparative operations and gap analysis.

- [Completeness — boundary case] The note claims both operations impose "the same two constraints" (context finite, yield depends on relatedness). A third potential constraint: **coherence of abstraction level**. Loading 30 notes that are all related but span three abstraction levels (foundational definitions, mid-level mechanisms, high-level design patterns) may frustrate comparative reading because the notes aren't comparable — you can't detect redundancy between a definition and a design pattern even if they're about the same topic. The note's "relatedness" constraint partially covers this, but relatedness and same-level-of-abstraction are distinct properties.

- [Internal consistency — tension acknowledged but unresolved] The "Tension" section (§ Tension: orientation and comparative reading pull index design in opposite directions) acknowledges that the two operations pull index design in different directions but leaves this unresolved. The note's central claim — that areas are justified by *both* operations imposing the *same* constraints — is somewhat undercut by this acknowledgment that the operations have genuinely different requirements for index structure. The note handles this honestly (it doesn't hide the tension), so this is INFO not WARN.

- [Internal consistency — definition drift] The note defines "area" as "a set of notes where reading together is expected to be productive" (§ Areas are the mechanism). But the "Conventions that follow" section shifts to discussing `areas:` as a frontmatter field that "generates Topics footer links." These are different objects: the conceptual area (a set for reading together) and the implementation mechanism (a frontmatter field driving index membership). The note moves between these without flagging the shift. The conceptual arguments would survive the areas-to-tags migration; the implementation conventions would not.

PASS:
- [Completeness — operations enumeration] The claim that orientation and comparative reading are the two operations that justify areas was tested against boundary cases. Both operations are well-defined, clearly distinct, and map to real agent activities. The core two-operation framework holds even though edge cases (incremental update) probe its boundaries.
- [Grounding alignment — stale indexes note] The note claims "a note that falls out of its area index disappears from maintenance" and links to stale-indexes-are-worse-than-no-indexes.md. The source note does establish exactly this mechanism: "Notes missing from the index become invisible not because they're hard to find, but because nobody looks for them." Attribution is accurate.
- [Grounding alignment — context efficiency note] The note cites context-efficiency-is-the-central-design-concern-in-agent-systems.md as the foundation for "context is the scarce resource." The source note directly establishes this: "the scarce resource is context — the finite window of tokens the agent can attend to." Attribution is accurate and the dependency is sound.
- [Grounding alignment — deep search note] The note claims /connect handles "cross-area connections that within-area operations don't reach" and links to deep-search-is-connection-methodology-applied-to-temporarily-expanded-corpus.md. The source note describes exactly this: expanding the corpus temporarily to find connections beyond routine area loading. Attribution is accurate.
- [Grounding alignment — type-system-index] The note refers to "three output-quality arguments" and links to type-system-index.md. That index does list exactly three arguments under "Output Quality." Attribution is accurate.
- [Grounding alignment — quality signals note] The note mentions comparative reading yield as a potential quality signal and links to quality-signals-for-kb-evaluation.md. The source note does discuss index coverage and cluster coefficients as quality signals, and the open question about "yield per area" as a signal is a reasonable extension. Attribution is accurate.
- [Internal consistency — no pairwise contradictions] The note's sections are internally consistent. The operations section defines two operations; the constraints section derives two constraints that apply to both; the mechanism section derives conventions from those constraints. The logical chain is sound throughout.
- [Internal consistency — summary faithfulness] The note has no compressed summary section, so there is no summary-body divergence to check.

Overall: 3 warnings, 5 info
===
