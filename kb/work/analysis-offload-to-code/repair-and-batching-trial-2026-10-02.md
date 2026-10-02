# Amendment and input batching trial

Commissioned on 2026-10-02 after the Luna and Sol trace comparison. The operator
approved amendment retries, input batch hints, fresh worker contexts, early
synthesis link checking, and a controlled Luna medium/Sol medium comparison.

## Method changes

- A refused output with unchanged inputs is preserved and named in its next
  handout. The worker amends failures and dependent findings, preserving the
  remaining analysis and records. Changed inputs require a fresh attempt.
- Python adds file groups to the invocation, using a 6 KiB byte budget. The
  original files and dependencies remain intact. Oversized files get their
  own entry and a bounded-range hint. No packets or summaries are created.
- Every analysis handout specifies `fork_turns=none`.
- Synthesis acceptance uses the same link-boundary check as retained members,
  before synthesis verification.

## Trial protocol

Both new whole-system runs use `https://github.com/jasonkneen/instinctual-memory`
at source commit `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`, the same committed
method revision, and the analyse-agentic-system skill. The existing clean
checkout remains read-only. No target execution or provider calls are permitted.

The parent follows the code-scheduled loop for both runs and passes each prompt
unchanged to fresh workers. All workers of the Luna run use `gpt-6-luna`,
`medium`; all workers of the Sol run use `gpt-6.1-sol`, `medium`.

The supplied review destinations are
`kb/agentic-systems/reviews/instinctual-memory-luna-repair.md` and
`kb/agentic-systems/reviews/instinctual-memory-sol-repair.md`. The current
published review and the previous retained sets are left unchanged.

After both runs stop, inspect validation, retained hashes and quotations,
worker launch settings, truncation and recovery, amendment behavior if reached,
and substantive coverage. Compare the profile selectors and trace sources,
runtime component inventories, and the source's two known polarity risks with
the previous runs. Report internal repaired errors separately from defects
that remain in accepted results. Record the run IDs and trace evidence here.
