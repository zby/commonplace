# Session trace audit of the refresh pilot

Audited on 2026-09-27 at the operator's request, after commit `34dc62e3`.

The traces contain recovered errors that a final success summary does not show.
No unresolved publication-integrity failure was found in the three current pilot
results. The main operational weaknesses are masked shell failures, repeated
citation repair, thread-capacity failures, and a status tool that exposes prior
analyses. These matter before expanding to the remaining corpus.

## Coverage and limits

The audit scanned 19 related JSONL traces: the root session and 18 workers,
including Company Brain, both pilot rounds, the abandoned Napkin attempt, and
both synthesis workers. It matched 719 recorded tool outputs to their calls;
none of those calls lacked an output. Root coverage stops at line 2668, before
the audit request at line 2669. This corrects the preliminary discovery update's
overcount of workers.

The scan examined nonzero exits, tracebacks even inside successful command
outputs, coordination errors, publication checks and actual output-truncation
markers. It followed substantive failures through correction and later checks.
Searches returning no matches and deliberate negative acceptance probes are not
counted as operational failures. Tool outputs containing source code's own error
messages are not evidence that an analysis tool failed.

Tool calls and outputs support the findings below. Some inter-agent messages are
encrypted in the local traces; their contents were not independently inspected.
This is an operational audit, not a fresh semantic review of every external-system
claim or a proof that every truncated source read was recovered.

## Findings and recoveries

### 1. Failed checks can end with a successful shell status

The initial Napkin specialist twice hit assertions about citation ranges beyond
EOF: `crud.ts` ended at line 198 rather than 226, and `vault-internals.ts` at 33
rather than 34. The shell continued to structural validation and hashing and
returned exit code zero. Company Brain's specialist similarly printed a quote
check traceback, then clean validation and a report hash; its tool wrapper
printed only stdout, dropping process-status metadata entirely.

These were recovered. Napkin's subsequent check explicitly passed 34 exact quote
anchors, all ranges and unchanged input/method hashes. Company Brain corrected
quote-block separation and passed 15 exact source matches. A clean structural
validator result had not established those source checks on the earlier attempts.

Evidence:

- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T22-28-04-01a0df67-4ce7-75b2-8960-03b2aeec6c9e.jsonl` (JSONL lines 105, 119; recovery 128–134)
- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T15-49-56-01a0ddfa-cc0b-7992-aa79-95f551ef6626.jsonl` (JSONL lines 184; recovery 191)

Operational implication: use separate checked calls or fail-fast command chains
for verification. Never infer that every check passed from the final shell status.

### 2. Citation repair was recurrent, including in the new Mem0 run

Company Brain publication preparation rejected multiple out-of-range source
citations. The coordinator and specialist corrected them; preparation and
publication subsequently succeeded.

Mem0's second run printed eight out-of-range citations while its local diagnostic
still exited zero and structural validation passed. A specialist follow-up then
failed because of the thread limit. The coordinator corrected 20 citation
occurrences across the specialist report and integrated result, disclosed the
report amendment, updated its hash, and passed preparation/publication. Inspection
of the correction code shows endpoint changes and an appended disclosure in the
specialist report; its comparison values were not reassigned. The integrated
result also received two supporting quote blocks and declaration formatting.

The workshop statement that “publication caught” the Mem0 endpoints is imprecise:
the trace shows a coordinator diagnostic caught them before successful publication
preparation. Company Brain did have a failed publication-preparation check.

Evidence:

- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T15-48-01-01a0ddf9-0e3c-73d3-8d67-cea9fa0a046a.jsonl` (JSONL lines 408; recovery 425–469)
- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T23-25-52-01a0df9c-370e-74e2-b7f1-77a651e58826.jsonl` (JSONL lines 253, 259, 273, 282)

Operational implication: source-bound range and quote verification is a necessary
acceptance step; structural validation alone is insufficient. Clamping a range
only establishes a valid endpoint, not that the range supports the associated
claim. This audit confirms the recorded repair and integrity checks, not a fresh
semantic judgment on every repaired citation.

### 3. Capacity failures affected communication as well as worker launches

There were 15 explicit thread-limit failures: eight `spawn_agent`, five
`send_message`, and two `followup_task` calls. They occurred across the initial
and replacement pilots. Thus an existing worker could finish successfully but
fail to notify its coordinator or accept a correction request.

The root recovered by letting coordinators end their turns, launching fresh
specialists itself, relaying completion information, and resuming coordinators.
The final current results bind their specialist reports and pass publication
checks. No missing specialist was silently replaced by coordinator-only analysis.
The Mem0 endpoint amendment above is a disclosed exception to who edited the
specialist's finished report, not a replacement of the specialist analysis.

Representative evidence:

- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T23-40-58-01a0dfaa-0d11-7ef2-bbd3-8cbd6388ab93.jsonl` (JSONL lines 98; later publication 207)
- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T23-39-08-01a0dfa8-5db1-72f0-b711-f0d63d190677.jsonl` (JSONL lines 126)
- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T23-25-52-01a0df9c-370e-74e2-b7f1-77a651e58826.jsonl` (JSONL lines 259)

Operational implication: reserve specialist capacity and treat notification and
follow-up failures as coordination failures requiring explicit recovery. The
workshop already limits scheduling to one coordinator plus its specialist.

### 4. A status lookup contaminated one analysis context

The second Napkin attempt called unfiltered `list_agents`. The response included
the earlier Company Brain epistemic report. This violated the source-only context
rule before Napkin's result was frozen. The coordinator marked the run failed,
stopped the specialist and published nothing. A fresh coordinator and specialist
produced Napkin run `-03`. The replacement's recorded execution reads and assembly
use its own source/input/report paths; no read of the failed run's draft was found.

Evidence:

- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T23-17-08-01a0df94-3b72-7033-b806-09a45e31fd18.jsonl` (JSONL lines 211–235)
- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T23-40-58-01a0dfaa-0d11-7ef2-bbd3-8cbd6388ab93.jsonl` (JSONL lines 45–207)

Operational implication: keep the existing restriction against unfiltered status
listings in source-only workers. This recovery was already recorded in
[contract-change.md](./contract-change.md); the traces corroborate it.

### 5. Record formatting and quote parsing required extra repair

The new Napkin result initially failed with duplicate record declarations. Mem0
failed similarly in both rounds. The new Dynamic Cheatsheet specialist invented
`MEM-EVD-*` identifiers outside the accepted vocabulary; its comparison validation
failed until these became supported `MEM-CLM-*` records. All were corrected and
revalidated before publication. The initial Napkin coordinator also had to replace
em-dash-separated IDs that the validator interpreted as shorthand.

The initial Dynamic Cheatsheet specialist's ad hoc quote checker first mistook an
inline `>` for quote markup, then merged adjacent quoted passages. After anchoring
the parser and separating blocks, all 22 exact quote checks passed. These failures
were in the checking/formatting path; they did not demonstrate false source claims.

Evidence:

- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T23-40-58-01a0dfaa-0d11-7ef2-bbd3-8cbd6388ab93.jsonl` (JSONL lines 169; recovery 176)
- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T23-25-52-01a0df9c-370e-74e2-b7f1-77a651e58826.jsonl` (JSONL lines 237; recovery 253)
- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T23-39-08-01a0dfa8-5db1-72f0-b711-f0d63d190677.jsonl` (JSONL lines 94; recovery 113–122)
- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T22-42-51-01a0df74-d5e1-7fb2-b2d3-f1e373cf224f.jsonl` (JSONL lines 106, 115; recovery 124)

### 6. Truncation and downstream failures were recovered in the current trial

The current synthesis worker's combined read lost 274 tokens from Mem0's component
and object records. Its subsequent bounded reread of lines 501–600 covers the
missing span. It then reproduced all 21 query records exactly and verified the
bundle twice. The trace supports these checks; no synthesis tool error was found.

The root's first bundle preparation lacked three required ontology targets and
was rejected; adding explicit ontology inputs produced a valid bundle. During
implementation, two successive test runs failed on stale output-format assertions;
the subsequent full run passed all 850 tests. After expanding bundle capture,
31 affected tests passed. The git whitespace gate also stopped a commit attempt;
the final commit preserved immutable quoted blank lines and corrected the ordinary
Markdown EOF issue. These were recovered checks, not evidence of a first-pass-clean
workflow.

Evidence:

- `/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T00-02-57-01a0dfbe-2c09-7ed2-bc7d-ea13f2915e10.jsonl` (JSONL lines 57; reread 65; query and bundle checks 112, 127)
- `/home/zby/.codex/sessions/2026/09/26/rollout-2026-09-26T15-48-01-01a0ddf9-0e3c-73d3-8d67-cea9fa0a046a.jsonl` (JSONL lines 1425; test passes 1806, 1828; commit gate 2644)

The all-generated comparison attempt also failed on Pond's missing/mismatched
retained result. This remains a corpus coverage limitation, not a recovered
full-corpus success. The accepted matrix and synthesis explicitly cover three
systems. [Acceptance](./per-value-acceptance.md) retains that narrower population.

## Current integrity recheck

During this audit, all three `commonplace-agentic-analysis-handoff` commands
succeeded for Mem0 `-02`, Dynamic Cheatsheet `-02`, and Napkin `-03`. Bundle
verification with `--source-root .` also succeeded against manifest
`101754b023abbd2efd352e11c8cc75a234dc81802829c2c2d15199b05f8b3113`, with matrix hash
`dc82c6f2e5e9084214147782cf7361c64b20e2940139122e5ded38ad5a4d800d`.

The audit changes no frozen result, specialist report, code or comparison output.
It does not rerun the full tests: the reported test outcomes above are verified
from their session outputs. These notes retain the operational lessons for the
next scheduling decision; they do not introduce a new system feature.
