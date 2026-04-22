# Connect skill redesign: per-destination discovery

> Workshop draft. Depends on the per-destination `COLLECTION.md` files folding into the library.

## Audience

Designing the new `cp-skill-connect` (and retiring the compiled topology it currently depends on) under the link-vocabulary architecture proposed in this workshop.

## What changes and why

The current [cp-skill-connect/SKILL.md](../../instructions/cp-skill-connect/SKILL.md) reads [`kb/reports/collection-topology.md`](../../reports/collection-topology.md) — a compiled register × register linking matrix — and picks relationship labels based on the source-register → target-register pair. The matrix is rebuilt by `cp-skill-compile-collections` from each `COLLECTION.md`'s outbound-linking table.

Two problems with the compiled approach, under the new architecture:

1. **The matrix loses fidelity.** Per-destination rules (`kb/notes/ → kb/reference/` can differ from `kb/notes/ → kb/agent-memory-systems/`) collapse into a single register-to-register cell. The compiled form can't represent the distinctions the new `COLLECTION.md` drafts make.
2. **It adds a drift risk.** Compile-time snapshot vs. live source; the matrix can lag the COLLECTION.md files.

Under the new architecture, the source collection's `COLLECTION.md` has everything the connect skill needs: destination blocks, search guidance per destination, authorised labels per destination. Live read replaces compile; the matrix becomes obsolete.

## Proposed flow

### Input

Unchanged: `$ARGUMENTS` is a note path or name. Determine the source collection from the path.

### Setup

1. Read the target note fully — claim, mechanism, scope, tensions.
2. Read `kb/<source-collection>/COLLECTION.md` — enumerate outbound destination blocks.
3. For each destination block, note:
   - **Search guidance** — when to prospect this destination from the current source.
   - **Authorised labels** — the label set writers may use for links to this destination, with reader-need context.

No read of `kb/reports/collection-topology.md`. That file (and `cp-skill-compile-collections`) can be retired once the fold-in lands.

### Discovery (per destination)

Connect is the skill that pays the cost of active search. Where `cp-skill-write` is bounded to dir-index + already-loaded context + user-named targets (see [`write-skill-design.md`](./write-skill-design.md)), connect runs the full prospecting procedure on every destination block. This is the only place in the KB workflow where body search, tag traversal, and link-following happen in service of linking.

For each destination block in source `COLLECTION.md`:

1. **Apply search guidance.** The guidance names concrete triggers ("when the claim describes behaviour the commonplace system exhibits") and latitude cues ("let the agent filter"). Use these to decide search breadth.
2. **Prospect using repo-local tools, in this order:**
   - Destination's `dir-index.md` (titles + descriptions — the cheapest surface; write already ran this pass, connect re-runs it in case dir-index has moved or write's candidate filter was too tight).
   - Tag indexes, when the source carries tags.
   - `rg` body search for terms and adjacent concepts the destination block names.
   - Link-following from promising candidates (one hop, then re-filter).
3. **Filter via articulation test** — every candidate must complete *"[source] connects to [target] because [specific reason]."*
4. **Label candidates** using the destination's authorised set. Each authorised label carries a reader-need; pick the one whose reader-need matches the connection's purpose. If no authorised label fits, the candidate is either off-scope or the collection author needs to extend the authorisation — surface it separately in the report (see "Off-authorisation candidates" below).

### Output

Same shape as current: report at `kb/reports/connect/<collection>/<note-name>.connect.md`. Sections unchanged (`Connections Found`, `Bidirectional Candidates`, `Raw Text Candidates`, `Rejected Candidates`, `Index Membership`, `Synthesis Opportunities`, `Flags`). Two new sections:

- **Reverse-edge candidates** — first-class. Not every useful link is authored from the source side. For this source, which notes *elsewhere* should link *to* this target? Particularly load-bearing for `kb/agent-memory-systems/` (theoretical notes typically link *into* reviews via `evidence` / `derived-from`), but applies everywhere there's an asymmetric authoring convention. The skill scans for notes in other collections that would legitimately link to the target under their own outbound rules; surfaces them as authoring prompts for the note authors of those source collections. The skill does not edit those notes or write draft links; it names the candidate reverse edges.
- **Off-authorisation candidates** — candidates that passed the articulation test but have no authorised label for the source→destination pair. Signals either (a) the author should extend the authorised set in `COLLECTION.md`, or (b) the candidate is genuinely off-scope and should be rejected. Not presented as draft links.

