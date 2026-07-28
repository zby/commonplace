# Exo methodology pitch

## Question

Two questions, the second deciding whether the first is worth anything:

1. What does Commonplace's artifact methodology offer a maximally-autonomous self-modifying agent — one that has solved code self-modification and left its prose layer entirely unverified?
2. Which parts of that offer survive the bitter-lesson objection ("the model is the knowledge layer"), and which are scarcity patches that thin as context grows?

Exo is the forcing case, not the subject. Question 2 is the one that determines whether this produces notes or only a pitch.

## Spine

The methodology aims at **objective constraints**, not house style. A constraint has the form *if you want X, you must have Y*. Where it is real, any system that wants X must satisfy it whether or not it has heard of Commonplace — so the predictive claim (independently built systems converge on satisfying it) is not a separate hope but the constraint's observable consequence, and therefore a test.

That splits every claim in this workshop into two layers, and only one of them is pitchable:

- **Candidate constraints** — artifacts classified so checks have targets; a declared contract per class so "good instance" is statable; lineage so invalidation is computable; authority declared so precedence and blast radius are knowable.
- **Witnesses** — YAML frontmatter, `COLLECTION.md`, the label vocabulary, review pairs, the freshness store. One solution among possible others. Pitching these as the direction is scope claimed rather than tested, which is the error [the bitter lesson punishes](../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) and which we diagnose in others.

Three conditions bound how far the spine reaches:

1. **Class membership is the live crux with Exo.** The constraint binds systems that want per-change criticism, selective revision, and verification of prose. Exo's bet is that they want none of it — the model supplies judgment, rollback handles errors, the log prevents repeats. If the bet holds they are outside the class and the constraint does not reach them. The argument's weight therefore sits on whether their goals put them under it, not on whether it is correct.
2. **Constraints admit many satisfiers, including implicit ones.** Directory convention, filename convention, a database schema, or the writing tool can all make a class legible to a check with nothing resembling frontmatter present. Systems can depart arbitrarily far in appearance and still comply. Only violation is excluded — keeping that line is what stops "objective constraint" from becoming a synonym for our design.
3. **Objectivity lives in the conditional.** They must stay free to decline X. Declining refutes nothing; it locates the constraint's boundary. A constraint whose antecedent cannot be declined is a demand.

**The inversion, and why this is the spine rather than a thread:** the 156 code-grounded reviews in `kb/agent-memory-systems/reviews/` are evidence about *us*, not about them. If systems that never heard of Commonplace keep arriving at typed prose, declared contracts, and invalidation, we found something structural. If none do, we most likely codified a house style and argued for it afterwards — which arguments alone cannot catch, because an argument can encode our own situation invisibly. That survey outranks drafting the pitch.

**Design it to find alternative satisfiers, not to count frequency.** Convergence has confounds — shared standards, shared engineering environment, a common local optimum — and its absence has innocent explanations: immature systems, structure hidden in code, or a system that accepts global rechecking instead of selective invalidation. A survey scanning for *our* mechanisms would systematically miss implicit satisfiers, which is not hypothetical: the Exo prose-partition error in thread 4 was exactly that failure, committed against a system already reviewed twice here. The stronger evidence is the intervention in thread 7; the survey's job is counterexamples and unfamiliar satisfiers.

## What would close it

- The corpus survey run, and its verdict recorded either way — including the outcome where it finds no convergence and the candidate constraints are demoted to house style.
- The claims that survive question 2 promoted to `kb/notes/`; the ones that don't, recorded as dropped and why.
- A decision on whether anything goes to the Exo project, and in what venue.
- Every thread below resolved or explicitly abandoned.

## Evaluation boundary

Exo at commit `baa07f67`, checkout at `related-systems/exoharness--exo/`. The system is already covered — [whole system](../../agentic-systems/exo.md) and [memory subsystem](../../agent-memory-systems/reviews/exo.md) — so this workshop does not re-review it. Claims about Exo should cite those artifacts or the checkout, not be re-derived.

Out of scope: the improvement criterion itself. Set aside by the maintainer on 2026-07-26 as unsettled work that belongs elsewhere. The pitch must therefore be honest that the methodology supplies places to attach checks, not a standard for what makes a change good.

## Threads

State as of the conversation that opened this workshop (2026-07-26). All provisional — nothing here has been tested against anything but discussion.

> **Read thread 11 first.** Several early threads reach for a structural deficiency in Exo and are refuted by the checkout. They are kept as record, corrected in place, not deleted. Thread 11 says why the pattern recurs and what to use instead.

**1. Ontology before oracle** *(landed 2026-07-26 as [verification needs a typed target before it needs an oracle](../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md); the first candidate constraint to test against the corpus)*

