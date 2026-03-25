---
description: Skills add structured discovery, user-facing invocation, and declarative execution policy (tool permissions, model override, context isolation) beyond the shared procedure
type: note
traits: []
tags: []
status: seedling
---

# Skills are instructions plus routing and execution policy

Instructions and skills share the same medium (distilled procedures in markdown), the same derivation process ([distillation from methodology](./skills-derive-from-methodology-through-distillation.md)), and the same writing constraints (imperative, step-sequenced, behaviourally complete). The procedure is interchangeable — you can promote an instruction to a skill or demote a skill to an instruction without rewriting the body. What differs is the harness integration surface: what the runtime does with the file beyond reading it. Not every skill uses all three affordances — a minimal skill may only use discovery and invocation — but the skill format makes them available.

## Three things skills add

### 1. Structured discovery

Both skills and instructions need an always-loaded description so the agent knows they exist. But they use different discovery surfaces:

- **Skills** appear in the harness's capability listing (system-reminder messages in Claude Code, `<available_skills>` in Codex) with name, description, and trigger conditions in a consistent format. The agent matches user intent against this structured menu.
- **Instructions** appear as routing rules in the system prompt file (CLAUDE.md, AGENTS.md) — free-form conditional pointers like "when doing X, read Y.md."

The skill surface is more structured; the instruction surface is more flexible. Both are always-loaded, both cost roughly the same tokens (~1-2 lines per entry). The [loading hierarchy](./instruction-specificity-should-match-loading-frequency.md) treats them equivalently — lightweight metadata always present, full body loaded on demand.

### 2. User-facing invocation

Skills with `user-invocable: true` can be triggered by a human typing `/skill-name`. This is the most reliable activation pathway — effectively 100%, because it's a direct command rather than a suggestion the agent may or may not follow. Instructions have no equivalent; the human must say "follow the procedure in X" or rely on a CLAUDE.md routing rule firing autonomously.

