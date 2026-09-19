# Initial import assessment

Working interpretation, 2026-09-19. None of these proposals changes library doctrine. Source numbers refer to the [reading record](./reading-and-search.md); the examples and transfer judgments below are our construction.

## Most promising import

Separate five questions that our existing prose sometimes compresses:

| Question | Example | Consequence for Commonplace |
|---|---|---|
| Does a requirement admit several realizations? | Return any integer above ten | Multiplicity alone does not make conformance vague |
| Are the interpretation conventions settled? | Write a short explanation | A candidate may be acceptable under one reading and excluded under another |
| Can satisfaction be decided by a procedure? | Whether a program terminates on every input | A defined property need not have a general executable checker |
| Does the interpreter conform? | It returns nine despite an explicit lower bound | Actual behavior cannot define its own correctness standard |
| Does added context preserve or revise meaning? | A later sentence changes what “short” means | Context updates need not be vocabulary extensions |

The first four distinctions refine the [three-way diagnosis](../../notes/llm-output-deviation-requires-three-way-diagnosis.md) without replacing its intended-set/valid-set/distribution account. Institutions become particularly relevant when representations or vocabularies change. A fixed set of acceptable outputs alone cannot specify the corresponding changes to observations and sentences.

The literature supplies several different tools. Sources 1–4 concern satisfaction and structure-preserving changes; source 6 gives a scoped natural-language precedent; source 7 retains unresolved semantic alternatives; source 8 varies interpretation conventions; source 9 permits selective preservation. These are candidates for different jobs, not competing complete theories of LLM operation.

## A bounded example: renaming, strengthening, and choosing

Take a controlled reporting vocabulary with two atomic propositions:

- `sourced`: every substantive factual assertion has an identified source.
- `brief`: the report has at most 200 words under a stipulated counting rule.

For the mathematical example, a signature is a finite set of proposition names. Sentences are Boolean formulas over them. Models are Boolean valuations, treated as a discrete category. A signature map is a function between name sets; sentence translation substitutes names, and model reduction composes a target valuation with that function. Satisfaction is ordinary Boolean evaluation. Identity and composition follow substitution/composition; satisfaction agrees for atoms by definition and for Boolean formulas by induction.

This is an instance of the propositional construction, not a new institution for ordinary English. In particular, assigning `sourced` to an actual report remains a semantic assessment. The Boolean formalization does not solve that assessment.

Let the initial requirement be `sourced`.

| Candidate report | `sourced` | `brief` | Initial requirement | Strengthened requirement |
|---|---|---|---|---|
| A | true | true | admitted | admitted |
| B | true | false | admitted | excluded |
| C | false | true | excluded | excluded |

**Rename:** map `sourced` to `evidence-linked` and `brief` to `within-limit`. Interpret those target names by the corresponding properties. Sentence translation and valuation reduction preserve satisfaction. Replacing the word while quietly changing what counts as a source would violate this stipulated mapping.

**Strengthen:** replace `sourced` with `sourced AND brief` over the same signature. The satisfying class shrinks. This is a change of requirement, not a renaming operation. An implementation committed to producing A conforms to both requirements, but selecting A does not retrospectively make B invalid under the original one.

**Execute:** let an interpreter generate A, B, or C. Its distribution is additional data. Concentrating on A changes behavior; it does not by itself change either requirement's satisfying class.

**Vary the reading:** replace the stipulated word limit with ordinary “brief.” Two reasonable counting or length conventions can classify the same report differently. A family of satisfaction relations now needs an account of which readings are admissible. Taking the union of their valid classes asks whether some reading accepts; taking the intersection asks whether every reading accepts. Neither choice is automatically the public meaning of the instruction. Standpoint-style machinery can expose this choice but cannot decide it for us.

**Counterexample to arbitrary context maps:** “Give a brief report; here brief means at most 200 words” followed by an authorized revision to 500 words changes the classification of a 300-word report. This is not a truth-preserving rename with the report held fixed. Treating every context addition as a signature morphism would conceal the requirement change.

## Candidate library corrections

1. In [Agentic systems interpret underspecified instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md), qualify the opening claim that natural-language specifications lack precise denotations. Distinguish multiple satisfying candidates from uncertainty about the satisfaction relation. The example above is enough to show why the distinction matters; a broad theory of natural language is unnecessary.
2. In that note's impossibility paragraph, separate semantic definition from a total executable interpretation/decision procedure. Any Tarski, Gödel, or halting claim must identify the formal assumptions and prohibited procedure. The existing blanket appeal does not itself establish the claimed limit for ordinary language. A dedicated primary-source audit is still needed before rewriting that argument.
3. In [Constraining](../../notes/definitions/constraining.md), distinguish narrowing within fixed conventions from choosing or revising the conventions. Both can change behavior, but set inclusion only follows when the candidates and interpretation basis are comparable.
4. Preserve the [interpreter-failure note's](../../notes/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) separation of conformity from actual behavior. Add a qualification only where unresolved public readings make the boundary contestable; do not collapse all violations into ambiguity.

These are proposed edits for later grounded promotion, not completed changes.

## What the initial pass establishes and leaves open

There is a direct literature connection, including a worked institutional construction for a restricted natural-language semantic domain (source 6). The import does not have to rely entirely on an analogy to software specification. The bounded example also separates three operations with different obligations: preserving conformance, strengthening a requirement, and choosing a realization.

It does not establish a satisfaction relation for unrestricted natural language, a semantics-preserving prompt transformation, a reliable way to assign report properties, or a solution to the ideal interpreter's correctness problem. Existing institution results can be borrowed only after their hypotheses hold for our construction.

The next discriminating case should use one real instruction and two consequential readings. Determine whether the defect is an omitted constraint, a contested convention, or a context revision. Then compare the existing valid-set description with an explicitly indexed family of readings. If the latter changes no diagnosis or permitted operation, stop at the conceptual corrections instead of developing a larger formalism.
