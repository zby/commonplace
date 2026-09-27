# Exercise an installed wiki from onboarding through revision

Run this pack with [Test Commonplace in an isolated installation](../../../kb/instructions/test-installed-commonplace.md).
The supervisor reads this file. Agents under test receive only the current
stage prompt and its permitted inputs, never the acceptance key below.
The default package is a wheel built from the working checkout; select a
published release explicitly when testing PyPI installation.

This ports the task families from the existing context scenarios:
[write a note](../write-a-note.md), [ingest a source](../ingest-a-source.md),
[answer a question](../answer-a-question.md), and
[respond to a change](../respond-to-a-change.md). It adds bootstrap and a
fresh-session check after revision. Actual files and runtime behavior decide
the execution path; the old fork tables are not an execution specification.

## Fixture and operator brief

The fictional Aster Lending Library lends camera kits and tripods to members.
Its wiki supports staff answering lending questions and keeping procedures
current. Lending rules, inspections, and policy changes are in scope; marketing
and unrelated library operations are out of scope. Useful notes distinguish
current rules from history and cite evidence when making policy claims.

The operator has no extra domain facts beyond this brief, the prompts, and the
policy fixtures. No fees or sanctions are specified. Do not invent them when
answering an agent's questions.

The fixtures are complete synthetic Markdown snapshots, not live sources.
Their `https://aster.example/` URLs identify fictional policy versions; do not
fetch them. No HTTP server, browser, or capture dependency is needed.

Immediately before stage 2, copy `fixtures/lending-v1.md` to the project's
`kb/sources/.snapshots/lending-v1.md`. Immediately before stage 4, copy
`lending-v2.md` to the corresponding path. Do not expose either before its
stage. Resolve `{snapshot_v1}` and `{snapshot_v2}` to these project paths.
Use the snapshot `type` declared by the installed contract; if it differs
from the fixture's type, change only that field in the supplied copy and
record the adjustment. Record both repository-fixture and supplied-copy
SHA-256 values. Validate each supplied copy with the installed validator
before taking the stage's starting-state capture. These copies are test
inputs, not worker-produced captures; their bytes must remain unchanged.

Each numbered stage is a fresh session in the same project. Stage 0 starts
after `commonplace-init`; stage N depends on stages 0 through N-1 passing.
No test-specific framework hints are added to the prompts. Let the agent
choose filenames and ordinary implementation details.

The orchestrator follows the instruction above and owns stage progression and
assessment. Launch each stage through a separate CLI agent selected and
isolated under that instruction. Keep `inputs/` and `records/` outside
`project/`; pass only the selected prompt to the worker. Enforce read-only
project access for stages 3 and 5. Start each stage only after accepting its
prerequisites. A zero process exit code is not an acceptance verdict. If a
suitable CLI or its isolation mechanism is unavailable, report the blocker
without substituting an internal sub-agent.

## Stage prompts

### 0 — Bootstrap

> Set up this new Commonplace wiki for Aster Lending Library. It should help
> staff answer member questions about camera-kit and tripod loans and keep
> lending procedures current. Include lending rules, equipment inspections,
> and policy changes; exclude marketing and unrelated operations. Useful notes
> should separate current rules from history and cite evidence for policy
> claims. Complete the project setup so a fresh agent session can use the wiki.
> Use the installed defaults where they fit. You may edit this project's
> files, but not the Commonplace installation. Do not commit or publish.

Bootstrap passes its file and pointer checks here. Verify automatic loading
of the resulting project instructions in stage 1's fresh session, before
accepting stage 1. Inspect runtime evidence; an explicit `cat AGENTS.md` alone
does not establish automatic loading. If loading cannot be established,
record stage 1 as blocked. Do not launch an extra verification conversation.

### 1 — Write a note

> Retain this as a useful note in our wiki: we inspect a returned camera kit
> before lending it again, because missing parts can make the next loan
> unusable. Inspection is a separate operation from recording the return.
> This is our chosen procedure and rationale, not a measured trial result.
> Finish the note using the wiki's conventions. Do not commit or publish.

