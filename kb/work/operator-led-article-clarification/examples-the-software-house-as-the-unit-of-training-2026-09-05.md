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
