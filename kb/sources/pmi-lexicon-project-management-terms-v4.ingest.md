---
description: "PMI defines progressive elaboration and rolling wave planning, anchoring Commonplace's information-timed planning claims while separating the core terms from broader methods."
source: "https://web.archive.org/web/20251208103054id_/https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf?rev=447328d841c249af985d14177ddd5f95"
canonical_source: "https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf?rev=447328d841c249af985d14177ddd5f95"
captured: "2026-08-28"
capture: pdftotext
capture_scope: full-source
archive_timestamp: "20251208103054"
capture_note: "Live canonical PDF returned HTTP 403; this complete replay contains Version 4.0, while PMI's current record identifies Version 5.0."
genre: reference-lexicon
snapshot_sha256: 9d080714b8d19af34088aa97d6368dc62d24062c90ea7487ed94021621eb0a27
ingested: "2026-08-28"
type: kb/sources/types/ingest-report.md
domains: [project-management, planning, context-engineering]
---

# Ingest: PMI Lexicon of Project Management Terms, Version 4.0

## Classification

This is a reference lexicon: it supplies concise, cross-referenced definitions rather than an argument, implementation guide, or empirical evaluation.
Author: Project Management Institute, the professional association that publishes and maintains the lexicon.

## Summary

The 2024 Version 4.0 lexicon defines project-management vocabulary across predictive, adaptive, and hybrid work. Its main value to Commonplace is the paired distinction between *progressive elaboration*, the iterative increase of plan detail as information and estimate accuracy improve, and *rolling wave planning*, the technique of planning near-term work in detail while leaving future work at a higher level. Read it when a methodology claim needs a compact PMI terminology anchor; it does not show that either practice improves outcomes or prescribe a complete planning method.

## Quotes

- **Source extract (verbatim):** progressive elaboration. The iterative process of increasing the level of detail in a project management plan as greater amounts of information and more accurate estimates become available.
  - **Source location:** PMI Lexicon of Project Management Terms, Version 4.0, p. 18, “progressive elaboration” entry
- **Source extract (verbatim):** rolling wave planning. An iterative planning technique in which the work to be accomplished in the near term is planned in detail, while the work in the future is planned at a higher level.
  - **Source location:** PMI Lexicon of Project Management Terms, Version 4.0, p. 24, “rolling wave planning” entry

## Connections Found

The lexicon is a terminology anchor for the information-timing rule in [An author should fix what the executor can't determine, not what it will](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md): plan detail increases as better information becomes available, with near-term work specified more closely than future work. It also provides scoped evidence for the planning consequence in [Codifying predictable choices leaves agents with less predictable work](../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md), but not for that note's broader claim about which choices to codify. Compared with [Manage Innovation Programs With a Rolling Wave](githens-manage-innovation-programs-rolling-wave.ingest.md), PMI supplies the minimal term and its relation to progressive elaboration; Githens adds a larger prescriptive package of relearning points, gates, baselines, and approvals.

## Extractable Value

1. **Separate the general process from the planning technique** -- Progressive elaboration names increasing detail as information and estimates improve; rolling wave planning names the near-term-detail/future-level planning pattern. This distinction can prevent a local implementation from being mistaken for the definition itself. [quick-win]
2. **Ground information-timed specification in established planning vocabulary** -- The paired definitions give the executor-detail note a recognized project-management instance of delaying detail that depends on information expected later. [quick-win]
3. **Bound the support for codification claims** -- The lexicon corroborates deferring future planning detail, but it says nothing about how an agent system should divide predictable from unpredictable work. It is useful as narrow corroboration, not as support for the wider theory. [just-a-reference]
4. **Calibrate the Githens method against a minimal baseline** -- Comparing the lexicon with the practitioner report separates rolling wave planning's defining information horizon from optional governance mechanisms such as gates and approvals. [quick-win]

## Limitations (our opinion)

This lexicon standardizes PMI's vocabulary; it does not argue for the definitions, report adoption beyond PMI, test planning outcomes, or identify failure conditions. The paired entries also do not say how to decide that information is accurate enough to justify more detail, so they cannot by themselves operationalize the method. PMI's institutional authorship is a strong signal for PMI usage, not proof of universal terminology. Finally, this retained observation is Version 4.0 while the capture metadata identifies Version 5.0 as current, so it should anchor the 2024 wording rather than be presented as PMI's latest formulation.

## Recommended Next Action

Update [An author should fix what the executor can't determine, not what it will](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) to cite this ingest for its project-planning example and state the bounded distinction between progressive elaboration and rolling wave planning.

---

Relevant Notes:

- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../notes/productive-deferral-requires-option-evidence-and-convergence.md) — abstracted-from: progressive elaboration and rolling-wave planning supply the intentionally coarse future-detail case
