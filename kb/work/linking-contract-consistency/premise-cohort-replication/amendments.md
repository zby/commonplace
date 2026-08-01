# Run amendments and parse failures

The frozen mapper prompt for batch `2-1` initially returned 25 of the required 26 JSON records; `case-93e833a0ae496b` was absent. The raw response is retained as `raw-mapper/mapper-2-1-attempt-1.jsonl` with its stderr companion. No record was dropped and no aggregation was performed from that attempt.

Per the stop condition, the identical frozen prompt and observation file were dispatched in one fresh `gpt-5.6-luna` context. The retry is the scored record for batch `2-1`; the failed attempt remains an audit artifact. This amendment changes neither the sample, packet, prompt, class definitions, exclusion rule, nor decision thresholds.

Batch `3-3` then returned 26 lines but one neutral identifier was truncated (`case-cbbd1d7667e81` instead of the frozen 16-character ID). Its raw response is retained as `raw-mapper/mapper-3-3-attempt-1.jsonl`; the identical frozen prompt was dispatched again in a fresh Luna context. The retry is scored, and the malformed attempt remains excluded and visible.
