---
description: "Five proposal-selection systems expose frozen functions, while a direct-update contrast shows why absence of a gate is not omission; HyperAgents supplies a preliminary partial unfreezing"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [foundations, self-improving-systems, deploy-time-learning]
---

# An omitted improvement-loop function and a frozen one need different repairs

When a [proposal-selection improvement loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) underdelivers, the useful first question is which of search, evaluation, and operative retention is doing no work — and then which of two things is wrong with it.

The architecture-neutral causal obligations belong to the [self-improving-system definition](./definitions/self-improving-system.md). Failure there is a missing or unestablished causal link. **Omitted** is narrower: a function is omitted only relative to an architecture that requires it. In a proposal-selection pathway, an accepted patch that is never installed omits operative retention. A direct update exposes no separate candidate–adoption decision, so adding a reject-capable gate would introduce proposal selection rather than fill an omitted universal function.

A function is **frozen** when its implementation or governing rule sits outside
the loop's [effective update
space](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — for
example, a fixed computational acceptance rule, a fixed human procedure, or a
declared edit surface. The loop can perform the function but cannot revise how
that function is performed. (The word is overloaded in this KB — frozen
weights, a frozen tool loop, a frozen taxonomy. Here it means only this:
outside the update space of the loop under discussion.) Frozen therefore names
update placement, not provenance or actor allocation. A human-authored rule
executed by computation is still computationally allocated; a person is a
current cut set only when an in-scope transition requires that person.

The two diagnoses are worth separating because their repairs are not the same
kind of work. Adding an omitted required function is bounded engineering:
connect an accepted proposal to a live authority path, for example, and the
loop gains the operative retention it lacked. Unfreezing a function changes the
update architecture, because whatever criterion governs the lift is itself
fixed one level up — the open question left standing at the end of [learning
inside a fixed decomposition](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).
Some functions should stay frozen because [machinery persists by warrant, not
position](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).
Objectives, commitments, authority boundaries, fixed general learning methods,
exact interfaces, and trusted kernels may all remain outside a particular
update space. A frozen acceptance rule may therefore be the warranted kernel
rather than the defect. Frozen names where a component sits; it does not by
itself convict. If the component instead embeds family-specific specialization
that people must redesign as claimed reach widens, it limits [domain
extensibility](./definitions/domain-extensible-software-factory.md), not because
all fixed machinery is forbidden but because the required specialization stays
human supplied.

When a freeze is defended rather than merely inherited, the defences split: a
**protective** freeze keeps the component outside the loop to resist a named
failure, such as objective hacking; an **affordable** freeze is a resource
compromise, liftable in principle. Lifting them costs different things — a
protective freeze needs a replacement defence, an affordable one only budget.

What makes the distinction load-bearing rather than pedantic is that **a reported improvement cannot separate them**. Headline gains cannot establish whether a required function is absent, present but frozen, or not required by the chosen architecture. Classifying the update architecture and then reading its effective update space is the only way to tell, which is why the readings below are drawn from what each paper declares editable rather than from its headline numbers.

## Five proposal-selection systems and one direct-update contrast

The [six-path evidence inventory](./evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) owns the underlying causal-path qualifications and supplied-machinery inventory. This table keeps the distinct update-architecture and lifecycle reading.

| System | Architecture and update determination | Evaluation in proposal selection | Operativity and lifecycle evidence |
|---|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) | **Proposal selection** — the same model mines failure signatures and proposes several bounded harness edits. | Present and reject-capable, **frozen**: a fixed two-split pass-count rule, whose "held-out" split the gate consults repeatedly. | Gate-passing edits are merged and exercised in later harness evaluations; no criterion-driven retirement path is reported ([Self-Harness lifecycle (snapshot required)](../sources/self-harness-harnesses-that-improve-themselves.ingest.md)). |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) | **Direct update** — a Refiner reads recent trajectory windows and directly determines edits to prompts, sub-agents, skills, and memory. | Not a separate role in this architecture: no independently rejectable candidate is exposed. | Edits enter the next step; prompt and harness changes are exercised, while memory reuse is sparse and most authored skills are unused. Limited deletion and demotion do not establish a system-wide retirement path ([Continual Harness lifecycle (snapshot required)](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md)). |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) | **Proposal selection** — typed Reflect/Select/Improve operators act over registered resources. | Present and typed, **frozen**: Evaluate can reject, but the objective, acceptance rule, and learnability mask are protocol state the loop does not set. | Versioned commit, lineage, and rollback supply the strongest lifecycle controls in this cohort; rollback is not retirement ([Autogenesis lifecycle (snapshot required)](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md)). |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) | **Proposal selection** — an engineer generalizes an accepted code-review comment into a candidate rule. | **Frozen at the instance level**: an engineer judges the correction generalizable, and [an accepted edit verifies the change, not the rule](./an-accepted-edit-verifies-the-change-not-the-rule.md). | The paper reports loading across two interfaces and no recurrence over 74 post-rule exposures, without a control isolating causal uptake. The file is append-friendly and rules are refined; removal is described inconsistently as rare and as prohibited. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) | **Proposal selection** — a fixed external model reads an archive agent's logs and proposes a descendant edit; benchmark score steers parent sampling. | Present as a **frozen** viability filter: children that compile and retain code-editing ability are admitted even when benchmark score regresses. | The archive is monotonic **by design** — the greedy variant drops from 50.0% to 39.7%, so non-retirement is part of the search mechanism. |
| [HyperAgents](../sources/hyperagents.ingest.md) | **Proposal selection** — a selected hyperagent rewrites the unified task/meta-agent program that generates later descendants. | Present and **frozen in the main experiments**: fixed viability checks, evaluators, and a handcrafted parent selector govern eligibility, scoring, and later use. An appendix makes parent selection editable, but not evaluation or the outer archive loop. | Selected patch lineages are replayed into later generations. Archive lineage preserves variants; no system-wide semantic retirement path is reported ([HyperAgents lifecycle (snapshot required)](../sources/hyperagents.ingest.md)). |

