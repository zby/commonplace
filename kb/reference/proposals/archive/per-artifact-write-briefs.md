---
description: "Proposal: whether to preserve an optional artifact-specific commission stating the intended reader update, delivered to writers by a validated pointer or a context-assembler role"
type: reference/types/design-proposal.md
tags: [context-engineering]
---

# Per-artifact write briefs

Collection and type contracts say what belongs in a collection and what shape an artifact takes. They do not select why one particular artifact should exist. The ordinary writing skill establishes that contribution from the live request and, for an edit, the incumbent artifact. A completely new note has no incumbent, and later revisions have no independent retained account of the audience, angle, scope, and reader update that commissioned it.

The multistage writing skill creates a temporary workshop brief. Its runs show one way to separate task-fixed intent from evidence, but that skill is neither the architectural baseline nor a required consumer of this proposal. A smaller version of that separation could enter ordinary writing as a durable brief.

A durable brief needs a delivery route: one declared, validated way by which a writer finds and loads it. This proposal offers two. A validated pointer read by the writing skill follows the direct-pointer design that `type:` already uses. The [deterministic write-context assembler](../deterministic-write-context-assembly.md), if adopted, could deliver the brief as a named input role instead. Neither route authorizes a writing skill to search for target-adjacent files by naming convention.

## Current state (as of 2026-09-26)

