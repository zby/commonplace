# Examples: the unit-of-training article, 2026-09-05

Every edit made to `kb/articles/the-software-house-as-the-unit-of-training.md`
by the operator-led method, with the operator's words where the operator gave
them, the agent's diagnosis, and the text before and after. Run started from
the procedure in [README.md](./README.md); the whole-article read (step 2) was
done first and reported before any prose work.

## 1. Training vs. learning: state the relation once

- **Commit:** see log (`Workshop:` trailer)
- **Kind:** Unintroduced term (undrawn distinction between two alternating terms)
- **Operator's verdict:** "ok - fix both", accepting the whole-article read
  finding: the article uses *training* (title, regime name, "What counts as
  training") and *learning* ("theory-mediated learning", the unit-of-learning
  note) without stating their relation, and "What is trained" cites the
  unit-of-learning note as if the terms were interchangeable.
- **Diagnosis:** The duality survives from the article's origin as the
  "training doctrine" half of the split (`292b0dd0`); it is deliberate but
  undrawn — training is the regime imposed, learning the capacity change it
  produces. Fixed by stating the relation once, at the point where the clash
  first bites: the section that puts the unit-of-learning note under the
  unit-of-training title.

**Before:**

> ## What is trained: the whole house
>
> [The deployed system, not the model alone, is the unit of
> learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md)
> because several components jointly determine its behaviour.

**After:**

> ## What is trained: the whole house
>
> In this article *training* names the regime — what production is arranged to
> do to the house — and *learning* names the retained change in capacity that
> results. Both have the same unit. [The deployed system, not the model alone,
> is the unit of
> learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md)
> because several components jointly determine its behaviour.

## 2. TL;DR: restore the sample-efficiency claim

- **Commit:** see log (`Workshop:` trailer)
- **Kind:** Lost claim after restructure (partial: one of three hypotheses
  dropped from the TL;DR)
- **Operator's verdict:** "ok - fix both", accepting the whole-article read
  finding: the TL;DR's last sentence names only "diagnosis and transfer",
  while the hypotheses section asks three questions (influence,
  transfer/recovery, sample efficiency) and the frontmatter description names
  all three ("causal influence, transfer, and learning cost").
- **Diagnosis:** The TL;DR silently narrowed the empirical hypothesis to two
  of its three questions. Fixed by naming the third; *sample efficiency* is
  the article's own term for it (the sample-efficiency hypothesis).

**Before:**

> dependencies change. Whether this improves diagnosis and transfer compared
> with other uses of the same evidence is an empirical hypothesis.

**After:**

> dependencies change. Whether this improves diagnosis, transfer, and sample
> efficiency compared with other uses of the same evidence is an empirical
> hypothesis.

## 3. TL;DR: introduce the mediator, label the example

- **Commit:** see log (`Workshop:` trailer)
- **Kind:** Unintroduced term; unlabelled example
- **Operator's verdict:** "1 - apply" (phase-2 sweep candidate 1)
- **Diagnosis:** *Mediator* connects to the subtitle's *theory-mediated
  learning* but the TL;DR never says what mediates what; the checking
  sentence is an example without being announced as one.

**Before:**

> The house's *program theory* is its understanding of the software's purpose,
> organization, and how to handle new requests. The proposed mediator is an
> *explicit project theory*: one possible written carrier of that understanding,
> stating design commitments, causal assumptions, and invariants. A house that
> explains why some files need product checks may adapt its checking policy when
> dependencies change.

**After:**

> The house's *program theory* is its understanding of the software's purpose,
> organization, and how to handle new requests. The regime's proposed mediator —
> what experience revises and later decisions consult — is an *explicit project
> theory*: one possible written carrier of that understanding, stating design
> commitments, causal assumptions, and invariants. For example, a house whose
> theory explains why some files need product checks can adapt its checking
> policy when dependencies change.

## Skipped: the premise boundary paragraphs (sweep candidate 2)

- **Operator's verdict:** "2 skip - building the seed is from a different cycle"
- **Lesson:** The agent's proposed why for "This boundary applies during the
  run" (that a human-built seed does not violate it) read the seed into the
  wrong cycle; the seed belongs to a different cycle than the run the boundary
  governs. A verdict-without-its-why fix that supplies the wrong why is worse
  than the compression; when the why is inferred rather than stated nearby,
  flag it for the operator instead of writing it in.

## 4. Derived indexes are an exception; the scope sentence gets its own move

- **Commit:** see log (`Workshop:` trailer)
- **Kind:** Verdict without its why; unsignposted role
- **Operator's verdict:** "3 indexes are kind of on the boundary between
  symbolic and distributed parametric - I think we can state that they are an
  exception" (phase-2 sweep candidate 3); follow-up after the first commit:
  "actually algorithms don't need to be pinned" — the pin covers
  distributed-parametric models only, so the sentence keeps only the embedding
  models pinned and names the building algorithms as ordinary revisable
  machinery. This corrects a claim the pre-edit article text also made
  ("under pinned algorithms and embedding models").
- **Diagnosis:** The index sentence stated a permission with no reason. The
  agent proposed "looks like an exception but is not one"; the operator
  corrected the frame: indexes sit on the boundary between symbolic and
  distributed-parametric forms, so state them as a genuine exception to the
  pin, justified because only the input records change. The article's reading
  instruction (experiments run before a complete house exists) was also
  buried as the paragraph's last sentence; it now stands alone.
- **Frame correction:** The agent's rewrite denied the exception to defend the
  premise; the operator accepted the exception instead. Lesson: when a rule
  has a borderline case, saying "this is an exception, and here is why it is
  safe" can be more honest than arguing the case back inside the rule.

**Before:**

> Training changes its surrounding state and machinery while keeping
> distributed-parametric models fixed. Derived indexes may be regenerated from changing records
> under pinned algorithms and embedding models. The experiments below test
> learning mechanisms in bounded components before a complete automated house exists.

**After:**

> Training changes its surrounding state and machinery while keeping
> distributed-parametric models fixed. Derived indexes are an exception: they
> sit on the boundary between symbolic and distributed-parametric forms, and
> they may be regenerated during the run because the records they are built
> from change while the embedding models used to build them stay pinned. The
> building algorithms are ordinary machinery the house may revise.
>
> The experiments below do not wait for a complete automated house. They test
> its learning mechanisms in bounded components.
