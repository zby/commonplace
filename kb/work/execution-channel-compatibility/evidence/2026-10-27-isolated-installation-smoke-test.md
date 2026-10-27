# Isolated installation smoke test — 2026-10-27

An isolated project directory was created under `tmp/` and `uv venv` successfully created a fresh Windows virtual environment. The first install attempt hit a permission error in the user uv cache; rerunning with `UV_CACHE_DIR` inside the temporary project passed that point.

The editable install then failed before package execution because the sandbox could not reach PyPI to fetch `jsonschema` and later `hatchling` (`os error 10013`). The package was not installed and no scripted validation ran.

No antivirus alert was observed during the attempt, but this is not evidence of antivirus compatibility: the test stopped during dependency acquisition, before any installed Commonplace command or larger scripted operation executed. The temporary directory was removed after the failed run.
