# Exo methodology pitch

## Question

Two questions, the second deciding whether the first is worth anything:

1. What does Commonplace's artifact methodology offer a maximally-autonomous self-modifying agent — one that has solved code self-modification and left its prose layer entirely unverified?
2. Which parts of that offer survive the bitter-lesson objection ("the model is the knowledge layer"), and which are scarcity patches that thin as context grows?

Exo is the forcing case, not the subject. Question 2 is the one that determines whether this produces notes or only a pitch.

## What would close it

- The claims that survive question 2 promoted to `kb/notes/`; the ones that don't, recorded as dropped and why.
- A decision on whether anything goes to the Exo project, and in what venue.
- Every thread below resolved or explicitly abandoned.

## Evaluation boundary

Exo at commit `baa07f67`, checkout at `related-systems/exoharness--exo/`. The system is already covered — [whole system](../../agentic-systems/exo.md) and [memory subsystem](../../agent-memory-systems/reviews/exo.md) — so this workshop does not re-review it. Claims about Exo should cite those artifacts or the checkout, not be re-derived.

Out of scope: the improvement criterion itself. Set aside by the maintainer on 2026-07-26 as unsettled work that belongs elsewhere. The pitch must therefore be honest that the methodology supplies places to attach checks, not a standard for what makes a change good.

## Threads

State as of the conversation that opened this workshop (2026-07-26). All provisional — nothing here has been tested against anything but discussion.

**1. Ontology before oracle** *(note candidate, currently the strongest)*

Verifying a mutable layer requires an artifact ontology before it requires an oracle. Exo isolates the variable: strong oracles for code (build, tests, restart-and-observe) sitting next to a completely unverified prose layer. The blocker isn't that prose oracles are hard — it's that the prose was never partitioned into classes with contracts, so no check has a target to attach to. The absence *presents* as an oracle gap and isn't one. Composes with [the boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) by adding that part of verification cost is ontological and comes due first.

**2. Unbounded history against bounded context** *(note candidate)*

[Crystallized reasoning under context scarcity](../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) declines to argue whether scarcity actually stays binding: "there's reason to expect task complexity to scale alongside context ... but that's a separate argument this note doesn't make." This is that argument, in a form specific to long-running self-improving agents: history grows monotonically with operation, context grows at best linearly with engineering. Re-derivation cost scales with history; retrieving a distilled conclusion does not. Exo is the clean case — append-only log by design, "nothing can erase," multi-year ambition.

Note the tension to resolve: the crystallized-reasoning note concludes that distillation-as-compression is *scarcity-conditional*, which concedes the bitter-lesson objection's form. Thread 2 is the attempted rescue. If it fails, the pitch must stand on the scale-invariant legs only (below).

**3. Which legs are scale-invariant**

Sorting the counters to "the model is the knowledge layer" by whether scaling touches them:

- *Compression* (distillation saves context) — scarcity-conditional. Weakest leg for this audience; thread 2 decides it.
- *Activation* — [knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md). Solid, but argues only for something-in-context; closes into thread 1 via "you can't route what you can't name."
- *Availability* — infinite context cannot recover what was never recorded. Rejected alternatives and abandonment reasons are absent from the log, not compressed in it. An information claim, so scaling doesn't reach it.
- *Commitment* — authority-bearing constraints bind as commitments, not compressed reasoning; survives the unbounded-context experiment by that note's own argument.
- *Determinism* — re-derivation varies run to run; a committed conclusion doesn't.

**4. Exo has no knowledge layer**

Its retained artifacts are events (what happened) and code/prompts (what to do). No artifact class for why. `SELF-CONTROL.md` and `RSI.md` are exactly that missing layer and are hand-written by humans, outside anything the improvement loop reads or maintains. Consequence: improvement accumulates as policy, never as understanding. May be a note or may just be evidence for threads 1–3.

**5. A loop can apply a contract but cannot warrant one**

Sharpening of "building the scaffolding needs a human operator." The agent can autonomously apply a contract; establishing that a given ontology or oracle is the right one needs evidence the loop doesn't generate. Check for overlap before writing — [warranted autonomy](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) and [methodological and computational closure](../../notes/methodological-and-computational-closure-track-different-changes.md) may already own it.

**6. The relocation note** *(decided)*

Rewriting [increasing computational autonomy relocates human effort](../../notes/increasing-computational-autonomy-relocates-human-effort.md) around the obstacle frame was considered and rejected: its payload is measurement ("measure improvements per human judgment, not human time"), and the bottleneck half is already owned by the boundary-of-verification note. Pending action if thread 1 lands: add one link naming what specifically sits at the frontier.

**7. Pitch assembly and venue**

Assembles from [axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) (the spine — already applied to Exo once by the memory review), [system-definition artifact](../../notes/definitions/system-definition-artifact.md), [lineage](../../notes/definitions/lineage.md), and [codify and relax](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) as the answer to their bitter-lesson framing. Hooks available in their own material: the design principle that "a mutation path that bypasses the tools also bypasses the record," and skills as the one prose class they already accepted frontmatter and validation for. Concede up front that storage substrate is the field they've genuinely nailed. Venue undecided — GitHub discussion on their repo is the obvious candidate.

## Bookkeeping

- Already shipped from this thread: `63effb8e` recorded the cloning-claim inconsistency in `kb/agentic-systems/exo.md` (README and `RSI.md` present cloning and clone lineage as shipped; `SELF-CONTROL.md` marks area 7 not built).
- Adjacent workshops, check before duplicating: [scaffolding-relaxation](../scaffolding-relaxation/README.md) (what stronger models made obsolete in scaffolding — shares thread 2's territory), [self-improvement-cluster-operationalization](../self-improvement-cluster-operationalization/README.md) (inward-facing counterpart).

---

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) — draws-on: the four-field record that is the methodology being pitched
- [System-definition artifacts are crystallized reasoning under context scarcity](../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) — tests: runs the unbounded-context experiment thread 2 must survive
- [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: oracle construction as the automation bottleneck, which thread 1 extends backwards to ontology
- [Exo](../../agentic-systems/exo.md) — evidence: the whole-system analysis this workshop reasons from
- [Exo agent memory system review](../../agent-memory-systems/reviews/exo.md) — evidence: the subsystem review that already applied artifact analysis to this system
