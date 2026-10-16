---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Archie runtime-client baseline: persistent model-role selection and zsh launch paths at the frozen revision."
run-id: AAS-2026-10-15-archie-1ab3d8b8ff03-01
reviewed-boundary: 76caf94548cf76f2399d9a7446da15e0daa22685
---

# Archie runtime report

## Runtime account

Archie's selected subsystem configures an external agent and starts it. It does not own the agent's next-step model/tool loop. The source-native work is persistent default-role selection followed by a role-configured `omp` invocation. The planned documentation assistant is a different, unimplemented design surface, not a safety envelope around these shell functions. Evidence is SRC-1 implementation and doctrine/design at the boundary's frozen commit; there are no supplied execution traces or experiments. All operation, activation and benefit remain unobserved.

### Ordinary invocation and ownership

A user installs the shell configuration through the `home` and `local` Stow packages, then starts a shell loading `.zshrc`. The loader sources `commands-agents.sh` when present. The relevant deployment and load requests are explicit (SRC-1, `scripts/install.sh`, `deployment-packages/home/.zshrc`, `deployment-packages/local/lib/zsh/commands.sh`):

> deploy_stow_packages() {
>     log_step "Deploy Archie with Stow"
>     stow_package "$HOME" home
>     stow_package "$HOME/.config" config
>     stow_package "$HOME/.local" local
> --- `scripts/install.sh`

> test -f "$ZSHLIB/commands-agents.sh" && source "$ZSHLIB/commands-agents.sh"
> --- `deployment-packages/local/lib/zsh/commands.sh`

The representative invocation is `omp:gpt` with optional appended arguments. Its alias selects `omp:openai`, which calls the default-setting helper before launching the external executable. The user is the ordinary initiating principal; the functions are callable shell code, not proof that every caller is human. The shell owns deterministic dispatch and argument construction. `omp` owns everything after handoff, including any role interpretation, context construction, model scheduling, tool decisions, delegation and terminal answer. See [RT-RTE-profile-launch](#rt-rte-profile-launch) and [RT-RTE-default-update](#rt-rte-default-update).

> omp:openai() {
>   _omp:set-default "openai-codex/gpt-6-luna:medium" || return 1
>   omp \
>     --smol openai-codex/gpt-6-luna:medium \
>     --slow openai-codex/gpt-6-sol:medium \
>     --plan openai-codex/gpt-5.6-terra:medium \
>     --model openai-codex/gpt-6-luna:medium "$@"
> }
> --- `deployment-packages/local/lib/zsh/commands-agents.sh`

The helper reads `modelRoles`, applies a symbolic JSON assignment to `.default`, and supplies the resulting whole value to `omp config set`. It does not itself implement the storage backend. The source-native retained configuration object is [RT-OBJ-model-roles](#rt-obj-model-roles); this baseline describes its process boundary, leaving memory-specific assessments to the memory analyst. A successful helper return permits launch; a reported helper failure returns 1. Launch is foreground shell execution, with no wrapper-specific output transformation or retry. The final `omp` command supplies the function's ordinary return status. The externally produced answer, any tool effects, and runtime recovery are uninspected.

### Complete profile surface and material alternatives

All seven functions share that progression. The following values are executable selectors, not verified provider capabilities (SRC-1, complete `deployment-packages/local/lib/zsh/commands-agents.sh`). The named model dependencies and mutability limits are recorded in [RT-CMP-model-services](#rt-cmp-model-services).

| Function | Persisted default | Launch model | smol / slow / plan selectors | Separate thinking flag |
| --- | --- | --- | --- | --- |
| `omp:openai` | `openai-codex/gpt-6-luna:medium` | same | `openai-codex/gpt-6-luna:medium` / `openai-codex/gpt-6-sol:medium` / `openai-codex/gpt-5.6-terra:medium` | none |
| `omp:anthropic` | `anthropic/claude-sonnet-4-6:medium` | `anthropic/claude-sonnet-4-6` | `anthropic/claude-haiku-4-5` / `anthropic/claude-opus-4-6` / `anthropic/claude-opus-4-6` | medium |
| `omp:antigravity` | `google-antigravity/gemini-3.8-flash:medium` | `google-antigravity/gemini-3.8-flash` | `google-antigravity/gemini-3.8-flash:low` / `google-antigravity/gemini-3.1-pro:high` / `google-antigravity/gemini-3.8-flash:high` | medium |
| `omp:kimi` | `kimi-code/kimi-for-coding:low` | `kimi-code/kimi-for-coding` | `kimi-code/kimi-k2-turbo-preview` / `kimi-code/kimi-for-coding:high` / `kimi-code/kimi-for-coding:medium` | low |
| `omp:kiro-gpt` | `kiro/gpt-5.6-terra:medium` | `kiro/gpt-5.6-terra` | `kiro/gpt-6-luna:low` / `kiro/gpt-6-sol:high` / `kiro/gpt-6-sol:medium` | medium |
| `omp:qwen` | `llamacpp-qwen38/qwen38-27b-single-iq4xs:low` | `llamacpp-qwen38/qwen38-27b-single-iq4xs` | `openai-codex/gpt-6-luna` / `openai-codex/gpt-6-sol` / `openai-codex/gpt-5.6-terra` | none |
| `omp:kiro-claude` | `kiro/claude-sonnet-5:high` | `kiro/claude-sonnet-5` | `kiro/claude-sonnet-5:low` / `kiro/claude-opus-5:high` / `kiro/claude-opus-5:medium` | high |

Aliases are `omp:gpt` → `omp:openai`, `omp:gemini` → `omp:antigravity`, `omp:claude` → `omp:anthropic`, and `omp:local` → `omp:qwen`. A local-labelled entry is therefore not an all-local guarantee:

> omp:qwen() {
>   _omp:set-default "llamacpp-qwen38/qwen38-27b-single-iq4xs:low" || return 1
>   omp \
>     --smol openai-codex/gpt-6-luna \
>     --slow openai-codex/gpt-6-sol \
>     --plan openai-codex/gpt-5.6-terra \
>     --model llamacpp-qwen38/qwen38-27b-single-iq4xs "$@"
> }
> --- `deployment-packages/local/lib/zsh/commands-agents.sh`

These are role requests, not evidence of multiple agents, isolated contexts, or actual remote calls. The README's GPT-5.6 launch descriptions differ from current executable GPT-6 selectors; the table above follows code, not prose (SRC-1, `deployment-packages/local/lib/zsh/README.md`).

### Forcing cases and bounded guarantees

Four source-level cases challenge overbroad interpretations; none was executed.

1. **Helper failure versus universal read-failure protection.** Every profile has `|| return 1` after its helper, and the helper stops on a nonzero assignment/pipeline status. This is a shell-control invariant over these seven functions, conditional on ordinary shell command resolution and status semantics. It is not proof that every failed `omp config get` is detected: the helper does not set pipeline-failure propagation, validate an object schema, or verify write read-back. Pipeline status depends on shell options and `jq`; a failing producer need not make the last pipeline command fail. A bounded search for `pipefail`, `PIPE_FAIL`, `setopt` and `modelRoles` in the shipped zsh library, home package and installer found installer Bash `pipefail`, but no corresponding agent-helper setting. The installer option is not a guarantee for later interactive zsh. See [RT-RTE-default-update](#rt-rte-default-update).
2. **Persistence then launch failure.** `config set` precedes launch. If configuration succeeds and the later launch fails, the wrapper has no compensating restore. Existing non-default keys are preserved by the JSON transform for an ordinary object input, but the whole-object read/modify/write has no wrapper lock or compare-and-swap. Concurrent invocations can overwrite one another's snapshots. Neither atomic durable storage nor transaction isolation is established inside external `omp` (SRC-1, helper quotation below).
3. **Local profile with nonlocal roles.** `omp:local` aliases the Qwen function, whose auxiliary selectors use `openai-codex`. Whether those roles are ever invoked is external-runtime behavior. Source supports a mixed capability request, not either guaranteed local-only execution or observed data export (SRC-1, Qwen quotation above).
4. **Appended arguments and bypass.** All functions append `"$@"` after preset options. No Archie whitelist or duplicate-option policy intervenes; which option wins is an uninspected `omp` parser contract. Direct `omp` invocation bypasses both helper and presets. User overrides are loaded after commands and can change shell behavior; the shipped template explicitly describes untracked overrides (SRC-1, `deployment-packages/home/.zshrc`, `deployment-packages/local/lib/zsh/overrides.dist.sh`). See [RT-RTE-direct-handoff](#rt-rte-direct-handoff).

The load-bearing preservation claim's owner is the helper; enforcement is `.default = $default`, and strength is a conditional symbolic transformation invariant, not a deployment guarantee. Covered paths are the helper and all seven calling profiles; direct external CLI configuration and launch are outside that enforcement. The external contract requires `config get` to return a usable roles object and `config set` to accept/persist its value truthfully. Implementation conclusion status: wired. Operation conclusion status: uninspected. The launch-after-success invariant has the same owner and covered functions; its narrower condition is helper return status, not actual provider readiness. Implementation conclusion status: wired. Operation conclusion status: uninspected.

The capability surface is unrestricted forwarded CLI input plus role selectors. Current grants, authentication and filesystem/network/tool authority belong to the external runtime and user environment and are uninspected. No deployed isolation envelope is supplied. In particular, the shell source does not make a documentation-only permission policy out of the planned assistant's prose. Provider-native tools, direct model calls, callbacks, extensions, subprocesses, remote workers, manual graph control and durable variants inside `omp` are uninspected, not evidenced absences. They cannot inherit a guarantee from this shell wrapper. Source gives no wrapper context-pruning, context-isolation or reload policy; model-visible working context remains external.

### Changes and planned assistant

The implemented behavior-changing admission is the helper's default-role update, [RT-RTE-default-update](#rt-rte-default-update). Its guidance is a hard-coded selector chosen by invoking a function; it is not a model-generated improvement proposal. No answer oracle, outcome comparison or improvement trigger participates. Loading deployed shell code is [RT-RTE-shell-load](#rt-rte-shell-load); it is a code-delivery path, not evidence of an automated product-improvement loop.

The assistant plan asks for documentation/context presets, restrictions and provider configuration but leaves those as decisions to define. [RT-CLM-assistant-guide](#rt-clm-assistant-guide) records this design separately. There is no warrant to transfer its read-only aspiration onto the shipped launcher. The Python CLI's inspected parser registers applet, downgrade, GUI and system entry groups, not these shell profiles (SRC-1, `src/archie/cli.py`). No broader desktop implementation is included here.

Inspected coverage follows the boundary plus the complete override template, which supplies doctrine/design about machine-specific shell loading, not another agent runtime. Shell and model service dependencies were not executed. No additional source, observation layer or boundary expansion is claimed.

## Shared records

### Components

#### RT-CMP-model-services
Label: Model services selected by profile roles

The provider/model selectors in the runtime account identify the external model dependency surface (SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`). The selectors themselves are symbolic strings in tracked shell source; the services they designate ordinarily supply distributed-parametric computation, whose numerical storage substrate and implementation are outside the frozen source. This record groups the opaque service surface, not a single shared weight set.

For **each** distinct selector listed in the seven profile rows, parameter change during operation is uninspected; an exact numerical model revision is not pinned by Archie; whether its endpoint can resolve to a different weight version is uninspected. Effort suffixes and model-family/version-looking names are not weight digests. This applies separately to the OpenAI-Codex Luna, Sol and Terra selectors, Anthropic Haiku/Sonnet/Opus selectors, Google Flash/Pro selectors, Kimi turbo/coding selectors, Kiro GPT and Claude selectors, and the llama.cpp Qwen selector. No row establishes online training or fixed weights. The Qwen request quoted in the runtime account witnesses both local-labelled and provider-labelled selections. Invocation requests are wired; actual service use is unobserved.

### Operative objects

#### RT-OBJ-model-roles
Label: External modelRoles configuration value

Source-native identity is `modelRoles`. Its inspected form is symbolic JSON transformed by `jq`, with `.default` assigned a string. The immediate substrate is a shell variable/argument; durable storage is delegated to external `omp config set` and its backend is uninspected. Source evidence and minimum passage are in [RT-RTE-default-update](#rt-rte-default-update). Non-default entries are not enumerated or replaced intentionally by the helper; malformed input and concurrent writers bound the preservation claim. This is configuration supplied to a runtime consumer, not a formulated theory, transcript or numerical parameter update.

### Routes

#### RT-RTE-shell-load
Label: Deploy and load agent profiles

Endpoints are tracked shell files → Stow deployment request → user shell loader → function/alias definitions. Installer and zsh own the progression. State effects are deployed links/files and shell definitions, not model context. The ordinary principal is an installing user, but no per-file human review follows from running the installer. Evidence is SRC-1, `scripts/install.sh`, `deployment-packages/home/.zshrc`, `deployment-packages/local/lib/zsh/commands.sh`; minimum deployment/loader passages are above.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Definitions become available to the sourcing shell if dependencies and files are present; installation success is not observed.
- Later read-back: inapplicable — static shipped code loading is not material accumulated through use.
- Delegated visibility: The loaded functions can invoke the external executable; no model receives the source merely because it was sourced.
- Selection predicate: Installer requests home/local packages; loader checks file existence and uses ZSHLIB, defaulting to the user's local zsh library.
- Invalidation or expiry: Shell definitions last for the shell unless changed; deployment replacement and reload semantics depend on installer/user actions.
- Activation or effect: Shell-level definition and later invocation are wired; actual loading and model behavior changes are unobserved.
- Evidence limits: Stow internals, installed environment and runtime shell overrides are not frozen execution evidence.

Change-admission account: the proposed material is shipped shell code, with deployment requested by an installer and existence-checked sourcing by zsh. Software performs I/O; the source does not identify per-content approvers or a code-review/veto policy. Users can decline installation or change their environment. No wrapper-specific rollback on source-load failure is shown; broader desktop recovery is outside scope. Guidance is the tracked definitions, and deployment retains them for later shells. This is deployment, not an outcome-driven improvement mode; no answer oracle or theory criticism route is established.

#### RT-RTE-default-update
Label: Update persistent default model role

Endpoints are function-selected string plus external `modelRoles` → `jq` transform → external configuration setter. The helper owns transformation and ordering; external `omp` owns storage. Context is current shell state and existing JSON, not model-visible conversation. Source: SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`.

> _omp:set-default() {
>   local default_model="$1"
>   local roles
>
>   roles="$(omp config get modelRoles | jq -c --arg default "$default_model" '.default = $default')" || return 1
>   omp config set modelRoles "$roles"
> }
> --- `deployment-packages/local/lib/zsh/commands-agents.sh`

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Setter status propagates from the helper, or assignment failure returns 1; profile calls stop on a nonzero helper result.
- Later read-back: A subsequent helper invocation requests modelRoles again; successful durable retention and later runtime default consumption depend on external omp.
- Delegated visibility: Entire transformed JSON value goes to the external setter; no model is shown reading it directly.
- Selection predicate: Calling profile supplies the new default string; current non-default fields come from config get, not from a search or model ranking.
- Invalidation or expiry: A later update can replace the default; no TTL, wrapper history or automatic restore is implemented in this helper.
- Activation or effect: Configuration mutation is requested before launch; actual persistence and changed inference behavior are unobserved.
- Evidence limits: Pipeline failure semantics, valid input shape and external getter/setter contracts constrain guarantees; no storage/read-back trace is supplied.

Admission account: invoking a profile triggers a fixed default replacement. Code proposes the hard-coded selector, `jq` computes the object, and `omp config set` is the software admission boundary. The ordinary user selects a profile, not each transformed field; programmatic callers are possible. There is no separate wrapper approval/veto, candidate evaluator or answer oracle. A caller can refrain from invoking it; the external setter can fail. Rollback is not automatic, including when launch later fails. No result-driven improvement trigger appears. The guidance that shapes the change is the profile literal; what is intended to persist is the configuration value, not rationale or criticism. The whole-object update does not enforce concurrency isolation. This is an operational configuration mode, not a bounded experiment or theory-building route.

#### RT-RTE-profile-launch
Label: Launch with profile role arguments

Endpoints are one of seven functions (or four aliases) → helper → foreground external `omp`. User/shell initiates; fixed shell rules choose role arguments and helper gating, then the external runtime owns next-step decisions. The runtime-account table supplies all branches and quotations supply ordinary and mixed-provider cases (SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: External process output reaches the shell without wrapper synthesis; function normally returns its final command status, or 1 on helper failure.
- Later read-back: The helper requests retained roles before launch as described in RT-RTE-default-update; external session persistence is uninspected.
- Delegated visibility: Omp receives role flags and all appended positional arguments intact; later model/tool visibility is external.
- Selection predicate: Invoked function/alias fixes presets; appended arguments remain available to omp's parser, whose override precedence is uninspected.
- Invalidation or expiry: Launch options belong to that process; the separately requested default update can outlast it.
- Activation or effect: Executable handoff is wired, not observed; role use, model compliance and task success are not established.
- Evidence limits: No external runtime/provider implementation, grants, sessions or execution traces support deeper loop conclusions.

Operating mode is an open external agent invocation with profile presets, not a fixed curriculum. No answer oracle is supplied. Calling a `--plan` or `--slow` option does not establish planning, delegation or an evaluation stage. Product/knowledge/capability modifications performed inside omp remain uninspected; this route itself constructs a launch request rather than admitting their contents.

#### RT-RTE-direct-handoff
Label: Bypass profile through external invocation

Endpoint is the shell's directly resolved `omp` command, which the wrapper itself demonstrates as callable. Owner of CLI parsing and agent work is external. This is an afforded alternate entry, not a second implemented agent loop in Archie. SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh` supplies the direct command calls above. Shell customization is explicitly loaded after the command library:

> test -f $HOME/.local/lib/zsh/commands.sh && source "$HOME/.local/lib/zsh/commands.sh"
> test -f $HOME/.local/lib/zsh/overrides.sh && source "$HOME/.local/lib/zsh/overrides.sh"
> --- `deployment-packages/home/.zshrc`

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: uninspected — direct CLI results and status semantics belong to the external executable.
- Later read-back: uninspected — direct runtime configuration/session read-back is outside the source implementation.
- Delegated visibility: Caller-selected CLI input reaches the external runtime without the profile argument construction.
- Selection predicate: Caller chooses direct command rather than one of the profile functions; local overrides can also alter shell resolution.
- Invalidation or expiry: uninspected — external runtime lifecycle and local customization are not supplied as execution evidence.
- Activation or effect: This alternate surface can avoid the helper and its presets; actual alternate calls are unobserved.
- Evidence limits: Callable dependency does not establish its full CLI, default semantics, extension behavior or tool authority.

This route defeats any system-wide claim that every omp launch must update the default first. It has no Archie admission gate, answer oracle or experiment policy; external change mechanisms are uninspected.

### Claims

#### RT-CLM-assistant-guide
Label: Planned constrained documentation guide

Claimed operation is optional, provider-agnostic documentation assistance with constraints on broad mutation. Its source is doctrine/design, not executable profile enforcement: SRC-1, `docs/epics/assistant.md`, `docs/work-items/assistant-03-agent-backed-documentation-guide.md`.

> - The loaded agent profile should constrain the agent toward documentation,
>   architecture explanation, and safe guidance instead of broad repo mutation by
>   default.
> - Provider-specific setup should remain user-configured, but the assistant may
>   supply prompt, context, and mode presets for supported agents.
> --- `docs/work-items/assistant-03-agent-backed-documentation-guide.md`

The work item is marked Planned and asks to define restrictions for editing, commands and out-of-scope answers. It does not supply an admission algorithm, working-context controller, permission grant or implemented fallback. This record does not assert those capacities are absent in external agents; it bounds attribution to Archie.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-role-arguments
Label: Profile role selection at runtime client boundary

Consumer is the external `omp` CLI; channel is symbolic command-line options and the configuration-set request. Force is executable argument construction, conditional on the external parser and configuration contract, not a natural-language recommendation and not proof of model compliance. Horizon is current launch for role flags and intended subsequent configuration consumers for persisted default. Evidence is SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`, particularly the quoted ordinary profile and helper. [RT-RTE-profile-launch](#rt-rte-profile-launch) and [RT-RTE-default-update](#rt-rte-default-update) separate immediate handoff from intended persistence. No observed authority activation or benefit is inferred.

## Annotations

none
