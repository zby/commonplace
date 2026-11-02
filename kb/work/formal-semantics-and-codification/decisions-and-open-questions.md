# Decisions and open questions

This register separates the workshop's conceptual and presentation decisions from promotion tasks and review checks. It replaces the overlapping question lists in the [account](./symbolic-form-and-codification.md), [form definition](./representational-form-definition.md) and [codification definition](./codification-definition.md). The operator requested this explanation on 2026-11-02. The [README](./README.md#goal) records the operator's decisions and the write boundary. On 2026-11-02 the operator approved the seven presentation recommendations below, requesting conservative application and a whole-document flow and coherence check. No presentation choices in this register remain open. Review checks, unresolved research questions in the side theory, and authorization to promote remain separate.

## Settled decisions

### Symbolic form comes before codification

The form definition supplies the membership criterion. Codification names the move into that form. The old circular explanation, where each definition sent the reader to the other for its criterion, is removed. Updating library links to the criterion is promotion work, not a remaining choice about the account.

### Adoption can codify a prompt

A system can leave a prompt's text unchanged and adopt a frozen model package, including its decoding procedure, as the governing reference for an operation. Under that path the prompt is symbolic. Merely pinning a model for repeatability does not make its behavior authoritative: the system must treat that behavior as what the operation permits.

The consequence is deliberate. An adopted package can conform exactly while producing an inadequate summary. Adoption fixes the reference; it does not certify that reference against the original requirement. The old question about whether to accept adoption as codification is closed. Its placement in the definition is settled below.

### Localization depends on the consumption path

A unit is separately identifiable content that the consumer interprets, checks or executes. A policy clause qualifies without having fixed consequences. A tensor operand qualifies under the runtime's path; the model's instruction-level commitments are not thereby separately exposed under the interpreter's path.

Classification therefore asks about localization first and assigned consequences second. The second question is not applicable where the relevant content is distributed across numerical state without such units. This resolves the old fourth-cell question and the question about whether path-relative localization belongs in the derivation: it is now part of that derivation, not merely a storage caveat.

### Opacity does not change symbolic membership

Symbolic content can be hard to inspect. The workshop keeps opacity separate from form and assesses it relative to a behavior or change of interest and an acceptable inspection cost. Scale, the reference's form and deliberate obfuscation are retained sources of that difficulty.

The old choice between excluding an opaque model package and classifying its prompt as symbolic is closed. The placement decision below keeps a short treatment in the definition and reserves the full treatment for a companion note.

### Authority and adequacy are separate

Formalizing a consumer describes its computation. It does not by itself make the consumer authoritative for the language it reads. Adopting a package establishes authority for the adopting system's operation, not for English's users generally.

The classification does not require the side theory's proposed explanation of repair and language change. Nor does it require showing that English cannot have a formal description. The probe's question about an interpreter's fidelity to scoped English remains a substantive adequacy question, not a condition silently added to symbolic membership.

## Approved presentation choices

### Keep the grades in the account and the boundary in the definitions

The account distinguishes an accepted written formal semantics, a governing reference from which one could be derived, and neither. Classification groups the first two together.

**Decision:** retain the full explanation in the account and the membership boundary in the definitions. The grades explain the reasoning; they are not three additional representational forms. The existing definition already uses the boundary, so no new grade labels were added. The Python example avoids a blanket claim that no written formal semantics exists.

### Keep the opacity definition short

The modifier and its three sources are settled. Repeating the full treatment in the account, definition and opacity note would obscure the short classification rule.

**Decision:** retain a short definition and contrasting examples in the form definition. Keep the fuller mechanisms and obfuscation evidence in the account until authorized promotion places them in the opacity note. The definition links to that treatment instead of repeating it. Readers needing the mechanisms pay one extra lookup; the definition remains focused on classification.

### State that codification permits declared clarification

A fixed execution contract can include questions, errors or defaults. Asking for an input does not itself reopen the governing rules.

**Decision:** state explicitly that codification can include declared clarification steps as part of execution. Keep the interactive-parser comparison in the account. The definition now contains that statement without adding the longer example.

### Retain the author-availability clause

The natural-language definition says conventions can make a reading wrong even when the author cannot be asked. It prevents a return to the rejected idea that authors alone determine correctness. It does not require the side theory's mechanism for how conventions persist.

**Decision:** retain the clause as a claim of the definition. The existing wording is unchanged. It keeps disagreement distinct from correctness and clarification distinct from semantic authority.

### State explicitly that adoption does not establish adequacy

The account already separates conformance to the reference from satisfaction of the original requirement. A reader encountering only the form definition might nevertheless hear “symbolic” as a quality judgment.

**Decision:** add one sentence beside the symbolic criterion: “Adopting a reference does not establish its adequacy to the task.” This states the existing distinction without adding a membership condition.

### Keep adopted models in the opening

Adoption as codification is settled. Naming only ordinary code and schemas in the opening could suggest a narrower definition.

**Decision:** keep adopted model packages in the existing opening list and explain adoption in the criterion section. No change to that list or explanation was needed.

### Keep historical terminology brief

The retired phrase collided with the programming-language sense of operational semantics and with operationalism. Removing that phrase reduces the need to teach both contrasts inside the definition.

**Decision:** retain the current brief terminology notice and see-also links. Detailed sense distinctions belong in the collision ledger. The definition's existing treatment is unchanged; this decision does not restore the retired phrase.

## Promotion tasks, not conceptual questions

The [follow-up list](./follow-up-library-changes.md#promotion-checklist) owns the work outside these drafts: audit dependencies on the old argument, redirect links to the new criterion, migrate terminology, update opacity coverage and repoint draft links. None of this is authorized by the present workshop edit.

## Review checks, not wording decisions

The boundary table is tested by adding cases and specifying their consumption paths. A new counterexample can reopen a claim; merely retaining a standing review check does not mean the operator's decisions are undecided. Useful comparisons already include a policy clause, schema field, tensor operand, adopted prompt, human approval input, and compiled and neural implementations behind the same API.

Before promotion, check that the two definitions classify these cases consistently with the account and preserve the distinction between conformance, specified behavior and requirement adequacy. The operator's promotion decision remains separate from these checks.
