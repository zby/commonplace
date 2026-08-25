---
description: "The base, type-rule, and schema sources of deterministic findings, their dereferencing limits, and the run-scoped execution model"
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

The explicit `landings` and `redirects` targets are outside this note pipeline. Both emit `[repository]` findings. `landings` checks that every top-level collection has a `README.md` and that no sibling `index.md` shadows it. `redirects` compares `properdocs.yml` with the live `docs_dir`: targets resolve, keys do not shadow pages, and the map is flat. Keeping these checks explicit prevents validation of one note or collection from failing on unrelated site configuration while still making the published-tree invariants deterministic.

## Scope: this is the deterministic half only

A type is verified by **three** mechanisms, and only the first two are the validator's:

| | Mechanism | When | Judges meaning? |
|---|---|---|---|
| 1 | `schema` — declarative JSON Schema | validate time | no |
| 2 | `type_rule` — imperative code the type registers | validate time | no |
| 3 | **type-conformance review gate** — the type spec's *body text* is the criterion, read by an LLM ([ADR 038](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)) | review time | yes |

This page documents 1 and 2. The third is not a lesser mechanism: **a type spec's natural-language instructions are an executable criterion, not documentation.** Everything a schema cannot express still binds — it binds at review time. That is why [`type-spec.md`](../types/type-spec.md) tells authors *not* to restate schema rules in body text: the schema already enforces them, so a restatement only spends reviewer judgment re-confirming what is already guaranteed, instead of on the properties only a reviewer can check.

## The three sources of a validator finding

| Source | Owner | Mechanism | Can dereference? |
|---|---|---|---|
| `base` | framework | imperative, applies to every typed note; repository-boundary rules may also cover bare library text | yes — link health, archive boundary, verbatim quotes |
| `type: <name>` | the type | imperative rules registered for that type | yes — tag-readme marks re-derive from the collection; type specs resolve their declared schemas |
| `schema` | the type | declarative JSON Schema over the parsed document | **no** |

**A type is not verified by its schema alone.** `tag-readme` proves it: its `complete` mark is checked by re-walking the collection and re-deriving membership from every tagged note — imperative, dereferencing, and impossible to express in a schema. `type-spec` supplies a smaller example: `type-spec.schema.yaml` can constrain the `schema:` field's shape, but an imperative rule must follow a non-null path and load the declared schema. So *who owns a rule* and *whether it dereferences* are independent axes, which is why the table has no empty cells and why "schema versus everything else" is the wrong mental model.

Type-spec documents are ordinary validation artifacts. Collection validation includes local type specs, and `commonplace-validate types` runs the same base, type-rule, and schema pipeline over the complete global and local type inventory. There is no separate type-system validation pass.

Imperative rules select types by canonical path, not by the type spec's bare `name`. An installed framework path under `kb/commonplace/` normalizes to its source identity, while a same-named collection-local type remains distinct ([ADR 048](./adr/048-imperative-type-rules-dispatch-by-canonical-path.md)). Reports still use the shorter `type: <name>` label because a display label is not an identity key.

## What the schema can and cannot express

The schema is **not** limited to frontmatter. `ParsedDocument.to_validation_object()` hands it `frontmatter`, `body`, `headings`, `links`, and `body_dates`, so a type can require a `## Reasoning` heading or constrain body content declaratively, and several do.

What a schema cannot do is **dereference** — it has no way to say *follow this path and look inside the artifact it names*. JSON Schema validates one instance document; the referent is another file. This is an inherited limit of the substrate, not a gap worth closing, and it is the whole reason a second, imperative check mechanism exists at all.

So the dividing line is not frontmatter/body. It is **intra-document** (declarable) versus **referential** (must be executed). A referential check's ground truth lives in a second artifact, which is precondition 3 of [a derived copy of recomputable truth must be checked or absent](../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — the rule that makes these checks obligatory rather than optional.

## The base contract

Every note **with frontmatter** is checked for the following, whatever its type. A type spec does not declare these and cannot opt out of them.

