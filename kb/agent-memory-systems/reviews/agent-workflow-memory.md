---
description: "Agent Workflow Memory review: workflow text distilled from web-agent trajectories, pushed into Mind2Web/WebArena prompts, with benchmark-specific induction loops"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# Agent Workflow Memory

Agent Workflow Memory, from Zhiruo Wang's `zorazrw/agent-workflow-memory` repository, is a research implementation for improving web agents by extracting reusable workflows from demonstrations or past agent trajectories. The checkout is not a general memory service, SDK, or persistent agent profile. It is two benchmark-specific pipelines: Mind2Web induces and injects workflow text plus exemplar actions; WebArena appends workflow files into a BrowserGym-style agent prompt and updates those files from successful or auto-evaluated trajectories.

**Repository:** https://github.com/zorazrw/agent-workflow-memory

**Reviewed commit:** [8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1](https://github.com/zorazrw/agent-workflow-memory/commit/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1)

**Last checked:** 2026-06-01

## Core Ideas

**Workflow memory is retained prose with embedded action traces.** The core retained artifact is a `.txt` workflow file, not a vector database or model checkpoint. Mind2Web reads `args.workflow_path` as the first memory exemplar and samples concrete examples from `data/memory/exemplars.json`; WebArena reads `flags.workflow_path` and appends the file contents to the system prompt before each action ([mind2web/memory.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/memory.py), [webarena/agents/legacy/agent.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/agents/legacy/agent.py)).

**Mind2Web has offline and online induction paths.** Offline induction groups training examples by domain, subdomain, and website, formats their action representations, asks an LLM to summarize common workflows, filters the generated text, and writes `workflow/{website}.txt` ([mind2web/offline_induction.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/offline_induction.py), [mind2web/utils/data.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/utils/data.py)). Online induction parses prior result JSON files into task trajectories, formats them like demonstrations, and overwrites the workflow file for later examples ([mind2web/online_induction.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/online_induction.py), [mind2web/pipeline.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/pipeline.py)).

**Mind2Web read-back is scoped before it is loaded.** `get_exemplars` always includes the workflow text if present, then filters concrete exemplars by website, subdomain, and domain when the metadata allows it, samples up to `retrieve_top_k`, and greedily drops examples when prompt tokens exceed the model limit ([mind2web/memory.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/memory.py)). A separate `workflow/retrieve.py` can build a FAISS index over workflow names and docstrings, retrieve top-k workflows for test queries, and write a selected workflow file, but the main Mind2Web pipeline does not call that utility directly ([mind2web/workflow/retrieve.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/workflow/retrieve.py)).

**WebArena uses a run-evaluate-induce loop.** `webarena/pipeline.py` iterates task ids for one website, runs `run.py` with that website's workflow file, runs model-based auto-evaluation, and then calls `induce_prompt.py` to update the workflow file from accumulated successful result directories ([webarena/pipeline.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/pipeline.py), [webarena/run.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/run.py), [webarena/README.md](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/README.md)). The pipeline is benchmark orchestration, not a reusable memory runtime.

**WebArena supports both manual-example and LLM-summary induction.** `induce_rule.py` parses BrowserGym logs, filters successful trajectories by ground-truth reward or auto-evaluator result, deduplicates by task template and abstract trajectory, optionally asks for manual acceptance, and writes concrete examples to a workflow file. `induce_prompt.py` uses the same trace parsing and filtering, then prompts an LLM to generate summary workflows with variable placeholders ([webarena/induce_rule.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_rule.py), [webarena/induce_prompt.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_prompt.py), [webarena/prompt/instruction.txt](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/prompt/instruction.txt)).

**The in-episode scratchpad is separate from workflow memory.** WebArena's inherited `Memory` prompt element can ask the agent to write `<memory>` for next steps, but `run.py` sets `use_memory=False`; the AWM path is the workflow file appended to the system prompt, while ordinary history, thoughts, actions, observations, and errors are transient prompt context ([webarena/agents/legacy/dynamic_prompting.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/agents/legacy/dynamic_prompting.py), [webarena/run.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/run.py)).

## Artifact analysis

- **Storage substrate:** `files` — Filesystem text files under `mind2web/workflow/` or `webarena/workflow/`, plus user-specified output paths such as `workflow/{website}.txt`
- **Representational form:** `mixed` — Prose workflow descriptions mixed with action snippets, placeholders, and in WebArena examples `<think>` / `<action>` blocks

**Workflow `.txt` files.** Storage substrate: filesystem text files under `mind2web/workflow/` or `webarena/workflow/`, plus user-specified output paths such as `workflow/{website}.txt`. Representational form: prose workflow descriptions mixed with action snippets, placeholders, and in WebArena examples `<think>` / `<action>` blocks. Lineage: imported seed files or LLM/manual distillates from training examples and successful result logs; online pipelines overwrite the active file rather than versioning individual updates. Behavioral authority: system-definition artifacts when loaded into the agent prompt as action guidance; knowledge artifacts when inspected as examples of solved web subtasks.

**Mind2Web concrete exemplars.** Storage substrate: `data/memory/exemplars.json`, loaded at inference. Representational form: structured JSON holding role/content messages with optional `specifier` metadata. Lineage: authored or preprocessed example demonstrations, not generated by the runtime pipeline in the inspected code. Behavioral authority: advisory system-definition context when sampled into the prompt; the `specifier` drives domain/subdomain/website filtering but there is no learned ranker in the main path.

**Induction scripts and prompts.** Storage substrate: Python scripts plus prompt text files under `mind2web/prompt/` and `webarena/prompt/`. Representational form: mixed symbolic control flow and prose instructions. Lineage: authored framework code. Behavioral authority: system-definition artifacts because they decide which traces are eligible, how examples are formatted, what the LLM is asked to extract, how output text is filtered, and where the retained workflow is written.

**WebArena result directories and auto-eval outputs.** Storage substrate: BrowserGym result directories under `webarena/results/`, including `experiment.log`, `summary_info.json`, screenshots, and `{model}_autoeval.json`. Representational form: mixed logs, screenshots, symbolic rewards, model-evaluator judgments, thoughts, actions, and task config references. Lineage: generated from agent rollouts, environment feedback, evaluator prompts, and task configs. Behavioral authority: knowledge artifacts as audit evidence; system-definition artifacts only when `induce_rule.py` or `induce_prompt.py` consumes them to update workflow memory.

**Mind2Web result JSON logs.** Storage substrate: JSON files under `results/{model}/{benchmark}/{website}/{suffix}/`. Representational form: mixed prompt/response records, predicted/target actions, token statistics, and metric arrays. Lineage: generated by `eval_sample` during inference from task examples, candidate scores, model responses, and metric calculations. Behavioral authority: knowledge artifacts as evaluation traces; system-definition artifacts on the online induction path because `online_induction.py` extracts their input/output steps into later workflow text.

**Optional FAISS workflow index.** Storage substrate: LangChain FAISS local index when `memory_path` is supplied by `mind2web/workflow/retrieve.py`. Representational form: distributed-parametric embeddings over workflow names and docstrings plus symbolic metadata ids. Lineage: derived from workflow text files and OpenAI embedding calls. Behavioral authority: ranking and selection system-definition artifact for producing a smaller workflow file, but the inspected benchmark pipelines do not make this the default read-back path.

The promotion path is trace -> selected successful or demonstrated trajectory -> workflow text -> prompt-injected procedure. It stays in readable prose/action form rather than becoming a validator, route table, or model checkpoint. The weak point is lineage governance: generated workflow files do not retain source trajectory ids, evaluator version, prompt version, acceptance status, or invalidation rules.

## Comparison with Our System

| Dimension | Agent Workflow Memory | Commonplace |
|---|---|---|
| Primary purpose | Improve web-agent benchmark performance with reusable task workflows | Maintain a typed methodology KB for future agents and maintainers |
| Canonical retained unit | Workflow text and concrete examples | Git-tracked markdown notes, instructions, indexes, reviews, schemas, and reports |
| Learning loop | Demonstration or rollout traces distilled into promptable workflows | Source-grounded writing, review, validation, and workshop-to-library promotion |
| Read-back | Website/task-scoped workflows pushed into action prompts | Pull through search/indexes/links, plus explicit instructions and generated context where configured |
| Governance | Success filtering, auto-eval/manual acceptance, prompt templates, token limits | Collection contracts, schemas, deterministic validation, semantic review, git history |

AWM is close to Commonplace in representational form: both systems deliberately keep important behavior-shaping material readable. The difference is artifact contract. Commonplace gives durable artifacts frontmatter, type specs, links, validation, review status, and git history. AWM's workflow text is easier to inject into a benchmark agent, but it carries little durable metadata about where a workflow came from or when it should stop applying.

The main design tradeoff is context efficiency versus reviewability. AWM compresses many traces into a short workflow file and pushes it into the agent's prompt, avoiding raw trajectory replay. But because workflows are free-form text and sometimes concrete traces, the agent still pays recurring prompt cost, and there is no deterministic check that a workflow remains valid for the current website state.

**Read-back:** `push` — Retained workflow memory is placed into the acting agent's prompt by the harness before action. The deployed Mind2Web/WebArena paths are instance-targeted by identifier signals: configured workflow paths, website-specific files, and Mind2Web domain/subdomain/website specifiers, with top-k and context-budget controls. The optional Mind2Web retriever can add embedding-based preprocessing over workflow names/docstrings, but it is not the central action-loop selector.

### Borrowable Ideas

**Treat successful traces as procedure candidates, not final memory.** A Commonplace analogue would keep review or validation run traces as evidence, then distill only repeated, useful procedures into an instruction or checklist. Ready for workshop artifacts; automatic promotion still needs review gates.

**Keep the memory artifact executable-looking but readable.** AWM workflows mix prose intent, placeholders, and concrete action syntax. Commonplace could use the same shape for operation recipes that are not worth codifying as scripts yet: readable enough for review, structured enough to execute. Ready for low-risk local procedures.

**Separate capture criteria from extraction style.** WebArena can choose trajectories by ground-truth reward or model auto-eval, then either preserve concrete examples or ask an LLM for summarized workflows. Commonplace should preserve this separation: first decide which evidence is eligible, then decide whether the promoted artifact is prose, symbolic, or mixed. Ready as a design rule.

**Use scope labels before semantic retrieval.** Mind2Web filters exemplars by website, subdomain, and domain before sampling. Commonplace already has path and type scoping, but generated context packets could make those scopes explicit before using expensive semantic retrieval. Ready where scope metadata exists.

**Retain induction prompts next to generated artifacts.** AWM's induction prompts are simple, but they make the compression policy inspectable. Commonplace-generated indexes, review summaries, or extracted procedures should keep the prompt or rule version that produced them. Needs a concrete metadata convention.

## Trace-derived learning placement

**Trace source.** Agent Workflow Memory qualifies as trace-derived learning. Mind2Web consumes annotated training examples for offline induction and prior inference result JSON for online induction. WebArena consumes BrowserGym experiment logs, task configs, summary rewards, auto-evaluator outputs, and screenshots through the evaluation path.

**Extraction.** Mind2Web extraction is LLM summarization over formatted task/action examples, followed by simple text filtering keyed to the website. WebArena extraction is either concrete-example selection with optional manual acceptance (`induce_rule.py`) or LLM workflow summarization over successful trajectories (`induce_prompt.py`). The oracle is benchmark reward, model-based auto-evaluation, manual acceptance, or ground-truth demonstrations depending on the path.

**Scope and timing.** Scope is benchmark and website oriented. Mind2Web offline induction is staged before inference; online induction alternates between running a chunk of examples and rewriting the workflow file. WebArena iterates run, evaluate, and update for website-specific task ids. The retained workflow is loaded in later task runs, not only in the episode that produced it.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), AWM belongs in the trace-to-prose-procedure family. It strengthens the survey's split between raw trace retention and distilled behavior-changing artifacts: logs and JSON results are evidence, while workflow files become the reusable action-shaping memory.

