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
| **distributed-parametric** | hand-tuned weights and thresholds — half of what the lesson displaced | deep learning — the widely cited quadrant |
| **localized forms** | hand-written feature extractors, then today's prompts, harnesses, curated KBs — the other half, and the lesson's next target | prompt, code, and harness search — bounded instances, scaling open |

“Localized” groups natural-language and symbolic artifacts; mixed systems should be decomposed into their operative parts. What the lesson originally displaced straddled both rows — hand-tuned weights and hand-written feature extractors — which is itself evidence that the selection ran along the column, not the row. The columns classify each part by its current production or update process, not by a pure origin story: a hand-authored prompt revised through measured search has entered the learned column for that update. The matrix distinguishes the axes conceptually; it does not assume that every quadrant has an equally scalable learning method.

The distinction rules out two symmetric positions. **Weights-monism** — the view that scalable learning happens only in distributed weights — goes beyond Sutton's production-method claim. That bounds what the 2019 essay establishes, not every later position Sutton holds.

[A 2026 interview with Sutton and Khurram Javed](../sources/sutton-javed-why-ai-models-stop-learning.ingest.md) acknowledges context as system state but treats continued weight updating as necessary for the structuring and generation of new concepts. The substantive dispute is therefore whether non-weight updates can supply the capabilities required for open-ended learning, not whether external state can change. Weight necessity is a serious empirical hypothesis, not a premise the lesson establishes by definition.

The systems cited here still deploy weights alongside harnesses, system prompts, and tools, so absorption at fixed task difficulty — absorption when the tasks assigned do not get harder as capability grows — has not yet made localized structure irrelevant. [External structure can recur at a moving frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) when assigned difficulty rises with capability and some reliability function remains advantageous to externalize; the argument does not require such recurrence after demand saturates or the function is fully absorbed.

The second position, **Hand-crafting-forever** — defending localized forms by defending the manual production of their content — fails the lesson's own test. [What scale removes is generalization whose scope was asserted rather than earned](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md), and hand authorship is a common way to embed such scope. The compliant position is to test search and learning over localized forms too.

## The machinery asymmetry explains the misreading

The cited cases suggest why the method axis is often conflated with parametric form: gradient descent supplies a computational evidence-to-update path together with credit assignment. Credit assignment is the problem of deciding which component bears responsibility for an outcome; the chain rule propagates that responsibility through parameter space. It need not expose a separately rejectable candidate, so proposal selection is one update architecture rather than the universal structure of learning. The localized quadrant has [fragments with the artifact class fixed in advance](./treat-continual-learning-as-representational-form-coevolution.md) — bounded instances of learned production over a single artifact class, such as prompt optimization, code evolution, and harness search — but no established method for a large, interdependent corpus. Before backpropagation scaled, hand-crafted features could likewise appear to mark a fixed boundary of learning because no general method reached them. That analogy motivates a search for the missing machinery; it does not show that such machinery must exist.

## Why the form axis does not collapse into weights

Mixed deployments have reasons to retain external state even as parametric learning improves. [Localized retention pays when sparse changes have bounded impact in a matching decomposition](./localized-retention-pays-where-change-is-sparse-in-a-matching.md): explicit dependencies can bound the affected artifacts and checks, provided that the local advantage exceeds translation, routing, consistency, and coordination costs. [Reproduction does not transfer authority](./parametric-reproduction-cannot-replace-an-authoritative-record.md), so a record's governance role survives content absorption, and [a commitment exists nowhere until recorded](./commitment-not-derivation-creates-new-ground-truth.md). Enforced checks can also [improve the selection environment for later candidates](./oracle-accumulation-improves-the-selection-environment.md) within their maintained domain, although overlap, drift, gaming, and maintenance costs can erase that gain.

These arguments establish persistent functions for localized state. They do not by themselves prove that learned semantic content must remain natural-language or symbolic rather than migrate into learned modular or parametric substrates. That stronger claim belongs to the scaling conjecture below.

## The learned-localized quadrant and its missing machinery

