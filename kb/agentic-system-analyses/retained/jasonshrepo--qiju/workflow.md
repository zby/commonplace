---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Qiju workflow account: requested session checkpoint, durable capture and later search-to-hydration handoff."
run-id: AAS-2026-11-08-qiju-1a12c31c13d1-01
reviewed-boundary: a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89
---

# Qiju workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a user-requested session checkpoint followed by a later agent's history question. It was selected because Qiju ships instructions for both ends and code connecting the record written at the first end to retrieval at the second. This is not a reconstructed execution trace: SRC-1 supplies implementation and doctrine/design, not an observed successful handoff. The frozen boundary and external-host limits are in [boundary](boundary.md#boundary-and-evidence). Qiju coordinates record I/O; the external coding host owns session interpretation, tool calls and the eventual user answer. It does not dispatch a worker or transfer a live conversation to another host. The relevant existing routes are [RT-RTE-record-capture](runtime.md#rt-rte-record-capture) and [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval).

Source inspection here covered SRC-1, `src/qiju/init_cmd.py` log instructions and search instructions, full `src/qiju/capture.py`, and the log/temp-entry handlers in `src/qiju/cli.py`. These refine the supplied runtime account at the same revision; they introduce no source or observed-run evidence.

### Request, composition and executable admission

The user requests saving, checkpointing or handing off project context. The installed log skill asks the foreground host to respect that scope, record completed work and agreed next steps, and distinguish rejected or undecided items. It asks for anchors rather than copies of artifact contents, plus decision process and rationale. The handoff to storage is therefore a selected model-authored account, not a raw transcript. SRC-1, `src/qiju/init_cmd.py`, states:

> Record what we have done and
> what we agreed to do next. Do not record your own suggestions as plans or next steps.
> --- `src/qiju/init_cmd.py`

The host calls `qiju temp-entry`, receives a workspace-local path, reads the empty file, then writes JSON containing title, tags, search terms, next steps and a Markdown body. This explicit file handoff satisfies a host Write tool's prior-read requirement; it is not a second agent context. Optional model metadata is requested only when authoritative. The host then calls log with the literal path and cleanup enabled. These are shipped instructions, not proof the host follows them. The model component and installed instruction authority are already characterized in [RT-CMP-host-model](runtime.md#rt-cmp-host-model) and [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance).

The next-step owner changes from host composition to deterministic admission in `capture.log_entry`. The CLI reads one JSON object; capture resolves project identity, normalizes metadata, repairs invalid/missing timestamps, redacts selected fields and validates shape. A conflicting explicit project at a valid selected marker is rejected. Passing those checks means structurally admitted data, not a verified account of what happened. The source's description of records as verified does not add a factual oracle. The user initiates the checkpoint but no per-sentence human approval gate is wired. See the admission and privacy limits of [RT-RTE-record-capture](runtime.md#rt-rte-record-capture).

### Persistence, rejection and recovery ownership

Code acquires the home lock, allocates or accepts an ID, validates the entry, and appends missing short/long copies. Existing IDs can skip writes; an archived ID returns immediately. Sequential tier writes do not form a cross-file transaction. The retry limitations and retained source passages are in [RT-RTE-record-capture](runtime.md#rt-rte-record-capture). A returned ID is an address for later retrieval, not evidence that a fresh payload replaced every existing copy.

A concrete rejection path precedes successful delivery: invalid JSON, a non-object input, schema rejection or a conflicting marker project reaches the log handler's error return. Cleanup is after the call to `capture.log_entry`, so these failures do not trigger that handler's staging deletion. SRC-1, `src/qiju/cli.py`, supplies the control order:

> print(entry_id)
>         if args.cleanup:
>             deleted, reason = staging.safe_cleanup(args.body, project=args.project, cwd=None)
> --- `src/qiju/cli.py`

> except (ValueError, schema.ValidationError, OSError, json.JSONDecodeError) as exc:
>         print(f"qiju log: {exc}", file=sys.stderr)
>         return 1
> --- `src/qiju/cli.py`

The host/caller, not an automatic recovery worker, must correct the input or invocation and retry. A separate root guard refuses to invent a project identity when discovery falls through to a bare current directory without a project argument or marker. Its diagnostic offers `qiju init`, an explicit project, or `QIJU_PROJECT_ROOT` as remedies; the worker must not mistake it for a stored checkpoint. SRC-1, `src/qiju/capture.py`:

> "qiju log: could not determine the project root, so refusing to create a new "
> --- `src/qiju/capture.py`

No executed failure/recovery example is supplied. Partial persistence after an I/O failure remains possible; retry with the same explicit ID may fill a missing tier, while ordinary generated-ID retry need not preserve identity. On success the CLI prints the ID and attempts guarded cleanup; cleanup refusal only warns. The skill tells the host to report that ID and not delete staging itself. Thus storage delivery is the log return and ID; user-facing checkpoint delivery additionally depends on the host reporting it. Neither establishes later use.

### Later retrieval, verification and answer delivery

On a subsequent history question, the external host chooses scope, keywords, time bounds and output shape. The search skill requests confirmation before open-ended or clearly older wide searches. For selected-history retrieval it describes two phases: candidate identification with IDs/summary, then exact-ID hydration with show. Selection code, tier merging and rendering are already established in [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval). The manifest can keep record bodies out of the model window until chosen; no sub-agent frame or host-context compaction is specified. Default full-record search and direct show remain executable alternatives, so two-phase retrieval is not enforced isolation.

Verification at this end is a host instruction, not an answer oracle: check returned project names and timestamps against the question. Stale, empty or mismatched current-project results are to trigger all-project fallback and disclosure of fragmented slugs. SRC-1, `src/qiju/init_cmd.py`:

> You **MUST NOT claim stale `current_project` results are the latest
> project state**. Otherwise, widen to `--scope all` only for cross-project questions.
> --- `src/qiju/init_cmd.py`

A second recovery rule addresses incomplete IDs: search first to recover the full suffix rather than guessing one.

> do NOT call `qiju show` with it — run `qiju search` first to recover
> the full `<uuid>:N` id. Never strip or guess `:N`.
> --- `src/qiju/init_cmd.py`

The consumer receives rendered selected fields or the hydrated record, not the original session. The host must interpret that material and produce the history answer or resume work. Qiju's terminal output here is CLI data; it has no final-answer acceptance test, automatic judgment of historical truth or acknowledgement that another host acted correctly. A delivered body does not establish activation or successful cross-session continuity. Retrospective revision is a separate procedure, [RT-RTE-skill-review](runtime.md#rt-rte-skill-review), not a mandatory completion stage of this checkpoint-and-recall workflow.

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

#### On [RT-RTE-record-capture](runtime.md#rt-rte-record-capture)

Workflow role: the producer-side handoff. User scope becomes host-authored JSON; executable rejection covers input form and selected identity checks, not narrative truth. The host/caller owns correction after a failure. Staging deletion follows successful capture; cleanup refusal does not retract storage delivery. The workflow's user-visible checkpoint is the reported record ID, while later dependent use remains unobserved. Supporting source passages and the root-fallback rejection are retained in the account above.

#### On [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval)

Workflow role: the later-consumer handoff. Search provides candidate material, the host selects hydration, and the host supplies the final answer. Time/project verification, all-project fallback and incomplete-ID recovery are requested host decisions, not enforced final-answer gates. Selected output shape controls what crosses into the host window; there is no Qiju worker return or automatic answer-delivery acknowledgement. Source instruction passages are retained above; actual compliance and benefit are unobserved.
