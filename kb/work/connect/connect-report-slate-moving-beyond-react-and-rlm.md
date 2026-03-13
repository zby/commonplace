# Connection Report: Slate: Moving Beyond ReAct and RLM

**Source:** [Slate: Moving Beyond ReAct and RLM](../../sources/slate-moving-beyond-react-and-rlm.md)
**Date:** 2026-03-12
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md (165 entries) — flagged 15 candidates by description:
  - [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md) — orchestrator/thread model is instance of bounded-context scheduling
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — Slate's thesis that context management is the bottleneck
  - [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — Slate's architecture addresses scheduler degradation
  - [rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation](../../notes/rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) — Slate explicitly compares to RLM
  - [decomposition-rules-for-bounded-context-scheduling](../../notes/decomposition-rules-for-bounded-context-scheduling.md) — thread dispatch is bounded-context scheduling
  - [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — episodes vs message passing coordination
  - [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) — threads provide scoping via isolation
  - [three-space-agent-memory-maps-to-tulving-taxonomy](../../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) — episodic memory maps directly
  - [distillation](../../notes/distillation.md) — episodes are distillation of execution traces
  - [ephemeral-computation-prevents-accumulation](../../notes/ephemeral-computation-prevents-accumulation.md) — thread episodes as compressed ephemeral artifacts
  - [related-systems/spacebot](../../notes/related-systems/spacebot.md) — process-type architecture comparison
  - [scheduler-llm-separation-exploits-an-error-correction-asymmetry](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — Slate separates orchestration from execution
  - [context-engineering](../../notes/context-engineering.md) — Slate's approach is context engineering
  - [memory-management-policy-is-learnable-but-oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — episodic memory management policy
  - [related-systems/agentic-memory-systems-comparative-review](../../notes/related-systems/agentic-memory-systems-comparative-review.md) — agency model dimension

**Topic indexes:**
- Read [computational-model](../../notes/computational-model-index.md) — confirmed all Scheduling & Orchestration section notes as candidates. No new candidates beyond index scan.
- Read [learning-theory](../../notes/learning-theory-index.md) — confirmed distillation and ephemeral-computation candidates. No new candidates.

**Semantic search:** (via qmd)
- query "thread weaving agent architecture bounded worker episodic memory context management orchestrator" --collection notes -n 15:
  - [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md) (93%) — strong, mechanism overlap confirmed
  - [related-systems/spacebot](../../notes/related-systems/spacebot.md) (56%) — strong, process-type architecture parallel
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) (43%) — strong, core thesis overlap
  - [injectable-configuration](../../notes/injectable-configuration-extends-frontloading-to-installation-specific-values.md) (40%) — weak, only surface vocabulary overlap
  - [memory-management-policy](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) (32%) — moderate, episodic memory angle
  - [minimum-viable-vocabulary](../../notes/minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md) (30%) — skip, no real connection
  - [frontloading-spares-execution-context](../../notes/frontloading-spares-execution-context.md) (28%) — weak, tangential
- query "thread weaving agent architecture bounded worker episodic memory context management orchestrator" --collection sources -n 10:
  - [the-anatomy-of-an-agent-harness](../../sources/the-anatomy-of-an-agent-harness-2031408954517971368.md) (50%) — moderate, both describe harness components
- query "compaction lossy compression agent context working memory degradation subagent synchronization" --collection notes -n 15:
  - [memory-management-policy](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) (88%) — evaluated above
  - [computational-model](../../notes/computational-model-index.md) (51%) — already scanned as topic index
  - [context-efficiency](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) (41%) — already flagged
  - [decomposition-rules](../../notes/decomposition-rules-for-bounded-context-scheduling.md) (41%) — already flagged
  - [three-space-agent-memory](../../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) (33%) — already flagged
  - [agentic-memory-systems-comparative-review](../../notes/related-systems/agentic-memory-systems-comparative-review.md) (33%) — already flagged
- query "expressivity inductive bias agent harness task decomposition strategy tactics" --collection notes -n 15:
  - [minimum-viable-vocabulary](../../notes/minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md) (88%) — skip, false match
  - No new candidates beyond index scan

**Keyword search:**
- rg "episodic memory|episodic" kb/notes/ — found [three-space-agent-memory](../../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md), [what-cludebot-teaches-us](../../notes/what-cludebot-teaches-us.md), [claw-learning-is-broader-than-retrieval](../../notes/claw-learning-is-broader-than-retrieval.md) (already in index candidates)
- rg "compaction|context rot|working memory" kb/ — found [llm-mediated-schedulers](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md), [context-efficiency](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md) (already flagged)
- rg "subagent|sub-agent|orchestrat" kb/notes/ — found 31 files, including all previously flagged candidates
- rg "RLM|Recursive Language Model" kb/ — found [rlm-achieves-the-clean-scheduler-model](../../notes/rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md), [ephemeral-computation](../../notes/ephemeral-computation-prevents-accumulation.md) (already flagged)
- rg "expressiv|inductive bias" kb/ — found [induction-bias-sequence-models](../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md), [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md) (already flagged; induction bias source is about ML architecture, not agent harness expressivity)
- rg "Karpathy|LLM OS" kb/ — found general references but no note-level match to Slate's OS framing

**Link following:**
- From [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md): followed links to [decomposition-rules](../../notes/decomposition-rules-for-bounded-context-scheduling.md), [llm-mediated-schedulers](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md), [scheduler-llm-separation](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — these four notes form a cluster around agent orchestration architecture that Slate directly maps onto
- From [rlm-achieves-the-clean-scheduler-model](../../notes/rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md): reveals design space (LLM-is-scheduler vs LLM-writes-scheduler vs versioned-scheduler) — Slate occupies a fourth point (LLM-dispatches-bounded-workers-with-episode-compression)
- From [related-systems/spacebot](../../notes/related-systems/spacebot.md): followed link to [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) — Spacebot's branches and Slate's threads are independently converging on the same architectural primitive

## Connections Found

- [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md) — **exemplifies**: Slate's thread-weaving architecture is a concrete implementation of the select/call loop. The orchestrator is the symbolic scheduler, threads are bounded LLM calls, episodes are the compressed results appended to scheduler state K, and thread dispatch is the `select` function. The key novelty relative to the abstract model is that Slate's episodes are compositionally reusable — a thread can be initialized with another thread's episode, making K items serve as both intermediate results and context for future calls.

- [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — **exemplifies**: Slate explicitly diagnoses the degraded-scheduler problem (ReAct loops, Claude Code's single-thread-with-compaction) and positions thread-weaving as a recovery strategy. Slate's episodes implement the note's "compaction" recovery (compressed representations of completed execution) combined with "externalisation" (episodes as external state shared between threads). The note's three recovery strategies (compaction, externalisation, factoring into code) map to Slate's episodes, which combine the first two while the orchestrator DSL approaches the third.

- [rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation](../../notes/rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) — **extends**: Slate addresses RLM's two weaknesses identified in the source: (1) over-decomposition risk from unbounded recursion (threads execute ONE action then return, forcing frequent synchronization) and (2) lack of intermediate feedback (episodes provide per-action feedback to the orchestrator). The note's design space (LLM-is-scheduler / LLM-writes-scheduler / versioned-scheduler) gains a fourth point: LLM-dispatches-bounded-workers-with-episode-compression, which achieves context efficiency without ephemeral computation's accumulation cost because episodes persist across the session.

- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **grounds**: Slate's core empirical claim — "the real bottleneck in long-horizon agentic tasks is context management, not model intelligence" — is the practitioner convergence evidence this note collects. Slate confirms both dimensions: volume (working memory degrades as context grows, citing "context rot") and complexity (strategy vs tactics require different reasoning modes that flat context conflates). Slate's thread isolation is one of the architectural responses the note catalogues (sub-agent isolation).

- [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) — **exemplifies**: Slate's threads provide exactly the lexically scoped frames this note identifies as the one mechanism for real context isolation. Each thread gets a bounded scope, executes in isolation, and returns only a compressed episode — the fork-think-return pattern the note identifies as "the closest production analogue to lexical scoping." Slate's episode boundary is more structured than a raw sub-agent return: it's a compressed representation rather than a full response, implementing the note's "return value problem" more explicitly.

- [distillation](../../notes/distillation.md) — **exemplifies**: Episode compression is distillation in the KB's sense — compressing a larger body of execution (the full tactical trace of tool calls and reasoning) into a focused artifact (the episode) shaped by the orchestrator's context budget. The source's table row "Many observations -> Summary | Agent that can't fit them all in context" maps directly to Slate's thread-execution -> episode compression. The episode targets the orchestrator as the consumer, retaining only what's needed for strategic decision-making.

- [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — **extends**: Slate introduces a third coordination mechanism beyond this note's conversation/refinement/forking triad: episode-based synchronization. Unlike conversation (where accumulated history persists), prompt refinement (clean restart), or forking (context cloning), episodes compress the completed execution into a reusable representation that can be composed with other thread contexts. The source explicitly contrasts this with message passing (Claude Code) and reduce-and-return (Devin/Manus). Episode-based coordination occupies a new point in the design space.

- [related-systems/spacebot](../../notes/related-systems/spacebot.md) — **parallels**: Spacebot's five process types (channels, branches, workers, compactor, cortex) and Slate's threads share the same core architectural insight: typed, bounded execution units supervised by a non-LLM orchestrator. Spacebot's branches (fork context, execute in isolation, return scrubbed conclusion) are structurally identical to Slate's threads (dispatch action, execute, return episode). Both systems converge on context isolation as the mechanism for long-horizon reliability. The key difference: Spacebot's compactor manages context overflow reactively (80%/85%/95% thresholds), while Slate's episodes prevent overflow proactively by compressing each thread return before it enters the orchestrator's context.

- [decomposition-rules-for-bounded-context-scheduling](../../notes/decomposition-rules-for-bounded-context-scheduling.md) — **exemplifies**: Slate's thread architecture implements several of these rules. "Separate selection from joint reasoning" — the orchestrator selects what to dispatch, threads do the reasoning. "Save reusable intermediate items in scheduler state" — episodes are exactly these intermediate items. "Exploit clean frames recursively" — each thread gets a clean frame. "Delay expensive co-loading until interactions justify it" — threads execute isolated actions, and only episodes (compressed representations) are composed in the orchestrator.

- [ephemeral-computation-prevents-accumulation](../../notes/ephemeral-computation-prevents-accumulation.md) — **contradicts (partially)**: Slate's episodes sit at an interesting point on the ephemeral/accumulating spectrum. Thread execution is ephemeral (the full tactical trace is discarded), but episodes persist as reusable compressed representations within the session. This is neither fully ephemeral (RLM's discard-everything) nor fully accumulating (versioned repo artifacts). The source demonstrates that per-session accumulation via episodes is sufficient for long-horizon tasks without requiring cross-session persistence, suggesting a middle ground the note's binary doesn't capture.

- [three-space-agent-memory-maps-to-tulving-taxonomy](../../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) — **exemplifies** (weak): Slate's episodes implement tractable episodic memory in LLMs — compressed representations of completed episodes, matching Tulving's episodic memory (personal experience). The source explicitly frames this as "tractable episodic memory" and the compression boundary (action completion) gives episodes the same lifecycle the note describes: high churn, arrive raw, consolidate. However, the connection is surface-level — Slate uses the term "episodic" for a specific architectural mechanism, not for the full three-space separation the note proposes.

**Bidirectional candidates** (reverse link also worth adding):

- [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md) <-> source — **exemplifies**: The note's open question "When should the orchestrator compact vs externalise vs recurse?" receives a concrete answer from Slate: compact via episodes at every thread return, externalise via persistent thread contexts, and the orchestrator handles recursion through thread composition. Worth adding as a source reference.

- [rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation](../../notes/rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) <-> source — **extends**: The note's design space (three points) should include Slate as a fourth point that navigates between ephemeral and accumulating by compressing rather than discarding.

- [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) <-> source — **extends**: Episodes are a new coordination primitive worth noting alongside conversation, refinement, and forking.

## Source-to-Source Connections

- [The Anatomy of an Agent Harness](../../sources/the-anatomy-of-an-agent-harness-2031408954517971368.md) — **extends**: Both sources derive harness components from model limitations. The Harness Anatomy provides the component taxonomy; Slate provides a specific architectural pattern (thread-weaving) that implements several of those components (context management, long-horizon execution, orchestration logic). Slate's thread architecture is a concrete instantiation of the Harness Anatomy's abstract "orchestration logic" component.

- [What Survives in Multi-Agent Systems (voooooogel)](../../sources/voooooogel-multi-agent-future.md) — **contradicts productively**: Voooooogel argues that hand-crafted hierarchies will be dissolved by stronger models and that forking will be the primary multi-agent pattern. Slate argues the opposite — that single-threaded agents have not been fully solved, and that thread-weaving with explicit episode compression outperforms naive multi-agent approaches. The tension is genuine: will episode-based synchronization survive model scaling, or is it a "current bodge" like ralph loops? Slate's counter-argument is that episode compression solves a structural problem (context management) that model intelligence alone cannot dissolve.

## Rejected Candidates

- [injectable-configuration-extends-frontloading-to-installation-specific-values](../../notes/injectable-configuration-extends-frontloading-to-installation-specific-values.md) — surfaced by semantic search (40%) but only surface vocabulary overlap (both mention orchestrator and sub-agent); no genuine connection to Slate's architecture
- [minimum-viable-vocabulary](../../notes/minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md) — false positive from semantic search (88% on expressivity query); the note is about naming/vocabulary, not agent harness expressivity
- [frontloading-spares-execution-context](../../notes/frontloading-spares-execution-context.md) — episodes pre-compute context for the main thread, but this is coincidental vocabulary overlap; frontloading is about static pre-computation, not runtime compression
- [context-engineering](../../notes/context-engineering.md) — too broad; Slate is context engineering in practice, but the definition note is just a vocabulary entry, not a claim to connect to
- [memory-management-policy-is-learnable-but-oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — AgeMem's RL-trained memory management is a different mechanism entirely; Slate's episode compression is architectural, not learned
- [scheduler-llm-separation-exploits-an-error-correction-asymmetry](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — Slate does separate orchestration from execution, but the error-correction asymmetry argument (bookkeeping vs semantic operations have different error profiles) is not what Slate is about; the connection would be "Slate separates these things" which is too generic
- [related-systems/agentic-memory-systems-comparative-review](../../notes/related-systems/agentic-memory-systems-comparative-review.md) — the review covers memory systems, and Slate has a memory component (episodes), but Slate's focus is on architecture, not memory design; the connection would require stretching
- [induction-bias-sequence-models](../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) — Slate uses the term "inductive bias" to describe how well models can use a given harness interface, but this is unrelated to the paper's ML-architecture induction bias about step-by-step state tracking

## Index Membership

- [computational-model](../../notes/computational-model-index.md) — Slate exemplifies the Scheduling & Orchestration cluster; as a source it would naturally be cited by notes in this area (especially bounded-context-orchestration-model and rlm-achieves-the-clean-scheduler-model)
- Not currently a member of any index (it's a source, not a note)

## Synthesis Opportunities

1. **The episode compression primitive needs its own note.** Slate's episodes, Spacebot's branch returns, and the conversation-vs-prompt-refinement note's "forking" pattern all describe the same architectural primitive: bounded execution that returns compressed results rather than full context. The bounded-context-orchestration model describes this abstractly as "result r appended to K," but the specific mechanism — compression at execution boundaries — is not named. A note titled something like "Episode boundaries are natural compression points" could synthesize: (a) Slate's episodes, (b) Spacebot's branch scrubbed conclusions, (c) the anthropic recommendation for 1-2K token sub-agent returns, and (d) the scheduling model's r = call(P) operation. The claim: execution boundaries are the natural points for distillation because the completed action provides a coherent unit to compress.

2. **The design space of agent orchestration patterns needs a map.** The rlm-achieves-the-clean-scheduler note identifies three points (LLM-is-scheduler, LLM-writes-scheduler, versioned-scheduler). Slate adds a fourth (LLM-dispatches-bounded-workers). Voooooogel adds a fifth (forking with shared KV cache). The bounded-context-orchestration model provides the framework but doesn't enumerate the instantiation space. A note mapping these points — with their tradeoffs on accumulation, expressivity, context efficiency, and synchronization — would synthesize across multiple sources and notes.

## Flags

- **Target is a source file (practitioner-report)** — not a note; connections point from source to notes, not note-to-note
- No existing notes or sources currently link to this source (rg "slate-moving-beyond" found zero references in kb/notes/)
- The source's comparison table (Section: Agent Architecture Comparison Table) could seed a structured comparison note, but that would be a write operation, not a connect operation
