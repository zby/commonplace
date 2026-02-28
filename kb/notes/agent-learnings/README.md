# Agent Learnings

Staging area for insights discovered by AI agents during work sessions.

## Purpose

Agents write notes here when they notice:
- Friction or gotchas worth documenting
- Patterns that should become conventions
- Corrections received that reveal missing guidance
- Tool-specific behaviors worth codifying

## When to Write

- **Do** jot down insights as you notice them
- **Don't** interrupt the current task to write extensive notes
- **Don't** need permission to create or update files here

## Template

```markdown
# Brief descriptive title

## Context
What situation triggered this learning.

## Learning
The insight, rule, or pattern discovered.

## Suggested Destination
Where this should be promoted (AGENTS.md, a specific README, architecture.md, etc.)
```

## Workflow

1. Agent creates note during work session
2. Human periodically reviews accumulated learnings
3. Good learnings get promoted to their destination:
   - `AGENTS.md` — general agent behavior
   - Tool READMEs — tool-specific guidance
   - `docs/architecture.md` — design insights
4. Note is archived or deleted after promotion

## Guidelines

- Keep notes brief and actionable
- One learning per note (easier to review/promote individually)
- Include concrete examples when helpful
- Don't duplicate what's already documented elsewhere
