The note presents a placement model (loading frequency × failure cost), three AGENTS.md layers (invariants, routing, escalation), exclusion rules, a nested topology, a lifecycle path, and six quality tests.

---

**Framework 1: Placement model (loading frequency × failure cost)**

Grounding: "Two variables determine placement."

- Simplest: a single high-frequency, high-cost invariant ("never force-push"). ✓
- Most extreme: a complex system with hundreds of instructions sorted into the three placement bins. ✓
- Between: an instruction needed in most sessions but not all (e.g., 80% frequency). The binary "always loaded" vs. "task-specific" doesn't clearly place this. INFO — the boundary between "every session" and "specific operation" is fuzzy. Instructions needed frequently but not universally lack a clear home.
- Adjacent: an instruction with high failure cost but low loading frequency (a rare but dangerous operation). The placement rule maps this to "task-specific + medium failure cost" but the high failure cost suggests it might warrant always-loaded status as a safety invariant. INFO — the model uses a 2×2 matrix but only three cells are named; high-failure-cost + task-specific gets medium treatment, which may under-weight the danger.

**Framework 2: Three layers**

- Layer 1 (Invariants): clear boundary — "must hold in every session and every task." ✓
- Layer 2 (Routing): "help the agent choose the next file, not execute full procedures." Clean scope. ✓
- Layer 3 (Escalation): three concrete examples make this testable. ✓
- Between: an instruction that is both a routing pointer and an escalation trigger (e.g., "if you're modifying X, load Y; if Y doesn't exist, escalate"). The layers handle this as a combination. ✓

**Framework 3: Exclusion rules**

Six exclusion categories. Each is defensible and maps to alternative placement. ✓

**Framework 4: Quality tests**

Six questions, each testing a different dimension of appropriateness. Clean and testable. ✓

No WARN. Two INFOs on boundary fuzziness in the placement model.