Verifying a mutable layer requires an artifact ontology before it requires an oracle. Exo isolates the variable: strong oracles for code (build, tests, restart-and-observe) sitting next to a completely unverified prose layer. The blocker isn't that prose oracles are hard — it's that the prose was never partitioned into classes with contracts, so no check has a target to attach to. The absence *presents* as an oracle gap and isn't one. Composes with [the boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) by adding that part of verification cost is ontological and comes due first.

**2. Distinguishing current commitments from historical events** *(note candidate; reframed 2026-07-26)*

The original framing was unbounded history against bounded context. Keep the mechanism, but lead with the sharper problem: the hard part is not fitting the history into the window, it is telling which of its contents are *still in force*. A log is undifferentiated as to currency — an attempt, its reversal, and the conclusion drawn are all just events. Compaction is the obvious counter to the context version of the argument, and it is unimplemented in Exo (the executor owns the policy per `docs/spec.md`), but it does not touch the currency problem and is itself bounded by "no universal distillation" below.

[Crystallized reasoning under context scarcity](../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) declines to argue whether scarcity actually stays binding: "there's reason to expect task complexity to scale alongside context ... but that's a separate argument this note doesn't make." This is that argument, in a form specific to long-running self-improving agents: history grows monotonically with operation, context grows at best linearly with engineering. Re-derivation cost scales with history; retrieving a distilled conclusion does not. Exo is the clean case — append-only log by design, "nothing can erase," multi-year ambition.

Initially recorded as a weak "attempted rescue" on the grounds that distillation-as-compression is scarcity-conditional and so concedes the bitter-lesson objection's form. **Upgraded 2026-07-26.** Scarcity-conditional does not mean transitional. Where the demand is generated by the same process that generates the capability — every self-modification adds to the history that must be reasoned over, and a more autonomous system produces more of it faster — scaling has to win a race rather than merely make progress. The historical precedent answers the bitter lesson on its own ground: compute fell by something like nine orders of magnitude and indexes, caches, compiled artifacts, and precomputed tables never went away. The response to bounds was structure, every time.

Two limits to respect when using it. Do not call the argument complexity-theoretic without machinery actually behind it — no established bound exists for LLM re-derivation, and the claim otherwise borrows rigor it has not earned. And the disanalogy: faster hardware is a constant factor that provably cannot change an exponent, whereas a better model may compress more insight per token, which is exponent-like. The reply is that compression has an information floor, but it needs stating, because that is where the analogy gets attacked.

The machinery may already exist. [agent-complexity-theory](../agent-complexity-theory/README.md) is trying to prove exactly this, with a normal form and a universality lemma to transfer results. Its first candidate result family — "orchestration cannot replace semantic inspection without a pre-built index" — is this argument as a lower bound. If it goes through, the answer to the scaling reply stops being "we do not know where finite capability ends" and becomes "no capability escapes this," which is a different pitch entirely.

Its second family is the constraint on our own side: "no universal distillation — no bounded summary preserves all task-relevant structure for a rich query family." So the pitch cannot promise that distilling the log solves anything. Distillation is relative to a query family. That strengthens thread 1 rather than weakening it — a contract per class *is* the declaration of which query family an artifact is distilled for, and without one you have summaries of undeclared scope, which is the undefined-domain failure one level up.

**3. Which legs are scale-invariant**

Sorting the counters to "the model is the knowledge layer" by whether scaling touches them:

- *Compression* (distillation saves context) — scarcity-conditional, but see thread 2: the scarcity is self-generated, so conditional is not the same as transitional. Upgraded from weakest leg to a serious one pending the lower-bound work.
- *Activation* — [knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md). Solid, but argues only for something-in-context; closes into thread 1 via "you can't route what you can't name."
- *Availability* — infinite context cannot recover what was never recorded. Rejected alternatives and abandonment reasons are absent from the log, not compressed in it. An information claim, so scaling doesn't reach it.
- *Commitment* — authority-bearing constraints bind as commitments, not compressed reasoning; survives the unbounded-context experiment by that note's own argument.
- *Stability* — re-derivation varies run to run; a committed conclusion fixes what was retained. Do not overstate this as determinism: the artifact stabilizes the retained content, while its downstream interpretation stays stochastic.

**4. No first-class maintained layer of explicit conclusions and rationale** *(corrected 2026-07-26 — the original "Exo has no knowledge layer" was false)*

Exo has memory, todos, a local profile, skills, prompts, a self map, and an event log. What it lacks is a maintained layer of explicit conclusions *about itself* carrying scope, evidence, authority, and invalidation conditions. `SELF-CONTROL.md` and `RSI.md` hold the real theory and are human-written, outside anything the loop reads or maintains.

