# RF-21 — The declared reviewer system prompt has no registered consumer

**State:** open  
**Repair shape:** dead-code removal or explicit wiring  
**Severity:** low

## Finding

`REVIEW_RUNNER_SYSTEM_PROMPT` is commented as the reviewer system prompt, but no
registered in-repository consumer imports or delivers it. The documented parent
task supplies only the generated prompt path. Some constraints are duplicated in
that generated prompt, so actual behavior may still be adequate, but the named
system-channel contract is not wired.

## Evidence

- [`REVIEW_RUNNER_SYSTEM_PROMPT`](../../../src/commonplace/review/protocol/prompt.py)
  is defined with a comment saying it is used as the system prompt.
- A tracked repository search finds only that declaration.
- [The batch procedure](../../instructions/run-review-batches.md) instructs the
  parent to send `Read {prompt_path} and follow it exactly.`

## Why it matters

Dead system-definition text invites drift: a maintainer can update it believing
reviewer behavior changed when no execution path consumes the edit. It also
confuses RF-13's attempt to define the effective judging configuration.

## Provisional repair direction

If the generated prompt is the complete worker contract, delete the constant and
its claim. If a separate system channel is required, make the parent interface
accept and record it, test delivery, and include its version in judging identity.

## Done when

- There is one authoritative reviewer-contract path.
- Every retained instruction has a registered consumer.
- A test fails when the documented dispatch path stops delivering that contract.
