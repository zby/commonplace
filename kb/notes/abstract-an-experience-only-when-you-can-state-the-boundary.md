---
description: Abstract an episode into a lesson only when you can state its boundary, else preserve the instance; an over-generalized lesson is one that drops the condition clause
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, deploy-time-learning, failure-modes]
---

# Abstract an experience into a lesson only when you can state where the lesson stops

After an episode, an agent learning from experience faces a choice: distill what happened into a broad lesson, or keep the concrete instance. Compress too eagerly and you get an *over-generalized* lesson the agent then applies everywhere; compress too little and rare, situation-specific knowledge never compounds. The usual handles — frequency, confidence, recency — don't separate the two cases. The discriminator is whether the agent can state the lesson's **boundary**: the condition under which it holds, equivalently where it stops applying.

## The boundary clause is the reach test applied to memory formation

The KB already has the test in another guise. A genuine generalization [predicts where it fails — change the constraint, change the conclusion](./first-principles-reasoning-selects-for-explanatory-reach-over.md); a note that merely records "X works" is adaptive fit, brittle the moment the context shifts. Abstracting an experience is the same move under a deadline: [distillation](./definitions/distillation.md) [transforms a single trace into a rule by adding a condition clause and a rationale the trace never contained](./distillation-is-transformation-not-selection.md). The condition clause *is* the boundary.

So an **over-generalized lesson is an abstraction asserted without its condition clause** — adaptive fit wearing the surface of reach. The failure mode the question names — agents applying a lesson everywhere, never learning when to disengage — is not a tuning problem. It is the structural consequence of storing the rule while dropping the boundary that would tell the agent where to stop. The complement holds too: a [fact has low reach by design](./learning-is-not-only-about-generality.md), so it has no boundary to state and nothing to gain from abstraction. The decision is not "compress or not" but "can I name the scope; if not, keep the instance."

## Successes and failures supply boundaries asymmetrically

The sharpest reason to treat episodes differently by outcome is that successes and failures carry boundary information asymmetrically:

- A **success is an existence proof**: it shows the approach was *possible* here. It does not establish that the approach is *better than alternatives* across cases, so any lesson abstracted from it imports a boundary the agent has not earned. Preserve it as a concrete, replayable demonstration rather than a rule.
- A **failure carries a directive** — "what to change" — that names a violated constraint. That directive is a candidate boundary, which makes failures the natural raw material for lessons. (This echoes Popper: a refutation is more informative than a confirmation because it locates a limit.)

This predicts the finding of [SkillRL](../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.md) — a skill-augmented RL framework that preserves successful trajectories as demonstrations while synthesizing failures into concise lessons — that processing successful episodes as replayable demonstrations while distilling failures into abstracted lessons beats uniform compression of both. Uniform compression abstracts both kinds the same way, but the failures were the half where a boundary was already on hand; the loss concentrates on the successes, which get over-generalized into rules no boundary justifies.

## What supplies — or strips — the boundary

The same lens organizes the mechanisms the field has surfaced — each turns on whether inspectable failure evidence survives processing, [which is itself a first-class learning bottleneck](./diagnostic-richness-constrains-outer-loop-learning-quality.md):

- **Evaluative vs directive feedback.** Feedback splits into how-well-it-went (evaluative) and what-to-change (directive). The directive component carries the scope; a scalar reward keeps only the evaluative and discards exactly the part that would bound the lesson — which is why reward-only signals tend toward over-generalization.
- **Uncompressed reflection.** Reflexion (an agent framework that retries tasks guided by verbal self-reflection) keeps verbal self-diagnoses uncompressed because the boundary lives in the specifics; compress them and the condition clause goes with the detail, leaving a bare directive that over-applies. "Compress them and they stop helping" is the boundary being stripped.
- **Process over outcome verification.** Checking intermediate steps rather than final answers validates the *mechanism* — the *why* — which is what earns a lesson [explanatory reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) rather than coincidental fit. A lesson that survives process validation has an articulable basis, so its boundary is statable; an outcome-only pass cannot tell a real rule from a lucky one.
- **Granular, individually addressable skills.** Storing skills as discrete units refined by feedback (VOYAGER, an LLM agent that builds a reusable skill library) keeps each skill's applicability condition attached to it. Collapsing them into one unified policy erases the per-skill boundaries — over-generalization by merger.

