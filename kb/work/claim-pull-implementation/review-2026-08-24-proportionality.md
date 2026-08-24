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

---

## Addendum: the write skill does not use ingests at all

Operator observation, 2026-08-24, and it is sharper than the proportionality
argument above. Checked against the current skill:

`cp-skill-write/SKILL.md` mentions an ingest **once**, at line 68, and only
passively — "Notes, sources, and ingests pulled into the session for this write
are first-class link candidates. If it was worth reading, it is worth considering
as a link." It never opens an ingest as authority, never mutates one, and its
`allowed-tools` are `Read, Write, Grep, Glob, Bash, Skill`. No `Task`.

So the plan does not extend what this skill does. **It changes its kind** — from
a skill that drafts and saves prose into one that dispatches a worker which
mutates a second collection's artifact under a lock, and then interprets that
mutation's transaction outcomes. That is why the complexity feels
disproportionate: it is not being added to a skill that was already doing
something adjacent.

### The design drifted from the operator's own statement

The originating instruction was: read the source, extract the claim, add it to
the ingest if missing, "**only after these preparations** it should use the claim
in the target note."

Preparations *before* the write. The implementation turned a **sequencing
discipline** into an **inline subroutine** of the write skill. Those have
different costs: the first is an author-visible ordering rule, the second is
permanent machinery on the most-used path in the repository.

### What follows

Grounding is a **precondition** of writing, not a step of it. The write skill's
whole job becomes: notice that the candidate leans on a named source, check
whether that source's ingest already carries the claim, and if not, **stop and
say so**, naming the route. It never dispatches, never mutates, never sees a
transaction.

Mutation stays entirely in `cp-skill-ingest`, which already owns ingest mutation
and is the natural home for it.

This deletes, rather than shrinks:

- `Task` in the write skill's allowed tools;
- the fresh-worker dispatch and its six-field packet;
- the `NARROW` redispatch loop and its second sequential round-trip;
- the lock-conflict branch;
- the `BLOCKED: legacy recovery required` routing;
- every transaction concept reachable from the write path.

The write skill's remaining delta is one check and one refusal message. That fits
the budget proposed above with room to spare, and it does not require settling
the mutation-protocol question first — with `cp-skill-ingest` the only mutator,
invoked one at a time, the concurrency pressure that motivated the locking
subsystem largely evaporates.

**The cost, stated honestly.** An author who has not pre-grounded pays a round
trip: write, refused, ground, write again. That is real friction, and it is the
friction the operator's original sequencing already implied. It is also
recoverable in a way permanent machinery is not — if the round trip proves
annoying in practice, the dispatch can be added later against evidence, which is
the reverse of the current order.

---

## Addendum 2: which part is optimistic locking, and which window actually matters

Operator question, 2026-08-24: does the write-time refusal fire when the ingest
was rewritten in the meantime — is it optimistic locking?

**No, and the distinction matters.** The two sides of the design are different
mechanisms and only one of them is concurrency control.

**The write-side refusal is a precondition check, not a lock.** It fires on
"this ingest does not carry the claim," which is the *common* case — nobody has
grounded it yet — not a race. It compares content against a requirement, not a
version against a version. Closer to "the file does not exist" than to "the
version changed under me."

**The ingest-mutation side is optimistic locking.** Capture the preimage digest,
stage the change, recheck the digest, promote. That is textbook optimistic
concurrency control, and the
[readiness critique](./readiness-critique-2026-08-24.md) A1 correctly found the
verify-and-commit is not atomic — so it is *broken* OCC, not something other than
OCC. The plan's remedy was to add pessimistic locking underneath it. The cheaper
remedy is to keep the OCC and accept it as best effort, which is the critique's
own option 3.

### The window that is being protected is not the window that matters

Both mechanisms address a gap measured in milliseconds. But there is a longer
gap neither touches:

> `cp-skill-write` reads the ingest, sees the claim, saves the note. A week
> later a re-ingest or a revised grounding changes that claim. The note now
> cites something the ingest no longer says.

A lock closes a sub-second window while leaving a months-long one wide open. The
consequence is identical either way — the note's citation needs rechecking — so
the lock is not buying correctness against the failure that will actually occur.
**This is a staleness problem wearing a concurrency problem's clothes.**

### Commonplace already has the right shape for it, and it is nearly free

