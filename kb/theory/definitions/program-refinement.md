---
description: "Definition — program refinement is the relation under which one artifact's permitted behaviors lie inside another's; a checked narrowing is a refinement step, an executor's unchecked choice only a candidate."
type: types/definition.md
tags: [learning-theory, constraining]
---

# Program refinement

An instruction, prompt or formal specification permits a set of behaviors. An artifact Q is a **program refinement** of an artifact P when every behavior Q permits is one P permits: Q narrows P's set without leaving it. A **refinement step** is a narrowing that is committed in a retained artifact and checked against P. The term is a compound; the bare word "refinement" stays ordinary English in this KB.

The KB needs the term for two jobs. [Constraining](./constraining.md) narrows an artifact's interpretation space, and program refinement is the formal reading of that narrowing. The [two accounts of prompting](../prompting-changes-failure-diagnosis-with-the-semantic-reference.md) need a name for the relation between what an instruction permits and what an executor produces, one that does not assert the executor landed inside the set.

## The relation and its source

The definition follows [Morgan's](../../sources/morgan-the-specification-statement.ingest.md) specification statement. A specification written as a precondition and a postcondition is read, verbatim, as "assuming an initial state satisfying pre, establish a final state satisfying post", and it is itself a program, "albeit an abstract one". Refinement orders such programs: Q refines P when every specification P satisfies, Q satisfies too, which Morgan glosses as "This means that Q is an acceptable replacement for P." Composition is monotonic, so refining a fragment in place refines the enclosing program. Morgan calls a specification with no concrete solution a miracle: it has a meaning in the calculus and no implementation.

The permitted set is a closed list, not an absence of rules. [Dijkstra's](../../sources/ewd472-guarded-commands.ingest.md) guarded commands make the choice a construct: when several guards hold, verbatim, "an arbitrary guarded list with a true guard will be selected for execution", and for the resulting program "Only permissible final states are possible and each permissible final state is possible". The weakest-precondition semantics requires every selectable branch to establish the postcondition, the reading later called demonic: the program is correct only if every permitted outcome is acceptable. Under that reading an instruction is only as good as the worst behavior it permits.

Programming-language standards grade the same openness. [N1570](../../sources/wg14-n1570-behavior-definitions.ingest.md) separates unspecified behavior, a closed set with no documentation duty, from implementation-defined behavior, verbatim, "unspecified behavior where each implementation documents how the choice is made", and from undefined behavior, which imposes no requirements. Adopting a pinned model package as the reference for an operation is nearest to the implementation-defined grade: the pin fixes which choice is made, though it documents the choice only by exhibiting it, not by stating how it is made.

## Candidate and checked

A refinement step is checked. An executor's output is not. Under the English account of prompting, the instruction permits a set and the executor produces one behavior. That behavior is a **candidate refinement** of the instruction: it may lie inside the set, where it is a selection the caller may still reject on adequacy, or outside it, where it is a violation, as [out-of-spec output](../out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) states. Nothing in the output marks which. Calling an unchecked output a refinement would assert the conformance that still has to be established.

Compilation by a trusted tool is a refinement step: the tool is held to a reference and its conformance is corroborated by independent tests outside the run, within their tested scope. Generated code is a candidate until checked against the applicable requirement, which is why [progressive constraining](../progressive-constraining-commits-only-after-patterns-stabilize.md) commits a pattern only after observed runs support it. [Codification](./codification.md) by rewriting is a refinement step when the rewritten artifact is checked against the rule it replaces. Codification by adopting a package fixes the permitted set without checking the English requirement against it.

Monotonicity holds only where composition is settled. When two instructions leave their scope and precedence open, as in [unsettled composition](../clear-instructions-can-compose-into-an-unsettled-contract.md), the combined permitted set is not defined, so no refinement of the combination can be checked. Settling the composition rule is the step that makes refinement of the parts meaningful for the whole.

## Scope

Use the term when one artifact's permitted behaviors are claimed to lie inside another's, and say whether the claim is checked. A constraining step, a conformant compilation, a validated code extraction and a settled composition rule are refinement steps. A model's output, a generated program and a sampled interpretation are candidate refinements until checked.

The relation is stated for a named consumer and reference, as constraining is. The same prompt permits different sets under an ordinary reading and under an adopted package.

## Exclusions

- **Iterative improvement.** Prompt refinement, note refinement and in-place refinement in this KB mean editing toward a better artifact. They need not narrow a permitted set and may widen it. The bare word keeps that ordinary sense.
- **Theory refinement.** The EITHER and FORTE line that [addressable theory](./addressable-theory.md) cites repairs a rule set against cases. It is revision, not a narrowing within a permitted set.
- **Adequacy.** A refinement of a wrong specification is a wrong program. Refinement preserves what the specification requires and says nothing about whether the requirement was the right one, the separation the [semantic-reference account](../symbolic-form-holds-consumers-to-a-semantic-reference.md) keeps.
- **Projection.** Earlier notes called the executor's collapse of a permitted set to one outcome a projection. The word is ordinary language here, apt for a silent and unrecorded choice, and carries no technical properties; the [collision ledger](../../reference/vocabulary-collision-ledger.md) records the decision.

## Misuse Cases

- Calling a model's output a refinement of its prompt. It is a candidate until checked.
- Writing "refinement" bare for the technical relation. In the library the bare word mostly names iterative improvement.
- Treating monotonicity as a free guarantee for prompts. It holds where the composition of instructions is settled, and the composition note shows when it is not.
- Reading an adopted package's documented choice as a refinement of the English requirement. It fixes the set; adequacy to the requirement is a separate check.

---

Relevant Notes:

- [Constraining](./constraining.md) — defined-in: the narrowing of interpretation space that program refinement reads formally
- [Codification](./codification.md) — defined-in: the two routes into symbolic form, only one of which is a checked refinement step
- [Addressable theory](./addressable-theory.md) — contrasts: theory refinement in the EITHER and FORTE sense is revision, not narrowing
- [Prompting changes failure diagnosis with the semantic reference](../prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — extends: the English account, where the executor's output is a candidate refinement of the instruction
- [Out-of-spec output is a failure of the interpreter, not the spec](../out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — contrasts: an output outside the permitted set is a violation, not a refinement
- [Progressive constraining commits only after patterns stabilize](../progressive-constraining-commits-only-after-patterns-stabilize.md) — extends: when a candidate becomes a checked refinement step
- [Clear instructions can compose into an unsettled contract](../clear-instructions-can-compose-into-an-unsettled-contract.md) — extends: where monotonicity fails because the combined permitted set is not defined
- [Symbolic form holds consumers to a semantic reference](../symbolic-form-holds-consumers-to-a-semantic-reference.md) — grounds: conformance to a reference is separate from adequacy to the requirement
- [Morgan, The specification statement](../../sources/morgan-the-specification-statement.ingest.md) — evidenced-by: a specification as a program, the refinement ordering and monotonic composition
- [Dijkstra, Guarded commands](../../sources/ewd472-guarded-commands.ingest.md) — evidenced-by: nondeterministic choice as a construct whose permitted final states form a closed set
- [WG14 N1570 behavior definitions](../../sources/wg14-n1570-behavior-definitions.ingest.md) — evidenced-by: unspecified, implementation-defined and undefined behavior as grades of an open choice
