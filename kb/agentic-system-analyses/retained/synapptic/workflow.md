---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Synapptic workflow: operator ingest from session transcripts through model extraction, profile merging, narrative synthesis and local publication, including rejection and delivery failures."
run-id: AAS-2026-10-15-synapptic-9dce97c66546-01
reviewed-boundary: bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f
---

# Synapptic workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is an operator's `synapptic ingest`, with the Claude Code output as the concrete delivery branch. It is selected because the shipped driver connects transcript selection, two kinds of model work, durable profile updates and publication in one invocation. It is not a coding-task completion workflow: Synapptic delegates bounded text transformations to inference services, while Python owns stage progression and file effects. The external coding assistant owns later instruction loading and coding work. The two supplied route records already describe this chain: [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile) and [RT-RTE-publish-archetypes](runtime.md#rt-rte-publish-archetypes). SRC-1, `src/synapptic/cli.py`.

Evidence is implementation at the boundary's frozen commit, not an observed execution. This lens directly inspected the ingest driver, extraction prompt/parser, synthesis prompt/filter, integration/discovery, narrative/observation state methods and Claude Code writer. These deepen the boundary's existing SRC-1 implementation coverage rather than add a source or an evidence layer. No target command, test or model provider was executed. The delivered-file path is wired, but end-to-end success is not demonstrated; an inspected return-shape mismatch prevents assuming normal CLI completion when destinations are updated.

### 1. Operator request becomes a session batch

The local user supplies the invocation, optional project restriction, model override, transcript budget, minimum line count and extraction limit. The driver discovers transcript paths and excludes session IDs represented by existing observation JSON filenames. It deduplicates and sorts remaining IDs by descending file size. A loaded queue does not determine this selection. Short transcripts and transcripts with no retained turns get empty observation files and are skipped. The extraction limit counts attempted nonempty extractions, not those skips. These are code decisions, not model task allocation. The selected session's path, project slug and session ID govern the next handoff. SRC-1, `src/synapptic/cli.py`, `src/synapptic/state.py`; [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile).

### 2. Extraction receives selected evidence, not the host's live context

Filtering and transcript conversion prepare a separate model request from retained user/assistant text, with prioritization under budget and transcript scrubbing. Tool results and thinking are not passed as equivalent evidence. The model gets the active extraction pattern, dimension descriptions, transcript text and, when the driver's global-profile condition holds, a compact existing-profile summary. That summary selects observations with weight at least 0.7 and caps each dimension at eight. A project-only profile does not activate this driver condition. The original transcript is not replaced, but this request supplies no evidence-reload tool. This is a bounded inference handoff, not a subordinate agent inheriting the coding assistant's environment. SRC-1, `src/synapptic/cli.py`, `src/synapptic/extract.py`; [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile).