[Factored dependency pairs for review freshness](../../reference/proposals/factored-dependency-pairs-for-review-freshness.md)
holds exactly this case. Its `source-as-gate` remainder is "a derived note's
consistency with the source snapshot from which it was worked out … one pair per
`(note, source)` edge, so each source invalidates independently with its own
diff." Its stated adoption criterion is "when a note's consistency with its
source is first wanted as a reviewable judgment" — which is precisely what this
workshop is building. The proposal records the cost as "a gate source plus a
wrapper, **no storage change**," and the factoring pattern is already proven
twice, with `COLLECTION.md`-as-gate shipped in
[ADR 041](../../reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md).

So the durable note-to-ingest relationship has an existing, cheap, twice-proven
mechanism waiting for a trigger, and this work is that trigger.

### Revised recommendation

Do not build locking. Instead:

1. keep best-effort OCC on ingest mutation — digest recheck immediately before
   write, failure means re-run;
2. keep the write-side precondition check as a content check;
3. carry the durable relationship with a factored `(note, ingest)` freshness
   pair rather than a write-time guarantee.

That is strictly cheaper than the current plan **and** it covers the failure the
locking subsystem does not reach. Adopting source-as-gate is also a decision this
workshop can hand to an existing proposal rather than invent, which is the
difference between one ADR and a subsystem.

---

## Addendum 3: what the write-side refusal actually does

Operator question, 2026-08-24: how does the refusal happen?

### The mechanism fits an idiom the skill already has

Step 5 is already "a cheap duplicate guard" — a targeted `rg` with an explicit
prohibition on enumerating the collection. The source check is the same shape,
added as one more bounded guard, firing only when the trigger fires.

**Step 5, additional guard.** When the candidate leans on a named external
source, resolve its ingest:

```bash
rg -l "^source: <exact-url>" kb/sources/*.ingest.md
```

- **No hit** — the source has no ingest. Refuse, naming the route
  (`cp-skill-ingest <url>`).
- **Hit** — read only that ingest's `## Claims` section. One section, not the
  ingest, and never the source.
  - The section carries the claim → cite the ingest, state which claim is used
    and why it transfers, save.
  - It does not → refuse, naming the grounding route.

**Step 6.** The refusal is a stop, not a branch: report the missing claim and the
literal next action. Write does not perform it.

Cost on an untriggered write: no I/O. On a triggered write: one `rg` and one
section read. No `Task`, no packet, no transaction, no second skill in the loop.

### The honest objection, and why it does not restore the dispatch

A writer judging whether a `Claims` section supports its own candidate is
**exactly the over-attribution configuration this workshop already documented**.
The [first worked case](../source-grounding/worked-case-agents-navigate.md)
called C1 and C3 subsumed; a blind pass tightened both to needs-narrowing. One
reader holding candidate and evidence together reads thematic overlap as support.

So the self-check is biased toward "yes." But note *which* error it is biased
toward, because the two failures are not symmetric:

- **Absence** — no ingest, or a `Claims` section that plainly does not mention
  this — is what the write-time check catches, and bias does not help a writer
  hallucinate a section that is not there. This is also the common case.
- **Over-attribution** — thematic overlap read as support — is what the
  write-time check misses, and no amount of care by the writer fixes it, because
  the bias is structural.

### The dispatch does not fix the failure it appears to fix

`draft-ground-source-dependent-claims.md` gives the worker `claims` containing
"the exact candidate wording" **and** has it read the source. One reader,
candidate and source together — the same configuration.

The Pirolli experiment that validated this design was **stricter than the design
it validated**. It separated the two: worker 1 saw the checksum-pinned source and
no candidate, and produced the reconstruction; worker 2 saw the candidates and
the `Claims` block and no source, and produced the verdicts. That separation is
why its verifier caught what the earlier single-reader pass missed.

The production worker collapses that separation back into one context. So the
expensive write-path dispatch buys the appearance of independent verification
without its mechanism.

### Where the blind check belongs instead

It does not have to run at write time, and it is better if it does not.

Once the note ships citing the ingest, `(note, ingest)` is a review pair — the
`source-as-gate` case from
[factored dependency pairs](../../reference/proposals/factored-dependency-pairs-for-review-freshness.md).
A blind verification is then an ordinary closed-ended verdict assay in the
existing review pipeline.

And the separation the experiment needed falls out of the architecture for free,
spread across time rather than across two dispatches:

- the **grounding** pass reads the source and writes `Claims` entries, with no
  target candidate in view;
- the **review** pass reads the note and the `Claims` section, with no source in
  view.

That is the experiment's design, obtained from mechanisms that already exist,
with nothing on the write path.

### Net

Write catches absence, cheaply, at the moment the author can still act. Review
catches over-attribution, blind, asynchronously, where rigor is affordable. The
write-time worker sits in the one position that is expensive *and* structurally
unable to do the harder job.
