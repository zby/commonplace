# Extractable theory notes from agent memory design

Target: [Designing a Memory System for LLM-Based Agents](../../notes/designing-agent-memory-systems.md)

Purpose: identify claims embedded in the synthesis note that could become standalone theoretical notes in `kb/notes/`, using the notes collection's quality bar: claim title, reach beyond the design study, composability as an imported premise, clear boundary conditions, and no dependence on the whole four-layer architecture.

## Summary

The source note is doing two jobs at once:

1. It proposes an architecture for agent memory: trace, observation, episode, library; role-split retrieval; typed cue indexes; extraction taxonomy.
2. It contains several general claims about memory, activation, promotion, source-of-truth control, and trace-derived learning.

The architecture can remain a synthesis note. The extractable material is the set of claims that another note could cite without importing the full architecture. The strongest candidates are not "parts of the architecture"; they are mechanisms that apply across memory systems, KB maintenance, review systems, and agent runtime design.

The stronger grounding found in [the grounding report](./2026-04-23-grounding-report.md) is that these candidates sit at the intersection of three theory clusters:

- **Context engineering:** memory is useful only when a context engine selects, frames, and injects it into a bounded call. This grounds claims about capture posture, cue activation, progressive disclosure, and trace loading.
- **Readable-artifact learning:** session traces become durable capacity through [distillation](../../notes/definitions/distillation.md), [constraining](../../notes/definitions/constraining.md), and [codification](../../notes/definitions/codification.md). This grounds claims about promotion, compiled cues, negative results, and procedure extraction.
- **Oracle theory:** extraction and promotion differ by signal strength. Corrections have strong interactive oracles; discoveries and broad syntheses have weak or delayed oracles. This grounds claims about build order, behavioral faithfulness, and promotion authority.

This suggests a useful filter: extract theory notes when the claim names a reusable mechanism in one of those clusters. Keep material inside the synthesis note when it only justifies the proposed four-layer architecture.

## Best extraction candidates

### Store-everything is a capture posture, not a memory design

Likely title:

`Store-everything is a capture posture, not a memory design`

Claim:

Retaining raw traces broadly preserves optionality for later redistillation, but it does not determine what the memory system should extract, promote, retain, redact, or evaluate. Those decisions must be governed by the output the memory system is meant to improve.

Stronger grounding:

This should be grounded first in context engineering, not storage economics. [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) explains why storage and context have different cost models: the hard problem is bounded context assembly, not persistence. [Agent runtimes decompose into scheduler context engine and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) locates broad trace retention on the execution substrate, while extraction/loading belong to the context engine and learning loop. [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) gives the most direct frame: "memory" decomposes into storage, activation, and learning.

Why it deserves a separate note:

The source note starts from the store-everything premise, then softens it by calling it a bet. The previous critique correctly notices that this is still too input-driven. A standalone note would reconcile the source note with the output-driven memory workshop: broad capture is a substrate choice; memory design is a target-relative policy.

Reach:

This applies beyond agent memory: logs, research notes, observability traces, full transcript retention, source snapshots, and workshop artifacts all benefit from broad capture but still need output-governed extraction.

Boundary:

The claim should not argue against broad trace retention. It should argue against confusing retention with value. "Store everything eligible under retention/redaction policy" is compatible with output-driven extraction.

Existing overlaps:

- [Session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) already separates storage from loading.
- [Distillation is transformation, not selection](../../notes/distillation-is-transformation-not-selection.md) already supports retaining source material for future transformations.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) supplies the scarce-resource argument that makes selective loading the design problem.
- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) supplies the storage/retrieval/learning decomposition.
- This proposed note would add the missing distinction between **capture policy** and **memory design objective**.

Suggested links:

- `grounds`: [Session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md)
- `grounds`: [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)
- `grounds`: [Agent runtimes decompose into scheduler context engine and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md)
- `grounds`: [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md)
- `grounds`: [Distillation is transformation, not selection](../../notes/distillation-is-transformation-not-selection.md)
- `contrasts`: [The chat-history model trades context efficiency for implementation simplicity](../../notes/the-chat-history-model-trades-context-efficiency-for-implementation.md)

### System-definition cues need behavioral faithfulness tests

Likely title:

`System-definition cues need behavioral faithfulness tests`

Claim:

