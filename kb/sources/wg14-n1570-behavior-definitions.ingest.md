---
description: "N1570 distinguishes documented implementation choices, permitted alternatives and behavior without standard requirements, bounding claims about shared semantics and conformance."
source: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
captured: "2026-11-02"
capture: pdftotext
capture_scope: excerpt
genre: official-statement
snapshot_sha256: 882a86a970a82e446d3f51c9d7a14c93fff875e121e125e27c4fb47243b05d94
ingested: "2026-11-02"
occasion: "How does N1570 classify behavior left open by the specification, and which obligations distinguish implementation-defined, undefined and unspecified behavior?"
type: types/ingest-report.md
domains: [C-language, behavior-categories, implementation-conformance]
---

# Ingest: WG14 N1570 behavior definitions

## Classification

An official committee-draft excerpt defining C terminology, not an empirical study of compiler behavior. Its evidential role is to establish what this draft says about permitted choices and implementation obligations.

Author: ISO/IEC JTC 1/SC 22/WG 14, the C language working group. The captured document is N1570, dated April 12, 2011, rather than the final published C11 standard.

## Summary

[N1570 §§3.4.1–3.4.4](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf) distinguishes several ways behavior can depend on choices or fall outside the standard's requirements. Implementation-defined behavior is unspecified behavior for which each implementation documents how the choice is made. Unspecified behavior involves an unspecified value or two or more possibilities provided by the standard, with no further requirements on which is chosen in any instance. Undefined behavior, arising from a nonportable or erroneous construct or erroneous data, is behavior for which the standard imposes no requirements; the accompanying note includes unpredictable results, documented behavior with or without a diagnostic, and termination among possible manifestations. Locale-specific behavior depends on national, cultural and linguistic conventions documented by each implementation. These definitions distinguish documented choice, permitted alternatives and absence of requirements; they do not equate every difference between implementations with non-conformance.

## Quotes

> implementation-defined behavior
> unspecified behavior where each implementation documents how the choice is made
> --- `kb/sources/.snapshots/wg14-n1570-behavior-definitions.md` @ `sha256:882a86a970a82e446d3f51c9d7a14c93fff875e121e125e27c4fb47243b05d94` — §3.4.1 paragraph 1

> undefined behavior
> behavior, upon use of a nonportable or erroneous program construct or of erroneous data,
> for which this International Standard imposes no requirements
> --- `kb/sources/.snapshots/wg14-n1570-behavior-definitions.md` @ `sha256:882a86a970a82e446d3f51c9d7a14c93fff875e121e125e27c4fb47243b05d94` — §3.4.3 paragraph 1

> NOTE Possible undefined behavior ranges from ignoring the situation completely with unpredictable
> results, to behaving during translation or program execution in a documented manner characteristic of the
> environment (with or without the issuance of a diagnostic message), to terminating a translation or
> execution (with the issuance of a diagnostic message).
> --- `kb/sources/.snapshots/wg14-n1570-behavior-definitions.md` @ `sha256:882a86a970a82e446d3f51c9d7a14c93fff875e121e125e27c4fb47243b05d94` — §3.4.3 paragraph 2, note

> unspecified behavior
> use of an unspecified value, or other behavior where this International Standard provides
> two or more possibilities and imposes no further requirements on which is chosen in any
> instance
> --- `kb/sources/.snapshots/wg14-n1570-behavior-definitions.md` @ `sha256:882a86a970a82e446d3f51c9d7a14c93fff875e121e125e27c4fb47243b05d94` — §3.4.4 paragraph 1

## Connections Found

The excerpt supplies definitional evidence for [Implementations do not establish shared semantics](../theory/implementations-do-not-establish-shared-semantics.md): its distinction between required agreement and permitted variation has a concrete language-reference example. For the present question, the useful addition is the documentation obligation that distinguishes implementation-defined behavior from unspecified behavior generally. It also qualifies the scope caveat in [Traditional software can bracket executor conformance; LLM systems cannot](../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md): undefined behavior is not itself evidence of compiler non-conformance, because the standard imposes no requirements on that behavior. This source supplies neither a conformance test nor evidence about compiler reliability rates.

## Extractable Value

1. **Separate the obligations, not just the labels.** Implementation-defined behavior requires each implementation to document how its choice is made (§3.4.1). Unspecified behavior permits the alternatives supplied by the standard without further requirements on the choice in any instance (§3.4.4); this definition does not impose the implementation-defined documentation obligation. Undefined behavior carries no requirements from this standard (§3.4.3), so it is not merely another choice among a bounded set of permitted alternatives. This is a precise reference for the occasion and for the shared-semantics note's treatment of variation. [quick-win]
2. **Do not infer non-conformance from differing outcomes alone.** The unspecified-behavior definition gives a concrete case where the reference permits several possibilities. The undefined-behavior definition separately prevents treating an unwanted outcome as a violation of requirements that this standard does not impose. This distinction sharpens conformance reasoning without establishing how reliably any compiler conforms. [quick-win]
3. **Keep locale dependence explicit.** Section 3.4.2 defines locale-specific behavior through local conventions and implementation documentation. It is useful adjacent vocabulary, but the excerpt does not establish its full relationship to the other categories or a complete taxonomy of C behavior. [just-a-reference]

## Limitations (our opinion)

The capture contains only §§3.4.1–3.4.4, including their notes and examples. It omits the remainder of N1570, so it cannot establish all C behavior categories, all circumstances invoking these categories, or the draft's broader conformance and diagnostic rules. The examples illustrate definitions; they are not sufficient guidance for classifying every arithmetic, shift or evaluation-order case. The source is a committee draft, not evidence that the final published standard or later revisions use identical wording.

The document defines obligations rather than measuring compliance. It provides no observations about actual implementations, their documentation quality, compiler-bug rates or the prevalence of undefined behavior. Its relevance to Commonplace is a bounded comparison about reference-governed behavior; it does not establish equivalent categories for natural-language instructions or validate the reliability claims in the conformance note.

## Recommended Next Action

No further extraction is needed for the occasion: the bounded C examples are incorporated in [the semantic-reference account](../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md#what-the-reference-leaves-open) and the [codification definition](../theory/definitions/codification.md#criterion). Keep their scope limited to this committee-draft excerpt; it does not establish the account's separate category of defects in a reference.
