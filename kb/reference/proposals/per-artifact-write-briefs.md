---
description: "Proposal: whether to preserve an optional artifact-specific commission stating the intended reader update, conditional on deterministic write-context assembly"
type: ../types/design-proposal.md
tags: [context-engineering, kb-maintenance]
---

# Per-artifact write briefs

Collection and type contracts say what belongs in a collection and what shape an artifact takes. They do not select why one particular artifact should exist. The ordinary writing skill establishes that contribution from the live request and, for an edit, the incumbent artifact. A completely new note has no incumbent, and later revisions have no independent retained account of the audience, angle, scope, and reader update that commissioned it.

The new, untested multistage writing skill creates a temporary workshop brief. That experiment shows one way to separate task-fixed intent from evidence, but it is neither the architectural baseline nor a required consumer of this proposal. A smaller version of that separation could instead enter ordinary new-note writing through deterministic context assembly.

This proposal depends on [deterministic write-context assembly](./deterministic-write-context-assembly.md). A durable write brief must become operative through that one coded, provenance-preserving path. This proposal does not authorize a second lookup convention in each writing skill. If the assembler is not adopted, the durable-brief options here remain unadoptable and current prompt/incumbent reconstruction continues.

## Current state (as of 2026-08-08)

- [`cp-skill-write`](../../instructions/cp-skill-write/SKILL.md) requires the writer to identify the intended audience, governing question or purpose, reader update, and distinguishing angle before drafting. It proceeds without a formal brief when the task or incumbent already determines them.
- [`cp-skill-write-multistage`](../../instructions/cp-skill-write-multistage/SKILL.md) is new and untested. It creates `brief.md` in a temporary workshop to record task-fixed intent separately from evidence, but successful promotion normally deletes the workshop. This is experimental design evidence, not established behavior that the proposal must preserve.
- A completed note's title, description, and body are its reader-facing account of the realized contribution. No retained artifact-specific commission is loaded automatically during later edits.
- Frontmatter `type:` points to the type contract. No field or validated association points to an artifact-specific write brief.
- The theory now distinguishes a topic from the particular [warranted reader update](../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) around which substantive writing organizes evidence and reasoning.
- The deterministic write-context assembler is only a proposal. No shipped command currently has a recognized brief input role.

## Problem

When several materially different contributions fit one topic, a new-note writer has to establish the commission from the live task before there is an artifact to inspect. Later writers can then mistake the incumbent artifact for its own specification. They can preserve accidental structure because it is present, or change the governing angle because the original task context is gone. A retained brief could preserve counterfactual information: not only what the current note says, but what it was meant to make its intended reader understand, infer, or do.

The brief can also become a shadow note. If readers need it to understand the artifact, the artifact is not self-standing. If it repeats claims, evidence, or prose, the two copies drift. If it is generated retrospectively from the incumbent, it records no independent intent and may launder accidental content into an apparent commission. Requiring one for every artifact would double files and maintenance even where the contribution is already obvious.

## Proposed boundary

A write brief, where present, is an artifact-specific commission. It may fix:

- the intended reader, especially where it narrows the collection default;
- the governing question, target claim, or practical purpose;
- the proposed update the reader should gain;
- the angle that distinguishes this artifact from nearby treatments;
- scope, exclusions, and decisions reserved for the user;
- named evidence inputs available to the writer, without treating user direction as evidence.

It does not supply warrant for the proposed update, override collection or type contracts, prescribe choices the executor can determine from live evidence, or excuse the finished artifact from making its own contribution legible. The brief is authoritative about retained intent only to the extent declared by its lifecycle; claims still earn acceptance through the artifact's evidence and reasoning.

Under either durable-brief option, a write brief is itself written and revised through the ordinary writing skill. It receives the collection and type context appropriate to whichever storage option is chosen, plus the live request that names the artifact it commissions. It is not eligible for another write brief. That non-recursive role boundary avoids a second writing procedure without creating a commission for the commission.

## Options

### 1. Keep intent transient or reconstruct it from the artifact

Ordinary writing continues to use the live request and incumbent. An experimental writing procedure may create temporary task-specific scaffolding, but no retained artifact-specific input enters the ordinary path.