A memory cue that fires and enters context has not closed the activation gap unless it causally changes the agent's later action in the intended direction. Cue quality must be evaluated by behavioral uptake, not by retrieval success alone.

Stronger grounding:

The cue is a system-definition artifact, so this belongs in the behavior-change half of continual learning. [Continual learning's open problem is behaviour, not knowledge](../../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md) grounds why a retrieved fact and a fired policy cue have different success criteria. [The readable-artifact loop is the tractable unit for continual learning](../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) explains why prompt snippets, rules, tests, and tools are the practical substrate for this kind of behavior change. [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) explains why the evaluation should move from "cue was present" to an oracle that discriminates changed behavior from unchanged behavior.

Why it deserves a separate note:

The source note has a strong activation design: cue match, priority arbitration, commitment. But "commitment" currently depends on imperative framing, checkpoint insertion, and contradiction surfacing. Recent evidence in the KB says live context can still be ignored. A standalone note would upgrade the activation theory: the unit of evaluation is not "was the cue retrieved?" but "did the cue change behavior for the intended reason?"

Reach:

This applies to always-loaded instructions, review gates, safety policies, prompt snippets, skills, guardrails, and generated memories. Any system-definition artifact that claims to steer action needs a behavioral test.

Boundary:

This is strongest for high-priority or always-loaded behavior-changing cues. Low-risk advisory context may not justify expensive ablations.

Existing overlaps:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) names the activation gap.
- [Continual learning's open problem is behaviour, not knowledge](../../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md) grounds the behavior-change criterion.
- [The readable-artifact loop is the tractable unit for continual learning](../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) grounds readable cues as a practical learning substrate.
- [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) grounds why cue evaluation needs a stronger behavioral oracle.
- [Prompt ablation converts human insight into deployable agent framing](../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) gives a method for testing framing.
- [Unit testing LLM instructions requires mocking the tool boundary](../../notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md) gives a testing route for instructions.
- The proposed note would connect those into a memory-specific criterion: fired cues must be behaviorally faithful.

Suggested links:

- `extends`: [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md)
- `grounds`: [Continual learning's open problem is behaviour, not knowledge](../../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md)
- `grounds`: [The readable-artifact loop is the tractable unit for continual learning](../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md)
- `grounds`: [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md)
- `mechanism`: [Prompt ablation converts human insight into deployable agent framing](../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md)
- `mechanism`: [Unit testing LLM instructions requires mocking the tool boundary](../../notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md)
- `evidence`: [Large Language Model Agents are not Always Faithful Self-Evolvers](../../sources/large-language-model-agents-are-not-always-faithful-self.ingest.md)

### Library-derived cues should be compiled views

Likely title:

`Library-derived cues should be compiled views`

Claim:

When a cue index entry is generated from a library artifact, the library artifact should remain the source of truth and the cue should carry provenance, source hash, and regeneration rules. Otherwise the cue becomes a divergent behavior-changing policy surface.

Stronger grounding:

The important addition from the grounding pass is role: a library-derived cue is not just a derived summary, it is a derived **system-definition** surface. That makes drift more dangerous than ordinary documentation drift because the cue can change behavior even when the explanatory source has changed. [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) grounds this role distinction; [System-definition artifacts are crystallized reasoning under context scarcity](../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) explains why those artifacts exist; [Always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) shows the broader family of behavior-shaping context surfaces that can drift from their sources.

Why it deserves a separate note:

The source note's "library to observation backflow" is important but under-specified. It says a plain library artifact often needs a companion cue so it can fire in the right situation. That creates a source-of-truth problem: library prose and cue index can drift. This claim is general and operationally useful outside agent memory.

Reach:

Applies to compiled indexes, generated review gates, AGENTS.md excerpts derived from notes, quickstart files derived from canonical guides, generated lint rules derived from policy, and any fast path derived from a deeper explanation.

Boundary:

Directly authored candidate cues are different. The compiled-view rule applies once the cue claims authority from a library artifact.

Existing overlaps:

- [Distilled artifacts need source tracking at the source](../../notes/distilled-artifacts-need-source-tracking-at-the-source.md) covers source tracking for distilled artifacts.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) grounds why the risk is specifically role drift: the derived cue is consumed as policy.
- [Always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) supplies the broader surface taxonomy for behavior-shaping context.
- [Archie](../../agent-memory-systems/reviews/archie.md) provides a concrete "canonical guide -> derived fast path" pattern.
- This proposed note would specialize the idea for behavior-changing compiled policy surfaces.

Suggested links:

- `extends`: [Distilled artifacts need source tracking at the source](../../notes/distilled-artifacts-need-source-tracking-at-the-source.md)
- `grounds`: [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md)
- `grounds`: [System-definition artifacts are crystallized reasoning under context scarcity](../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md)
- `grounds`: [Always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md)
- `evidence`: [Archie](../../agent-memory-systems/reviews/archie.md)

### Episodes are retrospective memory; workshops are active memory

Likely title:

`Episodes are retrospective memory; workshops are active memory`

Claim:

Retrospective episodes and active workshop artifacts solve different memory problems. Episodes compress what happened after a bounded effort; workshops hold work in motion with state, dependencies, expiration, and unresolved alternatives.

Stronger grounding:

The grounding pass clarifies that this is a runtime-boundary claim, not just a document-type distinction. Episodes are distilled retrospective artifacts for later retrieval; workshops are active state on the work surface. In the runtime decomposition, both live on the execution substrate, but they feed the context engine differently: episodes are loaded as memory; workshop artifacts are read and mutated as current work state. This prevents the four-layer architecture from accidentally absorbing the active work surface into retrospective memory.

Why it deserves a separate note:

The source note's episode layer is retrospective. The KB already has a workshop-layer theory, but the relation between "episode" and "workshop" is not yet explicit. The source note risks treating active work as trace or episode, which loses stateful process structure.

Reach:

This applies to KB design, agent runtime memory, project management, decision-record production, review runs, research workflows, and any setting where work has both live state and later narrative recall.

Boundary:

The note should not propose adding a fifth memory layer by default. It should clarify that the four-layer design describes retrospective memory; active workshops are adjacent work-surface artifacts that can later produce episodes and library notes.

Existing overlaps:

- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) is the main premise.
- [Agent runtimes decompose into scheduler context engine and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) grounds the execution-substrate distinction between active work state and retrieved memory.
- [Conversation vs prompt refinement in agent-to-agent coordination](../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) helps distinguish execution trace from compressed handoff.
- [Session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) helps distinguish stored trace, handoff artifact, and next-call context.
- This proposed note would bridge workshop theory to agent memory architecture.

