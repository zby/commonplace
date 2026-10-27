## Test-shim registration

After completing `INSTALL.md`, identify the uv-managed Python that the installation created. Register the test shims into a disposable bin directory:

```powershell
pwsh -File kb/work/execution-channel-compatibility/test-shims/register-test-shims.ps1 `
  -PythonPath <installed-uv-python> `
  -BinDirectory <test-root>\bin
```

Prepend only `<test-root>\bin` to the test process `PATH`. Do not add the project `.venv\Scripts` directory and do not invoke generated `commonplace-*.exe` files. The registrar prints the interpreter and shim paths; retain those values in the evidence report.
