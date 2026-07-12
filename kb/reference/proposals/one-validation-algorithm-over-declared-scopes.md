---
description: "Proposal: one validation algorithm over declared scopes, colocating a type's schema and imperative rules, and letting a KB declare the checks a schema cannot express"
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

**Collection-dependent deterministic checks do not exist.** A `COLLECTION.md` binds at review time only ([ADR 041](../adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)) — LLM-judged, Level B. There is no way for a collection to declare a mechanical check.

## The problem, stated

Three things are tangled that should be separate:

1. **Scope** — what the check quantifies over: this note, this note *and its type*, this note *and its collection*, the corpus.
2. **Mechanism** — declarative (schema) vs imperative (code). Forced by whether the check dereferences, not by who owns it.
3. **Owner** — the framework, the type, or the collection.

Today, mechanism is *coupled to owner*: if you own a type and need a check a schema cannot express, you must become the framework. That coupling is a design choice, not an inherited constraint, and it is the one that hurts.

## Option space

### A. Absorb schema into the rule registry (the maintainer's suggestion)

Make the schema *one kind of type rule*, so all of a type's checks are colocated behind a single registration:

```
checks_for(type) -> [SchemaCheck(schema_path), MarkCheck(...), QuoteShapeCheck(...)]
```

*For:* one place to look per type; the "two owners, two languages" split disappears from the caller's view; the algorithm becomes `for scope in scopes: for check in checks(scope): run`.
*Against:* it unifies the *call site*, not the *authoring surface* — the schema still lives in the KB and the imperative rule still lives in Python, so a type author still needs framework access for half their contract. It relieves the symptom this proposal is about, without curing it.

### B. A declarative mark primitive

Notice what `tag-readme`'s check actually *is*: *recompute a set from a query, compare it to what the note claims.* That is parameterizable. A type spec could declare:

```yaml
marks:
  complete:
    recompute: tag-members(index_key)
    compare: every-member-linked
```

*For:* the KB stays data — no code execution from a knowledge base. It generalizes the `mark` concept the vocabulary already carries, and it is exactly the shape the derived-copy rule demands (a derivation rule a machine can run). A collection-local type could then declare a mark **without touching the framework**.
*Against:* it is a new language, and languages grow. It covers marks; it does not cover the agent-memory quote-shape check, which is a *shape* assertion, not a recomputation. Whether one primitive or a small family is needed is unknown at n=2.

### C. A KB-side code hook (entry points, a `checks.py` per collection)

*For:* maximal reach; a downstream KB can express anything.
*Against:* it turns a knowledge base into a code-execution surface, which contradicts the substrate commitment that KB artifacts are inspectable data. Strongly disfavoured, and named here so the rejection is on the record rather than assumed.

### D. Push type-specific semantics to the review gate and accept the deterministic ceiling

The KB-side extension point for type-specific checks *already exists*: the type-conformance review gate makes a type spec's prose an LLM-judged criterion ([ADR 038](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)).

*For:* zero new machinery; already shipped.
*Against:* it is Level B — costly, non-deterministic, and it cannot hold a **mark**. A mark is a cached recomputable value, and the derived-copy rule says it must be machine-checked *or absent*; an LLM-judged mark is the forbidden hand-maintained-and-trusted state with a stronger trust signal attached. So D is sufficient for *semantics* and structurally insufficient for *marks*. This is the sharpest boundary in the option space.

### E. Collection-dependent deterministic checks

Currently absent. A collection could declare mechanical checks the way a type does — the natural home for rules like "every note here cites at least one source in `../sources/`."

*For:* completes the scope lattice; `COLLECTION.md` already *is* a contract, and it already binds at review time, so extending it to bind mechanically is continuous rather than novel.
*Against:* **no worked case demands it.** Adding it now would be speculative machinery, which is the thing this codebase's own discipline forbids.

## Forces

- **The schema cannot dereference.** Inherited. Any design must keep an imperative path; the only question is who may author it.
- **A mark must be machine-checked or absent.** This is what makes a *deterministic* type-owned check load-bearing rather than a convenience — and what makes option D insufficient on its own.
- **The KB is data, not code.** The substrate commitment that makes artifacts inspectable, diffable, and reviewable. Option C trades it away; that is why C is disfavoured.
- **Framework-owned closed registries fail under downstream pressure.** The `source_type` enum recurred three times from the epistack casework before [ADR 045](../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md) opened it. `_TYPE_RULES` is the same shape, and worse: a downstream KB cannot even contribute a *value*, it must contribute Python.
- **YAGNI, honestly applied.** Downstream demand for a collection-local imperative check is currently **n=0**. Nobody has hit this. The gap is real and predicted, not felt. Build-local-first says wait for the worked case — and says so loudly here, because this proposal is exactly the anticipatory design the discipline distrusts.
- **Identity should be path-valued.** Rule dispatch keying on a bare `name:` contradicts the type system's own path-valued identity. This one is a defect regardless of which option is taken.

## Free choices

- Whether the algorithm is expressed as an explicit scope lattice (`note-independent → type → collection → corpus`) or stays an ordered sequence with names attached.
- Whether `validate_collection_structure` and `orphan_info` move into the library, and whether the scope-expansion step (`impacted_marked_tag_readmes`) is a targeting concern or a validation concern. *(Their current placement in the CLI looks like accident rather than intent, but nothing depends on it.)*
- Whether option A's colocation is worth doing on its own, as a pure refactor, independent of whether B or E is ever adopted.
- The mark-declaration syntax in option B, if B is taken.

## What would settle it

A worked case. Specifically: **a downstream KB (the epistack casebooks are the live candidate) needing a mark or a deterministic type-owned check of its own, and being blocked.** That would convert this from an anticipated gap into a felt one, and would show which of B, D, or E the demand actually lands on — which is not currently knowable from inside the framework.

Until then, the defensible subset is small and worth separating out: **fix the name-vs-path dispatch key** (a defect on any option), and **decide whether A's colocation is worth a standalone refactor**. Everything else waits.

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why a mark demands a *deterministic* check, which is what makes the review-gate escape hatch insufficient
- [The validation contract](../validation-contract.md) — evidence: the shipped behavior this proposal would restructure
- [ADR 046 — Verbatim quotes are validated against their cited source](../adr/046-verbatim-quotes-are-validated-against-their-cited-source.md) — evidence: the second referential check, whose arrival surfaced the missing model
- [ADR 038 — Type-conformance reviews use the type spec as the gate](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — evidence: the existing KB-side extension point, and option D's basis
- [ADR 045 — Source genre is a single open field on the snapshot](../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md) — evidence: the precedent for a framework-owned closed registry failing under downstream pressure
- [First principles are inherited constraints, not design choices](../../notes/first-principles-are-inherited-constraints-not-design-choices.md) — grounds: the test separating the schema's dereferencing limit (inherited) from the mechanism/owner coupling (chosen, and the one that hurts)
