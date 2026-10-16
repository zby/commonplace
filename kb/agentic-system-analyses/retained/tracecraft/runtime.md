---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Tracecraft runtime baseline: bucket-backed coordination, session mirroring and shipped change paths at the frozen SDK revision."
run-id: AAS-2026-10-14-tracecraft-9c4af961e8e2-01
reviewed-boundary: "97c6b7447f8e696f0116357d9f86bb0ece25e5b1"
---

# Tracecraft runtime report

## Runtime account

Tracecraft executes storage and coordination commands, not the agent's model loop. Its installed `tracecraft` entry point dispatches Click commands for initialization, memory, messages, steps, artifacts, sessions and status. A shipped agent prompt tells an external host's agent when to call them. The prompt's delivery and compliance are separate from the SDK's fixed command rules. This account uses SRC-1 implementation and doctrine/design at the [boundary](boundary.md). No target execution was performed and no agent trace was supplied; operation, activation in model behavior and benefit remain unobserved. All paths below are commit-relative SRC-1 anchors. Added inspection covers the complete adapters, status aggregation, shipped Hermes instructions and CI/release workflows; no new source identity is introduced.

### Ordinary coordination invocation

The ordinary shipped loop starts with a caller configuring a bucket, project and agent through [RT-RTE-init-config](#rt-rte-init-config). Local config wins over global config; `TRACECRAFT_AGENT` can replace the recorded agent ID on each command. Identity is therefore caller-supplied attribution, not proof of a distinct authenticated agent. Bucket credentials are the service principal; the project is a key prefix. Configuration stores credentials and is chmodded to 0600. Init writes it before checking bucket access, so failed initialization can leave usable-looking configuration (SRC-1, `sdk/tracecraft/config.py`, `sdk/tracecraft/cli/init_cmd.py`).

The external agent checks registered peers and inbox, claims a step, performs work outside Tracecraft, shares state, and completes with a handoff. The host or human owns the next action; the SDK does not autonomously schedule the external work. [RT-BAP-agent-prompt](#rt-bap-agent-prompt) supplies the instruction channel. [RT-RTE-step-control](#rt-rte-step-control) supplies the symbolic task-state policy and completion output. Claim maps a normalized ID to a conditional claim object, then writes status; the later `step-status`, `status` and `wait-for` consumers resolve stored state. `wait-for` returns only when all specified states equal `complete`, reports review-needed state, fails immediately on blocked state and otherwise polls every five seconds until timeout. The note and next-action text are persisted but are not executed or substantively verified by the step machinery (SRC-1, `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/protocol.py`).

Progress, messages and files cross separate admission paths: [RT-RTE-memory-write](#rt-rte-memory-write), [RT-RTE-mail-exchange](#rt-rte-mail-exchange) and [RT-RTE-artifact-share](#rt-rte-artifact-share). Their immediate terminal outputs are CLI receipts or printed/downloaded data, not changes to an external model's context by themselves. The shipped Hermes skill instructs matching read commands after writes; the agent remains responsible for interpreting results (SRC-1, `examples/hermes-agent/SKILL.md`). `agents` and `status` are read-only views. The five-minute stale label is computed from stored heartbeat age, not observed process liveness. Status aggregates separate listings and GETs, not a transactional snapshot (SRC-1, `sdk/tracecraft/cli/agents.py`, `sdk/tracecraft/cli/status.py`, `sdk/tracecraft/protocol.py`).

### Ordinary session-retention invocation

An independent human, cron job or host-agent command starts [RT-RTE-session-mirror](#rt-rte-session-mirror). Registry code selects an adapter, which discovers existing host records; latest file modification time selects the active file-backed session unless a specific ID is requested. Claude Code discovery is cwd-scoped. Codex, OpenClaw and Hermes ignore cwd: `--all` for these adapters means their entire discovered set, not project isolation. OpenClaw adds an agent prefix to the session ID. Hermes selects the session owning the newest message ID, with newest-session fallback (SRC-1, `sdk/tracecraft/harness/claude_code.py`, `sdk/tracecraft/harness/codex.py`, `sdk/tracecraft/harness/openclaw.py`, `sdk/tracecraft/harness/hermes.py`).

A flush reads a local cursor, checks end-of-stream, consumes a delta, optionally redacts bytes, uploads a unique transcript part, overwrites cumulative metadata and finally saves the consumed cursor. JSONL file adapters return bytes and byte offsets; Hermes returns synthesized row JSONL and the highest row ID consumed. Its SQLite connection uses `mode=ro`; the mirror does not write the host database. The next-step policy is code: one-shot returns, follow sleeps and repeats against one resolved session, follow-all rediscovers every cycle. KeyboardInterrupt stamps end metadata. Ordinary errors propagate rather than forming a supervised retry loop. Local temporary files are removed in finally blocks (SRC-1, `sdk/tracecraft/cli/session.py`, `sdk/tracecraft/harness/base.py`, `sdk/tracecraft/harness/hermes.py`).

Later `session list` reads metadata; `session show --tail N` finds the first matching session metadata across harness folders, downloads every matching part in lexical order, concatenates bytes and prints the last N lines. It does not reconstruct a running host conversation or choose content for a model. [RT-RTE-session-compact](#rt-rte-session-compact) changes storage layout, not semantic content: byte concatenation is not model-context summarization. Host context trimming, isolated sub-agent windows and reloading into a model remain outside this source boundary. Here the explicit context controls are data selection at CLI reads; whether an external host inserts the returned text into a model window is uninspected (SRC-1, `sdk/tracecraft/cli/session.py`).

### Forcing cases and guarantee coverage

Four implementation forcing cases were inspected; none was executed.

| Case | Owner, enforcement and strength | Coverage and countercase | Bounded conclusion |
|---|---|---|---|
| Contended claim, including HF | CLI requests conditional write; S3 wrapper sends `IfNoneMatch=*`; service owns atomic arbitration. Strength: protocol requiring a deployment contract. | S3 claim write only, if service correctly implements conditional PUT. HF uses exists-then-write, so both writers can pass. Completion is a later ordinary overwrite. | implementation conclusion status: wired. operation conclusion status: uninspected. Atomic arbitration is not a backend-independent guarantee. SRC-1, `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/s3.py`, `sdk/tracecraft/hf.py`. |
| Alternate principal and direct store path | Completion checks the claim's agent string. Strength: policy. | `--force` bypasses mismatch rejection; no claim also permits completion. Config/env can choose the same ID. Direct wrapper writes can replace claim, status, history or handoff without CLI validation. | implementation conclusion status: wired. operation conclusion status: uninspected. Ownership is cooperative CLI discipline, not access isolation. SRC-1, `sdk/tracecraft/config.py`, `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/s3.py`, `sdk/tracecraft/hf.py`. |
| Late mail and cursor failure | Inbox writes cursor after printing; protocol relists a trailing five-minute window and retains at most 1000 seen keys. Strength: best effort. | Full inbox ignores cursor; `--delete` destroys direct messages but not broadcasts. A sufficiently late arrival can fall behind watermark; cap overflow can permit repeats. Concurrent same-ID readers are not arbitrated. | implementation conclusion status: wired. operation conclusion status: uninspected. Post-print advancement reduces crash skips but does not establish unconditional exactly-once or at-least-once delivery. SRC-1, `sdk/tracecraft/cli/messages.py`, `sdk/tracecraft/protocol.py`. |
| Mirror/compact interruption and alternate upload | Mirror writes part, meta, then local cursor; compact uploads merged copy and updates meta before deleting originals. Strength: best effort. | Failed meta/cursor write can cause repeated mirror bytes; missing/corrupt local state starts at zero. Interrupted compact leaves both merged and original objects, and show lists both. No multiwriter lock protects metadata. Artifact/direct store uploads bypass redaction; mirror allows `--no-redact`. | implementation conclusion status: wired. operation conclusion status: uninspected. Ordering favors retaining copies, not exact-once replay or universal secret removal. SRC-1, `sdk/tracecraft/cli/session.py`, `sdk/tracecraft/cli/artifacts.py`, `sdk/tracecraft/redact.py`. |

The claim/status crash case has a narrower enforcement point: `effective_status` and its listing variant use claim ownership only when no status is found. They therefore cover a claim written before an absent status, not arbitrary inconsistent pre-existing status. Complete writes status before handoff; a downstream waiter can see complete before the handoff is available. Those are separate objects, not an atomic transaction (SRC-1, `sdk/tracecraft/protocol.py`, `sdk/tracecraft/cli/steps.py`).

Capability surface is bucket JSON/file read, write, list and delete, plus local transcript access and a fixed optional `git diff --name-only HEAD` subprocess. The current credential grant and deployed isolation envelope are not supplied. Project prefixes and agent tags are not service authorization boundaries. SDK code makes no per-command human approval request; starting a command does not prove human approval of each content item. External hosts may add approvals or sandboxing, but these cannot be attributed to Tracecraft. Direct model calls, provider-native tools and remote reasoning workers belong to those excluded hosts; they are not necessary to the inspected storage paths (SRC-1, `sdk/tracecraft/s3.py`, `sdk/tracecraft/hf.py`, `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/store.py`).

### Change admission and mutability

Retained-content writes accept caller values or file bytes after local structural checks, not correctness review. Claims arbitrate task ownership, not the quality of the work. `--needs-review` stores a state that prevents `wait-for` success; it does not invoke a reviewer or require a distinct reviewer to clear it. Model/human authorship of individual values remains unresolved. Memory revision semantics are left to the memory analyst; this report establishes the control paths only.

Adapter additions require Python source plus a registry entry; CLI choices derive from the registry. The shipped capability-change path is source/package revision, not runtime model-authored plugin loading. [RT-RTE-package-release](#rt-rte-package-release) builds and publishes a release-selected revision. CI declares test and lint jobs, but the release workflow does not itself run the test suite, and branch protection or release authorization policy is not supplied (SRC-1, `sdk/tracecraft/harness/__init__.py`, `.github/workflows/ci.yml`, `.github/workflows/release.yml`). No inspected route calls a model or uses weights/embeddings; there is no distributed-parametric component to declare for these SDK routes. Model version fixity and training in external hosts remain uninspected, not claims about their absence.

## Shared records

### Components

#### RT-CMP-get-store
Label: Storage backend factory

Source-native identity: `get_store`; symbolic Python dispatch over JSON configuration. Substrate: installed source and local config, with remote bucket state in the returned backend. S3 is the default; HF is selected only by the `hf` value. It returns the backend plus config and performs no CLI schema or ownership checks itself. SRC-1 implementation, `sdk/tracecraft/store.py`:

> backend = cfg.get("backend", "s3")
> --- `sdk/tracecraft/store.py`

#### RT-CMP-harness-registry
Label: Harness adapter registry

Source-native identity: `REGISTRY`, a symbolic mapping from harness names to Python adapter classes, stored in package source. It contains Claude Code, Codex, OpenClaw and Hermes, not every host named in its docstring. `HARNESS_CHOICES` derives from it; `get_harness` instantiates the selected class with no arguments. SRC-1 implementation, `sdk/tracecraft/harness/__init__.py`, `sdk/tracecraft/cli/session.py`:

> HARNESS_CHOICES = sorted(REGISTRY)
> --- `sdk/tracecraft/cli/session.py`

### Operative objects

#### RT-OBJ-config
Label: Local configuration

Source-native identity: `.tracecraft.json` or `~/.tracecraft/config.json`. Symbolic JSON fields select credentials, backend, bucket, project and agent; substrate is local disk. Local precedence and process override mean the caller controls attribution independently of backend credentials. SRC-1 implementation, `sdk/tracecraft/config.py`:

> agent_override = os.environ.get("TRACECRAFT_AGENT")
> if agent_override:
>     cfg["agent_id"] = agent_override
> --- `sdk/tracecraft/config.py`

#### RT-OBJ-step-state
Label: Claim and status documents

Source-native identity: `steps/<sid>/claim.json` and `status.json`, symbolic JSON on the configured bucket. Claim stores agent/time; status stores state/agent/times. Fixed reader rules, not textual interpretation, determine pending/in-progress/complete behavior. SRC-1 implementation, `sdk/tracecraft/protocol.py`:

> claim_doc = store.get_json(f"steps/{sid}/claim.json")
> if claim_doc is not None:
>     return "in_progress", claim_doc.get("agent", "?")
> return "pending", None
> --- `sdk/tracecraft/protocol.py:170-173`

### Routes

#### RT-RTE-init-config
Label: Initialize configuration and registration

Owner/progression: caller supplies project, agent, backend and credentials; Click validates required S3 inputs, saves config, adjusts gitignore, ensures bucket and registers agent. Local config and remote registration are separate effects. Admission mode: open configuration request; no answer oracle. Caller proposes and can decline before invoking; software rejects missing required fields or service errors. Human versus model initiation is unresolved. Replacement is another init/config edit; failure can leave prior local side effects. HF privacy defaults to private on creation, but existing visibility is only read and warned about, not changed. Guidance is option help; config and registration persist. SRC-1 implementation, `sdk/tracecraft/cli/init_cmd.py`, `sdk/tracecraft/config.py`.

- Immediate return: configuration/bucket receipt and HF caveat/privacy warnings.
- Later read-back: every command reloads config; agents/status read registration.
- Delegated visibility: registration is visible to other holders of bucket read credentials.
- Selection predicate: explicit backend/bucket/project/agent or cwd and OS-user defaults; local config takes precedence later.
- Invalidation or expiry: config replaced by a later write; registration staleness computed after 300 seconds without a newer heartbeat.
- Activation or effect: writes local credentials and remote identity record; external agent uptake unobserved.
- Evidence limits: actual bucket grants, visibility and command execution are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> save_config(cfg)
> _ensure_gitignore_entry()
>
> store = _get_store(cfg, private=private)
> store.ensure_bucket()
> --- `sdk/tracecraft/cli/init_cmd.py`

#### RT-RTE-step-control
Label: Claim complete and wait

Owner/progression: calling agent chooses step; code normalizes lowercase and periods to hyphens, rejects slash/empty IDs, requests claim admission, then writes status. Completion optionally runs a fixed git subprocess for changed files and writes status and handoff separately. Code decides conflict rejection, while service decides conditional PUT outcome. Caller proposes outcome and text; no oracle verifies substantive completion. Mode: open task coordination, not an experiment. A mismatch can be rejected unless `--force`; blocked/review flags are mutually exclusive. Recovery permits forced completion but leaves the claim object in place; no release/lease expiry is implemented in these commands. Persisted guidance is optional note/next-action plus handoff fields. SRC-1 implementation, `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/protocol.py`, `sdk/tracecraft/s3.py`, `sdk/tracecraft/hf.py`.

- Immediate return: claim/completion receipt or rejection; status prints state; wait returns all-complete or raises blocked/timeout error.
- Later read-back: step-status/status/wait-for read durable state; handoff remains separately addressable through store access.
- Delegated visibility: peers with bucket access see state; `next_agent` records a recipient but does not dispatch work.
- Selection predicate: explicit normalized step IDs; waiter tests status equal to complete.
- Invalidation or expiry: status/handoff overwrite; claim has no automatic expiry here, even when an agent is stale.
- Activation or effect: symbolic stored state changes polling results; execution of handoff prose remains unobserved.
- Evidence limits: no contention execution, service contract verification, substantive work validation or downstream handoff uptake.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> claim_doc = store.get_json(f"steps/{sid}/claim.json")
> if claim_doc and claim_doc.get("agent") not in (None, agent) and not force:
> --- `sdk/tracecraft/cli/steps.py`

> kwargs["IfNoneMatch"] = "*"
> --- `sdk/tracecraft/s3.py`

> if self.fs.exists(path):
>     from tracecraft.s3 import PreconditionFailed
>
>     raise PreconditionFailed(key)
> --- `sdk/tracecraft/hf.py`

#### RT-RTE-memory-write
Label: Shared memory write and read

Owner/progression: caller supplies arbitrary string value; code rejects empty/slash/reserved keys, then writes a timestamp/UUID history snapshot before overwriting the live key. Natural-language values are wrapped in symbolic JSON provenance. No oracle or semantic veto; open caller-driven admission, with human authorship/approval unresolved. Guidance is shipped coordination instruction to share progress. Caller may replace a value with another set; no dedicated restore command is established here. SRC-1 implementation, `sdk/tracecraft/cli/memory.py`, `sdk/tracecraft/protocol.py`; doctrine/design, `examples/claude-code/CLAUDE.md`.

- Immediate return: set receipt; get prints value or metadata and returns failure when missing.
- Later read-back: get/list/history retrieve live values or selected historical snapshots across invocations.
- Delegated visibility: shared project bucket readers can retrieve values/history.
- Selection predicate: caller dot key maps to bucket path; history selects direct leaves and newest limit (default 20), prints oldest first among selected entries.
- Invalidation or expiry: live key overwritten; history has no automatic expiry in these commands and direct store deletion remains possible.
- Activation or effect: writes durable data and returns it on explicit reads; effects on agent decisions unobserved.
- Evidence limits: structurally accepted text is not verified knowledge; history/live writes are not transactional or protected against direct mutation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> store.put_json(append_key(_history_prefix(key), cfg["agent_id"]), {"key": key, **doc})
> store.put_json(_key_to_path(key), doc)
> --- `sdk/tracecraft/cli/memory.py`

#### RT-RTE-mail-exchange
Label: Send and consume messages

Owner/progression: caller supplies recipient and text; code rejects empty/slash/reserved recipients except `_broadcast`, adds sender/time and optional step, then appends JSON. Reader selects direct and broadcast streams, excludes own broadcasts, sorts delivered records by sent_at and optionally advances its durable cursor after display. Admission mode is open caller-driven communication; software structural veto only, no answer oracle or human per-message approval established. Guidance asks agents to check inbox periodically. Recovery is full read or replay after interrupted display; deprecated deletion is irreversible through this command. SRC-1 implementation, `sdk/tracecraft/cli/messages.py`, `sdk/tracecraft/protocol.py`; doctrine/design, `examples/claude-code/CLAUDE.md`.

- Immediate return: send receipt; inbox prints message text or no-message result.
- Later read-back: full inbox re-reads retained mail; --new uses bucket-resident stream cursor.
- Delegated visibility: recipient and project bucket credential holders; broadcasts are shared, and own broadcasts are suppressed in ordinary display.
- Selection predicate: exact mailbox prefixes, direct data leaves, optional watermark/seen filtering; five-minute grace window with 1000-key seen cap.
- Invalidation or expiry: --new preserves records; --delete removes displayed direct messages only; no automatic message expiry is implemented here.
- Activation or effect: stored mail and reader position change; model compliance with message text is unobserved.
- Evidence limits: sender clocks and upload delay bound incremental delivery; concurrent same-agent readers and actual host uptake uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if only_new and (direct_keys or broadcast_keys):
>     store.put_json(
>         cursor_key(my_id),
> --- `sdk/tracecraft/cli/messages.py`

#### RT-RTE-artifact-share
Label: Upload and download artifacts

Owner/progression: caller selects existing local file, optional step and destination. Code uses upload basename and normalized step/shared prefix; backend copies bytes. Content form is opaque arbitrary file bytes until a later consumer parses them, not automatically natural-language knowledge. Open caller-driven admission; no semantic veto/oracle/redaction or per-file human approval established. Guidance is the shipped skill's share-files procedure. Reupload replaces the same key; recovery/rollback depends on an available prior copy, not an implemented revision selector. SRC-1 implementation, `sdk/tracecraft/cli/artifacts.py`; doctrine/design, `examples/hermes-agent/SKILL.md`.

- Immediate return: upload/download receipt or missing-artifact error; list prints matching keys.
- Later read-back: download reads retained bytes into caller-selected local path.
- Delegated visibility: peers with bucket credentials and artifact name/step can download.
- Selection predicate: upload basename; download supplied name; explicit normalized step or shared prefix.
- Invalidation or expiry: same-key upload overwrites; no automatic expiry in CLI.
- Activation or effect: remote upload and local download only; interpretation/execution by recipient outside inspected route.
- Evidence limits: file contents, recipient behavior, service grants and deployment paths uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> store.put_file(key, path)
> click.echo(f"Uploaded {filename} -> {key}")
> --- `sdk/tracecraft/cli/artifacts.py`

#### RT-RTE-session-mirror
Label: Mirror and inspect host sessions

Owner/progression: caller chooses harness/session/cwd and cadence; registry/adapter decides discovery; fixed mirror code reads delta, applies default regex redaction unless disabled, writes part/meta/local state. Admission is automatic byte ingestion after caller initiation, not per-content human approval. No oracle judges retained content. Mode is one-shot or open-ended polling, not a reasoning curriculum. Host-produced trace is guidance-free input to this storage route; parts, metadata and cursor persist, not proposed theories. Failures reject a flush by raising; no rollback transaction spans its writes. Recovery derives next sequence from listing, but lost cursor restarts source consumption at zero. SRC-1 implementation, `sdk/tracecraft/cli/session.py`, `sdk/tracecraft/redact.py`, `sdk/tracecraft/harness/base.py`, `sdk/tracecraft/harness/hermes.py` and registry adapters.

- Immediate return: uploaded-byte/redaction receipt, no-new-data result, or discovery/service error; follow returns on interrupt after end marking.
- Later read-back: list reads metadata; show --tail downloads sorted parts and prints selected tail lines; metadata-only show is default.
- Delegated visibility: bucket readers can inspect mirrored sessions without sharing a running host conversation.
- Selection predicate: explicit ID or active adapter session; --all rediscovers all; min-bytes compares cursor delta (row IDs for Hermes, despite byte-labelled option).
- Invalidation or expiry: cursor advancement suppresses repeated normal flushes; stop clears local cursor and stamps end but does not terminate a running follow process; no transcript TTL here.
- Activation or effect: persists transformed trace bytes and bookkeeping, not an automatic model-context injection or behavior-shaping revision.
- Evidence limits: regex matches are not all secrets; cross-chunk secrets can evade independent flush redaction; source pruning/truncation, multiwriter metadata and host usage are not guaranteed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if no_redact:
>     out_bytes, counts = chunk, {}
> else:
>     out_bytes, counts = redact(chunk)
> --- `sdk/tracecraft/cli/session.py`

> store.put_json(meta_key, meta)
>
> # Persist local state. Advance the cursor to the position we read up to
> # (next_cursor), NOT cursor+raw_len — those differ for SQLite where the
> # cursor is a rowid and raw_len is synthesized-JSONL byte length.
> _save_state(
> --- `sdk/tracecraft/cli/session.py`

#### RT-RTE-session-compact
Label: Compact transcript parts

Owner/progression: caller requests a session and optional keep-tail count; code downloads selected parts, concatenates bytes, uploads a new sequence-zero part, rewrites metadata and then deletes originals. Open caller-requested layout maintenance with code admission: negative keep-tail rejected, fewer than two targets is a no-op. No answer oracle or semantic proposal; no per-byte human veto established. Guidance is preserve bytes/order while reducing object count. Merged blob and updated meta persist; partial failure can leave duplicate replay material, not a transactional rollback. SRC-1 implementation, `sdk/tracecraft/cli/session.py`.

- Immediate return: compacted/deleted counts or no-op/error.
- Later read-back: show uses listed part files, including surviving originals after interruption, rather than filtering through metadata parts.
- Delegated visibility: subsequent bucket readers see consolidated or partially consolidated layout.
- Selection predicate: first matching session metadata; lexically sorted part-pattern keys minus newest keep-tail parts.
- Invalidation or expiry: originals deleted only after merged upload and meta write; remaining files have no TTL here.
- Activation or effect: byte-preserving normal-path layout change, not semantic summarization or model-window eviction.
- Evidence limits: interrupted/concurrent maintenance and actual read equivalence unobserved; duplicates can change show output during partial completion.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> store.put_json(meta_key, meta)
>
> # 4. Now it's safe to delete the originals (merged copy already durable).
> deleted = 0
> for k in targets:
> --- `sdk/tracecraft/cli/session.py`

#### RT-RTE-package-release
Label: Admit package and adapter changes

Owner/progression: source contributors propose code/instruction changes; a published GitHub release selects its tag for checkout, build, artifact checks, installed CLI version smoke check and PyPI publication. Registry edits admit adapters into later installs. CI separately runs lint/format and Python 3.10/3.12 tests on main pushes/PRs. Mode is event-triggered packaging with fixed checks, not self-improvement. Test suite expectations are a reference outcome for CI; release's checks concern package validity and CLI startup, not answer quality. Human release and merge authorization is unresolved in frozen workflow configuration; failing job steps can reject publication, but CI success is not explicitly a release prerequisite. Guidance is declared workflow commands and adapter registry instructions. Packages/source persist; consumers install the new artifact. No automatic deployment rollback is shown; changing install version is an external consumer action. SRC-1 implementation, `.github/workflows/ci.yml`, `.github/workflows/release.yml`, `sdk/pyproject.toml`, `sdk/tracecraft/harness/__init__.py`.

- Immediate return: build/check/publish workflow results, not inspected run artifacts.
- Later read-back: later installations load released source, registry and CLI entry point.
- Delegated visibility: package distribution to installing consumers; PyPI service behavior outside registered evidence.
- Selection predicate: published-release tag; source package includes tracecraft* under sdk.
- Invalidation or expiry: a later install can replace package; no automatic rollback or revocation established by these files.
- Activation or effect: wired publication path; installation and execution of a changed package remain unobserved.
- Evidence limits: branch protection, environment approval, actual releases, successful CI and deployed upgrades not supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> - uses: actions/checkout@v4
>   with:
>     ref: ${{ github.event.release.tag_name }}
> --- `.github/workflows/release.yml`

### Claims

#### RT-CLM-mirror-idempotence
Label: Claimed mirror idempotence

Claimed operation: mirror docstring calls the route idempotent and safe for cron. Source: SRC-1 doctrine/design, `sdk/tracecraft/cli/session.py`. Implementation ordering establishes normal cursor suppression, not exactly-once recovery: part upload can succeed before metadata/local cursor updates, causing replay. No executed witness supplied.

> Idempotent and safe to re-run
> on a cron.
> --- `sdk/tracecraft/cli/session.py`

#### RT-CLM-secret-redaction
Label: Bounded credential redaction

Claimed operation: default mirror redaction catches recognizable credential shapes, explicitly not arbitrary secrets. SRC-1 doctrine/design and implementation, `sdk/tracecraft/redact.py`. Regex replacement counts provide an audit of matched patterns, not proof of safe disclosure; disabled mirroring and artifact/direct store paths have different coverage.

> This is
> NOT a real DLP system — it cannot catch arbitrary secrets, custom internal
> token formats, or business-logic data. It catches well-known token shapes.
> --- `sdk/tracecraft/redact.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-prompt
Label: Shipped coordination instructions

Consumer: external Claude Code or Hermes host agent if its host loads the example prompt/skill. Channel: natural-language project instruction or skill body, stored as shipped Markdown; not automatically installed or loaded by the storage SDK. Force: requested behavior interpreted by the model, not CLI invariant. Horizon: repeated agent actions and later sessions while the host continues to supply it. The prompt tells agents to claim before work, write progress and read inbox; Hermes also requests post-write verification. SRC-1 doctrine/design, `examples/claude-code/CLAUDE.md`, `examples/hermes-agent/SKILL.md`. Delivery, compliance and benefit are uninspected.

> 3. Run `tracecraft claim <your-step>` before starting work
> 4. Share progress via `tracecraft memory set`
> 5. When done, run `tracecraft complete <step> --note "context for next agent"`
> --- `examples/claude-code/CLAUDE.md`

#### RT-BAP-step-polling
Label: Persisted state controls dependency polling

Consumer: `wait-for`, `step-status` and aggregate status code. Channel: symbolic bucket status/claim JSON read through `effective_status` variants. Force: fixed code branching; a state equal to complete lets the waiter return, blocked raises, review-needed continues waiting. Horizon: later command invocations across hosts with the same bucket/project. This is behavioral authority over coordination tooling, not verification of completed work or enforcement of the next agent's textual instruction. SRC-1 implementation, `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/protocol.py`, `sdk/tracecraft/cli/status.py`.

> if all_done:
>     click.echo(f"All steps complete: {', '.join(step_ids)}")
>     return
> --- `sdk/tracecraft/cli/steps.py`

## Annotations

none
