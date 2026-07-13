---
description: "Proposal: simplify deterministic validation around artifact anchors and a run-scoped context; keep invalidation explicit until repeated cases justify dependency machinery"
type: kb/types/note.md
traits: [design-proposal]
tags: [type-system, kb-maintenance]
---

# Artifact-anchored validation over a run-scoped context

Deterministic validation grew a check at a time. It now mixes per-artifact checks, batch checks, target expansion, and shared-index construction across a library and a CLI. Some distinctions are named in reporting, but the sequence in `validate_note` and `validate_notes.main` remains the execution specification. This proposal asks what small common model those checks share, how much code that model can remove now, and which dependency machinery should remain deferred.

The trigger was shipping the verbatim-quote check ([ADR 046](../adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)), which produced a second referential check and made the missing model visible. Findings are now labelled by source ([validation contract](../validation-contract.md)), which fixes the *reporting* symptom without giving the *architecture* a shape.

## Current state (as of 2026-07-13)

**Per-artifact and batch concerns are undeclared and scattered across two layers.**

| Concern | What runs | Where it lives |
|---|---|---|
| artifact, type-independent | frontmatter parse, title/slug limits, link health, verbatim quotes | `lib/validation.validate_note` (the `base` group) |
| artifact, type-dependent | JSON Schema (`schema`) **and** imperative rules (`_TYPE_RULES`) | schema in the KB's `.schema.yaml`; imperative rules in framework Python |
| collection structure | `validate_collection_structure` — nested `COLLECTION.md` placement | **`cli/validate_notes.py`**, not the library |
| validation-scope graph | `orphan_info` — inbound authored-link presence within the selected batch, normally one collection | `lib/validation`, invoked and merged by the CLI |

Plus a scope-expansion step, `impacted_marked_tag_readmes`, which pulls tag-READMEs into the target set when an edited note could invalidate their marks — targeting logic living in the CLI.

[ADR 047](../adr/047-type-specifications-use-normal-deterministic-validation.md) retired the former `validate_type_specs` batch pass. Type definitions are notes of type `type-spec`: collection validation includes local definitions, `commonplace-validate types` targets the complete inventory, and an ordinary imperative type rule resolves each definition's declared schema. This is one shipped instance of giving a batch responsibility an artifact anchor; it does not settle the broader execution or invalidation design below.

[ADR 049](../adr/049-validator-resolution-returns-scope-and-loads-types-directly.md) removed duplicate target interpretation. `resolve_validation_target` now returns the selected paths plus optional collection scope, from which batch reporting, orphan calculation, and collection-structure validation derive. It also replaced type-spec synthetic self-resolution with a direct definition loader. These changes make scope and type loading explicit, but they do not declare check dependencies, share one execution protocol, or generalize incremental invalidation.

`orphan_info` is intentionally not a repository-wide graph. It asks whether another visible source artifact in the validated collection links to the note. Build-time-only `dir-index.md` pages and generated tag tails do not exist in the working tree and therefore do not contribute; links in authored prose, Relevant Notes footers, and curated tag-README heads do. The signal is authored integration into a collection, not mere discoverability in a generated inventory ([ADR 025](../adr/025-complete-generated-indexes-are-build-time-only.md)).

**A type's checks are split across two owners and two languages.** The declarative half is a `.schema.yaml` in the KB, authored by whoever owns the type. The imperative half is a Python decorator in the shipped package:

```python
@type_rule("kb/types/tag-readme.md")
@type_rule("kb/agent-memory-systems/types/agent-memory-system-review.md")
```

**`agent-memory-system-review` is a collection-local type** (`kb/agent-memory-systems/types/`, referenced as `../types/agent-memory-system-review.md`), yet its rule ships inside `llm-commonplace`. Every downstream project installing the package receives a registration for a type it does not have. Meanwhile a downstream KB **cannot add an imperative check at all** without editing the framework — there is no hook, entry point, or declarative escape.

The former name-vs-path dispatch defect is resolved by [ADR 048](../adr/048-imperative-type-rules-dispatch-by-canonical-path.md): `_TYPE_RULES` now keys applicability on canonical path-valued type identity. This proposal therefore retains only the broader execution, dependency, and authoring questions.

