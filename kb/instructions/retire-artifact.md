---
description: Retire a committed KB artifact — destination lookup, extraction gate, inbound handling, published redirect, and freshness-baseline retirement
type: kb/types/instruction.md
---

# Retire an artifact

**Target: $ARTIFACT_PATH**

Removes a committed artifact from the frontier — the set of files a reader or agent sweeps to find what is live — and leaves nothing dangling behind it: no broken inbound link, no claim delegated to a file that no longer exists, no dead public URL, no freshness baseline pointing at a missing input.

Two destinations. **Delete** is the default. **Archive** moves the file into a sink directory that nothing outside it links into, and is used where the artifact is a design object worth keeping after the decision it fed has shipped. Step 1 tells you which one applies; only steps 6 and 7 differ between them.

## When this does not apply

- **Renaming or moving.** Use `commonplace-relocate-note` or `commonplace-relocate-directory`, which rewrite inbound links for you. Step 9's baseline retirement still applies afterwards: relocation does not re-key or retire baselines, so a rename orphans them exactly as a deletion does.
- **Closing a workshop.** Use the closure protocol in `kb/work/COLLECTION.md` — extract, delete the directory, remove the `kb/work/README.md` entry. Steps 5 and 6 have nothing to act on, since no library artifact links into a workshop, and step 8 is a deliberate non-goal there: workshops are published but their URLs are not durable addresses, so closure leaves them dead on purpose. Step 9 still applies if a workshop file ever carried a baseline, though none has so far.
- **Retiring a term** from the project vocabulary. That is an ADR-scale change affecting every occurrence across the corpus, not a single-artifact operation.

## Steps

1. **Read the target's type spec to find its destination.** Open the file named by the artifact's `type:` frontmatter. If it names an archive directory, the destination is archive and that directory is where the file goes; if it says nothing about retirement, the destination is delete.

   Current assignment — `design-proposal` archives to `kb/reference/proposals/archive/`; every other type deletes.

   If the type spec is silent and you believe archive is right, stop and settle it as a type-level decision rather than deciding per artifact. The test is what survives a complete extraction (steps 2 and 4). Archive when that residue is **irreproducible observation** — dated measurements of a state that no longer exists, which nobody can re-derive at any price. Delete when it is claims: a successor either carries them or falsifies them, and either way nothing is lost.

   Do not archive on the grounds that the artifact holds deliberation. Options weighed, deciding forces, and free choices belong in the superseding ADR's `## Considered alternatives`, which is required precisely so the frontier keeps them ([adr type spec](../reference/types/adr.md)). An artifact whose only residue is deliberation has an incomplete extraction, not an archiving case.

   **Deletion is unrecoverable for consumers without history** — a reader install, an installed project, or a shallow clone cannot see deleted content, so for anything a durable artifact cites the step 4 extraction gate is the only thing standing between delete and permanent loss. Dated measurements that only a decision audit consults are the exception: the ADR keeps the compressed warrant and the full record stays in the implementing commits ([ADR 074](../reference/adr/074-git-is-the-change-history-layer.md)).

2. **Extract first, one piece per commit.** If the artifact holds content worth keeping, move each piece to its new home, retarget that piece's own inbound references, and commit before starting the next. Do not bundle extraction into the retirement — a retirement commit that also moves content cannot be reviewed for either.

   Under the archive destination this step is a gate, not an option. Shipped behavior goes to reference docs, decision-relevant reasoning — options weighed, deciding forces, free choices — to the superseding ADR's `## Considered alternatives`, transferable requirements to `kb/notes/`. What stays behind is the irreproducible remainder: dated current-state anchors and the measurements the design rested on. Deliberation left in an archived file means the extraction is not finished.

3. **Find references that delegate ownership.** Some references do not merely link the artifact; they name it as the owner of a criterion, test, or vocabulary. Retargeting such a link without moving the thing it names leaves a pointer to nothing:

   ```bash
   rg -n '<artifact-slug>' -g '*.md' kb/ | rg -i 'owns|belongs to|criterion|counterexamples|defined in'
   ```

   Each hit needs a successor that actually holds what the sentence claims it holds.

4. **Verify nothing unique remains.** For every claim in the artifact, locate the sentence elsewhere that states it and read that sentence. Do not accept that a successor "covers" a claim without checking its text. If a claim has no home, return to step 2. If it has one that states it worse, fix the successor first.

5. **Inventory inbound references, then stop for approval.**

   ```bash
   rg -c '<artifact-slug>' -g '*.md' kb/
   ```

   Present every reference with the disposition you propose for it and wait for approval before editing anything. Gitignored reports under `kb/reports/connect/` are exempt — leave them.

