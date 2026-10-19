# Treadle Headless

A standalone Python runtime for workflows that invoke headless workers.
Workflow code owns branches, checks and correction loops. The runtime owns
subprocess launches, separate output paths, bounded execution and run records.

This package is an independent implementation, staged in a Commonplace
workshop. It does not import Commonplace or require a Git checkout. It is not
a replacement for an existing Treadle installation. Initial platform: Linux,
Python 3.11 or newer.

## A call

```python
import sys
from pathlib import Path

from treadle_headless import CommandWorker, Request, Run

worker = CommandWorker(argv=(
    sys.executable, str(Path("worker.py").resolve()), "{prompt}",
))
request = Request(
    call_id="summarize-v1",
    task="Read the supplied source and write the requested summary file.",
    inputs={"source.txt": "Material to summarize."},
    required_outputs=("summary.txt",),
    worker=worker,
    timeout_seconds=60,
)

with Run(Path("run-records"), Path.cwd()) as run:
    result = run.call(request)
    if result.status == "delivered":
        print(result.outputs["summary.txt"])
    else:
        print(result.status)
```

`worker.py` represents your worker executable. It receives the path of a
generated prompt that lists absolute input and output paths. It must read the
inputs and write the named files. Standard output is execution evidence, not
the requested file result. Command arguments are passed without a shell.

The generic command adapter also accepts `{input_dir}`, `{output_dir}`,
`{problem_file}`, `{launch_dir}` and `{workdir}` path tokens. Named inputs and
outputs are single filenames. Each physical launch has fresh paths, including
when a call retries.

## Resume and corrections

Reopen the same run directory and repeat the same call to reuse a committed
result. Both the stable call identity and declared request must match.
Different identities request independent work even when their prompts match.

The caller must keep the surrounding environment compatible with reuse.
Changing ambient files, tools or workflow logic may require a new run. The
runtime does not infer those dependencies, pin code or manage environments.

Check delivered content in your workflow. For a correction, create a new call
with a stable identity for that correction, previous content and findings as
inputs. Bound that loop in workflow code. Replay a cached result through its
check; delivery does not certify acceptance. Use fixed sibling snapshots for
checks whose answer depends on other parallel results.

The default is one physical launch. Larger limits and execution retry policy
must be explicit. Each launch reservation spends an allowance before process
start. Restarting does not refund consumed allowances. An unresolved launch
reservation blocks automatic work: establish that the old worker has stopped
before acknowledging it with `acknowledge_stopped`. This operation records
your assertion; it cannot prove that the old process is gone.

`run.parallel(requests, max_workers=...)` preserves result order and waits for
all submitted work to settle before reporting an exception. It does not create
a dependency scheduler. The limit applies to that group; callers creating other
threads or parallel groups remain responsible for their combined concurrency.

## Harness adapters

```python
from treadle_headless.adapters import codex_worker, pi_worker

codex = codex_worker("gpt-6.1-sol", sandbox="workspace-write", effort="low")
pi = pi_worker(
    "gpt-6.1-sol", provider="openai", tools=("read", "write"),
    project_trust="no-approve",
)
```

Pass one of these as the request's `worker`. Put the run records inside a
directory the worker can write; the adapter does not widen the sandbox for
record paths. Pi's project-trust option controls resource loading, not OS
permissions. A `claude_worker` command factory is also available, but has not
been exercised with a real model in this implementation session.

Codex and Pi have each passed a bounded real file-copy probe and reuse check.
Their raw event streams remain in each launch's `stdout.log`. The standalone
`parse_evidence(harness, stdout_text)` helper extracts available session and
model fields; it does not infer the served model from the requested model.
`Attempt.evidence` is a separate optional worker-file protocol, not an
automatic interpretation of those CLI streams.

## Outcomes and recovery

`CallResult.status` distinguishes `delivered`, `incomplete`, `worker_problem`,
`usage_limit`, `process_error`, `timeout`, `launch_error`, `protocol_error`,
and an explicitly acknowledged `interrupted` launch. `RetryPolicy(on=(...),
backoff_seconds=...)` selects which eligible execution outcomes to retry up
to `Request.max_launches`. Usage-limit results are not automatically retried.
Recognition currently comes from the structured problem-file protocol;
provider quota messages in raw harness logs are not universally classified.

An uncertain launch raises `UncertainLaunchError` before new work starts.
Inspect `run.unresolved_launches()`, establish that the old worker and its
children have stopped, then call `run.acknowledge_stopped(launch_id)`. To allow
a subsequent launch, the original request must have remaining allowance and
an explicit retry policy including `interrupted`. Otherwise start a new run
deliberately. Changing execution policy or limits changes declared request
identity; it is not a way to continue the original call's budget.

Corrupt records raise `RecordError`. A persistence failure can poison the
current controller: close and reopen it before inspection or recovery. Never
delete a reservation merely to suppress uncertainty.

## Boundaries

Separate output directories prevent accidental reuse of another launch's
files. They do not restrict a worker's filesystem or network access. The caller
configures permissions, credentials and the harness environment. External
effects are not transactional and may need caller-owned recovery.

See [the execution contract](docs/design.md) for guarantees and limits, and
[harness evidence](docs/harness-evidence.md) for adapter evidence and tested
versions. Support claims must distinguish deterministic tests from actual
model invocations.

## Development

Run commands from this package directory:

```sh
uv sync
uv run pytest
uv run ruff check .
uv build
```

Tests use real subprocesses with deterministic worker fixtures. They do not
require model credentials. Real-harness probes are separate, bounded operations.
No package has been published by creating this source tree.

The [ordinary-file example](examples/README.md) demonstrates checks, corrections
and resume. To run a real, credential-using probe deliberately:

```sh
uv run python examples/smoke_harness.py codex /tmp/my-codex-probe --model gpt-6.1-sol
uv run python examples/smoke_harness.py pi /tmp/my-pi-probe --model gpt-6.1-sol
```