**A schema cannot dereference.** JSON Schema validates one instance document; it has no way to follow a path and inspect the artifact it names. That is inherited from the substrate and is why the imperative mechanism exists. It is not a defect to fix — it is the constraint the design must route around ([a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) is what makes the routing obligatory rather than optional).

**The collection-extension question has since been answered once, outside this proposal.** When the epistack casework needed new source genres and capture fields, the resolution ([ADR 045](../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md), decided 2026-07-12) was not a collection-level mechanism: **the collection declares its own local type** — a type-spec doc plus schema in its `types/`, listed in its `COLLECTION.md` Types menu, replacing or extending the shipped default. Types are the declared extension point ([collections and types](../collections-and-types.md)); a collection that wants different mechanical constraints on its artifacts points its Types menu at a local type that carries them.

## The problem, stated

Four things are tangled that should be separate:

1. **Anchor and applicability** — which artifact receives the finding, and which checks apply to it.
2. **Evaluation inputs** — what a check consults when it runs: the document, referents, a collection index, or check-definition artifacts such as schemas.
3. **Invalidation dependencies** — which changes can alter the check's result for a particular anchor.
4. **Owner and mechanism** — who defines the constraint (framework or type), and whether it is expressed declaratively (schema) or imperatively (code).

Today, mechanism is *coupled to owner*: if you own a type and need a check a schema cannot express, you must become the framework. That coupling is a design choice, not an inherited constraint, and it is the one that hurts.

And an execution model is missing: **nothing unifies artifact-local checks with checks evaluated from shared collection indexes.** `orphan_info` and `impacted_marked_tag_readmes` remain one-off CLI passes because there is no model that says what an indexed check is relative to a document-local check. Each new wide check would be another hand-merged special case.

## The unifying idea: anchored checks over a shared run context

Every existing check, whether artifact-local or evaluated from a wider index, fits one shape:

> A check is **anchored** on exactly one artifact — the artifact its finding lands on — and its design identifies both what it reads when evaluated and what changes could invalidate its result.

"Identifies" is deliberately weaker than "encodes in a generic dependency language." Evaluation inputs and invalidation dependencies are part of the check's model even when ordinary function calls and explicit selectors remain their implementation. Turning them into executable metadata is a later optimization that must earn its machinery.

| Check | Anchor | Evaluation inputs | Invalidation dependencies | Owner |
|---|---|---|---|---|
| frontmatter parse, title/slug limits | the artifact | its path and contents | path or contents | framework |
| type schema | the note | parsed note, type spec, schema and referenced schemas | note contents or type/schema definition closure | type |
| link health | the note | local link targets' existence | note links or target existence | framework |
| verbatim quotes | the note | contents of cited sources | quote/citation contents or cited-source contents | framework |
| tag-README marks (`complete`, `covered_by`) | the tag-README | relevant tag-membership indexes for its collection | mark declaration or membership of the relevant tags | type |
| orphan detection | the content note | authored-link graph of the validation scope | scope membership or authored outbound links within that scope | framework |
| nested-`COLLECTION.md` placement | the candidate `COLLECTION.md` | its path and ancestor collection boundaries | path/name or ancestor boundaries | framework |
| type-spec resolution | the type-spec doc | its frontmatter and declared schema target | type-spec contents or schema existence | type |

Under this model there can be **one small evaluation shape**: establish a validation run, resolve its anchors, parse each artifact once, expose shared indexes lazily from a run-scoped context, and evaluate applicable checks with findings attached to their anchors. Document-local and collection-indexed validation differ in what they read from the context, not in how findings are attached or reported.

The minimal realization needs no check-object hierarchy or dependency graph. A `ValidationRun` or `ValidationContext` can cache parsed artifacts, the authored-link graph, and tag-membership indexes; existing base functions, imperative type rules, and schema validation can keep their current dispatch. The CLI then resolves a target, asks the library to evaluate the run, and formats the returned results. This directly removes repeated parsing and hand-merging without first redesigning every check.

