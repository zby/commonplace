---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "DocMason's repo-native knowledge application and shipped agent workflows at commit f3970939593194a158ab7ea1d49995f06cbccc86."
run-id: AAS-2026-10-13-docmason-deba9ae199d5-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: f3970939593194a158ab7ea1d49995f06cbccc86
analysis-cutoff: "2026-10-13"
evidence-tier: code-grounded
source:
  identity: https://github.com/JetXu-LLM/DocMason
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/docmason-deba9ae199d5/related-systems/JetXu-LLM--DocMason
  revision: f3970939593194a158ab7ea1d49995f06cbccc86
  sha256: null
---

# DocMason boundary

## Boundary and evidence

This run analyses the shipped repo-native knowledge application: private-document compilation, agent-authored enrichment, validation and publication, retrieval and provenance tracing, ordinary question handling, conversation-derived memory, and local maintenance and evaluation. Its intended use is to explain how the repository supplies persistent evidence and governs host-agent work over that evidence. It is not an analysis of the enclosing Codex or Claude runtime.

The target class is **memory/knowledge/context-engineering system**, rather than enclosing runtime or merely a returning parser. Its model-dependent operation is supplied through authored agent contracts and canonical skills consumed by an external host. The deterministic Python program is only part of that operating surface. The target itself describes the inference boundary as follows (SRC-1, `README.md`):

> **All AI inference traffic** is handled by your chosen host agent (Codex, Claude Code, etc.) — DocMason itself makes zero model API calls. The network behavior of your AI agent is governed by that agent's own privacy and telemetry policy.
> --- `README.md`

This is a declared contract, not an observed network audit. Host model inference, vendor privacy policy, tool permissions, scheduling and actual instruction adherence remain external responsibilities. Their exclusion prevents conclusions about host isolation, inference confidentiality, or reliable enforcement of every authored rule.

The boundary kind is **whole-system** for the repo-native knowledge application, including its shipped drivers and consumers. Initial inspection traced both executable entries: the installed `docmason` command in `pyproject.toml` and module invocation through `src/docmason/__main__.py`. Both reach `src/docmason/cli.py`, which dispatches public deterministic operations and hidden `_ask` and `_hook` host wrappers. The ordinary host path is authored in `AGENTS.md` and `skills/canonical/ask/SKILL.md`; the `_ask` implementation opens persisted turns in `src/docmason/host_integration.py` through `src/docmason/ask.py`. These shipped callers are included, not classified as excluded enclosing applications (SRC-1).

The state loop includes document discovery and staged evidence building, source-level semantics and additive overlays, validation-derived retrieval and trace indexes, publication, later evidence consumption, and interaction-memory promotion. Inspection followed `src/docmason/knowledge.py` into `src/docmason/interaction.py` and `src/docmason/retrieval.py`: sync builds staged interaction memories, validation builds reader indexes, successful publication marks interaction entries promoted, and readers reload published records. This minimum implementation passage establishes the admission-to-publication edge (SRC-1):

> published_manifest = publish_staging(
>     paths,
>     validation_report,
>     rebuild_telemetry=rebuild_telemetry,
> )
> phase_costs["publish"] = perf_counter() - publish_started
> published = True
> published_signature = current_signature
> promoted_result = mark_promoted_interaction_entries(paths, target="current")
> --- `src/docmason/knowledge.py`

The containing branch admits validation statuses `valid` or `warnings`; this is an executable gate, not evidence that a real corpus passed it. Later consumption includes published retrieval records and promoted interaction contexts, as well as the separate pending-interaction overlay. Ordinary answers remain host-authored, with repository-owned turn and trace handling around them. The authored contract expressly includes the deeper evidence loop (SRC-1, `skills/canonical/ask/SKILL.md`):

> `ask` owns front-door legality, same-turn governance, workspace gating, and routing.
> The routed inner workflow owns the deeper evidence loop.
> --- `skills/canonical/ask/SKILL.md`

The public sample driver is included: `scripts/use-sample-corpus.py` explicitly copies a preset into the live corpus and can invoke bootstrap and sync. The hidden evaluator is also included despite not being the recommended product path: `src/docmason/operator_eval.py` dispatches suite runs, regression review, candidate promotion and baseline freezing; `src/docmason/evaluation.py` consumes current knowledge and replays ask, retrieve and trace cases. The tracked examples are schema aids, not retained experimental results (SRC-1, `sample_corpus/README.md`, `docs/workflows/operator-eval.md`, and the named implementation paths).

