# Evidence sort (2026-10-22)

**Done 2026-10-23** (commits `dd5f52842`..`25a75d0ef`): the three local notes
moved to `kb/reports/retained/` (one footer relabelled); the six-path audit
moved there too, and its applicability finding became
`kb/notes/evidence/consumer-channel-and-force-can-stay-fixed-while-the-governed-use.md`;
the episode note moved to `kb/work/`. The captured copies in
`simplification-instruction-comparison-20260807` kept their bytes. Still
open: the three evidence-shaped `kb/reference/` files below, and refreshing
`moves.tsv`, `redirect-changes.tsv` and `relocation-updates.tsv`, which
predate these moves.

Provisional sort of `kb/notes/evidence/` by scope of inference, for the
prerequisite step in the [README](./README.md). "Local" files move to
`kb/reports/retained/`. A subagent read the six candidates and three
evidence-shaped reference files in full and skimmed the other eleven;
moves still need operator confirmation.

## Move to `kb/reports/retained/`

- `single-artifact-review-bundles-still-cut-claude-costs-substantially` —
  the cost effect of one Commonplace refactor (26–51% per gate after
  cache-aware pricing); its only general content is pricing arithmetic. Its
  footer labels ("grounds", "extends") point at theory notes that do not cite
  it back; relabel on the move.
- `quotes-route-rollout-grounded-more-uses-without-earning-claim-ids` —
  "for a corpus of this size and shape, the direct model did not earn claim
  identifiers"; bounds ADR 073.
- `a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews` — one
  review setting and one model; evidence for ADRs 079 and 082. Two theory
  notes already carry the general reading and keep citing it.

## Split

- `six-commonplace-paths-establish-broad-addressability-not-completeness` —
  the Commonplace audit (path table, missing admission grant, requested
  versus executed model) moves; a short theory-evidence note keeps the
  design-space finding that consumer, channel and force can stay fixed while
  the assessed use changes, which the behavioral-authority definition and
  proposal cite.

## Stay in theory

- `seven-documentation-cases-left-routing-and-synthesis` (free variable:
  source-readable software KBs; its "Commonplace consequence" section is
  local but does not decide placement).
- `vibe-noting-trace-shows-persistence-enables-revision-not-certification`
  (existence witness; does not state the claim it verifies — a contract
  repair, not a move).
- `commonplace-as-a-reflective-system`,
  `tag-readme-trace-observed-causal-connection`,
  `commonplace-revision-used-theory-guided-computational-search`
  (existence witnesses).
- `real-self-improving-systems-occupy-combinations-no-rung-captures`,
  `six-reported-self-improvement-paths-expose-bounded-redesign-surfaces`,
  `missing-rationale-does-not-exclude-a-builder-weights-do-across-runs`
  (external casebooks).
- `independent-pass-tightened-three-of-four-pirolli-verdicts`,
  `two-rewrites-exposed-a-syntax-or-repetition-tradeoff`,
  `three-simplification-passes-exposed-different-tradeoffs`,
  `full-write-briefs-cut-edit-drift-one-line-briefs-did-not` (the last also
  backs ADR 092 and the write-brief type, but its inference generalizes).

## Misplaced for other reasons

- `in-one-episode-recognition-appeared-only-in-the-corpus-loaded-run` —
  self-described "single uncontrolled observation … not a result"; by the
  evidence-placement rule it belongs in `kb/work/` or `kb/log.md`.

## Evidence-shaped files already in `kb/reference/`

- `tag-readme-trace-as-self-improving-loop` — maps a Commonplace trace onto
  the self-improving-system definition; the existence claim in
  `commonplace-as-a-reflective-system` depends on it. Unclear: merge into
  that theory witness, or move to retained.
- `full-improvement-pass-closure` — a system description whose "Calibration
  evidence" section (5 passes, 2026-07-11) is local evidence; candidate to
  move that section to retained and link it.
- `harness-sub-agent-model-selection-regression` — an incident and state
  record, not evidence; stays (doubts: much of it describes an external
  harness, and its regression story is change history under ADR 074).

## Before moving

- Decide the retained form for a moved note (keep `types/note.md`, a report
  type, or plain text) and how it meets the reports contract's identity and
  change rules.
- Each move is a `commonplace-relocate-note` commit on its own; the split and
  any relabelling are separate commits.
