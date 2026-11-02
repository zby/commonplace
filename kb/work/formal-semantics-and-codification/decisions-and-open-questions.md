# Decisions and open questions

This register separates the workshop's settled choices from presentation choices, promotion tasks and review checks. It replaces the overlapping question lists in the [account](./symbolic-form-and-codification.md), [form definition](./representational-form-definition.md) and [codification definition](./codification-definition.md). The operator requested this explanation on 2026-11-02. The [README](./README.md#goal) records the operator's decisions and the write boundary. Recommendations below are proposals, not additional decisions or authorization to change the library.

## Settled decisions

### Symbolic form comes before codification

The form definition supplies the membership criterion. Codification names the move into that form. The old circular explanation, where each definition sent the reader to the other for its criterion, is removed. Updating library links to the criterion is promotion work, not a remaining choice about the account.

### Adoption can codify a prompt

A system can leave a prompt's text unchanged and adopt a frozen model package, including its decoding procedure, as the governing reference for an operation. Under that path the prompt is symbolic. Merely pinning a model for repeatability does not make its behavior authoritative: the system must treat that behavior as what the operation permits.

The consequence is deliberate. An adopted package can conform exactly while producing an inadequate summary. Adoption fixes the reference; it does not certify that reference against the original requirement. The old question about whether to accept adoption as codification is closed. Where to explain it in the definition remains a presentation choice below.

### Localization depends on the consumption path

A unit is separately identifiable content that the consumer interprets, checks or executes. A policy clause qualifies without having fixed consequences. A tensor operand qualifies under the runtime's path; the model's instruction-level commitments are not thereby separately exposed under the interpreter's path.

Classification therefore asks about localization first and assigned consequences second. The second question is not applicable where the relevant content is distributed across numerical state without such units. This resolves the old fourth-cell question and the question about whether path-relative localization belongs in the derivation: it is now part of that derivation, not merely a storage caveat.

### Opacity does not change symbolic membership

Symbolic content can be hard to inspect. The workshop keeps opacity separate from form and assesses it relative to a behavior or change of interest and an acceptable inspection cost. Scale, the reference's form and deliberate obfuscation are retained sources of that difficulty.

The old choice between excluding an opaque model package and classifying its prompt as symbolic is closed. What remains open is how much of the opacity explanation belongs in the definition rather than a companion note.

### Authority and adequacy are separate

Formalizing a consumer describes its computation. It does not by itself make the consumer authoritative for the language it reads. Adopting a package establishes authority for the adopting system's operation, not for English's users generally.

The classification does not require the side theory's proposed explanation of repair and language change. Nor does it require showing that English cannot have a formal description. The probe's question about an interpreter's fidelity to scoped English remains a substantive adequacy question, not a condition silently added to symbolic membership.

## Remaining presentation choices

### How much of the three-grade explanation should be retained?

The account distinguishes an accepted written formal semantics, a governing reference from which one could be derived, and neither. Classification groups the first two together. The choice is whether the definitions need all three grades or only the boundary that determines membership.

**Recommendation:** keep the full explanation in the account and the membership boundary in the definitions. The grades help explain the reasoning but are not three additional representational forms. Any example labeled as lacking a written semantics must be scoped carefully; the approved Python revision avoids a blanket absence claim.

### Where should the detailed opacity treatment live?

The modifier and its three sources are settled. Repeating the full treatment in the account, definition and opacity note may obscure the short classification rule.

**Recommendation:** retain a short definition and contrasting examples in the form definition. Put the fuller mechanisms and obfuscation evidence in the opacity note during authorized promotion. The cost is one extra lookup for readers who need the mechanism. This is a placement recommendation, not permission to edit that note now.

### How explicit should clarification be in the definitions?

A fixed execution contract can include questions, errors or defaults. Asking for an input does not itself reopen the governing rules. The account explains this with an interactive parser; the definitions currently mention clarification steps more briefly.

**Recommendation:** retain one explicit sentence that codification can include declared clarification steps, and leave the parser comparison in the account. Expand the definition only if readers still infer that codification excludes interaction. The remaining choice is explanatory detail, not whether clarification is permitted.

### Should the natural-language definition retain the author-availability clause?

The clause says conventions can make a reading wrong even when the author cannot be asked. It prevents a return to the rejected idea that authors alone determine correctness. It does not require the side theory's proposed mechanism for how conventions persist.

**Recommendation:** retain it as a claim of the definition. This keeps disagreement distinct from correctness and clarification distinct from semantic authority. Its inclusion remains a wording choice; it has not been removed as a supposedly unsupported dependency.

### Should the form definition state explicitly that adequacy is separate?

The account already separates conformance to the reference from satisfaction of the original requirement. A reader encountering only the form definition might nevertheless hear “symbolic” as a quality judgment.

**Recommendation:** add a short explicit sentence there, rather than relying on the codification definition or a misuse case: adopting a reference does not establish its adequacy to the task. This would state an existing decision, not introduce a new criterion. No additional sentence has been applied under this register alone.

### Should adopted models appear in the opening?

Adoption as codification is settled. The remaining choice is whether to name adopted model packages immediately or introduce the less familiar case after ordinary code and schemas.

**Recommendation:** keep the existing opening list inclusive and explain the case in the criterion section. Hiding it only in misuse cases would make the opening suggest a narrower definition than the workshop adopted.

### How much historical terminology should remain?

The retired phrase collided with the programming-language sense of operational semantics and with operationalism. Removing that phrase reduces the need to teach both contrasts inside the definition.

**Recommendation:** keep the current brief terminology notice and see-also links, with detailed sense distinctions in the collision ledger. Whether readers still need more explanation is the remaining editorial question, not a reason to retain the retired phrase.

## Promotion tasks, not conceptual questions

The [follow-up list](./follow-up-library-changes.md#promotion-checklist) owns the work outside these drafts: audit dependencies on the old argument, redirect links to the new criterion, migrate terminology, update opacity coverage and repoint draft links. None of this is authorized by the present workshop edit.

## Review checks, not wording decisions

The boundary table is tested by adding cases and specifying their consumption paths. A new counterexample can reopen a claim; merely retaining a standing review check does not mean the operator's decisions are undecided. Useful comparisons already include a policy clause, schema field, tensor operand, adopted prompt, human approval input, and compiled and neural implementations behind the same API.

Before promotion, check that the two definitions classify these cases consistently with the account and preserve the distinction between conformance, specified behavior and requirement adequacy. The operator's promotion decision remains separate from these checks.
