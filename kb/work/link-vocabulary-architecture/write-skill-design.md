# Write skill update: link guidance defers to COLLECTION.md

> Workshop draft. Depends on the per-destination `COLLECTION.md` files folding into the library.

## Audience

Updating `cp-skill-write` to match the link-vocabulary architecture proposed in this workshop.

## What changes and why

Current [`cp-skill-write/SKILL.md`](../../instructions/cp-skill-write/SKILL.md) teaches linking at the skill level — the **Universal Mechanics → Links** paragraph embeds a five-label set (`extends`, `foundation`, `contradicts`, `enables`, `example`). That list is stale against ADR 018 draft (no `mechanism` / `contrasts`) and — more importantly — bypasses the architecture this workshop proposes. Under per-destination `COLLECTION.md` blocks, authorised labels vary by source → destination pair; no universal list captures that.

Two problems with the current skill:

1. **Vocabulary duplication.** The skill teaches labels; `COLLECTION.md` authorises labels; they disagree silently.
2. **Search blind spot.** Step 4 (Search Before Writing) searches the target collection and `kb/notes/`, ignoring the per-destination search guidance now declared in `COLLECTION.md`. The skill misses candidate links from collections that explicitly support them.

Fix: defer linking authority to `COLLECTION.md`. The skill directs the writer to read per-destination blocks and pick labels from the authorised set. No embedded label list.

## Proposed edits

### Step 2 (Load Collection Conventions) — reframe

Current: "Read `kb/<collection>/COLLECTION.md` for the collection's writing conventions."

Replace with: "Read `kb/<collection>/COLLECTION.md` for the collection's writing conventions, including outbound-linking rules. Each destination block declares when to prospect that destination for link candidates and which labels you may use with what reader-need. Treat it as authoritative — no separate linking doc to consult."

### Step 4 (Search Before Writing) — narrow and make explicit

Current: "Search the target collection first, then `kb/notes/` if different."

Replace with:

> Unless the user requests otherwise, the write flow does not run active discovery. Link candidates come from three cheap sources, in order:
>
> 1. **Destination `dir-index.md`.** For each destination block in the source `COLLECTION.md`, read that destination's `dir-index.md` once. Titles and descriptions are the full surface — enough to catch near-duplicates in the target collection and enough to surface obvious connection points in other destinations. Do not open candidate notes to inspect their bodies unless the dir-index line itself is a match.
> 2. **Context already loaded.** Notes, sources, and ingests that were pulled into the session for this write are first-class candidates. If it was worth reading, it is worth considering as a link.
> 3. **User-named targets.** Link targets the user mentions in the prompt.
>
> In edit mode, also run the backlinks lookup on the target note — one query, no body search — so edits don't orphan dependents.

### Universal Mechanics → Links — rewrite

Current:

> **Links** use relative markdown paths from the source file. Prefer inline links as prose. Footer links for connections outside prose should carry a relationship annotation (`extends`, `foundation`, `contradicts`, `enables`, `example`). Every link must point to a real file.

Replace with:

> **Links.** Use relative markdown paths from the source file. Every link must point to a real file.
>
> Position encodes commitment. **Inline** prose connectors (`since [X](./x.md)`, `because [X](./x.md)`, `but [X](./x.md)`) are strongest — the target is a premise of the current argument. **Footer** links carry an explicit label + context phrase: `- [title](./path.md) — label: context phrase`.
>
> The collection's `COLLECTION.md` authorises labels per destination and names the reader-need each label serves. Pick a label whose reader-need matches the link's purpose; write the context phrase to answer *"[source] connects to [target] because [specific reason]."* If no authorised label fits, the candidate is off-scope for this collection — drop the link or ask the collection author to extend the authorisation.

### Suggest `cp-skill-connect` — load-bearing

Already in Step 6. Under the narrowed Step 4 this suggestion is no longer optional polish; it is how the note gets its full share of the graph. Write's Step 4 commits links that the author already has reason to believe in (dir-index, loaded context, user-named). Connect is the only path to candidates that require body search, tag traversal, link-following, or reverse-edge reasoning. The skill should say so — not "consider running connect later," but "connect is where the rest of your links come from."

## What stays the same

- The write flow (parse → load conventions → load type spec → search → draft → validate)
- Hard-fail on missing `COLLECTION.md`
- Articulation test as the filter for every link
- Inline vs footer distinction
- Frontmatter, description, filename, distillation-tracking, and rename mechanics

## Sequencing

Depends on the per-destination `COLLECTION.md` drafts being in the library:

1. Fold workshop's four `COLLECTION.md` drafts into their library locations.
2. Fold `link-vocabulary.md` into `kb/reference/link-vocabulary.md`.
3. Apply the edits above to `cp-skill-write/SKILL.md`. The skill no longer needs a compressed-vocabulary block to embed.

Coordinate with [`connect-skill-design.md`](./connect-skill-design.md) — both skills now read `COLLECTION.md` directly; the rewrites can land together.

## Open questions

- **Does `cp-skill-write` need any cached summary of per-destination rules, or is a live `COLLECTION.md` read every write-session fine?** Proposal: live read. `COLLECTION.md` is small and already loaded in Step 2.
- **What if a writer wants to link to a destination the source `COLLECTION.md` doesn't list?** Mirror the connect-skill design: don't author the link; flag it so the collection author can decide to extend the authorisation. Concretely: the writer can add a `<!-- pending destination: X -->` HTML comment or just raise the question to the collection author.
- **Teaching vs doing.** Previously a compressed vocabulary block was being staged for embedding into `cp-skill-write`. Under this proposal the block is retired — the skill points at `COLLECTION.md`, which has per-destination guidance. No separate writer-facing linking doc.
- **Revise flow.** `cp-skill-revise` (if present) has the same vocabulary-teaching problem. Worth auditing in a follow-up; same fix should apply.

## Related

- [README.md](./README.md) — workshop overview
- [connect-skill-design.md](./connect-skill-design.md) — parallel redesign for the connect skill; both skills consume `COLLECTION.md` directly
- [link-vocabulary.md](./link-vocabulary.md) — catalogue and authoring guidance for `COLLECTION.md` authors (not writers)
