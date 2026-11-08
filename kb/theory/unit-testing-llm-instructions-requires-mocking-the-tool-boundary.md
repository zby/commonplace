---
description: "Controlled tool responses and captured effects let instruction tests expose protocol violations that a plausible final artifact can hide; coverage depends on mock fidelity."
type: types/note.md
brief: unit-testing-llm-instructions-requires-mocking-the-tool-boundary.brief.md
traits: [title-as-claim]
tags: [document-system, constraining, learning-theory]
---

# Mocking the tool boundary makes instruction behavior testable in isolation

When an LLM instruction uses tools to read, search or modify external state,
replacing those tools with controlled responses lets a test fix what the agent
encounters and capture what it attempts. The test can check execution behavior
that is not recoverable from the final artifact alone.

This tests the instruction's execution, not just its output: [a satisfactory
artifact does not establish a reliable generator](./programming-practices-for-prompts-need-question-specific-evidence.md).
The expected behavior must come from the [applicable requirement](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md),
not merely reproduce what an earlier run happened to do.

## Example: discovery without source modification

Suppose an instruction must find connections among notes and write a report,
without modifying the source notes. A test supplies a target and candidate notes
through controlled reads and searches, and captures attempted writes.

The agent might produce a convincing report while also attempting to rewrite a
source note. Checking the report alone would miss that violation. Capturing the
attempted effects exposes it, even when the mock prevents the actual change.

The test must cover every available mutation route. Checking that no editing
tool was called is insufficient if a shell or another write tool can change the
same files. An unobserved route is a gap in the isolation claim.

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
