The note presents one main framework: a three-part decomposition of agent runtimes into scheduler, context engine, and execution substrate, with a practitioner mapping table.

---

**Framework: Three-part runtime decomposition**

Grounding definition: "The claim is that the functions are analytically distinct, and the distinction clarifies why practitioner taxonomies keep converging on similar component lists."

- Simplest instance: a raw LLM chat with no explicit runtime. The note addresses this: "Without an external substrate, both [scheduler and context engine] collapse back into flat conversation state." All three functions still exist conceptually but are collapsed into the conversation. ✓
- Most extreme: a fully modular agent platform with separate scheduling service, context management layer, and file/tool infrastructure. Each component maps cleanly. ✓
- Between: memory/search, which the practitioner mapping table assigns to "Context engine + execution substrate." This dual mapping is honest — retrieval logic is context engineering while stored artifacts are substrate. INFO — the dual mapping is acknowledged but not problematized. A designer deciding where to put a retrieval system would need further guidance on where the boundary falls.
- Adjacent concept: **evaluation infrastructure** — explicitly acknowledged in scope limits: "Evaluation infrastructure, policy layers, and social workflows may deserve their own treatment." ✓
- Adjacent concept: **safety/alignment layers** — sandboxes are placed under execution substrate. But safety policies that affect what the model can do (not just where it executes) could involve all three components: the scheduler decides whether to proceed, the context engine frames the safety constraint, the substrate enforces the sandbox. INFO — safety layers cross-cut the decomposition; the note places sandboxes in substrate but safety-as-policy may span components.

**Practitioner mapping table**

The six-row mapping (long-horizon execution, context management, memory/search, filesystem, bash, sandbox → scheduler/context engine/substrate) is comprehensive for the source it maps. No practitioner component is left unmapped. ✓

No WARN. Two INFOs: dual-mapped memory/search boundary, and safety layers cross-cutting the decomposition.
