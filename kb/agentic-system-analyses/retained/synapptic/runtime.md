---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Synapptic runtime baseline: transcript extraction, profile admission, publication, benchmark feedback and optional relay at the frozen revision."
run-id: AAS-2026-10-15-synapptic-9dce97c66546-01
reviewed-boundary: bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f
---

# Synapptic runtime report

## Runtime account

### Work and evidence basis

Synapptic performs transcript-to-instruction processing, not the coding assistant's enclosing tool loop. The ordinary operator entry is `synapptic ingest`: discover sessions, filter their text, ask a configured model for observations, route and merge them, synthesize narratives, and publish saved narratives. Code owns progression between stages; models propose observations and narrative wording. The returned artifact is a set of local files plus CLI progress messages, not a completed coding task. See [RT-RTE-ingest-profile](#rt-rte-ingest-profile) and [RT-RTE-publish-archetypes](#rt-rte-publish-archetypes). SRC-1, `src/synapptic/cli.py`, `src/synapptic/extract.py`, `src/synapptic/integrate.py`.

All findings below are implementation or first-party doctrine at the boundary's pin. No target code, examples, tests or model calls were executed. No supplied observed-run or causal-experiment evidence establishes invocation success, activation in an external assistant, privacy completeness or improvement. Additional inspection under SRC-1 covered the provider payloads/retries, filter, scrubber, custom-pattern loader, profile merge implementation, state write methods, all output writers, hook installation, both benchmark comparison paths, relay forwarding/app/routes and session-tracker return contract. Remaining relay browser/index/store internals and evaluator details are not exhaustively characterized here; their existence does not imply downstream profile admission or reliable execution.

### Ordinary invocation and control allocation

The user starts `ingest` as the local OS principal. Session IDs index discovered transcript files; project slugs identify per-project stores; a separate global profile supplies cross-project context. Unprocessed means no observation JSON filename for that session. The driver deduplicates IDs, optionally restricts project, sorts by file size descending, and counts extracted sessions against the requested limit. Short or empty sessions receive empty observation files. The loaded queue is not the selector in this driver, and the queue is cleared after extraction. SRC-1, `src/synapptic/cli.py`, `src/synapptic/state.py`.

Filtering retains user text and assistant text, not tool-use inputs, tool-result bodies or thinking blocks. Code boosts correction/preference/reaction turns and short replies after long assistant answers. Under budget pressure it prefers boosted turns with preceding assistant context, then recent remaining turns. If priority content alone exceeds the budget it truncates those turns proportionally. This is a fresh extraction context assembled from an external transcript, not compaction of the live host window. The original transcript remains outside that model invocation; no model-driven reload tool is supplied. The budget is a character approximation, not a strict tokenizer bound: proportional shares have a minimum size, and formatting/profile/template overhead is added later. SRC-1, `src/synapptic/filter.py`, `src/synapptic/extract.py`.

The extraction prompt combines a user-overridable pattern, active dimension descriptions, scrubbed transcript text and selected existing observations. Existing-profile context includes weight-at-least-0.7 items, capped at eight per dimension. The CLI only supplies its combined global/project context when the global profile has dimensions, so a project-only profile does not by itself activate that context path. The model returns text. Code accepts a JSON array, drops non-dicts, unknown dimensions and missing observations, defaults confidence and attaches session/time metadata. It does not verify that a proposed observation follows from its purported evidence. Subsequent merge is symbolic code using textual similarity, confidence blending, decay, source IDs and cross-project promotion. Detailed memory-revision assessment belongs to the memory member; these are the runtime's admission/control boundaries. SRC-1, `src/synapptic/extract.py`, `src/synapptic/profile.py`, `src/synapptic/cli.py`.

