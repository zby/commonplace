<!-- REVIEW-METADATA
note-path: kb/notes/session-history-should-not-be-the-default-next-context.md
last-full-review-note-sha: 65fc2e33a6dbdff0ee77e1160f7f3f40697306bf
last-full-review-note-commit: 3450a4f69505c86b643b4cf3d8f8cda9671e9ea6
last-full-review-at: 2026-03-24T20:56:42+01:00
last-accepted-note-sha: 65fc2e33a6dbdff0ee77e1160f7f3f40697306bf
last-accepted-note-commit: 3450a4f69505c86b643b4cf3d8f8cda9671e9ea6
last-accepted-at: 2026-03-24T20:56:42+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: session-history-should-not-be-the-default-next-context.md ===

Checks applied: 4

INFO:
- [Description discrimination] The first clause adds genuine mechanism ("Storing execution history and loading it into the next agent call are separate decisions"), but the second clause ("chat and framework-owned tool loops conflate them by making session history the default next context") substantially restates the title. The description still discriminates because the storage-vs-loading separation is the key insight a searcher would need, but tightening the second clause to name the consequence (e.g., context pollution, loss of selective loading) instead of echoing the title would strengthen retrieval value.

CLEAN:
- [Title composability] "since session history should not be the default next context, we designed..." reads naturally as a sentence fragment. No awkward grammar when linked.
- [Claim strength] The claim is specific and non-obvious. Many real systems (chat UIs, framework-owned tool loops) do default to session history as next context, and practitioners could reasonably argue that continuity is the right default. The note argues against a common design choice, not a truism.
- [Title-body alignment] The body directly supports the title claim: it separates storage from loading decisions, explains why chat and tool-loop defaults are wrong for orchestration, walks through three trace types with different loading profiles, and concludes with a practical principle favoring artifact-first loading over transcript inheritance. No drift detected.

Overall: 0 warnings, 1 info
===
