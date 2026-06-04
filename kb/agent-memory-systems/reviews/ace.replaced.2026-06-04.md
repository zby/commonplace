---
description: "ACE review: playbook-evolving agent loop that distills task attempts, reflections, and curation outputs into reusable prompt context"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-01"
---

# ACE

> Replaced 2026-06-04. See [ace](./ace.md) for the current review.

ACE, from the `ace-agent/ace` repository, is an agentic context-engineering framework that trains a task-specific playbook rather than model weights. The implementation runs a Generator over task samples with the current playbook, asks a Reflector to diagnose correct or incorrect attempts and tag used bullets, and periodically asks a Curator to add new playbook bullets. The result is a textual playbook that can be saved, selected by validation accuracy, and loaded into later evaluation or online adaptation runs.

**Repository:** https://github.com/ace-agent/ace

**Reviewed commit:** [bcb7cea0504afad6f55fec4845dd4864c9f9eee7](https://github.com/ace-agent/ace/commit/bcb7cea0504afad6f55fec4845dd4864c9f9eee7)

**Last checked:** 2026-06-01

## Core Ideas

**The retained memory is an evolving playbook, not a vector store or transcript database.** `ACE` initializes an empty sectioned playbook, optionally loads an initial playbook string, passes the whole playbook into every Generator prompt, and saves `final_playbook.txt`, `best_playbook.txt`, and intermediate playbooks under each run directory ([ace/ace.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace.py), [README.md](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/README.md)). The playbook format is deliberately simple: section headings plus lines like `[str-00001] helpful=5 harmful=0 :: advice`.

**The Generator consumes the playbook as always-loaded prompt context.** `GENERATOR_PROMPT` embeds the full playbook, current reflection, question, and task context, then asks the model to output reasoning, bullet ids used, and a final answer ([ace/prompts/generator.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/prompts/generator.py), [ace/core/generator.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/generator.py)). There is no retrieval index or pre-prompt selector in the main path; the context cost is bounded mainly by a configured playbook token budget and whatever curation keeps out.

**Reflection turns attempts into local learning signal.** For each sample, ACE generates an initial answer, checks it through the task `DataProcessor`, then invokes the Reflector with the model reasoning trace, predicted answer, ground truth when enabled, environment feedback, and the subset of playbook bullets the Generator cited ([ace/ace.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace.py), [ace/core/reflector.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/reflector.py), [ace/prompts/reflector.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/prompts/reflector.py)). The Reflector returns diagnostic prose and bullet tags, and `update_bullet_counts` increments helpful or harmful counters on cited bullets ([playbook_utils.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/playbook_utils.py)).

**Curation is delta-oriented but currently add-only in the applied path.** The Curator prompt asks for only missing new insights and returns JSON operations against the playbook ([ace/prompts/curator.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/prompts/curator.py), [ace/core/curator.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/curator.py)). The parser accepts names such as `UPDATE`, `MERGE`, `DELETE`, and `CREATE_META`, but `apply_curator_operations` only implements `ADD`; the other operation families are TODO comments in this commit ([playbook_utils.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/playbook_utils.py)).

**Optional deduplication is a second curation layer.** When enabled, `BulletpointAnalyzer` parses playbook bullets, embeds their text with a sentence-transformer model, finds high-similarity groups with FAISS-style cosine similarity, and either drops duplicates or asks an LLM to merge them while preserving combined helpful/harmful counts ([ace/core/bulletpoint_analyzer.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/bulletpoint_analyzer.py)). This is the strongest implemented response to playbook growth, but it is optional and runs after curator calls.

**Offline, online, and batched modes share the same playbook-learning contract.** Offline mode trains on train samples, periodically evaluates on validation samples, and keeps the best validation playbook. Online mode tests a window, trains on that same window, then moves on. `ACEBatch` parallelizes generator/reflector work over mini-batches, aggregates reflections and bullet tags, chunks curator calls, and can duplicate and shuffle reflections before curation ([ace/ace.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace.py), [ace/ace_batch.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace_batch.py), [eval/finance/run.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/eval/finance/run.py)).

## Artifact analysis

- **Storage substrate:** `in-memory` — An in-memory Python string during a run, with durable snapshots as `final_playbook.txt`, `best_playbook.txt`, and intermediate `*_playbook.txt` files under the configured results directory
- **Representational form:** `prose` `symbolic` — Free-text advice and diagnostics carried in sectioned playbook bullets, plus symbolic section headers, bullet ids, helpful/harmful counters, JSON operations, tags, metrics, and result records
- **Lineage:** `authored` `imported` `trace-extracted` — Authored framework prompts and processors, optional imported initial playbooks, and playbook bullets/counters derived from task attempts, reflections, curation, deduplication, and validation selection
- **Behavioral authority:** `knowledge` `instruction` `validation` `ranking` `learning` — Logs, reflections, and metrics serve as evidence; prompt templates and playbook bullets instruct Generator behavior; task processors and validation accuracy select outputs; counters and optional similarity analysis rank or maintain advice; curator operations mutate learned playbook state

**Playbook text and saved playbook files.** Storage substrate: an in-memory Python string during a run, with durable snapshots as `final_playbook.txt`, `best_playbook.txt`, and intermediate `*_playbook.txt` files under the configured results directory. Representational form: mixed prose plus symbolic structure: section headers, bullet ids, helpful/harmful counters, and free-text advice. Lineage: initialized from the default empty template or an imported `--initial_playbook_path`, then derived from task attempts, reflections, curator operations, optional deduplication, and validation selection. Behavioral authority: the playbook is a system-definition artifact when embedded in Generator prompts because it instructs future answers; it is also a knowledge artifact when inspected as accumulated task advice.

**Generator, Reflector, and Curator prompt templates.** Storage substrate: Python constants in `ace/prompts/`. Representational form: prose instructions with symbolic JSON output schemas. Lineage: authored framework code, not learned from traces. Behavioral authority: these are system-definition artifacts that define how attempts are made, how traces are interpreted, and which playbook mutations are admissible. The prompts give high authority to LLM outputs, but their effective quality is not verifiable from code alone.

**Reflection outputs and bullet tags.** Storage substrate: transient LLM responses during training, plus summaries in `bullet_usage_log.jsonl`, `pre_train_post_train_results.json`, and detailed LLM call logs when logging is enabled. Representational form: mixed prose diagnostics and symbolic tags. Lineage: derived from a task sample, Generator reasoning trace, predicted answer, environment feedback, optional ground truth, and cited playbook bullets. Behavioral authority: reflections are knowledge artifacts while used as evidence for curation; bullet tags become system-definition inputs because they update counters that later affect playbook statistics and curation context.

**Curator operations and operation logs.** Storage substrate: transient parsed JSON operations, with operation diffs logged to `curator_operations_diff.jsonl` when available. Representational form: symbolic operations plus prose reasons/content. Lineage: derived from recent reflection, question context, current playbook, playbook stats, token budget, and progress counters. Behavioral authority: curator operations are system-definition artifacts because accepted operations mutate the playbook that future Generator calls receive. In this commit, implemented promotion is mainly reflection insight to new playbook bullet; stronger edit/delete/merge promotion is named but not applied by `apply_curator_operations`.

**Evaluation and run result files.** Storage substrate: JSON files such as `run_config.json`, `train_results.json`, `val_results.json`, `initial_test_results.json`, `final_test_results.json`, `test_results.json`, and `final_results.json`. Representational form: symbolic metrics plus short prediction/error records. Lineage: derived from task processors, generated answers, ground truth comparisons, and run configuration. Behavioral authority: these are knowledge artifacts for audit and comparison, with one system-definition consequence in offline mode: validation accuracy chooses `best_playbook`.

**Optional bulletpoint analyzer state.** Storage substrate: transient embeddings and similarity groups in memory; merged bullets are written back into the playbook string. Representational form: distributed-parametric embeddings, symbolic similarity grouping, and prose merged bullets. Lineage: derived from current playbook bullet content, the configured embedding model, similarity threshold, and optional LLM merge call. Behavioral authority: the analyzer is a system-definition artifact on the maintenance path because it can suppress or rewrite retained advice before later prompt injection.

## Comparison with Our System

| Dimension | ACE | Commonplace |
|---|---|---|
| Primary purpose | Adapt task performance by evolving a prompt playbook | Maintain a typed methodology KB for future agents and maintainers |
| Raw evidence | Task samples, Generator outputs, correctness checks, reflections, usage logs | Source snapshots, notes, reviews, work artifacts, validation and review reports |
| Canonical retained unit | Sectioned playbook bullets with counters | Git-tracked markdown artifacts with frontmatter, type specs, links, and status |
| Learning loop | Trace-derived reflection and LLM curation during runs | Source-grounded writing, review, validation, and workshop-to-library promotion |
| Read-back | Always-loaded playbook in Generator prompt | Pull through search/indexes/links, plus explicit instructions and generated context where configured |
| Governance | JSON schema parsing, counters, validation accuracy, optional deduplication | Collection contracts, schemas, deterministic validation, semantic review, git history |

ACE is close to Commonplace in spirit because it treats context as the learned object. The important difference is authority and lifecycle. ACE gives a generated bullet direct future prompt authority once the Curator adds it. Commonplace usually requires an artifact to pass through a typed collection, source grounding, review, validation, and often a more explicit promotion boundary before it becomes durable instruction.

ACE also has a narrower context model. It does not browse a library, retrieve relevant notes, or assemble a bounded packet from indexed artifacts. It pushes the whole playbook into each Generator call and asks the Generator to report which bullets mattered after the fact. That makes the read-back path simple and robust for small-to-medium playbooks, but the main code path does not solve selective activation as playbook complexity grows.

The useful contrast is ACE's willingness to operationalize small learning cycles. A failed task attempt can become a reflection, a new bullet, a counter update, a validation-selected best playbook, and then instruction context for later attempts in the same run. Commonplace has stronger artifact governance, but less automatic conversion from local agent failures into candidate system-definition artifacts.

**Read-back:** `push` — The retained playbook is pushed by coarse always-load: every Generator call receives the whole playbook in prompt context. There is no instance-targeted signal or relevance-gated push activation in this commit

**Read-back signal:** `coarse` — Every Generator call receives the whole retained playbook; the review finds no instance-targeted selector or relevance-gated signal.

**Faithfulness tested:** `no` — ACE tracks validation accuracy and selected playbooks, but the review does not find a with/without read-back ablation proving the injected playbook changes behavior.

### Borrowable Ideas

**Treat local failures as candidate instruction deltas.** ACE's loop from wrong answer to reflection to curator operation would map well to Commonplace workshops: repeated validation or review failures could produce proposed rule bullets. Ready as a workshop report pattern; not ready for automatic promotion into instructions.

**Keep helpful/harmful counters on candidate advice.** ACE's counters are simple, inspectable, and cheap. A Commonplace analogue could track whether a proposed instruction helped, harmed, or was irrelevant across review cases before granting stronger authority. Needs a concrete evaluation harness first.

**Save intermediate context snapshots.** ACE writes intermediate, final, and best playbooks. Commonplace could use the same pattern for generated context packs or review bundles: keep the selected artifact, but retain enough snapshots to explain why it was selected. Ready for generated artifacts where snapshot volume is manageable.

**Use add-only curation before full rewrite.** ACE's implemented curator only adds new bullets, which avoids the context-collapse risk of repeated full rewrites. Commonplace should continue preferring localized edits and explicit replacements over wholesale regenerated methodology notes. Ready as a drafting principle.

**Run deduplication as a maintenance pass, not a hidden write path.** The optional analyzer separates growth from cleanup. Commonplace could borrow this for candidate link or note consolidation reports, but automatic merges should stay behind review until lineage and semantic checks are stronger.

## Write-side placement

**Write agency:** `automatic` — Generator attempts, Reflector diagnostics, Curator operations, counter updates, optional deduplication, and validation selection mutate or select saved playbook state during a run.

**Curation operations:** `dedup` `synthesize` `promote` — the Curator adds new playbook bullets from reflections, optional bulletpoint analysis drops or merges duplicate advice, and validation accuracy selects the best playbook snapshot.

### Trace-derived learning

**Trace source:** `session-logs` `trajectories` — Task-level Generator attempts, reasoning responses, correctness feedback, reflection rounds, and retained LLM/usage logs supply the learning signal.

**Learning scope:** `per-task` — The saved playbook is task-specific and benchmark/run-oriented rather than project- or corpus-global.

**Learning timing:** `online` `offline` `staged` — ACE supports offline training/validation selection, online windowed adaptation, and staged Generator -> Reflector -> Curator updates inside a run.

**Distilled form:** `prose` `symbolic` — The durable distilled artifact is a textual playbook with free-text advice plus section headings, bullet ids, counters, and curator operation structure.

**Trace source.** ACE qualifies as trace-derived learning. The qualifying traces are task-level Generator attempts: question/context, generated reasoning response, extracted final answer, bullet ids cited by the Generator, correctness feedback from a `DataProcessor`, optional ground truth, and subsequent reflection rounds. Detailed LLM call logs and usage logs are retained run artifacts when logging paths are enabled.

**Extraction.** Extraction is staged. The Generator first produces an answer and bullet-id usage signal from the current playbook. The Reflector then converts the attempt, feedback, and used bullets into diagnostic prose plus helpful/harmful/neutral tags. The Curator consumes recent reflection, current playbook, playbook stats, task context, token budget, and progress counters to emit JSON operations. `apply_curator_operations` assigns ids and inserts `ADD` operations into the playbook.

**Scope and timing.** Scope is task-run and benchmark-oriented. Offline mode learns from training samples and selects a best playbook through validation. Online mode learns in windows over the test stream. Batched mode learns from mini-batches by aggregating reflections before curation. Timing is staged inside a run rather than a persistent background service: the durable output is the saved playbook and result directory.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), ACE belongs in the trace-to-policy/playbook family. It strengthens the survey distinction between raw trace evidence and behavior-changing distilled artifacts: Generator attempts and reflections are evidence, while playbook bullets are the durable behavior-shaping object inserted into future prompts.

