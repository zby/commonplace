# Old-Note Triage Prompt

Use this procedure to triage one old note (either a historical path from [february-28.tsv](./february-28.tsv) or a live KB path) and recommend a concrete disposition.

## Intent and boundaries

- **Goal:** Start from the number-one question—**what role does this note play in the whole KB?**—evaluating how it serves the KB goal (`AGENTS.md`), its collection's goal (`COLLECTION.md`), and whether it helps address the KB's highest-value open gaps, especially [What gaps remain in our learning loop?](../../theory/questions/what-gaps-remain-in-our-learning-loop.md) (and sibling standing questions). From that role, check whether its claims and placement hold and recommend a concrete disposition, including which inbound citations would break or mislead if it changes.
- **Authority boundary (read-only triage):** Do **not** edit library notes, relocate files, retire artifacts, or run paid `commonplace-review` passes during triage unless the caller explicitly authorizes execution. Produce a grounded recommendation only.
- **Separation of states:** Keep **coverage** (traced vs. untraced), **judgment** (recommended verdict), and **execution** (completed edits) strictly separate.
- **No shortcuts:** Do not judge from the title alone, do not equate low inbound links with uselessness or high inbound links with soundness, do not keep a note merely because its prose is locally true without a KB role, and never claim a successor "covers" a note without reading the successor's actual text.

## Inputs

- `TARGET`: a historical path from the inventory (e.g. `kb/notes/<slug>.md`) or a current live path (e.g. `kb/theory/<slug>.md`).
- Optional `INVENTORY`: [february-28.tsv](./february-28.tsv) (to check for shared successors and avoid double-counting).

## Step 1 — Mechanical pre-checks (run before judging)

Gather objective facts first so judgment rests on verified state rather than memory:

1. **Trace lineage to current identity** (do not match by basename alone, and do not treat a `D` event in Git as proof of retirement):
   - Check whether the path exists live, was renamed/moved (`git log --follow --name-status -- <path>`), appears in [the 2026-10-23 Theory rename records](../../reports/retained/theory-collection-rename-20261023/README.md) or `properdocs.yml` `redirect_maps`, or was deleted (`git log --diff-filter=D -n 1 -- <path>`).
   - **Inspect the full deleting commit (`git show --stat <del-commit>`).** Many historical `kb/notes/*.md` files show `D` only because they were **split, merged, renamed during a vocabulary migration, or converted to an ADR** with too much diff for Git rename detection.
     - If the deleting commit created, renamed into, or merged into successor file(s), trace *each* successor forward to its current live path and triage the surviving live file(s).
     - Only if no successor exists, read the file just before deletion (`git show <del-commit>^:<path>`) and the commit message to record *why* it was retired, then classify as `already-gone`.
   - If the historical path resolves to a live file already triaged under another row in the inventory, note the **shared successor** and stop (count surviving notes once).
   - If live, check its recent commit history (`git log -n 5 --oneline -- <live-path>`) to see whether it was already substantively rewritten recently.
2. **Read the full live note** (frontmatter, body, `## Scope`, links, and any cited source/attribution).
3. **Inventory inbound links and separate live dependents from historical records:**
   ```bash
   rg -n '<live-slug>' -g '*.md' kb/
   ```
   Group hits into:
   - **Live dependents:** `kb/theory/`, `kb/reference/`, `kb/instructions/`, `kb/tags/`, `kb/articles/`. For each live dependent, read the citing paragraph and note *what specific premise* it imports from this note.
   - **Historical / working records:** `kb/sources/*.ingest.md`, `kb/reports/retained/`, `kb/agent-memory-systems/`, `kb/work/`. (These are dated records; path repointing may apply on move/retire, but their historical narratives are not rewritten.)
4. **Search for neighbors and potential duplicates or stronger successors:**
   - Run targeted `rg` searches in `kb/theory/`, `kb/theory/questions/`, `kb/reference/`, and `kb/instructions/` using the note's core mechanism terms.
   - Open and read the relevant passages of any candidate duplicate, successor, or contradicting note.