### Top-level tracked coverage

All rows refer to SRC-1 at the frozen commit. Included means within the functional boundary, not that every file has been read. Initial inspection covers the material entry and state-loop paths named below; inventory-only and deliberate exclusions are marked separately. No required local source path was inaccessible.

| Top-level tracked path | Treatment and material paths | Role and limit |
|---|---|---|
| `.claude/` | Included; `.claude/CLAUDE.md`, `.claude/settings.json` inspected; hook wrappers inventoried | Claude routing and optional capture/continuation plumbing. Host activation is not observed. |
| `.codex/` | Included; `.codex/hooks.json`, `.codex/hooks/on-prompt.sh` inspected; stop wrapper inventoried | Codex host hooks invoking the shared Python core; not a separate knowledge authority. |
| `.githooks/` | Excluded deliberately; `pre-commit`, `pre-push`, `README.md` inventoried | Contributor Git checks. No conclusion about installed hook enforcement. |
| `.github/` | Copilot instructions included and inspected; workflow files excluded deliberately | Host adaptation belongs to the application; CI, release publication and badge maintenance do not establish knowledge-loop behavior or successful releases. |
| `.gitignore` | Included; inventory-only | Persistence visibility and private-state tracking rules remain to be inspected; no claim about complete leakage prevention. |
| `AGENTS.md` | Included and inspected | Canonical routing, agent responsibility, evidence boundaries and maintenance instructions. |
| `CONTRIBUTING.md` | Excluded deliberately | Contributor process; no conclusion about actual development practice. |
| `LICENSE` | Excluded deliberately | Legal licensing; no license-compliance assessment. |
| `README.md` | Included and inspected | Product intent, host and dependency declarations; marketing claims are not run evidence. |
| `SECURITY.md` | Excluded deliberately | Security reporting policy; no security assurance assessment. |
| `adapters/` | Included; tracked `.gitkeep` only | Generated adapter destination; no generated user adapter instance is present to verify. Authored host mappings and adapter-generation code remain in scope. |
| `docmason.yaml` | Included and inspected | Workspace, persistence, agent, ingestion and publication defaults; declarations may differ from implementation. |
| `docs/` | Included; `architecture/README.md`, `workflows/operator-eval.md` inspected; workflow, setup and networking references inventoried | Application architecture and operator guidance. Product screenshots, badges and artwork are deliberately excluded from operational evidence; they cannot establish successful operation. |
| `knowledge_base/` | Included; tracked `.gitkeep` only | Staging and current publication destinations. No generated corpus is supplied, preventing observed publication-quality conclusions. |
| `ops/` | Excluded deliberately; `release-entry/README.md` inspected for role; Worker, SQL and deployment config inventoried | Ancillary update metadata/activity service, not corpus truth. No backend behavior, deployment or actual network-traffic conclusion. |
| `original_doc/` | Included; tracked `.gitkeep` only | Live private input destination. No private documents are supplied, preventing conclusions about real-user corpus handling. |
| `pyproject.toml` | Included and inspected | Package command entry, dependencies and Python requirements. |
| `runtime/` | Included; tracked `.gitkeep` only | Answers, turns, logs, memory ingest, control-plane and evaluation destinations; no execution trace or live maintenance artifacts supplied. |
| `sample_corpus/` | Included; `README.md` inspected; ICO/GCS manifest, text and Office/PDF fixtures inventoried | Shipped public input fixture set. Individual binary contents have not been inspected; no claim about sample extraction fidelity. |
| `scripts/` | Included; `use-sample-corpus.py` driver inspected and bootstrap call sites searched; other scripts inventoried | Corpus materialization, environment preparation, host context and update drivers remain in scope. Release packaging, badge/version maintenance and contributor checks are deliberately excluded from knowledge-loop conclusions. |
| `skills/` | Included; canonical `ask`, `knowledge-base-sync`, `knowledge-construction`, `grounded-answer` inspected; other canonical workflows and operator/optional skills inventoried | Model-consumed prompts, maintenance and evidence-consumption instructions; includes operator-eval and public-sample setup, not only Python APIs. |
| `src/` | Included; `docmason/cli.py`, `__main__.py`, `host_integration.py`, `knowledge.py`, `interaction.py`, `retrieval.py`, `operator_eval.py`, `evaluation.py` traced through bounded implementation reads; supporting modules inventoried/searched | Deterministic persistence, admission, sync, reader and evaluator implementation, plus host integration and derived projections. Full module audit is not claimed. Release-service implementation is ancillary and excluded from knowledge-loop claims. |
| `tests/` | Included; subsystem inventory and operator-eval suite wiring inspected | Authored checks for source builds, ask/composition, host hooks, interaction memory, retrieval, evaluation and workspace behavior. Test bodies require further inspection for individual assertions; no tests were executed. Release/backend contract tests do not establish knowledge-loop operation. |

