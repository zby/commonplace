# Closing completion retained an edit-introduced defect

## Evidence boundary

This record retains the failure that motivated the 2026-08-27 closing-state repair. It is evidence about one instrumented execution of `kb/instructions/run-full-improvement-pass-on-note.md`, not an estimate of failure prevalence.

- Pass: `20260826T214434Z-8272bf`
- Target: `kb/notes/candidacy-evidence-licenses-escalation-not-acceptance.md`
- Pass-start SHA-256: `eff95c5ee6ecdd1d313ab671b836288967041cd7dade7fd0ca6d8024d52dfc96`
- Assessed-final SHA-256: `32bd38b26793dfdb2702d7be01d9cc89f3dc477a428d2ea9183f7256983856c8`
- Recorded state before the repair: `phase: complete`, `resolution: not-required`
- Deterministic result before the repair: the note and packet validated, both captures matched their hashes, and the live note matched the final capture
- Closing semantic result: `sentence/parsing-ambiguity` FAIL, `sentence/misleading-link-text` FAIL, and `frontmatter/title-body-alignment` FAIL

The exact visible sentence retained in the final capture was:

> “Search results and thematic fit Peter Pirolli's account of proximal information scent as prior art for an agent-navigation note.”

The pass-start note had instead said:

> “Search and thematic fit nominated Pirolli as prior art for an agent-navigation note.”

Closing review identified the concrete regression: the edit dropped the finite verb `nominated`, leaving the reader to guess whether `fit` was a noun or the main verb. It also found that two new links promised external accounts while targeting local Commonplace analyses. The unchanged title acquired a categorical reading that the revised body no longer supported. All three findings were retained in Open items, but the old state contract still permitted `phase: complete`.

## Why structural validation was insufficient

The validator correctly established its own claims: frontmatter and links were structurally valid, captures existed and matched their hashes, and the resolution projection matched frontmatter. None of those checks means the captured prose parses or that the closing reviewers accepted it. The defect was not a missing deterministic check. It was a state-machine error: completion had no typed semantic prerequisite.

## Adopted consequence

Closing now records `closing_status` and the one-use `closing_repair_attempted` flag. A packet completes only as `ready`. A purely local defect introduced by the pass may receive one bounded correction and a full closing rerun against a new immutable capture. A title- or claim-level failure, a newly introduced angle, or a repeated defect becomes `hand-back`; that route restores the pass-start text before stopping. The claim-level finding in this run takes precedence, so its live note is rolled back rather than silently repaired into a different claim.
