<!-- REVIEW-METADATA
note-path: kb/notes/skills-are-instructions-plus-routing-and-execution-policy.md
last-full-review-note-sha: dd0b3d745c7d2dad04999f84cc9d7875223db0af
last-full-review-note-commit:
last-full-review-at: 2026-03-25T21:02:27+01:00
last-accepted-note-sha: dd0b3d745c7d2dad04999f84cc9d7875223db0af
last-accepted-note-commit:
last-accepted-at: 2026-03-25T21:02:27+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->

=== SEMANTIC REVIEW: skills-are-instructions-plus-routing-and-execution-policy.md ===

Claims identified: 14

WARN:
- [Completeness] The "three things skills add" enumeration is presented as exhaustive, but the title bakes in all three as definitional ("skills ARE instructions plus routing and execution policy"). A skill that uses only `name` and `description` in frontmatter — no allowed-tools, no model, no context:fork — gets discovery and invocation but no execution policy. Such a skill is instructions plus routing, not instructions plus routing and execution policy. The title overclaims for minimal skills. The body's own portability conclusion ("the universal features of skills are already achievable with an instruction file plus a routing entry") implicitly acknowledges this — universal skills have no policy, yet they're still skills.
- [Grounding] The ~20% activation rate is attributed to "passive CLAUDE.md instructions" generally, but the Scott Spence measurement was specifically about a CLAUDE.md instruction telling the agent to invoke a skill ("if the prompt matches skill keywords, use Skill(skill-name)"). That's a narrow instruction type (meta-routing: "use the Skill tool when..."), not CLAUDE.md routing rules in general. A routing rule like "when writing notes, read WRITING.md" may have different compliance characteristics. The note generalizes from the measured case to all passive instructions without flagging the scope expansion.
- [Internal consistency] The note claims "only argument substitution is genuinely cross-platform" (§3, final paragraph), but the cross-platform section documents that Cursor has bugs dropping arguments and GitHub Copilot doesn't support `$ARGUMENTS` at all. That's support on 2 of 4 platforms (Claude Code, Codex) with partial/broken support on a third (Cursor). "Genuinely cross-platform" overstates the portability — "most portable of the execution policy features" would be more accurate.

INFO:
- [Completeness] The note doesn't discuss skill *composition* — can one skill invoke another? In this repo, skills do invoke other skills (e.g., `/ingest` can call `/connect`). Instructions loaded via Read have no equivalent composition mechanism — the agent must decide to read a second instruction on its own. If skill composition is harness-supported (via the `Skill` entry in `allowed-tools`), that's a fourth affordance skills add. Worth investigating whether this is a real mechanical difference or just an agent behavior pattern.
- [Grounding] The Agent Skills specification at agentskills.io is cited for what it standardizes (name, description, allowed-tools experimental) and what it excludes (model, context, $ARGUMENTS). This is an external URL that could not be independently verified during review. The claim is plausible given the cross-platform research, but the spec should be checked directly if this note is promoted beyond seedling.

PASS:
- [Grounding] The link to [skills derive from methodology through distillation] accurately reflects the source. That note defines distillation as "extracting operational procedures from discursive reasoning in the same medium," which is exactly the shared derivation process claimed here.
- [Grounding] The link to [instruction specificity should match loading frequency] is accurately described. That note's loading hierarchy (CLAUDE.md → skill descriptions → skill bodies → task docs) grounds the progressive disclosure claim made here.
- [Grounding] The link to [methodology enforcement is constraining] is faithfully characterized. That note's gradient (ad hoc prompt → instruction → skill → hook → script) places instructions below skills on the enforcement spectrum, consistent with this note's framing.
- [Grounding] The link to [agent statelessness makes routing architectural] accurately reflects the source's "Source vs. compiled" section, which describes methodology as source and skills/routing as compiled artifacts.
- [Internal consistency] The note's main structural tension — execution policy is the strongest differentiator but also platform-specific — is explicitly acknowledged rather than hidden. The portability conclusion ("a platform-specific bonus, not a universal architectural distinction") is consistent with the cross-platform evidence presented.
- [Completeness] The cross-platform convergence/divergence section cleanly separates what converges (discovery, invocation) from what diverges (execution policy), with per-platform evidence for each claim. The three-line summary (lines 88-90) accurately reflects the detailed analysis.
- [Internal consistency] The "What stays the same" section is consistent with the linked sources — writing constraints, distillation process, directory signal, and quality standard all align with claims made in the grounding notes.

Overall: 3 warnings, 2 info
===
