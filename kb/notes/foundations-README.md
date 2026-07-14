---
description: Core theory the rest of the KB builds on — contextual competence, bounded context, reach, design methodology, composability
type: kb/types/tag-readme.md
index_source: tag
index_key: foundations
---

# Foundations

Core theory that the rest of the KB builds on. These notes define the quality criteria, the design methodology, and the fundamental constraints that shape every other decision.

## Notes

- [agent memory needs discoverable, composable, trusted knowledge under bounded context](./agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) — unifying theory: three properties form the minimal artifact-quality basis for remembered knowledge that serves contextual competence
- [context-efficiency-is-the-central-design-concern-in-agent-systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — context is the scarce resource; nearly every architectural pattern is a response to volume or complexity pressure
- [programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must-earn-first-principles-support](./programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must.md) — borrow from any source, filter through first principles; programming patterns get a fast pass
- [short-composable-notes-maximize-combinatorial-discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — the library exists for co-loading; short atomic notes maximize the surface area for cross-cutting discovery
- [a knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — content registers explain why theory, description, and prescription need distinct quality goals and asymmetric maintenance rules
- [a universal knowledge framework demotes content taxonomies to defaults and keeps answerability](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — universality keeps second-order obligations (declared contracts, answerability) and demotes content taxonomies to guarded defaults; contradicts the tripartition's exhaustiveness claim
- [first principles are inherited constraints, not design choices](./first-principles-are-inherited-constraints-not-design-choices.md) — the stable complement to the demotion claim: a membership test (inherited from consumer, substrate, domain, or machinery coherence) plus the principles that currently pass it
- [a-knowledge-base-should-support-fluid-resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — KB quality measured by how fluidly it supports moving between abstraction levels
- [charting-the-knowledge-access-problem-beyond-rag](./charting-the-knowledge-access-problem-beyond-rag.md) — exploratory decomposition: separates substrate, pointers, navigation modes, synthesis, and maintenance so RAG-vs-filesystem debates stop collapsing unlike tasks
- [mechanistic constraints make Popperian KB recommendations actionable](./mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — bridges conjecture-and-refutation with bounded-context mechanics
### Reflection and self-extension

Read in order: the two definitions fix the vocabulary, the middle three develop it, and the case note applies it to this system.

- [actionable theory](./definitions/actionable-theory.md) — definition: a relational property of theory, operator, available operations, and target system
- [reflective system](./definitions/reflective-system.md) — definition: aspect-bounded, causally connected self-representation inside a declared computational or socio-technical boundary
- [cross-representational reflection](./cross-representational-reflection.md) — synthesis: reflective coverage across behavior-bearing representations and the mappings between them
- [governed adaptation requires search, evaluation, and operative retention](./governed-adaptation-requires-search-evaluation-and-retention.md) — theory: reflection supplies the causal path, not the change loop that finds, accepts, and empowers a modification
- [closure under recommendations bounds methodology-governed self-extension](./closure-under-recommendations-bounds-governed-self-extension.md) — theory: the stronger condition — whether a methodology settles the form, verification, and authority decisions its own recommendations raise
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — comparison: the proof-governed corner of the design space, and what fallible-oracle systems reach that it cannot
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — case: the classification discharged against an observed repository trace

### Rationale and design method

- [design rationale management in Commonplace](../reference/design-rationale-management.md) — descriptive companion: how workshops, proposals, ADRs, and contracts distribute constraints, alternatives, and decisions—and what continuity shipped contracts do not enforce
- [Alexander's patterns connect to knowledge system design at multiple levels](./alexander-patterns-and-knowledge-system-design.md) — (speculative) pattern language as document types, generative processes as codification

- [agent context is constrained by soft degradation not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — the binding constraint is the soft degradation curve, not the hard token limit; agents are in the same soft-bound family as human cognition and organizational learning
- [soft-bound traditions as sources for context engineering strategies](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — catalog of twelve traditions with transfer assessment: what's already working, what's plausible, what's aspirational