This matters because autonomous activation is unreliable for both pathways. [Practitioner measurement](https://scottspence.com/posts/how-to-make-claude-code-skills-activate-reliably) found that a CLAUDE.md meta-routing instruction ("if the prompt matches skill keywords, use Skill(X)") activated at roughly 20%; other routing rule types may differ, but the general pattern of low autonomous compliance is consistent with broader findings (Jaroslawicz et al., 2025). Explicit `/command` invocation sidesteps this problem entirely.

### 3. Declarative execution policy

Skill frontmatter carries fields that modify the agent's execution environment at invocation time. In Claude Code ([frontmatter reference](https://code.claude.com/docs/en/skills#frontmatter-reference)):

- **`allowed-tools`** — pre-approves specific tools without per-use permission prompts. An instruction loaded via Read inherits the session's existing permissions.
- **`model`** — overrides the session model (e.g., force Opus for a complex workflow, Sonnet for a fast one).
- **`context: fork`** — runs the skill in an isolated subagent with its own conversation history.
- **`$ARGUMENTS`** — substituted into the skill body by the harness before injection, providing a built-in parameterization mechanism. Also supports positional access (`$ARGUMENTS[0]`, `$1`) and skill-directory reference (`${CLAUDE_SKILL_DIR}`).

Instructions have none of these. They are passive content — the agent reads them and follows them, but the runtime doesn't modify its own execution environment in response.

[Shilkov's reverse-engineering analysis](https://mikhail.io/2025/10/claude-code-skills/) confirms the injection mechanism: skills achieve "on-demand prompt expansion without modifying the core system prompt," injecting content as a hidden message with pre-approved tool permissions. [Lee's deep dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/) documents the dual-message pattern and the `contextModifier` function that changes tool permissions and model selection at invocation time.

## What instructions and skills share

The procedure itself is identical regardless of packaging:

- **Writing constraints** — imperative voice, step-sequenced, behaviourally complete, minimal reasoning, explicit scope boundaries, frontloaded for zero-context agents
- **Distillation process** — manual operation → notice stable core → extract and parameterize
- **Directory signal** — both live in `kb/instructions/`; promotion to a skill adds a subdirectory, SKILL.md frontmatter, and a symlink into `.claude/skills/`
- **Quality standard** — same execution-optimization requirements whether or not the procedure has routing

Instructions are not notes. Notes are for reasoning — an agent building understanding. Instructions are for execution — an agent that needs to act. They get their own directory (`kb/instructions/`) because the directory tells the agent what kind of reading the document demands. [Ad hoc instruction notes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) are a further distinction: one-off, written for a specific situation, not expected to be reused. Instructions in `kb/instructions/` are reusable procedures distilled from repeated operations. [Methodology notes](./agent-statelessness-makes-routing-architectural-not-learned.md) sit on the other side — they carry the reasoning instructions are distilled from.

## Cross-platform convergence and divergence

The discovery architecture converges across platforms: always-loaded metadata for capability listing, full body loaded on demand, always-on system prompt files for universal conventions. Claude Code discovers skills from `.claude/skills/`; Codex from `.agents/skills/` ([Codex skills docs](https://developers.openai.com/codex/skills)); Cursor from `.cursor/skills/` ([Cursor docs](https://cursor.com/docs/context/skills)); GitHub Copilot distinguishes instructions, prompts, agents, and skills ([GitHub Copilot docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills)). The [Agent Skills specification](https://agentskills.io/specification) formalizes the shared core (name + description + body).

The execution policy architecture diverges. Claude Code bundles all policy into SKILL.md frontmatter. Other platforms separate the "what to know" artifact (skill) from the "how to execute" artifact:

- **Codex** supports `$ARGUMENTS` ([slash commands](https://developers.openai.com/codex/cli/slash-commands)) with richer named-placeholder syntax (`$FILE`, `$TICKET_ID`), but has no per-skill tool or model control — those live at the config level.
- **Cursor** puts execution policy on [subagents](https://cursor.com/docs/context/subagents) (a separate concept from skills), which support `model` and `readonly` but not `allowed-tools`.
- **GitHub Copilot** puts `tools` and `model` on [custom agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents) (.agent.md), not on skills (SKILL.md).

The Agent Skills specification standardizes `name`, `description`, and `allowed-tools` (experimental), but `model`, `context`, and `$ARGUMENTS` are not part of the standard. Argument substitution is the most portable of the execution policy features (Claude Code, Codex, partially Cursor, absent in Copilot); the rest requires platform-specific configuration.

Summarizing portability:

1. **Structured discovery** — converged (all platforms scan skill directories for name + description)
2. **User-facing invocation** — converged (slash commands or `$` prefix across platforms)
3. **Declarative execution policy** — diverged (Claude Code-specific bundling; other platforms use separate abstractions)

## Practical implications

**If you want to stay portable across harnesses, the universal features of skills (discovery and invocation) are already achievable with an instruction file plus a routing entry in CLAUDE.md or AGENTS.md.** The execution policy features that genuinely differentiate skills are Claude Code-specific. This means the original claim that "instructions are skills without automatic routing" is roughly correct for the portable subset. The execution policy layer is a platform-specific bonus, not a universal architectural distinction. A procedure that needs execution policy is necessarily coupled to a specific harness.

**Promote an instruction to a skill when:**

- The procedure needs **execution policy** — pre-approved tools, model override, or forked context.
- Users should **invoke it directly** — recurring workflows benefit from `/command`, the most reliable activation pathway.
- The procedure **takes arguments** — `$ARGUMENTS` substitution is cleaner than relying on conversational inference.
- The body is **large** — a 400-line procedure benefits from progressive disclosure (metadata always loaded, body only on demand), though CLAUDE.md + Read achieves similar on-demand loading.

**Keep as an instruction when:**

- The procedure is **simple** — a few steps, no special tool permissions or model override needed.
- **Platform independence matters** — instructions work with any agent that can read a file.
- The procedure is **still developing** — instructions are lower-ceremony (no subdirectory, no symlink, no SKILL.md frontmatter). Promote when stable.
- **Occasional use** — invoked by a human saying "follow the procedure in X", not needed as autonomous or slash-invoked capability.

---

Relevant Notes:

- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — foundation: the distillation process that produces both skills and instructions
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — grounds: the loading hierarchy both participate in
- [always-loaded context mechanisms in agent harnesses](./always-loaded-context-mechanisms-in-agent-harnesses.md) — context: the discovery surfaces through which both are found
- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — context: instructions sit on the constraining gradient between ad-hoc notes and skills
- [ad hoc prompts extend the system without schema changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — distinguishes: ad hoc notes are one-off; instructions are reusable distilled procedures
- [agent statelessness makes routing architectural](./agent-statelessness-makes-routing-architectural-not-learned.md) — motivates: the source/compiled split applies to instructions the same way it applies to skills
- [instructions are typed callables](./instructions-are-typed-callables.md) — extends: instructions, like skills, have implicit type signatures
