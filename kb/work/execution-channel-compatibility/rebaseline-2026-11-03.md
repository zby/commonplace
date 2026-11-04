# Execution-channel rebaseline — 2026-11-03

## Scope and authority

The operator requested a current-state update before further execution-channel
work. This is a source-static triage plus a reconciliation of retained runtime
evidence, not a new platform test or authority to change production behavior.
Code inspected at `9d91230e1`; the working tree also contained the delivery
workshop closure and its INSTALL.md edits. Later unrelated edits are outside
this snapshot. The August skill audit and September inventory remain historical.

Selection authority: `src/commonplace/scaffold_manifest.py` supplies **11
promoted skills plus one router**, not 13. `pyproject.toml` declares **25**
commands. Library theory lives in `kb/theory/`; `kb/notes/` remains valid for
scaffold projects and must not be mechanically replaced everywhere.

## Evidence now available

The [retained delivery record](../../reports/retained/framework-delivery-acceptance-2026-11-03.md)
establishes bounded Windows installation, native/index skill routing and
command checks, Linux pi installed-worker execution, and synthetic live-session
upgrade behavior. The delivery workshop is closed. INSTALL.md owns its deferred
platform, runtime, release and workload checks; this workshop must not recreate
that acceptance backlog.

`.github/workflows/ci.yml` runs the supported tests with `-m ""` on Ubuntu and
Windows, builds and installs a wheel, verifies all declared command entry points,
and initializes/checks/validates a disposable project. Agentic-analysis tests
remain skipped on Windows. This is package evidence, not proof that all shell
recipes in skills work in PowerShell.

The local [October Windows report](./evidence/2026-10-27-codex-app-windows-powershell-a1.md)
ran procedure v6 against an old checkout. It remains evidence of the observed
command lookup and fresh-tool-shell behavior, not a current v7 survey. The
later delivery checks were not executions of this workshop's breadth protocol.
No current breadth-protocol report is established by this rebaseline.

## Current source census

The legacy-root scan includes all Markdown below `kb/instructions/` plus
`AGENTS.md`, `AGENTS.md.template`, `AGENTS.md.reader-fragment` and `INSTALL.md`.
The expanded scan also includes the canonical instruction trees relocated to
`kb/agentic-system-analyses/instructions/` and
`kb/agentic-systems/instructions/`. Runtime skill projections are excluded.

| Signal | Legacy-root scope | Expanded scope |
|---|---:|---:|
| Files | 127 | 147 |
| Shell-language opening fences, any indentation | 104 | 110 |
| Files containing those fences | 28 | 31 |
| Files mentioning `commonplace-*` lexically | 45 | 49 |
| Files mentioning standalone `rg` lexically | 15 | 15 |

The three instruction trees contain 123, 18 and 2 Markdown files respectively.
These are lexical counts, not counts of executable steps or confirmed defects.
They include examples and prose; they miss command-bearing inline and `text`
blocks. They do not replace the required-reference graph or per-locus inventory.

Of 25 declared entry points, 18 occur in the expanded scan. The seven not
mentioned are `commonplace-ack-trivial-note-changes`, `commonplace-freshness-ack`,
`commonplace-resolve-criteria`, `commonplace-review-job-list`,
`commonplace-store-healthcheck`, `commonplace-task` and
`commonplace-verify-quotes`. This is a documentation-scope observation, not proof
of missing documentation elsewhere.

One obsolete command is still prescribed in
`kb/instructions/simplification-passes/place-external-systems.md`:
`commonplace-agentic-analysis-handoff`. It is absent from the current registry.
The live workflow uses `commonplace-analysis`; selecting a replacement requires
reading the instruction's intended operation, not a blind textual rename.

## Promoted skill and router triage

All 12 selected skills include `Bash` in `allowed-tools`; only validate declares
Bash alone. This is metadata, not evidence of how any runtime enforces it.