Drop the earlier "improvement accumulates as policy, never as understanding" — skills and prompts can carry understanding. The accurate version: Exo does not distinguish rationale, evidence, policy, and self-description, and tracks no derivation between them. State this as an empirical characterization, not a verdict.

**5. A loop can apply a contract but cannot warrant one**

Sharpening of "building the scaffolding needs a human operator." **Too categorical as first stated** — a loop broad enough to generate evidence about its own contracts can compare candidates and revise them, so "cannot warrant" is false in general. The live question is narrower: which evidence crosses into the boundary, and what acceptance process warrants a *particular* contract. Check for overlap before writing — [warranted autonomy](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) and [methodological and computational closure](../../notes/methodological-and-computational-closure-track-different-changes.md) may already own what survives.

**6. The relocation note** *(decided)*

Rewriting [increasing computational autonomy relocates human effort](../../notes/increasing-computational-autonomy-relocates-human-effort.md) around the obstacle frame was considered and rejected: its payload is measurement ("measure improvements per human judgment, not human time"), and the bottleneck half is already owned by the boundary-of-verification note. Pending action if thread 1 lands: add one link naming what specifically sits at the frontier.

**7. Pitch assembly and venue** *(now the practical centre)*

**Positioning — adopt this and drop the diagnostic framing.** Commonplace is not scaffolding to add to Exo's protected substrate; it is a candidate for the mutable semantic layer Exo deliberately leaves open. `docs/spec.md` states the rationale itself: the exoharness is kept minimal "to maximize the space of behaviors that can evolve above it," with the executor owning memory, compaction, and prompt-assembly policy. So the proposal is a **replaceable, agent-editable semantic policy above the substrate** — and the agent must be free to alter, replace, or delete it. That is also the cleanest answer to the bitter lesson: the defensible invariant is that the system needs some way to maintain usable conclusions; our types and contracts are a hypothesis about how.

**The experiment, which should replace diagnosis as the ask.** Give an Exo instance a small Commonplace-like collection plus operations to create, revise, supersede, and invalidate semantic artifacts over its own prompts, skills, memories, self map, and design claims. Compare against an equivalent instance reasoning directly over event history. Measure: recurrence of previously diagnosed mistakes; stale or contradictory self-descriptions after modification; ability to explain why a policy exists; semantic regressions caught before adoption; cost of reconstructing prior decisions; overhead the explicit layer imposes. This is falsifiable, and a capable model plus raw history performing equally well is a real result rather than a failed pitch.

**Assembly notes**

Assembles from [axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) (the spine — already applied to Exo once by the memory review), [system-definition artifact](../../notes/definitions/system-definition-artifact.md), [lineage](../../notes/definitions/lineage.md), and [codify and relax](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) as the answer to their bitter-lesson framing. Hooks available in their own material: the design principle that "a mutation path that bypasses the tools also bypasses the record," and skills as the one prose class they already accepted frontmatter and validation for. Concede up front that storage substrate is the field they've genuinely nailed. Venue undecided — GitHub discussion on their repo is the obvious candidate.

**8. Having a form is not being reflective over it** *(note candidate)*

Three levels, which Exo separates cleanly: the form is present in the system (prompts, self map exist); the self-representation covers it mechanically (it reads and edits them); the system can operate on it as a commitment (it cannot — no statement of what a prompt claims, no check against another commitment, no selective revision on evidence, no invalidation when something it describes changes). [Reflective coverage is graded](../../notes/reflective-coverage-is-graded-across-representational-forms.md) supplies the two dimensions and [reflection buys addressability](../../notes/reflection-buys-addressability.md) already notes in scope that "mechanical observation or modification can coexist with weak semantic addressability" — what neither states outright is the three-level ladder, or that level 3 requires the classification thread 1 argues for.

The demonstration to use with Exo is internal to their system: their operation profile over symbolic form is rich (read, edit, compile, test, adopt, roll back, reject-capable gate); over prose it is read and edit. Same agent, same repo, same commit, profile collapses when the form changes.

Thread 10 adds a fourth rung: present, mechanically covered, operable as a commitment, and **wired** so the operation actually fires.

**9. Scoping the "cannot be only weights" argument** *(caution, not a thread to develop)*

The strong reading contradicts [reflection buys addressability](../../notes/reflection-buys-addressability.md), which holds that compounding is available without reflection, that parametric learners genuinely self-improve, and that requiring reflection for membership "fails against the field's central cases." Do not pitch it. The defensible form is what the readable forms buy — addressability and verifiability — not membership in self-improvement. Related: [the readable-artifact loop](../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) already argues the prose+symbolic pair is the tractable unit.

