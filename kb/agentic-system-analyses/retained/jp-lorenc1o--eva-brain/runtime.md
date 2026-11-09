---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Eva-brain runtime baseline: desktop ingest, branch admission, read-only consumers, settings and local-runtime setup at the frozen revision."
run-id: AAS-2026-11-09-eva-brain-de4240cd9e79-01
reviewed-boundary: "706fb91f4ee851cc355785f4e7c6eab37146938f"
---

# Eva-brain runtime report

## Runtime account

Eva is a desktop knowledge-maintenance application, not the model's inner tool loop. The Tauri frontend owns user interaction; Rust owns source copying, subprocess dispatch, Git branches, admission and operation events. Codex CLI, Claude Code or OpenCode owns model/tool progression inside a dispatched task. Retained Markdown supplies later tasks. The entry points are registered in SRC-1, `apps/desktop/src-tauri/src/main.rs`; the main orchestration is SRC-1, `apps/desktop/src-tauri/src/ingest.rs`. All findings below concern inspected implementation or source-native doctrine, not observed execution. No target code or tests were executed and no execution trace or causal comparison was supplied.

### Ordinary invocation: source to retained wiki

A person creates or imports a brain, selects sources, and starts ingest. Creation initializes Git and bootstraps missing infrastructure. Import copies into the managed library; a dirty existing Git source or a Git worktree is rejected. Existing operating files are preserved rather than overwritten. Opening a vault calls `ensure_schema`, then reloads Markdown, builds the vault and graph, and runs structural lint (SRC-1, `apps/desktop/src/main.ts`, `apps/desktop/src-tauri/src/ingest.rs`). Settings/bootstrap are covered by [RT-RTE-brain-settings](#rt-rte-brain-settings).

[RT-RTE-source-ingest](#rt-rte-source-ingest) begins with `ingest_enqueue`: validate the brain and runtime, require Node/tools, copy sources into `raw/` without replacing an existing destination, also discover non-hidden files already in `raw/`, sort names and queue them. A substring occurrence of the source name in `log.md` excludes it, including a prior rejection. Queue/current-job membership also suppresses duplicates. Source files are committed before dispatch. This is identity-by-name/log text, not content-addressed change detection.

A single Rust worker pops jobs from an in-memory queue. Each job has a numeric ID, vault path and source name. `run_job` reads runtime/model/profile settings from the vault, records the current HEAD and baseline lint issues, creates an `ingest/...` branch and a temporary Git worktree, then launches the selected adapter there. The model receives a natural-language extraction task: read `EVA.md`, read the raw source, search existing pages, merge instead of duplicate, preserve provenance and link new pages. The external runtime selects reads and writes. Claude/OpenCode get Eva MCP navigation; Codex uses native filesystem tools and `rg`. Their return is a textual summary, not the patch: the actual worktree determines the proposed edit.

On successful subprocess return, `gate_agent_changes` checks protected paths in both working status and the committed range, requires uncommitted changes, stages the worktree, commits agent edits, appends an Eva-owned log entry and commits it. It computes deletions without rename detection and compares lint issue strings against the baseline. No deletions and no new issue permits automatic merge. Otherwise it retains branch/worktree and sends a diff, deletions, issues and summary to the UI. A hold pauses the worker until a person accepts or rejects; acceptance merges despite the listed lint issues, while rejection discards the branch and logs rejection. Terminal outputs are merged/held/failed events, job status and, on merge, retained wiki content. Frontend `ingest:merged` reloads the brain (SRC-1, `apps/desktop/src/main.ts`).

Recovery is local and limited: agent/gate errors clean the worktree and branch; rejected branches are forcibly removed. Queue and held metadata are process memory, while Git branches and accepted content are filesystem state. The inspected worker has no durable queue reconstruction. A failed merge after a held item has been removed from state does not restore that item in `ingest_decide` or `query_decide`; code returns the Git error before cleanup. This is not an inspected crash-recovery guarantee (SRC-1, `apps/desktop/src-tauri/src/ingest.rs`).

### Alternate consumers and distinct admission paths

[RT-RTE-vault-query](#rt-rte-vault-query) launches a separate read-oriented subprocess on the real vault, not an ingest worktree. Optional working-set IDs become a prompt restriction. The returned JSON is parsed and checked for nonempty answer text, then displayed with citations. It is not automatically retained. A person can save it through [RT-RTE-analysis-save](#rt-rte-analysis-save): Rust constructs a Markdown analysis, index entry and log in a new worktree; every such save is held for explicit review, even with no lint issue. The UI also converts a profile-tool result to the same `QueryAnswer` shape and calls `query_save`. The command accepts a supplied answer object, not a signed or session-bound model result (SRC-1, `apps/desktop/src/main.ts`, `apps/desktop/src-tauri/src/ingest.rs`).

Health and profile tools use [RT-RTE-advisory-tools](#rt-rte-advisory-tools). Health asks for contradictions, provenance weaknesses, stale claims, gaps and questions; `nextStep` is advice, not an executed maintenance action. Profile tools generate cited products using profile-specific instructions and user customization. Their tool loop remains in the external runtime. There is no Eva-owned automatic health-to-edit loop in these inspected commands. Profile result saving uses the human-reviewed analysis route, not ingest auto-admission.

The MCP server has four read tools and reloads the wiki per call; no write tool is registered. This limits that server's channel, not the entire agent. `loadVault` excludes raw files, dot paths and infrastructure from wiki navigation; filesystem tools can still read the source and operating contract. MCP search selects at most ten lexical matches; read_page returns full page content and graph links. These are symbolic selection rules over natural-language material, not embedding retrieval (SRC-1, `packages/eva-mcp/server.mjs`, `packages/eva-mcp/vault-io.mjs`). This adds inspection of the complete server and loader to the boundary's initial coverage; memory transformations remain the memory analyst's responsibility.

### Controls, forcing cases and limits

The capability surface differs from the grant requested by Eva, and both differ from installed isolation. Codex receives `workspace-write` for ingest and `read-only` otherwise, plus ephemeral/config-isolation flags. Claude receives an allowed-tool list: filesystem write tools for ingest, only read/navigation tools otherwise; it gets strict MCP configuration and empty settings sources. OpenCode runs its build agent with `--auto`; generated permissions deny external-directory access and web tools, and additionally deny write/edit/patch/bash on read-oriented operations. Eva does not implement those runtimes' sandbox engines. Their installed versions, user environment and external subprocess behavior are not frozen (SRC-1, `apps/desktop/src-tauri/src/ingest.rs`).

Four forcing cases bound the conclusions:

1. **Agent commits protected edits itself.** `verify_agent_write_boundary` inspects both uncommitted status and base-to-HEAD path differences, so a clean status alone is not enough. An agent that commits all ordinary page edits but leaves no uncommitted change also gets the gate's “no changes” error rather than an automatic merge. The guarantee is a gate-local rejection rule, not a filesystem prohibition. It covers the named protected paths on ingest admission, not direct damage outside that worktree or every external tool effect. No such damage is demonstrated here.
2. **Rename or inherited lint debt.** `--no-renames` converts a move into delete/add, forcing a hold. Existing issue strings do not force review; only new strings do. Human acceptance can merge a held branch with issues. Structural lint checks links, inbound-link presence, title/type, summary source prefix and suspicious path roots; it neither proves semantic correctness nor even proves every page is reachable from the index. A mutually linked disconnected group can meet the inbound-link test. Thus the admission predicate is not a knowledge-quality oracle ([RT-CLM-structural-gate](#rt-clm-structural-gate)).
3. **Nonempty versus empty working set.** Supported query/profile callers pass `Option<Vec<String>>`; normalization checks lengths and deduplicates IDs but does not check page existence. Empty scope explicitly permits the whole brain. Nonempty scope only changes instruction text. MCP receives the full vault root, its schemas have no scope argument, and returned citations are not checked against scope. Native filesystem tools likewise remain available. The “strict” set is therefore model-directed policy, not an Eva-enforced read exclusion; actual out-of-set behavior is unobserved ([RT-RTE-vault-query](#rt-rte-vault-query)).
4. **Read-only output later becomes a write.** Query/profile results are display-only until save, but `query_save` constructs persistent content through a separate Rust path with mandatory human decision, not the ingest protected-path gate. This distinction prevents treating either “queries never affect the vault” or “all writes pass the ingest gate” as system-wide invariants. Settings, bootstrap, source copying and log writes are other deliberate non-agent writers.

For ingest admission the owner is Rust, enforcement is the gate, strength is an invariant of that inspected path, implementation conclusion status is wired and operation conclusion status is uninspected. Its external contracts are Git's path/status/diff/merge semantics, filesystem behavior and the lint CLI. Review is an admission policy: it is not independent semantic verification. For read-oriented runtime containment the owner is the external runtime, enforcement is requested via CLI/config, strength is a deployment guarantee contingent on runtime semantics, implementation conclusion status is wired for Eva's requests and operation conclusion status is uninspected. The source itself documents residual Claude memory-file discovery and OpenCode global-config merging; neither Eva's flags nor its post-hoc ingest gate establish whole-machine privacy, network isolation or universal nonmutation (SRC-1, `apps/desktop/src-tauri/src/ingest.rs`).

Working-context control at Eva's boundary is task-level separation and selected delivery: each command starts a subprocess with its own generated prompt rather than passing a foreground conversation. Ingest edits and summary escape that task; read-oriented tasks return structured results. This resembles a task frame only at the Eva caller boundary, not a proven clean model context: external runtimes own their internal histories, compaction, automatic memory loading and tool scheduling. MCP search returns ten ranked excerpts and explicit read_page can reload full content. The working-set instruction requests a narrower evidence window without removing other pages from the tools. Eva does not inspect model token windows or verify that selected evidence controlled the result (SRC-1, `apps/desktop/src-tauri/src/ingest.rs`, `packages/eva-mcp/server.mjs`).

Distributed-parametric reasoning is supplied by [RT-CMP-codex](#rt-cmp-codex), [RT-CMP-claude](#rt-cmp-claude) or [RT-CMP-eva-qwen](#rt-cmp-eva-qwen). Eva supplies no inspected weight-training loop. Runtime/model selection is mutable settings, while local setup installs capabilities through [RT-RTE-runtime-setup](#rt-rte-runtime-setup). That setup consumes live distributions and model tags rather than this repository's immutable code boundary. Product code changes enter through ordinary repository/build/release activity, not a model-driven self-patching command in the inspected Tauri registry. `apps/desktop/scripts/bundle-tools.mjs` stages MCP/lint code and built wiki-lib into app resources and installs runtime dependencies; this is additional inspected implementation coverage, not evidence of a completed release. The vault's behavioral instruction path is [RT-BAP-vault-contract](#rt-bap-vault-contract).

## Shared records

### Components

#### RT-CMP-codex
Label: Codex CLI model endpoint

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`: distributed-parametric model reasoning behind the external Codex CLI; parameter substrate is provider-owned and outside inspection. Eva launches `codex exec`, sends the prompt on stdin, reads the last-message file and rejects unsuccessful/empty results. Runtime default or a configurable model string selects the model, not an immutable weight revision. Parameter changes during operation are uninspected inside the provider; Eva's adapter implements no training. A default or alias endpoint may resolve to a different model; exact version fixity is not established.

> if !config.model.is_empty() {
>             command.args(["--model", &config.model]);
>         }
> --- `apps/desktop/src-tauri/src/ingest.rs:2379-2381`

#### RT-CMP-claude
Label: Claude Code model endpoint

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`: distributed-parametric reasoning behind Claude Code, with external provider weight storage. Configurable model and effort are passed only when nonempty. Exact model revision is not pinned by Eva; a runtime default or mutable model name can change resolution. Provider parameter mutation is uninspected; no Eva training operation is present in the adapter. This is distinct from Codex by dispatcher and runtime control contract, not evidence of distinct fixed model weights.

> command.args(["--strict-mcp-config", "--setting-sources", ""]);
> --- `apps/desktop/src-tauri/src/ingest.rs`

#### RT-CMP-eva-qwen
Label: Eva local Qwen model

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`: distributed-parametric local reasoning served by Ollama through OpenCode's OpenAI-compatible provider. Weight substrate is the external local Ollama model store. Base tag `qwen3.5:4b` becomes derived tag `eva-qwen3.5:4b`, with `num_ctx` 32768. The derivation configures inference context, not an inspected parameter-learning step. Exact weight digest is not pinned or verified; local tags and the serving endpoint are mutable. No parameter update is requested during ordinary task operation; Ollama internals remain uninspected.

> let modelfile = format!("FROM {OPENCODE_BASE_MODEL}\nPARAMETER num_ctx {OPENCODE_NUM_CTX}\n");
> --- `apps/desktop/src-tauri/src/ingest.rs`

### Operative objects

#### RT-OBJ-ingest-worktree
Label: Ingest branch and worktree

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`: temporary filesystem checkout associated with a Git branch and base commit. Natural-language Markdown edits and symbolic Git state are separate operative parts: the external agent interprets page content while Git/gate rules consume paths and diffs. Accepted content persists in the vault; held content remains in its branch pending a process-held review entry. Cleanup force-removes worktree and deletes branch; Git history of successful merges remains. This object describes staging and coordination, not a finding that every edit is safe or correct.

> let branch = format!("ingest/{slug}");
>     let worktree = std::env::temp_dir().join("eva-worktrees").join(&slug);
> --- `apps/desktop/src-tauri/src/ingest.rs`

### Routes

#### RT-RTE-source-ingest
Label: Source ingest and branch admission

Endpoints: user-selected/source-directory files → raw commit → queued job → model worktree edits → Rust gate → merge or held human decision. Owner: Rust for progression and admission; external runtime/model for edit proposals. Natural-language guidance asks for search-before-write, merge-over-duplicate, provenance and links; symbolic gate consumes Git path changes and lint issue strings. Operating mode: open source-ingestion tasks, not a bounded experiment. The person supplies sources; software admits clean proposals automatically, with a human veto/accept decision on held branches. No expected semantic answer is supplied: lint is a structural comparator, not an answer oracle. Recovery is cleanup/rejection with local Git history; no automatic semantic rollback is demonstrated. Guidance and accepted wiki persist, as does Eva's log; failed/rejected proposals are not merged.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: enqueue returns job count; events carry activity, merged page count/summary, held diff or failure.
- Later read-back: merged Markdown is reloaded by desktop and later model tasks; log text also controls source eligibility.
- Delegated visibility: subprocess sees the worktree and prompted raw source, plus filesystem/MCP access according to the adapter; parent receives summary and filesystem diff, not an independently checked reasoning trace.
- Selection predicate: source names not already in log text or queued/current names, then sorted; admission requires no deletion and no new lint issue for automatic merge.
- Invalidation or expiry: branch/worktree removed on cleanup; no automatic content expiry; recorded names suppress re-ingest even after rejection.
- Activation or effect: commits retained wiki edits and operation log, or holds them for a human; downstream behavioral change is not observed.
- Evidence limits: static implementation establishes wiring, not compliance with extraction guidance or quality gain; runtime sandbox internals are external.

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`:

> if deletions.is_empty() && new_issues.is_empty() {
> --- `apps/desktop/src-tauri/src/ingest.rs`

> names.retain(|n| !log_text.contains(n.as_str()));
> --- `apps/desktop/src-tauri/src/ingest.rs`

> verify_agent_write_boundary(worktree, base_commit)?;
> --- `apps/desktop/src-tauri/src/ingest.rs`

#### RT-RTE-vault-query
Label: Vault query with optional working set

Endpoints: frontend question and optional page IDs → Rust normalization → runtime-specific read-oriented invocation → JSON cited answer → UI. Owner: person chooses question/scope; model selects evidence and composes answer; Rust parses response and checks nonempty text. Operating mode: open requests. No expected-answer oracle or independent factual veto is implemented in this path. Policy form is natural-language evidence/scope instruction plus symbolic runtime configuration and JSON parsing. State is current invocation and retained vault, without an Eva chat continuation/compaction loop.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: parsed `QueryAnswer` with Markdown answer and page/source citations; error on invalid/empty response.
- Later read-back: inapplicable — querying alone writes no retained answer through the Eva command; saving is a separate route.
- Delegated visibility: runtime gets vault root, question, scope instruction and read tools; Eva receives final structured output, not the full tool history.
- Selection predicate: model-directed search/read; nonempty scope instructs restriction but is not applied to MCP or filesystem consumers; empty/absent scope permits whole brain.
- Invalidation or expiry: per-invocation subprocess/config files are temporary; latest UI answer can be replaced; no retained-answer expiry applies until save.
- Activation or effect: delivers answer to the person; no observed compliance, factual accuracy or scope exclusion.
- Evidence limits: supported input shapes and all three adapters were inspected; CLI read-only enforcement depends on external runtimes, and actual out-of-scope reading is unobserved.

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`:

> let scope = normalize_working_set(scope.unwrap_or_default())?;
> --- `apps/desktop/src-tauri/src/ingest.rs:3653-3670`

> return "No working set is active; use the whole brain as needed.".into();
> --- `apps/desktop/src-tauri/src/ingest.rs`

> let result = run_codex_agent(vault, &prompt, "read-only", Some(codex_query_schema()), config)?;
> --- `apps/desktop/src-tauri/src/ingest.rs`

SRC-1, `packages/eva-mcp/server.mjs` supplies the counterweight to a hard scope interpretation:

> const vault = () => loadVault(VAULT);
> --- `packages/eva-mcp/server.mjs`

#### RT-RTE-analysis-save
Label: Saved analysis admission

Endpoints: supplied question/answer object → Rust-formatted analysis/index/log in query worktree → review payload → accept/reject command → merge/discard. Owner: software prepares; human action in the shipped UI proposes save and decides admission. The command itself does not authenticate human identity or require a preceding query invocation. Model or caller supplies content; Rust chooses filename/title and filters reference strings, but embeds answer prose. Operating mode: optional retention after open queries or profile tools. No answer oracle; structural issues are displayed rather than an automatic veto on acceptance. Recovery uses cleanup and rejection logging; Git history supports inspection but no automatic semantic reversal is wired here.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: review ID, diff, new lint issues and deletions; decision returns success/error.
- Later read-back: accepted analysis and index are ordinary retained wiki consumed by later search/read and desktop reload.
- Delegated visibility: inapplicable — save uses Rust filesystem/Git operations, not a second agent; reviewer sees the generated diff.
- Selection predicate: supplied answer is formatted for a unique dated analysis path; all saves require an accept decision, not merely dirty lint cases.
- Invalidation or expiry: rejection removes proposed branch/worktree; accepted content has no automatic expiry; one pending save at a time in shared query state.
- Activation or effect: merges answer-derived content after acceptance; rejects leave only rejection log; later reliance and benefit unobserved.
- Evidence limits: supplied citations and prose are not semantically verified; UI human decisions do not make every possible command caller a human principal.

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`:

> if st.saving || st.held.is_some() {
>             return Err("resolve the pending analysis review before saving another answer".into());
>         }
> --- `apps/desktop/src-tauri/src/ingest.rs`

> fs::write(&page_path, analysis_markdown(question, answer, &title))
>             .map_err(|e| format!("write analysis: {e}"))?;
> --- `apps/desktop/src-tauri/src/ingest.rs`

#### RT-RTE-advisory-tools
Label: Health and profile-tool advice

Endpoints: user request/profile/options → read-oriented external model loop → parsed health findings or titled profile result → UI. Owner: Rust dispatch and parse; model diagnosis/composition; person determines next action. Policy form: natural-language evidence caution, profile extraction/maintenance lens, optional scope instruction and symbolic option limits. Operating mode: open advisory requests; health is not an automatic edit trigger. No independent expected-answer oracle: generated exam answers are products, not an externally supplied correctness reference. Rejection of malformed/empty output is software-controlled; substantive rejection belongs to the person. These commands do not admit product/instruction changes; optional profile-result retention is [RT-RTE-analysis-save](#rt-rte-analysis-save).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON health summary/findings or profile title/content/citations, displayed by the frontend.
- Later read-back: inapplicable — advisory invocation alone persists no finding; profile output can be separately saved.
- Delegated visibility: external runtime reads actual vault with read-oriented controls; caller receives structured final result only.
- Selection predicate: model chooses supporting pages under profile guidance; profile-tool scope is prompt-directed as on query; health is vault-oriented without a scope parameter.
- Invalidation or expiry: frontend resets health on vault opening; no durable automatic expiry or maintenance schedule is established.
- Activation or effect: suggestions and derived work reach the person, not an automatic maintenance executor.
- Evidence limits: requested contradiction analysis is not observed criticism or a demonstrated knowledge revision; schema/summary checks do not establish semantic correctness or compliance with requested finding count.

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`:

> `nextStep` is only a suggested action. Return no more than 12 findings.
> --- `apps/desktop/src-tauri/src/ingest.rs`

> if result.content.trim().is_empty() {
>         return Err("agent returned an empty tool result".into());
>     }
> --- `apps/desktop/src-tauri/src/ingest.rs`

#### RT-RTE-brain-settings
Label: Brain bootstrap and settings admission

Endpoints: create/import/open/settings commands → symbolic validation and text-template edits → Git-backed contract/manifest/starter state. Owner: person supplies choices through UI; software validates and writes. New/imported brains receive missing infrastructure, not replacement of existing instruction files. Settings require clean Git state and replace profile sections in `EVA.md` and manifest fields. Proposed changes concern language, purpose, extraction profile, runtime, model and effort; these can shape later prompts and dispatch. Admission is direct command success, not the agent gate or a second diff review. Human content control is supported by shipped UI choices, not independently proven for arbitrary callers. Operating mode: configuration, not experimentation; no answer oracle. Failure on create/import removes newly created destination; settings retain Git history but have no inspected automatic transaction rollback after partial I/O failure.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: brain path/entry/settings or error.
- Later read-back: runtime configuration and profile guidance are reread for later tasks; agents are told to read the retained `EVA.md`.
- Delegated visibility: inapplicable — template/filesystem edits are executed by Rust, not a model worker.
- Selection predicate: create/import validates paths and compatibility; bootstrap writes missing files; settings edit specified sections after clean-status check.
- Invalidation or expiry: settings remain until changed; existing operating files survive bootstrap; local Git provides history, not automatic expiry.
- Activation or effect: changes future adapter/model selection and supplied extraction guidance; actual model adherence remains unobserved.
- Evidence limits: configuration changes are implemented behavioral inputs, not evidence of learning or successful self-improvement.

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`:

> return Err("commit or resolve the brain's current changes before updating its settings".into());
> --- `apps/desktop/src-tauri/src/ingest.rs`

> if !root.join("EVA.md").exists() {
>         fs::write(root.join("EVA.md"), eva_schema(profile)).map_err(|e| e.to_string())?;
>         staged.push("EVA.md");
>     }
> --- `apps/desktop/src-tauri/src/ingest.rs`

#### RT-RTE-runtime-setup
Label: Local runtime capability installation

Endpoints: UI setup command → ensure Ollama installed/server ready → pull tagged base model → create larger-context derived model → install OpenCode if missing → readiness check. Owner: person starts setup; Rust decides missing components and invokes external installers; distributor determines downloaded code/model content. Policy form: symbolic presence/version checks and fixed download locations/tags, not model judgment. Operating mode: setup, not an improvement experiment. Admission does not ask a person to approve each installed byte; it uses installer exit status and readiness checks. Known-old Ollama is rejected when its version is parsed; unknown versions do not block, outside-verified versions warn. No answer oracle. Recovery cleans download/config intermediates but does not establish rollback of installed apps/models. This is capability admission, not model-generated modification of Eva's own code.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: progress events and readiness success/error.
- Later read-back: subsequent runs resolve installed CLI programs and local model tag; generated model config persists in external Ollama storage.
- Delegated visibility: external installer shell and Ollama processes operate on the host; no Eva model proposal is involved.
- Selection predicate: component/path/model presence and parsed version; missing components trigger install or pull, present derived model is reused.
- Invalidation or expiry: installed components persist; tags and live download endpoints are not immutable; no pinned-digest invalidation is implemented in this route.
- Activation or effect: makes local adapter available for later ingest/query/health/tools; actual successful installation or operation at this revision is unobserved.
- Evidence limits: external distribution contents and runtime internals are not frozen, and readiness is not an end-to-end semantic test.

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`:

> .arg("curl -fsSL https://opencode.ai/install | bash")
> --- `apps/desktop/src-tauri/src/ingest.rs`

> if model_present(&list, OPENCODE_DERIVED_MODEL) {
>         emit_setup(app, SetupStep::DerivedModel, "done", "Model configured");
> --- `apps/desktop/src-tauri/src/ingest.rs`

### Claims

#### RT-CLM-structural-gate
Label: Structural review claim

SRC-1, `schema/EVA.md` claims new lint issues and deletions require human review. The implementation supports that predicate on the ingest branch route, not universal semantic correctness, hard nonmutation of raw files, or review of every possible filesystem write. Lint enumerates structural checks; issue comparison is string membership. The human may accept held issues. Summary provenance checks require a `raw/` prefix, not proof that cited text entails the summary or even verification of source content. These distinctions constrain downstream interpretation of [RT-RTE-source-ingest](#rt-rte-source-ingest).

> New lint issues and deletions
> require human review before merging.
> --- `schema/EVA.md`

SRC-1, `packages/wiki-lib/src/lint.ts`:

> } else if (!source.startsWith('raw/')) {
> --- `packages/wiki-lib/src/lint.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-vault-contract
Label: Retained vault contract to agent behavior

Consumer: external runtime/model on ingest and read-oriented tasks. Channel: retained root `EVA.md` plus generated task prompts directing its reading; Claude-compatible/agent-neutral entry files are installed alongside it. Force: natural-language instruction to follow schema/profile, combined with symbolic dispatch settings parsed by Rust; neither delivery nor requests prove model compliance. Horizon: later tasks on the same retained brain until human settings/file changes. Settings admission and protected-path rejection separate human configuration changes from agent proposals. Source-authored knowledge enters the model via page reads, but this record concerns the operating contract, not the authority of every wiki statement.

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`:

> 1. Read EVA.md at the brain root first. It defines page types, provenance, directories, linking, and the merge-over-duplicate policy. Follow it exactly.
> --- `apps/desktop/src-tauri/src/ingest.rs`

SRC-1, `schema/EVA.md` states the intended effect:

> Treat these settings as
> instructions: write pages in the working language unless the human asks
> otherwise, and use the stated purpose to calibrate what is worth preserving.
> --- `schema/EVA.md`

## Annotations

none
