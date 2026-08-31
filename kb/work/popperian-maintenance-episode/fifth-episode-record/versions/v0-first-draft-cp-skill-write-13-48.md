---
description: "Re-reads Naur's program theory as application judgment: the irreducibility argument defeats rule-carrying text, while locating the capacity in human minds alone was a 1985 substrate default rather than a derived step"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, context-engineering]
---

# Irreducibility to rules bounds text alone, not text plus an interpreter

An argument that some capacity "cannot be reduced to any limited set of criteria or rules" refutes one thing: that a finite text can *decide* the cases by itself. It does not touch a system in which retained text supplies premises and a separate interpreter, competent over the relevant world, decides the case. The two targets are different. Text-as-decider must anticipate the cases; text-as-input to a judging interpreter need only carry what the interpreter cannot supply on its own.

The claim matters because irreducibility arguments are routinely read as arguments about where a capacity can *live* — in minds and not in artifacts. That reading needs an extra premise: that no non-human interpreter is available to pair with the artifact. The premise is often true, and when it is true it is usually invisible, because a default with an empty alternative set does not look like a premise at all.

## Naur's thesis has an argued half and an assumed half

Peter Naur's *Programming as Theory Building* is the clearest case, and the one this note works through. Naur argues that programming builds a theory held by programmers, and names three capabilities of the holder: mapping between world affairs and program text, justifying why each part is what it is, and incorporating a novel modification demand by perceiving similarity on the world side.

The third capability carries the argument. Naur writes that the required kind of similarity "only makes sense to the agent who has knowledge of the world, that is to the programmer, and cannot be reduced to any limited set of criteria or rules". Read as an argument, this establishes that program theory is an **application-judgment capacity** and not a body of propositions: what the holder has is the ability to decide a case that no enumerated criterion settles. Its counterfactual character points the same way — Naur observes that simplicity and good structure characterize a program text relative to alternative texts that "exist only as possibilities in the programmer's understanding". A capacity of that shape cannot be discharged by a rule set, and a text that must decide unaided is a rule set.

The move from there to *therefore the theory lives only in people's minds* is a separate step, and in the passage where Naur takes it the two clauses come apart:

> the decision that a part of the world is relevant can only be made by someone who understands the whole world. This understanding must be contributed by the programmer.

The first clause states the requirement: world-understanding. The second identifies who meets it. Nothing in the first clause selects a human bearer; it selects any bearer that understands the world. In 1985 the identification needed no defence, because the set of candidate world-knowing interpreters that could sit inside a software system was empty. The negative half of the thesis — not just *text alone cannot carry this*, but *only a person can hold it* — is therefore a report on the available substrates, not a conclusion the irreducibility argument produces.

That diagnosis leaves the argued half intact. Retained text still does not decide novel modification demands, and a knowledge base that expected it to would be making the mistake Naur identified.

## What a world-knowing interpreter changes, and what it does not

Once a substrate exists that interprets natural language and brings general world knowledge to bear, the empty candidate set is no longer empty, and the division of labour becomes a design question rather than a boundary fact. The conjecture is that an LLM reading retained artifacts can hold the capacity as a composite: the interpreter supplies the case-by-case similarity judgment, and the text supplies the premises the judgment cannot regenerate — which relevance decisions were made, what the intended scope was, which alternatives lost and why. This is the same composite that [theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) requires, and the retention side is governed by the recovery test in [design rationale must preserve decision premises its interpreter cannot regenerate](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md). What this note adds is why Naur's own argument does not block the move.

Naur's three capabilities split along that line rather than staying together. Justification is largely premise-shaped: the reason a part is what it is can be written down, and once written it is available to any competent reader. Similarity perception on a new demand is judgment-shaped: it must be exercised per case, on material the author never saw. Mapping sits between them, since the mapping's fixed points are recordable while extending it to an unrecorded corner of the world is a fresh judgment. So the thesis that program theory resists externalization is really a thesis about one of its parts, and the parts have different substrates.

Two failure modes keep the conjecture contestable rather than settled. First, world-understanding may be narrower in the interpreter than the case needs: a model's world knowledge is broad but excludes the organizational, embodied, and participation-acquired facts that a situated programmer picks up without articulating, and Naur's "understands the whole world" phrasing sets a demanding bar. Second, a capacity is dispositional — it must be there on the next occasion too. An interpreter that resamples its judgment per session may exhibit the capacity on average without holding it reliably, which is a different property from a human theory-holder's continuity. Either failure would leave the argued half of Naur's thesis untouched and defeat the substrate conjecture, so the two claims are worth keeping separate.

## The general reading rule

Generalized past Naur, the rule is: when an argument shows that a capacity is irreducible to rules, ask what it thereby bounds. It bounds *artifacts that must decide unaided*. To also bound *artifacts consumed by a judging interpreter*, the argument needs a further premise about which interpreters are available and what they know. Where that premise is stated, it can be tested. Where it is assumed, the argument's conclusion inherits the substrate landscape of its writing — and that landscape can change without anyone revisiting the argument.

The rule cuts both ways. It does not license reading every tacit-knowledge argument as obsolete, because the further premise is sometimes both true and defensible: some capacities need world access that no available interpreter has. It licenses only separating the two questions, so that the substrate question gets argued instead of inherited.

## Scope

- **Reading based on retained quotes.** The diagnosis rests on the passages retained in the [ingest](../../../../sources/programming-as-theory-building.ingest.md), particularly the relevance-decision passage where the requirement and the bearer appear in adjacent clauses. If the essay argues elsewhere that no non-human bearer could meet the world-understanding requirement, the "assumed half" reading is defeated for Naur specifically while the general reading rule survives.
- **Diagnosis versus refutation.** Showing that a step was assumed rather than argued does not show the step is false. Naur's conclusion could still hold for reasons he did not give.
- **Conjecture, not finding.** The composite-substrate claim in the second section is a conjecture. Nothing here shows that any current system holds program theory; it shows that the classical argument against the possibility does not reach a text-plus-interpreter system.
- **Publication date.** The essay was an invited 1984 keynote published in 1985. "In 1985" names the writing context, not a precise threshold — the candidate set stayed empty for decades afterwards.

## Open Questions

- What test would distinguish a composite that holds the capacity from one that produces plausible post-hoc justifications for whatever it did. A cohort of novel modification demands, scored on coherent extension versus patching, is the obvious shape, and it needs the oracle problem solved first.
- Whether dispositional reliability can be bought by retention. A retained record of past similarity judgments might stabilize the interpreter's future ones, which would make continuity a retention property rather than an interpreter property.
- Whether the participation-acquired facts Naur's transfer-by-guided-work route conveys are unwritable in principle or merely never written, since the two are indistinguishable from the outside when nobody tried.

---

Relevant Notes:

- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) — extends: states the substrate conditions this note clears the classical objection to
- [Design rationale must preserve decision premises its interpreter cannot regenerate](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md) — mechanism: how the text half of the composite is scoped, premise by premise
- [Attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md) — grounds: why a recovery failure locates missing content rather than proving in-principle inexpressibility
- [Legal drafting solves the same problem as context engineering](../../../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) — evidenced-by: a domain that never assumed its texts must decide unaided, and built its practice around a judging interpreter instead
- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — mechanism: the same premise/judgment split applied at instruction grain, where the executor plays the interpreter's role
- [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) — enables: the oracle any test of the composite's modification judgment would need
- [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) — abstracted-from: supplies the three theory-holder capabilities and the relevance-decision passage; the argued/assumed split and the general reading rule are this note's own