The learned-localized quadrant already has bounded instances. [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) generates program functions with a pretrained language model, evaluates them, and retains successful programs for further search. [AlphaDev](https://www.nature.com/articles/s41586-023-06004-9) used reinforcement learning and tree search to discover assembly sorting routines later incorporated into LLVM's standard C++ library. Their outputs are localized even though their search machinery includes parametric models.

Recent agent systems extend the pattern. One framework [searches prompts, tools, and their composition as symbolic learnables](https://arxiv.org/pdf/2406.18532); Memento-Skills [continually rewrites structured Markdown skills as persistent evolving memory](https://arxiv.org/pdf/2603.18743); and Co-Harness [alternates harness search with fine-tuning](https://arxiv.org/pdf/2607.22688), aiming to distill validated scaffolding into weights while keeping the harness revisable. Co-Harness is designed around cross-form coevolution, but its experiments do not establish that the allocation is efficient. Meta-Harness, an outer loop that searches task-specific LLM harness code, provides a precisely bounded result: [its ablation compares a fixed summary-without-traces treatment with raw-trace access and leaves episode-backed theory untested](./an-experiment-identifies-only-the-contrast-it-actually-runs.md).

These systems show that computation can optimize localized artifacts in bounded domains. They do not yet demonstrate efficient learning as corpus size, dependency density, and task horizon grow. The hard core is **credit assignment without a chain rule**: a deployment failure rarely identifies which artifact should change. Three discrete substitutes are visible in the methods cited here: explicit dependency edges [bound the affected validation work](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), retained episodes carry attribution signals, and accumulated evaluation checks price candidate changes. No general way to compose them is identified here, while soft evaluation signals, supersession, bounded maintenance, and consolidation remain adjacent problems. Where a localized-artifact path uses proposal selection, it [requires search, reject-capable evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md). A direct update may collapse those roles, but it still owes an evidence-responsive operative change.

## What may stay supplied

Compatibility with the lesson does not require every human-designed component to become self-modifiable. It distinguishes the human supply of task- or domain-specific competence from fixed machinery that implements a general production method over the reach being claimed.

Objectives, commitments, and grants of authority may remain supplied: evidence can bear on an objective without deriving the terminal objective itself, and nothing entails a commitment before it is made. Fixed general learning or search algorithms, metalanguages, runtimes, exact interfaces, resource controls, and trusted kernels may also remain. Their continued presence narrows what the claim covers, but fixed provenance alone does not make the method incompatible.

The pressure falls on family- or task-specific knowledge that people continue to construct as the system's claimed reach widens. A hand-built catalog of target solutions remains hand-supplied knowledge even when automatic retrieval selects among them. A general computational method that acquires the required production knowledge from permitted evidence is the stronger claim stated by [the pressure for agentic factory development](./broad-software-demands-create-pressure-for-agentic-factory-development.md). Whether supposedly general machinery has hidden target-specific scope is empirical.

Adoption need not remain human. [Computational closure](./methodological-and-computational-closure-track-different-changes.md) asks whether any required decision on the declared path still needs a person, while [warranted autonomy](./warranted-autonomy-is-bounded-by-oracle-domain.md) asks whether unattended evaluation is trustworthy. These are actor-allocation and warrant questions, not additions to the Bitter Lesson's production-method axis.

## Compatibility is assessed per portion of a path

Because the columns classify parts and updates, compatibility with the lesson is a property of a *portion of a path*, not of a methodology or an artifact class. On a declared path, a portion has moved to scalable production when evidence-responsive computation determines and makes its update operative. In proposal-selection architectures, search proposes candidates and a reject-capable evaluator admits one; direct-update architectures may determine the successor without a separate gate. The retained output's form does not decide the classification.

The remainder is not thereby judged incompatible. Transfer prefers decisions it can warrant, so what stays human-supplied is often what no available evaluation can check, [since warranted transfer leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md). Its difficulty does not reclassify the moved portion, [because a method's ceiling bounds the method, not the transfer already made](./a-method-ceiling-bounds-the-method-not-the-transfer-already-made.md).

Two limits keep this from becoming a convergence claim. Evidence that several portions moved does not establish closure; closure separately requires every decision assigned to the declared pathway to be computational. The remainder can also be replenished while assigned difficulty keeps pace with capability and some function stays advantageous to externalize, [since scaling absorbs scaffolding at fixed difficulty, not at the frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md).

A portion is worth having when it raises accepted outcomes per unit of total human effort, counting configuration, review, recovery, and repair — not when it reaches some share of the path, since a remainder small in count can be large in cost. In FunSearch, proposal and scoring moved while the specification, evaluator, skeleton, and function boundary stayed supplied; that bounds the demonstrated reach without erasing the moved production work.

## The conjecture and the stake

The prediction is narrower than the conceptual matrix: for long-lived agent systems undergoing heterogeneous change, learning through more than one representational form can remain on the efficient frontier rather than serve only as temporary scaffolding. A serious test must compare learned localized methods with parametric learning and distillation baselines as corpus size, dependency density, task horizon, evaluation cost, and compute grow.

The bet can lose. If selection over localized knowledge remains artisanal as those dimensions scale, the strong learned-localized claim fails, even though interfaces, authoritative records, and checks may remain external. Commonplace, the agent-operated knowledge-base framework, is a human-assisted experiment in the missing loop: people still identify reusable lessons, assign blame, choose a form, and accept updates. Whether theory-mediated proposals improve sample efficiency [remains an open bet](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md). [Reflective machinery must itself earn persistence rather than remain exempt by position](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).

## Scope

- "Fails", "the bet can lose", and "efficient frontier" throughout mean a worse frontier, not impossibility: a learned architecture with stable semantic modules, explicit scope, and localized update paths would confirm the mixed-form conjecture in a different substrate, not refute it.

## Open Questions

- Can the discrete credit-assignment substitutes — dependency edges, retained episodes, accumulated oracles — compose into a general method, or is per-domain assembly the ceiling?
- Which supplied choices encode task-specific competence that scalable production must replace, and which are warranted general machinery or authority boundaries over the declared reach?

---

Relevant Notes:

- [The bitter lesson selects against unearned reach, not against structure](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) — grounds: what the selection actually removes, which is what frees it from the form axis; it licenses claims and methods, not the persistence of any carrier
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
