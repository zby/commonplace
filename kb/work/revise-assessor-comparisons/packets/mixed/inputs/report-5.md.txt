---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/role-in-the-kb-gate.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
criterion: kb/instructions/role-in-the-kb-gate.md
criterion-sha256: 86d5c3082fa3fb82afab97a45faf7c7ae3265ce3a43ae7791051657759ca54bd
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/role
launch: 73a78ce12de84cca9ad16b61921c408e
completed-at: '2026-11-20T18:59:10Z'
findings:
- scope: passage
  quotes:
  - For Commonplace, we choose changes by asking whether they yield more useful and
    better-warranted knowledge work for the human judgment spent, on balance.
  reason: 'SUPPLIED — kb/reference/commonplace-as-an-instrument.md — links to the
    section anchor #what-commonplace-chooses-to-count as the statement of ''what Commonplace
    chooses to count as progress'', the objective against which the KB tests changes.
    The section states that objective in one sentence.'
- scope: passage
  quotes:
  - Automation alone does not answer that question.
  reason: 'DUPLICATED — kb/reference/commonplace-as-an-instrument.md — the dependent
    follows its link with ''Automating a task is not, by itself, a gain.'' The note
    states a narrower point: automation does not answer whether a gain is worth the
    judgment it costs. The dependent''s sentence is the stronger, shorter claim and
    the one its readers use. The note''s version is the more precise one, because
    it ties the point to the judgment cost rather than denying that automation can
    be a gain.'
- scope: passage
  quotes:
  - For Commonplace, we choose changes by asking whether they yield more useful and
    better-warranted knowledge work for the human judgment spent, on balance.
  reason: 'SUPPLIED — kb/reference/commonplace-declared-frame.md — cites the section
    anchor as ''the program objective'', which it distinguishes from a local acceptance
    criterion. The note supplies an identifiable program objective. It also supports
    the distinction: its factory-comparison paragraph says a pass answers a defined
    requirement and an on-balance judgment does not override it.'
- scope: passage
  quotes:
  - For Commonplace, we choose changes by asking whether they yield more useful and
    better-warranted knowledge work for the human judgment spent, on balance.
  reason: PARTLY SUPPLIED — kb/reference/proposals/ablation-baselines-for-the-declared-objective.md
    — the proposal 'tests Commonplace's objective on matched tasks' and, per its description,
    compares work quality and human effort. The note supplies the objective and says
    that evidence supports only some comparisons, which fits a matched-comparison
    design. It does not say what observation would count as 'more useful and better-warranted'
    work. It names 'human judgment spent' where the proposal measures 'human effort'.
    The proposal therefore cannot take its measured quantities from the note's wording.
- scope: passage
  quotes:
  - We choose this objective because we repeatedly have to decide whether a gain is
    worth the judgment it takes to build, operate, and maintain the change.
  reason: SUPPLIED — kb/reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md
    — cites the section anchor for the question 'whether investment in shared machinery
    repays its human cost across kinds of work'. The note's reason for the objective,
    worth weighed against the judgment it takes to build, operate and maintain a change,
    supplies that cost-repayment framing. The dependent says 'human cost' where the
    note says 'judgment'.
- scope: passage
  quotes:
  - A pass answers that defined question; an on-balance judgment does not override
    a binding requirement.
  reason: SUPPLIED — kb/theory/a-better-factory-claim-compares-operative-states.md
    — needs the concept of an on-balance judgment that 'can guide a choice beyond
    the checked scope' for an open family, together with the claim that passing declared
    requirements does not settle that judgment. The note supplies the concept through
    its title claim and Python and Commonplace examples. It states the boundary with
    declared requirements in its factory paragraph. The note does not use the dependent's
    term 'open family'.
