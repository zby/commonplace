---
description: "SEI's ATAM evaluates one architecture against prioritized quality-attribute scenarios and records risks, assumption-bound non-risks, sensitivity points and tradeoff points; precedent for evidence-bearing decision maps"
source: https://www.sei.cmu.edu/documents/629/2000_005_001_13706.pdf
captured: "2026-10-28"
capture: pdftotext
capture_scope: full-source
genre: practitioner-report
snapshot_sha256: 65204765b229d093f49528b7ffd8984479115061f69a9eda5fcb41f3826d5b9a
ingested: "2026-10-28"
occasion: "Designing a reusable design-space study for Commonplace: an evidence-bearing, revisable map of decision axes, compatibility rules and candidate regions that sits between a problem statement and an implemented ADR."
type: types/ingest-report.md
domains: [architecture-evaluation, quality-attributes, design-space, scenario-analysis]
---

# Ingest: ATAM: Method for Architecture Evaluation

## Classification

This is an SEI technical report (CMU/SEI-2000-TR-004) that defines a method
its authors say they "developed and refined in practice" over three years. It
gives the method's concepts and nine steps, plus one worked evaluation of a
disguised battlefield control system (BCS). It reports no comparative or
controlled evaluation, so it reads as a practitioner method report rather than
a scientific paper. That is why there is no contribution assessment section.
Author: Rick Kazman, Mark Klein and Paul Clements of the Software Engineering
Institute. They are the originators of SAAM, ATAM and attribute-based
architectural styles (ABASs), so they have a stake in the method's framing.

## Summary

The Architecture Tradeoff Analysis Method (ATAM) checks the consequences of
architectural decisions against quality-attribute requirements before
implementation. It is a risk-identification method, not a predictor of quality
values. Vague "-ilities" are turned into stakeholder scenarios with a stimulus,
an environment and a measurable response. There are three kinds: use-case,
growth and exploratory (stress) scenarios. Scenarios are organized in a utility
tree, prioritized High/Medium/Low on two axes (importance and perceived risk),
and then compared with a separate scenario list brainstormed and voted on by
the wider stakeholders. The architect traces the top scenarios through the
architectural approaches, while evaluators ask attribute-specific questions
taken from quality-attribute characterizations and ABASs. The method records
four outputs. Risks are problematic or unmade decisions. Non-risks are sound
decisions that hold only while their stated assumptions hold. Sensitivity
points are properties that are critical to one response. Tradeoff points are
properties that are sensitivity points for more than one attribute. Each risk
or non-risk is stored as decision, response and rationale. Step 8 re-runs the
analysis with the brainstormed scenarios as test cases. If it finds new
information, the report treats that as a failure of the earlier utility-tree
work and loops back. In the BCS case, two parameters (the numbers of
acknowledging and passive backups) controlled a performance/availability
tradeoff over a shared 9600-baud channel. Timing, switchover and availability
requirements were missing from a specification that had been "frozen" for two
years. A targeting vulnerability came to light, by the authors' account, only
because several attributes were analysed at once.

## Quotes

No source quotes have been retained yet.

## Connections Found

The KB had no earlier treatment of ATAM. For the occasion, the source's role
is **established precedent for a decision map whose entries carry evidence**:
it records decisions, the parameters that responses depend on, the parameters
where attributes conflict, and the assumptions under which each judgement
holds. It evaluates one existing architecture, though, not a space of
candidates.

For the general KB, it is independent practice evidence for three notes. It
supports [elicitation requires maintained question-generation
systems](../theory/elicitation-requires-maintained-question-generation-systems.md)
(is-evidence-for). ATAM elicits scenarios from each stakeholder perspective,
codifies attribute-specific question sets from characterizations and ABASs (a
domain checklist), and uses exploratory scenarios as adversarial probes. It has
no loop for maintaining those questions and no data on what they miss. It
supports [use tests a decomposition locally; retained rationale is what makes
transfer
testable](../theory/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md)
(is-evidence-for). A non-risk must be re-justified when its assumptions change,
which is retained rationale whose antecedents make a later change testable. It
supports [brainstorming: maintainability oracles for agentic
development](../theory/brainstorming-maintainability-oracles-for-agentic-development.md)
(is-evidence-for). ATAM's modifiability scenarios state maintainability as
person-effort budgets for named future changes. Those judgements are
qualitative and predictive, not calibrated oracle data.

It compares with [scenario decomposition drives
architecture](../theory/scenario-decomposition-drives-architecture.md) on the
axis of scenarios as the unit that turns vague architectural goals into
checkable requirements. ATAM uses them to evaluate a design, and the note uses
them to derive one. It compares with [changing requirements conflate genuine
change with disambiguation
failure](../theory/changing-requirements-conflate-genuine-change-with-disambiguation.md)
on concretizing underspecified requirements early versus bounding late
discovery. The BCS findings were absent requirements more than competing
interpretations, so the source does not test the note's two-way split. It
compares with [Parnas
1972](./parnas-1972-criteria-decomposing-systems-modules.ingest.md): both
judge a design against anticipated changes before any outcomes exist. Parnas
does this in a single worked comparison, and ATAM makes it a repeatable,
facilitated, multi-attribute procedure. Neither measures downstream costs.