External dependencies include the selected host agent and its model, shell/file/image capabilities, Python and parser libraries, and LibreOffice for Office rendering. Their implementations are not registered sources. Setup may rely on package/download infrastructure; released-bundle updating and its deployment backend are ancillary, deliberately outside this knowledge-application boundary. This prevents end-to-end installation, third-party parser correctness and deployed update/privacy conclusions, without excluding the shipped local preparation and update entry paths themselves (SRC-1, `pyproject.toml`, `README.md`, `skills/canonical/knowledge-base-sync/SKILL.md`).

The immutable reviewed boundary is commit `f3970939593194a158ab7ea1d49995f06cbccc86`, verified as the supplied checkout's HEAD with no reported working-tree changes. The applicability cutoff is the supplied run date, **2026-10-13**; it does not claim that upstream stayed unchanged until that date. Overall evidence is **code-grounded**, combining bounded implementation inspection with attributed design and instruction text. No target program, test, example, provider call or service was executed. Empty private-state destinations and absent host traces are evidence gaps, not failures to inspect available files. They prevent observed-run, efficacy and causal conclusions.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/JetXu-LLM/DocMason` | f3970939593194a158ab7ea1d49995f06cbccc86 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/docmason-deba9ae199d5/related-systems/JetXu-LLM--DocMason`. Implementation: bounded entry/dispatch, ask-wrapper, staged admission/publication, interaction marking/reload, retrieval reload and evaluator reads in the paths above; sample driver and host wrapper. Doctrine/design: README, AGENTS, configuration, canonical skills, host mappings, architecture, sample and operator-eval guidance. Whole tracked tree inventoried; listed inspection is not an evidence allowlist. | Implementation: [CLI dispatch](https://github.com/JetXu-LLM/DocMason/blob/f3970939593194a158ab7ea1d49995f06cbccc86/src/docmason/cli.py), [knowledge loop](https://github.com/JetXu-LLM/DocMason/blob/f3970939593194a158ab7ea1d49995f06cbccc86/src/docmason/knowledge.py), [interaction memory](https://github.com/JetXu-LLM/DocMason/blob/f3970939593194a158ab7ea1d49995f06cbccc86/src/docmason/interaction.py), [retrieval](https://github.com/JetXu-LLM/DocMason/blob/f3970939593194a158ab7ea1d49995f06cbccc86/src/docmason/retrieval.py), [evaluation](https://github.com/JetXu-LLM/DocMason/blob/f3970939593194a158ab7ea1d49995f06cbccc86/src/docmason/evaluation.py). Doctrine/design: [agent contract](https://github.com/JetXu-LLM/DocMason/blob/f3970939593194a158ab7ea1d49995f06cbccc86/AGENTS.md), [canonical ask](https://github.com/JetXu-LLM/DocMason/blob/f3970939593194a158ab7ea1d49995f06cbccc86/skills/canonical/ask/SKILL.md), [README](https://github.com/JetXu-LLM/DocMason/blob/f3970939593194a158ab7ea1d49995f06cbccc86/README.md). | Local tracked source is available. No private corpus, generated KB, live runtime/evaluation artifacts or host trace supplied: implementation/design only, not observed effectiveness, host compliance or causal improvement. Deliberate ancillary exclusions and uninspected available material are distinguished in the coverage table. |
