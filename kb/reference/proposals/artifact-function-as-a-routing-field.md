---
description: "Proposal: whether an artifact_function declaration should expose a document's intended whole-artifact job for writing and review routing without asserting atomicity"
type: ../types/design-proposal.md
tags: [context-engineering, kb-maintenance, type-system]
---

# Artifact function as a routing field

General writing and review procedures need to know what job an artifact performs as a whole. A theory note advances an argument, a reference document describes a shipped system, an ADR records a decision, an instruction directs behavior, and an article builds a self-standing explanation. All of them can contain claims that need checking. They should not all receive the artifact-level methods appropriate to an atomic claim note.

This proposal asks whether Commonplace should introduce an `artifact_function` declaration and how a procedure should resolve that function when no declaration is present. It does not add the field, choose its carrier, or make a per-artifact writing companion mandatory.

## Current state (as of 2026-08-22)

- Frontmatter `type:` identifies the artifact's type contract. Types carry structural and semantic expectations; explicit traits add independently checkable review expectations. The review selector can currently narrow a catalog gate by type or trait, but not by a separate artifact-function axis.
- A type spec wholly owns the semantics of its frontmatter fields. A collection supplies register, quality goal, title and description conventions, lifecycle, and link grammar; it cannot redefine what the same field value means in different directories.
- Specialized types already imply some whole-artifact jobs. An ADR records a decision, an instruction directs behavior, a definition pins a term, and a design proposal preserves an undecided design surface. The general `note` type does not determine one function.
- Collection placement is informative but not decisive. `kb/notes/` defaults toward composable theory claims while admitting synthesis notes; `kb/reference/` contains both bounded system accounts and composite architecture descriptions; `kb/articles/` admits self-standing, multi-claim exposition.
- [`run-full-improvement-pass-on-note`](../../instructions/run-full-improvement-pass-on-note.md) checks collection and type fit during synthesis, after several methods have already treated one central claim as the target's identity. Its packet records one `Update` sentence, and its compression, critique, split, reframe, merge, and delete logic mostly fit the `claim + atomic` case.
- Local semantic gates can inspect assertions inside any artifact. Their applicability does not imply that the artifact itself is one claim.
- No shipped field or resolver records a target's artifact function. No durable per-artifact write brief is currently loaded. Both [per-artifact write briefs](./per-artifact-write-briefs.md) and [deterministic write-context assembly](./deterministic-write-context-assembly.md) remain proposals.

## Problem

Without an explicit function axis, a general procedure has three poor defaults. It can infer the function independently on every run, hard-code a growing cross-product of collection and type cases, or apply the method developed for the most common artifact. The current full pass takes the third path in much of its editorial core: the presence of claims becomes a reason to search for one central claim, and finding several claims becomes pressure to split.

Adding `claim`, `description`, `decision`, `procedure`, and `exposition` as new types would make the distinction queryable, but these labels do not necessarily determine structure. It would also force false choices for artifacts that retain a structural type while serving a different semantic job. A reference note and a theory note can share the base `note` structure while requiring different artifact-level evaluation; an article can contain an argument without ceasing to be exposition.

A separate field creates its own risks. It may duplicate a function already entailed by a specialized type, drift away from the body, or turn an uncertain classification into apparently authoritative metadata. Putting the field only in a writing companion avoids burdening reader-facing frontmatter, but would either make the optional companion a hidden prerequisite or leave most artifacts without the routing signal. Requiring a companion in order to generalize a procedure would reverse the companion proposal's optional boundary.

The design must therefore separate four things that are currently easy to collapse:

| Axis | Question it answers | Current or proposed carrier |
|---|---|---|
| Collection | Under which register, quality goal, lifecycle, and link grammar is this artifact maintained? | Path plus `COLLECTION.md` |
| Type | Which structural and semantic artifact contract applies? | `type:` |
| Traits | Which independently checkable review expectations apply? | `traits:` |
| Artifact function | What primary whole-artifact job should guide artifact-level writing and review? | Proposed `artifact_function` declaration or resolved value |
| Composition shape | Does the artifact preserve one primary contribution or several contributions and their relations? | Not yet represented; must remain independent of function |

