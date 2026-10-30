# Handoff brief as received (2026-10-30)

Retained verbatim as the originating brief. It was written in an external
ChatGPT session and adopted by the operator as a research direction, not as
doctrine. Its instructions to revise library notes directly are overridden by
the operator's decision to work in this workshop first; see the
[README](./README.md).

---

# Auftragstaktik: Develop the economic foundation of open-ended knowledge work

## Objective

Develop the emerging theory of **open-ended knowledge work as recursive resource allocation under uncertainty** within Commonplace.

The longer-term goal is to establish a stronger theoretical foundation for Commonplace as an incremental route toward a general computational environment. We want to explain why supporting the economical management of provisional commitments could provide a cohesive, reusable foundation for many different kinds of intellectual work.

This is a research task, not a terminology migration or an instruction to implement new machinery. Investigate the implications, reconcile them with existing theory, and retain the strongest results in the KB.

## Starting hypothesis

Open-ended knowledge work is a recursive process of allocating bounded resources under uncertainty.

Workers make provisional commitments about what to believe, investigate, construct, or pursue. These commitments are guided by conjectures about their value relative to alternative uses of resources.

The conjectures need not be explicit, quantitative, or expressible as expected utilities. They may be qualitative judgments made under substantial uncertainty.

Workers learn from the consequences of their commitments, revise them, and retain useful results. Decisions about how to investigate, evaluate, and improve the working methods are themselves instances of the same process.

This suggests that economic reasoning may provide a more general organizing principle for knowledge work than epistemology alone.

However, economic allocation by itself is too broad: nearly all purposeful activity allocates scarce resources. Investigate what distinguishes the kind of open-ended, cumulative, knowledge-dependent work that Commonplace is intended to support.

## Research directions

Explore the following questions, treating them as starting points rather than a prescribed outline.

### 1. The nature of commitments

Examine the relationship between epistemic commitments, practical commitments, and the economic conjectures that justify investing resources.

Build on the existing distinction between explanatory and constructive commitments. Determine whether resource allocation is another kind of commitment, an operation governing commitments, or a separate conceptual layer.

Pay attention to differences between considering, adopting, acting upon, maintaining, and retracting commitments. Avoid collapsing a claim about truth into a decision about what is worthwhile.

### 2. Bounded rationality and the economics of investigation

Investigate connections to bounded rationality, metareasoning, value of information, opportunity cost, and resource-rational decision-making.

A key question is how workers decide when to investigate further and when to act despite uncertainty.

Do not assume numerical probabilities or utilities can always be estimated. Investigate what remains useful when economic judgments are qualitative and fallible.

### 3. Recursion and reflective improvement

An investigation is an investment justified by a conjecture. Selecting the investigation method is another investment. Improving that method is yet another.

Examine how these levels interact, including cases where discoveries change higher-level goals rather than merely advance them.

Connect this to Commonplace's existing work on reflective systems, learning software factories, and the principle that long-run learning strategies invest in their own machinery.

### 4. General operations for open-ended work

Revisit the question of whether a small set of composable operations can support a broad range of knowledge-work procedures.

Start with the existing theory-refinement-interface investigation rather than inventing a competing interface.

Explore scientific investigation, software architecture, legal drafting, exploration, and the design of the procedures used for those activities.

Distinguish two questions:

- Can the operations express these procedures?
- Does their reuse help bounded workers perform these procedures more economically?

Avoid declaring universality on the strength of examples.

### 5. Cumulative progress and revision

Investigate how retaining knowledge, decisions, rationales, experiments, and outcomes enables work to accumulate across bounded episodes.

Connect this to the existing accounts of backtracking, design rationale, discovery, revision history, and the commitment-versus-derivation boundary.

Consider the economics of retention itself: not everything is worth storing indefinitely, and different kinds of retained information have different future value.

### 6. Why this is an economical architecture for Commonplace

Keep two conjectures distinct:

**Work-level conjecture:** Managing provisional commitments recursively is an economical approach to open-ended work under bounded resources.

**Architecture-level conjecture:** Reusable computational support for this process offers an economical route toward a general computational environment.

The second does not follow automatically from the first.

Examine why starting with explicit knowledge management is a good strategy. In particular, consider the possibility that a relatively small shared interface can support a large variety of useful procedures, reducing duplication while permitting domain-specific extensions.

Identify what evidence would support or defeat that conjecture. Consider reuse across domains, implementation complexity, human judgment required, reliability, and the cost of managing the shared abstractions.

## Integration with the existing KB

Read the current GitHub source, not just the published site, which may be cached.

Start with `kb/index.md`, `AGENTS.md`, the theory and reference collections, and the relevant workshops. In particular, inspect existing material on:

- Explanatory and constructive commitments, and the commitment/derivation distinction.
- Theory builders, discovery, criticism, and addressable theories.
- Theory refinement and its proposed operations.
- Bounded context and agentic computation.
- Reflective improvement and investment in the system's machinery.
- Design rationale, backtracking, and retention.
- Commonplace as an instrument for testing general architectural principles.

Search for other relevant material before creating new notes.

Develop new theory notes where they add genuinely new mechanisms or arguments. Revise existing notes where the emerging account clarifies or extends them. Preserve useful distinctions already established.

Use a workshop for unresolved conceptual problems. Do not turn speculative conclusions into adopted doctrine or implement a generalized commitment store prematurely.

Update navigation and the project overview only insofar as the developed argument warrants it.

## Research discipline

Treat this proposal as a conjecture, not a conclusion to defend.

Look for counterexamples, existing theoretical frameworks that explain the same phenomena, and situations where the proposed generalization introduces more complexity than it saves.

Distinguish established results, arguments, design hypotheses, and empirical claims awaiting tests.

The aim is not to maximize the number of notes. Prefer a small, coherent set of substantial improvements with clear relationships to the existing theory.

## Desired outcome

The KB should emerge with:

1. A coherent explanation of the relationship between bounded workers, provisional commitments, economic reasoning, and cumulative knowledge work.
2. A clearer account of how this framework extends, rather than replaces, the project's Popperian theory-building foundations.
3. A research direction for discovering and testing general operations that could support such work.
4. A stronger, independently understandable economic argument for Commonplace's development strategy.
5. Explicit open questions and discriminating tests, including what would show that the proposed generalization is not worthwhile.

The central question to keep in view is:

**Can we build reusable computational machinery that makes open-ended intellectual work more economical for bounded workers, while allowing the machinery itself to improve through the same process?**

Develop the argument before committing to the architecture. Let the existing Commonplace system serve as the first case through which the theory is criticized and refined.
