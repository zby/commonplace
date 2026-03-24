<!-- REVIEW-METADATA
note-path: kb/notes/quality-signals-for-kb-evaluation.md
last-full-review-note-sha: 7fcd422068ef60dbf9f01805d264d4a689a8b33d
last-full-review-note-commit: d1d69393d519758d93ae3c6987b3fc2350077c45
last-full-review-at: 2026-03-24T20:56:25+01:00
last-accepted-note-sha: 7fcd422068ef60dbf9f01805d264d4a689a8b33d
last-accepted-note-commit: d1d69393d519758d93ae3c6987b3fc2350077c45
last-accepted-at: 2026-03-24T20:56:25+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: quality-signals-for-kb-evaluation.md ===

Checks applied: 4

INFO:
- [Title composability] The title "Quality signals for KB evaluation" is a bare noun phrase — "since quality signals for KB evaluation..." does not complete a thought. A composable alternative might be "many weak quality signals can substitute for a single reliable KB oracle" or similar. However, this is a speculative brainstorming note (status: speculative) cataloguing signals rather than arguing a claim, so a topical title is defensible here.

CLEAN:
- [Description discrimination] The description adds mechanism (combining graph-topology, content-proxy, and LLM-hybrid signals into a composite oracle), scope (mutation-based KB learning loop), and a key constraint (without requiring usage data). Against the topical title, the description carries substantial retrieval value — an agent seeing this in a list of 5 results would immediately know what distinguishes this note from other KB-quality notes.
- [Claim strength] The title is topical, not phrased as a claim. The exceptions apply: the note is exploratory/speculative (status: speculative), cataloguing candidate signals rather than asserting a thesis, so a topical title is the correct choice here. No false claim to sharpen.
- [Title-body alignment] The title promises a catalogue of quality signals for KB evaluation, and the body delivers exactly that — organized into static signals (graph topology, content proxies, structural health), metamorphic relations, compound signals, LLM-hybrid approaches, and agent-centric signals. The body extends beyond pure cataloguing into the "many weak signals" hypothesis and a learning-loop proposal, but the opening paragraph scopes this explicitly, and for a speculative brainstorming note this breadth is expected rather than scope drift.

Overall: 0 warnings, 1 info
===
