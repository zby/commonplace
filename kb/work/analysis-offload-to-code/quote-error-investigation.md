# Quote error investigation

Investigated on 2026-10-01 at the operator's request, following the
[stopped Luna trials](./split-luna-trials.md). This investigation reads the
saved tool calls, analyst artifacts and pinned source blobs. It does not
resume the failed runs, execute the target systems or change their artifacts.

## Finding

The retained quote error arose after successful grounding. The correction
worker rewrote a tool-generated quotation while authoring its report.
Analyst acceptance checked the quotation's format but did not match its
body against the source. The model judge subsequently caught the mismatch.

Matching every attributed quote in the final runtime, memory, epistemic and
reconciliation members gives:

| Run | Attributed quotes | Source matches | Mismatches |
|---|---:|---:|---:|
| `AAS-2026-10-01-pageindex-01` | 14 | 13 | 1 |
| `AAS-2026-10-01-instinctual-memory-01` | 16 | 16 | 0 |

The PageIndex initial memory report's four quotes also match. The
replacement report has three matches and one mismatch, carried unchanged
into `output/memory.md`. Instinctual Memory's initial and replacement memory
reports each have six matching quotes. The final Instinctual Memory epistemic
member has no attributed quotes. Counts measure source occurrence, not whether
the surrounding claim is supported or the selected context is sufficient.

## Where the quote changed

The pinned PageIndex commit is
`d2693d80791a86345ef78b3234834f5fe53a70a0`. The disputed passage is in
`pageindex/agent_tools.py`, lines 1588–1590. Its second line says:

```text
... first to locate relevant sections, then get_page_content() with targeted page ranges.
```

The correction report adds one word:

```text
... first to locate relevant sections, then call get_page_content() with targeted page ranges.
```

Tool-call timestamps below are UTC. The local Codex traces identify both
workers as `gpt-6-luna`.

| Worker | Time | Observation |
|---|---|---|
| `/root/split_pageindex_memory` | 06:43:29 | Helper batch exits 0 and emits the exact source passage. |
| Same | 06:45:49 | `apply_patch` creates `memory-report-0.md` with the passage unchanged. |
| `/root/split_pageindex_memory1` | 06:52:15 | Helper batch exits 0 and emits the same correct passage. |
| Same | 06:54:46 | `apply_patch` creates the replacement report with the extra `call`. |
| Same | 06:54:49, 06:55:05 | Structural validation passes. |
| `/root/split_pageindex_verify1` | 07:02:44 | Judge submits all fourteen quotes to the helper; this quote fails lookup. |

The memory traces are
`rollout-2026-10-01T08-41-20-01a0f632-32fb-71b2-934c-ba85d38d3bf5.jsonl`
and
`rollout-2026-10-01T08-50-37-01a0f63a-b47e-7ca3-bf10-bbffff6b7d58.jsonl`
under the local Codex session directory for 2026-10-01. Both helper responses
were complete, with no truncation marker. Source text, selection text and
helper output agree. The error first appears in the replacement patch.
The evidence establishes transcription drift; it does not establish the
model's internal reason for adding the word.

The [memory job](../../instructions/analyse-agentic-system/jobs/memory.md)
requires a whole-report rewrite in a correction round. The returned findings
concerned record references and object mappings, not this quotation. Rewriting
the whole report exposed already-correct evidence to another transcription.

## Why grounding did not prevent it

This section describes the trial implementation, before the analyst acceptance
repair below.

[Quote generation](../../../src/commonplace/lib/quote_generation.py) locates
selected text in the frozen source and renders the source's own bytes and
derived line range. The [CLI](../../../src/commonplace/cli/quote.py) returns
the citation on stdout; it does not insert or verify the completed document.
The worker constructs a new report patch containing the quote text.

[Worker rules](../../instructions/analyse-agentic-system/jobs/worker-rules.md)
require unchanged insertion. However,
[standing validation](../../../src/commonplace/lib/validation.py) checks only
the shape of these analysis citations. The memory job explicitly defers
assembled quotation checks to publication and forbids a separate worker quote
check. The workflow's `pass_refusals` and `record_check` consequently accept
this report before any deterministic occurrence check.

The existing `verify_quote_anchors` in
[analysis validation](../../../src/commonplace/lib/agentic_analysis.py)
rejects the altered quote against its cited range. It is called by assembled
run validation, after successful record and synthesis judgments. These failed
runs never reached that stage. Replaying that function directly on the saved
members produced the counts above without changing either run's state.

[The grounding skill](../../instructions/cp-skill-ground/SKILL.md) has a
different completion boundary: it writes an ingest's Quotes section, then
requires source matching by `commonplace-validate` on that written ingest.
The analysis quote helper supplies the generation part, but analyst acceptance
does not provide that post-write source check. The grounding skill itself was
not invoked in these traces.

## Other helper errors

- **Selections were not source text.** The PageIndex epistemic worker supplied
  a different bounds predicate, then corrected it. Its reading-guidance retry
  included the same extra `call` and remained rejected; it was not retained
  as a quote. Instinctual Memory selections changed `//!` to `///` or `//`,
  omitted intervening Rust comment markers, or paraphrased the tidy wording.
  Matching normalizes whitespace, not tokens or comment markers. Rejecting
  these selections is correct; later source-exact selections succeeded.
- **Selection files did not exist.** One Instinctual Memory memory call and
  one epistemic call named files not yet written. Those workers subsequently
  wrote selections and obtained quotations.
- **The source was not registered yet.** The Instinctual Memory boundary
  worker called the helper three times before its boundary output was
  accepted. Code writes the frozen source to run-state only after that job
  returns. The shared rule to generate every quote applies to this job too,
  although its run-state cannot yet satisfy the helper's precondition.
  The worker's final boundary used prose source anchors without quotes.

No observed helper error demonstrates incorrect quote generation. Failed
selections and premature calls are distinct from a successful citation
modified during document assembly.

## Repair

Implemented on 2026-10-01 following the operator's decision: the existing
source matcher now runs inside runtime, memory and epistemic output acceptance,
against the registered frozen source. A mismatching quotation triggers the
ordinary job retry before reconciliation or model judging. Memory correction
reports receive the same check. This requires no target execution, additional
quote-generation command or new quote representation. Worker rules and the
memory job's check instruction describe this acceptance step.

The workflow regression tests cover all three analysts and a memory correction:
a structurally valid report with an added quote word is refused, the retry
receives the source mismatch, and the repaired report proceeds to publication
without an extra reconciliation round. All 65 workflow tests and all 1,215
tests in the full suite pass. Read-only
replay of the saved PageIndex memory outputs through the new job validator
accepts `memory-report-0.md` and rejects `memory-report-1.md` at output line 272.

Still proposed: for the boundary job, require prose source anchors without quote blocks.
That job establishes the source identity; later analysts can quote it once
code has registered it. This removes the unusable grounding step from that
role without adding another source-registration phase.

The boundary instruction is unchanged by the analyst acceptance repair.
