---
description: "Proposal: reuse natural-language authoring mechanics in specialized writer prompts through literal inlining backed by deterministic source-to-copy checks"
type: ../types/design-proposal.md
tags: [architecture, context-engineering]
---

# Checked inline blocks for shared instruction text

Extracting a function in code separates one implementation from its call sites. Natural-language instructions have no equally reliable call operation: a link does not make the reader follow it, asking an agent to load another skill spends context and introduces another interpretation step, and invoking a whole workflow composes far more behavior than a caller may need. Yet copying the needed prose into every consuming prompt creates independent versions of behavior that should remain identical.

Commonplace has a concrete instance. [`cp-skill-write`](../../instructions/cp-skill-write/SKILL.md) carries universal artifact-authoring mechanics, while [`write-agent-memory-system-review`](../../instructions/write-agent-memory-system-review/SKILL.md) constructs a self-contained brief for a delegated writer. The specialized workflow needs some of the generic mechanics, but not the generic workflow around them. This proposal parks the design question exposed by that seam: whether a small natural-language instruction block should behave like an expanded function body—literal at each point of use, authoritative in one place, and mechanically prevented from drifting.

## Current state (as of 2026-07-28)

- `cp-skill-write` is the operational home for general authoring behavior. Its `Universal Mechanics` section currently covers frontmatter, descriptions, active vocabulary, links, filenames, lineage, and renames. [ADR 022](../adr/022-active-vocabulary-and-write-path-first-mentions.md) deliberately made it the single operational home for first-mention vocabulary behavior.
- `write-agent-memory-system-review` is a complete orchestration workflow, not a thin specialization of `cp-skill-write`. It prepares a checkout, manages replacement reviews, delegates drafting, performs taxonomy and semantic QA, and validates the result.
- The delegated writer receives a deliberately self-contained task brief. It reads the agent-memory collection and type contracts plus examples, but it neither invokes nor reads `cp-skill-write`. The brief also tells the worker not to follow the specialized parent skill if skill discovery surfaces it again.
- The shared note schema enforces the current 50–250-character description bound on completed artifacts. Generic writing and conversion instructions repeat that bound, and the agent-memory review type repeats it for its writers. Validation can reject the resulting artifact, but it does not ensure that every writing prompt taught the same rule before drafting.
- No mechanism marks reusable instruction regions, declares a source/copy relation between them, or checks their textual agreement.

## Problem

The desired reuse unit is smaller than either existing skill. Calling the whole generic writer from the specialized review workflow would combine target resolution, duplicate handling, writing, validation, and connect handoff with a parent workflow that already owns those responsibilities. A live reference to only `Universal Mechanics` avoids workflow duplication, but makes every delegated writer perform an additional read and decide how the general prose applies. An ordinary inline copy gives the worker the right text at the right moment, but has no force keeping it aligned when the source changes.

This is the natural-language equivalent of a missing function boundary, except the medium lacks trustworthy dereference and composition semantics. The design needs to preserve two properties that pull in opposite directions:

- one authoritative definition for maintainers; and
- literal, sufficient instructions in the bounded context that performs the work.

The existing rule that [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) rules out a trusted, hand-maintained middle state. The question is which checked or absent form fits instruction text.

## Option space

### Read the shared contract live

Extract the common mechanics into a source that every writer is explicitly told to read. The delegated writer consumes that file through a path in its task brief, with the source's prescriptive force. This preserves a single text but adds a read, exposes the worker to surrounding material it may not need, and relies on the worker to carry the relevant rules across the indirection.

The source could remain a named section of `cp-skill-write` or become a smaller neutral contract. The latter improves granularity but creates a new artifact whose discovery and authority must be explained.

### Compose the complete generic writer

Make the specialized workflow invoke `cp-skill-write` as a subroutine. The skill-loading or delegation channel would give the generic skill prescriptive force over drafting. This offers reuse only at the wrong granularity: both workflows would compete to own setup, artifact selection, validation, and handoff. It becomes plausible only if the generic skill is first split into a reusable authoring kernel and an orchestration shell—which returns the design to the smaller shared contract above.

### Keep independent inline prose

Repeat the mechanics manually wherever needed. Each writer consumes literal prose in its own skill or delegated task, with direct prescriptive force and no extra read. This is the simplest execution path but leaves no oracle for agreement. It is a description of the current failure mode, not a safe steady state: a maintainer can update one copy and receive no signal that another writer now teaches different behavior.

### Check marked inline copies against one source

Give the shared block one declared authority and place marked literal copies at specialized consumption sites. The delegated writer consumes the inlined block directly in its complete task brief, so no runtime dereference is required. A deterministic check extracts the declared source and each registered copy and fails when their text differs, giving the source/copy relation enforcement force during validation or tests.

This is closer to macro expansion than ordinary function calling: execution sees the expanded body, while maintenance sees one authoritative definition plus derived copies. The block must stay narrow. Truly shared artifact mechanics belong inside it; orchestration, collection-specific contracts, and deliberate overrides remain outside it.

### Generate consuming instructions from a shared fragment

Store the common block once and materialize complete skills or worker briefs through a build or generation step. Consumers still receive literal text with prescriptive force, while the generator owns agreement. This generalizes beyond the immediate pair and aligns with [generating instructions at build time](../../notes/generate-instructions-at-build-time.md), but it introduces a source/artifact lifecycle and does not currently cover the uninitialized Commonplace source checkout. It is adjacent to, but narrower than, the open proposal for [channel-compiled instruction artifacts](./channel-compiled-instruction-artifacts.md): the variable here is shared instruction content, not execution environment.

