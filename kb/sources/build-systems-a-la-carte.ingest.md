---
description: "How the scheduler×rebuilder build-systems framework grounds the KB's derived-artifact freshness machinery (staleness, verifying traces, recompute-vs-store)"
source_snapshot: "build-systems-a-la-carte.md"
ingested: "2026-07-06"
type: kb/sources/types/ingest-report.md
source_type: scientific-paper
domains: [build-systems, incremental-computation, staleness-detection, caching]
---

# Ingest: Build Systems à la Carte

Source: build-systems-a-la-carte.md
Captured: 2026-07-06
From: https://www.microsoft.com/en-us/research/wp-content/uploads/2018/03/build-systems.pdf

## Classification

Type: scientific-paper -- peer-reviewed functional-programming paper (Proc. ACM Program. Lang., ICFP 2018) with executable Haskell abstractions and a formal correctness definition.
Domains: build-systems, incremental-computation, staleness-detection, caching
Author: Andrey Mokhov (Newcastle), Neil Mitchell (Digital Asset / Shake author), Simon Peyton Jones (Microsoft Research). High credibility: SPJ is a foundational FP figure, Mitchell authored Shake, and the framework is executable rather than hand-waved.

## Summary

The paper unifies Make, Excel, Shake, Bazel, CloudBuild, Buck, and Nix as points in a single design space rather than isolated systems. Its central move is to separate two choices that are normally wired deep into any build system: the **scheduler** (which tasks run and in what order — topological, restarting, or suspending) and the **rebuilder** (whether a key needs rebuilding — dirty bit, verifying traces, constructive traces, or deep constructive traces). These axes are orthogonal, so any scheduler composes with any rebuilder to yield a correct build system, tabulated as a 3×4 grid where 8 of 12 cells are occupied by existing systems and the empty cells are buildable (notably "suspending constructive traces" = a monadic cloud build system the authors call Cloud Shake). Along the way it gives crisp definitions of **minimality** (rebuild only what transitively depends on changed inputs, at most once), **early cutoff** (stop when a recomputed result is unchanged), and dynamic vs static dependencies, and shows (§7.3) that minimal build systems are a strict generalization of memoization.

## Connections Found

The paper has **no lexical footprint** in the KB — none of its vocabulary (à la carte, early cutoff, content-addressable, verifying trace) appears anywhere. Every connection is conceptual, and all connections are **reverse edges**: the snapshot is immutable and authors no outbound links, so the value is which library artifacts should cite this paper as `evidence`. Discovery surfaced one tight neighborhood — the KB's "derived-artifact freshness" cluster — plus a review-freshness cluster in reference:

- **`a-derived-copy-of-recomputable-truth-must-be-checked-or-absent`** — its "checked or absent" rule for a derived copy is the rebuilder in prose: a verifying trace stores a hash of a derived value and re-checks it against the source (checked), while a content-addressable cache lets you drop and refetch (absent-and-recover). The paper is the formal, executable external corroboration of that asymmetry.
- **`link-graph-plus-timestamps-enables-make-like-staleness-detection`** — reasons from an informal Make analogy (timestamps, rebuild-if-source-newer) that this paper formalizes as Def 2.1 minimality plus the rebuilder ladder that generalizes crude timestamps to verifying/constructive traces. Strongest reverse edge.
- **`llm-recompute-cost-inverts-the-store-vs-recompute-default`** — the paper is the canonical build-system treatment of the ordinary "prefer recompute, distrust the stored copy" default the note claims LLMs invert; §7.3 (minimal build = generalized memoization) grounds the code-side baseline.
- **`distilled-artifacts-need-source-tracking`** — the dependency-record-plus-rebuild-on-change it requires is exactly the build dependency graph and minimality guarantee.
- Two reference docs, **ADR 032 (review-freshness-uses-db-snapshots-not-git)** and the **factored-dependency-pairs-for-review-freshness** proposal, implement hash-keyed re-checking of `(document, gate)` pairs — literally a verifying-traces rebuilder.

Discovery also flagged a latent synthesis: the KB's freshness machinery *is* a build system (scheduler = "when is review/re-distillation due", rebuilder ladder = `status:` dirty bits → hash-checked verifying traces → tag-README `complete`/`covered_by` marks, with early cutoff as the unchanged-result stop). Each of the four notes occupies one cell of that space without naming it. A workshop file is already developing this line (durable signal, non-actionable here).

