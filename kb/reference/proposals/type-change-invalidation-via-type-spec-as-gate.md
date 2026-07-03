---
description: "Proposal: make a note's type-spec a watched review input so type-contract edits invalidate accepted reviews, with planning for a generalized make-like review-input dependency set beyond note and gate"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance, observability]
status: seedling
---

# Type-change invalidation via type-spec-as-gate

Review freshness watches exactly two inputs — the note text and the gate text — but a gate's judgment can rest on a third input it never hashes: the note's [type spec](../../types/type-spec.md). A gate like `semantic/explication-quality` is selected only for `kb/types/definition.md` notes (`requires-type`) and its test leans on what that type contract asks a definition to do. Edit the definition type spec so the authoring bar shifts, and every accepted `explication-quality` review is now judged against a contract that no longer exists — yet the selector reports all of them fresh, because neither the note file nor the gate file changed. This is a false negative of exactly the kind the review system was built to prevent: a stale acceptance silently standing in for a review that would now decide differently.

This proposal has two levels. The adoptable-now level makes the note's type spec a watched review input, reusing the existing `gate-changed` invalidation machinery — *type-spec-as-gate*. The planning level names the generalized shape this is the first instance of: a review pair is a build target whose freshness depends on a *set* of inputs, and note-text and gate-text are merely the first two members.

## Current state (as of 2026-07-03)

Freshness compares three things and nothing else. `review_target_selector.py` computes `file_content_sha256` over the current note file and the current gate file (`current_note_hash`, `current_gate_hash`) and compares them against `accepted_note_hash` and `accepted_gate_hash` pinned in the acceptance row. Two hashes, two files. The `acceptance` table stores exactly these two accepted snapshot references per `(note_path, gate_path, model_partition)` key.

The type spec already participates in review *selection* but not in *freshness*:

- `resolve_gates.py` filters gates by the note's frontmatter `type` against each gate's `requires-type`, so type identity decides which gates run. But it reads the type *path*, never the type-spec *content*.
- Gates declare `watches: [body | frontmatter | ...]` and `staleness: changed | always | ...` — a per-gate statement of which parts of the *note* the gate inspects and when its accepted review goes stale. The vocabulary names note portions only; there is no token for an auxiliary file the gate depends on.
- The review prompt injects the note text and the gate text. It does not inject the type spec, so a reviewer's reliance on the type contract is latent, carried in the gate's own prose rather than passed as data.

The architecture doc already anticipates the widening: freshness "should widen to an effective review-contract hash rather than a leaf gate-file hash" if the review contract ever grows beyond a single gate file (see [review architecture](../review-architecture.md), freshness mechanism). Type-spec dependency is the first concrete pressure to widen it.

The two-hash model was fixed deliberately by [ADR 032](../adr/032-review-freshness-uses-db-snapshots-not-git.md), which moved freshness onto DB-owned content snapshots and off Git. That ADR is the substrate this proposal extends: it already resolves current input versions by content hash, so adding a third hashed input is the same resolver applied to one more file, not a new mechanism.

## The design: type-spec-as-gate (adoptable now)

Treat the note's type spec as a gate-side input. For a `(note, gate)` pair whose gate depends on the type contract, freshness hashes a third file — the type-spec doc named by the note's `type` — and the pair goes stale when that hash drifts, exactly as `gate-changed` fires today. "As-gate" is the whole idea: the type spec behaves like a second document on the gate side of the review, so the existing invalidation path carries it with no new selector reason and no new acceptance semantics.

Two structural sub-choices, cheapest first:

