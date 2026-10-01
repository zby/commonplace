---
{
  "type": "types/agentic-system-analysis-result.md",
  "description": "RSIAgent source-grounded runtime, memory and epistemic analysis: staged experience learning, role-separated verification and bounded improvement evidence.",
  "run-id": "AAS-2026-09-24-rsiagent-01",
  "system": "RSIAgent",
  "run-date": "2026-09-24",
  "result-disposition": "complete",
  "target-class": "enclosing runtime",
  "boundary-kind": "whole-system",
  "reviewed-boundary": "a9e56263f6deaa493496ad6b155fe24bf131bc12",
  "analysis-cutoff": "2026-09-24",
  "evidence-tier": "code-grounded",
  "memory-comparison": {
    "scope": "Actor-owned durable memory and its access metadata; accumulated Actor, Curriculum and Verifier context; retained worklogs, diagnoses, continuation projections and their later consumers in the shipped OSWorld and ALE paths. Excludes static instructions, model-provider internals, generic event telemetry, benchmark assets and VM implementation.",
    "axes": {
      "storage_substrate": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "files",
          "in-memory"
        ],
        "records": [
          "OBJ-6",
          "OBJ-7",
          "OBJ-8",
          "OBJ-9",
          "OBJ-10"
        ],
        "note": "Host and guest files plus live role histories; the bytes dictionaries are transport representations, not a separate KV store."
      },
      "representational_form": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "OBJ-6",
          "OBJ-8",
          "OBJ-9",
          "OBJ-10"
        ],
        "note": "Natural-language summaries and diagnoses and symbolic manifests/history envelopes are inspectable. Arbitrary Actor-owned payloads and retained images prevent an exhaustive whole-boundary mapping; filename/size displays do not determine payload form."
      },
      "lineage": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "imported",
          "other-compiled",
          "trace-extracted"
        ],
        "records": [
          "OBJ-6",
          "OBJ-7",
          "RTE-8",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Initial memory is imported; manifests and projections are mechanically compiled; Actor memory, diagnosis and summaries derive from task traces. Static shipped charters are excluded."
      },
      "behavioral_authority": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "BAP-5",
          "OBJ-6"
        ],
        "note": "Wired advisory knowledge consumption is established. Source claims learned scripts as well as procedures, but actual arbitrary memory payloads and their execution are not retained here, preventing an exhaustive force classification."
      },
      "write_agency": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "automatic"
        ],
        "records": [
          "RTE-7",
          "RTE-8",
          "RTE-10",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Agent and harness writes are automatic, including operator-triggered runs. Supplying an existing memory directory is import, not evidence of a manual memory-authoring workflow."
      },
      "curation_operations": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "RTE-7",
          "RTE-8",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Supported operations include prompted evolution of older claims and worklog consolidation/deduplication/decay; open-ended Actor-owned corpus editing and absent learned payloads prevent asserting a complete operation set."
      },
      "read_back_direction": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "pull",
          "push"
        ],
        "records": [
          "RTE-9",
          "RTE-10",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Actor and Curriculum request file bodies using Programs/Looks; harness automatically supplies whole inventories, diagnoses, worklogs and selected role histories."
      },
      "read_back_signal": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "coarse",
          "identifier"
        ],
        "records": [
          "RTE-9",
          "RTE-10",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Coarse push supplies current inventory, latest outcome and history windows. Identifier push selects existing Verifier history by agentic config or legacy model identity. Agent judgment in requested retrieval is not a push signal."
      },
      "trace_learning": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "yes"
        ],
        "records": [
          "RTE-7",
          "RTE-8",
          "RTE-10",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Automatic trace-fed Actor memory, diagnosis, worklogs and retained Verifier context projections feed later consumers. Filtering/re-encoding qualifies without semantic synthesis when its derived context persists; this states wiring, not improvement."
      },
      "trace_source": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "session-logs",
          "tool-traces",
          "trajectories"
        ],
        "records": [
          "RTE-7",
          "RTE-8",
          "RTE-10",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Actor experiences, machine observations, verifier action/results and earlier conversation turns feed qualifying routes; Verifier semantic replay uses session-logs and tool-traces. Event counters alone do not qualify."
      },
      "learning_scope": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "per-task",
          "cross-task"
        ],
        "records": [
          "RTE-7",
          "RTE-8",
          "RTE-10",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Worklog, stall continuation and Verifier replay concern one task; practiced experiences and Curriculum context feed later project/target tasks. Source projects are task episodes, not repository-scoped per-project horizons."
      },
      "learning_timing": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "online",
          "staged"
        ],
        "records": [
          "RTE-7",
          "RTE-8",
          "RTE-10",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Worklogs and Verifier checkpoint/replay update online during execution; outcome learning and ordered wave publication are staged before later practice/retries."
      },
      "distilled_form": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "OBJ-6",
          "OBJ-9",
          "OBJ-10",
          "RTE-12"
        ],
        "note": "Worklogs/diagnoses are natural language; Verifier projections preserve natural-language observations/reasons plus symbolic programs/envelopes and opaque images. Actor memory bytes remain unconstrained, preventing an exhaustive union."
      },
      "faithfulness_tested": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "no"
        ],
        "records": [
          "ABS-1"
        ],
        "note": "No retained execution evidence establishing recall dependence was identified in the enumerated and searched code/text surfaces. PDF, manuscript source, images and external run stores remain uninspected; no global absence is asserted."
      }
    }
  }
}
---

# RSIAgent agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-24-rsiagent-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/rsiagent.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-24-rsiagent-01/memory-report.md`

**Memory analysis report SHA-256:** 39cb08b284aef359d8aeaf1892ab27a420bde60fcbf0d90578dccb814f62b0b2

Run AAS-2026-09-24-rsiagent-01 opened on 2026-09-24. Source-native name: RSIAgent. The local result and retained copy describe the same frozen evidence. Publication completion belongs to the run state.

## Boundary and evidence

This analysis characterizes the shipped RSIAgent implementation for readers assessing how exploration, verification and memory changes connect to later computer-use attempts. The target is an enclosing runtime with a builder or improvement plane; boundary kind: whole-system. The evidence boundary is repository commit `a9e56263f6deaa493496ad6b155fe24bf131bc12`, captured on 2026-09-24; evidence tier: code-grounded. Source allowlist: `https://github.com/AetherLabsAI/RSIAgent`; the separately allowed paper was not used. All implementation reads were commit-addressed; no worktree or previous review supplied evidence.

Included: shared Actor/Verifier action loop, Curriculum control, learning admission and memory transport, OSWorld three-phase orchestration, and ALE shared-runtime worker/learning interfaces. Inspected configurations establish available/default routes, not an actual deployed grant set. Excluded: external model internals, benchmark evaluator implementations and assets, operating-system/QEMU internals, and remote service state. Consequently this result cannot establish exact model weights, evaluation correctness, deployed isolation, or remote rollback. It does not audit every recovery utility or benchmark-specific task. Those limits prevent a universal reliability or leakage guarantee; they do not prevent tracing the principal runtime and memory routes.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git repository | `https://github.com/AetherLabsAI/RSIAgent`; access root `/home/zby/llm/commonplace/related-systems/AetherLabsAI--RSIAgent` | `a9e56263f6deaa493496ad6b155fe24bf131bc12` | implementation | `core/`, `explore/`, `llm/client.py`, `config/roles/`, OSWorld pipeline/task/actor boundary, ALE worker/learning and memory adapter paths specified below | full commit-relative paths and minimum quotations on canonical records | no execution traces or inspected provider/benchmark internals; wired routes do not establish operation or effectiveness |
| SRC-2 | same Git repository | `https://github.com/AetherLabsAI/RSIAgent` | `a9e56263f6deaa493496ad6b155fe24bf131bc12` | doctrine/design: architecture and method; reported operation: score tables | `README.md`, `docs/ARCHITECTURE.md`, `docs/PAPER.md` | claim records below | author-reported aggregates are not run capsules or independently identified causal comparisons |

## Shared records

### Components

CMP-1 — Host harness. Python control code coordinates role calls, action parsing, phase transitions, persistence, isolation and sealed scoring. Symbolic form in repository source. Implementation conclusion status: wired. SRC-1 `core/loop.py:546-608,721-835,962-1040,1069-1189`; `core/self_evolving_loop.py:149-393`; `benchmarks/osworld/pipeline.py:540-628`. RTE-1, RTE-2, RTE-3, RTE-4, RTE-5 and RTE-6 below describe its distinct controls.

CMP-2 — Actor model. Distributed-parametric completion service selected by configuration, default target/practice identity `z-ai/glm-5.3`; target escalation selects `moonshotai/kimi-k3`. Endpoint selection conclusion status: wired; exact parameter/version pinning conclusion status: uninspected, because names resolve through OpenRouter with allowed provider fallback rather than an inspected weight digest. Operational parameter-update conclusion status: uninspected for provider internals; the inspected client is an inference call interface, while the fixed-weight experiment is CLM-3. SRC-1 `config/roles/actor.yaml:1-43`; `config/roles/target.yaml:1-47`; `llm/client.py:272-340`.

