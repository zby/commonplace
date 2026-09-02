---
description: "Industry study finds MDE succeeds mainly in narrow, customized domains while organization-wide scale-up creates a recurrent failure point"
source: https://eprints.lancs.ac.uk/id/eprint/69765/1/SO_SW_2012_12_0188.R1_Whittle.pdf
captured: "2026-09-02"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 7aa137287871145f89a7dade3e5609f4510775737c8b7ec2318e93c963632579
ingested: "2026-09-02"
occasion: "for kb/work/factory-theory-restart we need to ground the failure claim - snapshot and ingest a retrospective"
type: kb/sources/types/ingest-report.md
domains: [model-driven-engineering, software-factories, organizational-adoption]
---

# Ingest: The State of Practice in Model-Driven Engineering

## Classification

This is a scientific paper reporting an empirical software-engineering study based on a questionnaire of 450 MDE practitioners, 22 semi-structured interviews across 17 companies and nine sectors, and on-site observations. Author: Jon Whittle, John Hutchinson, and Mark Rouncefield were software-engineering researchers affiliated with Lancaster University; they describe their sampling and methods and point to separate publications for methodological detail.

## Summary

The study argues that model-driven engineering (MDE) was more widespread in industry than critics assumed, but its successful form was usually bounded: practitioners developed customized, often small domain-specific languages for narrow domains and generated parts of systems rather than whole systems. The authors report that adoption depended at least as much on organizational and social conditions as on technical capability, with grassroots introduction, developer support, domain expertise, and a business driver associated with success. Productivity from code generation alone was rarely decisive; respondents instead valued the explicit architectural structure MDE helped them build. The paper identifies the transition from local initiatives to organization-wide adoption as a common failure point.

## Quotes

- **Source extract (verbatim):** Findings suggest that MDE may be more widespread than commonly believed, but developers rarely use it to generate whole systems; rather, they apply it to develop key parts of a system often using domain-specific modeling languages developed specifically for the purpose.
  - **Source location:** Abstract, manuscript page 1
- **Source extract (verbatim):** Interview data shows that it is common to develop small domain-specific languages (DSLs) for narrow, well-understood domains.
  - **Source location:** “MDE Use is Widespread,” manuscript page 2
- **Source extract (verbatim):** 4. Most Projects Fail at Scale-Up. As noted above, MDE may work best when driven from the ground-up. A natural point, of course, arises when an organization wishes to unite such grassroots efforts and effect organizational change. This is, not surprisingly, where problems start to arise and managers should be careful to allocate appropriate resources during this transition phase.
  - **Source location:** “Tips of the Trade,” item 4, manuscript page 7

## Connections Found

The source is an empirical limitation and outcome anchor for the current software-factory theory. Its evidence that effective MDE was usually narrow, customized, and partial supports [A software factory is family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md), while its contrast between bounded success and organization-wide scale-up failure supports the scope discipline in [Universal software factory needs a declared universality axis](../notes/universal-software-factory-needs-a-declared-universality-axis.md). Compared with [Mass Customizing Solutions with Software Development Factories](./greenfield-mass-customizing-software-factories-2007.ingest.md), it supplies independent industry evidence about where the proposed machinery worked and where adoption broke down. It does not establish that the software-factory vision failed categorically or explain any particular institution's retreat.

## Extractable Value

1. **Narrow the factory failure claim to scale-up failure.** The paper supports a recurring breakdown when organizations tried to unite grassroots MDE efforts and impose organization-wide change; it does not support the stronger claim that family-scoped modeling or the whole software-factory program failed. [quick-win]
2. **Treat family scope as an observed success boundary, not only a proposed ontology.** Successful practice centered on small, customized DSLs for narrow, well-understood domains and on generating selected system parts, adding empirical support to the KB's family-scoped factory account. [quick-win]
3. **Separate bounded technical efficacy from organizational adoption reach.** A local MDE technique could work while wider rollout failed because developer buy-in, resources, incentives, training, and management structure changed the operating conditions. [deep-dive]
4. **Use the study as a counterweight to programmatic software-factory sources.** Greenfield describes the intended family machinery; this paper reports broader industry practice and constrains extrapolation from architectural ambition to whole-system or organization-wide success. [just-a-reference]

## Limitations (our opinion)

The survey recruited practitioners who already had industrial MDE experience, and the interview group was mostly positive about MDE, so the study cannot estimate MDE prevalence or failure rates across the software industry. Its observational questionnaire and interview evidence identifies associations and practitioner explanations, not controlled causal effects. The headline that most projects fail at scale-up is not accompanied here by a denominator or a separately reported scale-up outcome measure, so it should ground a qualitative recurring-failure claim rather than a quantitative rate. The article also summarizes methods whose fuller details appear in separate publications, and its 2014 practice snapshot does not establish current adoption patterns. Finally, it studies MDE across many organizations; it cannot by itself establish why Microsoft's software-factory strategy, a particular tool, or a particular project ended.

## Recommended Next Action

Revise the failure claim in the factory-theory-restart workshop to say that organization-wide MDE scale-up was a recurring failure point, not that the software-factory vision failed outright, and ground that narrower statement in this ingest.