## Curiosity Pass

**"Context engineering" here means prompt-playbook evolution more than retrieval.** ACE improves the context object itself, but the main read path is unconditional full-playbook injection, not selective read-back.

**The implemented operation surface is narrower than the Curator class name suggests.** The Curator validates operation names beyond `ADD`, and logging has branches for merge/update/create-meta diffs, but the function that actually rewrites the playbook only applies additions.

**The Generator is asked to produce chain-of-thought-like reasoning.** The prompt requests detailed reasoning in JSON and logs full prompts/responses when logging is enabled. That may be useful for reflection research, but it also makes the trace substrate heavier and more privacy-sensitive than a final-answer-only evaluator.

**Ground truth can be disabled, but the strongest learning loop uses it.** `no_ground_truth` switches reflection prompts to environment-feedback-only mode, yet the finance and evaluation paths are built around task processors that compare predictions to known targets.

**The token budget is advisory.** The Curator prompt receives `playbook_token_budget` and playbook stats, but I did not find a deterministic enforcement step that trims the playbook to budget after curation.

## What to Watch

- Whether `UPDATE`, `MERGE`, `DELETE`, and `CREATE_META` become implemented playbook operations; that would turn ACE from add-only accumulation into a stronger governed context editor.
- Whether read-back gains a pre-generation selector over playbook bullets; that would change the review from always-load push to engineered relevance-gated push.
- Whether curator decisions retain stronger lineage, such as source sample ids, reflection ids, prompt/model versions, and accepted operation history attached to each bullet.
- Whether token-budget enforcement becomes deterministic rather than prompt-advisory.
- Whether benchmark claims move into reusable tests around the core loop rather than evaluation scripts and saved run outputs only.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: ACE turns task attempts and reflections into durable playbook bullets that future Generator calls receive.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: ACE requires separating playbook text, prompt templates, reflections, tags, curator operations, logs, metrics, and optional embeddings by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: traces, reflections, logs, and result JSON mostly serve as evidence or audit context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: prompt templates, curator operations, playbook bullets, and optional deduplication rules instruct or configure future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: ACE distills execution feedback into reusable playbook advice rather than storing raw transcripts as memory.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: ACE activates stored advice by always injecting the playbook, not by storing it alone or retrieving it on demand.
