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
  ("under pinned algorithms and embedding models"). Second follow-up: "maybe
  double check about the pinned algorithms - the main idea is that the house
  can revise both natural language and symbolic forms of its own definition -
  this needs to be clear" — the paragraph now states that rule by
  representational form before placing indexes as the boundary case.
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
> distributed-parametric models fixed. The rule is by representational form:
> the house may revise both the natural-language and the symbolic forms of its
> own definition; only its distributed-parametric models are pinned. Derived
> indexes sit on the boundary between the forms and are an exception: they may
> be regenerated during the run because the records they are built from are
> revisable state and the embedding models used to build them stay pinned. The
> algorithms that build them are symbolic machinery, revisable like any other.
>
> The experiments below do not wait for a complete automated house. They test
> its learning mechanisms in bounded components.

## 5. The mechanism paragraph: unpack "separately testable from the outcome"

- **Commit:** see log (`Workshop:` trailer)
- **Kind:** Verdict without its why
- **Operator's verdict:** "apply the rest" (phase-2 sweep candidate 4)
- **Diagnosis:** A three-coordinate-clause mechanism sentence, and a closing
  verdict ("separately testable from the outcome of coherent modification")
  whose reason the reader could not reconstruct: mechanism claims are about
  how an update came to be, so they can differ between houses whose outcomes
  match.

**Before:**

> The proposed mechanism is that the explanation directs diagnosis toward the
> consumer path, the failure challenges the assumption that the input list is
> exhaustive, and a revised account identifies other files that need checks.
> Testing a second, untouched snippet asks whether that revision guides a later
> decision. These are claims about how updates are produced, separately testable
> from the outcome of coherent modification.

**After:**

> The proposed mechanism has three steps: the explanation directs diagnosis
> toward the consumer path; the failure challenges the assumption that the input
> list is exhaustive; and a revised account identifies other files that need
> checks. Testing a second, untouched snippet asks whether that revision guides
> a later decision. These are claims about how the house produces its updates,
> and they can be tested separately from the outcome: two houses can both end up
> modifying coherently while only one got there by revising an explanation.

## 6. "These episodes" and "persistence alone"

- **Commit:** see log (`Workshop:` trailer)
- **Kind:** Unintroduced term; verdict without its why
- **Operator's verdict:** "apply the rest" (phase-2 sweep candidate 5)
- **Diagnosis:** *Episodes* appeared as an anaphor with no antecedent;
  "persistence alone is insufficient" trailed the requirement it qualifies.
  Reordered: introduce episodes as episodes of production, state the
  insufficiency with its reason, then the requirement.

**Before:**

> Production implements current requirements and supplies evidence through
> operating consequences and retained history. These episodes may also be
> replayed, simulated, or augmented. Evidence of training requires experience to
> cause a retained change in the house's capacity on later requirements.
> Persistence alone is insufficient: every product edit changes the starting
> conditions of later work.

**After:**

> Production implements current requirements, and each episode of it supplies
> evidence: operating consequences and retained history. Episodes may also be
> replayed, simulated, or augmented. Evidence of training requires more than a
> change that persists — every product edit changes the starting conditions of
> later work. It requires experience to cause a retained change in the house's
> capacity on later requirements.

## 7. Introduce continuations

- **Commit:** see log (`Workshop:` trailer)
- **Kind:** Unintroduced term
- **Operator's verdict:** "apply the rest" (phase-2 sweep candidate 6)
- **Diagnosis:** *Continuation* first appeared here carrying the whole
  experimental design, and recurs in the hypotheses section ("paired
  continuations"). Introduced at first use: copies of the house that resume
  work from identical product snapshots.

**Before:**

> After correcting the failing edit in the example, give two continuations
> identical product snapshots. Retain the revised explanation and checking
> policy in one; restore their earlier versions in the other.

**After:**

> After correcting the failing edit in the example, run two *continuations*:
> copies of the house that resume work from identical product snapshots. Retain
> the revised explanation and checking policy in one; restore their earlier
> versions in the other.

## 8. The embodied-in-code comparison, said in ordinary words

- **Commit:** see log (`Workshop:` trailer)
- **Kind:** Compressed description
- **Operator's verdict:** "apply the rest" (phase-2 sweep candidate 7; the
  agent flagged "embody different lessons" as its interpretation of
  "equivalent current functionality" and the operator accepted)
