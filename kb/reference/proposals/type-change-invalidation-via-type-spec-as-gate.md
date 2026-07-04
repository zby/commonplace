---
description: "Proposal: make the type spec the gate of a per-note conformance review pair — type edits invalidate the cohort via existing gate-changed freshness; new dependencies become factored two-input pairs"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance, observability]
status: seedling
---

# Type-change invalidation via type-spec-as-gate

A note's type binds it twice: structurally through the schema, which the deterministic validator checks, and semantically through the [type spec](../../types/type-spec.md)'s authoring instructions, which nothing checks — the type-spec contract itself says the validator inspects only frontmatter and the declared schema. The semantic half is also the half that goes silently wrong when a type changes: edit a type's authoring bar and every note of that type may no longer do what its contract asks, with no mechanism that notices.

The check cannot be written as an ordinary review gate. A gate that restates the type contract is a compiled copy that drifts — [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). A gate that instead leans on the type spec silently carries a dependency freshness never hashes: review freshness compares exactly two snapshots, note text and gate text, so a type edit changes neither and every acceptance stays falsely fresh. The resolution is to stop treating the type contract as an input to some other gate and make it the gate: for each note, one *type-conformance pair* `(note_path, type_spec_path)` whose gate side is the note's own type spec.

## Current state (as of 2026-07-03)

- Freshness compares two hashes per pair. `review_target_selector.py` hashes the current note and gate files against `accepted_note_hash` / `accepted_gate_hash` pinned in the acceptance row ([ADR 032](../adr/032-review-freshness-uses-db-snapshots-not-git.md)). The snapshot table (`review_file_snapshots`) is role-neutral — keyed by path and content hash, storing full text — so `snapshot_file` works on any repo path, type specs included.
- Acknowledgement already absorbs gate-side edits: `ack_pairs` (behind `commonplace-ack-gate-review`) re-pins the *current* note and gate snapshots while carrying forward completed review evidence. Nothing restricts it to note-changed pairs.
- Gate resolution is catalog-rooted: `resolve_gates.py` lists gates under `kb/instructions/review-gates/` and filters applicability by `requires-type` / `requires_trait` read from gate frontmatter. It reads the note's type *path* for filtering, never type-spec *content*.
- `requires-type` gates inline their tests. `semantic/explication-quality` (requires `kb/types/definition.md`) carries Carnap's four explication criteria in its own body; it cites "the definition instructions" but the operative test is the gate's own hashed text. The type-contract dependency of existing gates is authoring-time consistency, not a runtime input.
- No gate reviews semantic conformance to the type contract; the review prompt injects note text and gate text only.
- The prompt scaffolding around the embedded texts — the runner system prompt and the rendered reading-scope and output-contract sections in `protocol/prompt.py` — is outside the freshness hash for every existing pair. Only the embedded note and gate texts are hashed; editing the scaffolding invalidates nothing.
- The architecture doc already anticipates freshness widening to an "effective review-contract hash" if the review contract grows beyond a single gate file (see [review architecture](../review-architecture.md), freshness mechanism).

## The design: the type spec is the gate

Derive, for each note, one type-conformance pair whose gate path is the type-spec `.md` named by the note's `type:` frontmatter. Everything downstream of pair derivation is the existing machinery, unchanged:

- **Invalidation matches exactly.** A type edit flips the gate hash for precisely the pairs whose gate is that type spec — the cohort of notes of that type — via the existing `gate-changed` reason. A note edit flips `note-changed`. No new selector reason, no new acceptance semantics.
- **Trivial type edits ack today.** Acking a type-spec-stale pair re-pins the current type-spec snapshot because the type spec *is* the gate snapshot. The operator judges triviality from the gate-side diff the same way as for any gate edit. (The rejected alternative — watching the type spec as a third input on other gates' pairs — required a third acceptance column, taught ack a new input, and left the whole trivial-ack path to be rebuilt.)
- **Acceptance identity, model partitions, warn selection, finalization**: untouched. The pair is an ordinary `(note_path, gate_path, model_partition)` key whose gate path happens to live in `kb/types/`.

New code is confined to the selection/prompt edge:

- **A second gate source.** Type-conformance pairs are derived from note frontmatter, not from catalog listing plus `requires-type` filtering. The resolver currently rejects ids escaping the gate catalog, so type specs enter as a distinct source with a stable id (e.g. a virtual `type/{name}` lens mapping to the type-spec path); the persisted gate identity is the type-spec repo path either way.
- **A conformance prompt shape.** Type specs are authoring instructions plus a template, not a Failure mode / Test procedure. Either a generic wrapper renders them ("does this note do what these authoring instructions ask? decide PASS/WARN/FAIL"), or type specs grow an authored review section. The wrapper is the cheap first cut.

## Existing gates stay self-contained

Type-as-gate works only if other gates do not *also* depend on unhashed type-contract text. Inspection says they already don't — the operative test is inlined — and this should be promoted from accident to authoring rule: a gate's test must be self-contained; if it needs contract language, it quotes it, converting the dependency into hashed gate text. When the type contract moves and a gate is edited to track it, `gate-changed` fires through the same path — correct invalidation with no extra mechanism. The type-conformance pair owns "does the note satisfy the contract"; type-scoped gates own their sharper, named failure modes; the two must state their boundary in gate text as adjacent gates already do, to avoid double-flagging one defect.

## The freshness boundary: what stays unhashed

Even with the type spec on the gate side, three prose layers shape a conformance judgment and only two are hashed: the note, the type spec, and the wrapper prompt that tells the reviewer how to apply authoring instructions as a gate. The wrapper joins scaffolding that is already outside freshness for every pair today, and beneath all of it sits the symbolic layer — the code assembling the prompts — equally unhashed. The truly thorough model would hash the *effective review contract*: embedded inputs plus scaffolding plus assembler version; the architecture doc names this widening. This proposal accepts the limitation and bounds it instead of closing it:

- **Why it is acceptable.** Scaffolding and assembler are shared by every pair and versioned in git. A change there is a system upgrade that shifts *all* judgments uniformly, so the correct response is a deliberate corpus-wide decision at upgrade time — a re-review sweep or a mass ack — not per-pair hash tracking, which would add cost without changing that decision.
- **The rule that keeps the bound real.** Judgment-bearing prose lives in hashed inputs; the unhashed layers stay mechanical. The wrapper may say how to emit a verdict, never what a good note of the type looks like — criteria belong in the type spec, where the hash sees them. A criterion that migrates into scaffolding silently exits freshness, reintroducing the false-fresh failure this proposal exists to remove.
- **The boundary must be visible in the code.** The prompt-assembly and freshness modules carry comments stating that scaffolding edits do not invalidate acceptances and that review criteria must not move into scaffolding, so future changes stay compatible with this direction rather than eroding it edit by edit.

This also settles the wrapper-vs-authored-review-section choice directionally: the moment conformance criteria need sharpening, they go into an authored `## Review` section of the type spec — hashed — not into a richer wrapper.

## Planning: factor dependencies into pairs, not inputs

The generalized shape behind this is still [make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — an accepted review as a build product, its inputs as prerequisites. But type-as-gate reveals the cheaper generalization: before widening one pair's input set to N, factor each dependency into its own two-input pair where the dependency document is the gate side.

- `COLLECTION.md`-as-gate: a note's conformance to its collection's register and conventions.
- Source-as-gate: a derived note's consistency with the source snapshot it distills — the multi-source invalidation case, one pair per `(note, source)` edge.

Each factored pair reuses the entire freshness/ack/warn stack, and each dependency invalidates independently with its own diff. The N-ary input-set design — acceptance pinning a variable set of `(input_key, role, resolver, accepted_version)` records — remains the fallback for a judgment that irreducibly reads three or more texts in one prompt; no such judgment is identified yet, which is exactly why the input-set table stays unbuilt. A fuller design for that general model — lineage targets, append-only events, per-event input versions, typed resolvers — is in flight in the workshop layer at `kb/work/lineage-mechanisms/general-lineage-refresh-state-design.md` (cited by path, not linked, per the no-workshop-links convention); factoring-into-pairs narrows how much of it review freshness will ever need.

The forces that keep even the factored pairs at planning: cohort blast radius (a `COLLECTION.md` edit stales a whole collection — same shape as a wide gate edit, so the answer is a cohort-scoped ack surface, an improvement to the existing ack command rather than new freshness semantics) and review cost (every factored dependency adds a pair per note; the corpus-times-dependencies product is real).

## Free choices

- **Gate id scheme.** A virtual `type/{name}` lens keeps the CLI uniform with `{lens}/{name}` ids; using the raw repo path is more literal. Persisted identity should be the type-spec path regardless — acceptance is path-keyed.
- **Wrapper prompt vs authored review section.** The wrapper needs no type-spec changes but reviews against prose not written as a test; an authored `## Review` section per type spec sharpens the check at the cost of every type spec growing reviewer-facing prose that must itself stay consistent. The freshness boundary weighs in for the section: it is hashed, the wrapper is not.
- **Universal or opt-in cohort.** Start opt-in with types whose authoring instructions carry real semantic bars (`definition`, `tag-readme`), or derive a pair for every typed note from day one. Opt-in keeps early review cost proportional to value.
- **Schema participation.** None: structural conformance to `.schema.yaml` is the validator's job; the conformance pair reviews the type-spec `.md` only.

## Adoption criteria

Adopt when a type-contract edit first requires re-judging its cohort, or when the missing semantic conformance check is first wanted — the cut is a gate source plus a prompt wrapper, with no storage change, so the threshold is low. Adopt a cohort-scoped ack (by type or fed from selector JSON) when the first real type edit stales more pairs than per-note acking comfortably clears. Adopt the N-ary input-set model only if a judgment appears that genuinely needs a third text in one prompt; the default answer to a new dependency is a new factored pair, not a wider input set.

## Risks

- **Self-containment is a discipline, not an enforcement.** Nothing stops a future gate from leaning on unhashed contract text; the guard is the review-gate authoring rule, and possibly a gate on gates. A gate that drifts into hidden dependency reintroduces exactly the false-fresh failure this proposal removes.
- **Conformance reviews may be vague.** Authoring instructions state what to do, not how to judge; until a type spec carries a review section, the wrapper-prompted reviewer sets its own bar, and cross-model consistency may be poor. Model partitioning contains this but does not fix it.
- **Double-flagging.** The conformance pair and type-scoped gates overlap (a definition failing explication also fails its contract); boundary statements in gate text are the existing tool, and they must be written when the conformance pair lands.

---

Relevant Notes:

- [link graph plus timestamps enables make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — rationale: the build-product/prerequisite model; factored two-input pairs are its cheapest review-side realization
- [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why the gate must be the type spec rather than restate it; an unchecked copy of the contract drifts
- [review system](../README-REVIEW-SYSTEM.md) — part-of: the freshness, acceptance, and ack concepts the conformance pair reuses unchanged
- [032-review freshness uses DB snapshots, not Git](../adr/032-review-freshness-uses-db-snapshots-not-git.md) — see-also: the role-neutral snapshot substrate that lets a type spec sit on the gate side without schema change
- [012-types for structure, traits for review](../adr/012-types-for-structure-traits-for-review.md) — see-also: the type/trait boundary this proposal extends into review, making the type contract itself reviewable
