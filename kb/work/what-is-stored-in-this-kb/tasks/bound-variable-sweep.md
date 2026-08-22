# Sweep `kb/notes/` for free choice-variables

## Status

**Closed 2026-08-23.** Results in [bound-variable-sweep-findings.md](../bound-variable-sweep-findings.md):
0/27 failures across both strata. Recommendation is to state the clause flatly
with no transition provision; three wording corrections have been applied to
the proposed contract edit. One residue item found for targeted cleanup, not
migration — see the findings' "Later choice-dependent residue".

## Why it exists

The [draft ADR](../draft-adr-collection-placement-follows-content-kind.md) and
the [proposed contract edits](../draft-collection-contract-edits.md) make the
longstanding `kb/notes/COLLECTION.md` requirement that titles and openings be
statable in general terms operational: a theoretical claim naming a choice must
bind it. Before the sweep, nobody knew how consistently the corpus already
followed that existing rule.

The answer changes how much pre-existing cleanup the clarification exposes. It
does not create a new semantic obligation, so an isolated old violation neither
breaks the collection nor requires a transition provision. A broad mismatch
would still make the clarification misleading unless paired with a cleanup
plan. Do not apply the contract edits before this reports.

## Question

Of notes sampled from `kb/notes/`, what share carry a free choice-variable in
a load-bearing claim, and what repair would each need?

## What counts

A claim carries a **free choice-variable** when all three hold:

1. It names or presupposes a selection some particular system made.
2. The sentence presents as general — no quantifier scopes the choice.
3. Its truth conditions depend on that selection.

These are **not** failures:

- **Universally bound.** "For any system that chooses X, Y follows."
- **Existential witness.** "At least one system does X, so X is feasible." The
  particular is evidence for a claim about the space.
- **Illustration after a general claim.** The claim stands without the example.

The discriminating test for the hard cases, which are notes using Commonplace
vocabulary: **restate the claim without the system-specific term.** If it
survives intact, the term was a label for something general — not a failure.
If the claim collapses or changes truth conditions, it depended on the
selection — a failure.

Judge the note's title, description, and opening argument. A free variable in
a late application paragraph is worth recording separately but is not the
finding.

## Sampling

Fixed so the result means something and cannot be cherry-picked:

- Frame: the 310 files directly under `kb/notes/`, plus all 23 under
  `definitions/`. Definitions are oversampled deliberately — the definition
  audit already suspects several of being stipulated machinery, so they are
  where failures are most likely and most consequential.
- Sample: sort each set by filename; take every 15th from the top-level set
  (≈20 notes) and every 3rd from `definitions/` (≈8).
- Skip nothing. If a sampled note is unreadable or ambiguous, record it as
  ambiguous rather than substituting a different note — substitution is how a
  sample stops being one.

## Output

Write `bound-variable-sweep-findings.md` in the workshop root. It must carry:

- One row per sampled note: path, verdict (`pass` / `fail` / `ambiguous`), and
  for a failure, the offending claim quoted and the repair it would need —
  **bind** (quantify the choice, note stays) or **relocate** (the proposition
  only reported what was selected).
- The rate, stated separately for the top-level sample and for `definitions/`.
- A recommendation on the contract clause: state flatly, or add a transition
  provision — and if the latter, what it should say.
- Any case where the three-part test was genuinely hard to apply. Those are
  more valuable than the rate; they are where the rule is underspecified, and
  the contract wording should absorb them before it binds.

## Completion condition

The findings file exists with every sampled note dispositioned, and the
contract-clause recommendation is specific enough to write from without
re-reading the sample.
