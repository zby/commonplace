=== SEMANTIC REVIEW: agent-is-a-tool-loop.md ===

Claims identified: 11

1. "The word 'agent' carries too much philosophical weight to define cleanly." (para 1 -- scope claim)
2. "an agent is a tool loop -- a prompt, a capability surface, and a stop condition" (para 1 -- definition, three components)
3. "The convention is deliberately minimal -- it says nothing about autonomy, planning, or goals." (para 2 -- scope claim)
4. "It names the unit of execution that a programmer spawns." (para 2 -- definition)
5. "A sub-agent is a child loop with its own prompt and capability surface." (para 2 -- definition)
6. "A multi-agent system is a tree of loops coordinated by code." (para 2 -- definition)
7. "Two loops with different tool surfaces but the same model are different agents" (para 2 -- definitional consequence)
8. "the same prompt run twice is two invocations" (para 2 -- definitional consequence)
9. "The convention tracks code structure, not character." (para 2 -- scope claim)
10. "If 'agent' means 'tool loop,' then spawning a sub-agent is spawning a sub-loop -- and the question of whether frameworks should expose the loop becomes the question of whether they support sub-agents as a first-class operation." (para 3 -- inference)
11. Link annotation: bounded-context orchestration model -- "each agent is one iteration of the `select/call/absorb` loop" (Relevant Notes section)

WARN:
- [Completeness] The three-component definition (prompt, capability surface, stop condition) omits state management. The tool-loop-index.md pseudocode includes an explicit `state` variable that accumulates tool results and drives the loop. The bounded-context orchestration model centers on `K` (the scheduler's full symbolic state) as a core component. An agent that runs `search -> read -> summarize` must carry intermediate results between iterations; something holds that state. A prompt alone does not account for it -- the prompt is the initial framing, while state is the evolving accumulation within the loop. The note's own definition of the tool loop ("running until the model finishes or the runtime cuts it off") implies persistence across iterations, but the three-component enumeration does not name what persists. A stateless single-shot LLM call also has a prompt, capability surface (none), and stop condition (one turn) -- but the note would not call that an agent, precisely because there is no loop iteration. The missing fourth element is what makes the loop a loop rather than a single call.

- [Completeness] The definition "A multi-agent system is a tree of loops coordinated by code" claims tree structure, but multi-agent systems can have non-tree topologies. A pipeline (A -> B -> C where C's output feeds back to A) is a cycle, not a tree. Peer-to-peer architectures where two agents negotiate by exchanging messages form a graph with mutual edges. The tool-loop-index.md itself references "conversation vs prompt refinement in agent-to-agent coordination," which describes return paths that imply graph structure. "Tree" is too narrow unless the note intends to restrict the convention to strictly hierarchical systems, which it does not state.

- [Grounding] The link annotation for bounded-context-orchestration-model.md says "each agent is one iteration of the `select/call/absorb` loop." The source note does not use the word "absorb" as a named operation -- its loop is `select/call/append` (literally `P = select(K); r = call(P); K = K + r`). The source also does not equate "agent" with "one iteration"; it equates an agent call with a bounded LLM invocation. An agent in the convention note is the entire loop (multiple iterations), not one iteration of it. The annotation conflates two levels: one iteration of the orchestration model's loop is one bounded call, while one agent (per this note's own definition) is a full tool loop containing many such calls.

INFO:
- [Completeness] The note says the convention "says nothing about autonomy, planning, or goals" and is "deliberately minimal." This is a strength for code organization, but a boundary case worth noting: a system that plans extensively (e.g., decomposes a goal into sub-goals before executing any of them) and a system that blindly executes tool calls without planning are both "agents" under this convention. The convention's value proposition is that it tracks code structure, but planning-heavy agents may have identical code structure (same prompt, tools, stop condition) yet very different operational character due to the prompt's content. The convention collapses the prompt's content and the prompt's structural role -- by design, but users of the convention should know that two agents with radically different behaviors are indistinguishable at the convention level.

- [Completeness] Claim 8 says "the same prompt run twice is two invocations." This distinguishes invocations from agents. But the note does not clarify what makes two loops the "same agent type" versus "different agents." If two loops share the same prompt template but are instantiated with different task parameters, are they the same agent or different agents? The convention identifies agents by code structure (prompt + capability surface + stop condition), but prompt templates with variable slots blur the identity boundary. This is an edge case the convention does not address.

- [Internal consistency] The note defines an agent as "a prompt, a capability surface, and a stop condition" (three components), but the sub-agent definition in claim 5 mentions only "its own prompt and capability surface" -- dropping the stop condition. This is likely just abbreviated phrasing rather than a real inconsistency, but it creates a minor ambiguity about whether the stop condition is truly a defining component or is implicitly inherited.

PASS:
- [Internal consistency] The core definitional chain is internally consistent: agent = tool loop -> sub-agent = child loop -> multi-agent = composition of loops. Each level builds on the prior without contradiction. The "tracks code structure, not character" framing is faithfully maintained throughout -- the note never slips into characterizing agents by their behavior or capabilities.

- [Grounding] The link to tool-loop-index.md is well-grounded. The index's Resolution section explicitly says "The first and third cases call for sub-agents -- fresh tool loops with their own prompt, capability surface, and stop condition," which matches this note's definition verbatim. The index also links back to this note with the annotation "convention: grounds the sub-agent mechanism by equating 'agent' with 'tool loop'," confirming bidirectional alignment.

- [Grounding] The link to subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md is well-grounded. That note's argument -- that different capability surfaces require fresh loops -- directly motivates this note's claim that "sub-agents are needed precisely because children need different capability surfaces." The source note's conclusion ("the framework treats spawning a new loop as a first-class operation") aligns with this note's inference in claim 10.

- [Internal consistency] The note's framing as "convention, not definition" is maintained consistently. It never claims the three-component model captures the essence of agency -- it explicitly disclaims that ("carries too much philosophical weight to define cleanly"). The payoff argument in paragraph 3 stays within the convention's scope, deriving a framework-design consequence rather than a philosophical one.

Overall: 3 warnings, 3 info
===
