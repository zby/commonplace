---
description: "Morgan's specification statement [pre, post] gives specifications a weakest-precondition meaning as programs; refinement, monotonic composition and miracles bear on formal permitted variation."
source: https://www.cs.ox.ac.uk/files/3391/PRG70.pdf
captured: "2026-11-04"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 14ace2bad0042b6766bf07099c05017a730f93aa8f17fb6a06fdacb4f670d9c7
ingested: "2026-11-04"
occasion: "Morgan, \"The specification statement\", ACM TOPLAS 10(3):403–419, 1988, reprinted as the first paper in Oxford PRG-70 \"On the Refinement Calculus\" (October 1988); ingest only that paper, not the other papers in the monograph. Occasion: how a specification written as precondition and postcondition is itself a program denoting the set of permitted outcomes, and how code refines it by choosing a subset; retain the definition of the specification statement and its weakest-precondition semantics, the refinement ordering, and the remark on miracles."
type: types/ingest-report.md
domains: [refinement-calculus, specification-statement, weakest-precondition, miracles]
tags: [constraining]
---

# Ingest: The specification statement (Morgan 1988, first paper of PRG-70)

## Classification

This is a theoretical computer-science paper. It extends a programming language with a new construct, gives the construct a formal semantics, and proves properties of it. It also gives small worked derivations. It has no empirical evaluation. The analysis covers only the first paper of the Oxford PRG-70 monograph *On the Refinement Calculus*. That paper is a reprint of Morgan's article in ACM TOPLAS 10(3), July 1988. The later papers in the monograph are out of scope here.
Author: Carroll Morgan of the Oxford Programming Research Group, a principal author of the refinement calculus. The paper was refereed at TOPLAS. It credits Back and Morris with closely related, independent work.

## Summary

Morgan adds the *specification statement* `w: [pre, post]` to Dijkstra's guarded-command language. It means "assuming an initial state satisfying pre, change only variables in w to establish post". It is given a weakest-precondition semantics: `[pre, post]<R> ≙ pre ∧ (∀w · post ⇒ R)`, with 0-subscripted variables naming initial values. A specification therefore is a program, though possibly not an executable one, and it sits in the program text where its implementation will go. Refinement `P ⊑ Q` means "every specification satisfied by P is satisfied by Q also". Formally, `P<R> ⇒ Q<R>` for every postcondition R. Theorem 3 shows that `pre ⇒ P<post>` holds exactly when `[pre, post] ⊑ P`. Satisfying a specification and refining it are therefore the same relation. Theorem 2 states that the sequencing, if and do constructors are monotonic under ⊑. This is what lets a fragment be refined in place. Refinement can reduce nondeterminism, and it can also make a program terminate where its predecessor might abort. The worked example refines a two-branch `if` into a deterministic program that always terminates. The extension admits *miracles*, such as `[true, false]`, which violate Dijkstra's Law of the Excluded Miracle (`P<false> = false`). A miracle refines every program but has no feasible refinement. Theorem 4 gives the feasibility test `pre ⇒ (∃w · post)`. Miracles can arise from mistaken design steps. Naked guarded commands are miracles when their guard is false. The paper suggests deliberate uses: case splits, backtracking, and loop-invariant proof rules. It notes that the extended `if P fi` is not monotonic, which limits its use in program development.

## Contribution assessment (our opinion)

The problem matters: top-down program development needed a single semantic framework in which unfinished fragments have exact meanings. Before that, specifications sat in a separate "where" clause beside the program. The central contribution is to make the specification a first-class program whose meaning is a predicate transformer. Everything else follows: refinement as one relation between any two programs, Theorem 3's equivalence of satisfaction and refinement, monotonicity, and miracles. This conjecture has survived. The refinement calculus became a standard method for formal program derivation, and Morgan's later textbook builds on this construct. That claim rests on my background knowledge, not on this capture. Originality is qualified by the paper itself: Back had already embedded single-predicate specifications using weakest preconditions, and Morris independently reached the same extension. The distinct additions here appear to be the predicate-pair form, which makes miracles expressible, and a deliberate, practically oriented use of them. The paper's own evidence is proof plus toy derivations (array search, array sum, a module interface). It shows that the framework is coherent and usable on small examples. It does not show that derivation scales or what it costs, which is a limitation of scope rather than a defect in the central result.

## Quotes

> The
> extension does this by providing one semantic framework Cor speci­
> fications and programa alike - developments begin with a program
> (a sinSle specification statement), and end with a program (in the
> executable language).
> --- `kb/sources/.snapshots/morgan-the-specification-statement.md` @ `sha256:14ace2bad0042b6766bf07099c05017a730f93aa8f17fb6a06fdacb4f670d9c7` — abstract; "Cor" and "programa" are OCR for "for" and "programs"

