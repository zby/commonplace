---
description: "Dijkstra's EWD 472 makes non-deterministic choice a construct with weakest-precondition semantics; anchors permitted-variation and demonic-correctness claims in the KB."
source: https://www.cs.utexas.edu/users/EWD/transcriptions/EWD04xx/EWD472.html
captured: "2026-11-04"
capture: trafilatura
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618
ingested: "2026-11-04"
occasion: "how nondeterministic choice is made a language construct with a weakest-precondition semantics, so that a program can denote a closed set of permitted outcomes rather than one; retain the definition of the guarded command set, the alternative and repetitive constructs' nondeterminacy, and the Law of the Excluded Miracle."
type: types/ingest-report.md
domains: [guarded-commands, weakest-precondition, nondeterminism, program-derivation]
---

# Ingest: Guarded commands, non-determinacy and formal derivation of programs (EWD 472)

## Classification

This is a theoretical computer-science paper, published in *Communications of the ACM* 18(8), 1975. It defines language constructs and a formal semantics, states theorems without proof and derives example programs. It reports no empirical evaluation. The capture is an automatic transcription of the EWD manuscript, not the typeset article. Author: Edsger W. Dijkstra, then a Burroughs Research Fellow; this paper is the originating source for guarded commands and weakest-precondition (wp) semantics.

## Summary

Dijkstra defines a guarded command as a boolean guard followed by a statement list. A guarded command set is an unordered set of such commands separated by "▯"; its textual order is semantically irrelevant. Two statements are built from a set. The alternative construct `if ... fi` aborts when no guard is true and otherwise executes an arbitrary guarded list whose guard is true. The repetitive construct `do ... od` repeats such selections and terminates properly exactly when no guard is true. So a program may leave the activity, and sometimes the final state, undetermined by the initial state. For the maximum-finding example the paper states: "Only permissible final states are possible and each permissible final state is possible". Meaning is given by the predicate transformer `wp(S, R)`: the weakest precondition guaranteeing that S terminates properly in a state satisfying R. The wp of `if` requires that some guard holds and that every eligible branch establishes R, so correctness quantifies over all permitted selections. The first stated property, `wp(S, F) = F`, is the condition later called the Law of the Excluded Miracle; this paper lists it but does not use that name. Theorems for `if` and `do` turn a chosen invariant and variant function into a loop-correctness rule. The paper presents this as a calculus for deriving programs. Alternative constructs can be derived routinely, while loops require the "invention" of an invariant and a variant. Non-determinacy also avoids choosing between deterministic variants, such as two versions of Euclid's algorithm, on timing assumptions the problem does not supply.

## Contribution assessment (our opinion)

The problem is how to give programs a semantics that supports deriving them from their specifications rather than verifying them afterward. Background knowledge, not this capture, suggests the paper's contribution was foundational. It tightened Hoare's partial-correctness preconditions into necessary and sufficient total-correctness preconditions, and it made bounded non-determinism a first-class, specifiable language feature rather than an implementation defect. The demonstrated value inside the paper is limited to small worked derivations (max, sorting four values, gcd) and theorems stated without proof. Its later significance, including *A Discipline of Programming*, refinement calculi and CSP-style guarded choice, is historical impact, not evidence the paper itself establishes. The central idea is hard to vary. Demanding that wp hold for every eligible branch is what lets an unordered choice coexist with guaranteed correctness. Weakening that quantifier would turn the guarantee into a probable one.

## Quotes

> The basic building block for both of them is the so-called “guarded command”, a statement list prefixed by a boolean expression: only when this boolean expression is initially true, is the statement list eligible for execution.
> --- `kb/sources/.snapshots/ewd472-guarded-commands.md` @ `sha256:a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618` — §1 Introduction: guarded command

> Note that a guarded command by itself is **not** a statement: it is a component of a guarded command set from which statements can be constructed. If the guarded command set consists of more than one guarded command, they are mutually separated by the separator “▯” ; our text is then an arbitrarily ordered enumeration of an unordered set, i.e. the order in which the guarded commands of a set appear in our text is semantically irrelevant.
> --- `kb/sources/.snapshots/ewd472-guarded-commands.md` @ `sha256:a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618` — §2: guarded command set; textual order irrelevant

