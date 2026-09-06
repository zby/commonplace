---
description: "A theory builder must construct and run programs because the consequences that discriminate a theory cannot be enumerated before the theory exists and individual checks can exceed any interpretation budget"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems, learning-theory]
---

# Unbounded consequence-checking makes theory builders write software

A system that manipulates theories must test them, and testing runs through consequences: state what should hold if the theory is right, then check whether it does. The [discovery lifecycle](./definitions/discovery-lifecycle.md) separates these as its consequence-derivation and test phases. Two properties of the checking step, taken together, decide what machinery the system needs.

**The consequences that discriminate a theory cannot be enumerated in advance.** Which consequence is worth checking depends on the theory, on the rival explanations in play, and on the evidence already gathered — none of which is fixed when the system is built. A checker written before the theory exists is not the checker that theory turns out to need.

**A single check can exceed what interpretation carries.** Some consequences are settled by reading one document. Others quantify over a corpus, require exact bookkeeping across many items, or must be recomputed whenever the evidence moves. For those, a bounded model call is the wrong instrument: it cannot hold the inputs, its result is not exact, and re-deriving the check at each use pays the derivation again with variance added.

Neither property alone forces much. Together they leave one option. The system cannot pre-supply the checks, by the first, and cannot discharge them by interpretation, by the second. So it must *construct* checking procedures against theories it did not have in advance and *execute them exactly* over inputs larger than a context window. That is producing and running software.

## A general harness satisfies the claim rather than defeating it

The obvious rival is a sufficiently general fixed harness: give the system strong retrieval, traversal, and comparison tools plus a code interpreter, and no theory-specific machinery change is ever needed.

That rival concedes the point. A harness whose general capability is *write a program and run it* meets the requirement by producing software at every check. The argument never predicts that some particular tool will be missing; it identifies which capacity must be present, and program construction is that capacity. A fixed library of checkers, however large, is what the first property rules out.

## From producing software to evolving it

Producing programs is weaker than being a [software house](./definitions/software-house.md), which asks for persistent responsibility for software as it develops. The bridge is recurrence, and it is economic rather than necessary.

Checks recur. A theory is re-tested as evidence accumulates, a revised theory inherits most of its predecessor's consequences, and different theories over the same corpus share traversal, indexing, and comparison. Where a check will be re-run, discarding its program and rebuilding it pays construction repeatedly and gives up the ability to notice that a consequence which held last month now fails, since [ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md). Retention is then the cheaper policy — and a retained checking program must be repaired when the corpus, schema, or theory moves under it. At that point the builder carries continuity of responsibility for software it keeps changing, which is what the definition asks.

The step is defeasible in a way the earlier ones are not: a builder whose checks never recur would produce software without evolving any.

## What the programs do not settle

The programs check consequences, not theories. Whether a generalization is worth holding — its explanatory-reach, its standing against rivals — is not what a checker decides, and [automated synthesis is missing good oracles](./automated-synthesis-is-missing-good-oracles.md) for exactly that judgment. The division is the one [code complements the weight–prompt pair with independently executed symbolic operations](./code-complements-weight-prompt-with-symbolic-operations.md) draws: proposing a consequence and interpreting a failure stay model-mediated, while a derived check, once specified, is where exact execution pays.

So the claim is narrow about what scale buys. Computation does not adjudicate theories. It says that the step between a theory and the evidence bearing on it is an open-ended computational demand, and a builder that cannot meet it cannot test what it holds.

## The domain-novelty route is weaker

A second argument reaches the same conclusion from demand novelty. A builder working across domains not fixed in advance will meet material its software cannot represent, retrieve, schedule, or govern: a new source kind needing a snapshot path, a new relation needing a schema and validator, a larger corpus needing a different index. Either a person repeatedly supplies those changes, and so occupies an internal production role, or the builder supplies them itself.

That route rests on a premise it does not establish — that unanticipated demands keep arriving — and the general fixed harness above refutes it rather than conceding to it. Its conclusion also follows close to analytically from the software-house definition once the premise is granted. The consequence-checking route needs no premise about novelty: it binds inside a single settled domain, because it is the theory, not the domain, that generates the unbounded demand.

## Scope

- The argument assumes the builder tests its theories against evidence. A system that authors and retains theories without exposing them to consequences has no checking demand and needs none of this.
- The first property concerns the checking procedure, not the existence of general tools. Reusable traversal, indexing, and comparison machinery covers many checks; what is ruled out is a fixed set covering all of them.
- Not every consequence requires scale. The argument needs only that some do and that which ones cannot be known before the theory exists.
- The retention step is economic. It predicts that checking programs are worth keeping where checks recur, not that every builder must retain them.
- Nothing here establishes that a builder can perform these operations without a human, only which operations the complete system must contain. Where they sit relative to the producer's boundary is a separate question.

## Open Questions

- What share of consequence-checks in a working knowledge base actually exceeds a bounded interpretation budget? The argument's practical weight turns on this and is unmeasured here.
- Does the recurrence premise survive theory revision, or do revised theories more often invalidate their predecessors' checks than inherit them?
- Is there a class of theory whose discriminating consequences are enumerable in advance, and if so, what distinguishes it?

---

Relevant Notes:

- [Software house](./definitions/software-house.md) — defined-in: supplies the persistent-responsibility boundary the retention step reaches
- [Discovery lifecycle](./definitions/discovery-lifecycle.md) — defined-in: supplies the consequence-derivation and test phases the checking demand arises in
- [Code complements the weight–prompt pair with independently executed symbolic operations](./code-complements-weight-prompt-with-symbolic-operations.md) — grounds: separates model-mediated interpretation from runtime-assigned exact execution
- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: why exact bookkeeping over many items belongs in symbolic execution rather than repeated interpretation
- [Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — grounds: what discarding a checking program costs beyond its reconstruction
- [A fixed-model house must retain missing procedures for theory use](./a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md) — extends: works out where a missing theory-use operation must be carried once model parameters are pinned
- [Automated synthesis is missing good oracles](./automated-synthesis-is-missing-good-oracles.md) — contrasts: the theory-quality judgment that consequence-checking does not supply
- [Broad software demands create pressure for agentic factory development](./broad-software-demands-create-pressure-for-agentic-factory-development.md) — contrasts: reaches a machinery-construction conclusion from demand breadth, the weaker route this note sets aside
