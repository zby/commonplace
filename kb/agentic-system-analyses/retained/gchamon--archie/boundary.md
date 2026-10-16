---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Archie's agent-launch profile subsystem and assistant design at commit 76caf94548cf76f2399d9a7446da15e0daa22685."
run-id: AAS-2026-10-15-archie-1ab3d8b8ff03-01
result-disposition: complete
target-class: runtime client
boundary-kind: subsystem-only
reviewed-boundary: 76caf94548cf76f2399d9a7446da15e0daa22685
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/gchamon/archie
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-archie/related-systems/gchamon--archie
  revision: 76caf94548cf76f2399d9a7446da15e0daa22685
  sha256: null
---

# Archie boundary

## Boundary and evidence

This run analyses Archie's shipped agent-launch profile subsystem, with its planned documentation assistant as design context. It does not treat the entire desktop configuration repository as an agent runtime. The intended use is to explain what Archie itself configures and hands to an external coding-agent runtime, and distinguish that implementation from the proposed assistant. The target class is **runtime client** and the boundary kind is **subsystem-only**: the shipped executable mechanism configures and invokes `omp`, rather than implementing the model/tool loop itself (SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`).

The implementation qualifies as an agent-related mechanism because its operation explicitly selects model roles and launches the external agent with role-specific model arguments. A representative entry point is:

> omp:openai() {
>   _omp:set-default "openai-codex/gpt-6-luna:medium" || return 1
>   omp \
>     --smol openai-codex/gpt-6-luna:medium \
>     --slow openai-codex/gpt-6-sol:medium \
>     --plan openai-codex/gpt-5.6-terra:medium \
>     --model openai-codex/gpt-6-luna:medium "$@"
> }
> --- `deployment-packages/local/lib/zsh/commands-agents.sh`

The included mechanism comprises all seven profile functions, four shorthand aliases, the helper that reads and writes the external runtime's `modelRoles`, and the shipped loading/deployment chain. The helper's persistence contract is visible at the process boundary; the external runtime's storage implementation is not part of Archie (SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`).

>   roles="$(omp config get modelRoles | jq -c --arg default "$default_model" '.default = $default')" || return 1
>   omp config set modelRoles "$roles"
> --- `deployment-packages/local/lib/zsh/commands-agents.sh`

The shell callers are included, not treated as an excluded enclosing application. The installer deploys the `home` and `local` Stow packages; the shipped `.zshrc` loads `commands.sh`, which loads the agent module (SRC-1, `scripts/install.sh`, `deployment-packages/home/.zshrc`, `deployment-packages/local/lib/zsh/commands.sh`). In particular:

> test -f "$ZSHLIB/commands-agents.sh" && source "$ZSHLIB/commands-agents.sh"
> --- `deployment-packages/local/lib/zsh/commands.sh`

### Functional coverage and limits

| Scope | Included evidence and inspection | Limit and conclusion prevented |
| --- | --- | --- |
| Agent-launch implementation | SRC-1, complete `deployment-packages/local/lib/zsh/commands-agents.sh` and `deployment-packages/local/lib/zsh/commands.sh`; shell initialization in `deployment-packages/home/.zshrc`; deployment function in `scripts/install.sh`. | Establishes source-level configuration and launch behavior, not successful installation, provider access or execution. |
| Operator contract | SRC-1, introductory and agent-profile sections of `deployment-packages/local/lib/zsh/README.md`. | Documentation is declared intent. Its model names differ from current code in places; it cannot override executable arguments. |
| Assistant design | SRC-1, complete `docs/epics/assistant.md` and `docs/work-items/assistant-03-agent-backed-documentation-guide.md`. | Included as planned design, not an implemented documentation retrieval, safety or context-injection mechanism. |
| Repository identity and alternate entry point | SRC-1, `README.md`, `pyproject.toml` and complete `src/archie/cli.py`. The Python CLI registers applet, downgrade, GUI and system commands; the agent profiles enter through zsh. | This is entry-point inspection, not coverage of every desktop command's implementation. |
| Desktop distribution and unrelated administration | Deliberately outside the functional target: other desktop configuration, system maintenance, Archinstall/provisioning, packaging and VM tooling, except the profile deployment chain above. Their paths were inventoried, not comprehensively inspected. | Prevents a whole-system account of Archie as an operating environment, including its system-state persistence and recovery. These are not missing agent-runtime implementations attributed to the profile subsystem. |
| Contributor instructions and session documentation | Repository-maintenance material is outside the selected runtime-client mechanism; it is not a shipped agent execution trace for this analysis. | No conclusion about contributor-agent workflows, retained session reuse or maintenance effectiveness. |
| External runtime and providers | `omp`, its configuration storage and role interpretation, model services/local servers, and user credentials are dependencies, not frozen implementations in SRC-1. `jq`, zsh and Stow support configuration, loading and deployment. | Prevents claims about model-call scheduling, tool permissions, context retention, actual inference, safety enforcement or end-to-end success inside those dependencies. |

