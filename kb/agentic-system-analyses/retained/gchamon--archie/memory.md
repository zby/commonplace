---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Archie memory account: model-role configuration read/modify/write at the external-runtime boundary, with planned context injection separated."
run-id: AAS-2026-10-15-archie-1ab3d8b8ff03-01
source-identity: "https://github.com/gchamon/archie"
reviewed-boundary: 76caf94548cf76f2399d9a7446da15e0daa22685
---

# Archie memory report

## Boundary and evidence

The included subsystem is Archie's shell-based runtime client, not the external agent runtime. Its retained material is the `modelRoles` configuration value requested from and returned to `omp`. The configuration can affect later configuration transformations; its downstream interpretation as a default model remains an external contract. It is not documentation memory or a transcript-derived knowledge store. The assistant's documentation/context proposal is included only as design (SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`, `docs/work-items/assistant-03-agent-backed-documentation-guide.md`).

Direct inspection covered the complete profile module, shell loader, `.zshrc`, override template, Python CLI dispatch, assistant epic and agent-backed assistant work item. All are SRC-1 at the frozen revision. These reads provide implementation and doctrine/design, not execution evidence. Installer deployment and the profile-reference discrepancy are supplied runtime findings, not independently re-inspected here. The source register remains in boundary. The source checkout's HEAD matched the reviewed revision and its short status was empty.

| Entry point or operation | Source path (SRC-1) | Coverage and limits |
| --- | --- | --- |
| All seven profile functions and four aliases | `deployment-packages/local/lib/zsh/commands-agents.sh` | Direct complete read; [RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch). Every function invokes the same configuration helper. Flags and forwarded arguments are current launch input, not retained conversation. |
| Getter, default replacement and setter | `deployment-packages/local/lib/zsh/commands-agents.sh` | Direct complete read; [RT-OBJ-model-roles](runtime.md#rt-obj-model-roles), [RT-RTE-default-update](runtime.md#rt-rte-default-update). Includes subsequent helper read-back; opaque backend prevents a durability guarantee. |
| Shell loading and customization | `deployment-packages/local/lib/zsh/commands.sh`, `deployment-packages/home/.zshrc`, `deployment-packages/local/lib/zsh/overrides.dist.sh` | Direct reads; [RT-RTE-shell-load](runtime.md#rt-rte-shell-load), [RT-RTE-direct-handoff](runtime.md#rt-rte-direct-handoff). Static code loading is not accumulated memory. Actual machine overrides are not supplied. |
| Deployment | `scripts/install.sh` | Supplied [RT-RTE-shell-load](runtime.md#rt-rte-shell-load); not directly re-inspected. Deployment does not demonstrate session reuse. |
| Python CLI dispatch | `src/archie/cli.py` | Direct complete read confirms applet/downgrade/GUI/system registrations, not a parallel profile-memory implementation. Subcommand internals outside the selected boundary are not covered. |
| Planned documentation/context injection | `docs/epics/assistant.md`, `docs/work-items/assistant-03-agent-backed-documentation-guide.md` | Direct complete reads; [RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide). No specified selector, budget or deployed consumer follows from this plan. |
| External session, tool, hook, service and model state | External `omp` and providers, invoked by `deployment-packages/local/lib/zsh/commands-agents.sh` | Outside the frozen implementation. Internal admission, retrieval, compaction, rejection, cleanup and model-visible context remain uninspected. Their absence cannot be inferred from wrapper coverage. |

A bounded search for `omp`, `modelRoles`, `commands-agents`, `compact`, `summari`, `context`, `memory` and `hook` across the shipped `commands*.sh`, `.zshrc`, CLI dispatch and included assistant documents checked the supplied routes for another relevant wrapper operation. The complete module and dispatch reads, not search misses alone, bound the account. Unrelated desktop persistence and contributor-session workflows remain deliberately excluded under boundary; this report makes no repository-wide absence claim.

## Core ideas

The only inspected use-changed retained object is operational configuration. A profile name selects a hard-coded string; a symbolic transform replaces one field of the current object; an external setter is asked to retain the result. This is not automatic extraction of lessons from interaction traces. Initial object provenance and external validation are unknown, while the subsequent `.default` transformation is fully visible ([RT-RTE-default-update](runtime.md#rt-rte-default-update)).

The concrete later consumer is another invocation of the helper's getter/transform chain. Reading the entire object preserves ordinary non-default fields through the next write, but the new profile literal supersedes the old default before launch. This is weaker than evidence that a later agent chooses its model from the retained default. Profile launches also pass an explicit `--model`; direct `omp` calls bypass the wrapper. Neither consumer precedence nor successful persistence is visible ([RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch), [RT-RTE-direct-handoff](runtime.md#rt-rte-direct-handoff)).

Context construction is not implemented by these shell functions. Role names such as `smol` and `plan` do not establish separate contexts, summarization or context budgets. The future assistant's context-injection task is a design requirement, not evidence of current documentation selection or source-trust enforcement ([RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide)).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-model-roles](runtime.md#rt-obj-model-roles)

Storage/form: symbolic JSON in an ephemeral shell variable and CLI argument, with intended persistent storage delegated to `omp`. The frozen source does not reveal a file, database, retention horizon or checkpoint format. The default string is configuration content, not access metadata; other keys are opaque content whose semantics are not established. There is no separately inspected display summary or derived natural-language representation (SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`; minimum passage in [RT-RTE-default-update](runtime.md#rt-rte-default-update)).

Lineage and consumers: the current object originates at external `config get`; its initialization and any external editing are unknown. The helper changes `.default` from a profile literal, retaining other fields for an ordinary object input. A later helper receives the requested whole value and transforms it again. The setter receives the full transformed JSON, not rationale, outcome evidence or criticism. No model is shown receiving either JSON or reasons. The default's downstream behavioral authority is intended configuration authority mediated by external interpretation, not model instruction authority.

#### On [RT-RTE-default-update](runtime.md#rt-rte-default-update)

Read-back is request-driven: invoking a profile causes `config get modelRoles`; the getter names the configuration key, not a semantic retrieval query. The selected retained part is the whole returned value. The shell then replaces the default and supplies the whole result to the setter. There is no wrapper ranking, token budget, unsolicited memory push or independent context-selection stage. A subsequent invocation repeats this chain if external storage fulfills its contract. The earlier default is discarded by replacement; other ordinary object fields can influence the next persisted object by surviving the transform. This establishes wired configuration read/modify/write, not observed retention or inference activation (SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`).

Write agency and curation: profile invocation selects a fixed proposal; code performs the field assignment and setter call. Starting a profile is not per-field human approval. Programmatic callers remain possible. No separate content reviewer or outcome-based evaluator intervenes in the helper. Initial admission control remains external and unknown; that does not obscure the known subsequent transformation. No trace-fed update is shown: the transformation inputs are configuration and a profile literal, not task outcomes. Failure gating, whole-object races and lack of wrapper rollback limit the retained-state guarantee; the supplied record's quotation and forcing cases support these bounds.

#### On [RT-BAP-role-arguments](runtime.md#rt-bap-role-arguments)

The retained value and launch flags have different horizons. Setter input requests persistent configuration change; flags supply current invocation options. Neither channel proves a model sees or follows retained text. Concrete authority at the inspected read-back consumer is the helper's symbolic transformation of the getter result; later model-role interpretation is delegated to `omp`. Source trust is reliance on command resolution and the external getter/setter contract, not an inspected provenance policy for retrieved documents (SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`).

#### On [RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide)

Planned context supply leaves the deciding agent, selected corpus parts, provenance checks, budget and consumption channel unresolved. The work item assigns those decisions rather than implementing them (SRC-1, `docs/work-items/assistant-03-agent-backed-documentation-guide.md`):

> - Define the documentation and architecture context the assistant should inject
>   into the agent session.
> --- `docs/work-items/assistant-03-agent-backed-documentation-guide.md`

> - Define how the assistant should present provenance, confidence, and fallback
>   behavior when the agent response goes beyond the local docs.
> --- `docs/work-items/assistant-03-agent-backed-documentation-guide.md`

These passages establish intended work, not trusted ingestion, source ranking or a working read-back route. The work item is explicitly Planned. Documentation editing/adoption and agent-profile generation policy therefore cannot be assessed as deployed memory curation.

## Write side

[RT-RTE-default-update](runtime.md#rt-rte-default-update) supplies the minimum helper passage and admission account. Acquisition requests an external configuration object; automatic transformation assigns the chosen default; physical I/O is delegated to the external setter. The user ordinarily chooses a function, while software constructs the admitted value. Whether an external setter validates, rejects, migrates or records history is uninspected. Wrapper admission has no separate confirmation, schema validator, evaluator or read-after-write verification (SRC-1, complete `deployment-packages/local/lib/zsh/commands-agents.sh`).

For ordinary JSON object input the transformation preserves non-default keys. This is not a general recovery guarantee: malformed input and pipeline status can undermine acquisition, concurrent snapshots can lose changes, and launch failure occurs after the requested write. A later invocation can replace the default, but the wrapper provides no old-value restore, TTL, deletion, withdrawal log or automatic cleanup. No retained result of evaluating success or failure feeds the next update. These conclusions are local to the complete helper and seven callers, not external `omp` maintenance behavior ([RT-RTE-default-update](runtime.md#rt-rte-default-update)).

There is no raw-trace-to-derived-memory chain or alternative compaction checkpoint in this selected shell implementation. External transcript retention, compaction and numerical-state changes remain uninspected, including the model mutability limits in [RT-CMP-model-services](runtime.md#rt-cmp-model-services). Profile literals are authored static code; deployment/loading is code delivery, not a trace-fed transformation. The planned assistant adds no implemented document-admission mechanism ([RT-RTE-shell-load](runtime.md#rt-rte-shell-load), [RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide)).

## Read-back

The concrete implemented request chain is subsequent profile invocation → helper getter → whole roles value → `jq` transformation → setter. It can carry non-default configuration across invocations, conditional on external persistence. It does not carry a prior answer, reasoning episode or summary into an inspected model invocation. Budget is the returned value as a CLI argument; no content/token-selection budget is specified in the wrapper ([RT-RTE-default-update](runtime.md#rt-rte-default-update)).

Potential later default use by the external runtime is a separate, uninspected consumer contract. Immediate profile launch cannot prove that use because it supplies its own model option. Likewise, direct invocation affords bypass but does not demonstrate a particular default-resolution policy ([RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch), [RT-RTE-direct-handoff](runtime.md#rt-rte-direct-handoff)).

No wrapper mechanism isolates tasks into model contexts, removes old turns, compacts tool results, leaves a reloadable stub, or reloads removed model context. This bounded statement follows the complete profile-module read; the external runtime may do any of these. The shell's local variable lifetime is not a model-context frame. Stack-frame or heap analogies would therefore misdescribe this inspected mechanism. The assistant plan also supplies no concrete context size, eviction policy or reload route (SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`, `docs/work-items/assistant-03-agent-backed-documentation-guide.md`).

## Integration issues

- No supplied fact requires correction, and no new declaration duplicates a supplied record; existing referents receive annotations.
- Persistence and external consumer issue: getter/setter implementation, durable backend, write validation, concurrency semantics and runtime default precedence are not frozen. This prevents claiming durable preservation or later model activation from [RT-OBJ-model-roles](runtime.md#rt-obj-model-roles), [RT-RTE-default-update](runtime.md#rt-rte-default-update) or [RT-BAP-role-arguments](runtime.md#rt-bap-role-arguments). The directly supported later consumer is the next helper transformation, not an observed model invocation.
- Context-design issue: [RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide) assigns future documentation injection and provenance/fallback decisions. It cannot support deployed selection, trust or budget conclusions. External session and context-control routes remain uninspected, not absent.

## Limitations and checks

The source identity and reviewed commit match the supplied boundary. HEAD was rechecked and source status was clean. The supplied contracts and pinned inputs governed this report; no prior analyses, external sources, target executions or runtime fixtures were used. Direct implementation reads were kept separate from supplied runtime findings and doctrine/design. No observed-run or causal-experiment evidence establishes activation, improved capacity or benefit.

Countercases checked before settling the account include explicit launch options superseding an assumed default consumer, direct invocation bypass, helper failure/pipeline ambiguity, whole-object concurrent writes, and configuration surviving failed launch. These prevent stronger persistence, safety and context claims without negating the visible transformation.

Deterministic validation: the initial check found only the disallowed pending marker; it was removed. The final validate-output check passed. This checks form and quotation occurrence, not analytical correctness or acceptance.
