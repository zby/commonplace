# When does a change run need to check ADRs?

Reasoning, not a decision. The trigger question is upstream of the mechanism:
you cannot design routing without knowing when the route should fire.

## The circularity

The natural trigger is "when the change would contradict, extend, or depend on
a prior decision." You cannot evaluate that without already knowing the
decisions. The trigger condition requires the knowledge the trigger would
fetch.

Any design that ignores this collapses to "always check," which is
unaffordable and will be skipped — and a skipped instruction is worse than no
instruction, because it creates the appearance of coverage.

## Working backwards from failure modes

Consultation earns its cost when it prevents:

- **Silent reversal.** Restoring a state that was deliberately rejected,
  without knowing it was.
- **Chesterton's fence.** Something looks arbitrary, gets cleaned up, and the
  reason it existed goes with it.
- **Parallel mechanism.** Building a second way to do something because the
  first was not known to be the chosen answer for that class.
- **Re-litigating.** Re-deriving a settled decision and reaching a worse
  version.

## Self-detecting triggers versus lookup triggers

The cut that makes the problem tractable: some of these announce themselves
from inside the change.

**Self-detecting.** Chesterton's fence and parallel mechanism are noticed by
the agent making the change — it cannot explain why something exists, or it is
about to create a second path to the same outcome. These need only an
instruction. No index, no routing surface.

**Lookup.** Silent reversal and re-litigating are invisible from inside the
change; nothing about the work looks wrong. Only a lookup catches them.

This splits the problem and sequences it. The self-detecting half can ship
cheaply and immediately. The lookup half is the smaller, harder residue, and
it is the only part that might justify a mechanism.

## An enforced decision needs no consultation

Where a decision left a trace at the site it constrains — a validator, a
schema, a test, a `# BACKCOMPAT:` marker — reversing it fails loudly, and
reading the ADR is redundant with reading the check.

So the routable set is not 72. It is the ADRs whose decisions have no
enforcement trace anywhere. Partitioning on that is concrete work and would
change what mechanism is warranted.

## Timing

Consulting after the change is written is close to useless: the effort is
spent and the author is biased toward keeping it. The trigger belongs at
approach selection, before commitment.

Review is the backstop for what the author missed. The review system already
has gates, so an ADR-consistency gate composes with an authoring instruction
rather than competing with it.

## What does not need it

A bug fix restoring intended behavior. A pure addition in an area no decision
touches. Writing a note. Workshop exploration, whose value is consumed rather
than accumulated. Naming these matters as much as naming the triggers, because
over-triggering is what makes an instruction ignorable.

## Corpus measurements, 2026-08-23

- **72 ADRs, 511 KB.** Roughly 128k tokens. Exhaustive reading is not viable
  alongside code and a task; it is a full context window by itself.
- **Descriptions total 17 KB** — 3% of the corpus, a few thousand tokens. A
  `rg "^description:" kb/reference/adr/` sweep is affordable on every change.
- **66 of 72 cite another ADR.** Cross-citation is dense, so once one relevant
  decision is found, link-following reaches its neighbourhood. Precision at
  entry matters more than recall.
- **40 mention supersession.**

The description layer being 3% of the corpus is the most consequential number
here. If descriptions are good enough to support a routing decision, the
mechanism may already exist and the missing piece is only an instruction that
says to use it. Testing that is cheaper than building anything, and the
repository's YAGNI rule says test it first.

## Detecting misses retrospectively

The hard half of observation: a miss leaves no trace at the time, because the
agent did not know what it did not consult. Candidate retrospective signals,
none yet validated:

- **An ADR superseding another without citing it.** The author plausibly did
  not know the earlier decision existed. Mechanically checkable against the
  cross-citation data above.
- **Two ADRs deciding the same question independently.**
- **A change reverted with a rationale that already existed.**
- `kb/log.md` entries recording a rediscovery.

## Open

- Does a self-detecting trigger actually fire in practice, or does an agent
  confidently explain a fence it has invented a reason for?
- Are the descriptions discriminating enough for routing, or do they describe
  the decision without indicating what class of change it constrains?
- Is "no enforcement trace" checkable, or does establishing it require reading
  each ADR and searching for its encoding?
