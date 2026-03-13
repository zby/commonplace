---
description: Instructions, skills, hooks, and scripts form a constraining gradient for methodology — from underspecified and indeterministic (LLM interprets and may not follow) to fully deterministic (code always runs), with hooks occupying a middle ground of deterministic triggers with indeterministic responses
type: note
traits: []
tags: [kb-design, learning-theory]
status: seedling
---

# Methodology enforcement is constraining

The ways we enforce methodology in the KB — instructions, skills, hooks, scripts — map directly onto the [constraining spectrum](./agentic-systems-interpret-underspecified-instructions.md). The enforcement layers parallel the [codification verifiability gradient](../notes/deploy-time-learning-the-missing-middle.md) — where codification moves code from prompt tweaks through schemas to deterministic modules, methodology enforcement moves practices from written guidance through structured skills to automated scripts. Each layer trades flexibility for reliability by reducing two things: **semantic underspecification** (committing to one interpretation of what the practice means) and **execution indeterminism** (ensuring the practice fires consistently across runs). Moving from instructions to scripts progressively eliminates both.

| Layer | Trigger | Response | Reliability | Example |
|-------|---------|----------|-------------|---------|
| Instruction | indeterministic (LLM remembers) | underspecified + indeterministic (LLM interprets) | lowest | "check descriptions" in CLAUDE.md |
| Skill | deterministic (user invokes) | underspecified + indeterministic (LLM executes) | medium | `/validate` checks note quality |
| Hook (warn) | deterministic (event fires) | underspecified + indeterministic (LLM acts on output) | medium-high | validate-note.sh outputs WARN on missing description |
| Hook (block) | deterministic (event fires) | deterministic (rejected) | high | exit 1 prevents the operation |
| Script | deterministic (user/hook runs) | deterministic (code runs) | highest | sync_topic_links.py rewrites Topics footer |

Instructions have the lowest reliability because both phenomena compound: the LLM may not remember to apply the practice (indeterminism in triggering), and when it does, it interprets the instruction through underspecified semantics ("check descriptions" admits multiple valid readings of what counts as a good description). Skills eliminate the trigger problem — the user invokes them deterministically — but the response is still an LLM interpreting an underspecified spec. Blocking hooks and scripts eliminate both phenomena entirely.

The key insight: hooks are not cleanly "deterministic." A hook that outputs a warning is a deterministic trigger with an underspecified, indeterministic response — the LLM decides what to do with the warning. Only blocking hooks (exit non-zero) are fully deterministic. This means the three-tier model (instruction → skill → hook) that arscontexta uses oversimplifies — the real picture is a gradient, which is just constraining.

## Maturation trajectory

This is [progressive compilation applied to methodology](../notes/programming-practices-apply-to-prompting.md) — new best practices should start as underspecified natural-language guidance and constrain toward precise, deterministic enforcement as they prove out:

1. **Instruction** — write it in CLAUDE.md or WRITING.md. Cheap to revise, tests whether the practice is worth encoding. If the LLM follows it inconsistently, that's signal.
2. **Skill** — encode it as a structured prompt. Reliable when invoked, but requires explicit invocation. Good for judgment-requiring operations that shouldn't be automated.
3. **Hook/script** — automate the deterministic parts. Only after the practice has constrained enough that you know exactly what the check should do.

**When to move down.** The strongest signal for automation is when the agent consistently proposes the same correct next step — meaning both that the LLM has converged on a single interpretation of the underspecified spec, and that it executes it reliably across runs. If the LLM's response is predictable and always right, the prompt-to-action path is just overhead; a hook or script would do the same thing without the latency or token cost. This is the codification trigger: a pattern has emerged from repeated execution, and constraining it commits to that interpretation in precise code — resolving the semantic underspecification by design rather than by luck, and eliminating the indeterminism entirely.

Not everything should complete the trajectory. Operations requiring semantic judgment (like "is this connection genuine?") belong permanently at the skill level — their [oracle strength](../notes/oracle-strength-spectrum.md) is too low to support deterministic verification. Attempting to automate judgment produces confident systematic errors — the over-automation risk. [ADR-001](./001-generate-topic-links-from-frontmatter.md) is a clean example of the trajectory completing: an LLM-generated Topics footer was recognised as fully mechanical, and the operation moved to a deterministic script.

**The trajectory requires active observation.** The [context engineering study](../sources/context-engineering-ai-agents-oss.ingest.md) found that 50% of AGENTS.md files were never changed after creation — write-once artifacts that never enter the maturation trajectory at all. The codification trigger above (observing that the agent consistently proposes the same correct step) only fires if someone is watching. Among the files that do evolve, additions (78 commits) and modifications (59) vastly outnumber removals (23) and section deletions (2) — pruning is a discipline, not an emergent behavior. Instructions accumulate unless someone actively removes them.

