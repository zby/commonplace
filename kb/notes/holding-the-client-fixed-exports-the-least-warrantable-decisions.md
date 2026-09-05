---
description: "A fixed-client benchmark measures worker capability; it leaves broader closure untested when the client supplies internal production decisions, while ordinary user requirements and acceptance may remain external"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems, evaluation]
---

# A benchmark that holds the client fixed exports the least-warrantable decisions by design

A common capability target has the form: the system performs at least as well as a competent remote contractor given the same brief, the same repository, the same tools and permissions, and the same feedback. The comparison is controlled by construction. To make the two workers comparable, the benchmark must hold constant everything that is not the worker — and what is not the worker is the **client**: the party that chooses the task, writes the brief, answers questions while the work runs, and accepts or rejects the result.

The closure claim must first name which of those decisions belong inside its boundary. A benchmark that holds an internal design, diagnosis, or successor-selection decision with the client cannot establish computational closure over that decision. Such decisions can carry the unsettled criteria, missing premises, and weak checks that resist transfer, [since warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md).

The [software-house boundary](./definitions/software-house.md) permits users to supply requirements, domain facts, preferences, observed outcomes, and acceptance judgments about visible behaviour. Keeping those inputs human does not defeat an automated-software-house claim. A client asked to diagnose an implementation failure or choose an internal revision instead supplies production work. The stronger closure claim examined below includes those production decisions; it does not require eliminating ordinary user participation.

## The overlap is structural, not coincidental

Experimental control and transfer difficulty can select the same decisions for different reasons. A benchmark fixes the brief and feedback to compare workers under the same conditions. A production process may leave internal design or admission with the client because its criteria or checks are not adequate for computational supply, [since warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md). Where these overlap, the comparison holds the hardest residual decisions outside the worker being tested. Other fixed inputs, including user preferences and delivery format, need not be difficult or internal production decisions.

The task horizon adds a fourth export. A benchmark task ends at delivery, so decisions that would arise after delivery — whether the change was actually the right one, what it costs later, what should follow — fall outside the measured interval whatever their warrant status.

## A held-constant input is not a measured variable

The mechanism is plain once the roles are separated: a benchmark measures variation in what it varies, and whatever it supplies or holds fixed sits outside its measurement. Holding the client fixed makes the worker's capability measurable and makes the client's decisions unmeasurable in the same run.

Stated against the cut-set test, [where computationally directed self-improvement is a fixed-boundary reallocation](./computationally-directed-self-improvement-is-a-reallocation.md): a system that passes this benchmark has shown that a human worker is not required for the worker's decisions under the given brief. If the client supplies other internal production decisions, the run leaves that human dependency untested. When the client supplies only permitted user inputs, their continued presence is compatible with automation.

Reading the worker result as closure over untested internal production decisions is boundary export: the claim includes a decision that the experiment supplied from outside its measured worker. Writing down the boundary distinguishes that error from legitimate external requirements and feedback.

## Naming the cut is not a concession

The result survives the correction intact. "Can supply the worker's decisions at contractor quality, given a client who chooses the task, supplies missing premises on request, and accepts the result" is a strong, informative capability claim. Naming the cut does not weaken the finding; it states which proposition the finding supports.

A benchmark can be redesigned to vary some client decisions — an underspecified brief with no follow-up channel, a task chosen by the system from an open backlog, an acceptance test the system does not author. Each such change makes the benchmark measure a different proposition, and each requires a new oracle for the decision now being varied. That is the cost the fixed-client design avoids, and the reason the design is common.

## The same shape appears wherever a benchmark supplies an ingredient

The general rule is that what a benchmark supplies is what it does not measure. One reason to supply an ingredient is that the benchmark lacks an oracle for producing it. [Known-target discovery benchmarks show reachability, not discovery closure](./known-target-discovery-benchmarks-show-reachability-not-discovery.md) under a different supply: importing a known target manufactures the missing evaluator, so the benchmark measures whether the target is reachable from the ingredients and leaves problem selection and prospective triage outside the test. Fixing an internal client decision and fixing a discovery target can both make a bounded capability measurable while leaving the broader path untested.

The rule generalizes past benchmarks that name a human role at all. For any controlled comparison, the list of held-constant conditions is a list of decisions the comparison cannot speak to, and where those conditions carry the warrant-hard decisions, the comparison cannot speak to warrant. When the comparison is against a human role specifically, the surrounding roles it must fix are the place to look, because a role is defined against the roles adjacent to it.

## Scope

- The claim is about what the benchmark measures, not about whether it is worth running. A fixed-client comparison can be the most informative measurement available and still not be a closure result.
- A remaining human client defeats closure only over decisions the claim places inside the production boundary. Ordinary user requirements, domain facts, and acceptance of visible behaviour may remain external.
- The claim assumes the comparison is controlled. An uncontrolled field comparison does not hold the client fixed, and correspondingly supports a weaker inference about capability.
- "Hardest to warrant" is relative to the representations, settled criteria, and oracles available at the time, inheriting that relativity from the residue argument. An acceptance decision that gains an independent check stops being an export and becomes a candidate variable.
- The claim says nothing about the effort share of the exported decisions. A client role that occupies a small fraction of the hours can still carry the whole warrant question.
- The claim is about the benchmark's construction, not about the systems it scores. A scored system may well be able to take client decisions; this benchmark is simply not the evidence for it.

## Open Questions

- Whether partially varying the client yields a graded measure or just a harder version of the same fixed-client test. Removing the feedback channel varies one export; acceptance stays fixed, so it is unclear whether the resulting scores order systems on anything but brief-parsing.
- How to evaluate computational internal admission independently while keeping user acceptance about visible behaviour external. A human who supplies the internal admission decision preserves the dependency; a human who assesses outcomes without choosing the internal successor need not do so.
- Which client-supplied production decisions are already checkable and worth varying in a benchmark while permitted user inputs remain fixed.

---

Relevant Notes:

- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — grounds: explains why internal production decisions left with the client can concentrate the difficult residual work
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](./computationally-directed-self-improvement-is-a-reallocation.md) — grounds: the cut-set and contraction test against which a fixed-client benchmark result is shown to be silent
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: bounds warranted automation of internal admission under the declared criteria
- [Known-target discovery benchmarks show reachability, not discovery closure](./known-target-discovery-benchmarks-show-reachability-not-discovery.md) — contrasts: the same supply-then-score construction with the evaluator imported instead of the client held fixed
- [The augmentation-automation boundary is discrimination not accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — contrasts: when the client supplies internal per-instance discrimination, worker capability does not establish automation of that broader production path
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — contrasts: why a single human-role comparison does not supply the commensurable grain that cross-system autonomy claims need