The assistant design explicitly calls itself planned and keeps agent support optional (SRC-1, `docs/work-items/assistant-03-agent-backed-documentation-guide.md`):

> ## Status
>
> <!--
> Use a short prose status for the current state of the work item.
> Supported values are `backlog`, `planned`, `doing`, `done`, `cancelled`, and `abandoned`.
> `killed` is reserved for GitLab graveyard history when a managed work item is removed from the repository.
> -->
>
> Planned
> --- `docs/work-items/assistant-03-agent-backed-documentation-guide.md`

> - Agent support is optional and should layer on top of the documented
>   assistant, not replace the non-agent topic browser.
> --- `docs/work-items/assistant-03-agent-backed-documentation-guide.md`

Tree inspection and bounded searches for agent names, `omp`, `modelRoles`, profile loading and deployment identified the shipped shell path and the assistant planning documents. This establishes a coherent narrow target; it does not assert that every repository file has been inspected. No material part of the selected shell mechanism was unavailable. Available but uninspected files are not access gaps.

The frozen evidence is the acquired Git checkout at **76caf94548cf76f2399d9a7446da15e0daa22685**. HEAD was checked against that pin and the worktree reported no changes. The applicability cutoff is **2026-10-15**; later repository revisions and moving web material are excluded. Overall evidence is **code-grounded**, with doctrine/design separately labelled. No target code, tests, examples, agent sessions or provider calls were executed. There is no observed-run or causal-experiment evidence.

The normalized source identity remains the supplied GitHub URL. The repository's own README identifies GitLab as canonical upstream and GitHub as its read-only mirror; this is identity context, not permission to add a second repository or change the frozen source (SRC-1, `README.md`).

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/gchamon/archie` | 76caf94548cf76f2399d9a7446da15e0daa22685 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-archie/related-systems/gchamon--archie`. Implementation: complete agent-profile module, shell loader and Python CLI; shell initialization and installer deployment function. Doctrine/design: root README, project metadata, zsh-library introduction and agent-profile reference, complete assistant epic and agent-backed assistant work item. Tracked tree and bounded repository searches established the initial path inventory. | Implementation: [profiles](https://github.com/gchamon/archie/blob/76caf94548cf76f2399d9a7446da15e0daa22685/deployment-packages/local/lib/zsh/commands-agents.sh), [loader](https://github.com/gchamon/archie/blob/76caf94548cf76f2399d9a7446da15e0daa22685/deployment-packages/local/lib/zsh/commands.sh), [shell initialization](https://github.com/gchamon/archie/blob/76caf94548cf76f2399d9a7446da15e0daa22685/deployment-packages/home/.zshrc), [installer](https://github.com/gchamon/archie/blob/76caf94548cf76f2399d9a7446da15e0daa22685/scripts/install.sh), [CLI](https://github.com/gchamon/archie/blob/76caf94548cf76f2399d9a7446da15e0daa22685/src/archie/cli.py). Doctrine/design: [README](https://github.com/gchamon/archie/blob/76caf94548cf76f2399d9a7446da15e0daa22685/README.md), [metadata](https://github.com/gchamon/archie/blob/76caf94548cf76f2399d9a7446da15e0daa22685/pyproject.toml), [profile reference](https://github.com/gchamon/archie/blob/76caf94548cf76f2399d9a7446da15e0daa22685/deployment-packages/local/lib/zsh/README.md), [assistant epic](https://github.com/gchamon/archie/blob/76caf94548cf76f2399d9a7446da15e0daa22685/docs/epics/assistant.md), [agent-backed assistant plan](https://github.com/gchamon/archie/blob/76caf94548cf76f2399d9a7446da15e0daa22685/docs/work-items/assistant-03-agent-backed-documentation-guide.md). | No checkout access gap for the selected subsystem. External runtime/provider implementations and inspectable executions are absent from this evidence set: their internals and successful operation cannot be established. Design documents support intentions only, not implemented assistant behavior. |
