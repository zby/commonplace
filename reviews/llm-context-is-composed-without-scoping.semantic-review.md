=== SEMANTIC REVIEW: llm-context-is-composed-without-scoping.md ===

Claims identified: 18

1. [Intro] "There is no scoping mechanism. Everything is global."
2. [Intro] "This is not even dynamic scoping, which at least has a stack with push and pop."
3. [Intro] The three pathologies (spooky action at a distance, name collision, inability to reason locally) are "the same ones that dynamic scoping produces."
4. [Structural parallel] Four-item enumeration of properties shared between flat context and dynamic scoping.
5. [What flat context buys] Dynamic scoping survived in Emacs Lisp because of "implicit communication" — functions influence each other without explicit parameter passing.
6. [What flat context buys] The right model is "lexical scope by default, dynamic scope when explicitly requested" (attributed to Common Lisp).
7. [Capture problem] Flat concatenation creates a composition-specific problem: capture. Framed as "the same problem Scheme's hygienic macros solve."
8. [Within-frame hygiene] Three mechanisms listed (role markers, delimiters/quoting, ordering conventions) are "the only scoping mechanisms available" within a single context.
9. [Within-frame hygiene] These mechanisms "can't prevent capture."
10. [Sub-agents] "Sub-agents are the one place where real isolation is achievable."
11. [Sub-agents] Sub-agent isolation "is lexical scoping."
12. [Sub-agents] Lexically scoped bindings: system prompt, specific input, explicitly passed context. Dynamically scoped bindings: user preferences, safety policies, global constraints.
13. [Return value problem] Codification becomes load-bearing because frame boundaries are explicit interface points for progressive typing.
14. [Return value problem] "The flat context has no such interface points."
15. [What exists today] Three existing systems listed as approximations of lexical scoping.
16. [What exists today] Three KB-design patterns listed as "already lexical scoping in practice."
17. [Undeveloped: Recursion] ConvexBench claim: LLMs collapse from F1=1.0 to F1~0.2 at depth 100, token count trivial (5,331); pruning history to direct dependencies recovers F1=1.0.
18. [Undeveloped: Recursion] This confirms: "the stack discipline's value is not just theoretical tidiness but measurable recovery of reasoning capability that flat accumulation destroys."

---

WARN:
- [Completeness] Claim 8 states role markers, delimiters/quoting, and ordering conventions are "the only scoping mechanisms available" within a single context. This misses at least one mechanism: **attention steering via structured prompting** — techniques like chain-of-thought, or explicit "ignore previous instructions" resets, which attempt to narrow effective scope within a flat context. More significantly, it omits **tool-use boundaries**: when a tool call returns structured output, the tool's execution happens outside the context window entirely, creating a de facto scope boundary even within a single agent frame (the tool's internal reasoning is invisible). The note later discusses sub-agents as providing isolation, but tool calls already provide partial isolation without spawning a sub-agent. The enumeration's "only" claim is stronger than what it covers.

- [Grounding alignment] Claim 17-18 attributes ConvexBench's performance recovery to the stack-frame/scoping discipline specifically. The source (Liu et al., 2026) describes a three-component solution: (1) external parsing tools that offload expression decomposition, (2) enforced recursive step-by-step verification, and (3) focused context pruning. The note frames the recovery as confirming "give each call a clean frame" — isolating the context-pruning component as the explanatory mechanism. But the source's ablation shows that decomposition alone (without focused context) already provides substantial gains, and the full solution bundles all three components. The note's framing — "When the authors prune accumulated history to retain only direct dependencies at each recursive sub-step (i.e., give each call a clean frame), performance recovers to F1=1.0" — presents a partial cause as the complete explanation. The parenthetical "(i.e., give each call a clean frame)" is an interpretive gloss the source does not make; the source frames it as "focused context" within an agentic framework, not as lexical scoping.