Target selection is related but not identical. A coarse statement such as "reads the collection" is sufficient to run a check but insufficient for precise incremental invalidation: a body-only edit should not revalidate every tag-README. Incremental targeting needs concrete dependency keys or an explicit invalidation selector, and may need old and new state. The inverse dependency map can be indexed, recomputed conservatively, or remain special-cased until repeated demand justifies a general engine.

This gives the current ad hoc behavior a more precise interpretation:

- **`impacted_marked_tag_readmes` is an invalidation selector.** It is a hand-computed inverse dependency for one check, not evidence that every inverse can be derived from a coarse read-scope label.
- **The derived-copy rule gets an address.** A wide-read check is precisely the recompute-and-compare that [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) demands; its evaluation dependencies name the ground truth from which the cached value is derived.
- **Definition changes are first-class invalidators.** A schema check depends not only on the note instance but on the type spec, schema, and referenced-schema closure. A later incremental-invalidation system must be able to target applicable notes after a schema edit even though the note contents did not change.

The residue is then small: current checks have two owners (framework and type), mechanisms remain schema or code, and dependencies describe both evaluation and invalidation. Collection remains an execution boundary and a menu of types; whether it should ever become a check owner remains a separate extension question (see option E).

This is a naming and structuring move before it is a code move: most checks already fit the model, but the current implementation does not share a run context or one result-attachment protocol. Precise dependency declarations are not required for that simplification.

## Option space (revised)

### A. Resolve schema and imperative rules through one type-check interface — **deferred: not the first experiment**

Make the schema *one kind of type check*, so all of a type's checks sit behind a single registration:

```
checks_for(type_profile) -> [SchemaCheck(schema_path), MarkCheck(...), QuoteShapeCheck(...)]
```

*For:* one dispatch path per resolved type; schema and imperative rules can implement the same finding protocol; applicability keys on the canonical path-valued type identity. This remains a bounded refactor if the current sequence later becomes a source of duplication.
*Against:* it unifies the *call site*, not the authoring surface, dependency model, shared-index lifecycle, or incremental targeting. The imperative half of a type's contract still lives in Python. It therefore does not by itself turn `orphan_info` or collection-structure validation into instances of one algorithm.

Schema findings should retain schema provenance after unification. Owner (`type`) and mechanism/source (`schema` or imperative rule) answer different repair questions; a single dispatch path is not a reason to collapse their labels.

Path-valued applicability is already shipped independently of A ([ADR 048](../adr/048-imperative-type-rules-dispatch-by-canonical-path.md)).

A does not exercise the part of the model that currently causes orchestration and repeated work. The first experiment should instead put orphan detection and tag-membership evaluation behind a run-scoped context while leaving the readable base → type rules → schema sequence intact. Revisit A only if that sequence itself becomes a source of duplication.

### B. A declarative mark primitive — **deferred: too much machinery at current demand**

A type spec could declare a mark's recomputation (`recompute: tag-members(index_key)`, `compare: every-member-linked`), keeping the KB data while letting a collection-local type own a dereferencing check.

*For:* it is exactly the shape the derived-copy rule demands, and under the anchored-check model it has a precise slot: a declared way for a type to author a collection-indexed check without code. The primitive could also declare the dependency keys needed for invalidation.
*Against:* it is a new language, and languages grow. There are three framework-side imperative registrations, but only one mark-shaped worked example: `tag-readme`. The primitive would therefore still be designed against one real example. A shared check interface would be useful substrate, but its exact form should not be dictated by a hypothetical declaration language.

### C. A KB-side code hook — **rejected, and not needed yet**

*For:* maximal reach.
*Against:* it turns a knowledge base into a code-execution surface, contradicting the substrate commitment that KB artifacts are inspectable data. No current demand exists. Named here so the rejection is on the record rather than assumed.

### D. Push type-specific semantics to the review gate

The KB-side extension point for type-specific *semantics* already exists: the type-conformance review gate makes a type spec's prose an LLM-judged criterion ([ADR 038](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)).

