---
description: "Use in a fresh sub-agent after implementation to independently review uncommitted changes, one commit, or a commit range."
type: types/instruction.md
---

# Review code

Independently find issues in the changes before they are accepted.

When a plan delegates review, load this prompt in a fresh sub-agent with the repository path and review target. Review the supplied commit (`<commit>^..<commit>`) or range (`<base>..<tip>`); otherwise review all uncommitted changes, including staged and untracked files.

Inspect the changes and relevant surrounding code and tests. Look for bugs, inconsistencies, regressions, missing tests, and overengineering. Do not modify files or delegate further.

Return actionable findings, most important first, with file/line references, impact, and suggested fixes. Avoid speculative issues and style-only preferences. If none, say so. State what you could not verify.
