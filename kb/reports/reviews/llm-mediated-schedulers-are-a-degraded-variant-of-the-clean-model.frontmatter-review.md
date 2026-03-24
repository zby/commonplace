<!-- REVIEW-METADATA
note-path: kb/notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md
last-full-review-note-sha: e7013840d48cd5f12543ade80e849b575cc93768
last-full-review-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-full-review-at: 2026-03-24T20:55:52+01:00
last-accepted-note-sha: e7013840d48cd5f12543ade80e849b575cc93768
last-accepted-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-accepted-at: 2026-03-24T20:55:52+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism ("the agent scheduler lives inside an LLM conversation it becomes bounded") and enumerates the three recovery strategies by name with their ordering. This goes well beyond the title, which only names the degradation diagnosis. An agent seeing this description in a search results list would immediately know both the causal story and the prescriptive structure of the note.
- [Title composability] "since LLM-mediated schedulers are a degraded variant of the clean model, we designed recovery strategies..." reads naturally as a linked prose fragment.
- [Claim strength] The claim that LLM-mediated scheduling is specifically a *degraded variant* rather than a different-but-valid paradigm is contestable — someone could argue that conversational scheduling has emergent strengths (flexible replanning, natural-language reasoning about priorities) that make it a distinct model, not merely a worse one. The claim takes a specific architectural position.

INFO:
- [Title-body alignment] The title captures the diagnostic half of the note ("degraded variant") but the body gives roughly equal weight to three recovery strategies (compaction, externalisation, factoring into code) that the title is silent on. The description compensates well — it names all three strategies — so retrieval is not harmed. If the note grows, consider whether the title should signal the prescriptive content too, e.g. "LLM-mediated schedulers degrade the clean model — three strategies recover the separation."

Overall: 0 warnings, 1 info
===
