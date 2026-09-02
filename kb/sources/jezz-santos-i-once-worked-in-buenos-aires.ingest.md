---
description: "A program participant reports Microsoft's Software Factories retreat, NuPattern's maintenance collapse, and Aspen's contrasting longevity."
source: https://www.linkedin.com/pulse/i-once-worked-buenos-aires-jezz-santos
captured: "2026-09-02"
capture: trafilatura
capture_scope: full-source
genre: practitioner-report
snapshot_sha256: 96aad11d57981a8154de7c01c1d378f965eb916f19990eee4d26fd99efd6045c
ingested: "2026-09-02"
occasion: "for kb/work/factory-theory-restart we need to ground the failure claim - snapshot and ingest a retrospective"
type: kb/sources/types/ingest-report.md
domains: [software-factories, product-strategy, tool-maintenance]
---

# Ingest: I ONCE WORKED in Buenos Aires

## Classification

This is a first-person practitioner retrospective: Jezz Santos recounts the Aspen program and the VSPAT/NuPattern product line from his later perspective rather than presenting a contemporary program record or controlled evaluation. Author: Santos identifies himself as the Aspen participant who became product manager and program lead for the tooling, giving him direct operational knowledge but also a strong stake in the interpretation.

## Summary

Santos recounts how Raytheon's Aspen program adopted Microsoft's Software Factories approach, how Microsoft's Visual Studio organization abandoned that strategy in favor of UML tooling, and how a separate team built VSPAT and later released it as the open-source NuPattern project. He attributes NuPattern's eventual end to deep Visual Studio coupling, repeated breaking platform changes, and maintenance demands that exceeded a small community's resources. He separately describes Aspen as a successful, long-lived program, so the retrospective distinguishes the failure of Microsoft's platform strategy and its successor tooling from the outcome of a customer deployment built around related ideas.

## Quotes

- **Source extract (verbatim):** The Visual Studio team had suddenly decided to pivot and go the way of UML, and effectively abandon the Software Factories strategy that we had predicated our program on.
  - **Source location:** “Software Factories” section
- **Source extract (verbatim):** In the end, this coupling became totally unmanageable for a small team like us given the resources we had in the open source community, as other small VS partners have learned the hard way. As a result, the NuPattern product died a slow death, and is no longer supported in any recent version of Visual Studio today.
  - **Source location:** “Free and open” section
- **Source extract (verbatim):** The Aspen program however, was a great success and lived on for many years after, led by John, long after I had to disengage.
  - **Source location:** “Free and open” section

## Connections Found

The retrospective is an outcome-side anchor and limitation for the KB's account of [software factories as family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md). Compared with the earlier [2003 program account](greenfield-short-software-factories-oopsla-2003.ingest.md) and [mature 2007 account](greenfield-mass-customizing-software-factories-2007.ingest.md), it reports Microsoft's organizational retreat and NuPattern's later maintenance collapse while preserving Aspen as a claimed counterexample to categorical initiative-wide failure. Its account of repeated host-platform breakage is also a bounded practitioner case for the external binding and revision-cost mechanism in [A theory's prototype standing is its expected revision cost](../notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md).

## Extractable Value

1. **Narrow the failure claim by unit of analysis.** The retrospective supports saying that Microsoft abandoned its Visual Studio Software Factories strategy and that NuPattern eventually became unmaintainable; it does not support saying that every software-factory deployment failed, because Santos reports Aspen as a long-lived success. [quick-win]
2. **Separate organizational withdrawal from technical invalidation.** The stated causes include a Visual Studio strategy pivot, internal ownership boundaries, and the costs of sustaining a deeply integrated extension, so discontinuation alone does not test whether family-scoped production machinery worked in its deployment domain. [deep-dive]
3. **Use host-platform coupling as a concrete revision-cost case.** Successive breaking Visual Studio changes repeatedly forced re-engineering until the small open-source team could no longer maintain NuPattern, illustrating how external binding can dominate a prototype's survivability. [quick-win]
4. **Preserve the distinction between factory construction and knowledge acquisition.** Santos describes people discovering customer problems, selecting abstractions, building templates, and revising the meta-tool through Aspen feedback; the tooling codified and applied the resulting patterns but did not itself discover them. [deep-dive]
5. **Treat the retrospective as a historical lead for stronger records.** Its first-person timeline identifies specific organizations, product names, and transitions that can guide later searches for contemporary announcements, repositories, or program evidence. [just-a-reference]

## Limitations (our opinion)

This is one participant's retrospective written roughly a decade after the events. It supplies no contemporary decision records, adoption data, cost figures, comparative baseline, or independent evidence for Aspen's success, Microsoft's motives, or NuPattern's cause of death. The account also combines several levels of outcome—corporate strategy, tooling product, open-source maintenance, and customer capability-building—so treating them as one experiment would erase the central distinction the source itself reveals. Deep platform coupling is a plausible explanation for NuPattern's maintenance collapse, but the narrative does not isolate it from loss of sponsorship, community size, product demand, or other causes.

## Recommended Next Action

Revise the failure claim in the factory-theory restart workshop to name the failed unit explicitly: Microsoft's Visual Studio Software Factories strategy was abandoned and NuPattern later became unmaintainable, while Aspen's reported longevity prevents an initiative-wide failure claim.
