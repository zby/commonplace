# Source-conformance semantic acceptance cases

These are fixture-only cases. Do not replace either live source ingest with the
fixture files in this directory. Before review, copy the fixture texts into an
isolated repository under their ordinary `kb/sources/<slug>.ingest.md` paths and
materialize each candidate below as a separate artifact. Give a fresh reviewer
only one candidate artifact and its complete fixture ingest criterion.

The expected outcomes are semantic invariants. Findings and exact prose may
vary. A `WARN` does not satisfy a required `fail` case.

## Preparation record

Prepared 2026-08-24 from the two exact name-paired snapshots.

- Pirolli snapshot checksum:
  `dcbc565308e0a9eab683087f729137d462f8b6f0d5a8808f989b10b3095e1da2`.
  The fixture has two Claims entries and eleven verified extracts.
- Agent Workflow Memory snapshot checksum:
  `470b8ee461cb933d48a4eab1f53643baeb247e8b909c50c9d26a9cc6e4cbe0bd`.
  The fixture has five Claims entries and twenty-five verified extracts.
- For both fixtures, every byte before `## Claims` and from
  `## Connections Found` onward equals the live ingest. Only the canonical
  empty Claims body was replaced.
- Both populated ingests and all seven candidate artifacts passed clean
  deterministic validation in an isolated repository.
- The production `source` selector derived exactly one source-conformance pair
  per candidate. Job creation produced seven one-note, one-criterion prompts;
  each embeds one complete Claims section and no snapshot path.

Blind outcomes remain pending. The prepared jobs must be executed by fresh
reviewers that have not seen the snapshots, reconstruction, expected matrix, or
this workshop packet.

## Pirolli

Criterion fixture:
`pirolli-proximal-information-scent-distal-content.ingest.fixture`.

### P1 — expected PASS

```markdown
# Proximal cues inform source-selection judgments

In Pirolli's Web-navigation account, proximal information-scent cues provide
concise information about unavailable distal content and inform source-selection
judgments ([source](../sources/pirolli-proximal-information-scent-distal-content.ingest.md)).
```

### P2 — expected FAIL

```markdown
# Follow or skip is the fundamental unit of navigation

Pirolli establishes that the follow-or-skip decision is the fundamental unit of
navigation ([source](../sources/pirolli-proximal-information-scent-distal-content.ingest.md)).
```

### P3 — expected FAIL

```markdown
# More pointer context makes navigation cheaper

Pirolli establishes that the more surrounding context a pointer carries, the
cheaper the navigation decision
([source](../sources/pirolli-proximal-information-scent-distal-content.ingest.md)).
```

### P4 — expected FAIL

```markdown
# Context avoids loading the target

Pirolli establishes that surrounding pointer context avoids loading the target,
and that this avoided load is the mechanism that makes navigation tractable
([source](../sources/pirolli-proximal-information-scent-distal-content.ingest.md)).
```

## Agent Workflow Memory

Criterion fixture: `agent-workflow-memory.ingest.fixture`.

### A1 — expected PASS

```markdown
# Online AWM leads on cross-domain step success

On Mind2Web cross-domain with GPT-4, AWMonline reports 35.5 step success and
AWMoffline reports 32.6
([source](../sources/agent-workflow-memory.ingest.md)).
```

### A2 — expected PASS

```markdown
# Text and code workflows trade step and task success

On Mind2Web cross-task with GPT-4, text workflows report 45.4 step success
versus 45.1 for code workflows, while full task success is 3.6 versus 4.8
([source](../sources/agent-workflow-memory.ingest.md)).
```

### A3 — expected FAIL

```markdown
# AWM and AWM-as-action tie on full task success

On Mind2Web with GPT-4, AWM and the AWM-as-action variant have the same 3.2
full task success ([source](../sources/agent-workflow-memory.ingest.md)).
```
