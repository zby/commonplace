# Supplied evidence and synthesis

## Boundary
Synthetic system Cedar, revision fixture-1. Only the supplied passages are evidence.

## Runtime record RT-01
Source src/checkpoint.py: `write_checkpoint(state)` serializes the current state to disk. The inspected function has no caller in the supplied evidence. Evidence status: implementation existence only.

## Verification context
No unresolved conflict. No other claim or required limitation is at issue.

## Synthesis excerpt
Cedar implements a function that serializes state to disk (RT-01). Its invocation frequency and use for resuming interrupted tasks are not established by this inspection.
