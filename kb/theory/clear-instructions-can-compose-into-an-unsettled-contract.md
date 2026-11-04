---
description: "Uses a JSON-only rule and a general exception rule to show how scope and precedence can leave combined requirements unsettled, even when each instruction has a clear ordinary use."
type: types/note.md
traits: [title-as-claim]
tags: [computational-model, llm-reliability]
---

# Clear instructions can compose into an unsettled contract

An instruction can have a clear ordinary use while its interaction with another instruction remains unsettled. Scope, precedence and exception handling determine which requirements govern a case. When those relationships are left to interpretation, making each sentence more precise need not make the combined contract precise. This matters when a KB assembles instructions from general policies, skills, task requests and tool contracts: reviewing each document alone can miss a consequential choice created by their combination.

The primary claim concerns the semantics of English instructions: what they jointly require can depend on relationships that the text and its governing conventions leave unsettled. It applies to human interpreters too. Using English to control execution makes the consequence operational: an executor must select a response or a recovery path, and that selection can conceal a choice the instructions did not settle. This note treats English as the governing requirement language. Its later comparison with a model-defined prompt language explains the different role English plays when used to predict execution.

## A format rule meets an exception rule

Consider a task instruction:

> Return JSON only.

Now suppose a general policy also applies:

> If the operation fails, raise an exception.

The format rule has a clear ordinary use: it excludes commentary around a normal result. The exception policy has a clear ordinary use: it prevents failure from being silently presented as success. Together, they leave questions that neither sentence answers explicitly:

- Does “return” cover only successful results, or every response to the caller?
- Is raising an exception a separate control path, or a message whose content must be JSON?
- Does the general policy supply an exception to the local format rule, or does the local rule constrain how the general policy is fulfilled?

A runtime or an inherited protocol could already settle these questions. In its absence, two readers could agree about what each rule normally does and still disagree about whether a non-JSON failure report violates the combined instructions. The case is constructed to expose the missing relationship; it is not a reported model trial.

The diagnosis therefore depends on the whole applicable contract. A Markdown wrapper around an ordinary successful result may clearly violate it. The same verdict cannot simply be carried over to every failure path without checking which rules govern that path.

## The missing information concerns composition

The uncertainty is about how requirements combine. **Scope** determines the cases a rule governs. **Precedence** determines which rule controls when requirements conflict. **Exception handling** determines how a special case changes the ordinary obligations. Uncertainty in any of these can leave the boundary between permitted behavior and violation unsettled.

This differs from a reference explicitly withholding a guarantee in a designated case. The [semantic-reference account](./symbolic-form-holds-consumers-to-a-semantic-reference.md) separates permitted variation, excluded guarantees and defects in the reference. If a rule precisely identifies a case where no guarantee applies, the absence of the guarantee is itself specified. In the example here, whether the format guarantee applies to an exception is the unresolved question. Actual formal specifications can also leave such relationships ambiguous; the comparison concerns what the governing rules settle.

One way to settle the example is to state that successful results are JSON and failures use a separate exception channel. Another is to require every response, including an error record, to be JSON and to prohibit a separate exception channel. These are different contracts. Choosing between them requires the caller's needs and the runtime's capabilities; polishing either original sentence does not supply that choice automatically.

## The two accounts of prompting locate the problem differently

When English instructions govern correctness, the combined contract needs an interpretation. A reader may need to resolve both what a rule requires and whether it applies. Disagreement does not automatically establish interpreter failure, but this does not make every violation contestable: an applicable contract can settle a case sufficiently to judge it.

When a system instead adopts a specified LLM package as the operation's semantic reference, the package fixes how the combined prompt executes, including any permitted variation. Its response can conform to that reference while failing the caller's intended contract. The composition is then computationally specified, but its effects may be [opaque](./opacity-depends-on-the-inspection-question-and-budget.md), meaning too costly to establish for the question at hand. English-based expectations about scope and precedence become predictions to check against that behavior as well as possible requirements for judging it.

The [two-level prompt account](./english-can-approximate-a-model-defined-prompt-language.md) examines English in this predictive role. A clause can identify a semantic responsibility while leaving some interactions out of its coarse description. Local reasoning works only as far as that description captures the relevant interactions. The connection to this note's claim is indirect: uncertainty about English applicability or precedence can limit the behavioral description we construct from it. A settled English reading can also predict model behavior poorly, so resolving the requirement and establishing predictive fidelity remain separate tasks.

## Consequence for KB instruction design

Instruction review needs cases that cross document boundaries, especially failure paths where a general policy meets a task-specific requirement. The question is which combined obligation the agent should follow. If the caller needs a definite outcome, the contract should supply the relevant composition rule or an explicit route for resolving the choice.

Settling that rule and reliably applying it are separate tasks. A written exception policy can settle the intended reading without ensuring that a model follows it. A harness that implements separate success and failure channels can enforce that particular separation, while leaving other judgments to the model. [Context scoping](./llm-context-is-composed-without-scoping.md) concerns the architectural exposure and influence of content; this note concerns what the applicable instructions jointly require.

## Scope

The claim is that unsettled composition can survive locally clear wording. It does not say that every English instruction is ambiguous in every context, that formal languages have flawless specifications, or that precedence alone resolves every conflict. Shared conventions and explicit contracts can settle many cases.

Whether missing or unreliable composition rules explain most prompting failures is an open empirical hypothesis. The example establishes a possible mechanism, not its prevalence. The same issue can arise in human-interpreted instructions; LLM execution is not a necessary condition.

---

Relevant Notes:

- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — contrasts: architectural influence boundaries differ from rules settling the combined instruction contract
- [Symbolic form holds consumers to a semantic reference](./symbolic-form-holds-consumers-to-a-semantic-reference.md) — grounds: distinguishes a declared absence of guarantees from a reference that does not settle a case
- [English can approximate a model-defined prompt language](./english-can-approximate-a-model-defined-prompt-language.md) — contrasts: English used to predict model behavior has a fidelity question separate from what the instructions require
- [Silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — extends: successful execution can hide a composition choice that the instructions left unsettled
