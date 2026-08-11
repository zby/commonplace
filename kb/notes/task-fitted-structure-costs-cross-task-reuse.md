---
description: "Current task fit does not warrant permanent structure: harden inherited constraints, and keep task-derived choices replaceable until discriminating use demonstrates transfer"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [document-system, foundations]
---

# Task-fitted structure costs cross-task reuse

A knowledge base's structural layer — types, tags, indexes, schemas, link vocabulary, and routing contracts — can be fitted to the questions it answers today. That fit has immediate value: routing gets cheaper, validation gets sharper, and an agent can infer a writing goal from one word. Yet it establishes usefulness only for the current question set. [Cross-task reuse value](./orchestration-strategies-and-run-state-have-opposite-persistence.md) is a separate property: how much a later, different task gains by retaining the structure. Present fit does not show that this value will transfer.

When the questions change, the cost is mismatch rather than missing content. A tag taxonomy discards no note, a type spec deletes no text, and an index removes no source. A lossy summary can be repaired by falling back to its retained source, as in [theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md). Structural mismatch is different: retained content makes a new taxonomy or index possible, but does not supply the new access path. The content remains available while the structure is shaped for questions nobody asks anymore.

Adoption and hardening are therefore separate decisions. Hardening makes a choice shared, binding, or expensive to replace. A KB can use task-derived structure now without granting it that permanence. If the KB is expected to outlive its current questions, it should keep such structure local and replaceable until varied use that could have exposed a bad fit earns broader scope. It may harden structure forced by boundary commitments, but only while those commitments hold.

## The bill comes due before export

Commonplace, the KB framework documented in this repository, already makes a strong version of this argument on one axis. [A universal knowledge framework demotes content taxonomies to defaults](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) because a taxonomy abstracted from the KBs its authors have seen — often just one — mistakes features of one structural profile for universals. But that note draws the boundary at the framework's edge:

> A single-purpose KB can benefit from hardcoding its profile; the burden begins when that profile is exported.

For a long-lived KB, that boundary is too late. Export is not the only way a KB meets questions it was not built for; its project can change around it. Drift and export run the same test: both bring structure fitted to one question set into contact with another. One does so across time, the other across installations. Hardcoding a profile therefore bets not only on other people's KBs, but also on the KB's own future. The second bet is harder to notice losing because no handover forces the mismatch into view.

The burden therefore begins whenever a KB is expected to outlive the question set that shaped it.

## What earns permanence

The first warrant for hardening comes from constraint. [A framework rule is an inherited constraint only if no rival preserves its boundary invariants](./a-framework-rule-is-inherited-only-without-a-boundary-preserving-rival.md): a rule with a rival that preserves the fixed invariants of a boundary commitment is a replaceable choice, so constraint can warrant hardening only for rules without one — and surviving that test leaves a rule contestable, not certified. Choosing a consumer, substrate, domain, or machinery fixes such invariants. Dropping a rule they genuinely force means changing the commitment, not merely selecting another workable design.

The second warrant comes from evidence. [Only derivation and inheritance give a decomposition starting scope warrant; discriminating use earns it](./only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md). Task-derived structure should begin local and replaceable, but it can earn broader scope by surviving genuinely different questions that could have exposed a bad fit. Promotion should record that evidence explicitly. Adoption by more tools or notes raises migration cost; it does not by itself demonstrate transfer.

At adoption, the source of warrant divides the structural layer into two classes:

- **Constraint-derived structure** is forced by current commitments. Finite consumer context, file-path semantics, and domain answerability remain binding when tasks change within those commitments. Their guarantee ends when the consumer, substrate, domain, or machinery commitment changes.
- **Task-derived structure** is one workable choice among rivals under the same commitments. Examples include a type set or link vocabulary local to one KB subtree, or a guarded default profile. It should be adopted at the narrowest useful scope and left replaceable. Its initial warrant reaches no further than the question that motivated it; broader scope must be earned.

Hence the rule: **harden what current constraints force; promote what discriminating use earns; configure everything else.** Structure that can name neither an inherited constraint nor evidence of transfer has no claim on permanence, however useful it is today.

## Cheap adoption magnifies the cost

Wikis make the accumulation risk acute because they offer many cheap ways to add structure. Any page can become an index, any convention a template, and any distinction a tag or namespace.

Retirement usually has weaker support. Adding a tag scheme can take one session; removing it may require an owner, dependency evidence, and a migration path. Without a retirement trigger, old layers can accumulate. Each may have answered a real question. Taken together, overlapping taxonomies, drifted indexes, and competing conventions raise routing and maintenance costs.

This outcome is not inevitable. Named owners, deprecation metadata, dependency checks, and scheduled audits can interrupt it. Wiki flexibility does not cause structural decay. It lowers adoption friction, so weak retirement pressure leaves more residue behind.

