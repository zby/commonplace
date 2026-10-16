---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Tracecraft memory: explicit shared-state read-back, cursor-controlled mail, and redacted host transcripts rather than automatic model-context reconstruction."
run-id: AAS-2026-10-14-tracecraft-9c4af961e8e2-01
source-identity: "https://github.com/arrmlet/tracecraft"
reviewed-boundary: "97c6b7447f8e696f0116357d9f86bb0ece25e5b1"
---

# Tracecraft memory report

## Boundary and evidence

Tracecraft retains coordination content and host-produced session records in a project-prefixed S3-compatible or HuggingFace bucket. This report covers the complete shipped memory loop at the [boundary](boundary.md): configuration and registration, shared values and snapshots, direct/broadcast mail and cursors, task state and handoffs, files, transcript ingestion, display, compaction and stop. It also checks the direct backend API and sampled evaluator read-back. External host prompt assembly, transcript creation/pruning, backend service implementation and actual agent compliance remain excluded. These exclusions prevent conclusions about reconstructed model conversations, complete host reasoning retention, service durability and behavioral uptake.

All source findings use SRC-1 at the frozen commit. Production evidence below is implementation; shipped example instructions and source docstrings are doctrine/design. Tests and benchmark drivers are implementation of evaluators, not observed passing runs. No target, tests, examples or services were executed. Supplied runtime records are provisional and were checked against direct reads, not used as the inspection boundary.

The following inventory covers the frozen CLI dispatch and exposed library surfaces. Source paths are commit-relative SRC-1 anchors. All production paths named here were read directly; linked runtime records also supply passages. Newly added detail includes operative-part separation, handoff consumer limits, OpenClaw checkpoints, compaction provenance loss, local cursor scope and sampled evaluator output handling.

