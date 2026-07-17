---
description: "Structure fitted to the questions a KB is asked today loses value when the questions change; wikis accumulate the damage because structure is cheap to add and nothing forces its removal"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [document-system, foundations]
---

# Task-fitted structure costs cross-task reuse

A knowledge base's structural layer — types, tags, indexes, schemas, link vocabulary, routing contracts — can be shaped to fit the questions currently asked of it. The fit is worth something: routing gets cheaper, validation sharper, and an agent can infer a writing goal from one word. But the fit is to a *question set*, and question sets drift. Structure justified by today's task holds no value for tomorrow's, and it does not disappear when the task that motivated it does.

The damage is **fit, not loss**. A tag taxonomy discards no content; a type spec deletes nothing; an index removes no note. That is why the retained-source repair ([theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md)) does not cover this case: a lossy summary can be repaired by falling back to the source it was shaped from, but a structural layer *is* the source — correctly preserved, wrongly shaped. Nothing is missing. The access path is simply built for a question nobody asks anymore.

## The bill comes due before export

Commonplace already holds a strong version of this argument on one axis. [A universal knowledge framework demotes content taxonomies to defaults](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) because a taxonomy abstracted from the KBs its authors have seen — often just one — mistakes profile features for universals. But that note draws the boundary at the framework's edge:

> A single-purpose KB can benefit from hardcoding its profile; the burden begins when that profile is exported.

Too generous, because **export is not the only way a KB meets a question it was not built for**. A single-purpose KB meets them by living: its question set drifts as the project it serves changes. Drift is the instance-level analogue of export — the same mismatch between structure and questions, arriving through time rather than through distribution. Hardcoding a profile bets not only on other people's KBs but on the KB's own future, and that second bet is the harder one to notice losing, because no handover ever forces the mismatch into view.

The burden therefore begins whenever a KB is expected to outlive the question set that shaped it.

## Wikis accumulate the damage

The failure is worst in a wiki, precisely because a wiki is *good* at structure. Its structural affordances are near-unlimited — any page can become an index, any convention a template, any distinction a tag or namespace — so structure is cheap to add.

It is also free to leave. Adding a tag scheme costs a session; removing one means establishing that no consumer depends on it, which nobody has time to do. Structure therefore accretes monotonically. Each layer was locally rational — someone had a real question and built what answered it — and the aggregate is a hodgepodge that serves no question well: overlapping taxonomies, indexes with drifted membership, three conventions for one distinction, none clearly wrong, none load-bearing enough to delete.

Task-fitting is the per-task error; the hodgepodge is that error integrated over time. A wiki's flexibility does not cause it, but it removes every natural brake on it — so the flexibility that makes a wiki adoptable is also what makes it degrade.

Neighbouring systems buy the opposite trade, and their reviews frame it as fixed shape versus extensibility without drawing the reuse consequence:

- [Sparks](../agent-memory-systems/reviews/sparks.md) names the trade outright — it "gets a clean agent protocol because entity/concept/summary/synthesis/collection pages and collection extractors are hardcoded."
- [Echel](../agent-memory-systems/reviews/echel.md) hardcodes `product/problem/user/need/feature/requirement/component/workflow/task/decision/evidence/risk/milestone` graph nodes: a taxonomy fitted to one workflow, and excellent for it.
- [sift-kg](../agent-memory-systems/reviews/sift-kg.md) automates the whole mistake — "Schema-free means 'discover a schema once, then reuse it.'" A model infers an entity/relation taxonomy from a sample of the first corpus, caches it, and reuses it unless forced. Fitting and freezing, both unsupervised.

None is wrong within its scope. They show that the cost falls *in the future*, which is exactly the cost that an assessment of present capability cannot see.

## What earns permanence

The discipline follows from a test the KB already has. [First principles are inherited constraints, not design choices](./first-principles-are-inherited-constraints-not-design-choices.md): a rule is a first principle iff it arrives in the constraint packet of a boundary commitment — consumer, substrate, domain, or machinery. Such rules cannot demote, because dropping one means re-choosing a commitment and taking a different packet whole.

