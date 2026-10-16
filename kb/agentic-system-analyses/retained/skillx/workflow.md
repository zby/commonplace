---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "SkillX workflow account: the default offline functional-skill construction request, rejection handling, checkpointing and final delivery."
run-id: AAS-2026-10-14-skillx-61e3fc8f9aa5-01
reviewed-boundary: b0047c848dbbcf019363d6d56eef8c558f69aefc
---

# SkillX workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is `run_pipeline` with one epoch, functional skills, shortest-trajectory plan selection, default pre-merge filtering and no expansion. It is selected because it connects the repository's central experience-to-skill operation to an explicit saved deliverable without joining separate exploration and inference APIs into a fictitious autonomous cycle. Its canonical route is [RT-RTE-library-build](runtime.md#rt-rte-library-build). This is a source trace at the [frozen boundary](boundary.md), not evidence of a completed invocation. SRC-1 supplies implementation and prompt doctrine; no model call, execution fixture or performance experiment was run.

### Request, ownership and handoffs

1. **The caller requests construction.** `run_pipeline` receives an input trajectory path, output directory and model/benchmark configuration. It loads dictionaries, constructs the shared LLM and pipeline, awaits `run`, then saves results. The Python orchestrator owns progression; no model receives scheduling authority over these stages. The caller selects parameters but does not approve each generated skill. SRC-1, `pipeline.py`; [RT-RTE-library-build](runtime.md#rt-rte-library-build).
2. **Code selects evidence and prepares context.** The stored reward must exceed the default 0.999 threshold. That is a supplied outcome signal, not a newly checked reference answer. Long feedback is summarized before extraction, so the later extractor receives the substituted copy rather than necessarily verbatim observations. For each task, code chooses the shortest successful history for plan extraction. The summarizer and plan extractor get stage-specific inputs rather than an enclosing live-agent conversation. These context and reward mechanisms are established by [RT-RTE-library-build](runtime.md#rt-rte-library-build), with SRC-1, `pipeline.py`, `data/loaders.py`, `extraction/tool_summary.py`.
3. **A model proposes a plan; code admits it separately.** Returned task/plan pairs update the plan map and enter the planning library before functional skills are filtered. Code then assembles one skill-extraction item per task: task text, shortest successful history, plan, experience metadata and epoch. Consequently rejecting every skill does not retract a plan already added. SRC-1, `pipeline.py`; see the workflow annotation on [RT-RTE-library-build](runtime.md#rt-rte-library-build).
4. **The functional extractor delegates one plan step at a time.** Its fresh messages contain extraction methodology, task, selected history, the step and a skill list initially taken from experience metadata. This is not automatically the entire accumulating functional library. Parsed `add`/`modify` proposals append to the local list used for subsequent steps. The next step therefore can see earlier proposals before filtering has admitted them. It is model-to-model context reuse under code sequencing, not delegation to an independently executing task worker. SRC-1, `extraction/skill_extractor.py`; the annotation below retains the relevant passage.
5. **Filters judge candidates; clustering and merging transform survivors.** The enabled filter pipeline can reject candidates using general-quality and tool-schema model verdicts. These are not executable skill tests or independent answer oracles. Code clusters survivors through embeddings and asks a model to merge multi-member clusters; a failed merge returns the first cluster member instead. This is a loss-tolerant fallback, not a repair proven equivalent to the requested merge. The external generation and embedding dependencies are [RT-CMP-llm](runtime.md#rt-cmp-llm) and [RT-CMP-embedding-service](runtime.md#rt-cmp-embedding-service). SRC-1, `pipeline.py`; filter limits and bypasses are [RT-CLM-quality-control](runtime.md#rt-clm-quality-control).
6. **Code converts and admits the deliverable.** Candidate dictionaries require a name; missing document/content/tools fields receive defaults. Conversion exceptions cause individual entries to be skipped. `SkillLibrary.merge` applies insertion/replacement rules, rather than asking a human to authorize the final content. A same-name functional skill can replace the prior entry. This workflow admits instruction content; it does not install those skills as callable tool implementations. SRC-1, `pipeline.py`, `core/skill.py`; [RT-RTE-library-build](runtime.md#rt-rte-library-build).

### What verification can reject, and what survives rejection

The default filter judges pre-merge candidates, not necessarily the text ultimately saved. In addition to model merging, clustering preparation can truncate functional content at its first `return`. The transformation mutates the nested skill dictionary after the default filter has run. Thus even an affirmative filter verdict is not a check of identical final bytes. The quality annotation below supplies this additional SRC-1 implementation evidence. This does not show that truncation is harmful in a particular skill; it limits what the earlier verdict establishes.

A concrete rejection path is supported: when no candidate passes pre-merge filtering, `_run_epoch` returns early. The outer `run` still appends the epoch result and saves the current library checkpoint. Plans may already have entered that library; zero newly admitted functional skills does not mean no output or no retained change. Neither this branch nor the final aggregate counts supply a semantic success criterion. SRC-1, `pipeline.py`; [RT-RTE-library-build](runtime.md#rt-rte-library-build).

Recovery has several owners and scopes. The shared LLM retries provider/format failures; the extractor catches item exceptions and returns `None`; batches preserve item indices while allowing other work to finish; merger failure retains a first candidate; conversion failure skips an entry. These are partial-result policies, not all-or-nothing recovery. SRC-1, `llm/client.py`, `extraction/base.py`, `pipeline.py`; [RT-CMP-llm](runtime.md#rt-cmp-llm), [RT-RTE-library-build](runtime.md#rt-rte-library-build). No workflow-level automatic restore follows from saving checkpoints: `run` starts a fresh library and the caller must arrange reuse of an earlier file. Completion and availability of external calls remain unobserved.

### Delivery and the next boundary

At the construction boundary, delivery means returning the in-memory results after writing the final unified library, per-epoch statistics summaries and aggregate statistics. Each completed epoch also writes its library checkpoint. The final epoch-summary file contains statistics, not the full extraction return objects. SRC-1, `pipeline.py`:

> summary = {
>     "epoch": epoch_result.get("epoch"),
>     "statistics": epoch_result.get("statistics", {})
> }
> --- `pipeline.py`

This is a file/API completion condition, not a claim that the skills work. Saving is sequential, not a transactional commit or a tested deployment. Later loading and prompt preparation are a separate route, [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare), with [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) describing the advisory delivery channel. The benchmark wrappers do not execute tasks, and the supplied runtime identifies rewrite/selector interface mismatches. Accordingly this account ends at saved construction results rather than asserting end-to-end benchmark delivery or improved performance.

### Added source inspection

Beyond reading the supplied baseline, this member inspected SRC-1 implementation in `pipeline.py` (`run`, `_run_epoch`, task preparation, clustering/merging, checkpointing, final saving and convenience invocation), the functional `extract` and clustering-preparation bodies in `extraction/skill_extractor.py`, batch exception/concurrency handling in `extraction/base.py`, retry validation in `llm/client.py`, and admission replacement in `core/skill.py`. These reads add implementation evidence only. Expansion, alternative extraction modes and live inference are not the selected workflow; their existence is not evidence that this construction request invokes them.

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

#### On [RT-RTE-library-build](runtime.md#rt-rte-library-build)

Workflow-specific handoff: functional extraction uses a local proposal list across sequential steps; proposal visibility precedes final admission. This adds detail to the supplied route, not a separate route identity. SRC-1, `extraction/skill_extractor.py`:

> if isinstance(exp_metadata, dict):
>     skill_library = exp_metadata.get("skills", [])
> else:
>     skill_library = []
> --- `extraction/skill_extractor.py`

> if skills:
>     plan_step_metadata[step] = skills
>     # Update skill library for next iterations
>     for skill_item in skills:
>         if skill_item.get("option") in ["add", "modify"]:
>             if "skill" in skill_item:
>                 skill_library.append(skill_item["skill"])
>     break
> --- `extraction/skill_extractor.py`

Workflow-specific rejection/delivery distinction: pre-merge rejection terminates the epoch's skill work, not the outer workflow's checkpoint step. Plans admitted earlier can survive. SRC-1, `pipeline.py`:

> if not filtered:
>     logger.warning(f"[Epoch {epoch}] No skills passed pre-merge filtering")
>     return epoch_result
> --- `pipeline.py`

> results["epochs"].append(epoch_result)
>
> # Update plans if extracted
> if epoch_result.get("plans"):
>     all_plans.update(epoch_result["plans"])
>
> # Save epoch checkpoint
> self._save_checkpoint(skill_library, epoch)
> --- `pipeline.py`

#### On [RT-CLM-quality-control](runtime.md#rt-clm-quality-control)

Workflow-specific check coverage: when clustering runs after default pre-merge filtering, preparation may change functional content before merging and saving. The earlier verdict therefore need not cover the final text even before considering model merger output. This qualifies the same supplied quality-control claim, rather than asserting a second guarantee. SRC-1, `extraction/skill_extractor.py`:

> if item.get("skill_type") != "atomic" and "return" in skill.get("content", ""):
>     skill["content"] = skill["content"].split("return")[0].strip()
> --- `extraction/skill_extractor.py`

No execution evidence establishes the incidence or consequences of this transformation. Choosing post-merge filtering changes check placement, but does not turn model verdicts into executable correctness tests.
