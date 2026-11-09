---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "KHMS memory's shipped capture, proposal, review, maintenance and retrieval loop at commit f739eb976dab199fd4cd64e352192cc0b112c047."
run-id: AAS-2026-11-08-khms-memory-c5267e800c56-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: f739eb976dab199fd4cd64e352192cc0b112c047
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/ksx-cz/khms-memory
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/khms-memory-6b2eaa00ba9d/related-systems/ksx-cz--khms-memory
  revision: f739eb976dab199fd4cd64e352192cc0b112c047
  sha256: null
---

# KHMS memory boundary

## Boundary and evidence

KHMS is in scope as a file-based long-term memory system serving LLM agents, not as the enclosing agent runtime. Its intended use is to retain evidence-linked knowledge across sessions and bring relevant retained knowledge back into an agent's context. The target is the whole shipped KHMS system: operational instructions, model-stage prompts, shell drivers, Python helpers, Claude Code hook integration, maintenance tools and evaluators. The separately deployed agent CLI supplies model execution; that does not make the shipped drivers external to KHMS. SRC-1: `README.md`, `AGENTS.md`, `claude-code/README.md`, `tools/nightly_distill.sh`, `tools/permark.py`.

The source declares the memory and admission design:

> Around that storage layer sits the part
> that makes it work in practice — **hook-driven recall** that pushes relevant cards into the
> session before the agent asks for them, and a **propose → review → approve** pipeline in
> which background jobs may only propose and nothing enters the knowledge directory unreviewed.
> --- `README.md`

This is a whole-system boundary rather than a retrieval-library boundary. Initial tracing covers the paths that produce journal and generated MARK records, prepare model inputs, retain proposals and checkpoints, admit reviewed cards, regenerate views, later retrieve cards, and propose or apply maintenance. It includes the prescribed human/agent actions as doctrine, without treating their performance as observed operation:

- **Capture and proposal:** journal MARK instructions in `AGENTS.md`; transcript/git generation and durable generated records in `tools/nightly_distill.sh`; the generator prompt in `tools/prompts/nightly-generate.md`; queue evaluation through `tools/permark.py` and `tools/prompts/nightly-marks.md`. The driver calls the evaluator and commits its post-checked output into carry batches; the current route is not inferred solely from the older sweep/consolidate description in the specification. SRC-1: those paths, including `tools/nightly_distill.sh`'s generator commit and MARK-stage call sites.
- **Admission and persistence:** `tools/approve_inbox.py` maps temporary IDs to allocated IDs, writes card files, records review completion, updates relations and invokes `tools/build_views.py`; the latter validates cards and generates views and `MEMORY.md`. Review authorization is an operational requirement, not evidence that every invocation has received human approval. SRC-1: `tools/approve_inbox.py`, `tools/build_views.py`, `AGENTS.md`.
- **Later consumption:** the shipped `tools/recall.sh` enters `tools/khms_recall_hybrid.py`; the hook loads retained cards through the search layer, runs selection, saves session state and emits context. `claude-code/settings.hooks.json` supplies the actual example event wiring. `spec/bootstrap-digest.md` and `AGENTS.md` prescribe loading the generated index and explicit recall. SRC-1: those paths and `tools/khms_hook.py`.
- **Maintenance and distribution:** include nightly retry/carry and ledger machinery, weekly synthesis and its prompts, triage and reviewed application, daily validity proposals, archive/erratum tooling, version-history access and read-only export. Representative initial inspection covers `tools/nightly_distill.sh`, `tools/weekly_synthesis.sh`, `tools/prompts/weekly-synthesis.md`, `tools/khms_triage.py`, `tools/apply_triage.py`, `tools/khms_validity_daily.sh`, `tools/khms_archive.py`, `tools/khms_versions.py` and `tools/khms_export.sh`. The remaining helpers at this same pin remain included evidence for subsequent tracing, not excluded responsibilities.
- **Evaluation:** include synthetic tests, the production-path retrieval evaluator, injection-use measurement guidance and historical triage experiment tooling. These are evaluation designs and attributed reports, not test results observed in this run. SRC-1: `tests/test_night_pipeline.py`, `tests/test_onboarding.py`, `tools/eval/run_eval.py`, `docs/measuring-injection.md`, `tools/khms_experiments/README.md`.

