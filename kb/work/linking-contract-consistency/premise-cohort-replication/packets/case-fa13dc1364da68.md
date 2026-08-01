# Case packet

Neutral case identifier: case-fa13dc1364da68

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Abstract an experience into a lesson only when you can state where the lesson stops

After an episode, an agent learning from experience faces a choice: abstract what happened into a broad lesson, or keep the concrete instance. Compress too eagerly and you get an *over-generalized* lesson the agent then applies everywhere; compress too little and rare, situation-specific knowledge never compounds. The usual handles — frequency, confidence, recency — don't separate the two cases. The discriminator is whether the agent can state the lesson's **boundary**: the condition under which it holds, equivalently where it stops applying.

## The boundary clause is the explanatory-reach test applied to memory formation

The KB already has the test in another guise. A genuine generalization [predicts where it fails — change the constraint, change the conclusion]; a note that merely records "X works" is adaptive fit, brittle the moment the context shifts. Abstracting an experience is the same move under a deadline: it turns a single trace into a candidate rule by adding a condition clause and a rationale the trace did not contain. The condition clause *is* the boundary.

So an **over-generalized lesson is an abstraction asserted without its condition clause** — adaptive fit wearing the surface of explanatory-reach. The failure mode the question names — agents applying a lesson everywhere, never learning when to disengage — is not a tuning problem. It is the structural consequence of storing the rule while dropping the boundary that would tell the agent where to stop. The complement holds too: a [fact has low explanatory-reach by design], so it has no boundary to state and nothing to gain from abstraction. The decision is not "compress or not" but "can I name the scope; if not, keep the instance."

## Successes and failures supply boundaries asymmetrically

The sharpest reason to treat episodes differently by outcome is that successes and failures carry boundary information asymmetrically:

- A **success is an existence proof**: it shows the approach was *possible* here. It does not establish that the approach is *better than alternatives* across cases, so any lesson abstracted from it imports a boundary the agent has not earned. Preserve it as a concrete, replayable demonstration rather than a rule.
- A **failure carries a directive** — "what to change" — that names a violated constraint. That directive is a candidate boundary, which makes failures the natural raw material for lessons. (This echoes Popper: a refutation is more informative than a confirmation because it locates a limit.)

This predicts the finding of [SkillRL] — a skill-augmented RL framework that preserves successful trajectories as demonstrations while synthesizing failures into concise lessons — that processing successful episodes as replayable demonstrations while abstracting failures into concise lessons beats uniform compression of both. Uniform compression abstracts both kinds the same way, but the failures were the half where a boundary was already on hand; the loss concentrates on the successes, which get over-generalized into rules no boundary justifies.

## What supplies — or strips — the boundary

The same lens organizes the mechanisms the field has surfaced — each turns on whether inspectable failure evidence survives processing, [which is itself a first-class learning bottleneck]:

- **Evaluative vs directive feedback.** Feedback splits into how-well-it-went (evaluative) and what-to-change (directive). The directive component carries the scope; a scalar reward keeps only the evaluative and discards exactly the part that would bound the lesson — which is why reward-only signals tend toward over-generalization.
- **Uncompressed reflection.** Reflexion (an agent framework that retries tasks guided by verbal self-reflection) keeps verbal self-diagnoses uncompressed because the boundary lives in the specifics; compress them and the condition clause goes with the detail, leaving a bare directive that over-applies. "Compress them and they stop helping" is the boundary being stripped.
- **Process over outcome verification.** Checking intermediate steps rather than final answers validates the *mechanism* — the *why* — which is what earns a lesson [explanatory-reach] rather than coincidental fit. A lesson that survives process validation has an articulable basis, so its boundary is statable; an outcome-only pass cannot tell a real rule from a lucky one.
- **Granular, individually addressable skills.** Storing skills as discrete units refined by feedback (VOYAGER, an LLM agent that builds a reusable skill library) keeps each skill's applicability condition attached to it. Collapsing them into one unified policy erases the per-skill boundaries — over-generalization by merger.

## When you can't state the boundary, preserve the instance

The complement of the rule is a positive instruction, not a discard. A rare fact's worth is [its retrievability, not its transfer]: preserved verbatim and findable, it pays off in the narrow context it came from. And even after a lesson is abstracted, the [source stays for edge cases the abstracted rule cannot cover] — which argues for keeping the instance whenever the boundary is in doubt. Over-eager abstraction is the expensive error: a verbatim instance that turns out generalizable can be abstracted later, but an over-generalized lesson silently misfires until something forces the boundary into view.

## Scope

The discriminator says *when* abstraction preserves explanatory-reach, not how an agent mechanically decides it — stating a boundary is itself a judgment, and whether a mined pattern [has explanatory-reach or is just a recurring local patch remains an open problem] at the field level. The claim narrows the question rather than closing it: it says what the agent must be able to produce (a condition clause) for an abstraction to be trustworthy, and what to do (preserve the instance) when it can't.