- [Completeness] Claim 10 states sub-agents are "the one place where real isolation is achievable." This overlooks **tool-mediated isolation**: a deterministic tool (e.g., a Python script) that processes input and returns output provides genuine isolation — its internal computation is entirely outside the LLM context. The note discusses tools elsewhere in the KB (codification, typed callables) but here treats sub-agents as the sole isolation mechanism. A tool call is arguably *stronger* isolation than a sub-agent (which still runs within an LLM and can be influenced by its own context engineering), yet it goes unmentioned. The claim would be more precise as "sub-agents are the one place where *LLM-mediated* isolation is achievable."

INFO:
- [Completeness] The three pathologies (claim 3) — spooky action at a distance, name collision, inability to reason locally — map well to classic dynamic-scoping problems. However, flat LLM context has at least one pathology that dynamic scoping does *not* produce: **attention dilution**. In dynamic scoping, looking up a binding is O(1) per scope level; in an LLM context, every token competes for attention with every other token, so adding irrelevant content degrades performance even when no name collision or scoping failure occurs. The note's KB itself discusses this in the "soft degradation" and "context efficiency" notes. This is not a gap in the analogy so much as an under-documented limitation of it — the pathologies of flat context are a superset of dynamic-scoping pathologies, not an equivalent set.

- [Internal consistency] The note says flat context "is not even dynamic scoping, which at least has a stack with push and pop" (claim 2), then later says "the pathologies are the same ones that dynamic scoping produces" (claim 3). These are not contradictory, but the framing creates a tension: if flat context is strictly worse than dynamic scoping (no stack), one would expect strictly worse pathologies, yet the note presents identical pathologies. The note implicitly handles this by saying the pathologies are "the same" while the mechanism is different (flat vs. stack-based), but a reader could reasonably wonder whether flat context produces *additional* pathologies beyond dynamic scoping's set. The attention-dilution point above is one such candidate.

- [Grounding alignment] The note links to the "three-space memory" note and claims that "operational debris pollutes search" is the scoping version of the three-space failure mode. The linked note frames these failure modes as consequences of flat *memory* (conflating knowledge, self, and operational spaces), not flat *context*. The mapping is plausible — memory and context both suffer from lack of separation — but the note equates two different claims (memory separation and context scoping) without acknowledging the domain shift. The three-space note is about persistent storage; this note is about within-session attention.

- [Completeness] The "lexically scoped" vs "dynamically scoped" partition for sub-agents (claim 12) lists user preferences, safety policies, global constraints, and project-level conventions as dynamically scoped. This omits a potentially important category: **emergent dynamic bindings** — things that enter the dynamic scope not by design but by accident, such as a user's emotional tone, implied urgency, or cultural context embedded in their messages. The partition implies dynamic scope is always "explicitly declared as special bindings," but in practice much of what persists across frames is implicit and uncontrolled. The note's own "spooky action at a distance" pathology applies here too — the scoped model doesn't fully solve it because some dynamic bindings are never explicitly declared.

PASS:
- [Internal consistency] The note's central analogy — flat context as dynamically scoped Lisp, sub-agents as lexical scoping — is maintained consistently throughout. The vocabulary (bindings, frames, stack, capture, hygiene) is used with stable definitions across all sections. No definition drift detected.
- [Internal consistency] The "What flat context buys" section acknowledges a genuine advantage of flat context (implicit communication), and this is consistent with the later design principle ("lexical scope by default, dynamic scope when explicitly requested"). The note does not strawman flat context.
- [Grounding alignment] The link to the codification note (claim 13) is accurate. The codification note defines codification as crossing a medium boundary from natural language to code, and this note's claim that frame boundaries enable progressive typing of return values aligns with codification's stated role as the constraining endpoint.
- [Grounding alignment] The link to "instructions are typed callables" (claim 16) accurately represents that note's content — skill type signatures do declare what bindings a sub-agent receives, which is the frame-interface pattern this note describes.
- [Grounding alignment] The Anthropic source attribution (line 95) — recommending sub-agents return 1,000-2,000 token summaries while internal reasoning stays out of the caller's window — is consistent with the lexically scoped frames pattern described. The note does not overclaim what the source says.
- [Internal consistency] The "Undeveloped directions" section is explicitly marked as speculative, which properly calibrates reader expectations for the ConvexBench interpretation and the tail-call/stack-unwinding analogies.

Overall: 3 warnings, 4 info
===
