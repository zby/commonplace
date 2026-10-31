# An implementation supplies a formal model, not proof of shared semantics

Working draft, 2026-10-31. Reconstructs the operator–assistant discussion behind the [workshop commission](./README.md). The constructions below are arguments and illustrative cases, not reported experiments or claims about universal agreement among programming-language practitioners.

## Question

Can Commonplace explain [codification](../../theory/definitions/codification.md) and symbolic [representational form](../../theory/definitions/representational-form.md) without its special use of “unique operational semantics”?

The proposed simplification is that symbolic artifacts have rules admitting a formal semantics, whether or not anyone has explicitly written it down. That is more familiar wording, but it conceals several different claims. We need to separate them before changing the definitions.

## 1. An implementation can supply the formal account

Take a compiler's complete implementation and a formal specification of the machine executing it. Include the runtime, relevant initial state, and environmental interactions needed to describe the behavior under discussion. If the claim concerns execution of compiled programs, include the target machine as well, not just the machine running the compiler.

Under these assumptions, the implementation and machine model determine a formal account of execution. The account can retain internal states or describe only selected observable behavior. It need not terminate on every input. Nondeterminism can be represented as permitted transitions rather than hidden by an assumption of one output per input.

This is a construction, not an inference from passing tests. The implementation's bugs are included in the behavior being described. A faithful formal model of a buggy compiler is still a formal model.

There are two limits. First, implementation source alone is insufficient when its behavior depends on machine or environmental details left unspecified. Second, a formal machine model is not a proof that physical hardware always conforms to it. The construction concerns execution under the supplied model; fidelity to a physical deployment is a further claim.

The operator's “witness” intuition works at this level: implementation plus machine model supplies a candidate formal account without requiring a separately authored, compact language semantics. It does not witness correctness against an independently intended language.

## 2. Agreement on tests does not establish shared semantics

Consider a toy language whose programs compute an integer expression. Its intended rule for addition is ordinary integer addition. Compiler A implements that rule except for one untested expression, where it returns zero. Compiler B has a different exception at another untested expression. Both pass a test suite that exercises neither exception.

Each compiler has formally describable behavior. Each behavior satisfies the tested expectations. Yet they disagree outside the tests and neither fully implements the intended rule.

The example separates three facts:

- A formal account exists for each implementation under its machine model.
- Those accounts agree on the tested observations.
- Those accounts need not agree on other observations.

If at least one modeled implementation passes the tests, there is already a formal account consistent with those tests: the account of that implementation. Several passing implementations do not turn that existence claim into a stronger result. They provide opportunities to expose disagreements that one implementation would not expose alone.

Thus incompatible compilers do not show that no formal semantics exists. They show that the compilers do not realize the same behavior where they differ. Calling their differences bugs additionally invokes a rule they were supposed to implement.

## 3. Shared semantics is a stronger, scoped claim

Two implementations need not have identical internal states, algorithms, or execution traces to implement the same language. The comparison must name which observations count and what variation the language permits.

For a deterministic operation whose result is fixed by the rules, a disagreement on that result defeats the claim that both implementations conform. For a rule that explicitly allows several outcomes, different outcomes can both conform. Merely defining a relation broad enough to include everything both implementations do would make coexistence trivial; it would not establish conformance to the rules being tested.

Independent implementations held to the same reference can corroborate a conformance conjecture through tests that could reveal a violation. They may share a bug, have different untested bugs, or agree with an inadequate test oracle. Passing tests does not prove conformance outside the tested cases.

There are two possible conjectures here:

1. The implementations agree on all observations where the rules require agreement.
2. Each implementation conforms to the intended rules, including rules allowing variation.

Neither is the bare conjecture that some formal account of each implementation exists. Agreement between implementations also does not by itself establish that the intended rules are correct for the user's task.

## 4. Formalizability is different from choosing a reference

Whether a standard, an implementation, or a mathematical specification supplies the reference does not decide whether an implementation can be formally modeled. The construction in section 1 applies whichever reference is chosen.

