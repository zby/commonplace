---
description: "Use when a settled article or note should be improved for a stated audience through the passes an assessment recommends, each run as a short intent packet, rather than a generic editorial rewrite or a full automated pass"
type: kb/types/instruction.md
---

# Revise an article or note

Make the artifact serve the operator's stated purpose without changing what it
claims, by assessing first and then running only the passes the assessment
recommends.

## Prerequisites

- The operator has stated the purpose in one line: who the reader is and what
  they should notice or be able to do.
- The artifact's claims are settled. A claim in dispute goes to the operator
  as a question, not into a pass.

## Steps

1. **Assess before editing.** Read the whole artifact. Report a ranked list
   of changes, highest value against the purpose first, each with its cost
   in one phrase and the pass from this directory that would make it. Name
   the sentence a hostile reviewer would attack first. Say what reads well
   in one sentence. Recommend only passes whose value against the purpose
   is clear; an item you would not defend is not recommended. Do not edit.

2. **Dispatch each recommended pass as a packet.** Proceed without waiting;
   the report gives the operator the chance to interrupt. Run passes one at a time,
   since they share one write scope. Each pass file carries an `effort`
   field: `simple` passes run in a fresh worker on a cheaper model or lower
   effort; `judgment` passes run on the session model, in the current
   context or a fresh worker. Use a fresh worker when the pass benefits from
   not having seen the conversation, as the figurative-phrasing and
   readability passes do. The packet is:

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

3. **Integrate.** After each pass read the diff, run `commonplace-validate` on
   the artifact, and commit the pass alone with a body saying what it was
   meant to make true. If the operator reverts part of a pass, record the
   threshold they applied in the pass file or a memory, so the next run
   starts from it.

4. **Stop when the recommended passes are done.** Report what each pass
   changed. Items you assessed but did not recommend are listed once, not
   run.

## Budget

- The assessment is one full read. Each pass is one more. Do not re-read
  linked notes unless a pass names them.
- A worker gets the artifact path and the packet, never the conversation.
- Propose-only work (the assessment, the figurative-phrasing list, title
  proposals) may run in parallel; edits to the artifact run in sequence.
- Stop when the recommended passes are done. An item not recommended costs
  nothing; recommending a pass of unclear value costs a read and a diff.

## Verify

- Every applied change traces to a recommended pass.
- No claim, evidence, or qualification changed unless the operator asked.
- Each pass has its own commit and validation passed before it.
- Operator reverts have been recorded as thresholds.

---

Relevant Notes:

- [Intent-framed delegation is a control regime; prompt length does not establish it](../../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) — rests-on: the packet fixes purpose, bounds, and return; the worker chooses means
- [An author should fix what the executor can't determine, not what it will](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — rests-on: why the passes state outcomes and preservation rules rather than edit sequences
