<!-- REVIEW-METADATA
note-path: kb/notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md
last-full-review-note-sha: 347f2f6285a6ac6ae0d56021413382ddfb62d36a
last-full-review-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-full-review-at: 2026-03-24T14:34:00+01:00
last-accepted-note-sha: 347f2f6285a6ac6ae0d56021413382ddfb62d36a
last-accepted-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-accepted-at: 2026-03-24T14:34:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism the title cannot carry: "recover from broken tools via agent workarounds" explains WHY the health signal degrades, and "underlying scripts and workflows" narrows what is at risk. Against a search result list on "tool loop health" or "observability," this would distinguish the note from adjacent notes about debugging intuitions or enforcement/recovery.
- [Title composability] "since apparent success is an unreliable health signal in framework-owned tool loops, we added degraded-execution reporting" reads as natural prose. The title functions as a linkable clause without grammatical awkwardness.
- [Claim strength] The claim is non-obvious and contestable. A reasonable counterargument is that framework-level logging already makes workaround paths visible, or that artifact-level success is the only metric that matters. The title stakes a specific position rather than stating a truism.
- [Title-body alignment] The body directly supports the title: it explains the three-outcome compression that weakens the health signal, why framework-owned loops encourage silent recovery, practical consequences (synchronous vs. asynchronous observation), and theoretical placement in the runtime decomposition. No claim drift or scope drift detected.

Overall: CLEAN
===