## Read-back placement

**Direction.** Agent Workflow Memory uses push from the acting agent's perspective. The agent does not ask for memory; the harness reads a retained workflow file or exemplar set and inserts it into the next prompt before generation.

**Targeting and signal.** Targeting is `instance` in the deployed benchmark loops. WebArena's signal is `identifier`: the pipeline chooses a website-specific `workflow/{website}.txt`, passes it as `workflow_path`, and the agent appends that file to the system prompt. Mind2Web also uses `identifier` signals: the configured `workflow_path` and exemplar `specifier` fields matching website, subdomain, and domain, followed by `retrieve_top_k` sampling. The optional Mind2Web retrieval utility adds an `inferred / embedding` preprocessing path over workflow names/docstrings, but it writes a selected workflow file ahead of the main loop rather than selecting inside each action call.

**Timing relative to action.** Read-back happens before action generation. Mind2Web inserts the selected demonstrations before each step's current observation query. WebArena appends the workflow file to the system prompt before the agent produces the next `<think>` and action.

**Selection, scope, and complexity.** AWM's strongest complexity control is scope: website-level workflow files, metadata-filtered exemplars, top-k exemplar sampling, and prompt-token checks that stop adding Mind2Web exemplars when the context would exceed the model limit. It does not verify whether the loaded workflow is the most relevant subroutine for the current page state.

