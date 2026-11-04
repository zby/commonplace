# Projection inventory

## Decision, 2026-11-04

Projection is not registered. It stays ordinary language, and the
[collision ledger](../../reference/vocabulary-collision-ledger.md) records why.
The technical relation is registered as
[program refinement](../../theory/definitions/program-refinement.md), a compound,
because the bare word already means iterative improvement across the library.
An executor's unchecked output is a candidate refinement. The remaining work
is a wording pass, not a rename: the Tier 1 sites that treat projection as a
model ("projection model", "spec-to-program projection model", "a valid
projection", "the projection-versus-compilation distinction") are reworded in
terms of candidate and checked refinement; metaphorical uses may stay. Tier 2
backlinks are re-grounded on the program-refinement and constraining
definitions.

Tier 1 done, 2026-11-04: commits 263966e5c (practices note and brief),
a3f3ccb75 (progressive constraining) and 9d800927d (the other eleven files).
No library file outside the ledger uses projection in the spec-to-program
sense. Tier 2 re-grounding and the Tier 3 label sweep remain; the Tier 1
files that also sat in Tier 2 (changing-requirements, commitment-not-derivation,
llm-output-deviation, progressive-constraining, specification-strategy,
fix-what-the-executor, constraining-README, both ingests) were re-grounded in
the same commits.

Working inventory for deciding whether "projection", the KB-local term for an
executor choosing one outcome from the set an instruction permits, is kept,
redefined or replaced by "refinement" after the Dijkstra and Morgan ingests.
Compiled 2026-11-04 by search; the counts are occurrences in library prose,
tag heads and ingest reports. Snapshots, ADRs, proposals and workshop files are
excluded. The word also has unrelated senses in the KB (context-view
projection, LLM-call projection in the select/call lemma, skill projection,
parametric projection); those files are not listed and need no change.

## Tier 1: files that use the term in the spec-to-program sense

Any rename or redefinition touches every file here.

| File | Uses | What the term does there |
|---|---|---|
| `kb/theory/progressive-constraining-commits-only-after-patterns-stabilize.md` | 7, including the description | Central use: "projection, not compilation"; one-shot generation "freezes a single projection" |
| `kb/theory/specification-strategy-should-follow-where-understanding-lives.md` | 4 | "admit multiple valid projections"; "silent projection" as the risk of a fossilized spec |
| `kb/theory/changing-requirements-conflate-genuine-change-with-disambiguation.md` | 3 | A spec author "performed a projection"; links the central note as the "spec-to-program projection model" |
| `kb/theory/commitment-not-derivation-creates-new-ground-truth.md` | 2 | "a projection, not a compilation"; footer grounds "the projection-versus-compilation distinction" on the central note |
| `kb/theory/fix-what-the-executor-cant-determine-not-what-it-will.md` | 2 | "independent local projections"; "plural projections described by" the central note |
| `kb/theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md` | 1 | "incompatible local projections" needing an actor to resolve them |
| `kb/theory/llm-output-deviation-requires-three-way-diagnosis.md` | 1 | Footer: "the projection model that makes `V` an object rather than a metaphor" |
| `kb/theory/a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md` | 1 | "projects an interpretation into [a gap]. Which way the projection goes" |
| `kb/theory/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md` | 1 | "freezes one projection of the theory", linking progressive constraining |
| `kb/theory/underspecification-and-indeterminism-complicate-programming-for.md` | 1 | In the working-tree rewrite: "does not establish that the implementation is a valid projection" |
| `kb/theory/underspecification-and-indeterminism-complicate-programming-for.brief.md` | 2 | Reserved decision: the term may remain until the refinement question is settled |
| `kb/tags/constraining-README.md` | 1 | Gloss on the central note: "the spec-to-program projection model, semantic boundaries, and the constrain/relax cycle" |
| `kb/sources/simplification-2090443748077416467.ingest.md` | 2 | "several materially different quality projections"; "which projection the user intended" |
| `kb/sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md` | 2 | "making projections visible"; links the central note as the "projection model" |

Fourteen files, thirty occurrences.

## Tier 2: links to the central note whose gloss depends on the model

These do not all use the word, but each cites
`prompting-changes-failure-diagnosis-with-the-semantic-reference.md` for the
interpretation-space or projection claim that note no longer states. They need
re-grounding whatever happens to the term: either to a paragraph added to the
central note's English-account section, to the constraining definition, or to
a new home. Line numbers are at the inventory date.

Theory:

- `kb/theory/definitions/constraining.md` 11, 79: "admits several valid readings"; "why natural-language artifacts leave an interpretation space to narrow"
- `kb/theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md` 10, 27, 37: outputs "outside the space of valid interpretations"; the "idealised two-phenomena model"
- `kb/theory/process-structure-and-output-structure-are-independent-levers.md` 32, 46: "interpretation narrowing"; constraints narrow "different parts of the interpretation space"
- `kb/theory/selecting-an-llm-output-fixes-a-result-not-its-interpretation.md` 12: "may admit several valid interpretations"
- `kb/theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md` 22: "every agent run selects among multiple valid interpretations"
- `kb/theory/writing-styles-are-strategies-for-managing-underspecification.md` 10: strategies for managing the interpretation space
- `kb/theory/legal-drafting-solves-the-same-problem-as-context-engineering.md` 16
- `kb/theory/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md` 14: "retain several valid executions even when activation is fixed"
- `kb/theory/methodology-enforcement-is-constraining.md` 45
- Plus the Tier 1 theory files that link the central note: changing-requirements 18, commitment-not-derivation 18 and 88, llm-output-deviation 75, progressive-constraining 10 and 31, specification-strategy 12

Tags:

- `kb/tags/constraining-README.md` 14 (also Tier 1)

Ingests:

- `kb/sources/agentic-code-reasoning.ingest.md` 53
- `kb/sources/context-engineering-ai-agents-oss.ingest.md` 43
- `kb/sources/eric-evans-ai-components-deterministic-system.ingest.md` 37
- `kb/sources/shi-agenti-chotiri-navichki-vazhlivishi-za-dobriy-prompt.en.ingest.md` 35
- `kb/sources/towards-a-science-of-ai-agent-reliability.ingest.md` 43
- Plus the Tier 1 ingests: simplification 33, what-spec-driven-development 38 and 70

Twenty-two files beyond Tier 1's overlap; twenty-nine link sites in all.

## Tier 3: every other backlink to the central note

The central note has 71 inbound files (37 theory, 29 sources, 4 tags, 1
reference). The 70 files not rewritten in the relocation commit still label it
by the deleted title "agentic systems interpret underspecified instructions".
Those outside Tier 2 need only the label and a gloss check, not re-grounding.

## What "interpretation space" does not need

Thirty-three files use "interpretation space". The term is defined in the
constraining definition and names the set, not the act of choosing from it.
Replacing projection by refinement leaves it in place: refinement narrows the
interpretation space. Only the Tier 1 and Tier 2 sites change.

## Sources now available for the decision

- `kb/sources/ewd472-guarded-commands.ingest.md`: nondeterministic choice as a
  construct; "Only permissible final states are possible and each permissible
  final state is possible."
- `kb/sources/morgan-the-specification-statement.ingest.md`: a specification
  as a program; refinement as "every specification satisfied by P is satisfied
  by Q also"; monotonic composition.
- `kb/sources/wg14-n1570-behavior-definitions.ingest.md`: unspecified,
  implementation-defined and undefined behavior as three grades of an open
  choice.
