---
description: "Four 2026 self-improving-agent systems read against search, evaluation, and retention: an absent function is bounded engineering, a function frozen outside the update space is not, and reported gains cannot separate the two"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [foundations, self-improving-systems, deploy-time-learning]
---

# An omitted improvement-loop function and a frozen one need different repairs

When a [proposal-selection improvement loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) underdelivers, the useful first question is which of search, evaluation, and operative retention is doing no work — and then which of two things is wrong with it.

A function is **omitted** when nothing in the loop performs it. An edit that becomes operative with nothing that could have refused it has no evaluation, however carefully it was proposed.

A function is **frozen** when something performs it, but that something sits outside the loop's [effective update space](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — a fixed acceptance rule, a human generalization judgment, a declared edit surface. The loop closes; it cannot revise how it closes. (The word is overloaded in this KB — frozen weights, a frozen tool loop, a frozen taxonomy. Here it means only this: outside the update space of the loop under discussion.) A frozen function is the loop-anatomy view of a human decision [deferred rather than removed](./computationally-directed-self-improvement-is-a-reallocation.md): externalized into an artifact the pathway consumes but cannot revise.

The two diagnoses are worth separating because their repairs are not the same kind of work. Adding an omitted function is bounded engineering: write the gate, write the retirement operation, and the loop has a part it lacked. Unfreezing a function is not, because whatever criterion governs the lift is itself fixed one level up — the open question left standing at the end of [learning inside a fixed decomposition](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Some functions should stay frozen: [machinery persists by warrant, not position](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md), which also argues that what stays permanently external is a function class rather than a component class — the objective, the standing commitments, the adoption *no*. A frozen acceptance rule may therefore be the warranted kernel rather than the defect. Frozen names where a component sits; it does not by itself convict.

What makes the distinction load-bearing rather than pedantic is that **a reported improvement cannot separate them**. Both systems improve inside their compound configuration, and both leave the neighbouring function untested by the result. Reading the update space is the only way to tell, which is why the readings below are drawn from what each paper declares editable rather than from its headline numbers.

## Four 2026 systems, read against the three functions

| System | Search | Evaluation | Operative retention |
|---|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) | computational — the same model mines failure signatures and proposes several bounded harness edits | present and reject-capable, **frozen**: a fixed two-split pass-count rule, whose "held-out" split the gate consults repeatedly | merged edits become operative; no retirement operation reported |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) | computational — a Refiner reads recent trajectory windows and edits prompt, sub-agents, skills, memory | **omitted**: edits take effect on the next step with no candidate comparison, regression gate, or rollback rule | present but unmanaged — memory is written far more often than it is read, and most authored skills are never used |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) | computational — typed Reflect/Select/Improve operators over registered resources | present and typed, **frozen**: Evaluate can reject, but objective, acceptance rule, and the learnability mask that says what is editable are protocol state the loop does not set | strongest of the four — versioned commit, lineage, rollback |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) | human — an accepted code-review comment is the candidate | **frozen at the instance level**: an engineer judges one accepted correction generalizable, and [an accepted edit verifies the change, not the rule](./an-accepted-edit-verifies-the-change-not-the-rule.md) | append-only always-loaded file, with an admitted rule conflict and acknowledged future saturation |

Three readings follow from the table.

**The strongest function is the one the paper is about.** Self-Harness contributes same-model proposal and its search is the most developed part; Autogenesis contributes a protocol and its retention layer is the most developed; Accumulated Behavioral Rules contributes a substrate for retained rules and says least about testing them. This is what one should expect of a research contribution, and it is exactly why the neighbouring function is where the placeholder sits.

**Evaluation is where the placeholders cluster.** Three of the four have a gate that cannot be revised by the loop it governs, and the fourth has no gate at all. None of the four searches over its own acceptance criterion. That may be the right design — the adoption *no* is a plausible member of the permanently external function class — but none of the four argues for it, so in each case the placement is inherited rather than defended. Autogenesis makes the boundary unusually legible rather than unusually bad: the learnability mask is inspectable protocol state, so what was editable can be read off instead of inferred. Version lineage and rollback establish that a rejected state is recoverable; they establish nothing about whether the accepting oracle was any good, and [warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) rather than by the reversibility of the commit.