Neighbouring systems illustrate the present-fit and future-transfer trade without proving a universal wiki law. [Sparks](../agent-memory-systems/reviews/sparks.md), a single-binary runtime for personal LLM wikis, hardcodes a small set of page types to provide a clean agent protocol. [Echel](../agent-memory-systems/reviews/echel.md), a local product-creation scaffold, fixes graph-node types around one software workflow. [sift-kg](../agent-memory-systems/reviews/sift-kg.md), a Python CLI and library for persistent knowledge graphs, discovers a schema from an initial corpus and reuses it. Each design can be excellent within its current scope. Assessing present capability does not show whether that scope will transfer.

## Scope

- **This is not an argument against structure or against deriving it from tasks.** As [scenario decomposition drives architecture](./scenario-decomposition-drives-architecture.md) argues, current questions should shape architecture; structure with no current question to answer is speculation. The disagreement concerns permanence, not origin. Today's task can justify adoption, but not hardening.
- **Locality bounds the blast radius; it does not supply retirement.** Structure local to one KB subtree contains most damage from a bad fit. Cross-subtree links can still widen the effect, and locality alone does not remove residue from past questions.
- **The cost is real but not always decisive.** A KB with a stable question set or a short life can rationally hardcode. The claim is that this bet is often invisible and rarely revisited, not that it is always wrong.
- **Commitment changes reopen hardened structure.** Constraint-derived structure survives task drift only while the commitment that forced it remains. A new consumer, substrate, domain, or machinery design requires a new constraint test.
- **Coordination value is a third warrant this rule does not cover.** A shared convention — a schema field, a link label, a routing key — can be worth hardening because every artifact and tool adopts the *same* one — [coordination value](./definitions/coordination-value.md), created by the shared commitment rather than earned by transfer. Its logic inverts the rule above: you commit before any use could show a fit, because waiting withholds the coordination itself. [Coordination value, and the conflict it creates when a better-in-principle theory pulls against it](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md), is treated where maintenance follows authored dependency edges rather than genre; this note governs only permanence warranted by inherited constraint or earned transfer.

## Open Questions

- What signal tells a maintainer that a piece of structure has outlived its question? Notes have staleness and review, but the structural layer has no equivalent. [Automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) places retirement among the judgment-heavy mutations whose oracle is missing.
- What evidence should promote task-derived structure to shared scope? Repetition is not enough unless the later questions could have exposed a bad fit, but nothing here sets a sufficient sample or weighs migration cost against replaceability.
- Can accretion be made self-limiting, so structural elements must periodically justify themselves against a current question rather than persist by default?
- When should a task-derived structure be committed as a shared convention before use could show it transfers, taking [coordination value](./definitions/coordination-value.md) in place of earned reach? That such conventions are legitimate is settled, and [how they behave once committed](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) is treated there; what remains open is the rule for making the commitment — the trade of the option value of staying replaceable against the coordination benefit and the later switching cost.

---

Relevant Notes:

- [A framework rule is an inherited constraint only if no rival preserves its boundary invariants](./a-framework-rule-is-inherited-only-without-a-boundary-preserving-rival.md) — grounds: the one-way test that demotes any rule with a boundary-preserving rival to a replaceable choice, leaving constraint-forced structure as what survives drift
- [Only derivation and inheritance warrant a decomposition's scope claim; discriminating use earns it](./only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md) — grounds: supplies the promotion path by which task-derived structure can earn wider scope without having been permanent at adoption
- [A universal knowledge framework demotes content taxonomies to defaults and keeps answerability](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — contradicts: agrees on the policy but draws the burden at export; this note argues drift brings it forward to the single-purpose instance
- [Scenario decomposition drives architecture](./scenario-decomposition-drives-architecture.md) — contrasts: deriving structure from current scenarios is right; hardening it on that basis is the cost named here
- [Constraining and extraction both trade generality for reliability](./constraining-and-extraction-both-trade-generality-for-reliability.md) — grounds: the underlying trade, applied here to the structural layer and across time rather than to artifacts at a moment of good task fit
- [Orchestration strategies and run state have opposite persistence](./orchestration-strategies-and-run-state-have-opposite-persistence.md) — mechanism: supplies cross-task reuse value as the quantity task-fitting spends
- [Files, not a database](./files-not-database.md) — contrasts: premature schema commitment is the ignorance failure (queries not yet known); this is the confidence failure (today's queries known too well)
- [Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — contrasts: the library/workshop split protects note granularity from task-shaping but leaves the structural layer unprotected
- [Automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — see-also: retire is the mutation this note needs, and the one whose oracle is missing
- [Sparks](../agent-memory-systems/reviews/sparks.md) — evidenced-by: names the fixed-shape/extensibility trade and buys hardcoded page types deliberately for a narrow scope
- [Echel](../agent-memory-systems/reviews/echel.md) — evidenced-by: a node taxonomy hardcoded to one product workflow
- [sift-kg](../agent-memory-systems/reviews/sift-kg.md) — evidenced-by: a schema discovered from the first corpus and cached — fitting and freezing automated
