---
description: "ACE review: trace-derived playbook evolution with generator-reflector-curator roles, coarse push read-back, and run-file lineage"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: outdated
last-checked: "2026-06-04"
tags: []
---

# ACE

> Replaced 2026-06-04. See [ACE](./ace.md) for the current review.

ACE, from `ace-agent/ace`, is a research framework for Agentic Context Engineering: it trains language-model agents by evolving a task-specific textual playbook. At the reviewed commit, the implementation runs generator, reflector, and curator LLM roles over benchmark samples; records reasoning traces, bullet usage, reflections, and results; and writes final, best, and intermediate playbooks as run artifacts. Its memory is not a general retrieval service. It is a learned prompt context that is pushed wholesale into later generator calls.

**Repository:** https://github.com/ace-agent/ace

**Reviewed commit:** [bcb7cea0504afad6f55fec4845dd4864c9f9eee7](https://github.com/ace-agent/ace/commit/bcb7cea0504afad6f55fec4845dd4864c9f9eee7)

**Last checked:** 2026-06-04

## Core Ideas

**The central retained artifact is an evolved playbook.** ACE initializes a standard sectioned playbook or accepts an `initial_playbook`, keeps the active playbook as a string during a run, and writes intermediate, final, and best playbook text files under a timestamped results directory ([`ace/ace.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace.py), [`README.md`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/README.md)). The playbook format is plain prose bullets with symbolic ids and helpful/harmful counters, such as `[str-00001] helpful=5 harmful=0 :: ...` ([`README.md`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/README.md), [`playbook_utils.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/playbook_utils.py)).

**Generator read-back is coarse push, not search.** `Generator.generate()` formats one prompt with the entire playbook, the current reflection, the task question, and task context; the generator is instructed to cite relevant bullet ids in its JSON output ([`ace/core/generator.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/generator.py), [`ace/prompts/generator.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/prompts/generator.py)). There is no vector search, metadata filter, or top-k selection over playbook items before generation. Context efficiency therefore comes from keeping the playbook compact enough to fit, not from retrieval-time narrowing.

**The reflector turns task feedback into learning signal.** For incorrect answers, ACE asks the reflector to analyze the generator's reasoning trace, predicted answer, ground truth when available, environment feedback, and the playbook bullets the generator claimed to use. For correct answers, the same path tags helpful bullets. Those tags update each bullet's helpful/harmful counters ([`ace/ace.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace.py), [`ace/core/reflector.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/reflector.py), [`ace/prompts/reflector.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/prompts/reflector.py), [`playbook_utils.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/playbook_utils.py)).

**The curator adds new lessons, but the main playbook mutator is narrower than the class comments imply.** `Curator.curate()` prompts for JSON operations, validates their shape, logs diffs, and applies them through `apply_curator_operations()` ([`ace/core/curator.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/curator.py), [`ace/prompts/curator.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/prompts/curator.py)). The implementation currently applies `ADD`; `UPDATE`, `MERGE`, `CREATE_META`, and `DELETE` are present as future-operation comments in the playbook utility, not as executed content rewrites ([`playbook_utils.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/playbook_utils.py)). The optional `BulletpointAnalyzer` separately uses sentence-transformer embeddings, FAISS similarity, and an LLM merge prompt to merge similar bullets when enabled ([`ace/core/bulletpoint_analyzer.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/core/bulletpoint_analyzer.py)).

**ACE's context-efficiency mechanism is grow-and-refine, not progressive disclosure.** The README frames ACE as avoiding brevity bias and context collapse through incremental delta updates guided by a token budget ([`README.md`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/README.md)). In code, `playbook_token_budget` is passed to the curator prompt and playbook stats are computed for the curator, but the generator still receives the whole current playbook each time ([`ace/ace.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace.py), [`ace/prompts/curator.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/prompts/curator.py)). This bounds expected volume by writing policy rather than by read-time selection, so complexity can still rise as the playbook accumulates many detailed bullets.

**The system keeps useful run lineage, but not review-grade provenance.** ACE writes `run_config.json`, `final_results.json`, initial/final/test result files, validation results, pre/post training answers, LLM call logs, bullet usage logs, curator operation diffs, intermediate playbooks, final playbook, and best playbook ([`ace/ace.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace.py), [`logger.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/logger.py)). That is enough to inspect a run's operational history. It does not attach durable source spans, acceptance reviews, expiration, or validity intervals to individual playbook bullets.

## Artifact analysis

- **Storage substrate:** `files` `in-memory` — The active playbook lives in memory during training/evaluation and is persisted as plain text under run result directories; logs and result JSON files are also file-backed.
- **Representational form:** `prose` `symbolic` `parametric` — Playbook lessons are prose; ids, section names, counters, JSON operation schemas, configs, result metrics, and bullet tags are symbolic; optional bulletpoint analysis uses embeddings and FAISS similarity during deduplication.
- **Lineage:** `authored` `trace-extracted` — Initial playbooks and prompts are authored, while refined bullets, counters, run logs, reflections, and best-playbook selection are derived from task trajectories and environment/ground-truth feedback.
- **Behavioral authority:** `knowledge` `instruction` `ranking` `learning` — Playbook bullets advise and instruct the generator, counters and validation accuracy influence curation/best-playbook selection, and traces/reflections feed the learning loop.

**Playbook bullets.** Storage substrate: in-memory string during a run, with intermediate/final/best text files written under the result folder. Representational form: prose bullet content plus symbolic ids, sections, helpful/harmful counters, and separator syntax. Lineage: authored when seeded through `initial_playbook`, trace-extracted when the curator adds lessons from reflections, and evolved when reflector tags update counters. Behavioral authority: knowledge and instruction for the generator because every generation prompt includes the current playbook.

**Generator, reflector, and curator prompts.** Storage substrate: repository Python modules. Representational form: prose instructions plus symbolic JSON response contracts. Lineage: authored framework code. Behavioral authority: instruction and learning policy, because they define what counts as a usable answer, what feedback the reflector extracts, and what operations the curator may propose ([`ace/prompts`](https://github.com/ace-agent/ace/tree/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/prompts)).

**Task trajectories and run logs.** Storage substrate: result JSON, JSONL logs, detailed LLM call logs, bullet usage logs, curator operation diffs, and error logs. Representational form: prose traces, symbolic metadata, ids, metrics, and timestamps. Lineage: trace-extracted from generator/reflector/curator calls and task evaluator outputs. Behavioral authority: mostly audit and learning input; the current code uses bullet usage and reflections for curation, while logs support later human/operator inspection.

**Validation and best-playbook artifacts.** Storage substrate: run files such as `initial_test_results.json`, `final_test_results.json`, `train_results.json`, `val_results.json`, and `best_playbook.txt`. Representational form: symbolic metrics plus prose playbook content. Lineage: derived from benchmark evaluation over train/validation/test samples. Behavioral authority: ranking and selection, because validation accuracy promotes a playbook snapshot to `best_playbook` for final testing.

**Optional bulletpoint analyzer.** Storage substrate: in-memory embeddings and reconstructed playbook text; no durable vector index is visible in the reviewed code. Representational form: parametric sentence embeddings, symbolic similarity groups, and prose LLM-merged bullets. Lineage: derived from current playbook content when `use_bulletpoint_analyzer` is enabled. Behavioral authority: deduplication and merge policy over retained playbook lessons.

**Promotion path.** ACE promotes task traces into reflection text, reflection text into new playbook bullets, bullet usage into helpful/harmful counters, and validation accuracy into a best-playbook snapshot. It does not promote lessons into externally reviewable instructions, tests, schemas, or validators; authority remains inside the next generator prompt.

## Comparison with Our System

| Dimension | ACE | Commonplace |
|---|---|---|
| Primary purpose | Improve benchmark/task performance by evolving prompt context | Maintain a git-native methodology KB for agents and operators |
| Canonical retained artifact | Task-specific playbook bullet with counters | Typed Markdown note, review, instruction, source snapshot, index, or report |
| Write path | Automatic trace-derived reflection and curator additions, plus optional authored seed playbook | Human/agent-authored artifacts, source snapshots, validation, semantic review, and deliberate replacement |
| Read-back | Pushes the whole playbook into generator prompts | Mostly explicit pull through search, links, indexes, skills, and loaded instructions |
| Context efficiency | Token-budgeted writing policy and optional dedup; no read-time retrieval selector | Collection routing, lexical search, curated/generated indexes, links, and scoped instructions |
| Governance | Benchmark accuracy, logs, counters, JSON parsing, optional dedup | Collection contracts, type specs, deterministic validation, semantic review gates, citations, archives |

ACE is close to Commonplace's concern with context as a behavior-shaping artifact, but it sits at a different authority level. ACE optimizes an agent's task playbook from repeated attempts. Commonplace maintains a library whose artifacts should stay inspectable, citeable, validatable, and reviewable across many later agents. ACE's strongest idea for us is not its exact generator-reflector-curator loop; it is the separation between trace capture, reflective diagnosis, and controlled update of a retained context.

The main divergence is read-back. ACE removes lookup failure by always injecting the whole playbook. That is useful for controlled benchmark loops, but it does not scale naturally to a large methodology KB where irrelevant context and stale advice are dangerous. Commonplace should not turn the whole library into a playbook. It can, however, use ACE-like reflections to create candidate updates after failed review or validation runs.

**Read-back:** `push` — The generator does not search for memory; ACE's orchestrator includes the entire retained playbook in each generator prompt.

**Read-back signal:** `coarse` — The read-back fires because generation is happening, not because a task instance matched a specific identifier, lexical query, embedding, or LLM relevance judgment.

**Faithfulness tested:** `no` — ACE evaluates initial and final/best playbooks and logs bullet ids used by the generator, but the reviewed code does not provide a with/without read-back ablation or causal test that isolated playbook injection.

### Borrowable Ideas

**Treat failed runs as candidate-update material.** Ready for review workflows. Commonplace could capture validation or semantic-review failures into a workshop note, ask for a reflector-style diagnosis, and propose candidate changes to notes, type specs, or instructions without applying them automatically.

**Keep the reflector separate from the curator.** Ready now as workflow vocabulary. ACE's split makes the diagnosis artifact distinct from the write operation. Commonplace already benefits from this separation in review gates; ACE reinforces that the updater should not be the same step that judged the failure.

**Use helpful/harmful counters only as weak salience.** Needs a specific consumer. Counters could help decide which instructions or review findings deserve attention, but they should not become authority by themselves. In Commonplace they would be advisory telemetry, not a replacement for validation or review.

**Borrow playbook snapshots for bounded workshops, not for the library.** Ready for temporary work. A workshop could maintain a short active playbook for a migration or review run, then promote durable conclusions into notes/instructions. The full Commonplace library should remain routed and typed rather than loaded wholesale.

**Do not borrow automatic ADD as library maintenance.** ACE's curator is intentionally additive and benchmark-driven. For Commonplace, automatic curation should produce candidates or drafts; durable library edits still need citations, type conformance, and review.

## Write-side placement

**Write agency:** `automatic` `manual` — ACE accepts a manually authored initial playbook, then automatically updates counters, adds new bullets, saves run artifacts, and selects best playbooks from task trajectories.

**Curation operations:** `evolve` `synthesize` `dedup` `promote` — Reflector tags evolve helpful/harmful counters on existing bullets; curator ADD operations synthesize new lessons; the optional analyzer deduplicates/merges similar bullets; validation accuracy promotes a snapshot to `best_playbook`.

### Trace-derived learning

**Trace source:** `trajectories` — Generator reasoning traces, predicted answers, bullet ids used, environment feedback, optional ground truth, reflection outputs, and evaluation results feed the learning loop.

**Learning scope:** `per-task` — The playbook is trained against a task/dataset configuration and saved under a task-named run folder; cross-task reuse is possible through `initial_playbook_path`, but not a distinct implemented routing layer.

**Learning timing:** `online` `offline` `staged` — ACE implements offline training over train/validation samples, online windowed train/test over test samples, and staged periodic curator/evaluation/save steps.

**Distilled form:** `prose` `symbolic` — Distilled lessons are prose bullets with symbolic ids, section placement, counters, and run metadata.

**Trace source.** ACE qualifies as trace-derived because the durable playbook changes in response to execution evidence. The core signal is not a user memory event stream; it is a task trajectory: prompt context, generator reasoning, final answer, correctness feedback, reflector diagnosis, bullet tags, and curator update.

**Extraction.** The extractor is LLM-mediated and evaluator-guided. The reflector diagnoses generator behavior and tags used bullets as helpful, harmful, or neutral. The curator reads the current playbook, recent reflection, playbook stats, question context, task progress, and token budget, then proposes JSON ADD operations. The oracle is the task evaluator and, when enabled, ground truth; there is no separate human acceptance gate in the reviewed code.

**Scope and timing.** Offline mode trains on train samples, periodically evaluates on validation samples, and optionally tests before and after training. Online mode first tests each window with the current playbook, then trains on the same window and carries the playbook into later windows. The batch variant parallelizes generator/reflector work over a snapshot and then runs synchronized curation ([`ace/ace_batch.py`](https://github.com/ace-agent/ace/blob/bcb7cea0504afad6f55fec4845dd4864c9f9eee7/ace/ace_batch.py)).

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), ACE belongs in the trace-to-playbook family: traces are distilled into prose/symbolic instructions that directly shape later model calls. It strengthens the survey distinction between trace preservation and behavior-shaping distillation. ACE does preserve logs, but the important learned artifact is the playbook, not the raw history.

## Curiosity Pass

**The README's "curator" sounds broader than the current mutator.** The core class and comments mention updating, merging, and deleting, but the reviewed `apply_curator_operations()` applies additions; other operation types are future-work comments unless the optional analyzer handles similarity merging.

**ACE is a context learner more than a memory store.** The durable state is a playbook meant to be read as prompt context. There is no database, retrieval API, MCP server, agent hook package, or user-facing memory management layer.

**The full-playbook push is both the feature and the risk.** It ensures that learned lessons are always available, but it also means context cost and interference rise with playbook growth. The design depends on curation quality.

**The best lineage is at the run level, not the bullet level.** Operators can inspect logs and result files, but a single bullet does not carry source task ids, source spans, model versions, acceptance status, or expiry.

**The optional analyzer introduces parametric machinery without making ACE a vector memory system.** Embeddings are used to find similar bullets for deduplication/merge, not to retrieve memories at generation time or persist a semantic index.

## What to Watch

- Whether `apply_curator_operations()` gains real UPDATE, MERGE, DELETE, pruning, or token-budget enforcement. That would move ACE from additive playbook growth toward stronger curation.
- Whether read-back changes from whole-playbook injection to task-instance retrieval or section selection. That would change ACE's activation class from coarse push to instance-targeted push.
- Whether playbook bullets start retaining source trajectory ids, prompt/model versions, confidence, or review status. That would make trace-derived lineage more audit-ready.
- Whether the planned tool-calling extension adds host hooks or runtime memory APIs. That would make ACE less like a benchmark trainer and more like an agent memory substrate.
- Whether the bulletpoint analyzer persists clusters or embeddings. Persistent parametric state would add a new retained artifact rather than a transient curation aid.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: ACE distills task trajectories into a behavior-shaping playbook.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: ACE has activation by construction because the playbook is pushed into every generator prompt.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: ACE uses task failures and reflections to update future behavior.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: ACE requires separating playbook bullets, prompts, run logs, validation results, and optional analyzer embeddings.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: playbook lessons advise the generator as remembered knowledge.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompts, JSON contracts, curation code, and evaluation selection configure later behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: ACE's core mechanism is engineering what context a future model invocation receives.
