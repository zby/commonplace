---
description: "Proposal: whether code should assemble a target's fixed authoring context while keeping named input roles closed rather than opening a generic provider mechanism"
type: ../types/design-proposal.md
tags: [context-engineering, kb-maintenance]
---

# Deterministic write-context assembly

Commonplace's ordinary writing procedure currently composes its authoring context itself. This is not one uniform operation: an edit has an incumbent artifact from which to resolve the target and recover evidence of its intended contribution, while a new write has neither. The skill therefore carries both filesystem mechanics and mode-specific instructions about what information to establish before drafting. A proposed per-artifact write brief would add another named input, but it is not the only reason to consider moving the deterministic part into code.

The design question is whether a narrow tool should compile the authoring context already knowable for the particular mode, including additional initiation information for a completely new artifact, and whether doing so must also open an extensibility mechanism for future inputs.

The two choices are independent. A coded assembler can have a closed set of named input roles. Making those roles open to arbitrary providers is a separate design with different costs.

## Current state (as of 2026-08-08)

- [`cp-skill-write`](../../instructions/cp-skill-write/SKILL.md) implements separate edit and new-write branches in prose. It resolves the target collection and type, reads their contracts, and establishes the intended contribution from the live request plus the incumbent when one exists.
- New-write mode defaults or selects a collection and type before a target artifact exists. It also has to establish audience, purpose, reader update, and distinguishing angle without an incumbent from which to recover them.
- [`cp-skill-write-multistage`](../../instructions/cp-skill-write-multistage/SKILL.md) is a new, untested experiment. Its separation of task-fixed intent into a temporary workshop `brief.md` is a possible source of features for ordinary writing, not established architecture or a required initial consumer. The standalone [`asd-ste100-inspired-rewrite`](../../instructions/asd-ste100-inspired-rewrite.md) instruction also repeats target, collection-contract, and type-specification reads.
- [`type-loading`](../type-loading.md) describes the shipped design as read-time composition of ordinary files. There is no resolver command or generated write-context packet.
- [ADR 018](../adr/018-types-are-path-references-to-instruction-docs.md) considered and rejected `commonplace-write-context`. The accepted comparison favored direct pointers and ordinary file reads because a synthesized packet introduced another interface for agents to interpret.
- The current skills own semantic as well as mechanical instructions: they say which paths to resolve, what failures stop writing, how contracts combine, and what the writer must decide.
- The [per-artifact write-brief proposal](./per-artifact-write-briefs.md) is unadopted. It depends on this proposal because it must not add a separate brief-discovery protocol to every writer.

## Problem

Direct file reads preserve transparency and avoid tooling, but the ordinary skill must encode the mechanics around them. Its new-write branch has to resolve a not-yet-existing target, expose the available structural choices, carry task-fixed information forward, and make missing semantic choices visible. Its edit branch can instead derive some of those facts from the incumbent. As more of that deterministic preparation is expressed in skill prose, the procedure becomes harder to inspect and test even before another consumer exists.

Other writing procedures provide secondary evidence that resolution mechanics can recur, but no design should be justified by treating an untested multistage experiment as a settled consumer. The immediate question is whether the ordinary path itself becomes clearer when code supplies a mode-appropriate context packet and the skill retains the writing judgment.

The opposite response is also dangerous. A generic context-provider interface would make new inputs cheap to add before their loading frequency, authority, context cost, or lifecycle has been justified. The prediction that more inputs will appear can become self-fulfilling because the extension point removes the friction that would otherwise test each addition.

The design therefore needs to distinguish a universal operation—resolve the known authoring context for a target—from an open universe of context sources.

## Options

### 1. Keep composition in each writing procedure

Each skill continues to resolve and read ordinary canonical files. A write brief, if ever adopted, would require an additional explicit read in every consuming procedure.

**Operativity path:** skill text remains the behavioral authority. Each changed skill affects the next agent invocation that loads it; no code or generated packet mediates the inputs.

This keeps the shipped file-native model and has no new runtime dependency. Its cost grows with the product of authoring inputs and consumers, and semantic agreement among those consumers remains a maintenance obligation.

### 2. Factor target and contract resolution into code

A narrow resolver identifies whether the operation is a new write or an edit, identifies the target collection and type, reports their canonical paths, and diagnoses missing or ambiguous inputs. In new-write mode it can report the valid type choices and facts that still need to be supplied; in edit mode it can report facts recovered from the incumbent. Writing procedures still read the returned files and explain how their scopes combine. A future brief relation could be resolved the same way without inserting its contents.

