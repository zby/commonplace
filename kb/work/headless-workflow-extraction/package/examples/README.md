# Ordinary-file workflow

`ordinary_files.py` runs two independent producers in parallel, freezes their
returned contents, then checks a combined file against that snapshot. The
deterministic worker makes the first combined file wrong so the workflow sends
one bounded correction with the prior candidate and feedback. All decisions
about acceptance, correction order, and stopping live in this example.

From an environment with `treadle-headless` installed, create an ordinary
working directory and source files, then run:

```sh
mkdir -p /tmp/ordinary-work
printf 'alpha\n' > /tmp/ordinary-work/left-source.txt
printf 'beta\n' > /tmp/ordinary-work/right-source.txt
python examples/ordinary_files.py /tmp/ordinary-records /tmp/ordinary-work --stop-after-producers
python examples/ordinary_files.py /tmp/ordinary-records /tmp/ordinary-work
```

The second command resumes with the two delivered producer results. A third
identical command rechecks their contents and reuses every delivered result.
`invocations.log` in the working directory shows each actual subprocess
launch. Set `--max-corrections 0` to stop after the rejected first combination.
Changing a declared source file causes its producer to launch again; callers
must ensure any undeclared environmental dependencies remain valid for reuse.
