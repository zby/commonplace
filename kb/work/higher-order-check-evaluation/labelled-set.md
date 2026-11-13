# Labelled set for the higher-order check

The labelled set for the first stage of this workshop (2026-11-13). Each
entry names the commit whose tree holds the text the check judges. Positives
are notes whose identity later changed. Kept notes went through a review that
could have changed their identity, and their identity did not change. A
label records what happened in history. It is not a judgment that the
historical outcome was right.

## How the set was built

- **Deletions.** `git log --diff-filter=D` over `kb/theory/*.md` and the
  predecessor path `kb/notes/*.md` (the collection moved to `kb/theory/` on
  2026-10-23 in 9c7563bf7) listed 146 commits. The commit subject and body of
  each were read, and the full diff where the subject was unclear.
- **Retitles and reframes.** Commit subjects containing retitle, rename,
  reframe, fold, merge, split, retire or rehome were read. The recorded
  dispositions of full improvement passes in workshop files were read from
  history, chiefly the ADR 066 test-run record
  (`kb/work/popperian-maintenance-episode/adr-066-test-runs.md` at
  `ecbdf6675^`) and the recoverability batch records
  (`kb/work/full-pass-recompute-cluster/batch-1.md` and `batch-2.md` at
  `a6f7dd145`).
- **`kb/log.md`.** It names the 2026-11-12 episodes and no other positive.
  Its other entries are observations, not identity changes of theory notes.
- **Text before the change.** For each positive, the text is the parent of
  the commit that made the change. Where a retitle followed an earlier body
  rewrite, the text is from before the retitle commit. That text has the
  rewritten body under the old title, so the label for it is `different-claim`.

Excluded:

- pure relocations, such as the `kb/notes/` to `kb/theory/` move, which kept
  every claim unchanged;
- renames that only completed a body reframe made in an earlier commit, such
  as af8feccf8, 3cc5bb920 and ba2c4cfc6. The identity change belongs to the
  earlier body edit, and the pass that made it is not recorded as one commit
  boundary;
- retirements forced by a vocabulary or architecture decision rather than by
  the note's own contribution: 643508db6 and 21021fcc9 (definitions retired
  with their terms), ee98903c3, 13b143cd3, 1ac2171dd and e64d88552;
- narrowings and trims that kept the claim, such as 89b5deb0b, 1d64cc251 and
  7a6ce359d;
- notes from before April 2026, whose type and frontmatter conventions differ
  from those the check is written for;
- further cases that were found but not used, to stay inside this stage's
  spend limit. They are listed under Reserve.

## Positives

| ID | Text at | Path in that tree | Kind | What happened and why |
|---|---|---|---|---|
| P01 | `bbc5ef0a4^` | `kb/theory/types-give-agents-structural-hints-before-opening-documents.md` | reject (merge residue) | Deleted after a full pass. Within a collection the type field is near-constant, so title and description route; the two conditions it added are owned by the verifiability and enforcement notes. |
| P02 | `765cbcb8b^` | `kb/theory/two-context-boundaries-govern-collection-operations.md` | different-claim | Retitled to "read-together note sets": the body had been generalized beyond Commonplace collections in bcc43d65a and the title no longer named its subject. |
| P03 | `5d92a3af0^` | `kb/theory/descriptive-link-labels-may-supply-claim-self-sufficiency.md` | reject | Deleted as unsupported; its evidence citation did not carry the claim. |
| P04 | `dafbdeb07^` | `kb/theory/execution-shaping-determines-directory-placement.md` | reject (obsolete) | Retired: its placement example contradicted adopted placement rules (content routing, ADR 084, ADR 099), and the reassessment found no contribution worth repairing. |
| P05 | `02bc1d716^` | `kb/notes/removing-a-human-judgment-can-degrade-the-judgments-that-remain.md` | merge | Retired as trivial: the parent note already stated the claim in one sentence; the defeater was kept as a clause there. |
| P06 | `bb866e5f9^` | `kb/notes/explicit-artifacts-buy-addressability-not-credit-assignment.md` | merge | Folded into reflection-buys-addressability as a section: expanding a bounded claim into a full note was judged reverse compression. |
| P07 | `a4dd014cc^` | `kb/notes/traditional-debugging-intuitions-break-when-tool-loops-can-recover.md` | merge | Full pass (run 11) recommended merging into the apparent-success note; its residue moved there, its prevalence claims failed warrant. |
| P08 | `3db8edd87^` | `kb/notes/unobserved-local-information-cannot-be-recovered-by-capability.md` | reject (merge residue) | Deleted the same day it was written: an analytic core true by definition plus claims owned by four existing notes. |
| P09 | `0e4fd6e6d^` | `kb/notes/model-absorption-threatens-only-the-generalizable-half.md` | reject, split | Full pass found the categorical claim contradicted by the recorded-then-trained channel and by its own concession; replaced by two narrower notes. |
| P10 | `e388db0d0^` | `kb/notes/a-self-improving-system-needs-a-profile-not-a-ladder.md` | merge | Retired after its load-bearing parts had been extracted into other notes; what remained was routing and paragraphs stated better elsewhere. |
| P11 | `5f9abf595^` | `kb/notes/programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must.md` | split, rehome | An operational policy in first person in the theory collection: split into a reference policy and a theory note on transfer over shared mechanism. |
| P12 | `3055180aa^` | `kb/notes/reflective-self-improvement-changes-how-a-system-generalizes.md` | merge | Its title claim was a premise; its contestable content was owned by the target-data conjecture note, which received a vocabulary section. |
| P13 | `c6b2744a8^` | `kb/notes/machine-searches-for-camouflage-human-writer-slips-into.md` | merge | A weak satellite: mostly the core note's mechanism plus a speculative corollary; one sentence moved into the core. |
| P14 | `171ec6492^` | `kb/notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md` | different-claim | Rewritten and retitled to "rule-based context selection needs a pre-existing signal", the claim the argument actually proved. |
| P15 | `8b1b6ee96^` | `kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md` | different-claim | The ADR 066 control case: its premises proved defective (replay of a side-effectful call), and the pass reframed it to "a checked outcome licenses retaining an episode, not abstracting its explanation". |
| P16 | `6571dab5b^` | `kb/notes/a-stronger-oracle-buys-autonomy-and-pays-in-reach.md` | different-claim | The title said autonomy is bought while the revised body said bare autonomy is free; retitled to "warranted autonomy is bounded by oracle reach". |