For the design-space study, ATAM compares with [first-principles analysis
maps a design space before selecting within
it](../theory/first-principles-analysis-maps-design-space-before-selection.md):
it evaluates a single position, so it shows what evaluation can miss when no
map of rival positions precedes it. Two sources ingested for the same study
supply what ATAM lacks. [Ritchey's General Morphological
Analysis](./ritchey-general-morphological-analysis.ingest.md) (compares-with)
generates and prunes the candidate regions that ATAM assumes already exist.
[Lane 1990](./lane-1990-design-spaces-and-rules.ingest.md) (compares-with),
from the same SEI lineage, attaches weighted rules to a design space and tests
them against held-out systems, the outcome check this report does not attempt.
ATAM in turn supplies the record form both lack: tradeoff points with written
reasoning and the assumptions that would reopen them.

Every one of these edges shows that the practice exists. None shows that it
works.

## Extractable Value

1. **Sensitivity and tradeoff points as the typed core of an axis map** --
   ATAM separates a parameter that one response depends on (a sensitivity
   point) from a parameter that is a sensitivity point for several attributes
   in opposite directions (a tradeoff point). The BCS case writes these down
   as functions of named parameters, for example QA = g(n, m) and QP = h(n, m,
   CO). A design-space study could adopt this distinction directly. Decision
   axes would carry the responses they are sensitive to, and a "compatibility
   rule" would be stated as a recorded tradeoff point with its reasoning, not
   as a bare incompatible pair. This bears on the occasion's axes and rules. It
   does not cover candidate regions. [quick-win]
2. **Assumption-bound non-risks as the revisability mechanism** -- Each risk
   and non-risk is recorded as decision, quality response and rationale. A
   non-risk stays valid only while its stated assumptions hold, and must be
   re-justified when they change. This gives a design-space study a concrete
   way to be revisable: each region or rule carries the assumptions that would
   reopen it. It is the same mechanism as the use-tests/rationale note, found
   in independent practice. [quick-win]
3. **Unmade decisions are first-class entries** -- ATAM counts "we haven't
   made that decision yet" as a risk and flags it, even though no component
   exists to name as a sensitivity point. A map that sits before an ADR needs
   this: open axes should appear as recorded, prioritized gaps, not as
   omissions. [quick-win]
4. **Two-route elicitation with a reconciliation check and a test step** --
   The architect-led utility tree (top-down) and the wider stakeholders'
   brainstormed scenarios (bottom-up) are compared, and any disagreement must
   be reconciled or explained. Step 8 then re-runs the analysis on the
   brainstormed scenarios as test cases. If it surfaces new information, the
   earlier steps are redone. For a design-space study, this gives a
   falsification check on whether the axes and priorities are complete: scenarios
   produced independently should map onto existing axes without new findings.
   [experiment]
5. **Two-dimension coarse prioritization** -- Utility-tree leaves are ranked
   on importance and on perceived difficulty or risk. The authors report that
   stakeholders could not reliably make distinctions finer than H/M/L. That is
   a practitioner observation, not a measured result, but it is a sensible
   default for prioritizing axes or scenarios without inventing precision.
   [quick-win]
6. **Scenario-relative quality as shared precedent** -- Use-case, growth and
   exploratory scenarios with stimulus/response turn qualities that have no
   operational meaning into checkable cases. The report calls statements like
   "the architecture shall be modifiable and robust" not refutable. ATAM is the
   established precedent that the scenario-decomposition, elicitation and
   maintainability-oracle notes share. Whether that common thread is a single
   mechanism or only a shared vocabulary is still open. [deep-dive]
7. **Single-attribute analysis hides cross-attribute flaws** -- In the BCS
   case, the contractor raised no performance or availability scenarios. The
   decisive tradeoff and the targeting vulnerability appeared only under joint
   analysis. This is one anecdote, but it is a concrete warning for a
   design-space study: axes must be checked against several evaluation
   criteria together, not one at a time. [just-a-reference]

## Limitations (our opinion)

The evidence is a method description written by the method's designers, plus
one disguised case that was altered "for pedagogical reasons". The report does
not say how many evaluations were run, does not report failed or
inconclusive ATAMs, and does not compare against unstructured expert review.
Yet the authors cite repeatability and effectiveness as the reason for having a
method. The claims of repeatability and of finding critical risks are therefore
asserted, not demonstrated. The connections above show the practice exists, not
that it works.

The BCS case does not isolate what made the difference. The key findings came
from back-of-the-envelope performance and availability models built by
evaluators with real-time analysis expertise (RMA, queuing). A simpler account,
that an expert modeller looking at a shared low-bandwidth channel would find
the tradeoff with or without ATAM's steps, is not ruled out. The authors call
any such method garbage-in, garbage-out and dependent on stakeholder
participation and documentation quality. In the case itself, the Phase 1
documentation was too thin to analyse.

For the occasion, the main boundary is that ATAM evaluates **one** proposed
architecture. Alternatives appear only as mitigation suggestions after the
evaluation, and the BCS's three backup options were handed over without being
modeled. ATAM therefore gives no method for enumerating candidate regions,
pruning combinations, or comparing alternatives. Sensitivity and tradeoff
points are found through the architect's chosen approaches, so axes the
architect never considered surface only if a scenario happens to stress them.
Those parts of a design-space study need another source. The report's quality
attribute characterizations also cover only performance, modifiability and
availability, with usability and security described as work in progress.

## Recommended Next Action

In the Commonplace design-space study's draft schema, model each recorded rule
on ATAM's outputs. Represent an axis's dependencies as sensitivity points,
represent compatibility rules as tradeoff points with written reasoning, store
judgements as assumption-bound risk or non-risk records, and list open axes as
unmade-decision risks. Note explicitly that candidate-region enumeration needs
a source other than ATAM.
