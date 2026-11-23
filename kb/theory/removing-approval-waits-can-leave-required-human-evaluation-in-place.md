---
description: "Separates removing a human approval wait from automating or retiring a required evaluation task; optional assessment need not be part of either change"
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: []
---

# Removing approval waits can leave required human evaluation in place

Suppose an agent fixes broken links in a knowledge base. It used to show each proposed replacement to a maintainer and wait for approval. Now it publishes the fix as soon as it confirms that the new page loads. The maintainer still has a Friday job: read a sample of the linked pages and undo any fixes that point readers to the wrong article. Publishing is automatic. Checking whether the fixes point to the right articles is still the maintainer’s job.

Now change one detail. Nobody has asked for a Friday review or expects one. The maintainer sometimes reads the same pages out of curiosity about how well the agent works. If the maintainer takes Friday off, the agent publishes just as before in both cases. Only in the first case has someone missed a job.

## What happens if the maintainer does nothing?

Two questions distinguish an approval wait from a required review:

- **Does anything stop?** Under the old rule, a fix stayed unpublished until the maintainer responded. Even a non-binding recommendation creates a wait if the agent cannot proceed without receiving it. Conversely, a check written by a person can run without a fresh human judgment on each fix. [A record of routine approvals does not show that human judgment is dispensable](./routine-approvals-do-not-show-that-human-judgment-is-dispensable.md).
- **Would the process owner count anything as missed work?** That is the test for a required task, whether written down or not. A year of skipped Friday reviews does not by itself retire the duty. Nor does a year of voluntary reviews turn a habit into a duty. Whether the review prevents enough harm to be worth doing is a separate question.

## Name the part that is automated

“We automated publishing” need not say anything about Friday. “We automated link maintenance” must account for Friday too. Moving the human check until after publication removes a wait. If software now decides whether a replacement points to the right article and undoes bad fixes itself, it has taken over the maintainer’s check. Deciding that nobody needs to check the article retires the requirement; it does not automate the review. A team can combine these changes, for example by checking every URL automatically and asking a person to inspect a sample of the destinations.

## Scope

The distinction concerns required human work, not every human influence on the agent. An optional Friday review might inspire a better rule for choosing links. That does not make the review a prerequisite for publishing fixes. If the agent cannot adopt its *next rule* until a maintainer assesses it, that later decision has its own approval wait. [Comparing the system before and after a change](./a-better-factory-claim-compares-operative-states.md) asks whether it improved, not whether a person had to intervene for it to operate.
