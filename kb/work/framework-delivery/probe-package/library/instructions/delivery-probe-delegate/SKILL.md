---
name: delivery-probe-delegate
description: Probe skill for the delivery test. Use only when asked to run the delivery-probe-delegate check.
---

# delivery-probe-delegate

This check tests whether the harness can hand a step to a sub-agent with a fresh context, as several Commonplace skills require. Do not read the target file yourself.

1. Start one sub-agent. Give it the absolute path of [the delegated step](../delegated-step.md), resolved from this file's location, and ask it to read that file and return the token it names.
2. Report the token the sub-agent returned, and say that a sub-agent read it.

If you cannot start a sub-agent, stop and report "no sub-agent available". Do not read the file yourself.
