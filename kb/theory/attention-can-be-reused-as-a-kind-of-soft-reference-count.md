---
description: "Very speculative: attention statistics and explicit output messages could help a harness decide what context to unload; model-generated future-use conditions could guide restoration."
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: [context-engineering]
---

# Model signals could guide harness-level context unloading and recall

**Very speculative.** A harness could use two kinds of model signal to manage active context: attention statistics that indicate recent use, and explicit output messages that identify what to unload and when to restore it. The first is retrospective; the second could express future-use conditions. They could operate separately or together. Neither mechanism is tested here.

For explicit messages, the model's ordinary output stream already supplies a communication channel. The missing pieces are agreed control messages, a harness that acts on them, and a policy that uses them reliably.

The proposed advantage is prospective: while material is still available, the model can identify circumstances in which it will matter again. For tasks with delayed dependencies, this could reduce active-context cost without the recall failures caused by unloading material and later having to rediscover why it mattered. Whether that advantage survives the cost of control messages, trigger detection, and reloading is unknown.

## From observed use to future-use conditions

Aggregated transformer attention weights could supply a retrospective signal: which messages the model has recently used. This is closer to a cache usage statistic than a reference count. A reference count records existing references; attention records weighted access during computation. Low attention cannot reliably distinguish irrelevant material from a dormant dependency, and high attention alone does not establish that retaining material improves the task outcome.

The stronger conjecture is a model-generated instruction: “I do not need this now; restore it before database work.” That instruction names a future-use condition rather than merely reporting recent use. Transformer attention weights do not themselves express such conditions. A model could instead generate them as ordinary output tokens, including structured tool calls. Access to internal attention weights is therefore optional, not a prerequisite.

For example, the model could identify schema details and query examples by stable identifiers and request that they leave active context until database-query construction resumes. The harness would retain the content and the restoration condition outside active context. When the model signals that it is entering query construction, the harness would restore the material before dependent reasoning continues. This is an illustrative mechanism, not an implemented protocol.

The distinction matters because [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md). Retaining a history does not require loading all of it into each invocation. Conditional recall would let the model help select what stays available now and what can wait.

## The output stream can carry the control signal

Two arrangements could use the existing output channel:

- **Explicit signaling:** the model emits a control message before starting an activity whose dependencies have been unloaded. The harness restores registered material before continuing execution.
- **Implicit monitoring:** the harness watches ordinary output for signs that a restoration condition holds. This requires less explicit signaling but may detect the need only after the model has made a decision that depended on the missing material.

Both require an execution boundary where the harness can intervene. With ordinary request-response model APIs, a practical route would be to stop or finish generation, assemble a revised input, and invoke the model again. The proposal does not assume that an API permits context insertion during uninterrupted generation.

The restoration condition must remain available after the content is unloaded. Otherwise the system could need the missing content to recognize the event that would restore it. A small reminder could remain in active context, or the harness could monitor an independently observable event. The content, the condition, and the machinery that detects the condition have distinct storage and execution costs.

## Training could reward timely recall

General learning could improve the policy that uses this channel. That does not require a new communication channel: the existing output stream is sufficient if the harness interprets its control messages. But [a context-operation interface bounds what its policy can realize](./context-operation-interface-bounds-context-policy.md). Training cannot make an unchanged harness unload or restore material unless some available operation already enables that effect.

A possible training route would combine demonstrations of the protocol with task rollouts in which the harness actually obeys the model's context decisions. Demonstrations could teach how to identify material, register a restoration condition, and signal an activity before its missing dependencies affect reasoning. Outcome-based training could then reward task success while charging for active-context use, extra calls, and unnecessary reloads. These are candidate training pressures, not demonstrated methods for this mechanism.

Delayed-dependency tasks would be important: a detail matters early, is irrelevant through a long intervening phase, and becomes necessary again under a later condition. Tasks without that structure might reward keeping everything or dropping old material without learning conditional recall. The specific target is to restore information before a dependent decision, not merely repair an error afterward.

Controlled continuations from the same checkpoint could compare retaining material, unloading it without a condition, and unloading it with conditional restoration. Such comparisons could help attribute outcomes to context decisions rather than merely imitate decisions found in successful runs. Their additional training cost would need to be counted.

## Scope

- This is not a claim that existing models reliably predict future information needs, or that attention statistics provide reliable eviction scores.
- KV-cache eviction manages cached key and value vectors used during transformer inference. This proposal manages addressable messages, documents, or fragments supplied as model input. The distinction is the managed representation and control interface, not simply “inside one call” versus “across calls”: caches can persist across turns.
- Unloading means removing material from active context, not deleting retained content. Ordinary search or explicit recall would still be needed for future uses that no registered condition anticipated.
- Reloading requires enough available context budget and a safe intervention point. Rebuilding an input may also sacrifice cache reuse; token savings alone do not establish lower total cost.
- A restoration cue can arrive too late, fail to occur, or activate too broadly. The mechanism could therefore add overhead without improving recall.
- The analogy to classical memory management remains loose. [Sub-agent scoping](./llm-context-is-composed-without-scoping.md) can discard a completed local context as a unit; conditional recall addresses material that may be needed again within continuing work.

## Open Questions

- Can a model specify useful future-use conditions while material is loaded, and still emit the right cue after that material has left its input?
- Which conditions should be explicit model signals, and which can the harness detect independently?
- Do conditional restoration instructions beat ordinary on-demand recall or attention-ranked eviction at comparable task success and total cost?
- Does outcome-based training improve the timing and usefulness of signals beyond prompting or supervised demonstrations?
- Do internal attention statistics add useful information once the model can issue explicit context-control messages?

---

Relevant Notes:

- [Bounded context orchestration model](./bounded-context-orchestration-model.md) — contrasts: code selects each call's context from explicit state rather than asking the model to manage an accumulating session context
