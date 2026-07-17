---
description: "A grep finds 36 ordinary uses of 'actionable' (high collision prior), yet the definition stays safe because its technical sense fires only when 'actionable' is predicated of a methodology in-clause"
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model]
---

# Clausal binding scopes a captured predicate-word like a coinage

Grammatical predication to an explicit subject can scope a predicate-word almost as well as a multi-word coinage does. When a technical sense fires only where the word is predicated of a named subject in the same clause, the ordinary occurrences of the bare word — which do not carry that predication — never activate the sense, so they never collide. This holds even when links to the definition anchor on the short predicate-word alone.

This is a worked corpus case for [vocabulary collisions are prevented at write time, not resolved at read time](../vocabulary-collisions-prevented-at-write-time-not-read-time.md): it both confirms that note's "capturing a common word is dangerous" premise for a specific term, and exposes a second enforcement-friendly scoping mechanism beyond the multi-word spelling that note foregrounds.

## The corpus check

A plain grep of `actionable` across `kb/notes/`, `kb/reference/`, and `kb/instructions/`, dropping the matches that link to or live inside the definition note and this note's own self-references, returns **36 matches**:

```bash
grep -rn "actionable" kb/notes kb/reference kb/instructions --include="*.md" \
  | grep -iv "actionable-methodology" \
  | grep -v "clausal-binding-scopes-a-captured-predicate-word-like-a-coinage.md"
```

(The self-exclusion matters for reproducibility: once this note exists, its own prose is part of the corpus and repeats `actionable` 8 times, inflating a naive re-run to 44.)

Every match is an ordinary use. They span plain prose ("actionable finding" in `kb/instructions/FIX-SYSTEM.md`, "actionable edits" in `kb/notes/quality-signals-for-kb-evaluation.md`, "non-actionable context" in `kb/instructions/cp-skill-ingest/SKILL.md`, "unactionable" in `kb/instructions/compression-bundle/detail-overhang.md`), a "non-actionable finding" label in the review-system docs, ADR guidance about "actionable guidance", the review and fix pipelines' "actionable findings", and a note titled `mechanistic-constraints-make-popperian-kb-recommendations-actionable.md` with its inbound links. None of the 36 invokes the operator / available-operations / target / setting relation that [actionable methodology](../definitions/actionable-methodology.md) defines. Where they predicate `actionable` of anything, the subject is a *finding*, an *edit*, a *step*, a *recommendation*, or *guidance* — never a methodology.

## Why the bare word would have collided

The collision prior tracks how often the exact string arises innocently in ordinary prose. Thirty-six innocent occurrences in three collections is a high prior: `actionable` is a common English word with a busy distributional life across the corpus, exactly the profile that makes [capturing a common word as an unscoped global technical sense](../vocabulary-collisions-prevented-at-write-time-not-read-time.md) dangerous. Had the definition bound the bare word — "actionable means the four-element operator relation" — every one of those 36 sites would have become a potential use site of the technical sense, and each co-load of a definition-bearing note with one of them would have re-armed the silent merge. Defining bare `actionable` would have been a bad move, and the grep says so quantitatively.

## Why the scoped definition doesn't collide

The definition avoids the trap despite superficially looking like a captured-word definition. Two facts do the work:

- The technical sense is scoped to the compound **actionable methodology**, and in practice the operator-relative predicate is only invoked when `actionable` is grammatically predicated of a methodology in the same clause. The definition note's own canonical form is "A methodology is **actionable** for a particular operator … when …", and `kb/index.md` uses the identical construction: "A methodology is actionable when some operator can actually carry it out."
- None of the 36 ordinary uses predicate `actionable` of a methodology. So even though the technical string `actionable` overlaps the innocent string exactly, the *grammatical trigger* does not overlap, and no ordinary site activates the sense.

The instructive detail is that the link anchor in `kb/index.md` sits on the word `actionable` alone, not on `actionable methodology`. Short-form anchor text would ordinarily be the danger sign the vocabulary-collisions note warns about — a citation that strips a locally-declared qualifier. Here it stays safe, because the scope is not carried by the anchor text or by the multi-word spelling; it is carried by the clause, which still predicates `actionable` of *a methodology*. The subject supplies the scope that the anchor omits.

This is the mechanism the existing note does not fully spell out. It ranks near a coined compound on that note's binding table: a compound like `trace-learning` is collision-free because nothing else occupies the exact string, whereas a clausally-bound predicate is collision-free because the technical reading requires a specific syntactic frame that innocent occurrences do not instantiate. Both convert the write-time uniqueness check into something a lexical pass can approximate — for the coinage, "does this string occur?"; for the bound predicate, "does this string occur *predicated of the scoping subject*?". The second is a harder grep than the first but far easier than sense-classifying every occurrence of a fully captured word.

## Scope and caveats

- The finding is one corpus at one time. The grammatical-binding argument generalizes — it is a claim about how predicate-words carry scope — but the 36-occurrence figure is a snapshot; re-running the grep is the honest way to refresh it.
- Clausal binding is weaker than a coinage where enforcement is concerned. A coinage is greppable by exact string; verifying that a predicate is *only ever* used in its scoping frame requires reading the clause around each occurrence, which is closer to the semantic audit the coinage rule is meant to avoid. The safety here is real but rests on writers keeping the predication discipline, with no positional slot enforcing it.
- The protection degrades if a writer ever predicates the technical `actionable` of a non-methodology subject, or predicates the ordinary `actionable` of a methodology. Neither happens in the current corpus, but nothing but convention prevents it — which is why this remains write-time prevention, not read-time resolution.

---

Relevant Notes:

- [vocabulary collisions are prevented at write time, not resolved at read time](../vocabulary-collisions-prevented-at-write-time-not-read-time.md) — grounds: the 36-occurrence grep verifies the high-innocent-occurrence-prior premise for a concrete term, and the clausal-binding case adds a scoping mechanism beyond the multi-word coinage that note foregrounds
- [actionable methodology](../definitions/actionable-methodology.md) — grounds: the worked case; verify that its technical sense is scoped to the compound and fires only when predicated of a methodology in-clause
