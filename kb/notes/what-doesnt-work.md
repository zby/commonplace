---
description: Anti-patterns and areas with insufficient evidence — auto-commits, queue overhead, validation ceremony, session rhythm
type: review
areas: [claw-design]
status: current
---

# What doesn't work

## Auto-commits

Hook-driven automatic commits after every note operation created a mess. Commits were noisy, hard to review, and we spent significant effort removing them. Agents should not commit without explicit human approval.

Together with [what works](./what-works.md), this is the manual observation log that a [KB learning loop](./automating-kb-learning-is-an-open-problem.md) would eventually feed from — these anti-patterns are ground truth for what mutations the loop should avoid proposing.

## Observations needing more evidence

The following areas showed friction, but we haven't tested them enough to draw conclusions.

- **26 skills/commands** — 16 local + 10 plugin. Most rarely used, but unclear which are valuable until we use the system more.
- **Queue and pipeline machinery** — adds significant complexity. Noticeable overhead for a single-contributor project, but may pay off differently at scale.
- **Schema validation as a separate ceremony** — a dedicated FAIL/WARN/PASS phase adds machinery. The frontmatter fields themselves are useful; the question is whether formal validation justifies its cost.
- **Session rhythm protocol** — orient → work → persist adds ceremony. Unclear whether it changes behavior beyond what good context already provides.
- **Connection requirements outpace connection-making** — orphan rate reached ~90%. The gap between connection rules and actual connections was noticeable, but the rules themselves may not be the problem.

Topics:
- [claw-design](./claw-design.md)
