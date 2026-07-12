---
description: "Proposal: one validation algorithm over anchored checks with declared read scopes; schema absorbs into the type's check list first, collection validation retires in favour of local types"
type: kb/types/note.md
traits: [design-proposal]
tags: [type-system, kb-maintenance]
---

# One validation algorithm over declared scopes

Deterministic validation grew a check at a time. It now has four scopes, three sources, two owners, and two layers, none of them named — the sequence in `validate_note` and `validate_notes.main` *is* the specification. This proposal asks what the algorithm should be, and where a check should live.

The trigger was shipping the verbatim-quote check ([ADR 046](../adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)), which produced a second referential check and made the missing model visible. Findings are now labelled by source ([validation contract](../validation-contract.md)), which fixes the *reporting* symptom without giving the *architecture* a shape.

## Current state (as of 2026-07-12)

**Four scopes exist, undeclared and scattered across two layers.**

| Scope | What runs | Where it lives |
|---|---|---|
| note, type-independent | frontmatter parse, title/slug limits, link health, verbatim quotes | `lib/validation.validate_note` (the `base` group) |
| note, type-dependent | JSON Schema (`schema`) **and** imperative rules (`_TYPE_RULES`) | schema in the KB's `.schema.yaml`; imperative rules in framework Python |
| collection | `validate_collection_structure` — nested `COLLECTION.md` placement | **`cli/validate_notes.py`**, not the library |
| corpus | `orphan_info` — inbound-link presence across a scope | `lib/validation`, invoked and merged by the CLI |

Plus a scope-expansion step, `impacted_marked_tag_readmes`, which pulls tag-READMEs into the target set when an edited note could invalidate their marks — targeting logic living in the CLI.

**A type's checks are split across two owners and two languages.** The declarative half is a `.schema.yaml` in the KB, authored by whoever owns the type. The imperative half is a Python decorator in the shipped package:

```python
@type_rule("tag-readme")
@type_rule("agent-memory-system-review")
```

**`agent-memory-system-review` is a collection-local type** (`kb/agent-memory-systems/types/`, referenced as `../types/agent-memory-system-review.md`), yet its rule ships inside `llm-commonplace`. Every downstream project installing the package receives a registration for a type it does not have. Meanwhile a downstream KB **cannot add an imperative check at all** without editing the framework — there is no hook, entry point, or declarative escape.

**Dispatch keys on the wrong identity.** `_TYPE_RULES` is keyed by the type's bare `name:` string, while type identity in this system is *path-valued* — that is the entire point of collection-local types. Two collections may each define a type named `x` and both silently receive the framework's rule for `x`.

**A schema cannot dereference.** JSON Schema validates one instance document; it has no way to follow a path and inspect the artifact it names. That is inherited from the substrate and is why the imperative mechanism exists. It is not a defect to fix — it is the constraint the design must route around ([a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) is what makes the routing obligatory rather than optional).

**The collection-extension question has since been answered once, outside this proposal.** When the epistack casework needed new source genres and capture fields, the resolution ([ADR 045](../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md), decided 2026-07-12) was not a collection-level mechanism: **the collection declares its own local type** — a type-spec doc plus schema in its `types/`, listed in its `COLLECTION.md` Types menu, replacing or extending the shipped default. Types are the declared extension point ([collections and types](../collections-and-types.md)); a collection that wants different mechanical constraints on its artifacts points its Types menu at a local type that carries them.

## The problem, stated

Three things are tangled that should be separate:

1. **Scope** — what the check quantifies over: this note, this note *and its type*, this note *and its collection*, the corpus.
2. **Mechanism** — declarative (schema) vs imperative (code). Forced by whether the check dereferences, not by who owns it.
3. **Owner** — the framework, the type, or the collection.

Today, mechanism is *coupled to owner*: if you own a type and need a check a schema cannot express, you must become the framework. That coupling is a design choice, not an inherited constraint, and it is the one that hurts.

And a fourth thing is simply missing: **nothing unifies note-scope and corpus-scope validation.** `orphan_info` and `impacted_marked_tag_readmes` live in the CLI as one-off passes because there is no model that says what a corpus check *is* relative to a note check. Each new wide check would be a new hand-merged special case.

## The unifying idea: anchored checks with declared read scopes

Every existing check, note-level or corpus-level, fits one shape:

> A check is **anchored** on exactly one artifact — the artifact its finding lands on — and declares a **read scope**: the ground truth it is allowed to consult, from the document alone, through dereferenced link targets, out to the corpus.

