---
description: Delete a committed KB artifact whose content has been absorbed elsewhere — ownership check, inbound retargeting, published redirect, and freshness-baseline retirement
type: kb/types/instruction.md
---

# Retire an artifact

**Target: $ARTIFACT_PATH**

Removes a committed artifact from the KB and leaves nothing dangling behind it: no broken inbound link, no claim delegated to a file that no longer exists, no dead public URL, no freshness baseline pointing at a missing input.

## When this does not apply

- **Renaming or moving.** Use `commonplace-relocate-note` or `commonplace-relocate-directory`, which rewrite inbound links for you. Step 7's baseline retirement still applies afterwards: relocation does not re-key or retire baselines, so a rename orphans them exactly as a deletion does.
- **Retiring a term** from the project vocabulary. That is an ADR-scale change affecting every occurrence across the corpus, not a single-artifact operation.

## Steps

1. **Extract first, one piece per commit.** If the artifact holds content worth keeping, move each piece to its new home, retarget that piece's own inbound references, and commit before starting the next. Do not bundle extraction into the retirement — a retirement commit that also moves content cannot be reviewed for either.

2. **Find references that delegate ownership.** Some references do not merely link the artifact; they name it as the owner of a criterion, test, or vocabulary. Retargeting such a link without moving the thing it names leaves a pointer to nothing:

   ```bash
   rg -n '<artifact-slug>' -g '*.md' kb/ | rg -i 'owns|belongs to|criterion|counterexamples|defined in'
   ```

   Each hit needs a successor that actually holds what the sentence claims it holds.

3. **Verify nothing unique remains.** For every claim in the artifact, locate the sentence elsewhere that states it and read that sentence. Do not accept that a successor "covers" a claim without checking its text. If a claim has no home, return to step 1. If it has one that states it worse, fix the successor first.

4. **Inventory inbound references, then stop for approval.**

   ```bash
   rg -c '<artifact-slug>' -g '*.md' kb/
   ```

   Present every reference with the target you propose for it and wait for approval before editing anything. Gitignored reports under `kb/reports/connect/` are exempt — leave them.

5. **Retarget by what each reference needs.**

   - a frame, an index, or "the X" as a whole → the curated head, `<tag>-README.md`
   - a claim → the artifact that now carries that claim
   - one property → that property's owning note

   In `kb/notes/`, `kb/reference/`, and `kb/instructions/`, rewrite the link text and the footer label context to match the new target; a footer entry whose context describes the old artifact is wrong even when its path resolves. In `kb/sources/*.ingest.md` and `kb/work/`, repoint the path and adjust link text only. Those are dated records of past passes: leave their narratives alone, including recommendations that have since been carried out.

6. **Add a published redirect.** Insert into `redirect_maps` in `properdocs.yml`, keeping the map alphabetical:

   ```yaml
   'notes/<old-slug>.md': 'notes/<successor-slug>.md'
   ```

   Skipping this breaks the artifact's public URL with no local symptom.

7. **Delete, then retire its baselines.**

   ```bash
   git rm kb/<collection>/<artifact>.md
   commonplace-freshness-status --missing
   ```

   An artifact that was never reviewed has no baselines and the report will not name it — nothing further to do. If it is named, every pair listed for that path needs retirement, one manifest per target key.

   **Scope the retirement to the deleted path.** The report covers the whole store, and this repository already carries orphaned baselines from earlier retirements; retiring everything it lists would destroy unrelated ones. Filter by artifact path:

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
- `rg -l '<artifact-slug>' -g '*.md' kb/` — nothing outside gitignored reports.
- `pytest`

---

Relevant Notes:

- [Freshness architecture](../reference/freshness-architecture.md) — operates-on: the baseline store step 7 mutates
- [Commands](../reference/commands.md) — operates-on: the relocation and freshness command surfaces this procedure calls
- [Stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) — rationale: why a dangling pointer costs more than a missing one, which is what steps 2, 5, and 6 are paying for
