<!-- REVIEW-METADATA
note-path: kb/notes/agents-navigate-by-deciding-what-to-read-next.md
last-full-review-note-sha: c3ac9804782d91ba09304e79a07ace91b6258e32
last-full-review-note-commit: 0d4ee7df7ed3293f4d6e0a7d48ed2ac46ea46a9f
last-full-review-at: 2026-03-24T14:34:00+01:00
last-accepted-note-sha: c3ac9804782d91ba09304e79a07ace91b6258e32
last-accepted-note-commit: 0d4ee7df7ed3293f4d6e0a7d48ed2ac46ea46a9f
last-accepted-at: 2026-03-24T14:34:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: agents-navigate-by-deciding-what-to-read-next.md ===

Checks applied: 4

WARN:
- [Description discrimination] The description "An agent doing a task navigates by deciding what to read — links, index entries, search tools, and skill descriptions are all pointers with varying amounts of context for that decision" restates the title's core claim and then enumerates pointer types. The note's central mechanism — that context surrounding a pointer reduces the cost of the navigation decision, and that different pointer types carry different amounts of context — is only gestured at with "varying amounts of context." The cost argument (why context matters, what it saves) is the note's main contribution and is absent from the description. In a search result list alongside other navigation/links notes, this description would not clearly distinguish this note from a general "types of pointers" note.
  Recommendation: Lead with the mechanism: context around a pointer lets the agent judge relevance without loading the target, making navigation cheaper. The enumeration of pointer types is scope, not mechanism — it can follow if space permits.

CLEAN:
- [Title composability] "Since agents navigate by deciding what to read next, the knowledge system should make that decision cheap" reads naturally. The title works as a linkable prose fragment.
- [Claim strength] The title frames navigation as a decision problem about what to read, rather than about what to do or what plan to execute. This is a specific, non-obvious framing — someone could reasonably argue agents navigate by following instructions or executing plans rather than by making per-pointer read decisions. The claim carries information.
- [Title-body alignment] The title claims agents navigate by deciding what to read next. The body supports this framing directly, then extends it with a cost/context analysis and design implications. The extensions are natural consequences of the title's claim, not drift — the body delivers on the title's promise and builds from it.

Overall: 1 warning, 0 info
===
