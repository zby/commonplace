---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "SoL-Pi's standalone Pi extension and shipped integration examples at commit 41fa7e0e230bedc5e639aed2e7b9cc5698726db1."
run-id: AAS-2026-10-14-sol-pi-42f04fbbc6bb-01
result-disposition: complete
target-class: extension or tool mechanism
boundary-kind: whole-system
reviewed-boundary: "41fa7e0e230bedc5e639aed2e7b9cc5698726db1"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/NVlabs/SoL-Pi
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/sol-pi-42f04fbbc6bb/related-systems/NVlabs--SoL-Pi
  revision: "41fa7e0e230bedc5e639aed2e7b9cc5698726db1"
  sha256: null
---

# SoL-Pi boundary

## Boundary and evidence

This run examines how SoL-Pi changes a model-driven agent's tool execution, observation replay, diagnostic-log consumption and context maintenance. The target is the standalone extension plus the integration paths shipped in this repository, not the upstream Pi runtime or the research process that originally discovered the mechanisms. The target class is **extension or tool mechanism**. Its operation serves Pi's model loop and, for diagnostic reduction, issues an additional model call through Pi's registry. The boundary kind is **whole-system** relative to this repository's shipped SoL-Pi responsibilities, not a claim to cover the enclosing hosts.

The frozen evidence is SRC-1 at `41fa7e0e230bedc5e639aed2e7b9cc5698726db1`, with applicability cutoff **2026-10-14**. The checkout's HEAD matches that pin, and the tracked-worktree status was clean when inspected. The evidence tier is **code-grounded**: entry points, state producers, admission checks, persistence, reload and consumption paths were inspected as source. No target code, test, example, model call or service was executed. Test source is implementation evidence for the evaluator's design, not an observed successful run. Compatibility and benchmark statements in documentation remain attributed reports.

### Entry points and functional inclusions

The package declares `src/sol-pi/index.ts` as its Pi extension. That entry reads the effective configuration at `session_start` and conditionally registers the four mechanisms. This is a host-loaded extension, rather than an enclosing agent runtime (SRC-1, `package.json`, `src/sol-pi/index.ts`, `src/sol-pi/config.ts`).

> "pi": {
> 	"extensions": [
> 		"./src/sol-pi/index.ts"
> 	]
> },
> --- `package.json`