| Check | Anchor | Read scope | Owner |
|---|---|---|---|
| frontmatter parse, title/slug limits | the note | the note | framework |
| type schema | the note | the note (parsed object) | the type |
| link health | the note | the note + existence of link targets | framework |
| verbatim quotes | the note | the note + contents of cited sources | framework |
| tag-README marks (`complete`, `covered_by`) | the tag-README | tag membership across the collection | the type |
| orphan detection | the note | the corpus inbound-link graph | framework |
| nested-`COLLECTION.md` placement | the `COLLECTION.md` file | its ancestor directories | framework |

Under this model there is **one algorithm**: given a target set, run every check anchored on each target against that check's read scope. "Note validation" and "corpus validation" are not two passes — they differ only in how wide the read scopes involved are. Corpus-level facts (the link graph, tag membership) become shared indexes built once per run: an *optimization* of wide read scopes, not a separate scope in the algorithm.

Two things that are currently ad hoc become derivable:

- **Targeting is the inverse image of read scopes.** Editing note *N* must re-validate every anchor owning a check whose read scope contains *N*. `impacted_marked_tag_readmes` is exactly this inverse image, hand-computed for one check and stranded in the CLI. With read scopes declared, targeting stops being per-check bespoke logic.
- **The derived-copy rule gets an address.** A wide-read check is precisely the recompute-and-compare that [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) demands; the read scope *names the ground truth* the cached value is derived from.

The residue of the original three-way tangle is then small: **owner** has two values (framework, type — collection drops out, see option E below), **read scope** is a per-check declaration, and **mechanism** is merely how a rule is expressed — after option A, a schema is just one intra-document check in the type's check list, not a separate source.

This is a naming and structuring move before it is a code move: the checks already behave this way; nothing currently says so.

## Option space (revised)

### A. Absorb schema into the type's check list — **the first step in any case**

Make the schema *one kind of type check*, so all of a type's checks sit behind a single registration:

```
checks_for(type) -> [SchemaCheck(schema_path), MarkCheck(...), QuoteShapeCheck(...)]
```

*For:* one place to look per type; the "two owners, two languages" split disappears from the caller's view; the algorithm becomes the anchored-check loop above. Every other continuation — B if it is ever wanted, C if it were ever accepted — would begin with this same absorption, which is what makes it safe to do now as a standalone refactor rather than anticipatory design.
*Against:* it unifies the *call site*, not the *authoring surface* — the imperative half of a type's contract still lives in Python. It relieves the symptom without curing it; the cure waits for demand (see B).

Done together with A: **fix the name-vs-path dispatch key**, a defect on any option.

### B. A declarative mark primitive — **deferred: too much machinery at current demand**

A type spec could declare a mark's recomputation (`recompute: tag-members(index_key)`, `compare: every-member-linked`), keeping the KB data while letting a collection-local type own a dereferencing check.

*For:* it is exactly the shape the derived-copy rule demands, and under the anchored-check model it has a precise slot: a declared way for a type to author a *wide-read* check without code.
*Against:* it is a new language, and languages grow. At n=2 imperative rules (one of which, `tag-readme`, is a framework type anyway) the primitive would be designed against one real example. If B is ever taken, A precedes it — the absorption is the substrate B would register into.

### C. A KB-side code hook — **rejected, and not needed yet**

*For:* maximal reach.
*Against:* it turns a knowledge base into a code-execution surface, contradicting the substrate commitment that KB artifacts are inspectable data. No current demand exists; and were it ever accepted, A would still come first. Named here so the rejection is on the record rather than assumed.

### D. Push type-specific semantics to the review gate

The KB-side extension point for type-specific *semantics* already exists: the type-conformance review gate makes a type spec's prose an LLM-judged criterion ([ADR 038](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)).

*For:* zero new machinery; already shipped. Together with local types (see E) it covers most of what a downstream KB has actually asked for.
*Against:* it is Level B — costly, non-deterministic, and it cannot hold a **mark**. A mark is a cached recomputable value, and the derived-copy rule says it must be machine-checked *or absent*; an LLM-judged mark is the forbidden hand-maintained-and-trusted state with a stronger trust signal attached. So D is sufficient for *semantics* and structurally insufficient for *marks*. This remains the sharpest boundary in the option space, and it is the boundary B waits behind.

### E. Collection-dependent deterministic checks — **retired: superseded by collection-local types**

