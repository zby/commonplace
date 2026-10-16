---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ai-modules' shipped skills, helper agents, persistent Markdown workflows, deployment machinery and evaluators at commit 0cf0227c416f75a79d7317f603a209a63e7a3c8f."
run-id: AAS-2026-10-14-ai-modules-a7044d5627d2-01
result-disposition: complete
target-class: extension or tool mechanism
boundary-kind: whole-system
reviewed-boundary: "0cf0227c416f75a79d7317f603a209a63e7a3c8f"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/TheAFH/ai-modules
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/ai-modules-a7044d5627d2/related-systems/TheAFH--ai-modules
  revision: 0cf0227c416f75a79d7317f603a209a63e7a3c8f
  sha256: null
---

# ai-modules boundary

## Boundary and evidence

This run analyses ai-modules as a shipped agent operating extension layer, not as an enclosing model runtime. Its intended use is reusable AI-assisted development, knowledge maintenance and editorial work through installable skills and helper-agent definitions. The target qualifies because its central workflows are instructions consumed by models: the host agent interprets them, calls bundled bookkeeping scripts, writes persistent state and may dispatch helpers. The repository also ships evaluator drivers that launch model-dependent workers. The class is **extension or tool mechanism**; persistent knowledge and task management are substantial capabilities inside that broader target, not a reason to narrow the target to the wiki alone (SRC-1, `README.md`, `plugins/ai_dev/skills/agent_spinner/SKILL.md`, `tests/lib/micro_deploy.py`).

> Each skill is a written procedure the model loads when its trigger fires.
> --- `README.md`

The **whole-system** boundary includes all three shipped plugins, their prompts, agents, hooks, bundled scripts and references; both marketplace registrations; output styles; deployment and uninstall machinery; repository-local standing instructions and retained state; and authored evaluators. It includes callers and consumers in this repository rather than treating a shipped caller as an external application. Local backlog and wiki content are worked instances and maintenance inputs, not independent implementations or proof that every declared rule held in operation (SRC-1, `README.md`, `AGENTS.md`, `Makefile`).

> The repo runs on the components it ships. Its backlog, knowledge base, charter, and
> changelog are all produced by the skills in `plugins/`, so those four directories double
> as worked examples of what the plugins do.
> --- `README.md`

Initial inspection traced these material paths:

- **Delivery into hosts:** marketplace registration names plugin roots; the Codex knowledge-management manifest exposes `./skills/`; `Makefile` invokes `deployment/deployment.sh`; its discovery routine enumerates skills, agents and hooks under plugins and styles under the repository root, then its main loop passes selected artifacts to `install_for_app`. Deployment documentation describes copied assets and generated per-host agent formats. This fixes delivery as part of the target, while actual host loading remains outside the implementation evidence (SRC-1, `.claude-plugin/marketplace.json`, `plugins/knowledge_management/.codex-plugin/plugin.json`, `Makefile`, `deployment/deployment.sh`, `deployment/README.md`).
- **Knowledge production, admission and later consumption:** `wiki_import` captures a named resource and waits for selections before page writes; `wiki_wrapup` mines the visible session and waits before writes. Both route approved changes to the wiki hub. The hub discovers and resumes existing state, reads schema/index/recent log, captures raw material, writes linked pages, updates navigation, lints, and later queries retained pages. Its query workflow can file a new synthesis back into the same store. `wiki_fix` delegates maintenance to `auto_shaper_wiki`; the agent declares orient, assess, remediate and verify phases. The initializer and linter implement mechanical scaffold and checking operations. These are instruction contracts plus inspected helper code, not observed compliance by an agent (SRC-1, `plugins/knowledge_management/skills/wiki_import/SKILL.md`, `plugins/knowledge_management/skills/wiki_wrapup/SKILL.md`, `plugins/knowledge_management/skills/wiki/SKILL.md`, `plugins/knowledge_management/skills/wiki_fix/SKILL.md`, `plugins/knowledge_management/agents/auto_shaper_wiki.md`, `plugins/knowledge_management/skills/wiki/scripts/init_wiki.sh`, `plugins/knowledge_management/skills/wiki/scripts/lint.py`).
- **Work-state lifecycle:** the task hub specifies query, update and archive operations, lint and durable-lesson capture into the wiki. `task_implement` later reads the retained task and its dependencies before building. `task_auto_check` freezes task intent, persists pointer-based helper handoffs and consumes gate/verifier returns before repairs. `agent_spinner` is advisory over family-governed runs and explicitly distinguishes role files from demonstrated callability (SRC-1, `plugins/ai_dev/skills/task/SKILL.md`, `plugins/ai_dev/skills/task_implement/SKILL.md`, `plugins/ai_dev/skills/task_auto_check/SKILL.md`, `plugins/ai_dev/skills/agent_spinner/SKILL.md`).
- **Evaluation consumer:** the wiki layer-2 driver stages a scenario outside the checkout, micro-deploys artifacts, launches a worker, retains response, timing and provenance data, snapshots resulting state, and removes the sandbox. The shared launcher builds a Claude/Cursor command and calls it through `subprocess.run`. These shipped callers are included; they cannot be omitted on the ground that they supply fixture state (SRC-1, `tests/wiki/layer2/run.py`, `tests/lib/micro_deploy.py`, `tests/lib/vendor.py`).

