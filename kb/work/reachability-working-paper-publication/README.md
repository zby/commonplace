# Workshop: Stage the reachability conjecture as a working paper

## Goal

Prepare a self-standing, versioned working-paper package for [The reachability
conjecture](../../articles/reachability-conjecture-the-llm-stays-fixed-the-software-house-learns.md)
without collapsing its live supporting knowledge base into one permanently
copied document.

The intended publication architecture has three layers:

1. the main paper states the conjecture, short argument, mechanism, evidence,
   limits, and experimental obligations;
2. frozen appendices preserve the load-bearing definitions, arguments,
   protocols, and evidence used by that paper version; and
3. links from each appendix lead to the live notes where the project can revise
   the argument after publication.

The authority rule is:

> The frozen appendix is authoritative for what that working-paper version
> argues. The linked live note is authoritative only for the project's current
> position.

This workshop stages and completes the package. It does not authorize
publication or change the article's lifecycle status. Promotion still requires
explicit approval naming `working-paper` and must follow [Publish an
article](../../instructions/publish-an-article.md).

## Inputs

- [Main draft](../../articles/reachability-conjecture-the-llm-stays-fixed-the-software-house-learns.md)
- [Nearest-constructions supplement](../../articles/nearest-existing-constructions-to-a-reachability-witness.md)
- [Transition-reachability supplement](../../articles/reachability-as-closure-under-the-seed-gate.md) — its formal correction ([PR #179](https://github.com/zby/commonplace/pull/179)) merged on main as commit 465de048; the freeze precondition is met
- the definitions, theory notes, and source captures classified in [dependency-audit.md](./dependency-audit.md)

## Working artifacts

- [artifact-manifest.md](./artifact-manifest.md) — planned paper components,
  snapshot/adaptation mode, live source, target destination, and readiness
- [dependency-audit.md](./dependency-audit.md) — which current dependencies are
  load-bearing enough to enter the versioned package and which remain live links
- [appendix-plan.md](./appendix-plan.md) — paper-native appendix structure,
  provenance headers, missing content, and assembly rules
- [staging/README.md](./staging/README.md) — boundary and naming rules for the
  actual copied or adapted appendix drafts once the source cohort is selected
- [staging/assembly-check.md](./staging/assembly-check.md) — status of each
  assembly check after the first full staging pass (2026-09-03) and the work
  that remains before a tag

## Work sequence

1. **Settle the paper definitions and the canonical protocol.** Write Appendix
   A's definitions of open-ended demand generation, adequate state, practical
   reachability, hitting probability, and continuation reliability, and
   Appendix C's treatment of retries, abstentions, rescues, and post-hoc demand
   removal. Everything else depends on these, so they come first.
2. **Audit the dependency closure.** Done 2026-09-03 in
   [dependency-audit.md](./dependency-audit.md); revisit only if a component
   changes role.
3. **Choose the publication mode.** Done 2026-09-03 in
   [artifact-manifest.md](./artifact-manifest.md): short appendices A to C,
   versioned supplements D and E. Do not call an edited adaptation a snapshot.
4. **Run the completeness checklist on the current body.** The main-body
   checklist in the dependency audit is the cheapest test in the plan and
   needs no staging; run it before any appendix is drafted.
5. **Stage the appendices and supplements.** Copy exact snapshots from the
   tagged source; write adaptations in the staging area; add direct
   primary-source references and provenance headers; keep live-note links for
   later developments.
6. **Assemble and test the paper package.** Verify that the main body remains
   understandable with links disabled, that appendices discharge every
   load-bearing dependency, and that the package contains no unresolved
   placeholders.
7. **Freeze a candidate.** Tag the source commit, record the tag and the mode
   of every component, then review the complete diff rather than regenerating
   a released version automatically from live notes.
8. **Publish only after approval.** Once the user explicitly approves the body
   and target lifecycle, apply the repository publication procedure and record
   the frozen package as the cited version.

## Boundaries

- Do not recursively copy every note reached by a link. Snapshot only the
  load-bearing dependency closure; optional examples, neighboring theories,
  implementation history, and later extensions remain live links.
- Exact snapshots may receive only mechanical transformations such as heading
  normalization, frontmatter removal, link rewriting, and provenance headers.
  Substantive edits make the artifact a paper adaptation.
- Appendices cite primary external sources directly. Commonplace ingest reports
  remain provenance and analysis aids, not the paper's sole scholarly record.
- A live-note revision does not silently revise an older paper. It may trigger a
  new working-paper version, a visible correction, or no paper change after
  explicit review.
- The main article remains the public draft during staging. Workshop copies are
  not alternative canonical versions of the paper.

## Current gaps to close

- final definitions for practical reachability, adequate state, and the demand
  and consequence process declared in advance;
- a reproducible witness protocol that separates one possible path from usable
  hitting probability and sustained continuation;
- the paper-native boundary between the broad reachability witness
  and the stronger explicit-theory mechanism experiment;
- direct bibliographic references and source locations for the Naur and Gödel
  arguments;
- deferred: a generated check that a live note has changed since the source
  tag. The first version relies on the tag alone;
- deferred (operator decision 2026-09-03): the fallible-theory part of the
  argument, including hitting probability and continuation reliability, will
  later be grounded in a search formalism. This version keeps the current
  informal probabilistic framing as is.

## What closes this workshop

1. The dependency audit identifies every load-bearing component and no appendix
   depends on an unversioned live note for its historical meaning.
2. The manifest records one source tag and the exact mode and provenance of
   every staged component.
3. The definitions, witness protocol, transition treatment, comparison evidence,
   and references are complete enough for an external technical reader to
   assess without traversing the KB.
4. Every frozen appendix links to its live successor, and each live source can
   point back to the paper version that froze it.
5. The assembled package validates and passes an external-reader review with
   hyperlinks disabled.
6. The user either approves promotion to `working-paper` and the publication
   procedure lands it, or explicitly decides to keep the package as a draft.
7. Durable process lessons are extracted to the article publication machinery;
   temporary staging copies are then removed with the workshop.