Three readings follow from the table.

**Classify the update architecture before diagnosing omission.** The row-level source routes above, together with the linked [six-path evidence inventory](./evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md), establish the exclusion system by system. Self-Harness, Autogenesis, Accumulated Behavioral Rules, the Darwin Gödel Machine, and HyperAgents each expose a candidate, a reject-capable gate, and later operativity, so their reported limit is a frozen criterion or lifecycle boundary rather than an absent required proposal-selection function. Continual Harness directly determines its successor, so its absent rejection stage is architectural, not an omission; its evidential limits lie in the fixed evidence-to-edit machinery and uneven evidence that individual retained artifacts affect later behavior. On those six readings, this cohort supplies no clean omitted-function example. Omission remains a valid diagnosis within proposal selection, but it is not instantiated here.

**Evaluation is frozen in the five proposal-selection cases.** Each has reject-capable admission or acceptance machinery outside the update space it governs; none searches over its own acceptance criterion. Continual Harness instead holds its evidence-to-edit rule and surrounding decomposition fixed, but has no evaluator to freeze. The papers justify these placements unevenly. The Darwin Gödel Machine separately hides a hallucination evaluator because objective hacking “occurs more frequently when these functions are not hidden” ([Darwin Gödel Machine, Appendix H](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md), verbatim), and freezes its exploration controller as an affordable compute compromise, a choice “made due to limited computational budget” ([Darwin Gödel Machine, Appendix J](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md), verbatim); neither defence establishes that its ordinary viability gate should remain fixed. Accumulated Behavioral Rules argues for human validation because authoritative bad rules amplify errors, but its data do not validate the engineer's generalization judgment. Self-Harness and Autogenesis do not separately defend why their gates remain outside the update space. Autogenesis at least makes the boundary unusually legible: its learnability mask exposes what is editable. HyperAgents supplies the sharpest partial unfreezing elsewhere: its main experiments also keep parent selection fixed, while an appendix installs evolving parent-selection code that governs later iterations. This moves search allocation rather than the acceptance criterion. The learned selector does not significantly beat random selection and remains below the handcrafted selector, so bringing a function inside the update space demonstrates operative reach without demonstrating a better function. Version lineage and rollback establish recoverability, not whether the accepting oracle was sound, because [warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md), not by commit reversibility.

**None of the six descriptions establishes a system-wide, criterion-driven retirement path across all retained artifact types.** Continual Harness reports limited deletion and demotion, while Accumulated Behavioral Rules supports in-place refinement and describes removal inconsistently: rules are “added and occasionally refined but rarely removed” ([Accumulated Behavioral Rules, Section II-A](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md), verbatim) in one section and “added and refined but not removed” ([Accumulated Behavioral Rules, Section VII](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md), verbatim) in another. The Darwin Gödel Machine and HyperAgents deliberately retain archive lineages because discarding apparently bad agents can foreclose stepping stones. Retirement is therefore an unresolved lifecycle placement, not a universally omitted stage of one improvement episode. The proposal-selection decomposition asks whether an accepted change becomes operative, not whether an operative change can later stop being one; it has no settled place for the operations catalogued in [retire, redact, supersede, relax](./agent-memory-requirements/retire-redact-supersede-relax.md).

## Scope

