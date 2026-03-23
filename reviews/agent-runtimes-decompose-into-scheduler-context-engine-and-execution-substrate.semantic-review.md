=== SEMANTIC REVIEW: agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md ===

Claims identified: 14

1. [Enumeration] Practitioner runtime taxonomies converge on three separable components: scheduler, context engine, and execution substrate. (Opening section)
2. [Definition] Scheduler owns control flow, decomposition, and state progression across bounded calls. Answers "what happens next?" (Opening list)
3. [Definition] Context engine decides what enters each bounded call and in what frame. Answers "what does this call get to see?" (Opening list)
4. [Definition] Execution substrate provides the persistent and executable world outside the model: files, tools, sandboxes, versioned artifacts. Answers "where do exact state and actions live?" (Opening list)
5. [Scope claim] The functions are analytically distinct even when implementations blur. (Opening section, "Not every system exposes these as neat modules")
6. [Causal claim] The decomposition clarifies why practitioner taxonomies keep converging on similar component lists. (Opening section)
7. [Mapping claim] Vtrivedy10's six practitioner components map cleanly into the three-part decomposition. (Mapping table)
8. [Causal claim] The source's "everything not the model" definition is descriptively useful but architecturally unstable — it names a perimeter, not a decomposition. (Below mapping table)
9. [Grounding claim] The scheduler is formalized by the bounded-context orchestration model. ("Why the split matters")
10. [Grounding claim] The context engine is formalized by context engineering: routing, loading, scoping, and maintenance. ("Why the split matters")
11. [Grounding claim] The execution substrate is grounded by inspectable-substrate and files-not-database notes. ("Why the split matters")
12. [Convergence claim] Three independent practitioner sources each emphasize different parts of the runtime, but convergence is clearer under this decomposition. ("Why independent sources converge here")
13. [Attribution] Lopopolo's report emphasizes constraints hardening across the runtime — most visible in scheduler and substrate. ("Why independent sources converge here")
14. [Attribution] The cybernetics thread frames the space as sensors, actuators, and feedback loops — especially clarifies the scheduler/substrate interface. ("Why independent sources converge here")

---

WARN:
- [Completeness] The three-part decomposition (scheduler, context engine, execution substrate) has a boundary case around **inter-component communication and data flow**. Consider a message bus, event system, or shared protocol layer that mediates between the scheduler and the context engine — for example, a standardized interface through which the scheduler tells the context engine what to load next. This is not clearly the scheduler (it is not deciding what happens next), not the context engine (it is not selecting or framing content), and not the execution substrate (it is not providing persistent state or tool execution). The note's Scope Limits section acknowledges "evaluation infrastructure, policy layers, and social workflows may deserve their own treatment," but does not address the communication fabric between its own three components. In many real agent systems, the integration layer is a distinct engineering concern with its own failure modes.

- [Completeness] The mapping table assigns "Memory/search" to "Context engine + execution substrate" with the split "Retrieval logic is context engineering; the stored artifacts live on the substrate." However, the boundary case of **learned or adaptive retrieval** — where the retrieval system improves its own indexing or ranking over time based on usage patterns — sits awkwardly across this split. The learning/adaptation mechanism is neither pure context-engine logic (it is not just deciding what to load for a single call) nor pure substrate (it is not just storing artifacts). It is a feedback loop that modifies the retrieval function itself. The note does not address whether self-modifying retrieval belongs to the scheduler (which manages state progression), the context engine (which does retrieval), or something else.

- [Grounding] The note claims Lopopolo's report "emphasizes how constraints harden across the runtime — instructions, structural tests, cleanup agents" and that "That improvement path runs through all three components but is most visible in the scheduler and substrate becoming more reliable over time." However, the Lopopolo source focuses on constraining, context engineering (AGENTS.md as map), and entropy management via cleanup agents — all of which are described in terms of repo artifacts, CI, and linters. The source does not discuss the *scheduler* becoming more reliable, nor does it use any language about control flow or state progression improving. The note's claim that the hardening is "most visible in the scheduler and substrate" is the note's own interpretive overlay; the source's emphasis is on constraining and verification infrastructure, which maps more naturally to the execution substrate and perhaps the context engine, but not obviously to the scheduler component as this note defines it.

