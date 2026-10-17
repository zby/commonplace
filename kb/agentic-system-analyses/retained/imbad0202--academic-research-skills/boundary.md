---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "academic-research-skills research, writing, screening and review workflows at frozen Git revision 060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a."
run-id: AAS-2026-10-17-academic-research-skills-6fe859d62c16-01
result-disposition: complete
target-class: workflow
boundary-kind: whole-system
reviewed-boundary: "060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a"
analysis-cutoff: "2026-10-17"
evidence-tier: code-grounded
source:
  identity: https://github.com/Imbad0202/academic-research-skills
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-academic-research-skills/related-systems/Imbad0202--academic-research-skills
  revision: 060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a
  sha256: null
---

# academic-research-skills boundary

## Boundary and evidence

This run covers the shipped academic research workflow package, not an enclosing model runtime. Its intended use is research exploration, literature screening, manuscript writing, review, revision, integrity checking and finalization. The target class is **workflow**: model-operated skills and role prompts supply the substantive work and orchestration; scripts supply supporting state, verification, transport and evaluation mechanisms. It is in scope because its operation depends on model interpretation and execution of those prompts, not merely on returning a deterministic computation. SRC-1, `academic-pipeline/SKILL.md`, `academic-paper-reviewer/SKILL.md`, `sr-screener/SKILL.md`, `package.json`.

> A lightweight orchestrator that manages the complete academic pipeline from research exploration to final manuscript. It does not perform substantive work — it only detects stages, recommends modes, dispatches skills, manages transitions, and tracks state.
> --- `academic-pipeline/SKILL.md`

The **whole-system** boundary includes all five skill families, standalone command entry paths, shipped agent roles, supporting references and templates, Claude plugin integration, the Pi adapter, literature importers, retained state and its consumers, verification helpers, optional cross-model paths, and evaluation/maintenance tooling. It does not narrow the target to a verification library or to the four skills listed by the root Pi manifest. The separately shipped `sr-screener` remains part of the target. SRC-1, `.claude-plugin/plugin.json`, `package.json`, `sr-screener/SKILL.md`, `docs/ARCHITECTURE.md`.

### Entry points and state-loop coverage

The initial trace establishes these shipped responsibilities; it does not certify every branch or check every implementation:

- **Enter and dispatch.** `/ars-full` directs the host to load `academic-pipeline`; that skill selects stages, dispatches research/writing/review skills and waits at user checkpoints. The root package manifest exposes four skill directories, command prompts and `pi/wrapper.js`. The wrapper transforms recognized `/ars-*` input into command text, persists ARS activation using custom session entries and reloads that state on session start/tree changes. The Claude hook manifest connects session startup and guarded tool use to shipped scripts. SRC-1, `commands/ars-full.md`, `academic-pipeline/SKILL.md`, `package.json`, `pi/wrapper.js`, `hooks/hooks.json`.
- **Produce and admit literature state.** The folder adapter creates passport entries and a rejection log from scanned files. The screening reporter writes screened records as corpus entries. The two literature consumers screen the supplied corpus and combine admitted records with external search results; they are not excluded merely because their input was prepared out of band. SRC-1, `scripts/adapters/folder_scan.py`, `sr-screener/scripts/build_outputs.py`, `deep-research/agents/bibliography_agent.md`, `academic-paper/agents/literature_strategist_agent.md`, `docs/ARCHITECTURE.md`.
- **Maintain and reload workflow state.** The state tracker specifies conversational state, while its recovery rule refers to an on-disk run ledger. `append_entry` validates the existing chain and named files under a lock before atomically replacing ledger bytes. The optional passport reset protocol halts at a boundary and specifies fresh-session resume from retained artifacts. These prompts, their callers and their persistence helpers are inside the boundary. SRC-1, `academic-pipeline/agents/state_tracker_agent.md`, `scripts/run_ledger.py`, `academic-pipeline/references/passport_as_reset_boundary.md`, `academic-pipeline/agents/pipeline_orchestrator_agent.md`.
- **Verify and consume outputs.** The standalone passport verifier loads YAML and invokes the verification gate with resolver clients and optional persistent cache; it refuses ordinary output without a prose-sourced reference join. The orchestrator's final-output pre-check connects finalizer/audit results to formatter refusal conditions before finalization. Research, review, revision, integrity reports and final process records are workflow outputs/inputs, not an excluded application layer. SRC-1, `scripts/verify_passport.py`, `scripts/verification_cache.py`, `academic-pipeline/agents/pipeline_orchestrator_agent.md`, `academic-paper/agents/formatter_agent.md`, `docs/ARCHITECTURE.md`.
- **Evaluate and improve.** Gold-set task discovery, measurements, report comparison and regression checking are shipped supporting paths. Their inclusion permits later examination of what was actually measured; this boundary makes no performance or causal claim from their presence. SRC-1, `evals/README.md`, `scripts/run_evals.py`.

