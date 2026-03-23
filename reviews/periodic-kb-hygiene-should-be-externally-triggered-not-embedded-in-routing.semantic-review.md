=== SEMANTIC REVIEW: periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md ===

Claims identified: 7

1. Routing instructions should optimize for high-frequency decisions: "where content goes, which type to use, and which docs to open next" (paragraph 1) -- scope claim / enumeration of 3 routing concerns
2. Periodic hygiene checks are "typically triggered by something external: a user request, a heartbeat job, or CI" (paragraph 1) -- enumeration of 3 external trigger types
3. "Placing periodic operations inside always-loaded routing instructions adds instruction noise on every session while helping only occasionally" (paragraph 2) -- causal claim
4. Two responsibilities are blurred: "Routing: 'what to do now for this task' / Operations: 'what to audit from time to time'" (paragraph 2) -- enumeration / dichotomy
5. "The separation keeps the default path lightweight without losing the maintenance playbook" (paragraph 3) -- causal claim about the benefit of separation
6. "The playbook itself lives in [maintenance-operations-catalogue...]" (paragraph 3) -- factual claim about location
7. The maintenance-operations-catalogue is "the staging ground for operations before promotion into kb/instructions/" (paragraph 3) -- characterization of the catalogue's role

WARN:
- [Completeness] The note enumerates exactly three high-frequency routing decisions: "where content goes, which type to use, and which docs to open next." The actual CLAUDE.md routing table also handles escalation boundaries (when to stop and load deeper guidance), search patterns (how to find existing content), and vocabulary definitions (term disambiguation). These are all loaded every session and are plausibly high-frequency. The enumeration presents itself as definitive ("should optimize for") but covers roughly half of what actually lives in the always-loaded routing surface. A reader could conclude that anything not in the list is a candidate for extraction.

INFO:
- [Completeness] The note enumerates three external trigger types: "a user request, a heartbeat job, or CI." A boundary case is a trigger embedded in the note graph itself -- e.g., a link-contract violation detected during normal traversal that reveals stale content. This is neither a user request nor a scheduler nor CI; it is an organic discovery during routine work. The maintenance-operations-catalogue note actually includes "after major edits" and "pre-release hygiene pass" as triggers for neighborhood tension review, which don't map cleanly to any of the three listed trigger types. The enumeration uses "typically" which softens the claim, so this is INFO rather than WARN.
- [Completeness] The routing/operations dichotomy ("what to do now for this task" vs. "what to audit from time to time") is clean but leaves a gap for one-time setup operations that are neither routing nor periodic audit -- e.g., "bootstrap this KB from scratch" or "onboard a new contributor." These are operational but not periodic. The dichotomy works for the note's stated scope (periodic hygiene) but could mislead if read as a complete taxonomy of non-routing concerns.
- [Grounding alignment] The note says the maintenance-operations-catalogue is "the staging ground for operations before promotion into kb/instructions/." The linked note confirms this characterization: "Once an operation is stable enough, it should be distilled into kb/instructions/ as an execution-oriented procedure." The attribution is accurate but omits a nuance: the catalogue note describes a four-step distillation pipeline (capture, re-run, mark ready, distill), not a simple binary staging/promotion. A reader of only this note might infer promotion is a one-step move rather than a maturation process.

PASS:
- [Grounding alignment] The link to instruction-specificity-should-match-loading-frequency is described as "extends this by applying always-loaded vs on-demand loading to maintenance operations." The linked note does establish the principle that "match instruction specificity to loading frequency" and explicitly says "CLAUDE.md should NOT contain detailed instructions for specific tasks." The current note is a specific application of that principle to maintenance operations. The relationship semantics ("extends") are accurate.
- [Grounding alignment] The link to instructions-are-skills-without-automatic-routing is described as defining "the target artifact for procedures that mature beyond note-level catalogues." The linked note confirms this: instructions are "reusable procedures distilled from repeated manual operations" living in kb/instructions/. The characterization is faithful.
- [Grounding alignment] The link to maintenance-operations-catalogue is described as operationalizing the current note "by collecting periodic checks and their distillation status." The linked catalogue note does exactly this -- it contains concrete operations (orphan detection, raw text capture detection, neighborhood tension review) with distillation status markers. The attribution is accurate.
- [Internal consistency] The note's two-responsibility distinction (routing vs. operations) is used consistently throughout. The title claim, body argument, and linked-notes section all align on the same position: periodic hygiene is operations, not routing, and belongs in externally triggered mechanisms. No definition drift or contradictions detected.
- [Internal consistency] The note does not have a compressed summary section, so there is no summary-body faithfulness risk. The title serves as the summary and accurately captures the body's argument.

Overall: 1 warning, 3 info
===
