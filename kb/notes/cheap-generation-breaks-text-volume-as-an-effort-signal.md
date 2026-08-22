---
description: "When text is cheap to expand but costly to verify, length stops evidencing author effort and can instead warn that the reviewer inherits unperformed checking"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [context-engineering, llm-reliability]
---

# Cheap generation breaks text volume as an effort signal

Where producing a long, coherent text artifact is costly, volume can serve as an imperfect signal that the author invested effort. Cheap generation breaks that inference wherever it lowers production cost without lowering verification cost. A large artifact can then require more reviewer effort than its author spent judging it. The mechanism applies to natural-language writing and symbolic source code alike: text names the inspected surface, not one [representational form](./definitions/representational-form.md).

That asymmetry makes apparently unreviewed expansion a rational triage signal. It does not show that the text is false, incorrect, or machine-generated. It lowers the expected return from inspection when volume rises without independent evidence of author judgment. [Reverse compression](./reverse-compression-is-when-llm-output-expands-without-adding.md) is the content-side failure; this is its signal-side consequence before the reviewer has established what the text contains or does.

Author effort is not the objective. It matters only as a proxy for judgment. Tests, evidence, a compact stated contribution, trusted authorship, or visible review can supply better signals. Surface style remains noisy, so this mechanism does not license AI detection or automatic dismissal of large text artifacts.

---

Relevant Notes:

- [AI;DR Hacker News discussion](https://news.ycombinator.com/item?id=49336573) — evidenced-by: self-selected participants repeatedly describe using apparent generation effort and reviewer-side verification cost to decide whether text is worth inspecting; the thread establishes the signal's use, not its accuracy or prevalence
