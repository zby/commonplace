---
description: "Separates formal models of implemented consumers from agreement and conformance claims, including why finite tests and formalized LLMs do not settle a language's semantics."
type: types/note.md
traits: [title-as-claim]
tags: [learning-theory, artifact-analysis]
---

# Implementations do not establish shared semantics

An implementation together with a sufficiently specified machine model supplies a formal account of its execution. It does not establish that another implementation has the same semantics, or that either conforms to an independently intended language. Formalizability therefore cannot by itself distinguish symbolic from natural-language [representational form](./definitions/representational-form.md), the classification of how content is encoded and consumed.

The constructions below are arguments and illustrative cases, not reported experiments or claims about universal agreement among programming-language practitioners.

## An implementation can supply the formal account

Take a compiler's complete implementation and a formal specification of the machine executing it. Include the runtime, relevant initial state, and environmental interactions needed to describe the behavior under discussion. If the claim concerns execution of compiled programs, include the target machine as well, not just the machine running the compiler.

Under these assumptions, the implementation and machine model determine a formal account of execution. The account can retain internal states or describe only selected observable behavior. It need not terminate on every input. Nondeterminism can be represented as permitted transitions rather than hidden by an assumption of one output per input.

This is a construction, not an inference from passing tests. The implementation's bugs are included in the behavior being described. A faithful formal model of a buggy compiler is still a formal model.

Implementation plus machine model supplies a candidate formal account without requiring a separately authored, compact language semantics. It does not witness correctness against an independently intended language.

## Agreement on tests does not establish shared semantics

Consider a toy language whose programs compute an integer expression. Its intended rule for addition is ordinary integer addition. Compiler A implements that rule except for one untested expression, where it returns zero. Compiler B has a different exception at another untested expression. Both pass a test suite that exercises neither exception.

Each compiler has formally describable behavior. Each behavior satisfies the tested expectations. Yet they disagree outside the tests and neither fully implements the intended rule.

The example separates three facts:

- A formal account exists for each implementation under its machine model.
- Those accounts agree on the tested observations.
- Those accounts need not agree on other observations.

If at least one modeled implementation passes the tests, there is already a formal account consistent with those tests: the account of that implementation. Several passing implementations do not turn that existence claim into a stronger result. They provide opportunities to expose disagreements that one implementation would not expose alone.

Thus incompatible compilers do not show that no formal semantics exists. They show that the compilers do not realize the same behavior where they differ. Calling their differences bugs additionally invokes a rule they were supposed to implement.

## Shared semantics is a stronger, scoped claim

Two implementations need not have identical internal states, algorithms, or execution traces to implement the same language. The comparison must name which observations count and what variation the language permits.

For a deterministic operation whose result is fixed by the rules, a disagreement on that result defeats the claim that both implementations conform. For a rule that explicitly allows several outcomes, different outcomes can both conform. Merely defining a relation broad enough to include everything both implementations do would make coexistence trivial; it would not establish conformance to the rules being tested.

Independent implementations held to the same reference can corroborate a conformance conjecture through tests that could reveal a violation. They may share a bug, have different untested bugs, or agree with an inadequate test oracle. Passing tests does not prove conformance outside the tested cases.

There are two possible conjectures here:

1. The implementations agree on all observations where the rules require agreement.
2. Each implementation conforms to the intended rules, including rules allowing variation.

Neither is the bare conjecture that some formal account of each implementation exists. Agreement between implementations also does not by itself establish that the intended rules are correct for the user's task.

## Formalizability is different from choosing a reference

Whether a standard, an implementation, or a mathematical specification supplies the reference does not decide whether an implementation can be formally modeled. The construction above applies whichever reference is chosen.

Reference choice matters when asking whether an implementation is wrong. An implementation taken as the reference defines behavior that another implementation is expected to preserve within the specified scope. An implementation tested against an independent specification can fail it. In either case, its actual computation remains formally describable under the machine assumptions.

The authority question concerns conformance, not the possibility of formal description.

## Formalizability alone cannot classify the artifact

The same construction applies to the computation of a fixed LLM implementation. Supply its weights, inference code, numerical operations, decoding procedure, and relevant state and inputs. Model sampling or environmental variation explicitly where needed. A sufficiently specified machine model can then describe the computation.

It does not follow that this account supplies a formal semantics of the natural-language prompt. It supplies a model of how this particular system responds to that prompt. A different model may respond differently without thereby violating the instruction. Conversely, it can violate an unambiguous instruction; natural-language interpretation can still be wrong.

So “its consumer can be formally modeled” cannot be the distinguishing condition for symbolic content. That would classify prompts as symbolic simply because computers consume them. Nor does requiring an unwritten formal account help: writing the account down should not change an artifact's representational form.

The distinction that remains is what the rules describe: the consumer's computation, or the interpretation committed to for the artifact. Code and a prompt can both participate in formally describable computations while playing different roles in those computations. Adopting a consumer as the reference for a scoped operation is a further act, not a consequence of formalizing it.

## Scope

Implementation source alone is insufficient when its behavior depends on machine or environmental details left unspecified. A formal machine model is not a proof that physical hardware always conforms to it. The construction concerns execution under the supplied model; fidelity to a physical deployment is a further claim.

This note removes formalizability as a classifier. The membership criterion for symbolic form and the move called [codification](./definitions/codification.md) require the further distinction between describing a consumer and holding consumers to a reference.

---

Relevant Notes:

- [Representational form](./definitions/representational-form.md) — defined-in: the classification cannot be settled merely by formalizing the consumer
- [Codification](./definitions/codification.md) — defined-in: committing an operation requires more than repeatability or agreement on tests