## Proposed boundary

`artifact_function`, if adopted, would assert the intended primary job of the artifact as a whole. It would select and interpret artifact-level methods: what counts as fidelity, what identity a duplicate must share, what a split must preserve, and what kind of failure could justify reframe, merge, rehome, or deletion.

The declaration would not assert that the body currently fulfills that job. A reviewer could find a mismatch between the declared function and the realized artifact. It would also not:

- enumerate every rhetorical move or truth-apt assertion in the text;
- supply evidence for any claim;
- replace collection or type conformance;
- encode lifecycle, maturity, authority, topic, or intended audience;
- imply that the artifact is atomic; or
- exempt claims inside descriptions, procedures, decisions, or exposition from local semantic review.

The motivating function vocabulary is `claim`, `description`, `decision`, `procedure`, and `exposition`. Existing definitions and design proposals also test whether `definition` and `design` deserve distinct values or are specializations of another function. These are candidate distinctions, not yet an enum. A value earns admission only when at least one consumer behaves differently because of it.

Function and composition shape form a cross-product rather than a hierarchy. The following are illustrative classifications, not proposed defaults:

| Artifact | Possible artifact function | Possible composition shape |
|---|---|---|
| Ordinary theory note | `claim` | atomic |
| Synthesis note | `claim` or a separately named argumentative function | composite |
| Bounded reference invariant | `description` | atomic |
| Architecture overview | `description` | composite |
| ADR | `decision` | atomic around one adopted choice |
| Instruction | `procedure` | atomic around one outcome or composite across independently usable procedures |
| Technical article | `exposition` | atomic or composite |

A generalized procedure should consume a **resolved artifact function**, not assume that a raw field is present. Resolution must preserve provenance: declared on the artifact, implied by an exact type, supplied as retained intent by an optional companion, inferred from authorized context, or left undetermined. An undetermined function is a valid report state. A mutating procedure that cannot safely select an artifact-level method should abstain rather than manufacture a declaration.

Any persisted field must have one global, type-owned meaning. A collection may supply evidence or a default used during resolution, but it cannot redefine `description` or any other value. A declared function that contradicts a specialized type is a conflict to diagnose, not an override rule to apply silently.

## Options

### 1. Resolve function transiently from existing inputs

A shared preflight derives the function from type, collection, traits, local framing, artifact text, and current user direction. It records a value and provenance for the current operation but persists no new field.

**Operativity path:** no resolver currently exists; one must be built or specified in each consuming procedure. The generalized full pass would use the result to select artifact-level adapters. Catalog review would need either its own deterministic mapping or function-specific gates would remain outside selector routing.

This avoids metadata drift and redundant declarations. Repeated judgment can produce different classifications for identical bytes, and an inferred value has no durable authorial force.

### 2. Encode function through existing types or traits

Specialized types continue to imply functions, while generic artifacts gain function-specific types or traits. The review selector can route trait- or type-specific gates through its existing applicability fields.

**Operativity path:** type specs or the trait vocabulary become the binding declarations; validation and conformance review inspect them; writing and full-pass procedures map them to their artifact-level methods. Existing selector support makes catalog-gate routing partly operative, but no current mapping governs the direct compression, critique, connection, and disposition stages.

This reuses shipped machinery. New types would violate the structural boundary where function changes no required shape, while traits would mix a primary classification axis with independently composable review expectations and would not by themselves define conflict or fallback behavior.

### 3. Allow an optional field on the artifact

An eligible artifact may declare `artifact_function` in its own frontmatter when type and other stable signals do not determine the intended job. Specialized types may imply a value without requiring a duplicate declaration. A resolver supplies one normalized result to procedures and reports how it was obtained.

**Operativity path:** a shared type contract defines the field's semantics and validation surface. Writing and revision procedures preserve or deliberately change the declaration; review selection may gain function applicability; the generalized full pass resolves the field before method selection. Because the declaration is part of the target bytes, changing it participates in ordinary artifact snapshot freshness, though resolver rules and type-implied mappings still need their own change semantics.

This makes exceptional ambiguity explicit without requiring a sidecar for every artifact. It leaves a design choice about whether absence means “derive,” “not applicable,” or “undetermined,” and it can duplicate information already fixed by type.

