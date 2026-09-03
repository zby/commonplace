# Reachability working-paper artifact manifest

## Status

Staging manifest. No paper version or source commit has been frozen, and no
publication state is authorized.

The eventual manifest must record one paper version and source cohort. An exact
snapshot is historical evidence for that version; a live note is a successor,
not a dependency that can silently redefine it.

## Planned package

| ID | Paper role | Live source | Mode | Planned staged artifact | Current state | Remaining work |
|---|---|---|---|---|---|---|
| M | Main paper | `kb/articles/reachability-conjecture-the-llm-stays-fixed-the-software-house-learns.md` | paper-native | published article path | substantial draft exists | complete dependency audit, paper invitation, references, final self-standing review, publication approval |
| A | Definitions and boundary | `kb/notes/definitions/software-house.md`; `kb/notes/definitions/representational-form.md`; main-paper terms | paper adaptation | `staging/appendix-a-definitions-and-boundary.md` | draft in staging (2026-09-03) | operator review of the paper-specific definitions: regime, demand process, adequate state, hitting probability, continuation reliability, practical reachability |
| B1 | Naur's machine-execution bridge | `kb/notes/naur-equates-machine-execution-with-formulated-criteria.md` | compressed adaptation | `staging/appendix-b-program-theory-and-naur.md` | live note ready | compress to the execution-versus-criteria distinction; add direct Naur references |
| B2 | Technology-relative compiler-transfer evidence | `kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md` | compressed adaptation | `staging/appendix-b-program-theory-and-naur.md` | live note ready | add direct case citation and distinguish what the case rules out from what newer retrieval and activation leave open |
| B3 | Longitudinal theory-holding test | `kb/notes/program-theory-sustains-search-under-delayed-feedback.md` | paper adaptation | `staging/appendix-b-program-theory-and-naur.md` | long live argument exists | retain only the derivation and tests needed by this paper; preserve wrong-theory, withholding, delayed-feedback, and recovery predictions |
| C | Witness protocol | main paper plus `kb/articles/nearest-existing-constructions-to-a-reachability-witness.md` | paper-native, canonical | `staging/appendix-c-witness-protocols.md` | broad and explicit-theory cores exist | complete the demand process declared in advance, run accounting, probability evidence, model and seed freeze, and intervention schedule |
| D | Nearest existing constructions (supplement) | `kb/articles/nearest-existing-constructions-to-a-reachability-witness.md` | versioned supplement | `staging/supplement-d-nearest-constructions.md` | comparison exists | freeze evidence basis and direct references; replace the protocol section with a pointer to Appendix C |
| E | Transition reachability and seed descent (supplement) | `kb/articles/reachability-as-closure-under-the-seed-gate.md` | versioned supplement, exact snapshot | `staging/supplement-e-transition-reachability.md` | formal correction merged (PR #179, commit 465de048) | review the corrected relation, then snapshot |
| R | References and provenance | source ingests and primary sources cited by all components | paper-native | `staging/references.md` | source captures exist | produce conventional bibliography, page or section locations, and direct primary-source citations; keep ingest links only as optional provenance |

## Publication modes

**Exact snapshot.** The staged text reproduces the source artifact at the frozen
commit. Allowed transformations are mechanical: remove frontmatter, lower or
raise heading levels, rewrite links, normalize citation formatting, and add the
provenance header. Any substantive wording change changes the mode to a paper
adaptation.

**Paper adaptation.** The appendix is edited for this paper: material may be
selected, reorganized, compressed, or joined with another source. The appendix
is authoritative paper text. Its source links record derivation and live
successors; they do not imply textual identity.

**Paper-native.** The content exists to make the paper complete and may combine
several live artifacts. The witness protocol and reference list belong here
because neither should be defined by whichever source note happens to be current
later.

## Freeze

The freeze for a version is one annotated git tag on the source commit, for
example `reachability-wp-v1`. Every appendix and supplement cites that tag in
its provenance header, and every live-source path in this manifest resolves
against it. Reviewing an exact snapshot means diffing it against the tagged
source after the allowed transformations.

A per-file manifest with source blobs and a generated drift check are deferred
until a second version is released. One tag records the whole source cohort for
the first.

## Provenance header

Every appendix or independently released supplement should open with a compact
header of this shape:

> **Versioned argument snapshot.** This appendix is authoritative for *The
> Reachability Conjecture*, version `<version>`. It is an `<exact snapshot / paper
> adaptation>` of `<source paths>` at tag `<tag>`. The [live
> version](<live link>) may contain later corrections or extensions and does not
> silently change this paper version.

For a multi-source adaptation, list all load-bearing live sources in a short
source block rather than claiming one textual predecessor.

## Live-successor status

Deferred with the drift check. A later publication page may report one of:

- unchanged since this paper version;
- revised since this paper version;
- materially revised;
- superseded.

This status is advisory navigation. The frozen appendix remains the historical
authority until a new paper version is explicitly released.
