---
description: Create or revise a reusable instruction by codifying stable decisions while preserving execution-dependent judgment.
type: kb/types/instruction.md
---

# Write an instruction

Write a procedure that removes predictable recurring decisions from execution
without freezing choices whose answer depends on evidence available only while
the work is running.

An instruction may be abstracted from repeated operations or operationalized
from established methodology. In either case, the evidence must identify a
stable decision rule and its boundary. Repetition alone does not make an
accidental sequence binding, and a single untested convenience does not earn
codification.

Instructions must be [**frontloaded**](../notes/frontloading-spares-execution-context.md) — self-contained enough for an agent with no prior context. Define terms inline. Don't assume the reader has loaded other KB documents. An instruction may be handed to a sub-agent that has nothing else in its context window.

## Prerequisites

Have one of these:

- repeated executions that expose which decisions remain stable across contexts;
- an accepted methodology whose mechanism entails the rule being operationalized;
- a machine or repository interface that already fixes the required protocol.

Otherwise keep the work in a workshop or log until its boundary is understood.

## Steps

1. **Name the operative path.** Identify who or what loads the instruction, when
   it fires, and what authority it has. Search direct callers, callees, and
   consumers of its arguments, result literals, mutation rules, and stop
   conditions before changing a live instruction.

2. **Classify the choices.** Fix upstream facts, commitments, interfaces,
   coordination decisions, and acceptance conditions that execution cannot
   safely recover. Codify recurring choices whose inputs are stable. Leave a
   bounded choice to the executor when authorized live or produced evidence
   can change it. Harmless, decoupled choices may remain open without extra
   machinery.

3. **Draft from the goal and boundary.** State the intended result first. Use
   imperative steps for required sequencing and exact commands or grammars for
   load-bearing interfaces. Where several means can work, state constraints,
   available evidence, decision ownership, and verification instead of
   prescribing a guessed route.

   For consequential delegation, inspect the failures that could violate
   acceptance, authority, composition, or recovery. Add controls for those
   surfaces only. The parent normally retains scheduling, integration, and
   recovery. When a consequential decision is deliberately deferred, preserve
   the option and name the discriminating evidence, convergence or return
   condition, decision owner, and invalidation or retry boundary.

4. **Add frontmatter.** Every instruction needs:
   ```yaml
   ---
   description: One line — what this instruction does, when to use it.
   type: kb/types/instruction.md
   ---
   ```
   Write the description for the situation in which the instruction should be
   retrieved, not as a summary of its internal vocabulary.

5. **Cut regenerable detail.** Keep the goal and the rationale needed to choose
   correctly at a boundary. Move durable theory to a methodology note. Remove
   explanations and method choices a competent executor can recover from the
   goal, authorized evidence, and repository contracts.

6. **Test the instruction.** Give it to an agent without the author's working
   context. A passing run needs no clarification about purpose, authority,
   owned outputs, interfaces, acceptance, or what returns control. It may choose
   different permitted means. Verify exact protocols mechanically where
   possible and test consequential branches, not only the happy path.

7. **Record the source relationship when useful.** A companion note is optional.
   Keep these relationships separate:
   - The stable core is generalized from repeated manual operations. If those source instances are retained and their collection authorizes the edge, record `Abstracted into:` at the source.
   - Where methodology notes shape the procedure body, record `Operationalized into:` in each methodology source note, pointing to the instruction. Do not collapse either relationship into a target-side `derived-from` link.

## Verify

- The operative consumer and trigger are known.
- Fixed choices have a stable-input, interface, authority, or coordination reason.
- Open consequential choices have an authorized chooser and discriminating evidence.
- Failure-relevant authority, composition, verification, return, and recovery
  surfaces have controls; generic packet fields were not added by rote.
- A cold reader can execute the instruction without guessing its purpose,
  permissions, owned outputs, interfaces, or acceptance condition.
- Exact protocols are mechanically checked where possible.

## Promotion to skill

If the instruction proves useful enough to warrant automatic routing:

1. Create `kb/instructions/<name>/` and move the instruction there as `SKILL.md`.
2. Add the skill frontmatter fields (`name`, `allowed-tools`, `context`, `model`).
3. Add `<name>` to `MANIFEST.promoted_skills` in `src/commonplace/scaffold_manifest.py`.
4. Update the control-plane routing table in `CLAUDE.md` or `AGENTS.md`.
 `commonplace-init` will then copy that instruction directory into the runtime skill surfaces (`.claude/skills/` and `.agents/skills/`) with the `commonplace-` prefix.
