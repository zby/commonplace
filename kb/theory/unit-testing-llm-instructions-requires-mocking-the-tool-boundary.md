---
description: Mock tools can record attempted writes without changing files. To rule out forbidden attempts in a test run, the test must observe every available write route.
type: types/note.md
brief: unit-testing-llm-instructions-requires-mocking-the-tool-boundary.brief.md
traits: [title-as-claim]
tags: [document-system, constraining, learning-theory]
---

# Recording attempted tool actions can expose instruction violations that output checks miss

When an LLM instruction uses tools to read, search or modify external state,
replacing those tools with controlled responses lets a test fix what the agent
encounters and capture what it attempts. The test can check execution behavior
that is not recoverable from the final artifact alone.

This tests the instruction's execution, not just its output: [a satisfactory
artifact does not establish a reliable generator](./programming-practices-for-prompts-need-question-specific-evidence.md).
The expected behavior must come from the [applicable requirement](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md),
not merely reproduce what an earlier run happened to do.

## Example: discovery without source modification

Suppose an instruction tells an agent to find connections among notes and write
a report. It permits writing the report but forbids attempting to change any
source note. A test supplies a target and candidate notes through controlled
reads and searches, and captures attempted writes.

The agent might produce a convincing report while also attempting to rewrite a
source note. Checking the report alone would miss that violation. One recorded
attempt is enough to show the violation, even if the mock prevents the change.

To conclude that the agent made no forbidden attempt in that run, the test must
observe every available way to write to the source notes. Checking that no
editing tool was called is insufficient if a shell or another tool can write to
the same files.

## What the checks establish

A captured trace can support deterministic checks such as whether an attempted
write targeted a protected source. Output structure can also be checked
mechanically. Whether a reported connection is justified usually needs semantic
judgment; a required name appearing in the report does not establish that
judgment.

A deterministic assertion does not make the agent's behavior deterministic.
Repeated runs can expose variation under the recorded conditions, but passing
the tested cases does not establish compliance on untested inputs.

## Scope

Mocking tests behavior against the simulated environment. A canned search result
can test how the agent uses that result; it cannot establish that a real search
implementation would return it. The mock must preserve the behavior relevant to
the failure being tested.

Mocking is one route to controlled execution, not a requirement for all
instruction tests. Real tools operating on an isolated temporary corpus can
support other checks. Neither route by itself demonstrates correctness in the
production environment.

## Open Questions

- Which tool behaviors must a mock preserve for failures found in isolation to
  remain relevant under real execution?
