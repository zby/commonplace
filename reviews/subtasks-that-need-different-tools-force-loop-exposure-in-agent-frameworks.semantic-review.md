=== SEMANTIC REVIEW: subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md ===

Claims identified: 12

1. [P1, title/opening] A framework-owned tool loop works well when one task runs against one stable set of tools.
2. [P1] The constraint appears when a parent task decomposes into children that each need a different capability surface.
3. [P2] Changing the capability surface changes the action alphabet of the next bounded call — what the model is allowed to do, not just what state surrounds it.
4. [P2] This requires constructing a fresh call with a fresh prompt, a fresh tool set, and often a fresh stop condition.
5. [P3, enumeration] A framework-owned loop has only awkward responses: (a) one giant static tool set, (b) a meta-tool that becomes the real scheduler, or (c) escape back into direct API calls.
6. [P4] The clean response is to spawn a sub-agent: a fresh tool loop with its own prompt, capability surface, and stop condition.
7. [P5] Adding tools is relatively clean; removing tools that already appear in the conversation history is not.
8. [P5, causal] The model has memories of calling those tools; their absence creates incoherence.
9. [P5, scope] You cannot cleanly shrink a context's action alphabet — you can only start a fresh context where it was never larger.
10. [P5] That asymmetry is why sub-agents keep winning over in-place tool mutation.
11. [P6, definition] Loop exposure is the general property — the framework lets the application control what the next step can do.
12. [P6] Sub-agents are the dominant mechanism because they provide the fresh context that dynamic tool removal cannot.

---

WARN:
- [Completeness] The three "awkward responses" enumeration (claim 5) — giant static tool set, meta-tool scheduler, escape to direct API calls — may miss a fourth option: **dynamic tool registration per turn**. Some frameworks (e.g. OpenAI Assistants API, LangGraph) allow the application to modify the tool list between turns within the same conversation/thread without spawning a full sub-agent. This is not the same as "one giant static tool set" (the tools do change) and not the same as "escape back into direct API calls" (the framework still manages the loop). The note's own later discussion of tool addition/removal partially acknowledges this space but does not fold it back into the enumeration. Whether dynamic per-turn registration counts as a clean response or still an awkward one is arguable, but the enumeration as written claims to be exhaustive ("only awkward responses") and does not cover it.

- [Completeness] The claim "you cannot cleanly shrink a context's action alphabet" (claim 9) is stated as absolute but the argument supporting it is specifically about conversation-history incoherence — the model remembering prior tool calls. This leaves a boundary case unaddressed: what about removing a tool the model has **never called** in the current conversation? The tool appeared in the tool list but was never invoked. Its removal would not create memories-of-calling incoherence. The note's argument does not distinguish between "tool was available and used" vs. "tool was available but unused," yet the incoherence mechanism it cites applies only to the first case. This may weaken the absolute framing.

INFO:
- [Completeness] The note's central scenario is parent-child decomposition where children need different tool surfaces. A boundary case: what about tasks where the **same** child needs a **sequence** of different tool surfaces (e.g., first search, then code, then review)? The note's sub-agent model handles this by nesting — the child itself becomes a parent that spawns sub-agents — but this recursive case is only obliquely acknowledged via the link to "semantic sub-goals that exceed one context window." A sentence explicitly noting the recursive case would strengthen the argument.

- [Grounding alignment] The note links to "stateful-tools-recover-control-by-becoming-hidden-schedulers" with the annotation "concession: grants the strongest stateful-tool escape hatch without treating it as a clean recovery." The linked note indeed says a stateful tool can "recover substantial control" and that "changing the action alphabet between sub-tasks" is where the recovery "starts to buckle." The attribution is accurate, but the reviewed note's framing is slightly stronger: it says the framework has "only awkward responses" (claim 5), while the stateful-tools note says a hidden scheduler "can recover substantial control" — which might be awkward but is not presented as purely awkward in the source. The gap is small but the emphasis differs.

- [Internal consistency] The note says "Adding tools is relatively clean: the model just sees new affordances" (claim 7), but earlier it says changing the capability surface "requires constructing a fresh call with a fresh prompt, a fresh tool set, and often a fresh stop condition" (claim 4). Adding tools IS changing the capability surface, yet the note treats addition as not requiring a fresh call. These two statements are consistent only if "changing the capability surface" in claim 4 is implicitly scoped to mean "changing in ways that require removal." The text does not make this scoping explicit, creating a potential ambiguity for a reader who encounters claim 4 before claim 7.

PASS:
- [Grounding alignment] The link to "bounded-context-orchestration-model" is annotated "background: each child task is naturally a fresh bounded call with its own selected context and tools." The bounded-context note indeed frames orchestration as a symbolic scheduler over bounded calls where each call gets its own prompt assembled from state. The reviewed note's concept of sub-agents as fresh bounded calls maps directly to this model. Attribution is accurate.
- [Grounding alignment] The link to "semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems" is annotated "complements: some sub-goals require fresh calls not only because tools change but because the sub-goal itself exceeds one context window." The linked note confirms this: it addresses context overflow as an independent reason for decomposition. The complementary relationship is correctly stated.
- [Internal consistency] The note's definition of "loop exposure" in P6 ("the framework lets the application control what the next step can do") is consistent with the entire preceding argument. The progression from problem (different tools needed) to failed responses (static set, meta-tool, escape) to clean response (sub-agents) to generalization (loop exposure) is logically coherent with no definitional drift.
- [Internal consistency] The add/remove asymmetry argument (claims 7-10) is internally consistent: adding tools adds affordances the model had no prior interaction with, removing tools creates incoherence with memories of prior calls, therefore fresh contexts sidestep the problem. The causal chain holds.

Overall: 2 warnings, 3 info
===
