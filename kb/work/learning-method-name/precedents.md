# Earlier systems against the three conditions

Written 2026-11-21 by an agent (claude-fable-5-2) from the ingests listed
below. It tests [the draft definition](./draft-definition.md) against earlier
traditions. The placements are the agent's readings of ingest reports, not
of the sources themselves. No ingest has retained quotes for these points
except Argyris. Treat each row as a claim to check, and try to find a system
that meets the definition.

## The comparison

Each row takes the system alone, without the people who built and tuned it.

| System | What it keeps | What decides | Can it question that rule? |
|---|---|---|---|
| Soar ([chunking](../../sources/chunking-in-soar-general-learning-mechanism.ingest.md)) | A rule for every solved subgoal | Nothing. Retention is automatic. | No |
| PRODIGY ([Minton](../../sources/minton-utility-of-ebl-aaai88.ingest.md)) | Rules whose estimated utility is positive | One formula, in time saved | No. It revises the estimate, not the formula. |
| BDI architectures ([survey](../../sources/bdi-agent-architectures-a-survey.ingest.md)) | No learned plans in the surveyed systems | The programmer's fixed ordering among hand-written plans | No |
| IRMA ([Bratman, Israel and Pollack](../../sources/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md)) | Plans during one run. Nothing from outcomes. | A deliberation process and a filter with an override | A footnote proposes tuning the override threshold |
| Truth maintenance, bare ([Doyle](../../sources/doyle-1979-truth-maintenance-system-aim-521.ingest.md)) | Beliefs that have a valid recorded reason | Support alone | No |
| Truth maintenance, dialectical design (same memo) | Every argument. The current beliefs are derived from them. | Unsolved. Doyle says explicit rules for choosing what to believe are needed and defers them. | Steps and premises can be challenged. The design has one three-node example. |
| EURISKO ([report](../../sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md), [Lenat and Brown](../../sources/why-am-and-eurisko-appear-to-work.ingest.md)) | Concepts and heuristics with a worth | Worth, set from task results and by other heuristics | Partly. The heuristics that judge are units the system can change. People corrected it repeatedly. |
| Organizations ([Zollo and Winter](../../sources/zollo-winter-routines-to-dynamic-capabilities.ingest.md)) | Changed routines, in manuals and tools | "Improved effectiveness", not defined | Not in this paper. The learning routines change; the criteria do not. |
| Organizations ([Argyris](../../sources/argyris-organizational-learning-and-mis-1977.ingest.md)) | Corrected practice | The governing objectives and policies | Double-loop learning questions them. Argyris reports that organizations rarely manage it. |

## What the comparison shows

- **No ingested program meets condition 2 alone.** Each one keeps changes by
  a rule it cannot question, or keeps everything.
- **EURISKO is the nearest program and is not yet checked.** Its judging
  heuristics are in the store and open to change. Whether that amounts to an
  on-balance judgment, or to one worth number under changing rules, needs a
  boundary case in [the checks](./definition-checks.md).
- **The system together with its designers always meets the definition.**
  Minton chose and revised PRODIGY's formula. Lenat corrected EURISKO. This
  agrees with [case 4 of the checks](./definition-checks.md).
- **Doyle names the gap that condition 2 fills.** A system in which every
  step can be challenged needs something that chooses between revisions. He
  states the need and has no judge to supply.
- **"Open to criticism" has two parts.** Recorded reasons make a judgment
  withdrawable. Something must also start the reconsideration. Doyle's bare
  system has the first part. IRMA has a policy for the second and learns
  nothing from outcomes. The draft's condition 3 does not say what starts a
  later round.
- **The sources use "deliberation" for choosing among options already
  given.** None uses it for revising the options or the measure. Zollo and
  Winter's "deliberate" means the degree of cognitive effort invested in
  learning, not weighing.
- **Double-loop learning is the closest stated concept to condition 2.** It
  separates correcting errors under fixed objectives from questioning the
  objectives.

## Limits

- The BDI survey samples representative architectures. It does not show that
  no BDI system learns plans.
- Doyle's mechanism for choosing revisions is in his thesis, which is not
  ingested.
- Both Doyle and Bratman snapshots have conversion damage. Quotes need
  checking against the page images.
- Zollo and Winter is the 1999 working paper, not the 2002 article. Its
  "codification" means writing manuals and tools, which the KB's
  [codification](../../theory/definitions/codification.md) excludes.
- A second round of ingests is in progress: Rao and Georgeff, Aamodt and
  Plaza, and Minton and Carbonell.
