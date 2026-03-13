# Connection Report: Constraining

**Source:** [constraining](kb/work/connect-refactoring/test-constraining-stripped.md)
**Date:** 2026-03-03
**Depth:** standard

## Discovery Trace

**Index exploration:**
- Read [learning-theory](../../notes/learning-theory-index.md) — the target's area index. Found candidates already listed in the Constraining section: [codification](../../notes/codification.md), [storing-llm-outputs-is-constraining](../../notes/storing-llm-outputs-is-constraining.md), [constraining-during-deployment-is-continuous-learning](../../notes/constraining-during-deployment-is-continuous-learning.md), [spec-mining-as-codification](../../notes/spec-mining-as-codification.md). Also found candidates in Deploy-time Learning section: [deploy-time-learning-the-missing-middle](../../notes/deploy-time-learning-the-missing-middle.md), [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](../../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md), [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md). Foundations: [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md), [learning-is-not-only-about-generality](../../notes/learning-is-not-only-about-generality.md). Applications: [unified-calling-conventions-enable-bidirectional-refactoring](../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md), [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md). Related areas: [document-system](../../notes/document-system-index.md).
- Followed link from [learning-theory](../../notes/learning-theory-index.md) to [distillation](../../notes/distillation.md) — co-equal mechanism mentioned in target note
- Followed link from [document-system](../../notes/document-system-index.md) to [wikiwiki-principle](../../notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) — type ladder as constraining gradient

**Semantic search:** (grep-only — qmd unavailable, MCP tools not available in this session)