## Step 2 — Run the six diagnostic tests

Apply these checks in order to a live note, starting from its role in the whole KB:

1. **Role in the whole KB and relevance to current gaps (the #1 question).**
   - **KB goal fit:** How does this note serve `AGENTS.md`'s purpose—helping agents and maintainers decide KB architecture, types, writing, context engineering, knowledge organization, or continual learning? Name the concrete reader and the specific decision it changes.
   - **Collection goal fit:** Does it deliver what its collection exists for (e.g. a transferable explanatory-reach claim in [kb/theory/COLLECTION.md](../../theory/COLLECTION.md), a change-operation premise in `kb/reference/`, a reusable reply/comparison in `kb/notes/`, or a recurring problem root in `kb/theory/questions/`)?
   - **Value for current open gaps:** Does the note bear on any of the live gaps in [What gaps remain in our learning loop?](../../theory/questions/what-gaps-remain-in-our-learning-loop.md) (autonomous noticing & structural search, active inquiry & faithful local judgment, clearing the accretion plateau, debugging credit assignment in a mixed prose-and-code store, selective double-loop criterion revision, whole-loop net gain / hypothesis payoffs, outgrowing the bootstrap) or its sibling standing questions ([How do we value notes?](../../theory/questions/how-do-we-value-notes.md), [How do we fight bloat in agent-produced systems?](../../theory/questions/how-do-we-fight-bloat-in-agent-produced-systems.md))?
   - **How this steers the verdict:**
     - *Helps close a current gap, even if buried in dated framing* → **high priority** to rescue, sharpen (`rebuild-in-place` / `targeted-update` / `relocate-and-recast`), and connect to the relevant standing question.
     - *Serves a real standing decision outside the learning-loop gaps* (e.g., durable navigation or writing guidance) → earns its place if sound and non-redundant.
     - *No clear KB role and no gap contribution* (even if locally true and well-formed) → strong candidate to **retire** or **merge**; validity alone does not justify maintenance and attention cost ([choosing what to learn requires both validity and learning-value gates](../../theory/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md)).
2. **Collection and form test.**
   - Apply the [theory placement test](../../theory/COLLECTION.md): *after every Commonplace-specific choice is scoped, does a substantive design-space claim remain?*
   - Check for collection/form mismatches:
     - Accurate only about local Commonplace practice already owned by a skill or reference doc → **retire** (or route to that doc).
     - Unadopted design/feature prescription ("system X should do Y", "we need mechanism Z") framed as a general law → **recast as a design proposal** in `kb/reference/proposals/`.
     - Living map of open problems or framework gaps wearing a `title-as-claim` → **relocate to `kb/theory/questions/`** ([ADR 142](../../reference/adr/142-questions-are-first-class-objects-in-kb-theory-questions.md)).
     - Useful comparison, analogy, or worked example without a general proof → **move to `kb/notes/`**.
     - Current-state Commonplace architecture/contract description → **move to `kb/reference/`**.
3. **Overclaim and scaffolding test.** Old notes frequently bury a crisp, defensible insight under inflated necessity claims, obsolete metaphors, or feature/gap sketches.
   - Test the headline against obvious counterexamples (e.g. does a missing index entry actually make a note unreachable, or can search still find it? does a boundary actually require a separate directory?).
   - Separate the minimal claim that actually holds from obsolete scaffolding (old terminology like *claw* or *harness*, task-state-machine sketches, feature wishlists, or "not built yet" inventories).
4. **Duplication and stronger-explanation test.**
   - Compare the note's surviving core against every neighbor you read in Step 1.4.
   - Distinguish **redundant/superseded** (another note states the same mechanism better or more cleanly) from **complementary** (e.g. one note explains *when* a cue helps while another explains *where* to place it). State the exact evidence that separates keeping from replacing.
5. **Currency and grounding test.**
   - Check factual statements about Commonplace ("we haven't built any of this yet", missing validators, old paths, links into frozen `kb/agent-memory-systems/` or superseded drafts).
   - Check external attributions (authors, papers, named patterns). If a load-bearing claim attributes a structure or result to an external work without a tracked ingest/quote or verified passage, **do not pass it on faith**—flag verification as a prerequisite.
6. **Dependent-premise impact test.**
   - For every live dependent found in Step 1.3, check whether it relies on:
     - the **surviving core** (must be preserved during any rewrite), or
     - a **weakened, overclaimed, or retired premise** (must be explicitly flagged for argument repair—never resolve this with a blind link redirect).

## Step 3 — Assign exactly one verdict

Choose the single primary disposition that fits the evidence:

| Verdict | When to choose it | Required follow-up if approved |
|---|---|---|
| **`already-gone`** | Historical path was previously deleted, retired, or an old deleted ADR; no live file remains. | Record deletion commit and reason; do not recommend retiring again or restoring. |
| **`keep-unchanged`** | Clear reader and decision; claims hold and are properly bounded; distinct from neighbors; placed in the right collection; no stale factual claims. | None. |
| **`targeted-update`** | Right home and sound core claim, but specific sections have stale current-state claims, minor category/scope bugs, or outdated links. | List the exact passages to fix in place. |
| **`rebuild-in-place`** | Genuine transferable insight survives, but the current text overclaims, conflates distinct concepts, or carries obsolete scaffolding. | State the narrowed claim to keep, what to cut, whether the filename still matches (use `commonplace-relocate-note` in its own commit if renamed), and which live dependents need citation/premise repair. |
| **`relocate-and-recast`** | Surviving value belongs in another collection or form (`kb/reference/proposals/`, `kb/theory/questions/`, `kb/notes/`, or `kb/reference/`). | Name destination, new form/title, what to keep vs. cut, and dependent repairs. |
| **`merge-or-retire-duplicate`** | Subsumed by an existing stronger note, skill, or reference doc (verified by reading its text). | Name the exact successor(s), any unique detail to extract first, dependent premise repairs, and retire via [retire-artifact.md](../../instructions/retire-artifact.md). |
| **`retire-obsolete`** | No surviving reader/decision, or core claim fails with nothing unique worth rescuing. | List dependent premise repairs and retire via [retire-artifact.md](../../instructions/retire-artifact.md). |
| **`verify-before-deciding`** | Disposition turns on an unchecked external attribution, unverified source claim, or unresolved empirical check. | Name the exact check needed and the conditional verdict for each outcome. |

## Output format

Return one concise record per note (matching the workshop log style—no filler):

```markdown
### `<historical-or-live-path>` -> `<current-live-path | deleted>`
- **Lineage:** <commit(s) tracing rename/move/rewrite/deletion, or `unchanged since YYYY-MM-DD`>
- **Verdict:** `<one verdict from Step 3>` (priority: `high | normal | low`)
- **KB role & goal fit:** <what role this plays for the KB goal and its collection goal, naming the concrete reader and decision—or `none`>
- **Relevance to current gaps:** <which gap(s) in `what-gaps-remain-in-our-learning-loop.md` or sibling standing questions this bears on, or `none`>
- **Evidence & reasoning:** <2–5 crisp sentences covering the decisive tests: claim validity, collection fit, comparison with named neighbors/successors, and stale or unverified points>
- **What to keep / cut:** <concrete keep/cut items, or `n/a`>
- **Live dependents affected:** <list each citing file whose premise must change, or `none` / `path-only`; separate historical records>
- **Not checked in this pass:** <state explicitly any external source, citation, or empirical claim left unverified>
- **Suggested `february-28.tsv` update:** `<historical_path>\t<coverage>\t<located_path_or_successor>`
```

## Stop and escalate conditions

Stop and flag for the operator instead of guessing when:
- Lineage is ambiguous across splits or shared successors.
- Retiring or narrowing a note invalidates a load-bearing argument in an ADR, active instruction, or design proposal.
- A verdict requires deciding an unsettled repo policy or choosing between two incompatible collection placements.
- A batch would trigger paid `commonplace-review` runs, deletions, or bulk relocations.