Two short passages retain the load-bearing consumption and host-authority distinctions:

> 3. **Read the relevant pages.**
> 4. **Synthesize an answer** with citations: "Based on
>    [page-a](concepts/page-a.md) and [page-b](entities/page-b.md)…"
> --- `plugins/knowledge_management/skills/wiki/SKILL.md`

> A role definition on disk is evidence that the file deployed, not evidence that it can be called: definition-present-and-uncallable is a real state, so a registration check reporting a definition as available settles deployment alone.
> --- `plugins/ai_dev/skills/agent_spinner/SKILL.md`

### Top-level coverage

The tracked root tree was enumerated at the frozen commit. “Included” defines the functional boundary, not a claim that every file has been read. Inspection statuses below distinguish available but not yet inspected material from exclusions; no material shipped path was found unavailable.

| Top-level tracked entry | Included or excluded | Role, material paths and initial inspection | Conclusion prevented by exclusion or remaining inspection limit |
| --- | --- | --- | --- |
| `.agents/` | Included | `.agents/plugins/marketplace.json`: Codex registration; searched registration and version descriptions. | Full registration consistency not yet checked. |
| `.claude-plugin/` | Included | `.claude-plugin/marketplace.json`: plugin discovery; read in full. | Host registration success is not observed. |
| `.cursor/` | Excluded | `.cursor/scratch/` proposal and roster files: local draft work, not deployed components. Tree inventoried; bodies not inspected. | No reconstruction of those draft sessions or attribution of their outcomes. |
| `.gitignore` | Included | Repository retention/ignored-state configuration; inventoried, body not yet inspected. | Exact ignore behavior not yet established. |
| `.markdownlint.jsonc` | Included | Published instruction lint configuration; role traced through `Makefile`, body not yet inspected. | Exact markdown rule configuration not yet established. |
| `AGENTS.md` | Included | Standing component-authoring rules, local wiki/task consumption and verification directions; read in full. | Declared policy, not demonstrated adherence. |
| `CLAUDE.md` | Included | Companion standing-instruction surface listed by the tree and README; content/parity not yet inspected. | No claim of byte parity or effective host instruction loading. |
| `CHANGELOG.md` | Included | Persistent git-history-derived state consumed/produced by `update_changelog`; role inspected in README and AGENTS, body and producer script not yet inspected. | No longitudinal change account or changelog correctness claim yet. |
| `CHARTER.md` | Included | Repository purpose and boundaries; opening sections inspected; consumer/protector traced to `plugins/ai_dev/hooks/charter_guardrail.sh`. | Later charter provisions and effective enforcement not yet established. |
| `LICENSE` | Excluded | Legal licensing, inventoried only. | No legal or licensing assessment. |
| `Makefile` | Included | Deployment, uninstall, backup cleanup and md/JSON/shell lint entry points; executable recipes inspected. | No claim that those commands passed. |
| `README.md` | Included | Product entry, full layout, plugin roles and distribution routes; read in full. | Performance and cost promises remain declared intent. |
| `TESTING.md` | Included | Test-design and verification policy, identified via AGENTS and test documentation; body not yet inspected. | No complete assessment of grader-design policy. |
| `deployment/` | Included | `deployment.sh` artifact discovery and install dispatch inspected; `README.md` read in full; `deployment.conf` and remaining transformation, backup and uninstall code available for later inspection. | No comprehensive cross-host deploy/uninstall correctness claim yet. |
| `plugins/` | Included | `knowledge_management/skills/wiki{,_import,_wrapup,_fix}/SKILL.md`, wiki scaffold/lint scripts and `agents/auto_shaper_wiki.md`; `ai_dev/skills/task{,_auto_check,_implement}/SKILL.md`, `agent_spinner/SKILL.md`, task sibling routing search, `hooks/charter_guardrail.sh`; `ai_editorial/skills/language_humanizer/SKILL.md`; representative manifests. Read full narrow front ends and selected hub/agent/script ranges. All remaining skill prompts, helper agents, references and scripts stay included and available, not excluded as mere documentation. | Detailed behavior of remaining helpers, git workflows, formatting, distillation, portability and semantic maintenance checks requires later source inspection. |
| `seed.txt` | Excluded | Single `seed` marker; read. No shipped behavior identified. | No interpretation of marker provenance. |
| `styles/` | Included | `natural-language.md` frontmatter, objective and scope inspected; delivery traced through deployment documentation and code discovery. | Actual style injection or adherence not observed. |
| `tasks/` | Included | Live task files and `archive/` are repository-local work-state instances. `wiki_log-rotation-and-retrieval.md` inspected as one retained task; producers/consumers traced through task hub, auto-check and implement. Remaining instances available, not yet inspected. | A task's proposed changes are not treated as shipped behavior; no backlog-wide completion verdict. |
| `tests/` | Included | `README.md`, wiki layer-2 caller, shared `lib/vendor.py` and `lib/micro_deploy.py` launch path inspected; `wiki/layer1/`, `task/`, `task_auto_check/`, `agent_spinner/`, git, deployment, editorial, style and trigger suites inventoried. Fixtures, graders, shared isolation/cache code and tracked result reports stay available for later inspection. | No suite-wide pass rates, effective isolation guarantee or causal effectiveness claim from this initial inspection. |
| `wiki/` | Included | `index.md` read: catalog of local retained pages; `SCHEMA.md`, `log.md`, typed pages and `raw/notes/` inventoried. Standing rules explicitly tell maintainers to read and update the corpus. Individual source-native research records and schema/log bodies not yet inspected. | No endorsement of cataloged host facts or observed-run claims until the underlying evidence is read. |