Reference choice matters when asking whether an implementation is wrong. An implementation taken as the reference defines behavior that another implementation is expected to preserve within the specified scope. An implementation tested against an independent specification can fail it. In either case, its actual computation remains formally describable under the machine assumptions.

This keeps the authority question in its proper place: it concerns conformance, not the possibility of formal description.

## 5. Why formalizability alone cannot classify the artifact

The same construction applies to the computation of a fixed LLM implementation. Supply its weights, inference code, numerical operations, decoding procedure, and relevant state and inputs. Model sampling or environmental variation explicitly where needed. A sufficiently specified machine model can then describe the computation.

It does not follow that this account supplies a formal semantics of the natural-language prompt. It supplies a model of how this particular system responds to that prompt. A different model may respond differently without thereby violating the instruction. Conversely, it can violate an unambiguous instruction; natural-language interpretation is not exemption from correctness.

So “its consumer can be formally modeled” cannot be the distinguishing condition for symbolic content. That would classify prompts as symbolic simply because computers consume them. Nor does requiring an unwritten formal account help: writing the account down should not change an artifact's representational form.

The candidate distinction is what the rules describe: the consumer's computation, or the interpretation committed to for the artifact. Code and a prompt can both participate in formally describable computations while playing different roles in those computations.

That distinction still needs a boundary test. In particular, a frozen prompt–model combination might be deliberately adopted as the reference for a narrow operation. The computation would remain formally describable. What, exactly, has become symbolic in that case: the packaged operation, the prompt, neither, or different parts under different consumption paths? This draft does not settle that question by asserting that the model is merely interpreting.

## 6. What the reductions permit us to remove

| Tempting reduction | Result |
|---|---|
| Symbolic means we do not know the formal semantics. | Reject: an explicit formal account must remain a qualifying case. “Not necessarily specified” is different from “unknown.” |
| Several agreeing executors witness the existence of a formal model. | Separate: implementation plus machine model supplies an account; tests support claims of agreement or conformance. |
| Different compiler bugs mean there is no formal semantics. | Reject as an existence claim: each modeled compiler still supplies an account, and the intended semantics can exist even when neither compiler conforms. |
| Agreement on tests establishes one shared semantics. | Reject: the toy compilers agree on the tests and differ elsewhere. |
| Shared semantics requires identical outputs in every case. | Reject where the reference explicitly permits variation; state the comparison scope. |
| A formally describable consumer makes its inputs symbolic. | Reject as a classifier: it includes LLM-consumed natural language. |
| Choosing an authoritative reference answers formalizability. | Reject: reference choice determines which behavior counts as a violation, not whether actual behavior has a formal account. |

These reductions remove reasons for maintaining a separate technical sense of “operational semantics.” They do not yet establish a complete replacement definition of symbolic form.

## Candidate wording and remaining work

The passages below are the initial formulation. [Candidate definitions using formal semantics](./candidate-definitions.md) holds the later wording and records why returning to shared semantics preserves the progress of these reductions.

A provisional formulation for discussion is:

> A symbolic artifact has committed rules for permitted behavior that admit a formal description. That description need not have been written down. Tests assess whether consumers conform to the rules; they do not establish formalizability merely by showing agreement.

For [codification](../../theory/definitions/codification.md), the corresponding candidate is:

> Codification commits a rule or operation stated in natural language to a symbolic artifact whose fixed rules determine what behavior is permitted.

The phrase “committed rules” must do more than rename the problem. Before promotion, test the candidate against a schema enum, a route table, a prose instruction executed by a model, and a frozen prompt–model package deliberately used as a reference. Preserve the difference between a precisely implemented check and the requirement it is meant to test, as explained in [fixed artifacts split into exact specs and proxy theories](../../theory/exact-implementation-does-not-validate-a-requirement.md).

The proposed vocabulary change remains open. The reductions above can be retained even if the candidate definition fails the boundary cases. No impossibility claim about formal semantics for natural language is needed to establish them.
