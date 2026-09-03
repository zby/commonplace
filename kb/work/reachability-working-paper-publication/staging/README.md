# Reachability working-paper staging area

This directory will hold candidate paper appendices and assembly artifacts while
the working-paper package is being prepared. Nothing here is authoritative or
published merely because it has been copied into the workshop.

## Planned files

```text
appendix-a-definitions-and-boundary.md
appendix-b-program-theory-and-naur.md
appendix-c-witness-protocols.md
appendix-d-nearest-constructions.md
appendix-e-transition-reachability.md
references.md
release-manifest.yml
```

Create these files only when their source cohort or paper-native role is clear.
Do not copy every candidate note pre-emptively.

## Staging rules

1. **Select before copying.** The dependency audit must say why the component is
   load-bearing and whether it is a snapshot, adaptation, or paper-native.
2. **Freeze exact snapshots mechanically.** Generate them from the declared
   source commit. Allowed transformations are frontmatter removal, heading
   normalization, link rewriting, citation-format conversion, and insertion of
   the provenance header. Do not edit their substantive text here.
3. **Edit adaptations explicitly.** A paper adaptation names all load-bearing
   source artifacts and is reviewed against them. It does not claim byte or
   wording identity.
4. **Keep historical and live authority separate.** The staged appendix is the
   candidate historical argument; its live link is for later developments.
5. **Use direct external references.** A source ingest may remain linked for
   provenance, but the staged appendix cites the primary paper, essay,
   practitioner account, or inspected repository directly.
6. **No hidden recursive dependencies.** A staged appendix must contain the
   propositions needed for its paper role. Its outbound live links may deepen or
   update the argument but cannot be necessary to recover what the released
   paper meant.
7. **No workshop links at release.** The public package must not point into
   `kb/work/`. Final appendix locations and stable links are chosen before
   publication.

## Candidate provenance block

Use this while staging:

```text
Versioned argument snapshot for: The Reachability Conjecture
Paper version: pending
Mode: exact snapshot | paper adaptation | paper-native
Frozen source commit: pending
Source paths: ...
Live successors: ...
Status: staging — not published
```

At release, replace every `pending` value and convert this into the reader-facing
header specified by the artifact manifest.

## Assembly check

Before a staged package can leave this workshop:

- all source commits and modes are recorded;
- exact snapshots reproduce their source blobs after allowed transformations;
- adaptations have source-comparison review;
- the main paper remains coherent with links disabled;
- every load-bearing dependency is discharged by the body or appendices;
- appendices contain direct scholarly references;
- all placeholders and workshop-only links are gone;
- the user has explicitly approved the complete body and the `working-paper`
  lifecycle transition.
