---
description: "How Commonplace decides which borrowed ideas to adopt — a fast pass for programming patterns on the software-mechanism bet, first-principles or target-side warrant for other sources, and direct observation as a separate evidence path"
type: kb/types/note.md
traits: []
tags: [foundations]
---

# Source-adoption policy

Commonplace draws its design from programming-language theory, cognitive science, HCI, legal drafting, and direct observation of its own use. Any source is admissible — the [related-systems](../agent-memory-systems/README.md) reviews exist to widen the input surface — but the *adoption gate* differs by source. This document records the policy the framework applies and the rationale it states for each gate; the policy is a working stance, not an established theory of cross-domain transfer.

## The programming fast pass

Commonplace adopts programming patterns — types, validation, testing, progressive compilation, version control, structural typing, and structural refinement as gradual typing — without first deriving why each transfers. The stated rationale is a bet: that agents interpreting prompts and interpreters interpreting programming languages are both bounded processors composing text under constraints, so the patterns transfer by shared mechanism rather than by analogy. The framework treats this as a hypothesis it operates under, not a demonstrated identity.

The parallel the bet rests on is that programming systems are formal, compositional, and text-based, and so is the KB — formal (frontmatter schemas), compositional (notes link and compose), text-based (markdown files). The policy applies the shared-mechanism reading most confidently to the *symbolic shell* — schemas, validators, typed artifacts, version control — where the substrates genuinely coincide. It does not extend the identity claim to the LLM's interpretive core, which still reads underspecified natural language probabilistically; patterns that depend on deterministic execution semantics fall outside the fast pass.

The framework cites [Thalo](../agent-memory-systems/reviews/thalo.md) — an independent project that built compiler-like tooling for knowledge management (a Tree-Sitter grammar, typed entities, a validation-rule set) — as convergence evidence: a separate team reached for the same toolbox. This is treated as corroboration for tooling of this kind, not proof of wholesale transfer, since it is equally consistent with shared engineering priors.

## First principles: the gate for everything else

For non-programming sources, the gate is first-principles support: a pattern is adopted with confidence when the framework can derive *why* it works from the domain's constraints — finite context windows, no import/resolution mechanism, text-only reasoning, everything loaded competing for attention. [Context loading economy](../notes/instruction-specificity-should-match-loading-frequency.md) and [directory-scoped types](../notes/directory-scoped-types-are-cheaper-than-global-types.md) are examples: both follow from the constraints without an analogy.

Cognitive-science and HCI patterns pass only when first-principles reasoning supports them. [Three-space memory](../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) is adopted because it maps to a real architectural need — separating concerns with different churn rates — not because Tulving's taxonomy is authoritative for LLM agents. The cognitive-psychology claims in the [Ars Contexta](../agent-memory-systems/reviews/arscontexta.md) review are acknowledged but not adopted wholesale; a spreading-activation model may not predict how a large context window behaves. The asymmetry with programming is not about field quality but about target fit: human cognition is associative, embodied, and affective, while LLM agents process text in a fixed window with no persistent cross-session state, so cognitive-science analogies need independent justification.

## Legal drafting: eligible but untested

Law has long methodology for the same problem — writing natural-language specifications interpreted by a judgment-exercising processor — and unlike programming it shares the prompt's medium: [natural language with irreducible ambiguity](../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md). The structural parallel is close (precedent constrains; canons of interpretation narrow the reading space), but the framework has not yet borrowed a concrete legal technique and applied it successfully. Until it has, legal drafting stays an eligible source, not a fast pass.

## Direct observation: a separate path

Direct observation of what works in this system — the improvement log, friction notes, prose reviews — does not go through the borrowing gate at all. It is evidence from the system itself, not transferred from another domain; the [verifiability gradient](../notes/verifiability-gradient.md), for instance, was found by watching patterns in use. The framework weights observation and constraint-derived design differently: observations are plentiful but individually weak (a single one may be a local quirk or an artefact of current scale), while inherited constraints are scarce but each is strong for as long as the commitment that forces it holds. Observations accumulate into confidence by recurring; a constraint-derived argument carries its confidence from its commitment and loses it if that commitment changes. Per the [wikiwiki principle](../notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md), observations are captured freely and refined, and the ones that recur across sessions graduate into durable patterns worth codifying.

---

Relevant Notes:

- [A borrowed pattern transfers only as far as source and target share a mechanism](../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) — rests-on: the general discriminator this policy applies — a fast pass only where the shared mechanism reaches, target-side evidence otherwise
- [Underspecification and indeterminism complicate programming-pattern transfer](../notes/underspecification-and-indeterminism-complicate-programming-for.md) — rests-on: why the programming fast pass stops at the symbolic shell and not the interpretive core
- [Legal drafting solves the same problem as context engineering](../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) — rests-on: the medium-sharing argument behind treating law as an eligible source
- [Instruction specificity should match loading frequency](../notes/instruction-specificity-should-match-loading-frequency.md) — see-also: an example of a first-principles adoption the gate references
- [Directory-scoped types are cheaper than global types](../notes/directory-scoped-types-are-cheaper-than-global-types.md) — see-also: a first-principles adoption derived from the absent import mechanism
- [Thalo](../agent-memory-systems/reviews/thalo.md) — evidenced-by: independent convergence on compiler-like tooling for knowledge management
- [Ars Contexta](../agent-memory-systems/reviews/arscontexta.md) — evidenced-by: the cognitive-science alternative the policy acknowledges but does not adopt wholesale
- [constraining](../notes/definitions/constraining.md) — defined-in: the term for narrowing an artifact's interpretation space
