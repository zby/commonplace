---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Qiju's shipped session-record CLI and host skills at commit a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89."
run-id: AAS-2026-11-08-qiju-1a12c31c13d1-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/jasonshrepo/qiju
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/qiju-9b7c9ef79e6f/related-systems/jasonshrepo--qiju
  revision: a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89
  sha256: null
---

# Qiju boundary

## Boundary and evidence

This run analyses Qiju as a memory/knowledge/context-engineering system for intentional session records and later coding-agent handoffs. The whole-system boundary includes both the deterministic record CLI and the shipped instructions through which model-driven hosts compose, retrieve and review records. It is not limited to the storage API. SRC-1, `pyproject.toml`, registers `qiju.cli:main`; SRC-1, `src/qiju/cli.py`, dispatches installation, capture, search, hydration, maintenance, migration, redaction, update and removal commands.

The classification rests on the shipped host interface, not on attributing host orchestration to Qiju:

> Qiju supports existing coding agents by installing portable Agent Skills. The
> skills tell the agent when and how to call the `qiju` CLI. The CLI writes and
> retrieves records.
> --- `docs/host-integration.md`

> Qiju is not an agent framework and does not orchestrate hosts.
> --- `docs/host-integration.md`

The included state loop is: installed log instructions guide an agent's JSON composition; the CLI admits and persists the record; maintenance retains and moves records; search and exact-ID hydration return retained content; installed search and retrospective instructions guide its later use. SRC-1, `src/qiju/init_cmd.py`, contains all three skill bodies and their local host installers. SRC-1, `src/qiju/capture.py`, normalizes, redacts and validates entries before appending to short and long JSONL under a lock. SRC-1, `src/qiju/storage.py`, reloads short, long and archive records; `src/qiju/search.py` filters them and retrieves exact IDs; `src/qiju/maintain.py` rotates short records, sweeps staging and archives long records. These responsibilities are included even though a host supplies the authored record and chooses tool calls.

The shipped consumer explicitly connects retrieval to later agent use:

> `qiju search` = **Phase 1: candidate identification.** Finds records and prints ids in
> `<uuid>:N` form. Use `--ids-only` or `--format summary` for a cheap candidate manifest:
> --- `src/qiju/init_cmd.py`

> Do not edit any skill files unless the user explicitly asks. Produce recommendations and proposed wording only.
> --- `src/qiju/init_cmd.py`

The latter is the retrospective's permission boundary, not evidence that recommendations succeed. The prompt bodies are doctrine/design evidence; their rendering and installation are implementation evidence. No target execution was performed.

### Tracked-tree coverage

The table accounts for every top-level tracked entry at the frozen commit. Included supporting material remains available to later analysts even when only its declarations have been inspected here. Initial inspection is not an evidence allowlist.

