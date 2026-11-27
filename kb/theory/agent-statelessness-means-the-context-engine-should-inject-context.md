---
description: "A release checklist and a spelling correction illustrate when supplying a referenced rule saves a consequential lookup and when a link is enough."
type: theory/types/structured-claim.md
traits: [title-as-claim]
tags: [context-engineering, architecture]
---

# Whether to supply a reference up front depends on the task

A system can show an agent a rule alongside its task or give it a link to follow. Supplying the rule up front helps when missing it would change the decision and the agent might not know to look. A link is preferable when the rule is unlikely to matter or is already in view.

## Evidence

Consider two tasks involving the same release checklist and the same linked policy:

- **Decide whether to release a build.** Suppose the checklist says “confirm independent approval,” and the policy says the approver must not have authored the change. An author’s sign-off is on file. Showing the one-sentence rule beside the checklist tells the agent why that sign-off is insufficient; the link alone leaves it to notice that “independent” has a specific meaning.
- **Correct a spelling error in the checklist.** The approver rule cannot change the spelling decision. Showing it because the editor opened the same file adds text without helping with the task. Leave the link available in case the scope changes.

## Reasoning

The link identifies *which* policy is relevant to approval, not *whether* the current task involves approval. A [selection rule needs a signal that distinguishes the cases](./rule-based-context-selection-needs-a-pre-existing-signal.md): starting a release review supplies one; merely opening the checklist does not. Nor does [starting a fresh session](./agent-statelessness-makes-routing-architectural-not-learned.md) settle the choice. A fresh agent can follow a link, and a rule read earlier in the same task may still be visible.

To test a proposed trigger, compare showing the rule with offering the same link alone. Include tasks where the rule changes the answer and tasks where it does not. Check whether the agent makes the right decision, how many lookups it needs, and how much irrelevant text it receives. Fewer lookups alone is not success if every reader gets a policy they do not need.