- **Which pairs watch the type spec.** Blanket (every pair hashes its note's type spec) is simplest but over-watches: universal prose gates like `prose/source-residue` do not consult the type contract, so a definition-type-spec edit would needlessly invalidate every prose review of every definition. Gate-scoped is more precise: a gate opts in by extending its `watches` vocabulary — `watches: [body, type-spec]` — declaring that its judgment depends on the note's type contract. `requires-type` gates are the natural opt-in set; they are already type-conditioned.
- **What part of the type spec counts.** The type-spec doc carries authoring prose, a template, and a pointer to a `.schema.yaml`. Structural conformance to the schema is the validator's job, not a reviewer's; a schema change that tightens required sections is caught by `commonplace-validate`, not by a semantic gate. So the review input is the type-spec *markdown* (its authoring instructions and template), and hashing the `.md` file — not the schema — is the right granularity.

Storage is the fork that decides how far this generalizes. The minimal change is a third accepted *snapshot reference* (`accepted_type_spec_snapshot_id`) beside the two existing ones — `review_file_snapshots` is already role-neutral, keyed by path and content hash, so pinning the type spec is the same `snapshot_file` call the note and gate use. A bare hash column would be smaller still, but it forfeits the stored text, and the text is load-bearing twice over: the accepted-vs-current diff is how an operator judges whether a type edit was trivial, and the snapshot is what acknowledgement re-pins. Either flat shape hard-codes "three inputs" the way today's schema hard-codes two — the next input class forces a fourth column. The alternative is to stop storing inputs as fixed columns and store them as rows: an input-set join table keyed by acceptance, one row per watched input with its role, resolver, and accepted version. That is strictly more work now and pays off only when a fourth input appears — which is precisely the level-two question.

**Acknowledgement must advance every watched input.** `ack_pairs` (behind `commonplace-ack-gate-review`) re-pins exactly two snapshots — note and gate. If the type spec becomes a watched input and ack does not also re-snapshot it, acking a type-spec-stale pair is a no-op: the accepted type hash still differs and the pair reports stale again on the next selection. Trivial type edits also break the ack surface's scale assumption: a note edit stales one note's pairs, but one type edit stales the *whole cohort* of that type's watched pairs at once, while the ack command is per-note (`note_path gate_id...`). Before blanket watching is operable, ack needs a cohort-scoped form — by type, or fed from selector JSON — or a typo fix in `kb/types/note.md` means hand-acking every note of the type. The note-side trivial-ack path (`ack_trivial_note_changes.py`) does not transfer: its triviality test normalizes *note portions* against `watches`, and a type-spec change is invisible to it.

## Planning: generalized make-like review-input dependencies

The type spec is not special; it is the first input beyond note-and-gate to earn watching. The general shape is [make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md): a review pair is a build target, its accepted review is the built product, and freshness is the comparison of each declared input's current version against the version present when the product was accepted. `make` rebuilds when any prerequisite is newer than the target; the review selector should restage a review when any watched input's hash differs from its accepted hash. Note-text and gate-text are two prerequisites hard-coded into a two-column schema; type-spec is a third the current schema cannot express without growing a column.

Other inputs are already visible as candidates, which is why the general model matters and a third column does not settle it:

- the collection's `COLLECTION.md` (register and linking conventions a gate may enforce);
- the active vocabulary block in root `AGENTS.md` (gates that check first-mention glossing);
- shared prose conventions a gate cites rather than restates.

Each is a real gate dependency and each would, under a fixed-column scheme, demand its own column. The general design instead makes the input set variable: an acceptance pins a set of `(input_key, role, resolver, accepted_version)` records, freshness resolves each input's current version and compares, and the selector reports *which* input changed. Note, gate, and type-spec become three roles in one uniform mechanism rather than three bespoke code paths. This is the same target/input decomposition the review key already hints at, generalized from two implicit inputs to an explicit dependency set.

The forces that keep this at planning rather than adoption:

- **Over-watching inverts the cost balance.** The make-like note accepts false positives because a redundant review is cheap and a missed one is expensive. That holds for a note editing its own type spec. It does not obviously hold for `AGENTS.md` vocabulary: a one-word convention tweak would restage every review of every note whose gates cite vocabulary — mass invalidation on a routine edit. The general model needs a way to bound blast radius (per-gate opt-in, sub-file watched regions) before broad inputs are safe to watch.
- **Granularity has no natural unit for auxiliary inputs.** The `watches` field sub-selects note portions to suppress trivial-change false positives (`ack_trivial_note_changes.py` reuses this). A type spec or a `COLLECTION.md` has no equally natural "the part this gate depends on" boundary, so watching the whole file is the only cheap option, and the whole file changes more often than the watched slice would.

A fuller design for the generalized model — lineage targets, append-only events, per-event input versions, typed resolvers, and the selector contract — is in flight in the workshop layer at `kb/work/lineage-mechanisms/general-lineage-refresh-state-design.md` (cited by path, not linked, per the no-workshop-links convention). This proposal holds only the shape and the adoption boundary; when that workshop closes, its conclusions should land here or in an ADR.

## Free choices

- **Reuse `watches` vs a new field.** `watches: [body, type-spec]` adds no field but overloads a token that until now names only note portions with one that names a separate file. A dedicated `depends-on:` (or `watches-inputs:`) field keeps the two notions distinct at the cost of a second freshness-relevant frontmatter list. The choice sets whether "input dependency" is a first-class gate concept or a lodger in `watches`.
- **Column vs input-set table.** A third acceptance column is the minimal type-spec-as-gate cut; the input-set join table is the general make-like cut. Adopting the column first and migrating later is viable — the acceptance schema is recreated rather than migrated in place — but each migration re-pins accepted baselines, so a column adopted then abandoned costs a full re-acceptance sweep.
- **Blanket vs gate-scoped watching.** Blanket needs no gate authoring but over-invalidates; gate-scoped needs every type-dependent gate to opt in but keeps blast radius tight. `requires-type` gates are the obvious first opt-in cohort either way.
- **Resolver reuse.** The type-spec input resolves by the same `file-content` hash the note and gate already use, so no new resolver is needed for the level-one cut. The general model's other candidate inputs (`AGENTS.md`, `COLLECTION.md`) are also local files, so the file-content resolver covers them too — the open resolver questions are external-source target kinds, which this proposal does not touch.

## Adoption criteria

Adopt type-spec-as-gate the first time a type-contract edit is observed to leave `requires-type` gate reviews falsely fresh — that is the concrete false negative, and until it bites, the two-input model is not wrong, only narrow. Prefer the single-column, gate-scoped, `requires-type`-cohort cut: it closes the observed gap with the least schema and authoring churn.

Adopt the generalized input-set model only when a *third* distinct input class earns watching beyond the type spec — a `COLLECTION.md` or vocabulary dependency that a gate genuinely rests on. Two inputs justify two columns; three justify a table. Building the variable input set before the third input exists is motion, not progress: it generalizes a pattern that still has only one instance past the original pair.

## Risks

- **A stale freshness cache is a trap.** The whole value of watching an input is that its absence is silent — a false-fresh review looks identical to a real one. Adding the type-spec input only helps if the resolver actually runs on every selection; a watched input that is declared but not hashed is worse than an unwatched one, because it advertises coverage it does not deliver. The freshness hash must include the type-spec input the instant a gate declares it watches it.
- **Overloading `watches` blurs two invalidation questions.** `watches` today answers "did the part of the note this gate cares about change?" Adding auxiliary files makes it also answer "did a file other than the note change?" The ack path (`ack_trivial_note_changes.py`) reads `watches` to decide triviality over note portions; it must not silently treat a type-spec change as an acknowledgeable trivial note change.
- **Migration re-pins baselines.** Because the acceptance store is recreated rather than migrated, any schema change here re-accepts every pair from scratch or requires a carry-forward path. Choosing the column cut first and the table cut later pays this cost twice.

---

Relevant Notes:

- [link graph plus timestamps enables make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — rationale: the make-like build-target model this generalizes review freshness toward; a review pair is a target and its watched inputs are prerequisites
- [review system](../README-REVIEW-SYSTEM.md) — part-of: the freshness, gate, and acceptance concepts this proposal extends
- [032-review freshness uses DB snapshots, not Git](../adr/032-review-freshness-uses-db-snapshots-not-git.md) — see-also: the content-snapshot freshness substrate a third input reuses unchanged
- [012-types for structure, traits for review](../adr/012-types-for-structure-traits-for-review.md) — see-also: the type/trait boundary that makes the type spec a review input rather than a validator-only artifact
- [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — see-also: the accepted freshness hash is a checked cache of a recomputable comparison; watched-but-unhashed inputs are the "absent check" failure
