---
name: delivery-probe-echo
description: Probe skill for the delivery test. Use only when asked to run the delivery-probe-echo check; takes one argument.
---

# delivery-probe-echo

The argument for this invocation is: $ARGUMENTS

1. Follow [the shared step](../shared-step.md).
2. Report `ECHO-V1` followed by the argument above, verbatim, and the absolute path of this file.

If the argument above is empty or still reads `$ARGUMENTS`, report that instead of inventing one.
