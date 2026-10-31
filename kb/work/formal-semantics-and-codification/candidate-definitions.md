# Candidate definitions using formal semantics

Workshop draft, 2026-10-31. The operator requested these definitions after the discussion retained in [the reductions note](./implementation-and-shared-semantics.md). These are candidates for review, not adopted vocabulary. The current library definitions remain authoritative and unchanged.

## What has been gained

Returning to a shared or unique semantics is not returning to the starting point. The reductions remove the need for Commonplace's special sense of “operational semantics” and isolate the remaining role of uniqueness:

1. A formal semantics need not have been explicitly written down.
2. An implementation plus a sufficiently specified machine model supplies a formal account of its behavior. This construction includes bugs.
3. Independent executors agreeing under tests that could expose disagreement corroborate a claim of shared semantics or conformance; agreement does not prove it.
4. Incompatible implementations can each have a formal account and pass the same tests. Their disagreement does not disprove the existence of formal semantics.
5. Permitted variation and ambiguity can be formally represented. Multiple permitted results are not disagreement about what is permitted.
6. “Unique” concerns the account of permitted behavior, not a unique mathematical presentation or a single output.

The remaining problem is narrower: when does an implementation's formal account describe the artifact's meaning, rather than merely that implementation's response to the artifact? This unresolved question does not erase the reductions above.

## Candidate 1: Shared or unique formal semantics

**Candidate definition:** An artifact has a unique formal semantics within a specified scope when one fixed account determines what behavior it permits, including explicitly allowed variation, and conforming interpreters preserve that account. The account need not have been explicitly specified, and equivalent mathematical presentations count as the same semantics.

“Shared formal semantics” emphasizes preservation across interpreters. “Unique formal semantics” emphasizes that their identities do not change what is permitted. These are explanatory phrasings here, not proposals to register two new terms. Prefer direct wording such as “the same rules for permitted behavior” where that carries the sentence.

The scope must fix the language version, relevant execution parameters, and observations being compared. Two interpreters may choose different permitted results while agreeing on the semantics. An interpreter that violates the rules has an implementation failure; its actual behavior can still have a formal description.

Whether actual implementations preserve the same account is conjectural unless established by stronger means. Passing conformance tests corroborates that claim, not the bare existence of some formal description of each implementation.

## Candidate 2: Symbolic representational form

Proposed replacement for the symbolic part of [representational form](../../theory/definitions/representational-form.md):

> Symbolic content is retained in identifiable units whose rules determine what behavior is permitted. Those rules are taken to admit a formal semantics that conforming consumers preserve, whether or not that semantics has been explicitly specified. The rules may permit variation; a consumer's identity does not change what is permitted.

“Taken to admit” records a conjectural commitment rather than requiring a completed formalization. Explicit formal specifications remain included. Code, schemas, grammars, and resolver-consumed tables remain candidate instances; structured formatting alone is insufficient.

## Candidate 3: Codification

Proposed replacement for the opening of [codification](../../theory/definitions/codification.md):

> Codification commits a rule or operation stated in natural language to a symbolic artifact whose fixed rules determine what behavior is permitted. Those rules are taken to admit a formal semantics that conforming consumers preserve, whether or not anyone has explicitly specified it. Codification is the symbolic region of constraining: making prose more precise alone does not establish that this change has occurred.

[Constraining](../../theory/definitions/constraining.md) retains its current meaning: committing choices that narrow or rank permitted readings or behaviors. No replacement definition of constraining as a whole is proposed here.

The full definition should retain these limits:

- Codification need not select a single result. It can commit to a rule permitting many results.
- Formalizing actual behavior does not show that it implements the intended rule correctly.
- A codified check does not establish that it captures its intended requirement.
- A skill's extraction from methodology or addition of frontmatter does not alone change how its operative instructions are interpreted.

## Unresolved boundary across the candidates

The shared or unique formal-semantics candidate defines the property under discussion; it does not establish which languages have it. Natural language might also have a complete formal semantics that we have not specified, so existence of one fixed account does not yet distinguish natural language from symbolic content.

The symbolic-form candidate retains the intended criterion while replacing the awkward terminology, but does not prove the distinction. Codification inherits this boundary question through “symbolic.” The complementary natural-language category must not be defined as “content for which formal semantics is impossible” on the strength of this draft.

## Constructive access: useful reduction, not a replacement definition

The operator proposed a possible practical basis for the distinction. For a programming-language implementation, we can construct a formal account by following its computational machinery. For unrestricted natural language, we lack an established general construction of its complete meaning.

A compiler genealogy need not be followed back to lambda calculus. An executable together with its machine model suffices to describe implemented behavior; compilation history matters separately to claims of faithful compilation. Complexity alone is not the obstacle: an enormous construction is still a construction.

But the construction also applies to a fixed LLM implementation. Distinguishing the resulting account of its responses from the prompt's meaning brings us back to the requirement for semantics that conforming interpreters preserve. Constructive access therefore clarifies what is available for an implementation without independently settling the language-level distinction.

The later assistant suggestion to define codification simply as replacing interpretation at use time with an implemented rule is not adopted here. The operator's correction was to retain the progress toward formal-semantics vocabulary, not to abandon the shared-semantics question.

## Semantic expansion: the operator's question

The operator distinguished two kinds of plurality:

- A rule already allows several answers. “Return an integer greater than 10” gives no disagreement about which integers qualify.
- Interpreters disagree about what the rule permits. A revised semantics might admit both readings, reject one, or require further words to disambiguate.

The further question is an indefinitely continuing sequence of revisions:

1. Start with a proposed semantics.
2. Encounter a disagreement that it does not settle.
3. Expand or revise the semantics to settle that case.
4. Encounter a further disagreement under the expanded semantics.
5. Repeat without reaching a final account.

This is not merely infinitely many disagreements covered by one fixed rule. It asks whether each attempted completion still leaves a case requiring semantic extension.

Two claims remain separate:

- No stage in such a sequence is final.
- No fixed formal account can describe the sequence of extensions itself.

The first does not establish the second. Nor does a sequence of unsuccessful accounts establish that every possible account must fail.

The discussion identified open texture and semantic-paradox literature as relevant. The literature search has not yet been retained as a source-grounded argument in this workshop. These paragraphs record the operator's question, not a claimed impossibility result.

## Review before adoption

Review should determine:

1. Whether “shared formal semantics” preserves the useful content of the current criterion without its special use of “operational semantics.”
2. What independently distinguishes a symbolic artifact from natural language if both admit complete formal semantics.
3. Whether the frozen prompt–model package is symbolic as an operation while its prompt remains natural-language content, or whether that answer merely assumes the classification under investigation.
4. Whether explicit permission rules, a complete account of meaning, and an executable decision procedure have been kept separate.

Promotion would require coordinated revisions of codification, representational form, the codification passages in constraining, and the vocabulary collision ledger. This file authorizes none of those edits.
