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

Instructions must be [**frontloaded**](../notes/frontloading-spares-execution-context.md)
into the context their declared consumer actually receives. They may omit a
rule supplied with binding force by verified Commonplace doctrine, an
applicable contract, or the invoked skill. They may not assume the author's
conversation, an unverified runtime load, or a link the executor is not
required to open. An instruction handed across an unverified path carries the
needed baseline itself.

## Prerequisites

Have one of these:

- repeated executions that expose which decisions remain stable across contexts;
- an accepted methodology whose mechanism entails the rule being operationalized;
- a machine or repository interface that already fixes the required protocol.

Otherwise keep the work in a workshop or log until its boundary is understood.

## Steps

1. **Name the operative path.** Identify who or what loads the instruction, when
   it fires, what authority it has, and which standing instructions that
   consumer receives with binding force. Search direct callers, callees, and
   consumers of its arguments, result literals, mutation rules, omitted
   inherited rules, and stop conditions before changing a live instruction.

2. **Classify the choices.** For each consequential choice the instruction does
   not state, determine whether a verified inherited rule governs it, task
   intent and authorized evidence deliberately leave it to execution, or the
   variation is irrelevant to acceptance and coupling. Anything else is a gap.
   Fix task-specific purpose, facts, commitments, interfaces, coordination
   decisions, authority, and acceptance conditions that those sources cannot
   determine. Codify recurring choices whose inputs are stable. Leave a bounded
   choice to the executor when authorized live or produced evidence can change
   or construct it.

3. **Draft from the goal and boundary.** State the intended result first. Use
   imperative steps for required sequencing and exact commands or grammars for
   load-bearing interfaces. Where several means can work, state constraints,
   available evidence, decision ownership, and verification instead of
   prescribing a guessed route.

   For consequential delegation, write the task packet as a delta from the
   verified Commonplace doctrine. Inspect the failures that could violate
   acceptance, authority, composition, or recovery and add task-specific
   controls for those surfaces only. The default that leaves scheduling,
   integration, and recovery with the parent need not be repeated when
   delivered, but any transfer does. Exact owned outputs and mutation scope
   remain explicit.
   When a consequential decision is deliberately deferred, preserve the option
   and name the discriminating evidence, convergence or return condition,
   decision owner, and invalidation or retry boundary.

4. **Add frontmatter.** Every instruction needs:
   ```yaml
   ---
   description: One line — what this instruction does, when to use it.
   type: kb/types/instruction.md
   ---
   ```
   Write the description for the situation in which the instruction should be
   retrieved, not as a summary of its internal vocabulary.

5. **Cut inherited or regenerable detail.** Keep the goal and the rationale
   needed to choose correctly at a boundary. Move durable theory to a
   methodology note. Remove a generic rule only after naming the binding
   artifact and verified consumption path that supplies it. Remove method
   choices a competent executor can derive from task intent, authorized
   evidence, and repository contracts. Record a narrow source dependency
   through source-side lineage; a universal Commonplace doctrine change reopens
   the whole commissioning cohort.

6. **Test the instruction.** Give it to a fresh agent through the declared
   consumption path, without the author's working conversation. A passing run
   identifies its inherited rules, delegated choices, irrelevant variation,
   and gaps; it needs no clarification about purpose, authority, owned outputs,
   interfaces, acceptance, or what returns control. It may choose different
   permitted means. Verify exact protocols mechanically where possible and test
   consequential branches, not only the happy path.

7. **Record the source relationship when useful.** A companion note is optional.
   Keep these relationships separate:
   - The stable core is generalized from repeated manual operations. If those source instances are retained and their collection authorizes the edge, record `Abstracted into:` at the source.
   - Where methodology notes shape the procedure body, record `Operationalized into:` in each methodology source note, pointing to the instruction. Do not collapse either relationship into a target-side `derived-from` link.

## Verify

- The operative consumer and trigger are known.
- Every inherited rule has a named binding source on the real consumption path.
- Fixed choices have a stable-input, interface, authority, or coordination reason.
- Open consequential choices have an authorized chooser and discriminating evidence.
- Failure-relevant authority, composition, verification, return, and recovery
  surfaces have controls; generic packet fields were not added by rote.
- A cold reader can execute the instruction without guessing its purpose,
  permissions, owned outputs, interfaces, or acceptance condition.
- Narrow source reliance has source-side lineage; broad Commonplace doctrine
  reliance has an identified commissioning cohort for change review.
- Exact protocols are mechanically checked where possible.

## Promotion to skill

If the instruction proves useful enough to warrant automatic routing:

1. Create `kb/instructions/<name>/` and move the instruction there as `SKILL.md`.
2. Add the skill frontmatter fields (`name`, `allowed-tools`, `context`, `model`).
3. Add `<name>` to `MANIFEST.promoted_skills` in `src/commonplace/scaffold_manifest.py`.
4. Update the control-plane routing table in `CLAUDE.md` or `AGENTS.md`.
 `commonplace-init` will then copy that instruction directory into the runtime skill surfaces (`.claude/skills/` and `.agents/skills/`) with the `commonplace-` prefix.
