---
name: cp-skill-library
description: Find and follow a Commonplace library procedure, instruction, or type by name. Use when the user names a Commonplace procedure or asks how Commonplace does something, and no more specific cp-skill applies.
type: types/instruction.md
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash
argument-hint: "[procedure, instruction, or type name or topic]"
---

# cp-skill-library

**Request: $ARGUMENTS**

**Intent.** Get the agent from a name or topic the user gives to the library file that governs it, and follow that file. The library indexes itself: every document in it carries a `description:` line, so searching those lines finds the right file without a separate list that could fall out of date.

This skill lives in the library's `instructions/` directory; the library root is its parent. Resolve the paths below from this file's real location.

- **A procedure or instruction:** search the `description:` lines of the Markdown files under `../` (the instructions directory, including skill directories) for the request's terms. Read the best match and follow it. If several fit, name them and ask which one the user means.
- **A type:** read `../../types/<name>.md`, or list `../../types/` when the name is uncertain.
- **Background or rationale:** start from `../../tags/README.md` or `../../reference/README.md`.

Links inside library files are relative to each file. If nothing matches, say so rather than guessing.