**Operativity path:** current skills remain the only consumers. User intent reaches the writer through the invocation context; incumbent content reaches it through the target read. Nothing persists as an independent per-artifact instruction.

This is the smallest system and avoids shadow intent. It cannot distinguish a later drift from an intentional change when the original commission is no longer present.

### 2. Put the intended contribution in the artifact itself

The artifact carries an explicit reader-facing purpose, contribution, or scope statement in its frontmatter or body. Later writers recover the angle by reading the artifact, and readers see the same declaration.

**Operativity path:** the type or collection contract authorizes the representation; writing and review procedures read it as part of the artifact. If structural, validation can require or constrain it.

This maximizes self-sufficiency and avoids a sidecar association. It does not preserve an independent commission against which the incumbent can be evaluated, and procedural details or rejected alternatives may burden readers.

### 3. Allow an optional durable write brief through the assembler

Selected eligible artifacts have an associated canonical brief. The proposed assembler recognizes the brief as a named input role, labels its authority, and supplies it to ordinary new-note writing and later substantive revision. In new-write mode the assembler may render an explicitly supplied commission or expose the contribution fields that remain unresolved before a durable association exists. When the target is itself a write brief, that role is inapplicable rather than missing. Absence preserves the current path for other targets.

**Operativity path:** the artifact or another validated association identifies the brief; the coded assembler resolves and injects it; writing and revision skills consume the assembled context. A brief edit affects future writes immediately. If the design later gives brief changes freshness consequences, the review system also marks the target for reconsideration.

This preserves independent intent only where its value exceeds its lifecycle cost. It depends on deterministic assembly so storage and association mechanics do not spread into every consumer. The multistage experiment may use the same role later if testing shows that it should, but it is not part of this option's initial operativity path.

### 4. Require a durable brief for every substantive artifact

Every eligible type carries a commission before drafting, and later maintenance always loads it. The write-brief role itself remains ineligible, so uniformity does not imply an infinite chain.

**Operativity path:** type and collection contracts require the association; the assembler refuses an eligible write without it; validation or review checks presence and any declared freshness relation.

This makes intended contribution uniformly explicit and reviewable. It adds an artifact, an association, and maintenance obligations even when title, description, request, and body already determine the contribution without ambiguity.

## Forces

- **Independent purpose versus self-standing prose.** A brief is useful as a specification only when it remains distinct from the current artifact. The artifact must nevertheless be understandable without loading hidden authoring context.
- **Intent versus warrant.** User direction can select a question and angle. It cannot make factual claims true or establish that the proposed update is worth retaining.
- **Continuity versus staleness.** Durable intent can prevent accidental drift, but audience priors, neighboring notes, and project needs change. A once-distinctive update can become redundant.
- **Optional value versus uniform machinery.** Ambiguous, commissioned, or consequential artifacts benefit most. Many small notes do not need another file.
- **Pre-draft independence.** A brief written or accepted before drafting contains counterfactual information. A brief generated from the finished artifact may only restate it.
- **Authority and precedence.** Artifact-specific intent may narrow the collection default but cannot silently override collection, type, linking, or validation requirements.
- **Association lifecycle.** New targets do not yet have frontmatter; renames, moves, retirement, splits, and merges must preserve or deliberately revise any relation.
- **Context cost.** A compact commission can spare reconstruction. An accreted history, outline, source dump, or critique packet would compete with the writing itself.
- **Experimental precedent.** The multistage brief suggests useful separations, but copying its whole lifecycle into ordinary writing would turn an untested experiment into architecture by accident.
- **One writer versus terminating context.** Briefs should benefit from the ordinary collection and type machinery. They should not recursively require the same artifact-specific role they provide to another target.

## Free choices