6. **Handle inbound references — this differs by destination.**

   **Delete:** retarget each reference by what it needs.

   - a frame, an index, or "the X" as a whole → the curated head, `<tag>-README.md`
   - a claim → the artifact that now carries that claim
   - one property → that property's owning note

   In `kb/notes/`, `kb/reference/`, and `kb/instructions/`, rewrite the link text and the footer label context to match the new target; a footer entry whose context describes the old artifact is wrong even when its path resolves. In `kb/sources/*.ingest.md` and `kb/work/`, repoint the path and adjust link text only. Those are dated records of past passes: leave their narratives alone, including recommendations that have since been carried out.

   **Archive:** retarget nothing into the archive. A live inbound link makes an archived document load-bearing again and ends the frontier's completeness, so every remaining reference resolves one of two ways — re-extract what it needs into the frontier and point there, or demote the reference to naming the artifact by title in prose, with no path and no link. An ADR records the proposal it adopted or retired this second way.

   Two link exceptions survive and need no change: the archive's own `README.md`, and files under `kb/work/`, which are deleted rather than accumulated and so cannot durably re-admit archived content.

7. **Dispose — this differs by destination.**

   **Delete:**

   ```bash
   git rm kb/<collection>/<artifact>.md
   ```

   **Archive:**

   ```bash
   git mv kb/<collection>/<artifact>.md <archive-dir>/<artifact>.md
   ```

   Then add a banner immediately below the title, naming the ADR that adopted or retired it, what now carries the live design, and what is left here:

   ```markdown
   > **Archived** (see [archive README](./README.md)). Adopted by [ADR NNN](../../adr/NNN-slug.md): {what carries the live design now}. {What remains here} — design texture only.
   ```

   Use "Retired by" instead of "Adopted by" when a later decision foreclosed the design rather than shipping it. Add a matching entry to the archive `README.md`'s Contents list: title, adopting or retiring ADR, date, and one line on what texture the file holds. Archived files may link out freely; they are frozen afterwards, corrected only for link integrity when something they point at moves.

8. **Add a published redirect.** Both destinations need one — archiving changes the artifact's URL just as deletion ends it. Insert into `redirect_maps` in `properdocs.yml`, keeping the map alphabetical:

   ```yaml
   'notes/<old-slug>.md': 'notes/<successor-slug>.md'
   ```

   Skipping this breaks the artifact's public URL with no local symptom. Point at a page that exists, never at another redirect key — the plugin emits one hop per entry, so a chain lands on a page that only redirects again. If the successor is itself the target of older entries, repoint those to the new page in the same edit. `commonplace-validate redirects` enforces all three conditions.

9. **Retire its baselines.** Both destinations orphan them — the store keys on path, which archiving changes and deletion removes.

   ```bash
   commonplace-freshness-status --missing
   ```

   An artifact that was never reviewed has no baselines and the report will not name it — nothing further to do. If it is named, every pair listed for that path needs retirement, one manifest per target key.

   **Scope the retirement to the retired path.** The report covers the whole store, and this repository already carries orphaned baselines from earlier retirements; retiring everything it lists would destroy unrelated ones. Filter by artifact path:

   ```bash
   RETIRED=kb/notes/<artifact>.md
   commonplace-freshness-status --missing --json \
     | python3 -c '
   import json, sys
   target = sys.argv[1]
   for t in json.load(sys.stdin)["targets"]:
       if any(i["artifact_path"] == target and i["status"] == "input-missing" for i in t["changed_inputs"]):
           print(json.dumps({"schema": "commonplace-freshness-retire/1",
                             "target_kind": t["target_kind"], "target_key": t["target_key"]}))
   ' "$RETIRED" \
     | while IFS= read -r manifest; do printf '%s' "$manifest" | commonplace-freshness-retire --input -; done
   ```

   Each call prints `retired` or `already-absent`; the operation is idempotent, so a re-run is safe.

## Verify

- `commonplace-validate` on each touched artifact — clean, link health in particular.
- `commonplace-validate kb/notes` — no new orphan, and no weight-gate warning on a curated head that absorbed routing.
- `commonplace-freshness-status --missing` — does not name the retired path.
- `rg -l '<artifact-slug>' -g '*.md' kb/` — for delete, nothing outside gitignored reports; for archive, nothing outside the archive directory and `kb/work/`.
- `uv run pytest`

---

Relevant Notes:

- [Freshness architecture](../reference/freshness-architecture.md) — operates-on: the baseline store step 9 mutates
- [Commands](../reference/commands.md) — operates-on: the relocation and freshness command surfaces this procedure calls
- [Proposals](../reference/proposals/README.md) — operates-on: the contract stating which proposals are eligible to archive and what must hold afterwards
- [Indexes lower recall when they suppress retrieval that would find more](../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — rests-on: why a misleading pointer can suppress the fallback that a missing pointer would trigger, which is what steps 3, 6, and 8 guard against