Minimum passages supporting the loop classification:

> write_passport(args.passport, entries)
> --- `scripts/adapters/folder_scan.py`

> When the input Material Passport carries a non-empty `literature_corpus[]`, this agent enters the **corpus-first, search-fills-gap** flow. The flow has five steps and four Iron Rules; the PRE-SCREENED block makes corpus utilisation reproducible. The merged `final_included` set feeds the Annotated Bibliography, Literature Matrix, Research Gap Identification, and Recommended Sources by Paper Section sections above without altering their formats.
> --- `academic-paper/agents/literature_strategist_agent.md`

> entry["hash"] = entry_hash(entry)
> entries.append(entry)
> payload = yaml.safe_dump(data, sort_keys=False, allow_unicode=True).encode("utf-8")
> atomic_replace(path, payload)
> --- `scripts/run_ledger.py`

> When the tracker's state and the ledger's report disagree after compaction or resume, a decision follows `references/pipeline_state_machine.md` § Checkpoint decision provenance, a step outcome follows the report's `step_outcomes`, which gives a receipt's recorded outcome only while its input files are unchanged (#898), and a counter takes the higher of the two values for its stage, so a lost count cannot reopen a retry or loop limit.
> --- `academic-pipeline/agents/state_tracker_agent.md`

### Top-level tracked coverage

The tracked tree was enumerated at the frozen revision. “Included” means inside the functional analysis boundary, not that every file has already been read. Initial substantive reads and searches are identified above and in the register. Remaining files are available for later source inspection; they are not access gaps. Grouped rows enumerate every top-level tracked name.

| Top-level file or directory | Boundary treatment and material paths/role | Inspection status; exclusion consequence |
|---|---|---|
| `academic-pipeline/` | Included: `SKILL.md`, `agents/pipeline_orchestrator_agent.md`, `agents/state_tracker_agent.md`, integrity/audit/observer roles, state machine, reset and process protocols, templates | Entry, state, reset and final-output paths initially inspected; other protocol branches available |
| `deep-research/` | Included: `SKILL.md`, research/source-verification/synthesis roles, `agents/bibliography_agent.md`, search and research protocols/templates | Corpus-consumer search and architecture trace initially inspected; detailed research branches available |
| `academic-paper/` | Included: `SKILL.md`, intake, literature, draft, revision, citation and formatter roles; writing and revision protocols/templates | Literature-consumer and formatter surfaces initially inspected; other writing branches available |
| `academic-paper-reviewer/` | Included: `SKILL.md`, field analyst, panel roles, synthesizer, full/re-review/calibration contracts | Skill entry and architecture trace inspected; detailed panel dispatch/contracts available |
| `sr-screener/` | Included: skill, protocol/reviewer/QC/reporter roles, `scripts/build_workflow.py`, `merge_decisions.py`, `build_outputs.py`, screening prompts/templates | Skill workflow search and corpus emission code inspected; other screening branches available |
| `agents/` | Included: plugin-exposed research architect, synthesis, report compiler and screening reviewer prompt surfaces | Tracked inventory inspected; prompt bodies available, not yet inspected |
| `commands/`, `skills/` | Included: slash-command dispatch and skill discovery projections | `commands/ars-full.md` and skill inventory inspected; other commands/projections available |
| `.claude-plugin/`, `.claude/`, `hooks/`, `pi/`, `package.json` | Included: plugin/marketplace packaging, checkout routing, hook launcher/guard, Pi manifest/wrapper/tests, root discovery manifest | Plugin manifest, hook manifest, root manifest and complete Pi wrapper inspected; remaining adapter files available |
| `scripts/` | Included: `adapters/`, verification gate/cache/clients, run ledger, passport maintenance, finalizer/audit and cross-model helpers, guard, checkers, tests and fixtures | Folder producer, ledger append, verifier and representative evaluation/state consumers inspected; detailed helpers remain available |
| `shared/` | Included: `handoff_schemas.md`, passport/evidence/reviewer/revision contracts, routing and trust rules, cross-model protocols, policy and authority registries | Responsibilities traced through inspected consumers and architecture; contract bodies remain available |
| `evals/`, `plugin-evals/`, `plugin-evals-citation-check/`, `plugin-evals-citation-locale/`, `tests/` | Included: gold and heldout corpora, harness manifests, prompt graders, fixtures, recorded results and regression tests | Tracked inventory and `evals/README.md` inspected; task discovery/report code searched; individual result validity not assessed |
| `docs/`, `examples/`, `audits/` | Included as evidence/support: `docs/ARCHITECTURE.md`, setup/data-flow/capability documents, design specs, workflow examples and source-native audit records | Architecture through corpus flow inspected; remaining documentation, example runs and audits not yet inspected. No observed-run or causal result claimed from their inventory |
| `.github/`, `tools/`, `.command-invariants.toml`, `pyproject.toml`, `requirements-dev.txt`, `requirements-pdf-content-classifier.txt` | Included: CI, release discipline, dependency/build and validation configuration | Tracked inventory inspected; detailed CI/release execution not assessed |
| `README.md`, `README.es-ES.md`, `README.ja-JP.md`, `README.ko-KR.md`, `README.zh-CN.md`, `README.zh-TW.md`, `QUICKSTART.md`, `MODE_REGISTRY.md`, `POSITIONING.md`, `CHANGELOG.md` | Included as declared usage, mode inventory and release context | Inventory inspected; full prose not yet inspected, so no compatibility or historical-progress conclusion follows |
| `CITATION.cff`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `LICENSE`, `NOTICE.md`, `SECURITY.md`, `THIRD_PARTY.md`, `.gitattributes`, `.gitignore`, `.gitleaks.toml`, `.gitleaksignore` | Excluded from substantive mechanism analysis: citation, governance/legal/security policy and repository hygiene metadata | Deliberate exclusion, not unavailable evidence; prevents conclusions about licensing compliance, governance effectiveness or secret-detection effectiveness |

### External dependencies and limits

The enclosing Claude Code/Pi runtimes, model providers, user decisions, external scholarly indexes, user-owned papers/corpora and optional renderers are external dependencies. Their shipped adapters and invocation instructions remain included. Runtime scheduling, model inference, provider service behavior, actual user compliance and external corpus truth are not attributed to this package. Python/PyYAML and optional Pandoc/tectonic capabilities are visible in the wrapper's dependency probes; resolver clients are constructed by the passport verifier. SRC-1, `pi/wrapper.js`, `scripts/verify_passport.py`, `docs/ARCHITECTURE.md`.

Host differences constrain enforcement conclusions. The wrapper explicitly reports:

> "Claude hooks: unavailable in Pi; write-scope enforcement remains prompt-level",
> --- `pi/wrapper.js`

Thus the boundary does not equate a prompt requirement, a Claude tool hook, a deterministic helper and host-level isolation. The implementation tier is **code-grounded** because executable entry, persistence and verification code was inspected; substantive model-role instructions are **doctrine/design**, not evidence that a particular model obeyed them. No target code, tests, examples, providers or external APIs were executed. No supplied trace was independently established as an observed run, and no experiment was performed. These are evidence limits, not source-access failures.

The frozen revision is **060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a** and the applicability cutoff is **2026-10-17**, the supplied run date. The acquired checkout's HEAD matched that revision and its status was clean when inspected. Only that Git object supplies source evidence; later repository changes, linked external papers/pages and live service results are outside this run. There is no additional capture or source repository.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Imbad0202/academic-research-skills` | 060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-academic-research-skills/related-systems/Imbad0202--academic-research-skills`. Implementation: complete `pi/wrapper.js`, `package.json`, `hooks/hooks.json`, `scripts/verify_passport.py`; bounded source in `scripts/adapters/folder_scan.py`, `scripts/run_ledger.py`, `sr-screener/scripts/build_outputs.py`; searches of `scripts/verification_cache.py` and `scripts/run_evals.py`. Doctrine/design: `commands/ars-full.md`, `.claude-plugin/plugin.json`, opening portions of `academic-pipeline/SKILL.md`, `academic-paper-reviewer/SKILL.md`, `docs/ARCHITECTURE.md` through corpus flow; bounded orchestrator source and searches of tracker/reset, screening and literature-consumer instructions; complete `evals/README.md`. Full tracked tree enumerated. These are initial reads, not an allowlist. | Implementation: [Pi adapter](https://github.com/Imbad0202/academic-research-skills/blob/060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a/pi/wrapper.js), [ledger](https://github.com/Imbad0202/academic-research-skills/blob/060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a/scripts/run_ledger.py), [verifier](https://github.com/Imbad0202/academic-research-skills/blob/060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a/scripts/verify_passport.py). Doctrine/design: [pipeline](https://github.com/Imbad0202/academic-research-skills/blob/060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a/academic-pipeline/SKILL.md), [architecture](https://github.com/Imbad0202/academic-research-skills/blob/060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a/docs/ARCHITECTURE.md). | No checkout access gap identified. Not-yet-inspected files are available, not excluded. Host/provider internals and user-owned inputs are outside the frozen source; no end-to-end execution, model compliance, research accuracy, performance uplift or causal effectiveness is established by this boundary. |