| Top-level entry | Treatment and material paths | Initial inspection and limits |
| --- | --- | --- |
| `src/` | Included: `src/qiju/cli.py` entry and dispatch; `src/qiju/init_cmd.py` log/search/review prompts and host installers; `src/qiju/capture.py`, `src/qiju/schema.py`, `src/qiju/redact.py`, `src/qiju/allowlist.py`, `src/qiju/config/` admission and privacy; `src/qiju/staging.py`, `src/qiju/id_gen.py`, `src/qiju/paths.py`, `src/qiju/util.py` staging, identity and filesystem support; `src/qiju/storage.py`, `src/qiju/archive.py`, `src/qiju/search.py` reload and consumption; `src/qiju/maintain.py`, `src/qiju/retro_redact.py`, `src/qiju/migrate.py` maintenance; `src/qiju/register.py`, `src/qiju/update_cmd.py`, `src/qiju/cleanup.py`, `src/qiju/block_format.py` installation lifecycle; `src/qiju/__init__.py` package marker. | CLI, capture, storage, search and maintenance read in full. Prompt bodies and local installers read; global installer paths and support modules surveyed through function/import declarations. Remaining bodies and configuration contents are available but not yet inspected, not access gaps. This boundary does not establish their detailed correctness. |
| `docs/` | Included: `docs/architecture.md`, `docs/host-integration.md`, `docs/cli-reference.md`, `docs/overview.md`, `docs/overview.zh.md`, `docs/redaction-and-privacy.md`. Architecture, user procedure, host interface and privacy doctrine. | Architecture and host integration read in full; other documents identified in the tree but not yet read. No operational success inferred from documentation. |
| `README.md` | Included: intended use, installation, user invocation and declared status. | Read in full; claims are attributed intent, not observed operation. |
| `README.zh.md` | Included: Chinese-language product documentation. | Available but not yet inspected; no claim of cross-language consistency. |
| `pyproject.toml` | Included: packaging, executable entry point, dependencies and test configuration. | Read in full. Declares Python >=3.11 and DuckDB 1.5.3; external dependency implementation is not inspected. |
| `assets/` | Excluded: `assets/logo.svg`, `assets/qiju-rag-cag-animation-en.gif`, `assets/qiju-rag-cag-animation.gif`, presentation media. | Deliberate exclusion; prevents assessing the visual comparisons or treating animations as execution evidence. Does not remove a state-loop responsibility. |
| `LICENSE` | Excluded: legal license text. | Deliberate exclusion; no legal interpretation supplied. |
| `NOTICE` | Excluded: attribution notice. | Deliberate exclusion; no attribution-compliance assessment supplied. |

The tracked tree contains no test directory or evaluator implementation, despite the test path declared in SRC-1, `pyproject.toml`. That absence bounds this run's evaluation evidence; it does not establish that upstream testing never occurred. The retrospective instructions in SRC-1, `src/qiju/init_cmd.py`, are included as a shipped review procedure, not a benchmark or observed evaluation.

### External boundary and time

The frozen evidence is the entire SRC-1 repository at commit `a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89`, with applicability cutoff 2026-11-08. HEAD was checked against the acquired revision. No other revision, live page, linked demo, issue, package release or repository is admitted. Overall evidence is code-grounded, with source-native documentation and prompt intent distinguished from executable behavior.

External hosts (Claude Code, Codex, Kiro and Cursor), their models, session context, tool permissions and skill-discovery behavior are outside the source boundary. Qiju's generated instructions and installation paths are inside it. This prevents conclusions about actual host compliance, recall quality or cross-host handoff success. Python, DuckDB, Git used for root discovery, and the local filesystem are external dependencies; their implementation and runtime durability are not demonstrated by this source inspection. User record stores and actual sessions were not supplied, so no observed-run or causal-experiment evidence supports effectiveness, performance, privacy completeness or failure recovery. These are evidence limits, not inaccessible shipped source paths.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/jasonshrepo/qiju` | a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/qiju-9b7c9ef79e6f/related-systems/jasonshrepo--qiju`. Implementation: tracked tree, `pyproject.toml`, full CLI/capture/storage/search/maintain bodies, prompt rendering and local installation in `src/qiju/init_cmd.py`; function/import survey of support and lifecycle modules listed above. Doctrine/design: `README.md`, `docs/architecture.md`, `docs/host-integration.md`, embedded log/search/review instructions. | Implementation: [entry point](https://github.com/jasonshrepo/qiju/blob/a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89/pyproject.toml), [capture](https://github.com/jasonshrepo/qiju/blob/a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89/src/qiju/capture.py), [retrieval](https://github.com/jasonshrepo/qiju/blob/a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89/src/qiju/search.py), [maintenance](https://github.com/jasonshrepo/qiju/blob/a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89/src/qiju/maintain.py). Doctrine/design and installation: [skills](https://github.com/jasonshrepo/qiju/blob/a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89/src/qiju/init_cmd.py), [host boundary](https://github.com/jasonshrepo/qiju/blob/a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89/docs/host-integration.md), [architecture](https://github.com/jasonshrepo/qiju/blob/a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89/docs/architecture.md). | No known checkout access gap. Uninspected available files are identified above. No supplied host traces, actual record stores, evaluator implementation or experiments: source supports implementation and declared intent, not observed effectiveness or causal improvement. |
