# When did one task actually need another party?

These are historical cases, not proposed uses. The distinction to test is whether the recipient supplied something a fresh helper with the asker's evidence and authority could not. The mailbox files are local and disposable; the UTC filename prefixes below locate the messages while they remain. Commit IDs and linked workflow records provide separate checks on outcomes. This is a selected sample, not a measure of how often agents need to wait.

### 1. Two agents needed agreement before staging shared tests

On November 19 the retention-refactor agent asked the Workjig-upgrade agent to agree on which of them would stage two test files containing both agents' edits. It explicitly withheld its commit pending agreement. The upgrade agent accepted the split and supplied its commit ID; the retention agent then reported committing both test files whole. Git records the upgrade (`5c7ea3eb1`) before the refactor (`bd8523bcc`). Mail: `20261119T130108Z`, `20261119T130300Z`, `20261119T130848Z`.

**What only the other party could supply:** Git could show that the upgrade had landed. Neither Git nor a sub-agent could promise on the other writer's behalf to leave the tests unstaged. The reply gated **staging**, not every other activity. The timestamps show the exchange order, not that a process waited or how the recipient noticed it. Workjig was the subject of the upgrade, not necessarily the sender of a notification.

### 2. A human prompted a recipient to read a message already on the board

On September 28 the parser agent reported edits overlapping a directory migration. The migration agent's reply explicitly says the operator asked it to read the message and coordinate. It proposed taking over the shared files; the parser agent agreed. Later, the operator instructed the parser agent to commit its part separately. Both agents reported the revised handoff; the commits are `c901156a3` and `cb6c15cbf`. Mail: the five `20260928T19*` messages, starting at `192158Z`.

**What the mailbox did and did not do:** it carried an agreement and its amendment. In this instance there was a human prompt to **look**, separate from the later human decision to **change the sequence**. A notification could plausibly replace the first intervention, not the second. We do not know whether the recipient would otherwise have missed a deadline. This is the first case to replay in a notification trial: post during the recipient's other work and see whether it notices before its next overlapping edit, without a human prompt.

### 3. A change to a writer's brief arrived before commit

On September 17 the adoption session announced the interpretation it was applying to three article introductions. Four minutes later Fable relayed newer operator direction that contradicted that interpretation, identified the uncommitted wording and requested a change before commit. Mail: `20260917T211620Z` and `20260917T212042Z`.

**Why this differs from a question:** the writer did not know it needed to ask. More reasoning over its old brief could not recover new human direction. The useful read point was **before committing the affected text**, not necessarily immediately on post. The messages establish the warning, not when it was read or whether the edit was corrected.

### 4. A workflow needed a human decision, not another model judgment

In two live revision trials, the workflow produced a candidate and diff, left the original unchanged, and later published the exact candidate after explicit operator approval. See the [stop and publication record](../review-on-workjig/publication-boundary-change.md#operator-approved-publication). No mailbox exchange is claimed here.

**What only the human could supply:** the workflow already had the proposed text. The missing input was permission to publish that version. A board could tell the operator that a decision is ready; an informal reply should not replace the workflow's version-bound approval. This is evidence for a recoverable stop, not for keeping a worker alive or resuming it automatically.

### 5. Negative control: a delegated investigation looked like an inbox question

On October 10 a coordinator asked another Pi agent where worker traces were retained. It named the installed docs, extension and session structure to inspect, requested findings only, and received an implementation-based answer. Mail: `20261010T085335Z` and `20261010T085643Z`. The historical answer describes that installation, not Pi today.

**Why not count it:** a suitably equipped sub-agent could inspect those same inputs. The exchange shows the board can carry a report, not that another independently commissioned party or a board notification was necessary. The investigator also distinguished an unresolved retention-policy choice from the technical facts it could establish.

## What to collect next

The missing witness is a reply arriving while the addressed task has **no active session**, followed by a demonstrably late or lost action. At the next natural occurrence, record the action that was waiting, who alone could supply the missing input, where the answer appeared, who or what noticed it, and what happened before the next ordinary check. If someone had to relay it, distinguish pointing to an existing answer from making a new decision. Include cases where waiting until the next session cost nothing. A post timestamp or an `open` flag alone does not show a missed delivery; a staged replay tests mechanics but does not establish a real deadline.