Rejected: the agent-orchestration "scheduler" note cluster (keyword collision — build scheduler ≠ agent control-flow scheduler) and `axes-of-artifact-analysis` (methodological rhyme only).

## Extractable Value

1. **The scheduler × rebuilder orthogonal decomposition as a naming frame for the KB's freshness machinery.** The paper's grid gives the KB a ready-made classification: detection/timing = scheduler, rebuild-decision = rebuilder. This is the missing vocabulary for a synthesis note that would unify `a-derived-copy-...`, `link-graph-plus-timestamps-...`, `llm-recompute-...`, and ADR 032 as cells of one design space. Highest reach — it names a space, not one point. [deep-dive]
2. **The rebuilder ladder (dirty bit → verifying traces → constructive traces → deep constructive traces) as a maturity axis for derived-artifact checks.** The KB already has dirty bits (`status:`) and verifying traces (review-freshness hash checks, tag-README marks) but has never seen them as rungs of one ladder; the higher rungs (content-addressable / constructive traces) name a design option — fetch-instead-of-recompute — the KB has not adopted and could evaluate. [experiment]
3. **"Minimal build = generalized memoization" (§7.3) as the formal spine under `llm-recompute-cost-inverts-the-store-vs-recompute-default`.** The note argues LLMs flip software's memoization default; the paper is the canonical statement of that default and proves minimality strictly subsumes memoization, so it is the precise external baseline the note inverts. [just-a-reference]
4. **"Verifying trace" as a precise term for the KB's hash-recheck freshness pattern.** ADR 032 and the review-freshness proposal reinvent a mechanism the paper names and situates; adopting the term improves retrieval and lets the KB point at prior art instead of re-deriving. [quick-win]
5. **Early cutoff as the "unchanged result stops the cascade" optimization.** The KB's re-distillation machinery implicitly wants this (a re-reviewed source whose distillate is unchanged should not cascade); the paper isolates it as a first-class, nameable property distinct from minimality. [just-a-reference]
6. **Self-tracking (Excel/Ninja recompute when the *task itself* changes, not just inputs) as a lens on tag-README/skill staleness.** The KB's "the type spec can change, so the inlined snapshot goes stale" concern (in `a-derived-copy-...`) is the self-tracking problem — tracking changes to the task, not only its dependencies. [just-a-reference]

## Limitations (our opinion)

Editorial opinion. The paper is strong and executable, but two gaps bound its transfer to this KB. First, its entire framework assumes a **deterministic, mechanically recomputable derivation** — `compute task store` gives the same value every time, and correctness is defined by exact re-derivation equality. The KB's hardest freshness cases are precisely the ones this excludes: re-distilling an instruction from a revised source is a judgment call (a Level B check in the KB's text-testing terms), not a deterministic recompute, so the paper's minimality and verifying-trace guarantees do **not** transfer to the review-by-LLM regime — they transfer only to the KB's deterministic end (mark validation, file-identity checks), exactly the boundary `a-derived-copy-...` already draws. Treating the whole freshness problem as "just a build system" would over-generalize. Second, the paper models correctness and structure but says little about the **cost of the check itself** relative to the cost of recompute — the asymmetry that drives the KB's decisions (cheap Level A validator vs expensive Level B judge, and the LLM recompute-cost inversion) is outside its frame. So the paper supplies the *structure* (schedulers, rebuilders, the ladder) but not the *economics* the KB reasons from; borrow its taxonomy, not its cost model.

## Recommended Next Action

Write a synthesis note in `kb/notes/` naming the design space — provisionally "the KB's derived-artifact freshness machinery is a build system" — that maps the KB's existing freshness patterns onto the paper's scheduler × rebuilder classification and cites this snapshot as `evidence`. Before drafting, check the in-flight workshop file `kb/work/lineage-mechanisms/verification-locus-and-provenance-theory.md`, which is already developing this line, to avoid duplicating or forking it; the note should either promote from that workshop or explicitly complement it. The five scattered reverse-edge candidates (four notes + ADR 032) then become the cells that note organizes, and the `evidence` edges can be authored from their side.