**Authority at consumption.** Workflow memory is advisory prose/action context, but because it is injected into system or demonstration context for the action model, it functions as a soft system-definition artifact. The code does not enforce the workflow steps as a plan, validator, or state machine.

**Faithfulness.** The repository evaluates task success with and without memory configurations at the benchmark level, but I did not find a code-level faithfulness test that perturbs a specific workflow, checks whether the agent used it, or isolates context injection from other prompt changes.

**Other consumers.** Humans can inspect and edit workflow files, induction prompts, result logs, and auto-eval outputs. The same artifacts also serve as benchmark reports and induction inputs, so workflow memory doubles as both operational prompt material and research evidence.

## Curiosity Pass

**The name says memory, but the mechanism is promptable procedure distillation.** AWM does not try to remember arbitrary facts about users, environments, or episodes. It remembers reusable action subroutines.

**Workflow files are overwritten as active state.** Online induction writes to the same `workflow_path`; WebArena induction writes the website workflow file. That keeps the loop simple but loses per-update history unless the surrounding filesystem or git workflow preserves it.

**The most reusable component is not in the main loop.** `mind2web/workflow/retrieve.py` is the closest thing to a general retrieval layer, with FAISS over workflow descriptions, but the main benchmark pipelines mostly rely on scoped files and exemplar filtering.