## Forces

- **Point-of-use sufficiency.** The drafting worker should receive the rules required for its task without discovering another workflow or reconstructing their relevance.
- **Single maintenance authority.** A universal rule should have one place where it is intentionally changed; all other occurrences should be visibly derived.
- **Composition granularity.** The reusable unit must exclude target selection, collision handling, graph work, and other orchestration owned by the caller.
- **Context cost.** Live reads load a surrounding artifact and consume a tool round trip; inlining consumes prompt tokens on every call. Which cost dominates depends on block size and reuse frequency.
- **Failure visibility.** Source-only and copy-only edits should fail near edit time, not emerge later as divergent writer behavior.
- **Local readability.** A maintainer reviewing the specialized worker brief should be able to see what the worker will receive without mentally executing a template system.
- **Override semantics.** Specialized differences must be explicit and outside the identical region. Allowing edits inside a supposedly shared block would turn exact checking into ambiguous semantic comparison.
- **Projection lifecycle.** Generated or copied instructions need a clear refresh path in source checkouts and installed projects; otherwise enforcement exists only in one operating environment.
- **Mechanism weight.** A one-off equality test may solve the present case more cheaply than a general fragment language, registry, or synchronizer. Generalization should follow another worked case rather than precede it.

## Free choices

- **Authority location.** The source may be a marked section inside `cp-skill-write`, where generic authoring behavior already lives, or a neutral fragment consumed by both writers. This turns on whether the fragment is conceptually part of the generic skill or an independent contract.
- **Identity boundary.** The first block might cover only frontmatter and description mechanics, or a larger set of universal mechanics. Inclusion turns on demonstrated invariance across writers, not convenience of copying a contiguous section.
- **Copy discovery.** Copies may name their source locally, or a central inventory may enumerate them. Local declaration favors inspectability; central registration favors complete enumeration.
- **Check surface.** Agreement may be enforced by the ordinary KB validator, by focused tests, or by generation that makes stale output detectable. This turns on where instruction-only edits already receive reliable checks.
- **Comparison strictness.** Exact normalized text identity gives a cheap oracle; structural or semantic equivalence would permit local formatting but requires a more complicated and less warranted judge.
- **Repair path.** A failed check may only explain the mismatch, or a separate command may refresh derived copies. Automatic rewriting should not be assumed until the authority and review ergonomics are proven.
- **Initial scope.** The mechanism may remain a focused check for these two writers or become a general facility for marked instruction regions. The second choice needs evidence of repeated demand.

## Operativity and oracle warrant

The live-read option operates through an explicit file-read instruction in the delegated brief: the worker is the consumer, the file path is the channel, and the shared contract's imperative prose supplies force. Its weakness is not missing force but dependence on an extra dereference and interpretation step.

Complete-skill composition operates through the harness's skill mechanism, with the generic workflow binding the drafting worker or a nested worker. Its present problem is conflicting ownership, not lack of a consumer.

Checked inlining operates through two paths. At execution time, the drafting worker consumes literal prose embedded in its task brief with the same prescriptive force as the rest of that brief. At maintenance time, validation or tests consume the marked source and copies and block mismatches. The deterministic oracle is warranted only for the claim that the regions are textually identical to the declared source. It cannot decide that the source is good, that a rule is truly universal, or that the surrounding prompt does not contradict it; those remain semantic review questions.

Generated instructions operate only where a generation/refresh channel exists. Installed projections have such a lifecycle, but the repository's own source checkout currently does not. Adoption would therefore need either a source-checkout consumer for generation or an explicit reason the mechanism need not protect that surface.

## Adoption criteria

- A worked extraction identifies a bounded block needed unchanged by both the generic writer and the delegated agent-memory writer, with specialized behavior demonstrably left outside it.
- Editing either the authority or a derived copy causes a normal developer check to fail before either divergent prompt can be treated as current.
- The check's error identifies the authority and affected copy clearly enough that repair does not require reverse-engineering the mechanism.
- The consuming worker receives no additional runtime read and can understand its complete drafting obligation from the literal brief.
- The chosen authority location remains consistent with `cp-skill-write` being the operational home of universal authoring behavior, or explicitly revises that ownership through a later decision.
- Prompt-size and maintenance measurements from the worked case show that inlining the selected block is cheaper than loading the source live.
- A second reuse case is observed before promoting the focused mechanism into a general-purpose fragment system.

## Out of scope

Choosing the exact marker syntax, defining a general natural-language module system, deduplicating collection-specific artifact contracts, or changing the description limit itself. This proposal concerns how identical prescriptive text can be reused without runtime dereference or silent drift.

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: rules out a trusted but unchecked inline copy and supplies the deterministic-oracle boundary
- [Natural-language content lacks reliable dereference, so facts need reinforcement at point of use](../../notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md) — rationale: explains why linking to shared prose does not reliably place it in the consuming context
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) — rationale: frames literal insertion of already-known instruction content as a context-shaping operation
- [Indirection is costly in LLM instructions](../../notes/indirection-is-costly-in-llm-instructions.md) — rationale: accounts for the execution cost of making a delegated writer follow an additional instruction reference
- [Generate KB skills at build time, don't parameterise them](../../notes/generate-instructions-at-build-time.md) — alternative: grounds the generated-artifact option and its standalone-consumer property
- [ADR 022 — Active vocabulary and write-path first mentions](../adr/022-active-vocabulary-and-write-path-first-mentions.md) — current-state: establishes `cp-skill-write` as the operational home for universal first-mention authoring behavior
