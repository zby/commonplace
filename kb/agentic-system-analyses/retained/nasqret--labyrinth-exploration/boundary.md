---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "The Labyrinth Exploration research skill and its shipped project tooling at commit 019a93da59313e697dc6f28bcfe1588a376c7565."
run-id: AAS-2026-11-23-labyrinth-exploration-4000731242d4-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "019a93da59313e697dc6f28bcfe1588a376c7565"
analysis-cutoff: "2026-11-23"
evidence-tier: code-grounded
source:
  identity: https://github.com/nasqret/labyrinth-exploration
  kind: git
  path: /mnt/bigdisk/commonplace/worktrees/labyrinth-exploration-f7a1b59e9b29/related-systems/nasqret--labyrinth-exploration
  revision: "019a93da59313e697dc6f28bcfe1588a376c7565"
  sha256: null
---

# Labyrinth Exploration boundary

## Boundary and evidence

Labyrinth Exploration is a skill for advancing open-ended research in mathematics, theoretical science and algorithms. It is a **memory/knowledge/context-engineering system**: a model acting as coordinator follows a shipped protocol for choosing questions from a durable research map, obtaining and checking new results, updating the map, and reusing it in later sessions and agent briefs. Its Python engine handles project files; it neither launches those agents nor verifies their mathematical claims. The distinction is visible in the skill's rule for admitting results and in the engine's separate `check` and `build` commands (SRC-1 `SKILL.md`, `references/codex.md`, `templates/lab.py`).

> - **Referee before consuming.** Results from agents or external models enter the notes,
>   the state-of-the-art table or the graph as established only after an independent
>   referee and your own spot check. Apply the referee's corrections; noting them is not
>   enough.
> --- `SKILL.md`

The **whole-system** boundary is the shipped skill, not the enclosing client and not just the engine. The installed skill and Codex metadata direct the coordinator to project-local files. The coordinator and campaign agents generate evidence and reports; the coordinator saves reports, records events and decides what updates the canonical research state after review. The example scripts exercise both initial state production and a later update. The CLI appends events and reloads the graph, events, frontier and state-of-the-art inputs for checks and derived outputs. The browser template consumes the embedded build data, while the session and campaign instructions direct the coordinator and agents back to the map, saved reports, journal and write-ups. Source-level tests exercise the copy into a project, updates, checks and output generation (SRC-1 `agents/openai.yaml`, `SKILL.md`, `references/loop.md`, `references/campaigns.md`, `examples/triangle-counts/README.md`, `examples/triangle-counts/exhaustive_n8.py`, `templates/lab.py`, `templates/dashboard.html`, `tests/test_lab.py`).

> Your computation scripts write frontier.json (and scatter.json); the engine itself contains nothing
> specific to a domain.
> --- `templates/lab.py`

**External dependencies and evidence limits.** Codex or Claude Code supplies skill loading, model inference, tools, permissions and agent lifecycle. Its internals are outside the boundary, so the skill's instructions and discovery checks do not establish actual routing, delegation, isolation or permission enforcement by a host. The project supplies its proofs, computations, optional blueprint, notes, journal and agent archive; only their shipped interfaces and example are in scope. This prevents conclusions about the correctness or completeness of any private research project. No cluster, literature service or private deployment is pinned; actual job execution, source access and hosting privacy are not established. Local build uses Python's standard library; the exhaustive tutorial adds NumPy, and browser rendering references external D3 and fonts. Those environments and dependencies were not exercised, so the boundary does not establish live rendering or portability beyond the source contracts (SRC-1 `references/codex.md`, `references/compute.md`, `templates/lab.py`, `templates/dashboard.html`, `examples/triangle-counts/exhaustive_n8.py`).

**Freeze.** The evidence is the tree at commit `019a93da59313e697dc6f28bcfe1588a376c7565`, with applicability cutoff 2026-11-23. No other revisions, repositories, captures or external documents are admitted. The overall evidence tier is **code-grounded** for inspected executable paths. Prompts, requirements and testing procedures establish intended operation; retrospective campaign descriptions are reported operation. No target execution was performed for this boundary (SRC-1).

