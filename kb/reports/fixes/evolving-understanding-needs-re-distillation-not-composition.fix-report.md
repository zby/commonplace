## Fix Report: evolving-understanding-needs-re-distillation-not-composition

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | sentence/clause-packing | sentence-split | Split six-concept sentence at line 13 into two at the colon boundary | fixed |
| 2 | sentence/clause-packing | sentence-split | Split four-property sentence at line 40, moving update-trigger to its own sentence | fixed |
| 3 | sentence/misleading-link-text | filename-link-text | Replaced three raw-filename link texts with human-readable note titles in Relevant Notes | fixed |
| 4 | sentence/misleading-link-text | (none) | INFO-level finding about "extracted into durable notes" link text | deferred |

### Warning-to-fix mapping

- **#1 (clause-packing, line 13):** "Six conceptual items... The sentence tries to do two jobs at once -- describe the reconciliation process AND introduce the two-dimension framework." Split at the colon: "...competes for context budget. The cost falls on two dimensions:..."

- **#2 (clause-packing, line 40):** "Four contrastive properties trail after the colon, each with its own qualifier... The reader must hold the attribution, the implementation claim, and all four properties simultaneously." Moved the update-trigger property to a new sentence: "It updates when understanding shifts, not when code changes."

- **#3 (misleading-link-text, lines 58-60):** "Three links use raw filenames as link text instead of human-readable titles... jarring alongside the other Relevant Notes entries that use readable titles." Replaced filename-style text with actual note titles: "A functioning knowledge base needs a workshop layer, not just a library", "Short composable notes maximize combinatorial discovery", "Storing LLM outputs is constraining".

### Deferred items

- **#4 (misleading-link-text, line 36):** INFO-level finding. The review itself notes the link is "Not misleading in content" -- the text "extracted into durable notes" accurately describes the action discussed. The target note does contain the relevant section on extraction bridges. The narrowing of expectations is minor and does not warrant changing the prose flow of the paragraph.

### New patterns

- **sentence-split:** A packed sentence combines multiple independent conceptual jobs (e.g., describing a process AND introducing a framework for analyzing it). Fix by splitting at the natural boundary (typically a colon or semicolon) so each sentence handles one job. The split preserves all content and the original argument flow.
- **filename-link-text:** Link text in a Relevant Notes section uses raw hyphenated filenames instead of human-readable note titles. Fix by replacing filename text with the actual `# Title` from the target note, matching the formatting convention used by other entries in the same list.