The inference service proposes observation text and confidence under the pattern's guidance. Python parses an array, discards non-dicts, unknown dimensions and missing observation text, defaults confidence, and attaches session/time metadata. The caller adds project identity. These checks can reject malformed candidates; they do not decide whether the claimed observation is supported by transcript evidence. Starting ingest is not per-observation human approval. The configured model's tool restrictions and unpinned service identity are addressed in [RT-CMP-call-llm](runtime.md#rt-cmp-call-llm), and proposal guidance in [RT-OBJ-pattern-prompt](runtime.md#rt-obj-pattern-prompt). SRC-1, `src/synapptic/extract.py`, `src/synapptic/cli.py`.

### 3. Code admits observations and builds profiles

The driver routes accepted observations into global/project batches and persists the session observations. After extraction it clears the queue, merges global and project batches, saves the resulting profiles and promotes qualifying cross-project patterns. Models do not choose the next stage. Weighted merging uses the symbolic mechanisms described in [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile), rather than an independent reviewer checking the model's evidential claims. Observation files preserve the extraction return for later separate merge operations; profile files become the next stage's input and future extraction context. This crosses both an immediate handoff and a durable read-back boundary. SRC-1, `src/synapptic/cli.py`, `src/synapptic/state.py`.

### 4. Synthesis produces instruction prose without a reviewer gate

The driver reloads global and selected project profiles and invokes synthesis where dimensions exist. Synthesis filters profile entries before constructing a YAML reference-data prompt. Guards and AI-failure entries can qualify at weight 0.5; other dimensions also require the configured evidence count and weight. Exclusions remove entries, and an explicit synthesis target can apply model verdicts, although ordinary ingest supplies no target model. If no entries survive, synthesis returns no narrative. SRC-1, `src/synapptic/synthesize.py`, `src/synapptic/cli.py`; [RT-RTE-publish-archetypes](runtime.md#rt-rte-publish-archetypes).

The synthesis model is asked for a user archetype, imperative guards with failure-derived reasons, and known weaknesses. That request is not verification that the output satisfies those conditions. The inspected function accepts returned text after optional fence stripping, and the driver saves truthy results. There is no intervening human approval or model-review stage in this driver. The explicit return boundary is:

> return narrative.strip()
> --- `src/synapptic/synthesize.py`

No answer oracle is supplied for either extraction or synthesis. The benchmark route is separate, not a prerequisite or publication gate in ingest; its scores and model judgments must not be retroactively treated as verification of this invocation. See [RT-RTE-benchmark-feedback](runtime.md#rt-rte-benchmark-feedback). SRC-1, `src/synapptic/cli.py`, `src/synapptic/synthesize.py`.

### 5. Publication is a file effect, not host acceptance

Integration reloads saved global/project narratives, combines their text and selects configured output writers for discovered destinations. In the Claude Code branch, an existing memory directory receives `user_archetype.md`; an existing `MEMORY.md` gets or repositions its reference. The writer does not create a missing index. Other platform writers are alternatives, not additional mandatory stages of this workflow. SRC-1, `src/synapptic/integrate.py`, `src/synapptic/outputs.py`; [RT-BAP-archetype-host](runtime.md#rt-bap-archetype-host).

The publication handoff carries combined saved prose, not the original transcripts or a newly checked evidence bundle. Integration computes target-filter counts but does not remove corresponding prose from those saved narratives; [RT-CLM-target-filtering](runtime.md#rt-clm-target-filtering) qualifies the source's filtering claim. Local delivery means the writer has written the selected destination. It does not establish that a host later loads the file, obeys its imperatives or improves. Configured outputs without eligible destinations need not produce any write. SRC-1, `src/synapptic/integrate.py`, `src/synapptic/outputs.py`.

### Rejection, recovery and terminal-state limits

**Extraction failure can consume the retry opportunity.** The extraction function returns an empty list for an empty provider return, invalid JSON or a non-array. The ingest caller saves that list just like a successful extraction. Processed-session selection then relies on file existence, so ordinary ingest skips that ID next time. Explicit session extraction can retry, but an empty observation file carries no success distinction used by this selector. Provider-level retries do not repair this cross-stage policy. This failure path is already evidenced in [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile). SRC-1, `src/synapptic/extract.py`, `src/synapptic/cli.py`, `src/synapptic/state.py`.

**Rejected or failed synthesis does not revoke older delivery material.** If profile filtering leaves no entries or the provider returns nothing, the driver does not save a replacement narrative. It nevertheless proceeds to integration, which loads any existing narrative. Consequently a current profile and published prose can describe different stage versions. This is an inspected freshness gap, not proof that a real user's output was stale. The load/save and progression support it directly:

> if narrative:
>             save_archetype(narrative, project_slug=None)
> --- `src/synapptic/cli.py:1109-1110`

> global_archetype = load_archetype(project_slug=None) or ""
> --- `src/synapptic/integrate.py`

**Publication can precede an exceptional return.** Integration appends five-element tuples, while ingest expects three. At least one appended update therefore causes unpacking failure after integration has performed its writes. An empty result list avoids that particular failure, but also does not prove publication. This is a source-level defect, not an executed failure trace:

> updated.append((slug, "claude-code", memory_dir, target_model, excluded_count))
> --- `src/synapptic/integrate.py`

> for slug, target, path in updated:
> --- `src/synapptic/cli.py`

Thus neither reaching a stage message nor intending to print `Done.` is a sufficient delivery criterion. Existing profile history and explicit stage commands offer operator recovery, but there is no cross-stage rollback tying observation files, profiles, narratives and external outputs to one committed version. Per-file atomic writes do not make this workflow transactional; see the runtime's guarantee/recovery account. SRC-1, `src/synapptic/state.py`, `src/synapptic/cli.py`.

Finally, the installed SessionEnd route is not interchangeable with this selected workflow: it detaches extraction, merge and synthesis without calling integration, and its shell sequencing does not gate later commands on earlier success. It can maintain internal state without refreshing external delivery. That comparison is limited to the supplied [RT-RTE-session-hook](runtime.md#rt-rte-session-hook), not evidence of host hook execution. SRC-1, `src/synapptic/bundle/hooks/synapptic-session-end.sh`.

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

#### On [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile)

Workflow role: upstream half of the selected operator pipeline. The extraction handoff delegates proposal wording, not progression or file admission. Shape rejection returns to the driver as an empty list rather than a separately tracked failed job; downstream merge/publication can continue. Recovery responsibility remains with the operator and explicit CLI paths. No per-item reviewer or independent answer oracle intervenes.

#### On [RT-RTE-publish-archetypes](runtime.md#rt-rte-publish-archetypes)

Workflow role: downstream half of the same invocation. Narrative generation and local publication have different completion boundaries: a saved narrative is not yet a platform write, a platform write is not host activation, and a post-write CLI exception is not evidence that no delivery occurred. Empty synthesis preserves the possibility of publishing an older saved narrative. Benchmark feedback is not an acceptance gate on this path.