**Keyword search:**
- grep "stabilis|stabiliz|interpretation space|crystallis|distillation|relaxing|bitter lesson" across kb/notes/ — returned 71 files
- Evaluated top candidates by reading full content. Key secondary discoveries:
  - [operational-signals-that-a-component-is-a-relaxing-candidate](../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — operationalises the relaxing section of the target note
  - [skills-derive-from-methodology-through-distillation](../../notes/skills-derive-from-methodology-through-distillation.md) — uses constraining as a contrast to distillation; three-way comparison table
  - [writing-styles-are-strategies-for-managing-underspecification](../../notes/writing-styles-are-strategies-for-managing-underspecification.md) — writing styles as interpretation-space narrowing, which is constraining applied to instructions
  - [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — codification as the mechanism; depends on constraining

**Link following:**
- From [codification](../../notes/codification.md) → already connected to target via parent mechanism link
- From [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) → relaxing as reverse of codification, connects to target's relaxing section
- From [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) → the "Constraining and Relaxing" section defines the same concepts; this is the theoretical foundation

## Connections Found

**Note:** The test file is a "stripped" version of the real `../../notes/constraining.md` — it has the same content but with all inline links and the Relevant Notes footer removed. The connections below are what discovery finds from the content alone.

- [codification](../../notes/codification.md) — **extends**: codification is the far end of the constraining spectrum where medium changes from natural language to executable code; the target note explicitly describes this as the last step in the spectrum table and defines it as "what constraining looks like when it crosses a medium boundary"

- [distillation](../../notes/distillation.md) — **synthesizes**: the target note's "Relationship to distillation" section defines a 2x2 matrix (constrained/not x distilled/not) establishing that the two mechanisms are orthogonal; the distillation note contains the same matrix, confirming mutual definition

- [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: the target note's core mechanism ("constrains the space of valid interpretations an underspecified spec admits") directly depends on the underspecification framework; the underspecified-instructions note defines "interpretation space" and "Constraining and Relaxing" as operations on it

- [deploy-time-learning-the-missing-middle](../../notes/deploy-time-learning-the-missing-middle.md) — **grounds**: defines the verifiability gradient that constraining operates along; the target note's spectrum table parallels the verifiability gradient table; deploy-time learning frames constraining as one of two mechanisms for system-level adaptation through repo artifacts

- [storing-llm-outputs-is-constraining](../../notes/storing-llm-outputs-is-constraining.md) — **exemplifies**: the simplest instance of constraining — keeping a specific LLM output commits to one interpretation, resolving both semantic underspecification and execution indeterminism; develops the generator/verifier pattern as an alternative strategy

- [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) — **enables**: determines when relaxing (the reverse operation described in the target note) is needed; the bitter lesson boundary is the decision criterion for the constrain/relax cycle the target describes — calculator decompositions make constraining permanent, vision-feature decompositions make it temporary

- [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](../../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — **extends**: develops the "trades generality for gains in the reliability+speed+cost compound" claim that the target note states in the constraining spectrum section; provides the full argument with concrete examples (calculator vs LLM)

- [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) — **exemplifies**: applies the constraining gradient to methodology enforcement (instruction -> skill -> hook -> script), showing the same spectrum the target note defines operating on a different substrate (practices rather than artifacts)

- [learning-is-not-only-about-generality](../../notes/learning-is-not-only-about-generality.md) — **grounds**: defines capacity decomposition into generality vs reliability+speed+cost compound; the target note's spectrum table is structured around this decomposition (each constraining step trades generality for compound gains)

- [constraining-during-deployment-is-continuous-learning](../../notes/constraining-during-deployment-is-continuous-learning.md) — **extends**: argues that the constraining the target note defines constitutes continuous learning per Simon's definition; extends the claim from "what constraining is" to "why constraining is learning"

- [spec-mining-as-codification](../../notes/spec-mining-as-codification.md) — **enables**: provides the operational mechanism for the far end of the constraining spectrum — how to discover specs from observed behavior and convert them to deterministic code

**Bidirectional candidates** (reverse link also worth adding):
- [codification](../../notes/codification.md) <-> source — already references constraining as parent mechanism
- [distillation](../../notes/distillation.md) <-> source — already has reverse link to constraining as co-equal mechanism
- [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) <-> source — already references constraining in its "Constraining and Relaxing" section
- [storing-llm-outputs-is-constraining](../../notes/storing-llm-outputs-is-constraining.md) <-> source — already references constraining as foundation
- [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) <-> source — already references constraining as foundation

## Rejected Candidates

- [operational-signals-that-a-component-is-a-relaxing-candidate](../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — discusses relaxing which is the reverse of constraining, but the relationship is indirect: this note operationalises the *bitter lesson boundary*, not constraining directly. Relaxing signals help you decide when to relax, which presupposes constraining but doesn't extend, ground, or contradict the constraining definition itself. The connection to [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) is stronger and more direct.

- [unified-calling-conventions-enable-bidirectional-refactoring](../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md) — describes how unified calling conventions make constraining and relaxing frictionless in practice. A real connection exists but it is an *application* of the mechanism, not a conceptual extension — and the note already links to constraining. Including this would not add traversal value beyond what the index already provides.

- [skills-derive-from-methodology-through-distillation](../../notes/skills-derive-from-methodology-through-distillation.md) — contains a three-way comparison table (codification / constraining / distillation) and argues that distillation is distinct from constraining. The comparison is useful but the relationship is about distinguishing terms, not connecting substantive claims. The distillation note itself is the better connection point.

- [writing-styles-are-strategies-for-managing-underspecification](../../notes/writing-styles-are-strategies-for-managing-underspecification.md) — writing styles narrow the interpretation space, which is formally constraining. But the note frames this as a property of underspecification management, not as constraining per se. The connection is mediated through [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) rather than direct.

- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — codification (the far end of constraining) is the mechanism that produces inspectable artifacts. But the connection is to codification specifically, not to constraining as a whole. Already connected via the codification note.

- [wikiwiki-principle-lowest-friction-capture-then-progressive-refinement](../../notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) — describes the type ladder as a "codification ladder for thoughts" and connects to [constraining-and-distillation-both-trade-generality-for-compound](../../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md). The connection to constraining exists but is indirect — it describes the UX of progressive refinement, which is one application of the constraining gradient. Already mediated through codification and the compound trade-off note.

- [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — oracle strength determines what can be codified (hard oracles enable it), which is relevant to the far end of constraining. But the connection is to codification specifically, not to the full constraining spectrum. Already captured via the codification note.

## Index Membership

- [learning-theory](../../notes/learning-theory-index.md) — already a member, listed under the "Constraining" section as the definition note for the mechanism
- Already member of: [learning-theory](../../notes/learning-theory-index.md)

## Synthesis Opportunities

None detected. The test note is a definitional note — it defines constraining as a mechanism and positions it relative to distillation and codification. The surrounding notes form a well-developed constellation that already covers the extensions (continuous learning), applications (methodology enforcement, stored outputs), and relationships (generality-compound trade-off). No uncaptured higher-order claim emerged from the discovery process.

## Flags

- **Note is a stripped test copy.** The real [constraining](../../notes/constraining.md) already has inline links and a Relevant Notes footer with 7 connections. The connections found here closely match the existing connections on the real note, which validates the discovery methodology — the same connections are discoverable from content alone without relying on existing links.
- **Existing vs discovered connections comparison:** The real note's Relevant Notes footer contains: codification, distillation, agentic-systems-interpret-underspecified-instructions, storing-llm-outputs-is-constraining, methodology-enforcement-is-constraining, deploy-time-learning-the-missing-middle, bitter-lesson-boundary. This discovery found all 7, plus 4 additional: constraining-and-distillation-both-trade-generality, learning-is-not-only-about-generality, constraining-during-deployment-is-continuous-learning, spec-mining-as-codification. The 4 additional are all genuine connections that the real note's Relevant Notes section could benefit from.