**10. Synchronization of retained self-description** *(landed 2026-07-26 as [stale self-description conceals its own staleness](../../notes/stale-self-description-conceals-its-own-staleness.md))*

Writing it found that the general requirement was already owned — [source lineage](../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) for the dependency record and [stale indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) for the worse-than-absent asymmetry, which that note already generalizes to specs and architecture docs. The note therefore claims only what reflexivity adds: the detecting process consults the artifact that drifted (so the error conceals its own evidence), the trigger has no edit event because the referent moves through acts rather than writes, and load scales with autonomy.

> A system that continues to consume claims about mutable aspects of itself needs a way to revalidate, revise, regenerate, supersede, or retire those claims when the relevant aspects change.

Corrected 2026-07-26. The first statement — "retention without intercession guarantees the theory becomes false" — overclaimed twice. Self-modification does not falsify every retained theory, only those about aspects that actually changed; and the requirement is **synchronization**, not specifically intercession over the same stored artifact, since regenerating or retiring it also satisfies it. The necessity is still generated by the system's own mutability, so it needs no amendment to [reflective system](../../notes/definitions/reflective-system.md) and does not collide with "intercession is a capability within reflection, but not every reflective architecture permits it."

Derive it from availability and reliability, not from resource limits. *Availability*: the log holds attempts, not conclusions, and alternatives dismissed without being tried leave no trace at all. *Reliability*: re-derivation is a per-call gamble with variance while retention is done once and checkable — and a more autonomous system needs the theory more often, so re-derivation error compounds fastest exactly where Exo is aiming. That inversion turns their ambition into the argument's support.

**What it proves about Exo is narrower than it first looks.** They have prose intercession: `SELF.md` is an agent-maintainable self map editable through the same shell path as everything else. The gap is **capability without a wire** — nothing connects "the code changed" to "the theory describing it is now false," and the documents holding the real theory (`RSI.md`, `SELF-CONTROL.md`) are human-written and sit outside the loop's consumption path, while only the navigational map is injected. In our own operativity vocabulary: no consumer, channel, or force makes the operation fire. This is the staleness observation from the opening of this thread, now with a reason it is necessary rather than merely useful.

**11. Caution: stop reaching for a structural deficiency** *(recurring near-miss)*

Four attempts so far have tried to locate Exo's gap in missing structure — not reflective on prose, no knowledge layer, lacks intercession, prose unpartitioned — and the checkout refuted every one. The fourth is the instructive one: the prose-partition claim reached a committed note before an external reader caught it, and the evidence refuting it (`SELF-CONTROL.md`'s eight-row state table and its routing rules) had been sitting in a system reviewed twice in this KB. Exo is genuinely strong on reflective structure every time it is checked: self-representation, causal connection, intercession, coverage across both forms. The gap has never been structural. It is always semantic: what the system can *do* with a covered component beyond reading and writing it.

The frame that gets this right is already in the [reflective system](../../notes/definitions/reflective-system.md) definition — the Smalltalk image, where "intercession is total" and yet "left alone, the image sits there for a decade and improves nothing ... **the programmer supplies the evidence-responsiveness**." Exo is a Smalltalk image for agents: maximal intercession, minimal everything else. Stated that way the disagreement is precise and not insulting — not "you are not reflective," but "you built a Smalltalk image for agents, and the open question is whether the model can occupy the seat the programmer used to."

## Bookkeeping

- Already shipped from this thread: `63effb8e` recorded the cloning-claim inconsistency in `kb/agentic-systems/exo.md` (README and `RSI.md` present cloning and clone lineage as shipped; `SELF-CONTROL.md` marks area 7 not built).
- Adjacent workshops, check before duplicating: [agent-complexity-theory](../agent-complexity-theory/README.md) (**the dependency** — its result families 1 and 2 decide how strong thread 2 can be stated), the closed scaffolding-relaxation workshop, promoted to [parametric reproduction alone cannot replace an authoritative record](../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) (what stronger models made obsolete in scaffolding — shares thread 2's territory), [self-improvement-cluster-operationalization](../self-improvement-cluster-operationalization/README.md) (inward-facing counterpart).

---

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) — draws-on: the four-field record that is the methodology being pitched
- [System-definition artifacts are crystallized reasoning under context scarcity](../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) — tests: runs the unbounded-context experiment thread 2 must survive
- [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: oracle construction as the automation bottleneck, which thread 1 extends backwards to ontology
- [Exo](../../agentic-systems/exo.md) — evidenced-by: the whole-system analysis this workshop reasons from
- [Exo agent memory system review](../../agent-memory-systems/reviews/exo.md) — evidenced-by: the subsystem review that already applied artifact analysis to this system