- [`cp-skill-write`](../../../instructions/cp-skill-write/SKILL.md) Step 4 requires the writer to identify the intended audience, governing question or purpose, reader update, and distinguishing angle before drafting. It proceeds without a formal brief when the task or incumbent already determines them.
- The same step already defines a consumer slot for retained intent. A context block counts as retained intent only when it identifies its source, subject, scope, and whether it is authoritative or advisory; current user direction prevails; an unresolved conflict with the incumbent goes to the user. The skill forbids an ad hoc history search and accepts older intent only when some mechanism supplies it through that input. No shipped mechanism supplies it.
- [`cp-skill-write-multistage`](../../../instructions/cp-skill-write-multistage/SKILL.md) has run on at least seven targets between 2026-08-14 and 2026-08-28 (run directories under `kb/work/multistage/`, recoverable from git history). Each run wrote a `brief.md`, and closing each run deleted it. The briefs mix two kinds of content. Some items are durable commission: governing question, audience and intended effect, the target claim marked authoritative, and items that must survive because a named citer relies on them. Other items bind only the run: local review findings to address, available evidence, "do not commit". The durable items are not loaded by any later write of the same target.
- The [directive-text rule](../../../instructions/cp-skill-write/SKILL.md#universal-mechanics) requires any document that directs action to open with its intent. For that class of documents, the intended contribution already lives in the artifact itself (Option 2 below).
- A completed note's title, description, and body are its reader-facing account of the realized contribution. For a note with the `title-as-claim` trait ([note type](../../../types/note.md)), the title states the governing claim; the reader update, exclusions, and citer-relied items are not recorded there.
- Frontmatter `type:` is a path to the type spec ([ADR 088](../../adr/088-type-values-are-paths-on-a-two-root-search-path.md)). No field or validated association points to an artifact-specific write brief.
- [Collections and types](../../collections-and-types.md#authoring-composition) states that ordinary writing composes exactly the writing skill, `COLLECTION.md`, and the type spec, and that "no third file joins this composition". Adopting Option 3 or 4 would amend that statement. [ADR 084](../../adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md) places kind rules and location rules; it does not address an artifact-specific commission, so it does not foreclose one.
- [Commonplace doctrine](../../definitions/commonplace-doctrine.md) now defines a handoff as a delta from the standing instruction: purpose, deviations, and deliberately open choices. A write brief is that delta retained past the task. The same definition excludes text that no worker runtime loads, which is why a stored brief needs an operativity path.
- The theory distinguishes a topic from the particular [warranted reader update](../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) around which substantive writing organizes evidence and reasoning.
- `type:` shows the shipped delivery pattern for a per-artifact input: frontmatter names a canonical file by path, the validator checks the pointer, and the writing skill reads the named file ([ADR 018](../../adr/018-types-are-path-references-to-instruction-docs.md)). No frontmatter field names a brief.
- The deterministic write-context assembler is only a proposal. No shipped command currently has a recognized brief input role.
- A pre-registered pilot tested this proposal's conjectures ([evidence note](../../../notes/evidence/full-write-briefs-cut-edit-drift-one-line-briefs-did-not.md)). It ran 95 edit runs on 10 documents, starting from each document's commissioned version. Under pressure edits, writers given the full original brief broke about a third as many unguarded commission items as writers given none. A brief rebuilt afterwards from the commissioned document did nearly as well. A one-sentence brief did no better than none. Writers with a brief did not over-constrain: every override run made the requested change and stated the amendment. Two limits apply. The rebuilt-brief and one-line verdicts rest on excluding two question runs, a reading chosen after unblinding. The pilot tested preservation through later edits, not new-note writing.
- The same pilot traced the ten documents from their commissioned versions to 2026-09-26. Of 350 realized commission items, 83 had been weakened or removed. 47 of those losses were recorded, usually in a record that named the overall rewrite but not the items it dropped, and 36 were not. Some recorded losses were deliberate reframings, where an unamended brief would now be stale.

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

A brief directs later writers, so it is directive text and the writing skill's existing [directive-text rule](../../../instructions/cp-skill-write/SKILL.md#universal-mechanics) already sets its form: intent first (the governing claim or purpose and the reader update), then the boundaries every route must respect (must-keep constraints and exclusions), with the means left to the writer. No separate brief format is needed. The same split suggests when a brief earns its keep: when the commission has boundaries a later writer cannot infer. A commission that is only intent may be fully carried by the title and a sentence of body text.

## Options

### 1. Keep intent transient or reconstruct it from the artifact

Ordinary writing continues to use the live request and incumbent. An experimental writing procedure may create temporary task-specific scaffolding, but no retained artifact-specific input enters the ordinary path.

**Operativity path:** current skills remain the only consumers. User intent reaches the writer through the invocation context; incumbent content reaches it through the target read. Nothing persists as an independent per-artifact instruction.

This is the smallest system and avoids shadow intent. It cannot distinguish a later drift from an intentional change when the original commission is no longer present.

### 2. Put the intended contribution in the artifact itself

The artifact carries an explicit reader-facing purpose, contribution, or scope statement in its frontmatter or body. Later writers recover the angle by reading the artifact, and readers see the same declaration.

**Operativity path:** the type or collection contract authorizes the representation; writing and review procedures read it as part of the artifact. If structural, validation can require or constrain it.

This maximizes self-sufficiency and avoids a sidecar association. It does not preserve an independent commission against which the incumbent can be evaluated, and procedural details or rejected alternatives may burden readers.

### 3. Allow an optional durable write brief

Selected eligible artifacts have an associated canonical brief. The writer receives it through one of the delivery routes below, as the retained-intent input that `cp-skill-write` Step 4 already defines, with its authority labelled. It informs ordinary new-note writing and later substantive revision. When the target is itself a write brief, the brief input is inapplicable rather than missing. Absence preserves the current path for other targets.

**Operativity path:** a validated association identifies the brief; the chosen delivery route loads it; writing and revision skills consume it as retained intent. A brief edit affects future writes immediately. If the design later gives brief changes freshness consequences, the review system also marks the target for reconsideration.

This preserves independent intent only where its value exceeds its lifecycle cost. The multistage procedure may consume the same input later if its use shows that it should, but it is not part of this option's initial operativity path.

### 4. Require a durable brief for every substantive artifact

Every eligible type carries a commission before drafting, and later maintenance always loads it. The write-brief role itself remains ineligible, so uniformity does not imply an infinite chain.

**Operativity path:** type and collection contracts require the association; the validator reports an eligible artifact without one; the delivery route loads it for every write; review checks any declared freshness relation.

This makes intended contribution uniformly explicit and reviewable. It adds an artifact, an association, and maintenance obligations even when title, description, request, and body already determine the contribution without ambiguity.

## Delivery routes

Options 3 and 4 need a route by which a writer finds and loads the brief. The route is independent of where the brief lives and what force it has.

### A. Validated pointer read by the writing skill

The association is a path-valued frontmatter field, in the same pattern as `type:`. Either the artifact names its brief or the brief names its target; a pointer on the artifact is found by the read the writer already performs. The validator checks that the pointer resolves to a file of the brief type and that a brief never names a brief. `cp-skill-write` gains one rule: when the target declares a brief, read it as retained intent.

**Operativity path:** the validator enforces the association; the writing skill reads the named file, as it reads the type spec named by `type:`. No new command is needed.

This follows the direct-pointer design ADR 018 chose over a generated packet: agents read ordinary repository files. Its cost grows with the number of consumers, because each writing procedure that should honor a brief needs the same read rule. With one consumer the cost is one rule. In new-write mode the target has no frontmatter yet, so the pointer is written with the new artifact, or the brief carries the target-side pointer until the artifact exists.

### B. Named role in the deterministic assembler

If [deterministic write-context assembly](../deterministic-write-context-assembly.md) is adopted, the brief can be one of its closed, named input roles. The assembler resolves the association, labels authority and provenance, and omits the role for write-brief targets. In new-write mode it may render an explicitly supplied commission or expose the contribution fields that remain unresolved.

**Operativity path:** the coded assembler resolves and injects the brief; writing skills consume the assembled context.

This keeps association mechanics out of every consumer. It is worth its cost when several writing procedures consume the brief, or when the assembler is adopted on its own evidence anyway. It is not a precondition for Route A.

Route A can ship first and move to Route B later without changing the brief or its association: only the reader changes.

## Forces

- **Independent purpose versus self-standing prose.** A brief is useful as a specification only when it remains distinct from the current artifact. The artifact must nevertheless be understandable without loading hidden authoring context.
- **Intent versus warrant.** User direction can select a question and angle. It cannot make factual claims true or establish that the proposed update is worth retaining.
- **Continuity versus staleness.** Durable intent can prevent accidental drift, but audience priors, neighboring notes, and project needs change. A once-distinctive update can become redundant.
- **Optional value versus uniform machinery.** Ambiguous, commissioned, or consequential artifacts benefit most. Many small notes do not need another file.
- **Pre-draft independence.** A brief written or accepted before drafting contains counterfactual information. A brief generated from the finished artifact may only restate it. In the pilot, restating was enough while the artifact still realized its commission: a brief rebuilt from the commissioned version preserved it nearly as well as the original. That result does not transfer to an artifact that has since drifted, because a brief rebuilt from it would encode the drift.
- **Boundaries versus summary.** The pilot's one-sentence briefs carried the governing claim, which writers kept anyway, and lost the must-keep and exclusion items, which is where edits drifted. A brief that only restates purpose adds little over a claim-bearing title.
- **Authority and precedence.** Artifact-specific intent may narrow the collection default but cannot silently override collection, type, linking, or validation requirements.
- **Association lifecycle.** New targets do not yet have frontmatter; renames, moves, retirement, splits, and merges must preserve or deliberately revise any relation.
- **Context cost.** A compact commission can spare reconstruction. An accreted history, outline, source dump, or critique packet would compete with the writing itself.
- **Experimental precedent.** The multistage briefs suggest useful separations, but copying their whole lifecycle into ordinary writing would turn a workshop procedure into architecture by accident. Their run-bound items (review findings, evidence lists, commit instructions) would be stale in a durable brief.
- **Pointer simplicity versus consumer multiplication.** A pointer read by one skill is the cheapest operative path and matches the shipped `type:` design. Each additional consumer repeats the read rule, which is the cost a coded assembler removes.
- **One writer versus terminating context.** Briefs should benefit from the ordinary collection and type machinery. They should not recursively require the same artifact-specific role they provide to another target.

## Free choices

- Where the brief lives and which side declares the association. A direct path is explicit; a naming convention is cheaper but makes discovery and rename behavior implicit, and neither delivery route accepts it.
- Which delivery route ships first. Route A needs no new code; Route B is available only if the assembler is adopted.
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

- One delivery route is chosen. Under Route A, the association is a validated path pointer and the writing skill reads only the file it names. Under Route B, the [deterministic write-context assembler](../deterministic-write-context-assembly.md) is adopted first or in the same decision, with a closed recognized role for the brief. Under either, no writing skill gains a target-adjacent search rule.
- An ordinary-writing pilot shows that a new-note writer can preserve explicit task-fixed intent and that later writers preserve or deliberately revise the governing contribution better than from the incumbent and task context alone. The later-writer half has pilot evidence (see Current state); the new-note half is untested.
- The brief records an intended reader update, scope, and fixed decisions without duplicating the artifact's claims, evidence, outline, or prose.
- The finished artifact remains self-standing: a reader can recover its realized contribution without opening the brief.
- A brief is independently authored or explicitly accepted; automatic retrospective summaries do not acquire intent authority.
- Absence is valid for artifacts whose contribution is already determined. Optionality does not create warnings or fictional missing state.
- Association, rename, move, split, merge, retirement, and orphan behavior are explicit and testable before durable briefs become common.
- The design states whether a brief edit merely affects the next write or stales the target for review. Binding force is not implied by the word `brief`.
- Collection and type contracts remain stronger constraints, while a live user decision can explicitly amend the commission rather than being treated as a conflict to hide.
- Context limits prevent a brief from becoming an accumulated authoring history or evidence bundle.
- Adoption does not depend on the multistage skill, and does not silently import its workshop or agent-stage machinery into ordinary writing.
- The ordinary writing skill authors briefs without a separate procedure. For a write-brief target, the brief input is deterministically omitted: the validator rejects a brief that names a brief (Route A), or the assembler omits the role and fails clearly on a malformed cycle (Route B).

## Risks

- **Shadow specification.** Writers may optimize for hidden intent while the published artifact no longer communicates why it exists.
- **Double truth.** Brief and artifact can disagree about the governing claim, audience, or scope with no obvious current authority.
- **Retrospective laundering.** Generating a brief from the incumbent can convert accidental content into apparently deliberate purpose.
- **Overconstraint.** Detailed structure or prose instructions can freeze choices a later writer should make from current evidence.
- **File multiplication.** Optional sidecars can become a customary requirement and enlarge navigation, validation, and retirement work.
- **Stale interestingness.** The intended update can cease to be nontrivial relative to the current KB while the brief continues to demand its preservation.
- **Instruction injection.** An unvalidated adjacent file could acquire behavioral authority merely by matching a lookup convention.
- **Lookup drift.** If skills learn to find briefs by proximity or naming rather than through the declared pointer or assembler role, each consumer grows its own discovery rule and ordinary files acquire behavioral authority by placement.
- **Commission regress.** If every written artifact is assumed to need a brief, the brief becomes another target needing another brief and the model has no principled stopping point.

---

Relevant Notes:

- [Warranted reader update is the objective of substantive writing](../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) — rests-on: the brief preserves the proposed audience-relative update around which evidence and reasoning should be organized
- [A bare writing prompt does not determine its intended contribution](../../../notes/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) — rests-on: topic and form leave materially different commissions open
- [An author should fix what the executor cannot determine, not what it will](../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — rests-on: the brief should retain authorial purpose and exclusions without prescribing live writing choices
- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: retaining a commission helps only when the writing path reliably loads it
- [Deterministic write-context assembly](../deterministic-write-context-assembly.md) — see-also: the proposal that would supply delivery Route B as a named assembler role
- [ADR 018: Types are path references to instruction docs](../../adr/018-types-are-path-references-to-instruction-docs.md) — compares-with: the shipped direct-pointer design that delivery Route A reuses
- [cp-skill-write](../../../instructions/cp-skill-write/SKILL.md) — procedure: the current contribution-resolution step a durable brief would inform
- [cp-skill-write-multistage](../../../instructions/cp-skill-write-multistage/SKILL.md) — see-also: a workshop procedure whose temporary brief suggests a possible separation without setting this proposal's architecture
