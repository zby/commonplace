The note's framework is a single definitional equivalence: agent = tool loop (prompt + capability surface + stop condition). It explicitly disclaims being a definition in the strong sense — it's a "technical convention for organizing code." This framing pre-empts most coverage complaints, but the convention still makes implicit coverage claims (the unit it carves out should cleanly map to recognizable agent implementations). I test whether it does.

---

**Testing the tool-loop convention**

Grounding: "a prompt, a capability surface, and a stop condition, running until the model finishes or the runtime cuts it off."

**Simplest instance: a single LLM call with no tool use**

The loop runs, the model produces output without invoking any tool, and the loop terminates (stop condition: model finishes). This is a tool loop that ran zero tool-call iterations. The convention accommodates it — "running until the model finishes" covers single-turn completions. INFO — this is the degenerate case of the framework. The name "tool loop" implies at least one tool call, but the definition doesn't require it. The convention is slightly broader than its name suggests.

**Most extreme: massively parallel multi-agent tree**

Covered explicitly: "a multi-agent system is a tree of loops coordinated by code." ✓

**Adjacent: reactive / event-driven agents**

An agent that runs indefinitely in response to events (webhook handler, monitor) has a stop condition of "never" — it terminates only when the runtime kills it. The note covers this: "running until the model finishes *or the runtime cuts it off*." "Runtime cuts it off" subsumes external termination. ✓

**Adjacent: human-in-the-loop agents**

A loop that pauses mid-run to await human input before continuing. The pause breaks the running loop — is it one agent invocation with a pause, or two separate invocations? The note defines stop condition as "model finishes or runtime cuts it off," but a human-pause is neither. INFO — the convention doesn't address whether a human interrupt suspends the loop (same agent, resumed) or terminates it (new invocation begins). This matters for code structure, which is exactly what the convention claims to track.

**Adjacent: agents without tool-call loops (pure chain-of-thought or structured output)**

A model that produces structured outputs via constrained decoding (JSON mode, guided generation) without invoking tool-use APIs. It has a prompt and a stop condition, but its "capability surface" is the output format constraint rather than a set of callable tools. Does it fit the convention? Probably yes — the capability surface can be interpreted broadly — but INFO — the convention's component names ("tool loop," "capability surface") are implicitly tool-call-centric, and non-tool agents are not addressed.

**What counts as granularity of "capability surface"?**

If an agent has read and write access to a file system plus a search tool plus a web fetcher, is that one capability surface or four? The note doesn't define the granularity of capability surface. This matters for the claim that "two loops with different tool surfaces but the same model are different agents" — what counts as "different"? INFO — the convention is underspecified at this level, but the note is explicit that it's a convention for code organization, where granularity is determined by the implementer.

---

No WARNs. Three INFOs: degenerate zero-tool-call case slightly misnamed by "tool loop," human-in-the-loop ambiguity for stop condition, and underspecified capability surface granularity. These are edge cases the convention doesn't address but also doesn't claim to — consistent with its stated minimal scope.