- Where the brief lives and which side declares the association. A direct path is explicit; a naming convention is cheaper but makes discovery and rename behavior implicit.
- Whether the brief is a typed KB artifact, a system-definition artifact outside ordinary collections, or retained workshop material with a durable target relation.
- Whether its force is advisory, intent-authoritative until explicitly amended, or review-invalidating when changed.
- Who may create or revise it, and whether a model-proposed brief requires human acceptance before it can constrain later writers.
- Whether a new-write invocation can supply or create a durable brief before the target exists, and what makes that association unambiguous.
- Whether the multistage experiment should ever consume the durable role. That is a later choice contingent on evidence from using that procedure, not part of initial adoption.
- How write-brief ineligibility is represented and validated across the possible storage forms. It must not depend on a filename coincidence or an agent remembering to skip a lookup.
- Whether writing a brief also loads selected metadata about the artifact it commissions, and how that subject context remains distinct from a brief for the brief.
- What happens when the incumbent artifact and brief disagree: preserve the commission, amend it, rewrite the artifact, merge with a neighbor, or retire the now-redundant target.
- Whether one brief may commission several artifacts after a split, or each resulting artifact must acquire its own angle.
- Which artifact types or risk classes may opt in, and whether any later evidence could justify a mandatory cohort.

## Adoption criteria

- The [deterministic write-context assembler](./deterministic-write-context-assembly.md) is adopted first or in the same decision, with a closed recognized role for the brief. No writing skill gains an independent target-adjacent search rule.
- An ordinary-writing pilot shows that a new-note writer can preserve explicit task-fixed intent and that later writers preserve or deliberately revise the governing contribution better than from the incumbent and task context alone.
- The brief records an intended reader update, scope, and fixed decisions without duplicating the artifact's claims, evidence, outline, or prose.
- The finished artifact remains self-standing: a reader can recover its realized contribution without opening the brief.
- A brief is independently authored or explicitly accepted; automatic retrospective summaries do not acquire intent authority.
- Absence is valid for artifacts whose contribution is already determined. Optionality does not create warnings or fictional missing state.
- Association, rename, move, split, merge, retirement, and orphan behavior are explicit and testable before durable briefs become common.
- The design states whether a brief edit merely affects the next write or stales the target for review. Binding force is not implied by the word `brief`.
- Collection and type contracts remain stronger constraints, while a live user decision can explicitly amend the commission rather than being treated as a conflict to hide.
- Context limits prevent a brief from becoming an accumulated authoring history or evidence bundle.
- Adoption does not depend on the multistage skill, and does not silently import its workshop or agent-stage machinery into ordinary writing.
- The ordinary writing skill authors briefs without a separate procedure; the assembler deterministically omits the write-brief role for those targets and fails clearly on any malformed association cycle.

## Risks

- **Shadow specification.** Writers may optimize for hidden intent while the published artifact no longer communicates why it exists.
- **Double truth.** Brief and artifact can disagree about the governing claim, audience, or scope with no obvious current authority.
- **Retrospective laundering.** Generating a brief from the incumbent can convert accidental content into apparently deliberate purpose.
- **Overconstraint.** Detailed structure or prose instructions can freeze choices a later writer should make from current evidence.
- **File multiplication.** Optional sidecars can become a customary requirement and enlarge navigation, validation, and retirement work.
- **Stale interestingness.** The intended update can cease to be nontrivial relative to the current KB while the brief continues to demand its preservation.
- **Instruction injection.** An unvalidated adjacent file could acquire behavioral authority merely by matching a lookup convention.
- **Dependency inversion.** If skills learn to find briefs themselves, the brief feature bypasses the assembler it depends on and recreates the complexity this proposal is meant to avoid.
- **Commission regress.** If every written artifact is assumed to need a brief, the brief becomes another target needing another brief and the model has no principled stopping point.

---

Relevant Notes:

- [Warranted reader update is the objective of substantive writing](../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) — rests-on: the brief preserves the proposed audience-relative update around which evidence and reasoning should be organized
- [A bare writing prompt does not determine its intended contribution](../../notes/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) — rests-on: topic and form leave materially different commissions open
- [An author should fix what the executor cannot determine, not what it will](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — rests-on: the brief should retain authorial purpose and exclusions without prescribing live writing choices
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: retaining a commission helps only when the writing path reliably loads it
- [Deterministic write-context assembly](./deterministic-write-context-assembly.md) — see-also: the prerequisite proposal that supplies the only proposed operativity path through which a durable brief reaches writers
- [cp-skill-write](../../instructions/cp-skill-write/SKILL.md) — procedure: the current contribution-resolution step a durable brief would inform
- [cp-skill-write-multistage](../../instructions/cp-skill-write-multistage/SKILL.md) — see-also: an untested experiment whose temporary brief suggests a possible separation without setting this proposal's architecture