| Entry point or operation | Directly inspected source paths | Coverage and limit |
|---|---|---|
| Dispatch, adapter registration and direct storage factory | `sdk/tracecraft/cli/__init__.py`, `sdk/tracecraft/harness/__init__.py`, `sdk/tracecraft/store.py`, `sdk/tracecraft/__init__.py` | [RT-CMP-get-store](runtime.md#rt-cmp-get-store), [RT-CMP-harness-registry](runtime.md#rt-cmp-harness-registry). CLI registers the routes below; the registry has four adapters. No separate host hook or model-tool registration appears in this inspected dispatch; cron/hook scheduling is external. |
| Init/config/agent and status views | `sdk/tracecraft/config.py`, `sdk/tracecraft/cli/init_cmd.py`, `sdk/tracecraft/cli/agents.py`, `sdk/tracecraft/cli/status.py`, `sdk/tracecraft/protocol.py` | [RT-OBJ-config](runtime.md#rt-obj-config), [RT-RTE-init-config](runtime.md#rt-rte-init-config), [MEM-OBJ-agent-registration](#mem-obj-agent-registration); source trust is caller attribution, not authenticated identity. |
| Memory set/get/list/history | `sdk/tracecraft/cli/memory.py`, `sdk/tracecraft/protocol.py` | [MEM-OBJ-memory-live](#mem-obj-memory-live), [MEM-OBJ-memory-history](#mem-obj-memory-history), annotation on [RT-RTE-memory-write](runtime.md#rt-rte-memory-write). History is not proof that each attempted value became live. |
| Send/inbox/full/new/delete and status unread counts | `sdk/tracecraft/cli/messages.py`, `sdk/tracecraft/protocol.py`, `sdk/tracecraft/cli/status.py` | [MEM-OBJ-message-content](#mem-obj-message-content), [MEM-OBJ-inbox-cursor](#mem-obj-inbox-cursor), annotation on [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange). Reader position and content are separate. |
| Claim/complete/step-status/wait-for | `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/protocol.py`, `sdk/tracecraft/cli/status.py` | [RT-OBJ-step-state](runtime.md#rt-obj-step-state), [MEM-OBJ-handoff](#mem-obj-handoff), annotation on [RT-RTE-step-control](runtime.md#rt-rte-step-control). Polling consumes state, not handoff reasons; no inspected CLI displays handoff content. |
| Artifact upload/download/list | `sdk/tracecraft/cli/artifacts.py` | [MEM-OBJ-artifact-file](#mem-obj-artifact-file), annotation on [RT-RTE-artifact-share](runtime.md#rt-rte-artifact-share). Content is opaque to the SDK; downloaded content interpretation is unresolved. |
| Mirror one-shot/follow/follow-all | `sdk/tracecraft/cli/session.py`, `sdk/tracecraft/redact.py`, `sdk/tracecraft/harness/base.py` | [MEM-OBJ-session-parts](#mem-obj-session-parts), [MEM-OBJ-session-meta](#mem-obj-session-meta), [MEM-OBJ-mirror-state](#mem-obj-mirror-state), annotation on [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror). Automatic retention after initiation, not automatic knowledge extraction. |
| Alternative host trace discovery/ingestion | `sdk/tracecraft/harness/claude_code.py`, `sdk/tracecraft/harness/codex.py`, `sdk/tracecraft/harness/openclaw.py`, `sdk/tracecraft/harness/hermes.py` | Same mirror parts with different lineage and cursors. File transcripts include OpenClaw checkpoint/topic files; Hermes synthesizes message-row JSONL. External content provenance and completeness are unresolved. |
| Session list/show/tail/compact/stop and totals | `sdk/tracecraft/cli/session.py`, `sdk/tracecraft/protocol.py` | Annotations on [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror) and [RT-RTE-session-compact](runtime.md#rt-rte-session-compact). Display tail is line-limited, not model-token-limited; maintenance changes storage/access metadata. |
| Direct put/get/list/delete/file operations | `sdk/tracecraft/s3.py`, `sdk/tracecraft/hf.py` | [MEM-CLM-history-immutability](#mem-clm-history-immutability). Alternative writes bypass CLI validation, snapshots and mirror redaction; unspecified API callers establish capacity only. Service-side versioning/retention and deployed authorization are uninspected. |
| Shipped model-facing read/write procedure | `examples/claude-code/CLAUDE.md`, `examples/hermes-agent/SKILL.md` | Annotation on [RT-BAP-agent-prompt](runtime.md#rt-bap-agent-prompt). Afforded external-agent use of returned text/files, not SDK context injection or observed compliance. |
| Evaluator read-back/rejection/cleanup | `sdk/tests/test_v025_features.py` (memory tests), `sdk/tests/test_session_cli.py` (compact tests), `benchmarks/messaging_bench.py` (preflight/trial/cleanup), `benchmarks/contention_bench.py` (durable verification and JSONL emission) | [MEM-RTE-evaluator-readback](#mem-rte-evaluator-readback). Sampled implementation, not exhaustive test audit; frozen numerical results and report-generation internals were not inspected, preventing numerical, report-consumer and benefit conclusions. |

## Core ideas

1. **Explicit read-back, not automatic context reconstruction.** Shared values, messages and downloaded files can reach later agent invocations through requested CLI calls. The shipped instructions request those calls; the storage SDK does not decide what enters a model window. [RT-BAP-agent-prompt](runtime.md#rt-bap-agent-prompt) and its annotation separate static instruction delivery from dynamic retained-content delivery.
2. **History, cursor and content serve different consumers.** Memory snapshots preserve submitted text and writer metadata. Mail cursors suppress previously listed records; they do not approve, summarize or delete content. Step status controls fixed polling rules; free-text handoff guidance has no corresponding inspected CLI content-reader. These distinctions prevent turning all bucket JSON into one undifferentiated knowledge store.
3. **Session transformations preserve or redact traces, not extract lessons.** File-backed adapters copy byte tails; Hermes serializes rows and decodes a content sentinel. Mirror regexes replace matched credential shapes; compact concatenates retained bytes. The later show consumer receives a decoded line tail, not a semantic summary or a restored host session. Checkpoint filenames are accepted as separate input transcripts, not interpreted as summary lineage. See [MEM-OBJ-session-parts](#mem-obj-session-parts).
4. **Trust and budget are mostly external.** Agent IDs, notes and values are caller-supplied. Bucket access, not an agent-specific content authority check, bounds visibility. Reads have key/prefix, newest-history, mailbox-cursor or session-tail selection, but no inspected relevance ranking or model-token budget. Physical persistence and structured rejection do not warrant text truth or agent uptake.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory-live
Label: Current shared memory value

Part of: [RT-RTE-memory-write](runtime.md#rt-rte-memory-write)

Source-native identity: `memory/<dot-key-as-path>.json`; a retained output of the parent route, distinct from its history output. Storage is a project-prefixed remote bucket. `value` is an arbitrary caller string, potentially natural-language content, symbolic text or serialized data; its semantic form cannot be determined from the CLI argument alone. The JSON envelope and lookup path are symbolic. Lineage is caller value plus code-added `set_by`/`set_at`, with model/human authorship unresolved. `memory get` returns value alone by default, dropping provenance from the display; `--with-meta` includes it. The SDK neither interprets nor verifies the value. A later external agent can interpret it if supplied as tool output; actual authority/compliance is unobserved. Same-key writes replace the live value; snapshots are a separate object with separate selection. SRC-1 implementation, `sdk/tracecraft/cli/memory.py`:

> doc = {
>     "value": value,
>     "set_by": cfg["agent_id"],
>     "set_at": now_iso(),
> }
> --- `sdk/tracecraft/cli/memory.py`

#### MEM-OBJ-memory-history
Label: Shared memory version snapshot

Part of: [RT-RTE-memory-write](runtime.md#rt-rte-memory-write)

Source-native identity: `memory/_history/<key-path>/<ts_ns>_<agent>_<uuid8>.json`. Symbolic bucket JSON wraps the same opaque/caller-text value, original key and writer metadata; this is a version copy, not derived knowledge or a reason for changing the value. Each CLI set writes the snapshot before live replacement. History lists only direct data leaves for the exact key, selects the newest positive limit (default 20; zero or negative bypasses that slicing), then prints selected values oldest first. Writer-clock ordering is not causal or global commit ordering. The display includes time/writer/value but not a semantic diff, approval or proof that the matching live write succeeded. No dedicated restore route is exposed by the inspected memory group; a caller could manually set a displayed old value. The history/live split refines the supplied route without duplicating it. SRC-1 implementation, `sdk/tracecraft/cli/memory.py`, `sdk/tracecraft/protocol.py`; the parent record supplies the write-order passage.

> hist_keys = sorted(direct_children(store.list_keys(prefix), prefix))
> if limit > 0:
>     hist_keys = hist_keys[-limit:]
> --- `sdk/tracecraft/cli/memory.py`

#### MEM-OBJ-message-content
Label: Retained direct and broadcast message

Part of: [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange)

Source-native identity: `messages/<recipient>/<append-key>.json`, including `_broadcast`. Storage is the project bucket. The symbolic envelope holds sender, recipient, timestamp and optional step; `message` is caller text consumed through human/model interpretation if delivered. This is communication content, not a trace-derived instruction revision. Inbox displays sender/time/direct-or-broadcast/optional-step/text, sorting fetched records by `sent_at`; it does not filter by step, extract reasons or merge a conversation into a summary. Sender attribution is caller config, not authentication. Full/new reads differ only in selection; `--delete` withdraws displayed direct records from later reads but preserves broadcasts. This object is distinct from the parent route's cursor, whose state has fixed software authority. SRC-1 implementation, `sdk/tracecraft/cli/messages.py`:

> if step_id:
>     doc["step"] = step_id
> store.put_json(append_key(f"messages/{recipient}/", sender), doc)
> --- `sdk/tracecraft/cli/messages.py`

#### MEM-OBJ-inbox-cursor
Label: Durable inbox read position

Part of: [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange)

Source-native identity: `messages/<agent>/_cursor.json`; symbolic bucket JSON containing direct/broadcast stream watermarks, seen-key arrays and update time. Derived automatically from listed keys after display, not from semantic understanding or acknowledgment by the recipient. `inbox --new` and status unread-count code consume it under fixed rules; it can suppress future displayed items and change unread counts. Ordinary full inbox ignores it. Five-minute grace and 1000-key seen cap bound replay/deduplication; own broadcasts can advance position without being displayed. Cursor write authority is software after a caller-requested read; concurrent readers with the same agent ID share and overwrite it. Reserved/nested leaves are excluded from mail and cursor poisoning. SRC-1 implementation, `sdk/tracecraft/cli/messages.py`, `sdk/tracecraft/protocol.py`, `sdk/tracecraft/cli/status.py`; the parent supplies the cursor-write passage.

> seen = [k for k in known if watermark is None or k > watermark]
> return {"watermark": watermark, "seen": seen[-SEEN_CAP:]}
> --- `sdk/tracecraft/protocol.py`

#### MEM-OBJ-handoff
Label: Structured step handoff

Part of: [RT-RTE-step-control](runtime.md#rt-rte-step-control)

Source-native identity: `steps/<sid>/handoff.json`, schema 2, project-bucket JSON. This is distinct from [RT-OBJ-step-state](runtime.md#rt-obj-step-state): state polling reads claim/status, not this document. `note` and `next_action` are optional caller text; routing/state/time fields are symbolic; optional `changed_files` is a symbolic path list from a fixed Git command, not a content diff or validated task result. Git failures and a non-repository return an empty list, so empty does not demonstrate no work. Original note reasons survive only if supplied; the code does not generate them. Completion overwrites the handoff with no CLI history. A bucket API caller can retrieve it, but no inspected shipped CLI command displays it, and `next_agent` does not dispatch it. The producer docstring's promised next-agent view is therefore not established as a wired read-back consumer. SRC-1 implementation and doctrine/design, `sdk/tracecraft/cli/steps.py`:

>     "next_action": next_action,
>     "note": note,
>     "created_at": now,
> }
> if changed_files_from_git:
>     handoff["changed_files"] = _git_changed_files()
> store.put_json(f"steps/{sid}/handoff.json", handoff)
> --- `sdk/tracecraft/cli/steps.py`

#### MEM-OBJ-artifact-file
Label: Shared artifact bytes

Part of: [RT-RTE-artifact-share](runtime.md#rt-rte-artifact-share)

Source-native identity: `artifacts/<normalized-step-or-shared>/<basename>`. Remote bucket file bytes are opaque to the SDK; format, original human/model/tool author, reasons and executable meaning depend on the uploaded file. A path/step label is symbolic addressing, not content relevance selection. Upload does not add writer metadata, snapshot history or redaction. Same-key upload replaces bytes; download reloads them to a requested local path. The Hermes skill affords a later agent download, but parsing/use is external and unobserved. Not interchangeable with the session parts: admission, transformation and consumers differ. SRC-1 implementation, `sdk/tracecraft/cli/artifacts.py`; the parent supplies upload evidence.

> dest = output or name
> if not store.exists(key):
>     raise click.ClickException(f"Artifact not found: {key}")
> store.get_file(key, dest)
> --- `sdk/tracecraft/cli/artifacts.py`

#### MEM-OBJ-session-parts
Label: Mirrored transcript part bytes

Part of: [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror)

Source-native identity: `sessions/<harness>/<session-id>/part-NNNNN-<uuid8>.jsonl`, remote bucket files. They contain mixed host trace payload, potentially natural-language turns, symbolic events, tools and opaque multimodal fields; a JSONL extension is not proof that every chunk is independently parseable or that all reasoning is recorded. File adapters tail bytes without parsing content or waiting for complete lines. Hermes selects message rows, decodes sentinel-prefixed `content` JSON, leaves tool/reasoning JSON strings as-is and serializes all row columns. This is a source-format conversion, not abstraction into lessons. Host trace can contain already-derived host checkpoints; Tracecraft's OpenClaw adapter surfaces topic and checkpoint files as separate transcripts without resolving predecessor lineage. Host model, human, tool and compaction origins remain local uncertainties, not inferred from an adapter name. SRC-1 implementation, `sdk/tracecraft/harness/base.py`, `sdk/tracecraft/harness/hermes.py`, `sdk/tracecraft/harness/openclaw.py`:

> for p in self.root.glob("*/sessions/*.jsonl"):
> --- `sdk/tracecraft/harness/openclaw.py`

> if "content" in d:
>     d["content"] = _decode_content(d["content"])
> --- `sdk/tracecraft/harness/hermes.py`

Mirror optionally regex-redacts each new chunk, then retains transformed bytes. Later `session show --tail` concatenates matching parts, splits lines and decodes UTF-8 with replacement; the printed display is not identical to an arbitrary byte payload. Default show displays metadata only. Normal-path compact concatenates stored bytes, not a semantic summary; it keeps no newly inferred theory, reason or instruction. Storage retention gives an explicit inspection channel, not automatic host restoration or changed agent behavior. SRC-1 implementation, `sdk/tracecraft/cli/session.py`, `sdk/tracecraft/redact.py`; [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror) supplies redaction evidence.

> lines = body.splitlines()
> click.echo("\n--- tail ---")
> for line in lines[-tail:]:
>     try:
>         click.echo(line.decode("utf-8", errors="replace"))
> --- `sdk/tracecraft/cli/session.py`

#### MEM-OBJ-session-meta
Label: Session retention metadata

Part of: [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror)

Source-native identity: `sessions/<harness>/<session-id>/meta.json`, symbolic remote bucket JSON. Derived from source descriptor, config, flush cursors, byte lengths, regex counts and prior metadata. List/show/status/receipts consume metadata for descriptions, sorting and totals; this is access/audit information, not transcript content. A metadata entry can be lost or stale under separate-write failure or multiwriter overwrites. Tail lists actual matching files rather than treating `parts` as an authoritative manifest. Compact replaces old per-flush entries with one merged count/length/time entry and surviving tail entries: original per-target cursor ranges, UUIDs and per-part redaction counts do not persist in the replacement manifest. Cumulative top-level counts remain. Thus payload order preservation does not establish preservation of detailed provenance. SRC-1 implementation, `sdk/tracecraft/cli/session.py`, `sdk/tracecraft/protocol.py`:

> merged_entry = {
>     "seq": 0,
>     "uuid": uniq,
>     "compacted_from": len(targets),
>     "uploaded_bytes": len(body),
>     "uploaded_at": _now_iso(),
> }
> meta["parts"] = [merged_entry] + sorted(surviving, key=lambda p: p.get("seq", 0))
> --- `sdk/tracecraft/cli/session.py`

#### MEM-OBJ-mirror-state
Label: Local mirror cursor checkpoint

Part of: [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror)

Source-native identity: `~/.tracecraft/mirror-state/<session-id>.json`, symbolic local JSON. Software saves harness/session/source-path/cursor/sequence/time after part and metadata writes. The next mirror reads cursor only; it does not validate the stored harness or source path against the currently selected source. Its pathname is keyed by session ID alone, not project/bucket/harness. Reusing an ID in another destination or harness can therefore reuse an unrelated cursor; actual collisions are unobserved. File cursors are byte offsets, Hermes cursors highest consumed message IDs. Stop removes this access checkpoint and records end time, not the transcript; missing/corrupt state restarts at zero. This can duplicate retained bytes while sequence discovery avoids ordinary same-name reuse. Local checkpoint has fixed authority over subsequent ingestion, not semantic authority over an agent. SRC-1 implementation, `sdk/tracecraft/cli/session.py`:

> def _state_path(session_id: str) -> Path:
>     return STATE_DIR / f"{session_id}.json"
> --- `sdk/tracecraft/cli/session.py`

> state = _load_state(sess.session_id)
> cursor = state.get("cursor", 0)
> --- `sdk/tracecraft/cli/session.py`

#### MEM-OBJ-agent-registration
Label: Retained agent registration

Part of: [RT-RTE-init-config](runtime.md#rt-rte-init-config)

Source-native identity: `agents/<agent>.json`, symbolic bucket JSON. Init writes caller/default identity, active status, null step, timestamps and initialized summary. Agents/status later display ID/status/step/heartbeat-age; they do not display the summary or prove process liveness. `collect_agents` computes stale after 300 seconds. Within inspected CLI dispatch, claims/completions/mirroring do not update this registration heartbeat or step; a direct store caller could. Thus it is durable registration plus computed age, not a reliable live scheduler state. It differs from [RT-OBJ-config](runtime.md#rt-obj-config), which is local credentials and command attribution. SRC-1 implementation, `sdk/tracecraft/cli/init_cmd.py`, `sdk/tracecraft/cli/agents.py`, `sdk/tracecraft/protocol.py`, `sdk/tracecraft/cli/status.py`:

> "heartbeat": now,
> "summary": "Initialized",
> --- `sdk/tracecraft/cli/init_cmd.py`

### Routes

#### MEM-RTE-evaluator-readback
Label: Evaluate durable storage read-back

Distinct identity: this is the sampled developer evaluation plane, not ordinary agent mail consumption [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange), task coordination [RT-RTE-step-control](runtime.md#rt-rte-step-control), or package publication [RT-RTE-package-release](runtime.md#rt-rte-package-release). It uses their storage wrappers/contracts but does not belong to exactly one supplied route.

Owner/progression: developer initiation selects test/benchmark and settings; fixed evaluator code proposes fixture messages or competing claims, reads retained results through a fresh client, compares against expected distinct bodies or exactly-one-winner/stored-owner criteria, and cleans temporary bucket objects. Contention rejects invalid trials or marks low-concurrency exclusions and writes trial fields to requested local JSONL. These expected counts/owner agreement are answer oracles for storage evaluation, not oracles for message truth or coding success. Tests compare CLI output and state against fixture expectations. Mode is bounded developer evaluation. Human judgment on results and package admission is unresolved; no source-inspected path here automatically turns evaluation rows into a live memory policy or instruction revision. Guidance is fixed evaluator rules; retained output is trial/result data, not automatically adopted criticism. Numerical frozen output and downstream report-generation code were not read.

- Immediate return: test assertions or benchmark measurements/result dictionaries and printed sweep context; no evaluated run was performed here.
- Later read-back: fresh verifier clients retrieve bucket messages/claims after writes in the evaluator invocation; optional local trial JSONL persists, but its later report consumer is uninspected — report-generation internals were not examined.
- Delegated visibility: temporary bucket results visible to holders of project credentials; local output visibility depends on caller filesystem and is uninspected.
- Selection predicate: benchmark-specific recipient or trial key; count message bodies or read stored claim owner; contention excludes simultaneous trials whose barrier spread exceeds selected bound.
- Invalidation or expiry: cleanup deletes test/trial objects; optional local result files survive separately; deletion failures can be tolerated, not proof of complete cleanup.
- Activation or effect: fixed evaluator comparisons set result/error/invariant/exclusion fields; automatic changes to deployed memory or model behavior are not established.
- Evidence limits: sampled evaluator source only; no executed tests, independently assessed numerical rows, later report reads or causal benefit evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 implementation, `benchmarks/messaging_bench.py`, `benchmarks/contention_bench.py`, `sdk/tests/test_v025_features.py`, `sdk/tests/test_session_cli.py`:

> bodies = set()
> for k in keys:
>     doc = verifier.get_json(k)
>     if doc and "message" in doc:
>         bodies.add(doc["message"])
> --- `benchmarks/messaging_bench.py`

> t.invariant_held = (
>     t.valid and win_count == 1 and t.stored_owner == t.declared_winner
> )
> --- `benchmarks/contention_bench.py`

> line = json.dumps(row)
> if out:
>     out.write(line + "\n")
> --- `benchmarks/contention_bench.py`

### Claims

#### MEM-CLM-history-immutability
Label: Claimed immutable memory history

Distinct claim with no supplied claim counterpart: [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) already describes nontransactional snapshots but does not declare this stronger source assertion. SRC-1 doctrine/design, `sdk/tracecraft/cli/memory.py`:

> Every set also appends an immutable snapshot under memory/_history/, so
> the current value is last-write-wins but no version is ever lost. See
> `memory history`.
> --- `sdk/tracecraft/cli/memory.py`

Implementation supports append-shaped unique keys and reserved CLI set namespace, not enforced immutability, complete prior provenance or universal no-loss. An initially direct-written live value is not snapshotted retrospectively. A snapshot can survive a failed live write; direct backend writes can replace/delete it or change live memory without any snapshot. Writers can be concurrent, and service retention policy is excluded. The precise claim is therefore bounded to the normal CLI set path's attempted write trail, not an immutable knowledge audit. SRC-1 implementation, `sdk/tracecraft/s3.py`, `sdk/tracecraft/hf.py`; [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) supplies write-order evidence.

> def delete(self, key):
>     try:
>         self.client.delete_object(Bucket=self.bucket, Key=self._key(key))
> --- `sdk/tracecraft/s3.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-config](runtime.md#rt-obj-config)

Memory consumers: every command reloads config; project/backend/bucket choose the storage namespace, agent ID chooses attribution and inbox/cursor selection. This is persistent access/configuration state, not accumulated task knowledge. Local config precedence and environment override allow context to change without a content revision. SRC-1 implementation, `sdk/tracecraft/config.py`; supplied record contains the override passage. Its credentials are not the provenance of the semantic values it addresses.

#### On [RT-OBJ-step-state](runtime.md#rt-obj-step-state)

Lineage: CLI claim and caller-selected completion state become symbolic documents; status consumers use fixed equality/branch rules. This part has software authority independent of the separately retained note's interpretation. `needs_review` keeps the waiter polling and `blocked` raises; neither state invokes a semantic reviewer. Clearing either through later completion is allowed by the same ownership/force policy, without distinct-reviewer approval. SRC-1 implementation, `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/protocol.py`; [RT-BAP-step-polling](runtime.md#rt-bap-step-polling) supplies polling evidence.

#### On [RT-RTE-memory-write](runtime.md#rt-rte-memory-write)

Write agency/admission: software wraps the caller's value and makes both writes after key checks; human versus model author/editor/approval remains unresolved. No correctness oracle, model synthesis or automatic lesson extraction is invoked. Reasons persist only inside supplied value text. Read-back is request-led: exact key get returns live content, prefix list returns addresses only, history returns selected past content with writer/time. History count is a version budget, not a token budget; value display has no semantic ranking. SRC-1 implementation, `sdk/tracecraft/cli/memory.py`, `sdk/tracecraft/protocol.py`; the parent supplies ordering evidence, and [MEM-OBJ-memory-live](#mem-obj-memory-live) / [MEM-OBJ-memory-history](#mem-obj-memory-history) split consumers and provenance.

#### On [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange)

Memory consumers: explicit inbox requests reload retained text; `--new` automatically selects from current reader cursor, but is still requested delivery, not independent push to a model. Selector inputs are configured agent ID, direct and broadcast keys, watermark/seen sets and own-broadcast suppression. Selected text reaches stdout with no token/count budget. Prefix/leaf hygiene excludes reserved/nested objects; cursor advancement reflects listed keys even if omitted from display. Full inbox is the alternate reload route; `--delete` destroys only displayed direct messages. No substantive triage/acceptance occurs. SRC-1 implementation, `sdk/tracecraft/cli/messages.py`, `sdk/tracecraft/protocol.py`, `sdk/tracecraft/cli/status.py`; parent and [MEM-OBJ-inbox-cursor](#mem-obj-inbox-cursor) supply passages. Status supplies counts, not mailbox content or actual reading acknowledgment.

#### On [RT-RTE-step-control](runtime.md#rt-rte-step-control)

Memory consumers: requested status/wait reads select normalized IDs and receive fixed states. They do not read note/next-action/changed-files. Retained handoff is separately addressable, not automatically delivered to the next agent. Status is written before handoff, so successful wait is not evidence that handoff content is present. Software rejects incompatible flags/owner mismatch unless force; human versus model completion judgment remains unresolved, and substantive task quality is not checked. SRC-1 implementation, `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/protocol.py`; parent and [MEM-OBJ-handoff](#mem-obj-handoff) provide passages. The docstring says:

> The handoff record is what the next agent sees instead of a shared
> conversation — so it carries machine-checkable state, not just a note.
> --- `sdk/tracecraft/cli/steps.py`

That declared intention does not identify a shipped content reader. The source-inspected consumers establish machine-checkable status separately, not next-agent uptake of this whole record.

#### On [RT-RTE-artifact-share](runtime.md#rt-rte-artifact-share)

Read-back is caller-requested exact addressing; code loads the entire file to disk, not selected semantic excerpts to a model. The selection inputs are name/step/output destination; storage does not set a model context budget. The Hermes skill supplies an afforded agent consumer role but no deployed wiring or downstream parsing. Material editing/adoption is reupload of same-key bytes; no history or semantic review is added. SRC-1 implementation, `sdk/tracecraft/cli/artifacts.py`; doctrine/design, `examples/hermes-agent/SKILL.md`; [MEM-OBJ-artifact-file](#mem-obj-artifact-file) retains the reload passage.

#### On [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror)

Trace origin and curation: bytes/rows originate in external host files/database; their full human/model/tool/host-compaction provenance is not authenticated by Tracecraft. After caller initiation, software chooses each delta by cursor, optionally replaces matched credential shapes and retains payload/meta/local checkpoint. No per-content human approval is established. Host rows may already carry reasoning or summaries, but Tracecraft does not convert them into durable behavior-shaping guidance.

Read-back consumers are requested list/show/status, not an enclosing model loop. List selects metadata by harness, sort recency/size and default limit 20; show selects first matching metadata across harness folders. Positive tail downloads all matching parts before selecting the last N lines; output limit does not bound download memory or model tokens. The returned metadata precedes the tail. Stop marks end but removes only local state and does not kill a running follow loop. SRC-1 implementation, `sdk/tracecraft/cli/session.py`, the four adapter paths in coverage, `sdk/tracecraft/redact.py`; parent and [MEM-OBJ-session-parts](#mem-obj-session-parts), [MEM-OBJ-session-meta](#mem-obj-session-meta), [MEM-OBJ-mirror-state](#mem-obj-mirror-state) supply passages.

#### On [RT-RTE-session-compact](runtime.md#rt-rte-session-compact)

Curation and lineage: caller initiates fixed byte concatenation after layout checks; no semantic answer oracle or model criticism is involved. Payloads normally preserve ordering, but replacing metadata loses target-specific flush lineage as described in [MEM-OBJ-session-meta](#mem-obj-session-meta). Keep-tail preserves newest N objects, not newest N model turns or tokens. Show reloads listed files, so interrupted deletion can display duplicates, not merely leave inert extra copies. The source calls this duplicate harmless, but the tail consumer reads it. SRC-1 implementation and doctrine/design, `sdk/tracecraft/cli/session.py`; the parent supplies safe-ordering passage.

#### On [RT-BAP-agent-prompt](runtime.md#rt-bap-agent-prompt)

This static instruction is not itself read-back memory accumulated through use. It affords external-agent requests that later return dynamic memory/mail/files; its interpreted authority and loading are external. In particular, Hermes post-write verification requests checking storage visibility, not truth, correctness or successful action by a recipient. SRC-1 doctrine/design, `examples/hermes-agent/SKILL.md`, `examples/claude-code/CLAUDE.md`:

> After any action, verify with the corresponding read command:
> - After `memory set` → `memory get`
> - After `send` → ask the recipient to check `inbox`
> - After `claim` → `step-status`
> --- `examples/hermes-agent/SKILL.md`

## Write side

**Caller-authored coordination content.** [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange), [RT-RTE-step-control](runtime.md#rt-rte-step-control) and [RT-RTE-artifact-share](runtime.md#rt-rte-artifact-share) accept caller strings/state/files subject to different structural/path/ownership checks. Author, editor and substantive approver can be human, model or other software; config attribution does not resolve them. Software physical I/O is established. A command invocation is not per-content human approval. There is no semantic admission test on these inspected CLI paths. Claim arbitration and `needs_review` constrain task state, not knowledge truth. The shipped prompt requests progress sharing and notes; it neither enforces reason retention nor selects a theory to adopt.

**Transformation and maintenance.** [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror) acquires host tails or Hermes rows, converts rows to JSONL where applicable, optionally redacts, uploads parts, updates meta and saves local cursor. This raw/host-derived input → transformed retained trace → requested display chain does not produce a new behavior-shaping memory artifact. [RT-RTE-session-compact](runtime.md#rt-rte-session-compact) merges bytes and replaces the manifest; it does not formulate lessons, criticize text or shorten a model window. Host checkpoint forms remain possible already-derived input with unresolved original derivation. Original reasons survive only to the extent that a host recorded them, redaction did not remove them and tail selection displays them; full reasoning completeness is not established.

**Rejection and withdrawal.** Invalid memory keys/recipient paths and step identifiers are rejected before relevant content writes; claims can reject existing ownership, complete can reject mismatched owners or incompatible flags, and compact rejects negative keep-tail. Service failures propagate; ordered multiobject writes are not transactions. Memory live replacement, handoff/status overwrite and artifact reupload change later content; snapshots and mail ordinarily remain. Inbox deletion removes direct messages, while full reload can recover cursor-hidden retained mail. Compact deletes original part files only after merged upload/meta. Stop deletes local cursor, leaving retained transcript and potentially enabling replay. Direct store deletes/overwrites bypass CLI admission/history/redaction. See [MEM-CLM-history-immutability](#mem-clm-history-immutability), [RT-CLM-mirror-idempotence](runtime.md#rt-clm-mirror-idempotence) and [RT-CLM-secret-redaction](runtime.md#rt-clm-secret-redaction).

**Evaluation.** [MEM-RTE-evaluator-readback](#mem-rte-evaluator-readback) traces temporary storage results into fixed checks and optional durable trial JSONL; cleanup removes underlying trial objects. Invalid/excluded measurements can remain marked in output rows rather than disappearing. The sampled memory tests check latest/history display; compact tests compare reconstructed tail before/after. These are contract checks with synthetic inputs, not empirical evidence of agent learning. No inspected mechanism here consumes trial results automatically to revise shared memory, host context policy or model parameters; later report/adoption judgment remains uninspected.

## Read-back

Every established dynamic content route here begins with a caller's request. Follow continuously writes traces, but does not independently supply them into a model invocation. Automatic selection *within* a requested read (mail grace filtering, history limit, session tail) is not a push route.

| Retained part | Later consumer, selection and channel | Authority and budget |
|---|---|---|
| Current value/history | `memory get` exact key; `history` exact-key direct leaves and newest limit; stdout | SDK treats value as data; human/model interpretation is afforded externally. Default get omits writer metadata. Version count only, no token budget. |
| Mail/content and cursor | Inbox configured recipient + broadcasts; full/new rules and own-broadcast exclusion; stdout. Status uses cursor for unread counts only. | Cursor has fixed selection authority; text has no SDK execution authority. No message-body budget. Late arrival and shared-cursor limits remain. |
| Claim/status | step-status, status and wait-for normalize IDs and resolve status/claim | Fixed branching over symbolic state; not work verification. Wait completion does not deliver handoff text. |
| Handoff | Direct backend GET capacity; producer text names next agent but no inspected CLI content reader | Consumer route wiring unresolved; stored recipient is not dispatch or selection of content for that recipient. |
| Artifact bytes | Requested download by name/step to disk; shipped instruction affords agent use | Arbitrary file content; parsing/execution uninspected, full-file reload. |
| Transcript/meta | List/show/status; metadata harness/sort/limit and first matching ID; optional all-parts download then line tail to stdout | Inspection output, not restoration/injection. Line limit, no semantic/token selection. Meta totals are not payload completeness checks. |
| Local mirror state | Subsequent mirror consumes cursor; remote listing supplies next sequence | Fixed ingestion suppression/recovery authority; state removal restarts source read. Not a model memory. |
| Registration/config | Agents/status and each command | Symbolic access/attribution/status display; not authenticated liveness or content trust. |

All rows are supported by SRC-1 implementation at the table's production paths and the declared objects/route annotations above. Shipped read commands and external-agent role are grounded by [RT-BAP-agent-prompt](runtime.md#rt-bap-agent-prompt). Calling storage methods with an unspecified hypothetical caller is only capability, not a proven next-agent route.

**Working-context control boundary.** The inspected target provides requested access to retained material, filtering what its CLI displays. It does not implement host sub-agent isolation, turn eviction, semantic summarization or token-window reconstruction in these routes. Those host responsibilities were excluded, so no conclusion about their presence or absence in the external agents follows. Session compact is storage-layout compaction, not removal of old turns from a model-visible context. Tail leaves the full remote transcript reachable through larger reads or file API access but displays only a selected line tail; it provides no in-window pointer that a model automatically dereferences. The stack-frame analogy has no inspected target frame to map here. External removed context can be manually inspected through retained transcript reads, but no automatic reload into the original host conversation is established.

## Integration issues

- **Handoff consumer unresolved:** [MEM-OBJ-handoff](#mem-obj-handoff) refines [RT-RTE-step-control](runtime.md#rt-rte-step-control) and [RT-OBJ-step-state](runtime.md#rt-obj-step-state). SRC-1 `sdk/tracecraft/cli/steps.py` promises what a next agent sees, yet dispatch/status/wait do not load handoff content. Runtime correctly calls it separately addressable; do not promote this to wired next-agent context delivery. A shipped content-reader or documented specific GET procedure is missing; API capacity and static advice do not close that gap.
- **Compaction provenance and duplicate significance:** [MEM-OBJ-session-meta](#mem-obj-session-meta) adds loss of per-target flush lineage to [RT-RTE-session-compact](runtime.md#rt-rte-session-compact). Runtime's byte-layout characterization remains valid, but it should not imply unchanged metadata. SRC-1 `sdk/tracecraft/cli/session.py` replaces entries and show reads file listings; interrupted duplicate copies can alter displayed tail. Detailed lineage and interrupted equivalence cannot be claimed.
- **Cursor scope:** [MEM-OBJ-mirror-state](#mem-obj-mirror-state) adds cross-project/harness destination ambiguity to [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror). SRC-1 `sdk/tracecraft/cli/session.py` keys local state only by session ID and uses cursor without identity validation. Actual ID collisions are unknown; independent cursor use is conditional on distinct IDs and stable destination/source, not a universal project-isolation guarantee.
- **Strong history claim:** [MEM-CLM-history-immutability](#mem-clm-history-immutability) qualifies source wording using SRC-1 `sdk/tracecraft/cli/memory.py`, `sdk/tracecraft/s3.py`, `sdk/tracecraft/hf.py`. [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) is already bounded correctly. Reconciliation should retain append history capacity without adopting enforced immutability or prior-value completeness.
- **Registration vs live status:** [MEM-OBJ-agent-registration](#mem-obj-agent-registration) adds that inspected CLI routes do not refresh init heartbeat/step; SRC-1 `sdk/tracecraft/cli/init_cmd.py`, `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/cli/session.py`, `sdk/tracecraft/protocol.py`. Runtime already distinguishes staleness from liveness. Direct writers are possible; observed live heartbeat maintenance is unestablished.
- **Alternative trace provenance:** [MEM-OBJ-session-parts](#mem-obj-session-parts) includes OpenClaw checkpoint/topic inputs and Hermes row conversion under [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror). SRC-1 adapter implementation establishes ingestion, not complete original conversation or reason lineage. External checkpoint derivation, row pruning and host semantic use remain unknown.
- **Evaluator consumer scope:** [MEM-RTE-evaluator-readback](#mem-rte-evaluator-readback) has no supplied route counterpart; it overlaps wrappers used by [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange) and [RT-RTE-step-control](runtime.md#rt-rte-step-control), not their ordinary caller routes. Local trial rows and source-defined checks are established; frozen numerical results/report-generation and automatic adoption are uninspected.
- **Record identity:** all other new objects declare an explicit part relation to one supplied route because the supplied baseline declared the route, not these separate material outputs. They are not replacement routes or duplicate [RT-OBJ-step-state](runtime.md#rt-obj-step-state) / [RT-OBJ-config](runtime.md#rt-obj-config). No same-referent new declaration was identified after comparison. Supplied route identities and generic fields were not re-declared.

## Limitations and checks

The frozen checkout HEAD was rechecked as 97c6b7447f8e696f0116357d9f86bb0ece25e5b1 and its status was clean. Input types, complete boundary/runtime members, worker rules and record contract were read; report identity matches the invocation and boundary. All conclusions are bounded to SRC-1 and this attempt's direct/source-supplied evidence. Production path inspection covers the routes, not a deployed run or exhaustive security audit. Method contracts are the supplied worktree versions; no method-history or unrelated run state was consulted.

No source inaccessible production branch was identified. Initial content authorship, actual bucket grants/retention, host trace completeness, host prompt loading, downstream content interpretation, handoff reader wiring, checkpoint derivation and observed benefit are not established. Available but uninspected evaluator output/report code prevents independent numerical and downstream-evaluation conclusions, not the source-grounded storage account. Source labels such as immutable, safe/idempotent and harmless duplicates were challenged against direct write/delete/order/read paths. Deterministic validation checks form, identities, relations and quotation occurrence; it does not establish the analytical claims or observed operation.

Validation: completed with the invocation's `commonplace-run validate-output` command; findings repaired until it passes.
