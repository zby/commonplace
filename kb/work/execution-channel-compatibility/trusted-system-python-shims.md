# Windows shims should invoke a trusted system Python

## Established conclusion

The Windows command surface should use Commonplace-owned shims rather than the `commonplace-*.exe` entry points materialized by uv. The shims should invoke a uv-managed Python runtime and dispatch to the Commonplace module through that interpreter.

The purpose is to avoid antivirus detections associated with executing the uv-generated entry-point executables. The shim is the user-facing command; the uv-generated `.exe` files are not part of the supported Windows command path.

Conceptually, a shim invokes:

```text
uv run --no-sync python -m commonplace.cli.validate_notes <arguments>
```

It must not invoke:

```text
.venv\Scripts\commonplace-validate.exe
```

## Trust boundary

The executable boundary is the uv-managed Python runtime. The supported command path avoids uv-generated `commonplace-*.exe` entry points; whether the uv-managed interpreter itself is accepted by the target antivirus must be validated. The Commonplace package and the shim remain interpreted code and may still be scanned by antivirus software; interpreter signing does not guarantee that imported package behavior will be accepted. The design therefore needs a Windows smoke test with the relevant antivirus product covering the shim, the interpreter, and representative commands.

## Installation consequences

The Windows installation procedure must make a usable uv executable and managed Python runtime prerequisites and verify them before installing the shims:

1. Locate the uv executable and its managed Python runtime.
2. Confirm that uv can run that interpreter.
3. Install Commonplace into the uv-managed environment without relying on generated Commonplace entry-point executables.
4. Put only the Commonplace shims on `PATH`.
5. Verify each shim by invoking the same bare names used by later instructions.

The Microsoft Store `python.exe` alias is irrelevant when uv supplies the runtime. A missing uv executable or unavailable managed interpreter is an installation prerequisite failure, not a PATH-repair problem.

## Current evidence

The native Windows probe on 2026-10-27 found:

- the Microsoft Store `python.exe` alias present but unusable;
- no `py` launcher;
- The uv-managed project interpreter is available; its Authenticode status is `NotSigned`, so antivirus acceptance must be tested behaviorally rather than inferred from a system signature;
- uv-generated `commonplace-*.exe` commands resolving outside the project venv.

This supports the runtime-boundary decision but does not yet prove that the antivirus accepts the complete shim path.

## Open checks

- Select the supported uv-managed Python distribution and verify its runtime behavior on a clean Windows install.
- Decide whether Commonplace is installed into the uv-managed environment or another uv-visible location.
- Define shim root discovery and behavior outside a Commonplace project.
- Test two projects with different package versions and confirm that shims dispatch to the intended project.
- Test the shim under the Windows Codex desktop channel and with the target antivirus enabled.
- Update `INSTALL.md`, the generated control-plane command guidance, and the execution-channel solution catalogue together.

This note records the conclusion carried forward from prior work. Validation remains required, but the workshop should validate this design rather than reopen the shim-versus-uv-executable decision.