External dependencies are the host harnesses named by the deployment paths (Claude Code, Codex, Cursor, Copilot/VS Code, Antigravity and OpenCode), their model providers, ordinary filesystem/Git tools, Bash/Python and deployment/lint dependencies. Host routing, context assembly, helper scheduling, model inference and sandbox enforcement are not owned by ai-modules. Their implementations, live installations and provider documentation fetched from outside this checkout are excluded. This prevents independently establishing current host compatibility, runtime confinement or actual model behavior across those hosts. Source-native statements about them may be analysed as attributed evidence, not substituted for inspected host code (SRC-1, `deployment/README.md`, `plugins/ai_dev/skills/agent_spinner/SKILL.md`, `tests/lib/vendor.py`).

The acquired checkout remains read-only at **0cf0227c416f75a79d7317f603a209a63e7a3c8f**; HEAD was checked against that pin and the worktree reported no changes. The applicability cutoff is **2026-10-14**, the supplied run date, not a claim about later revisions or installed vendor versions. The overall tier is **code-grounded** because executable scaffold, lint, deployment dispatch and evaluator launch paths were inspected alongside model-consumed instructions. No target, test, example, host or provider was executed. No access gap requires a partial-loop boundary: the initial unread files above remain reachable at the registered commit. Later analysis must distinguish executable bookkeeping from prompt-governed behavior and separately assess any retained operation reports or traces it uses.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/TheAFH/ai-modules` | 0cf0227c416f75a79d7317f603a209a63e7a3c8f | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/ai-modules-a7044d5627d2/related-systems/TheAFH--ai-modules`. Implementation: tracked tree; `Makefile`; `deployment/deployment.sh` discovery/main dispatch; `plugins/knowledge_management/skills/wiki/scripts/init_wiki.sh` and `lint.py` entry point; `plugins/ai_dev/hooks/charter_guardrail.sh` input handling and mutator scan; `tests/wiki/layer2/run.py` pass driver; `tests/lib/vendor.py` command builder; `tests/lib/micro_deploy.py` worker launcher. Doctrine/design: full `README.md`, `AGENTS.md`, `deployment/README.md`, plugin READMEs and selected manifests; full wiki import/wrapup/fix and task implement front ends; selected wiki/task hub, task auto-check, agent-spinner and wiki-shaper sections; editorial/style opening contracts; `CHARTER.md` opening, `wiki/index.md`, one live task instance. Detailed initial coverage is in the table above; listed paths are not an evidence allowlist. | Implementation: [deployment discovery/dispatch](https://github.com/TheAFH/ai-modules/blob/0cf0227c416f75a79d7317f603a209a63e7a3c8f/deployment/deployment.sh), [wiki checking](https://github.com/TheAFH/ai-modules/blob/0cf0227c416f75a79d7317f603a209a63e7a3c8f/plugins/knowledge_management/skills/wiki/scripts/lint.py), [evaluator caller](https://github.com/TheAFH/ai-modules/blob/0cf0227c416f75a79d7317f603a209a63e7a3c8f/tests/wiki/layer2/run.py), [worker launch](https://github.com/TheAFH/ai-modules/blob/0cf0227c416f75a79d7317f603a209a63e7a3c8f/tests/lib/micro_deploy.py). Doctrine/design: [product](https://github.com/TheAFH/ai-modules/blob/0cf0227c416f75a79d7317f603a209a63e7a3c8f/README.md), [wiki workflow](https://github.com/TheAFH/ai-modules/blob/0cf0227c416f75a79d7317f603a209a63e7a3c8f/plugins/knowledge_management/skills/wiki/SKILL.md), [orchestration contract](https://github.com/TheAFH/ai-modules/blob/0cf0227c416f75a79d7317f603a209a63e7a3c8f/plugins/ai_dev/skills/agent_spinner/SKILL.md). | No unavailable tracked source identified. Uninspected material is distinguished above, not labeled inaccessible. Host internals, external live configuration and independent execution are outside the frozen source. No observed-run or causal-experiment layer is claimed from source inspection; retained reports/traces must be examined with their conditions before they support such findings. |
