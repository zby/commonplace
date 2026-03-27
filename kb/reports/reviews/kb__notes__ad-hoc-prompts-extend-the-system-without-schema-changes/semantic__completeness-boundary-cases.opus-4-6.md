The note contains two frameworks: the two-strata model (deterministic base + prompt layer) and the constraining spectrum (instructions → skills → hooks → scripts). A third, softer claim is that ad hoc prompts are better than formal types for certain requirements (the collection example). Each is tested below.

---

**Framework 1: Two-strata model**

Grounding definition: "Any system with an LLM agent layer has two strata: a deterministic base (files, schemas, scripts, APIs) and a prompt layer on top."

- Simplest: a single-agent system with a system prompt. Base = code; prompt layer = system prompt. ✓
- Most extreme: large multi-agent system where agents spawn sub-agents. Each agent has its own base/prompt pair; the two-strata model applies recursively. ✓
- Boundary — **configuration files (YAML/JSON with behavioral content)**: a YAML file that configures which tools an agent has is part of the deterministic base. A YAML file whose values are natural language instructions fed to the agent occupies an ambiguous position — it's structured (deterministic-base-like) but its content is semantic (prompt-layer-like). The note doesn't map configuration files to a stratum. INFO — this is a genuine boundary case for systems like CLAUDE.md, settings.json with hook instructions, or `.github/copilot-instructions.md` files.
- Boundary — **requirements needing new capabilities**: the note claims requirements can be absorbed "without changing the deterministic base," but this assumes the needed capability already exists. Adding a genuinely new tool (file retrieval, code execution) requires a base change, not just a prompt. The note's examples are all consistent with this constraint (the agent already has the tools), but the top-level framing ("Any system... absorb new requirements") implies broader coverage. INFO — the scope is slightly overstated; the mechanism works within existing capability surfaces, not across capability gaps.

**Framework 2: Constraining spectrum**

Grounding: cited to [methodology-enforcement-is-constraining.md] as foundation.

- Simplest: a plain markdown file with instructions. ✓
- Most extreme: a compiled validation script. ✓
- Between items — **structured prompts with format constraints**: a prompt that says "respond ONLY in JSON with fields {x, y, z}" is stiffer than a plain instruction but not yet a skill with a declared signature. This intermediate tier isn't named in the spectrum. INFO — the spectrum appears continuous but is presented as discrete tiers; boundary cases between tiers are real but don't break the model.
- Adjacent: **compiled binaries or compiled tools** — tighter than scripts, but outside the KB's scope. Not claimed.

**Claim: paragraph-as-collection is better than a formal type**

The note asserts the paragraph "is also *better* than a formal type because it carries context a schema couldn't." This is argued for one specific case (grouping documents for a goal) but presented as a general advantage. When does the formal type win? The note moves this to Open Questions rather than answering it in the body. The claim as stated doesn't define its own scope. INFO — the claim is supportable for the cited case but the boundary (when format wins over prose) is unresolved. This is acknowledged in the Open Questions section, so the note is self-aware, but the body makes a stronger claim than it defends.

---

No WARNs. Three INFOs: ambiguous classification of behavioral config files, overstated scope of "any requirement" absorption, and unresolved boundary for when formal types outperform prose.