That test partitions the structural layer:

- **Constraint-derived structure** is forced. Bounded context is inherited from the consumer, path semantics from the file substrate, answerability from the domain. Change the task and these do not move — the task never justified them. This structure survives drift, and it is the only structure that does.
- **Task-derived structure** is a position *within* the design space: a workable choice among rivals under the same commitments. It should be adopted locally, declared explicitly, and left replaceable — a collection-local type set, a collection-owned link vocabulary, a guarded default profile — with its scope no wider than the question that motivated it.

Hence the rule: **harden what a constraint forces; configure everything else.** Structure that cannot name the commitment it inherits from has no claim on permanence, however useful it is today.

## Scope

- **This is not an argument against structure, or against deriving it from tasks.** [Scenario decomposition drives architecture](./scenario-decomposition-drives-architecture.md), and it should — structure with no current question to answer is speculation. The disagreement is about *permanence*, not origin: structure may be derived from today's task but not hardened on that basis.
- **Locality bounds the blast radius; it does not stop accretion.** Collection-local structure means a bad fit damages one collection rather than the framework. It does nothing about a single collection silting up with the residue of its own past questions. Locality is containment, not retirement — and retirement is what the hodgepodge actually needs.
- **The cost is real but not always dominant.** A KB with a genuinely stable question set, or a short life, can rationally hardcode. The claim is that this bet is usually invisible and rarely revisited, not that it is always wrong.
- **[Cross-task reuse value](./orchestration-strategies-and-run-state-have-opposite-persistence.md) is the quantity at stake** — how much a later, different task gains from keeping a part around. Constraint-derived structure has it by construction; task-derived structure has whatever the next task happens to grant it.

## Open Questions

- What signal tells a maintainer that a piece of structure has outlived its question? Notes have staleness and review; the structural layer has no equivalent, and [retire](./automating-kb-learning-is-an-open-problem.md) is among the judgment-heavy mutations whose oracle is missing.
- Whether accretion can be made self-limiting — a structural layer whose elements must periodically re-justify themselves against a current question rather than persisting by default.

---

Relevant Notes:

- [First principles are inherited constraints, not design choices](./first-principles-are-inherited-constraints-not-design-choices.md) — grounds: the membership test separating structure that survives drift from structure that does not
- [A universal knowledge framework demotes content taxonomies to defaults and keeps answerability](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — contradicts: agrees on the policy but draws the burden at export; this note argues drift brings it forward to the single-purpose instance
- [Scenario decomposition drives architecture](./scenario-decomposition-drives-architecture.md) — contrasts: deriving structure from current scenarios is right; hardening it on that basis is the cost named here
- [Constraining and extraction both trade generality for reliability](./constraining-and-extraction-both-trade-generality-for-reliability.md) — grounds: the underlying trade, applied here to the structural layer and across time rather than to artifacts at a moment of good task fit
- [Orchestration strategies and run state have opposite persistence](./orchestration-strategies-and-run-state-have-opposite-persistence.md) — mechanism: supplies cross-task reuse value as the quantity task-fitting spends
- [Files, not a database](./files-not-database.md) — contrasts: premature schema commitment is the ignorance failure (queries not yet known); this is the confidence failure (today's queries known too well)
- [Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — contrasts: the library/workshop split protects note granularity from task-shaping but leaves the structural layer unprotected
- [Automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — see-also: retire is the mutation this note needs, and the one whose oracle is missing
- [Sparks](../agent-memory-systems/reviews/sparks.md) — evidence: names the fixed-shape/extensibility trade and buys hardcoded page types deliberately for a narrow scope
- [Echel](../agent-memory-systems/reviews/echel.md) — evidence: a node taxonomy hardcoded to one product workflow
- [sift-kg](../agent-memory-systems/reviews/sift-kg.md) — evidence: a schema discovered from the first corpus and cached — fitting and freezing automated
</content>
