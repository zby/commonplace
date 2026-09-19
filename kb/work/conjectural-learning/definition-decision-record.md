# Decision record: what the conjectural-learning definition is for

Status: proposed by the drafting agent on 2026-09-19 at the operator's
request, after the definition reversed several times in one day. The purpose
and tests below are for the operator to adopt, change, or reject. Until then
they record why the drafts stand where they do.

## Context: what kept reversing

| Question | Positions taken, in order |
|---|---|
| Is addressability of parts required? | Required (library) → possible benefit → required again → stronger property and a conjecture |
| Is reconstruction from records inside the term? | Outside (library) → inside → split: retained criticisms inside, raw records outside |
| Does a theory used within one episode count? | Outside (library) → inside (first candidate) → relative to a declared horizon |
| Is learning in the weights covered? | Outside (library) → undetermined (first candidate) → outside, with coevolution as an extension |
| Must criticism produce a revision? | Yes → no: a part that survives counts |

Each reversal followed a good argument. They pulled in different directions
because the definition was being asked to do several jobs at once, and each
argument served a different job:

- **Name what the research program builds and studies.** This pulls toward a
  narrow term: addressable theories, retained, with fixed weights.
- **Keep the program's comparisons fair.** A benefit we believe in should be a
  conjecture with a baseline. Written into the definition it becomes true by
  stipulation. This pulls conditions out of the term.
- **Classify systems we did not build.** This needs membership that can be
  decided from a system's artifacts and interventions on them.
- **State an honest relation to Popper.** This pulls toward his generality
  and few additions.
- **Simplify the library.** This pulls toward fewer terms and shorter text.

The addressability reversals are the first two jobs in conflict. We build
addressable theories, and we also want to test whether addressability pays.

## Proposed purpose

The definition names the kind of learning process the research program
studies, so that the program's conjectures can be stated against it and tested
fairly. Classifying other systems and the relation to Popper are constraints
on how it is written. They do not decide its scope.

## Proposed tests for any change to the definition

1. **Kind, not degree.** A condition belongs in the definition only if
   removing it changes which mechanism does the learning: what eliminates
   errors, what they are eliminated from, or what persists. A condition whose
   removal leaves the mechanism and changes how well it works is a conjecture
   with a baseline. By this test formulation in language, operative use,
   criticism of content, and persistence across the horizon are definitional.
   Addressability of parts, and retaining the theory against rebuilding it
   from retained criticisms, are conjectures. Fixed weights are a study
   condition.
2. **Every exclusion is a named comparison.** An arrangement outside the term
   is specified well enough to be run as a baseline. The definition never
   settles an empirical question by leaving the rival out.
3. **Decidable without claims about internals.** Membership rests on
   formulated artifacts and on interventions that vary their content. Nothing
   depends on what a model does internally.
4. **Each condition is attributed.** Popper's, ours, or an empirical
   question.
5. **No term without a claim.** A new term enters only when a claim cannot be
   stated without it.
6. **A change reports the cases it flips.** Run the proposed wording against
   the cases below and say which change class. A change that flips none is
   wording. A change that flips one is a scope decision for the operator and
   names the test it appeals to.

## Cases to check a change against

Classification under the drafts as of 2026-09-19.

| # | Case | Class | Settled by |
|---|---|---|---|
| 1 | A retained theory with separate parts is criticized and revised part by part | Inside | Both conditions |
| 2 | A retained prose theory is criticized for what it says and replaced whole | Inside | Test 1; reversed twice |
| 3 | Formulated criticisms are retained and a theory is rebuilt from them when needed | Inside | Persistence of the effect of criticism |
| 4 | Raw records are retained and a theory is rebuilt from them each time | Comparison | No formulated criticism persists; test 3 |
| 5 | Prompts or programs are varied and selected by score | Comparison | Criticism of content |
| 6 | A theory is built while reasoning and discarded after the decision | Comparison at a cross-episode horizon; inside for a within-episode claim | Declared horizon |
| 7 | Weights are adapted and no formulated theory guides decisions | Comparison | Formulation |
| 8 | Weights, prompts, and code evolve together around a formulated operative theory | Inside, as an extension | Both conditions still hold |
| 9 | Instructions are applied and never criticized | Excluded | No criticism |
| 10 | A theory is stored and nothing consumes it | Excluded | Not operative |
| 11 | A theory survives an attempted refutation and the result is recorded | Inside | Criticism is attempted elimination |
| 12 | One model proposes and criticizes its own theories | Inside | The definition asks less than Popper here |
| 13 | Criticisms are written down, but placebo text of the same form has the same effect | Not shown to be inside | Content half of membership needs an intervention |

## Likely next reversals

- **Case 3.** The accepted review wording, “retains revisions or
  replacements”, would move it outside. Test 1 keeps it inside, since the
  mechanism is the same and only the cost differs.
- **Case 12.** Requiring an independent critic would move it outside. By
  test 1 this is arguably a change of kind, since who eliminates changes.
- **Case 6.** Whether within-episode learning deserves the word *learning*.
- **The name.**

## Consequences if adopted

Reviews of the definition are asked to state which test a proposed change
appeals to and which cases it flips. The decision log in the
[README](./README.md#directions-that-changed-the-first-formulation) keeps the
history; this record keeps the reasons the history should stop repeating.
At migration the purpose and tests could become an ADR or a short section of
the companion note, and the cases could become its boundary-case table.
