---
description: "Retire the codification criterion's ambiguous phrase; symbolic membership depends on a governing semantic reference, separately from opacity and task adequacy"
type: reference/types/adr.md
status: accepted
---

# 124-Retire unique operational semantics as the form criterion

**Status:** accepted
**Date:** 2026-11-02

## Context

The phrase “unique operational semantics” conflates a programming-language
term with a criterion for classifying content. The associated conjecture—that
an artifact's language admits a formal semantics—does not distinguish an
implementation's behavior from the semantics its users hold it to. A compiler
and a frozen model both admit formal descriptions of their computation. Such
a description includes implementation defects; it does not by itself supply
a governing reference for C or English.

The practical distinction is whether users hold consumers to a reference that
settles what the artifact permits. Inspection cost and success at the intended
task are further questions, not membership tests.

## Decision

Retire **unique operational semantics** from current Commonplace vocabulary.
Use the criterion in [representational form](../../theory/definitions/representational-form.md):
localized content is symbolic under a consumption path when its consequences
are fixed by the reference of a language that has a formal semantics or is
close to one. Here “close” means users hold consumers to a standard or
implementation from which a formal semantics could be derived. Short glosses
may say “held to a semantic reference” when the definition supplies that
qualification.

[Codification](../../theory/definitions/codification.md) names the move into
symbolic form, not a separate criterion. The move may rewrite the artifact or
adopt a consumer as the reference for an operation. Mere pinning or repeatability
is insufficient. Adopting a model package does not make it the reference for
English, establish task adequacy, or make its rules affordable to inspect.

Ask localization first and assigned consequences only for localized content.
Keep opacity relative to a consumption path, behavior or change, and inspection
budget. Preserve the distinctions between specified behavior, implementation
conformance, and requirement adequacy.

## Considered alternatives

**Retain the phrase with a narrower gloss.** Rejected because the
programming-language sense remains distinct and the formalizability conjecture
alone fails to select a governing reference. Renaming only the phrase would
leave that conceptual error intact.

**Exclude prompts or opaque references from symbolic form.** Rejected because
surface syntax and inspection difficulty do not decide whether a system has
adopted a mechanically specified reference. Opacity changes the available
checks, not membership.

**Treat every fixed consumer as a reference.** Rejected because a formal
account of an implementation's behavior does not establish its authority over
a language. Users must adopt it or hold it to another governing reference.

## Consequences

Authors and reviewers consume the revised definitions through the root
vocabulary links, theory arguments, tag navigation and the vocabulary collision
ledger. Those natural-language instructions constrain classification and
writing; no validator computes semantic membership. The ledger retains the
external programming-language and measurement senses without using them as
the Commonplace criterion.

Conformance tests can reveal disagreements against a reference but do not prove
its adequacy or correctness outside tested cases. An adopted model can conform
exactly while failing its task. Independent review remains necessary after
substantive definition changes; previous freshness records do not attest to the
new text.

This decision governs Commonplace's current technical vocabulary. It does not
rename the external discipline's operational semantics, alter quoted sources
or frozen historical evidence, assert that all natural language is
unformalizable, or prescribe when a project should adopt a model as its
reference.
