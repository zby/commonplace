---
description: "Proposal (adopted): replace project-activated Commonplace command environments with one user-level uv tool installation"
type: ../../types/design-proposal.md
traits: [has-external-sources]
tags: [architecture]
---

# User-level uv tool installation for Commonplace commands

> **Archived** (see [archive README](./README.md)). Adopted by [ADR 064](../../adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md): [Commonplace architecture](../../architecture.md), [instruction generation](../../instruction-generation.md), the install guide, and the health-check skill now carry the live design. The ADR retains the alternatives and resolved free choices; what remains here is the dated pre-change state and the reported native Windows evidence.

## Current state (as of 2026-08-08)

Before adoption, the `llm-commonplace` 0.1.4 package declared 22 `commonplace-*` console entry points. The full-install guide installed the package into each consuming project's `.venv`, then depended on activation or a generated `.envrc` to put that environment's command directory on `PATH`. The source checkout used the same project environment. Native Windows instructions carried activation, `.venv\Scripts`, and explicit `.exe` fallbacks because the documented direnv path did not apply there.

The repository had only one GitHub Actions workflow. The Pages job installed `.[docs]` with pip and invoked the dependency-provided `properdocs` executable directly. It did not exercise the package's command entry points or native Windows installation.

The exact generated `.envrc` was:

```bash
export PATH="$PWD/.venv/bin:$PATH"
export UV_CACHE_DIR="$PWD/.uv-cache"
```

These facts became unreproducible once ADR 064 removed the template, package inclusion, scaffold manifest entry, project-venv instructions, and pip-based Pages setup.

## Native Windows evidence before adoption

The proposal required a clean native Windows checkout, an editable `uv tool install --python ">=3.11" --editable .`, `uv tool update-shell`, complete process shutdown, and verification in a newly launched PowerShell plus each desktop or IDE agent runtime the maintainer intended to claim. A pass required all 22 entry points to resolve from `uv tool dir --bin` by bare name and `commonplace-validate --help` to exit successfully. Integrated-terminal success could not substitute for the agent command runner.

On 2026-08-08 the maintainer reported the Windows experiment positive and authorized implementation. No per-runtime result table or command transcript was committed, so the retained evidence supports the tested launch classes as reported but does not name product versions or warrant untested runtimes. ADR 064 therefore keeps support for additional desktop or IDE runtimes conditional on a fresh-process check in that runtime.

---

Relevant Notes:

- [ADR 064 — Install Commonplace commands as a user-level uv tool](../../adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) — adopted-by: the implemented decision
- [Commonplace architecture](../../architecture.md) — implemented-by: current command-installation and scaffold behavior
- [Instruction generation](../../instruction-generation.md) — implemented-by: current generated-artifact surface
- [uv tools](https://docs.astral.sh/uv/concepts/tools/) — evidenced-by: the external tool-installation mechanism evaluated