### 4. Put the field in an optional per-artifact write brief

Where a durable write brief exists, it may declare the intended function as part of the artifact-specific commission. Targets without a brief continue through type-based or transient resolution.

**Operativity path:** this option depends on adopting both the write-brief relation and deterministic context assembly. The assembler would load the declaration with intent-authoritative provenance, and writing procedures would consume it. Review and full-pass routing could not safely depend on it until the brief becomes a captured freshness and mutation-guard dependency.

This keeps authoring intent outside reader-facing content and makes the field one part of a broader companion that may also contain free-form prose. It cannot be the only routing source without making the companion effectively mandatory. It also raises a semantic question: an intended function in a commission and a function asserted by the artifact may need different names or force even if they use the same vocabulary.

### 5. Require the field on every eligible artifact

Every substantive typed artifact declares its function directly. Implicit text either remains outside the axis or must be promoted before function-routed procedures can mutate it.

**Operativity path:** shared schemas require the field; writers must set it; validators reject omission; review selection and generalized procedures may rely on it without inference. Existing artifacts require migration, and specialized types need a rule for redundant or contradictory declarations.

This maximizes queryability and makes routing deterministic from artifact bytes. It charges every artifact for a distinction that is often already obvious, turns classification uncertainty into a structural failure, and creates a second statement of facts already fixed by specialized types.

## Forces

- **Artifact-level routing versus local claim review.** Function should change whole-artifact methods while leaving assertion-level checks available everywhere.
- **Function versus composition.** The field is useful only if `claim` does not silently mean atomic and `exposition` does not silently mean composite.
- **Declared intent versus realized content.** A field can state what the artifact is meant to do; it cannot prove that the body succeeds. Procedures need to know whether they are repairing toward an intention or classifying the incumbent.
- **Stable authorial choice versus repeatable derivation.** Persisting a choice can prevent classification drift. Persisting a value that type or code can recompute creates a stale cache.
- **Global meaning versus collection evidence.** Local collection contracts are strong routing inputs, but allowing them to redefine a frontmatter value would break type self-containment.
- **Queryability versus false precision.** A small controlled vocabulary helps selection and search. Borderline and mixed-function artifacts need an honest unresolved state rather than the nearest convenient label.
- **Optional companions versus universal procedures.** A companion may sharpen intent for exceptional artifacts, but ordinary review and writing must continue when no companion exists.
- **Visible metadata versus hidden authoring context.** Artifact frontmatter travels with the reviewed bytes. A companion keeps reader-facing artifacts lean but introduces association, activation, precedence, and freshness work.
- **Routing force versus oracle warrant.** A function declaration can decide which question is asked; it does not warrant the model judgment that answers that question. Adding function-specific gates must not silently strengthen their enforcement force.
- **Current bytes versus external dependencies.** A direct field changes the artifact snapshot. Type mappings, collection defaults, companion declarations, and resolver versions can change routing without changing those bytes unless the system captures them explicitly.

## Free choices

- Whether `artifact_function` is a single primary value, an ordered list, or a value plus secondary functions. A single value makes routing simple but may falsify legitimately hybrid artifacts.
- Whether `claim` means one proposition, an argumentative whole that may synthesize several claims, or should instead be named `argument`.
- Whether `definition` and `design` are distinct functions, and what behavioral difference justifies each candidate value.
- Whether the declaration describes intended function, realized function, or both through separately named fields. One field should not switch force according to its carrier.
- Which types are eligible to declare the field and which imply a fixed function.
- When type implication and an explicit declaration agree, whether the redundant field is forbidden, permitted, or required. When they disagree, which diagnostic and repair path applies.
- Whether collection and traits may supply deterministic defaults or only evidence for an explicit inference stage.
- Whether inferred values may drive read-only review while mutation requires a declaration or stronger confidence.
- Whether an absent field resolves to an implied value, `undetermined`, or “axis not applicable,” and how those states remain distinguishable.
- Whether catalog gates gain a function-applicability field or function routing remains in a higher-level procedure that requests different gate sets.
- How a resolver's mappings, code version, type contracts, collection contracts, and optional companion inputs participate in review freshness and full-pass mutation guards.
- Whether an artifact's function can change in place or whether some changes imply retyping, rehoming, splitting, or creating a new artifact.

