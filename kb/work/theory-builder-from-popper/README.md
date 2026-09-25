# Theory builder from Popper

Posed 2026-09-25 by the operator (direction, not an agent proposal).

## Goal

Replace the KB's two overlapping base terms with one definition of exactly
the kind of system Commonplace builds, stated in terms borrowed from Popper.

- `conjectural-learning.md` is too broad for this job: it admits discarded
  theories, whole replacement, and systems without retention. It also
  presents itself as Popper's process under conditions, and then has to list
  where it narrows him.
- `theory-builder.md` (library version) does not require criticism, so a
  builder that never criticizes anything qualifies.

The new `theory-builder.md` requires localized, consumed, criticized, and
retained theories, and has no success condition: whether a builder learns is
the hypothesis under test. Localization is addressability's minimum; finer
grades are a design commitment. Criticism aimed at what localized units say is
what separates a builder from gradient descent.

## Decisions so far (operator, 2026-09-25)

Decision numbers D1–D8 refer to the
[consumer inventory](./consumer-inventory.md).

- Define the term in Popper's vocabulary; list the KB's additions as such.
- Reflective and autonomous are qualifiers, not conditions.
- Retire `conjectural-learning.md`, `reflective-theory-builder.md`,
  `autonomous-theory-builder.md`, and `externally-tested-theory-builder.md`;
  the qualifiers absorb the reflective and autonomous definitions. This
  reverses the 2026-09-21 workshop decisions that kept learner and builder
  apart and made criticism optional for a builder.
- Whole-theory rejection, and rebuilding from retained criticism (D3), are
  inside. Addressability is graded: localization (some unit carries content)
  is condition 1, finer grades are a design commitment. A model replaced
  whole is an addressable part of the machinery.
- Criticism aimed at what localized units say separates a builder from
  gradient descent; critique applied through weights is outside.
- D1: retitle the three notes named for conjectural learning (the research
  companion, the precedents note, the rules-weights evidence note). New
  titles come to the operator for approval; the companion's claim reverses.
- D2: retitle the article series away from "conjectural learning"; redirects
  keep old links working.
- D4: `conjectural-learning-checks.md` is replaced by
  [theory-builder-checks.md](../../notes/definitions/theory-builder-checks.md), promoted with the
  definition.
- D5: split the externally tested case. What a claim must supply for itself
  goes to `a-claim-without-external-assessment-carries-three-obligations.md`;
  the evaluation protocol, seed, extension, and intervention accounting go to
  the testing article.
- D6: generated reviews and retained results keep their link bytes and rely
  on redirects. The concurrent analysis batch is not paused; its output is
  treated as frozen under the old wording.
- D7: re-judge all source ingests condition by condition against the new
  definition, in batches delegated to subagents; swapping links alone is not
  enough.
- D8: restore "revision need not be small" (done) and "retention is the
  builder's, not the interpreter's" (done, in Boundary).
- N1: retention counts when what is kept is taken up on a new problem; rounds
  on one problem are one pass of error elimination (reading C). N2 and N3:
  the inventory's D1 titles and D2 headlines are approved; the lead article
  moves to `building-a-theory-builder-from-todays-llms.md`.
- Outside-system checks: `assess-learning-claims-during-ingest.md` and the
  analyse-agentic-system skill judge systems condition by condition against
  the new definition.

## Open

- Precedents note, Workspace Optimization: whether DreamTeam's levels within
  one game run count as new problems for condition 4. The note states it as
  unsettled by the source.
- Precedents note, runtime-model comparison: "additional contribution of
  learning through criticism" became "criticism aimed at what a theory says";
  check whether dropping "learning" changed the claim.
- Testing article grew from about 1,660 to 2,840 words; consider a
  tightening pass after the retitle.

- Problem granularity for condition 4 (raised by B4): workers read many
  instances of one task, or one benchmark's task family, as one problem, so
  instances are tests of one theory and only a different task is a new
  problem. This decided GEPA, procedural graphs, PoPE, and Corral. Confirm,
  and consider stating it in the definition's condition 4.
- Cleanup for step 6: unlinked "conjectural learning" outside Learning Claims
  sections (e.g. `automated-hypothesis-validation-sequential-falsifications`
  Extractable Value); its follow-up asks whether POPPER should be named in
  checks case 24.

## Steps

1. Draft [theory-builder.md](../../notes/definitions/theory-builder.md) and its
   [checks](../../notes/definitions/theory-builder-checks.md) — done.
2. Refresh the [consumer inventory](./consumer-inventory.md) against the
   current draft and the decisions above — done.
3. Operator approves the refreshed edit plan, including D1 and D2 titles —
   done (N1–N3).
4. Progress (2026-09-25): inventory steps 1–3 done — receiving sections
   (obligations note 33f44301, testing article 322953b6), definitions and
   AGENTS.md (38df120c), skills and types (3532f494). Inventory step 4:
   notes (85ef951e, 9e51af45) and articles (20a3928c). Step 5: ingest
   batches B1–B7 committed (467fea89, c666d569, 6ec3c22d, 58b83473,
   99b103c5, 37a36faa, 37a4d4c1). Next: settle problem granularity, then
   step 6 (relocations, deletions, redirects).
   Apply in the inventory's order: receiving sections, definitions, skills
   and types, notes and articles, ingest re-judging, links and redirects,
   frozen records last. Validate.
5. Close: delete this directory and its index entry.

## Closes when

The new definition replaces the library `theory-builder.md`, the retired
definitions are gone with their consumers migrated, and this directory is
deleted.
