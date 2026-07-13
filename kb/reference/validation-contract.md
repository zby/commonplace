---
description: "The three sources of validation findings — base, type rules, schema — what each can express, why dereferencing checks cannot live in a schema, and what every typed note is checked for regardless of its type"
type: kb/types/note.md
tags: [type-system]
---

# The validation contract

`commonplace-validate` enforces one contract on a note, but the clauses come from three places. Every finding is labelled with the source that produced it, because a reader who knows only the type spec would otherwise get failures from rules that spec never mentions:

```
PASS:
- [base] link health: all local relative links resolve
- [schema] type schema: note requirements satisfied
FAIL:
- [type: tag-readme] complete mark: missing entry for kb/notes/foo.md
```

In one sentence: **a type declares what the document must contain; the framework checks that what it points at is really there.**

## Scope: this is the deterministic half only

A type is verified by **three** mechanisms, and only the first two are the validator's:

| | Mechanism | When | Judges meaning? |
|---|---|---|---|
| 1 | `schema` — declarative JSON Schema | validate time | no |
| 2 | `type_rule` — imperative code the type registers | validate time | no |
| 3 | **type-conformance review gate** — the type spec's *prose body* is the criterion, read by an LLM ([ADR 038](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)) | review time | yes |

This page documents 1 and 2. The third is not a lesser mechanism: **a type spec's prose is an executable criterion, not documentation.** Everything a schema cannot express still binds — it binds at review time. That is why [`type-spec.md`](../types/type-spec.md) tells authors *not* to restate schema rules in prose: the schema already enforces them, so a restatement only spends reviewer judgment re-confirming what is already guaranteed, instead of on the properties only a reviewer can check.

## The three sources of a validator finding

| Source | Owner | Mechanism | Can dereference? |
|---|---|---|---|
| `base` | framework | imperative, applies to every typed note | yes — link health, verbatim quotes |
| `type: <name>` | the type | imperative rules registered for that type | yes — tag-readme marks re-derive from the collection; type specs resolve their declared schemas |
| `schema` | the type | declarative JSON Schema over the parsed document | **no** |

**A type is not verified by its schema alone.** `tag-readme` proves it: its `complete` mark is checked by re-walking the collection and re-deriving membership from every tagged note — imperative, dereferencing, and impossible to express in a schema. `type-spec` supplies a smaller example: `type-spec.schema.yaml` can constrain the `schema:` field's shape, but an imperative rule must follow a non-null path and load the declared schema. So *who owns a rule* and *whether it dereferences* are independent axes, which is why the table has no empty cells and why "schema versus everything else" is the wrong mental model.

Type-spec documents are ordinary validation artifacts. Collection validation includes local type specs, and `commonplace-validate types` runs the same base, type-rule, and schema pipeline over the complete global and local type inventory. There is no separate type-system validation pass.

## What the schema can and cannot express

The schema is **not** limited to frontmatter. `ParsedDocument.to_validation_object()` hands it `frontmatter`, `body`, `headings`, `links`, and `body_dates`, so a type can require a `## Reasoning` heading or constrain body content declaratively, and several do.

What a schema cannot do is **dereference** — it has no way to say *follow this path and look inside the artifact it names*. JSON Schema validates one instance document; the referent is another file. This is an inherited limit of the substrate, not a gap worth closing, and it is the whole reason a second, imperative check mechanism exists at all.

So the dividing line is not frontmatter/body. It is **intra-document** (declarable) versus **referential** (must be executed). A referential check's ground truth lives in a second artifact, which is precondition 3 of [a derived copy of recomputable truth must be checked or absent](../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — the rule that makes these checks obligatory rather than optional.

## The base contract

Every note **with frontmatter** is checked for the following, whatever its type. A type spec does not declare these and cannot opt out of them.

- **Frontmatter parses** — valid delimiters, well-formed YAML.
- **Title length** within `MAX_NOTE_TITLE_LENGTH`; **filename slug length** within `MAX_NOTE_SLUG_LENGTH` (derived-artifact types are exempt from the slug limit).
- **Link health** — every local relative link resolves to an existing target. *Warns.*
- **Verbatim quotes** — every `verbatim`-marked quotation resolves against the source it links ([ADR 046](./adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)). A quote absent from its cited source **fails**; an unpairable verbatim citation warns, but only in notes that demonstrably use the convention.

**Bare text opts out entirely.** A file with no frontmatter is typed `text` and gets no structural requirements at all — the type system's own rule, and deliberate: `text` exists to keep capture friction at zero, and it holds pasted traces and imported material whose relative links are broken by construction. Checking it would generate noise on artifacts whose purpose is to be unchecked.

### Why the two referential checks have different severities

Link health **warns**; a false verbatim quote **fails**. That asymmetry is the derived-copy rule, not an inconsistency. A dangling link costs the reader a bounded, recoverable search. A false verbatim quote tells the reader the text was checked when it was not — it *suppresses* the verification it claims to have done, which is silent and unbounded. Absence degrades; a false copy corrupts.

### Why the base checks are not type-configurable

Letting a type opt out of link health or verbatim-quote resolution would be a knob that can only ever be set wrong: a broken link is broken in every type, and a false `verbatim` claim is false in every type. The checks are already **self-selecting** — a note that makes no verbatim claim produces no candidates — so a type gate would add configuration without adding reach.

## Open

The referential class has no shared model. Link health and verbatim-quote resolution are separate hand-written passes; they now share one notion of code (`note_parser.blank_fenced_code_blocks`) after a fenced example was found being scanned as a live claim, but the parse model is still positionless — `ParsedDocument.links` is a tuple of URLs with no spans — so the quote checker carries its own link regex. A third referential check would mean a third parser. Tracked in [kb-graph-loader](../work/kb-graph-loader/README.md): a referential check is a graph edge being resolved, so a `LoadedNote` that carries *positioned* elements is what would retire the private parsers.

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why a referential check is obligatory rather than optional, and why a false copy fails where an absent one warns
- [ADR 046 — Verbatim quotes are validated against their cited source](./adr/046-verbatim-quotes-are-validated-against-their-cited-source.md) — evidence: the decision that added the second referential check and surfaced the class
- [ADR 024 — Schema severity is per-constraint, fail by default](./adr/024-schema-severity-is-per-constraint-fail-by-default.md) — evidence: how the `schema` source assigns its own severities
- [Commands](./commands.md) — see-also: the `commonplace-validate` command surface
- [ADR 038 — Type-conformance reviews use the type spec as the gate](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — see-also: the third verification mechanism, where a type spec's prose binds as an LLM-judged criterion at review time
