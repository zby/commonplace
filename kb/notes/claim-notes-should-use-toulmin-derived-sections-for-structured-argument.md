---
description: Three independent threads converged on Toulmin's argument structure — adopting Toulmin sections as base type `structured-claim` separates claim-titled notes (any note) from fully argued claims (the type)
type: structured-claim
traits: [has-comparison, has-external-sources]
areas: [document-system]
status: current
---

# Claim notes should use Toulmin-derived sections for structured argument

Claw conventions independently converged on [Toulmin's argumentation model](../sources/purdue-owl-toulmin-argument.md) without naming it. Adopting Toulmin's vocabulary as a new base type `structured-claim` makes the distinction explicit: any note can have a claim title (the title-as-claim convention), but only a `structured-claim` commits to the full argument scaffold.

## Evidence

Three independent threads arrived at the same shape:

1. **Claim titles.** [Title-as-claim](./title-as-claim-enables-traversal-as-reasoning.md) makes the title a Toulmin claim. Link semantics using "since" and "because" encode warrants — the assumptions connecting evidence to claim.

2. **Thalo's opinion entity.** The [Thalo type comparison](../notes/related-systems/thalo-type-comparison.md) already flagged that their opinion entity (Claim / Reasoning / Caveats sections) maps to Toulmin's claim / grounds+warrant / qualifier+rebuttal — and that we lack structured sections for argument-shaped notes.

3. **The affordance table.** [Types mark affordances](../notes/instructions-are-typed-callables.md) lists `claim` affordances as: verify, gather evidence, challenge, use as assumption. These are Toulmin operations: verifying grounds, strengthening backing, raising rebuttals.

4. **Distribution.** 30 of 62 notes (48%) currently carry `has-claim`. That's not a trait — it's the dominant document shape, which argues for a base type.

## Reasoning

The convergence isn't coincidence — Toulmin describes the structure of practical argument, and claim notes *are* practical arguments. The claim is in the title, the grounds are scattered in prose, the warrant is usually implicit, qualifiers are absent or buried. The notes already have Toulmin anatomy; they just lack the skeleton.

Making the skeleton explicit — required sections with Toulmin-derived names — converts the informal claim convention into a structural contract: deterministic section checks verify the scaffold, bounded semantic checks verify the content within each section. This is the [stabilisation pattern](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) applied to the type system.

### Why a base type, not a trait

The `has-claim` trait was always doing the job of a type. Traits mark properties a document *has* — a comparison table, external sources, code sketches. But Toulmin sections define the *entire document's shape*, not a property within it. A note with `## Evidence`, `## Reasoning`, and `## Caveats` isn't a note that happens to contain a claim — it *is* a structured claim. That's what base types are for.

### Why `structured-claim`, not `claim`

The word "claim" already has a meaning in the KB: title-as-claim means "the title makes an assertion." If the type were called `claim`, an LLM reading "titles should be claims" would infer every note needs `type: claim`. The name `structured-claim` makes the distinction self-documenting:

- **claim** (lowercase, informal) — a title that makes an assertion. Any note can have one. This is the title-as-claim convention.
- **`structured-claim`** (base type) — a note with full Toulmin sections. Only for developed arguments.

Most claims don't need the structure — only the ones worth structuring do.

### The promotion path

A note with a claim title starts as `type: note`. When the argument matures — evidence accumulates, reasoning gets explicit — it gets promoted to `type: structured-claim`. The remaining notes keep `type: note` with their claim-ish titles, honest about their level of development. Of the current 30 `has-claim` notes, perhaps 5-10 are developed enough for `type: structured-claim` today.

### Evidence vs Reasoning (from Toulmin)

The key insight from Toulmin that a simple Reasoning/Caveats split misses: **evidence and warrant are different things.** Evidence is checkable fact ("we observed X", "the code shows Y"). Warrant is the principle connecting evidence to claim ("because systems that do X tend to Y"). Separating them makes verification modular:

1. Are the evidence claims accurate? (checkable against sources)
2. Does the warrant actually connect this evidence to this claim? (bounded logical judgment)
3. Are the caveats reasonable? (completeness check)

## Section template for `type: structured-claim`

```markdown
---
type: structured-claim
---
# [Claim as title]

[Opening paragraph — claim stated as full sentence with context]

## Evidence

Observations, facts, references. Checkable.
(Toulmin: grounds)

## Reasoning

The principle connecting evidence to claim. Why does
this evidence imply this claim?
(Toulmin: warrant + backing)

## Caveats

- Scope limits (Toulmin: qualifier)
- Assumptions that must hold
- Counterarguments and responses (Toulmin: rebuttal)
```

**What gets merged vs kept separate:**

| Toulmin component | Our section | Rationale |
|-------------------|-------------|-----------|
| Claim | Title + opening paragraph | Already established convention |
| Grounds | `## Evidence` | Checkable facts, separated from reasoning |
| Warrant + Backing | `## Reasoning` | Both answer "why does evidence imply claim?" — the distinction between principle and support-for-principle is too fine-grained for KB notes |
| Qualifier + Rebuttal | `## Caveats` | Both answer "when does this not hold?" — bullets distinguish scope limits, assumptions, and counterarguments naturally |

**Deterministic checks enabled:**

- `type: structured-claim` → file must contain `## Evidence` and `## Reasoning` headings
- Optional: `## Caveats`
- Opening paragraph exists (first non-heading content after title)

**Semantic checks narrowed:**

- Does Evidence contain verifiable observations, not opinions disguised as facts?
- Does Reasoning connect the evidence to the title claim?
- Are obvious objections addressed in Caveats?

Each of these is a bounded judgment within a known section, not an open-ended document read.

## What happens to `has-claim`

The `has-claim` trait is retired. The 30 notes currently carrying it split into:

- **`type: structured-claim`** — notes with developed arguments that can fill Evidence/Reasoning/Caveats sections (estimated 5-10 today)
- **`type: note`** — notes with claim-like titles but free-form bodies. The title-as-claim convention still applies; they just don't commit to the Toulmin scaffold.

The other traits (`has-comparison`, `has-implementation`, `has-external-sources`) remain as traits — they describe properties within a document, not its overall shape. A `structured-claim` can still carry `traits: [has-comparison]` if it uses a comparison table as evidence.

## Caveats

- **Warrant is often implicit.** Toulmin acknowledges warrants are frequently unstated. Forcing authors to articulate them is the point — but it adds friction. The bet is that explicit warrants produce more trustworthy claims, worth the cost.
- **Migration effort.** Retiring `has-claim` means updating 30 notes. Most just drop the trait; a few get promoted. This should be a gradual process, not a batch migration.
- **New type in the enum.** `structured-claim` joins `note`, `spec`, `review`, `index`, `adr` in [document-classification](./document-classification.md). The validation skill and any scripts checking type enums need updating.

---

Relevant Notes:
- [title-as-claim-enables-traversal-as-reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — foundation: claim titles are Toulmin claims; `structured-claim` extends the convention with required argument sections while leaving the title convention available to all notes
- [Thalo type comparison](../notes/related-systems/thalo-type-comparison.md) — converges: Thalo's opinion entity (Claim/Reasoning/Caveats) is the same Toulmin shape; this note resolves the gap they flagged
- [programming-language types mark affordances](../notes/instructions-are-typed-callables.md) — foundation: the `claim` affordance table lists Toulmin operations without naming them
- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — enables: `structured-claim` has concrete structural requirements (sections), making it verifiable in the way `has-claim` as a trait was not
- [document-classification](./document-classification.md) — extends: `structured-claim` becomes a new base type alongside note, spec, review, index, adr
- [deterministic validation should be a script](../notes/deterministic-validation-should-be-a-script.md) — enables: the section-presence checks are hard-oracle, movable to a script
- [three distinct mechanisms](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) — foundation: the note → structured-claim promotion path is the verifiability gradient applied to the type system
- [Toulmin Argument (Purdue OWL)](../sources/purdue-owl-toulmin-argument.md) — source: the canonical framework this note adapts

Topics:
- [document-system](./document-system.md)