Read as a criterion, boundary-statability sharpens the [validity gate that decides what is trustworthy enough to learn from], and the abstraction operation it governs is one whose [authority must be earned per operation rather than granted at capture] — the boundary test is the oracle that licenses the abstracted rule.

## Sources

- [Inquiring line: "How can agents distinguish over-generalized lessons from genuinely useful long-tail knowledge?"] — poses the question and assembles the five mechanisms (SkillRL, Reflexion, feedback decomposition, process verification, VOYAGER) reorganized here under the boundary discriminator.
- [SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning] — the differential-processing finding: successful trajectories preserved as demonstrations, failed ones synthesized into concise lessons, grounding the success/failure asymmetry directly rather than through the umbrella article.
- Karl Popper — refutations are more informative than confirmations; grounds the success/failure asymmetry.

---

Relevant Notes:

## Artifact B

# First-principles reasoning selects for explanatory-reach over adaptive fit

Commonplace's first-principles methodology is valuable because it selects for explanations with **explanatory-reach**: claims that keep working outside the case that produced them because they capture why a pattern works, not just that it worked. This note adapts David Deutsch's adaptive-vs-explanatory distinction (his term is bare "reach") for KB design, treating adaptive fit and explanatory-reach as a polarity rather than a hard binary.

**Adaptive information** helps a system cope with the world. A genome, a neural network's weights, or a local rule of thumb can encode something useful without explaining why it works or where it stops working.

**Explanatory knowledge** gives a criticizable account of why the pattern works. It can be deliberately varied: change a load-bearing premise, and the explanation should constrain what changes in the conclusion. That variation is what gives an explanation its explanatory-reach.

Partial cases sit between the poles. A rule can transfer across a narrow family of cases because it captures shared structure, while still falling short of a full generative model. The point is not to demote every local observation; local fit is the evidence a later explanation must organize, predict, and improve.

## Why this matters for the KB

When a note derives a design pattern from inherited constraints — finite context, no scoping mechanism, text-in/text-out interpretation — the derivation can be explanatory: it says why the pattern works and predicts where it will fail. Change the constraint, and the conclusion should change with it.

That "can be" matters. First-principles stories become post-hoc rationalization when broad premises can justify several rival practices equally well. A useful derivation should rule out at least one plausible alternative, name the constraint that does the ruling out, or predict a failure that later use can confirm.

The [computational-model] area is an explanatory-reach bet under audit. Programming-language concepts such as scoping, partial evaluation, and scheduling were developed for compilers, but they reach into KB design when the shared invariant is explicit: bounded processors compose text under constraints, and unscoped composition lets distant bindings interfere. [LLM context is composed without scoping] therefore works only if the dynamic-scoping comparison predicts real context failures and useful remedies, not merely because the analogy is elegant.

## The negative test

This adapted distinction provides a quality check orthogonal to the KB's type system. A well-formed note can pass every structural check while still recording a pattern without explaining the mechanism. The test:

1. **Can you vary a load-bearing premise?** If changing one premise lets you predict a constrained change in the conclusion, the note is exposing causal structure. If any premise can move while the conclusion stays rhetorically intact, the derivation may be decorative.
2. **Does it reach?** Would the insight apply in a domain you have not considered, and can you say which invariant carries it there? If yes, the mechanism is deeper than the original case. If no, the note may be context-fitted.
3. **Can it be criticized?** Is there a specific way the explanation could be wrong, not just incomplete? The [falsifier blocks] practice operationalizes this.
4. **Does observed fit discipline the explanation?** Local success is not second-class residue; it is evidence. If the explanation cannot account for where the pattern actually works, fails, or costs too much to maintain, it has verbal explanatory-reach without operational grip.

The first three tests map to the three depths in [discovery]: shared feature (adaptive), shared structure (partially explanatory), generative model (fully explanatory, with explanatory-reach). The fourth is not a depth — it holds an explanation at any depth accountable to the observed fit it must organize.

## Scope

Explanatory-reach is the quality goal for theoretical notes, not the only kind of KB value. Descriptions need economy, instructions need precision, and logs may preserve local observations before the mechanism is understood. The explanatory-reach filter says when an observation is ready to become a transferable claim; it does not replace the capture layer that supplies the observations.

## Open Questions

- Where in the KB are notes that are well-formed but merely adaptive? Those are candidates for deepening.
- Which first-principles derivations currently rule out a rival practice, and which only explain an already-preferred practice after the fact?
- Should this note keep a direct Deutsch source, or is the adapted distinction enough if the KB-specific test stands on its own?

---

Relevant Notes:


Derived into:

- [review-explanatory-reach] — the four-part negative test restated as a recurring review procedure
- [COLLECTION.md] — the four-part negative test condensed into the "Tests for explanatory-reach" authoring block

## Under-review context phrase

the negative test (predict where it fails) is the boundary test this note applies to memory formation
