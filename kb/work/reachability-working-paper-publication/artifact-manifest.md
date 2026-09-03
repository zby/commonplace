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
| A | Definitions and boundary | `kb/notes/definitions/software-house.md`; `kb/notes/definitions/representational-form.md`; main-paper terms | paper adaptation | `staging/appendix-a-definitions-and-boundary.md` | outline only | define program-theory function, learning by the house, open-ended input process, adequate state, practical reachability, hitting probability, and continuation reliability in one paper vocabulary |
| B1 | Naur's machine-execution bridge | `kb/notes/naur-equates-machine-execution-with-formulated-criteria.md` | snapshot candidate | `staging/appendix-b-program-theory-and-naur.md` | live note ready | decide exact snapshot versus compressed adaptation; add direct Naur references |
| B2 | Technology-relative compiler-transfer evidence | `kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md` | snapshot candidate | `staging/appendix-b-program-theory-and-naur.md` | live note ready | add direct case citation and distinguish what the case rules out from what newer retrieval and activation leave open |
| B3 | Longitudinal theory-holding test | `kb/notes/program-theory-sustains-search-under-delayed-feedback.md` | paper adaptation | `staging/appendix-b-program-theory-and-naur.md` | long live argument exists | retain only the derivation and tests needed by this paper; preserve wrong-theory, withholding, delayed-feedback, and recovery predictions |
| C | Constructive-witness protocols | main paper plus `kb/articles/nearest-existing-constructions-to-a-reachability-witness.md` | paper-native | `staging/appendix-c-witness-protocols.md` | carrier-neutral and explicit-theory cores exist | complete prospective demand process, run accounting, probability evidence, model and seed freeze, and intervention schedule |
| D | Nearest existing constructions | `kb/articles/nearest-existing-constructions-to-a-reachability-witness.md` | paper adaptation or versioned supplement | `staging/appendix-d-nearest-constructions.md` | comparison exists | choose in-document appendix versus separately paginated supplement; freeze evidence basis and direct references |
| E | Transition reachability and seed descent | `kb/articles/reachability-as-closure-under-the-seed-gate.md` | paper adaptation or snapshot after correction | `staging/appendix-e-transition-reachability.md` | formal correction proposed in PR #179 | merge and review the corrected relation, then decide whether to preserve the complete supplement or a shorter paper adaptation |
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

## Fields to freeze for a release candidate

```yaml
paper: reachability-conjecture
version: pending
source_commit: pending
frozen_at: pending
components:
  - id: A
    mode: paper-adaptation
    staged_path: pending
    sources:
      - path: kb/notes/definitions/software-house.md
        source_commit: pending
        source_blob: pending
        live_path: kb/notes/definitions/software-house.md
```

Repeat the source path, source commit, source blob, live path, mode, and staged
path for every component. The final build or review should fail when an exact
snapshot's source content does not match its declared blob.

## Provenance header

Every appendix or independently released supplement should open with a compact
header of this shape:

> **Versioned argument snapshot.** This appendix is authoritative for *The
> Reachability Conjecture*, version `<version>`. It is an `<exact snapshot / paper
> adaptation>` of `<source paths>` at commit `<commit>`. The [live
> version](<live link>) may contain later corrections or extensions and does not
> silently change this paper version.

For a multi-source adaptation, list all load-bearing live sources in a short
source block rather than claiming one textual predecessor.

## Live-successor status

A future publication page or generated check may report one of:

- unchanged since this paper version;
- revised since this paper version;
- materially revised;
- superseded.

This status is advisory navigation. The frozen appendix remains the historical
authority until a new paper version is explicitly released.
