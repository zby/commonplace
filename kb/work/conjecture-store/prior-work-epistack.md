# Prior work: the epistack framework-additions menu

Extracted 2026-10-24 from the deleted workshop
`kb/work/epistack-framework-additions/` (added 028c9278c on 2026-07-08,
deleted 511c8f198 on 2026-07-23 after the FLF Epistemic Case Study
Competition; last state at `511c8f198^`). The casework ran in the sibling
`epistack-casebooks` repo. Only the decisions that bear on the conjecture
store are kept here; the workshop is not restored.

## Decisions the store reaches again

| Epistack decision (2026-07) | Conjecture store counterpart |
|---|---|
| The neutral map is the durable object; a verdict is a separate, labelled, downstream artifact computed over it and never merged in. | The store is primary state; theory and current design are projections computed from it. |
| Bare `confidence` and `status` fields rejected: a credence is not recomputable from ground truth, so as frontmatter it is a stale trusted cache. | The level is computed from the record fields and never stored. |
| Independence clustering: ten papers sharing a dataset, method, authorship or citation lineage are one piece of evidence, not ten. | Witnesses carry a source so independence can be judged; `corroborated` needs two independent sources. The epistack version is more developed: it names the shared dependencies to check. |
| Gap register (what is not known) distinct from crux (what would move the assessment, verdict-relative). | `missing` is the gap; `trigger` plus the refuters are the crux. |
| Belief ledger: previous state, current state, the update, the evidence responsible, what would reverse it. | The `witnesses` and `criticism` record, appended and never rewritten. |
| Support and rebuttal live on attributed edges, not as a stance scalar on the claim. | Criticism entries name the critic; the conjecture text carries no verdict. |
| Convergence through decorrelated adversarial review: a model checking its own claim under the same prompt is a correlated, weak oracle. | Same-source agreement counts as one witness; a critic from a different model family or a person. |

## What the store adds that the menu lacked

The menu was built for contested domains, where motivated actors produce
the evidence. It had no account of the uncontested bulk: many small
decisions bound to a project's own choices, decided once and reused. The
`choices` field and the design projection are that account. The menu's
machinery still applies there, with the threshold set low.

## Decisions that survived into the library

- Source genre as one open field on the snapshot, ADR 045.
- The verbatim-quote verifier, ADR 046.
- Register demoted to a default profile under open-ended text contracts,
  ADR 042, which is why a casework collection needs only its own
  `COLLECTION.md`, not a taxonomy change. The same route serves the
  conjecture collection.

## Unfinished business worth carrying

- **The silently-averaged mechanism was never tested.** The menu named it
  as its most load-bearing untested assumption and designed a cheap
  experiment. It is now a candidate conjecture in [candidates](./candidates.md).
- **The sibling repo is a second project.** The first candidate conjecture
  asks for a project other than Commonplace whose working notes factor into
  bound and unbound claims. `epistack-casebooks` is one, with its choices
  in its `AGENTS.md` and its casework in `kb/<case>/notes/`.
- **Independence as shared dependencies.** When the witness record is
  revised at stage 1, add the dependency kinds the menu listed: dataset,
  method, authorship, citation lineage, and for agents the model family and
  prompt.
