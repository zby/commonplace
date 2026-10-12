# AI Research OS Workshop rerun audit

## Disposition

**Integrate with recorded limits.** No consequential defect requiring a hold was established in this bounded audit. The publication already distinguishes prompt-directed research retention from successful execution, factual acceptance and improved capacity. Its unresolved lint-result inventory is explicitly retained as a local comparison limit, not silently certified.

No patch, advance, integration, commit or delegation was performed. The orchestrator still owns integration checks.

## Identity and comparison boundary

- Auditor: fresh independent `openai/gpt-6.1-sol`, medium reasoning, confirmed by `PI_PROVIDER`, `PI_MODEL` and `PI_REASONING_LEVEL`; session `01a1324f-62c0-778a-80e2-c7ac782bd5a5`.
- Audit date: 2026-10-12.
- Worktree `W`: `/home/zby/llm/commonplace/.commonplace/worktrees/ai-research-os-workshop-1a93869f8e7f`.
- Run `R`: `W/kb/agentic-system-analyses/state/AAS-2026-10-12-ai-research-os-workshop-1a93869f8e7f-01`.
- Frozen method: `c3a339786c62631c66b22c72f6a6ceca8e5ce45a`.
- Source: `https://github.com/iusztinpaul/ai-research-os-workshop`, revision `dc6660555266239cd36483cf51b5ab39febacf02`, under `W/related-systems/iusztinpaul--ai-research-os-workshop`.
- Publication `P`: `W/kb/agentic-system-analyses/retained/ai-research-os-workshop/`.
- Historical lead: [legacy review](../../../agent-memory-systems/reviews/ai-research-os-workshop.md), checked fully. It names the same source revision, so revision drift does not explain differences. Its Commonplace borrowing recommendations were not acceptance requirements, and its classifications were not treated as truth.
- Contract: [audit a rerun](../audit-a-rerun.md), read fully, and the workshop's auditor/profile and ownership rules.

## Consequential findings

### Public qualifications are adequate

`P/overview.md` describes a persistent, progressively queried wiki but explicitly withholds factual acceptance and improved capacity. `P/synthesis.md`, especially “A research-memory plugin, not an enclosing runtime,” “Later consumption and criticism,” and its limitations table, makes host ownership, lack of observed execution, advisory criticism, unresolved handoffs and incomplete accumulation visible. The overview's deterministic-pass list expressly disclaims semantic certification.

The legacy account's main architectural coverage survives: topic-local files, layered source/wiki/catalog retention, request routing, personal-source discovery, writer fan-out, deterministic navigation, optional human preservation, query save-back, lint, distill and render. The new synthesis adds materially useful qualifications rather than merely removing favorable claims.

### Two consequential legacy leads survive direct source checks

1. **GitHub delivery mismatch remains visible.** Frozen `plugins/ai-research-os/skills/research/agents/builder.md` lines 97–108 creates `wiki/repos/<repo-slug>` but copies staged specifications into `raw/<repo-slug>` and returns a wiki architecture pointer. `CONVENTIONS.md` lines 76–77 places GitHub specifications only under wiki. The new synthesis and its limitations table retain this seam; curated specifications are not mistaken for a complete code snapshot.
2. **Query save-back is not a coherent blanket read-only contract.** Frozen `research/SKILL.md` lines 109–255 prohibits ordinary wiki mutation at entry, then Q.5 instructs knowledge-document enrichment and a slim question pointer. `CONVENTIONS.md` lines 319–332 permits question-page additions for query save-back. `P/runtime.md` record `RT-RTE-query-answer` and the public synthesis retain the conflict and separately identify the stricter missing-YAML read-only fallback. This improves on treating the legacy pointer pattern as an unqualified working feature.

### Structural checking remains distinct from acceptance

Frozen `research-lint/agents/lint_judge.md`, read fully, forbids raw reads, caps full-page reads at eight, returns stale claims without writes, and appends contradictions/questions without rewriting old entries. The synthesis accurately describes bounded wiki-only criticism, flags for human judgment and no demonstrated criticism-to-revision-to-capacity chain.

`P/report-verification.md` retains the undeclared structural-diagnostic, stale-result and durable/transient parts as a local limit. `P/synthesis.md` carries the same qualification publicly. It prevents homogeneous part-level storage, retention and evaluator comparisons; it does not erase the separately supported mechanical/advisory distinction. I did not independently reconstruct every missing part.

### Small historical coverage losses do not establish a blocker