**Operativity path:** writing and revision skills call the resolver, then load and compose the named files themselves. Code owns path identity and mechanical errors; skill text remains the authority for reading order, role, precedence, and semantic use.

This removes duplicated filesystem logic while preserving native file reads. It may not simplify the consequential part of the procedure: every consumer must still interpret the same roles, combine them consistently, and decide what a missing optional or required input means.

### 3. Add a closed, mode-aware deterministic assembler

A package command or equivalent tool resolves a fixed set of named authoring roles and renders one inspectable packet. The collection and type contracts are the established common roles. The packet may differ by declared mode: an edit can include facts resolved from the incumbent, while a new write can include deterministic initiation material that would otherwise be spelled out or discovered inside the skill. For example, it could expose valid structural choices, preserve explicit task-fixed intent, and identify unresolved contribution fields. It must not invent answers to those fields. A write brief becomes another named role only if its companion proposal is adopted first or in the same decision.

Canonical Markdown and explicit invocation inputs remain authoritative. The packet is transient and identifies the source, role, and force of every included block. Features borrowed from the multistage experiment enter only when they make the ordinary path better; adopting this option does not adopt its workshop pipeline, multi-agent stages, or promotion lifecycle.

The assembler resolves paths, ordering, provenance, and mechanical errors. It does not select an angle, discover evidence, summarize source content through an LLM, or accept arbitrary extra context. Adding another role requires an explicit change to the assembler's contract and tests rather than registration through a generic provider API.

Named roles also need explicit applicability and termination rules. If a durable write brief is added, the ordinary writing skill should still write the brief artifact, but assembly for that target must omit the write-brief role. The brief still receives its collection and type contracts; it does not acquire a brief of its own. Cycle rejection remains a defensive backstop for malformed associations rather than the normal way recursion terminates.

**Operativity path:** the ordinary writing skill calls the package command with the known operation and target information, then consumes the rendered packet. Canonical contract or brief edits affect the next invocation because the packet is rendered from live files. The skill retains semantic drafting and stopping rules but no longer duplicates input lookup, mode branching, and combination mechanics that the tool can determine. Other writing procedures may adopt the same path later on their own evidence.

This centralizes a real invariant while deliberately preserving friction against scope growth. It introduces code, command availability, output semantics, and a new failure boundary.

### 4. Add an extensible context-provider mechanism

A registry or provider protocol lets independently defined inputs contribute blocks to the authoring packet. Collection, type, brief, vocabulary, evaluation, retrieval, or future sources could enter through the same extension surface.

**Operativity path:** providers register with the assembler; every writing consumer receives their output whenever the provider's selection rule matches the target. Provider registration therefore changes writing behavior without editing the consuming skills.

This is the most general design and the easiest to accrete. It needs admission, precedence, trust, context-budget, conflict, and observability rules before the first third-party or collection-defined provider can be treated as binding. No current requirement establishes that this openness is needed.

## Forces

- **Ordinary-path value versus speculative reuse.** The first implementation should earn its cost by improving ordinary new and edit writes. Reuse by the untested multistage procedure or future writers is possible but cannot supply the initial warrant.
- **Mode asymmetry.** An edit has an artifact, path, type declaration, and realized prose. A new write has only invocation inputs and defaults. Treating both as the same lookup either hides missing choices or burdens edits with initiation material they do not need.
- **File authority versus compiled convenience.** Writers should be able to identify the canonical source of every instruction. A transient packet is useful only if it preserves that provenance and does not become a second editable truth.
- **Context economy.** Assembly can remove discovery, tool calls, and repeated interpretation. It does not automatically reduce raw tokens when it inserts the same complete documents the agent would otherwise read.
- **Semantic restraint.** Code can determine paths and declared roles. It cannot determine an intended contribution or decide which evidence matters without crossing into the writing judgment it is meant to support.
- **Cross-runtime usability.** A package command with ordinary text output can serve different agent runtimes. A harness-specific injection hook would narrow the otherwise general operation.
- **Failure visibility.** Missing collections, invalid type paths, ambiguous new-write inputs, oversized packets, and unavailable optional inputs should be explicit states rather than partially assembled prompts.
- **Resistance to accretion.** A closed implementation keeps each new role expensive enough to require a scope, authority, loading condition, and context-cost argument.
- **Shared writing path versus recursive context.** An input artifact should not need a special writer, but applying its own input role to itself creates regress rather than useful context. Role eligibility must be narrower than eligibility for the ordinary writing skill.

