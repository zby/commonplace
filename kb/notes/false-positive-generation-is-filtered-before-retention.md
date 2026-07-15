---
description: "False-positive generation faces evaluation before retention, while false-positive acceptance becomes operative and can compound"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# False-positive generation is filtered; false-positive acceptance becomes operative

In a [proposal-selection improvement loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md), search and evaluation fail in ways that are not symmetric, and the asymmetry is structural rather than incidental.

Search sits *upstream of a filter*. A bad candidate — useless, harmful, off-target — reaches evaluation and is rejected. It cost effort and nothing else; it never became operative.

Evaluation *is* the filter. A bad acceptance is not caught by anything downstream, because retention is not a filter — retention is the machinery that makes the change stick. The accepted artifact acquires a consumer, a channel, and a force, and starts shaping behavior.

> Only the last filter's errors survive.

## What the claim covers, and what it does not

The asymmetry is between the two kinds of *false positive*. Search produces something that should not have been produced, and the filter catches it. Evaluation passes something that should not have passed, and nothing catches it.

Search's other failures are not filtered, because there is nothing to filter. Search also fails by **omission** — never generating the candidate worth having, choosing the wrong target, stopping too early — and those errors are invisible and permanent. No evaluator recovers them: [evaluation cannot select a candidate that search never reaches](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md). They are not *retained* either, since nothing enters the system; they are simply forgone, and the system cannot tell that they were.

The precise claim is:

> False-positive generation is filtered before retention; false-positive acceptance becomes operative.

That is what makes "make the evaluator stronger" no answer to a weak generator, and it is why the two functions cannot be traded against each other. It also means the consequence below ranks what to automate *among the errors the loop can see*. Omission errors are the reason automating search is not free either — a generator with narrow reach costs improvements no one will ever miss.

## The consequence: automate search first

The costs of automating the two functions are paid in different currencies.

**Automating search costs evaluation throughput.** Machine-generated candidates are judged by the same evaluator that judged the human's. The failure mode is a queue: candidates arriving faster than anything can judge or prune them, which is exactly the pathology in [entropy management must scale with generation throughput](./entropy-management-must-scale-with-generation-throughput.md). That is a *capacity* problem, and capacity problems are tractable — batch, prioritize, sample, or strengthen the evaluator.

**Automating evaluation costs correctness.** A weak oracle accepts changes that do not help, they are retained, and they compound: a bad note gets linked, cited, and distilled into a skill. That is not a capacity problem and no amount of throughput fixes it. It is bounded by [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md).

And taking the autonomy anyway does not break anything visibly — which is what makes it dangerous. A fallible evaluator still rejects some candidates, so it is a real evaluator and [the loop still closes](./definitions/self-improving-system.md). The system stays self-improving and looks healthy, running unattended, while its mistakes accumulate in the artifacts it keeps. Nothing announces the degradation, because the machinery that would have announced it is the machinery that was weakened.

So search is the function whose failures the loop already catches, and it is the one to automate first. Evaluation is the one that has to be *bought*, with an oracle.

This explains a common disappointment in agent-memory systems. Most of them automate search — mine the traces, extract the tips, write them down — and leave evaluation to a human or to nothing at all. The result is a growing pile of unjudged candidates that changes little. The [agent-memory-system-review](../agent-memory-systems/types/agent-memory-system-review.md) type already points at the same place from the other end when it says the distillation step's "trigger, oracle, and curation policy is often the most discriminating part." This claim says why: the oracle is the only part whose errors are both permanent *and* operative — an omitted candidate is lost, but an accepted bad one goes to work.

## The correction path does not escape the bound

The asymmetry is not absolute, and pretending otherwise would overstate it. A bad acceptance *can* be caught later — by a review sweep, a freshness pass, or a Popperian "do I still believe this?" reread. Retention is revocable.

But that correction path is itself evaluation, and it inherits the same bound. Three things follow:

- It spends evaluation capacity, which was the scarce resource to begin with.
- It runs against the same oracle that made the original mistake, so the blind spot that let the change in is the blind spot that lets it stay. A second pass with an unchanged oracle is not a second chance.
- Meanwhile the artifact has been operative, and may have acquired dependents — the cost of removing it is no longer the cost of never having accepted it.

False-positive generation is caught by machinery already running in the loop, at no extra cost. False-positive acceptance is caught only by spending more of the thing that was scarce, and only if the oracle has meanwhile improved.

## Scope

- The claim is scoped to the proposal-selection subtype of [self-improvement](./definitions/self-improving-system.md) — the architecture that has an acceptance step at all. A direct evidence-driven update pathway (gradient, reward, viability) adopts every update, so its failure surface is the adequacy of the objective and the update rule, not a gate's false positives.
- The claim assumes evaluation is the terminal filter. If a system adds monitoring or rollback downstream, that is not a counterexample — it is more evaluation, and it inherits the same bound.
- It holds whether evaluation runs before a candidate becomes operative or after. Post-hoc evaluation changes when the bad change is caught, not whether an unfiltered acceptance is retained.
- It ranks *what to automate first* under a fixed oracle. It does not say search is easy: [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md), and the judgment-heavy parts of search remain hard for their own reasons.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the loop whose functions this claim distinguishes, and the reach-versus-strength point it extends
- [Self-improving system](./definitions/self-improving-system.md) — extends: tells the autonomy gradient which function to climb first, and why the other must be bought
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — mechanism: why evaluation is the bounded function and its errors are the permanent ones
- [Entropy management must scale with generation throughput](./entropy-management-must-scale-with-generation-throughput.md) — evidence: the capacity failure that automated search produces when evaluation does not scale with it
- [Automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — contrasts: search is the safer function to automate, which does not make it the easy one
