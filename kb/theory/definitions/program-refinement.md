---
description: "Definition — program refinement is the relation under which one artifact's permitted behaviors lie inside another's; a checked narrowing is a refinement step, an executor's unchecked choice only a candidate."
type: types/definition.md
tags: [learning-theory, constraining]
---

# Program refinement

Under an applicable interpretation, an instruction, prompt or formal specification permits a set of behaviors, its **permitted set**. Given the interpretations of two artifacts P and Q, Q is a **program refinement** of P when every behavior Q permits is one P permits: Q narrows P's set without leaving it. This behavior-set reading must preserve P's guarantees, including any required termination; comparing successful outputs alone is insufficient. The judgment is relative to those interpretations. A formal specification fixes its interpretation through its reference. An English instruction may leave membership disputed, and where it does the refinement judgment stays unsettled. A **refinement step** is a narrowing that is committed in a retained artifact and checked against P. An executor's output is a **candidate refinement** until it is checked. The term is a compound. The bare word "refinement" stays ordinary English in this KB.

The KB needs the term for two jobs. [Constraining](./constraining.md) narrows an artifact's interpretation space, and program refinement is the formal reading of that narrowing. The [two accounts of prompting](../prompting-changes-failure-diagnosis-with-the-semantic-reference.md) need a name for the relation between what an instruction permits and what an executor produces, one that does not assert the executor landed inside the set.

## The relation and its sources

The formal anchor is [Morgan's](../../sources/morgan-the-specification-statement.ingest.md) specification statement. A specification written as a precondition and a postcondition is read, verbatim, as "assuming an initial state satisfying pre, establish a final state satisfying post", and it is itself a program, "albeit an abstract one". Refinement orders such programs: Q refines P when Q satisfies every specification that P satisfies, which Morgan states as "This means that Q is an acceptable replacement for P." His semantics concerns guarantees expressed through weakest preconditions, not merely sets of successful outputs. His section 3 example both removes a nondeterministic choice and guarantees termination in an additional initial state: "But Q differs from P in that Q will always terminate, even when z = 7."

The behavior-set account here is a scoped reading of that guarantee-preserving relation. It must not discard termination obligations. Morgan also admits specifications with no concrete solution, called miracles: a specification can have a precise meaning without an implementation. Applying this formal relation to English instructions is this KB's extension, conditional on the applicable interpretations; the paper does not settle those interpretations.

In the formal cases discussed here, the specification's rules settle membership, whether the permitted set is finite or infinite. Permitting several alternatives is different from leaving their permissibility unsettled. [Dijkstra's](../../sources/ewd472-guarded-commands.ingest.md) guarded commands make the choice a construct: when several guards hold, verbatim, "an arbitrary guarded list with a true guard will be selected for execution", and for the resulting program "Only permissible final states are possible and each permissible final state is possible". Dijkstra defines the weakest precondition by requiring execution to lead, verbatim, to "a properly terminating activity leaving the system in a final state satisfying the post-condition R". The guarantee covers every selectable branch, the reading later called demonic: correctness requires every permitted choice to meet the postcondition and termination obligation. Under that reading an instruction is only as good as the worst behavior it permits.

Programming-language standards distinguish several ways of leaving behavior open. [N1570](../../sources/wg14-n1570-behavior-definitions.ingest.md) separates unspecified behavior, a closed set with no documentation duty, from implementation-defined behavior, verbatim, "unspecified behavior where each implementation documents how the choice is made", and from undefined behavior, which imposes no requirements. Adopting a pinned model package as an operation's reference is a different move: it establishes the governing reference rather than selecting within latitude already supplied by a standard. Adoption does not establish that the package's behavior lies within what the English requirement permits.

## Candidate and checked

A refinement step is checked. An executor's output is not. Under the English account of prompting, the instruction has a permitted set and the executor produces one behavior. That behavior is a **candidate refinement** of the instruction: it may lie inside the set, where it is a selection the caller may still reject on adequacy, or outside it, where it is a violation, as [out-of-spec output](../out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) states. Nothing in the output marks which. Calling an unchecked output a refinement would assert the conformance that still has to be established. Calling it a candidate does not say what conformance would mean. That is fixed by the applicable interpretation of the instruction, which may itself be unsettled, as the [central note](../prompting-changes-failure-diagnosis-with-the-semantic-reference.md) sets out for disputed readings.

Compilation by a trusted tool is a refinement step: the tool is held to a reference and its conformance is corroborated by independent tests outside the run, within their tested scope. Generated code is a candidate until checked against the applicable requirement, which is why [progressive constraining](../progressive-constraining-commits-only-after-patterns-stabilize.md) commits a pattern only after observed runs support it. [Codification](./codification.md) by rewriting is a refinement step when the rewritten artifact is checked against the rule it replaces. Codification by adopting a package fixes the permitted set without checking the English requirement against it.

