---
description: "A large developer survey finds low, informal design-model use, supplying historical diffusion evidence but not a causal account of factory failure"
source: https://gorschek.com/wp-content/uploads/2019/11/GorschekTemperoAngelisModeling20140327.pdf
captured: "2026-09-02"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: a23556c66766c1945d95b68bc2828e3db4304a62af5445c0184877dbc57caa06
ingested: "2026-09-02"
occasion: "for kb/work/factory-theory-restart we need to ground the failure claim - snapshot and ingest a retrospective"
type: kb/sources/types/ingest-report.md
domains: [software-modeling, model-driven-engineering, software-factories]
---

# Ingest: On the use of software design models in software development practice

## Classification

This scientific paper reports a cross-sectional online survey of 3,785 object-oriented software developers, combining a fixed-choice model-use question with coded free-text explanations and demographic association tests.
Author: Tony Gorschek, Ewan Tempero, and Lefteris Angelis were university researchers reporting their own survey design, analysis, and validity assessment.

## Summary

The paper asks how often developers used design models to guide development rather than assuming adoption from studies of modelers. In its 2009 voluntary online sample, 48.6% reported never or rarely using models, 69% used them in less than 25% of cases, and about 11% used them more than 75% of the time. The authors found that use was commonly informal, rarely tool-supported, often not UML, and concentrated on early problem solving and communication rather than maintained development artifacts. They therefore argue that widespread basic modeling, which they treat as a prerequisite for widespread model-driven engineering (MDE), had not been achieved.

## Quotes

- **Source extract (verbatim):** About half of the respondents (48.6%, see Figure 7 and Table 2) never or rarely use design models as a guide for development. Almost 70% of the respon- dents use models in less than 25% of the cases, compared to about 11% that use models more than 75% of the time.
  - **Source location:** Section 4.2, “Extent of Design Model Use (RQ1)”

- **Source extract (verbatim):** However, the widespread use of at least basic modeling is a pre-requisite for the spread of model-drive engineering. Based on our survey, this pre-requisite is not being met.
  - **Source location:** Section 5, “Conclusions”

## Connections Found

This source is a historical population-level limitation on the adoption premise in [A software factory is family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md): Greenfield-style machinery includes model-driven development and maintained family assets, while this survey finds that even ordinary design models were seldom used or maintained. It compares with [Mass Customizing Solutions with Software Development Factories](./greenfield-mass-customizing-software-factories-2007.ingest.md) and extends [Where Is the Proof? — A Review of Experiences from Applying MDE in Industry](./where-is-the-proof-mde-industry.ingest.md) by adding broad, direct evidence about basic-model diffusion. It also corrects any prevalence inference drawn from [The State of Practice in Model-Driven Engineering](./state-of-practice-in-model-driven-engineering.ingest.md), whose MDE-practitioner sample characterizes adopters rather than the developer population.

## Extractable Value

1. **Ground a narrow historical failure claim** -- The survey directly supports the claim that widespread basic-model use, the prerequisite the authors name for MDE diffusion, was not met in their 2009 developer sample; it does not establish that software factories as a whole failed. [quick-win]
2. **Separate diffusion from adopter efficacy** -- The contrast with MDE-practitioner studies shows why success among selected adopters cannot establish population-level uptake. [quick-win]
3. **Treat model maintenance as an adoption boundary** -- Respondents commonly described disposable sketches rather than persistent, tool-supported models, which limits transfer from local modeling utility to factory machinery that depends on maintained formal assets. [deep-dive]
4. **Distinguish communication value from executable production machinery** -- The study preserves a useful role for informal diagrams in joint problem solving while showing that this role need not mature into model-driven automation. [deep-dive]
5. **Reuse the prevalence-first research design** -- Hiding the modeling question inside a broader developer survey reduces modeler-selection bias and offers a general method for testing whether a purported standard practice is actually widespread. [just-a-reference]

## Limitations (our opinion)

The large sample improves precision but does not make the voluntary, snowball-recruited respondents representative of all developers; the sample was limited to object-oriented experience, concentrated in North America and Europe, and observed practice in 2009. Model use was measured by one self-reported frequency question with deliberately broad wording, while explanations, media, and maintenance behavior were inferred from optional free text rather than direct observation. The fixed measurement design can express frequency bands, demographic associations, and coded explanation categories, but it cannot establish causal reasons for low adoption, the quality or effects of the models used, or whether a different tooling and workflow regime would change uptake. The reported associations therefore describe this sample rather than testing the factory decomposition or showing why MDE diffusion was low. Most importantly for the occasion, the paper does not directly study Greenfield-style software factories or agentic factory development, so using it as evidence of general factory failure would exceed its scope.

## Recommended Next Action

In the factory-theory restart, cite this ingest to ground only the scoped historical claim that widespread basic-model use—the prerequisite the authors identify for MDE diffusion—was unmet, and keep any broader software-factory failure claim as a separate inference.
