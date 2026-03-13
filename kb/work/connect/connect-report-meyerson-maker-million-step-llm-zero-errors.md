# Connection Report: Solving a Million-Step LLM Task with Zero Errors

**Source:** [Solving a Million-Step LLM Task with Zero Errors](../../sources/meyerson-maker-million-step-llm-zero-errors.md)
**Date:** 2026-03-09
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md (140 entries) — flagged 12 candidates based on description relevance:
  - [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — direct match: error correction with decorrelated checks
  - [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — oracle strength determines engineering investment
  - [reliability-dimensions-map-to-oracle-hardening-stages](../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — reliability dimensions as oracle hardening
  - [symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration](../../notes/symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) — decomposition and bounded calls
  - [decomposition-rules-for-bounded-context-scheduling](../../notes/decomposition-rules-for-bounded-context-scheduling.md) — decomposition rules
  - [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) — calculator regime vs vision features
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — context as scarce resource
  - [constraining](../../notes/constraining.md) — constraining interpretation space
  - [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) — constraining gradient
  - [spec-mining-as-codification](../../notes/spec-mining-as-codification.md) — manufacturing calculators
  - [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — inspectability and auditing
  - [storing-llm-outputs-is-constraining](../../notes/storing-llm-outputs-is-constraining.md) — generator/verifier pattern

**Topic indexes:**
- Read [learning-theory](../../notes/learning-theory-index.md) — confirmed error-correction, oracle-strength, and reliability-dimensions notes as core cluster. Additional candidate: [induction-bias-sequence-models](../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) (brackets same problem from opposite direction).
- No additional candidates beyond those already flagged.

**Semantic search:** (via qmd)
- query "extreme decomposition error correction voting microagents scaling million steps" on notes:
  - [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) (93%) — already flagged, direct MAKER reference
  - [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) (50%) — already flagged
  - [evans-ai-components-deterministic-system](../../notes/related_works/evans-ai-components-deterministic-system.md) (38%) — modeling/classification maps to insights/execution
  - [reliability-dimensions-map-to-oracle-hardening-stages](../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) (35%) — already flagged
  - [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) (34%) — safety/auditing parallel
  - [voooooogel-multi-agent-future](../../notes/research/voooooogel-multi-agent-future.md) (33%) — multi-agent architecture predictions
  - [learning-theory](../../notes/learning-theory-index.md) (33%) — index already read
  - [constraining](../../notes/constraining.md) (33%) — already flagged
- query on sources:
  - [meyerson-maker (self)](../../sources/meyerson-maker-million-step-llm-zero-errors.md) (93%) — self
  - [meyerson-maker ingest](../../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) (56%) — companion ingest
  - [towards-a-science-of-scaling-agent-systems](../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) (42%) — multi-agent scaling laws
  - [induction-bias-sequence-models](../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) (38%) — transformer failure at long-range tracking
  - [towards-a-science-of-ai-agent-reliability](../../sources/towards-a-science-of-ai-agent-reliability.md) (38%) — reliability dimensions
- query "microservices modularity independent agents scalability decomposition" on notes:
  - [evans-ai-components-deterministic-system](../../notes/related_works/evans-ai-components-deterministic-system.md) (50%) — already flagged
  - [voooooogel-multi-agent-future](../../notes/research/voooooogel-multi-agent-future.md) (39%) — already flagged
  - [symbolic-scheduling-over-bounded-llm-calls](../../notes/symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) (35%) — already flagged

**Keyword search:**
- grep "MAKER|MDAP|massively decomposed|million.step|microagent" in kb/notes/ — found:
  - error-correction-works-above-chance-oracles-with-decorrelated-checks.md (3 hits) — already flagged
  - reliability-dimensions-map-to-oracle-hardening-stages.md (2 hits) — already flagged
  - No other notes reference MAKER by name.
- grep "meyerson-maker|million-step-llm" in kb/ — found 5 files:
  - The two notes above plus sources/index.md, the ingest file itself, and induction-bias-sequence-models ingest (cross-reference)

**Link following:**
- From error-correction note: followed links to oracle-strength-spectrum, reliability-dimensions, codification, spec-mining. All already flagged.
- From reliability-dimensions note: links to oracle-strength-spectrum, spec-mining, relaxing-signals. Already covered.
- From ingest file: identified 8 connections already catalogued there (reliability paper, oracle-strength, bitter-lesson, constraining, storing-llm-outputs, voooooogel, evans). All verified in this report.

## Connections Found

### Already linked (existing connections in the ingest file and notes)

The ingest file (../../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) already catalogues 8 connections. Two KB notes already link back to the source:

1. [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — **grounds**: The MAKER paper is the primary empirical grounding for this note. MAKER demonstrates voting-based error correction with hard oracles; the note generalizes the principle to soft oracles with TPR > FPR. The O(s ln s) scaling law under maximal decomposition is referenced as the cost baseline.

2. [reliability-dimensions-map-to-oracle-hardening-stages](../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — **exemplifies**: MAKER's decomposition + voting is consistency hardening; red-flagging is predictability hardening. The note explicitly identifies MAKER as "architectural oracle hardening."

### New connections (not yet linked from any note)

3. [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — **exemplifies**: MAKER succeeds because Towers of Hanoi has hard per-step oracles (each move is deterministically verifiable). The paper's own insights/execution distinction maps directly onto the oracle-strength gradient: execution has hard oracles (MAKER's domain), insights have soft oracles (acknowledged future work). The O(s ln s) cost result only holds given sufficient oracle strength. The ingest file flags this connection but the oracle-strength note itself does not yet reference MAKER.

4. [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) — **exemplifies**: MAKER is the anti-bitter-lesson bet succeeding in the calculator regime. Small non-reasoning models (gpt-4.1-mini) outperform reasoning models (o3-mini) on cost-effectiveness for execution tasks because the spec IS the problem. This is direct empirical evidence for the note's claim that "calculators survive scaling because the spec is the problem." The ingest flags this but the bitter-lesson note does not reference MAKER.

5. [symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration](../../notes/symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) — **exemplifies**: MAKER is a concrete instance of the scheduling model. The symbolic scheduler manages the task state (disk configuration), decomposes into per-step sub-goals, and assembles minimal prompts for bounded LLM calls. The scheduler itself is deterministic code; only the one-step move decisions use LLM calls. This is the clean separation the model prescribes: symbolic bookkeeping outside, bounded semantic judgment inside. The key difference: MAKER's decomposition is predetermined (recursive Hanoi structure), not discovered dynamically by the scheduler.

6. [decomposition-rules-for-bounded-context-scheduling](../../notes/decomposition-rules-for-bounded-context-scheduling.md) — **exemplifies**: MAKER's "maximal agentic decomposition" (m=1) is the extreme case of "separate selection from joint reasoning" — each agent gets only the minimal context needed for its single step. The paper's cost analysis (O(s ln s) for m=1 vs exponential for m>1) provides quantitative evidence for why aggressive decomposition into narrow calls pays off. Also exemplifies "use symbolic operations wherever exactness is available" — the Hanoi recursion structure and state tracking are symbolic, not LLM-mediated.

7. [spec-mining-as-codification](../../notes/spec-mining-as-codification.md) — **enables**: Spec mining manufactures the hard oracles that MAKER depends on. MAKER assumes per-step oracles exist; spec mining is the operational mechanism for creating them in domains where they don't exist naturally. The progression is: mine a spec (create an oracle), then MAKER-style voting amplifies it. This note already references the error-correction note's amplification mechanism; MAKER is the concrete system that demonstrates the amplification step.

8. [towards-a-science-of-scaling-agent-systems](../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) — **contradicts/complements**: Kim et al. find naive multi-agent coordination yields -3.5% mean improvement with up to 17.2x error amplification. MAKER achieves zero errors over a million steps. The difference is MAKER's extreme decomposition + voting design vs Kim et al.'s tested topologies (Independent, Centralized, Decentralized, Hybrid) which use simple coordination without deliberate decorrelation. This brackets the multi-agent question from both sides: naive coordination usually hurts, but structured error-correcting coordination can succeed spectacularly in the right domain.

9. [induction-bias-sequence-models](../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) — **complements**: Ebrahimi et al. explain WHY transformers fail at long-range state tracking (kappa near 1 for transformers, meaning knowledge at one length doesn't transfer). MAKER shows HOW to build reliable systems despite that failure via decomposition + error correction. The two papers bracket the same problem from opposite directions. The induction-bias ingest already notes this cross-reference.

10. [research/voooooogel-multi-agent-future](../../notes/research/voooooogel-multi-agent-future.md) — **extends (with tension)**: MAKER's microagents are the extreme endpoint of "multi-agent for context isolation." But these agents don't collaborate, negotiate, or share context — they independently vote on single-step decisions. This is a fundamentally different multi-agent pattern from voooooogel's cooperative forking/spawning model. The tension: voooooogel predicts stronger models will dissolve fixed multi-agent architectures, but MAKER-style voting is structural error correction (redundancy that survives model improvement), not a role hierarchy that better models could absorb.

11. [evans-ai-components-deterministic-system](../../notes/related_works/evans-ai-components-deterministic-system.md) — **parallels**: Evans' modeling/classification distinction maps to MAKER's insights/execution split. Both identify a boundary where LLMs are reliable (classification/execution, with hard oracles) vs unreliable (modeling/insights, with soft oracles). Evans prescribes freezing taxonomies before classification; MAKER prescribes maximal decomposition before execution. Both are constraining strategies for the hard-oracle regime.

**Bidirectional candidates** (reverse link also worth adding):

- [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) <-> source — **exemplifies**: MAKER is the strongest empirical example of what happens when oracle strength is sufficient: voting achieves O(s ln s) scaling. The return path is worth adding because the oracle-strength note's "engineering move" section needs a concrete success case.
- [symbolic-scheduling-over-bounded-llm-calls](../../notes/symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) <-> source — **exemplifies**: The scheduling model claims symbolic bookkeeping outside + bounded LLM calls inside is optimal; MAKER is a million-step demonstration.
- [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) <-> source — **exemplifies**: The note needs calculator-regime success stories; MAKER is the strongest available.

## Rejected Candidates

- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — While MAKER's per-agent minimal context is a response to context scarcity, the connection is indirect. Context efficiency is about what to load into bounded windows; MAKER's decomposition is about error correction through redundancy. The context-isolation benefit is a side effect, not the paper's argument.

- [constraining](../../notes/constraining.md) — The ingest file flags a parallel (same reliability-over-training pattern, different mechanism). But the connection is too abstract to be useful: constraining constrains interpretation space through versioned artifacts; MAKER constrains error through voting. They share a "reliability without training" theme but operate on different substrates with different mechanisms.

- [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) — Red-flagging superficially resembles the constraining gradient (discarding bad outputs is a form of constraint). But the connection doesn't pass the agent-traversal test: an agent following this link from MAKER gains no actionable insight about methodology enforcement.

- [storing-llm-outputs-is-constraining](../../notes/storing-llm-outputs-is-constraining.md) — The ingest file calls voting a "generator/verifier pattern," which is accurate but too thin. The storing-outputs note is about committing to one interpretation; MAKER's voting is about selecting the correct interpretation from multiple candidates. The mechanisms differ enough that the link would confuse rather than clarify.

- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — MAKER's safety discussion (sandboxable microagents) aligns with the inspectability thesis, but the paper doesn't actually implement inspectable substrates. The connection is aspirational, not demonstrated.

## Index Membership

- [learning-theory](../../notes/learning-theory-index.md) — The source is already cited in the Oracle & Verification section (via the error-correction note). The source itself does not need separate index membership; its insights flow through the notes that reference it.

- The ingest file is already listed in kb/sources/index.md.

## Synthesis Opportunities

1. **Decomposition + error correction as a general architectural pattern.** Three notes together imply a higher-order claim: (a) the symbolic scheduling model says decompose into bounded calls, (b) the error-correction note says voting works with any above-chance oracle, (c) MAKER demonstrates that combining both achieves O(s ln s) scaling. The synthesis would argue: *any task that admits maximal decomposition with above-chance per-step oracles can be solved with log-linear cost scaling through voted micro-steps*. This generalizes MAKER beyond Towers of Hanoi to any "calculator regime" task. Contributing notes: symbolic-scheduling, error-correction-works-above-chance-oracles, oracle-strength-spectrum, MAKER source.

2. **The oracle-strength ceiling for multi-agent error correction.** The ingest file already notes this: "Oracle strength determines the ceiling for multi-agent error correction." The scaling-agent-systems source adds the negative result (naive coordination hurts when oracles are weak or absent). A synthesis note could formalize: *multi-agent voting architectures are viable only in the calculator regime; the genuine open problem is extending them to soft-oracle domains (insights, creative tasks)*. Contributing notes: oracle-strength-spectrum, error-correction-works-above-chance-oracles, MAKER source, scaling-agent-systems source, bitter-lesson-boundary.

## Flags

- **Tension:** [voooooogel-multi-agent-future](../../notes/research/voooooogel-multi-agent-future.md) vs MAKER source — voooooogel predicts fixed multi-agent architectures will be dissolved by stronger models. MAKER's architecture is fixed but structural (error correction via redundancy). Resolution may be that error-correction patterns survive model improvement while role-based hierarchies do not.
- **oracle-strength-spectrum note is missing concrete examples.** The note describes the spectrum conceptually but lacks the MAKER reference as a success case in the hard-oracle regime. This was flagged in the ingest file's recommended next action but has not been acted on.
