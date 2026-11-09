---
description: "A stalled agent-memory project illustrates how formal conflict checks leave prose-to-symbol identity judgments unresolved, without establishing a general impossibility."
source: https://arbustoemchamas.substack.com/p/i-naively-tried-vibe-coding-a-memory
captured: "2026-11-08"
capture: trafilatura
capture_scope: full-source
genre: practitioner-report
snapshot_sha256: 6fe7130a1ffe8727de955bb51665e4701e9591ea88f119f47456ef9b3da947da
ingested: "2026-11-08"
type: types/ingest-report.md
domains: [agent-memory, contradiction-detection, proposition-canonicalization, formal-verification]
learning_claims: true
---

# Ingest: A stalled agent-memory contradiction checker

## Classification

A first-person account of building a memory tool and failing to deliver its intended contradiction detector. The embedded model explanations and reading list are part of the account, not independently established research findings.
Author: Arbusto Em Chamas, a self-described newcomer to agent tooling who directed an agent-written implementation and explicitly disclaims systems-design expertise. The author supplies unusually candid failure testimony, but no inspectable implementation or evaluation in this capture.

## Summary

The author reports building a local Rust memory daemon with retained, supersedable facts and fused retrieval, then attempting automatic contradiction detection through a formal reasoning architecture. Despite reported machine-checked subsystem properties, the tool still does not flag contradictions. The proposed diagnosis, developed through conversations with models, is that an answer-set programming (ASP) solver compares formal atoms only after an upstream encoder has decided which prose memories express the same proposition. Merging atoms too eagerly can invent conflicts; leaving equivalent claims separate can prevent matching. The useful contribution is a concrete account of a semantic encoding bottleneck hidden behind working storage, retrieval, and formal machinery. The account does not establish that practical, bounded contradiction detection requires solving a universal philosophical problem.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a bounded practitioner illustration of [Semantic work can be relocated but not eliminated](../theory/semantic-work-can-be-relocated-but-not-eliminated.md): mechanical conflict rules depend on meaning-dependent judgments made during prose-to-atom encoding. Its distinctive value is the reported coexistence of substantial formal machinery and an undelivered semantic function. This is illustrative evidence, not a controlled test of the note's general claim. Storage and formal checks should not be read as evidence that the identity judgment works.

## Learning Claims (our opinion)

The intended mechanism retains extracted facts across sessions, retrieves them for agents, supersedes old commitments without deletion, and proposes a reasoning council in which abduction suggests causes, deduction certifies, and induction learns candidate rules. The source reports storage and classification working, but not the contradiction detector or successful rule learning. On our interpretation, this is a proposed criticism-and-revision mechanism, not demonstrated learning.

Against the [theory-builder definition](../theory/definitions/theory-builder.md), the memory tool has reported **localized content** in prose memories and fact-atoms, although the fidelity of the mapping between them is unresolved. **Consumption** is intended through retrieval into later sessions; working search is reported, but no example shows that changing a stored claim changes an agent's decision. **Content-directed criticism** is an explicit goal, but the desired automatic contradiction process is reported not to work. **Iteration** through retained criticism and revised memories is therefore not demonstrated by the existence of supersession records. The intended persistence is across sessions; actual reuse of criticism over that span is not shown. These gaps leave theory-builder membership for the tool unestablished, and improved capacity for future action remains a separate, untested claim.

Formal atom-level checks would operate downstream of the prose mapping. As in [learning inside a fixed decomposition](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improving a downstream component would not validate a mapping it cannot revise. Here neither the effective revision boundary nor a learning improvement is measured, so the case does not establish an unrepairable representation omission. It also illustrates why separately identifiable records are not enough for [addressable theory](../theory/definitions/addressable-theory.md): their intended content and the consequences assigned by an encoding remain open to criticism. The human-model development process does reconsider its design after failures, but that is distinct from the memory tool autonomously learning from contradictions.

## Extractable Value

1. **Locate the semantic responsibility before trusting formal checks.** The account supplies a concrete example for the existing semantic-work note: a solver's exact atom matching leaves the claim-to-atom judgment upstream. The reusable diagnostic is to ask who makes that judgment and how its errors are checked, not merely whether the solver is sound. [quick-win]
2. **Test the desired function separately from supporting infrastructure.** Working storage, retrieval, supersession, and reported proofs coexisted with failure to deliver contradiction detection. For a memory-system evaluation, paired prose cases with expected conflict judgments would distinguish encoding failures from solver failures; this source motivates that test but supplies no results. [experiment]
3. **Retain the negative engineering episode without its universal conclusion.** The author's stalled project is useful failure testimony against inferring task completion from implementation volume or formal sophistication. It is not evidence that bounded conflict detection is impossible or that agent-assisted coding generally fails. [just-a-reference]

## Limitations (our opinion)

This is one self-reported project, with no code audit, example memory bank, measured conflict precision or recall, comparison system, or reproducible failure trace. The account describes failed work rather than only success, but still selects episodes retrospectively and gives little operational detail about the encoding attempts. It cannot separate a difficult semantic problem from missing integration, unsuitable scope, or an ineffective implementation strategy. The reported Agda proofs are not independently checked, and their exact obligations are unspecified; even accepting them would not establish faithful encoding of prose.

The philosophical diagnosis and much of the bibliography come from model output. The claim that proposition identity has been unsolved since 1892 does not establish an impossibility theorem for this engineering task. Context, time, entity identity, and acceptable error rates could make a bounded conflict detector useful without a universal identity criterion. Conversely, naming proposition identity does not explain every failure in this implementation. Consistent with the semantic-work note, the case locates a plausible unpaid judgment; it does not measure its cost or show that the proposed diagnosis caused the failure. No controlled comparison tests formal encoding against model-judged conflicts or human-reviewed candidates.

## Recommended Next Action

Review `kb/theory/semantic-work-can-be-relocated-but-not-eliminated.md` for adding this ingest as a bounded practitioner example of semantic judgment moving into prose-to-atom encoding.