The legacy review explicitly warns that the always-loaded YAML catalog has no declared size bound. The new account describes the catalog and bounded downstream reads but does not explicitly repeat that scaling warning. Frozen Q.2 requires loading the canonical catalog and Q.3 bounds deeper disclosure, not the catalog itself. This is a useful historical detail to retain in the audit, not a repair to a false public guarantee: the new synthesis claims neither a globally bounded context budget nor demonstrated context-efficiency benefit.

The legacy Claude Code-specific packaging warning is also less explicit. The new boundary includes the plugin manifests and keeps host deployment outside the inspected implementation; it does not claim native Codex packaging or demonstrated host interchangeability. No consequential portability guarantee was found to contradict the legacy warning.

## Operational checks and evidence locators

Source HEAD equals the frozen revision; `git status --short` in the source checkout returned no changes. A read-only SHA-256 comparison checked all 13 publication files against `R/effects/publish.json`; all matched. That receipt records `state: completed`, with no prior publication replaced.

Trace `T` is `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-12T21-33-58-556Z_01a13209-639b-76ed-b2e9-63d8ee289902.jsonl`. Its line 157, message `7928ba86`, contains the returned coordinator handle `88f5dc89-3776-4e6c-b276-8dba3847a364` and nested worker messages under `message.details.jobs[0].result.messages`. Array indices below are zero-based within that coordinator message array.

I paired validation calls with actual tool results in each analytical worker, rather than counting tool proposals or trusting publication success. Passing `commonplace-run validate-output` results are present for all 13 model jobs: boundary, runtime, memory, epistemic, workflow, reconciliation, report verification, both memory-profile rounds, both profile verifications, synthesis and synthesis verification. Each uses the worktree command path and its own prompt path in a separate shell call. These are member-content passes, not job acceptance or claim support.

- Runtime worker: coordinator messages `[20].details.results[0].messages`; initial validation reports invalid condition-status values. Later result `[70]`, paired with `call_12SpIME69UCsthLPn9Fl3u6c|fc_06dbb65a8621c54f016acd5654265087d2b8d6f10f692fc817`, passes. This is repaired deterministic feedback, not a retained worker failure.
- Corrected memory profile: `[44].details.results[0].messages`; its complete invocation is retained in the read result, and result `[76]`, paired with `call_rtTK70UwXAJH0GTxI0p2dilY|fc_051f141e7a51d63e016acd6026e3e887d2b95a84ce2d219db3`, passes.
- Final profile verification: `[48].details.results[0].messages[67]`, paired with `call_HbWXjqeg9teDaUOPeOguLHiw|fc_0c39711e8086b3d7016acd611c02a087d29490edfb2452d508`, passes.

`R/state/attempts/000028-memory-profile.json` pins the prior profile refusal; `R/state/judgments/000031-apply-profile-verification-0.json` accepts the final verifier and cites the corrected profile hash `11f54e96fa6904282aa28c700de4a884f8338b660a135246e52d6cffcf1306c4`. `P/profile-verification.md` identifies the corrected authority, direction/signal and local inventory issues and lists no blockers. The second round is therefore not evidence of an unsupported coordinator retry or an ignored objection.

The live `R/state/handouts/000028-memory-profile/prompt.md` was unavailable at audit time. I recovered its complete invocation from the nested trace rather than reconstructing it or rerunning a closed worker check. This audit does not certify every worker read, truncation recovery or action from the validation results alone.

Run-specific validation, executed with `W` as cwd:

```text
.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/ai-research-os-workshop
VALIDATION SUCCESS
Target: kb/agentic-system-analyses/retained/ai-research-os-workshop
Scope: kb/agentic-system-analyses/retained/ai-research-os-workshop
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

## Coverage limits and unblock

This was a bounded audit, not a second whole-system analysis. I read the overview, synthesis, boundary, report/profile verification and historical review fully; searched specialist coverage; inspected selected runtime records; directly checked query, builder, conventions and lint-judge source; and examined validation call/result pairs and selected run judgments/receipt. I did not recheck every declaration, execute target code or connectors, inspect all generated examples, audit external hosts/services, or prove runtime benefit. No source access gap was established for the selected checks.

**Unblock:** none. Integrate without removing the published execution, acceptance, accumulation, host-boundary and coarse lint-part qualifications. Integration remains an orchestrator action, not an effect of this report.

## Report validation

`commonplace-validate kb/work/agentic-system-reruns/audits/rolling-06-ai-research-os-workshop.md` returned `VALIDATION SUCCESS`: one text file, zero failures and zero warnings.
