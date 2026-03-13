# Connection Report: Frontloading spares execution context

**Source:** [frontloading spares execution context](../../notes/frontloading-spares-execution-context.md)
**Test file:** kb/work/connect-refactoring/test-frontloading-stripped.md
**Date:** 2026-03-03
**Depth:** standard

## Discovery Trace

**Index exploration:**
- Read [kb-design](../../notes/kb-design-index.md) — the note is already listed under Architecture. Found candidates: [indirection-is-costly-in-llm-instructions](../../notes/indirection-is-costly-in-llm-instructions.md), [generate-instructions-at-build-time](../../notes/generate-instructions-at-build-time.md), [injectable-configuration-extends-frontloading-to-installation-specific-values](../../notes/injectable-configuration-extends-frontloading-to-installation-specific-values.md), [instruction-specificity-should-match-loading-frequency](../../notes/instruction-specificity-should-match-loading-frequency.md), [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md), [scenario-decomposition-drives-architecture](../../notes/scenario-decomposition-drives-architecture.md), [agent-statelessness-means-harness-should-inject-context-automatically](../../notes/agent-statelessness-means-harness-should-inject-context-automatically.md)
- Read [computational-model](../../notes/computational-model-index.md) — note is listed under "Related notes in other areas." Found candidates: [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md), [llm-context-is-a-homoiconic-medium](../../notes/llm-context-is-a-homoiconic-medium.md)
- Read [learning-theory](../../notes/learning-theory-index.md) — found candidates: [constraining](../../notes/constraining.md), [codification](../../notes/codification.md), [distillation](../../notes/distillation.md), [deploy-time-learning-the-missing-middle](../../notes/deploy-time-learning-the-missing-middle.md), [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](../../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md)
- Followed link from [injectable-configuration](../../notes/injectable-configuration-extends-frontloading-to-installation-specific-values.md) — it explicitly extends frontloading; confirmed bidirectional candidate

**Semantic search:** qmd unavailable, grep-only discovery

**Keyword search:**
- grep "frontload" — found 5 files linking to frontloading: [index](../../notes/index.md), [injectable-configuration](../../notes/injectable-configuration-extends-frontloading-to-installation-specific-values.md), [kb-design](../../notes/kb-design-index.md), [indirection-is-costly-in-llm-instructions](../../notes/indirection-is-costly-in-llm-instructions.md), [computational-model](../../notes/computational-model-index.md)
- grep "partial evaluation" — found: [computational-model](../../notes/computational-model-index.md), [kb-design](../../notes/kb-design-index.md) (both already in candidates)
- grep "execution context" — found: [deploy-time-learning-the-missing-middle](../../notes/deploy-time-learning-the-missing-middle.md), [agent-statelessness-makes-skill-layers-architectural-not-pedagogical](../../notes/agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md), [skills-derive-from-methodology-through-distillation](../../notes/skills-derive-from-methodology-through-distillation.md) (context budget theme)
- grep "indirection|build.time|crystallis|stabilis|distillation" — 64 files; filtered to those with genuine conceptual overlap

**Description scan:**
- Scanned descriptions of keyword hits. The note's core concepts (partial evaluation, context sparing, static/dynamic partition) cluster tightly around a specific set of architecture and learning-theory notes.

## Connections Found

- [indirection-is-costly-in-llm-instructions](../../notes/indirection-is-costly-in-llm-instructions.md) — **overlaps**: indirection elimination is a specific case of frontloading; the indirection note already links back to frontloading as the generalisation. Frontloading provides the broader principle (pre-compute anything static), indirection cost provides the specific cost model (every layer of indirection taxes context per read).

- [generate-instructions-at-build-time](../../notes/generate-instructions-at-build-time.md) — **overlaps**: build-time generation is the implementation pattern for frontloading applied to skill templates. Template expansion with `{{claw_root}}` is textbook PE, as the note itself states. The generate note is the "specialiser" the frontloading note refers to.

- [codification](../../notes/codification.md) — **distinguishes**: the note explicitly says "frontloading is not constraining" and that codification overlap is incidental. But the cases where frontloading produces a deterministic result (variable resolution, file listings) ARE codification — the pre-computed result happens to cross the medium boundary. The connection is about where the two principles overlap and where they diverge.

