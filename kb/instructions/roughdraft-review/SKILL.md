---
name: roughdraft-review
description: Open a Markdown file in Roughdraft for the user to review, wait for Done Reviewing, then respond to the CriticMarkup feedback. Use when the user wants to review, comment on, or annotate a Markdown file (they may call the tool "rd"), and when presenting a plan — write the plan to disk and offer it for review this way.
type: kb/types/instruction.md
user-invocable: true
---

# Roughdraft review

Roughdraft is a single-file Markdown viewer/editor for inline review. The user may refer to it as `rd` in natural language; treat `rd` as shorthand, but do not create or modify any shell alias, executable, symlink, or command named `rd`.

When the user asks for a plan, write the plan as a Markdown file on disk before asking them to review it.

## Opening a file for review

```bash
roughdraft open "/absolute/path/to/file.md"
```

Open one `.md` file at a time. If Roughdraft is not running, `roughdraft open` starts it automatically.

**Leave the command running.** Do not interrupt, kill, background, detach, or treat the waiting process as cleanup. The wait is intentional: Roughdraft exits the command after the user clicks Done Reviewing, and that exit is the signal to resume — read the file from disk and respond to any CriticMarkup comments or suggested changes.

## CriticMarkup (Roughdraft-flavored)

Base markers:

- Comment: `{>>comment<<}`
- Insertion: `{++new text++}`
- Deletion: `{--old text--}`
- Substitution: `{~~old~>new~~}`
- Highlight: `{==text==}`

Each marker may be followed by an attribute block: `id` (stable document-local id), `by` (author), `at` (ISO timestamp), `re` (parent comment/suggestion id in a reply thread).

When adding a new comment or suggested change: generate a stable id (`c1`, `c2`, … for comments; `s1`, `s2`, … for suggestions), set `by` to your agent label, set `at` to the current ISO timestamp, and set `re` when replying.

Preserve existing attribute blocks unless intentionally removing the associated comment or suggestion.

Typical shapes:

- Anchored comment: `{==selected text==}{>>Comment text<<}{id="c1" by="AI" at="2026-04-28T12:00:00.000Z"}`
- Suggested change: `{++new text++}{id="s1" by="AI" at="2026-04-28T12:10:00.000Z"}` or `{~~old~>new~~}{id="s2" by="AI" at="2026-04-28T12:11:00.000Z"}`
- Reply: `{>>Reply text<<}{id="c2" by="AI" at="2026-04-28T12:05:00.000Z" re="c1"}`

For local command and syntax details: `roughdraft help` and `roughdraft help criticmarkup`.