Suggested links:

- `extends`: [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md)
- `grounds`: [Agent runtimes decompose into scheduler context engine and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md)
- `grounds`: [Session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md)
- `contrasts`: [Conversation vs prompt refinement in agent-to-agent coordination](../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md)
- `grounds`: [Designing a Memory System for LLM-Based Agents](../../notes/designing-agent-memory-systems.md)

### Negative results are memory artifacts because final artifacts hide discarded paths

Likely title:

`Negative results are memory artifacts because final artifacts hide discarded paths`

Claim:

Durable work products usually preserve the chosen path, not the rejected alternatives. A memory system needs first-class negative-result records because the value of "why not X?" is highest when X becomes tempting again.

Stronger grounding:

The grounding pass adds two useful frames. First, this is a knowledge-role memory artifact with a possible system-definition companion: the negative-result record answers "why not?", while a cue can fire when the rejected path is proposed again. Second, promotion should follow oracle strength and reach: the failed path needs enough evidence, recurrence likelihood, or consequence to justify a durable artifact.

Why it deserves a separate note:

The source note treats negative-result preservation as a use case. The claim has enough reach to stand alone: final artifacts systematically omit discarded paths, so a separate memory artifact is needed to prevent rediscovery loops.

Reach:

Applies to research, design, architecture, policy, product decisions, debugging, source selection, and agent behavior. It is not specific to the four-layer architecture.

Boundary:

Not every failed attempt deserves promotion. The note needs a promotion standard: the rejected path should be likely to recur, costly to retry, or useful as evidence for a broader claim.

Existing overlaps:

- Decision-record practices sometimes include "alternatives considered," but many durable artifacts do not.
- [Ephemeral computation prevents accumulation](../../notes/ephemeral-computation-prevents-accumulation.md) gives the broader anti-ephemerality premise.
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) supplies the promotion difficulty.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) grounds the split between knowledge record and system-definition companion cue.
- [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) grounds why failed attempts need a promotion standard rather than automatic graduation.

