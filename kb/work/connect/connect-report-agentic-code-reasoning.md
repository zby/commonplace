# Connection Report: Agentic Code Reasoning

**Source:** [Agentic Code Reasoning](../../sources/agentic-code-reasoning.md)
**Date:** 2026-03-09
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md — flagged 10 candidates from full scan:
  - [structure-activates-higher-quality-training-distributions](../../notes/structure-activates-higher-quality-training-distributions.md) — structured templates steering generation quality
  - [structured-output-is-easier-for-humans-to-review](../../notes/structured-output-is-easier-for-humans-to-review.md) — separated sections enable independent review
  - [constraining](../../notes/constraining.md) — semi-formal templates as interpretation-space narrowing
  - [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) — templates as enforcement mechanism
  - [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — verification accuracy relates to oracle theory
  - [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — templates correcting shared failure modes
  - [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) — semi-formal reasoning as interpretation narrowing
  - [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — execution-free verification as oracle replacement
  - [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — semi-formal certificates as inspectable reasoning
  - [codification-and-relaxing-navigate-the-bitter-lesson-boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — templates vs end-to-end scaling

**Topic indexes:**
- Read [learning-theory](../../notes/learning-theory-index.md) via oracle-strength-spectrum links — confirmed oracle-strength and error-correction candidates
- Read [type-system](../../notes/type-system-index.md) via structure-activates note links — confirmed the three independent arguments for structured types cluster

**Semantic search:** (via qmd)
- query "structured reasoning templates improve LLM code analysis verification accuracy" — top hits:
  - [structure-activates-higher-quality-training-distributions](../../notes/structure-activates-higher-quality-training-distributions.md) (93%) — strong match, directly about structured templates improving output quality
  - [index.md](../../notes/index.md) (55%) — skip, already scanned
  - [generate-instructions-at-build-time](../../notes/generate-instructions-at-build-time.md) (45%) — weak, about template generation not reasoning templates
  - [legal-drafting-solves-the-same-problem-as-context-engineering](../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) (44%) — evaluated, shared theme (structured specifications) but connection is too generic
  - [programming-practices-apply-to-prompting](../../notes/programming-practices-apply-to-prompting.md) (43%) — evaluated below
  - [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) (39%) — already flagged from index
  - [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) (38%) — already flagged

- query "semi-formal reasoning structured prompting certificates execution tracing" (sources collection) — top hits:
  - [agentic-code-reasoning.md](../../sources/agentic-code-reasoning.md) (93%) — self-match
  - [convexbench-can-llms-recognize-convex-functions.ingest.md](../../sources/convexbench-can-llms-recognize-convex-functions.ingest.md) (38%) — evaluated, both show structured process > free-form reasoning
  - [towards-a-science-of-ai-agent-reliability.ingest.md](../../sources/towards-a-science-of-ai-agent-reliability.ingest.md) (34%) — evaluated, reliability framework applicable to verification

**Keyword search:**
- grep "semi-formal|structured reasoning|chain.of.thought|execution-free verification" in kb/notes/ — no matches (these terms are specific to the paper, not used in KB notes)

**Link following:**
- From structure-activates → human-writing-structures, structured-output, why-notes-have-types — confirmed the three-argument cluster for structured types
- From oracle-strength-spectrum → error-correction, spec-mining, reliability-dimensions — confirmed oracle-theory cluster
- From agentic-systems-interpret-underspecified-instructions → constraining, codification — confirmed constraining/interpretation-narrowing cluster

## Connections Found

### Notes

- [structure-activates-higher-quality-training-distributions](../../notes/structure-activates-higher-quality-training-distributions.md) — **exemplifies**: The paper provides direct empirical evidence for this note's thesis. Semi-formal reasoning templates (requiring premises, execution traces, formal conclusions) improve accuracy by 5-12pp across three code reasoning tasks. The paper's mechanism — templates steering the agent toward rigorous systematic analysis rather than heuristic guessing — is precisely the distribution-selection effect this note describes. The note is a seedling seeking evidence; this paper provides quantitative support. Notably, the note's status caveat ("past experience with structured-claim type showed that imposing structure can degrade quality") finds a partial echo in the paper's finding that for Sonnet, semi-formal reasoning does not improve over standard agentic reasoning (84.8% vs 85.3% on code QA), suggesting model capability is a boundary condition.

- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — **exemplifies**: The paper documents specific human-like failure modes that structured templates correct: making unsupported assumptions about function behavior (guessing from names), skipping case enumeration, and dismissing subtle differences — all recognizably human reasoning failures. The semi-formal template corrects these by forcing explicit evidence at each step, exactly the mechanism this note predicts (separating evidence from warrant prevents conflation). The paper's chain-of-thought comparison (standard CoT < semi-formal) parallels the note's observation that CoT reduces content bias.

- [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) — **extends**: Semi-formal reasoning templates are a concrete, measured interpretation-narrowing mechanism. The paper's "standard reasoning" (minimal prompt, no structural constraints) is maximally underspecified — the agent chooses how to reason. Semi-formal templates constrain the interpretation space by requiring specific sections (premises, per-test execution traces, formal conclusions). The 10pp accuracy gain measures the value of that narrowing. This is the note's "narrowing the interpretation space" principle with quantitative evidence.

- [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — **grounds**: The paper works in a domain with hard oracles (test execution determines ground truth) but positions LLM verification as a cheaper substitute. Semi-formal LLM reasoning at 93% accuracy is a soft oracle attempting to approximate the hard oracle. The paper's error analysis (incomplete tracing, third-party semantics, dismissing subtle differences) characterizes the gap between the soft oracle and the hard one — what the remaining 7% of errors look like. This is a concrete data point for the oracle-strength gradient.

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — **enables**: The paper establishes that semi-formal LLM verification has discriminative power (93% accuracy, well above the 50% random baseline). This means it satisfies the TPR > FPR condition for error correction amplification. The paper does not explore voting/repetition, but the error correction framework predicts that multiple semi-formal verification runs with decorrelated prompts could push accuracy beyond 93%. The three failure modes identified (incomplete tracing, third-party semantics, dismissing subtle differences) suggest decorrelation strategies: varying which code paths to trace first, varying the level of detail required.

- [structured-output-is-easier-for-humans-to-review](../../notes/structured-output-is-easier-for-humans-to-review.md) — **exemplifies**: The paper explicitly describes semi-formal certificates as designed to be "easier to manually validate than examining full agent trajectories." The structured format (premises, per-test traces, formal conclusion) turns holistic verification into focused checks: Are the premises correct? Does the trace cover all relevant paths? Does the conclusion follow? This is exactly the separated-sections-enable-independent-review mechanism this note describes.

- [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) — **exemplifies**: Semi-formal reasoning templates are methodology enforcement applied to code reasoning agents. The template constrains how the agent reasons (must state premises, must trace execution paths, must derive formal conclusions), not just what it outputs. This sits at the "skill" level of the enforcement gradient — deterministic invocation (the template is in the prompt) with underspecified response (the LLM fills in the sections). The paper's error analysis shows the template doesn't fully eliminate underspecification (the agent still sometimes makes incomplete traces), consistent with this note's prediction that skill-level enforcement leaves the response indeterministic.

**Bidirectional candidates** (reverse link also worth adding):
- [structure-activates-higher-quality-training-distributions](../../notes/structure-activates-higher-quality-training-distributions.md) <-> source — bidirectional: the source provides evidence the note needs; the note provides theoretical grounding for why the source's templates work.
- [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) <-> source — bidirectional: the source provides a measured instance of interpretation-narrowing; the note provides the theoretical framework that explains the mechanism.

### Sources

- [ConvexBench ingest](../../sources/convexbench-can-llms-recognize-convex-functions.ingest.md) — **synthesizes**: Both sources independently demonstrate that structured process constraints outperform free-form reasoning. ConvexBench shows this for symbolic compositional reasoning (convexity verification); this paper shows it for semantic code reasoning (patch equivalence, fault localization, code QA). The shared mechanism is: imposing structure on the reasoning process — not just the output format — recovers performance that unconstrained reasoning loses. Together they suggest a cross-domain principle: structured reasoning frameworks consistently outperform free-form approaches on tasks requiring deep multi-step analysis. (Already noted in ConvexBench ingest.)

- [Towards a Science of AI Agent Reliability](../../sources/towards-a-science-of-ai-agent-reliability.md) — **enables**: The reliability dimensions framework (consistency, robustness, predictability, safety) can be applied to evaluate the semi-formal verification approach. The paper's 93% accuracy is a consistency measurement; the error analysis reveals robustness gaps (third-party semantics, subtle differences). The semi-formal template is itself a reliability intervention — it improves consistency (structured output format) and predictability (explicit reasoning traces enable failure diagnosis).

## Rejected Candidates

- [legal-drafting-solves-the-same-problem-as-context-engineering](../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) — Surface-level overlap (both about structured specifications for interpretation-narrowing), but the connection is too generic. Legal drafting's specific techniques (defined terms, canons of interpretation, precedent) don't map to semi-formal reasoning templates in a way that yields insight beyond "both use structure."

- [generate-instructions-at-build-time](../../notes/generate-instructions-at-build-time.md) — qmd scored 45%, but the note is about generating operational skills from templates at setup time, not about using templates to structure reasoning. Different sense of "template."

- [programming-practices-apply-to-prompting](../../notes/programming-practices-apply-to-prompting.md) — Semi-formal reasoning templates could be seen as "programming practices applied to agent reasoning," but the note focuses on testing, typing, and version control transfer, not on structured reasoning formats. The connection is too indirect to pass the articulation test.

- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — Semi-formal certificates produce inspectable reasoning traces, but the note's core argument is about repo artifacts (code, configs, tests) being inspectable vs neural network weights being opaque. The paper's certificates are more about improving agent accuracy than about inspectability as a system property. Connection exists but is tangential.

- [codification-and-relaxing-navigate-the-bitter-lesson-boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — Semi-formal templates could be framed as "partial codification of reasoning methodology," but the paper does not discuss the tension between structured approaches and scaling. The connection is speculative.

- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — The paper notes semi-formal mode uses 2.8x more steps than standard. This relates to context cost, but the paper doesn't frame the trade-off in context-efficiency terms — the additional steps are treated purely as a cost against accuracy gains. The connection is observational, not analytical.

- [spec-mining-as-codification](../../notes/spec-mining-as-codification.md) — Semi-formal templates could be seen as a pre-mined spec for reasoning methodology, but the paper's templates are designed a priori from the task structure, not mined from observed failures. The analogy doesn't hold tightly enough.

- [reliability-dimensions-map-to-oracle-hardening-stages](../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — Applicable at one level of remove (via the reliability source), but the note's specific mapping of four dimensions to oracle-hardening moves does not gain much from this paper specifically. The paper's contribution is a specific intervention, not a reliability framework.

## Index Membership

- [learning-theory](../../notes/learning-theory-index.md) — The paper's main contributions (oracle replacement, structured reasoning as interpretation-narrowing) connect to the learning theory cluster via oracle-strength-spectrum and constraining.
- [type-system](../../notes/type-system-index.md) — The paper provides evidence for the structured-types cluster (structure-activates, human-writing-structures, structured-output) but is a source, not a note — its membership would be through the notes it exemplifies.

## Synthesis Opportunities

1. **"Structured reasoning frameworks consistently outperform free-form approaches on deep multi-step analysis tasks."** Three sources converge: this paper (code reasoning: 5-12pp gains), ConvexBench (symbolic reasoning: F1 0.2->1.0 recovery), and MAKER (execution tasks: zero errors over 1M steps). All impose process structure on reasoning, and all show gains across different domains. No note in the KB currently states this cross-domain principle. Contributing sources: agentic-code-reasoning, ConvexBench ingest, MAKER ingest. Contributing notes: structure-activates-higher-quality-training-distributions, human-writing-structures-transfer-to-llms-because-failure-modes-overlap.

2. **"Semi-formal verification satisfies the conditions for error-correction amplification."** The paper establishes TPR > FPR (93% accuracy vs 50% baseline). The error-correction note provides the amplification theory. The three failure modes (incomplete tracing, third-party semantics, dismissing subtle differences) suggest decorrelation strategies. No note currently connects these to predict achievable accuracy with voting. Contributing: agentic-code-reasoning, error-correction note, oracle-strength-spectrum.

## Flags

- The ingest file (../../sources/agentic-code-reasoning.ingest.md) already identifies 7 connections that substantially overlap with what this report finds. Five of the seven ingest connections match connections found here: structure-activates, human-writing-structures, agentic-systems-interpret, oracle-strength-spectrum, context-efficiency. The ingest's existing analysis is thorough and well-articulated.
- No split candidate detected — the source is focused on a single intervention (semi-formal reasoning) with variations across tasks.
- Tension: The paper claims execution-free verification is cheaper than running tests, but the ingest correctly notes this cost argument is asserted, not demonstrated. The oracle-strength-spectrum note predicts this tension: soft oracles substitute for hard oracles only when the cost differential justifies the accuracy gap.
