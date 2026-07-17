---
description: "ACE review: trace-learning playbook evolution, reflector-scored bullets, curator additions, optional deduplication, and coarse prompt read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-learning]
---

# ACE

ACE (`ace-agent/ace`) is an agentic context-engineering framework for improving task performance by evolving a retained playbook rather than fine-tuning model weights. At the reviewed commit, its core loop keeps a playbook string in memory during a run, feeds the whole playbook into generator prompts, uses execution feedback and reflector judgments to score used bullets, asks a curator model for additive playbook operations, optionally deduplicates similar bullets, and writes playbook snapshots plus run logs under timestamped result directories.

**Repository:** https://github.com/ace-agent/ace

**Reviewed commit:** [bcb7cea0504afad6f55fec4845dd4864c9f9eee7](https://github.com/ace-agent/ace/commit/bcb7cea0504afad6f55fec4845dd4864c9f9eee7)

**Last checked:** 2026-06-04

## Core Ideas

**The retained memory is an evolving playbook, not a retrieval store.** `ACE.__init__` initializes a plain-text playbook with fixed sections unless an initial playbook is provided; training mutates `self.playbook`, saves intermediate, final, and best playbook files, and evaluation-only mode can load a prior playbook path through task scripts ([ace/ace.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace.py), [eval/finance/run.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/eval/finance/run.py)). This makes ACE closer to Dynamic Cheatsheet-style prompt evolution than to a database-backed memory service.

**Generator, reflector, and curator separate use, judgment, and update.** The generator receives the current playbook, task question, context, and any reflection, then returns an answer and bullet ids it used. The reflector receives the reasoning trace, answer, feedback or ground truth, and the used bullets, then emits diagnostic text plus `helpful`, `harmful`, or `neutral` tags. The curator receives recent reflection, question context, playbook stats, token budget, and the current playbook, then emits JSON operations ([ace/core/generator.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/generator.py), [ace/core/reflector.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/reflector.py), [ace/core/curator.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/curator.py)).

**Automatic update is narrower than the high-level wording suggests.** The curator class docstring says it manages ADD, UPDATE, MERGE, and DELETE, and `_extract_and_validate_operations` accepts those operation names, but `apply_curator_operations` only implements `ADD`; update, merge, create-meta, and delete are marked as future TODOs in that function ([ace/core/curator.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/curator.py), [playbook_utils.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/playbook_utils.py)). Existing bullet evolution is therefore mostly counter updates, while semantic merging happens only through the optional `BulletpointAnalyzer`.

**Context efficiency is budgeted but coarse.** ACE has a `playbook_token_budget` config and passes the full current playbook to generator and curator prompts; the curator prompt sees current token budget and playbook stats, but the generator path does not retrieve top-k bullets before invocation ([ace/prompts/generator.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/prompts/generator.py), [ace/prompts/curator.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/prompts/curator.py)). Complexity grows with every retained bullet because all sections and counters are shown to the generator; the efficiency design is incremental delta growth and optional deduplication, not selective read-back.

**The optional bullet analyzer adds embedding-based deduplication as maintenance.** When enabled, `BulletpointAnalyzer` parses playbook lines, embeds bullet contents with a sentence-transformer model, groups bullets above a similarity threshold, and either keeps one or asks an LLM to merge a group while preserving the first id and combined helpful/harmful counts ([ace/core/bulletpoint_analyzer.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/bulletpoint_analyzer.py)). Those embeddings are transient; the retained result is a rewritten prose/symbolic playbook.

**The implementation records enough trace data for audit, but not a review gate.** Result directories include run configs, detailed LLM call logs, bullet usage JSONL, curator operation diffs, training/validation results, and playbook snapshots ([README.md](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/README.md), [logger.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/logger.py)). These artifacts preserve lineage for later inspection, but the code does not implement human review, provenance attachment per bullet, or rollback by semantic invalidation.

## Artifact analysis

- **Storage substrate:** `files` — During adaptation the operative playbook is an in-memory string on the `ACE` or `ACEBatch` instance, but retained state persists through optional initial playbook files and saved `intermediate_playbooks`, `final_playbook.txt`, and `best_playbook.txt` outputs.
- **Representational form:** `prose` `symbolic` `parametric` — Playbook bullets are prose advice with symbolic ids and helpful/harmful counters; optional deduplication uses transient parametric embeddings to decide which prose bullets to merge.
- **Lineage:** `authored` `trace-extracted` — Initial playbooks can be authored or supplied as files, while generated bullets and counters are derived from task traces, correctness feedback, reflector diagnoses, and curator decisions.
- **Behavioral authority:** `knowledge` `instruction` `ranking` `learning` — The playbook advises the generator as task knowledge, the prompt templates and run config instruct the loop, helpful/harmful counters and optional best-playbook selection affect salience, and task traces feed future learning.

**Playbook bullets.** Storage substrate: in-memory during a run and files when saved. Representational form: prose bullets with symbolic ids, section placement, and `helpful=X harmful=Y` counters. Lineage: initialized empty or imported from `initial_playbook_path`, then trace-extracted through reflection and curator additions. Behavioral authority: knowledge artifacts when read as strategies, mistakes, formulas, or examples; instruction-like authority in practice because the generator prompt tells the model to apply them.

**Prompt templates and task processors.** Storage substrate: repository Python modules and task scripts. Representational form: prose prompt instructions plus symbolic JSON formats, task config, and `DataProcessor` interfaces. Lineage: authored package code. Behavioral authority: instruction, validation, and routing authority because these files define how traces are interpreted, how answers are scored, which fields count as context/question/target, and which JSON fields models must emit.

**Reflection and bullet-usage traces.** Storage substrate: JSON/JSONL logs under result directories. Representational form: symbolic records containing sample ids, used bullet ids, answer correctness, context snippets, and reflection summaries. Lineage: trace-extracted from generator calls, evaluator results, and reflector outputs. Behavioral authority: mostly learning input; these traces are not read by the generator directly, but they drive counter updates, curator prompts, diagnostics, and possible future audit.

**Curator operations.** Storage substrate: transient model responses plus operation-diff logs. Representational form: symbolic JSON with prose reasoning/content. Lineage: trace-extracted from current playbook, recent reflection, task context, and playbook stats. Behavioral authority: learning and instruction authority over the retained playbook, but at this commit applied operations materially add bullets only; non-additive operations are accepted syntactically but not implemented by `apply_curator_operations`.

**Best-playbook snapshots.** Storage substrate: files under the run directory and the `self.best_playbook` in-memory field. Representational form: prose/symbolic playbook text plus validation metrics. Lineage: selected from the evolving playbook based on validation accuracy during offline training. Behavioral authority: ranking/salience authority, because final testing uses the best validation snapshot instead of necessarily using the last snapshot.

**Promotion path.** ACE promotes task experience into future behavior through a concrete chain: task sample -> generator reasoning and bullet ids -> evaluator correctness -> reflector diagnosis and bullet tags -> counter update and curator additions -> saved playbook -> later generator prompt. It can further promote a snapshot to `best_playbook` by validation accuracy. It does not promote individual bullets through a Commonplace-style review state, source citation, or validator.

## Comparison with Our System

ACE and Commonplace both treat context as a designed artifact rather than an incidental prompt. The major difference is authority and granularity. ACE learns a compact task playbook from rollouts and feeds that whole playbook back into future model calls. Commonplace maintains typed, human-readable library artifacts with collection contracts, validation, review history, and explicit linking, but it does not automatically learn new library artifacts from task trajectories.

ACE's strongest contribution is the raw-to-distilled loop. It does not merely store transcripts; it turns execution traces and feedback into future prompt material. Commonplace's closest analogue is a review or workshop workflow that turns source evidence into a durable note, but that transformation is deliberate and reviewed rather than automatic. ACE has better adaptation velocity; Commonplace has stronger auditability and semantic governance.

ACE's read-back is also simpler. The generator gets the entire current playbook, so lookup omission is reduced, but context dilution can grow with the playbook. Commonplace normally makes agents pull by `rg`, indexes, links, and skills, which keeps context smaller but depends on the agent choosing the right lookup. ACE shows why a bounded push path is tempting, while also showing why the pushed material needs a quality and freshness policy.

### Borrowable Ideas

**Reflector-scored retained advice.** A Commonplace analogue would let review runs mark retained guidance as helpful, harmful, or neutral in observed tasks, then surface that signal in indexes or review reports. This needs a concrete evaluation loop before implementation.

**Delta updates instead of full rewrites.** ACE's curator prompt asks for missing additions only. Commonplace could borrow this for workshop-to-note revision: ask for minimal claim additions or corrections rather than regenerating a whole note. Ready for constrained revision workflows.

**Trace logs as first-class lineage for learned artifacts.** ACE logs prompt, response, used bullets, correctness, and operation diffs. Commonplace could require any trace-derived note or instruction to link back to the run artifacts that caused it. Ready as a convention if trace-derived artifacts become common.

**Optional semantic dedup as maintenance, not source of truth.** ACE's bullet analyzer uses embeddings only to identify candidate redundancy, then rewrites retained prose. Commonplace could use embedding similarity to propose duplicate-note or duplicate-claim reviews while keeping authored Markdown as the retained authority. Needs a review gate before acting automatically.

**Validation-selected snapshots.** ACE's `best_playbook` selection is a simple but useful distinction between latest and best. Commonplace could use the same split for generated review outputs or benchmarked instructions: newest draft is not automatically the authoritative one. Needs measured tasks to avoid fake precision.

## Write side

**Write agency:** `manual` `automatic` — Users can seed the playbook from an authored file, but ACE's distinctive store changes are automatic: reflector tags update counters, curator operations add bullets, optional analyzer merges similar bullets, training saves snapshots, and offline validation selects `best_playbook`.

**Curation operations:** `evolve` `synthesize` `dedup` `promote` — Counter updates evolve existing bullets in place; curator ADD operations synthesize new bullets from reflections; optional analyzer deduplicates or merges similar bullets; validation accuracy can promote one snapshot to `best_playbook`.

### Trace-learning

**Trace source:** `trajectories` `session-logs` — ACE consumes per-sample task trajectories: generator responses, bullet ids, predicted answers, target comparison or environment feedback, reflector diagnoses, and logged LLM calls.

**Learning scope:** `per-project` `cross-task` — The learned playbook is task/run-scoped by default, but saved playbooks can be supplied to later runs and the framework is meant to be extended across task domains.

**Learning timing:** `online` `offline` `staged` — Offline mode trains on train samples and validates periodically; online mode tests each window with the current playbook and then trains on that window; saved playbooks create a staged handoff into later eval-only or adaptation runs.

**Distilled form:** `prose` `symbolic` — The durable learned output is a prose playbook with symbolic ids, sections, and helpful/harmful counters.

**Extraction.** For every training sample, ACE first generates with the current playbook, evaluates correctness through the task processor, and logs bullet usage. If the answer is wrong, it runs reflection rounds over the reasoning trace, predicted answer, ground truth or environment feedback, and the subset of bullets the generator cited; if the answer is right, it still reflects to tag helpful bullets ([ace/ace.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace.py), [playbook_utils.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/playbook_utils.py)). The oracle is task-specific correctness plus an LLM reflector; with `--no_ground_truth`, reflection uses environment feedback without the target.

**Distillation trigger and policy.** The curator runs at `curator_frequency` in the single-sample loop or once per curator chunk in batched training. Its prompt asks for missing insights only and the implementation applies ADD operations into matching sections with new ids. Existing bullet counters are updated from reflector tags, and the optional analyzer performs similarity-based deduplication after curation ([ace/ace.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace.py), [ace/ace_batch.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace_batch.py), [ace/core/bulletpoint_analyzer.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/bulletpoint_analyzer.py)).

**Survey placement.** ACE belongs in the strong trace-derived playbook family: it extracts lessons from task trajectories and turns them into future prompt material rather than merely indexing past conversations. It strengthens the survey distinction between raw trace retention and distilled behavior-shaping context. Its limitation is that distilled bullets have weak per-bullet provenance and no implemented invalidation path.

## Read-back

**Read-back:** `push` — Within ACE's own loop, the retained playbook is pushed into every generator call by prompt assembly; the generator does not first search or request memory.

**Read-back signal:** `coarse` — The full current playbook is always included for a generation call, keyed only by the run/task context rather than instance-level lexical, embedding, identifier, or judgment selection.

**Faithfulness tested:** `no` — ACE tracks validation/test accuracy before and after adaptation, but the reviewed code does not run a with/without-playbook read-back ablation or a per-bullet causal faithfulness gate.

**Targeting and signal.** The read-back path is coarse. `GENERATOR_PROMPT.format(playbook, reflection, question, context)` inserts the entire playbook for the current task run, and `evaluate_test_set` passes the supplied playbook to every test sample ([ace/core/generator.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/generator.py), [utils.py](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/utils.py)). The model may cite bullet ids in its output, but that is post-injection usage reporting, not pre-invocation selection.

**Selection, scope, and complexity.** Selection is all-or-nothing at playbook scope. `playbook_token_budget` and optional deduplication constrain growth indirectly, and curator prompts see playbook stats, but there is no implemented top-k retrieval or section filter for the generator path. Complexity therefore grows with the number and diversity of bullets, even when only a few are relevant to a given sample.

**Authority at consumption.** The generator prompt instructs the model to read the playbook carefully, apply relevant strategies, avoid listed mistakes, and include relevant bullet ids. That makes playbook read-back stronger than passive evidence but weaker than an enforced gate: ACE can measure whether answers improve, but it does not block answers that ignore the playbook or verify that a cited bullet was actually causally used.

**Faithfulness.** ACE measures whole-system task performance through initial/final testing, pre/post-train records, validation checkpoints, and best-playbook selection. That is useful evaluation, but it is not a read-back faithfulness test: helpful/harmful tags are reflector judgments over cited bullet ids, not ablations that remove the playbook or one bullet and measure behavior change.

**Other consumers.** Humans consume saved playbooks, run configs, LLM-call logs, bullet usage logs, curator operation diffs, and result JSON files for audit and debugging. Those are consumer surfaces, not additional read-back mechanisms for the generator unless a later run explicitly loads a saved playbook.

## Curiosity Pass

**The implemented curator is more conservative than the docstrings imply.** The code accepts names for update, merge, delete, and create-meta, but the playbook application function only implements ADD. This makes the system's real curation loop additive plus counter updates, with semantic merge delegated to the optional analyzer.

**The playbook can become a context-collapse risk in the opposite direction.** ACE is designed to avoid losing detail through repeated full rewrites, but always loading the full playbook can create context dilution as detail accumulates. The repository's solution is budget-aware curation and deduplication, not retrieval.

**Bullet counters are interpretable but underused as an access structure.** Helpful/harmful counts are visible to the generator and curator and included in stats, but they do not drive a deterministic selection policy before read-back. A future ACE variant could use them for ranking, pruning, or section-specific retrieval.

**Trace-derived does not mean provenance-rich.** ACE has run-level logs and operation diffs, but generated bullets do not carry source sample ids or confidence fields in the retained line format. That keeps the playbook compact but makes later audit and invalidation harder.

## What to Watch

- Whether `apply_curator_operations` implements UPDATE, MERGE, DELETE, or CREATE_META. That would move ACE from additive playbook growth toward stronger truth maintenance and consolidation.
- Whether the generator read-back path adds top-k retrieval, section filtering, or counter-based ranking. That would change ACE from coarse push to targeted push or mixed pull/push.
- Whether playbook bullets gain provenance fields linking them to samples, reflections, or operation logs. That would make trace-derived artifacts more reviewable and closer to Commonplace's evidence discipline.
- Whether the optional bullet analyzer becomes default or gains persisted embedding/index state. That would introduce a stronger parametric access layer rather than transient maintenance.
- Whether ACE measures per-bullet ablations, not only whole-playbook performance. That would make helpful/harmful counters more than reflector-labeled usage metadata.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: ACE activates retained playbook memory by pushing it into every generator prompt.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - applies: ACE turns task trajectories and feedback into future playbook behavior.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: ACE requires separating playbook text, logs, prompt contracts, curator operations, and best snapshots.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: playbook bullets advise future reasoning as retained knowledge.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompt templates, task processors, and curator machinery configure future behavior.
- [Lineage](../../notes/definitions/lineage.md) - frames: ACE's learned bullets need trace lineage to support audit, invalidation, and regeneration.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - frames: the same playbook line can be advice, prompt instruction, or learning input depending on the consumer path.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: ACE's core design question is how retained task context is assembled, bounded, and fed back into model calls.