Suggested links:

- `grounds`: [Ephemeral computation prevents accumulation](../../notes/ephemeral-computation-prevents-accumulation.md)
- `extends`: [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md)
- `grounds`: [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md)
- `grounds`: [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md)
- `see-also`: [Designing a Memory System for LLM-Based Agents](../../notes/designing-agent-memory-systems.md)

## Good candidates that may be revisions instead of new notes

### Atomic memory and narrative memory need different retrieval interfaces

Possible title:

`Atomic memory and narrative memory need different retrieval interfaces`

Claim:

Atomic observations answer "have we seen this before?"; episodes answer "what happened when we tried this?" The former wants lookup and trigger matching; the latter wants narrative compression and contextual reading.

Reason to hesitate:

This is currently the strongest internal argument for the four-layer architecture. It might belong inside the source note unless another note needs to cite the distinction independently. If extracted, it should weaken the layer-count claim: the distinction requires different interfaces, not necessarily different physical storage layers.

Added grounding:

The stronger extraction may be broader than this title: **memory layers are progressive distillation interfaces**. [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) grounds the general mechanism: descriptions, observation summaries, episode goals, and full artifacts are different-resolution pointers used to decide what to load. [Distillation](../../notes/definitions/distillation.md) grounds the transformation between resolutions. This makes the note less about "atomic versus narrative" and more about matching artifact shape to consumer task and context budget.

Quality risk:

The claim is solid but may be too close to architecture justification unless generalized beyond the four-layer design. If extracted, avoid arguing for a fixed trace/observation/episode/library stack. Argue instead that memory systems need distinct retrieval interfaces when their consumers ask different questions: "has this happened?", "what happened?", "why did we choose?", and "what should I do now?"

Suggested links:

- `grounds`: [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md)
- `grounds`: [Distillation](../../notes/definitions/distillation.md)
- `grounds`: [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)
- `contrasts`: [Designing a Memory System for LLM-Based Agents](../../notes/designing-agent-memory-systems.md)

### Typed cue indexes are on-situation context injection

Possible title:

`Typed cue indexes are on-situation context injection`

Claim:

Typed cue indexes are the action-triggered counterpart to on-reference loading and on-invoke skill loading. They inject system-definition context when a situation or proposed action matches a stored trigger, rather than waiting for a direct query.

Reason to hesitate:

The exact "typed cue index" mechanism may be too implementation-shaped for a theoretical note. But the broader loading category, **on-situation injection**, is reusable. It connects the source note's cue machinery to the KB's context-engine theory.

Added grounding:

[Agent statelessness means the context engine should inject context automatically](../../notes/agent-statelessness-means-the-context-engine-should-inject-context.md) already proposes "on reference" injection. [Always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) distinguishes always-loaded, on-demand, and capability-description surfaces. This proposed note would add a missing row to the loading hierarchy: always, on reference, on situation, on invoke, on demand.

Quality risk:

The note should not overclaim that typed cues solve activation. It should stay at the context-engine mechanism level and defer success criteria to `System-definition cues need behavioral faithfulness tests`.

Suggested links:

- `extends`: [Agent statelessness means the context engine should inject context automatically](../../notes/agent-statelessness-means-the-context-engine-should-inject-context.md)
- `grounds`: [Always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md)
- `grounds`: [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md)
- `pairs-with`: `System-definition cues need behavioral faithfulness tests`

### Extraction taxonomy should follow oracle strength

Possible title:

`Extraction taxonomy should follow oracle strength`

Claim:

Session-log extraction types should be ordered and operationalized by the strength of the signal that justifies extraction and promotion. Corrections, silent failures, preferences, procedures, discoveries, decision provenance, and negative results differ less by topic than by oracle quality, recurrence needs, and promotion risk.

Reason to hesitate:

This may be a revision to the source note's extraction taxonomy rather than a standalone note. Extract it if the oracle-strength ordering becomes useful outside agent memory, for example in review-system learning, workshop-to-library promotion, or KB maintenance automation.

Added grounding:

[Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) provides the primary vocabulary. [Trace-derived learning techniques in related systems](../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) supplies evidence that trace-mining systems converge on similar stages but stall at evaluation, trust, persistence, and retirement. [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) explains why learned extraction/promotion policies only close cleanly when the task supplies a strong oracle.

