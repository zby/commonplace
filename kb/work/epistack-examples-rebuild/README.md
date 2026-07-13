# Workshop: epistack-examples-rebuild

Rebuild the three epistack casebook demonstrations in the sibling [`epistack-casebooks`](../../../../epistack-casebooks/) repo on the **current** Commonplace surface — not patch the first build.

## Goal

Produce three conformance demonstrations (LHC, COVID, eggs) that validate clean under today's framework: snapshot `genre` ([ADR 045](../../reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md)), no ingest `source_type`, verbatim quotes machine-checked ([ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)), collection-conformance review against the shipped dialectical/evidential contracts, and no lifecycle-field churn ([ADR 044](../../reference/adr/044-user-verification-replaces-global-note-status.md)).

The plan has two parts:

- [plan.md](./plan.md) — index: **Part I** (this repo) and **Part II** (sibling)
- [epistack-rebuild-plan.md](./epistack-rebuild-plan.md) — **copy into the sibling repo** as the execution authority (`kb/work/rebuild-from-scratch/README.md`)

## Why rebuild, not repair

The sibling repo's first build was co-developed with the contract and upgraded in place. That left confounds the submission workshop already names: nearest-fit source typing, ingest prose that described a repository state that later ceased to exist, 18 verbatim-quote failures and 6 unresolved pairings across 14 casebook notes, and a collection-conformance gate that passed drifted notes until calibrated ([ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md); sibling `kb/work/post-commonplace-upgrade/`). ADR 046 explicitly deferred fixing those notes — the checker ships first so the rebuild lands checked, not hand-trusted.

The sibling's scaffolded `kb/types/` is also stale relative to upstream: snapshots still require family `tags` and lack `genre`; ingest reports still carry `source_type`. Running `commonplace-init` against the current package is part of the rebuild, not optional hygiene.

## Evaluation boundary

- **Work happens in the sibling repo.** This workshop is the framework-side plan and coordination surface. Framework changes land here only when casework earns them via `backlog-to-commonplace.md`.
- **Preserve captured sources; rebuild everything downstream.** Re-capture is wasted spend unless a snapshot's fidelity is itself in question. PDF siblings and extraction-layer markdown are inputs.
- **Do not adjudicate the three controversies.** Stance-neutral maps only.
- **Do not conflate this with the clean-room convergence experiment.** [epistack-submission/replication-plan.md](../epistack-submission/replication-plan.md) is a separate, preregistered, unrun evaluation. This rebuild is operational: one operator, one contract, one corpus — but with the contract fixed *before* writing begins.
- **Do not reopen Track A's failed factorial.** Sibling `kb/work/post-commonplace-upgrade/track-a/factorial/` stays preserved as failed-preparation evidence. Neutrality-instrument work remains a sibling concern; this rebuild may consume its calibration lessons (the v2 `## Review` wording) but does not launch new model experiments unless separately authorized.

## What closes the workshop

Close when all three hold:

1. Sibling `commonplace-validate` passes on every case `sources/` and `notes/` collection with zero failures.
2. `commonplace-verify-quotes` reports zero mismatches on all casebook notes (unresolved only where the convention is genuinely in use and the source layer cannot support verbatim — those citations must be relabeled `paraphrase layer` or `second-hand`, not patched around).
3. A collection-conformance review sweep on the rebuilt notes produces a documented warn queue that hand-verifies as real drift, not gate rationalisation — or passes clean.

Then: append a closing entry to the sibling backlog if anything new earned promotion; retire or fold the sibling `post-commonplace-upgrade` workshop; remove this workshop from [kb/work/README.md](../README.md).

## Inputs (read before executing)

| Input | Role |
|---|---|
| [plan.md](./plan.md) | Two-repo plan: framework side + copy instructions |
| [epistack-rebuild-plan.md](./epistack-rebuild-plan.md) | Casework procedure — copy to sibling before executing |
| Sibling `backlog-to-commonplace.md` | Evidence trail; append Outcome lines, do not rewrite history |
| Sibling `kb/work/post-commonplace-upgrade/track-b/source-type-inventory.md` | Authoritative genre decisions per source |
| Sibling case `notes/COLLECTION.md` | Fixed dialectical contracts (including v2 `## Review`) |
| [text-contract-profiles.md](../../reference/text-contract-profiles.md) | Shipped dialectical/evidential profile |
| [epistack-competition](../epistack-competition/README.md) | Two-repo protocol |
| [epistack-submission](../epistack-submission/README.md) | What the demonstrations must support at submission time |

## Bookkeeping

- Log operator interventions and any contract amendments in the sibling repo's `kb/log.md`. A contract amendment during rebuild is a finding, not a silent fix.
- Keep the old note bodies in git history; delete them from the working tree when rebuilding each case. Do not "repair in place" note by note — that preserves the confound the rebuild is meant to remove.
- Validate only the collection or files touched by each step unless a step explicitly calls for a full-repo sweep.