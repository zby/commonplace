---
description: "Finding the same document twice can be explained by a fixed index. Learning from the first lookup requires something to record the experience and something to use it."
type: types/note.md
traits: [has-comparison, title-as-claim]
tags: [architecture, context-engineering]
---

# A stateless agent can find the answer again but cannot benefit from having found it before

Suppose an agent finds the release checklist on Monday and again on Tuesday. A fixed search index can explain both successes. Even if a shortcut is missing on Tuesday, the agent can search by subject. **Stateless across tasks** means that nothing the agent did on Monday affects how it handles Tuesday’s task. It does not mean the agent forgets what it just read while working on the same task.

Now suppose Monday’s successful lookup is *why* the checklist ranks higher on Tuesday. The stateless model no longer explains the result. A search service might record which checklist worked and use that record to rank it higher for later release tasks. The system then benefits from experience even if each task starts with a fresh model call and the model weights never change. A log that search never consults would not explain the improvement.

The design question is whether the agent needs to **succeed from a cold start** or **get better with experience**. For the first, test whether it can find the current checklist from the task description alone. For the second, identify what records the outcome and what uses it on the next task. A system can do both.
