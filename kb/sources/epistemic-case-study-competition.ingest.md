---
description: "FLF's competition brief supplies an external task profile for testing provenance, argument structure, belief assessment, interoperability, and reuse in agent-operated KBs."
source: https://www.lesswrong.com/posts/frizRHnA6AZpJSDqw/lab-leaks-black-holes-and-eggs-epistemic-case-study
captured: "2026-07-12"
capture: web-fetch
genre: official-statement
snapshot_sha256: 2df87772d3c1beea51ac1045af144f775160e3519b0d58d9d7f0ebde6eab4b34
ingested: "2026-08-24"
type: kb/sources/types/ingest-report.md
domains: [epistemic-investigation, knowledge-bases, evaluation, interoperability]
---

# Ingest: Epistemic Case Study Competition

## Classification

This is an official competition brief: it states the sponsor's problem framing, requirements, cases, judging criteria, prize terms, and intended use of submissions. Author: Oliver Sourbut and Josh Jacobson write on behalf of the Future of Life Foundation, which is authoritative about its own competition and desired evaluation profile but has an institutional interest in presenting the agenda as important and tractable.

## Summary

The brief asks for AI-assisted workflows, tools, protocols, comparisons, or critiques that improve difficult epistemic investigations across three deliberately different cases. It decomposes the work into ingestion, structure, and assessment; requires provenance, claim and argument relationships, uncertainty and crux handling, missing-perspective detection, and change over time; and judges whether outputs help users reason, generalize, scale, interoperate without losing nuance, and support later work. For Commonplace, its main value is an external requirements and stress-test profile rather than evidence that this decomposition is complete or effective.

## Claims

No claims have been grounded yet.
## Connections Found

The brief is an external requirements anchor for evaluating Commonplace as an instrument across contested, closed, and open-ended investigations. Its ingestion requirements rest on the transformation described in [Raw accumulation does not create usable memory](../notes/raw-accumulation-does-not-create-usable-memory.md), while its assessment layer depends on keeping reasoning production distinct from [reasoning evaluation](../notes/reasoning-production-is-not-reasoning-evaluation.md) and tracking warrant only at the granularity evidence licenses. Its interoperability requirement also sharpens the distinction between shared exchange authority and a universal content taxonomy in [A universal knowledge framework demotes content taxonomies to defaults](../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md). The brief's use of “compounding” is best treated as an agenda claim: [Improvements can accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md) requires separate evidence for reuse, transfer, and a causal improvement to later improvement episodes.

## Extractable Value

1. **External evaluation profile** -- The COVID, black-hole, and eggs cases vary disagreement, closure, expertise, and question definition, giving [Commonplace as an instrument](../reference/commonplace-as-an-instrument.md) a concrete outside-system task profile rather than another internal structural check. [experiment]
2. **Three-layer capability matrix** -- Ingestion, structure, and assessment provide a useful top-level comparison frame, but the KB can make it more diagnostic by crossing them with provenance unit, support model, uncertainty representation, authority, update lifecycle, interoperability boundary, and available oracle. [deep-dive]
3. **Assessment requirements beyond polished synthesis** -- Correlated-evidence detection, rhetorical-versus-evidential weight, crux discovery, missing-perspective search, and “performed settling” are specific probes for whether an agent evaluates reasoning rather than merely producing it. [experiment]
4. **Interoperability-without-flattening test** -- The brief identifies a practical boundary condition for portable artifacts: shared structure must preserve differing scopes, caveats, uncertainty estimates, emphases, and evolution over time rather than forcing all content into one taxonomy. [deep-dive]
5. **Separate measurements for travel, transfer, and compounding** -- A reusable artifact can move between investigators, improve a later task, or make a later improvement episode more productive; the brief motivates testing these as distinct outcomes. [quick-win]

## Limitations (our opinion)

The brief is authoritative about FLF's intentions, not about whether its ingestion-structure-assessment decomposition is sufficient or whether the proposed tasks predict reliable performance elsewhere. It supplies no benchmark protocol, baseline, adjudication procedure, or result demonstrating that any workflow improves belief accuracy. Its examples of existing systems and its claims about generality and compounding are agenda-setting assertions from a sponsor seeking submissions, and alternative explanations such as better interfaces, more reviewer time, or domain expertise remain unseparated. The capture is also a point-in-time competition announcement whose named deadline and prize details should not be treated as current status.

## Recommended Next Action

Add a single external-task-profile evaluation subsection to [Commonplace as an instrument](../reference/commonplace-as-an-instrument.md) that maps current Commonplace capabilities and unresolved evidence gaps against the brief's ingestion, structure, and assessment requirements for the three case profiles.