- **Frontmatter parses** — valid delimiters, well-formed YAML.
- **Title length** within `MAX_NOTE_TITLE_LENGTH`; **filename slug length** within `MAX_NOTE_SLUG_LENGTH` (derived-artifact types are exempt from the slug limit).
- **Link health** — every local relative link resolves to an existing target. *Warns.*
- **Proposal archive boundary** — no library artifact links to a file under `kb/reference/proposals/archive/`. The archive README is a permitted target and may link to archived files itself; workshop files under `kb/work/` may also link in. Violations **fail**.
- **Verbatim quotes** — every `verbatim`-marked quotation resolves against the source it links ([ADR 046](./adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)). A quote absent from its cited source **fails**; an unpairable verbatim citation warns, but only in notes that demonstrably use the convention.
- **Ingest snapshot pairing** — when an ignored local snapshot is retained, its name-paired path, source URL, and exact-byte checksum must agree with the tracked ingest. A mismatch warns; when the recorded bytes exist under another filename, the warning locates them without treating that path as mutation authority. For a legacy ingest without a checksum, the source URL may locate a related capture but cannot establish exact-byte identity. Complete cache absence is silent.
- **Source quotes** — every `Source extract (verbatim)` in a tracked ingest's `## Quotes` section occurs in its checksum-verified name-paired snapshot. A false extract **fails**. The check is conditional on local retention; an absent or mismatched observation is not used to judge the extract.

**Bare text opts out of structural checks.** A file with no frontmatter is typed `text` and gets no title, slug, link-health, quote, type, or schema requirements — deliberate, because `text` keeps capture friction at zero and may hold imported material whose relative links are broken by construction. The proposal archive boundary is the one repository-level exception: bare library READMEs can otherwise make archived designs load-bearing just as readily as typed notes. Non-library outputs such as `kb/reports/` remain outside that rule.

A `kb/sources` collection sweep also audits the retained local snapshot cache.
It indexes exact ingest `source` URL values independently of checksums so legacy
checksum-less ingests and changed observations remain visibly related. A
derived ingest may also own exact precursor bytes through
`original_snapshot_sha256`; this accounts for a retained translation input
without pretending it is the ingest's primary observation. The sweep warns
about a Markdown snapshot that has no same-stem ingest and no URL or checksum
match, and about redundant alternate copies of an already valid pair. A
checksum-owned alternate that reveals path drift is reported on the affected
ingest instead, so one condition produces one warning.

### Why the two referential checks have different severities

Link health **warns**; a false verbatim quote **fails**. That asymmetry is the derived-copy rule, not an inconsistency. A dangling link costs the reader a bounded, recoverable search. A false verbatim quote tells the reader the text was checked when it was not — it *suppresses* the verification it claims to have done, which is silent and unbounded. Absence degrades; a false copy corrupts.

### Why the base checks are not type-configurable

Letting a type opt out of link health or verbatim-quote resolution would be a knob that can only ever be set wrong: a broken link is broken in every type, and a false `verbatim` claim is false in every type. The checks are already **self-selecting** — a note that makes no verbatim claim produces no candidates — so a type gate would add configuration without adding reach.

## Open

[ADR 050](./adr/050-validation-runs-share-parsed-artifacts-and-collection-indexes.md) gives referential checks a shared execution context: one validation run caches parsed artifacts and collection tag indexes and builds the authored-link graph once. It does not give Markdown elements a shared positioned representation. Link health and verbatim-quote resolution remain separate hand-written passes; they share one notion of code (`note_parser.blank_fenced_code_blocks`), but `ParsedDocument.links` is still a tuple of URLs with no spans, so the quote checker carries its own link regex. A third positioned referential check could still mean a third parser. Tracked in the kb-graph-loader workshop: a `LoadedNote` carrying *positioned* elements is what would retire those private parsers.

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: why a referential check is obligatory rather than optional, and why a false copy fails where an absent one warns
- [ADR 046 — Verbatim quotes are validated against their cited source](./adr/046-verbatim-quotes-are-validated-against-their-cited-source.md) — evidenced-by: the decision that added the second referential check and surfaced the class
- [ADR 024 — Schema severity is per-constraint, fail by default](./adr/024-schema-severity-is-per-constraint-fail-by-default.md) — evidenced-by: how the `schema` source assigns its own severities
- [Commands](./commands.md) — see-also: the `commonplace-validate` command surface
- [ADR 038 — Type-conformance reviews use the type spec as the gate](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — see-also: the third verification mechanism, where a type spec's natural-language instructions bind as an LLM-judged criterion at review time
- [ADR 050 — Validation runs share parsed artifacts and collection indexes](./adr/050-validation-runs-share-parsed-artifacts-and-collection-indexes.md) — implemented-by: artifact-local and collection-indexed checks share one execution context without a generic dependency engine
