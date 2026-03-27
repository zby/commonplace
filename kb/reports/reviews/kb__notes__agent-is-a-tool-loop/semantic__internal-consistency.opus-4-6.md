Key claims extracted (note is very short):

1. "Agent" carries too much philosophical weight to define cleanly.
2. As a technical convention: agent = tool loop (prompt + capability surface + stop condition).
3. The convention says nothing about autonomy, planning, or goals.
4. Sub-agent = child loop with its own prompt and capability surface.
5. Multi-agent system = tree of loops coordinated by code.
6. Two loops with different tool surfaces but the same model = different agents.
7. Same prompt run twice = two invocations (not one agent instantiated twice, but two distinct execution events).
8. Convention tracks code structure, not character.

---

**Pairwise consistency checks**

*(2) agent = tool loop (prompt + capability surface + stop condition) vs. (4) sub-agent = child loop with its own prompt and capability surface*

The sub-agent definition omits stop condition. Since a sub-agent IS a tool loop (claim 2), it implicitly has a stop condition. The omission is editorial (brevity) rather than contradictory. ✓

*(6) two loops with different tool surfaces but same model = different agents vs. (8) convention tracks code structure*

Consistent — identity is determined by configuration (prompt × capability surface), not by model identity or invocation count. This is a code-structural distinction. ✓

*(7) same prompt run twice = two invocations vs. (6) different tool surfaces = different agents*

The combination implies: agent identity = (prompt, capability surface), not (number of executions). An agent with the same prompt and surface, run multiple times, is one agent yielding multiple invocations. This is consistent across claims 6 and 7. ✓

*(1) "too much philosophical weight to define cleanly" vs. (2) "as a technical convention... an agent is a tool loop"*

Not contradictory. The note explicitly limits the equivalence to a technical convention. It doesn't claim to resolve the philosophical debate; it sidesteps it. ✓

*(3) "nothing about autonomy, planning, or goals" vs. the inference in the body: "the question of whether frameworks should expose the loop becomes the question of whether they support sub-agents as a first-class operation"*

The inference is about framework design, not about agent character. Consistent — the convention is minimal about what an agent *is* (deliberate) and derives code-structure implications from that minimal definition. ✓

**Definition drift**

"Tool loop" — used consistently as the equivalence class for agents. ✓
"Capability surface" — introduced as a component of the convention, used consistently in claims 2, 4, 6. ✓
"Convention" vs. "definition" — the note maintains the distinction throughout. ✓

**Summary/body mismatch**

The note has no explicit compressed summary. The body is compact and functions as its own summary. No mismatch possible. ✓

---

PASS — no WARNs, no INFOs. The note is internally clean. Its brevity and explicit scope-limiting ("a technical convention, not a definition") prevent most consistency failure modes from arising.
