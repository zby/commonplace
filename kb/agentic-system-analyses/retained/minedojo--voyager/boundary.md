---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Voyager's Minecraft agent runtime, retained skill libraries and shipped environment bridge at commit 55e45a880755d0c8c66ca7fb5fe7962ac8974f89."
run-id: AAS-2026-10-14-voyager-f16a44a0cfe3-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "55e45a880755d0c8c66ca7fb5fe7962ac8974f89"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/MineDojo/Voyager
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/voyager-f16a44a0cfe3/related-systems/MineDojo--Voyager
  revision: "55e45a880755d0c8c66ca7fb5fe7962ac8974f89"
  sha256: null
---

# Voyager boundary

## Boundary and evidence

This run analyses the shipped Voyager system for open-ended Minecraft task learning and later task execution with retained skills. It includes the Python driver, action/curriculum/critic agents, skill manager, prompts, checkpoint handling, JavaScript execution bridge, observations, control primitives, bundled collection plugin and distributed learned skill libraries. It is an **enclosing runtime**, not merely a skill-retrieval API: its driver selects tasks, calls the action model, executes generated programs, obtains task judgments, updates retained state and starts subsequent tasks. The boundary is **whole-system** at the repository revision, including both learning and inference consumers. Evidence: SRC-1, `voyager/__init__.py`, `voyager/voyager.py`, `voyager/agents/skill.py`, `README.md`.

The learning driver admits new skills on its success branch and updates curriculum progress afterward (SRC-1, `voyager/voyager.py`):

> if info["success"]:
>     self.skill_manager.add_new_skill(info)
>
> self.curriculum_agent.update_exploration_progress(info)
> --- `voyager/voyager.py`

Retained skills are not only published output. The manager reloads `skills.json`, opens its persistent Chroma collection, retrieves code for action prompts, and supplies the complete loaded skill set plus primitives as execution programs. The driver also exposes decomposition and inference using the same rollout machinery; those are included consumers, not an excluded application (SRC-1, `voyager/agents/skill.py`, `voyager/agents/action.py`, `voyager/voyager.py`). The execution endpoint combines the supplied programs and current action code (SRC-1, `voyager/env/mineflayer/index.js`):

> await eval("(async () => {" + programs + "\n" + code + "})()");
> --- `voyager/env/mineflayer/index.js`

Prompt instructions are part of the shipped mechanism, not instructions to this analysis. For example, the action prompt explicitly requests later reuse (SRC-1, `voyager/prompts/action_template.txt`):

> Your function will be reused for building more complex functions. Therefore, you should make it generic and reusable.
> --- `voyager/prompts/action_template.txt`

The frozen evidence is solely SRC-1 at **55e45a880755d0c8c66ca7fb5fe7962ac8974f89**, with applicability cutoff **2026-10-14**. HEAD was checked against the acquired revision. The overall tier is **code-grounded**: source inspection supports implementation claims, while README, FAQ and installation instructions supply declared intent and attributed operational reports. No target code, tests, examples or model calls were executed. A completed boundary means the target and source set are established, not that performance or reliable operation has been demonstrated.

### Repository coverage

The tracked top-level tree was enumerated. Every top-level entry is classified below. Included directories cover their material shipped paths, not only the initially read files. “Not yet inspected” names available evidence, not an access gap or functional exclusion.

