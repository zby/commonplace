# Four further cases

Written 2026-11-21 by an agent (claude-fable-5-2) at the operator's request.
The workshop already has two cases: one line added to `AGENTS.md`, and
[Python 3.11 over 3.10](./python-release-worked-case.md). Both compare
observable gains with possible losses, and in both a loser can avoid the loss
or the loss is small. The four cases here differ on those points. They are
described from general knowledge, with no outside source checked. Case D is
the longest because the operator named reversibility as something we often
use when deciding.

## Case A — a refactoring: the whole gain lies in future work

A team rewrites a module so that its parts can be changed separately. The
behaviour is the same before and after. Every test passes on both versions.

**What is different.** Nothing observable improves at the step. For any
measure that counts only current work, the successor is equal or slightly
worse, because the rewrite cost time and may have introduced faults the tests
miss. The gain exists only for measures that count changes not yet made.

**How the definition applies.**

- *Fix the comparison.* The period decides almost everything. Over the next
  week the refactoring loses. Over the life of the module it may win.
- *Reasonable measures.* A measure that stops at the next release is
  reasonable for a module about to be retired, and not for one the team
  expects to change every month. So the set of reasonable measures depends on
  a forecast: how often, and where, the module will change.
- *The verdict.* Improvement, if every reasonable forecast has enough later
  changes in the parts that were separated. Open, if plausible forecasts
  differ on that.
- *What would settle it.* Later changes. If the next several changes each
  touch one part, the forecast is confirmed. If they cut across the new
  boundaries, the refactoring made them harder.

**What it shows about the definition.**

- The measures can range over work that has not happened. The definition
  still applies, but the verdict then rests on a forecast, and the evidence
  arrives afterwards.
