---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "The instruction-only recall skill package (recall/) of Parcha-ai/parcha-skills at commit c82883b15e5e8f02483bee513b3c8dcac48e3c9e, without the separately distributed Recall engine it drives"
run-id: AAS-2026-11-05-parcha-skills-d5ad184aa4af-01
result-disposition: complete
target-class: "extension or tool mechanism"
boundary-kind: "complete artifact, partial loop"
reviewed-boundary: "c82883b15e5e8f02483bee513b3c8dcac48e3c9e"
analysis-cutoff: "2026-10-22"
evidence-tier: doc-grounded
source:
  kind: git
  identity: https://github.com/Parcha-ai/parcha-skills
  revision: "c82883b15e5e8f02483bee513b3c8dcac48e3c9e"
  path: /home/zby/llm/commonplace/.commonplace/worktrees/parcha-recall-d5ad184aa4af/related-systems/Parcha-ai--parcha-skills
  sha256: null
---

# Recall (parcha-skills) boundary

## Boundary and evidence

**Intended use.** `recall` is an agent skill for Claude Code, Codex and pi. It
instructs the agent to retrieve prior coding-agent sessions from a session-history
index, read only the best-supported part of a session, and then answer, continue,
repeat or turn the found work into a skill. The skill drives an engine that a
model-run agent calls; its operation consists of the model following the
instructions. It therefore falls in scope as a narrower mechanism of agent memory
retrieval and context engineering, not as a whole memory system (SRC-1,
`recall/skills/recall/SKILL.md`).

**Target and scope selection.** The caller restricts the target to the `recall/`
subtree; the other skills in the repository are context only. The package
declares itself instruction-only:

> Agent instructions for using a separately installed Recall system from Claude Code,
> Codex, or pi. This package contains the skill and plugin manifests. The implementation,
> installers, and deployment configuration are maintained separately and are not included.
> --- `recall/README.md`

> The Recall engine is distributed separately. This skill contains no executable
> implementation.
> --- `recall/skills/recall/SKILL.md`

The repository's own test enforces that the package holds only `.md`, `.json`,
`.yaml` and `LICENSE` files (SRC-1, `tests/test_portability.py`, test
`test_recall_and_tether_packages_contain_only_instructions`). The tree listing at
the reviewed commit confirms eight tracked files under `recall/`.

**Functional inclusions.**

- The skill procedure in `recall/skills/recall/SKILL.md`: interface selection
  (Recall MCP tools versus the local `RECALL_SCRIPT` CLI), the cold-start raw
  transcript scan with `rg`, outcome selection (find/verify, continue, repeat,
  skill-ify), search filters, evidence assessment through the `WHY` line,
  bounded reading through `show`, `related`, `session-export`,
  `session-relations`, index health, and the documented gotchas.
- The remote "central Brain" usage procedure in
  `recall/skills/recall/references/central-brain.md`, including deliberate
  capture through `recall_capture` and deletion through `recall_forget`.
- The query guidance in `recall/skills/recall/references/query-cookbook.md`.
- Packaging and discovery metadata: `recall/package.json`,
  `recall/.claude-plugin/plugin.json`, `recall/.codex-plugin/plugin.json`,
  `recall/README.md`, `recall/LICENSE`, and the repository-level registrations
  that expose the skill (`.claude-plugin/marketplace.json`,
  `.agents/plugins/marketplace.json`, root `package.json`).

**Functional exclusions and external dependencies.**

- *The Recall engine (`recall.py`), its SQLite index, ingest, ranking, entity
  index, redaction, retention watchdog and `session-export`/`session-relations`
  producers.* They are not in this repository at any path. The skill names the
  engine as a separately and privately distributed dependency. This prevents any
  implementation-level conclusion about how session state is produced, indexed,
  ranked, redacted or exported. Every statement about engine behavior (exact
  identifier matching, the evidence gate, thinking blocks never being stored,
  secret-shaped line redaction, incremental indexing) is available only as the
  skill's declared contract (`doctrine/design`), not as inspected behavior.
- *The central Recall Brain service and its MCP tools* (`recall_search`,
  `recall_show`, `recall_session_context`, `recall_exec`, `recall_capture`,
  `recall_forget`). These are private and absent. This prevents conclusions
  about cross-device storage, write admission, visibility enforcement, import
  connectors and deletion semantics beyond what the skill instructs the agent to
  do.
- *The host harnesses* (Claude Code, Codex, pi) that load the skill and produce
  the transcripts under `~/.claude/projects` and `~/.codex/sessions`. Their
  transcript formats and retention (`cleanupPeriodDays`) are external inputs; the
  target does not own them, and their responsibilities are not attributed to it.
- *The harness skill creator* used by the skill-ify outcome. It is an optional
  external dependency; the skill gives only a fallback instruction to write a
  standard `SKILL.md` package.

**Consumers inside the repository.** Other shipped skills consume Recall output.
`recap` calls the engine's `session-export` and `session-relations` commands and
checks their schema versions (SRC-1, `recap/skills/recap/scripts/recap.py`):

> if page.get("schema_version") != "recall.session-export.v1":
> --- `recap/skills/recap/scripts/recap.py`