The earlier draft held this open pending a worked case. The worked case arrived — the epistack casework's richer-source-type demand — and it landed somewhere else: the collection **declares a local type** ([ADR 045](../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md); [collections and types](../collections-and-types.md)). The move generalizes: any mechanical constraint a collection would declare over its artifacts, it can declare in a local type-spec's schema and route every write through it via the `COLLECTION.md` Types menu, which already exists and already gates authoring. A collection-scope check mechanism would duplicate that path while violating the boundary that a collection owns text-level features only, never frontmatter or structural semantics ([collections never own frontmatter semantics](../collections-never-own-frontmatter-semantics.md)).

Two residues, neither of which revives E:

- `validate_collection_structure` (nested `COLLECTION.md` is invalid) is not a collection-*declared* check; it is a framework invariant about what a collection *is*, anchored on the offending `COLLECTION.md` file. It stays, as an ordinary framework check.
- A local type still cannot carry an *imperative* check — but that is the type-owner gap options A/B address, not a collection gap.

So the scope lattice loses a level: **collection is not a check owner; it is a menu of types.**

## Forces

- **The schema cannot dereference.** Inherited. Any design must keep an imperative path; the only question is who may author it.
- **A mark must be machine-checked or absent.** This is what makes a *deterministic* type-owned check load-bearing rather than a convenience — and what makes option D insufficient on its own.
- **The KB is data, not code.** The substrate commitment that makes artifacts inspectable, diffable, and reviewable. Option C trades it away; that is why C stays rejected.
- **Framework-owned closed registries fail under downstream pressure — and the relief valve is now known.** The `source_type` enum recurred three times from the epistack casework before [ADR 045](../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md) opened it, and the extension route that closed the question was a collection-local type. `_TYPE_RULES` is the same closed-registry shape; the same relief valve covers its declarative half today (a local schema is already KB-authored) and would cover its imperative half only if B ships.
- **YAGNI, honestly applied.** The awaited worked case landed on local types + D, not on B or E. Demand for a KB-authored *imperative* check remains n=0: the felt gap this proposal can act on is the internal architecture (A, the dispatch key, the missing corpus/note model), not a new authoring surface.
- **Identity should be path-valued.** Rule dispatch keying on a bare `name:` contradicts the type system's own path-valued identity. A defect regardless of option.

## Free choices

- Whether the anchored-check model is adopted *explicitly* in code (checks as objects carrying `anchor`, `reads`, `owner`) or first as names on the existing sequence — the model constrains neither.
- Whether `validate_collection_structure` and `orphan_info` move into the library, and whether scope expansion (`impacted_marked_tag_readmes`) is computed generically from declared read scopes or stays special-cased until a second wide-read check exists. *(Their current placement in the CLI looks like accident rather than intent, but nothing depends on it.)*
- The mark-declaration syntax in option B, if B is ever taken.

## What would settle the rest

The actionable core no longer waits on anything: **do A plus the dispatch-key fix**, structured so the result reads as anchored checks with declared read scopes — that single refactor names the algorithm, dissolves the schema/rule split at the call site, and makes the CLI's corpus passes instances instead of exceptions.

What still waits is B, and its trigger is now sharper than "a worked case": **a collection-local type needing a mark** — a cached recomputable value that D cannot hold and a local schema cannot recompute. Until a downstream KB hits that exact wall, the imperative authoring surface stays framework-side.

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why a mark demands a *deterministic* check, and what a wide-read check's read scope names
- [The validation contract](../validation-contract.md) — evidence: the shipped behavior this proposal would restructure
- [ADR 046 — Verbatim quotes are validated against their cited source](../adr/046-verbatim-quotes-are-validated-against-their-cited-source.md) — evidence: the second referential check, whose arrival surfaced the missing model
- [ADR 038 — Type-conformance reviews use the type spec as the gate](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — evidence: the existing KB-side extension point, and option D's basis
- [ADR 045 — Source genre is a single open field on the snapshot](../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md) — evidence: the worked case whose resolution — declare a collection-local type — retires option E
- [Collections and types](../collections-and-types.md) — evidence: types as the declared extension point, and the `COLLECTION.md` Types menu option E's replacement rides on
- [Collections never own frontmatter semantics](../collections-never-own-frontmatter-semantics.md) — rationale: the boundary a collection-scope check mechanism would have violated
- [First principles are inherited constraints, not design choices](../../notes/first-principles-are-inherited-constraints-not-design-choices.md) — grounds: the test separating the schema's dereferencing limit (inherited) from the mechanism/owner coupling (chosen, and the one that hurts)