## Kept notes

Each kept note had a full improvement pass, or in K14 a targeted
reassessment, whose disposition kept its identity. Its file name and claim
still stand at HEAD on 2026-11-13. The text judged is the one the review saw:
the parent of the commit that applied the review.

| ID | Text at | Path in that tree | Review that kept it |
|---|---|---|---|
| K01 | `a6f7dd145^` | `kb/notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md` | Recoverability batch 2, item 8: keep. |
| K02 | `21d4038a5^` | `kb/notes/areas-exist-because-useful-operations-require-reading-notes-together.md` | Recoverability batch 1, item 3: keep, although the batch file named it the note most likely to come back delete or rehome. |
| K03 | `52546a417^` | `kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md` | ADR 066 run 10: plain keep, thesis repaired. |
| K04 | `52546a417^` | `kb/notes/human-analogies-suggest-functions-not-component-boundaries.md` | ADR 066 run 12: plain keep. |
| K05 | `ec4beed5f^` | `kb/notes/memory-design-adds-operational-axes-to-artifact-analysis.md` | ADR 066 run 16: plain keep. |
| K06 | `98eae44d0^` | `kb/notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md` | ADR 066 run 19: keep with exclusivity dropped. The title later gained "loadable" (fd94e55b0), an extension, not a different claim. |
| K07 | `faff75ab9^` | `kb/notes/bounded-context-orchestration-model.md` | ADR 066 run 23: plain keep with a scope and formalism repair. |
| K08 | `8b1b6ee96^` | `kb/notes/memory-backed-personalization-can-look-like-model-improvement.md` | ADR 066 run 4: planned upward reframe declined; plain keep. |
| K09 | `72b0b89ad^` | `kb/notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md` | Full pass 20260713T160500Z-c2db: keep. |
| K10 | `25873411a^` | `kb/notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md` | Full pass 20260819T105132Z-2a6408: keep. |
| K11 | `50d882fa7^` | `kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md` | One of six full passes, all keep-with-edits; title unchanged. |
| K12 | `50d882fa7^` | `kb/notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md` | As K11. |
| K13 | `50d882fa7^` | `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md` | As K11. |
| K14 | `f0b87be6f^` | `kb/theory/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md` | The 2026-11-08 frontier scan proposed revising its examples to the current connect protocol and no change to its claim. |

The kept set is weaker evidence than the positives. A keep says one review
did not change the note, not that the note should never change. Several kept
notes were edited by the pass that kept them, so the text judged here is the
text before those edits.

## Reserve

Found and not run in this stage:

- 757d6daa3: distillation-is-transformation-not-selection retired; its claims
  had better homes once its polemic target dissolved. It was left out because
  a term retirement drove it.
- 45545b8ec: framework-overhead note deleted; its general content moved into
  the context-cost family.
- 1b6fea180 and ffc7c00fa: two June 2026 split-and-rehome cases, a proposal
  and a claim in one theory note.
- bb866e5f9 (second note): a-theory-mediated-loop-closes-only-by-causal-co-indexing,
  folded with P06.
- c7f1605ba: a tombstone stub retired, an easy case.
- Twelve reframes in the ADR 066 record (runs 2, 7 to 9, 13 to 15,
  17, 18, 20 to 22): different-claim candidates whose pre-change commit has
  to be recovered from the batch commits.
- 28aa77089 and 1506fead5: two keep dispositions whose notes were later
  renamed. They are positives for a later identity change, not kept notes.