## Monotonicity

Morgan's Theorem 2 proves that refining a fragment in place refines the enclosing program for the constructors covered by its structural-induction proof: sequencing, the guarded alternative and the loop. His later extended guardless `if P fi` is explicitly not monotonic. Thus even a precisely defined composition operation need not preserve refinement. Monotonicity cannot be assumed for instruction composition. When two instructions leave their scope and precedence open, as in [unsettled composition](../clear-instructions-can-compose-into-an-unsettled-contract.md), there may be no agreed combined permitted set against which to judge refinement. A judgment can instead be made under an explicitly named interpretation. Settling composition supplies the basis for that comparison; establishing that the composition operation preserves refinement requires a further argument.

## Scope

Use the term when one artifact's permitted set is claimed to lie inside another's, and say whether the claim is checked. A constraining step is a program-refinement step when the narrowed permitted set lies inside the old one and that inclusion is checked; ranking readings alone does not establish a narrowing. A conformant compilation and a validated code extraction are refinement steps. Settling a composition rule establishes the standard against which refinement of the parts is judged; it is itself a refinement step only when the settled permitted set lies inside the one before. A model's output, a generated program and a sampled interpretation are candidate refinements until checked.

The relation is stated for a named consumer and reference, as constraining is, and under a named interpretation where English leaves one open. The same prompt permits different sets under an ordinary reading and under an adopted package.

## Exclusions

- **Iterative improvement.** Prompt refinement, note refinement and in-place refinement in this KB mean editing toward a better artifact. They may narrow or widen a permitted set. The bare word keeps that ordinary sense.
- **Theory refinement.** The EITHER and FORTE line that [addressable theory](./addressable-theory.md) cites repairs a rule set against cases. It is revision, not a narrowing within a permitted set.
- **Adequacy.** A refinement of a wrong specification is a wrong program. Refinement preserves what the specification requires and says nothing about whether the requirement was the right one, the separation the [semantic-reference account](../symbolic-form-holds-consumers-to-a-semantic-reference.md) keeps.
- **Projection.** Earlier notes called the executor's collapse of a permitted set to one behavior a projection. The word is ordinary language here, fitting a silent and unrecorded choice, and carries no technical properties. The [collision ledger](../../reference/vocabulary-collision-ledger.md) records the decision.

## Misuse Cases

- Calling a model's output a refinement of its prompt. It is a candidate until checked.
- Writing "refinement" bare for the technical relation. In the library the bare word mostly names iterative improvement.
- Treating monotonicity as a free guarantee for prompts. Settling instruction composition does not by itself establish that the composition operation preserves refinement.
- Treating adoption of a package as evidence that it refines the English requirement. Adoption fixes the governing reference; whether the package's behavior satisfies the English requirement needs a separate check.
- Judging refinement where the applicable interpretation is disputed, as if membership were settled. Name the interpretation, or report the judgment as unsettled.

---

Relevant Notes:

- [Constraining](./constraining.md) — defined-in: the narrowing of interpretation space that program refinement reads formally
- [Codification](./codification.md) — defined-in: the two routes into symbolic form, only one of which is a checked refinement step
- [Addressable theory](./addressable-theory.md) — contrasts: theory refinement in the EITHER and FORTE sense is revision, not narrowing
- [Prompting changes failure diagnosis with the semantic reference](../prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — extends: the English account, where the executor's output is a candidate refinement of the instruction
- [Out-of-spec output is a failure of the interpreter, not the spec](../out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — contrasts: an output outside the permitted set is a violation
- [Progressive constraining commits only after patterns stabilize](../progressive-constraining-commits-only-after-patterns-stabilize.md) — extends: when a candidate becomes a checked refinement step
- [Clear instructions can compose into an unsettled contract](../clear-instructions-can-compose-into-an-unsettled-contract.md) — extends: unsettled composition can leave no agreed combined permitted set against which to judge refinement
- [Symbolic form holds consumers to a semantic reference](../symbolic-form-holds-consumers-to-a-semantic-reference.md) — grounds: conformance to a reference is separate from adequacy to the requirement
- [Morgan, The specification statement](../../sources/morgan-the-specification-statement.ingest.md) — evidenced-by: bounds the behavior-set reading through termination guarantees, miracles and constructor-specific monotonicity
- [Dijkstra, Guarded commands](../../sources/ewd472-guarded-commands.ingest.md) — evidenced-by: specified nondeterministic choice with weakest-precondition guarantees of proper termination and acceptable final states
- [WG14 N1570 behavior definitions](../../sources/wg14-n1570-behavior-definitions.ingest.md) — evidenced-by: unspecified, implementation-defined and undefined behavior as grades of an open choice