> model: z-ai/glm-5.3
> provider_order:
>   - Z.AI
> provider_allow_fallbacks: true
> --- `config/roles/actor.yaml` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> resp = _c().chat.completions.create(model=model, messages=messages,
>                                                 max_tokens=max_tokens, temperature=temperature, **kwargs)
> --- `llm/client.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

CMP-3 — Kimi K3 role and visual models. Separate Curriculum, Verifier and visual-reader conversations use distributed-parametric model calls; sharing a model name does not share private role history. Role/visual invocation conclusion status: wired; exact-version pinning and provider parameter updates conclusion statuses: uninspected. Configurable model names are mutable endpoint identities. No embeddings or learned router are required by these inspected routes; this is a scoped inventory, not a repository-wide absence claim. SRC-1 `config/roles/curriculum.yaml:1-42`; `config/roles/target.yaml:55-98`; `core/loop.py:1217-1270`; `core/verifier.py:841-918`.

> model: moonshotai/kimi-k3
> provider_order: []
> provider_allow_fallbacks: true
> --- `config/roles/curriculum.yaml` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

CMP-4 — Guest VM and Verifier executor adapters. Symbolic code dispatches Actor programs to the VM and gives Verifier programs a selected execution boundary. Current target configuration selects `rollback_mirror`; the alternate executor uses private namespaces and read-only candidate mounts. Implementation conclusion status: wired; deployed operating-system/QEMU enforcement conclusion status: uninspected. SRC-1 `core/verifier_runtime.py:422-458,998-1112,1305-1345`; `config/roles/target.yaml:69-98`. RTE-3 scopes their guarantees.

### Operative objects

OBJ-1 — Natural-language task/project requirements and supplied inputs. Imported task instructions or Curriculum-authored project requests guide Actor and Verifier calls. Natural-language instructions coexist with arbitrary fixture bytes; those fixture contents are uninspected. Storage: files and in-memory request context. Delivery conclusion status: wired. SRC-1 `core/loop.py:546-596,962-1018`; `explore/charter.py:565-582`. A public task is not an answer key.

OBJ-2 — Candidate environment and deliverables. Actor programs change guest files, applications and service state. Content and representational form are task-dependent, not determined by the Python transport. These are the object of local verification and later official scoring. Production conclusion status: wired; actual candidate quality conclusion status: uninspected. SRC-1 `core/loop.py:1069-1169`; `core/verifier.py:841-918`; `benchmarks/osworld/task.py:259-317`.

OBJ-3 — Verifier report and terminal token. Model-authored natural-language evidence plus PASS/FAIL/UNVERIFIED or route tokens are retained by the host and consumed by the Actor/Curriculum. Report syntax is checked separately from report truth. Form/storage: natural language in files and conversation context; verdict token is symbolic control. Production and consumption conclusion statuses: wired; factual correctness conclusion status: uninspected. SRC-1 `core/verifier.py:1198-1274`; `core/verifier_runtime.py:422-437`.

OBJ-4 — Official benchmark score and grading checkpoint. External evaluator result is retained in host JSON after agent termination; it informs reporting, not the current protocol's learning loop. Symbolic fields store imported assessment values whose underlying evaluator correctness is excluded. Consumption conclusion status: wired. SRC-1 `benchmarks/osworld/task.py:259-317`; `benchmarks/osworld/pipeline.py:590-626`; `benchmarks/ale/worker.py:41-59,80-96`.

OBJ-5 — Actor-authored done checks and results. Natural-language descriptions and symbolic shell probes are proposed by the Actor, filtered by code and executed against the guest; results use textual PASS without FAIL. They can precede independent verification but do not inherit its isolation mechanism. Form/storage: mixed natural-language/symbolic conversation and files. Conclusion status: wired. SRC-1 `core/checks.py:139-200`; `core/loop.py:1339-1410`.

#### OBJ-6 — Actor-owned durable memory tree

Source: SRC-1 `explore/charter.py`, `explore/practice_loop.py`.

Operative object. Storage: host directory plus guest `~/.memory`, transported as relative paths to bytes. Form: unconstrained payload, with prose and scripts claimed; no exhaustive form assignment. Lineage: imported initial bank, then trace-extracted Actor updates. Consumer: future Actor and, on enabled routes, Curriculum. Authority: advisory content is wired; arbitrary executable payload force is not determinable from this source alone. This is derived memory, not the raw trace archive. Instructions expose no required rationale field, provenance field or entry identity. Actor may preserve causal reasons but retention is discretionary.

> Update your durable memory at {memory_root} in whatever way you judge will make a
> fresh future Actor Agent more capable. You may investigate remaining questions if
> the available project state makes that useful, and you may add, revise, reorganize,
> delete, or leave memory unchanged. You own the content, representation, retrieval
> strategy, scope, and stopping decision; there is no required schema, length,
> number of files, or number of turns. A FAIL may still contain valuable evidence,
> but must not be recorded as a verified success.
> --- `explore/charter.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> def _read_memory_tree(path: str) -> dict[str, bytes]:
>     root = Path(path)
>     if not root.exists():
>         return {}
>     if root.is_symlink() or not root.is_dir():
>         raise PracticeInfrastructureError("durable memory root is not a real directory")
>     files: dict[str, bytes] = {}
>     for candidate in sorted(root.rglob("*")):
>         if candidate.is_symlink():
>             raise PracticeInfrastructureError(
>                 f"durable memory contains a symlink: {candidate}")
>         if candidate.is_file():
>             files[str(candidate.relative_to(root))] = candidate.read_bytes()
>     return files
> --- `explore/practice_loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

#### OBJ-7 — Memory inventory, manifests and journal

Source: SRC-1 `explore/commit.py`, `explore/practice_loop.py`.

Operative access/provenance objects. Filenames and sizes form the displayed inventory; file and tree hashes identify byte states; the journal stores complete per-episode tar snapshots plus metadata. These are symbolic metadata and byte archives in files, compiled automatically from memory. The inventory selects no particular file body. Journal snapshots are described as invisible to the agent and support audit/recovery; they are not a normal retrieval index. Atomic installation stages a complete tree, fsyncs, renames the previous tree to a backup, and restores that backup if replacement fails. Successful replacement removes the backup; the journal remains a separate record.

> def _manifest(files: dict[str, bytes]) -> dict[str, dict[str, Any]]:
>     return {
>         name: {"bytes": len(data),
>                "sha256": hashlib.sha256(data).hexdigest()}
>         for name, data in sorted(files.items())
>     }
> 
> 
> def _listing(files: dict[str, bytes]) -> str:
>     return "\n".join(f"{name}  {len(data)}B"
>                      for name, data in sorted(files.items()))
> --- `explore/practice_loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> def journal(journal_dir: str, episode: int, files: dict, meta: dict) -> None:
>     """Append-only per-episode snapshot (tgz) + one meta line. Invisible to the
>     agent; pure rollback/audit insurance."""
>     os.makedirs(journal_dir, exist_ok=True)
>     p = os.path.join(journal_dir, f"ep{episode:03d}.tgz")
>     with tarfile.open(p, "w:gz") as tf:
>         for rel, data in sorted(files.items()):
>             info = tarfile.TarInfo(rel)
>             info.size = len(data)
>             info.mtime = int(time.time())
>             tf.addfile(info, io.BytesIO(data))
>     with open(os.path.join(journal_dir, "journal.jsonl"), "a") as f:
>         f.write(json.dumps({"episode": episode, "files": len(files),
>                             "bytes": sum(len(d) for d in files.values()),
>                             "ts": time.strftime("%Y-%m-%d %H:%M:%S"), **meta}) + "\n")
> --- `explore/commit.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>             moved_old = True
>         try:
>             os.replace(stage, destination)
>         except Exception:
>             if moved_old and backup.exists() and not destination.exists():
>                 os.replace(backup, destination)
>             raise
>         parent_fd = os.open(destination.parent, os.O_RDONLY)
>         try:
>             os.fsync(parent_fd)
>         finally:
>             os.close(parent_fd)
> --- `explore/practice_loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

#### OBJ-8 — Role conversation and raw evidence archives

Source: SRC-1 `core/verifier.py`, `explore/practice_loop.py`.

Operative context object, distinct from telemetry. Natural-language observations and reasoning, symbolic action programs and conversation envelopes, plus retained image payloads accumulate in live lists and transcript files. Each role has its own context; Verifier is not supplied the Actor's private reasoning/bank. Raw transcripts retain turns that a live-context projection can omit. These are primarily current-task or current-lineage state, not a common cross-role knowledge store. Exact image evidence is not interchangeable with its textual description.

> class VerifierSession(list):
>     """One Verifier Agent's conversation plus cumulative inspection telemetry.
> 
>     Conversation continuity preserves the Agent's own prior reasoning and findings.
>     The counters are telemetry only: evidence freshness is deliberately local to each
>     candidate inspection, because an earlier content probe may describe an artifact
>     that the Actor Agent subsequently revised.
>     """
> 
>     def __init__(self, messages=(), *, on_event=None):
>         super().__init__(messages)
>         self.informative_probes = 0
>         self.content_probes = 0
>         self.inspections = 0
>         # Crash-safe agentic-verifier continuation metadata. The raw transcript is
>         # authoritative; these fields carry only the environment result that follows
>         # the last retained Program/Look action and therefore is not itself a complete
>         # conversation pair.
>         self.pending_observation = ""
>         self.pending_images = []
>         self.pending_turn = None
> --- `core/verifier.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>     inspector conversation is persisted via ``sink`` for autopsy.
> 
>     ``session`` (E4-A1, 's design): with cfg.verifier_continuity, the caller
>     passes ONE :class:`VerifierSession` per run. The verifier's exchanges and its
>     prior probes/verdicts accumulate as its own history (like the Actor's), so a
>     WRONG issued at inspection N is remembered at inspection N+1. Mechanical
>     evidence freshness does NOT accumulate: every candidate inspection must read
>     the current artifact before PASS, while cumulative counters remain telemetry.
>     Actor-conversation blindness is untouched: the session holds only the
>     Verifier's own work. A legacy list still preserves conversation history only.
>     Flag off or session None -> fresh context, byte-identical to E3."""
>     if getattr(cfg, "agentic_verifier_config", ""):
>         return verify_agentic(
> --- `core/verifier.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>     """End pixel replay at a project boundary without compacting Agent context.
> 
>     Native Look pixels are needed throughout the Curriculum Agent's active project
>     decision, but replaying every historical image into every later project eventually
>     violates provider image-payload limits. The complete images remain losslessly in
>     the raw transcript that first recorded them. This live-context projection removes
>     only the private wire attachments after the project boundary; it retains every
>     message and every original character, then appends a truthful retrieval note so the
>     Agent can freely reissue a Look when old visual evidence is relevant again.
>     """
> --- `explore/practice_loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

#### OBJ-9 — WORK LOG and fresh-attempt handoff

Source: SRC-1 `core/actor.py`, `core/trace.py`.

Derived natural-language memory in live context and per-fold `worklog.txt`; optional strategy review is also retained on the pivot route. Producer: summarizer using the Actor model. Inputs: previous summary and older user/assistant turns, or the final 60 messages when a stalled attempt has no worklog. Handoff consumers: later Actor turns and a fresh Actor attempt on the same instruction. These are durable trace-derived behavior-shaping artifacts, not just display summaries of an unseen payload. The summarizer is instructed to retain decisions and one-line reasons, and its complete output is the context consumed later, subject to explicit caps.

>     def save_summary(self, n: int, text: str) -> None:
>         """The model-maintained WORK LOG at fold n (summary-mode compaction) —
>         persisted per fold so summary fidelity can be audited against the full
>         transcript."""
>         self._write(os.path.join(self._iter_dir(n), "worklog.txt"), text)
> --- `core/trace.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> You are given the CURRENT LOG and a batch of OLDER TURNS to fold in. Output the \
> UPDATED LOG only. Rules:
> - Record only what actually appears in the turns. NEVER invent, infer or embellish.
> - Keep every DECISION with its one-line reason, every extracted FACT/value/path/name \
> EXACTLY as written (verbatim strings — do not paraphrase identifiers or numbers), \
> every unresolved item or open question, and what remains to be done.
> - Dead ends and repetition: one line each ("tried X — failed because Y").
> - Prefer merging into existing entries over duplicating them.
> - ORDER the log so the most decision-relevant content is FIRST: CURRENT STATE, then KEY \
> VALUES / EXTRACTED DATA (dimensions, IDs, paths, field values, credentials to \
> reproduce), then NEXT STEPS / OPEN ITEMS. Put tool/format/reference notes that could be \
> re-derived from files on the machine LAST.
> - If unsure whether something matters, KEEP it in the original wording.
> - The log has a fixed character budget and is truncated from the BOTTOM if it overruns, \
> so keep the re-derivable reference detail last and NEVER drop extracted task DATA \
> (values, dimensions, IDs, credentials): if space is tight, drop a reference/format note \
> --- `core/actor.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

#### OBJ-10 — Learning diagnosis and Curriculum continuity notes

Source: SRC-1 `explore/charter.py`, `explore/target_learning.py`, `explore/unified_evolution.py`.

Derived natural-language artifacts plus symbolic outcome envelopes, stored in episode files and live Curriculum state. The Actor diagnosis explicitly carries hypotheses and causal reasons separate from durable memory. A later Curriculum prompt receives it verbatim inside the latest outcome. Curriculum-authored notes are read from its guest file, audited, and retained in the persistent session for later prompts. These are not authorizations for Curriculum to edit the Actor bank.

> role-owned handoff to the persistent Curriculum Agent, separate from durable
> memory. Explain the hypotheses that now seem most useful for choosing the next
> experience: attempted approaches, observed limitations, plausible causal reasons,
> what appears reliable, what remains uncertain, and which distinctions or stress
> cases could discriminate among competing explanations.
> 
> The Verifier establishes what was or was not verified; do not convert its verdict
> into an unsupported causal story. Ground claims in the trajectory and evidence
> available in your same context, label uncertainty honestly, and do not prescribe a
> fixed curriculum or grade future work. Do not include private chain-of-thought or a
> --- `explore/charter.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> def _outcome_text(record: dict[str, Any]) -> str:
>     pieces = [
>         record["label"],
>         "ORIGINAL REQUEST (verbatim):\n" + record["request"],
>         "TERMINAL OUTCOME: " + record["terminal_outcome"],
>         "VERIFIER REPORT (verbatim):\n" + record["verifier_report"],
>         "ACTOR LEARNING DIAGNOSIS (verbatim):\n" + record["learning_diagnosis"],
>     ]
>     return "\n\n".join(pieces)
> --- `explore/target_learning.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>                         require_completed_publication=True)
>                     session.history = curriculum_history
>                     recovering_turn = False
>                     notes = hooks.read_guest_text(vm, CURRICULUM_NOTES)
>                     if notes:
>                         if hooks.audit_text(
>                                 notes, mode="practice",
>                                 authorized_instruction=audit_target):
>                             raise PracticeBoundaryError(
>                                 "Curriculum notes failed target boundary")
>                         curriculum_notes = notes
>                         session.notes = notes
> --- `explore/unified_evolution.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

### Routes

RTE-1 — Task execution and model-controlled effects. Trigger: host starts/resumes an Actor attempt with OBJ-1 and available memory. Next-step owner: Actor model chooses Program, Look, Ask or Done; symbolic harness parses and dispatches. Context contains static role instructions, task, evolving conversation, observations, and optionally summaries; state includes OBJ-2 and traces. A Program calls an override executor or `vm.run_script`; a Look uses delegated vision or native images; Ask uses a configured user channel, otherwise a no-channel response. The host retains traces/history and returns LoopResult/history; task/iteration/watchdog or verified-completion conditions terminate. Transport recovery records uncertain effects and does not replay a failed program. SRC-1 `core/loop.py:546-608,962-1040,1069-1285`.

