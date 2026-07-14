---
description: "Qualified good-regulator theorem vocabulary for models, goals, disturbances, and optimal regulation"
source_snapshot: "conant-ashby-every-good-regulator-1970.md"
ingested: "2026-07-14"
type: kb/sources/types/ingest-report.md
domains: [regulation, models, cybernetics]
---

# Ingest: Every Good Regulator of a System Must Be a Model of That System

Source: [conant-ashby-every-good-regulator-1970.md](./conant-ashby-every-good-regulator-1970.md)
Captured: 2026-07-14
From: https://pespmc1.vub.ac.be/books/Conant_Ashby.pdf

## Classification

Genre: scientific-paper -- a formal theorem paper defining regulation and proving a model relation under explicit probabilistic/entropy assumptions.
Domains: regulation, models, cybernetics
Author: Roger C. Conant and W. Ross Ashby are primary cybernetics sources; the theorem is frequently quoted more broadly than its proof permits.

## Summary

Conant and Ashby formalize regulation using possible outcomes Z, acceptable outcomes G, regulator events R, reguland events S, and disturbances D (journal pp. 90-91; PDF pp. 2-3). They define successful regulation as minimizing outcome entropy H(Z). Given a fixed distribution over S, a regulator behavior p(R|S), a unique optimal outcome distribution, and the stated mapping assumptions, the **simplest optimal regulator** produces events related to S by a mapping h:S→R (pp. 94-96; PDF pp. 6-8). Hence the best simple regulator is a model in the specific sense that its actions are mapped versions of the reguland's actions—not necessarily a detailed internal simulation.

## Connections Found

This is constrained cybernetic background for [Reflective system](../notes/definitions/reflective-system.md). It does not define actionable theory or reflection.

## Inherited Vocabulary

### Exact terminology and definitions

- **Good regulator:** R is good for goal G when, for all disturbance values D, R relates to S so their interaction yields an outcome in G (journal p. 91; PDF p. 3).
- **Successful regulation:** H(Z), the entropy of possible outcomes, is minimal (journal p. 92; PDF p. 4).
- **Optimal regulator:** produces regulatory events so that H(Z) is minimal; the **simplest optimal regulator** maps reguland events S into regulator events R via h:S→R (journal pp. 94-95; PDF pp. 6-7).
- **Model:** in the theorem's operative sense, R's actions are S's actions as seen through mapping h—not any representation colloquially called a model (journal p. 95; PDF p. 7).

### Necessary conditions versus illustrative features

Modelhood is compulsory only for the simplest optimal regulators within the proof's class. Equally optimal but unnecessarily complex regulators need not be models in that minimal sense (journal p. 96; PDF p. 8). Fixed/slowly changing p(S), the R×S→Z outcome mapping, and the uniqueness simplification matter. Airport control, hunters, brains, and organisms are illustrations, not proof premises.

### Assumed system boundary and people as components

The formal boundary contains disturbances D, reguland/system events S, regulator events R, outcomes Z, goal set G, and their mappings. A human or brain may instantiate the regulator H/R, as in the hunter example, so people can participate, but the theorem is extensional over events and does not require human agency.

### Causal structure

Disturbances map to reguland events (D→S) and information reaches regulatory events (D→R directly or through S); regulator and reguland jointly map to outcomes (S×R→Z). Goal success constrains which mappings count as regulatory. The theorem then selects a simplest optimal S→R mapping (pp. 90-96).

### Constraints for later Commonplace notes

Never abbreviate this paper to “every effective system has a self-model.” Preserve **simplest**, **optimal**, the explicit reguland/regulator split, goal/outcome criterion, and mapping sense of model. Do not use it to define actionable theory or reflection, and do not classify Commonplace from it.

## Extractable Value

1. **Qualified model requirement** -- supplies exact assumptions that popular summaries omit. [quick-win]
2. **Goal-relative boundary** -- regulation cannot be identified without outcomes, a goal criterion, disturbances, regulator, and reguland. [deep-dive]
3. **Model need not be a simulation** -- the operative relation is a mapping between event sets. [quick-win]
4. **Human-neutral theorem** -- people may realize components, but nothing in the proof depends on personhood. [just-a-reference]

## Limitations (our opinion)

The theorem uses entropy-minimizing regulation and simplifying assumptions that do not directly describe plural, changing Commonplace goals or human approval. It establishes neither causal self-representation nor the capacity to inspect or modify that representation.

## Recommended Next Action

File this as supporting background and cite it later only where all theorem qualifiers can be stated locally.
