# Connection Report: Trajectory-Informed Memory Generation for Self-Improving Agent Systems

**Source:** [Trajectory-Informed Memory Generation for Self-Improving Agent Systems](kb/sources/trajectory-informed-memory-generation-self-improving-agents.md)
**Date:** 2026-03-13
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md (168 lines, every entry scanned) — flagged candidates:
  - [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — directly about RL-trained memory policy with oracle dependency; closest system in scope
  - [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) — the "boiling cauldron" mutations and oracle gap; this paper offers a working closed loop
  - [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md) — the paper's framework IS continuous learning from deployment
  - [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — the three timescales framework; paper provides a concrete mechanism
  - [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) — tip categories may map onto memory spaces
  - [distillation](kb/notes/distillation.md) — tip extraction IS distillation
  - [learning-is-not-only-about-generality](kb/notes/learning-is-not-only-about-generality.md) — tips are low-reach accumulation
  - [related-systems/agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) — new data point for the survey
  - [claw-learning-is-broader-than-retrieval](kb/notes/claw-learning-is-broader-than-retrieval.md) — paper's tips improve action capacity, not just retrieval
  - [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) — task/scenario goal completion as oracle
  - [context-engineering](kb/notes/context-engineering.md) — runtime retrieval and injection is context engineering
  - [spec-mining-as-codification](kb/notes/spec-mining-as-codification.md) — trajectory analysis extracts patterns, analogous to spec mining
  - [traversal-improves-the-graph](kb/notes/traversal-improves-the-graph.md) — trajectory analysis as reading execution to generate improvements
  - [related-systems/hindsight](kb/notes/related-systems/hindsight.md) — another memory system with consolidation and reflection

**Topic indexes:**
- Read [learning-theory-index](kb/notes/learning-theory-index.md) — confirmed memory-management-policy note as the primary connection point; no additional candidates beyond index scan
- Read [related-systems-index](kb/notes/related-systems/related-systems-index.md) — the paper would be a new related system entry in the lightweight (source-only) coverage tier; no specific new candidates

**Semantic search:** (via qmd)
- query "agent trajectory learning memory extraction tips from execution experience self-improvement" on notes — top hits:
  - [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) (93%) — strong match, already flagged
  - [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) (56%) — strong match, already flagged
  - [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) (43%) — already flagged
  - [crewai-memory](kb/notes/related-systems/crewai-memory.md) (41%) — weak, different architecture (crew-level memory, not trajectory learning)
  - [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md) (38%) — already flagged
  - [context-efficiency-is-the-central-design-concern](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) (37%) — tangential, about context as scarce resource
  - [sage](kb/notes/related-systems/sage.md) (31%) — weak, different system (BFT consensus, not trajectory learning)
  - [learning-theory-index](kb/notes/learning-theory-index.md) (30%) — routing index, not a direct connection

- query "agent trajectory learning memory extraction tips from execution experience self-improvement" on sources — top hits:
  - [trajectory-informed-memory-generation](kb/sources/trajectory-informed-memory-generation-self-improving-agents.md) (93%) — self-match
  - [agentic-memory-learning (AgeMem) ingest](kb/sources/agentic-memory-learning-unified-long-term-and-short-term-memory-management.ingest.md) (55%) — strongest sibling source
  - [mem0-memory-layer ingest](kb/sources/mem0-memory-layer.ingest.md) (42%) — relevant contrast (Mem0 stores facts, this paper stores tips)
  - [a-mem ingest](kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md) (36%) — relevant contrast (A-MEM's memory evolution vs trajectory tips)

- query "causal failure analysis recovery optimization agent runtime retrieval" on notes — top hits:
  - [enforcement-without-structured-recovery-is-incomplete](kb/notes/enforcement-without-structured-recovery-is-incomplete.md) (55%) — the paper's recovery tips parallel ABC's recovery strategies
  - [the-augmentation-automation-boundary-is-discrimination-not-accuracy](kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) (38%) — weak, different mechanism
  - [error-messages-that-teach-are-a-constraining-technique](kb/notes/error-messages-that-teach-are-a-constraining-technique.md) (36%) — interesting parallel: tips that teach agents are analogous to error messages that teach

**Keyword search:**
- grep "trajectory" in kb/notes/ — found 15 files, most using "trajectory" in passing (maturation trajectory, constraining trajectory); no new candidates beyond those already flagged
- grep "trajectory" in kb/sources/ — found the paper itself plus AgeMem and Slate sources (already covered)
- grep "self-improv" in kb/ — found 3 files, none new candidates
- grep "agent.*memory" in kb/sources/ — found 27 files, all already covered by semantic search or index scan

**Link following:**
- From [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md):
  - Links to [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md), [automating-kb-learning](kb/notes/automating-kb-learning-is-an-open-problem.md), [inspectable-substrate](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md), [distillation](kb/notes/distillation.md), [learning-is-not-only-about-generality](kb/notes/learning-is-not-only-about-generality.md), [deploy-time-learning](kb/notes/deploy-time-learning-the-missing-middle.md), [constraining-during-deployment](kb/notes/constraining-during-deployment-is-continuous-learning.md) — confirms the connection cluster; paper is a new data point in this existing neighborhood
- From [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md):
  - The six-dimension framework (storage unit, agency model, link structure, temporal model, curation operations, extraction schema) provides the analytical apparatus for positioning the paper's system
  - "Everyone automates extraction, nobody automates synthesis" — the paper's tip extraction is automated extraction; the consolidation/merging step approaches automated synthesis of operational knowledge

## Connections Found

- [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — **contrasts**: both study agent learning from execution trajectories, but AgeMem learns memory POLICY through RL (when to store/retrieve), while this paper learns CONTENT (what tips to extract and inject). AgeMem's learning is opaque (in weights); this paper's learning produces inspectable tips. Both depend on task-completion oracles. The paper is a data point for the same thesis: memory management is learnable when oracles exist.

- [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) — **exemplifies**: the paper demonstrates a closed learning loop (execute → analyze trajectory → extract tips → inject at runtime → improved execution) for a narrow domain. The "boiling cauldron" mutations map: Extract (tip extraction from trajectories), Synthesise (tip consolidation/merging), Retire (presumably, though not discussed). The paper has what the KB lacks — a clear oracle (task/scenario goal completion). But the tips are low-reach facts (task-specific procedural guidance), not high-reach theories.

- [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) — **extends**: the paper introduces a 12th system to the comparative review, with a distinctive position: developer-managed external service agency model (tips extracted by an external pipeline, not by the agent itself), no link structure between tips (pure retrieval via embedding similarity), no temporal model, unique curation operation (tip consolidation through LLM-based merging), and two-strategy retrieval (cosine similarity vs LLM-guided selection). It also provides evidence for "everyone automates extraction, nobody automates synthesis" — the tip consolidation step edges toward automated synthesis of operational knowledge.

- [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — **exemplifies**: the paper's framework is deploy-time learning — extracted tips are durable artifacts that persist across sessions and improve agent behavior without weight updates. The tips sit on the verifiability gradient between "restructured prompts" (inspectable, LLM-evaluated) and "prompt tests" (validated against benchmark). The three tip categories (strategy, recovery, optimization) map to different positions on the gradient.

- [distillation](kb/notes/distillation.md) — **exemplifies**: trajectory → tip extraction is distillation — compressing a larger body of reasoning (full execution trajectory) into focused operational guidance (actionable tips) shaped by use case and context budget. The three tip categories are three different distillation targets from the same source material (successful trajectories, failure trajectories, inefficient trajectories). The subtask-level granularity outperforming task-level is evidence that distillation granularity matters.

- [learning-is-not-only-about-generality](kb/notes/learning-is-not-only-about-generality.md) — **exemplifies**: the tips are accumulation (the most basic learning operation) at the low-reach end — procedural guidance for specific task types. Subtask-level tips have slightly more reach than task-level tips (they transfer across tasks sharing subtask structure), which may explain their superior performance. The paper confirms Simon's definition: the system's capacity for adapting to its environment changes permanently through tip accumulation.

- [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md) — **exemplifies**: the paper's framework constrains agent behavior during deployment through accumulated tips — the same mechanism the note describes, with trajectory analysis as the data source instead of human iteration. Each tip narrows the interpretation space for future similar tasks, trading generality for reliability.

- [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) — **exemplifies**: the paper's tips map primarily to the procedural/operational space (how to do things, high churn). Strategy tips are procedural knowledge about task execution. Recovery tips are operational knowledge about failure handling. Optimization tips are procedural knowledge about efficiency. None of the tips are semantic knowledge (facts about the world) or episodic/self knowledge (the agent's identity or calibration). This is a clean example of memory that is purely procedural.

**Bidirectional candidates** (reverse link also worth adding):
- [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) <-> source — **contrasts**: both directions useful because the paper provides a complementary approach (learning content vs learning policy) that the AgeMem analysis note could contrast directly
- [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) <-> source — **extends**: the paper is a new data point that fits the six-dimension framework and contributes evidence to the "extraction vs synthesis" convergence finding

## Rejected Candidates

- [context-engineering](kb/notes/context-engineering.md) — the paper's runtime retrieval is context engineering, but the connection is too generic. Every system that selects what to put in agent prompts is doing context engineering. No specific insight flows in either direction.
- [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) — task/scenario goal completion is a clear oracle, but the paper doesn't add anything to the oracle-strength framework. The oracle is simply task success/failure, already well-covered by AgeMem analysis.
- [related-systems/crewai-memory](kb/notes/related-systems/crewai-memory.md) — both are memory systems for agents, but the architectures are too different (crew-level shared memory vs trajectory-extracted tips) to produce a useful comparison. Surface vocabulary overlap only.
- [related-systems/hindsight](kb/notes/related-systems/hindsight.md) — both extract knowledge from agent experience, but the specific mechanisms are different (Hindsight extracts facts/observations from conversations; this paper extracts tips from execution trajectories). The comparison would be a paragraph of "they're both memory systems" without specific insight.
- [related-systems/sage](kb/notes/related-systems/sage.md) — different system entirely (consensus-based memory vs trajectory analysis).
- [spec-mining-as-codification](kb/notes/spec-mining-as-codification.md) — initial candidate because trajectory analysis extracts patterns from observed behavior (analogous to spec mining). However, the paper extracts natural-language tips, not deterministic rules. Spec mining commits to a single interpretation; tips remain underspecified guidance. The analogy is surface-level.
- [traversal-improves-the-graph](kb/notes/traversal-improves-the-graph.md) — trajectory analysis reading execution traces to generate improvements has a structural parallel to traversal improving the graph, but the mechanisms are entirely different (automated analysis of agent reasoning chains vs agent noticing improvement opportunities while reading notes). Too thin.
- [claw-learning-is-broader-than-retrieval](kb/notes/claw-learning-is-broader-than-retrieval.md) — the paper's tips improve action capacity (planning, recovery), aligning with the "broader than retrieval" claim. However, the note is about KB learning scope, not about external agent memory systems. The connection doesn't add specific insight to either side.
- [error-messages-that-teach-are-a-constraining-technique](kb/notes/error-messages-that-teach-are-a-constraining-technique.md) — recovery tips are "error messages from past experience," but the analogy doesn't survive scrutiny. Error messages are triggered in real-time by specific failures; tips are pre-loaded from past trajectories. Different mechanism.
- [enforcement-without-structured-recovery-is-incomplete](kb/notes/enforcement-without-structured-recovery-is-incomplete.md) — the paper's recovery tips relate to recovery from failures, but the note is about structured recovery in enforcement systems (corrective, fallback, escalation). Different domain and mechanism.
- [skill-synthesis-materializing-knowledge-as-skills ingest](kb/sources/skill-synthesis-materializing-knowledge-as-skills-2032179291031806408.ingest.md) — both extract operational knowledge from past experience (commit history / trajectories), but the source materials are already well-connected to the KB's distillation framework. Adding another source-to-source link would not add analytical value beyond "both exemplify distillation."

## Index Membership

- [learning-theory-index](kb/notes/learning-theory-index.md) — belongs in **Memory & Architecture** subsection as a reference source: demonstrates trajectory-based tip extraction as an alternative to RL-trained policy (AgeMem) for deploy-time agent improvement, with inspectable output and oracle dependency
- [related-systems-index](kb/notes/related-systems/related-systems-index.md) — belongs in the lightweight coverage tier alongside Mem0, Graphiti, Letta, AgeMem: a memory/learning system with source-level coverage only (no repo review)
- Already member of: none (source has no existing index membership)

## Synthesis Opportunities

**Trajectory distillation vs weight-based policy learning as two sides of the deploy-time learning coin.** The paper and AgeMem both learn from execution trajectories, but extract to different substrates: inspectable natural-language tips vs opaque model weights. Together with commonplace's manual artifact accumulation, they form a spectrum of trajectory-to-improvement mechanisms:

| System | What it learns from | What it produces | Substrate | Inspectable? | Oracle needed? |
|--------|-------------------|-----------------|-----------|:---:|:---:|
| This paper | Execution trajectories | Strategy/recovery/optimization tips | Text artifacts | Yes | Yes (task completion) |
| AgeMem | Execution trajectories | Memory management policy | Model weights | No | Yes (task completion) |
| Commonplace | Human+agent working sessions | Notes, connections, procedures | Files in repo | Yes | No clear oracle |

A synthesis note could argue: **trajectory analysis is the common mechanism; the output substrate (tips, weights, or files) determines the trade-off between inspectability and automation**. The paper and AgeMem are complementary strategies for the same problem, and commonplace could in principle adopt trajectory analysis as an input to its manual learning loop.

## Flags

- The paper's tip consolidation (LLM-based merging of semantically similar tips) is the closest any surveyed system comes to automated synthesis — worth flagging for the "everyone automates extraction, nobody automates synthesis" convergence finding in the comparative review.
- The subtask-level granularity outperforming task-level is a concrete data point for distillation theory: distillation granularity affects transfer, and finer-grained distillation (subtask-level tips) transfers better than coarser (task-level tips) because subtasks recur across tasks.
