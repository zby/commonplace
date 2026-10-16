---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Prime Agent's local/global harness entries, selected digest, trajectory refinement, context summaries and revivable Python namespace."
run-id: AAS-2026-10-14-prime-agent-8ec59ae12476-01
source-identity: "https://github.com/PrimeIntellect-ai/prime-agent"
reviewed-boundary: "33da15a2c15c4e903c372f69ae8e1156d77d53da"
---

# Prime Agent memory report

## Boundary and evidence

The memory boundary is the shipped runtime's retained harness, session context and namespace, plus skill admission and delegated-context controls. It includes all five harness kinds, not only entries called `memory`. SRC-1 is the repository at the supplied commit; HEAD was rechecked against that pin. All findings below use implementation or attributed doctrine/design. No target, test, example, model call or service was executed. Supplied runtime records establish the initial route inventory; direct reads below extend and challenge that inventory.

External provider internals, remote catalogs, third-party MCP storage and actual user session artifacts are not frozen evidence. This prevents conclusions about provider-side memory, live catalogs, exercised retention or measured benefit. Provider models and their unresolved internal state remain [RT-CMP-provider-model](runtime.md#rt-cmp-provider-model), not a locally inspected memory store. A file not inspected deeply is identified as such, not inaccessible or absent.

### Coverage inventory

| Entry point / part | Frozen source paths | Evidence and coverage / conclusion prevented |
|---|---|---|
| CLI/daemon session restore and ordinary accumulation | `crates/pa-cli/src/print_runtime.rs`; `crates/pa-daemon/src/agent_engine/lifecycle.rs` | Supplied [RT-RTE-print-prompt](runtime.md#rt-rte-print-prompt), [RT-RTE-daemon-session](runtime.md#rt-rte-daemon-session), [RT-OBJ-session-context](runtime.md#rt-obj-session-context); lifecycle restore searches checked. Durable file and live context remain different. All archive/repair variants were not traced; no complete recovery guarantee. |
| Prompt notes and memory facts | `crates/pa-core/src/refinement/mod.rs`; `prime-agent-runtime/src/rlm/harness.py` | Direct schema, loading, merge and helper reads: [MEM-OBJ-harness-entry](#mem-obj-harness-entry). Authorship is caller/model supplied; software checks shape, not truth. Initial user-store provenance is unknown. |
| Skill reference and argument contract | Same files; `crates/pa-core/src/refinement/ranking.rs` | Direct: [MEM-OBJ-skill-contract](#mem-obj-skill-contract). Not an installed package or autonomous call dispatcher. |
| Reusable subagent prompt | Same files; `prime-agent-runtime/src/rlm/factory.py` | Direct: [MEM-OBJ-subagent-entry](#mem-obj-subagent-entry); manual composition is afforded, factory resolution is wired. |
| Factory machine and description | `prime-agent-runtime/src/rlm/factory.py`; `prime-agent-runtime/src/rlm/harness.py` | Direct validation and resolution reads plus supplied [RT-OBJ-factory-machine](runtime.md#rt-obj-factory-machine), [RT-RTE-factory-run](runtime.md#rt-rte-factory-run). Stored spec is not the kernel-resident run registry. Bundled machine task internals remain uninspected; no complete per-machine memory characterization. |
| Direct create/update/upsert/delete and event authoring | `prime-agent-runtime/src/rlm/harness.py` | Direct: annotation on [RT-RTE-python-effects](runtime.md#rt-rte-python-effects). Separate admission from `/refine`; arbitrary filesystem writes remain another bypass. |
| `/refine`, queued refine, automatic review, rollback | `crates/pa-core/src/session_engine/slash_commands.rs`; `refine.rs`; `crates/pa-core/src/refinement/{executor.rs,planner.rs}` | Direct parse, planning, history projection, result application and persistence reads; annotate [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine). [MEM-OBJ-refinement-result](#mem-obj-refinement-result) distinguishes reasons retained from reasons delivered. Automatic review's full checkpoint scheduling is supplied runtime evidence, not independently exhaustively traced. |
| Automatic digest push | `crates/pa-core/src/session_engine/harness_digest.rs`; `crates/pa-core/src/refinement/ranking.rs` | Direct: [MEM-RTE-digest-delivery](#mem-rte-digest-delivery), annotation on [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest). Includes merge, rank, omission, stale-row replacement and persistence. |
| Requested full entry / search / overview | `prime-agent-runtime/src/rlm/harness.py` | Direct exposed operations: [MEM-RTE-harness-inspection](#mem-rte-harness-inspection). Returns full entries or explicit summaries, not automatic model delivery. |
| Manual/threshold compaction and resume | `crates/pa-core/src/session_engine/{compaction.rs,compaction_arms.rs,compact_session.rs,ipython_state.rs}` | Direct: [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary); annotate [RT-RTE-context-compact](runtime.md#rt-rte-context-compact). Summary, retained tail, separate digest and namespace notice have different lineage. |
| Kernel checkpoint / restore / prune | `prime-agent-runtime/src/rlm/repl.py`; `crates/pa-core/src/kernel/{state_snapshot.rs,provisioner.rs,manager/snapshot.rs}` | Direct: [MEM-OBJ-kernel-state](#mem-obj-kernel-state), [MEM-OBJ-kernel-manifest](#mem-obj-kernel-manifest), [MEM-RTE-kernel-revival](#mem-rte-kernel-revival). Per-variable loss and compaction pruning prevent intact-namespace guarantees. All protocol repair branches not audited. |
| Tree navigation, optional abandoned-branch summary, fork | `crates/pa-daemon/src/branch_navigation.rs`; `crates/pa-core/src/session_engine/branch_summarization.rs` | Direct: [MEM-RTE-branch-navigation](#mem-rte-branch-navigation). Fork prepare source states active-path copying; subsequent artifact-copy and kernel ownership details remain uninspected, preventing blanket fork-state equivalence. |
| Skills, prompt templates and instruction resources | `crates/pa-core/src/skills/mod.rs`; `crates/pa-core/src/session_engine/admission.rs`; `crates/pa-core/src/session_engine/runtime_wiring.rs` | Direct inventory/expansion/admission reads; annotate [RT-RTE-skill-install](runtime.md#rt-rte-skill-install). Supplied package/reload wiring; full loader precedence and project instruction editing lifecycle remain uninspected. Static bundled text is working context, not by itself use-derived memory. |
| Delegated work and explicit result crossing | `prime-agent-runtime/src/rlm/__init__.py`; `crates/pa-cli/src/print_rlm.rs`; `crates/pa-daemon/src/rlm_children/host.rs` | Supplied [RT-RTE-child-spawn](runtime.md#rt-rte-child-spawn), with distinct retained subagent-spec consumer checked in factory source. Child history and explicit collection are not automatic inheritance of parent history. All message/observe recovery variants not inspected. |
| Goals, quota parks, autonomous/scheduled wake-ups | `crates/pa-daemon/src/agent_engine/lifecycle.rs`; `crates/pa-core/src/session_engine/goal_driver.rs`; `crates/pa-daemon/src/scheduled_jobs.rs` | Runtime identifies continuations; lifecycle search reveals goal branch restore, quota restore and window adoption. These operative retained control parts remain incompletely inspected: exact schedule retention, cancellation and replay selection unknown. No full memory-lifecycle or recovery conclusion for them. |
| Exports, telemetry, traces, workspace snapshots and release payloads | Boundary inclusions; supplied [RT-RTE-release-update](runtime.md#rt-rte-release-update) | Excluded from detailed memory tracing here unless consumed by the routes above. No automatic trace-export-to-harness feedback is established by an export label. Uninspected downstream evaluators and package/update recovery cannot support efficacy or universal withdrawal claims. |

## Core ideas

1. **One JSON store serves several different consumers.** Textual facts and supplemental policies guide the foreground model. A skill record routes to an existing Python callable. A subagent entry can become a child's full prompt. Factory machine arguments are consumed by code, not just displayed to the model. Grouping these as undifferentiated natural-language memory would hide operative symbolic parts. [MEM-OBJ-harness-entry](#mem-obj-harness-entry), [MEM-OBJ-skill-contract](#mem-obj-skill-contract), [MEM-OBJ-subagent-entry](#mem-obj-subagent-entry), [RT-OBJ-factory-machine](runtime.md#rt-obj-factory-machine).
2. **Automatic delivery is a lossy, boundary-driven push.** The host merges global and local state, ranks within each kind and pushes compact hints. Relevance is not continuously refreshed solely because task terms change: the freshness fingerprint excludes those terms. Full-entry inspection is a separate requested route. [MEM-RTE-digest-delivery](#mem-rte-digest-delivery), [MEM-RTE-harness-inspection](#mem-rte-harness-inspection).
3. **Trajectory-fed editing retains more than its later readers see.** Refinement stores rationale, expected outcome and before/after edits. Its next planner receives bounded summaries, edit statuses and expected outcomes, not the entire audit. The digest omits event evidence. Labels such as `outcome` do not mean a post-change measurement: Rust writes the proposal's expected outcome there. [MEM-OBJ-refinement-result](#mem-obj-refinement-result).
4. **Conversation and executable namespace are separate memory domains.** A context summary is natural-language reconstruction; a dill payload can revive Python objects directly. The JSON namespace manifest and post-compaction notice only report names and losses, not object contents. Compaction can remove oversized live variables even though the kernel process survives. [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary), [MEM-RTE-kernel-revival](#mem-rte-kernel-revival).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-harness-entry
Label: Harness prompt and memory text

Source-native identity: `HarnessEntry` of kind `prompt` or `memory`, individually keyed by kind and ID in `harness_state.json`. Representational form: natural-language content; symbolic ID, path, scope, source, timestamps, version and metadata are access/provenance fields rather than truth warrant. Storage substrate: global `<agent dir>/harness/` or local session-artifact `harness/`. Local entries do not simply overwrite global entries in the merged digest: an ID collision gets a `local:` merged key, and both entries survive with scope labels. Rust skips malformed entries and degrades corrupt/unreadable files to empty; successful rendering therefore does not establish complete recovery. [SRC-1: `crates/pa-core/src/refinement/mod.rs`]

Lineage: caller-authored direct entries or refiner-derived trajectory lessons. New stores can be empty; actual populated user-store initialization is uninspected. `source = agent` and a version counter do not authenticate the creator or evidence. Consumers: selected text reaches the foreground model as user-role context, not base-system enforcement; full text can be requested through the kernel helpers. Prompt notes supplement policy, memory text asserts facts/preferences/decisions, but neither kind receives semantic verification by its label. Closest supplied records are [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine) and [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest), routes/authority rather than this stored content. No counterpart object after comparison.

> let merged_id = if merged.entries[&kind_key].contains_key(id) {
>     format!("local:{id}")
> } else {
>     id.clone()
> };
> --- `crates/pa-core/src/refinement/mod.rs`

#### MEM-OBJ-skill-contract
Label: Harness skill call contract

Source-native identity: skill-kind `HarnessEntry.content`, `reference` and `arguments`. Storage substrate: the same local/global harness JSON, not the installed Python package. Representational form: natural-language explanation plus symbolic Python import/call-pattern and argument records. Shape checks require a Python reference for a new skill and validate provided references; these checks do not demonstrate that the named callable exists or performs the asserted procedure. Lineage: direct authored contract or trajectory-fed refinement. Later consumers: foreground model receives truncated reference/arguments and text in the digest, or requests the full record and chooses a Python call. The kernel executes the call, but no automatic harness-skill dispatch is established. Closest supplied [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) is distinctly the filesystem package/body installation route, not this pointer/contract; [RT-RTE-python-effects](runtime.md#rt-rte-python-effects) is its possible executor. [SRC-1: `prime-agent-runtime/src/rlm/harness.py`, `crates/pa-core/src/refinement/ranking.rs`]

> if normalized.get("type") != "python":
>     reject("skill reference.type must be 'python'")
> if not any(isinstance(normalized.get(key), str) and normalized[key] for key in ("import", "python_import")):
>     reject("skill reference requires a Python import")
> if not any(isinstance(normalized.get(key), str) and normalized[key] for key in ("callable", "call_pattern")):
>     reject("skill reference requires a callable or call_pattern")
> --- `prime-agent-runtime/src/rlm/harness.py`

#### MEM-OBJ-subagent-entry
Label: Harness subagent prompt template

Source-native identity: subagent-kind `HarnessEntry.content`, with optional `metadata.model` and `metadata.thinking`. Representational form: natural-language task template plus symbolic spawn selectors. Storage substrate: local/global JSON; resolved template and settings are copied into the factory run's kernel memory. Lineage: direct authorship or refiner-derived reusable role. Foreground manual spawning is model-mediated composition from a hint/full entry; factory resolution loads the full entry by ID, then title fallback, validates spawn settings and uses its content as the prompt template. Inline machine subagent objects are an alternative authoring route that need no stored subagent entry. Later child model interprets the template; host code enforces valid selectors, not task truth. Distinct from the child session itself in [RT-RTE-child-spawn](runtime.md#rt-rte-child-spawn) and from the machine container [RT-OBJ-factory-machine](runtime.md#rt-obj-factory-machine). [SRC-1: `prime-agent-runtime/src/rlm/factory.py`]

> prompt = entry.content
> name = None
> metadata = entry.metadata if isinstance(entry.metadata, dict) else {}
> model = metadata.get("model")
> thinking = metadata.get("thinking")
> --- `prime-agent-runtime/src/rlm/factory.py`

#### MEM-OBJ-refinement-result
Label: Refinement audit and event projections

Source-native identity: `RefinementResult` and its compact `HarnessRefinementEvent` projection. Storage substrate: session audit entries, global `refinement_history.jsonl` for global refinement, and events inside harness JSON. Representational form: symbolic edit/status/before/after records plus natural-language rationale, reason, summary and expected outcome. This is derived update history, not the raw trajectory, and not a validated outcome report. Closest supplied [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine) is the producing route; no counterpart object after comparison. [SRC-1: `crates/pa-core/src/refinement/planner.rs`, `crates/pa-core/src/session_engine/refine.rs`]

The full result retains reasons and entry snapshots; rollback consumes the applied before/after records, skipping failed edits and reversing order. The next model planner's `history_for_prompt` selects the last twenty results but prints summary, applied/failed action identifiers, rollback ID and expected outcome. It does not print full rationale, per-edit reason, rejection explanation or before/after content. The planner's separate current-state overview selects up to forty entries per kind and 240 content characters. Foreground digest selects recent compact events, omitting their `evidence` field. Generic helper inspection of the state snapshot can return event evidence; automatic delivery cannot be described as full reason read-back. [SRC-1: `crates/pa-core/src/refinement/executor.rs`, `crates/pa-core/src/refinement/ranking.rs`, `prime-agent-runtime/src/rlm/harness.py`]

> evidence: proposal.rationale.clone(),
> outcome: proposal.expected_outcome.clone(),
> --- `crates/pa-core/src/refinement/planner.rs`

> format!(
>     "[{}]{} {}\n{edits}\nExpected outcome: {}",
>     item.id, rollback, item.summary, item.expected_outcome
> )
> --- `crates/pa-core/src/refinement/executor.rs`

#### MEM-OBJ-compaction-summary
Label: Compaction checkpoint summary
Part of: [RT-OBJ-session-context](runtime.md#rt-obj-session-context)

Source-native identity: compaction entry's `summary`, `first_kept_entry_id`, details and separately attached harness digest/fingerprint. Representational form: natural-language summary; symbolic boundary and file-operation metadata. Storage substrate: session JSONL and reconstructed model messages. Lineage: selected raw session prefix, optionally previous summary and split-turn prefix, through model summarization, then code-combined file-operation suffix. Old raw entries remain session history rather than being interchangeable with the summary. Later invocations see summary-first rebuilt context and retained tail; the harness digest is rendered at commit after summarization and never passed through that summarizer. It is therefore a second checkpoint input, not a learned fact inferred by the summary model. [SRC-1: `crates/pa-core/src/session_engine/compact_session.rs`, `crates/pa-core/src/session_engine/compaction_arms.rs`]

Reasons: summarization instructions ask for brief decision rationales and exact paths/names/errors; semantic fidelity and completeness are model compliance, not enforced equivalence. Default recent-tail budget is 20,000 estimated tokens, reserve 16,384; cuts avoid separating tool results from valid turn boundaries. These are adjustable settings, not a fixed universal memory capacity. Supplied [RT-RTE-context-compact](runtime.md#rt-rte-context-compact) identifies the producer; this declaration names its retained part, not another route.

> let mut summary = match &turn_prefix_slice {
>     Some(prefix) => split_summary(&history_slice.summary, &prefix.summary),
>     None => history_slice.summary.clone(),
> };
> --- `crates/pa-core/src/session_engine/compact_session.rs`

> // The digest snapshot and its fingerprint attach at the commit and never flow
> // through the summarizer; the read happens after the summarizer resolved.
> --- `crates/pa-core/src/session_engine/compact_session.rs`

#### MEM-OBJ-kernel-state
Label: Serialized Python namespace
Part of: [RT-CMP-repl-kernel](runtime.md#rt-cmp-repl-kernel)

Source-native identity: artifact `kernel-state.dill`; v2 framed per-name dill records, with legacy single-dict framing also accepted. Representational form: serialized symbolic executable objects and arbitrary caller values, not a readable natural-language memory. User values can themselves contain arrays, text or opaque objects; payload content and provenance are uninspected without session artifacts. Storage substrate: session artifact file and revived process namespace. Lineage: live namespace produced by model cells, imports and external inputs; snapshot serializes eligible names, skipping private/bootstrap names, unserializable objects and oversized values. Consumer is the kernel restore/unpickler before runtime bootstrap; its output can directly alter later Python execution. This component part is distinct from session message history and from the manifest. [SRC-1: `prime-agent-runtime/src/rlm/repl.py`, `crates/pa-core/src/kernel/state_snapshot.rs`, `crates/pa-core/src/kernel/provisioner.rs`]

Default aggregate cap is 256 MiB and per-variable cap 16 MiB. Pruning mode measures against the per-variable limit and removes oversized names from the live namespace only after payload and manifest replacements; ordinary over-budget skips do not by themselves delete live names. Raw-descriptor unpickling is guarded, but this is not general untrusted-pickle sandboxing. The supplied process component is the parent of this retained artifact, not the same object.

> for name in pruned:
>     ns.pop(name, None)
> --- `prime-agent-runtime/src/rlm/repl.py`

#### MEM-OBJ-kernel-manifest
Label: Namespace checkpoint manifest and notice
Part of: [RT-CMP-repl-kernel](runtime.md#rt-cmp-repl-kernel)

Source-native identity: artifact `kernel-state.json` and model-facing `ipython_state` notice. Storage substrate: JSON artifact, snapshot result metadata, session custom-message row and live model context. Representational form: symbolic saved/skipped/pruned names, byte count, Python version and timestamp; natural-language notice describes persistence and names. Lineage: checkpoint metadata and a fresh live namespace-name probe, not summarization of variable contents. Consumers: host bookkeeping/freshness checks, operator diagnostics and foreground model. A name list does not reconstruct the value and is not a complete persistence witness: listing can time out and still yield a no-detail notice. Parent is a process component because these are its retained/reporting parts. Distinct from [MEM-OBJ-kernel-state](#mem-obj-kernel-state) and from raw tool output in [RT-OBJ-session-context](runtime.md#rt-obj-session-context). [SRC-1: `prime-agent-runtime/src/rlm/repl.py`, `crates/pa-core/src/kernel/manager/snapshot.rs`, `crates/pa-core/src/session_engine/ipython_state.rs`]

> "savedNames": saved,
> "skipped": skipped,
> "pruned": pruned,
> "bytes": total,
> --- `prime-agent-runtime/src/rlm/repl.py`

### Routes

#### MEM-RTE-digest-delivery
Label: Boundary-triggered harness digest delivery

Endpoints: local/global harness files to renderer, custom prompt/session row and foreground model. Owner: session host. Progression: at cold start/resume defer an empty-context digest to first admitted turn; a populated context compares its newest digest with freshly rendered state; compaction attaches a fresh rendering at commit. Code loads and merges state, derives up to 48 query terms from active goal (weight 3) and last four user/assistant texts (weights starting at 2), then ranks each kind by weighted field overlap with within-kind inverse document frequency. Defaults retain three entries per kind, 140-character compact content/reference/argument snippets and ten recent refinement events. These are entry/character limits, not a fixed whole-message token budget. No counterpart route after comparison: [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest) is its authority path, and [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine) is a producer, not this independent read-back operation. [SRC-1: `crates/pa-core/src/session_engine/harness_digest.rs`, `crates/pa-core/src/refinement/ranking.rs`, `crates/pa-core/src/refinement/mod.rs`]

- Immediate return: a selected rendering or no new row when the newest in-context digest is fresh.
- Later read-back: the pushed row converts to a model-facing user turn; persisted digest details support context reconstruction, while later boundary renderings reload stores.
- Delegated visibility: inapplicable — this is per-session context delivery, not parent-to-child transcript forwarding.
- Selection predicate: cold-context trigger, current store fingerprint and interface flags; goal/recent text terms rank entries within each kind. Query changes alone do not invalidate a matching state fingerprint.
- Invalidation or expiry: state/flag changes or missing context digest permit refresh; host removes superseded digest rows and strips an older digest block from a compaction summary without removing the summary text.
- Activation or effect: context insertion is wired; guidance compliance and behavioral dependence on a delivered entry remain unobserved.
- Evidence limits: implementation and renderer instructions only; no populated store, model response or fidelity measurement inspected. No continuous per-turn relevance refresh is established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The host selects and admits the rendering automatically; a human need not approve every snippet. The renderer tells the model to treat compact entries as routing hints and inspect detail when needed. Source text is not authenticated by relevance score or promoted to the immutable system prompt. This push remains distinct from a foreground-requested search.

> /// The render flags the digest actually reads: the relevance query terms
> /// are excluded — the digest stays frozen per delivery.
> --- `crates/pa-core/src/refinement/ranking.rs`

> Some(state_fingerprint) => state_fingerprint == fresh.state_fingerprint,
> None => latest.digest == fresh.digest,
> --- `crates/pa-core/src/session_engine/harness_digest.rs`

#### MEM-RTE-harness-inspection
Label: Requested harness inspection

Endpoints: foreground Python call to `rlm.harness` get/list/search/overview/snapshot and caller. Owner: calling agent/caller selects operation, query, scope, kind and limit; helper reloads stale disk state and selects results. This exposes a documented model-facing read route rather than asserting that every storage API is routinely called. Full objects return to the Python namespace; the foreground model sees returned/printed tool output only as exposed by its cell. It is distinct from [MEM-RTE-digest-delivery](#mem-rte-digest-delivery)'s automatic push and adds the detail operation suggested by [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest). [SRC-1: `prime-agent-runtime/src/rlm/harness.py`, `crates/pa-core/src/refinement/ranking.rs`]

- Immediate return: full entry or list of entries, compact overview string, or full symbolic state snapshot according to operation.
- Later read-back: stored entries/events authored in earlier turns/sessions reach later helper invocations; the model can expose details through Python tool results.
- Delegated visibility: inapplicable — helper return is local; callers must explicitly send data or use a child prompt to cross contexts.
- Selection predicate: get uses exact kind/ID and scope; list orders by kind/path/title/ID; search uses query terms against title/content/path/ID, discounts common terms, removes zero-score matches and defaults to ten results with recency tie-breaking; overview defaults to twenty entries per kind and 120-character snippets.
- Invalidation or expiry: subsequent update/delete alters future reads; prior Python references or already-delivered text are not recalled automatically.
- Activation or effect: entries are available to caller computation and model interpretation; their actual use is unobserved.
- Evidence limits: exposed helper implementation and digest's inspection guidance establish an afforded model consumption route, not observed invocation or a guarantee that unprinted objects enter the model window.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> ranked = sorted(entries, key=lambda e: (score(e), recency(e)), reverse=True)
> ranked = [e for e in ranked if score(e) > 0]
> return ranked[:limit]
> --- `prime-agent-runtime/src/rlm/harness.py`

#### MEM-RTE-kernel-revival
Label: Namespace capture and revival

Endpoints: persistent live Python namespace to snapshot payload/manifest, later provisioner boot/restore and subsequent cell execution. Owner: kernel manager schedules capture; runtime serializes/revives; bootstrap reinstalls live host/skill handles after restore. Capture is code admission of current values under size/serialization checks, not content criticism or per-variable human approval. It preserves execution state, not distilled lessons. Closest supplied [RT-CMP-repl-kernel](runtime.md#rt-cmp-repl-kernel) is the process; [RT-RTE-context-compact](runtime.md#rt-rte-context-compact) can trigger pruning; neither is this persistence/restore route. [SRC-1: `crates/pa-core/src/kernel/manager/snapshot.rs`, `crates/pa-core/src/kernel/provisioner.rs`, `prime-agent-runtime/src/rlm/repl.py`]

- Immediate return: saved/skipped/pruned or restored/failed name metadata; no target allows no snapshot/restore.
- Later read-back: artifact-backed restart/resume boots restore payload into namespace before bootstrap; subsequent Python cells can consume revived objects without their original defining messages in the model window.
- Delegated visibility: inapplicable — revival restores the session kernel, not a child transcript or shared namespace.
- Selection predicate: configured snapshot target; debounced capture and teardown flush; eligible top-level names and byte caps; explicit post-compaction pruning selects over-per-variable-cap names. Restore accepts framed payload or legacy dict framing and filters reserved names.
- Invalidation or expiry: later capture replaces payload/manifest; skipped/unrevivable values are lost on restart; compaction prune deletes oversized live values; a busy kill can omit final flush. No complete external-resource revival is established.
- Activation or effect: restore assigns prepared values into live namespace; callable globals are rebound and later cells can depend on restored values. Actual restored executions are unobserved.
- Evidence limits: no payload or execution inspected; snapshot and manifest replacements are ordered, not one atomic multi-file transaction. Per-variable failures and framing failures have distinct results; full repair coverage not audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Guidance: compaction's summarizer is told to remember useful Python names; host notice independently reports current names/pruning. These displays do not supply serialized values. Snapshot error before commit preserves prior artifacts, while a manifest replacement error after payload replacement can leave a mismatched pair; pruning is withheld in that error branch. Recovery is therefore best effort, not universal exact replay. [SRC-1: `prime-agent-runtime/src/rlm/repl.py`, `crates/pa-core/src/session_engine/ipython_state.rs`]

> // bootstrap then overwrites live handles (rlm, skills) on top of anything restored.
> --- `crates/pa-core/src/kernel/provisioner.rs`

> for name, value in prepared.items():
>     ns[name] = value
> --- `prime-agent-runtime/src/rlm/repl.py`

#### MEM-RTE-branch-navigation
Label: Branch selection and abandoned-path summary

Endpoints: daemon `navigate_tree` request, retained tree paths, optional model summary, persisted branch-summary entry and rebuilt engine context. Owner: caller chooses target and whether to summarize; daemon pauses/settles running work, computes old-path entries outside the common ancestor, optionally invokes summary generation, changes leaf and rebuilds. New retained summary is natural language plus symbolic file metadata; plain navigation instead reloads the selected path. No supplied counterpart after comparison: [RT-OBJ-session-context](runtime.md#rt-obj-session-context) contains the session tree, while [RT-RTE-context-compact](runtime.md#rt-rte-context-compact) compresses the active path rather than carrying an abandoned path into another. [SRC-1: `crates/pa-daemon/src/branch_navigation.rs`, `crates/pa-core/src/session_engine/branch_summarization.rs`]

- Immediate return: navigation result, optional editor text and summary entry; cancelled/aborted or failed summary prevents that navigation's continuation.
- Later read-back: summary attached at the new leaf participates in rebuilt later model context; plain move reloads target branch history.
- Delegated visibility: inapplicable — tree navigation is same-session context selection, not child result collection.
- Selection predicate: requested target, old leaf, common ancestor and summarize option; summary input is newest-first budgeted abandoned-path messages, with accumulated file-operation tracking and exclusion of standalone harness digest rows.
- Invalidation or expiry: another branch move changes active path; entries remain retained tree material. Further summaries may replace the model's detailed view; factual equivalence is not enforced.
- Activation or effect: engine context rebuild is wired; actual reliance on summary or preservation of facts is unobserved.
- Evidence limits: daemon navigation and summary preparation inspected; full fork artifact transfer and all tree-repair branches uninspected. Summary model budget is caller-configured, not an invariant supplied here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller supplies navigation/summary instructions (human identity unresolved at a generic daemon request); model proposes summary, software persists/rebuilds or rejects abort/error. No obligatory per-summary approval or answer oracle is established. This is open-session context maintenance, not an improvement experiment. Raw abandoned entries and derived summary have different consumers and no semantic rollback guarantee.

> // Move the leaf and persist the summary entry, then rebuild the engine context.
> --- `crates/pa-daemon/src/branch_navigation.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-subagent-template
Label: Stored subagent content to child instructions

Consumer: later factory-launched child model. Channel: full harness subagent content resolved as the state's prompt template, with validated metadata selectors; child host receives the resulting task. Force: model-interpreted task instructions, alongside symbolic model/thinking selection by code. Horizon: stored entry survives within local session or global cross-session scope, but one factory run snapshots its resolved template in kernel memory; editing the entry is not proven to rewrite already-launched children. Distinct from [RT-BAP-machine-guards](runtime.md#rt-bap-machine-guards)' code progression and [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest)'s truncated foreground hints. [SRC-1: `prime-agent-runtime/src/rlm/factory.py`]

> run.states[state_id] = _StateRun(
>     state_id=state_id,
>     spec=state_spec,
>     position=position,
>     prompt_template=prompt,
> --- `prime-agent-runtime/src/rlm/factory.py`

## Annotations

#### On [RT-OBJ-factory-machine](runtime.md#rt-obj-factory-machine)

Memory-specific split: full symbolic `arguments.machine` or DAG sugar is consumed after validation/canonicalization; natural-language entry description is only a routing/display summary. Digest renders entry content but does not expose factory machine arguments as it does skill arguments. Library `MachineFile.spec` is an alternative source with file lineage rather than prior-session harness authorship. Subagent state references resolve to full stored text or inline prompt objects; run state is retained only in kernel registry, not durable workflow replay. [SRC-1: `crates/pa-core/src/refinement/ranking.rs`, `prime-agent-runtime/src/rlm/factory.py`]. See [MEM-OBJ-subagent-entry](#mem-obj-subagent-entry).

#### On [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine)

Trace origin is the session trajectory visible to the refiner, including human task/corrections, model messages, tool results and previous derived/custom context. It is mixed provenance, not pure independently checked environment evidence. Planner serializes a tail capped initially at 80,000 characters, plus projected state/history; request construction can further budget it. Model proposes evidence-responsive edit text; code validates/rejects/conflict-checks and physically writes. Manual invocation or factory opt-in is not per-content human approval. The durable behavior-shaping result is the edited entry, delivered through [MEM-RTE-digest-delivery](#mem-rte-digest-delivery), requested inspection or full factory resolution. Raw transcript retention alone does not constitute this transformation. [SRC-1: `crates/pa-core/src/refinement/executor.rs`, `crates/pa-core/src/refinement/planner.rs`, `crates/pa-core/src/session_engine/refine.rs`]

Reasons persist in [MEM-OBJ-refinement-result](#mem-obj-refinement-result), but subsequent automatic readers receive projections. Rejections persist as edit result statuses and leave target entries unchanged; rejection is structural/admission judgment, not a demonstrated unsuccessful tactic. Delete/rollback changes later store loads, not already delivered messages or copies. State write precedes global-history/audit/outcome writes; a later error need not mean no edit applied. Expected outcome is a model proposal, not measured validation.

> let conversation_text = conversation_text(messages, 80_000);
> --- `crates/pa-core/src/refinement/executor.rs`

#### On [RT-RTE-python-effects](runtime.md#rt-rte-python-effects)

Memory write agency: direct `upsert/create/update/delete/record_refinement` accepts caller-authored content. The helpers synchronize disk/lock, validate nonempty strings/record shapes and skill/factory contracts, increment versions, then save. `create` versus `update` existence checks differ from upsert; direct helper admission need not contain refiner rationale or automatic outcome records. `record_refinement` permits arbitrary caller evidence/outcome strings after type checks. `plan_refinement` only constructs advice strings; it is not a planning model or automatic improvement test. Generic caller identity leaves human involvement unresolved. [SRC-1: `prime-agent-runtime/src/rlm/harness.py`]

> self.entries[kind][entry_id] = entry
> self.save()
> return entry
> --- `prime-agent-runtime/src/rlm/harness.py`

#### On [RT-RTE-context-compact](runtime.md#rt-rte-context-compact)

Raw-to-derived chain is session prefix/previous summary to model-written checkpoint, code-added file-operation metadata, retained compaction entry, summary-first rebuilt later context. A split-turn prefix can receive a second summary. Automatic digest attachment occurs after summarization; kernel notice is another independent input. Pruning means kernel-process survival does not imply every variable survives: host explicitly prunes oversized variables before listing remaining names. Trigger is code/manual compaction; summarizer decides textual preservation under requested format; code chooses cut and commit validity. Aborts/skips do not admit a new summary; structural conflict re-prepares. Original disk history, summary/tail and surviving Python objects are distinct reachable material, not interchangeable model-window pointers. [SRC-1: `crates/pa-core/src/session_engine/compact_session.rs`, `crates/pa-core/src/session_engine/compaction_arms.rs`, `crates/pa-core/src/session_engine/ipython_state.rs`]

> let pruned = probe.prune_oversized_variables().await;
> --- `crates/pa-core/src/session_engine/ipython_state.rs`

#### On [RT-RTE-skill-install](runtime.md#rt-rte-skill-install)

Context selection distinguishes inventory and body. Inventory supplies names/descriptions/locations/imports, excluding model-disabled skills. Prompt admission can expand `/skill:<name>` into the full frontmatter-stripped body and caller arguments as a user-message block; a missing/failed-read skill passes through. Thus body expansion occurs in the current session context, not a verified forked frame. Independently the model is instructed to inspect a matching file through Python. Changed skill bodies can reach later invocations after startup/reload and expansion; static shipped content alone is not accumulated memory. Authorship/adoption stays filesystem/discovery driven as the supplied route states; no mandatory content approval follows from discovery. [SRC-1: `crates/pa-core/src/skills/mod.rs`, `crates/pa-core/src/session_engine/admission.rs`]

> let body = frontmatter::strip_frontmatter(&content).trim().to_string();
> --- `crates/pa-core/src/skills/mod.rs`

#### On [RT-RTE-child-spawn](runtime.md#rt-rte-child-spawn)

Working-context control: model/caller selects task and starts independent child context, keeping child working turns out of the parent's active window; explicit collect/messages/files cross selected outputs back. Child handles retain access identity, not automatically dereferenced parent-window memory. This resembles isolated task frames only in selected-input/result crossing: resident children and independently retained session histories can outlive a call and accept follow-ups. Retained spec consumption is separately established by [MEM-OBJ-subagent-entry](#mem-obj-subagent-entry) and [MEM-BAP-subagent-template](#mem-bap-subagent-template); spawning alone does not establish that a prior reusable spec was used. Evidence and minimum passages for context isolation/admission remain the supplied route, not a new independent observation.

#### On [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest)

Authority remains model-interpreted user-role hints. Added consumer limit: top-three/140-character default projections omit full fact conditions, factory machine arguments, most entries and event evidence. [MEM-RTE-digest-delivery](#mem-rte-digest-delivery) names automatic selector and freshness; [MEM-RTE-harness-inspection](#mem-rte-harness-inspection) names requested recovery of full detail. No delivered hint is thereby an authenticated or behaviorally activated lesson. [SRC-1: `crates/pa-core/src/refinement/ranking.rs`, `crates/pa-core/src/session_engine/harness_digest.rs`]

## Write side

### Admission and maintenance

| Write mechanism | Authorship / physical writer | Content admission and rejection | Retained result / withdrawal |
|---|---|---|---|
| Direct harness helpers | Caller supplies text/records; Python saves under cooperating lock | Software shape/existence checks, skill reference checks, factory gate/spec validation; generic caller identity does not establish human approval | Versioned entry or deleted record; caller event text separately authored. Later loads reflect edits; delivered/cached copies can survive. [RT-RTE-python-effects](runtime.md#rt-rte-python-effects) annotation |
| Manual/queued/automatic refinement | Model proposes from bounded mixed trajectory; Rust applies and saves | User can specify scope/instructions or request rollback; automatic review is model judgment; code can reject malformed/stale/protected edits. No independent expected-answer oracle or obligatory per-edit approval | Edited harness and audit/event projections; reverse applied before/after snapshots for rollback. Not transaction-wide rollback on audit error. [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine), [MEM-OBJ-refinement-result](#mem-obj-refinement-result) |
| Skill/instruction package files | Human/model/caller writes files; discovery/bootstrap later loads | Resource discovery/capability installation, not content approval. Full precedence/rejection branches remain uninspected | Edited filesystem resources; withdrawal/removal/reload can affect future load, not undo executed Python effects. [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) |
| Session summaries | Summary model authors; host chooses cut, persists and rebuilds | Code can skip/abort/retry conflict or fail persistence; human custom focus shapes request, not per-summary approval | Natural-language checkpoint plus retained tail and file metadata. Older raw entries remain; another summary replaces view. [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary), [MEM-RTE-branch-navigation](#mem-rte-branch-navigation) |
| Namespace checkpoint | Cells/imports create values; runtime serializes | Byte/serialization/name checks, not truth or utility evaluation | Payload + manifest; prune deletes per-variable-over-cap names only in explicit pruning mode, restore skips failures. [MEM-RTE-kernel-revival](#mem-rte-kernel-revival) |
| Unrestricted file effects | Foreground Python/shell caller | OS permissions, not universal harness admission; repository explicitly disclaims security sandbox | Can bypass helper locks/gates or edit raw stores; no all-writer invariant. [RT-CLM-user-permissions](runtime.md#rt-clm-user-permissions) |

Trace-fed refinement and compaction are different transformations. Refinement attempts reusable or local behavioral/factual edits from trajectory; compaction attempts continuation-preserving compression. Both have a later model consumer, but neither route's name or requested behavior proves accurate criticism, successful learning or measured improvement. `expectedOutcome` copied into an event is especially not a trace of subsequent validation. Evaluation-related refinement instructions are represented as requests, with actual evaluation execution unobserved. [MEM-OBJ-refinement-result](#mem-obj-refinement-result), [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine).

The direct-helper route is a counterexample to treating every harness update as a diagnosis/refinement pass. Inline factory subagent objects and library machine files are counterexamples to treating every factory launch as stored-role reuse. Snapshot/manifest skips and compaction pruning are counterexamples to treating every live variable as retained across all continuations. These alternatives qualify the primary routes rather than erasing them.

## Read-back

Automatic host push and requested lookup have different selection owners. [MEM-RTE-digest-delivery](#mem-rte-digest-delivery) chooses task-relevant compact hints and delivers a user-role context row at boundaries. [MEM-RTE-harness-inspection](#mem-rte-harness-inspection) supplies caller-chosen full entries or search matches; the model must expose/use the returned objects. A stored identifier is exact addressing for `get`, not evidence of semantic targeted selection; query overlap ranking is a distinct selector.

Factory consumes full machine arguments and resolved prompt templates, not only the digest hints. A direct ID/title reference routes stored subagent text to child instructions. Symbolic guards then decide machine progression, while child models interpret the task. [RT-RTE-factory-run](runtime.md#rt-rte-factory-run), [RT-BAP-machine-guards](runtime.md#rt-bap-machine-guards), [MEM-BAP-subagent-template](#mem-bap-subagent-template).

The planner reads a bounded trajectory, current-entry overview and reduced prior-result history. The audit retains more than either planner or digest receives. The ordinary foreground model receives notices/outcomes, not automatic full before/after replay. Rollback is a separate full-snapshot consumer and cannot be inferred from the model's visible rationale. [MEM-OBJ-refinement-result](#mem-obj-refinement-result), [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine).

Working-context control has several independent routes: child isolation keeps working messages out; skill selection avoids loading every instruction body; compaction replaces a prefix with summary/tail/digest; tree navigation selects another retained path; retry cleanup can drop failed assistant/goal-continuation rows from the live window without equivalent disk deletion. The cleanup is inspected in `compaction_arms.rs`, not evidence that dropped content is globally withdrawn. Later session reconstruction and kernel revival are separate reload operations. The stack-frame lens fits selected task inputs and explicit return crossing, but breaks for resident child sessions and retained tree branches. The active window holds text by value; skill locations and object names are instructions to perform later reads, not automatically followed/recounted heap references. [SRC-1: `crates/pa-core/src/session_engine/compaction_arms.rs`]. See [RT-RTE-child-spawn](runtime.md#rt-rte-child-spawn), [RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [MEM-RTE-branch-navigation](#mem-rte-branch-navigation), [MEM-RTE-kernel-revival](#mem-rte-kernel-revival).

## Integration issues

- **Correction/qualification to kernel survival:** [RT-RTE-context-compact](runtime.md#rt-rte-context-compact) and [RT-CMP-repl-kernel](runtime.md#rt-cmp-repl-kernel) remain valid process/context identities, but any reading that every variable survives compaction is false. `ipython_state` prunes oversized names before reporting remaining names. [MEM-RTE-kernel-revival](#mem-rte-kernel-revival), [MEM-OBJ-kernel-state](#mem-obj-kernel-state) retain the exact deletion witness. Analytical consequence: distinguish process persistence from value persistence. The source summarizer's own all-variables persistence note is similarly overbroad relative to post-commit pruning. [SRC-1: `crates/pa-core/src/session_engine/compaction.rs`, `crates/pa-core/src/session_engine/ipython_state.rs`]
- **History delivery qualification:** [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine)'s history-fed planning is wired, but it must not imply all retained reasons/rejections/before/after snapshots reach the next planner. [MEM-OBJ-refinement-result](#mem-obj-refinement-result) shows the projection, and distinguishes expected from observed outcome. Consequence: reason persistence and reason-based iteration need separate evidence. [SRC-1: `crates/pa-core/src/refinement/executor.rs`, `crates/pa-core/src/refinement/planner.rs`]
- **Freshness qualification:** [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest)'s relevance selection is valid per render, not continuously changing under new queries. [MEM-RTE-digest-delivery](#mem-rte-digest-delivery) shows query terms excluded from fingerprint. Consequence: task drift can leave a delivered hint selection unchanged until a relevant boundary/state change. [SRC-1: `crates/pa-core/src/refinement/ranking.rs`, `crates/pa-core/src/session_engine/harness_digest.rs`]
- **Identity review:** no new declaration intentionally duplicates a supplied referent. [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary) is a material part of [RT-OBJ-session-context](runtime.md#rt-obj-session-context); namespace payload/manifest are parts of [RT-CMP-repl-kernel](runtime.md#rt-cmp-repl-kernel). [MEM-RTE-digest-delivery](#mem-rte-digest-delivery) is the selector/delivery route corresponding to supplied authority path [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest), not a replacement identity. Text entries, contracts, subagent templates and audit records have separate consumers/encodings from their supplied producer routes. No supersession is proposed.
- **Unresolved included control parts:** persisted goals/quota parks, autonomous/scheduled wake-up state and all observe/message/recovery variants are inventoried but not fully traced. Supplied runtime and lifecycle search establish their relevance, not precise retention/replay/admission semantics. Consequence: no system-wide claim that every behavioral state is curated/recovered the same way. Records affected: [RT-RTE-daemon-session](runtime.md#rt-rte-daemon-session), [RT-OBJ-session-context](runtime.md#rt-obj-session-context), [RT-RTE-child-spawn](runtime.md#rt-rte-child-spawn). [SRC-1: `crates/pa-daemon/src/agent_engine/lifecycle.rs`]
- **Unresolved resource/fork/evaluation details:** full resource precedence, project instruction lifecycle, fork artifact copying, bundled factory machine task internals and exported-trace evaluator consumers remain available but uninspected. Prevented conclusions are in the coverage inventory; supplied [RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [RT-RTE-factory-run](runtime.md#rt-rte-factory-run) and new [MEM-RTE-branch-navigation](#mem-rte-branch-navigation) must retain those limits. No access failure or additional source is needed to state the supported mechanisms.
- **Unknown real content and behavior:** existing store initialization and payload values are not supplied; no actual output fidelity, consumer compliance or efficacy was observed. This limits activation/benefit, not the wired edit/delivery/restore capacities established above.

## Limitations and checks

Frozen source identity was rechecked with `git rev-parse HEAD`; it equals `33da15a2c15c4e903c372f69ae8e1156d77d53da`. The member follows the supplied memory type and record contract, with output-only write authority and no delegation. Source paths read beyond the initial register are recorded in the coverage inventory under SRC-1; evidence layers stay implementation or doctrine/design. Failed exploratory searches for nonexistent module paths were corrected to the actual tracked files and supply no absence evidence.

Load-bearing claims were challenged against alternative admission, full-entry readers, history projections, factory inline/library routes, snapshot skips and post-compaction pruning. No prior characterization or external source was used. No observed run, causal experiment, semantic-fidelity result or exercised learning claim is established. Supported wiring remains local to inspected paths; unresolved included parts are not converted into negative findings.

Validation: the invocation-specific `commonplace-run validate-output` check passed. This establishes form, identity and quotation occurrence, not semantic acceptance or effective memory use.
