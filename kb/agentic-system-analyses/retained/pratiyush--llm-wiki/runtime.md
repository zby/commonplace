---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "llm-wiki runtime baseline: session conversion, backend synthesis, host handoff, retrieval and publication at the frozen commit"
run-id: AAS-2026-10-16-llm-wiki-6786c5985cdc-01
reviewed-boundary: b1088890ee0743810a92577aecad946c6b3eb2d2
---

# llm-wiki runtime report

## Runtime account

### Work and ordinary invocation

llm-wiki combines deterministic file-processing commands with instructions interpreted by an external coding agent. It claims to compile coding-session history into an interlinked wiki. It is not one autonomous model loop. The ordinary shipped `/wiki-sync` procedure first invokes Python conversion, then instructs the foreground agent to ingest newly converted files, and finally completes any pending agent-backend syntheses. A plain `llmwiki sync` does not itself execute that semantic ingest. SRC-1: `CLAUDE.md`, `.claude/commands/wiki-sync.md`, `llmwiki/cli.py`. See [RT-RTE-session-conversion](#rt-rte-session-conversion), [RT-RTE-host-ingest](#rt-rte-host-ingest) and [RT-RTE-agent-completion](#rt-rte-agent-completion).

> 3. **If `N > 0`**: for each newly written markdown file under `raw/sessions/`, follow the **Ingest Workflow** from `CLAUDE.md`. Process one project at a time. If there are more than 20 new files total, ask the user whether to process them all or a subset first.
> --- `.claude/commands/wiki-sync.md`

The user initiates the slash command; the host schedules the model and supplies tools. The Python CLI selects adapters, filters changed source files, normalizes records, renders redacted/truncated Markdown, guards writes, and persists conversion state. On successful conversion, the CLI may build and lint according to schedule. Control returns to the foreground agent, which is asked to read raw files plus index/overview, produce source pages, update concepts/entities and navigation, retain conflicting claims, and log the operation. Its terminal response reports conversion counts, updated projects/pages and contradictions. Pending UUID prompts are completed serially in that same conversation, not by an agent invoked by the backend. Host/model identity, current permissions, isolation and actual compliance are not supplied. SRC-1: `llmwiki/cli.py`, `llmwiki/convert.py`, `CLAUDE.md`, `.claude/commands/wiki-sync.md`.

A separate command, `llmwiki synthesize`, resolves a configured backend from `examples/sessions_config.json`, checks availability, loads raw Markdown and mtime state, calls the backend for changed files, wraps returned text in source-page metadata, writes under `wiki/sources/<project>/<date>-<slug>.md`, saves state, and rebuilds the index after successful writes. It does not perform all the entity/concept/overview maintenance requested by the host ingest procedure. Backend selection can yield canned dummy output, an Ollama HTTP request, or a pending-agent placeholder; therefore a successful synthesis counter is not proof of completed model synthesis. SRC-1: `llmwiki/cli.py`, `llmwiki/synth/pipeline.py`, `llmwiki/synth/base.py`, `llmwiki/synth/agent_delegate.py`. See [RT-RTE-backend-synthesis](#rt-rte-backend-synthesis).

> out_path.write_text(page_content, encoding="utf-8")
>
>             # Update state
>             state[rel] = p.stat().st_mtime
>             summary["synthesized"] += 1
> --- `llmwiki/synth/pipeline.py`

This is an implementation account, not a successful-run report. SRC-1 supplies implementation and doctrine/design only. No provider, target command, test or example was executed for this report. End-to-end operation, activation of retrieved knowledge, answer quality, speed and benefit remain unobserved. The frozen [boundary](boundary.md) fixes the whole-system scope and external-host exclusions.

### Material alternate and forcing cases

Four forcing cases constrain the baseline:

1. **Default/unknown backend:** the resolver defaults to dummy and falls back to dummy for unknown names; its canned output is still written as a source page. An unavailable configured backend instead returns an error through the CLI; comments promising automatic fallback on unavailable agent detection do not match that dispatch. SRC-1: `llmwiki/synth/pipeline.py`, `llmwiki/synth/base.py`, `llmwiki/cli.py`.
2. **Agent backend:** the pipeline records a placeholder as synthesized before the external foreground agent completes it. UUID checking protects the completion association, not semantic correctness; prompt reuse searches by slug alone, not the project/date composite. Thus the header identity and later page sentinel are material coordination state, not a completed generation guarantee. SRC-1: `llmwiki/synth/agent_delegate.py`, `llmwiki/synth/pipeline.py`.
3. **MCP sync:** a caller-facing confirmation gate constructs a child CLI command with `--dry-run` by default, but the inspected sync parser has no such option. The default route therefore reaches an argument-error path, not a preview conversion. With `dry_run=false` and `confirm=true`, the flag is omitted and ordinary sync can execute. The handler does not inspect the child's return code before returning `_ok(output)`. No execution is supplied; these are source-grounded control-flow findings. SRC-1: `llmwiki/mcp/server.py`, `llmwiki/cli.py`. See [RT-RTE-mcp-access](#rt-rte-mcp-access).
4. **Publication model route:** `build --synthesize` invokes an external Claude executable directly, outside the source-page backend selector. It supplies a bounded metadata brief, not the raw-body synthesis prompt, and uses the returned prose for the reader landing page. Consequently neither backend configuration nor the source-page prompt cap governs this model path. SRC-1: `llmwiki/build.py`. See [RT-RTE-reader-build](#rt-rte-reader-build).

These cases challenge model-call, completion, permission and evidence-strength assumptions without executing the target. Provider-native tools, host shell policy and remote-worker internals are not available for inspection and are not credited as llm-wiki controls. Shipped adapter imports expose Python code execution in the invoking process; `llmwiki/adapters/__init__.py` has a fixed contrib-name set and import-based registration, not evidence of an isolated extension sandbox. Current enabled adapters and actual host grants are deployment facts not supplied by this checkout.

### Guarantee scope and effect boundaries

**Raw immutability is a scoped write policy, not an invariant over the filesystem.** Owner: converter. Enforcement point: `_raw_write_guard`, immediately before both Markdown-copy and normalized-session writes. Covered paths: those two converter branches. An existing output is rejected/quarantined unless `force` is true; collision handling may choose another filename first. External contract: filesystem access and callers using this converter. Alternate paths: host tools, editor writes, direct filesystem changes and `--force` are outside the refusal guarantee. Instruction text also forbids raw edits, but does not revoke host tools. Guarantee strength: policy. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1: `llmwiki/convert.py`, `CLAUDE.md`.

> if not out_path.exists() or force:
>         return
> --- `llmwiki/convert.py`

**Semantic provenance and contradiction preservation are requested behavior.** Owner: foreground agent or synthesis model. Enforcement point: instructions in the host schema and source-page template, not a veto before every wiki write. The pipeline accepts backend text and writes it; the candidate workflow is another optional admission mechanism, not a universal gate. External contract: host loads the schema and the model follows it. Direct writes, dummy output and completion helpers do not establish compliance. Guarantee strength: best effort. Implementation conclusion status: afforded. Operation conclusion status: uninspected. SRC-1: `CLAUDE.md`, `llmwiki/synth/prompts/source_page.md`, `llmwiki/synth/pipeline.py`, `llmwiki/candidates.py`.

> 2. Every claim must be traceable to something said in the session
> --- `llmwiki/synth/prompts/source_page.md`

**MCP read containment is endpoint-specific.** Owner: MCP server. Enforcement point: resolved-path containment plus allowlist in `tool_wiki_read_page`. It covers explicitly requested page reads, not all host Read tools or the server's independently implemented corpus traversal/query/export operations. Required external contract: ordinary filesystem resolution and stable files during the check/read interval; no deployed filesystem isolation is established. Guarantee strength: policy. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1: `llmwiki/mcp/server.py`.

**Local Ollama privacy is a default, not a network prohibition.** Owner: configuration loader/HTTP adapter. Enforcement point: default loopback URL and warning when another host is configured. A remote URL is allowed. The request carries the first 8,000 body characters and metadata. Host delegation and build-time Claude are separate egress paths. Required external contract: configured service and its own data handling. Guarantee strength: best effort. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1: `llmwiki/synth/ollama.py`.

### Context, coordination and recovery

Working-context controls differ by route. Ollama and pending-agent rendering slice the raw body to 8,000 characters, retaining the prefix preferentially and leaving the complete file on disk for separate reads. This is input filtering, not host conversation compaction. Build-time Claude receives grouped counts/dates/models and up to eight slugs per project, with a 32,000-byte total prompt cap; truncation can cut JSON mid-document. MCP query selects lexical matches under per-file/aggregate scan budgets and returns snippets plus an overview prefix. Host query doctrine instead asks the model to read index/overview and folder `_context.md` before deciding which full pages to read. These paths constrain delivered context differently; none demonstrates that selected content changed an answer. SRC-1: `llmwiki/synth/ollama.py`, `llmwiki/synth/agent_delegate.py`, `llmwiki/build.py`, `llmwiki/mcp/server.py`, `CLAUDE.md`.

The pending backend writes a durable prompt for a later foreground turn; it does not create a separate model context/frame. The build-time CLI is a separate process with selected input and stdout return; its internal model context is opaque. Files remain reloadable rather than being live window references. No target-managed foreground-context eviction or subagent frame lifecycle is established by these inspected routes. Subagent labels on source sessions describe recorded input provenance, not llm-wiki launching workers. SRC-1: `llmwiki/synth/agent_delegate.py`, `llmwiki/build.py`, `CLAUDE.md`.

Recovery is route-local. Conversion quarantines selected failures and saves state/counters; synthesis catches per-file exceptions, logs a summary and retains successful mtime entries; invalid synthesis-state shapes reset or drop invalid entries, permitting rework. Ollama retries configured transient failures but short-circuits connection refusal/DNS failures. Completion refuses absent/mismatched sentinels, then writes the body and best-effort deletes the prompt. Build clears its output tree before regeneration, so it is not atomic publication; failure can leave partial output. No cross-file transaction or automatic undo is established for the inspected write loops. SRC-1: `llmwiki/convert.py`, `llmwiki/synth/pipeline.py`, `llmwiki/synth/ollama.py`, `llmwiki/synth/agent_delegate.py`, `llmwiki/build.py`.

Added inspection within SRC-1, at the same pin, covers backend implementation bodies, prompt rendering, candidate transitions, pipeline orchestration, MCP control/read/query code and build-time Claude input/return. These extend initial boundary inspection as implementation and doctrine/design evidence only. Adapter-specific normalization, individual lint rules, all editor/deployment variants, self-learn maintenance instructions and real user corpora were not exhaustively traced here; this report does not establish their semantic guarantees, all change-admission routes, or deployed performance. Knowledge revision details remain for the memory analyst. Product code changes require external repository editing/release machinery; no inspected runtime path installs a successor codebase or updates model weights.

## Shared records

### Components

#### RT-CMP-ollama
Label: Ollama synthesis model

SRC-1: `llmwiki/synth/ollama.py`. Distributed-parametric model behind a configurable HTTP endpoint; numerical weights reside in the external service, not this repository. Default model tag is `llama3.1:8b`; exact weights are not pinned. The configured URL/tag may resolve to another model. No parameter-changing request is implemented in this adapter; service-side parameter changes and provider internals are uninspected. It returns a string consumed by [RT-RTE-backend-synthesis](#rt-rte-backend-synthesis).

> DEFAULT_MODEL = "llama3.1:8b"
> --- `llmwiki/synth/ollama.py`

#### RT-CMP-claude
Label: Build-time Claude model

SRC-1: `llmwiki/build.py`. Distributed-parametric component invoked through an external executable, with weights/provider state outside the checkout. The command specifies a dated model identifier, not an inspectable weight digest. No parameter update is requested; exact numerical version and endpoint reassignment are uninspected external contracts. Distinct from the foreground host agent, whose model identity and mutability are wholly supplied by its deployment.

> [claude_path, "-p", "-", "--model", "claude-haiku-4-5-20251001"],
> --- `llmwiki/build.py`

### Operative objects

#### RT-OBJ-source-page
Label: Source-page synthesis prompt

SRC-1: `llmwiki/synth/prompts/source_page.md`, `llmwiki/synth/pipeline.py`. Natural-language synthesis guidance with symbolic substitution slots; stored as package Markdown, replaceable by `wiki/prompts/source_page.md`. It requests summary, claims, quotes, connections, contradictions and a tag comment. The body interpretation is model-mediated; template selection/substitution is code-governed. This static guidance is not itself accumulated memory.

> if USER_PROMPT_OVERRIDE.is_file():
>         return USER_PROMPT_OVERRIDE.read_text(encoding="utf-8")
> --- `llmwiki/synth/pipeline.py`

#### RT-OBJ-pending-prompts
Label: Pending synthesis coordination files

SRC-1: `llmwiki/synth/agent_delegate.py`. UTF-8 Markdown files under `.llmwiki-pending-prompts/`, holding symbolic UUID/slug/project/date headers and a natural-language rendered prompt. A matching symbolic sentinel is stored in the wiki source page. The prompt is task material for later host interpretation; the sentinel controls completion association. These parts have different consumers: the agent reads prompt text; completion code checks UUID equality.

> if found_uid != uid:
>         raise ValueError(
>             f"uuid mismatch: page carries {found_uid}, caller passed {uid}"
>         )
> --- `llmwiki/synth/agent_delegate.py`

### Routes

#### RT-RTE-session-conversion
Label: Session conversion to raw Markdown

SRC-1: `llmwiki/cli.py`, `llmwiki/convert.py`. Endpoints: adapter-discovered files → raw Markdown and `.llmwiki-state.json`. Principal is the invoking user/host; converter owns next-file progression. Symbolic predicates select adapter, mtime, project, ignore, time and live-session eligibility. Normalization, redaction and message/tool-preview truncation precede physical writes. Markdown-copy input and normalized JSONL input share the raw write guard. Vault invocation redirects raw/state paths. Human initiation is not per-file approval; code admits selected renderings, with force as explicit bypass and quarantine/retry as recovery. No answer oracle or bounded improvement experiment is used; this is an open operational sync.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Integer status and conversion/filter/error counters printed to the caller; CLI may build/lint after success.
- Later read-back: Raw Markdown is loaded by synthesis, host ingest and reader build; conversion state selects future work.
- Delegated visibility: Adapter normalization sees selected native records; later models receive rendered material, not necessarily full original records.
- Selection predicate: Enabled/explicit adapters, changed mtimes, project/ignore/date/live filters; force resets prior state.
- Invalidation or expiry: Mtime equality suppresses repeat work; force reprocesses; raw guard can reject existing output.
- Activation or effect: File and state writes are wired; subsequent semantic effects are unobserved.
- Evidence limits: No private stores or run artifacts; individual adapter normalization and complete redaction coverage are not established.

> records = adapter.normalize_records(records)
>             records = filter_records(records, drop_types)
> --- `llmwiki/convert.py`

#### RT-RTE-host-ingest
Label: Foreground host ingest and query

SRC-1: `CLAUDE.md`, `.claude/commands/wiki-sync.md`, `.claude/skills/llmwiki-query/SKILL.md`. Endpoints: selected raw sources/current user question → host-generated wiki pages or cited chat answer. The foreground agent proposes and decides semantic changes under natural-language guidance; user permission is specifically requested for saving substantial query answers and for large ingest batches, not every page mutation. Host tool grants and human veto enforcement are external. Operating mode is open ingest/query; no expected-answer oracle is supplied. Ingest guidance requests both claims remain visible on contradiction. Recovery is manual re-editing; no transactional rollback is specified. Knowledge admission here is distinct from the optional candidate path below.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Requested progress/final summary or answer with wikilink citations.
- Later read-back: Index, overview, source/entity/concept pages and optionally saved answers enter later queries.
- Delegated visibility: Foreground host is instructed to read raw sources and selected wiki context; no internal worker delegation is required.
- Selection predicate: User source path/new-file list for ingest; model relevance judgment after index/overview and folder context for query.
- Invalidation or expiry: Ingest may revise pages and append contradiction sections; staleness handling is instruction-mediated, not a universal read exclusion.
- Activation or effect: Instructions afford page writes and context-based answers; actual compliance and behavioral dependence are unobserved.
- Evidence limits: Host implementation, permissions, model weights and context-window lifecycle are not supplied.

> 5. If the answer is substantial (3+ paragraphs), ask the user if they want it saved to `wiki/syntheses/<slug>.md`.
> --- `CLAUDE.md`

#### RT-RTE-backend-synthesis
Label: Backend source-page synthesis

SRC-1: `llmwiki/cli.py`, `llmwiki/synth/pipeline.py`, `llmwiki/synth/base.py`, `llmwiki/synth/ollama.py`. Endpoints: discovered raw page → backend body → source page/index/log/state. CLI resolves backend; pipeline serially owns next-file dispatch. Dummy is deterministic text generation; Ollama interprets the template through [RT-CMP-ollama](#rt-cmp-ollama); agent mode hands off through [RT-RTE-agent-completion](#rt-rte-agent-completion). Code admits returned text after tag extraction/merge and metadata wrapping, without per-content human approval or correctness oracle. Backend can fail; pipeline skips individual errors. Force can replace prior pages, preserving existing tags when parse/read succeeds, not preserving the prior body. Prompt override supplies user-authored guidance, persisted independently of generated pages. Open operational synthesis, not a scored successor experiment.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts, errors and backend name; CLI returns nonzero for reported errors.
- Later read-back: Wiki files become query/host context; mtime state governs later synthesis selection.
- Delegated visibility: Ollama receives metadata plus first 8,000 raw-body characters, not the complete corpus or existing wiki pages.
- Selection predicate: Raw discovery and absent/older synthesis-state mtime, or force; availability checked before processing.
- Invalidation or expiry: Raw mtime/force control regeneration; prompt/model changes alone are not the selection predicate.
- Activation or effect: Source-page write/index rebuild are implemented; semantics and benefit are unobserved.
- Evidence limits: Placeholder and dummy successes are not evidence of model reasoning; provider internals and service execution are unavailable.

> name = (synth_cfg.get("backend") or "dummy").strip().lower()
> --- `llmwiki/synth/pipeline.py`

#### RT-RTE-agent-completion
Label: Deferred agent synthesis completion

SRC-1: `llmwiki/synth/agent_delegate.py`, `.claude/commands/wiki-sync.md`, `llmwiki/synth/cli_helpers.py`. Endpoints: raw/template → durable UUID prompt and placeholder → later foreground-generated body → sentinel-checked replacement. Runtime environment flags only heuristically establish backend availability, not permissions or a live worker. The backend never invokes the agent. The host agent proposes body text; completion code admits any supplied string after target/sentinel checks. User or caller can decline/delay completion; no content correctness veto or answer oracle is implemented here. Guidance persists in pending prompt until completion cleanup. It is an open handoff, serial by procedure, not a controlled experiment. UUID reuse searches pending headers by slug; project/date are not part of that lookup. Replacement preserves frontmatter but does not implement its docstring's claimed appended-body preservation: `new_body` is written directly.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Initially placeholder text; later completion writes supplied body and returns through CLI helper.
- Later read-back: Later host turn reads pending prompt; later queries read completed source page.
- Delegated visibility: Current foreground host receives rendered prompt, truncated body and metadata; completion code receives body string/target/UUID.
- Selection predicate: Agent availability heuristic; existing prompt selected by slug; completion requires matching page UUID.
- Invalidation or expiry: Prompt deleted best effort after write; no automatic expiry; sentinel prevents completing an already nonsentinel page.
- Activation or effect: Prompt/placeholder and completion writes are wired; actual later turn and synthesis are unobserved.
- Evidence limits: No observed completion, cross-project collision outcome or host compliance; vault prompt storage remains rooted in backend default rather than proven vault-isolated storage.

> new_body = synthesized_body.lstrip("\n")
>     target_page.write_text(frontmatter + new_body, encoding="utf-8")
> --- `llmwiki/synth/agent_delegate.py`

#### RT-RTE-mcp-access
Label: MCP query and guarded command surface

SRC-1: `llmwiki/mcp/server.py`, `llmwiki/cli.py`. Endpoints: host tool request → lexical ranked snippets/full allowed page/export text or sync child output. Server code owns ranking and tool dispatch; caller owns question/path/flags. Query is not an LLM answer generator: body/title token scores select pages, returning up to requested count, 400-character snippets and 1,000-character overview prefix; index prefix is a no-match fallback. Read-page containment/allowlist is a separate endpoint. Sync's proposed dry-run/confirmation policy is symbolic and caller-set, not verified human consent. Default `--dry-run` is rejected by the shipped sync parser; live confirmed calls omit it. Generic child-output success wrapping is not child success. No answer oracle is involved.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: MCP text content, including snippets, page contents, exports or child stdout/stderr; not a guaranteed correct natural-language answer.
- Later read-back: Query/read endpoints reload wiki files; confirmed sync can produce raw/state files through the CLI.
- Delegated visibility: Host receives selected snippets/full requested content; sync subprocess inherits process-level filesystem/environment access.
- Selection predicate: Query title/body lexical scores and scan budgets; page-path containment/allowlist; caller flags for sync.
- Invalidation or expiry: Files reread per call; no query-result persistence here; scan budgets may omit material without semantic invalidation.
- Activation or effect: Tool-result delivery is implemented; host use of results is unobserved. Default sync path affords an argument error, not preview conversion.
- Evidence limits: No MCP session/host grants/deployed isolation supplied; endpoint-specific guards are not universal host-tool policy.

> if dry_run:
>         cmd.append("--dry-run")
> --- `llmwiki/mcp/server.py`

#### RT-RTE-reader-build
Label: Reader publication and optional overview generation

SRC-1: `llmwiki/build.py`, `llmwiki/pipeline.py`. Endpoints: raw files/project metadata → regenerated reader/search/export artifacts, with optional metadata-only Claude prose. Builder owns deterministic progression; optional model call uses [RT-CMP-claude](#rt-cmp-claude). The `all` orchestration runs build, graph, export and lint, optionally synthesis first; default continuation and strict/fail-fast flags govern error propagation, not semantic admission. Build's project-stub creation is opt-in, while output regeneration is destructive. Model stdout is accepted if process succeeds/nonempty, not validated against an expected answer. The prompt asks for a brief third-person account; only generated site presentation persists from this optional call, not an installed source-page prompt or model update. Human controls invocation/configuration, not per-paragraph approval. Recovery is rerun/manual restoration, not transactional rollback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Build return code/logs and generated files; optional Claude failures degrade to no model overview.
- Later read-back: Readers and export/MCP consumers load generated artifacts; wiki project stubs can be retained when seeding requested.
- Delegated visibility: Claude subprocess receives grouped metadata brief with safe slugs and 32,000-byte cap, not full session bodies.
- Selection predicate: Raw source discovery and project grouping; `synthesize` opt-in; first eight session slugs per project in brief.
- Invalidation or expiry: Output directory cleared before rebuilding; no atomic swap; model prose regenerated only when requested.
- Activation or effect: Publication file writes and subprocess request are wired; reader utility and model correctness unobserved.
- Evidence limits: No deployment, process execution, publication success or performance result supplied; this is not evidence that full semantic wiki traversal drives the reader.

> shutil.copytree(RAW_SESSIONS, sources_out)
> --- `llmwiki/build.py`

#### RT-RTE-candidate-admission
Label: Optional candidate promotion and merge

SRC-1: `llmwiki/candidates.py`, `llmwiki/cli.py`. Endpoints: existing `wiki/candidates/<kind>/<slug>.md` → promoted page, merged target or archived candidate. Caller selects action; code implements it. Candidate creation/proposal identity is unresolved by these transition functions, and CLI access does not authenticate a human reviewer. Promotion changes status and writes target then deletes candidate; merge appends body then archives; discard archives with reason. Promotion can overwrite a same-named target. Caller can reject by discard or abstention; no model/answer oracle ranks the content. Operating mode is explicit operational selection, not a curriculum. Guidance is the candidate status/action contract; retained products are text/status and archive/reason material. Archive supports historical recovery, not automatic undo of overwritten target text. This optional route does not mediate direct ingest or pipeline writes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Destination path or missing-file error through CLI.
- Later read-back: Promoted/merged content is available to ordinary wiki consumers; archives/reasons remain on disk.
- Delegated visibility: Transition functions see candidate and target text; no evaluator delegation is implemented in them.
- Selection predicate: Caller-supplied slug/kind/action/merge target, with lookup and target-existence checks.
- Invalidation or expiry: Promotion deletes candidate; merge/discard archives it; stale-listing is not automatic rejection.
- Activation or effect: File/status transitions wired; reviewed status does not establish substantive review or later answer dependence.
- Evidence limits: No candidate provenance, exercised review or improvement outcome is supplied.

> text = _rewrite_status(text, old="candidate", new="reviewed")
>     target.write_text(text, encoding="utf-8")
>     candidate.unlink()
> --- `llmwiki/candidates.py`

### Claims

#### RT-CLM-history-compilation
Label: Session history compilation claim

SRC-1: `CLAUDE.md`. Claimed work is structured, interlinked knowledge compilation, supported architecturally by the converter plus host instructions and synthesis backends, not by supplied successful execution.

> You are maintaining an **LLM Wiki** (per [Karpathy's spec](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)) that compiles the user's Claude Code session history into a structured, interlinked markdown knowledge base.
> --- `CLAUDE.md`

#### RT-CLM-append-preservation
Label: Completion hand-edit preservation claim

SRC-1: `llmwiki/synth/agent_delegate.py`. The docstring claims appended lines survive, but implementation constructs replacement solely from preserved frontmatter and supplied synthesized body. This comparison limits a recovery guarantee; it is not an observed data-loss report.

> Preserves the frontmatter + appends any lines the agent wrote
>     after the sentinel (so hand edits survive).
> --- `llmwiki/synth/agent_delegate.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-source-guidance
Label: Source-page prompt authority

Consumer: Ollama synthesis model or later foreground host. Channel: selected template rendered with source metadata/body, delivered by HTTP or durable pending prompt. Force: natural-language instruction mediated by model interpretation, not a programmatic truth validator. Horizon: each synthesis invocation; user override remains available across sessions. SRC-1: `llmwiki/synth/pipeline.py`, `llmwiki/synth/ollama.py`, `llmwiki/synth/agent_delegate.py`, `llmwiki/synth/prompts/source_page.md`. See [RT-OBJ-source-page](#rt-obj-source-page) and [RT-RTE-backend-synthesis](#rt-rte-backend-synthesis). Editing the override is a direct behavior-guidance admission affordance, not evidence of autonomous prompt improvement or activation.

#### RT-BAP-wiki-context
Label: Retained wiki answer context

Consumer: foreground query agent after host Read or MCP response. Channel: index/overview, selected page text and optional folder-context guidance. Force: epistemic context and relevance guidance, not a universal higher-priority runtime policy. Horizon: later questions/sessions while files remain available. SRC-1: `CLAUDE.md`, `.claude/skills/llmwiki-query/SKILL.md`, `llmwiki/mcp/server.py`. See [RT-RTE-host-ingest](#rt-rte-host-ingest) and [RT-RTE-mcp-access](#rt-rte-mcp-access). Implemented/requested delivery supports the authority path's availability; it does not establish model compliance, improved capacity or exercised self-improvement.

## Annotations

none
