---
description: "Proposal: mechanically verify verbatim-marked citations against their source snapshot — a Level A deterministic check, not a review gate, since the derived-copy rule forbids leaving it hand-trusted"
type: kb/types/note.md
traits: [design-proposal]
tags: [document-system]
status: seedling
---

# Verifiable quotes

A `verbatim`-marked citation asserts that a quoted span is copied exactly from a source. That assertion is currently hand-maintained and unchecked: an author (or agent) writes `"quote"` plus a citation saying `verbatim`, and nothing confirms the quote actually appears in the referenced source. That is precisely the state [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) forbids — a copy of information recomputable from a ground-truth source, trusted by hand instead of machine-checked. This proposal designs the check.

## Current state (as of 2026-07-09)

- The **grounding-layer marker** convention — every proposition cites a source with a prose locator plus one of `verbatim` / `paraphrase layer` / `second-hand` — is live in the sibling `epistack-casebooks` repo's `kb/lhc/notes/COLLECTION.md`, as part of the dialectical/evidential profile's mandatory-evidentiality clause. It is now also recorded as a shipped default in this repo's [text-contract profile catalogue](../text-contract-profiles.md) (dialectical/evidential entry), so any future collection adopting that profile inherits the same three-part citation shape.
- The convention is **prose-shaped, not machine-structured**. Reading the five live casebook notes: a verbatim quote appears either as a blockquote (`> "..."`) or an inline quoted span, followed within a sentence or two by a parenthetical citation carrying a markdown link to the source snapshot and the literal word `verbatim` (e.g. `([LSAG report](../sources/lsag-2008-review-safety-lhc-collisions.md), Abstract, verbatim.)`). No locator syntax or anchor format was ever specified beyond this pattern — the sibling repo's own `COLLECTION.md` says as much: "A structured source-span locator type remains unadopted; revisit if review tooling ever needs machine-checkable spans (e.g. a staleness gate that re-verifies quotes against snapshots)."
- Five casebook notes with roughly a dozen verbatim citations already exist as a ready-made prototyping corpus. **This proposal did not originate from a felt friction case** — no author has yet been burned by an unverified quote drifting from its source — it originates from applying the derived-copy rule to a convention that already exists. The existing corpus means it can still be exercised without waiting for new casework.
- [Factored dependency pairs for review freshness](./factored-dependency-pairs-for-review-freshness.md) names **source-as-gate** as a *different*, not-yet-adopted mechanism: a `(note, source)` freshness pair for judging whether a note's distillation of a source is still consistent — a Level B, LLM-judged review gate. This proposal is not that. Verbatim-quote matching is fully decidable (does string X occur in file Y), so it needs none of the freshness-pair/review-job machinery — it is a [Level A deterministic check](../../notes/text-testing-framework.md), the same tier as link validity or required-heading checks, not Level B judgment.

## The design

**What gets checked.** For every `verbatim`-flagged citation in a note: extract the quoted span, resolve the linked source file, and test whether the span occurs in that file (after normalization — see below). `paraphrase layer` and `second-hand` citations are explicitly out of scope; they never claimed exact text.

**Applying the derived-copy rule's four preconditions** (from the grounding note) confirms this is enforceable, not just checkable-in-principle:

1. **Derivation rule** — a strict substring test, not a judgment call. Met.
2. **Machine-locatability** — the quote names its source via the adjacent markdown link; the check follows that link the same way link-health already does. Met, contingent on the extraction heuristic below actually finding the pairing.
3. **Ground truth exists at validation time** — the source snapshot is a captured, checked-in file. Met (snapshots are stamped-not-authored and don't change except on an explicit refresh, per `kb/sources/COLLECTION.md`).
4. **Validator expected to bottom out** — the extraction heuristic (below) is itself a hand-authored pattern-match, not a strict grammar. Per precondition 4's own allowance (the tag-README `complete` mark's scoped `rg` sweep is the precedent), a centralized, versioned heuristic amortized across every note is still far cheaper than N hand-trusted claims, even though the heuristic itself isn't provably complete.

