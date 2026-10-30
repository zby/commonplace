---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Tortoise workflow: SDK session capture through staged extraction, gap-review recovery, graph admission and later framework context delivery."
run-id: AAS-2026-10-30-tortoise-0c919b4ca77d-01
reviewed-boundary: "54922a800f96858935b58ef250da569a4896df44"
---

# Tortoise workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a fresh SDK session capture using v2 extraction, followed by a later framework callback reading the graph. It was selected because it connects Tortoise's model-dependent memory formation to an explicit shipped consumer, rather than treating extraction's returned payload as delivery to an agent. The two invocations require a caller and a shared graph; this is not an automatic scheduler that starts the next agent task. The supplied baseline establishes these endpoints in [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) and [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

This account retains the [boundary](boundary.md#boundary-and-evidence)'s complete-artifact, partial-loop scope. All new source inspection is SRC-1 implementation evidence at the frozen revision, in `tortoise/extractor_v2.py`: S1/S2 orchestration, optional vet/classification call sites, S3 dispatch, S4 rendering and union, pre-S5 checks and result construction. These extend initial inspection without adding a source. No target code was executed and no successful run, host-model compliance or benefit is established. Optional gate internals and all alternative harness workflows are not traced here.

### Request, delegation and intermediate products

1. **Caller to SDK.** The caller supplies conversation turns and optionally a session identity. SDK code validates identity and stored-window content, writes Session/turn material, then chooses extraction. No provider can still produce a stored-session receipt without derived memories. Fresh keyed v2 capture is the selected path; replay, M2 and hosted policy are distinct branches, not steps joined into this workflow ([RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-hosted-capture](runtime.md#rt-rte-hosted-capture)). The caller requests capture, not human approval of each resulting proposition.
2. **Transcript to narrative.** `extract_session_v2` splits conversation material into chunks and calls `run_s1` separately. Each call receives chunk text, the master vocabulary and date context. Code collects successful chunk stories and compiles them; one failed chunk does not cancel the rest. Thus later stages may receive an incomplete account even though the function continues. This is a sequence of bounded model calls, not independently scheduled agents with their own action tools (SRC-1, `tortoise/extractor_v2.py`).
3. **Narrative to candidate list.** S2 receives the compiled story, master, date and source turns, and proposes a structured embed list. A partial parsed list is used but recorded as incomplete. Optional VET runs before classification, and optional classify-later assigns kinds before search. Their call sites catch failures or use a fail-open wrapper; their presence is not evidence of a universal rejection gate. S3 then calls `search_graph` with the current list and story. Backend eligibility and degraded search are bounded by the runtime's capture record; graph evidence is not guaranteed available on every backend (SRC-1, `tortoise/extractor_v2.py`; [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)).
4. **Candidates and priors to gap review.** S4 receives the story, rendered search results, current S2 list, date, output contract and available source-transcript block. Vocabulary/chains vary with classify-later mode. Code, not the model, decides whether to run it: a nonempty story is the local trigger even if S2 failed. Its default delta contract requests gaps and full-item corrections rather than re-emitting unchanged items. Code unions the result with S2. It preserves omitted S2 items and lets S4 win on identity-key collisions; this is not a truth check. The detailed handoff and recovery are [WF-RTE-gap-review](#wf-rte-gap-review) (SRC-1, `tortoise/extractor_v2.py`).
5. **Union to payload and store.** Optional post-union VET is a second gate because S4 can add material. Further classification/entity-resolution stages can intervene before deterministic chain enforcement and S5 payload construction. Chain-completeness findings are warnings, not a stop condition. An S5 exception yields a null payload plus diagnostics rather than an escaping exception at that call site. The SDK, not the extraction model, owns subsequent graph writes, provenance and bounded promotion/calibration. Payload construction is therefore not proof of durable graph admission; configured event stores also have separate failure outcomes (SRC-1, `tortoise/extractor_v2.py`; [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-OBJ-event-emission](runtime.md#rt-obj-event-emission)).

The per-chunk continuation mechanism is explicit:

> except Exception as e:  # per-chunk failure is non-fatal
>             failed_chunks += 1
>             errors.append(f"S1 chunk failed: {type(e).__name__}: {e}")
> --- `tortoise/extractor_v2.py`

The pre-S5 completeness check does not veto delivery:

> # where FIX P repairs them to statement). A pack chain whose first
>     # emitted step is missing its next step (ruleLifecycle: rule without
>     # rationale) is an incomplete chain — warn per the chain's manifest
>     # enforcement, never block. Notes are collected NOW and merged into
> --- `tortoise/extractor_v2.py`

### Verification, failure and recovery ownership

Verification here has several meanings that must stay separate. Parsing/shape checks control which model output is usable. Optional vetting can change the candidate list. Graph search supplies existing material to review, not an expected-answer oracle. Deterministic union preserves baseline candidates; chain checks can repair or warn. None establishes semantic correctness of every retained assertion. Human per-item approval is not inserted by the selected SDK route ([RT-RTE-session-capture](runtime.md#rt-rte-session-capture); SRC-1, `tortoise/extractor_v2.py`).

The inspected failure path is S4 throwing after S2 produced candidates: orchestrator code keeps S2, appends an error and continues. A malformed S4 section preserves S2 content for that section while usable sections can still merge. Empty delta is a normal no-change response. Partial accepted S4 output is merged but recorded as incomplete. Recovery is therefore code-owned continuation with diagnostics, not an independent reviewer demanding that the model fix every defect. Conversely, S4 can fill an empty S2 result when a story survives. Neither continuation nor rescue proves that omitted information was recovered ([WF-RTE-gap-review](#wf-rte-gap-review)).

The S5 exception branch separately records failure and constructs a diagnostic result:

> except Exception as e:  # S5 must NEVER block the pipeline (design §7.4)
>         errors.append(f"S5 failed: {type(e).__name__}: {e}")
> --- `tortoise/extractor_v2.py`

This is not a transaction-wide rollback. The SDK already stored source session material before extraction; capture retry is conditional and provenance/promotion are best effort. The caller must distinguish receipt counts/errors from a fully successful memory write. Same-session replay can also leave a nonfatal provenance gap unhealed ([RT-RTE-session-capture](runtime.md#rt-rte-session-capture)).

### Delivery and next-step ownership

The immediate delivered result is the SDK receipt: session identity, counts, extraction outcome and diagnostics. It is not an answer to the conversation's original task. A later framework callback supplies a bounded recent window to the reflex, which selects graph pointers under confidence, prior-mention and pointer-budget rules. The adapter takes the nondegraded block and appends/prepends it through its framework-specific channel. Retrieval trouble can result in silence so the host turn continues; that silence does not prove there was no relevant retained content ([RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)).

For this workflow, memory is delivered to agent work when the selected block reaches the upcoming host request. The host still owns the next model invocation and all task actions. The block's authority is interpretive context, not a hard execution constraint ([RT-BAP-framework-block](runtime.md#rt-bap-framework-block)). Receipt delivery, graph storage, block injection and changed agent behavior are distinct milestones; only wiring is established here.

Working-context isolation is similarly bounded. Extraction stages receive selected chunk/story/list/search inputs; S1's compiled story replaces the full chunk sequence as a narrative input to later stages, with source turns separately available to mapping/review. The framework reflex receives a filtered tail rather than the entire host history. Neither mechanism establishes host-wide compaction or a nested-agent return frame, and injection does not remove the host's original conversation (SRC-1, `tortoise/extractor_v2.py`; [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-gap-review
Label: S4 gap review and union recovery

Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

This is the internal S4 handoff and merge within v2 extraction, not another session-capture door. Owner/endpoints: `extract_session_v2` → `run_s4` / `render_s4_prompt` → extraction model via `_complete_parsed` → `merge_embed_lists` → downstream checks and S5. Its state is the current story, S2 list, graph-search result and merged list, all current-run data. Natural-language review instructions and source content travel in rendered text; JSON arrays, identity keys and section checks have symbolic consumers. SRC-1, `tortoise/extractor_v2.py`, supplies implementation evidence.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: parsed S4 candidate sections are unioned into `complete_list`; failure leaves the S2 baseline and an error, not a separate user-facing answer.
- Later read-back: inapplicable — this internal stage does not itself persist review inputs/results for a later invocation; eventual graph admission and later retrieval belong to the parent capture and context-delivery routes.
- Delegated visibility: model receives story, rendered graph priors, S2 list, date, output rules and available source-transcript block; core-only mode removes pack vocabulary/chains from this prompt.
- Selection predicate: story exists; default delta mode asks only for gaps/corrections; merge requires a dictionary with at least one content-bearing section. Optional downstream gates may further alter the union.
- Invalidation or expiry: review state lasts for this extraction; S4 omissions do not delete S2 candidates. Identity collisions replace the corresponding baseline item with the S4 item in the union.
- Activation or effect: code constructs the list passed to later checks and S5; the stage itself does not write the graph or establish downstream model use.
- Evidence limits: call, prompt rendering, merge and error continuation inspected; parser internals, vet adjudication, exhaustive S5 checks and exercised accuracy/recovery remain outside this focused trace.

The orchestrator proposes a review request; the model proposes gaps/corrections; code decides merge eligibility and identity precedence. No human per-content decision or expected-answer oracle is present in this handoff. Operating mode is open session processing, not a labelled-answer experiment. Guidance is the rendered story, search priors, vocabulary and output rules; the result is a candidate memory change, not a changed extraction model or method. The stage has no standalone durable admission or rollback mechanism. S4 failure falls back to S2; persistence and replay recovery are the parent route's responsibilities.

The actual supplied review context includes both proposed material and prior graph material:

> .replace("{story}", story)
>             .replace("{search_results}", _render_search_results(search))
>             .replace("{embed_list_json}", json.dumps(embed_list, indent=1))
> --- `tortoise/extractor_v2.py`

Code preserves the candidate baseline on collisions/omissions according to explicit merge rules, not model compliance alone:

> merged.append(s4_by_key.get(k, item))   # S4 wins on collision; S2 never dropped
> --- `tortoise/extractor_v2.py`

Failure continuation is explicit:

> except Exception as e:
>             errors.append(f"S4 failed: {type(e).__name__}: {e} — kept S2 output")
>             _bump_census(error_census, e)
> --- `tortoise/extractor_v2.py`

A null/empty delta and a partially parsed result have different treatment. Empty usable output is a normal no-change case; a partial parse is still used but recorded as incomplete:

> if stage_stats.get("partial"):
>             errors.append("S4 output partial — truncated tail dropped "
>                           "(embed list incomplete)")
>             _bump_census_class(error_census, "partial_parse")
> --- `tortoise/extractor_v2.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

none