- This is the case closest to a claim of learning. Learning in
  [Simon's sense](../../theory/learning-is-not-only-about-generality.md) is
  improved capacity for future action. A retained change that helps no current
  task can still be an improvement, and can only be shown to be one later.
  That matches
  [the test for compounding](../../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md),
  which looks at a later episode.
- "Open now, settled later" is a normal verdict, not a failure of the
  definition.

## Case B — approving a medicine: no common scale, and no opting out

A regulator decides whether a new medicine may be sold. Trials show that it
relieves a condition for most patients and causes serious harm to a few.

**What is different.**

- The gains and losses are of different kinds: relief of symptoms for many,
  severe harm for a few. No exchange rate between them is given.
- The people harmed cannot be identified beforehand, so they cannot choose to
  stay out, as a blocked project stays on Python 3.10.
- The harm cannot be undone.

**How the definition applies.**

- *Reasonable measures.* In the Python case, a measure that counts only the
  worst-off project was excluded, because that project could keep the old
  version. Here no patient can avoid a harm that nobody can predict, so a
  measure that gives severe irreversible harm very high weight is reasonable.
  So is one that adds up relief across all patients.
- *The verdict.* For a mild condition with other treatments available, those
  measures disagree: open. For a fatal condition with no other treatment,
  even the harm-weighted measures favour approval: improvement.
- *What regulators do with "open".* They narrow the question until the
  measures agree. A medicine is approved for the patients in whom the benefit
  is large or the alternatives are absent, and excluded for groups in whom the
  harm is more likely. Each narrowing changes whose outcomes the comparison
  covers.

**What it shows about the definition.**

- Whether a measure is reasonable depends on the situation, not on its form.
  The worst-off measure was unreasonable for a default that projects can
  decline. A similar measure is reasonable when the loss is irreversible and
  cannot be declined.
- The measures do not need a common scale for a verdict. They need one only
  for a weighted average. When measures in different units agree, the verdict
  holds; when they disagree, no average is available to settle it.
- An open verdict can be resolved by narrowing the area the claim covers. This
  is the operator's earlier point about progress in a declared application
  area, reached from the other side: the area is cut down to where every
  reasonable measure agrees.

## Case C — a removal: the loss is visible and the gain is not

A project deletes a command that few people use. Commonplace does this kind of
thing by rule: [ADR 085](../../reference/adr/085-withdrawn-proposals-are-deleted.md)
deletes withdrawn proposals, and `AGENTS.md` says to keep no backwards
compatibility without a consumer need.

**What is different.** It mirrors the `AGENTS.md` case. There a few tasks gain
visibly and every task may lose a little. Here a few users lose visibly, and
everyone else gains a little on every later task: less to read, less to keep
consistent, fewer wrong turns.

The two sides also differ in what evidence they leave. A user who lost the
command can report it. Nobody reports the search that no longer returned a
stale document. The gain never appears as an event.

**How the definition applies.**

- *Reasonable measures.* A measure that counts only reported events will
  reject every removal, and will accept every addition whose cost is spread
  thin. It is not reasonable, because it is blind to one kind of effect
  whichever side that effect falls on.
- *A consistency check.* The same measures must serve both cases. If we accept
  the `AGENTS.md` line by judging its small cost on every prompt to be
  negligible, we cannot then count a small saving on every task as decisive
  for a removal. Whatever weight a thinly spread effect gets, it gets on both
  sides.
- *The verdict.* Improvement, if the users of the removed thing have another
  way to do the same work, since their loss is then a one-time change of
  habit. Open, if some users lose a capability they cannot replace.

**What it shows about the definition.**

- The set of reasonable measures is constrained across cases, not only within
  one. A measure chosen to win one comparison has to give acceptable verdicts
  on the others.
- Which effects leave evidence is not the same as which effects are large. A
  reasonable measure counts an effect by its size and reach, not by whether
  someone complained.

## Case D — a step that cannot be undone

A team publishes an interface that other projects will build on. After that,
changing it breaks their code. Compare a change to an internal function, which
can be reverted in one commit.

**What is different.** In every earlier case the comparison was between two
states. Here the step also changes which later steps are available. Before
publishing, the team can choose any interface. Afterwards it cannot.

### What reversibility does to a decision

Reversibility does not change the verdict. It changes what an open verdict
permits.

- **Reversible and open: adopt provisionally.** Trying the step is the
  cheapest way to get the missing evidence. If it turns out worse, the loss is
  what accrued during the trial, plus the cost of going back.
- **Irreversible and open: do not take the step yet.** Trying it is the same
  as deciding. The team first needs the evidence, or a way to make the step
  reversible, or a narrower step.

So under an open verdict a reversible step can still be the right decision.
It remains a decision and not a demonstrated improvement, as the
[on-balance note](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md)
says of ADR 085.

### Reversibility bounds the effects nobody listed

This answers part of the question the workshop began with. For a reversible
step, the unlisted effects cannot do more harm than accrues before the step is
reverted. The bound comes from time, not from counting effects:

> worst case ≤ harm per unit of time × time until the harm is noticed, plus the
> cost of reverting.

No count of effects and no per-effect bound is needed. Three conditions are
needed instead:

1. **The harm is noticed.** A loss that nobody detects is never reverted. The
   `AGENTS.md` line is easy to delete, but a task that fails because of it
   does not say why. That step is reversible in the mechanical sense and only
   weakly reversible in practice.
2. **The harm done in the meantime can itself be undone.** A medicine can be
   withdrawn from sale; the patients already harmed are not restored. Case B
   is irreversible for this reason.
3. **Nothing has been built on the step.** A published interface, a public
   address, or a term used in two hundred notes can still be changed in
   principle. Each dependent raises the cost. Reversibility belongs to the
   step together with what has come to depend on it, and it decays with time.

### How the definition applies to the irreversible step

- *Reasonable measures.* A measure that puts a price on the options given up
  is reasonable here, as the harm-weighted measure was reasonable for the
  medicine. The set of reasonable measures is wider for an irreversible step.
- *The verdict.* A wider set agrees less often, so "open" is more common. That
  is the definition reporting correctly that the step needs more support.
- *What people do.* They turn the irreversible step into reversible ones:
  - a draft before a published text;
  - a deprecation warning before a removal. In the Python case,
    `inspect.getargspec` warned on 3.10 before it was removed in 3.11;
  - a copy before a deletion;
  - a release to a few users before a release to all.

Commonplace has this built into its rules:

- An article moves from draft to working paper to published. A draft may be
  rewritten silently. A published article is frozen, and
  [the articles contract](../../articles/COLLECTION.md) requires explicit
  approval for promotion.
- Workshops are deleted when they close and nothing in the library links into
  them, so a workshop step costs little to undo. A library note that others
  link to costs more.
- `AGENTS.md` forbids a hard reset or a force-push without explicit
  permission.

In each rule the support demanded rises as the step gets harder to undo.

**What it shows about the definition.**

- A verdict and a decision are different things, and reversibility is the
  main ground for deciding while the verdict is open.
- Reversibility supplies the bound on omitted effects that the statistical
  sources could not, under the three conditions above.
- A possible link to the naming workshop, which is the agent's reading and
  not the operator's: conjecture and criticism works because a tentative
  theory is cheap to drop. A theory builder can act on open verdicts so long
  as its steps stay reversible. Retention that later work builds on makes a
  step harder to undo, so it should need more support.

## What the six cases cover together

| Case | Where the gain is | Where the loss is | Can a loser avoid it? | What decides the verdict |
|---|---|---|---|---|
| One line in `AGENTS.md` | A few tasks, observed | Every task, possible and small | No | How often tasks run near their limit |
| Python 3.11 over 3.10 | Most projects, repeated | A few projects, found beforehand | Yes, by staying | Whether blockers are widespread |
| A refactoring | Future changes only | Now, and certain | Not applicable | A forecast, confirmed later |
| Approving a medicine | Many patients | A few, severe and permanent | No | Whether the claim can be narrowed |
| A removal | Everyone else, thinly and unseen | A few users, visible | Only if another way exists | Whether the same weights are used as for additions |
| An irreversible step | As in the underlying comparison | The options given up | No | Whether the step can first be made reversible |