*For:* zero new machinery; already shipped. Together with local types (see E) it covers most of what a downstream KB has actually asked for.
*Against:* it is Level B — costly, non-deterministic, and it cannot hold a **mark**. A mark is a cached recomputable value, and the derived-copy rule says it must be machine-checked *or absent*; an LLM-judged mark is the forbidden hand-maintained-and-trusted state with a stronger trust signal attached. So D is sufficient for *semantics* and structurally insufficient for *marks*. This remains the sharpest boundary in the option space, and it is the boundary B waits behind.

### E. Collection-owned deterministic checks — **no present demand; local types handled the worked case**

The earlier draft held this open pending a worked case. The worked case arrived — the epistack casework's richer-source-type demand — and it landed somewhere else: the collection **declares a local type** ([ADR 045](../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md); [collections and types](../collections-and-types.md)). That establishes the default for intra-document mechanical variation: use a local type-spec and schema, routed through the `COLLECTION.md` Types menu. A generic collection-owned check mechanism would duplicate that path while violating the current boundary that a collection owns text-level features, not frontmatter or structural semantics ([collections never own frontmatter semantics](../collections-never-own-frontmatter-semantics.md)).

The worked case does **not** establish that every possible collection constraint is reducible to a local schema. A relation spanning artifacts or heterogeneous types may be inherently collection-indexed, and schemas cannot dereference. No such downstream requirement exists today, so there is no reason to introduce collection ownership now; if one arrives, the design must first ask whether the relation has an honest artifact anchor and type owner before reopening this option.

Two residues, neither of which revives E:

- `validate_collection_structure` (nested `COLLECTION.md` is invalid) is not a collection-*declared* check; it is a framework invariant about what a collection *is*, anchored on the offending `COLLECTION.md` file. It stays, as an ordinary framework check.
- A local type still cannot carry an *imperative* check — the current extension gap considered by B, not evidence by itself for collection ownership.

For current demand, **collection is a validation boundary and a menu of types, not a check owner**. That is a maintained design default, not a proof that a future relational worked case cannot challenge it.

## Forces

- **The schema cannot dereference.** Inherited. Any design must keep an imperative path; the only question is who may author it.
- **A mark must be machine-checked or absent.** This is what makes a *deterministic* type-owned check load-bearing rather than a convenience — and what makes option D insufficient on its own.
- **The KB is data, not code.** The substrate commitment that makes artifacts inspectable, diffable, and reviewable. Option C trades it away; that is why C stays rejected.
- **Framework-owned closed registries fail under downstream pressure — and the declarative relief valve is known.** The `source_type` enum recurred three times from the epistack casework before [ADR 045](../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md) opened it, and the extension route that closed the question was a collection-local type. `_TYPE_RULES` is the same closed-registry shape for imperative rules; local schemas relieve its declarative half, while B would address only the narrower mark-shaped imperative demand.
- **YAGNI, honestly applied.** The awaited worked case landed on local types + D, not on B or E. Demand for a KB-authored *imperative* check remains n=0. Present demand supports naming the execution/dependency model; it does not yet require a new authoring language or collection-owned checker.
- **Identity is path-valued.** [ADR 048](../adr/048-imperative-type-rules-dispatch-by-canonical-path.md) now establishes this as a shipped boundary the broader design must preserve.
- **Evaluation reads and invalidation are related but distinct.** A broad index may be cheapest to build once for evaluation while a narrow dependency key is needed to avoid invalidating unrelated anchors.
- **Diagnostic provenance must survive dispatch unification.** Owner says whose contract is being enforced; mechanism and check identity tell an operator where and how to repair it.

## Free choices

- The exact boundary of the run-scoped context: parsed artifacts only, or also lazy authored-link and tag-membership indexes.
- Whether `validate_collection_structure` becomes an anchored result in the same library run immediately or follows after orphan and tag-README checks prove the context boundary.
- How results retain check identity, owner, and mechanism without forcing every existing check into a new object hierarchy; dispatch-owned provenance is sufficient if it stays unambiguous.
- The granularity and representation of invalidation keys, if a later implementation earns them: artifact, path existence, frontmatter field, tag membership, schema-definition closure, or another small vocabulary proven by repeated selectors.
- Whether dependency inverses are ever computed generically or maintained in indexes. Until repeated demand establishes common machinery, explicit selectors such as `impacted_marked_tag_readmes` remain the default.
- The mark-declaration syntax in option B, if B is ever taken.

