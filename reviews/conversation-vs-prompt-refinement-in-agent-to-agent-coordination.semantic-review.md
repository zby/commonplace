=== SEMANTIC REVIEW: conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md ===

Claims identified: 14

**Claim inventory:**

1. The note examines "one local case of the broader handoff-artifact problem" (intro)
2. "The calling agent has at least three options" — conversation, prompt refinement, hybrid (intro enumeration)
3. "Conversation feels natural because humans can't rewind" (intro)
4. "Conversation is cheaper for the caller" (The tradeoff)
5. "Prompt refinement is cleaner for the callee" — fresh lexically scoped frame without accumulated debris (The tradeoff)
6. "Prompt refinement is more work for the caller" (The tradeoff)
7. "Conversation preserves intermediate results" — the later in the task a question arises, the stronger the case for continuing (The tradeoff)
8. In the bounded-context orchestration model, adding prompt-refinement logic to the scheduler is "incremental complexity in the right place" (Where should complexity live?)
9. When the caller is also an LLM, "the 'right place for complexity' argument weakens" (Where should complexity live?)
10. Design heuristic: "conversation is the natural interface for human-agent interaction; prompt refinement has advantages for agent-agent interaction when the caller is a symbolic scheduler" (Where should complexity live?)
11. The voooooogel onboarding interview is useful "not because conversation is the right interface, but because the caller's initial prompt was underspecified" (Onboarding and forking)
12. Forking is "a third pattern — context cloning — that preserves a selected trace prefix for reuse without continuing the same conversation indefinitely" (Onboarding and forking)
13. With KV-cache sharing, "the cloned prefix is also computationally cheap" (Onboarding and forking)
14. The three-option enumeration (conversation, refinement, hybrid) is later expanded to include context cloning/forking as a distinct pattern (Onboarding and forking)

---

WARN:
- [Completeness] The note opens with "at least three options" — conversation, prompt refinement, and hybrid — but the "Onboarding and forking" section identifies a fourth pattern, "context cloning," which the note says is "neither pure conversation... nor pure refinement." The initial enumeration and the final taxonomy are inconsistent: the note starts with three options, ends with four (or at least three-and-a-half, since forking is treated as distinct from the hybrid). The hybrid option also receives no further analysis after its one-sentence introduction — it is never mentioned in "The tradeoff" section or "Where should complexity live?" — making it unclear whether the note considers it a real design option or a footnote. A reader could reasonably wonder whether the "three options" framing undercounts the space from the start.

- [Grounding alignment] The note claims the voooooogel onboarding interview is useful "not because conversation is the right interface, but because the caller's initial prompt was underspecified." This reframes the source's argument in terms the source does not use. The source says: "it's just too difficult to ask a model to reliably spawn a subagent with a single prompt" — which is a claim about the difficulty of single-shot prompting, not about underspecification per se. The source treats the conversation as a positive mechanism ("let spawned instances ask questions back to their parent"), not as a workaround for a failure. The note's "refinement lens" reading is an inference the note itself is making, not an attribution to the source. The note does hedge with "one reading through the refinement lens," which mitigates this, but readers may still over-attribute the reframing to voooooogel.

- [Completeness] The tradeoff section is organized as a set of factors (caller cost, callee cleanliness, intermediate work preservation), but it omits a factor the note's own linked sources make salient: **error propagation**. The session-history note explicitly discusses how "local tactical debris survives beyond the stage where it mattered" and how "downstream stages must re-interpret rather than consume a clean artifact." In the conversation pattern, the sub-agent's initial misframing and the correction exchange remain in context and can bias subsequent reasoning — a cost beyond mere token volume. The note mentions "accumulated debris of the initial misframing, the question, and the correction" in passing under refinement's benefit but does not identify error propagation / context pollution as a distinct tradeoff dimension, despite its linked foundations treating it as central.

INFO:
- [Completeness] The design heuristic "conversation is the natural interface for human-agent interaction; prompt refinement has advantages for agent-agent interaction when the caller is a symbolic scheduler" frames the choice as depending primarily on caller type. But the note's own tradeoff section identifies task progress ("the later in the task a question arises, the stronger the case for continuing") as an independent variable. These two dimensions — caller type and task progress — could interact: even a symbolic scheduler might prefer conversation when the sub-agent is 80% through an expensive task. The heuristic as stated collapses these two dimensions into one.

- [Grounding alignment] The note says prompt refinement gives the callee "a fresh lexically scoped frame" and links to the scoping note. The scoping note's concept of lexical scoping via sub-agents is about isolation from inherited conversation history — a sub-agent gets "its own system prompt, its own input, no inherited conversation history." This aligns well with refinement's clean-context benefit. However, the scoping note's "lexically scoped frame" concept is broader than what prompt refinement provides — it includes the design-time declaration of what bindings are visible, the return-value interface, and progressive typing. The note uses "lexically scoped frame" as shorthand for "clean context," which is accurate but narrower than the full concept in the linked source.

- [Internal consistency] The note says "Conversation feels natural because humans can't rewind. Once we've said something, we can only append corrections. Agents have no such constraint — they can cheaply re-invoke with a better prompt." The claim that re-invocation is "cheap" stands in tension with the later claim that "Prompt refinement is more work for the caller" and the observation that conversation preserves intermediate results (which refinement discards). "Cheap" here appears to mean computationally feasible (agents can do it), not low-cost, but the unqualified word could mislead.

- [Completeness] The open questions ask "Does the conversation/refinement distinction collapse with KV-cache sharing?" but the note already partially answers this in the forking section: "With KV-cache sharing, the cloned prefix is also computationally cheap." The relationship between the open question and the partial answer in the body is not made explicit. If KV-cache sharing makes forking cheap, and forking subsumes both patterns (as the fourth open question suggests it might), the note already has the ingredients for a tentative answer.

PASS:
- [Grounding alignment] The note's characterization of the bounded-context orchestration model is accurate. The linked note describes a "symbolic scheduler over unbounded exact state" that "assembles prompts and orchestrates the workflow." The reviewed note's claim that "the scheduler is already the coordination layer — it holds unbounded symbolic state, assembles prompts, and orchestrates the workflow" is a faithful paraphrase.

- [Grounding alignment] The note's use of the LLM-mediated scheduler note is accurate. The linked note says "the LLM serves as both scheduler and executor — it suffers the same attention dilution and compositional overhead." The reviewed note's claim that when the caller is also an LLM, "both sides are context-constrained" correctly reflects this.

- [Grounding alignment] The note's characterization of voooooogel's forking pattern is accurate. The source says: "have the parent instance spawn a single fresh subagent, be interviewed about all ten tasks at once by that subagent, and then have that now-onboarded subagent fork into ten instances, each with the whole onboarding conversation in context." The note's summary — forking preserves "a selected trace prefix for reuse without continuing the same conversation indefinitely" — captures the essential structure.

- [Internal consistency] The "Where should complexity live?" section and the tradeoff section are mutually consistent. The tradeoff section presents factors without resolving them; the architecture section resolves them conditionally based on caller type. The tentative heuristic is appropriately hedged ("suggests a tentative design heuristic rather than a hard principle") and does not overclaim.

- [Grounding alignment] The parent note (session-history-should-not-be-the-default-next-context) explicitly identifies conversation-vs-refinement as "one instance of the general problem" and lists the same three patterns (conversation, prompt refinement, context cloning). The reviewed note's framing as "one local case of the broader handoff-artifact problem" is consistent with the parent's framing.

Overall: 3 warnings, 4 info
===
