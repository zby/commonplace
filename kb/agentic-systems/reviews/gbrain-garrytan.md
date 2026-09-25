---
type: types/note.md
description: "GBrain adds provenance-carrying memory, deterministic context push, nightly maintenance and hash-guarded skill delivery to existing agent harnesses; its fact curation catches near duplicates, not contradictions."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-23-gbrain-01
source-identity: https://github.com/garrytan/gbrain
reviewed-revision: "6040075c6cb95be5881cc2e1b76ef7d71f4e5d29"
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-23-gbrain-01/result.md
analysis-result-sha256: e07b4133703a2594672dd77ac8b6906e6d1173f83b658e0165b42f4f1885f2b1
---

# GBrain

**Evidence basis:** Static code and committed documentation at `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29` (v0.54.1.0), inspected on 2026-09-23. No system was executed. Host harness internals, model providers, the closed-source Memorable CLI, the separate evals repository and the author's deployment were not inspected.

GBrain is a memory and context service for agents that already exist. It stores pages and provenance-carrying facts in PGLite or Postgres, keeps Markdown files canonical for file-backed pages, and serves one operation contract through a CLI and MCP servers. Around that core it adds retrieval and cited synthesis, automatic context push through harness hooks, background maintenance through a nightly cycle and a durable job queue, and a large skill set whose distribution is a product surface in its own right. The host harness keeps the agent loop, so nothing in this review establishes that a host used what GBrain delivered. The [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-23-gbrain-01/result.md) retains the source excerpts, route records and fourteen comparison fields.

## How agent-facing parts reach harnesses

| Mechanism | What is delivered | How updates and local edits are handled | Records |
|---|---|---|---|
| Claude and Codex plugins | A generated skill tree, persona variants, an MCP server started by a launcher (`serve --surface starter --source-guard`) | CI regenerates the tree and fails on any byte difference. Each release force-pushes a history-less `codex-plugin` branch. No hooks, and no runtime version check of an installed plugin. Refresh is up to the host marketplace. | RTE-13, ABS-1, ABS-5 |
| Workspace scaffold | Copies of skills and shared conventions | Copies once and never overwrites. A reference lens shows diffs but cannot tell a local edit from upstream change. | RTE-14 |
| Harness bridge | Copies in the harness's native skills directory, with a SHA-256 per written file | A three-way comparison separates `upstream_drift` from `local_edit`. Only proven drift is applied. Removal touches only recorded files. | RTE-15 |
| Stub skills | Frontmatter kept locally; the body replaced by an instruction to call `get_skill` or `gbrain skill` | Text is fetched at use time from the serving brain host's skill source. "Always current" means current relative to that host. | RTE-15, CLM-4 |
| Shared brain skills | Versioned skills stored in the brain, a hash-checked local cache, and a router skill | Compare-and-set publication, separate editor and publisher grants, and hash-checked delivery. Edited managed files stop following. The source itself calls router activation advisory and unverified. | RTE-16 |
| Bootstrap and in-agent installs | Identity templates, a marker-delimited instruction block, marker-keyed hooks, MCP registrations | Receipts record owned files and hashes, so reruns, upgrades and uninstall touch only what GBrain wrote. | RTE-17 |

