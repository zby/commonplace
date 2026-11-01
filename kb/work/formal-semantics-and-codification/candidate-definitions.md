# Candidate definitions of codification and representational form

Workshop draft, revised 2026-11-01. This file is step 3 of the [workshop](./README.md): it applies the [commitment account](./codification-as-commitment.md) to the library definitions. The proposed wording states the criterion as two parts, a designated reference that governs the artifact and settles the relevant choices by rules a clerk could execute, makes addressability a separate graded property, and retires the phrase "unique operational semantics" with the formalizability conjecture behind it. The rejected formal-semantics candidates of 2026-10-31 are summarized in a footnote[^rejected]. The library definitions remain authoritative and unchanged.

## What changes and why

The current [codification](../../theory/definitions/codification.md) definition grounds the symbolic side in a conjecture that the reference rules admit a formal semantics, and treats consumer agreement as evidence for it. The [reductions](./implementation-and-shared-semantics.md) show that formalizability is trivial for any machine-consumed artifact and that agreement corroborates conformance only. The same sentences appear in the assigned-consequences axis of [representational form](../../theory/definitions/representational-form.md).

The proposed wording therefore:

- states the criterion as two conjuncts: a designated reference governs, and it settles the relevant choices by rules a consumer forbidden insight could execute;
- makes addressability of the reference a separate, graded property that sets inspection method and revision locus, not membership;
- removes the formalizability conjecture and the sentence treating agreement as evidence for it;
- retires the fixed phrase "unique operational semantics", which collided with the programming-language term, in favor of plain wording;
- rewrites the clerk paragraph, recasts tests as corroborating conformance, keeps the proxy-versus-requirement split, and narrows the repeatability misuse case to repeatability.

## Proposed library wording

### Codification: opening

> Codification commits a rule or operation stated in natural language to a symbolic artifact, such as code or a schema, whose permitted behavior is settled by a designated reference that a clerk could execute. Fixed rules, implemented by a runtime, parser, validator, type checker, query engine, resolver, or adopted model package, determine what behavior is permitted, including any variation and any clarification steps they explicitly provide for. The consumer changes from a model or human who reinterprets the text on each use to one bound by those rules, so what the artifact permits no longer depends on who reads it.

### Codification: criterion and testing

> The criterion has two parts. First, a designated reference governs the artifact: the system has adopted an implementation, a specification, or a specification plus execution parameters as what the artifact's language means, so a consumer held to it that departs from it is wrong. Adoption is an act of the system; running an implementation does not by itself adopt it.
>
> Second, the reference settles the relevant choices by rules a consumer forbidden insight could execute: each step of applying the reference is mechanically checkable. A reference that settles by judgment about what was intended, such as a human arbitrator, governs without codifying. What the reference leaves open is permitted variation, a required external selection, or a defect, and only the last is a failure of the reference.
>
> An artifact whose consequences no such reference fixes is reinterpreted on each consumption, and two readings of it can both be reasonable.
>
> Whether a formal semantics exists for the artifact's language is not the criterion. Any implemented consumer together with a machine model supplies a formal account of its own behavior, and this holds for a frozen language model as much as for a compiler. That account describes the consumer. It does not make the consumer the artifact's designated reference.
>
> How addressable the reference is, whether the rule that assigns a consequence can be pointed at, read, and revised separately, is a separate and graded property. It sets how a codified artifact is checked, statically where the rules can be read and by running cases where they cannot, and where it is revised. It does not set whether the artifact is codified: a large codebase and an adopted model package are both codified, and neither is fully addressable in practice.

The clerk paragraph is rewritten: Turing's clerk follows exact instructions without insight ([Church–Turing](../../sources/church-turing-thesis-sep.ingest.md)), so a rule is a candidate for codification when a clerk could execute each step of applying it. That is a condition on the steps, not a claim that every consequence is decidable, and not the old "where such a semantics can exist" framing. The testing paragraph is kept with two changes: "corroborate the conjecture" becomes "corroborate conformance to the reference", and "Testing does not prove uniqueness or guarantee convergence on it" becomes "Testing does not prove conformance outside the tested cases."

The terminology section drops the explanation of the special phrase and keeps the ordinary-English contrast. The Plotkin and operationalism contrasts move to a one-line see-also, since the term they collide with is no longer used.

### Representational form: symbolic form

> **Symbolic** content sits in localized units whose consequences, under the consumption path in question, are fixed by a designated reference that a clerk could execute. Fixed rules, implemented by a parser, interpreter, runtime, schema, validator, route table, adopted model package, or similar consumer, determine what behavior is permitted, including any variation they explicitly allow. The category is architectural, not a claim about classical symbolic AI.

### Representational form: inspection rule

> Form sets the default inspection method: read natural-language content, check symbolic artifacts against their reference, statically where its rules can be read and by running cases where they cannot, and probe distributed-parametric artifacts behaviorally.

### Representational form: assigned-consequences axis

> **Assigned consequences** — under the consumption path in question, are the artifact's consequences fixed by a designated reference a clerk could execute, or is it reinterpreted on each consumption? A written formal semantics is neither necessary nor sufficient. Many programming languages have none and still sit on this side, because an implementation is designated as their reference. A frozen model's computation can be formally described without the model becoming the reference for the English it reads; it becomes that reference only when a system adopts the package for an operation. If two consumers held to one reference disagree about what the rules permit, one of them is wrong ([codification](../../theory/definitions/codification.md) states the test). Content no reference fixes can carry two reasonable readings, which is [underspecification](../../theory/agentic-systems-interpret-underspecified-instructions.md).

### Representational form: misuse case

> Counting a fixed prompt and model as symbolic because its behavior repeats. Repeatability is not designation: a prompt becomes symbolic under a consumption path only when a system adopts the model package, decoding included, as the reference for that operation. Under any other path the same prompt is natural-language.

### Constraining

Two phrases change: "where the artifact has a unique operational semantics" becomes "where a designated reference a clerk could execute settles what the artifact permits", in the misuse case and the footer label.

### Vocabulary collision ledger

The `operational` row loses its codification sense, since the fixed phrase is retired. The row keeps the lineage sense, the external senses, and the workshop-local sense. Its guidance changes from "write the fixed phrase whole" to "say that a designated reference a clerk could execute settles what the artifact permits".

Other library uses of the fixed phrase are migrated to the same wording. The two source ingests that gloss the phrase keep it as a historical reference to the retired term.

Promotion requires coordinated revisions of codification, representational form, constraining, the collision ledger, and the other library uses of the retired phrase. This workshop authorizes none of those edits.

## Open questions about the wording

1. Is dropping the Plotkin and operationalism contrasts safe once the colliding phrase is gone, or do readers still arrive with the programming-language sense of "semantics"?
2. Does any library note rely on the formalizability conjecture rather than on the two-part criterion? The migration list should check each use of the retired phrase, not only replace it.
3. "Adopted model package" now appears in the list of implementing consumers. Does the library want that consequence stated in the definition, or only in the misuse case?

[^rejected]: Four candidates of 2026-10-31 kept formal semantics as the ground, with an "adequate reference interpreter" doing the distinguishing work. They were rejected because the constructibility clause is satisfied by every machine-consumed artifact after the reductions, and adequacy is a graded language-fidelity judgment nobody can run. Their text is in commit 9f67de3f1; [Astra's first review](./review-2026-11-01-astra.md) covers why designation alone is also insufficient.
