# Candidate definitions of codification and representational form

Workshop draft, revised 2026-11-01. This file is step 3 of the [workshop](./README.md): it applies the [account of the difference](./where-meaning-is-settled.md) to the library definitions. The earlier formal-semantics candidates of 2026-10-31 are retained in a footnote[^rejected]. The library definitions remain authoritative and unchanged.

## What changes and why

The current [codification](../../theory/definitions/codification.md) definition grounds the symbolic side in a conjecture that the reference rules admit a formal semantics, and treats consumer agreement as evidence for it. The [reductions](./implementation-and-shared-semantics.md) show that formalizability is trivial for any machine-consumed artifact and that agreement corroborates conformance only. The same sentences appear in the assigned-consequences axis of [representational form](../../theory/definitions/representational-form.md).

The proposed wording therefore:

- states the criterion directly as where meaning is settled, a designated prior reference against the author on request;
- removes the formalizability conjecture and the sentence treating agreement as evidence for it;
- retires the fixed phrase "unique operational semantics", which collided with the programming-language term, in favor of plain wording;
- keeps the clerk test, the testing paragraph with tests recast as corroborating conformance, the proxy-versus-requirement split and the repeatability misuse case.

## Proposed library wording

### Codification: opening

> Codification commits a rule or operation stated in natural language to a symbolic artifact, such as code or a schema, whose permitted behavior is settled by a designated reference. Fixed rules, implemented by a runtime, parser, validator, type checker, query engine, or resolver, determine what behavior is permitted, including any variation they explicitly allow. The consumer changes from a model or human who reinterprets the text on each use to one bound by those rules, so what the artifact permits no longer depends on who reads it.

### Codification: criterion and testing

> The criterion is constitutive, not formal. A symbolic artifact's language means what its designated reference says it means. The reference fixes the language version and any implementation or execution parameters needed to settle what is permitted. When two consumers held to that reference disagree about what the rules permit, one of them is wrong. Departures are failures to implement the committed rules, not alternative admissible interpretations. Natural language has no such prior reference. Its meaning is settled by its author on request, in the same language, so two readings can both be reasonable, and a consumer that cannot ask must leave them open.
>
> Whether a formal semantics exists for the artifact's language is not the criterion. Any implemented consumer together with a machine model supplies a formal account of its own behavior, and this holds for a frozen language model as much as for a compiler. That account describes the consumer. It does not make the consumer constitutive of the artifact's meaning.

The clerk-test paragraph is kept as written. The testing paragraph is kept with one change: "corroborate the conjecture" becomes "corroborate conformance to the reference", and the sentence "Testing does not prove uniqueness or guarantee convergence on it" becomes "Testing does not prove conformance outside the tested cases."

The terminology section drops the explanation of the special phrase and keeps the ordinary-English contrast. The Plotkin and operationalism contrasts move to a one-line see-also, since the term they collide with is no longer used.

### Representational form: symbolic form

> **Symbolic** content sits in localized units whose permitted behavior is settled by a designated reference: fixed rules, implemented by a parser, interpreter, runtime, schema, validator, route table, or similar consumer, determine what behavior is permitted, including any variation they explicitly allow. The category is architectural, not a claim about classical symbolic AI.

### Representational form: assigned-consequences axis

> **Assigned consequences** — does a designated reference settle what the artifact permits, or is it reinterpreted on each consumption? A written formal semantics is neither necessary nor sufficient. Most programming languages have none and still sit on this side, because an implementation is designated as their reference. A frozen model's computation can be formally described without the model becoming the reference for the English it reads. Two consumers held to one reference disagreeing about what the rules permit means one of them is wrong ([codification](../../theory/definitions/codification.md) states the test). Natural language has no prior adjudicator; its author settles meaning on request, so two readings can both be reasonable, which is [underspecification](../../theory/agentic-systems-interpret-underspecified-instructions.md), not a defect of any particular text.

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

[^rejected]: **Rejected candidates of 2026-10-31.** Four definitions tried to keep formal semantics as the ground. *Fixed formal semantics*: an artifact has one when a designated account determines its permitted behavior, specified mathematically or constructible from an implementation and execution model. *Adequate reference interpreter*: an interpreter is an adequate semantic reference for a language within a scope when it preserves the language's relevant distinctions of meaning; designation alone does not establish adequacy. *Symbolic form*: localized units with fixed rules whose formal account is explicit or constructible from an adequate reference interpreter. *Codification*: commitment to a symbolic artifact whose rules have such an account, where the commitment fixes an interpretation and satisfaction of the original requirement stays separate. They were rejected because the constructibility clause is satisfied by every machine-consumed artifact after the reductions, so all discriminating weight fell on "adequate", which is a graded language-fidelity judgment that nobody can run and that the workshop itself could not settle as a representational distinction. The candidates also smuggled the real discriminator in through an asymmetry: a compiler may "define a new language by stipulation" while a prompt–model package may not. Stated plainly, that asymmetry is the constitutive criterion in [where meaning is settled](./where-meaning-is-settled.md). The candidates additionally dropped the clerk test, which survives the reductions. The "fixed formal semantics" candidate would have replaced one KB-special phrase with another needing its own ledger row. The assessment programme that accompanied the adequacy candidate, namely recovering roles and scope, preserving meaning under paraphrase, distinguishing entailment from permission, and separating linguistic competence from knowledge and compliance, is retained in the [standalone question](./perfect-english-reference-question.md).
