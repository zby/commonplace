# Which old notes still earn their place?

Posed by the operator on 2026-11-27. Review all old notes, including ones whose titles give no reason for suspicion. For each, identify the reader or decision it still helps, check whether its claims hold, and decide whether its present home and form serve that use. The three-note pilot justifies looking; it cannot tell us what fraction of the library is worthless. A misplaced proposal, an obsolete prescription, a redundant explanation and a note with no surviving use call for different actions.

## Coverage and next decision

Start with the oldest day examined in the pilot. [February 28 inventory](./february-28.tsv) lists **79 distinct historical paths**, not 79 surviving notes: every direct Markdown child of `kb/notes/` reported as added on 2026-02-28 in the history ending at `b03a3038e`. This includes navigation and files that may have been renamed, split or retired. The list can be regenerated from the repo root:

```sh
git log b03a3038e --diff-filter=A --format='@%as' --name-only -- kb/notes |
  awk '/^@/{d=$0} d=="@2026-02-28" && /^kb\/notes\/[^/]+\.md$/{print}' | sort -u
```

Three entries have pilot findings; the other 76 have not been traced. Trace current identities with Git history and the [collection rename records](../../reports/retained/theory-collection-rename-20261023/README.md), not basename alone. Record exclusions, prior retirements, shared successors and unresolved identities rather than silently dropping them. Count surviving notes once. Keep coverage separate from judgments and judgments separate from completed changes.

**Scope still to settle:** this date and directory define the first batch, not the meaning of *all old notes*. Before claiming full coverage or budgeting a larger sweep, agree with the operator on the age cutoff, whether age means first appearance or last substantive revision, and which historical collections and subdirectories count. Extend the inventory to that boundary. No paid batch reviews or further retirements are authorized by this framing.

## How we found and checked the pilot

We searched Git for additions under `kb/notes/`, then matched February 28 basenames against current direct children of `kb/theory/`, `kb/reference/` and `kb/instructions/`. That shortcut misses renamed notes and was not a verified lineage trace. We deliberately chose titles that named a skill, prescribed an implementation, or predicted a scaling failure. We did **not** choose them by score, review warning, or random draw.

All three lacked a stored `critique`. After operator approval, `commonplace-review` completed three critiques in local run `20261127T173416Z` with no guard changes. The critiques were inputs, not placement verdicts. We applied the [theory collection test](../../theory/COLLECTION.md): once Commonplace's particular choices are stated, what substantive claim remains? We checked the current consumer, compared stronger existing explanations, then inspected inbound references before recommending deletion. For future cases, record the evidence that distinguishes keeping the note from replacing it. A note need not have inbound links to serve a real reader. The [higher-order check workshop](../higher-order-check-evaluation/README.md) evaluates a reviewer; this workshop evaluates the notes.

## Pilot findings and approved actions

| Historical note (filename stem) | Evidence and finding | Approved disposition |
|---|---|---|
| `convert-still-requires-semantic-description` | The [convert skill](../../instructions/cp-skill-convert/SKILL.md) still requires a description that adds information beyond the title. That justifies reading the text, not writing the description *at conversion time*. The note itself admits deferral. No live note relies on it. | Retire the standalone theory note; redirect readers to the skill. Accurate about local practice, not independently useful as theory. |
| `notes-need-quality-scores-to-scale-curation` | Limited inspection time does not establish that per-note scores are necessary. The [connect skill](../../instructions/cp-skill-connect/SKILL.md) already uses scoped search, titles and link following. Popularity can demote the new, weakly linked target a reader needs. [How do we value notes?](../../theory/questions/how-do-we-value-notes.md) already uses this as a proposal, not a retention rule. | Recast in `kb/reference/proposals/` as *Ranking link candidates under a fixed inspection budget*. Compare against relevance-based search at equal cost, including misses on low-degree notes. No change to `connect` and no experiment commissioned. |
| `generate-instructions-at-build-time` | The distinction is *who resolves the value*: shell expansion can avoid model interpretation without generating a copy. The [successor theory note](../../theory/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) explains this and regeneration cost. The [architecture](../../reference/architecture.md#where-the-library-is-read) describes generated pointers to canonical skills. The [channel-compilation proposal](../../reference/proposals/channel-compiled-instruction-artifacts.md) relies on the old stronger claim; merely redirecting its citation would falsely make its design choice an adopted rule. | Correct the dependent argument, route theory and architecture citations separately, then retire. Preserve frozen evidence and fixtures as historical records. |

**Implementation status at workshop opening:** the operator approved the pilot dispositions and reference handling. All three files are still at their old theory paths. Do not count approval as execution; reconcile the working tree before resuming cleanup. For new cases, use the [retirement procedure](../../instructions/retire-artifact.md) before deleting anything.

Close when every item in the agreed inventory has a traceable disposition or explicit operator-accepted exclusion, approved changes have been verified or handed off, and any durable conclusions have a library home. Report counts against that inventory, distinguishing unchanged keepers, useful material moved or merged, and notes with no identified remaining use.