`precap` instructs its agent to search prior sessions with Recall when installed
(SRC-1, `precap/skills/precap/SKILL.md`). These consumers call the separately
distributed engine, not code in `recall/`; the `recall/` skill documents the
export interface they rely on. They are excluded from the functional boundary by
the caller's scope, and because their own consumption logic belongs to other
skills. They may be inspected as context for how retrieved session evidence is
later consumed. This exclusion prevents attributing Recap's or Precap's evidence
handling to Recall; it does not hide any Recall responsibility, since the export
producer is absent either way.

**Boundary kind.** The skill package is a complete artifact: every file it ships
is in the inspected tree. The memory loop it participates in is partial: the
paths that produce, maintain and admit session state (indexing, redaction,
central capture) are outside the repository, and only the agent-side retrieval
and consumption procedure is inspectable. Hence `complete artifact, partial
loop`, not `whole-system`.

**Frozen revision and cutoff.** Git commit
`c82883b15e5e8f02483bee513b3c8dcac48e3c9e` of
`https://github.com/Parcha-ai/parcha-skills`, committed 2026-10-22. The analysis
cutoff is that commit date; claims apply to the skill text at that revision.

**Evidence tier.** `doc-grounded`. The target's shipped artifact is
instructions. The skill text is the executable procedure the agent follows, so
it supplies `implementation` evidence for the agent-side procedure. Everything
about the engine and service it calls is declared contract only. No observed run
or causal experiment is available for Recall within this source.

**Coverage of top-level tracked entries.**

| Path | Status | Role | Conclusion an exclusion prevents |
|---|---|---|---|
| `recall/` | Included; all 8 files inspected (`skills/recall/SKILL.md`, `skills/recall/references/central-brain.md`, `skills/recall/references/query-cookbook.md`, `README.md`, `package.json`, `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `LICENSE`) | The target skill package | — |
| `.claude-plugin/`, `.agents/plugins/` | Included as registration | Marketplace entries pointing at `./recall` | — |
| `package.json` | Included as registration | Lists `./recall/skills` among pi skill roots | — |
| `README.md` | Included as context, inspected at the Recall rows and the instruction-only statement | Repository description of Recall's packaging | — |
| `tests/test_portability.py` | Included as packaging evidence; Recall-specific tests inspected | Enforces instruction-only content and pi caveat text | — |
| `scripts/prove_portability.py` | Context; inspected only for the Recall name entry | Portability proof script listing the package | Detailed portability-proof behavior for Recall |
| `recap/` | Excluded by caller scope; Recall call sites in `skills/recap/scripts/recap.py` and `skills/recap/SKILL.md` inspected as context | Downstream consumer of Recall session export and relations | Attributing Recap's evidence ledger, redaction and synthesis to Recall |
| `precap/` | Excluded by caller scope; Recall mention inspected as context | Downstream consumer of Recall search | Attributing Precap's investigation procedure to Recall |
| `.github/` | Excluded; `SECURITY.md` and `SUPPORT.md` Recall lines inspected | Repository policy and CI workflows | None material; they confirm the engine is maintained separately |
| `autoqa/`, `blast-radius/`, `cascade/`, `desloppify/`, `hands-free/`, `parable/`, `review-loop/`, `snippets/`, `tdd/`, `tether/`, `unslop/`, `verify-release/` | Excluded by caller scope; not inspected beyond a repository-wide search for Recall references (only `parable/` matched, with incidental mentions) | Other skills and snippets | Conclusions about those skills; none about Recall |
| `docs/` | Excluded by caller scope; no Recall reference found by search | Repository research and publication notes | None about Recall |
| `.gitignore`, `.gitleaks.toml`, `LICENSE` | Excluded | Repository hygiene and license | None |

Unavailable evidence: the Recall engine and the central Brain service. Deliberate
exclusions: the other skills, by caller scope. Not yet inspected: the excluded
skills' internals, which do not bear on Recall's mechanism.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Parcha-ai/parcha-skills` | `c82883b15e5e8f02483bee513b3c8dcac48e3c9e` | `implementation`: the skill text as the agent-executed procedure, and in-repo consumers and tests; `doctrine/design`: the skill's declarations about the absent engine and central service | Access root `related-systems/Parcha-ai--parcha-skills/`. Initially inspected: all of `recall/`; Recall entries in `.claude-plugin/marketplace.json`, `.agents/plugins/marketplace.json`, `package.json`, `README.md`, `tests/test_portability.py`, `.github/SECURITY.md`, `.github/SUPPORT.md`; Recall call sites in `recap/skills/recap/scripts/recap.py`, `recap/skills/recap/SKILL.md`, `precap/skills/precap/SKILL.md` | `recall/skills/recall/SKILL.md`, `recall/skills/recall/references/central-brain.md`, `recall/skills/recall/references/query-cookbook.md`, `recall/README.md`, `recall/package.json`, `tests/test_portability.py`, `recap/skills/recap/scripts/recap.py` | The Recall engine (`recall.py`, index, ranking, redaction, export) and central Brain service are not in the repository; this prevents implementation-level or observed-run conclusions about state production, ranking, redaction, retention and capture, which remain declared contract only. No run traces or experiments for Recall exist in this source |