INFO:
- [Completeness] The execution substrate is defined as providing three things: persistent state, tool execution surfaces, and safety boundaries. The simplest possible instance of an agent runtime — a single script that calls an LLM API, reads stdin, and writes stdout — has minimal persistent state (just the conversation), no sandboxing, and trivial tool execution. Under the note's decomposition, this system has an extremely thin execution substrate, a collapsed scheduler (the script's main loop), and essentially no context engine. The decomposition still applies but does not illuminate much about this minimal case. The note's value proposition ("the distinction clarifies why practitioner taxonomies keep converging") is most useful for systems of moderate-to-high complexity. This is not a problem, but worth noting as a scope observation.

- [Completeness] The note assigns the cybernetics source's "sensors" and "actuators" language as cutting "across all three components but especially clarifies the scheduler/substrate interface." However, sensors (which read state) could equally be framed as a context-engine concern (they determine what the system sees), not just a scheduler/substrate interface. The mapping of cybernetic concepts to the three-part decomposition is suggestive but not developed enough to confirm a clean fit.

- [Grounding] The note claims the cybernetics thread "frames the space as sensors, actuators, and feedback loops" and that this "especially clarifies the scheduler/substrate interface: the scheduler reads state from the substrate and writes decisions back to it." The cybernetics ingest does describe sensors, actuators, and feedback loops, but its emphasis is on *externalized judgment* and *evaluation infrastructure* — not on a scheduler/substrate interface specifically. The note's framing of the cybernetics source as clarifying a scheduler/substrate interface is a reasonable interpretation but goes beyond what the source explicitly argues. The source's feedback loops are about constraining and correcting agent behavior, not about how a scheduler component interacts with a substrate component.

- [Internal consistency] The note defines the context engine as answering "what does this call get to see?" and later says "many things attributed vaguely to 'memory' are actually context-engine decisions. Retrieval, injection, frame construction, progressive disclosure, and compaction all concern bounded visibility, not durable storage." But the context-engineering note it links to includes "maintenance" as a fourth operational component — and maintenance (compaction, cleanup) has a temporal, cross-session dimension that extends beyond "what does this call get to see." The note's one-line definition of the context engine is narrower than the full concept it maps to. Not a contradiction, but the compact definition undersells the temporal dimension of the context engine.

PASS:
- [Completeness] The six-to-three mapping table was tested against all six of Vtrivedy10's practitioner components. Each maps to exactly one or two of the three runtime components with a stated rationale. No practitioner component is left unmapped, and no mapping is forced into an implausible category. The split of "Memory/search" across two components is explicitly justified. The mapping is internally consistent.

- [Grounding] The bounded-context orchestration model note does formalize a symbolic scheduler driving bounded LLM calls through a select/call loop. The note's claim that this "formalizes the scheduler component" is accurate — the orchestration model describes exactly control flow, decomposition, and state progression, matching the scheduler definition.

- [Grounding] The context-engineering note does decompose into routing, loading, scoping, and maintenance. The note's claim that context engineering "formalizes the context engine" is accurate.

- [Grounding] The inspectable-substrate note does argue that repo artifacts (files, diffs, tests) are governable in ways weights are not. The files-not-database note does argue for filesystem-first substrate. Both ground the execution substrate component as claimed.

- [Grounding] The Vtrivedy10 ingest does derive six components from model limitations and does define harness as "everything not the model." The note's characterization of the source is accurate, and the note's critique ("architecturally unstable — names a perimeter, not a decomposition") is the note's own move, clearly distinguished from attribution.

- [Internal consistency] The note's three definitions (scheduler, context engine, execution substrate) are used consistently across all sections. The scheduler is always about control flow and state progression. The context engine is always about what enters bounded calls. The execution substrate is always about persistent state and tool surfaces. No definition drift was detected.

- [Internal consistency] The Scope Limits section accurately reflects the body's claims. It does not overclaim exhaustiveness ("not a claim that these three components are the only ones that matter") and does not overclaim implementation requirements ("not a claim that every implementation must enforce hard module boundaries"). The body supports both qualifications.

Overall: 3 warnings, 4 info
===