> export function registerConfiguredFeatures(pi: ExtensionAPI, config: SolPiConfig): void {
> 	if (config.actionFusion) registerActionFusion(pi);
> 	if (config.observationPack) registerObservationPack(pi);
> 	if (config.evidencePreservingReducer) {
> --- `src/sol-pi/index.ts`

The included core paths are:

- **Action Fusion:** replacement `edit` and `write` definitions, optional follow-up shell execution, queue/path handling and result presentation. Its caller is the host's model-selected tool invocation; the actual base tools and shell are supplied by Pi (SRC-1, `src/sol-pi/extensions/action-fusion/index.ts`, `src/sol-pi/extensions/action-fusion/then-run.ts`, `src/sol-pi/extensions/action-fusion/file-queue.ts`).
- **ObservationPack:** eligibility and object identity, local archive creation, projected placeholders, replay accounting, paged `obs_recall` and JSONL ledger. The `context` event consumes stored tool-result messages without replacing their persisted history; recall later reads the archived object (SRC-1, `src/sol-pi/extensions/observation-pack/index.ts`, `src/sol-pi/extensions/observation-pack/observation.ts`, `src/sol-pi/extensions/observation-pack/ledger.ts`).
- **Evidence-Preserving Reducer:** diagnostic candidate selection, raw-log archives, reducer prompt and provider call, receipt admission, replacement tool results and decision journals. The resulting receipt points the agent to an archive path for exact readback; that readback uses the host's ordinary shell rather than a separate SoL-Pi recall tool (SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/index.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/candidate.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/archive.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/provider.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/journal.ts`).
- **Online Context Compact:** the model-facing plan tool and its guidance, plan-transition detection, economic/window-pressure selection, session-state append/restore, native compaction callbacks and automatic continuation. State restoration reads the active session branch. Compaction and the subsequent task turn belong to the same inspected extension path, rather than to an assumed external resumer (SRC-1, `src/sol-pi/extensions/online-context-compact/tools.ts`, `src/sol-pi/extensions/online-context-compact/extension.ts`, `src/sol-pi/extensions/online-context-compact/state.ts`, `src/sol-pi/extensions/online-context-compact/economics.ts`).

> export function appendOnlineState(pi: ExtensionAPI, state: OnlineState): void {
> 	pi.appendEntry(ONLINE_STATE_ENTRY, state);
> }
> --- `src/sol-pi/extensions/online-context-compact/state.ts`

> pi.sendMessage(
> 	{
> 		customType: "sol-pi-online-context-compact",
> 		content: compacted ? POST_COMPACTION_PLAN_REMINDER : SKIPPED_COMPACTION_REMINDER,
> 		display: false,
> 	},
> 	{ triggerTurn: true },
> );
> --- `src/sol-pi/extensions/online-context-compact/extension.ts`

Shared configuration, trust-dependent admission, runtime archive roots and TUI reporting are included. Session-directory and in-memory/no-session archive modes are both within scope (SRC-1, `src/sol-pi/config.ts`, `src/sol-pi/runtime-paths.ts`, `docs/configuration.md`, `docs/compatibility.md`).

The shipped examples are also included, despite not being in the package's default extension entry:

- **SoL-Pi Skill:** the Python launcher configures an isolated Pi agent directory, starts persistent or detached runs, records prompts/events/session paths, rereads those records for status and cost summaries, and reports the result back through Claude Code or Codex hooks. The transcript exporter selects and trims host conversation content; bundled skills describe a model-mediated fallback when hooks do not run. These are shipped producer/consumer and host-integration responsibilities, not excluded merely because they launch Pi as a subprocess (SRC-1, `examples/sol-pi-skill/bin/sol-pi-run`, `examples/sol-pi-skill/bin/sol-pi-context`, `examples/sol-pi-skill/probe/sol-pi-probe.ts`, `examples/sol-pi-skill/codex-hooks/hooks.json`, `examples/sol-pi-skill/claude-plugin/sol-pi/hooks/hooks.json`, `examples/sol-pi-skill/codex-skill/sol-pi/SKILL.md`, `examples/sol-pi-skill/claude-plugin/sol-pi/skills/sol-pi/SKILL.md`).
- **SoL-Pi Visual:** explicit extension loading, trusted-project configuration, model prompt guidance, `magnify` tool registration, image/receipt production and image readback are included. Blender's scene creation/rendering and visual grading are not implemented by this extension (SRC-1, `examples/solpi-visual/README.md`, `examples/solpi-visual/src/index.ts`, `examples/solpi-visual/src/scene/index.ts`, `examples/solpi-visual/src/scene/magnify.py`, `examples/solpi-visual/src/scene/policies.ts`).

> write_json(run_dir / 'result.json', result)
> return result
> --- `examples/sol-pi-skill/bin/sol-pi-run`

> if (run_dir / 'result.json').exists():
>     return json.loads((run_dir / 'result.json').read_text())
> --- `examples/sol-pi-skill/bin/sol-pi-run`

### External dependencies and excluded conclusions

Pi owns the enclosing agent/session loop, tool definitions, native summarization, provider registry/authentication, extension dispatch and trust API. Node.js, TypeBox and the Pi TUI support the extension; the skill launcher additionally uses Python and host transcript/hook conventions; Visual uses Python/Pillow and external scene/render tools (SRC-1, `package.json`, `src/sol-pi/extensions/evidence-preserving-reducer/provider.ts`, `examples/sol-pi-skill/README.md`, `examples/solpi-visual/README.md`). Only SoL-Pi's calls and declared expectations of those dependencies are covered. Their implementations are not frozen here, so this run cannot establish upstream runtime correctness, actual host hook delivery, live authentication behavior or cross-version compatibility independently.

The linked paper, blog, pricing pages and benchmark dataset are not part of the frozen source. No raw benchmark trajectories, live-provider results or intervention/comparison runs were supplied as separate evidence. This prevents independently establishing claimed savings, reconstruction quality or the causal effectiveness of the original auto-research process. Repository statements about those results may be cited only as reported operation, not as observed runs or causal experiments (SRC-1, `README.md`, `examples/solpi-visual/README.md`, `docs/compatibility.md`). Missing execution evidence does not make the source inspection incomplete.

### Top-level coverage

The table accounts for every top-level tracked file or directory at the pin. “Included” fixes functional scope; it does not assert that every leaf or test assertion has already been inspected. Named uninspected leaves are available evidence, not access gaps. All paths below belong to SRC-1.

| Top-level path | Classification and material paths | Role / inspection and limit |
|---|---|---|
| `.gitattributes` | Excluded; repository metadata | Deliberate exclusion; no conclusions about checkout attribute behavior. |
| `.github/` | Excluded; `.github/workflows/star-history.yml` | Tree identified the star-history workflow, outside agent-state operation; no CI or popularity-update correctness conclusion. |
| `.gitignore` | Excluded; repository metadata | Deliberate exclusion; no conclusion about ignored deployment artifacts. |
| `AGENTS.md` | Included; inspected | Agent-facing installation entry, routing to the canonical procedure. |
| `CLAUDE.md` | Included; inspected | Claude-facing import of the same installation procedure. |
| `CONTRIBUTING.md` | Included as maintenance doctrine; not yet inspected | Available contribution/benchmark policy; no assessment of that policy in this member. |
| `LICENSE` | Excluded | Legal terms are not evaluated; no licensing conclusion. |
| `README.md` | Included; inspected | Target identity, installation, mechanisms, archive policy, external-result claims. Claims are not execution evidence. |
| `SECURITY.md` | Included; inspected | Permission and sensitive-data contract; not a security audit. |
| `THIRD_PARTY_NOTICES.md` | Excluded | Legal attribution, not runtime behavior; no dependency-license conclusion. |
| `agents-install.md` | Included; inspected | Canonical agent installation/configuration/verification procedure; its commands were not run. |
| `assets/` | Excluded; `assets/sol-pi-hero.png` | Presentation image; no interpretation of image-only assertions. |
| `docs/` | Included: `docs/configuration.md` and `docs/compatibility.md` inspected; `docs/star-history.md` excluded | Config/trust, persistence/continuation contract and reported compatibility. Popularity documentation excluded; no popularity conclusions. |
| `examples/` | Included: `examples/README.md`; Skill launcher, exporter, probe, hooks and both skills; Visual entry, config, runtime paths, policies, tool and Python crop helper inspected | Includes state export, task/run records, summary reload, host result delivery and crop receipts/readback. Skill tests and plugin metadata are available but not yet inspected in detail; Visual result images are available but not yet inspected. No example runtime success or benchmark reproduction is claimed. |
| `package-lock.json` | Included as dependency pin; not yet inspected | Available dependency resolution evidence; no complete supply-chain assessment. |
| `package.json` | Included; inspected | Package extension entry, distribution file list, peer dependencies and test/check commands. |
| `scripts/` | Included: `scripts/check-sol-pi-config.mjs` and `scripts/check-pi-compat.mjs` inspected; `scripts/update-star-history.mjs` excluded | Configuration and public-API preflights included; star-history generation identified by search and deliberately excluded. No preflight execution or popularity pipeline result claimed. |
| `sol-pi.example.json` | Included as configuration template; not yet inspected | Available shipped example; executable config loader and documented schema inspected instead. No template-consistency verdict yet. |
| `src/` | Included: `src/sol-pi/index.ts`, config and runtime paths; all four `src/sol-pi/extensions/` mechanism paths | Inspected registration and material production, admission, persistence, reload and consumption paths described above. Queue, candidate and economics helpers searched; further detail remains available. TUI helper and some pure parsing/projection helpers not yet read in full; no exhaustive algorithm/security verdict. |
| `tests/` | Included: `tests/pi-package-integration.test.ts` inspected in full; `tests/all-mechanisms.test.ts` and `tests/online-context-compact-agent-session.test.ts` searched | Evaluators include deterministic provider/session integration, persistent/in-memory/no-session cases and compact/continue checks. Other mechanism, recovery, economics, stress, config and presentation suites identified in tree but not yet inspected in detail. No test-pass or exhaustive coverage claim. |
| `tsconfig.json` | Included as build configuration; not yet inspected | Available typecheck configuration; no typecheck-result claim. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/NVlabs/SoL-Pi` | 41fa7e0e230bedc5e639aed2e7b9cc5698726db1 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/sol-pi-42f04fbbc6bb/related-systems/NVlabs--SoL-Pi`. Implementation: package entry/config/runtime roots; four mechanism registrations, archive/recall, reducer provider/receipt/journal, OCC tools/state/continuation; both shipped example integration paths; configuration/API preflights and selected evaluator source. Doctrine/design: root README, agent installation entries/protocol, security, configuration/compatibility docs, both example READMEs and skills, Visual policies. Reported operation: documented compatibility checks and Visual result claims. The coverage table records exact initially inspected paths and available uninspected material; it is not a source allowlist. | Implementation: [extension entry](https://github.com/NVlabs/SoL-Pi/blob/41fa7e0e230bedc5e639aed2e7b9cc5698726db1/src/sol-pi/index.ts), [OCC loop](https://github.com/NVlabs/SoL-Pi/blob/41fa7e0e230bedc5e639aed2e7b9cc5698726db1/src/sol-pi/extensions/online-context-compact/extension.ts), [skill driver](https://github.com/NVlabs/SoL-Pi/blob/41fa7e0e230bedc5e639aed2e7b9cc5698726db1/examples/sol-pi-skill/bin/sol-pi-run), [package evaluator](https://github.com/NVlabs/SoL-Pi/blob/41fa7e0e230bedc5e639aed2e7b9cc5698726db1/tests/pi-package-integration.test.ts). Doctrine/design: [installation](https://github.com/NVlabs/SoL-Pi/blob/41fa7e0e230bedc5e639aed2e7b9cc5698726db1/agents-install.md), [configuration](https://github.com/NVlabs/SoL-Pi/blob/41fa7e0e230bedc5e639aed2e7b9cc5698726db1/docs/configuration.md). Reported operation: [compatibility](https://github.com/NVlabs/SoL-Pi/blob/41fa7e0e230bedc5e639aed2e7b9cc5698726db1/docs/compatibility.md), [Visual report](https://github.com/NVlabs/SoL-Pi/blob/41fa7e0e230bedc5e639aed2e7b9cc5698726db1/examples/solpi-visual/README.md). | No access gap to this checkout was encountered. Upstream Pi, enclosing hosts, linked paper/blog/dataset and live providers are outside this frozen source. No supplied raw execution or causal experiment establishes real-world savings, host delivery, compatibility or benchmark effectiveness independently; documentation supports attribution only. |