| Skill | Current observation | Disposition for the next pass |
|---|---|---|
| `cp-skill-validate` | Ordinary targets call the package; `all` still runs a POSIX conditional/glob loop. The CLI explicitly rejects `all`, with a regression test. Draft-role, today/recent and receipt modes have since been added. | Resolve aggregate-validation design against the current rejection contract before implementing the old E1 proposal; preserve all current target modes. |
| `cp-skill-connect` | Tag discovery still uses `rg -l … \| xargs -r rg`; the zero-match guard prevents search widening. | Package/helper ownership and empty-match semantics still need a decision and test. No shipped tag/path resolver is established by this scan. |
| `cp-skill-health-check` | Steps 1–2 retain POSIX tests; Steps 4–5 have PowerShell forms and supported-shim recognition. Step 3 is runtime-native delegation diagnosis. Step 6 uses plain argv commands, not a POSIX program. | Pair the actual layout/presence checks, not every Bash-labelled fence. Correct the denial diagnosis: matching init outputs do not prove the Windows read rule grants access. Full Windows health coverage remains open. |
| `cp-skill-snapshot-web` | `command -v`, `mktemp`, `awk`, shell variables, byte concatenation and `wc` remain in capture paths. | Preflight versus byte-sensitive workflow implementation remains a real portability boundary; test empty/error paths and exact bytes. |
| `cp-skill-revise-autoreason` | Shell assignments, `mkdir -p` and `cp` prepare runs and blind-judge packets. Delegation itself uses harness workers. | Separate portable filesystem work from orchestration; do not treat a worker-copy pass as full AutoReason acceptance. |
| `cp-skill-ingest` | Backup prose explicitly allows native byte-copy (`cp` / `Copy-Item -LiteralPath`) and requires SHA-256 verification; temp directory is platform-selected. | Native-copy choice is already explicit; do not classify this as an unpaired POSIX copy recipe. Exact-byte behavior and failure handling still need runtime evidence. |
| `cp-skill-ground` | Requires exact snapshot digest/source checks without a shell recipe. | Do not invent a shell defect from the checksum requirement; verify available byte/hash operations in worked cases. |
| `cp-skill-write-multistage` | Main skill has no shell fence. Its promotion reference requires exact-byte drift checks, replacement and rollback, and calls relocation/validation commands. | Trace the reference, not just SKILL.md; exact-byte recovery remains unverified on Windows. |
| `cp-skill-write` | Narrow `rg` discovery and package validation; no embedded shell workflow found in this triage. | Tool availability and path/quoting checks, not automatic conversion to a new helper. |
| `cp-skill-convert` | Package relocation and artifact edits. | Preserve native/package route; verify arguments and filesystem behavior in runtime cases. |
| `cp-skill-add-collection` | Package validation plus authored collection/index changes. | Include this manifest member in coverage; the older selected set is not authoritative. |
| `cp-skill-library` | Router asks for description searches and file reads; no shell fence. | Assess runtime search/read capabilities rather than assume a shell implementation. |

## Non-promoted and probe gaps

The September per-file classifications have not all been repeated. Their
paths/counts must not be used as a current complete inventory. Expand beyond
`kb/instructions/`, then trace required references and classify actual command
positions. In particular, the validator now has `--output`; old suggestions to
add output-file support need checking command by command before implementation.

The frozen v7 probe's authority comparison uses only `uv tool dir --bin` and
has no supported Windows-shim classification. It must be revised before a
current Windows breadth run. A new revision must also distinguish a matching
read-rule file from effective permission, preserve shell-read versus native
Read evidence, and report uv inventory denial without escalating merely to
complete the survey. Preserve v7's no-repair and disclosure boundaries.

The earlier Windows sandbox lacked uv/rg; a later independent run could use
them, and the newest Codex inventory read needed escalation. None establishes
universal presence or absence. Record those environments separately.

## Next decision boundary

1. Revise the breadth probe for supported shims and permission evidence; assign
   a new procedure ID rather than silently changing v7's method.
2. Choose the first bounded E1 change. Health layout checks and connect's
   zero-match search are concrete candidates; aggregate validation requires
   resolving its conflict with the current CLI contract first.
3. Before authorizing implementation, trace affected consumer instructions and
   select Windows fixtures. A missing host produces a pending runtime check,
   not an inferred pass.
4. Complete non-promoted/reference classification before deciding whether
   channel compilation is unnecessary. A proposed reduction is not measured
   evidence that most shell dependence has already disappeared.

## Reproduce the lexical census

Run from the source root with Python 3.11 or newer. The counts describe this
snapshot; future counts may change.

```python
from pathlib import Path
import re

controls = [Path(p) for p in (
    "AGENTS.md", "AGENTS.md.template", "AGENTS.md.reader-fragment", "INSTALL.md"
)]
roots = ["kb/instructions", "kb/agentic-system-analyses/instructions",
         "kb/agentic-systems/instructions"]
for label, selected in [("legacy-root", roots[:1]), ("expanded", roots)]:
    paths = set(controls)
    paths.update(p for root in selected for p in Path(root).rglob("*.md"))
    texts = [p.read_text(encoding="utf-8") for p in paths]
    fence = r"^\s*```(?:bash|sh|powershell|batch|cmd|console|shell)\b"
    print(label, len(paths),
          sum(len(re.findall(fence, s, re.M)) for s in texts),
          sum(bool(re.search(fence, s, re.M)) for s in texts),
          sum(bool(re.search(r"\bcommonplace-[a-z0-9-]+", s)) for s in texts),
          sum(bool(re.search(r"(?<![\w-])rg(?![\w-])", s)) for s in texts))
```