- **Diagnosis:** "Compare implementations with equivalent current
  functionality" did not say what is compared with what or why equivalence
  matters. Reordered so the patch-is-both-production-and-training point leads,
  and the comparison is spelled out: implementations that currently behave the
  same but embody different lessons.

**Before:**

> When learning is embodied in product code, compare implementations with
> equivalent current functionality on later maintenance tasks. A patch can be
> both production and training, and the acquired capability can remain specific
> to one product. The comparison identifies its contribution to later work.

**After:**

> Learning can also be embodied in product code: a patch is then both
> production and training. To measure what it taught, compare implementations
> that currently behave the same but embody different lessons, on later
> maintenance tasks. The acquired capability can remain specific to one product;
> the comparison identifies what it contributes to later work.

## 9. Define the training lineage at first use

- **Commit:** see log (`Workshop:` trailer)
- **Kind:** Unintroduced term (two sites)
- **Operator's verdict:** "apply the rest" (phase-2 sweep candidate 8; the
  agent flagged its definition for checking and the operator accepted)
- **Diagnosis:** *Training lineage* appeared first in the continuity bullet
  and again in the Bitter Lesson section as "that training lineage" with no
  local antecedent, never defined. Defined at first use as the history of
  retained changes made while the models stay pinned; the second site now
  says "the training lineage".

**Before (continuity bullet):**

>   outside a model checkpoint. Their effective use may still depend on the
>   model, so replacing it requires revalidation and lies outside the fixed-model
>   training lineage.

**After (continuity bullet):**

>   outside a model checkpoint. Their effective use may still depend on the
>   model, so replacing the model requires revalidation and falls outside the
>   *training lineage* — the history of retained changes made while the models
>   stay pinned.

**Before (Bitter Lesson):** "that training lineage; the seed may be human-built"

**After (Bitter Lesson):** "the training lineage; the seed may be human-built"

## 10. Introduce source observations

- **Commit:** see log (`Workshop:` trailer)
- **Kind:** Unintroduced term
- **Operator's verdict:** "apply the rest" (phase-2 sweep candidate 9)
- **Diagnosis:** *Source observations* separates the facts supplied to every
  treatment from the observations each continuation makes itself —
  load-bearing for the whole treatment table, unexplained. Introduced in
  place: the facts observed before the continuations start, which each
  treatment retains in its own form.

**Before:**

> Use paired continuations with the same starting product, fixed models, tools,
> source observations, request sequence, and resource ceilings. Vary how
> observations are retained, then let each continuation learn from its own
> actions and observations. Compare four treatments:

**After:**

> Use paired continuations with the same starting product, fixed models, tools,
> request sequence, and resource ceilings, and the same *source observations*:
> the facts observed before the continuations start, which each treatment
> retains in its own form. Vary that retained form, then let each continuation
> learn from its own actions and observations. Compare four treatments:

## 11. Unpack "the retained learning pathway"

- **Commit:** see log (`Workshop:` trailer)
- **Kind:** Verdict without its why
- **Operator's verdict:** "apply the rest" (phase-2 sweep candidate 10)
- **Diagnosis:** Why the reconstruction sentence was there, and what "the
  retained learning pathway" meant, were both compressed: the treatments
  differ in what survives to the next decision, not in what the model can
  think in the moment.

**Before:**

> their explanations. All may revise executable machinery and its tests. A
> model can reconstruct an explanation while reasoning in any treatment. The
> comparison concerns the retained learning pathway.

**After:**

> their explanations. All may revise executable machinery and its tests. In any
> treatment the model can still build an explanation while reasoning; no
> treatment forbids thinking in theories. What differs is what survives to the
> next decision: the comparison concerns what each treatment retains, not what
> the model can construct in the moment.

## 12. Map the two kinds of change onto the two histories

- **Commit:** see log (`Workshop:` trailer)
- **Kind:** Unintroduced term
- **Operator's verdict:** "apply the rest" (phase-2 sweep candidate 11)
- **Diagnosis:** *History* arrived mid-paragraph ("both histories") and the
  mapping from the two kinds of change to the two histories was implicit.
  Now each kind of change is introduced as its own request history.

**Before:**

> Test two kinds of change separately. Adding another configured exporter input
> preserves the initial account of direct inputs. Adding indirect includes breaks
> its assumption that the list is exhaustive.

**After:**

> Test two kinds of change separately, each as its own request history. In the
> first history, adding another configured exporter input preserves the initial
> account of direct inputs. In the second, adding indirect includes breaks its
> assumption that the list is exhaustive.
