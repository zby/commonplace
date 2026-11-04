---
description: "Audit of the semantic-reference and opacity revision chain, identifying remaining contradictions and arguments that still make natural-language ambiguity the defining obstacle in prompting."
type: types/note.md
tags: []
---

# Prompt semantics coherence audit, 2026-11-03

The definitions have changed further than several central arguments and their navigation. The KB now permits a prompt to have symbolic form under an adopted model reference, but still routes readers through claims that prompting differs from programming because it necessarily lacks precise semantics or necessarily executes probabilistically. The latest commit also promotes a proposed explanation of opacity into stronger definitional claims than its own scope permits.

This dated report is consumed by the requested KB coherence review and subsequent revision selection. It records findings, not completed repairs or new doctrine.

## Inputs and method

Inspected checkout HEAD: `3b7719bdaac77845ec358437730f89d49cae1f97`. The unrelated installation and framework-delivery working changes were outside the audit. Producer: Codex; exact model identifier unavailable. Governing instruction: the user's request to trace the definition revision chain from the latest commit and check KB coherence under the reference-LLM counterexample.

The relevant chain includes:

| Commit | Contribution |
|---|---|
| `c42dd3976` | Extracts the semantic-reference account. |
| `91cf09580`, `3d3bf2b44` | Relocates and revises opacity as question- and budget-relative. |
| `11c1d60f3` | Adopts path-relative form and reference-based codification. |
| `a2a3a089d` | Migrates ten vocabulary and interpretation consumers. |
| `29e7fd0ce` | Scopes nine dependent arguments to readable code and named paths. |
| `0cc7f89d1`, `78daf69a4` | Aligns links and resolves editorial leftovers. |
| `cc0493478` | Separates output variation from necessary indeterminism. |
| `cd786ae93`, `3b7719bda` | Adds supporting ingests and proposes near-decomposability as opacity's mechanism. |

Method: inspect the chain and definitions; search across `kb/` for opacity, English, natural language, prompt language, precise/underspecified semantics, deterministic execution and the retired criterion; read the central arguments and selected dependents; compare their conclusions under an adopted, fully specified reference-model package. Search included historical reports and external-system analyses, but findings distinguish current Commonplace claims from historical or source-attributed text. A backlink search for the four central prompting, programming-practices, verifiability and scoping notes returned 74 files across theory, tags, reference, instructions and articles. That count measures potential propagation, not 74 confirmed defects.

## Governing distinction

[Representational form](../../theory/definitions/representational-form.md), the classification of content under its consumption path, now separates localization from whether a reference fixes consequences. [Codification](../../theory/definitions/codification.md), the move into symbolic form, can occur by adopting a model package without rewriting the prompt. [Opacity](../../theory/opacity-depends-on-the-inspection-question-and-budget.md) separately asks whether a behavior or change can be established at acceptable inspection cost.

The audit's counterexample is a prompt executed against a complete model package adopted as the operation's reference, with runtime conditions and decoding specified. Its semantics need not be English semantics. Making that reference authoritative does not make the behavior easy to understand, make outputs adequate to the task, or make prompt edits easy to assess. A deterministic instance also removes randomness without removing those difficulties.

This supports the user's revised emphasis, with a qualification already required by the opacity definition: opacity is a practical, question-relative difference, not a universal partition of prompts from traditional programs. Traditional programs can also be opaque. English interpretation still matters when English governs requirements or conformance; it is not a necessary premise of the general prompting-versus-readable-code comparison.

## Findings

### F1 — The central prompting note incorporates the exception but retains the old thesis

[Agentic systems interpret underspecified instructions](../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) (since rewritten; the link reaches the replacement note), especially lines 16–44, 75–98 and 112–126 at the inspected revision, acknowledges reference adoption and nonessential indeterminism. Later sections still organize the design space as underspecified LLM semantics versus precise deterministic code. They define replacement with code as simultaneously resolving ambiguity and removing sampling, call LLM adherence always probabilistic, and say each constrained piece escapes both testing obligations.

These conclusions do not follow for the adopted deterministic package. Nor does moving to a symbolic reference necessarily expose a readable rule or settle requirement adequacy. The migration changed a local explanation without rebuilding the note's governing argument.

