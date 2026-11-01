# Candidate definitions of representational form and codification

Workshop draft, revised 2026-11-01. This file is step 3 of the [workshop](./README.md): it applies the [account of symbolic form](./codification-as-commitment.md) to the library definitions. Symbolic form is defined first, by the language: a formal semantics or something close to one, where "close" means a reference the language's users hold consumers to and from which a formal semantics could be derived. Codification is then the move into symbolic form. Whether the result can be read is marked by the modifier *opaque* on symbolic form, with two sources, and the phrase "unique operational semantics" is retired with the formalizability conjecture behind it. The rejected formal-semantics candidates of 2026-10-31 are summarized in a footnote[^rejected]. The library definitions remain authoritative and unchanged.

## What changes and why

The current [codification](../../theory/definitions/codification.md) definition grounds the symbolic side in a conjecture that the reference rules admit a formal semantics, and treats consumer agreement as evidence for it. The [reductions](./implementation-and-shared-semantics.md) show that formalizability is trivial for any machine-consumed artifact and that agreement corroborates conformance only. The same sentences appear in the assigned-consequences axis of [representational form](../../theory/definitions/representational-form.md), which then sends the reader to codification for the test.

The proposed wording therefore:

- puts the criterion in symbolic form, where the form definition's own sentence "codification moves content from natural-language into symbolic form" already implies it belongs: the artifact's language has a formal semantics or is close to one, where close means its users hold consumers to a reference, a standard or an implementation, from which a formal semantics could be derived;
- defines codification as the move into symbolic form, made either by rewriting the artifact or by adopting a consumer as the reference under a consumption path;
- says that a formalization of a consumer is the semantics of a language only when that language's users hold consumers to it, so a frozen model adopted for an operation codifies the operation without defining the semantics of English;
- adds the modifier *opaque* to symbolic form for content whose reference cannot be read per rule, from the artifact's scale or from the reference's form; the modifier sets inspection method and revision locus, not membership;
- removes the formalizability conjecture and the sentence treating agreement as evidence for it;
- retires the fixed phrase "unique operational semantics", which collided with the programming-language term, in favor of plain wording;
- rewrites the clerk paragraph, recasts tests as corroborating conformance, keeps the proxy-versus-requirement split, and narrows the repeatability misuse case to repeatability.

## Proposed library wording

### Representational form: symbolic form

> **Symbolic** content sits in localized units whose consequences, under the consumption path in question, are fixed by the reference of a language that has a formal semantics or is close to one. A language is close to a formal semantics when its users hold its consumers to a reference, a standard or an implementation, from which a formal semantics could be derived; a consumer held to the reference that departs from it is wrong. Fixed rules, implemented by a parser, interpreter, runtime, schema, validator, route table, adopted model package, or similar consumer, determine what behavior is permitted, including any variation they explicitly allow. The category is architectural, not a claim about classical symbolic AI.

### Representational form: assigned-consequences axis

> **Assigned consequences** — under the consumption path in question, are the artifact's consequences fixed by the reference of a language close to a formal semantics, or is it reinterpreted on each consumption? A written formal semantics is neither necessary nor sufficient. Many programming languages have none and still sit on this side, because their users hold implementations to a reference from which one could be derived. A formal semantics can be derived from an implementation together with a machine model, or from a specification that states which expressions count and under what conditions an action is permitted; it cannot be derived from a human judge, so a reference that settles by judgment about what was intended governs without assigning consequences. A frozen model's computation can be formally described without the model becoming the reference for the English it reads; it becomes the reference only for the prompts of a system that adopts it for an operation. If two consumers held to one reference disagree about what the rules permit, one of them is wrong. Content no reference fixes can carry two reasonable readings, which is [underspecification](../../theory/agentic-systems-interpret-underspecified-instructions.md).

### Representational form: the opaque modifier

> Symbolic content is **opaque** under a consumption path when the reference that assigns its consequences cannot be read per rule. Opacity has three sources: the artifact's scale, where each unit is readable against the reference and the whole is not; the reference's form, where the reference is itself distributed-parametric, as a frozen model package is, so that even a one-line artifact's consequences cannot be read; and deliberate obfuscation, where a function-preserving transformation is chosen to show as little as possible; cryptography proves the strong form of that goal impossible in general, so symbolic form guarantees neither readability nor hiding. Opaque content is still symbolic: what counts as wrong is fixed. What it loses is checking by reading, revision by locating the rule, and declared gaps; its gaps are found on use. Opacity is an inspection property, not a form ([opacity is a scale threshold](../../theory/opacity-is-a-scale-threshold.md)).

### Representational form: inspection rule

> Form sets the default inspection method: read natural-language content, check symbolic artifacts against their reference, by reading where the artifact is not opaque and by running cases where it is, and probe distributed-parametric artifacts behaviorally.

### Representational form: misuse case

> Counting a fixed prompt and model as symbolic because its behavior repeats. Repeatability is not adoption: a prompt becomes symbolic under a consumption path only when a system adopts the model package, decoding included, as the reference for that operation. Under any other path the same prompt is natural-language, and no adoption makes the package a reference for English.

