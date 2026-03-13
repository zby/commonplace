# Connection Report: Constraining

**Source:** [test-constraining-stripped](kb/work/connect-refactoring/test-constraining-stripped.md)
**Date:** 2026-03-03
**Depth:** standard

## Discovery Trace

**Index exploration:**
- Read [learning-theory](../../notes/learning-theory-index.md) -- found candidates: [codification](../../notes/codification.md), [distillation](../../notes/distillation.md), [deploy-time-learning-the-missing-middle](../../notes/deploy-time-learning-the-missing-middle.md), [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](../../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md), [storing-llm-outputs-is-constraining](../../notes/storing-llm-outputs-is-constraining.md), [constraining-during-deployment-is-continuous-learning](../../notes/constraining-during-deployment-is-continuous-learning.md), [spec-mining-as-codification](../../notes/spec-mining-as-codification.md), [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md), [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md), [unified-calling-conventions-enable-bidirectional-refactoring](../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md), [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md), [operational-signals-that-a-component-is-a-relaxing-candidate](../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md), [learning-is-not-only-about-generality](../../notes/learning-is-not-only-about-generality.md), [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md)

**Semantic search:** qmd unavailable, grep-only discovery

**Keyword search:**
- grep "stabilis" -- 50 files; top candidates already covered by index exploration
- grep "distillation" -- 23 files; all relevant ones covered by index
- grep "crystallis" -- 44 files; all relevant ones covered by index
- grep "interpretation.?space|underspecif" -- 25 files; [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) confirmed as key connection
- grep "relaxing|relax" -- 25 files; [operational-signals-that-a-component-is-a-relaxing-candidate](../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) found as specific extension
- grep "bitter.?lesson" -- 12 files; [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) confirmed
- grep "learning.?mechanism|deploy.?time.?learning" -- 35 files; no new candidates beyond index

**Description scan:**
- Scanned descriptions of all candidate notes. No additional candidates surfaced beyond index + keyword results.

**Link following:**
- From [codification](../../notes/codification.md): links to [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) (determines what can codify) and [spec-mining-as-codification](../../notes/spec-mining-as-codification.md) (operational mechanism). Both already in candidate set.
- From [distillation](../../notes/distillation.md): links to [skills-derive-from-methodology-through-distillation](../../notes/skills-derive-from-methodology-through-distillation.md). Evaluated: relevant to distillation, not directly to the constraining definition note.
- From [operational-signals-that-a-component-is-a-relaxing-candidate](../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md): links back to [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) and [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md). Both already evaluated.

## Connections Found

### Core definitional connections

- [codification](../../notes/codification.md) -- **extends**: codification is the far end of the constraining spectrum, the point where constraining the interpretation space crosses a medium boundary from natural language to executable code; the target note explicitly defines codification as "what constraining looks like when it crosses a medium boundary"
- [distillation](../../notes/distillation.md) -- **contrasts/complements**: the co-equal orthogonal learning mechanism; the target devotes a full section to the 2x2 matrix showing that constraining (how constrained?) and distillation (was it extracted?) operate on independent dimensions of the same artifacts
- [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) -- **grounds**: provides the theoretical foundation for "interpretation space" that constraining operates on; the spec-to-program projection model and the concept of semantic underspecification are what constraining constrains

### Framework connections

- [deploy-time-learning-the-missing-middle](../../notes/deploy-time-learning-the-missing-middle.md) -- **grounds**: the organizing framework within which constraining operates as one of two mechanisms; provides the verifiability gradient that structures the constraining spectrum from prompt tweaks to deterministic code
- [learning-is-not-only-about-generality](../../notes/learning-is-not-only-about-generality.md) -- **grounds**: defines the capacity decomposition (generality vs reliability+speed+cost compound) that constraining trades on; the "compound" terminology in the constraining spectrum table derives from this decomposition
- [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](../../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) -- **extends**: articulates the specific trade-off that every constraining step enacts -- generality sacrificed for compound gains; develops the comparison with distillation's parallel trade-off