> by giving a weakest precondition semantics
> to [pre,post], we make this intermediate stage (1) into a program - albeit
> an abstract one.
> --- `kb/sources/.snapshots/morgan-the-specification-statement.md` @ `sha256:14ace2bad0042b6766bf07099c05017a730f93aa8f17fb6a06fdacb4f670d9c7` — introduction, on the statement [pre, post] written where its implementation will go

> The simple specification statement [pre, post} comprises two predicates over
> the program variables v. Informally, it means "assuming an initial state
> satisfying pre, establish a final state satisfying post.
> --- `kb/sources/.snapshots/morgan-the-specification-statement.md` @ `sha256:14ace2bad0042b6766bf07099c05017a730f93aa8f17fb6a06fdacb4f670d9c7` — section 2.1, informal meaning preceding Definition 1; the Definition 1 formula itself is OCR-garbled and not retained

> The statement %JY: [true, % = y] can set y to:z, % to y, or hoth:z and y to
> some third value.
> --- `kb/sources/.snapshots/morgan-the-specification-statement.md` @ `sha256:14ace2bad0042b6766bf07099c05017a730f93aa8f17fb6a06fdacb4f670d9c7` — section 2.2, example of the choice of final state a specification permits; "%JY" and "%" are OCR for "x, y" and "x"

> For programs P and Q, we give P ~ Q the informal meaning: "every
> specification satiefied by P is satisfied by Q also." This means that Q is an
> acceptable replacement for P.
> --- `kb/sources/.snapshots/morgan-the-specification-statement.md` @ `sha256:14ace2bad0042b6766bf07099c05017a730f93aa8f17fb6a06fdacb4f670d9c7` — section 3, informal meaning preceding Definition 6; "~" is OCR for the refinement symbol; the Definition 6 formula is OCR-garbled and not retained

> We now state the well-known but crucial fact that the program con­
> structors are monotonic with respect to ~; only this ensures that refining
> a fragment (say P above) "in placet" in some larger program, refines that
> larger program overall.
> --- `kb/sources/.snapshots/morgan-the-specification-statement.md` @ `sha256:14ace2bad0042b6766bf07099c05017a730f93aa8f17fb6a06fdacb4f670d9c7` — section 3, sentence introducing Theorem 2; the theorem's formula is OCR-garbled and not retained

> A surprising con.sequence of the exteoeioo is the appearance of mir­
> at:le8: program fragments that do not satisfy Dijketra's Law of the
> Ezduded Mirad~.
> --- `kb/sources/.snapshots/morgan-the-specification-statement.md` @ `sha256:14ace2bad0042b6766bf07099c05017a730f93aa8f17fb6a06fdacb4f670d9c7` — abstract; OCR-garbled spelling of "extension", "miracles", "Dijkstra's" and "Excluded Miracle"

> An unexpected consequence of our extension is the introduction of ab­
> stract programs that do not obey Dijkstra's Law of tAt: t:zduded miracle.
> These correspond to specifications that have no concrete solution, just as
> negative numbers stand for insoluble equations in elementary arithmetic
> --- `kb/sources/.snapshots/morgan-the-specification-statement.md` @ `sha256:14ace2bad0042b6766bf07099c05017a730f93aa8f17fb6a06fdacb4f670d9c7` — introduction; "tAt: t:zduded miracle" is OCR for "the Excluded Miracle"

## Connections Found

For the occasion, the source is a **formal anchor**. It gives an exact model of a specification as a program with permitted variation, and of code as a narrowing of that variation. One correction to the occasion's framing matters. The paper's semantics is a predicate transformer, not a set of outcomes. Read relationally, `[pre, post]` permits, from any pre-state, every final state satisfying post. Refinement then does two things: it may shrink the set of permitted outcomes where the predecessor terminates, and it may add termination where the predecessor could abort. "Choosing a subset" is therefore only half of refinement. Miracles are the edge case where the permitted set is empty and termination is still promised.

The source is a formal counterpart of [Symbolic form holds consumers to a semantic reference](../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md). The shared axis is conformance to a reference that declares permitted variation. In the calculus, weakest-precondition semantics is the reference, refinement is conformance, and a deterministic implementation conforms to a nondeterministic specification. It also gives [constraining](../theory/definitions/constraining.md) a precise instance. Each refinement step narrows permitted behaviors while keeping every guarantee of its predecessor. The definition does not state the monotonicity condition, under which narrowing a part narrows the whole.

The strongest connection beyond the occasion is evidence for [Near-decomposability may make local inspection affordable](../theory/near-decomposability-may-make-local-inspection-affordable.md). That note separates locating a repair from establishing that the repair preserves required invariants. Theorem 2 states a sufficient formal condition for the second: the replacement refines the fragment's specification, and every enclosing constructor is monotonic. The non-monotonic `if ... fi` shows that the condition can fail even inside a formal language. This also bears on the note's open question about certificate checking without near-decomposition. Specification interfaces can replace interaction summaries, but only for callers that rely on the specification alone.

