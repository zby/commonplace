---
type: types/note.md
description: "Closure evidence and backlog disposition for the code-scheduled analysis workflow, retaining bounded publication and amendment observations without obsolete full analysis sets."
---

# Analysis offload: closure evidence, 2026-10-02

The operator commissioned closure of the analysis-offload-to-code workshop
after reviewing its backlog. The main goal is met: code opens runs, assembles
worker inputs, schedules jobs, validates outputs, builds manifests and renders
published reviews. Analysts retain source interpretation; independent judges
check records and public synthesis. This report supports future assessment of
that division and selects small failure cases for future model evaluations.
It does not establish analysis reliability or a general model ranking.

The operator declined retrofitting old analyses because their value for current
workflow comparisons is declining. Four live retained sets and their three
generated reviews are retired. The workshop's 25 working documents are deleted
after extraction. Their full records remain in Git; ignored run states and
older frozen archives are left untouched.

## Implemented result

The workflow module is `src/commonplace/lib/agentic_workflow.py`; the separately
tested scheduling engine is `src/commonplace/workflow/`. The
[analysis skill](../../agentic-systems/instructions/analyse-agentic-system/SKILL.md)
loads the driver loop and job-specific prompts. It is 70 lines at closure,
compared with approximately 526 at workshop opening. This measures instruction
placement, not total worker reading or token savings.

Permanent lens-prefixed IDs removed the proposed register mapping and memory
rewriting machinery ([ADR 096](../../reference/adr/096-analysis-passes-declare-their-own-records-under-lens-prefixes.md)).
Code renders the public review from judged synthesis
([ADR 097](../../reference/adr/097-agentic-analysis-drops-decisions-that-change-no-result.md)).
Record reconciliation and verification precede independently authored and
checked synthesis ([ADR 098](../../reference/adr/098-separate-analysis-reconciliation-from-synthesis.md)).
Shared contracts and direct parameterized invocations deliver each worker's
dependencies. Refused outputs are preserved for bounded amendment; every
analysis handout requests a fresh context. Input groups use a 6 KiB hint and
oversized-file range guidance. Synthesis links are checked at acceptance.

## Publication and amendment observations

Three fresh Sol medium runs on 2026-10-01 used method commit
`2ad1816a79e0e5d9b1e178a109d3615fdfab61e5` and Instinctual Memory source commit
`6acb13dc35765bf5ccfc87e445dd09c480f1c28a`. Runs ending `05`, `06` and `07`
all reached verified synthesis. Only `07` published: their shared review
destination made the other two openings stale. These were repetitions of
`gpt-6.1-sol` at medium effort, not the intended comparison of models.
Later trials used distinct destinations.

The 2026-10-02 trials used that same source pin and fresh worker contexts.
Their full trial protocol and trace audit were committed in `6f0240b7` and
`e6be4e13`; those records distinguish recovered errors from remaining defects.

| Setting | Method pin | Run | Outcome | Accepted jobs / handouts | Truncated deliveries |
|---|---|---|---|---:|---:|
| Luna medium | `a7d04e9b` | `AAS-2026-10-02-instinctual-memory-01` | Published | 12 / 12 | 21 |
| Sol medium | `a7d04e9b` | `AAS-2026-10-02-instinctual-memory-02` | Published | 8 / 8 | 0 |
| Luna xhigh | `6f0240b7` | `AAS-2026-10-02-instinctual-memory-03` | Stopped before synthesis | 10 / 11 | 10 |

The xhigh method differed only by the committed trial report; code, types and
worker instructions were unchanged. The medium pair shared worker capacity;
xhigh ran separately. One observation per setting cannot establish reliability,
isolate the four preceding fixes or locate an absolute model capability limit.

Xhigh exercised the real amendment path: code refused two runtime headings and
preserved the output; a fresh worker fixed those headings in about 77 seconds.
All nineteen declared records survived. Every nonblank, nonheading line was
unchanged. The preserved output SHA-256 was
`b2579f82b4ad1690a5d5bdf2a93297cc0f3b752478a1d546d5683ebb62d2e20b`.
Original worker trace: `01a0fb84-1966-7b32-a2cf-c9c6076d4fc7`; amendment:
`01a0fba1-210b-72d2-b775-5af5fa64bd05`.

## Small failure cases worth reusing

**A quotation changed after successful grounding.** A correction worker inserted
a word while writing the report. The workflow now matches analyst quotations
against frozen sources at acceptance. Scripted workers exercise refusal,
amendment and publication without an extra reconciliation round. This checks
occurrence; it does not establish that the surrounding claim follows.

**A grouped read bypassed the hints.** Xhigh memory0 printed two reports in one
large delivery, lost an internal range and recovered only part of it. Printing
range headings inside an oversized result did not bound delivery. Sol medium
had no truncated deliveries, so the hints can be followed but do not enforce
reading discipline. No bounded-read wrapper is adopted at closure.

**The judge missed further instances of a format defect.** Xhigh's first judge
identified invalid conclusion-status values in runtime and epistemic records.
After the correction pass, its second judge found the same defect in two memory
routes. The earlier judge had received those passages without truncation. The
run stopped when its bounded correction allowance was exhausted. Final judge
trace: `01a0fbf1-a5b8-7c41-91ac-aebc33a2814d`. No new review was published.

**Successful shape and quote checks did not establish coverage.** Published
medium analyses and the stopped xhigh reports still had semantic gaps. Xhigh's
four typed reports passed deterministic validation and all 82 quotation blocks
matched, while interpretation defects remained. More effort improved some
reading and coverage without establishing completion or defect-detection
reliability. General extra retry rounds are not adopted on this evidence.

## Backlog disposition

| Original item | Closure disposition |
|---|---|
| Run opening (1) | Workflow start allocates IDs, pins the method and records destination expectations. The separate opening proposal needs no second command. |
| Memory finalization and ID mapping (2, 4) | Removed by permanent analyst-prefixed IDs; no replacement mapper is required. |
| Manifest and review generation (3, 5) | Implemented as code-owned workflow operations. |
| Read wrapper (6) | Deferred; retain the reading failure case, with no active implementation commission. |
| Probe runner (7) | Deferred until a commissioned analysis needs target execution. These trials prohibited it. |
| Prior-analysis deny hook (8) | Dropped; audits observed no forbidden reads, and enforcement would be harness-specific. |
| Required record fields (9) | Seven unconditional route fields are checked at member acceptance under [ADR 100](../../reference/adr/100-check-required-route-fields-at-member-acceptance.md). No new adequacy assay or old-set migration. |
| Broader cross-member checks (10) | Deferred; existing identity/reference/profile checks remain, and semantic consistency stays with verification. |
| Fail-fast Bash wrapper (10a) | Dropped by the operator as generic agent command discipline outside this KB's scope. |
| Source seed scanners (11) | Dropped; no evidence here establishes that seed lists improve coverage. |
| Worker-input assembly (12) | Implemented through generated invocations and declared dependencies. |
| Status and comparison staleness (13, 14) | `step` supplies the next action; the handoff reports comparison staleness. Separate commands are unnecessary. |

Role-specific packets, output skeletons, balanced compaction candidates and
draft intent paragraphs are not adopted. Their estimates did not establish
enough benefit to commission further implementation or trials at closure.
The [shared-contract conformance proposal](../../reference/proposals/shared-analysis-contract-conformance.md)
remains separate: generic type reviewers need complete shared criteria and
freshness dependencies. The code-scheduled-workflows workshop retains ownership
of the generic engine and its proposal; this closure does not close that work.
