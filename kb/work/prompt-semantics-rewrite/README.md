# Proposal: the main argument for the prompting rewrite

## Commission and status

On 2026-11-03 the operator requested a proposal for rewriting
[Agentic systems interpret underspecified instructions](../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md),
following the [coherence audit](../../reports/retained/prompt-semantics-coherence-audit-2026-11-03.md)
and the discussion of coarse and detailed prompt semantics. This is an agent
proposal for the argument, not an adopted replacement or an empirical result.
Its purpose is to settle what the central note should explain before rewriting
it and its dependents.

Current stage, 2026-11-04, later: every audit finding has a repair commit
and the projection term is retired; see Disposition below. The earlier stage
note follows. The central rewrite and supporting extraction are
implemented for review. Fable's review requested an explicit shared prediction
burden, an English adjudicator, a qualified conjecture title, a standalone
prompt approximation note, and a concrete MDL residual mapping. The library
now carries those changes. This workshop remains the review checklist before
selecting the next dependent repairs; it is not an independent semantic reference.

The operator's direction is to make opacity central to the comparison with
traditional programming, preserve the useful localized semantics of prompts,
and treat English-versus-programming-language differences as a supporting
question. The operator's further framing starts by constructing a prompt
language with English surface forms and semantics supplied by a particular
LLM package, then contrasts programming in that language with asking a
fallible interpreter to execute English instructions. The adopted reference
must not be treated as defining English generally. Keep the current question-
and budget-relative definition of opacity. Near-decomposability remains a
conjectured explanation.

The workshop closes when review of the central note and its tag summary is
complete and the next dependent repairs are handed back to the audit, or the proposal is
rejected with any useful conclusions retained elsewhere. Broader dependent
repairs remain tracked by the audit. This proposal does not authorize an
empirical trial or resolve the vocabulary unification candidate.

## Disposition

| Item | Status | Where |
|---|---|---|
| F1 central note | closed | aef13b709 rebuild, d3a6459b0 relocation, Astra's revision |
| F2 navigation | closed | computational-model head summarizes the two accounts |
| F3 testing advice | closed for the practices note (b4858b39b, a0f274dc7); automated-tests-for-text being edited in another session | |
| F4 scope from form | closed | 7093080cd |
| F5 definitional overreach | closed | 9d91230e1 and the near-decomposability revision |
| F6 partial evaluation | closed | acc843c5d |
| F7 verifiability gradient | closed | 35daecae2 |
| F8 five dependents | closed | fa55d03b0 (progressive constraining), 406e44952 (the other four) |
| Projection term | retired for program refinement | a00f07fa0 definition; sweeps 9d800927d, 6c4fc3ea1, 16c834161; [inventory](./projection-inventory.md) |
| Astra's Tier 1 review | four claim repairs applied | fa55d03b0, d2751437d, 4176fa06b, 4b35dc051 |
| Open | review of the repairs above; workshop closure; the addressability unification candidate stays in the ledger | |

## Proposed main claim

**Prompting can be understood as programming in a precise but opaque
model-defined language, using English as an accessible approximation, or as
executing English specifications through a fallible interpreter. Which
account governs determines what counts as an interpreter error.**

The main explanatory task is to connect the two accounts without switching
the governing reference unnoticed. The coarse/detailed distinction belongs
inside this account: English supplies a candidate behavioral abstraction of
the model-defined language, and can separately supply the requirement against
which that language's behavior is judged.

The practical comparison with traditional programming remains relative to
the inspection question. A prompt may be understandable for one change; a
conventional program may be opaque for another. Formal precision does not
establish affordable inspection.

## Proposed argument: two accounts and their connection

### Programming in the model-defined prompt language

Consider a language whose expressions use English surface forms, but whose
semantics is determined by a specified LLM package. Fix the model, inference
and decoding rules, runtime assumptions, and how conversation context and
other inputs enter execution. The package supplies a precise computational
account, including any permitted variation, which can be formally described.
Under this stipulated reference, writing prompts is programming in that
language. Constructing this account does not imply that every user has adopted
the package as the authority for what their instructions mean.

This language has an unusual practical difficulty: its precise semantics can
be too complex to inspect usefully. English gives the programmer an accessible
approximation. “Translate into French” identifies a task and a place to change
the target language. “Preserve personal names” identifies another meaningful
part. These readings suggest what edits should do without exposing the model
computation that realizes their effects. Their fidelity to the package needs
evidence; English is not an exact specification of this model-defined language.
Empirical probes and learned model-specific conventions can also make the
language usable.

If the coarse description captures the interactions relevant to a question,
it supports local reasoning. When it does not, more detailed understanding or
additional evidence is needed. Opacity concerns whether that answer can be
established at acceptable cost. It does not require every prompt or every
property of a prompt to be obscure, and useful understanding need not expose
individual weight-level computations.

