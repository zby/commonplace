The note presents a four-mechanism survey (system prompt files, capability descriptions, memory, configuration injection) and four design principles.

---

**Framework: Four always-loaded mechanisms**

Grounding: "This note catalogues the user-facing mechanisms — the surfaces that project authors and tool developers control."

- Simplest: a single CLAUDE.md file with one constraint. ✓
- Most extreme: a system with all four mechanisms fully populated across multiple platforms. ✓
- Between: **runtime-injected system context** (e.g., tool schemas, safety preambles). The note explicitly scopes these out: "Platform-injected context... is not configurable and falls outside the scope of this survey." ✓
- Adjacent: **project documentation** (README, docs) that isn't explicitly configured but could be auto-loaded. Not covered. INFO — some harnesses auto-load project docs alongside system prompts. The note's scope (user-configurable surfaces) excludes these, but the boundary between "configured" and "auto-discovered" project context is blurring.
- Adjacent: **volatile project state** ("code freeze", "migration in progress"). The note explicitly identifies this as a gap: "Volatile project state is a gap... it's the content most likely to go stale." ✓ — honest gap acknowledgment.

**Five content types in system prompt files**

Constraints, routing rules, definitions, domain scope, operational recipes. The note acknowledges tension between practitioner practice (embedding recipes) and theoretical recommendation (routing to on-demand docs). ✓

**Design principles**

Four principles (shared budget, cadence matching, ambient/on-demand distinction, volatile state gap). All are internally consistent and grounded in the survey. ✓

No WARN. One INFO on auto-discovered project context as a boundary of the "user-facing" scope.
