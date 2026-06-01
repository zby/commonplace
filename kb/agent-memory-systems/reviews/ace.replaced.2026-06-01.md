---
description: "Playbook-learning loop that turns benchmark attempts and reflections into prompt-injected bullets with counters, append-only curation, and optional duplicate merging"
type: ../types/agent-memory-system-review.md
status: outdated
tags: []
last-checked: "2026-05-16"
---

# ACE

> Replaced 2026-06-01. See [ace](./ace.md) for the current review.

ACE (Agentic Context Engineering) is a research framework from ace-agent for improving a task runner by evolving a sectioned playbook. A generator answers with the current playbook in prompt context, a reflector diagnoses the answer and tags used bullets as helpful or harmful, and a curator proposes JSON operations that update the playbook for later samples. The important implementation detail is narrower than the README framing: the ordinary operation path appends new bullets, while update/merge/delete remain mostly future hooks; optional bulletpoint analysis can merge similar bullets as a separate embedding-plus-LLM pass.

**Repository:** https://github.com/ace-agent/ace

**Reviewed commit:** [4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2](https://github.com/ace-agent/ace/commit/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2)

## Core Ideas

**The durable memory is the playbook, not the raw task trace.** ACE initializes a text playbook with fixed sections such as `STRATEGIES & INSIGHTS`, `FORMULAS & CALCULATIONS`, `COMMON MISTAKES TO AVOID`, and `OTHERS`; trained runs save `final_playbook.txt`, `best_playbook.txt`, and intermediate playbooks under the result directory. Raw attempts, pre/post answers, validation errors, LLM logs, and bullet usage logs are retained as run evidence, but the generator's future behavior changes through the playbook string injected into its prompt. See [`ace/ace.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/ace/ace.py) and [`logger.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/logger.py).

**Bullet IDs create addressable prompt memory.** Each playbook line has the format `[slug-00001] helpful=X harmful=Y :: content`. The generator prompt asks the model to return `bullet_ids` for relevant lines, and `Generator._extract_bullet_ids` parses those IDs from JSON or text. The reflector then receives only the referenced bullets and emits tags for them. This gives ACE a stronger artifact contract than one-blob cheatsheets: the retained prose is still a prompt document, but individual bullets are addressable enough for counters and targeted reflection. See [`ace/prompts/generator.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/ace/prompts/generator.py), [`ace/core/generator.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/ace/core/generator.py), and [`playbook_utils.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/playbook_utils.py).

**Helpful/harmful counters are symbolic feedback, not hard gates.** `update_bullet_counts` increments counters when the reflector tags a used bullet. `get_playbook_stats` summarizes total, high-performing, problematic, unused, and per-section counts; those stats are passed into the curator prompt. The code does not automatically demote, delete, or suppress harmful bullets. The counters influence future curation only through prompt context and optional human inspection. See [`ace/core/reflector.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/ace/core/reflector.py) and [`playbook_utils.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/playbook_utils.py).

**The implemented curator path is append-heavy.** The curator prompt asks for pure JSON with an `operations` list, but the available operation described to the model is `ADD`. `_extract_and_validate_operations` permits `UPDATE`, `MERGE`, `DELETE`, and `CREATE_META`, and the logger knows how to describe several operation types, but `apply_curator_operations` only applies `ADD`; the other branches are TODO comments. ACE therefore avoids whole-document rewrite, but the ordinary maintenance path still grows the playbook rather than editing it in place. See [`ace/core/curator.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/ace/core/curator.py), [`ace/prompts/curator.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/ace/prompts/curator.py), and [`playbook_utils.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/playbook_utils.py).

**Optional bulletpoint analysis is the real merge/refinement mechanism.** If enabled, `BulletpointAnalyzer` parses bullets, computes sentence-transformer embeddings, groups bullets above a similarity threshold, and asks an LLM to merge each group while preserving the first ID and summing helpful/harmful counts. This is not the curator's `MERGE` operation; it is a separate post-curation cleanup pass. That distinction matters because merge authority sits outside the main operation language. See [`ace/core/bulletpoint_analyzer.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/ace/core/bulletpoint_analyzer.py).

**Offline and online modes are benchmark loops.** Offline mode trains on train samples, periodically validates, and preserves the best validation playbook. Online mode tests a window with the current playbook, then trains on that same window before moving on. Finance and Mind2Web runners expose the same ACE class with task-specific processors and optional initial playbook loading. The learning signal is benchmark feedback and optionally ground truth, not open-ended project memory. See [`ace/ace.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/ace/ace.py), [`eval/finance/run.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/eval/finance/run.py), and [`eval/mind2web/run.py`](https://github.com/ace-agent/ace/blob/4f679bef3b78e973a0e13a0acc2b4a7f6f7e41a2/eval/mind2web/run.py).

## Comparison with Our System

ACE is one of the closest reviewed systems to commonplace's interest in retained symbolic artifacts that change later agent behavior. The difference is scope and authority. ACE optimizes one benchmark/task stream by injecting a single evolving playbook into every generator call. Commonplace accumulates cross-domain notes, instructions, reviews, and indexes whose activation depends on navigation and task framing.

| Dimension | ACE | Commonplace |
|---|---|---|
| Primary learned artifact | Sectioned playbook text with bullet IDs and counters | Typed markdown notes, instructions, indexes, and review artifacts |
| Trace source | Benchmark samples, generator responses, correctness feedback, reflections | Human/agent editing work, source inspection, review findings, workshop artifacts |
| Durable behavior-changing unit | Prompt-injected playbook bullet | File-level artifact plus frontmatter, links, and type contract |
| Raw trace role | Evidence/logs for a run; not directly injected later | Workshop/source evidence can remain inspectable and can be promoted |
| Update model | Counter update plus `ADD` operations; optional duplicate merge pass | Direct file edits, validation, semantic review, manual promotion |
| Authority | Playbook is injected with instruction force into generation | Mixed: notes advise, instructions constrain, validators enforce |
| Evaluation | Task/benchmark correctness, validation windows | Validation and review gates, weaker direct task oracle |
| Storage substrate | Result files under run directory; playbook is plain text | Git-tracked markdown KB |

**Where ACE is stronger.** It has a concrete closed loop with a real oracle: answers are checked, reflections are generated, counters are updated, and a playbook is re-used immediately. Bullet IDs are a useful middle ground between unstructured prompt memory and full KB files. The append-only curator is also safer than whole-document rewrite: a bad curator call can add noise, but it is less likely to erase the entire playbook.

**Where commonplace is stronger.** Commonplace has stronger artifact contracts. Notes have type specs, descriptions, status, authored links, and validation. ACE bullets have IDs and counters, but no source provenance per bullet, no status lifecycle, no supersession relation, and no independent validator for whether a bullet remains true. ACE also has no retrieval or progressive disclosure: the current playbook is the context surface, subject to prompt-level token-budget pressure.

**The closest design question is authority.** ACE's playbook looks like a knowledge artifact in storage - prose distilled from prior task attempts. At consumption time it acts as a system-definition artifact: the generator prompt tells the model to read the playbook, apply relevant strategies, avoid listed mistakes, and report bullet IDs. The same text therefore crosses an authority boundary when injected. Commonplace usually separates these surfaces more explicitly: a note can advise, while an instruction or validator carries stronger force.

**Read-back:** push — the current playbook is injected into every generator prompt before the model answers.

## Borrowable Ideas

**Stable bullet IDs inside a prompt artifact.** Ready to borrow for workshop-scale artifacts. A temporary playbook could use stable IDs for reflection, review comments, or score counters without promoting every item into a full note.

**Counters as weak evidence, not lifecycle state.** Ready as a caution. Helpful/harmful counts are cheap and useful, but they should not be mistaken for validation. In commonplace terms, they are review signals that might trigger promotion, repair, or retirement; they are not enough to set `status: current`.

**Append-first curation.** Ready for narrow automated capture. ACE's curator avoids destructive edits by only adding missing insights. That is a good default for trace-derived capture in a workshop layer, where preserving evidence matters more than elegance. A later human or validator can consolidate.

**Optional duplicate merge as a separate maintenance pass.** Useful but needs a use case. Keeping merge/refinement outside the primary write loop reduces risk, but ACE's version has no citation preservation or review gate. A commonplace analogue would need to preserve bullet lineage before merging.

**Benchmark-window online learning.** Needs a measurable task. ACE's online loop is attractive only when the task has a cheap correctness oracle. For ordinary KB writing, the oracle is too soft; for validation-warning repair or benchmarked agent procedures, it could fit.

## Trace-derived learning placement

**Trace source.** ACE consumes bounded task attempts: question/context/target samples, generator reasoning and answers, bullet IDs used by the generator, correctness feedback from a data processor, and reflector diagnoses. Offline mode separates train, validation, and optional test samples; online mode tests a window and then trains on that same window.

**Extraction.** The reflector converts an attempt plus feedback into diagnosis, a key insight, and bullet tags. The curator converts the latest reflection plus current playbook and stats into JSON `ADD` operations. The optional bulletpoint analyzer extracts similar-bullet groups with embeddings and asks an LLM to merge them. The oracle is benchmark correctness or ground truth when available; without ground truth, the reflector relies on environment feedback.

**Storage substrate.** Raw and intermediate state is stored as result-directory files: detailed LLM logs, `pre_train_post_train_results.json`, `train_results.json`, validation/test results, `bullet_usage_log.jsonl`, `curator_operations_diff.jsonl`, intermediate playbooks, `final_playbook.txt`, and `best_playbook.txt`. The distilled retained artifact is the playbook text. There is no database-backed memory store.

**Representational form.** The raw trace is mixed JSON/prose evidence. The operative distilled artifact is prose with a small symbolic wrapper: bullet IDs, helpful/harmful counters, and section headers. Optional merging uses embeddings transiently for similarity, but ACE does not retain embeddings or learned weights as memory.

**Lineage.** Run logs preserve enough material to inspect where a playbook came from, but lineage is not attached to individual bullets. A bullet records an ID and counters, not the sample, reflection, curator operation, or validation result that created it. The operation diff log records additions and some potential update/merge metadata for audit, but the playbook line itself is the source of truth once saved.

**Behavioral authority.** Raw attempts and reflections are knowledge artifacts: evidence and explanation for a run. The playbook becomes a system-definition artifact when injected into the generator prompt, because the prompt instructs the model to use it while answering and to cite used bullet IDs. Counters have weaker authority: they shape curator context and statistics but do not directly enforce generation behavior.

**Scope and timing.** ACE is per-task or per-benchmark, with optional reuse through `initial_playbook_path`. It supports offline adaptation from train/validation data and online staged adaptation over test windows. It is not a cross-project memory system.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), ACE is a trajectory-run artifact-learning system: repeated task attempts are distilled into symbolic prompt artifacts. It sits between Dynamic Cheatsheet and ExpeL. It is more structured than whole-document cheatsheet rewrite because bullets are addressable and counted, but less mature than systems with implemented edit/remove/supersession operations or per-item provenance. It strengthens the survey's claim that trace-derived artifact learning has a structure spectrum: single blob, addressable bullets, operation language, executable skills, and weights are different design points, not one technique.

## Curiosity Pass

**The README overstates deterministic maintenance.** The README says the curator converts lessons into structured delta updates with de-duplication and pruning. The code-grounded version is narrower: the curator asks for `ADD`, the operation applier only adds, and duplicate merging is optional through a separate analyzer. Pruning is at most prompt advice through token budget and stats.

**The unused `get_next_global_id` is a small but meaningful fault line.** `playbook_utils.get_next_global_id` can derive the next ID from an existing playbook, but `ACE.__init__` sets `self.next_global_id = 1` even when `initial_playbook` is supplied. If a user starts from a non-empty playbook, new bullets may collide unless another path resets the counter. That is exactly the kind of invariant an addressable memory artifact needs code to enforce.

**What property does ACE claim to produce?** A task-specific context artifact whose bullets increasingly capture strategies, formulas, mistakes, and heuristics that improve later answers.

**Does the mechanism transform data, or relocate it?** It transforms, but narrowly. Attempts and feedback become reflections; reflections become prose bullets; bullet tags become counters. The durable transformation is symbolic and prompt-facing, not database retrieval or model training.

**What is the simpler alternative?** Append every reflection's `key_insight` to a flat list and inject the list. ACE earns its complexity if bullet IDs and counters improve maintenance enough to beat that baseline. The source implements the machinery for that hypothesis, but the maintenance path is still mostly additive.

## What to Watch

- Whether `UPDATE`, `MERGE`, `DELETE`, and `CREATE_META` become real operations in `apply_curator_operations`, or remain prompt/logging vocabulary.
- Whether bullet IDs are initialized safely from an existing playbook when `initial_playbook_path` is used.
- Whether token-budget pressure becomes an enforced pruning policy rather than a number shown to the curator.
- Whether per-bullet lineage appears: source sample, reflector output, curator operation, and validation history.
- Whether optional duplicate merging proves useful without corrupting counters or losing provenance.
- Whether ACE expands beyond benchmark loops into project/session traces, where correctness oracles are weaker.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places ACE as addressable-bullet artifact learning between single-blob cheatsheets and richer operation/lifecycle systems
- [Dynamic Cheatsheet](./dynamic-cheatsheet.md) - contrasts: ACE uses bullet IDs, counters, and append operations instead of whole-document rewrite
- [ExpeL](./expel.md) - compares-with: both distill trajectories into rules, but ExpeL's operation vocabulary is richer than ACE's currently implemented appender
- [Autocontext](./autocontext.md) - compares-with: both use playbook-like artifacts, while Autocontext has broader multi-role gating and optional weight promotion
- [distillation](../../notes/definitions/distillation.md) - exemplifies: ACE compresses attempts and reflections into reusable prompt bullets
- [deploy-time learning](../../notes/deploy-time-learning-is-the-missing-middle.md) - exemplifies: ACE changes a prompt-time artifact during evaluation/training rather than training model weights
- [a functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - sharpens: ACE's playbook is closer to a workshop artifact that can later be consolidated than to a permanent library note
