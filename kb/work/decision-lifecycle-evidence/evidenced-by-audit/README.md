# Audit of `evidenced-by` edges under ADR 091

## Scope and method

Run on 2026-09-26, after [ADR 091](../../../reference/adr/091-refutation-needs-a-checkable-counterexample-corroboration-a-test.md)
made "origin is not corroboration" binding in `kb/notes/COLLECTION.md`. The
operator asked for an audit of the existing edges before any are changed.

Every file outside `kb/work/`, `kb/reports/`, snapshots, collection contracts,
types, and the link vocabulary that contains `evidenced-by` was listed (212
files) and split into six batches. One read-only Opus worker per batch read
each edge's source context and skimmed its target, then classified it:

- **CORROB-OK** — the phrase already names a test the claim could have failed.
- **QUALIFY** — the target qualifies, bounds, or illustrates; no corroboration
  is claimed. No change needed.
- **CORROB-UNTESTED** — the wording presents the target as confirming the
  claim ("confirms", "shows", "corroborates", "independently converging") but
  names no test.
- **ORIGIN** — the claim was generalized from the target.
- **MISLABEL** — the target is not an observation or source (a premise, a
  companion, an instruction, a definition).

Workers judged timing from git creation dates only where it decided the
class. Classifications are model judgments and have not been reviewed edge
by edge. Batch files hold every non-QUALIFY edge as `file:line` with a
proposed replacement label and phrase; nothing in the library was edited.

## Results

| class | edges | share |
|---|---|---|
| CORROB-OK | 5 | 1% |
| QUALIFY | 206 | 58% |
| CORROB-UNTESTED | 20 | 6% |
| ORIGIN | 91 | 26% |
| MISLABEL | 34 | 10% |
| **total** | **356** | |

Batch 05 (source ingests) also holds 33 *recommended* `evidenced-by` edges,
instructions to a future note author: 21 QUALIFY, 7 CORROB-UNTESTED, 4
ORIGIN, 1 MISLABEL. They are counted separately and not in the table.

Per batch: [00](./batch-00.md) (91, including 42 agentic-systems citations of
pinned code, all QUALIFY), [01](./batch-01.md) (80, the highest ORIGIN count:
33), [02](./batch-02.md) (66, holding four of the five CORROB-OK edges, all
in `knowledge-storage-does-not-imply-contextual-activation.md`),
[03](./batch-03.md) (66), [04](./batch-04.md) (50, mostly `kb/reference/`,
where MISLABEL concentrates), [05](./batch-05.md) (ingests).

## What the numbers say

- **The KB almost never records a test.** Five edges of 356 name what a claim
  risked. The rest of the positive evidence is qualification, origin, or
  asserted confirmation.
- **About a quarter of the edges are origin.** Most common: a note generalized
  from an earlier ADR, a Commonplace episode, or a source it was written
  from. Under ADR 091 these explain where a claim came from and do not
  corroborate it.
- **Some edges can become real tests.** Workers found evidence recorded after
  the claim that the claim could have failed: ADR 069's binding-path audit
  (universal-framework note), the GBrain review (privilege-quarantine note),
  the program-theory evidence dated a day after its note, and the causal
  perturbation evidence already cited in the knowledge-storage note. Their
  phrases can name the test instead of being downgraded.
- **Some claimed predictions are not tests.** ADR 044 implemented a note's
  own recommendation three days later; ADR 056 appeared the same day as the
  note that "predicts" it. Implementing a claim does not test it.

## Contract gaps the fixes run into

These need an operator decision before a bulk relabel, because the obvious
fix is not a permitted label.

1. **Origin toward a note.** `abstracted-from` may not target `kb/notes/`.
   Several origin edges point to notes, including the evidence note
   `notes/evidence/commonplace-as-a-reflective-system.md` ("direct evidence
   base"). Options: permit `abstracted-from` toward `notes/evidence/`, or use
   `grounds`/`extends` and accept that the origin reading is lost.
2. **Origin toward an external URL.** No origin label may target `external`.
   Workers suggest ingesting the source first (Toulmin, Lampinen, Bainbridge)
   or rephrasing as qualifying in the meantime. Three arXiv links already
   have ingests and can be re-pointed.
3. **Reference edges into notes.** `kb/reference/COLLECTION.md` does not allow
   `evidenced-by` toward `kb/notes/`, yet five reference edges do (ADRs 068,
   079, 082, and two in the change-candidates doc). This is existing data
   that violates the contract, so it should be cleaned up rather than
   legalized.
4. **Reference docs pointing to the ADR they describe.** Reference has no
   `abstracted-from` toward reference and no registered label for "the
   decision this doc describes"; an unregistered `decision:` label already
   appears eight times. Falling back to `see-also` loses meaning.
5. **Ingests use `evidenced-by`.** `kb/sources/COLLECTION.md` does not permit
   it; the direction from source to claim is `is-evidence-for` (three edges).

## Proposed next steps

1. Operator decides gaps 1, 2, and 4 (gap 3 and 5 are plain cleanup).
2. Apply CORROB-OK upgrades and CORROB-UNTESTED rephrasings first: about 25
   edges, each a phrase edit with no label-vocabulary question.
3. Apply ORIGIN and MISLABEL relabels per batch after spot-checking a sample
   of each batch's classifications, one commit per batch.
4. Retire this directory once the edges are fixed; the counts above are the
   durable finding and belong in the commit message or a log entry.
