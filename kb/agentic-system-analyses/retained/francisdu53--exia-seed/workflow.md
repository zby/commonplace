---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "EXIA SEED workflow: primary conversation capture, asynchronous model consolidation, fragment rejection and later memory delivery."
run-id: AAS-2026-11-07-exia-seed-804e805b7a8d-01
reviewed-boundary: c7497ac96da20bd1818096e35a59b6c0237f9730
---

# EXIA SEED workflow report

## Workflow account

### Selected workflow and evidence limit

The representative workflow is **retain a primary conversation, consolidate its closed batch into subject pages, and supply selected memory on a later request**. It is selected because the provider explicitly connects batch closure to the shipped consolidation CLI, whose page output is consumed by the provider's recall interface. This is one connected production path, not a composition of unrelated benchmark capabilities. It is a memory workflow within an external assistant, not a general multi-agent task planner. Its model delegation is a bounded request for structured content; code retains scheduling and write authority ([RT-RTE-conversation-ingest](runtime.md#rt-rte-conversation-ingest), [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation), [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery)).

Evidence is SRC-1 implementation at the reviewed commit, supplemented by the supplied runtime records. Inspection here covers `plugin/exia_seed/__init__.py` capture, launch and recall bodies, `plugin/exia_seed/outils/consolider.py` completely, and `plugin/exia_seed/consolidation.py` lock, source assembly, proposal admission and completion bodies. These deepen already included source coverage; they supply implementation, not observed execution. No run trace establishes successful model calls, actual retention, host context insertion or useful final answers. The enclosing Hermès runtime remains outside the [boundary](boundary.md#boundary-and-evidence).

### 1. Foreground turn to closed batch

Hermès supplies user and assistant text to `sync_turn`. The provider permits raw capture only in its active primary context. It delegates formatting and retention handling to the raw writer, including spoken-response substitution and secret masking. The writer retains source lines, not an approved final knowledge product. Day/volume closure or a session-end/reset hook makes a batch available to consolidation. Source admission is automatic under those rules; there is no ordinary per-turn human approval step. The user can invoke recognized omission/withdrawal instructions, whose effect is scoped to raw ingestion and future consolidation rather than a general erasure guarantee ([RT-RTE-conversation-ingest](runtime.md#rt-rte-conversation-ingest); SRC-1, `plugin/exia_seed/__init__.py`).

A closed batch triggers a host-context thread if automatic consolidation is enabled and no such thread is alive. That thread launches the same CLI used outside conversation. This handoff does not pass the foreground message history to another conversational agent: it starts a process that discovers pending files under the configured memory root. The primary assistant can continue while consolidation runs. An already active thread causes this launch attempt to return, not enqueue another task. Pending work therefore depends on a later launch opportunity ([RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation); SRC-1, `plugin/exia_seed/__init__.py`).

### 2. Process to model proposal

The CLI loads configuration, closes an older open batch (or today's batch with `--forcer`) and calls the consolidator. A nonblocking advisory file lock permits one cooperating consolidation writer; contention returns `deja_en_cours` rather than delegating a competing write. The consolidator selects pending closed batches against an estimated input budget and appends pending explicit notes. The first batch may exceed the budget. It supplies numbered source lines, existing node names/aliases, concept vocabulary and a system instruction to the auxiliary model. Speaker flags and source timestamps stay available to deterministic checking and metadata production. Full foreground tool history and full existing page bodies are not this proposal call's input ([RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation); SRC-1, `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/outils/consolider.py`).

The model proposes facts, node/section routing, citations and metadata. It does not receive an EXIA SEED action tool executor. Its configured endpoint is mutable, not an immutable model version ([RT-CMP-consolidation-model](runtime.md#rt-cmp-consolidation-model)). This request separates working contexts: the foreground session stays out, selected persisted source material goes in, and response text returns. It is not host-history compaction or proof of a fixed model context ceiling.

### 3. Verification to retained state

Code parses the response, including salvage of complete fragments where possible. Each fragment passes `_controler` before node resolution and page insertion. Software can veto defined citation, speaker and lexical failures; the proposal model cannot override that veto through a page-writing tool. There is no expected-answer oracle or required human reviewer. The gate establishes specified lexical support, not semantic entailment or user confirmation of every claim. Mixed valid/invalid citation lists and mixed agent/user citations explain why the stronger reading of citation verification is unwarranted ([RT-CLM-citation-control](runtime.md#rt-clm-citation-control)).

Accepted fragments are routed through aliases to subject pages; code derives utterance times and checks proposed event/deadline values against cited text. Unsupported dates can be stripped without rejecting the entire fact. Accepted page changes can trigger a further model pass for identity summaries, whose bounded excerpts do not guarantee coverage of every page fact. Pages, progress journals, index/log, used new concepts, graph, page hash chain and a best-effort Git commit are separate completion steps, not an atomic transaction ([RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation); SRC-1, `plugin/exia_seed/consolidation.py`).

### 4. Rejection and recovery branch

An unreadable response yields `echec_json` before progress journals advance; the selected inputs remain eligible for a later attempt. By contrast, a parseable response can reject individual fragments and still advance every selected batch and note. Such rejected content is not automatically reconsidered. Verification therefore filters the retained product but does not ensure every input is eventually represented. The code owns this distinction; the model is not asked to repair each rejected fragment within the same call ([RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation)).

Process-launch failure, nonzero exit and timeout are logged by the provider, without a retry loop in that method. A later automatic/manual/nightly invocation can revisit still-pending work. Timeout does not prove all inputs remain pending: it may interrupt after some writes or journal updates. Summary failure can leave old summaries; graph failure does not undo written pages; Git failure is not a page-admission rollback. These are partial-progress recovery policies, not successful recovery observations or all-or-nothing guarantees (SRC-1, `plugin/exia_seed/__init__.py`, `plugin/exia_seed/consolidation.py`; [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation)).

### 5. Delivery has two endpoints

The immediate product is retained page state and a consolidation report, not a foreground assistant answer. Normal CLI completion is quiet and returns zero; anomalous report statuses are printed. The provider treats nonempty stdout as an anomaly, so zero process exit alone does not mean every fragment was accepted (SRC-1, `plugin/exia_seed/outils/consolider.py`, `plugin/exia_seed/__init__.py`).

The later delivery endpoint is selected memory returned to Hermès. Recall reconstructs its cache when the graph edge file timestamp changes. In phase 2, a later primary query produces subject summaries and selected facts; `_souvenirs` returns the block to the host. In phase 1, automatic recall only computes/journals and returns empty. Explicit search/read remain alternate delivery paths in either phase. Consequently retained pages are not necessarily automatically supplied on the next turn, and a graph failure can delay visibility through an already loaded cache ([RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery)).

The host owns final placement and the next model decision. Returned conduct rules have model-interpreted force, not executable enforcement. Delivery is complete on EXIA SEED's side when the block or tool result is returned; successful answer delivery, compliance and benefit cannot be inferred from that return ([RT-BAP-recalled-content](runtime.md#rt-bap-recalled-content)).

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

#### On [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation)

Workflow handoff: the thread invokes a fresh process with no explicit foreground-history argument. This is process isolation for the consolidation call, not a delegated general agent session (SRC-1 implementation, `plugin/exia_seed/__init__.py`):

> r = subprocess.run([sys.executable, str(outil)], capture_output=True, text=True,
>                                timeout=self._reglages.get("consolidation_delai_s", 900))
> --- `plugin/exia_seed/__init__.py`

Workflow recovery: parse failure exits before progress advancement. A later invocation can retry those inputs, but no same-call repair round is scheduled (SRC-1 implementation, `plugin/exia_seed/consolidation.py`):

> return {"statut": "echec_json", "extrait": (reponse or "")[:300]}
> --- `plugin/exia_seed/consolidation.py`

The separate CLI completion signal is weaker than admission success; anomalous report statuses can still accompany a zero exit (SRC-1 implementation, `plugin/exia_seed/outils/consolider.py`):

> if a.verbeux or r.get("statut") not in ("ok", "rien", "vide", "deja_en_cours"):
>         print(json.dumps(r, ensure_ascii=False, indent=1))
>     return 0
> --- `plugin/exia_seed/outils/consolider.py`

#### On [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery)

Workflow completion: the phase-2 provider endpoint returns selected recall text to the host, while its exception path returns no memory. This supports local delivery/degradation, not the host's final answer or the docstring's timing claims (SRC-1 implementation, `plugin/exia_seed/__init__.py`):

> return s["bloc"]
> --- `plugin/exia_seed/__init__.py`
