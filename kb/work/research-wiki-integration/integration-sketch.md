# Integration Sketch

## Proposed Shape

Keep two candidate shapes alive.

### Track A: Full ARIS-Shaped Subsystem

Start by preserving ARIS's own structure under a workshop:

```text
kb/work/<workshop>/
  README.md
  research-wiki/
    index.md
    log.md
    gap_map.md
    query_pack.md
    papers/
    ideas/
    experiments/
    claims/
    graph/
      edges.jsonl
```

Use this when the goal is to test whether ARIS Research Wiki works as a coherent subsystem. Keep ARIS names here, including `query_pack.md`, so the experiment measures the original design rather than a rewritten version.

### Track B: Generalized Commonplace Pattern

In parallel, define the likely commonplace-shaped form:

```text
kb/work/<workshop>/
  README.md
  investigation/
    working-readme.md
    log.md
    gaps.md
    edges.jsonl
    sources/
    ideas/
    claims/
    experiments/
    LINT_REPORT.md
```

Use this when the goal is to generalize lessons from ARIS into normal commonplace workshop conventions. This should start as a convention, not a new global collection. Once two or three workshops use it successfully, promote the stable parts into `kb/reference/` or `kb/instructions/`.

The tracks should inform each other, but not collapse immediately. Track A may stay as an ARIS-like subsystem if the whole lifecycle is useful. Track B should absorb only the parts that prove broadly useful outside research-wiki-shaped work.

## Static Versus Dynamic Orientation

Treat ARIS's `query_pack.md` as a specialized README, not a fundamentally different species of document.

The useful split is:

- `README.md` - stable workshop orientation: question, scope, current position, important files, and closure criteria.
- `investigation/working-readme.md` - dynamic agent orientation: compressed current state, failed ideas, active claims, active gaps, source cards, probes, and pending decisions.

Keeping the dynamic part separate costs one loading hop, but avoids turning the canonical README into a high-maintenance generated artifact. For the first implementation, prefer the separate document. If a workshop is small enough that one hop matters more than churn, it probably does not need the investigation-map pattern at all.

## Entity Files

Use plain markdown initially:

- `sources/<slug>.md` - a workshop source card that points to a `kb/sources/` snapshot and ingest report.
- `ideas/<slug>.md` - a candidate direction, including status, rationale, blockers, and failure notes.
- `claims/<slug>.md` - a claim under test with status, evidence, counterevidence, and promotion target.
- `experiments/<slug>.md` - a probe, review run, validation trial, or comparison that updates claims and ideas.
- `gaps.md` - open questions and missing coverage.
- `edges.jsonl` - optional structured edges for generated views.

Avoid frontmatter until the shape has stabilized. Workshop files are allowed to be plain markdown, and premature typing would make the experiment harder to change.

## Status Vocabulary

Start with small local enums:

Ideas:

- `proposed`
- `selected`
- `testing`
- `supported`
- `invalidated`
- `parked`
- `retired`
- `promoted`

Claims:

- `reported`
- `under-test`
- `supported`
- `invalidated`
- `qualified`
- `promoted`
- `retired`

Experiments:

- `planned`
- `running`
- `concluded`
- `blocked`
- `interpreted`

Gaps:

- `open`
- `addressed`
- `resolved`
- `superseded`

## Generated Working README

`investigation/working-readme.md` should be the default file an agent loads before working in a substantial workshop. Keep it hard-budgeted. A first budget can be:

| Section | Budget |
|---|---:|
| Workshop question and current position | 500 chars |
| Active gaps | 1200 chars |
| Active claims | 1600 chars |
| Failed or retired ideas | 1600 chars |
| Current ideas | 1200 chars |
| Experiments/probes | 1000 chars |
| Source cards | 1400 chars |
| Open decisions | 800 chars |

Failed ideas should have a reserved section. If the pack must shrink, remove lower-priority source detail before removing failure memory.

## Minimal Helper

First helper scope:

1. Rebuild `investigation/working-readme.md` from workshop investigation files.
2. Append simple receipts to `log.md`.
3. Emit `LINT_REPORT.md` with warnings for:
   - active claims with no evidence or experiment,
   - failed ideas missing failure notes,
   - open gaps with no idea,
   - source cards with no snapshot or ingest report,
   - promoted items still listed as active,
   - edges pointing at missing files.

Do not build paper ingestion first. Commonplace already has source ingest. The missing feature is lifecycle synthesis over active workshop artifacts.

## Promotion Path

At closure, each investigation item must land in one of these states:

- Promoted to `kb/notes/`, `kb/reference/`, `kb/instructions/`, or `kb/reference/adr/`.
- Folded into an existing artifact.
- Retired with a reason.
- Filed as local negative memory in the closing summary.
- Deleted because it was only transient scaffolding.

The final durable output should link to source snapshots or ingest reports, not to the workshop files. Library collections should still not link into `kb/work/`.

## First Trial Candidate

This workshop can test the pattern on itself:

- `classification-comparison.md` is a candidate claim map.
- `lifecycle-analysis.md` is a candidate lifecycle analysis.
- `borrowable-features.md` is a candidate idea/decision ledger.

Do not build the helper until this hand-authored version shows which fields actually matter.