## What stays the same

- Articulation test for every connection
- Discovery trace capture (indexes read, queries, candidate evaluations)
- Bidirectional candidates (return links worth adding)
- Raw text candidates (targets without frontmatter)
- Quality gates (path verification, load-bearing links to seedlings)
- Never mutate library artifacts (report-only)
- Reflection into `kb/log.md` for stale links, errors, tensions noticed

## What changes

| aspect | current | new |
|---|---|---|
| Linking rules source | compiled `collection-topology.md` | live per-destination blocks in source `COLLECTION.md` |
| Organising axis | register × register matrix | source → destination (one block per destination) |
| Label selection | one set per register pair | one set per source→destination pair |
| Search strategy | uniform across all collections | per-destination search guidance from source `COLLECTION.md` |
| Drift risk | compile step can lag source | live read; no intermediate artifact |
| Off-scope candidates | no explicit handling | surfaced in a dedicated report section as authoring-signal |

## Sequencing

The skill rewrite depends on the library having the new `COLLECTION.md` files:

1. Fold the workshop's four `COLLECTION.md` drafts into their library locations.
2. Fold `link-vocabulary.md` into `kb/reference/link-vocabulary.md`.
3. Rewrite `cp-skill-connect/SKILL.md` per this design.
4. Delete `kb/reports/collection-topology.md` and remove `cp-skill-compile-collections` (or repurpose it if another consumer emerges — currently the topology report's only consumer is the connect skill).

## Open questions

- **How does the skill parse `COLLECTION.md`?** Options: (a) convention-based — destination blocks are `### → ` headers under `## Outbound linking conventions`, search guidance is a `**Search:** ...` line, labels are in a markdown table; (b) an explicit YAML block inside `COLLECTION.md` for machine-readable rules; (c) let the model interpret the whole outbound section. Preference: (c) for v1 — cheaper, works today, degrades gracefully if a `COLLECTION.md` diverges in formatting. Revisit if parsing becomes brittle.

- **Instructions' strict frontloading posture.** `instructions-COLLECTION.md` authorises only `rationale` (→ notes) and `operates-on` (→ reference) for outbound, both with audience disclaimers (meta-readers, not execution). The connect skill should respect this: when prospecting from an instruction, only surface candidates that fit these narrow labels, and annotate them as meta-reader edges. Don't propose `see-also` sprays from instructions.

- **Off-authorisation candidates.** When a candidate passes the articulation test but has no authorised label, should the skill: (a) silently drop it, (b) list it in the "Off-authorisation candidates" section with a suggestion to extend authorisation, or (c) propose a label anyway with an audit flag? Proposal: (b) — surface it; authoring signal is valuable.

- **Search latitude.** `link-vocabulary.md` says "prefer slight over-retrieval." In practice, how much? Proposal: scan every destination's `dir-index.md` fully (cheap), run focused body search on each destination for named concepts, follow one hop of link-following from promising candidates. No hard cap on candidates — the articulation test is the filter.

- **Agent-memory-systems asymmetry.** Theoretical notes most often link *into* this collection via `evidence` / `derived-from`; from this collection, `rationale` and rare `evidence` are authorised. This is the canonical case where Reverse-edge candidates (above) are load-bearing. The skill must be able to compute the reverse direction: for a target in agent-memory-systems, scan `kb/notes/` outbound rules for labels targeting descriptive collections and surface notes that could plausibly author such an edge. Similar asymmetries likely exist elsewhere; the skill's reverse-edge logic should be general.

## Related

- [README.md](./README.md) — workshop overview
- [link-vocabulary.md](./link-vocabulary.md) — catalogue and authoring guidance
- [instructions-COLLECTION.md](./instructions-COLLECTION.md) — strict outbound policy to respect
- [notes-COLLECTION.md](./notes-COLLECTION.md), [reference-COLLECTION.md](./reference-COLLECTION.md), [agent-memory-systems-COLLECTION.md](./agent-memory-systems-COLLECTION.md) — per-destination search guidance the new skill consumes