Quality risk:

The note could become a catalogue. It needs a sharp claim: extraction schemas and build order should be derived from oracle strength, not from an intuitive list of memory types.

Suggested links:

- `grounds`: [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md)
- `evidence`: [Trace-derived learning techniques in related systems](../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md)
- `grounds`: [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md)
- `extends`: [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md)

### Graduation should wait until retrieval cost exceeds maintenance cost

Possible title:

`Graduation should wait until retrieval cost exceeds maintenance cost`

Claim:

Promoting an observation into a durable artifact creates maintenance obligations. Late graduation keeps storage cheap; premature graduation creates stale policy and curation debt.

Reason to hesitate:

This is valuable, but it may overlap with existing maintenance and entropy notes:

- [Entropy management must scale with generation throughput](../../notes/entropy-management-must-scale-with-generation-throughput.md)
- [Notes need quality scores to scale curation](../../notes/notes-need-quality-scores-to-scale-curation.md)
- [Ephemeral computation prevents accumulation](../../notes/ephemeral-computation-prevents-accumulation.md)

It may be better as a revision to one of those notes or as a short companion only if the "retrieval cost versus maintenance cost" formulation becomes reusable.

Added grounding:

The grounding pass adds a role-sensitive version of the claim. Knowledge-role graduation creates curation and retrieval obligations; system-definition graduation also creates behavior-change risk. That means the threshold should be higher for always-loaded instructions, guardrails, compiled cues, and tests than for ordinary knowledge records. [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md), [Methodology enforcement is constraining](../../notes/methodology-enforcement-is-constraining.md), and [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) are the useful grounding links if this becomes standalone.

### Reach reveals itself through accumulation

Possible title:

`Reach reveals itself through accumulation`

Claim:

An observation's generality is often unknowable when first captured. Multiple low-reach observations can later reveal a high-reach pattern, so capture and promotion should be separated.

Reason to hesitate:

This is elegant and probably true, but it partly restates the source note's store-broadly/promote-selectively position. It could become the theoretical core of "store-everything is a capture posture," or a separate note if the reach mechanism becomes central elsewhere.

Suggested direction:

Do not extract first. Fold it into the store-everything/capture-posture note as one mechanism.

Added grounding:

This is where [first-principles reasoning selects for explanatory reach over adaptive fit](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) should enter if the claim is extracted later. The memory-design version is: low-reach observations are often only distinguishable from high-reach patterns after accumulation. [Quality signals for KB evaluation](../../notes/quality-signals-for-kb-evaluation.md) can provide possible weak signals for when reach has become visible through links, recurrence, and neighborhood coherence.

### Silent failures should be extracted before final success normalizes them

Possible title:

`Silent failures should be extracted before final success normalizes them`

Claim:

When a task succeeds through fallback, retry, or workaround, the final answer hides degraded guarantees and tool defects. Session-log extraction should treat these as first-class repair or policy candidates.

Reason to hesitate:

There are already strong observability notes:

- [Apparent success is an unreliable health signal in framework-owned tool loops](../../notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned.md)
- [Silent disambiguation is the semantic analogue of tool fallback](../../notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md)
- [Enforcement without structured recovery is incomplete](../../notes/enforcement-without-structured-recovery-is-incomplete.md)

This may be better as a revision to the first note or a prescriptive extraction rule in instructions, unless we want a memory-specific note about "silent-failure extraction."

Added grounding:

The oracle-strength grounding makes this a stronger candidate than before. Silent failures have visible operational signals, errors, retries, fallback paths, degraded guarantees, but their significance still requires judgment. That puts them between hard-oracle corrections and weak-oracle discoveries. [Spec mining is codification's operational mechanism](../../notes/spec-mining-as-codification.md) also explains the graduation path: repeated silent failures can become checks, recovery rules, or deterministic guards.

Suggested links if extracted:

- `grounds`: [Apparent success is an unreliable health signal in framework-owned tool loops](../../notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned.md)
- `grounds`: [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md)
- `mechanism`: [Spec mining is codification's operational mechanism](../../notes/spec-mining-as-codification.md)
- `extends`: [Enforcement without structured recovery is incomplete](../../notes/enforcement-without-structured-recovery-is-incomplete.md)

## Lower-priority or keep-inside candidates

### Session logs are a composite soft oracle

The source note's "session logs as composite oracle" section is useful, but there is already a broader cluster around soft oracles, automated synthesis, and quality signals. Extracting it risks making a catalogue note rather than a sharp claim. Better use it as evidence inside future notes about capture posture, promotion oracles, or behavioral faithfulness.

Grounding to reuse:

- [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) gives the main vocabulary.
- [Quality signals for KB evaluation](../../notes/quality-signals-for-kb-evaluation.md) is the KB analogue of manufacturing a composite soft oracle from weak signals.
- [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) is the contrast case: when a hard task-completion oracle exists, the loop can be learned directly; session-log learning in open-ended settings lacks that advantage.

### Retrieval splits by role, not content

This is a strong design move, but it may already be covered by [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md), [Continual learning's open problem is behaviour, not knowledge](../../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md), and the source note itself. Extract only if future work repeatedly needs the exact retrieval/activation consequence of the role axis.

Grounding to reuse:

This should cite [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) if extracted. The retrieval split is one instance of the larger decomposition: knowledge-role access is context-engine retrieval and navigation; system-definition access is activation and behavior change.

### Typed cue indexes bridge the activation gap

This exact title is still too design-specific to extract as theory. It would make a better reference or instruction artifact once fields, matching rules, priority budgets, and tests are specified. The theoretical extraction should either be `System-definition cues need behavioral faithfulness tests` or the broader loading-mechanism claim `Typed cue indexes are on-situation context injection`.

### Four layers separate trace, observation, episode, and library

Do not extract as a theory note. This is the source note's architecture, not a standalone principle. If extracted, it would duplicate the synthesis without improving composability. The separable theory is narrower and better grounded as `Memory layers are progressive distillation interfaces` or `Atomic memory and narrative memory need different retrieval interfaces`.

## Suggested extraction order

1. `Store-everything is a capture posture, not a memory design`
2. `System-definition cues need behavioral faithfulness tests`
3. `Library-derived cues should be compiled views`
4. `Episodes are retrospective memory; workshops are active memory`
5. `Negative results are memory artifacts because final artifacts hide discarded paths`

This order fixes the source note's biggest theoretical overcommitment first, then strengthens the activation theory, then handles source-of-truth control and workshop integration. Negative results are valuable but less urgent because they do not currently create a contradiction in the architecture.

Near-term supporting candidates, not first-pass extractions:

- `Typed cue indexes are on-situation context injection` - write when the context-engine loading hierarchy needs the "on situation" row.
- `Extraction taxonomy should follow oracle strength` - write if the extraction taxonomy starts getting reused outside the memory-design note.
- `Memory layers are progressive distillation interfaces` - write only if the four-layer architecture needs a generalized defense without preserving the exact layer count.

## Impact on the source note

If these are extracted, `designing-agent-memory-systems.md` should become more explicitly architectural:

- Link to `Store-everything is a capture posture, not a memory design` in the opening and weaken "store everything" from premise to capture substrate.
- Link to `System-definition cues need behavioral faithfulness tests` in the commitment section and add a sentence that cue firing is only a candidate behavioral intervention.
- If `Typed cue indexes are on-situation context injection` is not extracted, still revise the cue section to name the mechanism as on-situation loading, parallel to on-reference and on-invoke context loading.
- Link to `Library-derived cues should be compiled views` in the library-to-observation backflow section and add provenance/source-hash/regeneration fields.
- Link to `Episodes are retrospective memory; workshops are active memory` near the episode layer and clarify that active work surfaces are adjacent to the retrospective memory stack.
- Link to `Negative results are memory artifacts because final artifacts hide discarded paths` in the negative-result use case and keep the source note focused on how the four-layer architecture stores and activates those records.
- If `Extraction taxonomy should follow oracle strength` stays unextracted, still revise the extraction section to order signal types by oracle strength and promotion risk.
- If `Memory layers are progressive distillation interfaces` stays unextracted, still revise the architecture section to present the four layers as one progressive-disclosure design rather than a universal layer count.

## Notes not to write yet

Do not write all candidates at once. The extraction should preserve composability, not create a burst of thin notes. Start with the first two because they repair real tensions in the current synthesis. Write the others when a second artifact needs to cite them or when the source note revision would otherwise become bloated.