> If in the initial state none of the guards is true, the program will abort, otherwise an arbitrary guarded list with a true guard will be selected for execution.
> --- `kb/sources/.snapshots/ewd472-guarded-commands.md` @ `sha256:a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618` — §2: selection rule of if ... fi

> An example —illustrating the non-determinacy in a very modest fashion— would be the program that for fixed x and y assigns to m the maximum value of x and y :
> --- `kb/sources/.snapshots/ewd472-guarded-commands.md` @ `sha256:a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618` — §2: the if-fi max example, where both guards hold when x = y

> allow non-deterministic program components for which at least the activity evoked, but possibly even the final state, is not necessarily uniquely determined by the initial state.
> --- `kb/sources/.snapshots/ewd472-guarded-commands.md` @ `sha256:a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618` — Abstract

> To conclude this section we give a program where not only the computation but also the final state is not necessarily uniquely determined.
> --- `kb/sources/.snapshots/ewd472-guarded-commands.md` @ `sha256:a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618` — §2: introduces the maximum-index program

> 0 ≤ k < n **and** (∀i: 0 ≤ i < n: f(k) ≥ f(i))
> --- `kb/sources/.snapshots/ewd472-guarded-commands.md` @ `sha256:a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618` — §2: the condition k must eventually satisfy

> Only permissible final states are possible and each permissible final state is possible .
> --- `kb/sources/.snapshots/ewd472-guarded-commands.md` @ `sha256:a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618` — §2: closing sentence on the maximum-index program

> F denotes, by definition, the condition that is satisfied by no state at all.
> --- `kb/sources/.snapshots/ewd472-guarded-commands.md` @ `sha256:a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618` — §3.1: meaning of F

> has, by definition, the following properties . 1) For any S, we have for all states
> --- `kb/sources/.snapshots/ewd472-guarded-commands.md` @ `sha256:a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618` — §3.1: first wp property; formula follows in a table row

> wp(S, F) = F
> --- `kb/sources/.snapshots/ewd472-guarded-commands.md` @ `sha256:a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618` — §3.1: property 1; the capture does not name it the Law of the Excluded Miracle

> More specifically: we shall use the notation “wp(S, R)”, where S denotes a statement list and R some condition on the state of the system, to denote the weakest pre-condition for the initial state of the system such that activation of S is guaranteed to lead to a properly terminating activity leaving the system in a final state satisfying the post-condition R .
> --- `kb/sources/.snapshots/ewd472-guarded-commands.md` @ `sha256:a6a25b25c97c641aef61283653706ab5428d142470d041ce0c64ac4617841618` — section 3.1, weakest precondition includes proper termination

## Connections Found

For the occasion, the source is the formal anchor for a specification that denotes a closed set of permitted outcomes. It is the KB's first source on classical formal program semantics. Its main role is to supply a precise instance for claims that currently state permitted variation abstractly. [Symbolic form holds consumers to a semantic reference](../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md) says a reference "may leave permitted variation". EWD 472 is evidence for that claim: a fully formal semantics whose meaning is a permitted outcome set. [Implementations do not establish shared semantics](../theory/implementations-do-not-establish-shared-semantics.md) says nondeterminism can be represented as permitted transitions. The paper is evidence for that claim too: the semantics is authored independently of any implementation, guard order is irrelevant, and concurrent guard evaluation is admitted.

