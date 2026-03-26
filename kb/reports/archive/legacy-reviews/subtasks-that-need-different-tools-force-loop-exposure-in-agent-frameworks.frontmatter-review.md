<!-- REVIEW-METADATA
note-path: kb/notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md
last-full-review-note-sha: 1e4a9e28c149fa74c6ab4c98473ddd1bcc71177b
last-full-review-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-full-review-at: 2026-03-24T20:57:04+01:00
last-accepted-note-sha: 1e4a9e28c149fa74c6ab4c98473ddd1bcc71177b
last-accepted-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-accepted-at: 2026-03-24T20:57:04+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] Description adds mechanism ("the parent must construct fresh calls for each child") and implication ("a framework-owned loop is no longer the right control surface") beyond what the title carries. The title names the forcing function; the description explains the causal chain. Strong discriminator in a search result list.

CLEAN:
- [Title composability] "since subtasks that need different tools force loop exposure in agent frameworks, we designed..." reads naturally as a sentence fragment. Works as a linkable clause.

CLEAN:
- [Claim strength] The claim is specific and contestable: someone could reasonably argue that a single large static tool set, meta-tools, or dynamic tool registration suffice without exposing the loop. The note itself engages these counterarguments (giant static tool set, meta-tool as hidden scheduler, escape to direct API calls). Not a truism.

INFO:
- [Title-body alignment] The body fully supports the title's claim but extends beyond its scope. Paragraphs 5-6 develop a substantial argument about tool *removal* asymmetry — "You cannot cleanly shrink a context's action alphabet — you can only start a fresh context where it was never larger" — which is a distinct insight from the subtask-dispatch framing the title promises. The final paragraph synthesizes both threads ("Sub-task dispatch is not the only case"), which is honest, but the title scopes only to the subtask case. The extension is well-integrated and the core claim is solid, so this is mild scope drift rather than misalignment.
  Recommendation: Consider whether the removal-asymmetry argument deserves its own note (it's a standalone insight about context alphabet shrinkage), or widen the title to cover the general case, e.g. "changing the tool surface mid-task forces loop exposure in agent frameworks."

Overall: 0 warnings, 1 info
===