### Executing English through a fallible interpreter

There is another account of the same activity. Treat the English instruction
as the governing specification and the LLM as its fallible interpreter. Now
an output that violates an unambiguous instruction is an interpreter failure.
An instruction may also leave several acceptable readings, in which case an
unwanted choice need not be an interpreter failure. This account retains the
distinction between underspecification and nonconformance. The governing
instruction includes the applicable surrounding rules: scope, precedence and
exceptions can leave the combined requirements unsettled even when each
clause has a clear ordinary use. This is a claim about English instruction
semantics that applies to human interpreters too. Using those instructions to
control execution makes the consequences operational: execution can select
a behavior without the contract having settled which behavior is required.

Suppose the applicable contract requires a successful response to contain
JSON only, and the package wraps that successful response in Markdown. Under
English instruction execution, that is a violation. Under the
model-defined language, if execution followed the adopted package, the wrapper
is behavior that the program permits and that fails the user's requirement.
The practical failure remains; its diagnosis changes with the reference.
Execution can still fail to conform to the package itself, for example if the
deployment runs a different version from the one adopted.

### The connection: English as requirement and approximation

English plays two roles across the accounts. As a requirement language, it
states what the system should do. As an approximate description of the
model-defined language, it suggests what a program will do. The same words
can serve both purposes, but behavioral evidence bears on their predictive
fidelity without deciding what the requirement ought to be.

| Finding | Question and primary home |
|---|---|
| Unsettled requirement | What do the English instructions jointly require? The instruction-composition note examines scope, precedence and exceptions. |
| Interpreter nonconformance | Does execution violate a sufficiently settled applicable instruction, or the separately adopted package reference? Name the reference before assigning the failure. |
| Inadequate prediction of execution | Does the coarse English description capture the package's behavior for the question? The near-decomposition note examines local reasoning and its limits. |

These findings can coexist. An output may defeat a prediction and violate a
settled requirement. An unsettled English requirement can coexist with a
precise model-defined behavior. The distinction determines what must be
clarified or tested; it does not sort every failure into one exclusive class.

The [instruction-composition note](../../theory/clear-instructions-can-compose-into-an-unsettled-contract.md)
belongs primarily to the English-semantics account. Its connection to opacity
is indirect: an unsettled English account can limit our ability to describe
or predict the model-defined language. The
[prompt approximation note](../../theory/english-can-approximate-a-model-defined-prompt-language.md)
primarily concerns English as a behavioral approximation. Neither supporting
note should silently switch those roles.

## How the argument develops

1. **Construct the model-defined prompt language.** Make the package and
   input boundary explicit, and explain in what sense prompting is programming.
   Use [the semantic-reference account](../../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md)
   to distinguish stipulating a language for analysis from adopting it as a
   deployment's governing reference.
2. **Explain how an opaque language is usable.** Develop English as a coarse
   behavioral account, using the translation example from the
   [prompt approximation note](../../theory/english-can-approximate-a-model-defined-prompt-language.md).
   Local meaning survives; the reliability and scope of its predictions are
   further questions. Near-decomposability supplies a candidate explanation
   of manageable interactions, not a premise needed to establish the language.
3. **Introduce English instruction execution as the second account.** Use
   the same prompt and output to show how changing the reference changes the
   diagnosis. Preserve both unambiguous violations and acceptable alternative
   readings. Do not assert that most users hold this account without evidence.
4. **Keep approximation and requirement distinct.** A behavior can refute an
   English-based prediction while also violating an English requirement. The
   model-defined account does not remove that requirement or excuse failure.
   Neither account asserts a literal internal interpret-then-execute pipeline.
5. **Derive practical choices from the diagnosed problem.** Clarify a
   requirement when acceptable behavior is unsettled; probe or refine the
   behavioral account when model effects are unknown; extract a readable
   procedure when its cost and scope justify doing so; enforce a predicate
   through a boundary that actually checks it. Each intervention answers a
   different problem.

## Consequences for the rewrite plan

The reference-model construction becomes the opening argument rather than an
exception introduced after English interpretation. Opacity explains the cost
of programming in that language; the two-level semantic account explains how
useful programming remains possible. Near-decomposability follows as a
candidate mechanism for local reasoning. The addressability unification can
remain unresolved without blocking any of these steps.

The existing English-interpreter argument now has a clear home as the second
account. Retain its useful failure distinctions, including the scoped claim
in [traditional software can bracket executor conformance](../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md).
English-specific discussion is secondary to the general comparison, but it
is necessary when English governs the instruction's correctness.

After the central note and tag summary, repair testing and debugging consumers
first: they must say whether an observation concerns reference conformance,
the fidelity of a behavioral abstraction, or task adequacy. Then repair
scoping, partial-evaluation and extraction arguments. Their conclusions must
follow from the actual checks and interactions, not from the form label alone.

