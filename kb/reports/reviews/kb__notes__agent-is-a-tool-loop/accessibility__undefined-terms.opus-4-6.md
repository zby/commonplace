warning

One term is used without inline definition.

---

**"capability surface"** (line 11, first use): "an agent is a tool loop — a prompt, a capability surface, and a stop condition."

"Capability surface" is presented as one of three named components of a tool loop, but it is never defined. What is a capability surface? In context it means the set of tools the agent can call. Without that definition, the term is opaque — "surface" is not a standard word in this sense and the reader has no way to infer the meaning from context.

The same concept appears again at line 13 as "tool surfaces" ("Two loops with different **tool surfaces** but the same model are different agents"), but neither instance is glossed. Using two different terms ("capability surface" at line 11, "tool surfaces" at line 13) for the same concept without defining either compounds the ambiguity.

Recommended fix: define inline on first use, e.g., "a capability surface (the set of tools the agent can call)." Consider also aligning the two terms — either use "capability surface" consistently or explain that they refer to the same thing.

---

All other terms in the note are either defined inline or are standard:

- "tool loop" — defined inline: "a prompt, a capability surface, and a stop condition, running until the model finishes or the runtime cuts it off."
- "stop condition" — sufficiently glossed by the surrounding clause: "running until the model finishes or the runtime cuts it off."
- "sub-agent" — defined inline: "A sub-agent is a child loop with its own prompt and capability surface."
- "multi-agent system" — defined inline: "a tree of loops coordinated by code."