Upgrade ties these together (RTE-18). The CLI prints a machine marker when a newer version exists. `gbrain upgrade` swaps the binary and applies migrations, then lists new and drifted scaffolded skills without overwriting them. Sources: [plugin manifest](https://github.com/garrytan/gbrain/blob/6040075c6cb95be5881cc2e1b76ef7d71f4e5d29/.claude-plugin/plugin.json), [release job](https://github.com/garrytan/gbrain/blob/6040075c6cb95be5881cc2e1b76ef7d71f4e5d29/.github/workflows/release.yml), [harness bridge](https://github.com/garrytan/gbrain/blob/6040075c6cb95be5881cc2e1b76ef7d71f4e5d29/src/core/skillpack/harness-bridge.ts), [shared-skills adapter](https://github.com/garrytan/gbrain/blob/6040075c6cb95be5881cc2e1b76ef7d71f4e5d29/src/core/shared-skills/adapter.ts), [instruction block](https://github.com/garrytan/gbrain/blob/6040075c6cb95be5881cc2e1b76ef7d71f4e5d29/src/core/bootstrap/instructions-block.ts), [upgrade](https://github.com/garrytan/gbrain/blob/6040075c6cb95be5881cc2e1b76ef7d71f4e5d29/src/commands/upgrade.ts).

## Memory and what reaches the agent

Facts are the main retained unit. They require a provenance string, which nothing verifies, and they are written both to a page's `## Facts` fence, which is canonical, and to the database. Automatic capture runs from four lanes:

- compaction segments (on by default in the bootstrap lane);
- opt-in per-turn writeback;
- session-end transcripts processed by a maintenance sweep;
- page writes.

Extracted facts reach later sessions through requested reads and through push. That makes trace learning wired. Push is deterministic: lexical entity matching, session identity and recency choose what gets injected, never an embedding or model call. Pushed content is world-visible only and labelled "data, not instructions". In a bootstrapped workspace, the agent also keeps standing rules in `MEMORY.md`, which the harness imports as instructions every session. Exact records: OBJ-2, OBJ-14, RTE-5, RTE-6, RTE-9, RTE-24, BAP-8.

Fact curation handles near duplicates, not contradictions:

- `remember` supersedes an old fact only at cosine ≥ 0.95 with the same entity, visibility and kind.
- Extraction lanes never supersede.
- The LLM contradiction classifier has no non-test caller, although an operation description still advertises it (CLM-7).
- Consolidation copies the highest-confidence text of a fact cluster into a take and makes no model call.

Contradicting facts can therefore sit side by side until someone withdraws one. Withdrawal keeps history and refuses re-assertion of the same claim. Sources: [fact decision](https://github.com/garrytan/gbrain/blob/6040075c6cb95be5881cc2e1b76ef7d71f4e5d29/src/core/facts/single-prepare.ts), [consolidate](https://github.com/garrytan/gbrain/blob/6040075c6cb95be5881cc2e1b76ef7d71f4e5d29/src/core/cycle/phases/consolidate.ts), [turn context](https://github.com/garrytan/gbrain/blob/6040075c6cb95be5881cc2e1b76ef7d71f4e5d29/src/core/context/turn-context.ts). Exact records: RTE-1, RTE-7, RTE-9, OBJ-18.

## Maintenance, checks and self-revision

The nightly cycle writes derived pages without review: synthesis from transcripts (only when a corpus directory is configured), pattern pages, and optional enrichment. Its synthesis check repairs quoted spans against the source transcript; it does not test the synthesized claims. LLM-proposed takes wait for human acceptance, and LLM take grades are cached rather than applied unless an operator opts in. No general rollback exists for cycle writes (ABS-3). Exact records: RTE-8, RTE-10, RTE-21.

SkillOpt is the one route with an external answer oracle: a benchmark the skill author supplies.

- *Proposal.* An optimizer model reads failure trajectories, the scoring criteria and previously rejected edits, then proposes surgical edits to a `SKILL.md`, each tied to an observed failure.
- *Acceptance.* An edit is accepted only when the median judge score beats the current best by more than 0.05.
- *Human gates.* The nightly path only writes proposals. Bundled skills need a held-out set and an explicit flag. Shared skills publish through editor authority.

This is operative use and criticism of a formulated procedure against stated consequences. No retained run shows an improvement, so improved capacity, and hence [conjectural learning](../../notes/definitions/conjectural-learning.md), stays unestablished at this boundary. Health remediation and SkillOpt scores give narrow [reflective](../../notes/definitions/reflective-system.md) loops over brain health and skill performance. No route revises how GBrain itself builds theories. Sources: [accept rule](https://github.com/garrytan/gbrain/blob/6040075c6cb95be5881cc2e1b76ef7d71f4e5d29/src/core/skillopt/validate-gate.ts), [reflect prompt](https://github.com/garrytan/gbrain/blob/6040075c6cb95be5881cc2e1b76ef7d71f4e5d29/src/core/skillopt/reflect.ts), [nightly phase](https://github.com/garrytan/gbrain/blob/6040075c6cb95be5881cc2e1b76ef7d71f4e5d29/src/core/skillopt/cycle-phase.ts). Exact records: RTE-11, OBJ-10, CLM-2, CLM-9.

## Controls and limits

Remote MCP callers pass through surface filters, OAuth scope checks, stdio-only restrictions on local operations, and a source guard for writes. They see only world-visible facts and cannot persist synthesis. The trusted local CLI, `gbrain call`, Markdown sync and serve-side harvest all run as local callers, and direct SQL is outside the protocol by the source's own statement. The source also documents that local files and shared credentials do not isolate agents (RTE-22, CLM-6).

This static boundary supports conclusions about what GBrain writes, selects and delivers. It cannot establish:

- host activation of skills, hooks or instruction blocks;
- extraction fidelity;
- measured benefit of recall (ABS-7);
- SkillOpt gains;
- the reported benchmark and scale figures (CLM-1, CLM-3).

Host traces, retained SkillOpt runs and a fidelity check of extracted facts against their sources would change these assessments.
