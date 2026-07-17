---
description: "Agent Workflow Memory review: web-agent workflow files induced from successful traces and pushed into WebArena/Mind2Web prompts"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# Agent Workflow Memory

Agent Workflow Memory, from `zorazrw/agent-workflow-memory`, is research code for WebArena and Mind2Web web-navigation agents that retain reusable workflows as text files. The repository induces workflow prose from training examples or prior agent trajectories, stores those workflows under benchmark-specific `workflow/` paths, and loads the selected workflow text into future prompts rather than exposing a general memory database or agent-callable retrieval API.

**Repository:** https://github.com/zorazrw/agent-workflow-memory

**Reviewed commit:** [8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1](https://github.com/zorazrw/agent-workflow-memory/commit/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1)

**Last checked:** 2026-06-04

## Core Ideas

**The central memory artifact is a workflow text file.** AWM stores reusable web-task routines as plain `.txt` files, such as the checked-in WebArena `workflow/{website}.txt` files and Mind2Web workflow outputs. WebArena's runner appends the chosen file directly to the system message when `workflow_path` is set, while Mind2Web reads `args.workflow_path` and converts its whole contents into an exemplar message before each sample ([webarena/run.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/run.py), [webarena/agents/legacy/agent.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/agents/legacy/agent.py), [mind2web/memory.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/memory.py), [webarena/workflow/](https://github.com/zorazrw/agent-workflow-memory/tree/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/workflow)).

**Workflow induction is trace-to-prose distillation.** The WebArena prompt-based induction path collects successful result directories by ground-truth reward or model auto-evaluation, parses `experiment.log` into think/action trajectories, deduplicates by task template and abstract action sequence, then asks an OpenAI chat model to summarize common subroutines into workflows. Mind2Web's offline path generates workflows from training examples; its online path reads previous result JSON files and induces a workflow file from the accumulated trajectories ([webarena/induce_prompt.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_prompt.py), [webarena/induce_rule.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_rule.py), [mind2web/offline_induction.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/offline_induction.py), [mind2web/online_induction.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/online_induction.py)).

**Context efficiency is coarse file selection plus token-fit truncation, not fine-grained retrieval.** The ordinary WebArena path loads the whole selected workflow file into the system prompt. Mind2Web loads the whole workflow file plus a random sample of concrete examples filtered by website, subdomain, or domain, and stops adding exemplars when the assembled prompt would exceed the model token limit. A separate `mind2web/workflow/retrieve.py` utility can build a FAISS index over workflow names/docstrings and write selected workflows to an output file, but that is an offline preparation utility rather than an agent-side lookup in the main inference loop ([mind2web/memory.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/memory.py), [mind2web/workflow/retrieve.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/workflow/retrieve.py), [mind2web/run_mind2web.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/run_mind2web.py)).

**The write oracle is benchmark success, auto-evaluation, or human inspection.** WebArena can select successful trajectories by `summary_info.json` cumulative reward or by `{model}_autoeval.json`; `induce_rule.py` then optionally asks the operator whether to add each candidate workflow unless `--auto` is passed. `induce_prompt.py` skips manual inspection and lets the model produce summary workflows from selected examples. Mind2Web uses ground-truth annotated training examples offline and prior model-result files online ([webarena/autoeval/evaluate_trajectory.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/autoeval/evaluate_trajectory.py), [webarena/autoeval/evaluator.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/autoeval/evaluator.py), [webarena/induce_rule.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_rule.py), [mind2web/offline_induction.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/offline_induction.py)).

**Adoption is script-and-file oriented.** The repository is not packaged as an installable memory service. Users run benchmark-specific scripts, pass workflow paths, and inspect or edit text files. This makes the memory easy to diff and patch, but weak on provenance, versioning, invalidation, and source-level review.

## Artifact analysis

- **Storage substrate:** `files` — Authored code, prompts, checked-in WebArena workflows, induced workflows, result logs, and optional Mind2Web FAISS index files all persist as repository or local filesystem artifacts.
- **Representational form:** `prose` `symbolic` `parametric` — Workflows, prompts, thoughts, and examples are prose; scripts, JSON result records, config files, action traces, and workflow parsers are symbolic; the optional FAISS/OpenAIEmbeddings path is parametric retrieval state.
- **Lineage:** `authored` `trace-extracted` — Prompt templates and seed workflow files are authored or checked in; WebArena and Mind2Web induction derive new workflow files from task examples, result JSON, experiment logs, success signals, and LLM summarization.
- **Behavioral authority:** `knowledge` `instruction` `ranking` `learning` `validation` — Workflow text serves as advisory/instructional prompt context for future actions; candidate scores and FAISS similarity can rank examples/workflows; induction learns from traces; reward and auto-evaluation validate which trajectories enter the write path.

**Workflow files.** Storage substrate: repository or local text files under `webarena/workflow/`, Mind2Web `workflow/`, or a user-provided `--workflow_path`. Representational form: prose subroutines mixed with concrete action snippets such as `click('id')`, `fill(...)`, and `select_option(...)`. Lineage: checked-in files are retained source material; newly generated files are trace-extracted summaries from successful or selected task trajectories. Behavioral authority: prompt-level knowledge and instruction because the acting model sees the workflow text before producing the next action.

**Induction scripts and prompts.** Storage substrate: Python scripts and prompt text in the repository. Representational form: symbolic parsers, filters, and subprocess pipelines plus prose induction instructions. Lineage: authored system-definition artifacts. Behavioral authority: learning and validation; they decide which traces qualify, how examples are formatted, what the LLM is asked to abstract, and where the new workflow file is written.

**Result and trajectory logs.** Storage substrate: WebArena `results/` directories and Mind2Web JSON logs under the configured result path. Representational form: symbolic JSON and log files containing observations, actions, model outputs, rewards, auto-evaluation records, and task metrics. Lineage: trace-extracted from benchmark runs. Behavioral authority: evidence for induction and evaluation, not the normal read-back surface.

**Concrete example memory.** Storage substrate: Mind2Web's `data/memory/exemplars.json` and runtime-loaded examples. Representational form: prose chat messages with symbolic specifier fields. Lineage: imported dataset examples rather than induced workflow summaries. Behavioral authority: knowledge context added beside workflow memory; examples are filtered by website/subdomain/domain and randomly sampled up to `retrieve_top_k`.

**Workflow retrieval utility.** Storage substrate: local FAISS output under `--memory_path` and selected workflow text written to `--output_path`. Representational form: parametric embeddings over workflow names/docstrings plus symbolic metadata ids. Lineage: derived index over existing workflow files. Behavioral authority: ranking and routing for preparing a smaller workflow file, but not an agent-internal read-back path in the main runner.

Promotion path: AWM promotes raw task traces into durable prose workflows, then promotes selected workflow files into prompt context for future tasks. It does not promote workflows into executable tools, validators, typed artifacts, or reviewed rules with source spans.

## Comparison with Our System

| Dimension | Agent Workflow Memory | Commonplace |
|---|---|---|
| Primary purpose | Improve web-navigation agents by reusing induced subroutines | Maintain a typed, source-grounded methodology KB for agents |
| Main retained artifact | Plain workflow `.txt` files and example messages | Typed Markdown notes, reviews, instructions, indexes, schemas, and source snapshots |
| Write path | Benchmark traces and examples distilled by scripts/LLMs into workflow text | Human/agent-authored artifacts governed by collection contracts, validation, and review |
| Read-back | Selected workflow file is pushed into the system or exemplar prompt | Mostly explicit pull through search, indexes, links, skills, plus loaded instructions |
| Governance | Benchmark reward, model auto-evaluation, manual inspection option, token-limit checks | Frontmatter/type validation, link checks, source citations, semantic review, git history |

AWM and Commonplace share the idea that trace evidence should be distilled before reuse. AWM's distillation target is deliberately lightweight: a text playbook that can be pasted into an acting prompt. Commonplace's target is usually a source-grounded artifact with type metadata, explicit lineage, and reviewable claims.

The tradeoff is speed versus auditability. AWM can update a workflow after every task or every small batch of Mind2Web examples, and its text files are easy to inspect. But an induced workflow has weak internal provenance: it does not cite the exact source trajectory steps, model prompt version, evaluation decision, or examples that justified each subroutine.

AWM is also much more push-oriented than Commonplace. Once a user or pipeline chooses `workflow_path`, the agent gets the memory as ambient prompt context. Commonplace usually requires an agent to navigate toward relevant notes unless an instruction or skill is already loaded.

### Borrowable Ideas

**Use benchmark success as a write-side gate for trace-extracted playbooks.** Ready for narrow workflows. Commonplace could allow a workshop to distill repeated validation-fix or review-triage traces only after a deterministic or reviewed success signal.

**Keep the distilled artifact as editable prose before codifying it.** Ready now. AWM's text workflows are easy to inspect and revise before they gain stronger authority. Commonplace should preserve that low-friction stage for operational playbooks before turning them into skills, validators, or commands.

**Separate raw traces from the prompt artifact.** Ready now. AWM does not replay whole logs into future tasks; it writes a smaller workflow file. Commonplace should keep raw run logs as evidence and serve a distilled note or checklist to later agents.

**Do not borrow coarse always-load read-back without scoping metadata.** Needs a stronger use case. Pushing a whole workflow file is simple, but it risks context dilution and stale instructions. Commonplace would need source links, scope, status, expiry, and a suppression path before pushing comparable memory automatically.

**Use retrieval utilities as preparation, not hidden agent authority.** Ready as a design rule. The Mind2Web FAISS utility is safer when it writes an inspectable selected workflow file; Commonplace should prefer reviewable prepared context over opaque runtime injection.

## Write side

**Write agency:** `automatic` `manual` — WebArena and Mind2Web scripts automatically derive workflow files from selected examples or prior trajectories; WebArena's rule path can require manual acceptance of candidate workflows; users can also edit the text files directly.

**Curation operations:** `consolidate` `dedup` `synthesize` — Induction consolidates multi-step trajectories into shorter common workflows, WebArena deduplicates candidates by task template and abstract action sequence, and the LLM prompt path synthesizes new prose subroutines across selected examples. The code does not implement contradiction invalidation, decay, or durable promotion tiers.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `trajectories` — The write path consumes WebArena experiment logs, action traces, result summaries, auto-evaluation records, Mind2Web result JSON, and annotated task trajectories.

**Learning scope:** `per-project` `cross-task` — Workflows are scoped to a website or benchmark split and reused across tasks on that site/domain rather than learned only for a single task.

**Learning timing:** `online` `offline` `staged` — Mind2Web supports offline induction from training data and online induction after batches of test examples; WebArena's pipeline stages run, evaluation, and workflow update steps.

**Distilled form:** `prose` `symbolic` — The retained output is prose workflow text with embedded symbolic action snippets and file/path conventions.

**Trace source.** WebArena's `pipeline.py` runs inference with a workflow file, evaluates the trajectory, then updates the workflow file from result directories. `induce_prompt.py` and `induce_rule.py` parse `experiment.log` into think/action trajectories and filter candidates by benchmark reward or model auto-evaluation. Mind2Web's online induction reads previous result JSON and reconstructs per-step environments and actions.

**Extraction.** Extraction is split between deterministic preprocessing and LLM abstraction. Deterministic code removes invalid action steps, groups by task template, optionally deduplicates by abstract trajectory, formats examples, and filters generated text by website header. The abstraction oracle is an OpenAI chat completion prompted to extract repeated workflows; the acceptance oracle is benchmark reward, model auto-evaluation, manual inspection, or annotated training data depending on the path.

**Scope and timing.** The retained memory normally lives at website granularity, e.g. `workflow/shopping.txt` or `workflow/aa.txt`. Online Mind2Web learning updates the file after previous batches; WebArena stages updates after evaluation. The workflow file can then be reused for later tasks, but the code does not maintain entry-level version history or invalidation metadata.

**Survey placement.** AWM is a trace-to-prose-workflow system. It strengthens the survey split between raw traces as evidence and distilled playbooks as behavior-shaping artifacts. It also shows the weak-governance corner of trace-learning: useful workflows can be generated cheaply, but without source spans or per-entry review their authority should remain prompt-level advice, not enforcement.

## Read-back

**Read-back:** `push` — The acting WebArena or Mind2Web agent does not choose memories by calling a retrieval tool; the runner or pipeline chooses a workflow path and pushes the selected workflow text into the system message or exemplar prompt before action generation.

**Read-back signal:** `coarse` `identifier` — The active path loads the whole selected workflow file; selection is usually by website/domain/task-family identifier supplied through `--workflow_path`, not by per-instance semantic matching. The separate Mind2Web FAISS utility affords embedding preselection, but that utility writes a file before inference rather than serving agent-side read-back.

**Faithfulness tested:** `no` — The repository reports benchmark evaluation paths and supports baseline/no-memory commands, but the inspected code does not implement a memory-specific faithfulness test showing that a particular pushed workflow changed the agent's downstream action.

**Direction edge cases.** From the operator's perspective, passing `--workflow_path` is an explicit pull from a file. From the acting agent's perspective, the workflow is pushed: it appears in the system message or demonstration context before the model acts. Static shipped README instructions and prompt templates do not count as memory read-back; only workflow files and example memories retained for later runs do.

**Targeting and signal.** WebArena relies on the caller to match the workflow path with the website task, and the README warns users to keep workflow files aligned with task ids. Mind2Web filters concrete examples by website, subdomain, or domain and loads the chosen workflow file. This is identifier-scoped coarse read-back: all selected workflow contents are included, and the code does not select the individual workflow most relevant to the current task inside the main inference path.

**Injection point.** WebArena appends workflow text to `sys_msg` before constructing chat messages. Mind2Web builds `exemplars` before the action loop and inserts those messages before the current query. Both are pre-invocation context assembly. After-task evaluation and induction are write-side maintenance, not read-back into the same action.

**Selection, scope, and complexity.** Selection is mostly file-level. Mind2Web adds at most `retrieve_top_k` concrete examples and checks token limits while extending the demonstration message list. WebArena uses large token limits in `ChatModelArgs`, but the workflow file itself is unbudgeted beyond the model prompt fitting around the main prompt. Effective context dilution is not verified from code.

**Authority at consumption.** The workflow text has soft instruction authority: it is prompt context describing reusable subroutines and action idioms. It does not become an executable action API, hard gate, or validator. Because it is inserted into high-priority system or demonstration context, stale workflows could still steer behavior strongly in practice.

**Faithfulness.** The repository distinguishes baseline and workflow-memory runs in README commands and benchmark pipelines, but I did not find a with/without ablation harness that isolates individual workflow injections or audits whether the agent followed a fired workflow. The mechanism is structurally implemented; behavioral effect is an empirical claim.

**Other consumers.** Human researchers consume workflow files, result directories, auto-evaluation Markdown/JSON logs, and generated outputs. The files are inspectable, but there is no structured review state, confidence field, expiry, or source pointer per workflow entry.

## Curiosity Pass

**The WebArena runner is marked deprecated but still central in the docs.** `webarena/run.py` begins with a deprecation warning, yet the root README and WebArena README use it as the way to run AWM on WebArena. The review treats it as implemented research code, not as a polished stable interface.

**There is less retrieval than the term memory suggests.** The main read-back path is file injection. The FAISS utility is real code, but it prepares an output workflow file rather than giving the agent a runtime memory lookup tool.

**The Mind2Web "retrieve_top_k" name is partly misleading.** In `memory.py`, it controls random sampling from filtered concrete examples, not semantic retrieval over the workflow text. Semantic workflow retrieval lives in the separate `workflow/retrieve.py` utility.

**The induced workflow format is easy to edit but hard to audit.** A workflow can contain useful abstracted procedure text, concrete ids, and action syntax, but there is no per-block citation back to the successful trajectory, no model/prompt version on the block, and no invalidation rule when the website changes.

**AWM stops before codification.** It keeps workflows as prompt prose and action examples. That is safer than silently generating executable browser tools, but weaker than a reviewed rule, validator, or typed skill when the same routine must be trusted across many runs.

## What to Watch

- Whether future AWM code attaches workflow blocks to source trajectory ids, success/evaluation records, model/prompt versions, and website versions; that would make trace-extracted workflows auditable.
- Whether the FAISS workflow retriever becomes part of the online inference path; that would change read-back from coarse file push toward instance-targeted inferred selection.
- Whether workflow files gain entry-level suppression, expiry, or invalidation when a website UI changes; without that, stale workflow push remains the main design risk.
- Whether AWM promotes common workflows into executable browser helpers or validators; that would move the retained artifact from prose advice toward symbolic system-definition authority.
- Whether evaluations include memory-specific ablations for workflow text, concrete examples, and online updates; that is needed to separate context presence from behavioral use.

Relevant Notes:

- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: AWM distills web-agent trajectories into reusable prose workflows.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: workflow files matter because the runners push them into future prompts.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: AWM bundles trace logs, workflow prose, retrieval indexes, prompts, and evaluation outputs under different forms and authorities.
- [Use trace extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - exemplifies: successful task traces are abstracted into future behavior guidance.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: workflow text and concrete examples mostly act as advisory context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - contrasts: AWM's workflow files influence behavior but are not enforced validators or executable tools.
