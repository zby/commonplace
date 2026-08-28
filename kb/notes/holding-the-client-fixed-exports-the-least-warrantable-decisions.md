---
description: "Why a 'matches a competent remote contractor given the same brief, tools, and feedback' comparison measures capability under a fixed client role rather than closure: the decisions it holds constant are the warrant-hard residue"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems, evaluation]
---

# A benchmark that holds the client fixed exports the least-warrantable decisions by design

A common capability target has the form: the system performs at least as well as a competent remote contractor given the same brief, the same repository, the same tools and permissions, and the same feedback. The comparison is controlled by construction. To make the two workers comparable, the benchmark must hold constant everything that is not the worker — and what is not the worker is the **client**: the party that chooses the task, writes the brief, answers questions while the work runs, and accepts or rejects the result.

Those are the decisions that resist warranted transfer. Task choice and acceptance land on the unsettled-criterion and no-independent-check rows of the residue, [since warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md); mid-task feedback supplies premises that were not represented where the worker could read them. A benchmark of this form therefore fixes, as its control, the same decisions that a self-improvement claim would have to discharge.

## The overlap is structural, not coincidental

Two different reasons pick out the same set, and they pick it out for a shared cause. The experimental reason is control: a comparison is fair only when both workers face the same demand and the same acceptance test. The warrant reason is that goal-setting and acceptance are the decisions the worker has no independent standard of its own to settle, [since warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md). The warrant-carrying part of the client role — choosing the task and accepting the result — is made of decisions the worker has no independent standard to settle; other client decisions, such as delivery format or scheduling, are settleable and are held fixed for control alone. So the roles a controlled comparison must externalize and the decisions that are hardest to warrant are drawn from the same well.

The task horizon adds a fourth export. A benchmark task ends at delivery, so decisions that would arise after delivery — whether the change was actually the right one, what it costs later, what should follow — fall outside the measured interval whatever their warrant status.

## A held-constant input is not a measured variable

The mechanism is plain once the roles are separated: a benchmark measures variation in what it varies, and whatever it supplies or holds fixed sits outside its measurement. Holding the client fixed makes the worker's capability measurable and makes the client's decisions unmeasurable in the same run.

Stated against the cut-set test, [where computationally directed self-improvement is a fixed-boundary reallocation](./computationally-directed-self-improvement-is-a-reallocation.md): a system that passes this benchmark has shown that a human worker is not required for the worker's decisions under the given brief. It has not shown that the human client is out of the cut set, because the run was constructed with the client in it. Passing is compatible with the client remaining indispensable; the design presupposes that they are present.

Reading such a result as closure over a pathway is therefore the degenerate move in which the hard decision is supplied from outside the declared path — boundary export. It produces apparent warrant precisely where warrant is missing, and writing the cut down is what makes the error easy to see.

## Naming the cut is not a concession

The result survives the correction intact. "Can supply the worker's decisions at contractor quality, given a client who chooses the task, supplies missing premises on request, and accepts the result" is a strong, informative capability claim. Naming the cut does not weaken the finding; it states which proposition the finding supports.

A benchmark can be redesigned to vary some client decisions — an underspecified brief with no follow-up channel, a task chosen by the system from an open backlog, an acceptance test the system does not author. Each such change makes the benchmark measure a different proposition, and each requires a new oracle for the decision now being varied. That is the cost the fixed-client design avoids, and the reason the design is common.

## The same shape appears wherever a benchmark supplies an ingredient

The general rule is that what a benchmark supplies is what it does not measure, and a benchmark supplies an ingredient when it cannot score it — which is to say, when the ingredient has no cheap oracle. [Known-target discovery benchmarks show reachability, not discovery closure](./known-target-discovery-benchmarks-show-reachability-not-discovery.md) for the same reason under a different supply: importing a known target manufactures the missing evaluator, so the benchmark measures whether the target is reachable from the ingredients and leaves problem selection and prospective triage outside the test. Fixing the client and fixing the target are two instances of one construction — supply the decision you cannot score, then read the residual score as capability.

The rule generalizes past benchmarks that name a human role at all. For any controlled comparison, the list of held-constant conditions is a list of decisions the comparison cannot speak to, and where those conditions carry the warrant-hard decisions, the comparison cannot speak to warrant. When the comparison is against a human role specifically, the surrounding roles it must fix are the place to look, because a role is defined against the roles adjacent to it.

## Scope

- The claim is about what the benchmark measures, not about whether it is worth running. A fixed-client comparison can be the most informative measurement available and still not be a closure result.
- The claim assumes the comparison is controlled. An uncontrolled field comparison does not hold the client fixed, and correspondingly supports a weaker inference about capability.
- "Hardest to warrant" is relative to the representations, settled criteria, and oracles available at the time, inheriting that relativity from the residue argument. An acceptance decision that gains an independent check stops being an export and becomes a candidate variable.
- The claim says nothing about the effort share of the exported decisions. A client role that occupies a small fraction of the hours can still carry the whole warrant question.
- The claim is about the benchmark's construction, not about the systems it scores. A scored system may well be able to take client decisions; this benchmark is simply not the evidence for it.

## Open Questions

- Whether partially varying the client yields a graded measure or just a harder version of the same fixed-client test. Removing the feedback channel varies one export; acceptance stays fixed, so it is unclear whether the resulting scores order systems on anything but brief-parsing.
- Whether acceptance can be varied without either a captured evaluator or a human acceptor. Letting the system judge its own delivery reintroduces self-confirmation; keeping a human judge preserves the export. Whether a third construction exists is the load-bearing open question for closure benchmarks.
- Whether every client decision is warrant-hard. If some are checkable, a benchmark could vary those and claim partial closure over a named subset, which would be a more useful result than either extreme.

---

Relevant Notes:

- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — grounds: supplies the residue classification that identifies the exported client decisions as the warrant-hard ones, and names boundary export as a degenerate closure move
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](./computationally-directed-self-improvement-is-a-reallocation.md) — grounds: the cut-set and contraction test against which a fixed-client benchmark result is shown to be silent
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: why acceptance is the decision no worker-internal oracle can settle, which is what makes the client a separate role
- [Known-target discovery benchmarks show reachability, not discovery closure](./known-target-discovery-benchmarks-show-reachability-not-discovery.md) — contrasts: the same supply-then-score construction with the evaluator imported instead of the client held fixed
- [The augmentation-automation boundary is discrimination not accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — contrasts: a fixed-client benchmark leaves the human as the per-instance discriminator, so a passing aggregate score is an augmentation result rather than an automation one
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — contrasts: why a single human-role comparison does not supply the commensurable grain that cross-system autonomy claims need