**Extraction heuristic (no new citation syntax required).** Rather than inventing a structured citation format, detect the pattern already in use: a quoted span (blockquote or inline `"..."`) paired with the nearest citation in the same or next sentence/paragraph that contains both a markdown link and the token `verbatim`. This will not resolve every case — nested quoting inside a paraphrase-layer citation, or a verbatim citation separated from its quote by more than a sentence, will misfire. Three outcomes per candidate, not two: **match** (quote found in source), **mismatch** (quote not found — the claim is false), **unresolved** (couldn't confidently pair a quote with a citation — a parser limitation, not necessarily a defect, but worth surfacing so an author can tighten the citation).

**Normalization before comparison.** Exact byte match is too strict: smart vs. straight quotes, whitespace collapsing (line-wrapped PDF extraction), and minor capture-tool artifacts are expected even for genuinely verbatim text. The check needs a normalization pass (quote-mark folding, whitespace collapse, at minimum) before substring comparison — otherwise it produces false mismatches on correct quotes, which is worse than not checking at all (it trains authors to distrust the tool).

**Where it runs.** A free choice — see below — but the check's shape (cross-file body-text comparison, not frontmatter/structure) doesn't fit `commonplace-validate`'s existing JSON-schema machinery, which validates one document's frontmatter and structure, not body content against a second file. It is closer in kind to link-health (which already parses markdown links and resolves paths) than to schema validation.

## Forces

- **For: this is exactly the rule the KB already committed to.** An unchecked "verbatim" claim is the textbook hand-maintained-and-trusted state the derived-copy rule forbids — the false-copy failure mode (silent, unbounded wrongness) is worse than the absent-copy one (a bounded recomputation), and "verbatim" is precisely the kind of claim a reader stops independently verifying once the KB asserts it.
- **For: cheap once built, and the corpus already exists.** Level A checks are fast, deterministic, and reusable — no per-note review cost the way a semantic gate would add. Five existing notes mean it can be validated against real data on day one.
- **Against: no felt need yet.** No worked case has actually produced a wrong verbatim citation; this is anticipatory, which cuts against the KB's own build-local-first, prove-it-first discipline. Mitigation: the existing corpus substitutes for a live-friction trigger, and the check is cheap enough (Level A, no new type or schema) that building it doesn't accrue the kind of speculative-machinery debt heavier proposals would.
- **Against: the extraction heuristic isn't complete.** Some verbatim citations will land in `unresolved` rather than being checked at all, especially as citation prose style varies across authors and cases. Mitigation: report `unresolved` as its own category rather than silently passing it, so coverage gaps are visible rather than assumed away.
- **Against: false mismatches from under-normalization would be worse than no check.** A checker that cries wolf on correct quotes teaches authors to ignore it, which is the outcome the derived-copy rule exists to prevent one level up. Mitigation: normalization is not optional polish here, it's load-bearing; ship nothing until the five-note corpus passes clean.

## Free choices

- **Where it lives.** A flag on `commonplace-validate`, a dedicated command (`commonplace-verify-quotes`, following the existing per-purpose command pattern), or a `scripts/` accumulation-substrate script per [ADR 040](../adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md) that graduates to a package command once it proves durable. Leaning toward starting in `scripts/` — this is unproven machinery on an unproven need, exactly what that substrate is for.
- **Severity on mismatch.** `fail` by default per [ADR 024](../adr/024-schema-severity-is-per-constraint-fail-by-default.md)'s stance (softness is the marked case), or `warn` initially given the extraction heuristic's imprecision risk, tightening to `fail` once the false-positive rate is known from real runs.
- **Whether `unresolved` blocks anything.** Treating it as pure signal (never blocks, always reported) versus a soft nudge (warns after some grace period) is undecided; leaning toward pure signal until there's evidence authors respond to it.
- **Scope beyond the dialectical/evidential profile.** The grounding-layer marker convention is currently specific to that profile. Nothing about the check is profile-specific in principle — any collection citing sources with a `verbatim` flag could use it — but there's only one instance to design against today.

## Adoption criteria

Prototype against the sibling repo's existing five casebook notes before writing anything into this repo's shipped tooling. Adopt once the prototype (a) achieves a low `unresolved` rate on real citations without hand-tuning per note, and (b) produces zero false mismatches after normalization — both are cheap to measure against the existing corpus, so this doesn't need to wait for a sixth note or a new case.

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: the inherited principle this proposal instantiates; verbatim citations meet all four of its enforcement preconditions
- [Text testing framework](../../notes/text-testing-framework.md) — rationale: places this check at Level A (deterministic), distinguishing it from source-as-gate's Level B judgment
- [Factored dependency pairs for review freshness](./factored-dependency-pairs-for-review-freshness.md) — contrasts: names the adjacent, not-adopted source-as-gate mechanism this proposal is deliberately narrower than
- [Text contract profiles](../text-contract-profiles.md) — operates-on: the profile catalogue entry recording the grounding-layer marker as a shipped default of the dialectical/evidential profile
- [ADR 024: schema severity is per-constraint, fail by default](../adr/024-schema-severity-is-per-constraint-fail-by-default.md) — rationale: the severity model the mismatch/fail free choice draws on
- [ADR 040: scripts directory is the accumulation substrate for ad-hoc tooling](../adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md) — rationale: the home this proposal's leaning free choice points to for unproven tooling
- [extensible-controlled-vocabularies workshop](../../work/extensible-controlled-vocabularies/README.md) — part-of: the workshop discussion that surfaced this as the one already-first-principled item in a wider, still-speculative borrowing thread