Implementation conclusion status: wired; operation/activation conclusion statuses: uninspected. Immediate return is a new observation; later read-back is handled by the memory records; delegated visibility is selected images/questions, not the complete Actor conversation. Selection predicate is parsed action type. History lifetime and compaction depend on configuration. Recovery is bounded by controller/provider policy. Product changes are admitted by action dispatch without a semantic preapproval gate in this route; the Actor proposes and chooses, the host may reject malformed or unsupported actions. Guest privileges and attached services define the effective grant. Rollback is not implied for ordinary Actor actions. Guidance is task/role instructions and any retrieved retained memory; their actual effect is not established by delivery. No independent answer oracle is supplied here. Guarantee strength: protocol for dispatch/recovery, no claimed guarantee of task correctness.

> execute_program = program_executor or vm.run_script
> trace = execute_program(
>     turn.lang, turn.code, timeout=cfg.script_timeout)
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> "The failed program was NOT replayed. Its result is unknown; "
> "inspect live state before relying on any partial effects."
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

RTE-2 — Actor done-check execution and local admission. Trigger: non-practice Done with OBJ-5. Actor proposes probes; host regex filters malformed, constant or recognized mutating probes and limits count; guest executes accepted probes. It records output and derives a Boolean from PASS without FAIL. Depending on configuration, independent verification follows. One-shot visual/witness nudges do not form permanent correctness gates. Rejected checks can trigger independent arbitration when accepted checks pass. Immediate return is failure/repair or continuation toward done; persistence is saved checks, not a separate learned policy; there is no automatic later-task selection or delegated memory read-back in this route. Expiry is the attempt horizon. SRC-1 `core/checks.py:139-200`; `core/loop.py:1339-1410`. Implementation conclusion status: wired; operation conclusion status: uninspected. Guarantee strength: best effort for regex screening, protocol for token interpretation. This mechanism cannot establish universal read-only execution or task truth; its execution path differs from RTE-3.

> out = vm.run_command(c.probe, timeout=timeout) or ""
> passed = bool(re.search(r"\bPASS\b", out)) and not re.search(r"\bFAIL\b", out)
> --- `core/checks.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

RTE-3 — Independent Verifier investigation and disposition. Trigger: candidate inspection from RTE-1 and RTE-2 or learning task hook. A separate persistent Verifier conversation reads requirements and candidate evidence, chooses programs/visual probes, and publishes OBJ-3. The host checks report-token syntax and consumes the report for revision, learning eligibility, or handoff; it does not mechanically prove that the report's claims follow from evidence. Curriculum can request more verification of the unchanged candidate on enabled routes. Immediate return is the report/verdict, delegated visibility excludes Actor memory/private paths when configured, later same-candidate read-back uses the specialist's Verifier records, and invalidation occurs at candidate/task boundaries. SRC-1 `core/loop.py:721-835`; `core/verifier.py:841-918,1198-1274`; `core/verifier_runtime.py:422-458,1010-1112,1305-1345`.

Implementation conclusion status: wired; operation/effectiveness conclusion statuses: uninspected. Owner/enforcement point for guest isolation: host's AgenticVerifierExecutor and QEMU transaction. Current target selects rollback mirror: guest effects are restored before return, and rollback failure raises an infrastructure error. Remote service effects are outside this contract. Alternate effect-isolated mode invokes private mount/PID/network/IPC/UTS namespaces, checks candidate read-only mounts, and keeps scratch writable. These are distinct deployed dependencies; neither covers ordinary Actor actions or RTE-2 regex-screened checks. Guarantee strength: protocol conditional on host/guest/QEMU contract; deployed isolation remains uninspected. Verifier proposes and decides local correctness; host can reject malformed reports/infrastructure failures; human operators configure or halt the run. Requirement-grounded model investigation is not access to a supplied gold answer. No claim-content oracle beyond the inspected evidence is established.

> if callable(validator) and validator(code) is None:
>     return _trace(
>         "Verifier report was preserved but NOT accepted by the host "
> --- `core/verifier_runtime.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> self._rollback_transaction.rollback()
> --- `core/verifier_runtime.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> "Verifier rollback failed; the candidate is not safe to "
> --- `core/verifier_runtime.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

The alternate legacy branch in `verify_independent` runs when no agentic verifier config is selected: model-authored JSON chooses filtered probes and visual observations, with local evidence counters and doubt clarification before PASS. It does not use the agentic executor simply by sharing the Verifier name. This branch is wired at SRC-1 `core/verifier.py:1332-1465,1465-1515,1550-1615`; deployed use is uninspected. The memory profile includes its optional conversation continuity, while isolation conclusions remain branch-specific.

Shared quotation: see OBJ-8.

RTE-4 — Curriculum proposal and stopping decisions. Trigger: a target outcome and Actor diagnosis or a completed practice project. Persistent Curriculum context receives prior outcomes, private notes and an optional disposable Actor-memory copy whose edits cannot write back to the canonical bank. It proposes a natural-language project plus fixtures, readiness, or STALLED; the harness parses the handoff and dispatches a fresh Actor/Verifier task or returns control. The Curriculum owns selection and can decline further practice; it does not grade the candidate or author Actor memory. Humans select study design, roles and stopping policy. Host boundary/format checks can reject publication. No expected solution is supplied by this route; fixture creation is allowed, worked solutions and grading logic are prohibited by prompt policy. SRC-1 `explore/unified_evolution.py:288-366,530-635`; `explore/charter.py:504-585`.

Immediate return: project/readiness token. Later read-back: persistent Curriculum history/notes plus updated outcome and memory availability. Delegated visibility: project request and fixtures; private hypothesis/rationale are intentionally omitted from the Actor project. Selector: model judgment under charter, not a deterministic information-gain estimator. Expiry: target lineage. Activation and achieved learning are uninspected; implementation conclusion status: wired; guarantee strength: policy for semantic role separation, protocol for tokens and transitions.

Guidance explicitly asks for hypotheses about the Actor's bottleneck, revised on contradictory outcomes. The subject is internal capability, and outcome-dependent notes/context can alter future project selection: a reflective operational route is wired. Formulated theory generation, use and content-directed criticism are afforded by the executable prompt route; actual produced theories and observed criticism are uninspected. Revision/changed reliance is afforded; improved capacity attributable to criticism is uninspected. Addressability is afforded at the level of free-form hypotheses/notes but no fixed assumption/claim schema is enforced. Retention and read-back are specified by the integrated memory records. This is not evidence that it revised a theory of its theory-building organization.

> Maintain and revise hypotheses about the Actor Agent's actual bottleneck. Treat
> each project as an experiment: its purpose is to improve capability or reduce
> important uncertainty. Use the terminal Verifier Agent verdict and evidence from
> each project, including failures; do not optimize for easy passes, episode count,
> memory volume, or a predetermined curriculum. When evidence contradicts your
> theory, change the theory. {search_contract}
> --- `explore/charter.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> curriculum_prompt = self_evolving_curriculum_charter(
>     target,
>     project_history="\n".join(project_summaries),
>     latest_outcome=latest_outcome,
>     curriculum_notes=curriculum_notes,
> --- `explore/unified_evolution.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

RTE-5 — Frozen-memory test execution and sealed measurement. Trigger: completed Phase 2 and a precommitted Phase 3 task set. OSWorld copies memory and verifies its hash, runs tasks with no host memory writeback, then verifies the boundary records and aggregates external scores. Task runner enters official evaluation after agent completion and preserves the candidate across grader errors. ALE's separate worker similarly runs baseline/Phase 3 with verified input memory, closes Verifier executors, checks memory again and returns `safe_to_grade`; learning phases return that flag false. SRC-1 `benchmarks/osworld/pipeline.py:540-628`; `benchmarks/osworld/task.py:194-317`; `benchmarks/ale/worker.py:16-103`.

Immediate return: agent result followed by host score; persistence: frozen memory lock, host records/checkpoints. Delegated visibility: task inputs and memory, not official scores. Selection: precommitted tasks and whole frozen memory tree; no subsequent learning consumer in this protocol. Invalidation: mismatch raises; candidate recovery preserves completed state rather than rerunning the Actor after grading failure. Owner: host; strength: protocol at inspected orchestrator boundaries, dependent on excluded evaluator/guest services. Implementation conclusion status: wired; deployment and scoring correctness conclusion statuses: uninspected. A bounded pre-Actor scan quarantines recognizable OSWorld BaseTask source beneath `/home/user`; it is not an all-channel proof against benchmark leakage. Official evaluator is the answer-oracle provider for final measurement, and has no admitted feedback path to learning here. Optional evaluator correction is a separately recorded measurement mode, not an agent-authored improvement.

> if after["tree_sha256"] != frozen_record["tree_sha256"]:
>     raise ProtocolError("Phase-3 evaluation mutated frozen host memory")
> --- `benchmarks/osworld/pipeline.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> result = (phase1 if spec["phase"] == "phase1" else phase2)(spec)
> result["safe_to_grade"] = False
> --- `benchmarks/ale/worker.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

RTE-6 — Target/practice learning sequence. Trigger: Phase 2 fresh target attempt. The host obtains a local verification, invokes the same Actor's learning after FAIL or enabled PASS, updates memory, and invokes Curriculum. Default curriculum review can request practice even after PASS; fresh target testing follows actual practice. The alternate verifier-pass policy can terminate after PASS learning. STALLED causes a final fresh target test rather than becoming correctness. UNVERIFIED remains distinct. SRC-1 `core/self_evolving_loop.py:149-393`; `config/roles/target.yaml:1-98`; SRC-2 `docs/ARCHITECTURE.md:32-55`. Implementation conclusion status: wired; observed improvement conclusion status: uninspected. Memory admission itself is the specialist's separate canonical route. Immediate return is loop result with live environment, memory and termination reason; later read-back occurs through new Actor creation from memory, not inherited prior task history. Curriculum sees diagnosis/verdict, not a gold score. Human contribution is initial protocol configuration or intervention; computational roles propose execution, assessment, memory edits and practice. Host type/state conditions can veto malformed transitions. Persistence and recovery preserve identity and distinguish infrastructure failure. Guidance and content-directed criticism belong to RTE-4 and the memory reconciliation route, not the control loop alone. Guarantee strength: protocol for sequencing, no guarantee of improvement.

> should_learn = (
>     verification.verdict is TargetVerdict.FAIL
>     or (verification.verdict is TargetVerdict.PASS
>         and hooks.learn_on_pass))
> --- `core/self_evolving_loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> actor = hooks.fresh_target_actor(memory, target_cycles)
> --- `core/self_evolving_loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

#### RTE-7 — Phase 1 ordered learning publication

Source: SRC-1 `explore/phase1_wave.py`.

Route, implementation conclusion status: `wired`; benefit conclusion status: `uninspected`. After all branches finish, the harness iterates assignment order. Each branch Actor resumes its own task history, receives the latest canonical bank, distills and reconciles, then the host audits, journals and installs the result. The branch learned from the common pre-wave state during work but writes against the successively updated bank; publication is serialized, not a file-level union of independent deltas. A boundary rejection raises before installation. The whole wave waits for its branches; incomplete branch errors stop publication. No separate semantic judge verifies the learned claims. Generic reusable memory crosses task episodes.

