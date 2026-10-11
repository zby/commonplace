# Open questions

Each question records its current answer in the live method, where one exists,
and what evidence would discriminate between options. Current answers come
from [current arrangement](./current-arrangement.md). No question here is
decided by being listed.

## How much of the general layer does the runtime role already provide?

Current answer: by instruction, all of it. The runtime role is scoped to
consequential work, routes, guarantees and admission mechanisms, and is told it
is not a product inventory.

Discriminating evidence: a coverage audit against the frozen worktree that
lists material components and entry paths absent from Components and Routes,
and whether the record declared them as untraced. See
[evidence base](./evidence-base.md).

## Is memory too broad for one focused investigation?

Candidate splits discussed: retention and representation; retrieval and
contextual use; maintenance and withdrawal. No split, names or worker count has
been adopted.

Current answer: one role, told to cover every included part along the record
contract's coverage dimensions.

Discriminating evidence: memory worker traces showing context pressure or
truncated coverage, and audit findings that a coverage dimension was skipped
rather than bounded. Three narrower workers triple discovery cost and add
reconciliation; the split must show omissions the single worker could not have
closed with a sharper stopping rule.

## Where do feedback and adaptation belong relative to the epistemic role?

Current answer: the epistemic instruction (`trace-epistemic.md`) owns them by
default. Not yet examined in this workshop.

## Should lenses receive the general map, and when?

Current answer: yes, as an order-only input. Lenses are handed the runtime
record and wait for it; a runtime change does not re-run them.

Open parts: whether the map anchors discovery toward runtime's paths, and
whether a runtime correction that changes located paths should trigger lens
reruns. Discriminating evidence: the share of lens anchors that fall outside
runtime-located paths across retained runs. A share near zero is consistent
with either good runtime coverage or anchoring; a coverage audit separates
those.

## Which lenses should be fixed across systems?

Comparison needs fixed lenses with comparable fields; the memory profile is
one. Other questions may need proportionate treatment or optional depth. Not
yet examined.

## What is a sufficient answer and a defensible stopping point for each lens?

Current answer: runtime has a stopping rule for guarantee paths (two to four
forcing cases, state what remains unobserved); memory has a coverage-dimensions
rule; epistemic and the verifier have none stated.

The missing piece is a form for the stopping statement itself: what was
searched, by what method, what was found, and what remains unobserved, placed
beside the claims it limits rather than in a general disclaimer.

## What should a verifier check without becoming a second exhaustive analysis?

Current answer: judge coverage against the frozen repository tree, for every
record, with a materiality threshold but no stopping rule.

Proposed answer under examination:
[verification coverage bounds](./proposals/verification-coverage-bounds.md).

## Can the existing reports and comparison profile express the result unchanged?

Current answer: the runtime record's anchored shared records already name
located paths; the verification record already carries declared limits. No
contract gap has been shown. A gap counts only when a named consumer cannot
read something it needs.
