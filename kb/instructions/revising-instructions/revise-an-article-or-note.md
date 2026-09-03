---
description: "Use when an operator wants a settled article or note improved for a stated audience through chosen passes, each run as a short intent packet, rather than a generic editorial rewrite or a full automated pass"
type: kb/types/instruction.md
---

# Revise an article or note

Make the artifact serve the operator's stated purpose without changing what it
claims, by proposing ranked changes first and running only the passes the
operator selects.

## Prerequisites

- The operator has stated the purpose in one line: who the reader is and what
  they should notice or be able to do.
- The artifact's claims are settled. A claim in dispute goes to the operator
  as a question, not into a pass.

## Steps

1. **Assess before editing.** Read the whole artifact. Return a ranked list of
   changes, highest value against the purpose first, each with its cost in
   one phrase. Name the sentence a hostile reviewer would attack first. Say
   what reads well in one sentence. Do not edit.

2. **Let the operator select.** Wait for the operator to pick items or name
   passes from this directory. A pass the operator did not select does not
   run.

3. **Dispatch each selected pass as a packet.** Run passes one at a time. A
   pass may run in the current context or in a fresh worker; use a fresh
   worker when the pass benefits from not having seen the conversation, as
   the figurative-phrasing and readability passes do. The packet is:

   ```
   Purpose: {the operator's one line}
   Artifact: {path}
   Pass: kb/instructions/revising-instructions/{pass}.md
   Defend: {claims the operator has marked as divergence; a pass may not narrow them}
   Write scope: {the artifact only | none, return proposals}
   Return: the pass's report, nothing committed
   ```

   The worker chooses means within the pass. It does not widen the write
   scope, add claims, or remove evidence.

4. **Integrate.** After each pass read the diff, run `commonplace-validate` on
   the artifact, and commit the pass alone with a body saying what it was
   meant to make true. If the operator reverts part of a pass, record the
   threshold they applied in the pass file or a memory, so the next run
   starts from it.

5. **Stop when the selected passes are done.** Offer the next ranked items;
   do not run them.

## Verify

- Every applied change traces to a selected pass.
- No claim, evidence, or qualification changed unless the operator asked.
- Each pass has its own commit and validation passed before it.
- Operator reverts have been recorded as thresholds.

---

Relevant Notes:

- [Intent-framed delegation is a control regime; prompt length does not establish it](../../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) — rests-on: the packet fixes purpose, bounds, and return; the worker chooses means
- [An author should fix what the executor can't determine, not what it will](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — rests-on: why the passes state outcomes and preservation rules rather than edit sequences
