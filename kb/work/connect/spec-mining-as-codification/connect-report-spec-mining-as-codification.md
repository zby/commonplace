# Connection Report: Spec mining is codification's operational mechanism

**Source:** [spec-mining-as-codification](kb/notes/spec-mining-as-codification.md)
**Date:** 2026-03-09
**Depth:** standard

**Note type:** text (no frontmatter). Candidate for `/convert` to add frontmatter with `status: seedling`.

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md (141 entries). Flagged 17 candidates based on description relevance:
  - [codification](kb/notes/codification.md) — definition note that this operationalizes
  - [constraining](kb/notes/constraining.md) — sister concept on same spectrum
  - [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — reverse direction (when to un-codify)
  - [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — the trade-off spec mining enacts
  - [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) — mined specs become enforcement artifacts
  - [error-correction-works-above-chance-oracles-with-decorrelated-checks](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — mined specs become oracle checks
  - [automated-tests-for-text](kb/notes/automated-tests-for-text.md) — mined specs could become tests
  - [deterministic-validation-should-be-a-script](kb/notes/deterministic-validation-should-be-a-script.md) — end product of spec mining
  - [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — spec mining produces inspectable artifacts
  - [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — oracle hardening is what spec mining achieves
  - [unified-calling-conventions-enable-bidirectional-refactoring](kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md) — enables the codify/relax cycle that spec mining feeds
  - [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) — spec mining reduces underspecification
  - [legal-drafting-solves-the-same-problem-as-context-engineering](kb/notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) — law mines precedent from cases (analogous process)
  - [learning-is-not-only-about-generality](kb/notes/learning-is-not-only-about-generality.md) — spec mining trades generality for reliability
  - [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) — spec mining as one automation mechanism
  - [quality-signals-for-kb-evaluation](kb/notes/quality-signals-for-kb-evaluation.md) — metamorphic relations section explicitly cites spec mining
  - [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md) — simplest constraining; spec mining is the more structured version

**Topic indexes:**
- Read [learning-theory](kb/notes/learning-theory-index.md) — source note already listed in Constraining section. Additional candidates from index structure: error-correction, reliability-dimensions, inspectable-substrate (already flagged). The index's Applications section flagged [unified-calling-conventions](kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md) which already references spec-mining.

**Semantic search (via qmd):**
- Query "spec mining codification deterministic rules from observed behavior oracle hardening" in notes:
  - [spec-mining-as-codification](kb/notes/spec-mining-as-codification.md) (93%) — self
  - [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) (56%) — already linked from note
  - [error-correction-works-above-chance-oracles-with-decorrelated-checks](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) (47%) — strong candidate, mined specs are decorrelated checks
  - [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) (47%) — maturation trajectory mirrors spec mining process
  - [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) (46%) — spec mining resolves underspecification
  - [deploy-time-learning-is-agile-for-human-ai-systems](kb/notes/deploy-time-learning-is-agile-for-human-ai-systems.md) (44%) — weak, agile parallel is indirect
  - [learning-theory](kb/notes/learning-theory-index.md) (43%) — index, not a connection target
  - [programming-practices-apply-to-prompting](kb/notes/programming-practices-apply-to-prompting.md) (43%) — weak, surface overlap on testing
  - [constraining](kb/notes/constraining.md) (43%) — parent mechanism
  - [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md) (41%) — already links back to spec-mining
  - [codification](kb/notes/codification.md) (39%) — definition note, already linked
  - [distillation](kb/notes/distillation.md) (38%) — weak, spec mining is constraining not distillation
  - [title-as-claim-enables-traversal-as-reasoning](kb/notes/title-as-claim-enables-traversal-as-reasoning.md) (37%) — rejected, no genuine connection
- Query "spec mining codification extracting deterministic verifiers from failures" in sources:
  - [harness-engineering-is-cybernetics](kb/sources/harness-engineering-is-cybernetics-2030416758138634583.ingest.md) (88%) — strong, externalized judgment as oracle manufacturing aligns with spec mining
  - No other hits above threshold

**Keyword search:**
- `rg "crystallis|spec mining" kb/notes/ kb/sources/` — 48 notes files, 5 sources files. Confirmed coverage of all candidates already found via index + semantic search. No new candidates surfaced.
- `rg "spec-mining-as-codification" kb/` — 12 files already link to the target note (listed in backlinks check).

**Link following:**
- From [codification](kb/notes/codification.md): links to constraining, distillation, deploy-time-learning, oracle-strength-spectrum, spec-mining. All already in scope.
- From [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md): has a "Connection to spec mining" section that explicitly describes the workflow: observe failure -> classify by reliability dimension -> mine a spec -> oracle hardens. This note already links to spec-mining.
- From [unified-calling-conventions-enable-bidirectional-refactoring](kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md): describes spec-mining as step 2 of the codify-via-unified-calling workflow. Already links to spec-mining.
- From [quality-signals-for-kb-evaluation](kb/notes/quality-signals-for-kb-evaluation.md): metamorphic relations section cites spec mining applied to KB structure. Already links to spec-mining.
- From [agent-behavioral-contracts](kb/sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md): extractable value item 6 names ContractSpec DSL as a "spec-mining target" format. Already links to spec-mining.

## Connections Found

### Already linked (from/to the target note)

The note already contains outbound links to three notes:
- [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — codification is defined there
- [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md) — spec mining converts blurry zone to calculator regime
- [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) — spec mining moves components toward hard oracle

The following notes already have inbound links to the target:
- [codification](kb/notes/codification.md), [learning-theory](kb/notes/learning-theory-index.md), [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md), [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md), [unified-calling-conventions-enable-bidirectional-refactoring](kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md), [quality-signals-for-kb-evaluation](kb/notes/quality-signals-for-kb-evaluation.md), [agent-behavioral-contracts ingest](kb/sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md), [towards-a-science-of-ai-agent-reliability ingest](kb/sources/towards-a-science-of-ai-agent-reliability.ingest.md), [wikipedia-bitter-lesson ingest](kb/sources/wikipedia-bitter-lesson.ingest.md)

### New connections (not yet linked in either direction)

- [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — **complements**: Spec mining describes how to move a component into the calculator regime; the relaxing-candidate note describes how to detect when a component should move the other direction. Together they form the codify/relax cycle's operational mechanisms. The target note's "Risks" section (encoding biases as vision features) directly addresses what the relaxing-candidate note detects — if a mined spec is brittle under paraphrase or sensitive to distribution shift, it was a vision feature, not a calculator. The two notes are the push and pull of the same boundary.

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — **enables**: Spec mining manufactures new oracles; error correction amplifies existing ones. The progression is: mine a spec (create an oracle with TPR > FPR), then amplify through decorrelated repetition. The error-correction note says "first construct an oracle with TPR > FPR, then amplify" — spec mining is HOW you construct it. Each mined spec is a new check that can be added to the decorrelated-check ensemble.

- [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) — **exemplifies**: The maturation trajectory (instruction -> skill -> hook -> script) is spec mining applied to methodology. The "codification trigger" described there ("a pattern has emerged from repeated execution") is the same observation step as spec mining's "watch the system do tasks, identify repeated micro-actions." The enforcement gradient's end state (deterministic script) is exactly what spec mining produces.

- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — **grounds**: Spec mining works because the mined artifacts (deterministic functions, schema rules, unit tests) are inspectable. Chollet's worry about blackbox codebases is precisely what spec mining avoids — instead of opaque weight updates, you get reviewable, testable, revertable code. The inspectable substrate is what makes spec mining's "falsifiable mined specs" possible: you can test them, and if they break under distribution shift, you can relax them back.

- [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) — **exemplifies**: The "boiling cauldron" mutations (extract, relink, synthesise) are spec mining applied to knowledge structure rather than system behavior. The note explicitly discusses "codifiable operations" as one axis of mutation classification. Spec mining's workflow (cluster failures, find deterministic rules, write verifiers) is a concrete instantiation of the automated mutation loop the automating-KB note envisions.

- [legal-drafting-solves-the-same-problem-as-context-engineering](kb/notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) — **parallels**: Case law constraining (courts repeatedly interpreting a statute, converging on one reading) is spec mining in a legal medium — observe judicial behavior, extract the pattern, codify it. The legal note's observation that "codification is stronger constraining, not codification" maps to spec mining's partial codification step (regression tests that don't become deterministic code). And ABC's ContractSpec DSL (noted in the legal-drafting note) is a concrete target format for mined behavioral specs.

- [harness-engineering-is-cybernetics](kb/sources/harness-engineering-is-cybernetics-2030416758138634583.ingest.md) — **grounds**: The thread's core claim that the hard part is "externalizing system-specific judgment so the harness can evaluate and correct" is exactly what spec mining does — it externalizes judgment from the LLM into deterministic artifacts. The "out-evaluate, not out-implement" framing names spec mining's design philosophy: you don't need better generation, you need better verification, and spec mining manufactures the verification.

**Bidirectional candidates** (reverse link also worth adding):

- [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) <-> source — **complements**: The reverse link is valuable because someone reading the relaxing-candidate note should know that spec-mining is the inverse operation. The two notes form a matched pair describing both directions of boundary movement.

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) <-> source — **enables (reverse: feeds)**: An agent reading error-correction should know that spec mining is the oracle-manufacturing mechanism that creates the oracles error correction amplifies.

- [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) <-> source — **exemplifies (reverse: generalizes)**: The reverse link would help: "the maturation trajectory generalizes spec mining from system behavior to methodology."

## Rejected Candidates

- [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — Surface match only. The trade-off note describes the abstract framework; spec mining operates within that framework but doesn't extend or exemplify it in a way that adds decision value beyond what the existing codification->constraining chain already provides.

- [automated-tests-for-text](kb/notes/automated-tests-for-text.md) — Weak connection. Mined specs could become tests, but the automated-tests-for-text note is about testing KB note artifacts, not about testing system behavior. The overlap is "testing" as a concept, not a genuine semantic relationship.

- [deterministic-validation-should-be-a-script](kb/notes/deterministic-validation-should-be-a-script.md) — Too narrow. The note is a concrete KB-specific decision about moving validation checks to a script. Spec mining is the general mechanism; this is one possible end product. The connection path through codification is sufficient.

- [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) — Indirect. Spec mining reduces underspecification, but the relationship is through codification, which already links to that note. Adding a direct link would create a redundant path without decision value.

- [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md) — Too loose. Storing an output is the simplest constraining; spec mining is a structured process. The connection is "both constrain" which is already captured by the codification->constraining chain.

- [deploy-time-learning-is-agile-for-human-ai-systems](kb/notes/deploy-time-learning-is-agile-for-human-ai-systems.md) — Surface level. The agile parallel to spec mining (iterative extraction from observed behavior) is real but indirect. The connection through deploy-time-learning-the-missing-middle is already established.

- [learning-is-not-only-about-generality](kb/notes/learning-is-not-only-about-generality.md) — Generic. Spec mining trades generality for reliability, but so does all codification. No added decision value beyond the existing chain.

## Index Membership

- [learning-theory](kb/notes/learning-theory-index.md) — Already listed in the Constraining section. No change needed.
- [kb-design](kb/notes/kb-design-index.md) — Not currently a member. Should NOT be added: spec mining is a general mechanism, not KB-design-specific. Its KB applications are reached through quality-signals and automating-kb-learning.

## Synthesis Opportunities

**Codify/relax operational pair.** The target note (spec mining = how to codify) and [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) (how to detect when to relax) together describe both directions of the boundary. A synthesis note could articulate the complete operational cycle: mine -> codify -> monitor relaxing signals -> if triggered, relax -> re-observe -> re-mine. Neither note alone captures this cycle; codification.md mentions the cycle abstractly but doesn't provide operational mechanisms for both directions. This would concretize the constrain/relax cycle at the mechanism level.

**Oracle manufacturing pipeline.** The target note (spec mining creates oracles), [error-correction-works-above-chance-oracles-with-decorrelated-checks](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) (error correction amplifies oracles), and [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md) (reliability dimensions target specific oracles) together describe a complete pipeline: identify which oracle to harden (reliability dimensions) -> mine a spec for it (spec mining) -> amplify through decorrelated repetition (error correction). No note currently describes this three-step pipeline end-to-end.

## Flags

- **Text file:** The target note has no frontmatter. It should be converted to a note with `status: seedling` and a description, and placed in the `learning-theory` area. It already has well-developed structure and argumentation.
- **Tension:** The target note's "Risks" section (encoding biases) is addressed by [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) but neither note cross-references the other. This is a gap worth closing.
