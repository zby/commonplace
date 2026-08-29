---
description: "The lesson's axis is production method — hand-crafted versus search-and-learning — not representational form. Learned localized forms are therefore a coherent scaling hypothesis, with cross-artifact credit assignment as the decisive open problem"
type: kb/types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [learning-theory, deploy-time-learning, foundations]
---

# The bitter lesson selects production methods, not representational forms

[Richard S. Sutton's 2019 essay “The Bitter Lesson”](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) contrasts leveraging human knowledge with leveraging computation through search and learning. That is a claim about **production method** — how a system's behavior-determining content gets made. The folk compression “structure loses to weights” silently substitutes a claim about **representational form** — [how retained content is encoded and consumed](./definitions/representational-form.md) in natural-language, symbolic, or distributed-parametric form. Crossing these two axes yields four idealized quadrants:

| | hand-crafted | learned (search + selection) |
|---|---|---|
| **distributed-parametric** | hand-tuned features and weights — the lesson's original kill | deep learning — the celebrated quadrant |
| **localized forms** | today's prompts, harnesses, curated KBs — the lesson's next target | prompt, code, and harness search — bounded instances, scaling open |

“Localized” groups natural-language and symbolic artifacts; mixed systems should be decomposed into their operative parts. The columns classify each part by its current production or update process, not by a pure origin story: a hand-authored prompt revised through measured search has entered the learned column for that update. The matrix distinguishes the axes conceptually; it does not assume that every quadrant has an equally scalable learning method.

The distinction rules out two symmetric positions. **Weights-monism** — the view that scalable learning happens only in distributed weights — goes beyond Sutton's production-method claim. That bounds what the 2019 essay establishes, not every later position Sutton holds. [A 2026 interview with Sutton and Khurram Javed](../sources/sutton-javed-why-ai-models-stop-learning.ingest.md) acknowledges context as system state but treats continued weight updating as necessary for the structuring and generation of new concepts. The substantive dispute is therefore whether non-weight updates can supply the capabilities required for open-ended learning, not whether external state can change. Weight necessity is a serious empirical hypothesis, not a premise the lesson establishes by definition. The systems surveyed here still deploy weights alongside harnesses, system prompts, and tools, so absorption at fixed task difficulty has not yet made localized structure irrelevant. [External structure can recur at a moving frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) when assigned difficulty rises with capability and some reliability function remains advantageous to externalize; the argument does not require such recurrence after demand saturates or the function is fully absorbed.

**Hand-crafting-forever** — defending localized forms by defending the manual production of their content — fails the lesson exactly as charged. Hand authorship is a common way to commit a requirement-to-objective proxy beyond the scope that assessed it, [which one case-level conjecture offers as the diagnosis of a structured method's loss under scaling](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md). The compliant position is to test search and learning over localized forms too.

## The machinery asymmetry explains the misreading

The surveyed cases suggest why the method axis is often conflated with parametric form: gradient descent supplies a complete computational loop of proposal, evaluation, retention, and credit assignment. Credit assignment is the problem of deciding which component bears responsibility for an outcome; the chain rule propagates that responsibility through parameter space. The localized quadrant has [fragments with the artifact class fixed in advance](./treat-continual-learning-as-representational-form-coevolution.md) — prompt optimization, code evolution, and harness search — but no established method for a large, interdependent corpus. Before backpropagation scaled, hand-crafted features could likewise appear to mark a fixed boundary of learning because no general method reached them. That analogy motivates a search for the missing machinery; it does not show that such machinery must exist.

## Why the form axis does not collapse into weights

Mixed deployments have reasons to retain external state even as parametric learning improves. [Localized retention pays when sparse changes have bounded impact in a matching decomposition](./localized-retention-pays-where-change-is-sparse-in-a-matching.md): explicit dependencies can bound the affected artifacts and checks, provided that the local advantage exceeds translation, routing, consistency, and coordination costs. [Reproduction does not transfer authority](./parametric-reproduction-cannot-replace-an-authoritative-record.md), so a record's governance role survives content absorption, and [a commitment exists nowhere until recorded](./commitment-not-derivation-creates-new-ground-truth.md). Enforced checks can also [improve the selection environment for later candidates](./oracle-accumulation-improves-the-selection-environment.md) within their maintained domain, although overlap, drift, gaming, and maintenance costs can erase that gain.

These arguments establish persistent functions for localized state. They do not by themselves prove that learned semantic content must remain natural-language or symbolic rather than migrate into learned modular or parametric substrates. That stronger claim belongs to the scaling conjecture below.

## The learned-localized quadrant and its missing machinery

The learned-localized quadrant already has bounded instances. [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) generates program functions with a pretrained language model, evaluates them, and retains successful programs for further search. [AlphaDev](https://www.nature.com/articles/s41586-023-06004-9) used reinforcement learning and tree search to discover assembly sorting routines later incorporated into LLVM's standard C++ library. Their outputs are localized even though their search machinery includes parametric models.

Recent agent systems extend the pattern: [prompts, tools, and their composition are searched as symbolic learnables](https://arxiv.org/pdf/2406.18532); [structured Markdown skills are continually rewritten as persistent evolving memory](https://arxiv.org/pdf/2603.18743); and [harness search alternates with fine-tuning](https://arxiv.org/pdf/2607.22688), aiming to distill validated scaffolding into weights while keeping the harness revisable. Co-Harness is designed around cross-form coevolution, but its experiments do not establish that the allocation is efficient. Meta-Harness, an outer loop that searches task-specific LLM harness code, provides a precisely bounded result: [its ablation compares a fixed summary-without-traces treatment with raw-trace access and leaves episode-backed theory untested](./an-experiment-identifies-only-the-contrast-it-actually-runs.md).

These systems show that computation can optimize localized artifacts in bounded domains. They do not yet demonstrate efficient learning as corpus size, dependency density, and task horizon grow. The hard core is **credit assignment without a chain rule**: a deployment failure rarely identifies which artifact should change. Three discrete substitutes are visible in the methods surveyed here: explicit dependency edges [bound the affected validation work](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), retained episodes carry attribution signals, and accumulated evaluation checks price candidate changes. No general way to compose them is identified here, while soft evaluation signals, supersession, bounded maintenance, and consolidation remain adjacent problems. [A general proposal-selection loop still requires search, reject-capable evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md); localized credit assignment must route outcomes through that loop.

## What stays supplied

Search and learning should produce localized *knowledge* content when the method proves competitive. Three things remain supplied rather than learned:

- The objective, because [no loop can supply its own notion of better](./self-improvement-is-relative-to-a-declared-objective.md).
- Commitments, because nothing entails a decision before it is made.
- The adoption “no,” [allocated per decision](./methodological-and-computational-closure-track-different-changes.md) and moved inward only as far as an [oracle](./warranted-autonomy-is-bounded-by-oracle-domain.md) — a signal used to evaluate candidates — earns authority in that domain.

The lesson's target is hand-crafted content, not human authority.

## Compatibility is assessed per portion of a path

Because the columns classify parts and updates, compatibility with the lesson is a property of a *portion of a path*, not of a methodology or an artifact class. On a declared path, a decision has moved to scalable production when its candidates are proposed by search or a model and accepted by an oracle the candidate did not author. That portion is governed by the lesson, whatever form its retained outputs take. The remainder is not thereby condemned; it is predicted: transfer prefers the decisions it can warrant, so what stays hand-supplied is what no available oracle can check, [since warranted transfer leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md). Its difficulty does not reclassify the moved portion, [because a method's ceiling bounds the method, not the transfer already made](./a-method-ceiling-bounds-the-method-not-the-transfer-already-made.md).

Two limits keep this from becoming a convergence claim. Portions do not stack toward closure: each is taken at an oracle, and the next decision is harder to warrant. And the remainder is replenished while assigned difficulty keeps pace with capability and some function stays advantageous to externalize, [since scaling absorbs scaffolding at fixed difficulty, not at the frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md). A portion is worth having when it raises accepted outcomes per unit of total human effort, counting configuration, review, recovery, and repair — not when it reaches some share of the path, since a remainder small in count can be large in cost. The moved portion still has the three supplied items above; in FunSearch, proposal and scoring moved while the specification, evaluator, skeleton, and function boundary stayed supplied.

## The conjecture and the stake

The prediction is narrower than the conceptual matrix: for long-lived agent systems undergoing heterogeneous change, learning through more than one representational form can remain on the efficient frontier rather than serve only as temporary scaffolding. A serious test must compare learned localized methods with parametric learning and distillation baselines as corpus size, dependency density, task horizon, evaluation cost, and compute grow.

The bet can lose. If selection over localized knowledge remains artisanal as those dimensions scale, the strong learned-localized claim fails, even though interfaces, authoritative records, and checks may remain external. Commonplace, the agent-operated knowledge-base framework, is a human-assisted experiment in the missing loop: people still identify reusable lessons, assign blame, choose a form, and accept updates. Whether theory-mediated proposals improve sample efficiency [remains an open bet](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md). [Reflective machinery must itself earn persistence rather than remain exempt by position](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).

## Scope

- "Wins" and "need" throughout mean worse-frontier, not impossibility: a learned architecture with stable semantic modules, explicit scope, and localized update paths would confirm the mixed-form conjecture in a different substrate, not refute it.

## Open Questions

- Can the discrete credit-assignment substitutes — dependency edges, retained episodes, accumulated oracles — compose into a general method, or is per-domain assembly the ceiling?
- What would license moving one of the supplied-side operations inward — the migration-earned criterion applied to the loop's own operators, one oracle at a time?

---

Relevant Notes:

- [Unsupported proxy scope may explain a structured method's loss under scaling](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) — grounds: a case-level diagnosis of what a loss under scaling may select against, which is what frees the selection from the form axis; it supplies no inverse guarantee for assessed structure
- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — grounds: why the portion of a path that has moved to scalable production is the portion an independent oracle reaches, and why the remainder's difficulty is predicted
- [A method's ceiling bounds the method, not the transfer it already made](./a-method-ceiling-bounds-the-method-not-the-transfer-already-made.md) — grounds: the non-retroactivity that keeps the remainder's difficulty from reclassifying the moved portion
- [Representational form](./definitions/representational-form.md) — defined-in: the derived carve supplying the form axis and the localized-forms class
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](./localized-retention-pays-where-change-is-sparse-in-a-matching.md) — mechanism: why heterogeneous change keeps the form axis from collapsing into weights
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — grounds: the answer to "the harness is temporary"
- [Oracle accumulation improves selection for later candidates in its maintained domain](./oracle-accumulation-improves-the-selection-environment.md) — grounds: the symbolic layer's compounding role in the loop this note calls for
- [Treat continual learning as representational-form coevolution](./treat-continual-learning-as-representational-form-coevolution.md) — extends: the coevolution frame and per-class fragment inventory this note reads through the two-axis carve
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — grounds: the bounded-validation-radius factoring that makes the localized loop a coherent target
- [An experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: the precise reading of the strongest fourth-quadrant fragment
- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: the open bet on the proposal operator being theory-formation
- [Sutton, The Bitter Lesson (original essay)](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) — abstracted-from: the production-method opposition is Sutton's own carve; the orthogonality claim is this note's extension
- [Symbolic Learning Enables Self-Evolving Agents](https://arxiv.org/pdf/2406.18532) — evidenced-by: prompts, tools, and their composition searched as learnables — a fourth-quadrant fragment
- [Memento-Skills: Let Agents Design Agents](https://arxiv.org/pdf/2603.18743) — evidenced-by: structured Markdown skills as continually rewritten persistent memory — a fourth-quadrant fragment
- [Co-Harness: Co-Evolving Harnesses and Model Weights](https://arxiv.org/pdf/2607.22688) — evidenced-by: harness search alternating with parametric distillation — the closest published shape to full coevolution
- [Reflection buys addressability](./reflection-buys-addressability.md#what-addressability-does-not-buy) — extends: what addressability does not buy: credit assignment, coherence, retrieval, admission
