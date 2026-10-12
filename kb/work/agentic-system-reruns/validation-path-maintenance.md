# Validation-path maintenance decision

## Decision

**Lift the shared pause for fresh eligible analyses.** The three investigated
systems received correct validation commands. Their workers changed the
`--artifact` argument when executing them. No producer defect was established;
no method correction is necessary. Existing instructions already require the
supplied absolute paths and literal command. This decision does not certify
old attempts or release individual recovery holds.

Subsequent [rolling execution 04](./rolling-04.md) recorded recurrence of worker
path confusion despite correct supplied commands. The operator then stopped new
dispatch and requested substantive checks before a simpler worker verification
command is added. This later stop controls scheduling; the diagnosis below does
not authorize restarting or establish that the current interface prevents
transcription errors.

The operator authorized this investigation in the [workshop plan](./README.md).
Origin method inspected: `0603655112dd7942004648ef732e930841d99910`.
Runtime: `openai/gpt-6.1-sol`, medium; worker-launch diagnostic succeeded,
agent-depth and nesting-limit unknown. Loaded tools expose `action` and
`handles`. The [resume record](./resume-2026-10-12.md) leaves no integration
queue or owned running pipeline. Subsequent inspected orchestrator sessions
ended without launching analyses. Agent Skills remains separately reserved.
The pre-existing uncommitted README changes belong to its commissioning editor;
this session does not stage those bytes or infer clean-origin integration.

## Evidence boundary

Read [batch 03](./batch-03.md), the [AgeMem audit](./audits/batch-03-agemem.md)
and the [Agent-R audit](./audits/batch-03-agent-r.md). Two fresh read-only
workers compared delivered prompts and actual paired validation calls/results.

Historical trace, abbreviated T below:

```text
/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-12T13-59-16-666Z_01a13069-19ba-745a-b8d3-80c377c91314.jsonl
```

Every trace locator below is within JSONL line 31, message `5f3ae59f`.
Array indexes are zero-based. Coordinator C is
`message.details.results[index]`; W is the specified nested worker result.
Complete delivered invocations are W's `messages[3].content[0].text`, retained
read results. The original AgeMem and Agent-R on-disk handouts are gone:
`src/commonplace/artifactrun/engine.py:445–459` removes completed handouts.
No missing prompt or candidate was reconstructed or rewritten.

Agent Skills evidence was read only from T, not its worktree or changing owner
files. This avoids accessing changing files before owner coordination. Its
current process ownership and recovery disposition remain unknown.

## Invocation comparisons

The correct artifact path in every inspected invocation is:

```text
/home/zby/llm/commonplace/.commonplace/worktrees/<worktree>/kb/agentic-system-analyses/state/<run>/artifact
```

These substitutions identify the literal paths in the trace:

| Target | Worktree | Run |
|---|---|---|
| AgeMem | `agemem-32274e5bddc1` | `AAS-2026-10-12-2601-01885v1-32274e5bddc1-01` |
| Agent-R | `agent-r-216224d4270a` | `AAS-2026-10-12-agent-r-216224d4270a-01` |
| Agent Skills | `agent-skills-for-context-engineering-2423c2f20f83` | `AAS-2026-10-12-agent-skills-for-context-engineering-2423c2f20f83-01` |

Executable is the worktree's `.venv/bin/commonplace-validate`; candidate is
`<correct run path>/state/handouts/<attempt>/outputs/<filename>`.
The command structure is executable, candidate, `--artifact`, supplied artifact
path, `--role`, member role. The following table retains exact paired call
locators; provider suffixes can be resolved at those locators.

| Attempt | C index; W locator | Failed call/result messages and call ID | Changed artifact argument | Recovery evidence |
|---|---|---|---|---|
| AgeMem `000005-runtime`, `report.md` | 1; `messages[23].details.results[0]` | 47/48; `call_4j0zCSZtekoEmMYIpUuFGM7j` | worktrees/`agemem-32274e5bddc1-01/artifact` | 49/50; `call_wfdyUGtRW9apPkOcwvDCTVw6` restores supplied path; pass |
| AgeMem `000008-epistemic`, `report.md` | 1; `messages[27].details.results[1]` | 47/48; `call_EF6Mu2gZdKnwheGy6241PCvS` | full path but worktree changed to `agemem-32274e5bddc1-01` | 49/50; `call_ctOklI0yVVCzBkSGtuK70jQZ` restores supplied path; pass |
| AgeMem `000024-memory-profile`, `profile.md` | 1; `messages[39].details.results[0]` | 51/52; `call_edMlJoJfljxfnIWTQPORt0g7` | worktrees/`agemem-32274e5bddc1-01/artifact` | 53/54; `call_6OFanEsx9fv8GoHd6ecZeMbQ` restores supplied path; pass |
| Agent-R `000003-boundary`, `boundary.md` | 2; `messages[18].details.results[0]` | 35/36; `call_oqwsdVjAP83IHcenQ2IZFoPn` | worktrees/`agent-r-216224d4270a-01/artifact` | 37/38 restores supplied path, ambiguous quote finding; 41/42 `call_8sXY6ogO5aPBa4Sez8XSPntF` passes after quote correction |
| Agent Skills `000008-epistemic`, `report.md` | 3; `messages[25].details.results[1]` | 52/53; `call_HJkZasq3srhJVwSck7Vu0ii5` | worktrees/`agent-skills-for-context-engineering-2423c2f20f83-01/artifact` | No supplied-path call or passing result in the worker's 57 retained messages |