**Concrete examples and abstract workflows blur together.** WebArena can write concrete successful trajectories or LLM-summarized workflows to the same kind of prompt file. That is convenient, but it makes authority and generality ambiguous: a concrete action id can be useful on a stable benchmark site and brittle elsewhere.

**The BrowserGym memory scratchpad is disabled in the AWM run path.** That helps keep the comparison clean: the memory being evaluated is the external workflow file, not the inherited in-episode `<memory>` mechanism.

## What to Watch

- Whether workflow files gain source metadata, evaluator version, prompt version, and accepted/rejected status; that would make trace-derived procedures auditable rather than just promptable.
- Whether semantic workflow retrieval becomes part of the online action loop instead of a preprocessing utility; that would move AWM from scoped push to stronger relevance-gated read-back.
- Whether workflow text is compiled into a symbolic state machine, action schema, or validator; that would reduce recurring prompt cost and make stale concrete ids easier to catch.
- Whether the induction loop preserves multiple candidate workflows with confidence or coverage estimates instead of overwriting one active file; that would make maintenance and rollback closer to Commonplace's artifact lifecycle.
- Whether benchmark auto-eval is calibrated against false positives; AWM's online learning quality depends directly on the oracle that decides which traces become memory.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - compares: AWM distills web-agent traces into reusable prose/action workflows rather than replaying full trajectories.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: AWM separates workflow files, exemplars, induction prompts, logs, evaluator outputs, and optional embeddings by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: AWM's workflow files matter because the harness actively pushes them into prompts.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: AWM extracts future behavior from past task traces after the task is over.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: AWM keeps result logs as evidence but loads distilled workflows instead of raw histories.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: workflow text becomes behavior-shaping instruction when inserted into the agent prompt.
