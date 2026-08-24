# Second review: retained-mechanism proportionality, 2026-08-24

Operator concern, 2026-08-24: migration complexity is acceptable because it is
paid once, but **the retained mechanism must be slick, and `cp-skill-write` must
not absorb much complexity.** This review checks the plan against that
constraint. It supersedes nothing in the
[first review](./review-2026-08-24.md), whose four concerns were dispositioned
well.

**Finding: the claim model is proportionate; the mutation protocol is not, and
it leaks into the writing skill.**

## Measurements

| Artifact | Size |
|---|---|
| `cp-skill-write/SKILL.md` today | 117 lines |
| `mutation-and-dispatch-contract.md` | 430 lines, of which 105 are the guarded-replace package surface |
| Draft ADR | 476 lines |
| Grounding-worker instruction | 269 lines |

Permanent surface currently proposed beyond the claim model: a new
`commonplace-guarded-replace` CLI plus `lib/guarded_replace.py` (stage
reservation, section capture and splice, shared target locking, logical-path
candidate validation, atomic replacement, guarded rollback), a new
`markdown_sections.py` with `note_parser.py` changes, changes to validation
internals to accept candidate bytes at a logical path, a persistent
`.commonplace-locks/` runtime directory with a `.gitignore` entry, and
`cp-skill-ingest` reshaped into a transaction coordinator.

## Where the weight came from

Traceable to one decision. The
[readiness critique](./readiness-critique-2026-08-24.md) A1 correctly found that
hash-then-rename is not compare-and-swap, and offered three remedies:

1. serialize under a shared lock with a recheck while held;
2. a code-owned guarded-promotion helper; or
3. **weaken the ADR and acceptance boundary to a best-effort last-moment stale
   check.**

The plan took 1 and 2 together. Option 3 costs one sentence and no code.

The TOCTOU is real; the disagreement is about proportionality. Price the failure
it prevents: two mutations landing on the *same ingest file* inside the same
few-second window, in a KB whose ingests change on occasional re-ingest or
grounding. Frequency is near zero. The consequence is one lost claim entry —
**detectable** by the digest comparison the design already performs, and repaired
by re-running the grounding. That is a rare, cheap, self-announcing failure, and
it is being bought off with a permanent locking subsystem.

## The part that violates the operator constraint directly

A lock conflict returns `BLOCKED` for fresh retry, so **concurrency machinery
becomes a branch the writing skill has to handle.** Counting result paths the
writer must reason about: `SUPPORTED`, `NARROW` (with redispatch to a second
fresh worker), `CONTRADICTS`, `BLOCKED`, `BLOCKED: legacy recovery required`
(report a literal manual instruction and stop), and lock conflict. Six.

Alongside these, `cp-skill-write` also gains: splitting Step 6 into three stages,
`Task` in allowed-tools, holding the candidate as a transient string, a
link-authorization precheck, the three-condition trigger, a six-field handoff
packet, and a new judgment distinguishing "bounded candidate with a named
source" from "substantial grounding" that routes to multistage.

That is roughly ten new behaviors in a 117-line skill, several of them evaluated
on writes that never trigger grounding. The skill stops being a writing
procedure with a gate and becomes a protocol client.

## Recommendation

**Cut, in order of value:**

1. **Drop the lock, the `commonplace-guarded-replace` command, the lock
   directory, and the validation-internals change.** Take critique option 3:
   recheck the digest immediately before writing, best effort, and state the
   weakened guarantee plainly in the ADR. The critique already licensed this.
2. **Keep the one thing that actually prevents data loss**, which is not a
   concurrency mechanism: `cp-skill-ingest` passes the existing `Claims` block to
   the drafting worker as required content and verifies it round-trips
   byte-for-byte, failing if it does not. That defends the real hazard —
   re-ingestion silently erasing claims — with a content check.
3. **Collapse the writer's result handling to a binary.** `SUPPORTED` or
   `not supported, with a reason`. Let the author decide what to do with a
   reason; do not encode `NARROW` redispatch, legacy-recovery routing, and lock
   retry as protocol inside the skill. Redispatch in particular puts two
   sequential fresh-worker round-trips on the write path.
4. **Re-examine `markdown_sections.py`.** Most defensible of the four, since an
   offset-preserving scanner is generic infrastructure with other uses. But if
   the `Claims` grammar is fixed, splicing one section is a heading-boundary
   operation, and the general scanner may be answering a question V1 does not
   ask.

**Do not cut:** the required `## Claims` section, the two distinct verification
hops, the trigger boundary and its stated blind spot, the primary-source-only
scope, and the worked-case-first ordering. Those are the substance, and they are
right.

**Migration is fine.** The 285-file heading addition is paid once, is mechanical,
and is explicitly barred from semantic backfill. It is not where the weight is.

## The general shape of the error

Each addition here was individually justified by a real finding. The locking came
from a genuine TOCTOU; the staging came from wanting failed attempts to leave the
incumbent byte-identical; the redispatch came from wanting revised wording
rechecked. What is missing is a **standing budget** for the retained mechanism,
against which each addition has to argue. Without one, a sequence of locally
correct answers composes into a subsystem nobody would have proposed up front —
and the cost lands on the most-used skill in the repository.

Proposed budget, offered as a target rather than a rule: `cp-skill-write` gains a
trigger, a dispatch, and a binary gate; everything else lives in the worker or
the ingest skill. Any proposal that pushes a third concept into the writing skill
should have to say what it removes.