## Free choices

- Whether the agent-facing result contains literal source text, a manifest of source paths for the agent to read, or both. Literal rendering reduces runtime indirection; a manifest preserves native file reads and may use editor caches better.
- Whether structured data is an internal representation only or also a public output format. The LLM-facing surface can remain Markdown even if tests use a typed object.
- Whether ordinary writing is the sole initial consumer. The multistage experiment can be reconsidered after its own behavior has been tested.
- How new-write mode supplies a proposed target, collection, and type before an artifact exists.
- Which additional new-write information is worth compiling. Every candidate needs a deterministic source, a named role, a loading condition, and a context-cost argument; the existence of the tool is not sufficient warrant.
- Whether the packet includes provenance and context-cost diagnostics, and how clearly it separates diagnostics from binding instructions.
- Whether failure to find an optional role is silent absence or an explicit diagnostic. A declared-but-missing input should not look the same as an undeclared one.
- Whether the closed assembler is adopted independently of write briefs, using only the already-shipped collection and type inputs.
- Where role eligibility is declared. A type-level rule is explicit; an association-level rule accommodates more storage forms but must still be deterministic and validated.

## Adoption criteria

- The assembler materially simplifies both branches of ordinary writing rather than adding a command the skill must extensively explain.
- Existing-target and new-target cases resolve deterministically, with explicit unresolved states where the target does not yet determine a collection or type.
- A new-note pilot shows that mode-specific information prevents repeated discovery or lost task intent without asking code to choose the note's contribution.
- Every inserted instruction identifies its canonical path, semantic role, and force. The packet is never an independently editable artifact.
- Contract changes take effect without a build or cache-refresh step.
- The assembler performs no LLM judgment, source discovery, angle selection, or evidence synthesis.
- The initial input set is closed. Adding a new role requires a named contract and test change; no generic extra-input list or provider registry ships incidentally.
- Tests establish agreement between the assembler, type validation, collection resolution, and the ordinary writing skill's accepted cases.
- A context-cost comparison counts both output bytes and avoided tool/discovery work; the assembler does not win merely by moving the same complexity behind a command.
- Failure remains understandable when the command is unavailable in an installed project or a runtime cannot invoke it.
- The ordinary writing skill can author a write brief. The write-brief role has an explicit eligibility rule that excludes write-brief targets, and the assembler rejects malformed association cycles, so writing a brief never searches for a brief for that brief.

## Risks

- **Opaque mega-prompt.** A writer may obey combined text without understanding which source has authority or how to inspect it.
- **Moved rather than removed complexity.** If skills still explain packet interpretation, precedence, and most resolution failures, the command becomes an extra layer around the same procedure.
- **Accidental extension platform.** A convenient internal abstraction may be exposed as a provider API without evidence that arbitrary authoring inputs should be admissible.
- **Context amplification.** Literal assembly may duplicate already-loaded instructions or insert complete files when a path and targeted read would have been cheaper.
- **Source divergence.** Summarized, normalized, or cached copies can drift from canonical files unless output is live and mechanically attributable.
- **Authority injection.** Treating any target-adjacent file as an instruction source would let ordinary content acquire behavioral force merely through placement or naming.
- **Tool dependency.** A writing path that previously needed only file reads now depends on installed code and a stable command surface.
- **Recursive activation.** If role applicability is inferred from proximity or convention, writing one context artifact can trigger an unbounded chain of context-for-context artifacts.

---

Relevant Notes:

- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) — rests-on: deterministic assembly can replace repeated discovery and interpretation with already-resolved authoring inputs
- [Instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) — rests-on: target-specific inputs should load only for the write that needs them
- [An author should fix what the executor cannot determine, not what it will](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — rests-on: the assembler may resolve known bindings but must not freeze situation-dependent writing judgments
- [ADR 018: Types are path references to instruction docs](../adr/018-types-are-path-references-to-instruction-docs.md) — compares-with: the accepted direct-file design and its earlier rejection of a synthesized write-context packet
- [Type loading](../type-loading.md) — evidenced-by: the current three-input read-time authoring model and absence of a resolver
- [Per-artifact write briefs](./per-artifact-write-briefs.md) — see-also: the first proposed optional input whose adoption depends on this assembly boundary