- These are readings of published descriptions, taken through this KB's ingest reports rather than from code. Code-grounded reviews exist for [Autogenesis](../agentic-systems/autogenesis.md) and [HyperAgents](../agent-memory-systems/reviews/hyperagents.md); the Darwin Gödel Machine code has not been inspected here, and the remaining three systems have not been independently reproduced. A code-grounded audit could move any cell.
- **"Omitted" applies only after the architecture has been classified.** Within a reported proposal-selection loop, omission means that the published account establishes no implementation of a required role. A direct pathway does not omit evaluation merely because it has no rejection stage.
- The six sit in one research neighbourhood — 2025–26, mostly fixed-weight editing of readable harness, rule, or scaffold artifacts, one of them observational production data. The five proposal-selection rows instantiate frozen evaluation, while Continual Harness supplies an architecture-boundary contrast; the sample contains no empirical omitted-function case and supports no claim about the field's distribution.
- Search, evaluation, and operative retention describe proposal selection, not the universal anatomy of self-improvement. The architecture-neutral obligations belong to [self-improving system](./definitions/self-improving-system.md): a direct pathway can freeze its update rule or fail a general causal link, but it does not omit an evaluator it never required. Retirement remains a separate lifecycle-placement question, and [whether any coarse function list can serve as a cross-system ontology is still open](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md).

## Open Questions

- Is retirement a fourth loop function, a second requirement inside operative retention, or a property of the retained artifact's lifecycle that sits outside the loop entirely?
- Is there a system in this neighbourhood whose acceptance criterion, rather than only its search or parent-selection policy, is inside its own update space, and what stops the resulting regress from being vacuous?

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: supplies the three functions these readings diagnose, and the criterion that makes an unconditional trigger not an evaluator
- [Self-improving system](./definitions/self-improving-system.md) — grounds: supplies the architecture-neutral causal anatomy and establishes why a direct update does not require a reject-capable gate
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: the effective-update-space notion that "frozen" names, and why improvement inside a boundary does not test the boundary
- [Revising an improvement objective is licensed from outside it or is not improvement](./revising-an-improvement-objective-is-licensed-from-outside-it.md) — grounds: the level argument behind "fixed one level up" — the criterion governing an unfreeze cannot come from inside the function being unfrozen
- [Machinery persists by warrant, not position, in a reflective loop](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) — extends: which frozen components should be lifted and which have earned their place
- [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — contrasts: a weak evidence surface degrades a function that is present, which is a third diagnosis alongside omitted and frozen
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — mechanism: why a frozen or omitted gate costs more than a weak generator
- [Real self-improving systems occupy combinations no single rung captures](./evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) — contrasts: profiles cases on reflection, cumulativity, and allocation; this note distinguishes the direct-update boundary from frozen functions within proposal selection
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — contrasts: the one placement whose acceptance machinery sits inside its own update space, at the declared cost of unreachable unprovable changes — but a theoretical construction, never run; the [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) is a declared departure from it, not an implementation — it relaxes the proof requirement to a viability filter at acceptance and demotes benchmark score to a search signal
- [Retire, redact, supersede, relax](./agent-memory-requirements/retire-redact-supersede-relax.md) — extends: the lifecycle operations for which none of the six establishes a system-wide, criterion-driven path across all retained artifact types
- [Computationally directed self-improvement is a fixed-boundary reallocation](./computationally-directed-self-improvement-is-a-reallocation.md) — grounds: separates current human necessity from human provenance and placement outside the update surface
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — extends: parks the prior question of whether a coarse function list can be a cross-system ontology, which these readings assume and do not settle
- [Readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — see-also: the shared substrate that makes all six paths inspectable enough to diagnose this way
- [Ingest: Huxley-Gödel Machine (snapshot required)](../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) — evidenced-by: the name-borrowing lineage substitutes a benchmark estimate for the utility proof, and shows the immediate benchmark score is a weak selection signal even where the gate is frozen on it
- [Ingest: Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) — abstracted-from: the frozen-gate reading, including the repeatedly consulted "held-out" split
- [Ingest: Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) — abstracted-from: the direct-update classification, next-step installation, uneven later artifact use, and limited lifecycle management
- [Ingest: Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) — abstracted-from: the learnability mask as inspectable frozen boundary, and rollback as reversibility without semantic safety
- [Ingest: Self-Improving AI Coding Agents Through Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) — abstracted-from: the instance-level frozen gate, reported loading and non-recurrence, and the append-friendly rule substrate with in-place refinement and unresolved removal policy
- [Ingest: Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) — abstracted-from: the fixed viability-filter acceptance, the separate protective and affordable freezes, and monotonic retention as mechanism rather than oversight
- [Ingest: HyperAgents](../sources/hyperagents.ingest.md) — abstracted-from: editable task/meta-agent code under a supplied outer process, the parent-selection appendix as partial unfreezing, and one cross-domain compounding contribution without established sustained compounding