| Top-level entry | Classification and material paths | Initial inspection and consequence of exclusions or remaining inspection |
|---|---|---|
| `.github/` | Excluded: issue template and issue-closing workflow. | Tree inspected; contents not inspected. No conclusions about repository support or issue-management automation. These paths do not supply the agent loop. |
| `.gitignore` | Excluded: source-control ignore policy. | Tree inspected; contents not inspected. No conclusions about which local runtime artifacts Git would omit. |
| `FAQ.md` | Included: operational guidance on login, resets, model choice and cost. | Read; statements remain attributed reports, not observed runs. |
| `LICENSE` | Excluded: legal terms. | Tree inspected; contents not inspected. No license interpretation. |
| `README.md` | Included: intended design, installation, learning entry point, checkpoint resume and learned-library inference caller. | Read completely; reported performance is not independently established. External website, paper and video links are not acquired sources. |
| `images/` | Excluded: `pull.png` presentation image. | Tree inspected; image not inspected. No conclusions from the image or visual demonstrations. |
| `installation/` | Included: Minecraft instance setup and Fabric-mod setup instructions. | Both Markdown files read. External game, mods, authentication service and launcher-library implementations are not frozen here. |
| `requirements.txt` | Included: Python dependency declaration. | Read; declarations do not freeze installed dependency behavior. |
| `setup.py` | Included: package metadata and dependency-loading setup. | Read; no installation or packaging execution performed. |
| `skill_library/` | Included: README and trial1–trial3 `skill/code/`, `skill/description/`, `skills.json`, Chroma parquet data and index files. These are shipped retained state for later consumption. | Tree and README inspected; trial1 `mineWoodLog.js` and its description sampled. Other skill bodies, JSON payloads and binary indexes not yet inspected. Their existence is not proof of successful training, index consistency or transfer performance. |
| `voyager/` | Included: public `__init__.py`; `voyager.py` learning, rollout, decomposition and inference; `agents/{action,critic,curriculum,skill}.py`; `prompts/` including action response format, curriculum QA and task decomposition; `control_primitives/` and `control_primitives_context/`; `env/bridge.py`, launcher, process monitor, Mineflayer server, observation modules and skill loader; bundled `env/mineflayer/mineflayer-collectblock/` source, docs and examples; `utils/` persistence, parsing and event recording. | Full driver and skill manager read; action persistence/prompt assembly, curriculum reload/progress/QA persistence, critic judgment dispatch and retry parsing traced. Bridge, launcher, observation base, skill loader, server start/execution path, event recorder, prompt loader, primitive loader, action/curriculum/critic/skill prompts and dependency manifest inspected. Remaining agent helpers, prompt bodies, concrete primitives/observations, bundled plugin internals/examples and utility helpers are available but not yet inspected. They remain in scope for later source tracing; no claim of exhaustive line-level review is made. |

### Functional inclusions and limits

- **State production, admission and maintenance:** generated action code, critic judgment, success-conditioned skill admission, generated skill descriptions, JSON/code/description persistence and Chroma persistence; curriculum task histories and QA cache; chest memory updates; event recording and resume. Initially traced in SRC-1, `voyager/voyager.py`, `voyager/agents/skill.py`, `voyager/agents/curriculum.py`, `voyager/agents/action.py`, `voyager/utils/record_utils.py`.
- **Later consumption:** resume constructors, retrieved code in action prompts, all loaded programs passed to environment execution, and inference with a separately supplied skill library. Initially traced in SRC-1, `README.md`, `voyager/voyager.py`, `voyager/agents/skill.py`, `voyager/agents/action.py`.
- **Evaluators:** the shipped task critic and recorder-derived item/time/position summaries are included. The README's empirical comparisons are reported results only. No independent benchmark run, causal intervention or inspectable end-to-end execution trace was established during this boundary job (SRC-1, `voyager/agents/critic.py`, `voyager/utils/record_utils.py`, `README.md`).
- **External dependencies:** Minecraft/Fabric/mods, OpenAI chat and embedding services, LangChain, Chroma, Mineflayer and third-party plugins remain external implementations, except the collection plugin source shipped inside this repository. Their declarations and Voyager-side integration are included, not their unfrozen upstream implementations. This prevents conclusions about service/model internals, exact resolved dependency behavior, real game synchronization and reproducible end-to-end performance (SRC-1, `requirements.txt`, `voyager/env/mineflayer/package.json`, `installation/fabric_mods_install.md`, `voyager/env/bridge.py`).
- **Other artifacts:** community checkpoint repositories, linked papers, website, issue discussions and videos are not in the frozen source set. They cannot establish checkpoint quality, historical causes, comparative performance or observed operation for this run. Links alone do not register their contents (SRC-1, `README.md`, `FAQ.md`, `skill_library/README.md`).

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/MineDojo/Voyager` | 55e45a880755d0c8c66ca7fb5fe7962ac8974f89 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/voyager-f16a44a0cfe3/related-systems/MineDojo--Voyager`. Implementation: tracked tree; `setup.py`, `requirements.txt`, `voyager/__init__.py`, full `voyager/voyager.py` and `voyager/agents/skill.py`; selected action/curriculum/critic paths detailed above; environment bridge/launcher, Mineflayer start and execution path, observation base and skill loader; prompt and primitive loaders; event recorder; trial1 wood-log code and description. Doctrine/design: `README.md`, `skill_library/README.md`, both installation files, action/curriculum/critic/skill prompts. Reported operation: README performance claims and FAQ operational guidance, without inspecting linked external evidence. | Implementation: [driver](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py), [skill manager](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/skill.py), [execution bridge](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/env/mineflayer/index.js). Doctrine/design: [README](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/README.md), [action prompt](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/action_template.txt). Reported operation: [FAQ](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/FAQ.md) and README. | No repository access gap encountered. Initial inspection is not an allowlist; remaining available paths are identified in the coverage table. Unfrozen external dependencies and linked artifacts cannot support implementation claims here. No observed-run or causal-experiment layer established; distributed skills alone do not establish the process or outcomes that produced them. |
