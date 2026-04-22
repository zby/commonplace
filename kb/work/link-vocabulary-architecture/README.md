# Link vocabulary architecture

## Question

Link vocabulary currently lives in several places that disagree: [ADR 009](../../reference/adr/009-link-relationship-semantics.md) declares five canonical labels (extended toward seven in [ADR 018 draft](./adr-018-draft.md)); each `COLLECTION.md` has an outbound table; and [`linking-conventions.md`](./linking-conventions.md) compresses the vocabulary for embedding in `cp-skill-write`. The existing design treats the seven labels as universal and lets `COLLECTION.md` narrow per edge. An alternative architecture fits the observed drift better and serves the connect skill's needs: **each `COLLECTION.md` declares outbound rules per destination collection** (search guidance + authorised labels), selecting from a shared [link-vocabulary.md](./link-vocabulary.md) catalogue. The theory of links is weak; per-destination rules enable fine-grained experimentation and give the connect skill a concrete map of where to search for link targets.

("Register" throughout this workshop means one of three content modes — theoretical, descriptive, prescriptive — that determines a collection's quality goal, title conventions, and linking rules. See [`register`](../../notes/definitions/register.md).)

This workshop drafts the files that would live under the alternative: four proposed `COLLECTION.md` revisions and one authoring resource (`link-vocabulary.md`) with a label catalogue plus guidance on per-destination authoring.

## Theoretical grounding

The architecture is justified by [`links-as-possibility.md`](./links-as-possibility.md):

- Links are bets on reader state — the subset of readers with an unmet need. Required content is inlined, not linked.
- Every label names the reader-need the link serves (the condition under which following pays off). Labels that only describe document relationships fail the test.
- Two reader classes (agent, human); this KB optimises for agents because their context state is predictable and humans can follow the agent path. Parallel vocabularies are not maintained.

Each label in the proposed vocabularies is retrofitted against this theory in [`label-audit.md`](./label-audit.md). The audit drives the drop/merge decisions below.

## Key moves from the conversation that spawned this workshop

1. **Vocabulary is a property of the artifact, not the authoring procedure.** Canonical definition lives in durable, tooling-accessible files (`COLLECTION.md`, type definitions, the catalogue), not inside the writing skill. The skill *teaches* the vocabulary by importing/quoting it.

2. **Collection, not register, is the anchor.** Each `COLLECTION.md` is the authoritative source for its outbound link rules. Register-level groupings in the catalogue are advisory — they help find labels that match a source's shape. Collections experiment freely. For the writer authoring a note, there is one source of truth: the `COLLECTION.md` of their collection. No upward traversal. Role stays read-time and doesn't anchor anywhere.

3. **Per-destination organisation.** Outbound rules in each `COLLECTION.md` are grouped by destination collection, not by register. Each destination block declares (a) search guidance for the connect skill — when to prospect that destination for link targets — and (b) authorised labels with collection-specific reader-need context. This serves two motives: it enables fine-grained experimentation (`kb/notes/ → kb/reference/` can diverge from `kb/notes/ → kb/agent-memory-systems/`), and it gives the connect skill a concrete map of where to search.

4. **Three layers, collection-owned:**
   - **Collection grammar** — `COLLECTION.md`, authoritative and self-contained, organised per destination. Single source of truth for note writers and for the connect skill.
   - **Authoring resource** — [`link-vocabulary.md`](./link-vocabulary.md): label catalogue plus authoring guidance. Referenced when authoring or reviewing a `COLLECTION.md`, not when writing a note. Deliberately lowercase filename — narrow audience, not a top-level "read me."
   - **Type-specific overrides** — type definition, only for specialised types that genuinely diverge (`definition`, `index`, `adr`).

5. **Labels must name reader-needs, not document relations.** Retrofitted against this in [`label-audit.md`](./label-audit.md). Drops: `cross-reference`. Merge: `rationale` + `justification` → `rationale`. Fold: `describes` → `part-of` / `see-also`.

## What this workshop proposes that's different from current state

- Each `COLLECTION.md` reorganises its outbound-linking section **per destination collection** rather than by register. Each destination block carries search guidance + authorised labels. Connect skill reads this directly.
- The seven labels from ADR 009/018 go into a shared catalogue tagged "theoretical-shaped" — common starting set for theoretical sources, not a universal vocabulary.
- Descriptive and prescriptive label clusters added to the catalogue. Collections pick and mix per destination.
- Cross-collection labels (`rationale`, `evidence`, `procedure`, `operates-on`, etc.) go into the same catalogue, not a separate cross-register document.
- Leave `cp-skill-write`'s linking section as a pedagogical surface that *quotes* the authoring collection's `COLLECTION.md`, not the canonical home.

## Relation to existing work

- [ADR 009](../../reference/adr/009-link-relationship-semantics.md) — declares five canonical labels. Under this proposal, ADR 009 records the default template for theoretical collections. `kb/notes/` adopts it; future theoretical collections may copy and adapt.
- [ADR 018 draft](./adr-018-draft.md) — proposes `mechanism` and `contrasts`. Complementary: extensions fit inside the theoretical register's default template.
- [`linking-conventions.md`](./linking-conventions.md) — operational distillation. Under this proposal, the skill still carries a teaching version, but defers to the authoring collection's `COLLECTION.md` and the shared cross-register toolkit for canonical definitions.
- [`linking-theory.md`](../../notes/linking-theory.md) open question *"Is the vocabulary the right one?"* — reframes to *"one universal vocabulary, or a shared catalogue with per-destination selections in each collection?"*
- [`findings.md`](./findings.md) — corpus drift analysis (3420 footer links, 236 distinct labels) that drove `mechanism` and `contrasts` adoption. Informs which labels the register-level defaults should include.

## Plan

1. Draft the authoring resource — `link-vocabulary.md` — label catalogue plus per-destination authoring guidance.
2. Draft proposed COLLECTION.md for each of the four collections (notes, reference, instructions, agent-memory-systems) with per-destination outbound blocks.
3. Ground the vocabulary in reader-need theory — `links-as-possibility.md`.
4. Retrofit each label against the theory — `label-audit.md`.
5. Apply audit recommendations to the proposed drafts (drops, merges, folds).
6. Design the consuming connect skill for per-destination discovery — [`connect-skill-design.md`](./connect-skill-design.md).
7. Decide: fold into library, iterate, or abandon.

## What closes this workshop

- Four proposed `COLLECTION.md` revisions reviewed; each either merged into library or rejected with reasons.
- A decision about where `link-vocabulary.md` lives in the library (candidates: `kb/reference/link-vocabulary.md`, absorbed into `kb/notes/links-index.md`, or split between `kb/reference/` and `kb/instructions/`).
- `cp-skill-connect/SKILL.md` rewritten per [`connect-skill-design.md`](./connect-skill-design.md); `kb/reports/collection-topology.md` and `cp-skill-compile-collections` retired.
- ADR 009 either updated, superseded, or explicitly left as-is with rationale for how it composes with this architecture.