## When you can't state the boundary, preserve the instance

The complement of the rule is a positive instruction, not a discard. A rare fact's worth is [its retrievability, not its transfer](./memory-management-policy-is-learnable-but-oracle-dependent.md): preserved verbatim and findable, it pays off in the narrow context it came from. And even after a lesson is distilled, the [source stays for the edge cases the distillate can't cover](./constraining-and-distillation-both-trade-generality-for-reliability.md) — which argues, with [the bias toward trace retention](./distillation-is-transformation-not-selection.md), for keeping the instance whenever the boundary is in doubt. Over-eager abstraction is the expensive error: a verbatim instance that turns out generalizable can be abstracted later, but an over-generalized lesson silently misfires until something forces the boundary into view.

## Scope

The discriminator says *when* abstraction preserves reach, not how an agent mechanically decides it — stating a boundary is itself a judgment, and whether a mined pattern [has reach or is just a recurring local patch remains an open problem](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) at the field level. The claim narrows the question rather than closing it: it says what the agent must be able to produce (a condition clause) for an abstraction to be trustworthy, and what to do (preserve the instance) when it can't.

Read as a criterion, boundary-statability sharpens the [validity gate that decides what is trustworthy enough to learn from](./choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md), and the abstraction step it governs is the "distil" operation whose [authority must be earned per operation rather than granted at capture](./trace-derived-memory-earns-authority-per-operation-not-at-capture.md) — the boundary test is the oracle that licenses the distilled rule.

## Sources

- [Inquiring line: "How can agents distinguish over-generalized lessons from genuinely useful long-tail knowledge?"](https://inquiringlines.com/inquiring-lines/how-can-agents-distinguish-over-generalized-lessons-from-genuinely-useful-long-t/) — poses the question and assembles the five mechanisms (SkillRL, Reflexion, feedback decomposition, process verification, VOYAGER) reorganized here under the boundary discriminator.
- [SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning](../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.md) — the differential-processing finding: successful trajectories preserved as demonstrations, failed ones synthesized into concise lessons, grounding the success/failure asymmetry directly rather than through the umbrella article.
- Karl Popper — refutations are more informative than confirmations; grounds the success/failure asymmetry.

---

Relevant Notes:

- [first-principles reasoning selects for explanatory reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: the negative test (predict where it fails) is the boundary test this note applies to memory formation
- [distillation is transformation, not selection](./distillation-is-transformation-not-selection.md) — mechanism: abstracting an episode adds the condition clause whose presence or absence this note keys on
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — extends: a fact is low-reach by design, so the abstract-or-preserve choice only bites where reach is plausibly on offer
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — evidence: a preserved fact's value is its retrievability, not its transfer — the long-tail half of the decision
- [constraining and distillation both trade generality for reliability, speed, and cost](./constraining-and-distillation-both-trade-generality-for-reliability.md) — extends: the distilled lesson keeps its source for the edge cases it can't cover
- [trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — see-also: the field marks "reach vs local patch" as open; this note offers a discriminator, not a closure
- [diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — grounds: that inspectable failure evidence carries the boundary the directive component supplies
- [choosing what to learn requires both validity and learning-value gates](./choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — extends: boundary-statability is a concrete criterion for that note's validity gate
- [trace-derived memory earns authority per operation, not at capture](./trace-derived-memory-earns-authority-per-operation-not-at-capture.md) — extends: abstracting an episode is the "distil" operation in that authority pipeline; the boundary test is its oracle
