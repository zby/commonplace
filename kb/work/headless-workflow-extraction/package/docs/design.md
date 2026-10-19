# Execution contract

Treadle Headless runs caller-written Python workflows through subprocess
workers. It does not schedule a declarative graph or ask an agent to advance
a step program. Calls return delivered files and execution evidence; the
workflow decides whether their contents are acceptable and what to do next.

## Boundaries

The caller supplies an existing working directory, task inputs, output names,
worker configuration and limits. The runtime creates separate launch files,
collects results, bounds launches and retains records. It needs neither Git
nor Commonplace.

The caller owns environment preparation, sandbox permissions, credentials,
external effects and domain validation. A fresh output directory is not a
sandbox. A retained result is not evidence that the environment is unchanged
or that the output passed a current check.

## Identity and persistence

A run owns its record directory under an exclusive controller lock. Within a
run, the caller gives each logical call a stable identity. Reuse also requires
matching declared request material. Two independent calls with identical
prompts have different identities. Changes to supplied content must not reuse
the earlier result.

Every physical launch receives a fresh directory and its own prompt, inputs
and output paths. Files left by a failed launch are evidence of that launch;
they cannot become another launch's result. The runtime records returned
content with the invocation that produced it. Model or session identity that
the harness does not establish remains unknown.

Only complete, atomically committed result records are reusable. Workflow
acceptance is separate: a resumed workflow reruns its checks against the
intended input snapshot. It must not use changing sibling output state as an
implicit input to a parallel check.

## Budgets and interruption

A durable reservation precedes each process start and spends one launch
allowance. A reservation can therefore count a process that did not actually
start if the controller stopped between reservation and launch. This is a
conservative budget, not an exact process census. Retrying cannot reset spent
allowances by restarting the controller.

An unfinished reservation makes prior execution uncertain. Automatic resume
must stop until the operator establishes that the old worker is no longer
running and explicitly acknowledges that uncertainty. A PID alone is not
sufficient evidence: it may have been reused. Recovery does not refund the
reservation or adopt unrecorded output files.

Handled timeouts terminate the owned process group, including children whose
leader has already exited. Independent parallel calls settle before group
failure is reported. Abrupt process death cannot promise that children have
stopped; that case follows the explicit recovery rule above.

Retries of execution failures are bounded and explicit. Content corrections
are caller-owned calls carrying feedback and previous results. A bounded
workflow loop controls their allowance. These two budgets must not be
conflated.

## Limits

No exactly-once guarantee covers worker side effects. The caller must make
external effects repeatable or supply an appropriate recovery policy.
Cross-run cache reuse, process migration, distributed controllers, environment
pinning and general automatic recovery are outside the initial scope.

The public API and tested support claims are recorded in the package README
and harness evidence. This document states the intended contract; acceptance
tests and release evidence establish which parts the implementation meets.
