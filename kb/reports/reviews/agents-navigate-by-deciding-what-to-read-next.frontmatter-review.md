<!-- REVIEW-METADATA
note-path: kb/notes/agents-navigate-by-deciding-what-to-read-next.md
last-full-review-note-sha: 33d215b103b904f2ed806817a72e53ead08514fc
last-full-review-note-commit: 0d4ee7df7ed3293f4d6e0a7d48ed2ac46ea46a9f
last-full-review-at: 2026-03-24T22:33:37+01:00
last-accepted-note-sha: 8565eacd5bd7bb2f52a5213451e198e65ee89adc
last-accepted-note-commit: 09d91abac8ab71a82447d352a0fe42f760f1a853
last-accepted-at: 2026-03-24T22:54:57+01:00
last-acceptance-kind: trivial-change-ack
review-type: frontmatter-review
-->
=== FRONTMATTER REVIEW: agents-navigate-by-deciding-what-to-read-next.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism ("context surrounding a pointer ... determines how cheaply an agent can judge relevance without loading the target") and scope ("inline links carry most context, search results carry least") beyond the title's general claim. An agent searching for "pointer context" or "navigation cost" would immediately distinguish this note from others about agent navigation. The prior review's WARN about description restating the title has been addressed — the description now leads with the cost mechanism and names the pointer-type spectrum.
- [Title composability] "since agents navigate by deciding what to read next, we designed..." reads naturally as a sentence fragment. Works as inline link text.
- [Claim strength] The claim that navigation reduces to a per-pointer read/skip decision is a specific framing, not the only one — someone could argue agents navigate via structured plans, exhaustive scanning, or orchestrator routing. The claim is contestable and carries information.
- [Title-body alignment] The body opens by establishing the per-pointer decision framing, then develops what makes that decision tractable (context richness of different pointer types) and closes with design implications. The title captures the framing; the body delivers on it. The note's deeper contribution (the context-cost analysis) lives in the description, which is the intended division of labor between title and description in this KB.

Overall: CLEAN
===
