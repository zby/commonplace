# Candidate definitions of codification and representational form

Workshop draft, revised 2026-11-01. This file is step 3 of the [workshop](./README.md): it applies the [commitment account](./codification-as-commitment.md) to the library definitions. It was revised after [Astra's review](./review-2026-11-01-astra.md), which showed that designation alone cannot carry the criterion. The rejected formal-semantics candidates of 2026-10-31 are summarized in a footnote[^rejected]. The library definitions remain authoritative and unchanged.

## What changes and why

The current [codification](../../theory/definitions/codification.md) definition grounds the symbolic side in a conjecture that the reference rules admit a formal semantics, and treats consumer agreement as evidence for it. The [reductions](./implementation-and-shared-semantics.md) show that formalizability is trivial for any machine-consumed artifact and that agreement corroborates conformance only. The same sentences appear in the assigned-consequences axis of [representational form](../../theory/definitions/representational-form.md).

The proposed wording therefore:

- states the criterion as two conjuncts: a designated reference governs, and it settles the relevant choices by rules a consumer forbidden insight could follow;
- removes the formalizability conjecture and the sentence treating agreement as evidence for it;
- retires the fixed phrase "unique operational semantics", which collided with the programming-language term, in favor of plain wording;
- keeps the clerk test, the testing paragraph with tests recast as corroborating conformance, the proxy-versus-requirement split and the repeatability misuse case.

## Proposed library wording

### Codification: opening

> Codification commits a rule or operation stated in natural language to a symbolic artifact, such as code or a schema, whose permitted behavior is settled by a designated reference. Fixed rules, implemented by a runtime, parser, validator, type checker, query engine, or resolver, determine what behavior is permitted, including any variation and any clarification steps they explicitly provide for. The consumer changes from a model or human who reinterprets the text on each use to one bound by those rules, so what the artifact permits no longer depends on who reads it.

### Codification: criterion and testing

> The criterion has two parts. First, a designated reference governs the artifact: the system has adopted an implementation, a specification, or a specification plus execution parameters as what the artifact's language means, so a consumer held to it that departs from it is wrong. Second, the reference settles the relevant choices by rules a consumer forbidden insight could follow. A reference that settles by judgment about what was intended, such as a human arbitrator, governs without codifying. Where the reference leaves a choice open, that is a declared gap, not an alternative admissible interpretation. Natural language has conventions that make some readings wrong, but no designated reference for them, so two readings can both be reasonable and no consumer can settle the dispute by rule.
>
> Whether a formal semantics exists for the artifact's language is not the criterion. Any implemented consumer together with a machine model supplies a formal account of its own behavior, and this holds for a frozen language model as much as for a compiler. That account describes the consumer. It does not make the consumer constitutive of the artifact's meaning.

The clerk-test paragraph is kept as written. The testing paragraph is kept with one change: "corroborate the conjecture" becomes "corroborate conformance to the reference", and the sentence "Testing does not prove uniqueness or guarantee convergence on it" becomes "Testing does not prove conformance outside the tested cases."

The terminology section drops the explanation of the special phrase and keeps the ordinary-English contrast. The Plotkin and operationalism contrasts move to a one-line see-also, since the term they collide with is no longer used.

### Representational form: symbolic form

> **Symbolic** content sits in localized units whose permitted behavior is settled by a designated reference through rules a consumer follows without judging what was intended: fixed rules, implemented by a parser, interpreter, runtime, schema, validator, route table, or similar consumer, determine what behavior is permitted, including any variation they explicitly allow. The category is architectural, not a claim about classical symbolic AI.

### Representational form: assigned-consequences axis

> **Assigned consequences** — is the artifact consumed under a commitment to a designated reference that settles what it permits by rules a clerk could follow, or is it reinterpreted on each consumption? A written formal semantics is neither necessary nor sufficient. Many programming languages have none and still sit on this side, because an implementation is designated as their reference. A frozen model's computation can be formally described without the model becoming the reference for the English it reads. Two consumers held to one reference disagreeing about what the rules permit means one of them is wrong ([codification](../../theory/definitions/codification.md) states the test). Natural language has conventions but no designated reference for them, so two readings can both be reasonable, which is [underspecification](../../theory/agentic-systems-interpret-underspecified-instructions.md), not a defect of any particular text.

The repeatability misuse case is kept, with "Repeatability is not a unique operational semantics" becoming "Repeatability does not make the model a designated reference".

### Constraining

Two phrases change: "where the artifact has a unique operational semantics" becomes "where a designated reference settles what the artifact permits", in the misuse case and the footer label.

### Vocabulary collision ledger

The `operational` row loses its codification sense, since the fixed phrase is retired. The row keeps the lineage sense, the external senses, and the workshop-local sense. Its guidance changes from "write the fixed phrase whole" to "say that a designated reference settles what the artifact permits".

Other library uses of the fixed phrase are migrated to the same wording. The two source ingests that gloss the phrase keep it as a historical reference to the retired term.

## Open questions about the wording

1. Is dropping the Plotkin and operationalism contrasts safe once the colliding phrase is gone, or do readers still arrive with the programming-language sense of "semantics"?
2. Does any library note rely on the formalizability conjecture rather than on the constitutive reading? The migration list should check each use of the retired phrase, not only replace it.

Promotion requires coordinated revisions of codification, representational form, constraining, the collision ledger, and the other library uses of the retired phrase. This workshop authorizes none of those edits.

[^rejected]: Four candidates of 2026-10-31 kept formal semantics as the ground, with an "adequate reference interpreter" carrying the discriminating weight. They were rejected because the constructibility clause is satisfied by every machine-consumed artifact after the reductions, and adequacy is a graded language-fidelity judgment nobody can run. Their text is in commit 9f67de3f1; [Astra's review](./review-2026-11-01-astra.md) covers why designation alone is also insufficient.
