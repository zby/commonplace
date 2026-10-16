---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "VLM-wiki workflow account: instructed image-to-wiki authoring and later query, contrasted with the implemented image-report driver's delivery and failure boundary."
run-id: AAS-2026-10-14-vlm-wiki-311faef777b4-01
reviewed-boundary: "503c43f98b5d1e21c74df384fdffd3e0652573b3"
---

# VLM-wiki workflow report

## Workflow account

The representative workflow is **user-requested image ingest, wiki authoring and subsequent question answering**. It was selected because it connects the system's model-dependent interpretation to its persistent knowledge product and intended later use. This multi-step procedure is source-supported as instructions, not as a repository-owned orchestration loop or an observed successful execution. The closest supplied records are [RT-RTE-agent-workflow](runtime.md#rt-rte-agent-workflow), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and [RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions). SRC-1: `AGENTS.md`.

### Request and responsibility handoffs

1. **Person to enclosing AI host.** Trigger keywords include `add image` and `vlmwiki`. On first use, the instructions ask the agent to check and create the raw/wiki directory structure, configuration, index and log. The person supplies the task and media; the external host supplies model execution and file tools. Loading these instructions, selecting an actual model and granting filesystem access are host responsibilities, not implemented guarantees of VLM-wiki. The advertised model fallback remains a declaration; see [RT-CMP-ide-model](runtime.md#rt-cmp-ide-model). SRC-1: `AGENTS.md`.
2. **Visual interpretation to article-writing decisions.** The instructed sequence reads the image with a VLM, extracts date/location/people/activities, generates a caption and saves raw material under a month directory. The model then chooses applicable category updates. Identification and significance are consequential decisions: an identified person or place changes which pages should be updated. These are task stages, not evidence of separate agents, isolated contexts or a structured inter-model payload. SRC-1: `AGENTS.md`.

> 1. **Read image**: Use VLM to analyze the image
> 2. **Extract metadata**: Date from filename/exif, location if available, people, activities
> 3. **Generate description**: Detailed caption of what's in the image
> 4. **Store raw**: Save to `raw/images/YYYY-MM/`
> --- `AGENTS.md`

3. **Interpretation to persistent wiki.** The requested handoff is article content plus media references, tags, related links and dates. The template includes raw-source links and related-article links. The model is asked to create moment/person/place pages as applicable and update patterns when discovered; the category-selection passage is retained in [RT-RTE-agent-workflow](runtime.md#rt-rte-agent-workflow). File-tool execution and actual writes remain external host behavior. Initiating ingest is not per-claim approval, and the inspected procedure/template supplies no separate content reviewer or expected-answer oracle. A prescribed format is not a verification gate. SRC-1: `AGENTS.md`, `references/article-template.md`.
4. **Retained wiki to a later answer.** A separate user question starts index-first retrieval and synthesis with internal citations. This is the intended downstream consumer, not an automatic continuation of the ingest request. The procedure depends on relevant articles being discoverable through the index; it does not establish that an ingest invocation updated navigation correctly. [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) retains the exact query instructions. A synthesis becomes an archive only on an additional user request, which explicitly asks for an archive file, index update and log append. SRC-1: `AGENTS.md`.

### Verification, recovery and what counts as delivery

For the host-mediated procedure, delivery means the requested knowledge artifacts have actually been written; later query delivery means an answer has been returned. The source prescribes those outputs but supplies neither an execution trace nor a host return protocol. The inspected image procedure, conventions and article template specify content/format but no executable acceptance test, semantic rejection stage, correction loop or transactional rollback. Recovery ownership therefore remains with the user/enclosing host, whose concrete capabilities are uninspected. This is a limit on the established workflow, not evidence that hosts cannot review or repair content. Raw immutability likewise remains a policy rather than an enforced file boundary; see [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability). SRC-1: `AGENTS.md`, `references/article-template.md`.

### Concrete failure check: the narrower image-report route

The implemented batch driver provides a checkable model handoff and failure path, but it must not be silently inserted into the instructed image-to-wiki chain. [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis) identifies this separate route: caller to Python, Python to Qwen with one base64 image and a fixed Chinese prompt, response back to Python, then Markdown and summary JSON to disk. The supplied runtime record retains its model identity and report-write passages. The provider does not receive the wiki or article-writing instructions. This inspection establishes no automatic consumer that compiles its returned reports into wiki pages. SRC-1: `scripts/qwen_vlm_analyzer.py`.

The batch CLI requires a key and `y` confirmation; those gates authorize starting calls, not accepting each response's factual content. The callable function has no CLI confirmation. Inside the batch loop, Python admits returned text directly, without a semantic validator. An exception during inference or report writing is caught per image, recorded as failure, and processing continues to the next image. Thus batch completion is not all-images success. SRC-1: `scripts/qwen_vlm_analyzer.py`.

> except Exception as e:
>     print(f"分析失败: {e}")
>     results.append({
>         "image": str(image_path),
>         "error": str(e),
>         "status": "failed"
>     })
> --- `scripts/qwen_vlm_analyzer.py`

The source implements continuation, not automatic retry or repair of that image. Summary writing occurs after the loop, outside its per-image handler, so that handler does not guarantee a summary survives a later write failure. A failure after opening a report can also leave partial output; no rollback is shown in this driver. Recovery beyond continuation requires caller action. For this narrower route, successful local delivery is report persistence plus summary/status return, not wiki admission, user review or downstream answer correctness. These are source-level paths, not observed failures or successful runs. SRC-1: `scripts/qwen_vlm_analyzer.py`.

### Evidence scope

This member inspected SRC-1 `AGENTS.md`, `references/article-template.md` and the complete `scripts/qwen_vlm_analyzer.py` at the registered commit. They supply doctrine/design and implementation respectively; this adds focused inspection, not a new source or evidence layer. No target code, host, provider or service was executed. The account can establish the requested workflow and the narrower driver's wired handoffs, but not compliant host execution, caption accuracy, successful later retrieval or user benefit.

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

#### On [RT-RTE-agent-workflow](runtime.md#rt-rte-agent-workflow)

Workflow selection: image ingest is the representative authoring branch. Its consequential handoffs are user media to visual interpretation, interpretation to category decisions, and category decisions to persistent articles. These are instructed responsibilities within a host-mediated task, not established subagent delegation. Verification and host-level recovery are not specified by the inspected procedure. Requested artifact creation is the delivery boundary; successful execution is unobserved.

#### On [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)

Workflow position: a later, separately triggered consumer of authored knowledge. Index discovery intervenes between persistence and answer synthesis, so written articles alone do not establish that their content reaches a later answer. Archive persistence requires an additional user request rather than following automatically from query delivery.

#### On [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis)

Failure-check scope: the per-image exception handler encloses both inference and Markdown writing but not the later summary write. The recovery action is recording failure and continuing; it neither repairs a partial report nor guarantees summary delivery. This implemented route is a contrast to, not proof of execution of, the instructed wiki-authoring chain.