## Adoption criteria

The path-valued dispatch defect was fixed independently by [ADR 048](../adr/048-imperative-type-rules-dispatch-by-canonical-path.md).

### Near-term: artifact-anchored evaluation over a run-scoped context

This bounded model is ready for an ADR when a small implementation sketch or prototype can cover ordinary per-artifact validation, tag-README marks, and collection-scoped authored-link orphan detection while satisfying these tests:

- full-collection validation produces the same findings and severities;
- every finding remains attached to one artifact and retains unambiguous source provenance;
- each artifact is parsed at most once per validation run;
- shared graphs and membership indexes are built once per validation scope rather than once per anchor;
- `validate_notes.main` is reduced to target resolution, library invocation, and presentation rather than continuing to merge wide checks itself;
- base checks, imperative type rules, and schema validation may remain functions in their current sequence—no check classes or generic dependency representation are required.

The implementation should be judged as a simplification, not merely an abstraction: its new run/context code should replace repeated parsing and CLI orchestration rather than sit beside them.

### Deferred: generalized incremental invalidation

Incremental targeting remains dependency-correct where an explicit selector exists and otherwise explicitly conservative. A generic invalidation model is ready for a separate ADR only after at least two unlike selectors expose a stable common vocabulary beyond "reads this collection." That later design must account for old and new state, deletions, path-existence changes, and definition closures. Schema and referenced-schema changes invalidating applicable notes belong to that later gate; they are not a condition for adopting the run-scoped evaluator.

Option A remains deferred because common schema/type-rule dispatch would establish only a call interface, not the collection-indexed execution model that currently promises code reduction.

Option B still waits, and its trigger is sharper than "a worked case": **a collection-local type needing a mark** — a cached recomputable value that D cannot hold and a local schema cannot recompute. Option E waits for a mechanical relation that is inherently collection-owned after attempting an honest artifact anchor and type owner. Until either wall is reached, the imperative authoring surface stays framework-side and collections remain routing/validation boundaries rather than rule hosts.

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why a mark demands a *deterministic* check, and what its evaluation dependencies name
- [The validation contract](../validation-contract.md) — evidence: the shipped behavior this proposal would restructure
- [ADR 046 — Verbatim quotes are validated against their cited source](../adr/046-verbatim-quotes-are-validated-against-their-cited-source.md) — evidence: the second referential check, whose arrival surfaced the missing model
- [ADR 038 — Type-conformance reviews use the type spec as the gate](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — evidence: the existing KB-side extension point, and option D's basis
- [ADR 045 — Source genre is a single open field on the snapshot](../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md) — evidence: the worked case whose resolution — declare a collection-local type — removes present demand for option E
- [ADR 025 — Complete generated indexes are build-time only](../adr/025-complete-generated-indexes-are-build-time-only.md) — evidence: why orphan detection sees the authored collection graph rather than generated inventory links
- [ADR 047 — Type specifications use normal deterministic validation](../adr/047-type-specifications-use-normal-deterministic-validation.md) — evidence: the shipped artifact-anchored replacement for the former special type-system batch pass
- [ADR 048 — Imperative type rules dispatch by canonical path](../adr/048-imperative-type-rules-dispatch-by-canonical-path.md) — partial-adoption: fixes applicability identity without deciding the broader execution model
- [ADR 049 — Validator resolution returns scope and loads types directly](../adr/049-validator-resolution-returns-scope-and-loads-types-directly.md) — partial-adoption: removes duplicate target interpretation and synthetic type loading without introducing the broader execution model
- [Collections and types](../collections-and-types.md) — evidence: types as the declared extension point and the `COLLECTION.md` Types menu used by the current worked case
- [Collections never own frontmatter semantics](../collections-never-own-frontmatter-semantics.md) — rationale: the boundary a collection-scope check mechanism would have violated
- [First principles are inherited constraints, not design choices](../../notes/first-principles-are-inherited-constraints-not-design-choices.md) — grounds: the test separating the schema's dereferencing limit (inherited) from the mechanism/owner coupling (chosen, and the one that hurts)
