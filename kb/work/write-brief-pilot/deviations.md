# Deviations from the frozen protocol

## 1. Runs voided by a usage-limit interruption (2026-09-26)

Seventeen writer runs were terminated mid-task by an API usage limit (HTTP 429, session limit), not by anything in the experiment: 6fe813 996d53 a1f0b9 c78267 fbe348 d1d6fc b3331b 9e9ed4 86554b 22c6c8 af67ee b5fd49 07b799 45aebe eee284 33e3f0 a81609. Fourteen had already written a `candidate.md` that may be incomplete. All seventeen are void. Their outputs are deleted unread, and each run is re-executed from its unchanged packet by a fresh worker. The run order for the re-executions follows the original key order. Recorded before any re-execution and before any scoring.

## 2. Minor isolation slip in run 22c6c8 (2026-09-26)

The re-executed worker for run 22c6c8 reports that a sibling search printed two lines of the file currently at the target's library path. It reports that they match lines 8 and 10 of its own `document.md`, so it gained no information from the current version. The run is kept.

## 3. Arm-revealing clause redacted from one scoring copy (2026-09-26)

Scoring copy `scoring/6/pressure/92a1a9.md` is a question file whose text referred to "the retained brief", which would reveal to scorers that it came from a brief arm. Before any scoring, that clause was replaced in the scoring copy with a bracketed redaction note; the original run output is unchanged. A search of all other scoring copies for brief and retained-intent wording found only the incumbent's own term "brief-output floor", which is identical across arms.