**Priority: high.** Reconstruct the general account around reference, inspection, adequacy and execution conditions. Keep natural-language projection as a scoped case. The English/Tarski discussion can remain supporting material or move behind the already separate semantics notes.

### F2 — The navigation still advertises the superseded distinction

[Computational model](../../tags/computational-model-README.md), line 14, calls underspecified semantics and execution indeterminism the core distinction for LLM instructions. This is the shortest route by which a reader inherits the old thesis even after the definitions changed.

**Priority: high.** Revise the entry with the central argument, rather than leaving navigation to summarize an obsolete conclusion.

### F3 — Testing advice conflates semantics, implementation and requirements

[Programming practices](../../theory/underspecification-and-indeterminism-complicate-programming-for.md), lines 12–34, says prompts are harder to verify because code has precise semantics, calls execution indeterminism novel, and says deterministic code has no gap between what it says and does, so only outputs need testing. [Automated tests for text](../../theory/automated-tests-for-text.md), line 21, repeats the last claim.

The reference-model counterexample removes the proposed categorical distinction. The existing semantics account also separates execution conformance from requirement adequacy for conventional code. Generator testing and generated-artifact testing remain distinct even when a producer is deterministic. The text-testing pyramid can survive without this justification.

**Priority: high.** Retain the practices; rebuild their explanation and make statistical repetition conditional on the property and execution variation being assessed.

### F4 — Scope guarantees are still inferred from representational form

[LLM context is composed without scoping](../../theory/llm-context-is-composed-without-scoping.md), under “The architectural response,” says the scoping problem is specific to natural-language content and that symbolic artifacts inherit scope from their interpreter. Its footer repeats that natural-language content has no deterministic interpreter.

An adopted model prompt is symbolic under the new definition without acquiring lexical isolation. Conversely, symbolic membership does not require a language to offer lexical scope. Constructing separate contexts remains a viable architectural response, but its benefit depends on excluded inputs and enforced boundaries, not the form label.

**Priority: high.** State the actual model/harness boundary and guarantee. Recheck the linked [shared-medium argument](../../theory/llm-context-interprets-instructions-and-content-through-one-medium.md) and [specification-level separation](../../theory/specification-level-separation-recovers-scoping-before-it-recovers.md) for the same inference. Their design observations need not be discarded.

### F5 — The latest commit turns a conjectural mechanism into a definition and necessity claim

[The near-decomposition note](../../theory/near-decomposability-may-make-local-inspection-affordable.md) explicitly calls the transfer conjectural. Its Scope says it needs a worked case before entering a definition as more than a mechanism. Yet [representational form](../../theory/definitions/representational-form.md), under “Opacity and inspection,” states that inspection cost *is* the length of the cheapest known explanation. [Addressable theory](../../theory/definitions/addressable-theory.md), under “Blame localizes only where interactions are weak,” states weak interaction as necessary for a located part to be a sound repair candidate.

The necessity does not follow from the admitted conjecture. A strongly coupled shared routine can still be implicated by a trace and repaired; coupling may broaden regression obligations without making it an unsound candidate. Also, description length alone does not account for the work of finding or checking an explanation. The earlier opacity definition admits abstraction, certificates and other analysis, not only affordable local reading.

**Priority: high.** Preserve question-relative inspection cost as the definition. Mark near-decomposability and the description-length reading as proposed mechanisms or proxies, with their conditions. Separate localization of a repair candidate from containment of its effects. This finding concerns internal warrant and logical strength; it does not adjudicate the external literature.

### F6 — Partial evaluation denies semantics where it should question equivalence

[Frontloading is partial evaluation](../../theory/frontloading-is-partial-evaluation-not-divide-and-conquer.md), under “Where the analogy stretches,” says there is no exact `[[P]]` because the program has underspecified semantics. Under the adopted package, a precise computational meaning can exist. What remains difficult is establishing that replacing a procedure by its precomputed result preserves the relevant behavior.

**Priority: medium.** Scope the claim to ordinary-language interpretation, and distinguish existence of semantics from evidence of equivalence and the cost of proving it. The separate claim that a shared text medium makes the operation partial evaluation also needs its own justification; it is not established by the new definitions.

### F7 — The verifiability gradient still bundles independent properties

[The verifiability gradient](../../theory/verifiability-gradient.md) calls its whole prompt-to-code ladder symbolic, presents deterministic modules as uniformly rewardable, and says a memory note is not diffable or reviewable. Its practical placement question remains useful, but a fixed reference does not supply a task oracle, and a text note can be diffed and reviewed.

