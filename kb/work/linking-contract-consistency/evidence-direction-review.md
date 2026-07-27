# Evidence direction review

## Question

Do the authorized source/review → note uses of `evidence` represent accidental mislabelling that should be removed, or a recurring inverse reader journey that has earned its own directional label?

The shared catalogue currently defines `evidence` as asymmetric, with the authored journey running from a theoretical claim to a descriptive observation. The live source and agent-memory contracts also authorize `evidence` in the reverse direction, from an evidence-bearing analysis or review to a theory note.

## Method

The review extracted Markdown footer links whose immediate label is `evidence`, accepting both the current em dash form and older double-hyphen form. It resolved each relative target and selected:

- `kb/sources/` → `kb/notes/`;
- `kb/agent-memory-systems/` → `kb/notes/`.

For each selected edge, it read the containing artifact's connection/relevance section, recommended action where present, and target-side links back to the source artifact. Generated reports and workshop copies were not treated as authorizations or durable library evidence.

## Corpus result

The review found **26 edges across 7 source artifacts and 20 target notes**:

| source artifact | shape | source→note `evidence` edges | target links back |
|---|---|---:|---:|
| [Language Models Don't Always Say What They Think ingest](../../sources/language-models-dont-always-say-what-they-think.ingest.md) | ingest report | 4 | 1 |
| [Gödel Machines ingest](../../sources/goedel-machines-schmidhuber.ingest.md) | ingest report | 5 | 1 |
| [Ashby ultrastability](../../sources/ashby-design-for-a-brain-ultrastability.md) | source review | 4 | 3 |
| [In Search of Lost Domain Generalization ingest](../../sources/in-search-of-lost-domain-generalization.ingest.md) | ingest report | 3 | 1 |
| [Towards Faithfully Interpretable NLP Systems ingest](../../sources/towards-faithfully-interpretable-nlp-systems.ingest.md) | ingest report | 3 | 1 |
| [FALSIFYBENCH ingest](../../sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md) | ingest report | 5 | 0 |
| [Fintool review](../../agent-memory-systems/lightweight/fintool.md) | agent-memory review | 2 | 0 |

Of the 26 edges:

- **19 have no target→source return link**;
- **6 have a reciprocal target→source `evidence` footer**, sometimes alongside an inline citation;
- **1 has a target→source `abstracted-from` footer** plus an inline citation.

The concentration is informative. This is not a long-established corpus-wide convention, but neither is it one accidental edge: it recurs across three artifact shapes, with ingest reports contributing 20 edges, a source review 4, and an agent-memory review 2.

## What the links actually do

### They map a source into the claim landscape

The dominant reader journey is:

> I am reading an analysis of this source or system; show me the KB claims that this observation supports, qualifies, bounds, or instantiates.

That journey is native to the artifact contracts. An ingest report exists to record how a source fits the KB; its `Connections Found` section keeps settled, durable connection judgments. A source review explains relevance to the KB. An agent-memory review closes with relevant theory and borrowable implications.

Examples span several evidential roles:

- **Direct corroboration:** Fintool's S3 source-of-truth and derived PostgreSQL index bear on [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md).
- **Formal limit case:** the Gödel machine bears on [the boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) by making the verification boundary constructive.
- **Negative or floor case:** Ashby's Homeostat bears on [reflective system](../../notes/definitions/reflective-system.md) precisely because it adapts without self-representation.
- **Qualification:** DomainBed bears on the formalization-boundary warning in [formal symbolic systems assess explanatory-reach only through causal and proof obligations](../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md).
- **Pending target integration:** the FALSIFYBENCH ingest records five evidence-bearing connections while explicitly saying some target-side evidence edges should follow only after the full paper is read.

The final case is important: a source-side edge can assert that evidence bears on a claim without asserting that the target note has already incorporated, cited, or accepted it.

### They are not lineage edges

Most target notes pre-exist the source analysis, and their substantive claims are not reconstructible from these source artifacts. Relabelling the edges `derived-from` or `abstracted-from` would falsely assert an origin or maintenance regime. The source is corroboration, counterweight, boundary evidence, or an instance—not the generator of the target.

### They are not mandatory reciprocal links

Only 7 of 26 target notes link back at all. Where both directions exist, each serves a distinct reader:

- note → source: inspect the observation that warrants or qualifies the claim;
- source analysis → note: see where this observation lands in the KB's theory.

The 19 one-sided cases show that source-side authors did not merely mirror a target citation. Conversely, the reciprocal cases are useful two-way navigation when both reader needs are present.

## Finding

The inverse journey is real and recurring, so removing source/review → note authorization would discard part of what source analyses are for. But retaining `evidence` in both directions makes an explicitly asymmetric label ambiguous.

The existing label also collapses two different statements:

1. **This claim points to evidence it uses or wants the reader to inspect.**
2. **This source bears on that claim, whether or not the claim has incorporated it yet.**

The distinction matters operationally. The second statement can be authored during ingestion and become a future update signal; it is not proof of target-side uptake.

## Recommendation

Retain both reader journeys, but defer naming them until the vocabulary adopts a consistent directional grammar. The proposed `evidence-for` identifier is withdrawn: without a global grammatical rule it does not say reliably whether the source is evidence for the target or the target supplies evidence for the source.

The workshop's candidate invariant is now documented in [directional label grammar](./directional-label-grammar.md): every directional identifier must complete `source <label> target`. Under that rule, the current `evidence` identifier also needs review because its declared meaning is “target is evidence for source.” The leading replacement pair is `evidenced-by` / `is-evidence-for`: both make the source endpoint their grammatical subject. It remains provisional until the whole asymmetric-label audit tests its boundary against neighboring relations.

Whatever names are selected, the semantic boundary established here remains:

| journey | reader need | assertion boundary |
|---|---|---|
| claim or descriptive assertion → corroborating observation/source | “show me the observation bearing on this assertion” | The target artifact is worth inspecting as warrant, qualification, or boundary evidence. |
| evidence-bearing source/review → claim | “show me the claim this observation bears on” | The source bears materially on the target claim; it does **not** assert that the target already cites, incorporates, or accepts it. |

Both relations are asymmetric. Authoring either remains an independent reader-aid decision, and a reciprocal pair is allowed only when both journeys help.

## Proposed changes, not yet applied

1. Audit every asymmetric label against `source <label> target`.
2. Test the leading `evidenced-by` / `is-evidence-for` pair against overlap with `grounds`, existing `supports` drift, and qualification/boundary evidence.
3. Clarify that the claim/description → source journey is not restricted to the theoretical register; `kb/reference/` and external-system analyses already use it coherently.
4. Update the shared catalogue and affected collection contracts together.
5. Migrate the 26 reviewed inverse edges and any renamed claim→observation edges only after the target grammar is adopted.

## Decision status

The two reader journeys are established from corpus evidence; `evidenced-by` / `is-evidence-for` is the leading identifier pair but is not adopted. The next step is the full directional-label grammar audit, followed by one coordinated vocabulary, collection-contract, and corpus migration proposal.