Synthesis filters profile entries and requests a Markdown user archetype, imperative guards and known weaknesses. Its guard-evidence requirement is model guidance, not an evidence-checking gate. The driver saves any truthy narrative after fence stripping. Integration then reloads saved global/project narratives, concatenates them and invokes configured platform writers for discovered destinations. The host, not Synapptic, controls whether these files enter future model context and with what precedence. See [RT-BAP-archetype-host](#rt-bap-archetype-host). SRC-1, `src/synapptic/synthesize.py`, `src/synapptic/integrate.py`, `src/synapptic/outputs.py`.

### Four forcing cases and alternate paths

1. **Detached maintenance is not equivalent to full ingest.** Installation registers a SessionEnd shell hook. For selected explicit-exit reasons it starts detached `extract -s`, `merge`, then project/global `synthesize`; a PID-file check skips a session when another hook is active. The shell commands are sequential without failure chaining. Standalone synthesis saves narratives but does not integrate them. Thus this automatic path can update internal state without refreshing external instruction files. See [RT-RTE-session-hook](#rt-rte-session-hook). SRC-1, `src/synapptic/cli.py`, `src/synapptic/bundle/hooks/synapptic-session-end.sh`.

2. **A failed extraction can become a processed session.** Provider failure or invalid extraction JSON yields an empty list; the ingest driver still saves observations. Processed selection tests file existence, not extraction success. A later ordinary ingest therefore skips that ID. Explicit `extract -s` can select it again, but ordinary automatic retry is not assured. Profile/narrative/output writes are not one transaction. In addition, integration appends five-element result tuples while ingest unpacks three elements after publication. With at least one updated destination this source path reaches an unpacking exception after writes, rather than reliably reaching `Done.` This is an inspected defect, not an observed failure trace. SRC-1, `src/synapptic/extract.py`, `src/synapptic/state.py`, `src/synapptic/cli.py`, `src/synapptic/integrate.py`.

3. **Model-specific guard filtering is computed but not applied to publication.** Integration resolves a target model and computes full/filtered entry counts, yet combines already-saved narratives without regenerating or removing their text. Standalone `synthesize --target-model` really supplies the model-specific filter to synthesis; ordinary ingest does not. A computed excluded count therefore does not prove the published narrative omitted those guards. Benchmark feedback has separate automatic per-model verdict writes and human-confirmed global exclusion flags. See [RT-RTE-benchmark-feedback](#rt-rte-benchmark-feedback) and [RT-CLM-target-filtering](#rt-clm-target-filtering). SRC-1, `src/synapptic/integrate.py`, `src/synapptic/synthesize.py`, `src/synapptic/cli.py`.

4. **Relay requests are not constrained like internal model calls.** Internal Claude subprocess calls disable tools; direct provider payloads request text without tool definitions. By contrast `synapptic run` starts a real external tool with inherited OS environment and relay URL overrides, forwarding arbitrary host request bodies, including tool definitions. The host retains tool execution and permission decisions. Anthropic and OpenAI relay handlers also differ: the tracker returns `(session_id, is_new)`, unpacked by Anthropic but assigned as one session ID by OpenAI before storage. That mismatch prevents assuming equivalent session persistence or successful OpenAI forwarding. Neither defect was executed. See [RT-RTE-relay-forwarding](#rt-rte-relay-forwarding). SRC-1, `src/synapptic/providers.py`, `src/synapptic/cli.py`, `src/synapptic/relay/routers/anthropic.py`, `src/synapptic/relay/routers/openai.py`, `src/synapptic/relay/sessions.py`.

### Guarantees, grants and recovery

**Internal inference has a narrow tool grant, not a system sandbox.** The adapter owner enforces an empty tool list at the Claude invocation and supplies no tools in inspected Anthropic/OpenAI/Ollama inference payloads. Guarantee strength: protocol; implementation conclusion status: wired; operation conclusion status: uninspected. This covers extraction, synthesis and evaluator calls through that adapter, including Claude session resume. It requires the external CLI/provider to honor its contract. It does not cover the separate relay, launched host tools, installed shell hook or local Python file writes. Synapptic itself runs with its user's file/subprocess/network authority; no deployed isolation envelope is established by these sources. SRC-1, `src/synapptic/providers.py`, `src/synapptic/cli.py`.

> cmd = ["claude", "-p", "--model", model, "--output-format", "json", "--tools", ""]
> --- `src/synapptic/providers.py`

**Injection resistance and scrubbing are best effort.** Extraction/synthesis label their inputs as reference data. The default extraction path applies regex/entropy scrubbing to transcript text, but the inspected observation writer serializes model output without a scrubber call. Existing profile context, synthesized narratives and raw relay request bodies do not pass through that transcript scrubber in their inspected routes. Thus scrubbing's own module-level statement that it precedes persistence is broader than the traced enforcement. Guarantee owner: prompt/filter authors; enforcement: transcript conversion and model instructions; guarantee strength: best effort; implementation conclusion status: wired; operation conclusion status: uninspected. Required external contract: the model treats delimited data as data. Neither syntax acceptance nor instruction wording establishes factual grounding or confidential-data exclusion. SRC-1, `src/synapptic/filter.py`, `src/synapptic/scrub.py`, `src/synapptic/extract.py`, `src/synapptic/synthesize.py`, `src/synapptic/state.py`, `src/synapptic/relay/forwarder.py`.

> text = scrub_text(turn.text) if scrub else turn.text
> --- `src/synapptic/filter.py`

> with open(obs_path, "w") as f:
>         json.dump(payload, f, indent=2)
> --- `src/synapptic/state.py`

**Atomic replacement is per file.** State/output writer owners flush, fsync and rename temporary files for profiles, narratives and published outputs. Guarantee strength: protocol; implementation conclusion status: wired; operation conclusion status: uninspected. This requires local filesystem rename semantics; it is not a cross-stage transaction, concurrent-writer lock or rollback guarantee. Observation JSON uses ordinary writes. Profile saves also copy history snapshots. CLI rollback copies a previous global profile, not project profiles, narratives or already-published outputs. Failures leave potentially mixed stage versions. SRC-1, `src/synapptic/state.py`, `src/synapptic/outputs.py`, `src/synapptic/cli.py`.

> f.flush()
>             os.fsync(f.fileno())
>         tmp.rename(path)
> --- `src/synapptic/outputs.py`

**Provider recovery is bounded.** `call_llm` applies estimated rate limits and retries returned failures carrying HTTP 429/503, aborting daily limits; adapters impose 300-second call timeouts. These are best-effort recovery rules, not successful-result guarantees. CLI-subprocess errors and bad extraction JSON are not equivalent to retryable HTTP failures. Relay forwarding has its own httpx timeouts and streaming callbacks, not `call_llm` recovery. Console metrics, Ollama token logs, saved benchmark results and relay SQLite/dashboard records provide observability interfaces, not evidence that a particular run succeeded. SRC-1, `src/synapptic/providers.py`, `src/synapptic/relay/app.py`, `src/synapptic/relay/routers/anthropic.py`, `src/synapptic/benchmark.py`.

## Shared records

### Components

#### RT-CMP-call-llm
Label: Configured inference services

Source-native identity: `call_llm` and its provider/model configuration. Representational form: distributed-parametric inference behind symbolic request adapters; substrate: external model service or Claude CLI, with local configuration supplying endpoint/model names. The extraction and synthesis calls use the pipeline configuration; benchmark generation/responses and judge calls may use different configurations and therefore different services/weights. For each role, parameters are not changed by the inspected client requests, exact weights/service version are not pinned, and mutable model names/endpoints can resolve to a different implementation. Provider-internal training, state and parameter mutability remain uninspected. Claude benchmark resume additionally introduces retained session context without establishing weight updates. SRC-1, `src/synapptic/providers.py`, `src/synapptic/benchmark.py`.

> model = config.get("model") or PROVIDERS.get(provider, {}).get("default_model", "sonnet")
> --- `src/synapptic/providers.py`

### Operative objects

#### RT-OBJ-pattern-prompt
Label: Extraction pattern prompt

Source-native identity: named `patterns/<name>/prompt.md`. Natural-language extraction guidance with symbolic format placeholders; stored in a user pattern directory or package resources. It directs failure diagnosis and rule proposals. User files take precedence over built-ins; absent named templates fall back to default in extraction. Changing a pattern changes later proposals without an internal review or benchmark requirement. This is a prompt-content extension point, not evidence that arbitrary extension code executes. SRC-1, `src/synapptic/patterns.py`, `src/synapptic/extract.py`, `src/synapptic/bundle/patterns/default/prompt.md`.

> user_path = PATTERNS_DIR / name / "prompt.md"
>     if user_path.exists():
>         return user_path.read_text()
> --- `src/synapptic/patterns.py`

### Routes

#### RT-RTE-ingest-profile
Label: Ingest to weighted profiles

Endpoints/progression: local user invokes `ingest`; CLI discovers and filters transcripts, model proposes JSON observations, code validates a limited shape, stores project-tagged observations, routes global/project entries, merges and promotes. Code owns next steps; no separate human per-observation approval. Model sees selected conversation text and optionally a high-weight existing-profile summary, not a complete execution record. Executor effects are local observation/profile/history writes plus inference requests. Symbolic checks admit candidate text but do not independently judge its truth. Guidance is [RT-OBJ-pattern-prompt](#rt-obj-pattern-prompt); model substrate is [RT-CMP-call-llm](#rt-cmp-call-llm). SRC-1, `src/synapptic/cli.py`, `src/synapptic/extract.py`, `src/synapptic/profile.py`, `src/synapptic/state.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Progress/count messages and durable observation/profile files; extraction itself returns a list, including empty on provider/parse failure.
- Later read-back: Subsequent extraction reads high-weight profile text; synthesis reads profiles; separate merge reads saved observations.
- Delegated visibility: The configured extraction model receives filtered/scrubbed text and selected profile context; it receives no Synapptic tool grant for additional evidence.
- Selection predicate: Previously unprocessed discovered IDs, optional project, descending transcript size, minimum lines, extraction limit; merge routes by dimension and matches by text similarity.
- Invalidation or expiry: Empty observation files still mark processed; merge decay/pruning changes retained weights/content; explicit session extraction can bypass ordinary processed selection.
- Activation or effect: Wired profile/context changes; actual changed model decisions from retained content remain unobserved.
- Evidence limits: No supplied extraction/profile history or run verifies correctness, privacy, recovery or behavioral activation.

Admission: the model proposes observation wording/confidence; code accepts recognized dimensions and nonempty observations, then deterministic merge rules admit profile updates. The user can alter source/pattern/configuration or stop processing, but starting ingest is not approval of each claim. Recovery is explicit re-extraction or profile history restoration, not an integrated transaction rollback. Operating mode: open transcript analysis, not an answer-key curriculum. Answer oracle: none established; a model-supplied evidence field is not a reference outcome.

> if not raw_output:
>         return []
> --- `src/synapptic/extract.py`

> ids.update(p.stem for p in obs_dir.glob("*.json"))
> --- `src/synapptic/state.py`

#### RT-RTE-publish-archetypes
Label: Synthesis and output integration

Endpoints/progression: CLI filters weighted profiles, calls the narrative model, saves nonempty output, then ingest calls integration to combine saved global/project text and dispatch platform writers. Code selects qualifying entries and destinations; model determines prose and imperatives. State is profile YAML, saved Markdown and output configuration. Executor runs under the local user's authority. External assistant loading is a separate boundary. SRC-1, `src/synapptic/synthesize.py`, `src/synapptic/integrate.py`, `src/synapptic/outputs.py`, `src/synapptic/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Narrative string/file, then writer results; ingest can fail unpacking integration results after writes.
- Later read-back: Integration reloads archetypes; benchmarks reload profiles/archetypes; external host may read published assistant-specific files.
- Delegated visibility: Synthesis model receives a filtered YAML profile; external hosts receive combined narrative text in their instruction/memory channel.
- Selection predicate: Synthesis thresholds differ for guards/AI failures versus other dimensions; excluded flags and optional target-model verdicts filter source entries. Integration selects configured targets and discovered existing project destinations.
- Invalidation or expiry: New saves replace narrative/output content; failed synthesis can leave an older narrative available for integration; no automatic freshness check links a saved narrative to its current profile.
- Activation or effect: Local publication is wired; host instruction loading, compliance and benefit are unobserved.
- Evidence limits: Target-model filtering counts do not alter combined saved text; host precedence/reading contract is external; no publication trace was supplied.

Admission: model proposes prose under the shipped synthesis prompt; code accepts truthy output without checking headings, word counts or guard grounding. User selects configuration or an explicit synthesis target; no per-narrative approval is required. Rollback does not automatically restore all published variants. Operating mode: open synthesis; answer oracle: none. The guidance asks for failure-derived preventive imperatives and rationales, retained as Markdown for later host consumption.

> narrative = call_llm(prompt, config=config)
>     if not narrative:
>         return None
> --- `src/synapptic/synthesize.py`

> combined = combine_archetypes(global_archetype, project_archetype, slug)
> --- `src/synapptic/integrate.py`

Theory account: guards are localized natural-language prescriptions with proposed failure explanations; the source requests them, without supplied generated guards proving their content. theory-builder conditions 1–4: condition 1 implementation conclusion status: afforded (whole guards/narratives can express inspectable guidance); condition 2 implementation conclusion status: afforded (later models receive that guidance, but content-dependent decisions are not demonstrated); condition 3 implementation conclusion status: uninspected (the extraction request for failure diagnosis does not establish claim/result/blame/revision content); condition 4 implementation conclusion status: afforded (profiles feed future extraction/synthesis, without evidence that a criticism result drives a next round). These are separate architectural limits, not a demonstrated theory-builder classification. Addressability: profile observations and full narrative text are separately editable; narrative rewording need not preserve a one-to-one guard identity. Persistence: files span sessions until replaced; later external use is unobserved. learning: future improvement is not established. Reflection: the wider host-plus-Synapptic path can represent host failures and deliver preventive instructions back; neither represented-host behavior changes nor representation-mediated activation is supplied. Autonomous theory builder and reflective theory builder: not established by the prompt and storage loop alone. Self-improvement, if assessed over the host-plus-Synapptic boundary toward fewer recurrent coding failures, remains dispositional: trace-to-update wiring exists but later live behavioral dependence and improvement are unestablished; Synapptic alone does not own the external host behavior.

#### RT-RTE-session-hook
Label: SessionEnd maintenance driver

Endpoints/progression: external host emits session metadata to installed shell hook; hook notifies local relay, checks reason/PID, detaches extraction, merge and synthesis. User installation authorizes machinery registration; host event initiates later work. Shell owns sequencing, CLI/model stages own content changes. State crosses processes through files; PID/log paths coordinate best effort, not a durable work queue. SRC-1, `src/synapptic/bundle/hooks/synapptic-session-end.sh`, `src/synapptic/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Hook exits success after detaching or skipping; progress/errors go to a temporary log rather than host feedback.
- Later read-back: Separate merge reloads observations; synthesis reloads profiles; future extraction reloads profiles. External output integration is not invoked here.
- Delegated visibility: Background CLI receives session ID/project; providers receive extraction/synthesis prompts, not the live host tool context.
- Selection predicate: Nonempty session ID, explicit exit/clear/logout reasons, no apparently live previous-hook PID; extract explicitly selects the session.
- Invalidation or expiry: PID file removed on normal background completion; skipped concurrent events have no retry scheduling in this script.
- Activation or effect: Automatic internal state updates are wired; refreshed external instruction files are not produced by this hook sequence.
- Evidence limits: Host hook delivery, detached-process completion and race behavior were not observed.

Admission: installer copies a skill and executable shell hook and edits settings registration. The human chooses installation, code registers it, and host execution remains an external contract. Later content is model/software-admitted as in [RT-RTE-ingest-profile](#rt-rte-ingest-profile), not individually user-approved. Recovery is removal/uninstallation or rerunning CLI stages; commands proceed without `&&`, so synthesis is not conditional on successful extraction/merge. Operating mode: event-triggered maintenance; answer oracle: inapplicable — this driver supplies no independent content evaluation.

> synapptic extract -s '"$SESSION_ID"' >> '"$LOGFILE"' 2>&1
>     synapptic merge >> '"$LOGFILE"' 2>&1
>     synapptic synthesize -p '"$PROJECT"' >> '"$LOGFILE"' 2>&1
> --- `src/synapptic/bundle/hooks/synapptic-session-end.sh`

#### RT-RTE-benchmark-feedback
Label: Behavioral benchmark feedback

Endpoints/progression: user invokes benchmark; models generate scenarios, produce conditioned/unconditioned responses and judge rule compliance; code classifies comparisons and saves results/model verdicts; human may confirm broader guard exclusions. State includes selected guards, cached cases, response sessions, result JSON and profile verdict/exclusion fields. A separate judge configuration is supported, not required. SRC-1, `src/synapptic/benchmark.py`, `src/synapptic/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Scores, classifications, calibration controls, token summaries and saved benchmark results; empty results return without feedback writes.
- Later read-back: Model verdicts affect explicit target-model narrative filtering; exclusion flags affect later synthesis; cases can be reused from cache.
- Delegated visibility: Response model receives scenario and selected profile treatment; judge receives rule/response, not external task outcomes. Batched judges receive only the first 300 response characters per pair.
- Selection predicate: Selected profile guards/test cases, seed/cache/refresh options, per-guard or batched mode; verdict matching uses text prefix/similarity.
- Invalidation or expiry: Refresh/cache controls change scenarios; later verdict writes overwrite per-model classification; include-guards command removes selected exclusion flags.
- Activation or effect: Feedback writes can alter later synthesis eligibility; integrated outputs do not automatically enact model-specific verdict filtering, and actual behavior improvement is unobserved.
- Evidence limits: No benchmark execution artifact; generated scenarios and model judgments are not independent answer oracles or real coding outcomes.

Operating modes differ materially. Per-guard mode removes the matching guard from the full archetype for WITHOUT, or appends it for WITH if not found; seeded order balancing reduces order bias, and Claude can reuse two separate condition sessions across cases. Batched mode contrasts full archetype versus no archetype across scenario chunks. Its per-rule scores cannot identify an individual guard's effect separately from the full-profile treatment. Same-model generation/judging, similarity-based removal and retained condition-session context constrain causal attribution even in per-guard mode. Model judgment supplies compliance labels; fixed comply/violate controls calibrate the judge but are not an external answer oracle for ordinary generated tests.

Admission: code automatically records non-unclear/non-untestable per-model verdicts before confirmation. A human can veto the offered global backfire/redundant exclusions, but not those already-recorded verdicts through that prompt. Guidance under evaluation is the profile's guard text; surviving text, verdicts and exclusion reasons persist. Recovery includes guard re-inclusion and profile history; output regeneration/publication remains separate. The route selects rule reliance by scores, not by a demonstrated content-directed criticism locating blame in theory, test, data or auxiliary assumptions. Thus it must not be equated with a completed theory-criticism/revision cycle.

> raw_without = call_llm(without_prompt, config=config, temperature=temperature)
> --- `src/synapptic/benchmark.py`

> verdicts_saved = record_model_verdicts(results, project_slug=project)
> --- `src/synapptic/cli.py`

#### RT-RTE-relay-forwarding
Label: Optional tool relay

Endpoints/progression: `run` starts/reuses uvicorn, waits for dashboard readiness and launches an external executable with provider URL overrides. FastAPI handlers parse metadata, assign session identity, forward bytes via httpx and log/store usage; SSE callbacks record completion. The host owns planning, tools and subsequent requests. Dashboard/browser consume local metrics or transcript material; this route establishes observability, not a relay-to-profile update chain. SRC-1, `src/synapptic/cli.py`, `src/synapptic/relay/app.py`, `src/synapptic/relay/forwarder.py`, `src/synapptic/relay/routers/anthropic.py`, `src/synapptic/relay/routers/openai.py`, `src/synapptic/relay/sessions.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Upstream response bytes or SSE stream; CLI waits for host exit and prints daily database totals rather than an isolated proven per-launch total.
- Later read-back: SQLite metrics/sessions support restart restoration and UI queries; this does not establish automatic profile learning from relay records.
- Delegated visibility: Upstream receives the host's raw body and cleaned headers; arbitrary host tool definitions are not removed. External tool retains inherited environment and local execution powers.
- Selection predicate: Explicit run/relay use, route-specific provider and request stream flag; tracker groups by extracted tool identity rather than supplied IP/system hash.
- Invalidation or expiry: Tracker expires inactive sessions and reloads recent records; launcher leaves relay running for other sessions; no inferred semantic session isolation.
- Activation or effect: Forwarding/metrics wiring is present; successful deployment and equivalent Anthropic/OpenAI behavior are unobserved, with an inspected OpenAI session-return mismatch.
- Evidence limits: No service traffic or deployment trace; upstream and host tool security contracts remain external.

The current internal-inference tool restriction is not applied here. Header filtering removes hop-by-hop and selected network-identifying headers, not prompt content, tool schemas or provider authorization. Default local binding is configuration, not a demonstrated authentication/isolation envelope. The launcher permits registry tools or a fallback executable and passes extra arguments, so host permissions cannot be inferred from a Synapptic provider call. This is delegated host execution, not internal sub-agent planning.

> response = await client.post(
>         url,
>         content=body,
>         headers=cleaned,
>     )
> --- `src/synapptic/relay/forwarder.py`

> session_id = tracker.get_or_create(source_ip, user_agent, system_hash)
> --- `src/synapptic/relay/routers/openai.py`

> return session_id, True
> --- `src/synapptic/relay/sessions.py`

### Claims

#### RT-CLM-target-filtering
Label: Model-specific publication filtering claim

Claimed operation: integration's module documentation says target-specific redundant/backfire guards are excluded from written archetypes. Inspected implementation resolves a model and counts filtered entries, but sends combined saved narratives unchanged to writers. This supports an implementation qualification, not an effectiveness claim. Explicit target-model synthesis is a different path that does filter profile inputs. SRC-1, `src/synapptic/integrate.py`, `src/synapptic/synthesize.py`.

> Each target maps to a model family — guards marked redundant/backfire for
> that family are excluded from the archetype written to that target.
> --- `src/synapptic/integrate.py`

> write_claude_code(combined, memory_dir)
>                     updated.append((slug, "claude-code", memory_dir, target_model, excluded_count))
> --- `src/synapptic/integrate.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-archetype-host
Label: Published narrative to host behavior

Consumer: external coding assistant. Channel: Claude memory/user-archetype reference, Cursor always-apply rule file, Copilot/Gemini/Codex marked instruction sections, or other target-specific whole-file conventions/rules outputs. Force: natural-language profile and imperative guard guidance; no Synapptic runtime enforcement of host compliance. Horizon: future project sessions until overwritten/removed, conditional on the host reading the file. Claude writer updates an existing MEMORY.md reference but does not create a missing index. Integration requires discovered project destinations; a configured target alone does not establish delivery. SRC-1, `src/synapptic/outputs.py`, `src/synapptic/integrate.py`, `src/synapptic/synthesize.py`.

> index_path = memory_dir / "MEMORY.md"
>     if index_path.exists():
>         content = index_path.read_text()
> --- `src/synapptic/outputs.py`

## Annotations

none