- [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: the underspecified semantics framework is what makes frontloading's PE analogy require stretching. The note explicitly references underspecified instructions as the domain PE operates in here. The "where the PE definition stretches" section is entirely about this gap.

- [instruction-specificity-should-match-loading-frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) — **motivates**: the context loading hierarchy is one response to the problem frontloading identifies. If execution context is the bottleneck, the loading strategy (slim CLAUDE.md, on-demand loading) is the architectural consequence. The existing note already has this connection.

- [injectable-configuration-extends-frontloading-to-installation-specific-values](../../notes/injectable-configuration-extends-frontloading-to-installation-specific-values.md) — **extends**: injectable configuration identifies a third frontloading channel (installation-specific values) that the frontloading note's "static/dynamic" partition doesn't explicitly cover. The injectable note explicitly builds on frontloading as its foundation. Strong bidirectional connection already present.

- [programming-practices-apply-to-prompting](../../notes/programming-practices-apply-to-prompting.md) — **exemplifies**: frontloading as PE is a direct case of applying a PL concept (partial evaluation) to the LLM instruction domain. The programming-practices note discusses progressive compilation and typing transfers; frontloading is another such transfer with a different cost model (context, not time).

- [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) — **grounds**: the note's "binding-time analysis" concept from PE maps directly to this note's claim that context is flat concatenation. Frontloading is justified partly because every token in the flat context competes for attention — the absence of scoping makes context sparing more urgent. The scoping note's section on "the context loading strategy as binding-time analysis" is the direct connection.

- [distillation](../../notes/distillation.md) — **distinguishes**: distillation extracts from a larger body of reasoning into a focused artifact. Frontloading pre-computes static sub-procedures and inserts results. Both spare context, but through different operations. Distillation is extraction shaped by a use case; frontloading is computation of known-static inputs. Worth distinguishing to prevent conflation.

- [skills-derive-from-methodology-through-distillation](../../notes/skills-derive-from-methodology-through-distillation.md) — **enables**: distillation is a context-budget operation (driven by finite context). Frontloading spares the context that distillation then operates within. The two are complementary: frontload what's computable, distil what requires judgment but is too large to load in full.

**Bidirectional candidates** (reverse link also worth adding):
- [indirection-is-costly-in-llm-instructions](../../notes/indirection-is-costly-in-llm-instructions.md) <-> source — already bidirectional in the real note
- [injectable-configuration-extends-frontloading-to-installation-specific-values](../../notes/injectable-configuration-extends-frontloading-to-installation-specific-values.md) <-> source — already bidirectional in the real note
- [programming-practices-apply-to-prompting](../../notes/programming-practices-apply-to-prompting.md) <-> source — the programming-practices note doesn't currently mention frontloading or partial evaluation as a transferred practice; adding it would strengthen the "practices we apply" section
- [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) <-> source — the scoping note already mentions binding-time analysis but doesn't link to frontloading as the note that develops that concept

## Rejected Candidates

- [constraining](../../notes/constraining.md) — the note explicitly says "frontloading is not constraining." While the mechanisms interact (some frontloading produces constraining as a side effect), the core claim is about context sparing, not interpretation-space narrowing. Linking would conflate two distinct operations.
- [deploy-time-learning-the-missing-middle](../../notes/deploy-time-learning-the-missing-middle.md) — the verifiability gradient is about how artifacts harden over time. Frontloading is about what to compute before the LLM runs. The concepts are adjacent but the connection is too indirect to be useful — they share no specific mechanism.
- [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) — the enforcement gradient (instruction -> skill -> hook -> script) doesn't relate to the static/dynamic partition that frontloading operates on. The generate-at-build-time note already connects to this for the constraining aspect.
- [scenario-decomposition-drives-architecture](../../notes/scenario-decomposition-drives-architecture.md) — mentions context loading but at a different level of abstraction (user stories, hop counts). No specific mechanism overlap with partial evaluation.
- [agent-statelessness-means-harness-should-inject-context-automatically](../../notes/agent-statelessness-means-harness-should-inject-context-automatically.md) — auto-injection is about reactive loading (based on what the agent reads), not pre-computation of static inputs. Both spare context but through fundamentally different mechanisms (reactive vs proactive).
- [llm-context-is-a-homoiconic-medium](../../notes/llm-context-is-a-homoiconic-medium.md) — homoiconicity is about the instructions/data boundary, not about the static/dynamic partition. Surface connection only.
- [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](../../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — too abstract to provide a useful link; the trade-off framework doesn't illuminate frontloading specifically.
- [directory-scoped-types-are-cheaper-than-global-types](../../notes/directory-scoped-types-are-cheaper-than-global-types.md) — shares the "context is expensive" intuition but the mechanism (type scoping) is unrelated to partial evaluation.

## Index Membership

- [kb-design](../../notes/kb-design-index.md) — already a member under Architecture. Entry describes frontloading correctly.
- [computational-model](../../notes/computational-model-index.md) — already listed under "Related notes in other areas" as a PE application. Not a full member, which is appropriate since the note's primary area is kb-design.

## Synthesis Opportunities

**Frontloading + distillation as complementary context-sparing operations.** Frontloading pre-computes static inputs to spare context. Distillation extracts focused artifacts to spare context. Together they define the two dimensions of context-budget management: compute what you can before runtime (frontloading), and compress what you can't compute (distillation). Neither note makes this claim explicitly. A synthesis note could argue that context-budget management decomposes into these two operations, with the static/dynamic partition from PE determining which applies to any given piece of context.

## Flags

- No split candidate. The note is focused on a single concept (partial evaluation applied to LLM instructions) with clear scope boundaries.
- No tensions detected.
- **Reverse link gap:** [programming-practices-apply-to-prompting](../../notes/programming-practices-apply-to-prompting.md) and [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) would benefit from reverse links to this note but currently lack them.
