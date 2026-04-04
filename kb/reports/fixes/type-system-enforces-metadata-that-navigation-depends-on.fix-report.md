## Fix Report: type-system-enforces-metadata-that-navigation-depends-on

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Completeness boundary cases | boundary-case-acknowledged | Broadened "crosses from text to note" to include directly-created notes | fixed |
| 2 | Completeness boundary cases | boundary-case-acknowledged | Distinguished deterministic (present/non-empty) from judgment-level (discriminating) enforcement | fixed |
| 3 | Completeness boundary cases | — | Title says "metadata" but body only covers description; review notes this is warranted by the base type's requirements | deferred |
| 4 | Internal consistency | — | No issues found | n/a |

### Warning-to-fix mapping

- **#1 (Enforcement scope):** "The text-to-note crossing framing understates the enforcement scope — notes created directly are also enforced, but this path isn't mentioned."
- **#2 (Enforcement levels):** "'Discriminating' enforcement is qualitatively different from 'present/non-empty' enforcement (LLM rubric vs. deterministic check), but the note treats them as a single mechanism."
- **#3 (Metadata breadth):** "Title says 'metadata' (general) while body only covers `description`; the linked navigation note argues `type` is also used for routing, but `type` has a default rather than being strictly required."

### Deferred items

- **#3 (Metadata breadth):** The review itself notes the body's focus on description "is warranted by the note base type's requirements." Expanding to cover `type` would broaden the argument's scope; narrowing the title would weaken the claim. Neither is a framing fix — human judgment needed on whether to expand or leave as-is.

### New patterns

- (none)