The model dependence is visible in the evaluator's shipped command construction, rather than inferred from its name:

> def claude_cmd(agent, model, rules, effort=None):
>     return [agent, "-p", "--model", model, "--output-format", "json", "--tools", "",
>             "--system-prompt", rules, "--setting-sources", "", "--strict-mcp-config",
>             "--no-session-persistence", "--effort", effort or EFFORT]
> --- `tools/permark.py`

The return path into model context is explicit:

> def emit(event, text):
>     print(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": text}}))
> --- `tools/khms_hook.py`

### Tracked-tree coverage

Every top-level tracked file or directory is classified below. “Included” denotes functional and evidentiary scope, not a claim that every line has already been inspected. Material entry points and their consumers were initially traced above; individual helper internals not yet inspected remain available at the same registered commit.

| Top-level tracked path | Coverage | Role and material paths | Limit or conclusion prevented |
|---|---|---|---|
| `.github/` | Included | `workflows/test.yml`: dependency installation, boundary scan and synthetic test command | Inspected CI definition, not a CI execution or proof of green status. |
| `.gitignore` | Included | Separates runtime base artifacts from the code repository | Does not establish the state or contents of any deployed base. |
| `AGENTS.md` | Included | Bootstrap, journal capture, review, explicit retrieval, calibration and generated-index consumption instructions | Prescribed agent behavior is not observed compliance. |
| `LICENSE` | Included | MIT distribution terms | Administrative evidence, not operational support. |
| `README.md` | Included | System purpose, current pipeline account, configuration, updates and maintenance entry points | Reference-deployment claims remain attributed reports. |
| `claude-code/` | Included | `README.md` and `settings.hooks.json`: host dependencies, cron recipe and hook event wiring | A wiring example does not establish a real harness installation. |
| `docs/` | Included | `measuring-injection.md`: measurement methods, reference-deployment numbers and replay narrative | No underlying deployment trace or controlled experiment was acquired. |
| `examples/` | Included | `README.md`, `K-00002.md`–`K-00009.md`, sample inbox/journal and `golden_set.jsonl`: fictional miniature base and retrieval labels | Landing inspected; individual fixture contents remain available for later inspection. These are not real retained memories or outcome evidence. |
| `requirements.txt` | Included | Core PyYAML requirement and optional dense-stack dependency note | No installed environment was tested. |
| `spec/` | Included | `khms-spec.md` and `bootstrap-digest.md`: card schema, evidence/link semantics, review rules and instructions propagated through the generated index | Declared contracts may lag code; neither specification alone nor bootstrap text establishes current implementation. |
| `tests/` | Included | Synthetic suites for capture, night/weekly carry, approval, hooks, recall, links, shared writers, archive and versions; initial reads of `test_night_pipeline.py` and `test_onboarding.py` | Other test internals are not yet inspected; no tests were executed. Tests using fake agent CLIs cannot establish real-model quality. |
| `tools/` | Included | Capture/preprocessing; `nightly_distill.sh`, `permark.py`, `generated_marks.py`, ledger/batch helpers; `approve_inbox.py`, view/index builders; `khms_hook.py`, recall/search/select, embedding daemon; weekly/triage/validity/archive/erratum/version/export tools; `prompts/`; `eval/`; `khms_experiments/` | Initial inspected slices establish the loop and entry-point relationships, not exhaustive correctness of every helper. No shipped responsibility is deliberately excluded. |

### External boundary and evidence limits

The frozen evidence is SRC-1 at full commit `f739eb976dab199fd4cd64e352192cc0b112c047`, with applicability cutoff **2026-11-08**. The acquired checkout's HEAD matched that pin and its status was clean at initial inspection. Evidence is **code-grounded**: shipped source establishes inspectable control flow, while operational instructions establish intent. No target code, test, model call or example was executed.

External dependencies are the enclosing Claude Code/headless-agent runtime and its providers; Python/PyYAML and Linux shell utilities; the deployment scheduler and credentials; optional embedding libraries/model artifacts; and optional Nextcloud/DAV storage history. KHMS's shipped integration and client code remain included, but dependency implementation is outside SRC-1. This prevents conclusions about host scheduling guarantees, actual model behavior, embedding quality, or storage-service durability. SRC-1: `claude-code/README.md`, `requirements.txt`, `tools/permark.py`, `tools/embed_server.py`, `tools/khms_versions.py`.

The real memory base, private configuration and prompt extensions, deployment transcripts/logs, historical server versions and experiment answer caches were not acquired. These are unavailable evidence, not deliberately omitted shipped paths. Their absence prevents verifying reference-deployment performance numbers, successful recovery, actual review adherence, completeness of captured knowledge, and the usefulness of cards in later real decisions. `docs/measuring-injection.md` provides reported operation, not the underlying trace. The examples and fake-agent tests cannot fill that gap. External links in documentation are not additional registered sources and were not followed. SRC-1: `docs/measuring-injection.md`, `examples/README.md`, `tests/test_night_pipeline.py`, `tools/khms_experiments/README.md`.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/ksx-cz/khms-memory` | f739eb976dab199fd4cd64e352192cc0b112c047 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/khms-memory-6b2eaa00ba9d/related-systems/ksx-cz--khms-memory`. Tracked tree enumerated. Implementation: entry-point and call-site slices in `tools/khms_hook.py`, `tools/recall.sh`, `tools/khms_recall_hybrid.py`, `tools/approve_inbox.py`, `tools/build_views.py`, `tools/nightly_distill.sh`, `tools/permark.py`, `tools/weekly_synthesis.sh`; maintenance/configuration/evaluator slices listed above; synthetic test slices in `tests/test_night_pipeline.py` and `tests/test_onboarding.py`. Doctrine/design: root documentation, both spec files, Claude Code documentation/settings, generator prompt and MARK/weekly prompt excerpts, examples landing, workflow/dependency files and experiment README. Reported operation: reference-deployment narrative and metrics in `README.md`, `claude-code/README.md`, `docs/measuring-injection.md`. | Implementation: [nightly driver](https://github.com/ksx-cz/khms-memory/blob/f739eb976dab199fd4cd64e352192cc0b112c047/tools/nightly_distill.sh), [per-mark evaluator](https://github.com/ksx-cz/khms-memory/blob/f739eb976dab199fd4cd64e352192cc0b112c047/tools/permark.py), [approval](https://github.com/ksx-cz/khms-memory/blob/f739eb976dab199fd4cd64e352192cc0b112c047/tools/approve_inbox.py), [hook](https://github.com/ksx-cz/khms-memory/blob/f739eb976dab199fd4cd64e352192cc0b112c047/tools/khms_hook.py). Doctrine/design: [bootstrap instructions](https://github.com/ksx-cz/khms-memory/blob/f739eb976dab199fd4cd64e352192cc0b112c047/AGENTS.md), [specification](https://github.com/ksx-cz/khms-memory/blob/f739eb976dab199fd4cd64e352192cc0b112c047/spec/khms-spec.md). Reported operation: [measurement account](https://github.com/ksx-cz/khms-memory/blob/f739eb976dab199fd4cd64e352192cc0b112c047/docs/measuring-injection.md). | No missing material shipped path was identified. Uninspected helper details remain within the registered source. External runtime/provider implementation, deployed base/configuration, raw deployment traces, server history and private experiment evidence are unavailable; no observed-run or causal-experiment layer is established. This prevents real-world effectiveness, compliance, durability and causal improvement conclusions. |
