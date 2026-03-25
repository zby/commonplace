# Findings: Skills vs Instructions

## 1. Verified mechanical differences in the loading mechanism

### 1.1 Execution context modification (skills only)

Skills carry frontmatter fields that modify the agent's execution environment at invocation time:

- **`allowed-tools`** — pre-approves specific tools without per-use permission prompts. An instruction loaded via Read inherits the session's existing permissions and cannot expand them.
- **`model`** — overrides the session model (e.g., force Opus for a complex skill, Sonnet for a fast one). Instructions run on whatever model the session is using.
- **`context: fork`** — runs the skill in an isolated subagent with its own conversation history. Instructions have no equivalent; isolation requires manually launching an Agent.

This is the strongest mechanical difference. It means skills are not just routed procedures — they are procedures with declarative execution policy.

### 1.2 Content injection pathway

- **Skill**: The harness injects two messages — a visible metadata message (`<command-message>` tag) and a hidden instruction message (`isMeta: true`) containing the full SKILL.md body. The content enters the context as a user message, invisible in the UI but visible to the model's API call.
- **Instruction via Read**: The content enters the context as a tool result, visible to both the model and the user.

Whether this framing difference affects compliance is undocumented. Both end up in the context window. The practical difference is that skill content is hidden from the UI, which matters for user experience but not obviously for agent behavior.

### 1.3 Argument substitution

Skills support `$ARGUMENTS` (and other variables like `${CLAUDE_SESSION_ID}`), resolved by the harness before injection. Shell command injections (`` !`command` ``) execute during expansion and their output replaces the placeholder.

Instructions have no built-in argument mechanism. The agent must infer parameters from the surrounding conversation context, or the human must specify them in the invocation.

### 1.4 User-facing invocability

Skills with `user-invocable: true` can be triggered by the user typing `/skill-name`. This is a direct, unambiguous activation signal — the most reliable invocation pathway measured (see §2).

Instructions cannot be slash-invoked. The user must ask the agent to follow a specific file, or the CLAUDE.md routing rule must fire.

### 1.5 Discovery surface

Both surfaces carry name + description + condition, both are always-loaded:

- **Skills**: Listed in `system-reminder` messages as available skills. The Skill tool's schema includes an `<available_skills>` listing. Descriptions and trigger conditions are explicitly formatted for the agent to match against user intent.
- **CLAUDE.md routing entries**: Appear as conditional rules in the system prompt file (routing table rows, escalation boundaries, inline pointers).

The skill surface is more structured — each entry follows the same format with explicit trigger conditions. CLAUDE.md entries are free-form, which gives more flexibility but less consistency.

### 1.6 Token cost

Roughly equivalent per entry. Skill descriptions in system-reminder are ~1-2 lines; CLAUDE.md routing table entries are ~1-2 lines. The Skill tool schema definition is a fixed cost (~200-300 tokens for the tool description regardless of how many skills exist). Not a meaningful differentiator.

### 1.7 Promotion pathway

Skills are the terminus of a clear promotion path: manual operation → instruction → skill. Demotion is also clean: remove the symlink and routing entry, keep the procedure file. This is correctly described in the existing KB note.

## 2. Activation reliability

Neither mechanism is highly reliable for autonomous activation. Practitioner evidence (Scott Spence, 2025-2026):

| Mechanism | Measured activation rate |
|---|---|
| Explicit `/skill-name` invocation | ~100% (user-driven) |
| LLM pre-evaluation hook (forced skill reasoning) | ~84% |
| Passive CLAUDE.md instruction ("if X, use Skill(Y)") | ~20% |
| Skill auto-activation (no hooks, no routing rule) | unreliable, no firm number |
| Multi-skill prompts with passive instructions | ~0% |

CLAUDE.md instruction compliance degrades linearly with volume (Jaroslawicz et al., 2025: "even the best models follow fewer than 30% of instructions perfectly in agent scenarios"). Multiple practitioners report that "prompt-level instructions are suggestions" and only code hooks provide reliable enforcement.

**Key finding**: The most reliable activation is explicit user invocation — which is a skill-only affordance. For autonomous activation, both pathways are unreliable without enforcement hooks. The skill description surface may be slightly better structured for auto-activation than free-form CLAUDE.md entries, but neither is dependable.

## 3. Assessment of the KB claim

The note [Skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) (formerly "Instructions are skills without automatic routing") claims: "Skills have two aspects: the procedure itself and the routing machinery... The difference is a judgment call about whether the procedure is common enough to warrant automatic routing."

**This is correct as a first approximation but understates the difference.** The routing/discovery distinction is the primary one, and the core insight — that the procedure is the same medium and the same distillation process — is sound. But "automatic routing" covers only differences §1.4 and §1.5 above. It does not account for:

- **Execution context modification** (§1.1) — skills carry declarative execution policy (tool permissions, model override, context isolation) that instructions cannot express
- **Argument substitution** (§1.3) — skills have a built-in parameterization mechanism
- **User-facing slash invocation** (§1.4) — skills offer the most reliable activation pathway

The note's framing of the promotion path (instruction → skill by "adding the trigger machinery") is accurate but incomplete. Promotion adds not just triggers but execution policy. Demoting a skill to an instruction loses not just discoverability but also tool pre-approval, model control, and argument handling.

**Suggested revision**: "Instructions are skills without routing or execution policy" would be more precise. Or: the current title holds if "routing" is understood broadly to include the full harness integration surface (discovery, invocation, execution context), not just the activation trigger.

## 4. When to create a skill vs. a CLAUDE.md routing entry

### Create a skill when:

- **The procedure needs execution policy** — pre-approved tools, model override, or forked context. This is the clearest signal. If you need `allowed-tools` or `context: fork`, you need a skill.
- **Users should invoke it directly** — recurring workflows that benefit from `/command` invocation (the most reliable activation pathway).
- **The procedure takes arguments** — `$ARGUMENTS` substitution is cleaner than relying on conversational inference.
- **The body is large** — skills keep only metadata in always-loaded context; the full body loads on demand. A 400-line procedure makes more sense as a skill than as an instruction file pointed to by a 2-line CLAUDE.md entry (though the CLAUDE.md + Read pathway also achieves on-demand loading).

### Keep as a CLAUDE.md routing entry when:

- **The procedure is simple** — a few steps that don't need special tools or model override.
- **Platform independence matters** — instructions work with any agent that can read a file. Skills are coupled to harness-specific discovery mechanisms (`.claude/skills/`, `.agents/skills/`).
- **The procedure is developing** — instructions are lower-ceremony; they don't need a subdirectory, symlink, or SKILL.md frontmatter. Use them during iteration and promote when stable.
- **Occasional use** — invoked by a human saying "follow the procedure in X", not needed as autonomous or slash-invoked capability.

### The middle ground

The evidence suggests a third pattern worth acknowledging: **CLAUDE.md routing rule + Skill tool invocation**. Several skills in this repo are pointed to by both a CLAUDE.md routing entry and a skill description. This is belt-and-suspenders — the routing rule fires if the agent follows CLAUDE.md, the skill description fires if the agent matches intent against available skills, and the user can invoke `/skill-name` directly. Given the low reliability of any single autonomous activation mechanism, redundant discovery surfaces may be pragmatically justified for critical workflows.

## Cross-platform convergence

The always-loaded-instructions + on-demand-skills architecture appears across all major agent platforms (Claude Code, Codex, Cursor, GitHub Copilot). This is convergent design, not a Claude-specific quirk. The fundamental pattern: lightweight metadata for discovery + full content loaded on demand + always-on rules for universal conventions. The commonplace KB's existing notes ([always-loaded context mechanisms](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md), [instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md)) correctly describe this architecture.

## Sources

- [Extend Claude with skills — Claude Code Docs](https://code.claude.com/docs/en/skills)
- [How Claude remembers your project — Claude Code Docs](https://code.claude.com/docs/en/memory)
- [Inside Claude Code Skills — Mikhail Shilkov](https://mikhail.io/2025/10/claude-code-skills/)
- [Claude Agent Skills: A First Principles Deep Dive — Lee Han Chung](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/)
- [How to Make Claude Code Skills Activate Reliably — Scott Spence](https://scottspence.com/posts/how-to-make-claude-code-skills-activate-reliably)
- [Custom instructions with AGENTS.md — Codex](https://developers.openai.com/codex/guides/agents-md)
- [Agent Skills — Codex](https://developers.openai.com/codex/skills)
- [Skill authoring best practices — Claude API Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Claude Code CLAUDE.md vs Skills — UX Planet](https://uxplanet.org/claude-code-claude-md-vs-skills-35685676b367)
- [I Wrote 200 Lines of Rules for Claude Code. It Ignored Them All. — DEV Community](https://dev.to/minatoplanb/i-wrote-200-lines-of-rules-for-claude-code-it-ignored-them-all-4639)
- [Skills vs. Commands vs. Rules — Cursor Forum](https://forum.cursor.com/t/skills-vs-commands-vs-rules/148875)
- [GitHub Copilot: Instructions vs Prompts vs Custom Agents vs Skills — DEV Community](https://dev.to/pwd9000/github-copilot-instructions-vs-prompts-vs-custom-agents-vs-skills-vs-x-vs-why-339l)