The maturation trajectory parallels [document type maturation](./document-types-should-be-verifiable.md) — just as documents start as untyped `note` and gain type information as they codify, practices start as written guidance and gain enforcement structure as they prove out. Both are gradual typing applied to different substrates: types accumulate verifiable structural properties; enforcement accumulates deterministic triggers and responses. The [loading frequency hierarchy](./instruction-specificity-should-match-loading-frequency.md) mirrors the same gradient from the information-delivery side — CLAUDE.md instructions, skill descriptions, skill bodies — but for loading specificity rather than enforcement reliability.

## Current state

We have hooks in `.claude/hooks/` but they aren't wired up (`"hooks": {}` in settings.json) and reference old paths. We have scripts that work (sync_topic_links.py, generate_notes_index.py). We have skills that work (validate, connect, ingest). We have instructions that work (CLAUDE.md, WRITING.md). The gradient exists — we just haven't needed to push anything further toward the deterministic end yet.

## Open questions

- When should a WRITING.md instruction become a validate check? [Oracle strength](../notes/oracle-strength-spectrum.md) may provide the answer: a practice is ready to move down the gradient when you can cheaply verify whether it was followed correctly. If verification requires semantic judgment, the practice stays at skill level; if it can be reduced to structural checks, it is a candidate for scripting.
- Should hook warnings be treated differently from skill output? The LLM sees both as text, but the trigger mechanism differs.
- Are there practices currently at skill level that should be scripts? (sync_topic_links.py was probably this — a skill-level operation that turned out to be fully deterministic.)

---

Relevant Notes:

- [codification: the missing middle](../notes/deploy-time-learning-the-missing-middle.md) — grounds: the verifiability gradient for code (prompt tweaks -> schemas -> evals -> deterministic modules) is the general pattern this note instantiates for methodology
- [constraining is learning](../notes/constraining.md) — foundation: the constraining gradient for code; this note applies the same gradient to methodology
- [programming practices apply to prompting](../notes/programming-practices-apply-to-prompting.md) — synthesizes: the maturation trajectory is progressive compilation applied to methodology — flexible instructions frozen into rigid, efficient automation
- [001-generate-topic-links-from-frontmatter](./001-generate-topic-links-from-frontmatter.md) — exemplifies: a skill-level operation that completed the maturation trajectory into a deterministic script
- [what doesn't work](./what-doesnt-work.md) — examples: validation ceremony and session rhythm protocol as premature automation
- [document types should be verifiable](./document-types-should-be-verifiable.md) — parallels: document type maturation (note -> traits -> promoted base type) follows the same gradual-typing pattern as methodology maturation (instruction -> skill -> hook -> script); both trade flexibility for reliability as verifiability increases
- [oracle strength spectrum](../notes/oracle-strength-spectrum.md) — determines when a practice is ready to move down the enforcement gradient: cheap verification enables scripting; expensive verification keeps the practice at skill level
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — mirrors: the loading hierarchy (CLAUDE.md -> skill descriptions -> skill bodies) parallels the enforcement hierarchy, but for information specificity rather than practice reliability
- [error messages that teach are a constraining technique](./error-messages-that-teach-are-a-constraining-technique.md) — extends: adds the inform axis orthogonal to the trigger/response gradient; the most effective enforcement artifacts simultaneously constrain and teach
- [spec mining as codification](./spec-mining-as-codification.md) — generalizes: the maturation trajectory (instruction → script) is spec mining applied to methodology; both share the same codification trigger ("a pattern has emerged from repeated execution")
- [Agentic Note-Taking 23: Notes Without Reasons](../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.md) — exemplifies: the judgment/verification gradient explains why automated link generation (judgment operation) degrades quality while automated link validation (verification operation) preserves it
- [Context Engineering for AI Agents in OSS](../sources/context-engineering-ai-agents-oss.ingest.md) — validates: 169 annotated commits across 10 actively maintained AGENTS.md files show add-then-modify dominance (Add 78, Modify 59, Remove 23, Remove-section 2), confirming the maturation trajectory empirically
- [ABC: Agent Behavioral Contracts](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md) — formalizes: hard/soft constraint vocabulary and Drift Bounds Theorem (D*=α/γ) provide mathematical grounding for the enforcement gradient; maps warning hooks to soft constraints with recovery windows
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — exemplifies: three harness pillars (instructions → structural tests → automated cleanup agents) map to the constraining gradient; "every mistake is a harness bug" is the maturation trajectory in practitioner language
- [enforcement without structured recovery is incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — extends: adds the recovery column (corrective → fallback → escalation) missing from the enforcement gradient; oracle strength determines which recovery strategies are viable at each layer
