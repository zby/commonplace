---
description: "For KBs expected to face changing questions, current-task fit warrants reversible adoption, not costly entrenchment; permanence needs enduring constraint, discriminating transfer evidence, or coordination value"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [document-system, foundations]
---

# Current-task fit alone does not warrant costly structural entrenchment

A knowledge base's structural layer — types, tags, indexes, schemas, link vocabularies, and rules for where artifacts belong — can be fitted to the questions it answers today. That fit has immediate value: routing gets cheaper, validation gets sharper, and an agent can infer a writing goal from one word. Yet it establishes usefulness only for the current question set. [Cross-task reuse value](./orchestration-strategies-and-run-state-have-opposite-persistence.md) is a separate property: how much a later, different task gains from retaining the structure. Present fit alone does not show that the structure will remain useful.

When the questions change, the structure can become a mismatch even if the underlying content remains intact. A lossy summary can be repaired by falling back to its retained source, as in [theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md). Retained content likewise makes a new taxonomy or index possible, but it does not provide the new access path. Discovery and migration must still rebuild it. Structure can also influence what gets captured, so structural mismatch and content loss are not mutually exclusive. The narrower point here is that retaining content does not neutralize structural mismatch: [learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

Adoption and entrenchment are therefore different decisions. Adoption uses a choice for current work. Entrenchment embeds that choice in dependencies or migration costs that make replacement expensive. A binding choice that remains cheap to extend or replace is outside this claim. If a KB is expected to outlive its current questions, current-task fit warrants adopting task-derived structure at the narrowest useful scope. Until another warrant appears, keeping that structure replaceable preserves the adaptation options that entrenchment would spend.

## The bill comes due before export

Commonplace already makes this argument along one axis. [A universal knowledge framework demotes content taxonomies to defaults](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) because a taxonomy abstracted from the KBs its authors have seen — often just one — can mistake features of one structural profile, or bundle of structural choices, for universals. But that note draws the boundary at the framework's edge:

> A single-purpose KB can benefit from hardcoding its profile; the burden begins when that profile is exported.

For a long-lived KB, that boundary is too late. Export is not the only way a KB encounters questions it was not built for; its project can change around it. Drift and export pose the same transfer test: both bring structure fitted to one question set into contact with another. One does so across time, the other across installations. Hardcoding a profile therefore bets not only on other people's KBs, but also on the KB's own future. The internal bet can be harder to notice failing because no handover forces the mismatch into view.

A KB expected to outlive its current question set therefore faces transfer risk before export. That risk is not always large enough to decide against entrenchment, but present fit alone does not price it.

## What warrants entrenchment

The first warrant is an enduring constraint. [A framework rule with a boundary-preserving rival is not an inherited constraint](./a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md). Choosing a consumer, substrate, domain, or machinery commits the KB to invariants that a rival design must preserve. If replacing a rule requires changing one of those commitments, the rule is inherited from them rather than merely selected. Failing to find a boundary-preserving rival makes entrenchment defensible, not permanently certified; when the commitments change, the constraint test must run again.

The second warrant is transfer evidence. [Use tests a decomposition locally; retained rationale is what makes transfer testable](./use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md), and [derivation and inheritance give a decomposition only starting scope warrant; discriminating evidence or proof earns scope](./derivation-and-inheritance-give-starting-warrant-earns-scope.md). Task-derived structure should therefore begin local and replaceable. It earns wider scope only by remaining useful across different questions that could have exposed a bad fit, and only for the scope those cases exercise or a proof establishes. Adoption by more tools or notes raises migration cost; it does not demonstrate transfer.

The third warrant is [coordination value](./definitions/coordination-value.md). A shared schema field, link label, or routing key can become useful because every artifact and tool commits to the same interface. Waiting for transfer evidence may prevent the shared use that creates this interoperability. Coordination can therefore justify entrenchment before discriminating use when its expected benefit exceeds fragmentation, lock-in, and later switching cost. This note does not supply that decision threshold.

The resulting rule is: **use current-task fit to adopt; entrench only what enduring constraints force, discriminating use or proof earns for a stated scope, or coordination value justifies.** A cheap additive choice need not satisfy this rule merely because it is binding today. The rule governs choices whose dependencies make later replacement costly.

## Cheap adoption and weak retirement accumulate cost

Wikis make structural additions cheap. Any page can become an index, any convention a template, and any distinction a tag or namespace.

When adoption is cheap but retirement requires an owner, dependency evidence, and a migration path, additions can outpace removals. Once those additions acquire dependants, overlapping taxonomies, drifted indexes, and competing conventions raise routing and maintenance costs even though each once answered a real question.

This outcome is not inevitable. Named owners, deprecation metadata, dependency checks, and scheduled audits can interrupt it. The [comparative review of 148 agent memory systems](../agent-memory-systems/agentic-memory-systems-comparative-review.md) provides one bounded observation: only seven of 139 automatically writing systems implement all seven tracked lifecycle operations. That result supports an adoption-versus-retirement asymmetry in the reviewed corpus; it does not prove a universal wiki law.

## Scope

- **The claim does not oppose structure or task-derived design.** As [scenario decomposition drives architecture](./scenario-decomposition-drives-architecture.md) argues, current questions should shape architecture; structure with no current question to answer is speculation. The disagreement concerns costly entrenchment, not origin or reversible use.
- **Locality preserves option value only when dependencies and change remain bounded.** [Localized retention pays when sparse changes have bounded impact in a matching decomposition](./localized-retention-pays-where-change-is-sparse-in-a-matching.md). A nominally local structure with cross-subtree dependants may already be expensive to replace.
- **Entrenchment costs are not always decisive.** A KB with a stable question set or a short life can rationally hardcode. Coordination value can also outweigh replaceability. The claim is that current-task fit alone does not settle the trade.

## Open Questions

- What signals show that a structural element has outlived its question, and what lifecycle rule would make that signal trigger review or retirement rather than passive accumulation? [Automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) places retirement among the judgment-heavy mutations whose oracle is missing.
- What evidence is enough to promote task-derived structure, and how should the exercised cases or proof determine the scope earned?
- When should coordination benefit justify costly commitment before transfer evidence exists? The missing rule must compare interoperability against the option value of replaceability, fragmentation, lock-in, and migration cost.

---

Relevant Notes:

- [Constraining and extraction both trade generality for reliability](./constraining-and-extraction-both-trade-generality-for-reliability.md) — grounds: the underlying trade, applied here to the structural layer and across time rather than to artifacts at a moment of good task fit
- [Orchestration strategies and run state have opposite persistence](./orchestration-strategies-and-run-state-have-opposite-persistence.md) — mechanism: supplies cross-task reuse value as the quantity costly task-fitting can spend
- [Files, not a database](./files-not-database.md) — contrasts: premature schema commitment is the ignorance failure; this is the confidence failure of knowing today's queries too well
- [Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — contrasts: the library/workshop split protects note granularity from task-shaping but leaves the structural layer exposed
- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — contrasts: repeated-run stability can warrant present codification without establishing cross-question permanence
- [Operational signals that a component is a relaxing candidate](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — extends: offers partial signals for detecting a structural choice whose fit may be failing