On the design side, the source compares with [An author should fix what the executor can't determine, not what it will](../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) on leaving bounded choices open. The guards delimit the eligible alternatives, and Dijkstra leaves later determinization "entirely to the circumstances". It compares with [Commitment, not derivation, creates new ground truth](../theory/commitment-not-derivation-creates-new-ground-truth.md) on deferring unentailed choices. The symmetric Euclid program omits a choice that only timing assumptions could justify. On what a calculus mechanizes, it compares with [Causal and proof obligations are two formal routes to assessing explanatory-reach](../theory/formal-systems-assess-explanatory-reach-through-causal-and-proof.md). The calculus checks an invariant once someone has chosen it but does not supply one. The [bounded-context orchestration model](../theory/bounded-context-orchestration-model.md) has a `do`-shaped loop that ends when nothing is selectable. The two differ on selection: wp correctness must hold for every choice, while the model treats `select` as a policy designers compare.

Among sources, [Agent Behavioral Contracts](./agent-behavioral-contracts-formal-specification-runtime.ingest.md) is the contrasting pole on how a contract handles non-determinism. wp is demonic: every permitted selection must succeed. ABC defines statistical compliance. [ToolGate](./toolgate-contract-grounded-and-verified-tool-execution-for-llms.ingest.md) prunes candidates with Hoare-style preconditions and replaces arbitrary selection with learned ranking. Its guarantee therefore rests on postcondition checks, not on all branches being correct. [Seemann's essay](./is-ai-the-next-layer-of-abstraction.ingest.md) requires a translation that is both well defined and deterministic. EWD 472, by Dijkstra, whom Seemann cites, shows a defined semantics can be non-deterministic, so definedness is the requirement doing the work. [Programming practices for prompts need evidence matched to the question](../theory/programming-practices-for-prompts-need-question-specific-evidence.md) compares on separating conformance from requirement adequacy. A guarded program can conform exactly to its semantics while leaving the outcome open within a declared set, which is a precise, non-statistical kind of variation.

## Extractable Value

1. **A permitted-outcome-set semantics, stated precisely.** A guarded command set is an unordered set of alternatives. `if` selects any branch with a true guard and aborts if none holds. `do` repeats until no guard holds. wp requires every eligible branch to establish the postcondition. This gives the KB a formal referent for "permitted variation": the program denotes a closed set of acceptable outcomes, and conformance means landing in that set, not reproducing one output. High reach. It explains why precise semantics and non-unique outcomes are compatible. [quick-win]
2. **Demonic quantification as the guarantee mechanism.** Correctness survives arbitrary selection only because the wp of `if` quantifies over all true guards. This contrasts with ToolGate's learned ranking and ABC's statistical compliance. It names what a design gives up when it replaces "every permitted choice is correct" with "the chosen one is probably correct". [quick-win]
3. **The Law of the Excluded Miracle as a well-formedness condition.** `wp(S, F) = F`: no statement can guarantee to establish an impossible postcondition. With monotonicity and the conjunction and disjunction properties, it replaces Hoare's inference rules. Retaining it requires attribution care. The paper states the property but not the later name. [just-a-reference]
4. **Non-determinism as a deferred commitment.** The symmetric Euclid program avoids a version A/B choice that "can only be justified by making assumptions" about timing, and the non-deterministic program is "a helpful steppingstone" toward later determinization. This is a classical case for the KB's rule of leaving bounded, all-acceptable choices open. [quick-win]
5. **Routine versus invention in a formal calculus.** Alternative constructs derive almost mechanically. Loops need an invented invariant and variant function, which the calculus then checks. This is a classical instance of formalization relocating judgment upstream rather than removing it. [just-a-reference]
6. **Termination and deadlock are the same state.** "All guards false" means termination in a sequential program and deadlock in an operating system. The method transferred from process synchronization to sequential programs. This matters for orchestration loops that end when nothing is selectable. Whether the empty state is success or failure depends on the context. [experiment]

## Limitations (our opinion)

The paper argues by construction and worked example. It states its theorems without proof, and its examples are small numeric programs, so it does not show the calculus scaling to large or interactive systems. Its non-determinism is bounded and finite-choice. Its semantics only covers initial states where termination is guaranteed ("for other initial states we don't care"). So it does not address unbounded choice, fairness, divergence or probabilistic outcomes, which are the cases closest to LLM execution. Transferring it to prompts and agent workflows is an analogy at the level of specification shape. The paper says nothing about natural-language references, where the permitted set is itself unsettled. The capture also has a fidelity gap. Although marked `full-source`, the automatic transcription drops several formula lines: the BB definition, part of the DO definition, the consequents of Theorems 1–4 and steps of the gcd derivation. A claim about those exact formulas needs the typeset CACM article (snapshot required) or a cleaner transcription, not this capture alone. The name "Law of the Excluded Miracle" does not appear in the capture, so any quote retained for it can support only the property `wp(S, F) = F`.

## Recommended Next Action

Cite this ingest as the formal instance in [Symbolic form holds consumers to a semantic reference](../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md), at its statement that a reference "may leave permitted variation", grounded in retained quotes of the guarded command set definition, the `if`/`do` selection rules and the permitted-final-states sentence.

---

Relevant Notes:

- [EWD 472 transcription](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD04xx/EWD472.html) — derived-from: the captured primary source
