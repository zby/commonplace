---
description: "Tool usefulness, computational autonomy, warrant, and system power move independently in a human-agent system, so a progress claim has to say which one moved and autonomy gains do not license power claims"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [foundations, self-improving-systems]
---

# Tool usefulness, computational autonomy, warrant, and system power are separate dimensions

A human–agent system can be described along at least four properties. A change that moves one of them does not thereby move the others, and a reading on one does not fix a reading on the rest.

- **Tool usefulness** — how well the human–agent composite performs its declared function for its operators, counting what the operators must supply. It is read against a declared function, [since self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md).
- **Computational autonomy** — how much of a declared path runs without a person. This is an allocation reading over named functions against a declared boundary, [since methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md).
- **Warrant** — whether what runs unattended can be trusted, [bounded by the domain the available oracles can assess](./warranted-autonomy-is-bounded-by-oracle-domain.md).
- **System power** — which consequential tasks the system can perform, at what quality and breadth, judged by external evaluation of outcomes rather than by who performed which step.

Each is asked of the same system, and each asks a different question: how well it serves, who does the work, whether the unattended part can be trusted, and what it can do at all.

## Pairs that come apart

The separation is shown by cases where one property is high and a neighbouring one is low.

| Case | High on | Low on |
|---|---|---|
| An acceptance gate handed to an unattended model with a rubric | autonomy | warrant |
| A debugger or a compiler a person drives step by step | usefulness | autonomy |
| A strong model whose every consequential action waits for human approval | power | autonomy |
| A capable system whose operators must supply heavy setup, prompting, and review | power | usefulness |
| A transfer that leaves a person only the calls no oracle can check | autonomy | usefulness |

**Autonomy without warrant.** Bare autonomy is free: removing the person from a gate takes one decision, and the gate then runs unattended whether or not anything can check what it accepts. Warranted autonomy is the constrained quantity, because [it extends only to the candidates an oracle can assess at the required confidence](./warranted-autonomy-is-bounded-by-oracle-domain.md). The two move together only when the oracle keeps up.

**Usefulness without autonomy.** A tool that a person drives at every step can still perform its declared function very well for its operators. Nothing in the usefulness reading rewards the person's absence; it rewards the outcome the operators get for what they supply.

**Power without autonomy.** Capability and allocation are set by different things. A system built around a strong model can reach consequential outcomes while a person approves each one, and moving that approval inside the boundary changes who decides without, by itself, changing what the composite can reach.

**Power without usefulness.** A system that can in principle do hard work may still cost its operators more setup, correction, and review than the work is worth to them. Usefulness prices what the operators supply; power does not.

**Autonomy against usefulness.** Raising autonomy can lower usefulness later. When a system preferentially moves the checkable decisions out, [the residue left with people is harder to warrant per decision](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md), and the person also loses the contact with routine cases that used to inform those calls. Human hours need not fall either, because [freed attention tends to move to the next frontier](./increasing-computational-autonomy-relocates-human-effort.md).

## Autonomy does not entail power

The denial worth stating separately is the one from autonomy to power. Autonomy is defined over the allocation of steps on a declared path; power is defined over externally evaluated outcomes. Reassigning a step from a person to a computational actor changes the allocation and leaves the reachable outcome set undetermined until it is measured.

The Bitter Lesson is the usual reason to expect a power gain anyway. Its axis is production method — hand-crafted content versus content produced by scalable search and learning — rather than either representational form or actor allocation, [as the production-method reading sets out](./the-bitter-lesson-selects-production-methods-not-representational.md). Read that way it motivates a conjecture: replacing hand-designed selection with scalable search and learning may raise what the system can achieve. That is an empirical conjecture, and supporting it takes a comparison holding the objective and regime fixed across the two methods, [since a scaling loss or win identifies a cause only when the rival explanations are ruled out](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) and [an experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md). The allocation reading of autonomy does not supply that conclusion by itself.

## A progress claim has to name its dimension

The practical consequence is a reporting rule. A claim of progress should say which dimension moved and on what evidence, because the four have different evidence types: usefulness needs the operators' function and cost, autonomy needs an allocation record against a declared path, warrant needs the oracle and its domain, and power needs an external outcome comparison.

The common error is moving one dimension and reporting it as another. Handing a gate to a model and reporting a capability gain reports autonomy as power. Reporting an autonomy transfer as a usefulness gain skips the effort the transfer displaced into review and repair. Reporting an unattended run as a trusted one reports autonomy as warrant. Naming the dimension makes each of these checkable rather than rhetorical.

## Scope

- The four are not claimed exhaustive. Other properties of a human–agent system — cost, latency, horizon, breadth of reachable artifacts — may deserve their own coordinates, and finer decompositions of these four are possible. What the note fixes is that these four do not reduce to one another.
- Separability is a claim about entailment, not about correlation. The four can move together in practice; better oracles often raise warrant and autonomy at once. The claim is that observing a move on one does not license inferring a move on another.
- Each dimension is read against a declared boundary and a declared function. Two readings taken against different boundaries are not comparable, and moving the boundary can change a reading without changing the system.
- The measures on each dimension are separately hard, and this note does not supply them. Autonomy in particular lacks a commensurable decomposition, [since measuring it well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md); usefulness and power both need outcome measures that do not collapse into activity counts or self-scored prose.

## Open Questions

- Whether power and tool usefulness stay distinct once operator effort is priced into the outcome measure, or whether a sufficiently complete usefulness measure absorbs power as a special case at zero operator burden.
- Whether the four dimensions admit any general ordering rule — a way to say that a change is forward overall — or only a partial order in which changes that trade one dimension against another stay incomparable without an explicit objective.
- Whether the misreporting error can be detected from a repository's own change record, by checking whether claimed gains name a dimension and cite its evidence type.

---

Relevant Notes:

- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: separates bare autonomy from the warrant that makes an unattended gate trustworthy
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](./increasing-computational-autonomy-relocates-human-effort.md) — grounds: why an autonomy gain need not appear as a usefulness gain in human hours
- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — mechanism: how raising autonomy can lower the quality of the human judgments that remain
- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — grounds: the actor-allocation reading this note uses for computational autonomy
- [Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md) — grounds: why tool usefulness is read against a declared function rather than in the abstract
- [The bitter lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md) — grounds: the lesson's axis is how content is produced, which is neither an autonomy claim nor a power theorem
- [Unsupported proxy scope may explain a structured method's loss under scaling](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) — grounds: the conditions a scaling comparison must meet before it supports a causal reading
- [An experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md) — enables: the matched-comparison discipline a power claim needs
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — extends: the unsolved measurement problem on one of the four dimensions
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](./computationally-directed-self-improvement-is-a-reallocation.md) — contrasts: the contraction test reads the autonomy dimension alone and leaves the other three open