Every altered-path result reports missing `ARTIFACT.yaml` at the altered
location and `Command exited with code 2`. Agent-R's supplied-path intermediate
check exits 1 for a quotation matching source lines 210 and 247. Passing checks
return exactly:

```text
Member content check passes; invocation residue not checked. This is not job acceptance or claim support.
```

Those successful trace results contain no numeric status field. The validator
implementation returns 0 on that branch; this is implementation-based status
interpretation, not an invented retained result.

Agent Skills' subsequent problem write, W `messages[54].content[1].arguments.content`,
claims the command ran “exactly as supplied.” The paired call contradicts that
claim. Its request for a corrected invocation therefore does not establish a
producer defect. No evidence here establishes that the prescribed check would
have passed, and later publication checks cannot discharge that obligation.

Agent-R's recovery restores the supplied invocation; it does not substitute an
unauthorized alternative for a defective supplied command. AgeMem likewise
restores the supplied paths. Their quote repairs remain distinct from path
transcription failures. This is a narrow diagnosis, not exhaustive worker
compliance certification.

## Current contract and checks

The relevant producer and contracts have no diff from frozen method
`cd6e8250c5277c5c6295b6940a9b01e034c9daa7`:

- `src/commonplace/artifactrun/store.py:50–60`: artifact directory is run/artifact.
- `src/commonplace/artifactrun/handouts.py:164–189`: absolute artifact binding
  and prompt-section rendering use that directory.
- `kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs-engine/prompt-section.md:33–41`:
  run the rendered validator command as written, inspect its complete result,
  and repair until passing.
- The same directory's `follow-worker-rules.md`, “Read the prompt”: use supplied
  absolute paths rather than reconstructing them from directory names.
- `src/commonplace/cli/validate_notes.py:583–624,650–683` and
  `src/commonplace/lib/validation.py:1998–2045`: load the supplied artifact's
  manifest and validate the candidate for the named role; invocation errors
  and content failures have distinct nonzero statuses.

Executed current-method checks:

```text
uv run pytest tests/commonplace/artifactrun/test_handout_delivery.py tests/commonplace/artifactrun/test_prompt_section.py -q
12 passed in 3.57s

uv run pytest -m '' tests/commonplace/agentic_analysis/test_boundary.py::test_handout_is_context_complete_and_uses_engine_names tests/commonplace/agentic_analysis/test_instruction_composition.py -q
6 passed in 4.62s
```

The slow boundary test checks the actual analysis template's rendered command,
including the full artifact argument. Generic delivery tests cover absolute
paths on opening, retry and resume. These checks establish current producer
behavior, not whether a future model will copy the command correctly.
No code or method files changed; no correction commit or new regression test
is warranted. No full-suite or historical revalidation claim is made.

## Execution check and release scope

For fresh runs, the binding worker rule remains literal execution of the
rendered command. Do not shorten or rebuild any path. A missing-path result
requires comparison with the supplied invocation before attributing a defect.
A worker must return a problem rather than claim a passing check it did not
perform. Fresh auditors must compare delivered validation commands with paired
calls/results when validation-path problems occur, and must not infer execution
from publication. This check is operational scrutiny under the existing audit,
not new analyst evidence or a changed acceptance contract.

Fresh source-first coordinators receive only their target/source commissions
and standard skill, not historical findings or this maintenance diagnosis.
The shared producer suspicion is resolved for new work. Agent Skills retains
its reservation and unsupported-validation obligation; ACE retains its open
attempt and prior-worker-status requirement; Academic Research Skills retains
its source-exposure recovery requirement. No old run, frozen method, retained
output or historical trace is edited. No cleanup or push is authorized.

Investigation handles: `1987d185-253e-45b2-a2f7-ce823b067853` (AgeMem/Agent-R)
and `41476c81-1ba7-4961-a41e-ba6e0508f092` (historical Agent Skills trace).
Both returned normally. They were read-only maintenance workers, not system
pipelines or recovery workers.