| Top-level tracked path | Coverage and role | Exclusion or inspection limit |
|---|---|---|
| `.github/` | Included as evaluation: `.github/workflows/tests.yml` configures the unit suite on pushes and pull requests. | Workflow definition, not CI results. |
| `.gitignore` | Excluded: checkout ignore rules, not part of research-state management. | No account of which local files a given checkout omits from Git. |
| `CHANGELOG.md` | Excluded: release history rather than the pinned implementation. | No conclusions about earlier versions or migration behavior. |
| `LICENSE` | Excluded: licensing terms, not runtime or protocol. | No license analysis. |
| `MAINTAINING.md` | Included as package maintenance and test routing, distinct from maintenance of a research project. | No release or deployment was observed. |
| `README.md` | Included as entry and orientation documentation: installation, example setup, requirements and operating scope. | Describes intended use, not an observed client run. |
| `SKILL.md` | Included: host-facing method, state setup and resumption, review and integration rules, session handoff. | Instructions are not host enforcement. |
| `agents/` | Included: `agents/openai.yaml` declares Codex display and invocation metadata. | Selection behavior remains a host responsibility. |
| `assets/` | Excluded: explanatory SVGs (`assets/hero.svg`, `assets/loop.svg`, `assets/tiers.svg`, `assets/campaign.svg`) and preview/screenshot PNGs, not project state or the shipped dashboard implementation. | No visual fidelity or screenshot reproduction claims. |
| `docs/` | Included: `docs/tutorial.md` documents setup, reload, review, update and handoff; `docs/codex-testing.md` separates engine tests, native discovery and proposed live tests. | A test recipe is not a transcript. |
| `examples/` | Included: `examples/README.md` and `examples/prompts.md` route use; `examples/triangle-counts/README.md` ties `examples/triangle-counts/knowledge.json`, `examples/triangle-counts/events.jsonl` and `examples/triangle-counts/sota.json` to `examples/triangle-counts/make_example.py`, `examples/triangle-counts/exhaustive_n8.py` and the CLI/browser outputs. | Fixture contents are not fully inventoried here. Referenced referee reports are not bundled, so fixture review labels do not establish review. |
| `references/` | Included: `references/codex.md` adapts host operation; `references/loop.md` and `references/campaigns.md` govern production, admission and reuse; `references/schema.md` documents the files; `references/compute.md`, `references/saturation.md` and `references/lessons.md` cover compute, escalation and reported experience. | Initial inspection followed the loop and client paths and located the other contracts; it is not an exhaustive reading of every reference. |
| `templates/` | Included: `templates/briefs/attack.md`, `templates/briefs/referee.md`, `templates/briefs/writer.md` shape the handoffs; `templates/lab.py` appends, reloads, checks and builds; `templates/dashboard.html` reads the embedded data for display. | Initial inspection traced entry points and key consumers, not every branch, brief field or view. |
| `tests/` | Included as evaluation: `tests/test_lab.py` covers classification and project setup, state updates and diagnostics; `tests/test_skill.py` and `tests/test_codex.py` cover package consistency and metadata. | Test source, not outcomes. |
| `tools/` | Included as evaluation: `tools/codex_smoke.py` exercises native discovery; excluded as presentation tooling: `tools/make_graphics.py` and `tools/screenshots.py` generate documentation assets. | No native discovery result or visual reproduction conclusion. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/nasqret/labyrinth-exploration` | 019a93da59313e697dc6f28bcfe1588a376c7565 | implementation; doctrine/design; reported operation | Access root `related-systems/nasqret--labyrinth-exploration/`. Implementation: tracked tree, CLI load/append/build/check/status paths, browser data and view hooks, example producer/update paths and their project tests, CI and discovery entry point. Doctrine/design: `SKILL.md`, `agents/openai.yaml`, client and iteration references, campaign and artifact guidance, tutorial and validation entry points. Reported operation: campaign and review anecdotes in `references/campaigns.md`. | Implementation: [CLI](https://github.com/nasqret/labyrinth-exploration/blob/019a93da59313e697dc6f28bcfe1588a376c7565/templates/lab.py), [dashboard](https://github.com/nasqret/labyrinth-exploration/blob/019a93da59313e697dc6f28bcfe1588a376c7565/templates/dashboard.html), [project tests](https://github.com/nasqret/labyrinth-exploration/blob/019a93da59313e697dc6f28bcfe1588a376c7565/tests/test_lab.py). Doctrine/design: [skill](https://github.com/nasqret/labyrinth-exploration/blob/019a93da59313e697dc6f28bcfe1588a376c7565/SKILL.md), [Codex adapter](https://github.com/nasqret/labyrinth-exploration/blob/019a93da59313e697dc6f28bcfe1588a376c7565/references/codex.md). Reported operation: [campaign account](https://github.com/nasqret/labyrinth-exploration/blob/019a93da59313e697dc6f28bcfe1588a376c7565/references/campaigns.md). | Implementation: host internals and live execution evidence are outside the pin; no observed host or test behavior. Doctrine/design: project-specific files and example referee reports are not supplied; no actual admission or review compliance conclusion. Reported operation: underlying campaign traces and comparison conditions are not supplied; no independent reconstruction or causal estimate of effectiveness. |
