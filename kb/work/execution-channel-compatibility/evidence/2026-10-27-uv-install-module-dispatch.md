# Isolated uv installation and module dispatch — 2026-10-27

## Tests

- W1 isolated installation
- W2 managed-Python module dispatch

## Result

Both tests passed with a project-local uv cache and network access.

- `uv venv` created a fresh Windows environment under a disposable test root.
- `uv pip install --python <test-root>\\.venv\\Scripts\\python.exe -e .` succeeded.
- Thirteen packages were resolved and installed, including `llm-commonplace`, `jsonschema`, `pytest`, `PyYAML`, `referencing`, and `hatchling`.
- The CLI module was invoked through the test environment's Python with `validate_notes.main()` and returned the expected help output with exit status 0.
- The uv-generated `commonplace-validate.exe` entry point was not invoked.
- No antivirus alert appeared during installation or module execution.

## Boundary

This validates uv-managed installation and direct module dispatch. It does not validate a production shim because no shim implementation exists in the repository. It also does not establish antivirus compatibility on the machine and policy that originally produced the larger-validation detection.

The disposable test directory remains available for the next shim and project-isolation tests.