The calculus compares with [Clear instructions can compose into an unsettled contract](../theory/clear-instructions-can-compose-into-an-unsettled-contract.md) on whether a combination of requirements is settled. In the calculus, every combined specification has a defined meaning, and an unsatisfiable one is a detectable miracle. That separates settled-but-infeasible from unsettled. It compares with [Underspecification and indeterminism complicate programming for prompts in distinct ways](../theory/underspecification-and-indeterminism-complicate-programming-for.md) on where multiple valid outcomes live. Here they are a first-class object inside a formal language. Refinement removes them step by step. They are not peculiar to natural language. It compares with [Specification strategy should follow where understanding lives](../theory/specification-strategy-should-follow-where-understanding-lives.md) as the formal extreme of spec-first: the specification is placed where the code will go, and each step is checked. Miracles from mistaken tactics are a precise version of a specification step that later proves unworkable.

Among sources, it compares with [Ingest: Is AI the next layer of abstraction?](./is-ai-the-next-layer-of-abstraction.ingest.md) on what makes moving between abstraction layers trustworthy. The calculus relates layers by a correctness-preserving relation, not a deterministic translation, so defined meaning does not require determinism. It compares with [Ingest: Program synthesis (Gulwani, Polozov, Singh 2017)](./program-synthesis-gulwani-polozov-singh-2017.ingest.md) on how a program is obtained from stated intent. The calculus uses human-directed derivation by laws, while synthesis searches a program space.

## Extractable Value

1. **Satisfaction is refinement of a specification statement** -- Theorem 3 makes "P meets (pre, post)" identical to `[pre, post] ⊑ P`. A requirement and its implementations live in one ordered space, so "this artifact meets the spec" and "this artifact is a valid narrowing of that one" are the same check. This is the cleanest formal model the KB has for the permitted-variation vocabulary in the symbolic-form and constraining notes. Bound: it holds for a total-correctness predicate-transformer semantics over a fixed state space. [quick-win]
2. **Refinement has two directions, not one** -- the refinement ordering both reduces nondeterminism and widens the region where termination is guaranteed, as the paper's two-branch `if` example shows. The occasion's "code refines by choosing a subset" holds only where the specification's precondition holds. Outside it, the specification promises nothing, and code may do anything. This distinction between permitted variation and excluded guarantees maps onto the symbolic-form note's separation of the two. [quick-win]
3. **Miracles and the feasibility test** -- `[true, false]` refines every program and is refined only by miracles, so a development that reaches one is doomed. Feasibility is the checkable condition `pre ⇒ (∃w · post)`. Miracles can enter from mistaken steps, and the paper argues this simplifies the theory: soundness is delegated to unimplementable programs, so fewer applicability conditions are needed. For the KB, this is a formal case of a requirement that is settled but unsatisfiable. It can sharpen the scope section of the clear-instructions note. [quick-win]
4. **Monotonicity is the condition for safe local replacement** -- Theorem 2, with the non-monotonic `if ... fi` as a counterexample, gives a precise sufficient condition for when refining a part refines the whole. This is high-reach for the parked question about which properties survive composition. Bound: the guarantee covers only properties expressed through the part's specification. A caller that depends on more than the specification is not protected. [deep-dive]
5. **Specifications as module interfaces** -- the database-module example puts a specification statement in the definition module, and the Algol-60 copy rule gives calls their meaning. This is an early, precise form of "the interface is the contract". It is useful as background for contract-grounded tool execution, but the claim is not new to the KB. [just-a-reference]

## Limitations (our opinion)

The paper supports its claims by proof and toy derivations only. It does not show that derivation by refinement scales to realistic programs, how much specification effort it costs, or how often practitioners reach miracles. The program-synthesis ingest records the general cost that formal specifications can be as hard to write as the program. The results are internal to a total-correctness weakest-precondition semantics over a fixed vector of program variables. The paper itself notes that Z deliberately avoids a fixed state, so carrying the results into settings without a declared state space, such as natural-language instructions or agent contexts, needs an explicit mapping. The paper does not give one. Applying "permitted variation" from this source to LLM outputs is an analogy until someone states what the reference semantics and the refinement relation are in that setting. Monotonicity is proved only for `;`, `if` and `do`. The paper does not say which constructors from other formalisms, or which composition operations in agent systems, preserve it. The capture is OCR of a scanned PDF and contains symbol errors in formulas. Formula details should be checked against the published TOPLAS text before exact retention. The snapshot's `full-source` scope covers the whole monograph, but this analysis read only the first paper. Claims about the later papers' laws, procedures, data refinement or program conjunction are not established here.

## Recommended Next Action

Retain, through `cp-skill-ground`, the occasion's core passages from the first paper: the abstract's single-framework claim, Definition 1 with its informal meaning, the refinement ordering (Definition 6 with "every specification satisfied by P is satisfied by Q also"), Theorem 2's monotonicity sentence, and the miracle definition with its feasibility consequence. Check each formula against the TOPLAS text because the OCR is unreliable.