- scope: passage
  quotes:
  - A pass answers that defined question; an on-balance judgment does not override
    a binding requirement.
  reason: DUPLICATED — kb/theory/a-better-factory-claim-compares-operative-states.md
    — both notes state the boundary between declared requirements and an on-balance
    judgment, each from its own side. The note says the judgment does not override
    a binding requirement. The dependent says passing the requirements does not settle
    the broader judgment. The two statements complement each other rather than restate
    one claim. Each states the direction its own readers need, so neither states the
    boundary better overall.
contract: report
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/role/calls/launches/73a78ce12de84cca9ad16b61921c408e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/role/artifact/reviews/c0685a2cca4370cdeeea0751/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/role/calls/launches/73a78ce12de84cca9ad16b61921c408e/outputs/review.md
raw-output-sha256: 65d770d7728b9e6e072bcf61a43f5f75008d390d2b9ffa22e936259909c77d26
---

# Role in the KB: On-balance judgments can guide improvement without a global measure

## Role
The note is the KB's citable statement of Commonplace's program objective. Four of its five dependents link directly to the section anchor `#what-commonplace-chooses-to-count`: two reference documents and two proposals that test or apply that objective. A fifth dependent, a theory note on better-factory comparisons, relies on the note's general concept of an on-balance judgment as what guides choice beyond declared requirements.
Relied on: the objective sentence (more useful and better-warranted knowledge work for the human judgment spent, on balance); its rationale (whether a gain is worth the judgment to build, operate and maintain a change); that automation alone does not settle that question; the term "on-balance judgment"; and the boundary that a pass answers a declared requirement and an on-balance judgment does not override it. Unused: the Python 2/3 text handling, the `random.py` diagnostic and the 3.10/3.11 release table; the library-hours case; the three choices that fix a comparison; the rule to investigate an unknown only if a plausible answer could reverse the choice; the total-order/partial-order paragraph; the tag-coverage trace and the `AGENTS.md` routing-line example; and the closing point that agents can offer reasons without a global score.

## Dependents
- `kb/reference/commonplace-as-an-instrument.md` — the objective as "what Commonplace chooses to count as progress".
- `kb/reference/commonplace-declared-frame.md` — "the program objective", which it distinguishes from a local acceptance criterion.
- `kb/reference/proposals/ablation-baselines-for-the-declared-objective.md` — the objective as something to test on matched tasks, comparing work quality and human effort.
- `kb/reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md` — the objective as the question whether shared machinery repays its human cost.
- `kb/theory/a-better-factory-claim-compares-operative-states.md` — the concept of an on-balance judgment and its boundary with declared requirements.

## Duplication
- `commonplace-as-an-instrument.md` restates the automation point as "Automating a task is not, by itself, a gain." The note's version is narrower: automation does not answer whether a gain is worth its judgment cost. The two wordings differ in strength.
- `a-better-factory-claim-compares-operative-states.md` and the note each state one side of the boundary between declared requirements and on-balance judgment. The two statements complement each other and do not compete.

## Untaken recommendations
None. No linking passage recommends a change to the note.

## Reach
- The heading "What Commonplace chooses to count" and its anchor `#what-commonplace-chooses-to-count` reach four dependents through their link targets: `commonplace-as-an-instrument.md`, `commonplace-declared-frame.md`, `ablation-baselines-for-the-declared-objective.md` and `reusable-commitment-support-across-kinds-of-knowledge-work.md`.
- The objective sentence and its terms ("useful", "better-warranted", "human judgment spent", "on balance") reach the same four dependents. The two proposals paraphrase the human-judgment term as "human effort" and "human cost".
- The automation sentence reaches `commonplace-as-an-instrument.md`.
- The term "on-balance judgment" in the title claim and the factory-requirement paragraph reach `a-better-factory-claim-compares-operative-states.md`. That paragraph also bears on `commonplace-declared-frame.md`'s separation of local criteria from the program objective.
- A change to the Python, library-hours, partial-order, investigation-rule, tag-trace or `AGENTS.md` material reaches no dependent.