## Adoption criteria

- The field has a globally fixed semantic definition owned by a type contract; no `COLLECTION.md` selects or redefines its truth conditions.
- At least one ordinary writing or review consumer demonstrates a behavior difference that cannot be routed cleanly from current type and trait signals alone.
- Pilots cover an atomic theory note, an atomic reference document or ADR, a composite synthesis note, a composite article, and a procedure. The result preserves local claim checking in every case.
- The consuming procedure resolves composition shape separately and never interprets `artifact_function: claim` as proof that the whole artifact is one atomic claim.
- Resolution has explicit provenance and conflict behavior. `undetermined` is representable, and mutating procedures abstain when the unresolved choice could change the edit or disposition.
- Specialized types do not create unchecked duplicate truth. The design either derives their function, validates an explicit agreement, or makes the declaration canonical and removes the competing implication.
- Absence remains valid wherever existing contracts already determine the function or no function-specific consumer needs it. Optionality does not itself produce a warning.
- A per-artifact write brief remains optional. If it can carry function intent, procedures that require a resolved function still operate without the brief and distinguish companion intent from artifact assertion.
- Every external input that changes method selection or authorizes a mutation is represented in review freshness and in the guarded full-pass packet. Direct artifact bytes are not called the complete dependency set when resolution used more.
- Function-specific gates state their own failure modes and warrant boundaries. The declaration controls applicability, not the verdict or downstream disposition.
- The candidate vocabulary is justified by worked differences in evaluation or repair, not by a desire to classify every document exhaustively.
- Adoption does not require a universal migration until pilots show that required declarations outperform optional resolution for artifacts whose function is already evident.

## Risks

- **Atomic-claim laundering.** Consumers may treat `claim` as permission to force one proposition even when the artifact is an intentional synthesis.
- **Label over body.** A stale or aspirational declaration may cause procedures to optimize for metadata instead of noticing what the artifact actually does.
- **Duplicate truth.** Type, field, trait, collection prior, and companion can each imply a different function with no clear authority.
- **Premature vocabulary.** An early enum can freeze distinctions before cross-collection cases reveal which functions change behavior.
- **Primary-function fiction.** A hybrid artifact may have two equally load-bearing jobs, while a singular field makes one disappear from routing.
- **Companion normalization.** Once a companion is the easiest place to put the field, optional sidecars may become a de facto requirement despite their lifecycle cost.
- **Hidden staleness.** A companion, mapping, or contract edit can change applicable reviews while accepted results remain fresh against unchanged artifact bytes.
- **Inference laundering.** Writing a model-inferred value into frontmatter can make one contestable classification look user-authorized or mechanically established.
- **Routing as enforcement.** A function-specific review may move from problem-noticing to blocking or automatic mutation without independent calibration.
- **Metadata burden.** Required classification adds migration, validation, and maintenance work even where a specialized type already supplies the only plausible answer.

---

Relevant Notes:

- [Document types should be verifiable](../../notes/document-types-should-be-verifiable.md) — rests-on: whole-artifact function should not become a family of types unless each distinction entails a checkable artifact contract
- [The collection–type split is asymmetric: collections never own frontmatter semantics](../collections-never-own-frontmatter-semantics.md) — evidenced-by: any persisted function field must keep one type-owned meaning across collections
- [ADR 012: types for structure, traits for review](../adr/012-types-for-structure-traits-for-review.md) — compares-with: the existing type and trait routing surfaces that a dedicated function axis would supplement or reuse
- [Per-artifact write briefs](./per-artifact-write-briefs.md) — compares-with: the optional companion is one possible carrier for retained function intent but cannot be assumed for every artifact
- [Deterministic write-context assembly](./deterministic-write-context-assembly.md) — see-also: the proposed closed assembly path required if function intent is loaded from a separate artifact
- [Run a full improvement pass on one note](../../instructions/run-full-improvement-pass-on-note.md) — procedure: the first intended consumer whose artifact-level methods currently couple claim function with atomic composition
