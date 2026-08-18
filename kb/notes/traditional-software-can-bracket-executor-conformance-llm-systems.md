---
description: "Wrongness is a relation to a norm, never intrinsic to a computation; classical stacks bracket the executor-conformance norm so every failure resolves to the spec, and LLM systems cannot, which is what generates the three-source deviation taxonomy"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [llm-reliability, computational-model]
---

# Traditional software can bracket executor conformance; LLM systems cannot

Wrongness is never intrinsic to a computation. An executor — a CPU, a compiler, an LLM forward pass — always computes exactly its own function, and nothing internal to that computation can be in error. Wrongness is a relation between the behavior produced and a norm held outside the computation. Which norm you hold the behavior to decides what "wrong" names.

Any `specification → executor` pipeline is governed by two such norms, not one.

- **Intent against meaning.** The author's intent `I` against what the specification publicly means — its valid set `V`. A mismatch here is what a programmer calls "a bug in my code": the artifact says something other than what the author meant. The failure belongs to the author.
- **Meaning against behavior.** The specification's public meaning against what the executor actually did. A mismatch here is executor non-conformance — the compiler-bug case.

The second norm is the one that gets forgotten, so state it carefully. A compiler whose output diverges from the language standard is buggy even though the compiler binary executed its own instructions flawlessly. The attribution is to a *role* — conforming interpreter of this language — not to the physics of the machine. Nothing about the substrate is doing the work here: the same analysis applies unchanged to a contractor working from a brief, who also executes their own function faultlessly while failing the role.

## Classical practice brackets the second norm

Classical software engineering does not deny the second norm; it brackets it. Compiler and CPU conformance is reliable enough that in practice every wrong output resolves to "my code doesn't mean what I intended". The bracket is what licenses the everyday inference *wrong output ⇒ my spec is wrong*, and it collapses error analysis to one question with one culprit.

A second simplification rides alongside it. Code aims at a unique semantics: once language, implementation, flags, and target are fixed, `V` is a singleton per input, and any divergence counts as a bug, a portability limit, or explicitly unspecified behavior. So there is no residual question of *which* admissible behavior you got.

Together the two simplifications produce the strong form programmers actually say out loud: you cannot call the output wrong if the program is correct. That statement is not a truth about computation. It is the two brackets talking — conformance assumed, plurality assumed away.

## Neither simplification survives the move to LLM systems

The prompt's public meaning is fixed by shared linguistic-competence norms. These are weaker than a language standard and contestable at the margin, since [natural language has no conforming-interpreter standard to appeal to and no attainable formal semantics](./agentic-systems-interpret-underspecified-instructions.md) — but they are not vacuous. No competent reading of "output JSON only" admits a markdown wrapper.

An LLM in an agentic pipeline is deployed *as* an interpreter of that language, so it occupies exactly the compiler's role and inherits the second norm. What it does not inherit is the reliability that made the norm ignorable. Its conformance to the words' meaning is probabilistic and materially unreliable: [output the spec rules out is produced anyway](./out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md), across constraint violation, hallucination, fully specified bookkeeping, and framing sensitivity. The compiler-bug case is the dominant regime rather than the negligible one.

The other bracket goes too. `V` is plural, because the specification language admits many valid readings of one instruction.

So error analysis for an LLM system irreducibly needs three questions where classical practice needed one:

1. Does the spec mean what I intended? — underspecification, a property of the specification.
2. Did the interpreter honor what the spec means? — interpreter failure, a property of the interpreter.
3. Which sample did I draw? — indeterminism, a property of the sampling process.

[The three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md) is therefore not a new phenomenon list assembled from LLM symptoms. It is the classical analysis with both brackets removed. That is also why its questions cannot be merged or traded against each other: they were never one question, only jointly invisible.

## Keeping the category coherent

The distinction survives only under strict bookkeeping about which norm a failure violates. Interpreter failure is deviation from `V` — the spec's public meaning under a competent reading — never deviation from `I`. An unwanted output that the words admit is underspecification, and it is the author's problem in exactly the sense a programmer means when they say they didn't understand their own program.

Relaxing this makes the category absorb everything: any disappointing output could be called the interpreter's fault, because the author always wanted something more specific than they wrote. The public-meaning boundary is what stops "interpreter failure" from degenerating into "I am unhappy with this output", and it is what makes the remedies separable at all.

## The practical consequence: verification is structural

Because executor conformance can no longer be assumed, it has to be re-established per output by machinery outside the executor — validation, [oracles](./oracle-strength-spectrum.md), voting, [decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md). This is not defensive engineering culture or distrust of a young technology. It replaces a guarantee that traditional stacks receive from the platform for free, which is why verification is a structural component of an LLM system rather than an afterthought bolted on for safety.

The standard architectural remedies read the same way once the bracket is visible: they are attempts to re-purchase it. [Constraining](./definitions/constraining.md) — narrowing what an artifact can be read to mean, up to committing it to code — moves work onto a substrate whose conformance is assumable again. [Scheduler-LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) does the same for bookkeeping, relocating exact state transitions to a symbolic executor. The gain is not that the code is smarter than the model. It is that on that substrate, question 2 goes back to being answerable by assumption.

## Scope

The classical bracket is empirical and contingent, not a theorem. It leaks at undefined behavior, floating-point and concurrency edges, and occasionally at real compiler bugs. What matters is the rate: low enough that the default inference stays sound, and rare enough that when it does break, engineers notice — precisely because their habitual reasoning stops working. The claim is about which regime dominates, not about a categorical difference in kind between substrates.

The public-meaning boundary is a triage rule, not a decision procedure. Genuinely borderline attributions between underspecification and interpreter failure remain contestable, and the competent-reader test settles them only well enough to route a remedy.

Where an LLM is not deployed as an interpreter of an instruction — open-ended generation with no operative spec — the second norm has little content, and the analysis reduces to the first.

## Open Questions

- Interpreter failure is a rate, so the bracket could in principle return. If conformance reliability rises far enough with model generation, practice would re-collapse toward two questions. The threshold is unknown, and it is worth noting that it would be a change in engineering economics, not in the structure of the analysis.
- Partial brackets are unexplored. Schema-constrained decoding and hard output validators make conformance assumable for *some* properties of an output while leaving the rest probabilistic; whether that composes into a usable per-property bracket, or just relocates the question, is untested here.

---

Relevant Notes:

- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — grounds: why natural language supports no conforming-interpreter standard and no attainable formal semantics, which is what makes the second norm weak but non-vacuous
- [out-of-spec output is a failure of the interpreter, not the spec](./out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — grounds: the component claim for interpreter failure, with the worked catalogue of outputs falling outside `V`
- [LLM output deviation requires three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md) — extends: supplies the reason the diagnosis has exactly these three questions — it is the classical two-norm analysis with both brackets removed
- [constraining](./definitions/constraining.md) — defined-in: the narrowing operation this note reads as re-purchasing the conformance bracket
- [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — mechanism: the architectural form of re-purchasing the bracket, moving exact bookkeeping to a substrate whose conformance can be assumed
- [oracle strength spectrum](./oracle-strength-spectrum.md) — mechanism: the graded machinery that re-establishes conformance per output when it cannot be assumed
- [error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — mechanism: the conditions under which per-output conformance checking actually pays