## Distinctions the rewrite must preserve

The [instruction-composition note](../../theory/clear-instructions-can-compose-into-an-unsettled-contract.md)
adds the JSON/exception boundary case. English uncertainty can concern not
only a clause's meaning but also its applicability, precedence and exceptions
when combined with other rules. The JSON-wrapper example above must be read
against the full applicable contract. Under the model-defined account those
interactions have specified computational consequences, but the English-based
description of them may be insufficient. Missing composition rules are a
candidate mechanism, not an established explanation of most failures.

| Question | What settles it |
|---|---|
| What behavior does the operation permit? | The governing reference, if one is adopted; otherwise the applicable interpretation of the instruction |
| Does this execution conform? | Evidence against that reference or instruction |
| Does the permitted behavior meet the requirement? | An assessment against the requirement, separate from reference adoption |
| Can we understand the behavior or edit affordably? | The available descriptions, tools and evidence for the question and budget |
| Can runs vary? | The specified execution conditions, including decoding and environmental inputs |

[Underspecification and execution variation](../../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md)
remain relevant, but neither defines the whole prompting problem. A precise,
deterministic reference can still be opaque or inadequate. Ordinary-language
requirements can still leave several acceptable outcomes, for prompts and
conventional programs alike.

[Codification](../../theory/definitions/codification.md), the move into symbolic
form, must retain both routes: rewriting into a governed language and adopting
a consumer as the reference. Only some cases provide a cheaper, more readable
implementation. Do not reinstate a universal prompt-to-code ladder of
precision, reliability and cost.

## What to keep, move or replace from the incumbent

- Keep checkpoints, testing, progressive extraction and versioning as useful
  practices, but justify each against a named question rather than the old
  two-phenomena thesis. Detailed cost claims belong in their existing companion
  notes unless needed for this argument.
- Keep natural-language ambiguity as a scoped case. Move the extended
  English/Tarski discussion out of the main line by linking the existing
  semantics notes. No impossibility theorem about English is needed here.
- Replace “the model picks a valid program” with an account that admits
  instruction violations as well as reasonable interpretations.
- Replace categorical claims that LLM adherence is probabilistic, that code
  automatically enforces desired properties, and that extraction escapes
  requirement testing.
- Update the [computational-model head](../../tags/computational-model-README.md)
  with the adopted argument. Decide the final title and any relocation after
  the thesis is settled; the current title should not constrain the rewrite.

## Tests of the proposed argument

These are conceptual acceptance cases, not reported model trials:

- An ordinary English prompt whose model is not adopted as its semantic
  reference: language interpretation still matters.
- The identical prompt under an adopted deterministic package: the inspection
  problem survives even though the reference fixes execution.
- The same JSON-wrapper response assessed under both accounts: the diagnosis
  changes, while the unmet user requirement remains.
- An adopted stochastic package: permitted variation is compatible with
  precise semantics.
- A model upgrade: under the model-defined account it changes the language's
  reference; under English instruction execution it changes the implementation
  being assessed against the instruction. Neither account licenses assuming
  unchanged behavior.
- A prompt whose coarse account predicts a local edit adequately: the
  argument must allow local transparency.
- A prompt edit that changes interacting output properties: the account must
  identify which abstraction failed without assuming all prompt meaning is
  lost.
- Readable local code and opaque conventional code: the distinction follows
  the inspection question rather than the implementation label.
- An authoritative model-based check that accepts an unsuitable result:
  reference conformance must remain separate from task adequacy.

## Open choices before promotion

Use “model-defined prompt language” as a scoped construction in the note.
“Prompt” already names a consumption path in the KB; introducing this language
must not turn every prompt into symbolic content regardless of reference
adoption. A separate registered definition is warranted only if downstream use
needs it. Use “English surface forms” rather than claiming an exact English
grammar: prompts can also contain fragments, code and other languages.

Do not claim that English resemblance is the only source of usability, or
that most users treat LLMs as buggy English interpreters. The argument needs
neither a universal usability claim nor a population claim about users.

The claim that prompt abstractions support less reliable compositional
reasoning than conventional programming needs a specified comparison and
evidence if asserted empirically. The conceptual account alone establishes
that formal precision does not entail affordable inspection; it does not
measure the difference between systems.

The [unification ledger](../../reference/vocabulary-unification-ledger.md#addressability-and-near-decomposability)
records the operator's suggestion that addressability and near-decomposability
may be the same underlying organization used for different goals. The rewrite
can use meaningful parts and manageable interactions without deciding whether
the terms should merge. It must not silently reduce addressability to editable
strings or assume independent effects from separate clauses.

The existing [ideal-interpreter workshop](../ideal-interpreter/README.md)
explores another semantics framing. This proposal needs no ideal interpreter:
its detailed reference is an actual adopted package. Any later integration
must preserve that distinction.