### Codification: opening

> Codification moves a rule or operation stated in natural language into [symbolic form](../../theory/definitions/representational-form.md): into an artifact, such as code or a schema, in a language that has a formal semantics or is close to one. Fixed rules, implemented by a runtime, parser, validator, type checker, query engine, resolver, or adopted model package, determine what behavior is permitted, including any variation and any clarification steps they explicitly provide for. The consumer changes from a model or human who reinterprets the text on each use to one bound by those rules, so what the artifact permits no longer depends on who reads it.

### Codification: criterion and testing

> The criterion is the one symbolic form states: the artifact's language has a formal semantics or is close to one. The move is made in one of two ways. Rewriting the artifact in such a language is the ordinary way. Adopting a consumer as the reference for an operation, such as a pinned model package with its decoding procedure, is the other: the text does not change, and its form under that consumption path does, because the system is now the sole user of the language of prompts as that package reads them and holds the consumer to it.
>
> What the reference leaves open is permitted variation, a required external selection, or a defect, and only the last is a failure of the reference. An artifact whose consequences no reference fixes is reinterpreted on each consumption, and two readings of it can both be reasonable.
>
> A formalization of a consumer is not the semantics of the language. Any implemented consumer together with a machine model supplies a formal account of its own behavior, and this holds for a frozen language model as much as for a compiler. That account is the semantics of a language only when the language's users hold consumers to it, so adopting a frozen model codifies the operation it is adopted for and leaves the semantics of English untouched.
>
> A codified artifact can be opaque, in the sense [symbolic form](../../theory/definitions/representational-form.md) gives the modifier: a large codebase from its scale, an adopted model package from the form of its reference. Opacity sets how the artifact is checked, by reading where it is not opaque and by running cases where it is, and where it is revised: with a schema the rule is fixed, with a frozen package only the prompt is editable. It does not set whether the artifact is codified. An opaque codification is a poor one, not a failed one.

The clerk paragraph is rewritten: Turing's clerk follows exact instructions without insight ([Church–Turing](../../sources/church-turing-thesis-sep.ingest.md)), which is why a formal semantics can be derived from a reference whose every step of application is mechanically checkable. The clerk explains derivability; it is not the criterion's wording. That is a condition on the steps, not a claim that every consequence is decidable, and not the old "where such a semantics can exist" framing. The testing paragraph is kept with two changes: "corroborate the conjecture" becomes "corroborate conformance to the reference", and "Testing does not prove uniqueness or guarantee convergence on it" becomes "Testing does not prove conformance outside the tested cases."

The terminology section drops the explanation of the special phrase and keeps the ordinary-English contrast. The Plotkin and operationalism contrasts move to a one-line see-also, since the term they collide with is no longer used.

### Constraining

Two phrases change: "where the artifact has a unique operational semantics" becomes "where the artifact's language has a formal semantics or is close to one", in the misuse case and the footer label.

### Vocabulary collision ledger

The `operational` row loses its codification sense, since the fixed phrase is retired. The row keeps the lineage sense, the external senses, and the workshop-local sense. Its guidance changes from "write the fixed phrase whole" to "say that the artifact's language has a formal semantics or is close to one, and link symbolic form for the gloss".

Other library uses of the fixed phrase are migrated to the same wording. The two source ingests that gloss the phrase keep it as a historical reference to the retired term.

Promotion requires coordinated revisions of representational form, codification, constraining, the collision ledger, and the other library uses of the retired phrase. This workshop authorizes none of those edits.

## Open questions about the wording

1. Is dropping the Plotkin and operationalism contrasts safe once the colliding phrase is gone, or do readers still arrive with the programming-language sense of "semantics"?
2. Does any library note rely on the formalizability conjecture rather than on the gloss? The migration list should check each use of the retired phrase, not only replace it.
3. "Adopted model package" now appears in the list of implementing consumers. Does the library want that consequence stated in the definition, or only in the misuse case?
4. "Close to a formal semantics" names a graded thing with a two-valued gloss. Does the library want the three grades of step 2, or only the boundary?
6. The opacity note says opacity is a scale threshold. The reference's form and deliberate obfuscation are two further sources, and both put opacity at small scale. Does the note take them, or does the form definition carry them alone?
5. Moving the criterion from codification into symbolic form reverses the current pointer between the two definitions. Does any other library note link codification for the test and need to link form instead?

[^rejected]: Four candidates of 2026-10-31 kept formal semantics as the ground, with an "adequate reference interpreter" doing the distinguishing work. They were rejected because the constructibility clause is satisfied by every machine-consumed artifact after the reductions, and adequacy is a graded language-fidelity judgment nobody can run. Their text is in commit 9f67de3f1; [Astra's first review](./review-2026-11-01-astra.md) covers why designation alone is also insufficient. The present wording returns to formal semantics as the ground and replaces the adequacy judgment with who is held to the reference.