> 
>             # Drain every future so successful siblings retain an owned handle
>             # for cleanup even when another branch fails. Never commit a partial
>             # wave merely because the failing future happened to return first.
>             if branch_errors:
>                 boundary = next((e for e in branch_errors
>                                  if isinstance(e, PracticeBoundaryError)), None)
>                 raise boundary or branch_errors[0]
> 
>             rendered_outcomes: list[str] = []
>             for index, _project, _episode_dir in assignments:
>                 branch = completed[index]
>                 if park_verified_branches:
>                     branch.desktop, branch.vm = vm_factory()
>                     _replay(hooks, branch.vm,
>                             str(branch.episode_dir / "candidates/cycle_001"))
>                 memory_record = _commit_branch_memory(
>                     branch=branch, hooks=hooks, memory_cfg=memory_cfg,
>                     canonical_memory_dir=memory_dir,
>                     journal_dir=journal_dir, corpus_path=corpus_path,
> --- `explore/phase1_wave.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> 
>     before = _read_memory_tree(str(canonical_memory_dir))
>     hooks.install_memory(
>         str(branch.episode_dir / "memory_before_commit"), before)
>     _push_canonical_memory(hooks, branch.vm, str(canonical_memory_dir))
>     history, _ = _run_free_phase(
>         hooks=hooks, vm=branch.vm, cfg=memory_cfg,
>         prompt=self_evolving_actor_memory_distillation_msg(
>             branch.terminal_outcome, branch.verifier_report),
>         role="ACTOR",
>         sink_root=str(branch.episode_dir / "memory_distillation"),
>         target=target_direction, history=branch.actor_history)
> --- `explore/phase1_wave.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>     candidate = _pull_terminal_memory(hooks, branch.vm)
>     accepted = hooks.audit_memory(
>         candidate, corpus_path,
>         str(canonical_memory_dir.parent / "audit_rejects.jsonl"),
>         authorized_instruction=target_direction, require_corpus=True)
>     if accepted != candidate:
>         raise PracticeBoundaryError("terminal memory failed the target boundary")
>     hooks.journal_memory(
>         str(journal_dir), branch.project_index, accepted,
>         {"kind": "phase1-parallel-terminal-memory",
>          "terminal_outcome": branch.terminal_outcome})
>     hooks.install_memory(str(canonical_memory_dir), accepted)
>     hooks.install_memory(
> --- `explore/phase1_wave.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

#### RTE-8 — Phase 2 target/practice distillation, reconciliation and admission

Source: SRC-1 `benchmarks/ale/learning.py`, `benchmarks/ale/practice.py`, `explore/charter.py`, `explore/commit.py`, `explore/practice_memory_recovery.py`, `explore/target_learning.py`.

Route, implementation conclusion status: `wired`; improved future capacity: `uninspected`. `_promote_learning` accepts the task Actor's history and final report, invokes distillation, reconciliation and separate diagnosis, then fetches candidate memory. Admission audits the candidate bank against the benchmark boundary, rejects any filtered candidate as a whole, journals, and installs it. OSWorld uses a word-shingle boundary test; ALE hooks replace the audit with its public-task-aware text validator. Neither is a truth test for causal lessons. The instruction asks the Actor to formulate interpretations, criticize stale or conflicting claims and revise them; the retained bytes could express addressable theories, but their actual granularity and rationale are unknown without a bank. Prompted content-directed criticism is wired; attributable improvement is not established.

>     actor_history, _ = _run_free_phase(
>         hooks=hooks,
>         vm=vm,
>         cfg=cfg,
>         prompt=memory_prompt,
>         role="ACTOR",
>         sink_root=str(episode_dir / "memory_distillation"),
>         target=audit_target,
>         history=actor_history,
>         audit_mode=audit_mode,
>     )
>     actor_history, _ = _run_free_phase(
> --- `explore/target_learning.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>         vm=vm,
>         cfg=cfg,
>         prompt=self_evolving_actor_memory_reconciliation_msg(),
>         role="ACTOR",
>         sink_root=str(episode_dir / "memory_reconciliation"),
>         target=audit_target,
>         history=actor_history,
>         audit_mode=audit_mode,
>     )
>     diagnosis, actor_history = _run_learning_diagnosis(
>         hooks=hooks,
> --- `explore/target_learning.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>         sink_root=str(episode_dir / "learning_diagnosis"),
>         target=audit_target,
>         history=actor_history,
>         audit_mode=audit_mode,
>     )
>     _atomic_text(episode_dir / "learning_diagnosis.md", diagnosis)
> 
>     candidate_memory = _pull_terminal_memory(hooks, vm)
> --- `explore/target_learning.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>     accepted_memory = hooks.audit_memory(
>         candidate_memory,
>         corpus_path,
>         str(lineage / "audit_rejects.jsonl"),
>         authorized_instruction=audit_target,
>         require_corpus=True,
>     )
>     if accepted_memory != candidate_memory:
>         raise PracticeBoundaryError("terminal memory failed the target boundary")
>     hooks.journal_memory(
>         str(journal_dir),
>         experience_index,
>         accepted_memory,
>         {"kind": experience_kind, "terminal_outcome": terminal_outcome},
>     )
>     hooks.install_memory(str(memory_dir), accepted_memory)
>     return accepted_memory, diagnosis, actor_history
> --- `explore/target_learning.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> Inventory the complete current durable-memory tree at {memory_root} and inspect
> every claim-bearing file. Reconcile the corpus as a whole against the trajectory
> and final Verifier evidence already in context. Look for conflicting assertions,
> unsupported causal explanations, stale environment assumptions, and conclusions
> broader than the observed evidence. Investigate when that is useful; otherwise
> narrow or qualify claims, preserve uncertainty, reorganize them, or remove them.
> Do not merely append this episode while leaving contradicted older advice stated
> as fact.
> 
> This is not a prescribed memory format or a request for a separate report. You
> still own the content, representation, retrieval strategy, scope, and stopping
> decision. There is no required claim table, schema, report, length, number of
> files, or number of turns. Neither the Verifier Agent nor Curriculum Agent grades
> the memory. Declare done when the complete memory you choose to carry forward is
> --- `explore/charter.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> def silent_audit(files: dict, corpus_path: str, reject_log: str,
>                  authorized_instruction: str = "",
>                  require_corpus: bool = False) -> dict:
>     """Return the accepted subset of ``files``. A file is rejected if it shares
>     any 8-gram shingle with a task instruction (task-leakage tripwire — should
>     ~never fire). Rejections are logged host-side ONLY: no agent feedback."""
>     if not os.path.exists(corpus_path):
>         if require_corpus:
>             raise RuntimeError(
>                 "target-aware memory audit requires the instruction corpus")
>         return files
>     corpus = set(json.load(open(corpus_path)))
>     if require_corpus and not corpus:
> --- `explore/commit.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>         return {
>             name: data
>             for name, data in files.items()
>             if not self.text(
>                 name + "\n" + data.decode("utf-8", "ignore"),
>                 authorized_instruction=authorized_instruction,
>             )
>         }
> 
> 
> def hooks_for(pool, corpus, public_task=None):
>     from core.loop import run_attempt
>     from explore.practice_loop import PracticeHooks
> --- `benchmarks/ale/practice.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

ALE target learning calls the same promotion mechanism with `actor_history=output.history`, its terminal verdict and verifier report. The outcome is recorded with `same_actor_context: True`; this code path is not evidence that every operation actually succeeded. A learning-recovery branch restores saved candidate/fixtures and the prior committed bank rather than rerunning completed work, then checks the saved transcript hash and remaining original budget before continuing.

>             episode.mkdir(parents=True, exist_ok=True)
>             learned, diagnosis, history = _promote_learning(
>                 hooks=hooks,
>                 vm=environment.vm,
>                 cfg=output.cfg,
>                 lineage=root,
>                 episode_dir=episode,
>                 experience_index=learning_updates,
>                 before_memory=memory,
>                 actor_history=output.history,
>                 terminal_outcome=verdict.value,
>                 verifier_report=report,
>                 target=direction,
>                 audit_mode="exam",
>                 emit=lambda kind, **payload: event(root, kind, payload),
>                 project_open=False,
>                 corpus_path=spec["corpus"],
>                 memory_dir=active_memory,
>                 journal_dir=root / "memory_journal",
>                 experience_kind="ale-phase2-target-" + verdict.value.lower(),
>                 target_visible_inputs=(),
> --- `benchmarks/ale/learning.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> def restore_learning_candidate(*, hooks, vm, episode_dir, fixture_dir, memory_dir,
>                                target, emit, saved):
>     """Restore archived inputs for learning; do not rerun Actor or Verifier work."""
>     require(saved['resume_kind'] == 'verified_memory', 'wrong pending memory state')
>     require(V._read_memory_tree(str(memory_dir)) == saved['before_memory'], 'canonical memory changed')
>     V._fresh_vm(hooks, vm, target)
>     V._replay(hooks, vm, str(fixture_dir))
>     V._replay(hooks, vm, saved['candidate_dir'])
>     V._push_canonical_memory(hooks, vm, str(memory_dir))
>     emit('PRACTICE_MEMORY_CANDIDATE_RESTORED', status='completed', project_open=True,
>          memory_phase_open=True, payload=dict(project_index=1, actor_replayed=False,
>              verifier_replayed=False, memory_committed=False))
>     return {key: saved[key] for key in ('terminal_outcome', 'verifier_report', 'actor_handoff',
>                                       'actor_history', 'before_memory')}
> --- `explore/practice_memory_recovery.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>         if first:
>             require(kwargs.get('initial_history') == meta['source_history'], 'recovery dropped Actor context')
>             require(sha(meta['source_transcript']) == meta['source_sha256'], 'failed transcript changed')
>             instruction += ('\n\nINFRASTRUCTURE CONTINUATION: The disposable learning VM became '
>                             'read-only before memory distillation completed. This fresh VM has the '
>                             'same saved candidate and prior committed memory. Your full work and '
>                             'failed learning history are retained. Previous private scratch files '
>                             'outside that candidate are absent. Continue this unfinished learning phase.\n')
> --- `explore/practice_memory_recovery.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

#### RTE-9 — Actor memory read-back and frozen evaluation

Source: SRC-1 `benchmarks/ale/worker.py`, `benchmarks/osworld/task.py`, `core/loop.py`, `explore/charter.py`.

Route, implementation conclusion status: `wired`; content activation and benefit: `uninspected`. On a new attempt, the harness imports the whole bank to the guest and automatically pushes a complete filename/size inventory into the opening prompt. This is coarse push of access metadata, not automatic relevance retrieval. The Actor is the actual requesting consumer: it can list, search, preview, read or execute through its Programs and view supported files through Looks. Requested file content is pull. Lifecycle nudges after verifier evidence, compaction, interruption recovery and stagnation only invite another request; they never choose file bodies or rank entries. No retrieval token budget, fixed top-k or privileged INDEX file exists in this interface. General tool/LLM context budgets still apply.

> def memory_preamble(listing: str = "") -> str:
>     """Expose frozen memory without choosing retrieval for the Actor Agent.
> 
>     The mechanical listing contains names and sizes only.  No file body is
>     injected into context and no filename, including ``INDEX.md``, is privileged.
>     Listing, searching, previewing, re-reading, and deciding relevance all remain
>     actions of the Actor Agent itself.
>     """
>     if listing:
>         files = f"\nCurrent durable-memory inventory ({len(listing.splitlines())} files):\n{listing}\n"
>         state = "The inventory is populated."
>     else:
>         files = "\nCurrent durable-memory inventory: empty (0 files).\n"
>         state = "There is no prior durable memory to retrieve in this attempt."
>     return f"""[YOUR MEMORY — notes from your own prior practice in this environment.
> They may be wrong, outdated, or inapplicable to this task: treat them as hints
> and verify against the live environment. They are available under ~/.memory/
> from the durable host snapshot: any local work-phase edits are
> discarded and cannot update durable memory. The complete file inventory is below.
> {state}
> First understand the task, then inspect memory as you judge useful: you may list,
> search across, preview, re-read, or fully read files in any order. Read a file as
> deeply as needed before relying on it. If new evidence changes your understanding,
> you become stalled, or earlier context is compressed, reconsider both previously
> useful and unread memory. You decide what to retrieve and how to use it.]
> --- `explore/charter.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> def _memory_revisit(cfg, event: str) -> str:
>     """Offer retrieval at lifecycle boundaries without choosing for the Actor.
> 
>     This is inert when no frozen memory is attached. It never names, ranks, reads,
>     or summarizes a memory file; the Actor Agent may ignore it entirely.
>     """
>     if not getattr(cfg, "env_memory_dir", ""):
>         return ""
>     return ("\n\n[MEMORY RETRIEVAL OPPORTUNITY] " + _MEMORY_REVISIT[event]
>             + " Durable memory remains available at ~/.memory. Consider re-reading "
>               "previously useful files or inspecting unread files that may now be "
>               "relevant; decide yourself what, if anything, to retrieve.")
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

Frozen evaluation imports memory but never writes guest edits back. OSWorld explicitly continues memory-OFF if upload fails; ALE raises on failed upload and verifies the original memory identity before and after evaluation. Therefore configured memory availability is not a universal guarantee of attachment. No inspection of a frozen snapshot proves the Actor read or used a particular claim.

>         if getattr(cfg, "env_memory_dir", ""):
>             # P2 eval flag: FROZEN practice memory rides along read-only —
>             # synced IN, never synced out (write-lock by construction). Only a
>             # mechanical recursive file inventory is shown. Retrieval is entirely
>             # the Actor Agent's decision; no body or filename (including INDEX.md)
>             # receives privileged treatment.
>             from explore.commit import push_memory       # noqa: E402 (our code,
>             from explore.charter import memory_preamble  # no benchmark contact)
>             if push_memory(vm, cfg.env_memory_dir):
> --- `benchmarks/osworld/task.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>                     for f in _files)
>                 opening_extra = memory_preamble(_ls)
>                 log.info("env memory attached (%s, files %d)", cfg.env_memory_dir, len(_files))
>             else:
>                 log.warning("env memory push FAILED — running memory-OFF")
>         ask_user = (de.user_simulator.respond
>                     if de.user_simulator is not None else None)
> --- `benchmarks/osworld/task.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>     memory = spec.get("input_memory")
>     if memory is not None:
>         verify_memory(memory)
>         if not push_memory(vm, memory["path"]):
>             raise RuntimeError("Frozen evaluation memory upload failed")
>         cfg.env_memory_dir = memory["path"]
>         opening = memory_preamble(_listing(_read_memory_tree(memory["path"])))
> --- `benchmarks/ale/worker.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>             session.close_executor()
>     if memory is not None:
>         verify_memory(memory)
>     sink.save_transcript(actor.build_system(cfg), history)
>     return {
>         "status": result.status,
>         "agent_result": asdict(result),
>         "safe_to_grade": True,
>         "memory": memory or "off",
>         "memory_writeback": False,
>     }
> 
> --- `benchmarks/ale/worker.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

#### RTE-10 — Curriculum read-back across projects

Source: SRC-1 `explore/charter.py`, `explore/phase1_boundary_recovery.py`, `explore/practice_loop.py`, `explore/unified_evolution.py`.

Route, implementation conclusion status: `wired`; effectiveness: `uninspected`. Before the next practice decision, the harness restores the canonical bank to a disposable guest copy and records its file count, bytes and hash. `read_only` permits Curriculum to request relevant bank files as evidence; `none` supplies an empty tree while preserving the Actor diagnosis channel and Actor learning. Read-only here concerns canonical writeback authority: discarded edits cannot update the bank. It should not be restated as a proven guest filesystem permission guarantee.

The harness automatically supplies project summaries, latest outcome, notes and prior conversation. Diagnosis explicitly asks for hypotheses and reasons and is copied verbatim into that outcome, so there is a wired later reader of rationale. Curriculum decides the next experience from this evidence. Those decisions can direct later tasks, but the remembered content enters as evidence rather than a binding routing rule. Across a project boundary, old image attachments stop being replayed; original message text plus a retrieval notice survives, while exact pixels remain in the raw transcript. This is a context projection rather than an LLM summary.

>                 curriculum_memory_dir = memory_dir
>                 if curriculum_memory_access == "none":
>                     # Use the ordinary full-replacement transport with an empty
>                     # source, including after a practice Actor used this VM.
>                     # Canonical memory and all Actor learning paths are unchanged.
>                     curriculum_memory_dir = lineage / "curriculum_empty_memory"
>                     curriculum_memory_dir.mkdir(exist_ok=True)
>                     if any(curriculum_memory_dir.iterdir()):
>                         raise PracticeInfrastructureError(
>                             "Curriculum ablation attachment must remain empty")
>                 _push_canonical_memory(hooks, vm, str(curriculum_memory_dir))
>                 session.turns += 1
>                 curriculum_sink = curriculum_dir / f"turn_{session.turns:03d}"
>                 attached_memory = _read_memory_tree(str(curriculum_memory_dir))
> --- `explore/unified_evolution.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

Shared quotation: see RTE-4.

>     memory_contract = (
>         "CURRENT ACTOR-OWNED DURABLE MEMORY is available at ~/.memory as a "
>         "disposable evidence copy. Inspect whichever files you judge relevant to "
>         "understand what the Actor Agent retained and which uncertainty should be "
>         "tested next. Do not edit, rewrite, approve, reject, or grade the memory; "
>         "the Actor Agent exclusively owns its contents and any changes you make "
>         "to this guest copy are discarded. Use memory only as evidence for "
>         "selecting the next experience."
>         if phase1_exploration or phase2_outcome
>         else ""
> --- `explore/charter.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>                 "terminal_outcome": practice["terminal_outcome"],
>                 "actor_handoff": practice["actor_handoff"],
>                 "verifier_report": practice["verifier_report"],
>                 "learning_diagnosis": diagnosis,
>                 "memory_before": _manifest(practice["before_memory"]),
>                 "memory_after": _manifest(learned),
>             }
>             _atomic_json(episode_dir / "outcome.json", record)
>             latest_outcome = _outcome_text({
>                 "label": f"PRACTICE PROJECT {project_index}",
>                 **record,
>             })
>             _atomic_text(episode_dir / "outcome.md", latest_outcome)
>             project_summaries.append(
>                 f"practice project {project_index}: "
>                 + practice["terminal_outcome"])
> --- `explore/unified_evolution.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>                 raise PracticeInfrastructureError(
>                     "persistent Curriculum visual observation is not text")
>             message["content"] = (
>                 content
>                 + "\n\n[HARNESS PROJECT-BOUNDARY SENSORY ARCHIVE: "
>                   f"{len(valid)} exact Look image(s) from the prior project remain "
>                   "losslessly stored in that turn's raw transcript but are not "
>                   "resent as pixels in this new project context. Reissue a Look "
>                   "whenever you judge those pixels relevant.]"
>             )
>             archived.append({
> --- `explore/practice_loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

A completed-boundary recovery chooses the latest saved Curriculum segment for the last wave, checks alternating role pairs, restores those messages and scopes old visuals. This is identifier-based historical state selection, with hashes and run identity controlled by the recovery workflow; it is not semantic search.

>         transcripts = sorted((lineage / "curriculum" / f"wave_{last_wave:03d}").glob(
>             "segment_*/transcript.json"))
>         _require(bool(transcripts), "completed Curriculum context is missing")
>         last_transcript = max(transcripts, key=lambda p: int(p.parent.name.split("_")[1]))
>         messages = json.loads(last_transcript.read_text()).get("messages")
>         _require(isinstance(messages, list) and bool(messages)
> --- `explore/phase1_boundary_recovery.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>         history, _ = _scope_prior_curriculum_visuals(messages)
>         outcomes = (lineage / "waves" / f"wave_{last_wave:03d}" / "outcomes.md").read_text()
> --- `explore/phase1_boundary_recovery.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

#### RTE-11 — Context folding, synthesis and resumed Actor

Source: SRC-1 `config/roles/target.yaml`, `core/actor.py`, `core/loop.py`, `explore/practice_loop.py`.

Route, implementation conclusion status: `wired`; summary faithfulness and improvement: `uninspected`. Target config enables 80-pair maximum verbatim history, 500,000-character keep budget, 900,000/500,000 high/low marks, 10-pair fold batches and 500,000-character worklog cap. The floor is six recent pairs. When eligible history crosses the threshold, older pairs feed a summarizer together with the previous worklog. Each input message is rendered as first 1,500 plus last 2,500 characters if long; thus a comment calling general transport lossless must not be generalized to summarization. Output is capped, with deterministic digest fallback if empty. Each folded log is saved. The next Actor call receives unchanged task text, the complete retained log and the unfolded tail. This is automatic coarse push, not a memory-file request.

> # Lossless long-context transport.
> trace_head: 0
> trace_tail: 0
> history_keep_pairs: 80
> keep_chars: 500000
> ctx_high_water: 900000
> ctx_low_water: 500000
> fold_batch: 10
> worklog_max_chars: 500000
> --- `config/roles/target.yaml` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> def _fold_input(content, head: int = 1500, tail: int = 2500) -> str:
>     """v21 (context): render a folded message as head+tail (was a [:4000] PREFIX that
>     hid the last ~4k of a fat trace — where tracebacks and final error lines land)."""
>     s = str(content)
>     if len(s) <= head + tail:
>         return s
>     return s[:head] + "\n…[trace middle elided]…\n" + s[-tail:]
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>     batch = history[covered * 2:(covered + n_pairs) * 2]
>     rendered = "\n\n".join(
>         f"[{'YOU' if m['role'] == 'assistant' else 'ENV'}]\n"
>         + _fold_input(m["content"]) for m in batch)
>     out = chat(cfg.model, SUMMARIZER_SYSTEM,
>                f"CURRENT LOG:\n{summary or '(empty)'}\n\nOLDER TURNS TO FOLD IN:\n"
>                f"{rendered}\n\nOutput the updated log only.",
>                max_tokens=cfg.max_tokens, temperature=0.0,
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>     cap = cfg.worklog_max_chars
>     if out.strip():
>         summary = _cap_worklog(out.strip(), cap)          # v21: line-boundary, keep top
>     else:                                   # summarizer starved -> deterministic fallback
>         combined = summary + "\n" + _digest_lines(batch)
>         if len(combined) > cap:                           # keep the TAIL (newest) here,
>             b = combined.find("\n", len(combined) - cap)  # at a line boundary
>             combined = combined[b + 1:] if b >= 0 else combined[-cap:]
>         summary = combined
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>     covered += n_pairs
>     if sink is not None:
>         sink.save_summary(turn_no, summary)
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>         if cfg.history_keep_pairs > 0:      # compaction = model-written WORK LOG (the
>             before_fold = covered
>             summary, covered = _llm_operation(
>                 "Actor work-log compaction",
>                 lambda: _fold_summary(                          # only mode
>                     history, covered, summary, cfg, sink, res.turns))
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>                      # survive only as a summarizer paraphrase (some runs lost it).
>                      "TASK (verbatim, unchanged — this is the actual goal):\n"
>                      + instruction + "\n\nWORK LOG — your running summary of earlier "
>                      "turns (full details live in the machine; re-probe if you need "
>                      "specifics):\n" + summary}]
>                    + history[covered * 2:]) if summary else history
>         else:
>             ctx = history                   # 0 = full history (short-horizon default)
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

A stalled attempt may synthesize a log from its final 60 messages; a strategy pivot asks for a materially different approach from the stalled worklog/final turns. The new attempt gets that handoff via `opening_extra`, and the pivot path saves it explicitly. Non-pivot handoff is preserved in the next attempt's transcript. Reasons are requested in the worklog and the post-mortem prompt; later Actor context reads whatever survives the caps. No semantic checker verifies that those reasons are faithful. This route is per-task, online trace learning. Practice `_phase_cfg` forces `history_keep_pairs=0` and `max_resumes=0`, so do not attribute target folding to the practice roles.

>     discarded history builds the handoff the folding would have built."""
>     tail = history[-60:]
>     rendered = "\n\n".join(
>         f"[{'YOU' if m['role'] == 'assistant' else 'ENV'}]\n" + _fold_input(m["content"])
>         for m in tail)
>     out = chat(cfg.model, SUMMARIZER_SYSTEM,
>                "CURRENT LOG:\n(empty)\n\nOLDER TURNS TO FOLD IN:\n" + rendered
>                + "\n\nOutput the updated log only.",
>                max_tokens=cfg.max_tokens, temperature=0.0,
>                reasoning_effort=cfg.reasoning_effort,
>                reasoning_max_tokens=getattr(cfg, "reasoning_max_tokens", 0),
>                **_provider_request(cfg))
>     return _cap_worklog((out or "").strip(), cfg.worklog_max_chars)
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>     parts = ["A task attempt just stalled without changing any files. "
>              "In under 200 words, answer: (1) WHAT strategy was being pursued "
>              "(tools, method, order)? (2) WHERE exactly did it get stuck? (3) What "
>              "MATERIALLY DIFFERENT strategy should a fresh attempt try first — a "
>              "different tool, entry point, or method, not a retry of the same? "
>              "Plain text only."]
>     if worklog.strip():
>         parts.append("WORK LOG of the attempt:\n" + worklog.strip()[:8000])
>     if tail.strip():
>         parts.append("FINAL TURNS of the attempt:\n" + tail.strip()[:6000])
> --- `core/actor.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>         wl = res.worklog if cfg.resume_with_worklog else ""
>         if not wl and getattr(cfg, "resume_synthesize_worklog", False) and history:
>             wl = _call_with_transport_pause(
>                 lambda: _synthesize_worklog(history, cfg), cfg,
>                 label="resume work-log synthesis",
>                 on_pause=_record_resume_transport_pause)  # never hand off empty-handed
>         if cfg.strategy_pivot and res.surface_delta == "":   # v18: nothing banked -> pivot
>             review = _call_with_transport_pause(
>                 lambda: _strategy_review(history, res.worklog, cfg), cfg,
>                 label="resume strategy review",
>                 on_pause=_record_resume_transport_pause)
>             extra = pivot_handoff_message(review, wl)
>             tag = f"pivot{n}"
>         else:                                  # banked or unknown -> v15 continuation
>             extra = handoff_message(wl)
>             tag = f"resume{n}"
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>             _verifier_session_identity(rcfg), VerifierSession())
>         if verifier_session_prepare is not None:
>             verifier_session_prepare(rcfg, active_verifier_session)
>         sink2 = ArtifactSink(_os.path.join(sink.root, f"resume{n}"))
>         if tag.startswith("pivot"):
>             sink2.save_summary(0, "PIVOT SELF-REVIEW:\n" + extra)
>         r2, h2 = run_attempt(instruction, vm, rcfg, sink2, iters_budget=iters_left,
>                              wall_budget=wall_left, opening_extra=extra,
>                              verifier_session=active_verifier_session,
>                              surface_baseline=surface_baseline,
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> def _phase_cfg(base_cfg, required_path: str = ""):
>     cfg = copy.deepcopy(base_cfg)
>     # These switches define the generic Agent-owned transport. Model identity,
>     # sampling, tool access, and emergency ceilings remain exactly configured.
>     cfg.practice_mode = True
>     cfg.independent_verify = False
>     cfg.agent_decided_stop = True
>     cfg.practice_done_requires = required_path
>     cfg.history_keep_pairs = 0
>     cfg.max_resumes = 0
>     return cfg
> --- `explore/practice_loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

#### RTE-12 — Verifier continuity and selective semantic replay

Source: SRC-1 `core/loop.py`, `core/verifier.py`.

Route, implementation conclusion status: `wired`; operational success: `uninspected`. A Verifier session accumulates its own history across inspections and Actor resumes on one target. The harness selects a session by agentic configuration path or legacy model identity; a model/role switch therefore does not automatically inherit another model's private reasoning. `run_attempt` receives that selected history as `initial_history`. The legacy flag-off path instead uses fresh context.

On actionless decoder failure, checkpointing keeps history through the latest real Program/Look and carries its following observation separately. Semantic replay removes actionless narration while preserving actual actions, results and valid action reasoning; original raw transcripts remain available for audit. These deterministic projections derive a later context, but do not constitute semantic synthesis or prove new knowledge. They supply retained evidence to later validation work; they do not make previous probes current or make telemetry a decision rule. This is current-task continuity, not a cross-task Verifier memory bank.

> def _verifier_session_identity(cfg) -> tuple[str, str]:
>     """Conversation identity for a persistent Verifier Agent.
> 
>     A role/model switch must not feed one model another model's private reasoning
>     history. Same-identity Actor resumes keep the exact existing session.
>     """
>     agentic = str(getattr(cfg, "agentic_verifier_config", "") or "")
>     if agentic:
>         return "agentic", agentic
>     return "legacy", str(getattr(cfg, "verifier_model", "") or cfg.model)
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

Shared quotation: see RTE-11.

> def _agentic_substantive_checkpoint(previous: list, raw: list):
>     """Keep one Verifier Agent's history through its last real machine action.
> 
>     ``run_attempt`` appends complete user/assistant pairs. A Program or Look is a
>     substantive action; narration that merely promises a future action is not. The
>     environment observation produced by the last action is the following user
>     message, so return its complete text and durable image attachments separately
>     for lossless delivery in the recovery prompt.
> 
>     The complete ``raw`` history remains archived by the segment's ArtifactSink.
>     This helper only chooses what is allowed back into the live semantic context.
> --- `core/verifier.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> def _agentic_semantic_replay(raw: list):
>     """Re-encode all real actions and their results without actionless turns.
> 
>     This is an event-triggered decoder recovery, not context-length compaction: no
>     Program, Look, program trace, textual look result, or valid action reasoning is
>     truncated or summarized. Repetitive narration/nudges that never caused a machine
>     action remain in the archived raw transcripts but are removed from live context.
>     """
> --- `core/verifier.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>             result, raw_history = run_attempt(
>                 prompt, vm, verifier_cfg, segment_sink,
>                 wall_budget=remaining,
>                 **({"iters_budget": remaining_iters} if remaining_iters is not None else {}),
>                 initial_history=current_history,
>                 continue_context=continuing,
>                 terminal_handoff_ready=terminal_report_ready,
> --- `core/verifier.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>     vsys = build_verifier_system(cfg)                    # v35: config-true mechanics
>     continuity = session is not None and getattr(cfg, "verifier_continuity", False)
>     history: list = session if continuity else []
> --- `core/verifier.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

The checkpoint/replay branch does qualify as trace learning under the comparison contract. It automatically produces a changed behavior-shaping context: actionless turns disappear, retained action/result pairs are re-encoded, and pending evidence is carried into a subsequent recovery call. This is more than storing and replaying an unchanged raw log. The transformed `current_history` replaces the persistent session and is passed as `initial_history` into the next Verifier `run_attempt`. That subsequent segment persists its full history through `save_transcript`; `agent_decided_stop` is forced true for this role. Thus the derived projection is durable in the later segment transcript as well as retained across live calls. The `recovery.json` sidecar alone is metadata, not the derived content, and a final projection with no later call is not claimed to have been consumed.

Trace-learning mapping for this route: sources `session-logs` and `tool-traces`; scope `per-task`, established by the repeated inspection of the same target/candidate lifecycle; timing `online`, triggered by completed segments or actionless recurrence; form includes natural-language observations/reasons and symbolic programs/message structure, while retained image payloads prevent an exhaustive normalized form assignment. No new proposition or semantic synthesis is required for this mapping. The criterion is the retained transformation and later behavior-shaping use. Reasons survive where they are part of the preserved valid action reasoning; later Verifier context receives them. No faithful use or benefit is demonstrated.

>             if recurrent and not advanced and not semantic_replay_active:
>                 replayed, replay_observation, replay_images, replay_turn = \
>                     _agentic_semantic_replay(current_history)
>                 if replayed and len(replayed) < len(current_history):
>                     current_history = replayed
>                     pending_observation = (
>                         replay_observation or pending_observation)
>                     pending_images = replay_images or pending_images
>                     pending_turn = replay_turn or pending_turn
>                     semantic_replay_active = True
>                     semantic_replay_activated = True
> --- `core/verifier.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>             if isinstance(persistent, VerifierSession):
>                 persistent.pending_observation = pending_observation
>                 persistent.pending_images = list(pending_images)
>                 persistent.pending_turn = pending_turn
>                 persistent.transport_recurrence = semantic_replay_active
>             persistent[:] = current_history
> 
>             # The raw transcript already contains every discarded byte. This compact
>             # sidecar makes the recovery boundary directly auditable without copying
>             # or truncating any conversation content.
> --- `core/verifier.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>     verifier_cfg = load(getattr(cfg, "agentic_verifier_config", ""))
>     # Generic handoff transport, matching self-evolution's Agent phases.  These
>     # switches do not choose how to investigate or when the evidence is sufficient.
>     verifier_cfg.practice_mode = True
>     verifier_cfg.independent_verify = False
>     verifier_cfg.agent_decided_stop = True
>     verifier_cfg.max_resumes = 0
> --- `core/verifier.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

>     res.wall_secs = time.time() - t0
>     res.worklog = summary
>     if agent_decided_stop and sink is not None:
>         sink.save_transcript(system, history)
>     return res, history
> --- `core/loop.py` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

### Claims

CLM-1 — Broad-then-deep exploration is intended to produce reusable knowledge through Curriculum, Actor and Verifier interaction, followed by frozen memory reuse. Conclusion status: claimed, with wiring supported by RTE-1, RTE-3, RTE-4, RTE-5, RTE-6 and the integrated memory routes. SRC-2 `README.md:55-113`.

> The paper's central strategy is **broad-then-deep exploration**: first acquire
> diverse experience, then investigate hard cases, hidden constraints, and boundary
> conditions.
> --- `README.md` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

CLM-2 — Reported aggregate performance improves from 71.97 to 78.98 mean partial-credit percent on the stated OSWorld corpus and 83.75 to 84.82 on ALE. Conclusion status: claimed; evidence layer: reported operation. SRC-2 `README.md:118-144`; `docs/PAPER.md:50-96`. These are strongest as reported bundle-level gains. They mix retained baseline entries and selected RSI runs/checkpoints with differing budgets, and the stage cohort was selected for improvements. Neither independently observed operation nor causal attribution to memory reconciliation, theory criticism, or any one component is established here.

> Selected runs, checkpoints, budgets, and evaluation scopes are not fully
> matched. These tables are manuscript-reported results, not a new result-file
> audit or a matched-protocol leaderboard submission by this release.
> --- `docs/PAPER.md` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

CLM-3 — Model parameters remain fixed during exploration/downstream tasks. Conclusion status: claimed. SRC-2 `README.md:55-63`. CMP-2 and CMP-3 establish inference-facing calls and mutable model identities, not provider-side weight immutability. Fixed parameters would still permit learning through retained procedures and knowledge.

> Model parameters stay fixed
> throughout exploration and downstream task execution.
> --- `README.md` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

### Evidenced absences

#### ABS-1 — No retained recall-dependence experiment in the inspected boundary

Evidenced absence, conclusion status: `absent`, bounded to the enumerated and keyword-searched code/text surfaces below. No qualifying retained execution evidence of recall dependence was identified there. This does not establish absence in the uninspected PDF, media, manuscript sources referenced by the documentation, external run stores or undocumented experiments. The tree enumeration found no `results/` entries and identified `docs/RSIAgent.pdf` as present but outside the commissioned evidence. Test names include memory retrieval lifecycle, Curriculum memory access, history hygiene and role continuity; test code is not an observed assay. The manuscript-facing documentation expressly describes stage comparisons as not a new result-file audit and acknowledges unmatched scopes and separate historical controls. Those reports do not establish a recall-faithfulness experiment for this pinned implementation. The report assigns `faithfulness_tested: no` only under that retained-evidence definition; it does not assert that nobody ran such an experiment elsewhere.

Shared quotation: see CLM-2.

> The four-task stage comparison uses an exploratory cohort selected for recorded
> improvements: T080, T085, T089, and T106. `appendix/ablation_protocol.tex` describes
> the historical baselines, single-stage scores, and two historical evaluation
> draws averaged for each full-RSI result.
> 
> The broad-only condition evaluates preserved BRS memory directly. The deep-only
> condition starts with empty memory and allows **at most two practice projects
> selected by the Curriculum Agent**; target attempts and memory updates are additional.
> The Actor Agent retains memory access, while the Curriculum Agent does not
> directly read its memory in those comparisons.
> --- `docs/PAPER.md` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

> Those ablations used separate experiment controls. The released default instead
> uses `curriculum_review` and a read-only memory view for the Curriculum Agent, with no
> --- `docs/PAPER.md` @ `a9e56263f6deaa493496ad6b155fe24bf131bc12`

The reproducible search record is:

```bash
git --no-replace-objects -C related-systems/AetherLabsAI--RSIAgent ls-tree -r --name-only a9e56263f6deaa493496ad6b155fe24bf131bc12
git --no-replace-objects -C related-systems/AetherLabsAI--RSIAgent ls-tree -r --name-only a9e56263f6deaa493496ad6b155fe24bf131bc12 -- README.md docs tests/test_memory_retrieval_lifecycle.py tests/test_curriculum_memory_access.py results
git --no-replace-objects -C related-systems/AetherLabsAI--RSIAgent grep -n -i -E 'faithful|ablat|recall|dependence|memory.off|memory.on' a9e56263f6deaa493496ad6b155fe24bf131bc12 -- README.md 'docs/*.md' tests/test_memory_retrieval_lifecycle.py tests/test_curriculum_memory_access.py
```

The first command enumerated the complete tracked tree. The second returned README, documentation, documentation media/PDF/manifest and the two named tests, with no results entries. The grep returned README's stage-ablation mention; `docs/PAPER.md`'s faithful-PNG statement and stage-ablation section; and the test of preventing a changed recovery access setting. Each relevant prose hit was read in bounded commit-addressed ranges. The tests were inspected at `tests/test_memory_retrieval_lifecycle.py` lines 1–130 and `tests/test_curriculum_memory_access.py` lines 1–135: these use fake model/VM/hooks and check delivery/visibility/state boundaries, not retained runs establishing dependence on recalled semantic content. The commands supply a bounded search, not proof that every possible phrase or binary artifact was inspected. The reported `no` means the required observed/causal evidence is not established in this analysis's evidence set.

Source: SRC-1 complete tree and named tests; SRC-2 `README.md`, `docs/PAPER.md`. Other uninspected routes are limitations, not absence claims.

### Behavioral-authority paths

BAP-1 — Consumer Actor/Verifier; channel task/role prompt; force instruction; horizon one task or role session. OBJ-1 constrains intended work through RTE-1/RTE-3. Conclusion status: wired; activation uninspected. SRC-1 `core/loop.py:546-608,962-1018`.

BAP-2 — Consumer host transition logic, Actor and Curriculum; channel OBJ-3 report/token; force validation and operational admission for completion/revision/learning; horizon candidate/target cycle. Local evidence does not grant universal epistemic warrant. Conclusion status: wired. SRC-1 `core/verifier.py:1198-1274`; `core/self_evolving_loop.py:241-332`.

BAP-3 — Consumer host practice controller; channel Curriculum terminal token/project; force routing; horizon next project or target retry. Report justification is advisory context, while token dispatch governs sequencing. Conclusion status: wired. SRC-1 `explore/unified_evolution.py:582-635`.

BAP-4 — Consumer host reporter/operator; channel OBJ-4 external score; force measurement for benchmark reporting; horizon completed evaluation. Agent behavioral authority is inapplicable within the inspected protocol, which seals measurement after learning/execution. Conclusion status: wired. SRC-1 `benchmarks/osworld/pipeline.py:590-628`; `benchmarks/ale/worker.py:80-96`.

#### BAP-5 — Advisory memory and continuity authority

Source: SRC-1 .

Behavioral-authority path, implementation conclusion status: `wired`. Actor bank hints and WORK LOG/diagnosis enter through user context or requested tool results, affecting the Actor's and Curriculum's judgments. Curriculum's current bank copy is explicitly evidence for selecting an experience. Verifier consumes its own earlier reasoning/evidence as context while current-candidate evidence freshness remains separate. The static role instructions bind behavior but are outside the accumulated-memory profile. A remembered claim is not mechanically promoted to validation authority by being copied into memory. The actual authority of an arbitrary learned executable remains unknown because no payload and invocation trace is retained.

Evidence anchors are retained once above on RTE-9, RTE-10 and RTE-12. The distinction rests on the exact phrases “treat them as hints”, “Use memory only as evidence” and the current-candidate freshness rule.

## Runtime account

An operator selects an OSWorld or ALE study and role/provider configuration. In learning mode, a Curriculum proposes practice or a fresh target runs; the Actor gets task requirements, a reset environment and available memory, then calls the configured model with its evolving history. Model-selected programs act on the guest; visual calls return either images or a separate model's report. The Verifier uses an independent conversation and selected isolation boundary to judge the resulting candidate. A grounded terminal report permits same-Actor memory learning; the Curriculum receives diagnosis and outcomes to select another task. New independent attempts reset task interaction/environment while carrying admitted memory. Frozen evaluation disables learning and subsequently calls the external grader (RTE-1, RTE-3, RTE-4, RTE-5, RTE-6).

This is a bounded experimental/curriculum runtime, not evidence of unattended arbitrary open-request deployment. Independent runtime-client extension hooks can replace program execution, rendering, user responses, verification routing and task environments. Those capabilities delimit the built-in guarantees: callers providing hooks must preserve the contracts. The Actor has code execution, not just a fixed named-tool catalog; direct service calls inherit the guest's connectivity and grant. The Verifier's rollback cannot undo mutations of remote services (SRC-2 `docs/ARCHITECTURE.md:15-20`). The inspected ordinary program dispatch proceeds without a human approval transition; this describes RTE-1, not every external deployment. Operator configuration or interruption is different from per-action approval.

Four static forcing cases distinguish the important controls:

1. Verifier isolation fails: the trusted executor/rollback error prevents safe return for grading; it is infrastructure failure, not candidate FAIL. RTE-3. A regex-screened Actor done check has a different boundary (RTE-2), so the Verifier guarantee cannot be generalized.
2. Target PASS occurs: under curriculum review it may still lead to practice; if practice occurs, a fresh target attempt is required. Curriculum readiness is not correctness. RTE-4 and RTE-6.
3. Frozen memory changes: the Phase 3 hash comparison rejects the boundary record. Upload behavior differs: OSWorld task runner can continue memory-OFF after a failed guest upload; ALE evaluation raises. Thus host hash stability alone does not establish that a particular guest used memory. RTE-5 and integrated transport records.
4. Provider/controller or grader fails: uncertain Actor actions are not replayed; completed grading candidates are preserved for retries. Unverified or stalled states stay distinct from success. RTE-1, RTE-5 and RTE-6.

No dynamic check planned. Considered end-to-end VM runs, live-provider calls and isolated regression tests. The first two require benchmark images, external services and credentials not provisioned for this analysis; tests alone would not establish deployed guarantees or learning benefit. Static source tracing suffices for the wired conclusions reported here. No attempted check is represented as an observed outcome.

## Lens scoping

### Memory/context scope

Full lens commissioned against SRC-1 and SRC-2 and the complete frozen boundary. Trigger: CLM-1 and the retained-memory/continuation routes. The specialist inventories learned file trees, read-back, Curriculum and Verifier continuity, recovery and trace-fed summarization. Static shipped instructions and task products are excluded from the memory comparison unless changed through use and consumed later. Actual payload semantics and model activation remain bounded by the absence of run artifacts.

### Epistemic scope

Full lens invoked locally using `kb/instructions/analyse-external-system-epistemic-architecture.md`. Trigger: CLM-1 and CLM-2, RTE-3 verification and RTE-4 theory-directed search, and the integrated memory reconciliation route. Assessed: candidate generation, local checks/verdicts, memory hypotheses and their operational admission, curriculum decisions, and sealed measurement. Excluded: truth of benchmark oracle implementations, unobserved internal model reasoning and uninspected production runs. The lens annotates canonical IDs and never substitutes architectural implementation for observed candidate state.

## Lens outputs

### Memory/context lens

The fresh specialist inventoried OBJ-6, OBJ-7, OBJ-8, OBJ-9 and OBJ-10 and RTE-7, RTE-8, RTE-9, RTE-10, RTE-11 and RTE-12. Findings and minimum source support are retained on those canonical records; the local report is provenance only. Actor-owned file memory crosses tasks, while role histories, worklogs and replay projections preserve continuity within a task or target lineage. A whole inventory is pushed; the Actor and enabled Curriculum choose which file bodies to pull. Neither inventory presence nor successful copying establishes activation.

RTE-7/RTE-8 stage experience-driven learning and whole-corpus reconciliation before host publication. The host audits leakage/transport boundaries, not truth of the memory. Rationale is discretionary in OBJ-6, explicitly requested in OBJ-10 and carried to Curriculum through RTE-10, and explicitly requested in OBJ-9 and supplied to the later Actor through RTE-11. Reconciliation is a wired prompt procedure for finding conflicting or overbroad claims; actual formulated criticism and resulting improvement require an instance trace.

The comparison includes automatic durable trace-fed writing on RTE-7, RTE-8, RTE-10, RTE-11 and RTE-12. RTE-12 qualifies because it changes the live context and persists the selected projection in a later segment transcript; merely preserving raw history would not suffice. Source/scope/timing therefore include session-logs, tool-traces and trajectories; per-task and cross-task; online and staged. Fixed natural-language worklogs coexist with unconstrained bank bytes, symbolic projections and image payloads, so aggregate representation, distilled form, behavioral force and curation remain not-determinable. Known file/in-memory storage, automatic writing and pull/push direction preserve that same scope. Coarse push supplies inventories and current context; identifier push actually selects a role-specific retained Verifier session. No embedding or judgment-based push is inferred from model-selected pull.

ABS-1 limits faithfulness-tested no to the retained evidence inspected here. It does not claim that no outside experiment exists, and no test-code fixture is elevated to an observed semantic recall assay.

### Epistemic lens

#### 1. Source-and-claim boundary

See SRC-1 and SRC-2 and Boundary and evidence. The question is what verification and memory reconciliation license for later reliance, and whether theory criticism demonstrably improves capacity. CLM-1 supplies the reusable-knowledge claim; CLM-2 supplies only reported outcome improvement. The assessed and excluded routes are named in Epistemic scope.

#### 2. Epistemic-object overlay

OBJ-1 carries imported or authored requirements; task requests are normative rather than assertions of achieved correctness. OBJ-2 is a candidate product/state, not automatically a truth-apt theory. OBJ-3 contains truth-apt assessment and evidence statements. OBJ-4 imports an external measurement; OBJ-5 contains proposed tests and Boolean check results. Retained memory, diagnoses and Curriculum hypotheses are the specialist objects; their individual propositions are unavailable, so the transformation of any particular learned assertion is indeterminate between reshaping, derivation and ampliative conjecture. Free-form output may include policies without truth-apt content; storage labels do not decide this.

#### 3. Authority-route ledger

| route/function | architectural status | target and content/update relation | evaluator, timing and result | epistemic license | operational and behavioral consequence | limits |
|---|---|---|---|---|---|---|
| RTE-1: content transformation | implemented | OBJ-2; non-truth-apt policy/content update: guest task work, with task-dependent possible truth-apt output | Actor under OBJ-1 produces candidate before verification | no general claim warrant from generation | guest effects through BAP-1 | specific candidate contents uninspected |
| RTE-2: check/evidence production | implemented | OBJ-5 against OBJ-2; no content change to checked candidate intended | program/regex and PASS/FAIL token logic, at Done | only output semantics of the authored probe | repair/continuation or request independent inspection | no proof of probe adequacy or universal read-only behavior |
| RTE-3: check/evidence production | implemented | OBJ-3 about OBJ-2; truth-apt transformation: indeterminate | independent model chooses evidence investigations and forms report | locally claimed task compliance, conditioned on selected evidence | supplies BAP-2 | model assessment is not a supplied answer oracle |
| RTE-3: disposition/acceptance | implemented | OBJ-3; no content change | lexical report validity plus local verdict permits revision/termination | report-token validity does not validate explanations | BAP-2 changes progression | acceptance criterion is task requirements interpreted by Verifier, not general theory truth |
| RTE-4: content transformation | implemented | Curriculum hypotheses/diagnosis; truth-apt transformation: indeterminate | model proposes bottleneck account and discriminating task from evidence | proposed explanation, not demonstrated cause | guides project/routing through BAP-3 | no produced instance available |
| RTE-4: operational admission/selection/consumption | implemented | project and readiness token; no content change | model semantic decision plus host format/boundary checks | readiness is not correctness | dispatches practice or returns to target | no independent expected answer |
| RTE-5: check/evidence production | implemented | OBJ-4 assessment of OBJ-2; acquisition/import | external official evaluator after execution | benchmark-domain measurement, conditional on excluded oracle | host reporting BAP-4 | no agent feedback; corrections/variants must be distinguished |
| RTE-6: operational admission/selection/consumption | implemented | learned memory and next task; no content change in orchestration itself | local PASS/FAIL and explicit stop policy | grounded experience eligibility, not memory truth | invokes memory update and new consumer | full memory write checks are in integrated records |

| RTE-7/RTE-8: content transformation | implemented | OBJ-6; truth-apt transformation: indeterminate, including possible conjectures and policy changes | same Actor distills and reconciles after local verification | prompt demands grounded, qualified claims; no automatic truth certification | produces candidate future memory | no actual learned bank available |
| RTE-7/RTE-8: check/evidence production | implemented | OBJ-6; no content change | host leakage/path/transport checks | boundary compliance only | can veto publication | does not check causal lesson truth |
| RTE-7/RTE-8: disposition/acceptance | implemented | OBJ-6; no content change | complete learning and boundary acceptance | operational admission, not epistemic acceptance of every assertion | replaces canonical memory | Actor owns semantic stopping |
| RTE-7/RTE-8: retention | implemented | OBJ-6 and OBJ-7; no content change | journal and atomic tree install | byte lineage/recovery | permits later RTE-9/RTE-10 use | retention is not post-acceptance epistemic integration |
| RTE-9/RTE-10: operational admission/selection/consumption | implemented | OBJ-6, OBJ-7, OBJ-8, OBJ-10; no content change | requested reads plus automatic inventory/outcome/context supply | advisory/evidential BAP-5 | influences later Actor/Curriculum judgment if used | activation uninspected |
| RTE-11: content transformation | implemented | OBJ-9; truth-apt transformation: indeterminate | summary intended as non-ampliative reshaping; strategy review can propose new policy | no independent fidelity test | later Actor continuation through BAP-5 | caps and model invention remain possible |
| RTE-11: retention | implemented | OBJ-9; no content change | per-fold files and continuation transcript | provenance for retained summary | later calls receive stored guidance | no correctness acceptance |
| RTE-12: content transformation | implemented | OBJ-8; non-ampliative reshaping of selected action/result history | symbolic checkpoint/replay rules | preserved selected evidence, not fresh candidate evidence | recovery context through BAP-5 | image payload/operation uninspected |
| RTE-12: retention | implemented | OBJ-8; no content change | session update and later segment transcript | inspectable continuation lineage | role-matched history read-back | no inference of better validation from retention |

Memory object dispositions: OBJ-6 is indeterminate between preserved experience, entailed interpretation, ampliative explanation and non-truth-apt procedures; source lineage and admission are RTE-7/RTE-8, later consumers RTE-9/RTE-10, and individual claim warrant is uninspected. OBJ-7 manifests/inventories are symbolic derivations from bytes and paths; discovery lifecycle not applicable, byte identity does not entail content truth. OBJ-8 raw evidence is acquired/imported and its replay projection is non-ampliative reshaping under RTE-12; discovery lifecycle not applicable to this transport transformation. OBJ-9 intends a faithful summary but actual semantic preservation is indeterminate without input/output evidence; strategy-review suggestions also remain uninspected. OBJ-10 contains proposed causal hypotheses and Curriculum notes, but actual instances are unavailable; preservation versus ampliation is indeterminate. For OBJ-6, OBJ-9 and OBJ-10, observed candidate state is no instance observed for production, criticism, acceptance and later use. The code does not supply a candidate-linked discovery lifecycle merely by having these routes.

#### 4. Per-object lifecycle disposition

OBJ-3 assessment is an indeterminate truth-apt transformation: source observations are retained, but no actual report establishes whether a conclusion preserves, derives from or goes beyond them. Checking and disposition are implemented by RTE-3; observed candidate state: no instance observed. Its operative verdict is not proof that each reported explanation was tested. OBJ-4 is acquisition/import: discovery lifecycle not applicable; external source warrant is uninspected. OBJ-5's PASS Boolean is entailed by the implemented token rule, conditional on actual probe output; discovery lifecycle not applicable, and task-correctness warrant does not follow from that Boolean alone.

For the specialist's memory/diagnosis/Curriculum objects, individual content edges remain indeterminate. The architecture supports formulation, criticism and revision, but there is no observed instance that can be assigned conjecture, test, acceptance or integration. Observed candidate state for each is no instance observed. Retention and operational reuse are implemented, without establishing epistemic acceptance of each claim. If an actual memory rule is ampliative, its lifecycle would require a candidate-linked theory, consequence, test, admission criterion and later use; these are not supplied by storage or the existence of a reconciliation prompt.

No lifecycle record for OBJ-1: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-1, RTE-4. No lifecycle record for OBJ-2: no identified candidate truth-apt output in the inspected task-product boundary; relevant direct-adaptation or update routes: RTE-1. This does not claim that arbitrary task deliverables could never contain assertions.

#### 5. System-claim versus route comparison

| claim | design/implementation support | observed-run support | causal support | bounded conclusion |
|---|---|---|---|---|
| CLM-1 | role separation, actual verification calls, memory write/read-back and frozen use are wired | no inspected run artifacts | none established | a reusable-experience learning architecture is supported; correctness/benefit of its generated knowledge remains uninspected |
| CLM-2 | paper reporting text names corpus and aggregation caveats | attributed aggregates only | unmatched selected runs and retained baseline entries do not identify component effects | reported aggregate gains are claimed; causal criticism-to-capacity inference is unsupported |
| CLM-3 | configured inference clients and external memory adaptation | no provider weight audit | not applicable | fixed weights are a design/report claim; provider parameter identity is uninspected |

#### 6. Bounded conclusion

The Verifier licenses a local task disposition; memory reconciliation then asks the Actor to reassess its retained account against that evidence. The Curriculum uses diagnosis and outcome history to select further experiments. This separates task success, explanation and next-experiment choice in the instructions and control flow. It does not mechanically certify each lesson or establish that its criticism produced improved capacity. Direct operational reuse and host admission are stronger evidenced facts than epistemic acceptance of individual learned claims.

## Reconciliation

The input, report and method hashes match the commissioned identities; the report is complete and independently source-read. The coordinator owns all final IDs. No prior target review entered either construction context. The following proposal mappings are the only retained uses of specialist-local IDs.

| specialist proposal | canonical ID | disposition |
|---|---|---|
| MEM-OBJ-1 | OBJ-6 | accepted with scoped evidence/uncertainty |
| MEM-OBJ-2 | OBJ-7 | accepted with scoped evidence/uncertainty |
| MEM-OBJ-3 | OBJ-8 | accepted with scoped evidence/uncertainty |
| MEM-OBJ-4 | OBJ-9 | accepted with scoped evidence/uncertainty |
| MEM-OBJ-5 | OBJ-10 | accepted with scoped evidence/uncertainty |
| MEM-RTE-1 | RTE-7 | accepted with scoped evidence/uncertainty |
| MEM-RTE-2 | RTE-8 | accepted with scoped evidence/uncertainty |
| MEM-RTE-3 | RTE-9 | accepted with scoped evidence/uncertainty |
| MEM-RTE-4 | RTE-10 | accepted with scoped evidence/uncertainty |
| MEM-RTE-5 | RTE-11 | accepted with scoped evidence/uncertainty |
| MEM-RTE-6 | RTE-12 | accepted with scoped evidence/uncertainty |
| MEM-BAP-1 | BAP-5 | accepted with scoped evidence/uncertainty |
| MEM-ABS-1 | ABS-1 | accepted with scoped evidence/uncertainty |

Material issue dispositions: preserve unknown payload/form/authority/curation unions; include target worklog learning while practice disables folding; distinguish optional bank rationale, explicit diagnosis rationale and worklog reasons; treat Curriculum read-only as canonical writeback policy; retain OSWorld memory-OFF versus ALE failure behavior; do not infer recall faithfulness or causal benefit from reported ablations. A requested follow-up corrected the initial omission of Verifier replay from trace-learning dependencies: RTE-12's transformed history is persisted by its next consumer, so the final report and profile include it. The follow-up also narrowed ABS-1 to exact searched code/text surfaces and documented its commands. These were substantive integration issues resolved by the specialist before integration, not coordinator-only classification changes.

Ownership remains separate: RTE-4 selects projects, RTE-6 sequences target outcomes, RTE-7/RTE-8 author and admit memory, RTE-9/RTE-10 deliver it. RTE-3's task verdict does not become a semantic grade on OBJ-6. RTE-11 and RTE-12 remain distinct because generative worklog synthesis and deterministic replay have different preservation limits. No canonical IDs were reassigned or split; no unsupported conflict was strengthened. Runtime and memory inspection separately identified role separation and the upload asymmetry; no stronger independent-convergence claim is needed.

## Bounded synthesis

RSIAgent implements an experience-to-memory-to-new-attempt route across separate Actor, Verifier and Curriculum contexts. Its distinctive contribution is not simply persistent files: completed execution is independently investigated, the same Actor is asked to reconcile the whole learned corpus, and Curriculum uses outcomes and diagnoses to choose further work. Phase 1 imposes ordered learning after a wave; Phase 2 can continue after an initial PASS; Phase 3 uses frozen host memory and keeps final external scores outside learning. These distinctions matter when assessing what a memory update was allowed to learn from.

The supported contribution is a wired architecture for revision and later reuse, with reported aggregate gains at the bundle level (CLM-2). Improved capacity attributable specifically to criticism of an operative formulated theory remains uninspected. Theory formulation, use, criticism and revision are afforded by the prompt-and-state routes; an actual theory instance and a controlled comparison are needed to establish conjectural learning. This finding does not confuse automatic trace-fed writing with demonstrated improvement.

Reflection conclusion status: wired at the operational level of outcome-responsive representations of Actor limitations guiding later practice and memory changes (RTE-4 and RTE-6 and specialist records). Whether it operates as a reflective theory builder that revises its theory-building organization is uninspected. Self-improvement mechanism conclusion status: wired; achieved improvement conclusion status: claimed at the reported aggregate comparison and uninspected for a causal attribution to the criticism process. Reflection, memory retention and improved capacity are separate findings.

For a bounded computer-use study, the design supports separating practice feedback from final scoring and retaining both success and failure lessons. It provides weaker evidence about the truth or causal reach of those lessons: memory authoring is model-owned and unconstrained in format, while the host checks boundaries and publication rather than lesson semantics. Remote effects, opaque provider identities, upload failure and differing verification paths further limit blanket guarantees. Candidate-linked memory snapshots, trajectories, verdicts and matched intervention comparisons would strengthen the assessment; a source change connecting official scores into learning would change the present boundary characterization.

## Limitations

| limitation | affected source, record, or route IDs | inspected boundary | conclusion prevented | evidence that would resolve it |
|---|---|---|---|---|
| no inspected runtime instances or executed probes | SRC-1, RTE-1, RTE-3, RTE-4, RTE-6 | implementation only | activation, actual criticism, improved capacity and reliability | pinned run trajectories, memory snapshots and intervention comparisons |
| reported aggregate confounding | SRC-2, CLM-2 | README/PAPER reporting notes | causal attribution to components or the criticism process | matched task/budget runs with candidate-linked provenance |
| provider internals excluded | CMP-2, CMP-3 | inference interface/model names | exact immutable weights or provider-side parameter changes | model/version attestation and provider evidence |
| external evaluator and VM internals excluded | CMP-4, RTE-3, RTE-5 | adapter/control boundaries | evaluator truth, deployed isolation or remote rollback | pinned dependencies, deployment inspection and targeted execution |
| unconstrained learned contents unavailable | SRC-1; integrated memory objects/routes | memory byte transport and prompts | complete aggregate payload form, truth and actual theory addressability | retained actual memory corpus and production history |
| lower-level hooks and alternate modes | RTE-1, RTE-2, RTE-3, RTE-5 | named entry paths and configurations | a single isolation or admission guarantee over all extensions | inspect deployed hook implementations and alternate grants |

## Verification and blockers

### Semantic verification

Checked all canonical identities, source boundary and evidence-layer distinctions. Every adopted memory object and route resolves in Shared records; report proposals map uniquely, and the profile uses exact canonical tokens. RTE-7, RTE-8, RTE-10, RTE-11 and RTE-12 were each checked against the trace-learning criterion, including task horizon, timing, retained form and later consumer. Their dependent profile fields preserve full-route coverage and explicit opaque payload uncertainty. RTE-9/RTE-10 distinguish requested file bodies from coarse inventory/outcome push; RTE-12's identifier signal selects an actual existing session, not a listed filename.

Checked that memory admission audits benchmark boundaries rather than semantic truth; task correctness, explanation, retained rationale and improved capacity remain separate. Prompted criticism is wired as a procedure, actual theory instances/criticism/improvement remain uninspected; reflection is scoped to outcome-responsive self-representation. No implementation or source-code test is upgraded to observed execution. Alternate legacy verification, isolation modes, callback executors, failed memory upload and external service limits restrict guarantees. Source quotations retain complete pinned attribution and are checked for occurrence by publication preparation; semantic support was reviewed on their attached records. No unresolved semantic or source-access blocker remains.

### Deterministic validation

The exact target is `kb/reports/state/agentic-system-analysis/AAS-2026-09-24-rsiagent-01/result.md`. Validation result: clean PASS under `commonplace-validate --full`; source quotation occurrence and publication identity are additionally checked by the guarded publication command.

### Blockers

None.