### 2 — Ingest a source

> Ingest the supplied local snapshot {snapshot_v1} into this wiki so staff
> can use it to answer lending-policy questions. Use the provided snapshot;
> do not fetch its source URL. Do not commit or publish.

### 3 — Answer from retained knowledge

> Using our wiki, can a member borrow a camera kit for 60 hours? Can they borrow
> a tripod for 60 hours? What late-return fee should staff quote? Explain the
> answers and cite the supporting material. This is a read-only question.

### 4 — Respond to a policy change

> The policy in the supplied local snapshot {snapshot_v2} now supersedes the
> earlier version. Use this snapshot without fetching its source URL.
> Incorporate it into our wiki and make the current lending rules easy for a
> later reader to find. Update existing guidance where needed, preserve the
> earlier source as history, and leave unrelated guidance intact. Do not commit
> or publish.

### 5 — Answer after revision

> Using our wiki, can a member borrow a camera kit for 60 hours now? Can they
> borrow a tripod for 60 hours? Is recording a returned camera kit sufficient
> before lending it again? What late-return fee should staff quote? Cite the
> supporting material. This is a read-only question.

## Evaluator-only acceptance key

All authored KB artifacts must pass the installed validator with no failures
or warnings. Framework files must remain unchanged. A justified request for
missing framework capability is a blocker, not a successful operation.

| Stage | Required outcome |
|---|---|
| 0 | Project instructions are created with purpose and scope filled in; library and skill pointers resolve to the isolated installation. The files contain the supplied scope and resolving procedure pointers; verify runtime loading in stage 1. A passing `init --check` alone is insufficient. |
| 1 | The fresh session automatically loads the project instructions created in stage 0. A retained artifact distinguishes recording a return from inspecting equipment, preserves the supplied rationale and its status as a chosen procedure, and invents no measured result. It is reachable through the normal project search/navigation path. |
| 2 | A tracked ingest exists under the installed contracts, identifies the supplied snapshot's source URL, preserves all three policy facts, and pins the supplied copy's exact checksum. The provided snapshot remains unchanged; the worker need not capture a source. Any required worker isolation occurred. A connection report can legitimately contain no candidates; do not require invented connections or authored backlinks. |
| 3 | Camera kit: no, the limit is 48 hours. Tripod: yes, seven days exceeds 60 hours. Fee: unknown/not specified. Citations resolve and the cited retained material supports each policy answer. No KB content is changed. |
| 4 | The supplied v2 snapshot has a distinct tracked ingest. Both supplied snapshots and the old ingest's pinned checksum remain unchanged. Current guidance clearly says 72 hours for camera kits and seven days for tripods, with supporting links; the old 48-hour rule is historical, not a competing current rule. Inspection guidance remains intact. |
| 5 | Camera kit: yes, 60 is within 72 hours. Tripod: yes. Recording return alone is insufficient; inspection is still required. Fee remains unspecified. The camera answer cites the new policy/current grounded guidance; inspection cites the retained procedure. No KB content is changed. |

Assess policy fidelity by reading the cited text, not by checking only that a
link resolves. For ordinary ingest citations that claim retained source
support, check the Quotes section; where the workflow requires the pinned
snapshot, verify that boundary. The executor's assertion that it validated
its work is not a substitute for evaluator checks.

Record whether each fresh session actually loaded project instructions and
retrieved retained content. Previous answers in a shared conversation cannot
stand in for retrieval. If a later stage fails because an earlier stage's
output is incomplete, keep that dependency in the diagnosis.

## First-run boundary

This pack tests ingestion of supplied snapshots and one small wiki through
one revision. It does not test HTTP access, web/PDF capture, shared-clone
source availability, large-KB retrieval, other operating systems, or stability
across repeated runs.
Retain usage totals when the runtime supplies them. Detailed context
measurement is optional; never treat the older scenarios' file-size estimates
as measured runtime tokens.