### Lifecycle and dynamics

- [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) -- **extends**: determines the lifecycle dynamics of constraining; when the spec IS the problem (calculators), constraining is permanent; when the spec approximates the problem (vision features), relaxing is eventually needed
- [operational-signals-that-a-component-is-a-relaxing-candidate](../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) -- **extends**: operationalises the relaxing half of the constrain/relax cycle described in the target note's "Relaxing" section; provides testable signals (paraphrase brittleness, isolation-vs-integration gap, process constraints) for detecting when a constrained component is a relaxing candidate

### Instances and applications

- [storing-llm-outputs-is-constraining](../../notes/storing-llm-outputs-is-constraining.md) -- **exemplifies**: the simplest instance on the constraining spectrum; storing one LLM output commits to a single interpretation and freezes it against indeterminism; develops the generator/verifier pattern as an alternative to constraining the prompt
- [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) -- **exemplifies**: applies the constraining spectrum to methodology enforcement rather than code/artifacts; the instruction -> skill -> hook -> script gradient parallels the constraining gradient, trading flexibility for reliability
- [spec-mining-as-codification](../../notes/spec-mining-as-codification.md) -- **extends**: provides the operational mechanism for how the far end of the spectrum works in practice -- observe behavior, extract deterministic rules, grow the calculator surface monotonically
- [constraining-during-deployment-is-continuous-learning](../../notes/constraining-during-deployment-is-continuous-learning.md) -- **extends**: connects constraining to AI labs' continuous learning concept; argues that constraining with versioned artifacts constitutes genuine continuous learning per Simon's definition

### Enabling architecture

- [unified-calling-conventions-enable-bidirectional-refactoring](../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md) -- **enables**: makes the constrain/relax cycle a local operation by providing stable call sites; without unified calling, each constraining step is a breaking change requiring call-site updates
- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) -- **extends**: argues that constraining to repo artifacts (the inspectable substrate) defeats Chollet's blackbox concern not through human supervision but through the diffable, testable nature of the artifacts themselves

**Bidirectional candidates** (reverse link also worth adding):
- Most of the above notes already link back to the real [constraining.md](../../notes/constraining.md). The bidirectional graph is well-established for this hub note.

## Rejected Candidates

- [writing-styles-are-strategies-for-managing-underspecification](../../notes/writing-styles-are-strategies-for-managing-underspecification.md) -- writing styles manage the interpretation space for instructions, but the relationship to the constraining *definition* note is indirect; the connection is to the underspecified-instructions note, not to constraining itself
- [programming-practices-apply-to-prompting](../../notes/programming-practices-apply-to-prompting.md) -- mentions constraining as one of several practices, but the connection to the definition note is indirect; connects more directly to deploy-time-learning and the computational model
- [ad-hoc-prompts-extend-the-system-without-schema-changes](../../notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md) -- represents the counterpoint (staying underspecified rather than constraining), but the relationship is implicit rather than direct
- [legal-drafting-solves-the-same-problem-as-context-engineering](../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) -- mentions constraining but is primarily about the law/engineering parallel; the connection is to the underspecified-instructions framing, not constraining per se

## Index Membership

- Already member of: [learning-theory](../../notes/learning-theory-index.md) -- correctly listed in the "Constraining" section as the definition note
- No additional index membership needed. The note's area `[learning-theory]` is correct and sufficient.

## Synthesis Opportunities

None detected. The constraining concept is well-developed with clear connections already identified. The 2x2 matrix (constrained x distilled) in the target note IS a synthesis that already exists.

## Flags

- **Hub note detection**: This note connects to 14 notes across the knowledge base. However, this is expected and appropriate -- it is a *definition* note for one of two core learning mechanisms. All connections serve the same domain (learning-theory). No split candidate.
- **Note on the test context**: The test note is a stripped version of `../../notes/constraining.md` (no inline links, no Relevant Notes section). The real `../../notes/constraining.md` already has these connections established as inline links. This report confirms the connections that the real note should have.