**Priority: medium.** Separate reference adoption, inspection cost, execution cost and oracle quality. Code extraction can improve several together in a named case; neither symbolic membership nor determinism entails those improvements.

### F8 — Several downstream explanations still equate codification with extraction

These are concrete follow-up targets, with different repair needs:

- [Metacircular methodologies](../../theory/llm-executed-methodologies-are-metacircular-interpreters.md), “Codification is the compiled path,” says each instruction–skill–hook–script step reduces underspecification and indeterminism. This also conflicts with [methodology enforcement](../../theory/methodology-enforcement-is-constraining.md), which expressly rejects that inherent ladder.
- [Progressive constraining](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) treats code generation as producing a valid implementation from the allowed space, though generation can violate the requirement. Its opening calls the spec-to-program mapping many-to-one while its parent argument says one-to-many. Scope its advice to evidence-guided extraction; observed stability alone does not establish adequacy.
- [Instructions as typed callables](../../theory/instructions-are-typed-callables.md), line 31, frames operation implementations as movement from underspecified to precise semantics. Preserve that case while distinguishing an adopted model check from an independently justified requirement predicate.
- [Constraining during deployment](../../theory/constraining-during-deployment-is-continuous-learning.md), lines 10–16, calls prompts symbolic without a named adopted reference and attributes generality, speed, cost and reliability gains to every constraining step. Both exceed the revised definitions and the now-scoped trade-off note it cites.
- [Codification and relaxing](../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) correctly scopes its main argument to code extraction, but its complement paragraph still defines relaxing as replacing a codified component with a learned one. A replacement learned component can itself be codified under adoption; preserve the explicit extraction scope throughout.

**Priority: medium.** Repair these as dependent arguments, not by replacing every occurrence of “natural language” with “opaque.”

## What remains useful

[Implementations do not establish shared semantics](../../theory/implementations-do-not-establish-shared-semantics.md) and [symbolic form holds consumers to a semantic reference](../../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md) supply the distinction this audit uses. The latter already says the classification is architectural rather than a theory of language.

[Traditional software can bracket executor conformance](../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) explicitly scopes itself to ordinary prompt interpretation and separates the adopted-reference case. It can remain as a scoped account; it should not stand in for the whole programming comparison. [Natural-language meaning](../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) can remain a hypothesis about language rather than a prerequisite for the architecture.

[Legal drafting](../../theory/legal-drafting-solves-the-same-problem-as-context-engineering.md) and [source adoption policy](../../reference/source-adoption-policy.md) remain useful for requirements interpreted as natural language. Their claim to address prompting's distinctive medium needs that scope stated. The audit does not establish that their borrowing policy must change.

The earlier migration already scoped [inspectable artifacts](../../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md), [readable artifact loops](../../theory/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), and several code-extraction arguments. Preserve those distinctions rather than restarting the vocabulary migration.

## Revision order and acceptance

The revision should leave the KB able to explain why adopting a reference model fixes what an operation means without making it easy to inspect or adequate to its task.

1. Resolve F5's definitional overreach so dependents have a stable account of opacity.
2. Rebuild F1's central argument and F2's navigation around the independent questions.
3. Repair F3–F8 and inspect the central notes' backlinks for premises that changed.
4. Retain English-specific arguments under explicit scope; preserve source quotations and dated evidence as historical records.

Acceptance cases: an ordinary English prompt; the identical prompt under an adopted deterministic model; an adopted stochastic package; readable conventional code; opaque conventional code; a model-based check whose output is authoritative but inadequate to its intended requirement. Each account should distinguish what is fixed, what is observable at acceptable cost, what varies, and what evidence supports task adequacy. These are conceptual review cases, not proposed automated tests.

## Scope

This is a repository-wide search with targeted semantic reading, not a line-by-line certification of every KB artifact. External-system collections had no matches for the narrow obsolete-thesis phrases in the final scoped search; that is not a semantic clearance of those collections. Historical reports, ingests and archived proposals were not judged stale merely for retaining old terms. No external factual claims were reverified, no formal review jobs or freshness acknowledgements were run, and no library claims were edited. The eight findings group related defects; they are not a count of affected files.