**Retirement is absent from all four, and the three-function decomposition has no slot for it.** Continual Harness's create-and-forget tail and the always-loaded rules file are the same failure seen from two substrates: retained material accumulates, and nothing removes it. The decomposition asks whether an accepted change becomes operative, not whether an operative change can stop being one — the lifecycle operations catalogued in [retire, redact, supersede, relax](./agent-memory-requirements/retire-redact-supersede-relax.md) have no home in it. This is a gap in the model, not just a gap in the systems, and it is left open below rather than patched by asserting a fourth function.

## Scope

- These are readings of published descriptions, taken through this KB's ingest reports rather than from code. Autogenesis has released code that has not been inspected here; the other three have not been independently reproduced. A code-grounded audit could move any cell.
- **"Omitted" is relative to the described loop, not to the deployed system.** A paper may not report a gate it runs. The diagnosis says what the published account establishes, which is the same standard applied to the benchmark numbers.
- The four sit in one research neighbourhood — 2026, mostly fixed-weight editing of readable harness or rule artifacts, one of them observational production data. The table shows that the omitted/frozen distinction does work on real cases; it is not a survey and supports no claim about the field's distribution.
- Search, evaluation, and retention are a diagnostic model offered in the spirit of a reference architecture, not a derived-complete list of loop functions — and [whether a coarse function list can serve as a cross-system ontology at all is still open](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md). The retirement finding is direct evidence that this particular list is incomplete. **This note is therefore not a first-principles map of improvement-loop functions**; it is four readings against a provisional list, and its contribution to such a map is the omitted/frozen axis plus one function the map will have to place.

## Open Questions

- Is retirement a fourth loop function, a second requirement inside operative retention, or a property of the retained artifact's lifecycle that sits outside the loop entirely? All four systems fail it; none of them distinguishes these.
- Is there a system in this neighbourhood whose acceptance criterion is inside its own update space, and what stops the resulting regress from being vacuous?
- Does the omitted/frozen distinction survive on direct-update pathways, where there is no candidate to reject? A gradient learner's loss function is frozen in exactly this sense, but nothing there is omitted.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: supplies the three functions these readings diagnose, and the criterion that makes an unconditional trigger not an evaluator
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: the effective-update-space notion that "frozen" names, and why improvement inside a boundary does not test the boundary
- [Revising an improvement objective is licensed from outside it or is not improvement](./revising-an-improvement-objective-is-licensed-from-outside-it.md) — grounds: the level argument behind "fixed one level up" — the criterion governing an unfreeze cannot come from inside the function being unfrozen
- [Machinery persists by warrant, not position, in a reflective loop](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) — extends: which frozen components should be lifted and which have earned their place
- [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — contrasts: a weak evidence surface degrades a function that is present, which is a third diagnosis alongside omitted and frozen
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — mechanism: why a frozen or omitted gate costs more than a weak generator
- [Real self-improving systems occupy combinations no single rung captures](./real-self-improving-systems-occupy-combinations-no-rung-captures.md) — contrasts: profiles cases on reflection, cumulativity, and allocation; this note cuts the same kind of casebook by per-function gap instead
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — contrasts: the one placement whose acceptance machinery sits inside its own update space, at the declared cost of unreachable unprovable changes — but a theoretical construction, never run; the [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) is a declared departure from it, not an implementation — it relaxes the proof requirement to a viability filter at acceptance and demotes benchmark score to a search signal
- [Retire, redact, supersede, relax](./agent-memory-requirements/retire-redact-supersede-relax.md) — extends: the lifecycle operations all four systems lack and the decomposition has no slot for
- [Computationally directed self-improvement is a fixed-boundary reallocation](./computationally-directed-self-improvement-is-a-reallocation.md) — grounds: supplies "deferred rather than removed" — the externalized human decision a pathway cannot revise, which "frozen" names from inside the loop anatomy
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — extends: parks the prior question of whether a coarse function list can be a cross-system ontology, which these readings assume and do not settle
- [Readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — see-also: the shared substrate that makes all four loops inspectable enough to diagnose this way
- [Ingest: Huxley-Gödel Machine](../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) — evidenced-by: the name-borrowing lineage substitutes a benchmark estimate for the utility proof, and shows the immediate benchmark score is a weak selection signal even where the gate is frozen on it
- [Ingest: Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) — abstracted-from: the frozen-gate reading, including the repeatedly consulted "held-out" split
- [Ingest: Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) — abstracted-from: the omitted-evaluation reading and the create-and-forget retention tail
- [Ingest: Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) — abstracted-from: the learnability mask as inspectable frozen boundary, and rollback as reversibility without semantic safety
- [Ingest: Self-Improving AI Coding Agents Through Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) — abstracted-from: the instance-level frozen gate and the monotonic always-loaded rule file
