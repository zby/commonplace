The note presents a five-phase architecture (seed search, snapshot & inter-connect, synthesize & redirect, bridge to KB, report), three abstraction depths, and an MVP design.

---

**Framework: Five-phase architecture**

- Simplest: the MVP (single-pass search, snapshot, connect, bridge, report). ✓
- Most extreme: iterative multi-round search with synthesis and redirect loops. ✓
- Between: a single iteration of the full pipeline (including Phase 3 synthesis). The note handles this as the intermediate step before iteration. ✓

**Three abstraction depths** (shared feature, shared structure, generative model) are borrowed from the discovery note. Clean application. ✓

**Architectural tensions** — depth vs. cost, workshop lifecycle, stopping criterion. All honestly identified with specific proposals. ✓

**Stopping criteria** map to oracle types on the oracle-strength spectrum — nice application of existing KB theory to a practical design. ✓

No WARN, no INFO. Well-structured brainstorm with honest tensions.
